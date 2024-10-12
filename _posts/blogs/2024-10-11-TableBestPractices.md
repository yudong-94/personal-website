---
title: "Top 5 Principles for Building User-Friendly Data Tables"
date: 2024-10-11
categories:
  - blog
tags:
  - data science
  - analysis
  - data engineering
---

**Designing intuitive and reliable tables that your data team will love**

---

Working in data science and analytics for seven years, I have created and queried many tables. There are numerous times I wonder, "What does this column mean?" "Why are there two columns with the same name in table A and table B? Which one should I use?" "What is the granularity of this table?" etc. 

If you've faced the same frustration, this article is for you! 

In this article, I will share five principles that will help you create tables that your colleagues will appreciate. Please note that this is written from the perspective of a data scientist. Therefore, it will not cover the traditional database design best practices but focus on the strategies to make user-friendly tables. 

---

#### I. Single Source of Truth

Maintaining a single source of truth for each key data point or metric is very important for reporting and analysis. There should not be any repeated logic in multiple tables.  

For convenience, sometimes we compute the same metric in multiple tables. for example, the `Gross Merchandise Value (GMV)` calculation might exist in the customer table, monthly financial report table, merchant table, and so on. These columns are then referenced in more downstream tables with even more variations. Over time, they can diverge. Everything worked fine, until one day, a stakeholder came to us asking "Why is the monthly GMV in this dashboard different from the other? Is your data wrong?" When we dig into layers and layers of the data pipeline, we realized last quarter we agreed to only include cleared transactions in GMV, but forgot to make the change in every table… This hurts stakeholders' trust and we will end up spending more and more time investigating and maintaining the complex data model.  

So how to solve this? Maintain a single version of the GMV calculation in a dedicated table. Then every other table that needs the GMV metric should use this table, instead of creating their own calculation logic.  

**DON'Ts**:
* Keep multiple versions of the same calculation across different tables.

**DOs**:
* Maintain one version of each key metric. 
* Reference that source-of-truth table in downstream tables, rather than duplicating the logic everywhere. 

---

#### II. Consistent Granularity  

If a table is on the daily level, keep it daily. Mixing data with different granularities in a single table can lead to confusion and data integrity issues.  

This is my real example: I once created a table to report the `Operations Service Level Agreement (SLA)` performance - we had SLA defined for different Operations workflows and we wanted to track how often we could meet it. The SLA was defined at two levels: `touchpoint level` (each interaction) and `case level` (the entire process) - a case can have back-and-forth and be touched by multiple people on the Operations team. We want each touchpoint to be completed within a specific time limit and the whole case to be solved within a time range. I thought it was much easier to dump one table into BI tools for reporting, so I created a table mixing the two granularities. It had a column called `sla_level` with two values `touchpoint` and `case`. I was hoping people would  filter on a specific SLA level to get the metric they need.  

Why is this problematic? Not everyone had the context I just explained. They often did not include this filter in the reporting, and ended up double counting a case, as it would show up in both case level and touchpoint level. 

What should I have done instead? Create two tables, one on the touchpoint level, and another on the case level, explain their differences clearly in the table documentation, and only use the appropriate one for different use cases.  

**DON'Ts**:
* Mix rows or columns with different data granularities in the same table. This could lead to misuse of your data and incorrect analysis.

**DOs**:
* Only have one type of granularity in each table.

---

#### III. Descriptive Naming Conventions  

I have to admit that I have created temp tables called `txn_temp`, `tnx_temp_v2`, `tnx_subset_v3`, `txn_final`:) It's okay to have them in your exploratory code (as long as you can remember what they stand for when you look back…). But if you are going to share them with your colleagues or use them in an official data pipeline, you should give them more intuitive names. For example, the txn_subset_v3 should be something like refund_transactions, which clearly explains what is the subset and spells out transactions instead of txn.  

The same principle applies to the column names. This just happened to me yesterday - I was querying the monthly number of cases created, and I did `SELECT DATE_TRUNC('month', created_at) AS created_month, COUNT(DISTINCT case_id) FROM cases GROUP BY 1 ORDER BY 1`. Then I got 'created_at' does not exsits error… Taking a closer look, I realized the timestamp column was named created_date , though it was actually of the datetime type. What makes it worse is that similar columns could be `created_at` or `created_time` or `created_date` in different tables.  

