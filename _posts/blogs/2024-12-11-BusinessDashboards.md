---
title: "5 Essential Tips to Build Business Dashboards Stakeholders Love"
date: 2024-12-11
categories:
  - blog
tags:
  - data science
  - career
header:
  teaser: /assets/images/article_covers/business_dashboard_cover.jpg
excerpt: "A practical guide to designing clear, effective, and actionable dashboards for decision-making."
---

**A practical guide to designing clear, effective, and actionable dashboards for decision-making**

Working in data science, dashboarding often feels like an **unfavored** but **unavoidable** work. Why is it unfavored? Dashboarding is less technical (less fancy) than analysis and modeling, and more repetitive. But why is it also unavoidable? It is the first and must-have step to understand any product, opening the gate to analysis and modeling. It even helps build trust with stakeholders as dashboarding is usually among the first requests from your stakeholders.  

Meanwhile, the difficulty of dashboarding is also often **undervalued**. I have seen numerous dashboards built by colleagues in the past seven years. Surprisingly, not everyone does this ‘easy task’ well. You might be wondering, isn’t dashboarding just creating a bunch of charts? Well, Yes and No. To build a good dashboard, you need to logically organize each visualization and simplify the complex data for your audience. **It is more about data-informed decision-making**. Moreover, a good dashboard can always enable self-serve analytics and reduce tedious data pull requests, benefitting the data team in return.  

**In this article, I will share my top five tips for designing effective business dashboards that provide clarity, actionable insights, and lasting value**. These tips apply to any dashboarding tools you use — no matter it is Tableau, Looker, PowerBI, or something else.  

### I. Start with the North Star metric 🌟  

Dashboards are built to measure performance — whether it’s for a product, a marketing campaign, an experiment, a team, etc. Therefore, you should have a North Star metric that best aligns with the goal. On the high level, the North Star metric should be **simple, focused, and actionable**. For example, it could be DAU (Daily Active User) for the Facebook App, GMV (Gross Merchandise Value) for Amazon, and Minutes Watched for YouTube.  

**Pro Tips**:
* You should discuss with your stakeholders to agree on the North Star metric, and highlight it in a predominant location on the dashboard (usually the first section with the largest font sizes).
* If your team has a specific target for the North Star metric, make sure to display it clearly on your dashboard to indicate if the metric is trending in the right direction.
* Take it one step further, you can also set up alerts if the metric drops below a critical threshold to provide a timely warning — this is a very common feature supported by most BI tools.

### II. Focus on common business questions 🤔  

The best dashboards deliver actionable insights promptly and enable decision-making. Therefore, beyond displaying your North Star metric, the dashboard should include secondary metrics and deep-dive functionality to address common business questions and automate data exploration requests.  

Let’s assume we are building a dashboard tracking the health of the ChatGPT App and we have decided MAU (Monthly Active User) to be the North Star metric, measuring the overall user base size and stickiness. But when it goes up or down significantly, it is always the data scientist’s responsibility to identify the root cause. A common way to conduct root cause analysis is to break down the metric by its funnel steps and explore important segments. To automate this step, after showing the MAU trend on the dashboard, we could add the below sections:  
* Let's decomposite MAU. `MAU this month = MAU last month + new users acquired this month - users churned this month`. Therefore, it will be helpful to include the # of new users trend and churn rate trend to diagnose if a decrease in MAU is due to lower user acquisition or higher user churn.
* Stakeholders might care more about certain segments. For example, maybe ChatGPT is expanding European markets right now, therefore people want to understand the MAU trend in Europe vs. other markets. In this case, you should highlight it in a section breaking down the MAU by region. Other common segments include devices, user tenure, age groups, etc. You can also include these segments as filters on the dashboard, so your stakeholders can explore the data on their own.

This example above also demonstrates that the secondary metrics and deep dive sections are largely influenced by the business understanding. Therefore, **dashboarding is also an iterative process with stakeholders**, and it is critical to identify common business questions and design the dashboards accordingly.

**Pro Tips**:
* Align with stakeholders about what business questions they would like to answer with the dashboard, and include corresponding deep-dive sections to enable self-service analytics;
* It is a good idea to provide a dashboard mockup during the design phase, including the North Star and secondary metrics, segments, and filters on the dashboard. Simply discussing in a meeting is hard, but providing a visual draft will inspire conversation, clarify requests, and reduce unnecessary revisions later.  

