---
title: "How AI Is Rewriting the Day-to-Day of Data Scientists"
date: 2025-06-03
categories:
  - blog
tags:
  - data science
  - llm
header:
  teaser: /assets/images/article_covers/ai_for_ds_cover.jpg
excerpt: "From eliminating low-value tasks to accelerating high-impact projects, here’s how AI is reshaping the data science workflow."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/how-ai-is-rewriting-the-day-to-day-of-data-scientists/).  

---

**From eliminating low-value tasks to accelerating high-impact projects, here’s how AI is reshaping the data science workflow**

In my past articles, I have explored and compared many AI tools, for example, [Google's Data Science Agent](https://yudong-94.github.io/personal-website/blog/GoogleDataScienceAgent/), [ChatGPT vs. Claude vs. Gemini for Data Science](https://yudong-94.github.io/personal-website/blog/LLMComparisonSQL/), [DeepSeek V3](https://yudong-94.github.io/personal-website/blog/DeekSeepDSEvaluation/), etc. However, this is only a small subset of all the AI tools available for data science. Just to name a few that I used at work:
* **OpenAI API**: I use it to categorize and summarize customer feedback and surface product pain points (see [my tutorial article](https://yudong-94.github.io/personal-website/blog/TextAnalyticsWithGPT/)).
* **ChatGPT and Gemini**: They help me draft Slack messages and emails, write analysis reports, and even performance reviews.
* [**Glean AI**](https://www.glean.com/): I used Glean AI to find answers across internal documentation and communications quickly.
* [**Cursor**](https://www.cursor.com/en) and [**Copilot**](https://github.com/features/copilot): I enjoy just pressing tab-tab to auto-complete code and comments.
* **Hex Magic**: I use Hex for collaborative data notebooks at work. They also offer a feature called [Hex Magic](https://hex.tech/product/magic-ai/) to write code and fix bugs using conversational AI.
* [**Snowflake Cortex**](https://www.snowflake.com/en/product/features/cortex/): Cortex AI allows users to call LLM endpoints, build RAG and text-to-SQL services using data in Snowflake.


I am sure you can add a lot more to this list, and new AI tools are being launched every day. It is almost impossible to get a complete list at this point. Therefore, in this article, I want to take one step back and focus on a bigger question: **what do we really need as data professionals, and how AI can help.**  

In the section below, I will focus on two main directions - eliminating low-value tasks and accelerating high-value work.  


---

### I. Eliminating Low-Value Tasks  

I became a data scientist because I truly enjoy uncovering business insights from complex data and driving business decisions. However, having worked in the industry for over seven years now, I have to admit that not all the work is as exciting as I had hoped. Before conducting advanced analyses or building machine learning models, there are many low-value work streams that are unavoidable daily - and in many cases, it is because we don't have the right tooling to empower our stakeholders for self-serve analytics. Let's look at where we are today and the ideal state:  

**Current state: We work as data interpreters and gatekeepers (sometimes "SQL monkeys")**

* **Simple data pull requests** come to me and my team on Slack every week asking, "What was the GMV last month?" "Can you pull the list of customers who meet these criteria?" "Can you help me fill in this number on the deck that I need to present tomorrow?"  
* **BI tools do not support self-service use cases well**. We adopted BI tools like Looker and Tableau so stakeholders can explore the data and monitor the metrics easily. But the reality is that there is always a trade-off between simplicity and self-servability. Sometimes we make the dashboards easy to understand with a few metrics, but they can only fulfill a few use cases. Meanwhile, if we make the tool very customizable with the capability to explore the metrics and underlying data freely, stakeholders could find the tool confusing and lack the confidence to use it, and in the worst case, the data is pulled and interpreted in the wrong way.  
* **Documentation is sparse or outdated**. This is a common situation, but could be caused by different reasons - maybe we move fast and focus on delivering results, or there is no great data documentation and governance policies in place. As a result, tribal knowledge becomes the bottleneck for people outside of the data team to use the data.  

**Ideal state: Empower stakeholders to self-serve so we can minimize low-value work**

* Stakeholders can do simple data pulls and answer basic data questions easily and confidently.
* Data teams spend less time on repetitive reporting or one-off basic queries.
* Dashboards are discoverable, interpretable, and actionable without hand-holding.

So, to get closer to the ideal state, what role can AI play here? From what I have observed, these are the common directions AI tools are going to close the gap:  

1. **Query data with natural language (Text-to-SQL)**: One way to lower the technical barrier is to enable stakeholders to query the data with natural language. There are lots of Text-to-SQL efforts in the industry:  
- For example, **Snowflake** is one company that has made lots of progress in [Text2SQL models](https://www.snowflake.com/en/engineering-blog/arctic-text2sql-excot-sql-generation-accuracy/) and started integrating the capability into its product.
Many companies (including mine) also explored in-house Text2SQL solutions. For example, **Uber** shared their journey with [Uber's QueryGPT](https://www.uber.com/blog/query-gpt/) to make data querying more accessible for their Operations team. This article explained in detail how Uber designed a multi-agent architecture for query generation. Meanwhile, it also surfaced major challenges in this area, including accurately interpreting user intent, handling large table schemas, and avoiding hallucinations, etc.  
- Honestly, to make Text-to-SQL work, there is a very high bar as you have to make the query accurate - even if the tool fails just once, it could ruin the trust and eventually stakeholders will come back to you to validate the queries (then you need to read+rewrite the queries, which almost double the work 🙁). It also has a strict prerequisite of a well-documented and clean database. So far, I haven't found a Text-to-SQL model or tool that works perfectly. I only see it achievable when you are querying from a very small subset of well-documented core datasets for specific and standardized use cases, but it is very hard to scale to all the available data and different business scenarios.  
- But of course, given the large amount of investment in this area and rapid development in AI, I am sure we will get closer and closer to accurate and scalable Text-to-SQL solutions.  

2. **Chat-based BI assistant**: Another common area to improve stakeholders' experience with BI tools is the chat-based BI assistant. This actually takes one step further than Text-to-SQL - Instead of generating a SQL query based on a user prompt, it responds in the format of a visualization plus text summary.  
- [**Gemini in Looker**](https://cloud.google.com/gemini/docs/looker/overview) is an example here. Looker is owned by Google, so it is very natural for them to integrate with Gemini. Another advantage for Looker to build their AI feature is that data fields are already documented in the LookML semantic layer, with common joins defined and popular metrics built in dashboards. Therefore, it has lots of great data to learn from. Gemini allows users to adjust Looker dashboards, ask questions about the data, and even build custom data agents for Conversational Analytics. Though based on my limited experimentation with the tool, it times out often and fails to answer simple questions sometimes. Let me know if you have a different experience and have made it work…  
- Tableau also launched a similar feature, [**Tableau AI**](https://www.tableau.com/products/artificial-intelligence). I haven't used it myself, but based on the demo, it helps the data team to prepare data and make dashboards quickly using natural language, and summarise data insights into "Tableau Pulse" for stakeholders to easily spot metric changes and abnormal trends.  
- Similar to the challenges with Text-to-SQL, accuracy is always a top concern when it comes to chat-based BI assistants. How reliable are the visualizations they generated? Do they have the business context behind the metrics and dashboards to interpret them correctly 🤔? If you are not confident with these questions, you likely won't feel comfortable with your stakeholders using them.  

3. **Data Catalog Tools**: AI can also help with the challenge of sparse or outdated data documentation.  
- During one internal hackathon, I remember one project from our data engineers was to use LLM to increase table documentation coverage. AI is able to read the codebase and describe the columns accordingly with high accuracy in most cases, so it can help improve documentation quickly with limited human validation and adjustments.
- Similarly, when my team creates new tables, we have started to ask Cursor to write the table documentation YAML files to save us time with high-quality output.
- There are also lots of data catalogs and governance tools that have been integrated with AI. When I google "ai data catalog", I see the logos of data catalog tools like Atlan, Alation, Collibra, Informatica, etc (disclaimer: I have used none of them). This is clearly an industry trend.


---

### II. Accelerating high-value work
Now that we've talked about how AI could help with eliminating low-value tasks, let's discuss how it can accelerate high-value data projects. Here, high-value work refers to data projects that combine technical excellence with business context, and drive meaningful impact through cross-functional collaboration. For example, a deep dive analysis that understands product usage patterns and leads to product changes, or a churn prediction model to identify churn-risk customers and results in churn-prevention initiatives. Let's compare the current state and the ideal future:  

**Current state: Productivity bottlenecks exist in everyday workflows**  

* **EDA is time-consuming**. This step is critical to get an initial understanding of the data, but it could take a long time to conduct all the univariate and multivariate analyses.
* **Time lost to coding and debugging**. Let's be honest - no one can remember all the numpy and pandas syntax and sklearn model parameters. We constantly need to look up documentation while coding.
* **Rich unstructured data is not fully utilized**. Business generates lots of text data every day from surveys, support tickets, and reviews. But how to extract insights scalably remains a challenge.

**Ideal state: Data scientists focus on deep thinking, not syntax**  

* Writing code feels faster without the interruption to look up syntax.
* Analysts spend more time interpreting results, less time wrangling data.
* Unstructured data is no longer a blocker and can be quickly analyzed.

Seeing the ideal state, I am sure you already have some AI tool candidates in mind. Let's see how AI can influence or is already making a difference:  

1. **AI coding and debugging assistants**. I think this is by far the most adopted type of AI tool for anyone who codes. And we are already seeing it iterating.
- When LLM chatbots like **ChatGPT** and **Claude** came out, engineers realized they could just throw their syntax questions or error messages to the chatbot with high-accuracy answers. This is still an interruption to the coding workflow, but much better than clicking through a dozen StackOverflow tabs - this already feels like last century.
- Later, we see more and more integrated AI coding tools popping up - [**GitHub Copilot**](https://github.com/features/copilot) and [**Cursor**](https://www.cursor.com/en) integrate with your code editor and can read through your codebase to proactively suggest code completions and debug issues inside your IDE.
- As I briefly mentioned at the beginning, data tools like [**Snowflake**](https://www.snowflake.com/en/product/features/cortex/) and [**Hex**](https://hex.tech/product/magic-ai/) also started to embed AI coding assistants to help data analysts and data scientists write code easily.

2. **AI for EDA and analysis**. This is somewhat similar to the Chat-based BI assistant tools I mentioned above, but their goal is more ambitious - they start with the raw datasets and aim to automate the whole analysis cycle of data cleaning, pre-processing, exploratory analysis, and sometimes even modeling. These are the tools usually advertised as "replacing data analysts" (but are they?).  
- [**Google Data Science Agent**](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/) is a very impressive new tool that can generate a whole Jupyter Notebook with a simple prompt. I recently wrote an [article](https://yudong-94.github.io/personal-website/blog/GoogleDataScienceAgent/) showing what it can do and what it cannot. In short, it can quickly spin up a well-structured and functioning Jupyter Notebook based on a customizable execution plan. However, it is missing the capabilities of modifying the Jupyter Notebook based on follow-up questions, still requires someone with solid data science knowledge to audit the methods and make manual iterations, and needs a clear data problem statement with clean and well-documented datasets. Therefore, I view it as a great tool to free us some time on starter code, instead of threatening our jobs.   
- [**ChatGPT's Data Analyst tool**](https://chatgpt.com/g/g-HMNcP6w7d-data-analyst) can also be categorized under this area. It allows users to upload a dataset and chat with it to get their analysis done, visualizations generated, and questions answered. You can find my prior article discussing its capabilities [here](https://yudong-94.github.io/personal-website/blog/GoogleDataScienceAgent/). It also faces similar challenges and works better as an EDA helper instead of replacing data analysts.  

3. **Easy-to-use and scalable NLP capabilities**. LLM is great at conversations. Therefore, NLP is made exponentially easier with LLM today.  
- My company hosts an internal hackathon every year. I remember my hackathon project three years ago was to try BERT and other traditional topic modeling methods to analyze NPS survey responses, which was fun but honestly very hard to make it accurate and meaningful for the business. Then two years ago, during the hackathon, we tried **OpenAI API** to categorize and summarise those same feedback data - it worked like magic as you can do high-accuracy topic modeling, sentiment analysis, feedback categorization all just in one API call, and the outputs well fit into our business context based on the system prompt. We later built an internal pipeline that scaled easily to text data across survey responses, support tickets, Sales calls, user research notes, etc., and it has become the centralized customer feedback hub and informed our product roadmap. You can find more in [this tech blog](https://medium.com/brexeng/brexs-ai-powered-engine-for-identifying-customer-insights-72aadeb62e8e).
- There are also lots of new companies building packaged AI customer feedback analysis tools, product review analysis tools, customer service assistant tools, etc. The ideas are all the same - utilizing the advantage of how LLM can understand text context and make conversations to create specialized AI agents in text analytics.

---

### Conclusion  

It is easy to get caught up chasing the latest AI tools. But at the end of the day, what matters most is using AI to eliminate what slows us down and accelerate what moves us forward. The key is to stay pragmatic: adopt what works today, stay curious about what's emerging, and never lose sight of the core purpose of data science - to drive better decisions through better understanding.
