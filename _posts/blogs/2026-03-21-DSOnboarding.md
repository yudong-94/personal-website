---
title: "Your First 90 Days as a Data Scientist"
date: 2026-03-21
categories:
  - blog
tags:
  - data science
  - career
header:
  teaser: /assets/images/article_covers/ds_onboarding.jpg
excerpt: "A practical onboarding checklist for building trust, business fluency, and data intuition."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/your-first-90-days-as-a-data-scientist/).  

---
I joined a new company about five months ago. This is my first time starting at a company as a Data Science Manager, which makes onboarding especially challenging. However, it has also been one of the fastest-growing periods of my career.

The first three months at any new job are fundamentally a building phase — building connections, domain understanding, and data knowledge — and a smooth onboarding sets the foundation for later success. Therefore, in this article, I’ll share what mattered most in the beginning months and my checklist for any data science onboarding.

---

### I. Build Connections  

Before anything else, let me start with building connections. When I was at school, I pictured data scientists as people spending all day long heads-down writing code and building models. However, as I became more senior, I realized that data scientists make real impacts by embedding themselves deeply in the business, using data to identify opportunities, and driving business decisions. This is especially true today with tighter DS headcount and AI automating basic coding and analysis workflows.  

Therefore, building connections and earning a seat at the table should be a top priority during onboarding. This includes:  

* **Frequent onboarding sessions with your manager and onboarding buddy**. These are the people who best understand your future scope, expectations, and priorities. In my case, my manager was my onboarding buddy, and we met almost daily during the first two weeks. I always came with a prepared list of questions I encountered during onboarding.
* **Set up meet-and-greet calls with cross-functional partners**. Here is the agenda I usually follow in those calls:
  - 1. Personal introductions
  - 2. Their focus area and top priorities
  - 3. How can my team best support them
  - 4. Any onboarding advice or “things I should know”
