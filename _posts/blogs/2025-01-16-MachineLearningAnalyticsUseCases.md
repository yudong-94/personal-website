---
title: "Unlocking the Power of Machine Learning in Analytics: Practical Use Cases and Skills"
date: 2025-01-16
categories:
  - blog
tags:
  - data science
  - machine learning
  - analysis
---

**Your essential machine learning checklist to excel as a data scientist in analytics**

In the past decade, we have seen explosive growth in the data science industry, with a rise in machine learning and AI use cases. Meanwhile, the “Data Scientist” title has evolved into different roles at different companies. Thinking about functions, there are Product Data Scientists, Marketing Data Scientists, those specialized in Finance, Risk, and people supporting Operations, HR, etc.

Another common distinction is the DS Analytics (often referred to as DSA) and the DS Machine Learning (DSML) tracks. As the name suggests, the prior focuses on analyzing data to derive insights, while the latter trains and deploys more machine learning models. However, this does not mean that DSA positions do not involve machine learning projects. You can often find machine learning among the required skills in the job descriptions of DSA openings.

This overlap often leads to confusion among aspiring data scientists. During coffee chats, I frequently hear questions like: Do DSA positions still require machine learning skills? Or do DSAs also deploy machine learning models? Unfortunately, the answer is not a simple Yes or No. Firstly, the boundaries between the two positions are always blurry (even a decade after the data science job became a trend). Sometimes, within the same company, DSAs supporting different functions could be using very different skill sets. Secondly, machine learning itself is a broad field, covering things from simple linear regression to complex neural networks, and even LLM. Therefore, some of them could be fantastic tools for analytics purposes, while others are more tailored for building a production-grade predictive model.

But if I have to answer the question: “Yes, DSAs also use machine learning skills, but just not in the same way as DSML positions. Instead of building complex models and optimizing for scalability, accuracy, and latency, DSAs primarily leverage machine learning as a tool to generate insights or support analyses and focus more on generating interpretable and actionable outputs to better inform business decisions.”

In the section below, I will explain this answer further with three common machine learning use cases in analytics. These examples will provide a more concrete answer to the above question, and highlight the machine learning skills you need to succeed in a DSA position.

---

### Use Case 1: Metrics Driver Analysis

Usually, the first step to understanding a business or a product is to define and track the right metrics. But after completing this step, the question becomes how can we move the metrics in the right direction. Machine learning is a powerful tool for understanding what drives these metrics and how to influence them.

Let’s say you are tasked to improve customer retention. You might have heard tons of assumptions from user interviews, surveys, and even business intuition. A common way to validate the assumptions is to build a classification model to predict retention and identify important features.

Here is the process:
1. **Establish the assumptions** based on conversations with your stakeholders and customers, and your business understanding. For example,
- Customers with longer tenures are less likely to churn;
- Heavy usage of feature X indicates higher loyalty to the product;
- Customers who only use the mobile app are more likely to churn due to the missing features on the app.
2. **Collect features** based on your assumptions, for example, *customer tenure, time spent and frequency on feature X, and if the user is mobile only or not*.
3. **Build a classification model** to predict if a customer churned or not. Common classification models include Logistic Regression and tree-based models (random forests, XGBoost, LightGBM, CatBoost, etc.). My go-to model is the XGBoost model because it captures nonlinear relationships and feature interactions, has built-in methods to handle imbalanced datasets and avoid overfitting, and typically achieves a good accuracy baseline even before extensive parameter tuning.
4. **Generate data insights and business recommendations**. You can use the model’s Feature Importance to understand which assumptions were correct. You can also use SHAP values to decompose the prediction into contributions from each feature. For example, if the model reveals that mobile user only is a very important feature and is correlated with a high churn rate, the next steps could be 1. improving the mobile app to close the feature gaps; 2. launching an email campaign encouraging mobile-only users to try more features on the desktop version. And of course, you will monitor the effectiveness of these recommendations and continue monitoring the retention rate.

From the above example, you can see that building the model is only part of the task for DSAs. The real value comes from interpreting results and translating them into actionable business strategies.

### Use Case 2: Customer Segmentation  

We always talk about product-market fit; a critical part is understanding your customer portfolio and their needs. Therefore, data scientists are often asked to conduct customer segmentation tasks, grouping users based on similar behaviors or preferences.

