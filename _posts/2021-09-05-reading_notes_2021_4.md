## Reading Notes 2021 July - August

This year I have been reading DS&Analytics related blogs with my friend Elise every Friday and Sunday night. This blog summarise the best articles we read in the past two months. As you can see, we read a lot about experimentations and causal inferences recently as we always find more interesting posts when digging deeper into this field. Hope you enjoy the reading as well :)  

#### Experimentation and Causal Inference
1. [**Experiments at Airbnb**](https://medium.com/airbnb-engineering/experiments-at-airbnb-e2db3abf39e7): A pretty old post by Airbnb covering their experiment infra and common considerations  
2. [**A/B Tests for Lyft Hardware**](https://eng.lyft.com/a-b-tests-for-lyft-hardware-570330b488d4): Different from most experimentation posts that focus on UI testing, this article talks about how Lyft tests hardware  
3. [**An A/B Test Loses Its Luster If A/A Tests Fail**](https://towardsdatascience.com/an-a-b-test-loses-its-luster-if-a-a-tests-fail-2dd11fa6d241): An introduction to why A/A test is important and how to properly do it  
4. [**How User Interference May Mess Up Your A/B Tests**](https://towardsdatascience.com/how-user-interference-may-mess-up-your-a-b-tests-f29abfcfccf8): How user interferences impact A/B tests and potential solutions to it  
5. [**Switchback Tests and Randomized Experimentation Under Network Effects at DoorDash**](https://medium.com/@DoorDash/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash-f1d938ab7c2a): Following the above one, a more detailed explanation of switchback tests by DoorDash  
6. **Experimentation in a Ridesharing Marketplace** ([Part I Interferences Across a Network](https://eng.lyft.com/experimentation-in-a-ridesharing-marketplace-b39db027a66e), [Part II Simulating a Ridesharing Marketplace](https://eng.lyft.com/https-medium-com-adamgreenhall-simulating-a-ridesharing-marketplace-36007a8a31f2), [Part III Bias and Variance](https://eng.lyft.com/experimentation-in-a-ridesharing-marketplace-f75a9c4fcf01)): A series of articles from Lyft discussing the challenges of ridesharing marketplace experimentation and how they tackled it  
7. [**How Wish A/B Tests Percentile**](https://towardsdatascience.com/how-wish-a-b-tests-percentiles-35ee3e4589e7): Wish talks about how it tests percentile in experiments  
8. [**How Not To Run an A/B Test**](https://www.evanmiller.org/how-not-to-run-an-ab-test.html): Why not peak early testing results and how to do it correctly  
9. [**Why We Moved Away from Conversion Rate As a Primary Metric**](https://medium.com/crap-talks/why-we-moved-away-from-conversion-rate-as-a-primary-metric-14b2d6cb5996): An interesting real case of how to choose the best metric for experiments  
10. **How to Use Causal Inference In Day-to-Day Analytical Work** ([Part 1](https://towardsdatascience.com/how-to-use-causal-inference-in-day-to-day-analytical-work-part-1-of-2-b5efbdbf8ab0), [Part 2](https://towardsdatascience.com/how-to-use-causal-inference-in-day-to-day-analytical-work-part-2-of-2-1824e7024cd2)): A comprehensive introduction to basic casual inference techniques  
11. A collection of articles on common causal inference approaches:  
a. [**A Practitioner’s Guide To Difference-In-Differences Approach**](https://towardsdatascience.com/does-minimum-wage-decrease-employment-a-difference-in-differences-approach-cb208ed07327)  
b. [**An Ultimate Guide to Matching**](https://towardsdatascience.com/an-ultimate-guide-to-matching-and-propensity-score-matching-644395c46616)  
c. [**Regression Discontinuity Design: The Crown Jewel of Causal Inference**](https://towardsdatascience.com/the-crown-jewel-of-causal-inference-regression-discontinuity-design-rdd-bad37a68e786)  
d. [**A Practitioner’s Guide To Interrupted Time Series**](https://towardsdatascience.com/what-is-the-strongest-quasi-experimental-method-interrupted-time-series-period-f59fe5b00b31)  
12. [**How Airbnb Measures Future Value to Standardize Tradeoffs**](https://medium.com/airbnb-engineering/how-airbnb-measures-future-value-to-standardize-tradeoffs-3aa99a941ba5): Airbnb introduces how it sets up a standardized framework to measure future value using propensity score matching
13. [**Causal Inference — Estimating Long-term Engagement**](https://medium.com/mercadolibre-tech/causal-inference-estimating-long-term-engagement-fac517929073): Compares the techniques to estimate long-term engagement with causal inference  

#### Others
1. [**3 Common Mistakes When Fighting Customer Churn**](https://productcoalition.com/3-common-mistakes-when-fighting-customer-churn-7d927bee0482): Discussion of common mistakes regarding improving customer churn
2. [**Using Sentiment Score to Assess Customer Service Quality**](https://medium.com/airbnb-engineering/using-sentiment-score-to-assess-customer-service-quality-43434dbe199b): How Airbnb used sentiment model to complement NPS
3. [**Task-Oriented Conversational AI in Airbnb Customer Support**](https://medium.com/airbnb-engineering/task-oriented-conversational-ai-in-airbnb-customer-support-5ebf49169eaa): A case study of how Airbnb used task-oriented dialog system to handle mutual cancellations
4. [**Using Chatbot to Provide Faster COVID-19 Community Support**](https://medium.com/airbnb-engineering/using-chatbots-to-provide-faster-covid-19-community-support-567c97c5c1c9): AI-based application of helpbot to facilicate COVID support
5. [**Possible Bias in Surveys**](https://towardsdatascience.com/possible-biases-in-surveys-3a5fda36c8a6): Three types of common bias in surveys and how we should improve the design to avoid them
6. [**Statistics: Are you Bayesian or Frequentist?**](https://towardsdatascience.com/statistics-are-you-bayesian-or-frequentist-4943f953f21b): An easy-to-understand article talking about the difference between Bayesian and Frequentist
7. [**Product Requirements Document (PRD): A Guide for Product Managers**](https://productcoalition.com/product-requirements-document-prd-a-guide-for-product-managers-bc15354fe91a): How to write a good PRD doc

#### Snack -- A Small Case Discussion  
Last month, I saw [a post on LinkedIn](https://www.linkedin.com/posts/activity-6831426218764709888-vaSH):  
*Today I learned that LinkedIn helps 6 individuals find a job every minute. This isn't a random number, but a rigorously computed metric that's tracked constantly. Isn't that amazing?*  
This post immediately caught my eye. So Elise and I spent some time brainstorming this metric might have been defined. And I am sharing it.  

There are two major components to this metric -- **whether a user is searching for opportunities on LinkedIn**, and **whether the user found a job**. We started with finding the proxies to both components:  
1. **whether a user is searching for opportunities on LinkedIn**:  
a. P0 (highest confidence) - active messages or positive message reaction to recruiter's messages (for example, click the schedule time to chat link in a message)  
b. P1 - LinkedIn apply actions (apply via LinkedIn or click on the apply button that leads to the job site)  
c. P2 - Other actions including browsing job boards, react to job opportunity LinkedIn posts, subscribe to LinkedIn premium, turn on 'open to opportunity' badge, etc.  
2. **whether the user found a job**:  
a. Most direct -- job change on profile (when job start time > job searching start time)  
b. Some indirect proxies (less accurate) -- turn off 'open to opportunity' badge, decrease in LinkedIn apply or activity interval, etc. -- but this could be a result of lost hope on finding a job on LinkedIn, so overall not very helpful here  

Next step, we can link these proxies together, and use a sort of backward attribution method to to build up the metric:  
If a user updated their job on LinkedIn profile, we can use below signals to attribute the job hunting success to LinkedIn:  
1. **Strong signals**: They once 'LinkedIn apply' to the new employer or clicked the job post of that employer, or had message with someone (recruiter/employee) from the new employer;  
2. **Moderate signals**: They once interacted with posts or people from the new company;  
3. **Weak signals**: Other activities on LinkedIn (proxies discussed in above section, but not relevant to the new employer).  
As you can see, the strong signals are the ones we have most confidence to tell that the job hunting success can be attributed to LinkedIn, but we might not want to include the weak signals as that could over-estimate this metric.  

We also talked about potentially using surveys and pop-ups to collect true flags -- for example, asking a user 'whether you found this job with the help of LinkedIn' when they update profile -- and collection data from the signals discussed above to train and improve a classification model to improve the accuracy of this metric.  


--  
[⬅️Previous](https://yudong-94.github.io/personal-website/blogs/reading_notes_2021_3)  [➡️Next](https://yudong-94.github.io/personal-website/blogs/reading_notes_2021_5)  


<a href="https://yudong-94.github.io/personal-website/" title="Back to Home Page">Back to Home Page</a>
