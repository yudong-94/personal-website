---
title: "I Tracked Every Article I Wrote in 2025 — Here’s What the Data Says"
date: 2026-01-04
categories:
  - blog
tags:
  - data science
  - analysis
  - career
header:
  teaser: /assets/images/article_covers/writing_review_2025_cover.jpg
excerpt: "12 articles · 36.5k reads · $2,960 earned — trade-offs and lessons."
---
I started writing data science content on Medium in mid 2024, and it has become part of my monthly routine in 2025. Not surprisingly, it even showed up as one of the three big themes in my 2025 year-in-review by ChatGPT.

Over the year, I tracked every article I published — views, reads, earnings, and engagement patterns — across Medium and Towards Data Science. Those numbers revealed a lot about writing itself: which topics resonate, how attention works, and why some articles feel rewarding even when they don’t maximize earnings.

**In this article, I’ll double-click into my 2025 writing journey with real numbers and the stories behind them.**

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/chatgpt_2025_themes.jpg" alt="My 2025 Three Big Themes by ChatGPT" width="800" height="600">
</div>

---

### Let’s Begin with the Numbers  

Before diving into reflections, let’s start with the hard numbers. As data scientists, we rarely tell a story without them.  

Here are the key metrics for my 2025 writing journey. I published most articles on both Medium and Towards Data Science (TDS), as TDS became an independent platform in Feb.  

* **Articles posted**: 12
  * 3 were “boosted” by Medium
  * 7 were featured in TDS “Editor’s Picks”
* **Total reads**: 36.5k
* **Total followers on Medium**: 4,156
  * Email subscribers: 285
* **Total earning**: $2,960
  * Medium: $2,160
  * TDS: $800

---

### Stories behind the Numbers  

A good data scientist not only presents numbers but also tells the story. What are the stories behind the above numbers?  

#### 1. AI became my favorite topic and the best-performing topic  

Among the 12 articles I wrote, half were related to AI, and they had more traction than other topics.  

AI is evolving rapidly. Its impact on the data science industry shows up in various ways — improved work efficiency, unlocking new possibilities, and even new interview processes. As a result, I didn’t just write about AI tools, but also about how AI is reshaping the data science career itself.  

