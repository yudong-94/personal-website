---
title: "A Product Data Scientist’s Take on LinkedIn Games After 500 Days of Play"
date: 2026-01-06
categories:
  - blog
tags:
  - data science
  - career
header:
  teaser: /assets/images/article_covers/linkedin_games_cover.jpg
excerpt: "What a simple puzzle game reveals about experimentation, product thinking, and data science."
---

This article was initially posted on [Towards Data Science](https://towardsdatascience.com/a-product-data-scientists-take-on-linkedin-games-after-500-days-of-play/).  

---
I am on a 500-day streak on LinkedIn Games. Yes, LinkedIn also has games, and they’ve been around for over a year. From time to time, I notice new games, design tweaks, and new features being rolled out. As a Data Scientist, I have always wondered what LinkedIn is trying to achieve with LinkedIn Games and how they are testing the changes.

With AI augmenting and even automating many coding and basic analytics tasks, product sense and domain expertise become more and more important for data scientists. Therefore, in this article, I am using LinkedIn Games as an example to show how a Product Data Scientist thinks and works. This is also the type of mental exercise I practice when preparing for product case interviews.

---

## I. What’s the goal of LinkedIn Games  

The first step in any product case is to understand the product's goal. [Per LinkedIn](https://www.linkedin.com/help/linkedin/answer/a6284860), “Games on LinkedIn are thinking-oriented games to help you sharpen your minds, take a quick break, and have the opportunity to connect with each other and spark conversations.”  

These games are quick brain teasers, so they do help users “sharpen minds and take a quick break” to some extent. But I believe the real intention hides behind the last part — “connect with each other and spark conversations”.  

Why does this matter? LinkedIn generates most of its revenue from talent solutions, the advertising platform, and premium subscriptions. All of these rely on an active user base — recruiters need a large pool of active candidates, advertisers need targeted impressions, and the value of premium subscriptions increases with the network size. Moreover, the key to maintaining an active user base is user engagement and interactions, which ultimately lead to higher retention.  

In data language, MAU (monthly active users) is one of the most common metrics to measure the active user base of a product. `MAU in month X = active users in month X-1 + users acquired/resurrected in month X - users churned in month X`. For LinkedIn, I believe LinkedIn Games is a feature that is designed to grow MAU by reducing the last component, “users churned this month.”  

## II. How does LinkedIn Games achieve this goal  

Now that we are clear about the goal of improving retention, the next question is, **how** does LinkedIn Games achieve it? I think there are two mechanisms — direct interactions with LinkedIn Games and indirect engagement driven by coming back to the platform.  

### 1. Direct interactions with LinkedIn Games  

Every day, LinkedIn publishes a game post and encourages users to share their scores and tips. This is exactly what they meant by “help you … connect with each other and spark conversations.” Below is a screenshot I took at around 10 PM Pacific Time on 11/29 — around 22 hours after the daily Zip game was refreshed. You can find the entry point to this post after finishing a game, or it might show up on your homepage. This post had 1240 reactions and 1370 comments. Many users post their scores and interact with each other.  

This kind of social interaction is valued by many LinkedIn users. Sharing your good game score is also similar to sharing a small achievement, so it does not work against the professional social network image of LinkedIn. As a result, LinkedIn Games creates a network effect that increases retention.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/zip_game_post1.jpg" alt="Zip game post by LinkedIn 1 (Image by the author)" width="300" height="250">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/zip_game_post2.jpg" alt="Zip game post by LinkedIn 2 (Image by the author)" width="300" height="250">
</div>

### 2. Indirect engagement from returning to the platform  

Meanwhile, there are absolutely people like me who are simply addicted to the games but never share scores or comment on the post. No interaction does not mean LinkedIn Games does not achieve the retention goal for this group of users. The fact that it brings users back every day is already a strong retention lever.

Linked Games achieves this by creating a habit loop. Let me put it in the **Hooked Model** (Trigger-> Action -> Reward -> Investment) to unpack it:

1. **Trigger**: Users are prompted to return by external triggers like push notifications and homepage modules, and internal triggers such as the desire to maintain a streak.  
2. **Action**: The puzzles are easy to understand, low-friction to enter, and quick to play.  
3. **Reward**: Users get a different puzzle every day, earn streak badges, and can compete with their connections.  
4. **Investment**: Users “invest” by building a streak, getting connections to play, sharing results, improving their leaderboard rank, etc. Every day, users build up sunk effort, making it harder to stop.  

With this habit loop, users come back daily. As long as a user opens LinkedIn, there is also a chance that they will check out other things, like network updates, messages, job openings, etc. These actions could all lead to meaningful engagements outside of the Games feature and increase overall retention.  

## III. Experimentations on LinkedIn Games  

We covered the goal of LinkedIn Games and the mechanisms behind it — **LinkedIn Games aims to improve user retention by encouraging interaction on Games content and increasing overall product engagement**. As a data scientist, if you work on this product, a key part of your job will be collaborating with Product Managers, Designers, and Engineers to brainstorm initiatives and run experiments to measure the retention impact. And this is clearly happening with LinkedIn Games, as I have noticed so many design changes over time. Let me walk through some examples and discuss how data scientists will be involved.  

### 1. Entry points to LinkedIn Games  

Right now, you can access LinkedIn Games through:  
* [Games hub](http://linkedin.com/games)
* Search for games on the LinkedIn Search bar
* My Network page
* Today’s Games section under LinkedIn News on your Desktop homepage or Side panel in the LinkedIn mobile app
* Notifications  

But this is not always the case. I remember one day the entry point on the My Network page disappeared, and I had to search in the app to find the games. But a few days later, it appeared again. The location of entry points determines how easy it is to find the feature, for both new and returning users. But more entry points aren’t always better. While more entry points increase visibility, each of them can create a contextual bias — users who land on My Network might behave differently than those who come through a notification— thus, different entry point has different impacts on engagement and retention. In other words, they will cannibalize each other.  

For example, the My Network entry point sits below the invitations and above the connection recommendations. When a user visits this page to play the daily game, inevitably, they will see the pending invitations, and it will remind them to take action — expanding connections is a critical part of making a user’s LinkedIn experience meaningful and valuable. Meanwhile, if they go to their homepage for the games, they will instead see other users’ posts, and are more likely to interact with the posts.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/entry_point1.jpg" alt="LinkedIn Games entry points on My Network page and homepage 1 (screenshots by the author)" width="600" height="300">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/entry_point2.jpg" alt="LinkedIn Games entry points on My Network page and homepage 2 (screenshots by the author)" width="600" height="300">
</div>


Different types of interactions have different impacts on retention, and it is hard to estimate the exact impact of removing/adding an entry point without running an experiment. Now the task is on the data scientists to design the experiment.  

Here is how it could look like:  

* **Experiment design**: control = current design, treatment = removing the entry point on My Network  
* **Randomization unit**: user-level A/B testing, 50% users will randomly see the control vs. the treatment design  
* **Primary metric**: 7-day retention rate — time window can vary based on how quickly we want to measure the retention impact and any past learnings. One caveat is that retention is a lagging metric, and LinkedIn Games might have relatively low traffic compared to the rest of the platform, which makes it difficult to detect retention impact in the short term. In that case, the primary metric might need to shift to a leading indicator of retention, or data scientists might need to rely on causal inference techniques to estimate the retention lift more reliably.  
* **Secondary metrics**: % users played a game; % users interacted with network posts; % users added connections; Average sessions per user; Average time spent per user  
* **Guardrail metric**: average app/website performance  

Data scientists will work with the cross-functional team to align on metrics based on the goal of the experiment, run power analysis to determine the experiment time length and scope, conduct implementation checks, and eventually analyze the results to make a call on the best combination of entry points.  

### 2. Notifications  

Several months back, I started receiving reminder notifications like “You’re on a xxx-day streak. Play xxx now to keep it going”. Later, after finishing the games, there is another set of notifications saying “congrats on finishing xxx”.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/notification.jpg" alt="LinkedIn Games notification (screenshot by the author)" width="300" height="300">
</div>

Notifications can be annoying, but they are very effective in bringing users back. For example, Duolingo is famous for its creative and “psychologically manipulative” notifications (I am on a 1735-day Duolingo streak, by the way). [Their early blog post](https://blog.duolingo.com/hi-its-duo-the-ai-behind-the-meme/) described how Duolingo used multi-armed bandits to find the best-performing notification.  

Similarly, optimizing notifications can have a huge impact on LinkedIn Games. Data scientists can run experiments to test  

1. **When to send the reminder notification** — it could be during lunch break or after work time when users are more likely to be available, or when the user usually opens the app, or even when they played the game yesterday.  
2. **When to send the congrats notification** — the congrats notification could be used to bring a user back to the app and encourage them to post their results and interact with other players. Similarly, we can test sending it right after finishing the game, or maybe later in the day when more users have played the game.  
3. **The message text** — should the tone be neutral or more aggressive? How long should it be?  
4. **The CTA (call to action) text** — “Solve now”? “Play now”? “Extend your streak”? Different text on the button could lead to different click-through rates.  
5. **Frequency** — if a user does not come back to play the game after the first notification, should we send another reminder?  

Here is just a short list off the top of my head, but it’s already lots of different combinations of notification designs. It is totally possible that text A coupled with timing X is better than text B coupled with timing Y. Therefore, running experiments for each decision one by one is both inefficient and could lead to a sub-optimal result. That is why Duolingo mentioned the **multi-armed bandit** framework above. It is a framework to test multiple variations simultaneously, and unlike traditional A/B tests, it speeds up the experiments by automatically diverting more traffic to the winning arms based on a reward function and reducing the number of arms in the test quickly. Therefore, the multi-armed bandit could be very useful to test LinkedIn Games notifications. If you want to learn more, [here](https://multithreaded.stitchfix.com/blog/2020/08/05/bandits/) is another article by Stitch Fix on how they use multi-armed bandits in their experimentation platform.  

So what’s the data scientist’s role here? Of course, they will brainstorm with the stakeholders to come up with different variations, define the reward functions (e.g., whether a user plays today’s puzzle), run the multi-armed bandit setup, and interpret the results.  

### 3. Game results page  

Another area where I have noticed many changes is the game results page. After finishing the game, the user first lands on a results summary, with attractive stats cards like “On fire 500-day win streak!”, “Top 95% All players”, and “Smarter than 90% of CEOs”. It also has a prominent “Share” button that prompts you to share your results as a post or as a direct message to your connections.  

After that, there is a long results page with seven major sections:  

1. Header — how quickly the user solved the puzzle with copy and share CTAs.  
2. Connection leaderboard — where you rank among your connections. If you click on “see full leaderboard”, there are CTAs to nudge connections who haven’t played today.  
3. The “play another game” CTA asks you to explore different games.  
4. Another summary panel with more stats, including all-time win rate, best score, streak badges, and a push notification toggle.
5. Weekly industry and school leaderboards with share options.  
6. Link to the daily game post, where you can react or comment directly.  
7. “Unlock this week’s bonus puzzle” by inviting your connections to play the game.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/linkedin_games/game_results_page.jpg" alt="Game results page (screenshots by the author)" width="900" height="200">
</div>

Do you see the pattern? Every section has some CTAs to encourage sharing, engagement, or social interaction. However, is the current sequence of cards the best sequence for the retention outcome? Is there a better UI for the results stat cards with a higher share rate? Do people even care about the ranking of their employer and school?  

To answer these questions, a data scientist would design experiments similar to the one we discussed in the entry points section to measure the click-through rates, interactions, and overall retention impact.  

To take one step further, different users might have different preferences. For example,  
* User A wants to “show off” their score and how much smarter they are than the CEOs, so the current sequence works perfectly for them, as they can do it right on the first screen.
* User B feels a strong sense of belonging to their community, so they will share the leaderboard, asking coworkers or classmates to join the game to improve the ranking of their company or school. Therefore, displaying the leaderboards on top will improve their engagement.
* User C loves to share their puzzle tips and discuss with other players, so we should move the post up on the results page.
* User D simply enjoys the game, and they would invite others to unlock more puzzles if they are offered this option. But with the current design, they might not even scroll down all the way to the bottom and miss the “unlock this week’s bonus puzzle” card.  

This kind of **personalized** results page makes a lot of sense theoretically, but how to make it work is another complicated data science question. Data scientists could segment users based on user profiles and past activities — for example, how many connections they have, how many of their connections have played the games, if the user often posts or comments, etc. Then the data scientists could analyze the experiment results by different user segments to identify which design works the best for each segment and come up with the personalization strategy. To make the system even smarter, data scientists could build a machine learning model to predict the card layout that maximizes engagement for each user.

### 4. Nuance: Network effect  

Last but not least, let me talk about an important nuance for running experiments on a social platform like LinkedIn — the **network effect**. A/B testing has a strong **Stable Unit Treatment Value Assumption (SUTVA)**, which assumes an individual user’s outcome is determined only by the treatment they receive, and is not affected by the treatments of other users. However, this does not always hold on social networks.

Considering the LinkedIn Games example — Assume we changed the leaderboard UI and, as a result, users in the treatment group have a higher chance to “nudge” their connections. And many “nudged” users — some in the control group — end up playing the game too. This network effect biases the experiment result and dilutes the relative impact between treatment and control. LinkedIn has [written](https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests) about this exact challenge and walked through how they detected the impact of this interference using cluster-based experiments. In short, LinkedIn groups closely-connected users into one cluster while minimizing interactions between clusters, then they use clusters as the randomization unit (users in the same cluster either all go to treatment or all go to control) to measure the impact with minimum interference. Therefore, for changes that could have a strong network effect, the cluster-based experiment is a good alternative. Though the trade-off is that cluster-based experiments often reduce power, so they require careful cluster construction and power analysis.  

---

LinkedIn Games seem simple, but behind every button, notification, streak badge, and leaderboard, there is likely a chain of product hypotheses, experiments, decisions, and data science work.  

Of course, this is just my brain exercise as a LinkedIn user, but I hope this article helps you better understand what Product Data Science looks like in practice. When preparing for product case interviews or even when you notice a new feature on a product you use regularly, you can apply similar mental exercises to sharpen your product sense and become a stronger data scientist.  