### III. Define metrics clearly 📐  

Now that we have discussed what metrics to include on the dashboard, the following tips focus on how to deliver the data insights easily.  

Though we always say that a good data visualization should be intuitive and self-explanatory with minimum text, let’s be honest, **business dashboards value accuracy and clarity more than anything else**. Therefore, I recommend including concrete metric definitions and all the necessary descriptions on the dashboard.  

Returning to our ChatGPT MAU example, to avoid confusion, you should be explicit about:
* What qualifies as an ‘active’ user? does it mean creating at least one new conversation in the past 30 days, or does interacting with an old thread count too?
* Are we looking at all registered users or only ChatGPT Plus subscribers?  

Every reader has their own interpretation of a metric, and your company might have had multiple versions of an OKR — My team was just cleaning up four versions of the TTR (time to resolution) calculation for the CX team last week… Therefore, it is a good idea to be extra specific.

**Pro Tips**:
* Include a detailed description of each metric to avoid confusion. You can also link to internal documentation if it exists.
* Other helpful details include the goal and scope of the dashboard, the freshness of the dashboard (refresh frequency and when was it last updated), and the links to related dashboards or analyses.  

### IV. Choose the right visualizations 📈  

We are at the fourth tip now and finally get to the visualization part :) I have written about my [7-year weekly visualization journey](https://yudong-94.github.io/personal-website/blog/WeeklyVizJourney/) and [7 less common but powerful visualization types](https://yudong-94.github.io/personal-website/blog/SevenVisualizationTypes/). These articles focus on making single data visualizations but could be too creative or complicated when it comes to visualizations in a dashboard. Again, the goal of a dashboard is to deliver data insights quickly, so **it prioritizes clarity and simplicity**.  

You can find many examples of good business dashboard design on [this Tableau Public page](https://public.tableau.com/app/discover/business-dashboards).  

**Pro Tips**:
* **Pick simple and intuitive visualization types**. I recommend sticking to basic chart types in dashboards— use bar charts for comparisons and line charts for trends. I am personally against pie charts because it is visually hard to compare the relative sizes of the slices (unless you explicitly label them).
* **Combine summary stats and trendlines**. It might sound repetitive, but putting summary stats and trendlines together helps stakeholders quickly see the current number without hovering over the charts and compare it with the targets. For example, when tracking a weekly metric like CSAT, I will include summary stats of CSAT this week, % change week-over-week, and % over/above the target, and then put the weekly CSAT trend next to them.
* Of course, all the important considerations for single visualizations are still relevant and you should be detail-oriented. For example, you should cover sufficient historical data in line charts, include clear title and axis labels, use effective color schemes, add helpful tooltips, etc.  

### V. Optimize dashboard performance 🚅  

Apart from visual design, **performance is another key piece in dashboarding**. Honestly, the most common complaint I’ve heard from stakeholders about business dashboards is “This dashboard loads too slowly” :(  

Here are two parts of the dashboard performance:
* **Data connection and underlying tables**. All the metrics come from your database, so your data infrastructure and pipeline influence the dashboard performance. Taking Looker as an example, if you load a Looker dashboard without any cached results, it hits your data warehouse, runs the SQL query, retrieves the result, and at the end renders the visualization. Therefore, how your underlying table is structured and your data warehouse setup matters. I once saw a Looker-generated query that joins six large tables together given how the joins are defined in [LookML](https://cloud.google.com/looker/docs/what-is-lookml) (the Looker configuration files used to create semantic data models). However, only three tables were really necessary for the specific metric. This sort of suboptimal setup increases the query time and eventually slows down your dashboard.
* **BI tool limitation**. Of course, each BI tool has its own limitations. But generally speaking, you should limit the number of charts on your dashboard to ensure the responsiveness of the UI elements.  

Above are my top five tips for designing an effective business dashboard. To recap, here is my checklist 📋:
* Align with your stakeholders on the key business questions they would like to answer with the dashboard;
* Define your North Star metric, secondary metrics, and key segments;
* Make sure all the metrics are clearly defined on the dashboard to avoid confusion;
* Choose simple and intuitive visualization types with attention to detail;
* Optimize the dashboard performance with thoughtful underlying infrastructure design.  

Dashboarding is more than just data visualization but requires stakeholder collaboration, business understanding, data modeling, and even a bit of UX design. By following these tips, you will create dashboards that empower decision-making and build trust with your audience.
