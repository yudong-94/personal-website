---
title: "From Data Scientist to Data Manager: My First 3 Months Leading a Team"
date: 2024-11-26
categories:
  - blog
tags:
  - data science
  - career
---

**Reflections on moving from hands-on work to mentoring and leading**

This is the 7th year in my data science career, a journey filled with dashboards, metrics, analyses, and models. But in August, I stepped into a new territory: becoming a people manager for the first time. To be honest, whenever asked about my career goal in the past, I always said I preferred staying on the IC track. I loved the technical challenges and owning projects end-to-end. However, when this opportunity came up, I decided to give it a shot. After all, you don’t know if something is right for you until you try.

In this article, I will share my initial experience as a manager — what has changed, what I’ve enjoyed, and what’s been challenging. If you are debating between the IC and people management path, I hope it will help shed some light.

---

### My path to management  

To set the stage, let me share how I transitioned to a people manager. When I first joined the team four years ago, everyone on the team was a **‘full-stack’ data scientist** — we each supported a specific domain and owned everything from building data pipelines, defining business metrics, and dashboarding, to analysis, experimentation, and modeling. This framework worked well for a startup. However, with the company becoming more mature and the team growing, we started to see the limitations: team members had varying preferences over data engineering vs. data analytics vs. data science work, but we were all required to do a bit of everything; Stakeholders often evaluated us based on the dashboards or reports we delivered, but did not realize how much effort we needed to put into building the underlying data pipeline; It was hard to standardize things like data engineering best practices as it was only one part of everyone’s role.

As a result, late last year, we restructured the team into three sub-teams: Data Engineers, Data Analysts, and Data Scientists. This change clarified responsibility and allowed for deeper expertise in each stage of the data cycle. I was then a Senior Data Scientist on the DS team. But as the data org grew, in August, I was offered the opportunity to manage the Data Analysts team, focusing on generating source-of-truth metrics reporting and actionable data insights. As I mentioned above, **I decided to embrace the challenge and experience the people manager life.**

---

### What has changed?  

#### 1. My meeting time doubled  

The first change I noticed is how much my meeting time has increased… Let me show you some numbers: when I was an IC, my average meeting time was about 7 hours per week, which means I had at least 80% of the time to focus on my projects. However, in the past three months, my average meeting time was roughly 14 hours per week, with one week exceeding 18 hours, more than doubling my prior meeting time.

So where does all this time go? Here is the breakdown:
1. **Regular meetings with the team (~5 hours)**. I host a weekly team meeting for sprint planning, team events, and discussions. I also have weekly 1:1s and monthly growth check-ins with everyone on the team, helping me understand their projects and growth opportunities, and serving as a two-way feedback channel. And of course, I have 1:1 scheduled with my manager and managers on the DE and DS teams to align priorities and collaborate effectively.
2. **Regular cross-functional meetings (~3 hours)**. The data analytics team works closely with stakeholders to help them track key metrics and conduct analysis. Therefore, it is critical to have regular meetings with stakeholders to take new requests and present findings. While I encourage my team to lead these discussions, I often attend to understand the team's focus, provide support, clarify priorities, or push back when needed.
3. **Project syncs and ad-hoc meetings**. There are often projects that involve multiple teams or span multiple sprints. In that case, project sync meetings are unavoidable. I attend those meetings to align on the project scope and progress. I also always make myself available for ad-hoc meetings, when my team wants to review their projects or brainstorm analysis ideas.
Do I like meetings? Unfortunately no, as I am an introvert. I’ve also found my days to be more scattered as I only have 30-minute blocks here and there between the meetings. However, these conversations are crucial for me to always be on the same page with my team.

#### 2. More mentoring and coaching  

When I was an IC, success meant delivering high-quality projects. However, as a manager, my success comes from ensuring my team has everything they need to deliver their projects. Therefore, management comes with a lot of mentoring and coaching.

The monthly growth check-in meetings are the perfect venue for me to understand what my team is missing and what areas they want to grow. Based on their feedback, I host monthly L&D sessions on topics like text analytics with LLM, A/B Testing 101, and (up next) Causal Inference 101.