There are numerous approaches to customer segmentation. Let me name a few:
1. **Simple demographics segmentation**. For example, you work for a fashion retailer that owns product lines with different price tiers. In this case, a simple solution to customer segmentation is to break down customers based on their household income (if you have this data).
2. **RFM (Recency, Frequency, Monetary) analysis**. You can collect metrics including how recently a customer spends (recency), how often they spend (frequency), and how much they spend (monetary). Then you can categorize high-recency, high-frequency, and high monetary value customers as VIP customers; high-recency, high-frequency, and low monetary value customers as price-sensitive customers, etc.
3. Back to our topic, you can also build an **unsupervised learning model** (K-Means Clustering, Hierarchical Clustering, DBSCAN, etc.). Unlike the classification model example above, unsupervised learning is a type of machine learning that identifies patterns and relationships in unlabeled data without predefined output labels. Let’s still stick to the fashion retailer example:
- You can **collect features** including customer demographics (age, income, etc.) and purchase patterns (how often and how much they spend on different product lines and types), then run them through a clustering algorithm like K-Means. This will automatically group your customers into several clusters.
- Though there are no existing true labels, you still need to **evaluate the model outputs**. Usually, you would examine the characteristics of each cluster to understand if the output makes business sense and what type of customers they represent, then give them a label that is intuitive to your stakeholders. For example, you might find a cluster of customers mostly purchasing discounted products, and you can label them “Bargain Hunters”; Another cluster of customers who spend a lot on luxury brands could be the “Luxury Shoppers” group.
- Once you have the reasonable segments, they could be used to inform product strategies and conduct targeted email campaigns and personalized product recommendations.

### Use Case 3: Experimentation and causal inference  

Another common task for DSAs is measuring the causal impact of a certain event. This involves randomized experimentation and more advanced causal inference methods when a controlled experiment is not feasible.

When it comes to randomized experiments like A/B tests, an application of Machine Learning is to reduce noise in experiment results by controlling for covariates. These adjustments improve the sensitivity of experiments and lead to smaller sample sizes or shorter test durations while maintaining statistical power. **CUPED (Controlled Pre-Experiment Data)** is one of those variance reduction methods that can incorporate machine learning techniques. It reduces the variance of the outcome metric by adjusting for pre-experiment covariates that are predictive of the outcome — something you can achieve with a machine learning model.

When it comes to causal inference, there are lots of machine learning use cases as it can be used to address key challenges like confounding, non-linearity, and high-dimensional data.

Here is an example of using machine learning to enhance **Propensity Score Matching**, which is a useful technique to manually create two comparable groups when you don’t have perfectly randomized test and control groups. Suppose your company launched a newsletter program and your stakeholder wants you to assess its impact on customer retention. However, users who subscribed to the newsletter might inherently differ from those who did not. To apply the Propensity Score Matching method here,
1. You can **train a machine learning model** (for example, logistics regression or XGBoost) to predict the likelihood of a user subscribing to the newsletter.
2. **Use the predicted “propensity scores” to match** newsletter subscribers with similar non-subscribers.
3. **Compare the retention rate from this matched control and treatment group**. This will give you a more fair evaluation of the newsletter’s impact on customer retention.
Machine learning also can be incorporated into other causal inference methods, such as Regression Discontinuity, Instrumental Variables, and Synthetic Control, which help address biases in observational data and derive the causal relationship.

---

I hope the three use cases above give you a concrete idea of how you can use machine learning in analytics workflows.

If you aim to be a Data Scientist specializing in Analytics, Here is your essential machine learning skills checklist for your interview preparation and daily work.

1. **Data Preparation**:
- Handle missing values and outliers
- Encode categorical variables
- Apply data normalization techniques
2. **Common ML Algorithm**: understand assumptions and pros and cons of each model and how to pick the right one
- **Supervised learning models**: Regression models (Linear Regression, Logistic Regression), Tree-based models (Random Forest, XGBoost)
- **Unsupervised learning models**: K-Means and Hierarchical Clustering
3. **Model Training and Evaluation**:
- Select the right evaluation metric
- Prevent overfitting
- Handle imbalanced datasets
- Feature selection and feature engineering
- Hyperparameter tuning
4. **Model Interpretation**:
- Understand coefficients in Regression models
- Understand Feature Importance in tree-based models
- Use interpretability tools like SHAP
- Translate model insights into business insights and communicate them effectively to non-technical stakeholders

By mastering these skills and understanding the use cases discussed, you’ll be well-equipped to leverage machine learning effectively as a Data Scientist in Analytics.
