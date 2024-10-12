---
title: "Seven Common Causes of Data Leakage in Machine Learning"
date: 2024-09-12
categories:
  - blog
tags:
  - data science
  - machine learning
  - data engineering
---

**Key Steps in Data Preprocessing, Feature Engineering, and Train-test Splitting to Prevent Data Leakage**

When I was evaluating AI tools like ChatGPT, Claude, and Gemini for machine learning use cases in my last article, I encountered a critical pitfall: data leakage in machine learning. These AI models created new features using the entire dataset before splitting it into training and test sets - a common cause of data leakage. However, this is not just an AI mistake; humans often make it too.
Data leakage in machine learning happens when information from outside the training dataset seeps into the model-building process. This leads to inflated performance metrics and models that fail to generalize to unseen data. In this article, I'll walk through seven common causes of data leakage, so that you don't make the same mistakes as AI :) 

---

## Problem Set Up  

To better explain data leakage, let's consider a hypothetical machine learning use case:
Imagine you're a data scientist at a major credit card company like American Express. Each day, millions of transactions are processed, and inevitably, some of them are fraudulent. Your job is to build a model that can detect fraud in real-time. You have historical data that includes known fraud cases, making this a classic classification problem with imbalanced data, as fraudulent transactions are typically a small percentage of the total.  

Below are some features you have at hand:
* **Transaction-related features**: transaction amount, currency, time, billing address, type (online vs. physical), location, etc.
* **Card-related features**: credit limit, card balance, card type, card tenure, etc.
* **Merchant-related features**: merchant name, merchant category, merchant address, etc.
* **Customer-related features**: customer address, age, income, spending history, etc.

---

## Mistakes in Data Pre-processing 

To prepare your dataset for model development, you will often conduct essential data transformation steps, such as scaling numeric features, encoding categorical variables, and imputing missing data. These transformations could involve calculating distribution or metrics from the multiple rows of the dataset. Therefore, if they are applied to the entire dataset before splitting into training and test sets, you risk leaking information from the test set into the training process.  

Here's how that can happen:  

### Mistake 1: Scaling numeric features with the full dataset 

In our fraud detection case, we have many numeric features, such as transaction amount and card tenure. Certain machine learning models, like logistic regression with L1 or L2 regularization (Ridge or Lasso regression), require normalizing  numeric variables as the regularization penalizes large coefficients. Typically, this involves calculating the mean and standard deviation of a feature (using something like StandardScaler from scikit-learn). If you calculate the distribution of transaction amount using the entire dataset and then apply them to standardize both the training and test sets, you are exposing the transaction information from unseen data (testing data) to training. Therefore, we should standardize the transaction amount in both the training and testing sets with the mean and standard deviation from the training set only.  

### Mistake 2: Performing target encoding on the full dataset  

Many machine learning models only accept numeric variables. Therefore, we need to encode the categorical variables into numeric variables. While one-hot encoding is common, target encoding is another popular approach. Target encoding replaces the categories with numeric values derived from the target variable (fraud or non-fraud here). This usually involves calculating the target mean of each category (for example, the fraud rate from each merchant category). If you calculate the mean from the full dataset, you are again leaking important information about the target data in the test set to the training set as you included the fraudulent transactions in the test set. Therefore, we should calculate the target mean for each category using only the training data, and then apply the learned encoding to the test set.  

### Mistake 3: Imputing missing values with test set information  

Missing data is common in real-world datasets. For example, we might not have income from every customer. A common approach is to impute missing numeric values with the median value (i.e. median customer income from non-null rows). For a similar reason, you should only calculate the median value from the training set, instead of the full dataset, and apply it across both sets.  

### Mistake 4: Upsampling/SMOTE before Splitting the Data  

As mentioned above, fraud detection is typically an imbalanced classification problem, where fraudulent transactions make up a tiny fraction of the total. Resampling, specifically upsampling (duplicating minority class records), is a useful technique to balance the dataset. If you upsample the minority class (fraud records) before splitting it into training and test sets, the same fraud cases could appear in both, leading to artificially high performance. SMOTE (Synthetic Minority Over-sampling Technique) is another common method to handle imbalanced datasets. Similarly, if it is applied before the train-test splitting, synthetic examples generated from test data can leak information into the training set. Therefore, these imbalanced dataset treatments should be applied to the training set only - once the training set has been augmented with upsampling or SMOTE, you should train your model on the augmented training set, and evaluate the performance on the original test sets.

---

## Mistakes in Feature Engineering  

Now that you have prepared the datasets, you are ready to create new features as part of feature engineering. However, this also carries the risk of data leakage.  

### Mistake 5: Using Future Data in Feature Engineering  

In fraud detection, a sudden change in spending behavior is often a red flag. Therefore, you might create features like transaction amount to average amount, measuring how unusual a certain transaction is compared to the customer's average spending. But what data points we should use to calculate this average? To avoid data leakage, we need to make sure no future data are being used, as they will not be available when you make predictions on real-time transactions. In this case, only past transactions should be used to compute the average spend.

---

## Mistakes in Train-test Splitting  

While a random split of data into training and test sets is common, it's not always appropriate. Certain splitting strategies can inadvertently cause data leakage by allowing the model to "see" test data during training.  

### Mistake 6: Data Overlapping in Training and Test Sets  

Our fraud detection dataset is on the transaction level, which means it will have multiple transaction records from the same customer. It is not uncommon for fraudsters to make several similar fraudulent transaction attempts within a short time. If you randomly split the data into training and test sets, transactions from the same customer could end up in both, allowing the model to "learn" from the test data. A solution here is to use the group shuffle split instead of a random split, which performs the train-test split at the customer level, ensuring the transactions from the same customer stay together during the split. This ensures your model is tested on truly unseen data and can better generalize to new customers.  

### Mistake 7: Failing to Use Temporal Splits for Time-Series Data  

When working with time-series data (e.g., stock prices, weather patterns, user activity logs), it's crucial to maintain the time-based sequence during the train-test split. Randomly splitting the data can result in severe data leakage as the model will learn from future events that wouldn't be available at prediction time.  

Let's assume a new machine learning use case, where you want to predict the future transaction amount of a customer. Randomly splitting the dataset could cause future transactions to influence the training set. Instead, you should use a temporal split, where all the data points in the test set occur after the training data. This mirrors real-world scenarios, where predictions are always made based on historical data.

---

## Conclusion  

When building machine learning models, we often discuss data pre-processing, feature engineering, and train-test splitting as separate steps. However, they are deeply interconnected, and mistakes in one can impact the entire modeling process. As shown in the examples above, the sequence of these steps needs to be carefully designed to avoid data leakage. In our example, you should follow the sequence of 
1. data collection
2. train-test split
3. data pre-processing (only based on training data)
4. feature engineering (only using information available at prediction)
5. model training and evaluation

More generally, to prevent data leakage, always ask yourself two key questions:  
1. **Am I exposing information from the test set to the training process?**
2. **Am I using future data that won't be available when making prediction?** 

These two questions will help you avoid overly optimistic performance metrics and build models that generalize well to new data. You should also apply the same principles to the cross-validation process to ensure each fold is also free from leakage.  
