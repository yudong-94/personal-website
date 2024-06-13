---
title: "My Five Key Learnings To Be a Better Data Scientist"
date: 2024-06-12
categories:
  - blog
tags:
  - career
---

#### Reflection on my six-year data science career

I started my first full-time data science job in January 2018 as an Associate Product Analyst. This is the 7th year of my DS career, now as a Senior Data Scientist. Six years passed very fast (especially with the pandemic). I worked for two companies, supported at least 10 different teams, collaborated with partners on product, engineering, design, finance, and operations, and touched various data science realms including data pipelining, dashboarding, metrics review, deep dive analysis, A/B testing, and modeling. 

Therefore, I feel it's time to reflect on this journey. Here are my five key learnings.

#### I. Technical Skills Are Important But …
When I was at school, I used to be fascinated with technical skills. I spent lots of time learning and exploring different machine learning models and participated in Kaggle competitions. However, since I started working in the industry, I realized there is way more I need to worry about than writing codes and building fancy models, and some of those things are actually more important.  

**One of those things I want to highlight is understanding the business context**, no matter you are more on the analytics side or the ML side. We are hired by companies to create (monetary) value, therefore, at the end of the day, companies care the most about whether the analysis you did or the model you built could bring more users, increase revenue, or cut costs. And understanding the business context is the key. We have all heard of the term 'actionable insights' - the best insights are the ones that your business stakeholders can act on. But again, if you do not have enough domain knowledge, you will not know which insights are actionable.  

Also, we are mostly given clean datasets at school. But in reality, data is always messy. You will likely spend at least 30% of your time collecting data, cleaning them, and even setting up data pipelines to ensure you have good-quality data to run analysis or build models. And it requires a deep understanding of the business context to identify what is 'good-quality data'. For example, good business sense makes it easier for you to notice it when a business metric you calculated is clearly off the normal range; Different missing values imputation techniques have different implications, and business understanding can help you choose the best solution.  

Not to mention that today AI tools like ChatGPT have lowered the technical barriers to being a data scientist, and will continue to do so. In [this article](https://yudong-94.github.io/personal-website/blog/EvaluatingChatGPTinDataScience/), I evaluated the data analysis capability of ChatGPT. You can see how much it can do a junior data analyst/scientist's job, but what is clearly missing is the knowledge of your specific business problem.  

**To conclude, technical skills are the minimum requirements to land you a data science job. But they are not the only things differentiating you (from chatGPT) and making you a great data scientist.** 

Then what is the best way to gain business context? 
1. **Use the product yourself if you can**. I remember I had at least five test accounts when I was working at Ancestry. And I use Brex a lot as a user myself. Trying different user paths and clicking around in the UI is incredibly helpful in understanding the engagement model and identifying potential drop-off spots and pain points. 
2. **Talk to your cross-functional partners**, including PMs, engineers, designers, etc, and meet regularly with them to share your findings. They usually have tons of understanding of the product from different perspectives and can help you understand the current product goal, what has been tried in the past, and the learnings, plus what is doable and what is not.  

#### II. Don't Undervalue Reporting and Dashboarding Work  

This one might be an unpopular one.  

Being a data scientist today means a lot of different things. Especially if you are working at a startup, you are almost required to be "full-stack". Among all those different task types, we all love doing deep dive analysis, running A/B testing, and building complicated models, meanwhile, reporting and dashboarding work is usually unfavored. I feel the same way most of the time, and we data scientists are often evaluated based on those more technical projects. Still, I want to say these work have their values and are critical for a new product feature or a new business unit that had little data support in the past. I believe they have three main values:  
1. **It helps to set up the baseline**. Before doing any of those advanced analytics, we always need to ask ourselves what is our goal or what are we trying to improve. However, this is a difficult question if we don't have a dashboard tracking our key metrics, or we don't even have an agreement on the key metrics. Imagine we made lots of effort to optimize our marketing budgets with media mix modeling to acquire tons of new users, but those users churned at 90% per month (but we did not know as we did not track retention rate), then it's just wasting money.
2. **It could bring quick insights**. At the beginning phase of product development, things could change very fast, and that means constant changes in metrics. So it is important to monitor the metrics closely and diagnose any trend shifts quickly. Even for a mature product, you might see metrics anomalies from time to time, due to changes in the feature, in user mix, or the competitive environment, etc. It is important to catch them early on with routine reporting and metrics reviews.
3. **Last but not least, it is a great way to earn trust**. Reporting and dashboarding are fundamental to understanding a product and measuring its impact, thus business stakeholders usually value it a lot. Being able to build accurate reporting, discuss the metrics, and provide business recommendations accordingly is very helpful to build relationships with your cross-functional partners, especially in the early days.  

But of course, when we have a set of agreed key metrics to monitor, we should make sure to automate these reporting work, so we can make more time for those work we love better, and eventually unlock more values.  

#### III. Effective Communication and Collaboration  

If you ask me what is the biggest surprise out of school, I would say - meetings. I never thought that a data scientist needed to attend so many meetings on a daily basis. Sometimes, meetings take more than half of the day for me. However, the majority of them are necessary. Today, I view data science projects as an iterative process - I go to cross-functional meetings to collect business pain points and questions, and then I translate them into data questions. Next, I use data science tools to run analyses and translate them into business languages. Lastly, I bring the insights back to my stakeholders, and we discuss ideas and next steps, which could evolve into an experiment we want to run, a model we want to build, or another analysis. These steps repeat themselves and effective communication and collaboration are the key to delivering continuous business values.  

Honestly, this has been hard for me, as I am very introverted (and based on my observation, many data folks are), plus English is not my first language. Below are some methods I found useful to improve my communication skills.  

**First, Listen to what others say in the meetings**. Many times I am too shy to speak in meetings, especially when I am new to a team. In those cases, I took the opportunity to learn from others instead, especially when my manager or senior teammates were in those meetings. What I learned includes how to communicate with different stakeholders, how to talk about data solutions in plain English, how to set the right expectations, how to make small talk, and how to push back :)  

