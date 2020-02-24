<head>
  <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-112502179-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-112502179-1');
</script>
</head>

# A Starter Code for Xgboost Regression -- Use Kaggle House Price Prediction Competition as An Example

These days I have been writing too much SQL... Therefore, last week, to refresh my knowledge on xgboost and general modeling project process in R and Python, I spent two days to write the simple starter code for the Kaggle beginner level completition ['House Prices: Advanced Regression Techniques'](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) with a R version and a Python version. The result turns out to be acceptable since the code does not include very comprehensive feature engineering (sorry I am lazy lol). The RMSE is 0.134. But please forgive me that I do not want to mention the ranking on leaderboard since there are >30 submission with RMSE 0, which obviously submited the result from this publicly available dataset :(   
My code can be found in this [github repo](https://github.com/yudong-94/Kaggle-House-Prices-Prediction). Hope you will find it helpful in some way.    

### About the [dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

The dataset is a public dataset compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset.  

### What I Did (The Modeling Process I Followed)

1. **Data Overview**  
It's important to start your modeling from looking at the real data and understand what each column means and how it looks like. [Data dictionary](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) always come handy in this case.  
2. **Exploratory Data Analysis**  
But just a head(10) cannot really solve the myth of 'is this column useful'. So now it's the turn to look at closer look at those interesting variables. This include plot the distributions and correlations (scatterplot for numeric variables, barplot / boxplot for categorical variables, or whatever suits your scenario). This gives you a sense of what could be a strong feature while what is simply a noise...    
3. **Data Cleaning and Preparation**  
To make your data make sense (...) and prepare it for modeling, there are still a lot to do:  
you need to fix the data types (reading a csv directly always cause some data type issue, and sometimes there are columns coded with integer index but should not be considered as integers);  
NAs definitely need to be handled (get rid of the whole column if NA rate is too high, or impute it with reasonable values);  
And in the case of models like xgboost which does not accept categorical variables, you need to transform categorical variables to numeric variables. Two common methods are one-hot encoding and target encoding. A personally like target encoding, becuase one-hot encoding created too many columns yet target encode still perserve just one column yet encoded the info from our target variable;  
Last but not least, don't forget to create some new features based on domain knowledge or just common sense (here for this starter code, I just created some pretty simple ones, not much feature engineering are involved).     
4. **Modeling with Xgboost**  
I used the regressor in Xgboost for modeling, and the objective is set to optimize the RMSE of log(SalePrice), which is the same as the evaluation criteria of the competition. Also, I only did a 80/20 split of the training set for model validation, but ideally, you know, you should do a k-fold (especially when there are more data available).  

### Packages Used  
**R** -- tidyverse (mainly dplyr and ggplot2), xgboost  
**Python** -- numpy, pandas, matplotlib, seaborn, xgboost, scikit-learn (for splitting data only...)  

btw it's the first time I have used seaborn, and its grammar is surprisingly intuitive comparing to ggplot2 and matplotlib...  

### What Can Be Improved From This Code
Nothing is perfect, not to mention that this is just a starter code which spent only a weekend to write...  

Here are the things I think could be improved from this code:  
1. **More EDA + Feature Engineering**  
A lazy me skipped several variables in EDA since there are too many... I think a better way to do it is -- looking at all the variables and do a pre-screening to have some idea which variables could carry more info for your prediction obejective. Then validate it with your feature importance and choose which to drop to avoid noise / make modeling faster. Also, you need to create more features based on the knowledge you gained from EDA and feature importance, and keep testing them and iterate.  
2. **K-fold cross-validation**  
As I mentioned above, I only did a 80/20 split of the training set for model validation here, which is not idea (but for simplicity). One thing to notice is, you need to do target-encoding only with your traning set for each fold, instead of create before CV, which will introduce info leakage.  
3. **Tunning Parameters**  
I did not do a through parameter tunning here, but just played with several values of max_depth, eta and nrounds. But given good feature engineering, tunning hyperparameter is always a good next step to improve your model performance. Some strategies include grid search (comprehesive but computational expensive), random search (faster but not global optimal), bayesian optimization (selects the next hyperparameter value based on the function outputs in the previous iterations).  
4. **Model Ensemble**  
Here only xgboost is used, but more models could be used, from the linear regression to other tree-based models (RF, lightGBM, catboost), or even deep leanring models. Then ensembling the predictions from these models will give a better overall prediction (at least in the case of Kaggle competitions... you know, in real world, we need to think about cost.)  