I especially like the last question as it consistently provides great insights. Five years ago, when I onboarded at Brex, I asked the same question and summarised the responses into categories [here](https://yudong-94.github.io/personal-website/blog/AdviceOnStartingANewJob/). The best I got this time is “Don’t be afraid to ask dumb questions. Play the new-hire card as much as possible in the first three months.”
* For those key partners, **set up weekly/bi-weekly 1:1s and get yourself added to recurring project meetings**. You may not contribute much at first, but just listening in and collecting the context and questions is helpful.
* If you are onboarding as a manager like me, you should **start talking to your direct reports early**. During onboarding, I aim to learn three things from my direct reports: 1. Their projects and challenges, 2. Their expectation of me as a manager, 3. Their career goals. The first helps me ramp up on the area. The latter two are critical for establishing trust and a collaborative working relationship early on.  

### II. Build Domain Context  

Data scientists succeed when they understand the business well enough to influence decisions — not just analyze outcomes. Therefore, another priority during onboarding is to build your domain knowledge. Common strategies include **talking to people, reading docs, searching Slack, and asking a lot of questions**.  

I usually start with conversations to identify key business context and projects. Then I dig into relevant docs in Google Drive or Confluence, and read Slack messages in project channels. I also compile the questions after reading the docs, and ask them in 1:1s.  

However, one challenge I ran into is digging into the rabbit hole of docs. Each document leads to more documents with numerous unfamiliar metrics, acronym names, and projects. This is especially challenging as a manager — if each of your team members has 3 projects, then 5 people means 15 projects to catch up. At one point, my browser’s “To Read” tab group had over 30 tabs open.  

Luckily, AI tools are here to rescue. While reading all the docs one by one is helpful to get a detailed understanding, AI tools are great to provide a holistic view and connect the dots. For example,  
* Many companies use Glean, which has access to internal docs and Slack. I often chat with Glean, asking questions like “How is metric X calculated?”, “Provide a summary of the project Y, including the goal, timeline, findings, and conclusion.” It links to the document sources, so I can still dive deeper quickly if needed.
* Another tool I tried is NotebookLM. I shared the docs on a specific topic with it, and asked it to generate summaries and mind maps for me to collect my thoughts in a more organized way. It can also create podcasts, which are sometimes more digestible than reading docs.
* Other AI tools like ChatGPT can also connect to internal docs and serve a similar purpose.  

### III. Build Data Knowledge  

Building data knowledge is as important as building domain knowledge for data scientists. As a front-line manager, I hold myself to a simple standard: I should be able to do hands-on data work well enough to provide practical, credible guidance to my team.  

Here is what helped me ramp up quickly:  
1. **Set up tech stack in week one**: I recommend setting up the tech stack and developer environment early. Why? Access issues, permissions, and weird environment problems always take longer than expected. The earlier you have everything set up, the sooner you can start playing with the data.
2. **Make full use of AI-assisted data tools**: Every tech company is integrating AI into its data workflows. For example, I have my Cursor connected to Snowflake with internal data knowledge and context to generate SQL queries and analysis grounded in our data. Though the generated queries are not yet 100% accurate, the tables, joins, and past queries it points me to serve as excellent starting points. It won’t replace your technical judgment, but it dramatically reduces the time to first insight.
3. **Understand key metrics and their relationships**: Data knowledge not only means being able to access and query the data, but understand the business from a data lens. I usually start with weekly business reviews to find the core metrics and their trend. This is also a great way to contextualize the metrics and have an idea of what “normal” looks like. I’ve found this incredibly helpful when gut-checking analyses and experiment results later.
4. **Get your hands dirty**: Nothing enforces your data understanding more than doing some hands-on work. A good onboarding program usually includes a mini starter project. Even as a manager, I did some IC work during my onboarding, including opportunity sizing for the planning cycle, designing and analyzing multiple experiments, and diagnosing and forecasting metrics movement. These projects accelerated my learning far more than passive reading.  

### IV. Start Small and Contribute Early  

While onboarding is primarily about learning, I strongly recommend starting small and contributing early. Early contributions signal ownership and build trust — often faster than waiting for a “perfect” project. Here are some concrete ways:  

* **Improve the onboarding documentation**: As you go through the onboarding doc, you will run into random technical issues, notice broken links, or find outdated instructions. Not just overcoming them yourself, but enhancing the onboarding doc is a great way to show that you are a team player and want to make onboarding better for future hires.
* **Build documentation**: No company has perfect documentation — from my own experience and chatting with my friends, most data teams face the challenge of outdated or missing documentation. As you are onboarding and not busy with projects yet, it is the perfect time to help fill in those gaps. For example, I built a project directory for my team to centralize past and ongoing projects with key findings and clear points of contact. I also created a collection of metrics heuristics, summarising the causal relationship between different metrics we learned from past experiments and analyses. Note that all these documents also become valuable context for AI agents, improving the quality and relevance of AI-generated outputs.
* **Suggest process improvements**: Every data team operates differently, with pros and cons. Joining a new team means you bring a fresh perspective on team processes and might spot opportunities to improve efficiency. Thoughtful suggestions based on your past experience are super valuable.  

---

In my opinion, a successful onboarding aims to establish **cross-functional alignment, business fluency, and data intuition**.

Here is my onboarding checklist:

1. Week 1–2: Foundations  
  - Meet key business partners
  - Get yourself added to core cross-functional meetings
  - Understand team focus and priorities at a high-level
  - Set up tech stack, access, and permissions
  - Write your first line of code
  - Read documentation and ask questions
2. Week 2–6: Get your hands dirty  
  - Deep dive into team OKR and commonly used data tables
  - Deep dive into your focus area (more docs and questions)
  - Complete a starter project end-to-end
  - Make early contributions: Update outdated info, build one piece of documentation, or suggest one process improvement, etc.
3. Week 6–12: Ownership  
  - Be able to speak up in cross-functional meetings and provide your data-informed point of view
  - Build trust as the “go-to” person for your domain

Onboarding looks very different across companies, roles, and seniority levels. What helped you ramp up faster in your first 90 days, or what do you wish you had done differently? Share your onboarding tips in the comments so others can learn from them too.
