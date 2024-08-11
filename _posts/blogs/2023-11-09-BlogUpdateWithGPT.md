---
title: "Update My Blog with GPT"
date: 2023-11-09
categories:
  - blog
tags:
  - llm
  - coding
  - website
---

Today, I gained access to the GPT All Tools feature, an exciting upgrade for Plus users that integrates DALLE, browsing, and analysis with GPT-4, all within a single conversation. As it's been a year since the last major update to my blog, I am hoping GPT-4 can help me with this task.  

### Can GPT-4 Read My Website?

Keen to gather fresh ideas for my website improvement, the first step obviously is to let GPT understand my website. After sending the link to my ['About Me' page](https://yudong-94.github.io/personal-website/about/), it accessed the page using the 'browsing' feature and provided a neat summary. My only complain is, it somehow assumed me to be a 'he/him'... But when I pointed it out, it apologized sincerely (?).  

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/blog-summary.png" alt="GPT Blog Summary">

### I Want A New Website Title

The original title of my blog — Yu Dong's Blog — has served me well, yet it's simplicity called for a dash of creativity. Knowing GPT's flair for inventive text, I solicited some suggestions. Among the various imaginative titles, 'DongDataDive' struck a chord with me for its rhythmic appeal.  

```
DataStoryteller: A name that highlights your focus on storytelling through data.
DongDataDive: Alliteration can make a name catchy, and this one suggests a deep dive into data science topics.
AnalyticsAlcove: This name suggests a cozy, insightful corner where readers can explore analytics.
TheDataNarrative: Emphasizes your blog as a place where data tells a story.
YuInsights: A play on “you insights,” suggesting personalized insights from data.
NarrativeNumbers: Reflects a blog where numbers are turned into narratives.
Dong'sDataDen: Another alliterative name that suggests expertise and a specialized focus on data.
DataVizDiary: For a blog that frequently shares data visualizations.
InsightfulBytes: Implies that readers will gain insightful information in small, digestible formats.
AnalyticAdventures: Suggests a journey through the world of analytics.
```


### Let's Create A Profile Picture!

With GPT-4 now somewhat familiar with my website, I tasked it with creating a new profile picture, putting DALLE3's image generation to the test. My brief was simple: encapsulate the essence of my website's content and feature a cat (because I am a cat person). The process was straightforward — I requested a DALLE3 prompt followed by the image creation. Although I expected step-by-step outputs, GPT-4 produced a delightful image of a cat amid data and charts directly. This charming illustration now is my official profile picture.  

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/profile-image-generation.png" alt="GPT Profile Picture Generation">

### Please Analyze My Website Performance

The above use case was to create an image from text. So let's also try asking GPT to interpret a picture. I submitted screenshots of my Google Analytics report from the past 12 months to GPT, seeking an analysis of my website's performance.  

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/google-analytics-question.png" alt="Analyze Google Analytics Report">

The output is very promising and makes a lot of sense. Here is part of it:  
```
1. Traffic Acquisition:
- The majority of your sessions come from 'Organic Social', which suggests that your social media efforts are effective in driving traffic to your site.
- 'Direct' traffic is also significant, indicating that a good number of users are accessing your site by typing the URL directly into their browser or using bookmarks, implying a returning audience.
- 'Organic Search' and 'Referral' traffic are relatively lower, suggesting potential growth areas in search engine optimization (SEO) and obtaining backlinks from other sites.
2. Users by Country:
- The United States dominates your user base, followed by Taiwan and Canada. This indicates that your content resonates mostly with users in these countries or that your marketing efforts are focused there.
- The presence of users from diverse countries such as India, China, Brazil, and Germany suggests international appeal, but there may be room to increase outreach or tailor content to these and other non-English speaking regions.
3. Page Views and User Engagement:
- The 'Posts by Category' page has the highest number of views, which could mean users are interested in navigating through different topics on your blog.
The 'Five Years in My DS Career' post is likely one of your most popular pieces, possibly due to its personal and professional insights into a career in Data Science.
- The event counts for 'page_view' and 'user_engagement' are quite high, indicating that users are interacting with your content.
- The 'scroll' and 'session_start' events suggest that users are browsing through content and likely reading multiple articles.
4. User Metrics:
- With 583 users and the same number of new users, it seems your site is attracting visitors but may need to work on retaining them, as these numbers should ideally be different with returning visitors included.
- An average engagement time of 1 minute and 15 seconds is a bit on the lower side, indicating that while users are visiting your site, they may not be staying long enough to engage deeply with the content.
```

### Implement SEO Tags with the Help of GPT-4

Despite regular postings, my website traffic hadn't seen much activity since a spike in January—following a LinkedIn post of my [five-year summary](https://yudong-94.github.io/personal-website/blog/FiveYearsInMyCareer/). So, what can I do to improve it?

Initially, GPT-4's suggestions felt broad - improve CSS, add interactive elements, etc. Given that it could only assess my GitHub Pages-hosted site at a surface level, without delving into sub-pages, the advice was understandably generic.

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/website-ideas.jpg" alt="Website Ideas">

Determined, I delved deeper into SEO strategies and discovered the `jekyll-seo-tag` plugin recommended by GPT. The step-by-step guidance it offered was straightforward and user-friendly.

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt-jekyll-seo-tag.jpg" alt="How to Implement Jekyll SEO Tag">

However, coding is rarely a one-shot success. Integrating the plugin required navigating through a series of error messages and customizing the default layout of the [minimal-mistakes template](https://github.com/mmistakes/minimal-mistakes) I use - a daunting task given my limited experience with Ruby and front-end development. Thankfully, GPT's assistance significantly streamlined the process, even though I had to google a little bit to figure out a package version conflict issue.  

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/gpt-layout-update.jpg" alt="How to Update Layout">

GPT also enlightened me on local site testing - a practice I had bypassed by directly pushing code to my main branch and waiting for deployment. Below, you can see the successful addition of the SEO tag.  

<img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/seo-tags.png" alt="SEO Tags">

### Conclusion  

In this example, I tried multiple GPT features, including browsing, DALLE3, image recognition, code interpreter, etc. And that all happened in one chat and took me less than 2 hours! This absolutely blew my mind. If I want to do all these myself, I might need to learn several new tools, spend hours and hours googling, and have 10+ stackoverflow tabs open. And of course, I will never be able to create a picture of a cute cat with the data science theme. By the way, this post is also polished by GPT. Thank you, GPT :)

Next, I am excited to try out the new GPTs and build my own GPT app!  