Another example is that we sometimes add a column created by the `row_number()` window function to easily query the first or last occurrence of a partition in the table. I have seen multiple times that people just leave the column name as `rn`. emmm... Right Now? Real Numbers? Registered Nurse? Even if you know it stands for row_number, you will still need to look up the underlying SQL code to understand what is the partition and in what order. Therefore, if you do need to keep this column in the final table, please make it descriptive likerow_num_by_customer_order_date_asc. This is a much longer name, but in my opinion, longer names are better than short but confusing names.
It would also be helpful to have a consistent naming convention across tables. For example, all the tables on the customer level could be named with the customer_ prefix, so you have customer_demographics, customer_status, customer_signup_information, etc.  

**DON'Ts**:
* Tables called `xxx_temp`, `xxx_v1`, `xxx_final`.
* Unconventional/confusing abbreviations in table or column names.
* Tables on the same level and topic but named very differently (e.g. `customer_demographics` and `status_of_customer`).

**DOs**:
* Clear, descriptive, and intuitive table and column names - longer names are better than short but confusing names.
* Consistent naming conventions across tables.

---

#### IV. Appropriate Data Type and Format  

When it comes to intuitive tables, it's not just about descriptive table and column names, but also about appropriate data types and formats.
Let me give you some examples: 
1. Assume that we havecountry fields in different tables, such as the country where a customer is located, the merchant country of a transaction, the billing address country, etc. However, some of them are of the full country name (`United Stated`), some are in two-digit country code (`US`), and some are in lower cases (`us`). Then later, you are going to build a fraud detection model, and you want to create a feature to determine if the merchant country is the same as the customer's billing address country. Ideally, this can be done by a simple join, but in this case, you will have to check if all the country values in the two columns are consistent. As a result, you will need to clean up a bunch of values and find some country names to two-digit country code mapping to join the two tables. This is a very error-prone process.
2. We all love binary columns - they are very handy when we need to filter on some common segments. However, I've seen them both in `TRUE/FALSE` and `1/0` formats here and there. What's worse? Sometimes the `1/0` is of integer type, but sometimes in string… It is clearly much better to keep them all consistent in the TRUE/FALSE format.
3. For all the monetary value fields like `transaction_mount`, `delivery_fee`, or `product_price`, they should be in a consistent unit as well. If some of them are in dollars, while some are in cents, you can easily calculate profits that are 100x or claim a profitable deal to be unprofitable.

**DON'Ts**:
* Have different data types or formats for columns that are similar.

**DOs**:
* Use appropriate data types. For example, always use `TRUE/FALSE` boolean values for the binary columns; `xx_time` columns are always in the datatime format, while the `xx_date` columns should be in date format.
* Keep consistent formats. For example, all the `country` fields are in two-digit country codes, and all the money-related fields are in dollars. 

---

#### V. Complete Documentation 

Last but not least, a good table always comes with a complete table documentation. A good documentation ensures that everyone using the table will understand what it's for and use it appropriately.  

What makes a "complete table documentation" though is a separate topic that might be worth its own article. But here are the key components in my opinion:  
1. **Table description**: What is the purpose and data topic of this table? When should people use this table? What is the granularity of the table? Any caveats that users should keep in mind?
2. **Column documentation**: The data type and meaning of each column. If a column has a complex calculation logic, it is also important to explain that logic.
3. **Data source**: Where does the data come from? In the ideal state, data users should be able to explore the data lineage easily to understand the upstream tables and columns. This helps a lot when we need to troubleshoot a data issue or a metric change.
4. **Frequency and freshness**: How often is the table updated and when was it last refreshed? 

**DON'Ts**:
* Create a table with no documentation or incomplete information;
* Keep the documentation outdated when you update a table logic.

**DOs**:
* Always maintain complete and up-to-date table documentation. 

---

These are my top five principles to make a table that is friendly to your data colleagues. Follow them, data investigation will be faster, analysis will be easier, and models will be more accurate.
