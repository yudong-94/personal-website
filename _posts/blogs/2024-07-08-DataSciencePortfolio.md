---
title: "Building a Standout Data Science Portfolio: A Comprehensive Guide"
date: 2024-07-08
categories:
  - blog
tags:
  - data science
  - analysis
  - website
  - coding
  - career
---

### Learn how to create an impactful data science portfolio that showcases your skills and attracts potential employers

#### Context

I started [my data science portfolio website](https://yudong-94.github.io/personal-website/) in 2018 when I was fresh out of school. Unsurprisingly, I set it up, hoping it could help my job search and career development. Six years later, I'm proud of the progress and consistency in updating it. My portfolio has become a rich repository of my journey, projects, and insights.  
Having a data science portfolio helps you document your learnings, reflect on your career, and engage with the data science community. It's also invaluable for job searches, showcasing your skills and projects in greater depth than a traditional resume.  
In this article, I will discuss how to set up a data science portfolio, its content strategy, and what makes a good portfolio. If you've considered this idea but don't know where to start, this article is for you.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/portfolio_screenshot.png" alt="Screenshot of My Data Science Portfolio Website" width="600" height="400">
</div>

---

#### Set Up Your Portfolio

There are multiple ways to set up your data science portfolio. Below are the five most common options with their pros and cons.  

##### Option 1: GitHub

First, let me clarify, you don't need a personal website to have an amazing data science portfolio. Setting up a website and maintaining it takes significant time. If you don't have a website already and are in the job-hunting process, you should think twice and do your cost-benefit analysis. Data science interviews these days cover a broad range of topics, from SQL, Python, machine learning, and deep learning, to statistics, causal inference, product cases, and behavioral questions. Therefore, preparing for the interviews is already time-consuming. Prioritize your time wisely and start with the skills that you need to enhance the most or that your target companies require the most.  
If you just need a central place to showcase your technical projects, GitHub is the easiest and probably the most popular way. I started using GitHub when I was at school to collaborate with my classmates and host my course projects and have found it a great way to showcase my technical skills.  

**Advantages**:
* Super easy to set up! You just need a GitHub account, and each of your projects could be its own repo.
* It is widely used among developers and data scientists, so maintaining a good GitHub portfolio shows your professionalism.
* The nature of GitHub also makes it perfect for saving and sharing code, which is critical for many data science projects. Just make sure to include a clean and easy-to-follow readme file for each repo, as if you are writing a project summary to your stakeholders at work. That way, you can practice business writing, and your readers can quickly understand your project.

**Drawbacks**:
* GitHub is great for hosting code, but more difficult to show content in other formats. 
* It is not easily customizable compared to a website.

##### Option 2: Medium and Other Blogging Platforms

Medium is also a good place to build your data science portfolio. It is perfect to showcase your expertise. However, you don't have to be an expert in a field to write on Medium. You can use it to document your learnings and share thoughts on data science.  
I started posting my articles on Medium recently, check it out [here](https://ydong029.medium.com/) and please let me know what content you want to see next :) 

**Advantages**:
* It is easy to get started. You just need an account, and you are ready to go! I also found the Medium UI to be clean and intuitive to writers.
* Medium handles the article distribution for you, so you can reach a wider audience easily compared to doing SEO of your website yourself. 
* Medium also makes it easy to interact with your readers so you can collect feedback and engage with a community of people sharing the same interests.
* It even offers a monetization option ([Medium Partner Program](https://medium.com/partner-program)) where you can put your article behind the paywall and receive earnings based on engagement. This can be an additional incentive for you to continue writing.

**Drawbacks**:
* It is a blogging website, which means it could be challenging to share code-heavy technical content. You might still need to maintain a clean GitHub repo and link it to your articles.
* You also have less flexibility in layout and design.

##### Option 3: [GitHub Pages](https://pages.github.com/)
This is the option I went with for my portfolio website and I highly recommend it. You still host your content on a GitHub repo, but it spins up a website for you for free. Essentially, you can write each webpage easily as a markdown file, and the directory tree will be translated to the URLs. You can find a quickstart guidance [here](https://docs.github.com/en/pages/quickstart). 
I used the Minimal Mistakes Jekyll template to make my website look slightly better than the default UI and documented my setup process in [this article](https://yudong-94.github.io/personal-website/blog/BlogUIRampup/). Recently, I also revamped the design with the help of ChatGPT, which you can read [here](https://yudong-94.github.io/personal-website/blog/BlogUpdateWithGPT/). It's still very basic, and I plan to improve it further, for example by adding the visual thumbnails of my articles. Please let me know if you have any suggestions!  

**Advantages**:
* It's free, relatively easy to set up with basic coding skills, and offers various customization through the Jekyll templates.
You can do version control and local tests via GitHub.

**Drawbacks**:
* While you can write every page in markdown, you will need some front-end knowledge to further customize the website design. For example, I had to add some small pieces of CSS and HTML code to add two images side by side (but of course, you can ask ChatGPT for help).
* There are other limitations. For example, there are no built-in tools for SEO and analytics, which might limit audience reach; adding interactivity elements like comments and subscriptions is challenging since this is a static site without a backend server; Using a custom domain is a bit tricky requiring DNS configuration.

**Bonus Point**:
* You can integrate Google Analytics into your website hosted on GitHub Pages easily. For the Jekyll template I used, I simply added a few parameters to the `_config.yml` file. This helps you understand site traffic and audience behavior, and practice your web analytics skills. I also use it to measure the impact of my LinkedIn and Medium posts (yes I will monitor the traffic from this article as well 😀). Here is a [LinkedIn engagement analysis](https://yudong-94.github.io/personal-website/blog/LinkedInPostAnalysis2023/) I wrote in the past.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/google_analytics_screenshot.png" alt="A Recent Google Analytics Screenshot of My Website" width="600" height="400">
</div>

##### Option 4: Website Builders Like Squarespace and Wix

Another option is to use website builder tools like Squarespace and Wix. They offer user-friendly drag-and-drop interfaces, ideal for people who are less comfortable with coding and prefer a more visual approach to building your site.  
I haven't tried this approach myself, so please let me know your experiences below.  

**Advantages**:
* They provide a great variety of pre-designed templates, helping you build a professional-looking website with minimal effort.
* They usually provide built-in SEO and analytics tools to understand web traffic better and optimize the website for search engines.

**Drawbacks**:
* The convenience comes with a cost. What you can do with the free tier is relatively limited, so you might need to pay a subscription fee starting from ~$20 monthly to have a fully functional website you'd like.

##### Option 5: Build Your Website from Scratch…
Of course, if you are familiar enough with website development and want 100% flexibility and customization, building your website from scratch is another option.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/portfolio_option_comparison.png" alt="Comparison of the Five Options" width="600" height="400">
</div>

---

#### Portfolio Content

What is more important than the platform choice is the content choice. Data science is a broad field, so luckily, you have lots of options. Here are some of them:  

1. **Data visualization**: Data visualization is a foundational data science skill for presenting your findings to stakeholders. With that being said, you should not only focus on making your visualization visually attractive but also think about what story it tells and how to make it clear to your audience. I make one visualization every week and put it on my website. You can find my 330 weeks of data visualization journey [here](https://yudong-94.github.io/personal-website/blog/WeeklyVizJourney/), discussing how to pick a dataset to visualize and what tool to use.
2. **Analysis reports**: You can conduct some exploratory data analysis and publish your analysis report on your portfolio. You can try different tools, techniques, and approaches you usually don't have time to use at school or work. If you are looking for a job, it is a great opportunity to showcase your skills and insights -  you can analyze a dataset related to your target industry, or write a case study of the target company. For example, you can discuss the user acquisition and retention strategy and metrics of a social media app, or analyze the lifetime value (LTV) of a subscription service. 
3. **Machine learning case studies**: Machine learning is another critical skill for a data scientist. Kaggle is always a good resource where you can find all sorts of datasets and tutorials, practice in the playground, or enter an active competition with the possibility of winning real money! Once you complete a machine learning project, writing a blog is a good way to reflect on your learnings. Key things to include are the dataset description, feature engineering, models you tried and picked, training and evaluation process, and of course, your code (with clear comments).
4. **Tool tutorials**: You can share step-by-step guides on solving common data science problems or using popular tools and libraries. This could serve as great evidence of your expertise during your job search and help you engage with the broader data science community. For example, check out my article here on how to conduct topic summarization and categorization using the OpenAI API.
5. **Learning notes**: It's also totally fine if you are not an expert and comfortable enough to write tutorials. Instead, you can write learning notes from your readings, courses, certifications, work projects, etc. This reinforces your memory. It also shows you are self-motivated and continuously learning new knowledge, which is critical to being a good data scientist. Here are [my notes on the ChatGPT Prompt Engineering for Developers course](https://yudong-94.github.io/personal-website/blog/ChatGPTPromptEngineering/) by DeepLearning.ai.
6. **Career journey**: Apart from technical content, you can also document your career journey on the portfolio, including work experience, career reflections, and advice for aspiring data scientists. This content not only helps others but also is an amazing opportunity for you to look back on your career. For example, here are [My Five Key Learnings To Be a Better Data Scientist](https://yudong-94.github.io/personal-website/blog/FiveCareerLearnings/).

Of course, you don't need to do all of the above, but hopefully, these ideas will inspire you.  
It's a good idea to pick the topics that interest you the most so you can keep up with them. For example, I have two blog series that I have continued for years: 1. [My weekly visualization project](https://yudong-94.github.io/personal-website/categories/#data-viz) where I explore and visualize one interesting dataset every week. You can read more about my journey [here](https://yudong-94.github.io/personal-website/blog/WeeklyVizJourney/). 2. [My bi-monthly reading notes](https://yudong-94.github.io/personal-website/tags/#reading-notes) where I track and summarise the DS-related blogs I read every two months. This strategy keeps me motivated and ensures my portfolio stays fresh and relevant.

---

#### What Makes a Good DS Portfolio

Creating a compelling data science portfolio isn't just about showcasing your technical skills; it's also about presenting them in a way that reflects your unique personality and professionalism. Here are three key elements that I believe make a great data science portfolio:  
* **Be yourself**: Let your personality shine through your portfolio. Share your interests, motivations, and what excites you about data science. This personal touch can make your portfolio more engaging and memorable - In fact, I've found Medium articles with personal experience and stories attract more audience.
* **Be professional**: Always write your articles as if you will present them to your business stakeholders. Each project should include a clear explanation of the problem, your approach, the tools and methods used, and the outcomes. Make sure your content is well-organized and easy to follow, detailed but not overcomplicated, and free of typos.
* **Quality > Quantity**: More is not always better. Focus on showcasing a few high-quality projects rather than overwhelming viewers with numerous mediocre ones. It would be best if you prioritized highlighting projects that have real-world applications or are relevant to your target job or industry.

---

#### Final thoughts

Building and maintaining a data science portfolio requires effort and dedication, but the journey is as rewarding as the skills and opportunities it brings. Start small, pick a project that excites you, and gradually expand your portfolio. Remember, the goal is progress, not perfection.  
I hope this article helps you find a clear path to embark on this exciting journey!