**My article with the highest earnings on Medium ($1200+) is [my evaluation of the Google Data Science Agent](https://ydong029.medium.com/googles-data-science-agent-can-it-really-do-your-job-4c6dcd1302ce?source=post_page-----2b52883cfc95---------------------------------------)**, where I tried to use the agent to complete a common data science task, and demonstrated its pros, cons, and best use cases. I believe this article resonated because it taps into a common fear in the AI era: Will my job be replaced by AI? And it answered this question with a concrete example.  

**The article that got the most reads on TDS (4k+) is [my tutorial on how to use ChatGPT to better prepare for data science interviews](https://medium.com/data-science-collective/how-i-used-chatgpt-to-land-my-next-data-science-role-a366374f83cf?source=post_page-----2b52883cfc95---------------------------------------)**. This article focuses on how to make full use of AI to advance your career. Therefore, it is very practical for people who are looking for new opportunities, especially in this tough job market.

#### 2. Trade-off between views and reads  

Let me explain "views" vs. "reads" first — views are simple page views, while reads are the page views that lasted at least 30 seconds. If we define "read ratio" as `reads / views` , **a higher read ratio means people get hooked by your content and read a good chunk of it**.  

Besides AI-related articles, I also write about my career tips, as well as specific data science topics. For example, [my experience working at a startup](https://medium.com/data-science-collective/from-data-scientist-ic-to-manager-one-year-in-6c4389e93eba?source=post_page-----2b52883cfc95---------------------------------------), and [my first year in people management](https://medium.com/data-science-collective/what-being-a-data-scientist-at-a-startup-really-looks-like-df6d6fbcbcbf?source=post_page-----2b52883cfc95---------------------------------------). Unlike AI, which is a hot keyword right now, articles on those niche topics usually get much fewer views, but sometimes a higher read ratio.  


For example, I wrote an article on [data science use cases in customer support](https://ydong029.medium.com/the-secret-power-of-data-science-in-customer-support-12691fd3c914?source=post_page-----2b52883cfc95---------------------------------------) — this is not a popular domain and only got ~900 views on TDS in 30 days since publication (vs. my average of 4900). However, its read ratio is as high as 56% (vs. my average of 34%). Clearly, there is a selection bias of the people who clicked into the article in the first place — they are interested in this specific topic. And since fewer people have covered this topic in the past, the viewers are more likely to finish the whole article. This “low-view, high-read-ratio” pattern isn’t great from a pure monetization perspective, but it often feels more fulfilling, as I know there are people genuinely caring about these niche domains and enjoying the articles.  

As a writer, the ideal articles you want are those with high views as well as high read ratios. Hot topics and clickbait-style titles will bring you high views, but how to engage the audience in the first 30 seconds and convince them to stay is very hard, and that’s the balance I have been trying to strike.  

#### 3. Earnings on Medium highly depend on whether it is boosted or not  

Medium article earnings usually follow the 80/20 rule, with 20% of the articles bringing you 80% of the money.  

While the earning model is a black box, I tried to unpack it with my own data on Medium (details in my [Nov 2024 article](https://medium.com/data-science/my-medium-journey-as-a-data-scientist-6-months-18-articles-and-3-000-followers-c449306e45f7)). The two key factors I uncovered are 1. the number of reads from Medium members, and 2. whether your article is boosted or not. “Boost” is a program where Medium hand-picks high-quality stories and weights those stories for extra distribution via the recommendation algorithm. According to Medium, “95% of Boosted stories get at least 500 extra views within two weeks”. You can read more about this program [here](https://medium.com/blog/a-new-boost-for-top-stories-541884654fdb).  

I collected my first 30-day member reads and earnings data from all my published articles on Medium and refreshed my simple linear regression analysis. It is clear that when an article is boosted, it earns 10x. I got three articles boosted in 2025, and their total earning was ~$1800, which was 83% of my total Medium earnings.  

How to get your article boosted remains a myth, and there are many speculations online. However, people agree it has to be something that carries your own story and thinking.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_reads_earnings.jpg" alt="Medium member reads vs. earning of my past articles" width="800" height="600">
</div>

Linear regressions:  

* **Boosted articles**: Earnings = 0.288 * member reads — 30  
  * R-squared = 0.996  
  * P-value < 0.0001  
  * sample size = 6  

* **Not Boosted articles**: Earnings =0.027 * member reads + 1.6  
  * R-squared = 0.960  
  * P-value = <0.0001  
  * sample size = 27  

Note: Of course, the sample sizes are small, so the exact coefficients should be taken with a grain of salt — but the magnitude of the difference is hard to ignore.  

#### 4. Earning on TDS is more flat  

Meanwhile, the earnings on TDS are much more flat — I got $100 each for eight articles I wrote. Basically, publishing one article on TDS covers about three meals per month — haha.  

**TDS has a tiered [author payment program](https://towardsdatascience.com/announcing-the-towards-data-science-author-payment-program/)**. The lowest tier requires 500 views in 30 days and pays a flat $100 until your article exceeds 5,000 views. Hitting 500 is not too hard, as I only had one missing the threshold — probably too niche, but I will publish it on Medium very soon, and we will see how Medium readers react to it. Unfortunately, my best record so far is 4,013 views in 30 days — Getting at least one article exceeding 5,000 views is on my 2026 new year resolution list :)  

#### 5. Medium vs. TDS  

Now that I’ve talked about the different earning programs on Medium and TDS, if you are also interested in publishing data science content online, which one should you go with? A simple answer is probably both, to maximize your reach. But here are a couple of notes:  

* These two platforms have different audiences and distribution channels. Medium is a diverse platform with various topics and a broad user base, and it uses a recommendation algorithm to distribute the content. This means your articles rely on the algorithm to be matched to the readers. However, TDS is very much data science-focused (and these days, 90% of the articles are related to AI). Therefore, its audience is already filtered and has a much more similar taste. It also distributes articles on platforms like LinkedIn and X. As a result, I sometimes see inconsistent patterns of which articles get popular on which platform — in other words, even if it does not work well on A, there is still a chance it will become viral on B. **In short, Medium rewards breakout hits, while TDS rewards consistency**.  
* If you decide to publish articles on both platforms, please remember that your article has to remain exclusive to TDS in its first 30 days to qualify for [TDS’s author payment program](https://towardsdatascience.com/announcing-the-towards-data-science-author-payment-program/) — “During these 30 days, articles must remain exclusive to Towards Data Science. After that, authors are free to republish or remove their articles.”  

#### 6. Writing is more than making money  

Though earning is one of my key metrics for writing, honestly, I view it more as some sweet extra money to dine in a great restaurant or fund my travel — it clearly has a lower hourly pay than my full-time job.

**However, what I value more is the experience itself**. Coming up with ideas helps me reflect on my career and deepen my learning; organizing those thoughts into articles strengthens my communication skills; publishing the articles brings me closer to the data science community and allows me to connect with more people who share the same interests.  

If you’re considering writing — especially as a data scientist — I’d encourage you to start before you feel “ready.” The feedback loop itself is the reward.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/article_covers/writing_review_2025_cover.jpg" alt="My year with ChatGPT" width="800" height="600">
</div>
