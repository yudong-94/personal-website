---
title: "FERC topic modelling"
date: 2025-10-05
categories:
  - blog
tags:
  - data science
  - career
header:
  teaser: /assets/images/article_covers/ds_at_startups.png
excerpt: "What I learned about growth, visibility, and chaos over the past five years."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/what-being-a-data-scientist-at-a-startup-really-looks-like/).  

---

**What I learned about growth, visibility, and chaos over the past five years**

After an incredible five years, I left Brex in August. Time really flies. I joined Brex when it was three years old, and I can still vividly remember my first day. At the same time, those five years felt much longer. This is all due to the extensive knowledge I’ve gained along the way, from joining a young data team and learning the full data cycle, to collaborating with Operations, GTM, and Product, and eventually [transitioning into management](https://towardsdatascience.com/from-data-scientist-ic-to-manager-one-year-in/). This accelerated growth is one of the biggest benefits of joining a startup as a data scientist.

“Shall I join a startup or a more established company?” I hear this question from my network all the time. In this article, I will share the data scientist’s life at a startup based on my own experience. Hopefully, this will help you navigate through your own career path.

*A quick note: “startup” is a broad term that covers many types of companies. For context, Brex is a US-based fintech startup that provides corporate cards, banking services, and expense management software for business customers. I joined Brex after three years of full-time experience in product data science. At the time, Brex was a three-year-old Series C startup with 500+ employees. Therefore, my experience may differ from what you’d experience at an earlier-stage company.*

---

### I. Domain-specific vs. Goal-oriented  

Startups move fast — they need to adjust strategies based on the market feedback and iterate constantly to ensure product-market fit. Data Scientists, as an expensive resource, need to shift their focus area accordingly to create the largest business value.  

Taking my own experience as an example:  

1. When I first joined Brex, the priority was to onboard as many customers as we could while controlling for fraud risk. Therefore, I worked closely with the Onboarding team to optimize the account application flow and improve resource allocation for the Operations team.
2. As our customer base grew, the next priority was to scale our customer support (CX) function to provide the best-in-class support. I partnered with the CX team to analyze customer pain points and reduce product frictions. (Read [my article](https://towardsdatascience.com/the-secret-power-of-data-science-in-customer-support/) for more details on DS in CX.)
Later, I collaborated with the Implementation team to accelerate ramp-up for new customers and with the product team to identify churn drivers and improve retention.  
3. As you can see, startups are very goal-oriented. At large firms, you might specialize in one product feature for years; At a startup, the company’s needs can completely change within a quarter, and data scientists change their domains more frequently as a result.

The upside is that this allows the data scientists to explore and collaborate with more functions and have a more holistic view of the business. I worked with nearly every team at Brex in the past five years — watching how GTM (go-to-market) found prospects and closed deals, seeing how Product and Customer Support worked together to address customer pain points, and learning how the Customer Success team reduced churn and drove upsell. This is a far more effective way to understand business operations than reading books or taking courses at a business school. It also ensures the data scientists have clear and high-impact business questions to solve.  

But what’s the challenge? Data scientists need to follow the company’s strategy and adapt to changes constantly. This means shifting priorities accordingly, and sometimes having to build things the fastest way, instead of the most scalable or reliable way. Tech debt piles up quickly with tons of one-off dashboards and multiple versions of the same metric, confusing stakeholders and the data team itself. Establishing the best practices takes time, so living with the chaos sometimes is unavoidable — though being able to set up the standards from 0 to 1 (or seeing others doing so) is also a rewarding part of working at a startup, especially for aspiring data science leaders.  

### II. Data Analyst vs. Data Engineer vs. Data Scientist? All the Above.  

Job titles in data these days are confusing — Some Data Scientists focus on experimentation, while some are deep in machine learning; Some Data Analysts simply build dashboards, but some primarily do product analytics. But when it comes to startups, titles matter less — you will likely do everything.

When I joined Brex, everyone had the same title, “Data Scientist”, but we all had to wear multiple hats. We split the data team into DS, DA, and DE functions only since early last year. As I mentioned above, startups are goal-oriented. Therefore, when there are limited people and no clear team structure, you will need to do everything to achieve the goal.  

* **Data Engineering**: I learned [data modeling](https://towardsdatascience.com/top-5-principles-for-building-user-friendly-data-tables-0dfe168cecc1/), Airflow, ETL processes, [SQL optimization](https://towardsdatascience.com/mastering-sql-optimization-from-functional-to-efficient-queries-74d8692f10be/), and many other data engineering skills in the past five years. I remember one of my first projects at Brex was to migrate our data pipelines from dbt to an internal tool. Yes, as a data scientist at a startup, there is a high chance you also need to build, own, and maintain your own data pipelines.
* **Analytics**: Joining a startup means there are many business areas with no or minimal data support. Therefore, to help the team better understand their performance and gain their trust, the very first step (after you have built the data pipelines) is to define the success metrics and build the dashboards. Once the metrics are closely monitored, questions like why they moved or how to move them come next naturally. These are all common analytics tasks.
* **Data Science**: There are also plenty of advanced data science use cases at startups. Machine learning models are helpful to detect fraud, predict churn, estimate LTV (lifetime value), etc. Causal inference is also critical to evaluate the impact of a marketing campaign or a product launch.  

Is it a good or bad thing to wear multiple hats?  

If you are not yet sure about which type of data track you are most interested in, joining a startup will help you to get some flavor of everything and decide which route to go next. Or if you would like to become a Head of Data or even build your own company someday, this full-cycle exposure is super valuable.  

Meanwhile, the downside is also very clear — you will spend time on things you are not interested in, or not that relevant to your long-term career goal. The fact that you own the whole data lifecycle can also confuse stakeholders, as they usually only care about a certain type of output, for example, dashboards or models, but do not realize you need to spend another 50% of time on data pipelining.  

### III. Higher visibility  

Data scientists at startups never lack visibility. From day one at Brex, I got to work directly with the C-suite. Leadership will often come to you with urgent and important business questions, hoping you can do some data magic to uncover insights and drive business growth. This is not something you usually get to experience at an established company, especially as a junior data scientist. It is a high-pressure but highly rewarding environment.  

For example, during the [Silicon Valley Bank Crisis in March 2023](https://en.wikipedia.org/wiki/Collapse_of_Silicon_Valley_Bank), many startups were impacted, facing the risk of losing their operational funds. I worked very closely with the leadership team to help startups survive this hard time. I created a real-time tracker on new customer applications, analyzed application review velocity to estimate additional workforce needs, and collaborated with other DS to automate and speed up onboarding checks. It was an intense weekend, working cross-functionally in a war room (virtually on Zoom) from 8 am to midnight. However, this is one of my best memories at Brex, showing the true customer obsession from our leadership, and how data scientists can contribute directly and drive huge business impact.  

### IV. Exposure to new tools  

Young startups are also brave enough to try a new tech stack. Therefore, they are often the early adopters of new tools, while larger companies might take months (and layers of approval) before even piloting, not to mention the significant migration costs.  

For example, during my time at Brex,

* We started exploring LLM use cases in data science two years ago, and have access to all major LLM APIs (OpenAI, Claude, and Gemini) internally, open to everyone. Every year, Brex hosts an internal hackathon and encourages employees to innovate. Two years ago, I collaborated with engineers to build an [AI-powered customer feedback platform](https://medium.com/brexeng/brexs-ai-powered-engine-for-identifying-customer-insights-72aadeb62e8e?) to automatically categorize, summarize, and analyze various unstructured feedback data. Last year, I built a RAG-based chatbot to help stakeholders retrieve customer feedback related to a specific product feature easily. This year, I worked with other data scientists to explore text-to-SQL capabilities with Claude Code and Snowflake CLI. I absolutely enjoyed these opportunities to apply cutting-edge techniques to data science workstreams.
* We frequently piloted new data solutions. For example, we were an early customer of [Hex](https://hex.tech/) for collaborative and easy-to-share data notebooks. We use [Statsig](https://www.statsig.com/) for experimentation and event tracking. We also tried various AI-powered business intelligence software for better self-service analytics.
* Working at a startup helped me stay informed of new technologies and adopt them into my daily workflows. That not only made the work more exciting but also kept me competitive as the industry evolved.  

On the flip side, being an early adopter can mean disrupting existing workflows and rebuilding infrastructure. It also means a less stable development experience.  

---

### Conclusion  

So, should you join a startup or a more established company?  

Startups offer speed, variety, visibility, and cutting-edge exposure. But they also bring chaos, shifting priorities, and the need to wear hats you may not enjoy. If you thrive in ambiguity and want to accelerate your learning curve, a startup can be an incredible place to grow as a data scientist.  

For me, five years at Brex have taught me an incredible amount of knowledge about business and data. I will forever be grateful for the lessons, the people, and the chance to see what data science can look like at a fast-growing startup.  