**Secondly, polish presentation skills**. Presentation is one of the most common ways to share analytics work with stakeholders and make an impact. Polishing presentations has two parts - to make the best deck and to communicate data insights most effectively. There are many articles online educating you on how to make slides. In my opinion, some key takeaways are: 
1. Limit the number of text on your slides. On the analysis slides, summarise insights in one sentence and put it in the slide header to accompany the charts.  
2. Pick the right type of visualization and make the charts and labels large enough so people can easily understand.  
3. I specifically like to structure my presentation this way: context -> key insights -> recommendations -> detailed analysis -> summary (repeat the key insights and recommendations to strengthen their impression). It makes it easier for the audience to capture the main message you want to convey. 

As for verbal communication, I am 95% confident that my business stakeholders will not be able to explain what is 'statistically significant' accurately. But that's fine. I mean, it also takes me several seconds to phrase it scientifically. However, it is our job to conduct analysis with rigorous statistics and communicate our findings in easy-to-understand ways. And if you don't feel confident enough, rehearsing before the official presentation always helps.  

Of course, with more experience in the field, I started to support product teams on my own and lead analytics initiatives. Those opportunities are super valuable as they force me to collaborate cross-functionally and grow fast.  

#### IV. Be a Team Player
Being a senior data scientist myself now, I am not only required to be a good IC, but also be able to contribute to the team and help others grow. I feel the increasing importance of being a good team player. So, how to be a good team player?  

**The first thing that comes to my mind is writing good documentation.** This is small (and tedious) but super important. One thing people usually struggle with at onboarding is understanding all the tables, metrics, and past projects. When that happens to me, I usually search in Slack, Confluence, and Google Drive first, then ask teammates. And that's when I hope there is better documentation. So, to make others' lives easier (and make your own life easier when you need to go back to something after three months), adding detailed table documentation, and writing project summary and model methodology docs is critical.  

**And to extend the scope a little bit, I think we should always think about setting up best practices for the team when we see opportunities**. Just taking documentation as an example, seeing how many tables are missing descriptions, maybe it's a good time to propose a team-wide initiative to increase documentation coverage and set up requirements for new tables. I have launched a Looker training to help teammates and stakeholders get started with Looker quickly and drafted a SQL query optimization course to advocate SQL best practices to save query time and costs.  

**Lastly, try to mentor your junior teammates**. It is something new to me so I am still learning. In the past six years, I have met many great managers and mentors, so I totally understand how valuable a good mentorship is to someone new in the field. I have also found this mentorship process mutually beneficial as I got to know more about others' projects and learn new domain knowledge and techniques.  

#### V. Keep Learning and Be Prepared
**The last takeaway I would like to share is to keep learning**. We all know that data science is a fast-evolving field. There are new models and new techniques every day. For example, so many AI tools emerging every day and making our lives as data scientists easier. I set aside some time every Friday and Sunday night to read interesting blogs on Medium (see my bi-monthly reading notes here). Not every blog I read will help me immediately at work, but they at least educate me on what is out there, and when I encounter a new problem, I know what I could potentially use.  

**Moreover, learning should not be limited to the data science field**. DS roles are highly cross-functional these days, so I also find it helpful to deepen my understanding of engineering frameworks, data pipeline tools, product design knowledge, etc. It makes the conversations with my stakeholders smoother and prepares me for future challenges.
