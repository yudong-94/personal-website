---
title: "My Medium Journey as a Data Scientist: 6 Months, 18 Articles, and 3,000 Followers"
date: 2024-11-11
categories:
  - blog
tags:
  - data science
  - analysis
  - career
---

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    img {
        margin: 10px;
        max-width: 100%;
        height: auto;
    }
</style>

**Real numbers, earnings, and data-driven growth strategy for Medium writers**

---

I started writing data science and AI content on Medium in May 2024. This is my sixth month and I just hit a major milestone — 3,000 followers! I am very proud of my achievements.

In this article, I will share how this journey started, what I have been writing, and what I learned. Plus, as a data scientist, I always enjoy analyzing my own data. I collected a dataset of my Medium stats, including article views👀, reads📖, claps👏, earnings💵, etc. Join me as I break down my Medium experience using data and share my data-driven writing strategies.

---

### My Medium Journey Overview

#### How it all began

My writing habit dates back well before I started writing on Medium. I have been running my data science portfolio site since 2018, back when I started my first full-time job. I post articles there and occasionally share them on LinkedIn. It helps me connect with friends and colleagues in the data domain. Earlier this year, I posted an article about [my experimentation with the custom GPTs](https://yudong-94.github.io/personal-website/blog/MyFirstGPTs/), and it reached nearly 10k impressions on LinkedIn. This is not bad at all but it also leads me to wonder how I can reach an even wider audience.

Meanwhile, I have been a Medium Member since 2020. It has been invaluable for me to learn skills outside of my daily work and keep up with new technologies in the industry. Being in the industry for seven years, I feel it is time to be on the other side to share my knowledge with the community (and get my $5 monthly Medium subscription fee back 😀).

This is how the story started. I first tried posting some of my old articles on Medium, then moved on to writing brand-new content, submitting my articles to publications like Towards Data Science, and posting two to four new articles each month.

#### What I write about
My articles cover these three categories:
* **Technical tutorials**: Many people come to Medium to learn how to do X, just as I do. Therefore, a majority of my articles fall under this category. This includes my article with the highest earning: [Mastering SQL Optimization: From Functional to Efficient Queries](https://yudong-94.github.io/personal-website/blog/SQLOptimization/).
* **Learnings**: We don’t know everything, but that is okay. I enjoy exploring new things and sharing my discoveries on Medium. For example, I have [a series of articles](https://yudong-94.github.io/personal-website/blog/LLMComparisonSQL/) comparing ChatGPT, Claude, and Gemini on various data science and analytics tasks.
* **My career stories**: With seven years in the industry, I have lots of career stories and reflections. In fact, the article that brought me the most claps and new followers is [330 Weeks of Data Visualizations: My Journey and Key Takeaways](https://yudong-94.github.io/personal-website/blog/WeeklyVizJourney/).

#### How writing on Medium has helped me
Writing on Medium of course helped me engage more with the data science community and earn some extra money. But it brought me many more benefits, including:
* **It makes me more confident in expressing my opinions.** I have been following Towards Data Science so many years as a reader, and have always seen it as a publication for those top-notch data science articles. Now being an author who publishes here regularly, I feel much more confident in my data skills and story-telling abilities. And every clap and comment is a wonderful form of recognition.
* **It enhances my knowledge and skills.** The process of writing an article is like re-learning something or re-experience a journey. It requires lots of fact-checks and reflections. Therefore, every article I write reinforces my understanding of the topic.
* **It helps me to keep this habit of reading and writing.** Working in a second language isn’t easy (my native language is Mandarin Chinese) and regular reading and writing are the keys to constantly improving my English communication. Because now I am writing on Medium, I also tend to read others’ articles more to get inspiration. This created a positive cycle of reading and writing.

---

### Mapping My Journey with Data

As a data scientist, I like collecting and analyzing data to improve decision-making. This also applies to blogging. Let’s start with some key metrics of my Medium journey (as of 11/3):
* **Stories posted**: 18
* **Total reads**: 54k
* **Total claps**: 6,926 (~385 per article)
* **Total followers**: 3,210
* **Total earning**: $2,140  

These are just the top-line metrics. To dig deeper, I prepared a dataset with daily stats on views, reads, claps, follows, and earnings for every article by following [this guide](https://levelup.gitconnected.com/how-i-extract-data-from-my-medium-stories-f5e690a3d783). Here is what I discovered from the exploratory data analysis.

#### Key Data Insights

**1.80% of article views happen in the first 7 days.**

As shown in the charts below, on average, 50% of the views come within the first 3 days, and 80% within the first 7 days. After 2 weeks, daily views usually drop below 50. This is likely because 1. publications like Towards Data Science usually share new articles on social media within the first few days after publishing, and 2. Medium prioritizes newer articles when distributing them through its recommendation system.

This means you can already tell if your article is a hit in 3 days.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_daily_views_by_article.png" alt="Daily views by articles" width="600" height="500">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_daily_views_dist.png" alt="Daily views distribution" width="600" height="500">
</div>

**2.Medium members are 3x more likely to read an article than non-members.**

Medium defines `views` as people who visited your story’s page and reads as people who read your story for at least 30 seconds. Therefore, the `read ratio = # reads / # views` tells how engaging your article is to the audience that visits it.

An interesting pattern I noticed is that the **Medium members have a read ratio of around 60%, while it is closer to 20% for non-members**. This shows the motivation to read more when you are paying the subscription fee :) Meanwhile, it might also be driven by the fact that non-members will hit the paywall if they have already exceeded the preview limit for the month (if those views are not excluded from the Medium stats, which I could not verify).

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_read_ratio.png" alt="Member vs. non-member read ratio" width="600" height="500">
</div>

**3.Article earnings follow the 80/20 rule.**

80% of my earnings come from just 3 articles, which is a perfect example of the 80/20 law. In fact, [my best-performing article](https://yudong-94.github.io/personal-website/blog/SQLOptimization/) alone has brought me nearly $1,000 now. On the other hand, as you can see in the histogram below, many articles earn less than $10.

My three best-performing articles also happen to be the three that are boosted by Medium. “Boost” is a program where Medium hand-picks high-quality stories and weights those stories for extra distribution via the recommendation algorithm. According to Medium, “*95% of Boosted stories get at least 500 extra views within two weeks*”. You can read more about this program [here](https://medium.com/blog/a-new-boost-for-top-stories-541884654fdb).

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_earning_hist.png" alt="Article earning histogram" width="600" height="500">
</div>

**4. Member reads and whether boosted or not are key to earnings.**

So what factors determine the earnings? Medium has never revealed its formula but shared some key factors in [its help center article](https://help.medium.com/hc/en-us/articles/360036691193-Calculating-earnings-in-the-Partner-Program). And here is my take by analyzing my (small sample of) earnings data. Two major factors that influence earnings the most are:

1. **If your article is boosted or not.** In the help article, Medium also says there is “*a multiplier of engagement points when the story is Boosted.*”. As you can see in my chart below, earnings from the boosted articles are clearly outliers compared to the not-boosted articles.
2. **Number of member reads.** It is not surprising that the more reads you get from the Medium members, the higher your earnings will be. When I separated boosted vs. not boosted articles, I found a strong positive correlation between member reads and earnings. And please note that this is member reads — unfortunately reads from non-members don’t matter according to the help article.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/ds_portfolio/medium_earning_regression.png" alt="Correlation between member reads, boosts and earnings" width="600" height="500">
</div>

Here are the fitted regression formulas:
1. **Boosted articles**: `Earnings = 0.28 * member reads - 43`
- R-squared = 0.998
- P-value = 0.029
- But please note that I only have 3 data points haha!
2. **Not Boosted articles**: `Earnings =0.027 * member reads + 2.1`
- R-squared = 0.965
- P-value = <0.001
- sample size = 15
The slope for boosted articles is 10x that of non-boosted ones. In other words, **when your article is boosted, you earn 10x 💰**.

Medium says reading time and engagement like claps, highlights, and responses also impact earnings. However, my articles are mostly between 7 to 10 minutes long, so the reading time probably doesn’t vary too much (and the data is not available to me). As for the engagement metrics, they all appear to be highly correlated with member reads. Therefore, just using `member reads` itself already has a strong predictive power in my case.

Eventually, when I get a significantly larger dataset one day, I plan to run a more rigorous regression analysis with all the metrics I have access to. But please let me know if my findings match your Medium article stats :)

---

### Data-driven Medium Writing Strategy  

What can we learn from the analysis above? Here are my data-driven recommendations on Medium writing:
1. **Write regularly to build your audience**: Earning is highly correlated with member reads. What is the best way to increase member reads? To build your audience. Every new article has a chance to attract more followers, and if your articles show up on someone’s homepage often, they have a higher chance to follow you and read your future articles.
2. **Quality over quantity**: I’ve seen people recommending posting articles every day. But that is not what I mean by writing regularly. I believe fully polishing an article on a topic that you are really into is the way to engage your audience and improve the read ratio. It also increases your chance of getting “boosted”. (And honestly, I am not the type of creative person who can come up with new writing ideas every day…)
3. **Submit to publications**. Publications like Towards Data Science have established their subscriber bases and distribute accepted articles across various channels like emails, LinkedIn posts, Twitter (I mean… X), etc. This means your article will reach a much wider audience than you just letting Medium do their recommendation algorithm magic or sharing it on your social media. This is particularly important for new writers. Additionally, only publication editors can nominate your article for a “Boost” (read more [here](https://help.medium.com/hc/en-us/articles/23964242497559-Browse-100-publications-in-the-Boost-Nomination-Program)). So this also gives you a higher chance to earn more money.
4. **Optimize your title and opening**. A ‘read’ counts when someone reads your story for at least 30 seconds. What can people see in 30 seconds? That’s probably only enough time to read the title and subtitle and skim through the first paragraph. Therefore, you should try to optimize the first impression to grab the reader’s interest. This is the same reason why companies do SEO and marketing email optimization. I would like to A/B test my titles if I could, but unfortunately, that is not doable on Medium. So I am also learning by trial and error now.
5. **Create content that is ‘you’**. Among my past articles, the ones that perform best are always the ones with more personal touches. Even for technical topics like SQL optimization, I included my personal experiences and examples. Essentially, your content shouldn’t be something that ChatGPT is able to create by itself.

I hope this article gives you more insights into writing on Medium (especially in the data science domain) and inspires you to embark on a similar journey.