Of course, applying a skill in real projects is the best way to master it. Therefore, I try my best to review my team’s projects timely and brainstorm analysis ideas with them. It might be a small piece of advice every time, for example, how to optimize a query they wrote, how to make a visualization more user-friendly, or how to better format an analysis report (you can find all of them in my past articles as my writing ideas are always inspired by real work). However, I believe these small but consistent improvements help them become a better data analyst every day.

Mentoring and coaching have been among the most fulfilling aspects of becoming a manager — I feel deeply rewarded when I see people grow with my help.

#### 3. Overseeing more projects with a broader scope  

As an IC, I focused on projects for specific domains like Risk, Operations, CX, Product, Implementation, etc. Now, as a manager, my scope is essentially the whole company…

We have data analysts assigned to different organizations across the company. Therefore, I had to learn new functions like Sales and Marketing quickly to better support them. At first, I was a bit worried if I would be helpful enough given my limited context there. I eventually bridged the gap by reading existing documentation, key dashboards, and past analyses, and by diving into the ongoing projects. One lesson I learned is that the manager-report relationship is not just one-way coaching, but a mutual learning experience. My direct reports are my best teachers when it comes to learning domain knowledge, and I trust their judgment in scoping their work.

This increased scope also helps me zoom out from single projects, and see the big picture. I’ve started noticing connections between projects across domains as they serve the same company goal. This benefits me a lot when I need to prioritize projects for my team and make sure they are aware of similar initiatives supported by each other.

On the other hand, this change also means less time for me to do hands-on projects. Though I still carve out up to 50% of my capacity for IC work (given the limited resources on the team), the time I could spend on diving into new methodologies is now rare, and that is the piece I truly miss.

#### 4. Visibility into the behind-the-scenes work  

Another very positive change for me is that I now have more visibility into what happens behind the scenes. Here are some examples:

* **Process optimization**: As an IC, I just followed the established process by my manager without much thought, no matter if it was adopting a new sprint planning process, building a team hub in Confluence, or following a certain doc format. However, as a manager, I now constantly think about how to improve the team productivity through process improvements. For example, several people on the team mentioned they got ad-hoc requests all over the place, from Slack direct messages, JIRA tickets, ad-hoc meetings, emails, etc. To improve the requests intake process, I suggested centralizing all the requests in specialized Slack channels like #gtm-data-help or #ops-data-help using a request form, and always asking stakeholders to post their requests there. This process helped the team to better manage the workload and helped the stakeholders to better format their requests while seeing all the other ongoing data tasks in their domain.
* **Hiring**: I’ve successfully hired two people since becoming a manager. In the past, I’ve only been involved in the hiring process as an interviewer. But being a hiring manager is a totally different story — I needed to prepare the job description, align with recruiters on the candidate profile, design the interview loops, review resumes, conduct interviews, participate in every debrief, and eventually make hiring decisions. This is much more effort than what I would have expected. But I also find it very rewarding to grow my team.
* **Performance review**: I recently completed my first performance review — it is not the critical year-end review that decides promotion and compensation changes, but a smaller quarterly review — but it is still something very new to me. To ensure the performance review never surprises anyone, I constantly use the weekly 1:1s and monthly growth check-ins to align expectations and collect feedback. Therefore, doing the performance review is more or less celebrating the great work they’ve done in the past quarter and setting goals for the next quarter. However, doing this process myself gives me more insights into how daily work translates into ratings.

---

### How do I like my new role?  

With all the changes above, how do I like my new role?

On the positive side, I enjoy helping people grow. It is very fulfilling to pay forward the mentorship and guidance I have received in my career. The expanded scope also gives me valuable insights into how businesses run and how to better align data projects with company goals.

On the flip side, I do miss the IC time of doing hands-on data science work, owning projects end-to-end, and diving into technical details. Sitting in meetings all day is exhaustive and poses a challenge to centralize focus time.

However, I am absolutely enjoying the challenge so far. Whether I stick with management long-term or return to the IC track, this experience is teaching me invaluable lessons that will benefit my career for years.
