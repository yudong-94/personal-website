---
title: "How I Used ChatGPT to Land My Next Data Science Role"
date: 2025-11-15
categories:
  - blog
tags:
  - data science
  - career
header:
  teaser: /assets/images/article_covers/chatgpt_for_interview_cover.jpg
excerpt: "Practical AI hacks for every stage of the job search — with real prompts and examples."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/how-i-used-chatgpt-to-land-my-next-data-science-role/).  

---

**Practical AI hacks for every stage of the job search — with real prompts and examples**

In the past, I wrote about [how recent AI developments are changing data science interview loops](https://towardsdatascience.com/rethinking-data-science-interviews-in-the-age-of-ai/) from a hiring manager’s perspective.

I recently went through several interviews myself. Job hunting is always stressful. Being on the other side, I realized how much ChatGPT could streamline and accelerate the interview preparation process for data scientists.

Therefore, in this article, I will share my ChatGPT hacks for job search and interviews with real examples.

---

## Step 0 — Create a ChatGPT Project  

Before getting started, I highly recommend **creating a new [project](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) in ChatGPT to organize all the files and conversations**. Job search is never an easy and quick process — you will likely have separate chats for different positions. A ChatGPT project keeps everything in one independent folder and ensures persistent memories across all chats.  

For my setup, I uploaded my resume and past projects so that ChatGPT can better understand my background and make tailored recommendations.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_new_project.png" alt="Create a ChatGPT project and upload files (image by the author)" width="600" height="800">
</div>


My past projects doc is a collection of my best projects that can be used in my resume and interviews, written in the **R-STAR** structure. Here is one example:  

>**R(esult)**: Build an AI-based internal app that centralizes customer feedback with automated feedback classification and analysis. This is now a critical tool for PMs and Engineers to set the product development roadmap.
>
>**S(ituation)**: We have customer feedback scattered in 20+ different data sources (NPS, CSAT, other surveys, CX Cases, In-product feedback tool, Customer Calls, etc.). The hold lots of values but are not being shared and analyzed broadly and effectively.
>
>**T(ask)**: Consolidate all the data sources and close the feedback loop between Customer Support and Product teams.
>
>**A(ction)**: 1. Built data pipeline to integrate all these 20+ data sources into one source of truth dataset. 2. To uncover the topcs and trends, we tried traditional NLP models (BERT), but they took a long time and the output wasn’t quite stable. Then we switched to OpenAI API for classification and summarization — after a few rounds of prompt engineering, we achieved high accuracy within a week (70% label accuracy out of 11 categories). 3. Developed an automatic pipeline to process the new feedback with OpenAI API daily and collaborated with eng to set up an internal server and app to make the tool easily accessible to everyone.
>
>**R(esult)**: One stop shop for all customer feedback, facilitated roadmap prioritization. Won Hackathon ‘Customer Love’ award and All Hands cultural point shout out.

Once the documents were uploaded, I added a project-level instruction so ChatGPT could act as my personalized career coach. Here is my prompt:  

>I am applying for Data Scientist roles in the United States.
You are an expert career coach specializing in data science job search and interview preparation.
>
>Analyze my resume, portfolio, and past projects to fully understand my background, skills, and expertise.
>
>Your responsibilities include:
1. Job Search Support: Analyze job descriptions and identify skill or experience gaps.
2. Resume & Portfolio Refinement: Suggest targeted improvements and help tailor them to specific roles.
3. Interview Preparation: Create structured study and preparation plans for both technical and behavioral interviews.
4. Mock Interviews: Conduct realistic mock interviews with feedback and scoring.
>
>Please maintain a professional tone and always provide practical, detailed, and actionable guidance.

## Step 1 — Application  

### Analyze Job Descriptions and Customize Resume  

The job market today is very competitive. Therefore, it is essential to carefully read the job description and **customize your resume** accordingly. ChatGPT makes this process much faster.  

In the sections below, I will use the [Data Scientist, Platform and B2B Products](https://openai.com/careers/data-scientist-platform-and-b2b-products/) position at OpenAI as an example. Disclaimer — I did not really apply for this position, but feel it could be fun to use an OpenAI opening to better illustrate the ideas in this article :)  

The first step I took was to share the job description with ChatGPT and ask it to help me understand this role better, including its domain, data science use cases, and key skills. If you are not sure if a role is a good fit for your background, you can also ask ChatGPT to evaluate for you. For example, below I asked it to compare two different openings at OpenAI and make a recommendation.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_read_jd.pngchatgpt_for_interview_read_jd" alt="Analyze job description with ChatGPT (Image by the author)" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_compare_jd.png" alt="Compare openings with ChatGPT (Image by the author)" width="300" height="400">
</div>


Once you have a good understanding of the position and have made up your mind to apply, ChatGPT can quickly update your resume based on the domain and required skills. In the screenshot below, it generated a customized version of my resume and highlighted the most relevant experiences. You can also add more specific instructions on what and how you want it to change and keep iterating with ChatGPT.  

One thing to note, though — **I did spot some obvious mistakes**, such as the reversed title sequence under my employer's name. Make sure you don’t just copy and paste everything it writes, but read through your new resume line by line and correct any wrong or hallucinated contents :)  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_update_resume.png" alt="Customize your resume with ChatGPT (image by the author)" width="600" height="800">
</div>


In the job application process, you can also use ChatGPT to update your LinkedIn profile, edit cover letters, and draft referral request messages.  

## Step 2 — Interview Preparation  

Now, let’s assume your applications got some traction with the help of ChatGPT. Congratulations! Time to get ready for your interviews.  

### 1. Understand the Business Context  

I don’t usually go straight to mock interviews. Instead, for every position I interviewed for, my first step of interview preparation was always to **research the products and business models, think about key metrics, and come up with data science use cases**. ChatGPT can be the perfect brainstorming partner here. Let’s see an example below:

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_company_research.png" alt="Company research with ChatGPT (image by the author)" width="600" height="800">
</div>


In this case, ChatGPT generated a pretty comprehensive and detailed table by itself, summarising lifecycle stages, product focus, key metrics, and data science use cases. That being said, **I feel it is more helpful to take a stab yourself first**. For example, when I was preparing for my DoorDash interviews (my current employer), I drew a mind map and asked ChatGPT to refine it further. This hybrid approach helped me to enhance my understanding and spot gaps.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_brainstorm.png" alt="Brainstorm metrics and data science use cases (image by the author)" width="600" height="800">
</div>


### 2. Product Case Interview Preparation  

Product case interviews have been increasingly important for Data Science roles, especially given AI’s strong capability in coding. As a result, I usually spend at least 50% of my interview preparation time here. ChatGPT can help you find and create role-specific sample cases and conduct mock interviews with you.  

In the screenshot below, I simply described the common topics in the product case round with question examples. The generated case interview questions followed the pattern pretty well, while tailoring to the business context of this Platform and B2B Products DS role.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_case_questions.png" alt="Product case question generation with ChatGPT (image by the author)" width="600" height="800">
</div>


With these valuable question prompts, next, you can conduct mock interviews with ChatGPT. A mock interview can be a very expensive service. For example, [DataInterview](https://www.datainterview.com/coaching) charges $247 for a one-hour mock interview, and an [InterviewQuery](https://www.interviewquery.com/pricing) premium subscription, which includes mock interview service, costs $79 per month. Of course, practicing with real people has its benefits, but ChatGPT is free (assuming you are already a subscriber) and customizes to your background!  

I like practicing in real-time with the [voice mode](https://chatgpt.com/features/voice/) to simulate a real interview setting — I asked ChatGPT to act as the interviewer, evaluating my responses and asking follow-up questions. Below is a screenshot of my mock interview when I was preparing for DoorDash's onsite.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_voice_mode.png" alt="Mock interview in ChatGPT voice mode (image by the author)" width="600" height="800">
</div>


Mock interviews with ChatGPT could run into two challenges, though:  
1. The question it generates might not always be suitable for the role you are interviewing for. In this case, you can try to find real interview questions (you can likely find some past interview questions for large companies online), or come up with good questions yourself, or give ChatGPT more instructions on what a good case question looks like and ask it to learn and iterate.  
2. Another thing I noticed is that ChatGPT tends to react very positively (“you did great in this question”, “that is a great answer”). This helps build confidence in a way, but if you notice this happening too often, I recommend you be more explicit in your instructions — asking ChatGPT to act like the interviewer, evaluate this and that, and give a comprehensive evaluation of the response.  


### 3. Behavioral Interview Preparation  

ChatGPT is equally powerful for behavioral rounds. Except for conducting mock interviews, it can match your past projects to common behavioral question topics, such as handling conflicts, leadership, cross-functional collaboration, and prioritization, and refine the storyline for concise and compelling interview responses.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_bq.png" alt="Behavioral interview preparation with ChatGPT (image by the author)" width="600" height="800">
</div>


### 4. Create Interview Preparation Plan  

ChatGPT is known as a good planning assistant. Seeing everything it can do above, you can provide your timeline and focus areas to get a concrete interview preparation plan and a daily checklist.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/chatgpt_for_interview_plan.png" alt="ChatGPT generates an interview preparation plan (image by the author)" width="600" height="800">
</div>


## Step 3 —After Interviews: Offer Evaluation and Negotiation  

The last stage of the job search process is the offer evaluation and negotiation. I know you are very excited to receive the offer, but don’t just accept it as-is. According to a [study](https://resources.careerbuilder.com/news-research/73-of-employers-would-negotiate-salary-55-of-workers-don-t-ask), **73% of U.S. employers say they are open to negotiating salary on initial offers, but 55% of candidates don’t ask for more**. As a data professional, I am sure you understand the power of compounding — even a moderate increase compounds over time through raises, bonuses, and equity.  

ChatGPT can help you research similar offers in the industry, compare compensation packages, draft recruiter replies, and prepare negotiation scripts.  

---

## Final Thoughts  

The job search process can feel overwhelming, but tools like ChatGPT turn it into a more structured journey. For me, ChatGPT acted as my personal career coach, helping me stay organized, efficient, and confident.  

Here are the key takeaways:  

* **Before getting started**: Use a ChatGPT Project to centralize your job search materials and context. Upload your resume and past projects so ChatGPT can tailor advice.  
* **Job application**: Let ChatGPT analyze job descriptions and customize your resume. Don’t skip the human review — always fact-check your content.
Interview preparation: Brainstorm business metrics and data science use cases with ChatGPT and conduct mock interviews using voice mode to simulate conversation.  
* **Offer evaluation**: Ask ChatGPT to research comparable offers and draft negotiation strategies.  

If you are thinking or in the middle of job hunting, I hope my tips help you make full use of these AI tools at every stage and facilitate your career!
