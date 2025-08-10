---
title: "Rethinking Data Science Interviews in the Age of AI"
date: 2025-08-07
categories:
  - blog
tags:
  - data science
  - llm
  - career
header:
  teaser: /assets/images/article_covers/ds_interview_with_ai_cover.jpg
excerpt: "How AI is transforming data science interviews — and what hiring managers and candidates should do to adapt."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/rethinking-data-science-interviews-in-the-age-of-ai/).  

---

**How AI is transforming data science interviews — and what hiring managers and candidates should do to adapt**

AI is [rewriting the day-to-day of data scientists](https://yudong-94.github.io/personal-website/blog/AIforDataScience/). To stay competitive, data scientists must learn how to improve productivity and unlock new possibilities with AI. Meanwhile, this transformation also poses a challenge to hiring managers: how to find the best talent that will thrive in the AI era? One critical step in building a strong AI-empowered data team is to revamp the hiring process to better evaluate candidates’ ability to work alongside AI.  

In this article, I will share my perspective on how data scientist interviews should (would) evolve in the age of AI. While my focus here is on Data Scientist Analytics (DSA) roles, the ideas here also apply to other data positions, such as Machine Learning Engineers (MLE).  

---

### I. The Traditional Data Scientist Interview Loop  

Before talking about how things will change, let’s go through the current structure of data scientist interviews. Aside from the initial recruiter call and hiring manager screening, a typical data scientist interview process includes:  
1. **Coding interviews**: SQL or Python coding questions to test syntax and basic logic.
2. **Statistics interviews**: Statistics and probability questions, as well as the most common statistical applications in data science workflows, such as A/B testing and causal inference.
3. **Machine learning interviews**: Deep dive into machine learning algorithms, experiences, and cases.
4. **Business case interviews**: Discuss a hypothetical problem to test analytical thinking and business understanding — metrics, funnels, growth, retention strategies, and analytical approaches.
5. **Behavioral interviews**: Standard “walk me through a project / a time when you XXX” to understand how candidates handle specific situations and if they are a cultural fit.
6. **Cross-functional interviews**: Data Scientist is a technical role, but it is also highly cross-functional, aiming to drive real business impact using data. Therefore, many data scientist interview loops today include a cross-functional interview round to chat with a business partner to assess the domain knowledge, communication skills, and stakeholder collaboration.
From the list above, you can see that data scientist interviews usually have a good mix of technical and non-technical evaluations. But with AI entering the game, some of these interviews will change significantly, while some will become even more important. Let’s break it down.

---

### II. How Interviews Will Shift in the Age of AI  

In my opinion, how the interview loops are going to change depends on two things: 1. Can AI handle the task quickly? 2. Does it tell how the candidate uses AI thoughtfully?  

#### Coding Interviews: Most Likely to Change First

What can AI do quickly? Simple coding tasks. Therefore, the **coding interview** is probably the first one to be impacted.  

Today’s coding interviews ask candidates to write SQL and Python code correctly. The SQL questions usually require simple joins, CTEs, aggregations, and window functions. And the Python questions could be straightforward data manipulation with pandas and numpy, or easy LeetCode-style questions. But let’s be honest, these interview questions can be solved by AI easily today. In [my article one year ago](https://yudong-94.github.io/personal-website/blog/LLMComparisonSQL/), I evaluated how ChatGPT, Claude, and Gemini perform in simple SQL tasks, and was impressed already by all three — Claude 3.5 Sonnet even got full points in my test.  

Let’s take one step back. For data scientists, the real coding challenge today comes from 1. Understand the data and locate the correct tables and fields; 2. Translate your data questions into the correct query/code. In other words, today’s coding interviews mostly test basic syntax, which might be fair for entry-level candidates, but have been failing to evaluate actual problem-solving for a long time, even without the evolution of AI. The fact that AI can answer them quickly only makes this round even more outdated.  

So, how can we make the coding interviews more meaningful? **I think, firstly, we should allow candidates to use AI tools like GitHub Copilot or Cursor during the coding interview to mimic the new work environment with AI**. I have seen this happening gradually in the industry. For example, [Canva introduced AI-assisted coding interviews recently](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/), and [Greenhouse also says](https://www.greenhouse.com/guidelines-for-using-ai-in-our-interviewing-process), “*We welcome transparent use of generative AI in the interview process for certain roles with the expectation that candidates can thoroughly explain the prompts they create and/or discuss in-depth the technical decisions they make.*” Even Meta is going to let candidates use AI during coding tests ([news](https://www.wired.com/story/meta-ai-job-interview-coding/)). I think allowing candidates to use AI is better than trying every means to prevent them from cheating with AI, as they will use (and are expected to use) AI at work anyway :).  

Meanwhile, instead of asking simple SQL/Python questions, I have a couple of ideas:  
1. Ideally, we could set up an environment with multiple documented tables and ask the candidates to do a live problem-solving session with the help of AI. Instead of asking questions like “write a query to calculate MAU since 2024”, ask more open-ended questions like “how would you investigate customer churn since 2024?”. The evaluation will not only be based on code accuracy, but also on how the candidates frame their analysis and interpret the results. And when the candidate interacts with the AI tool, how do they prompt, iterate, and evaluate the output. Though this does make interviewers’ lives harder — they will have to be very familiar with the datasets and be able to follow the candidates’ logic, ask follow-up questions, and assess the responses.
2. Alternatively, we can ask candidates to evaluate the AI outputs — this is probably easier to set up and less stressful and time-consuming than the above format. While AI can help with coding, it’s still humans’ responsibility to evaluate the output. Not every AI-generated code is correct, even if it runs without errors. The interviewer can describe what they are trying to do and show AI-generated code, then ask the candidates to identify if the logic is correct, if it ignores any edge cases, if there is any better alternatives, or if the code can be optimized further — this requires the candidate to fully understand how to translates between the business logic and the code. It is also easier to design a standard rubric with this problem setup.

#### Statistics and Machine Learning Interviews: Less Theory, More Context

Next, let’s talk about **statistics** and **machine learning interviews**. AI is a great teacher — it explains basic stats and machine learning concepts clearly and can help brainstorm different methodologies — try asking ChatGPT, “explain p-value to me like I am five”. However, knowing the theories doesn’t always mean applying the appropriate methods based on business scenarios. You can find a good example in my Google Data Science Agent evaluation article — it does a great job setting up a modeling framework with functional starter code, but it requires a clear problem statement and a clean dataset. Human expertise is also necessary for feature engineering, choosing the best domain-specific data science practices, and tuning the models. Keeping that in mind, I think statistics and machine learning interviews should **ask fewer theoretical questions or coding models from scratch, but integrate more with business case interviews to test if the candidates can apply theories to a business context**. So instead of asking isolated questions like “What’s the difference between Ridge and Lasso Regression?” or “How to calculate the sample size for an A/B test?”, present a real-world problem and observe how the candidates approach the questions analytically, if the proposed methods make sense, and if they communicate their ideas logically. It’s not like we no longer need the candidates to have solid stats and ML knowledge, but we will test the knowledge more seamlessly in the case discussion. For example, when going through a hypothetical fraud detection case, we can ask why the candidate proposes XGBoost over Random Forest, and if it is better to impute missing values in household income as the median or zero.  

The good news is we’ve already seen many of these technical + business case interviews in the industry. My prediction is that AI will make it even more predominant.  

#### Behavioral & Cross-functional Interviews: Mostly Unchanged, But With New Twists

For the remaining two interview types, **behavioral interviews** and **cross-functional interviews**, they will likely stay here. They evaluate the candidates’ soft skills, such as cross-functional collaboration, communication, conflict resolution, and ownership, as well as their domain knowledge. These are the things AI cannot replace. However, there could be some shifts in what questions people ask. Interviewers can add questions about the candidates’ past experience with AI tools to get more signal on how they use AI to boost productivity and solve problems. For example, a product manager might ask, “How can we use AI to improve customer onboarding?” These conversations can surface the candidates’ ability to identify AI use cases that drive real business value.  

#### Take-home Assignments: Still Controversial, But Useful

Besides these common interview formats, there is also a controversial one that comes up in data science interview loops from time to time — **Take-home assignments**. It is usually in the format of providing a dataset and asking the candidates to do an analysis or build a model. Sometimes there are guiding questions, sometimes not. Deliverables range from a Jupyter notebook to a polished slide deck.  

I know there are candidates who really hate it. It takes a lot of effort — though recruiters always say average candidates take about 4 hours, the actual time you spend is usually significantly longer, as you want to be comprehensive and showcase your best work. And what makes it worse is, the candidates may just end up being rejected without the opportunity to even talk to the team — how frustrating! Unsurprisingly, I heard from my team’s recruiter a while back that take-home assignment leads to a high drop-off rate in the hiring process (so we removed it).  

But take-home assignments do have value. It tests end-to-end skills from problem framing, coding, writing, to presentation. And the nature of working with your local environment with your preferred tools now means you can seek AI’s help to complete the assignment faster and better! Therefore, take-home assignments can easily evolve and become more common in this new era, with higher expectations for depth, interpretation, and originality. The challenge, though, is for hiring managers to come up with an assignment that AI cannot easily solve or will only generate the minimum acceptable solution. For example, a simple data manipulation task will not be appropriate, but an open-ended question that requires making assumptions based on domain knowledge, tradeoff discussion, and prioritization will work better. And a follow-up live interview is always helpful to validate the understanding.  

Now let’s summarise the traditional interview formats vs. the new formats under the AI era:  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_interview_with_ai.png" alt="traditional interview formats vs. the new formats under the AI era" width="600" height="400">
</div>

---

### III. What This Means for Candidates  

Above is my take on how data scientist interview loops will transform under the age of AI. However, these shifts may still take a while to happen across the industry.  

So, what should the candidates do to prepare themselves better ahead of time?  
* **Know when and how to use AI thoughtfully**. As companies start to allow the use of AI and even evaluate how you use AI during interviews, understanding how to use it thoughtfully becomes critical. Don’t just prompt and paste. You should understand what AI does well and where it falls short, and how to evaluate the outputs. Not to mention that AI is also a super helpful tool in interview preparation. It can help you understand the position better, set up a preparation plan, and do mock interviews — I can write a whole article on this (maybe next time).
* **Understand the business deeply**. Now that technical skills are getting easier with AI assistance, business understanding and domain knowledge become the key for a candidate to stand out. Therefore, everyone should collaborate more with stakeholders at work to develop their business knowledge. And when you prepare for interviews, spend time doing company research to understand its product — what would be the key metrics, how to grow the product further with data, and what should be the retention strategy.

Thanks for reading! If you’re a hiring manager, I’d love to hear how your team is adapting. And if you’re a candidate, I hope this helps you prepare smarter for the future of interviews.
