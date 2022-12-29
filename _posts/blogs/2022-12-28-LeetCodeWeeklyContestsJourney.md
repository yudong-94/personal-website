---
title: "My Atypical LeetCode Weekly Contests Journey As a Data Scientist"
date: 2022-12-28
categories:
  - blog
tags:
  - learning
---

  
I did my first [Leetcode Weekly Contest](https://leetcode.com/contest/) back in April 2020 ([Contest 186](https://leetcode.com/contest/weekly-contest-186/)). Since then, I have been participating in the weekly contest almost every Saturday, and finished 123 of them. Honestly it is pretty uncommon for a person like me, who chose a data science career (especially analytics focus), to keep grinding Leetcode. Well, to be fair, I am not really grinding, but only doing the weekly contests. So I feel it might be interesting to write a post to share my experience and learnings.  
  
### My Background  
  
First, let me just quickly talk about my coding background so you know where I started.  
  
My first interaction with coding was in high school, when I learned some VB. It’s nothing advanced but writing some basic IF ELSE and loops, to conduct a bubble sort or check if a number is a prime number.  
  
But then I majored in accounting for undergrad, which means I didn't really have any coding classes (except for SQL if that counts). However, the more I studied accounting, the more I realized it’s not really my thing, especially after doing some internship. I started to take courses on Coursera (see more in [my online courses reviews](https://yudong-94.github.io/personal-website/blog/MOOCList/) to explore different fields, and eventually decided to come to the US for a Master’s degree in Business Analytics. One of the courses I took back then was the [Fundamentals of Computing Specialization by Rice University](https://www.coursera.org/specializations/computer-fundamentals). I was able to finish all the six courses and one capstone exam in this specialization in about nine months (while doing my undergrad). This specialization covers much of the material that first-year Computer Science students take at Rice University, and I got to learn things like BFS, DFS, graph algorithms, and dynamic programming, for the first time, and finished more than 20 projects in Python. And I found myself actually enjoying coding a lot.  
  
Then when I was at USC studying Business Analytics, of course I took some more technical courses, but mainly focusing on how to use R or Python for Data Science. I also did one course in Data Mining, where I learned Scala (which is not required in the class as you can choose Python or Scala), and was able to build a [movie recommender system](https://github.com/yudong-94/My-Movie-Recommender) from scratch using Spark and collaborative filtering algorithm.  
  
That’s pretty much about my coding background before I started the Leetcode Weekly Contest. In one sentence, I do have some limited experience, but never took any systematic CS education.  
  
### Why I Started  
  
The Leetcode story started in April 2020, when I was thinking about looking for a new job opportunity. It wasn’t because I was unhappy with my job back then, but I simply felt it was the time to try something new as someone early in the career. I was chatting with a friend who recently started a new position. He was a software engineer (so obviously he did not know much about DS interviews lol) and he said he did Leetcode Contest every week to practice coding skills. Honestly, I knew I would barely need to tackle any Leetcode algorithm questions in interviews based on my knowledge, and I myself was an interviewer from time to time. However, somehow I thought, well, maybe this was a good idea to practice Python as I was mainly using SQL in my job at that time, and it only took 90 minutes per week. So that’s how I started.  
  
Not surprisingly, the first one was a total failure -- I spent 17 minutes finishing the first question (with two errors), then I could not solve the second one in the remaining 73 minutes. My rank for that contest was 5780 / 11688. Leetcode Contest also has this Contest Rating thing, which compares your contest performance against all the other participants and updates your culumative rating after each contest. It has a baseline of 1500 points, but after the first contest, my rating was down to 1480… That was very sad but somehow motivated me as I did not want to stop there and I wanted to prove myself.  
  
### My Leetcode Weekly Contests Journey  
  
As I did not want to spend extra time grinding Leetcode (as I knew it was very unlikely to see those questions in my interviews), my strategy was to make the best use of the weekly contests. I kept abstracting the questions and googling during the contest, and after the contests end, I read the discussion forum and the solutions posted by other participants so I could always learn something. And this worked. Each contest has four questions -- usually one Easy, two Medium, and one Hard. After refreshing the basics like the Big O notation of common operations and algorithms, I was able to solve the first three questions in my fourth contest for the first time. The rating trend represents the learning curve pretty well. In the first year of participating in the contest, I was able to uplevel my contest rating from 1480 to 1954. After then, the progress became much slower as you can imagine, but I did not stop as it has become my Saturday night routine.   
  
![LeetCode Screenshot 1](/assets/images/Leetcode Screenshot 1.png)  
  
Now after 123 contests, I usually have no problem solving the first three in 30-40 minutes, and with some luck, I can solve the fourth question occasionally (solved them 8 times in the most recent 20 contests). I have reached a rating of 2153, which is top 1.32% among all contest participants. And I have solved almost 400 questions, including 31 Hard. Skill wise, I remember one year ago, I was still struggling understanding many of the dynamic programming (DP) solutions in the discussion board, but now I can design my own DP solution during the contest. I am pretty confident in when I can use algorithms like binary search and techniques like two pointers. And in many cases, I am able to tell if a solution will get TLE (Time Limit Exceeded) given the data size and big O, before actually trying it out. So honestly I am pretty happy and proud of what I have achieved.  
  
![LeetCode Screenshot 2](/assets/images/Leetcode Screenshot 2.png)  

  
### Does It Help Anything?  
  
Now let’s go back to the reality: I am a data scientist, with analytics focus, i.e. DSA. So, is participating in Leetcode contests helpful in any means? Well, yes and no.  
  
As I mentioned I was preparing for DS interviews when I started doing Leetcode contests. But during the interview process, I only had one company that actually asked me some Python algorithm questions, but it’s the easiest of Leetcode Easy level questions (much easier than two-sum). And obviously, the chances that I will write the Python algorithms I learned from the contests at work is close to 0 (and I highly doubt if Software Engineers would write Leetcode-style code at their work). However, the Python practices and the algorithmic thinking training is definitely helpful. Here are two real examples:  

Last month at work I noticed one table, whose primary key was supposed to be ‘id’, actually had duplicate ‘id’s. The table logic was written in a large SQL script. It was essentially left joining 30+ tables to one base table, and getting one or more columns from each joined table. So it was likely getting duplicate ‘id’s from one of these joins. But how should I locate which one it is? Well, this was a perfect time to do something similar to binary search -- I commented out the second half of the left joins, and checked if ‘id’ was distinct with only the first half of the joins. It turned out to be unique, so I knew the bad join was among the second half, so I did another ‘binary search’ in the second half of joins, and repeated this process. And after only 5 tries, I was able to locate the bad join and get it fixed.  
  
And here is another example. There was one time I was helping a product team to prioritize their content strategy. Each content could only cover a certain percentage of audience (users), and two contents could have audience overlap. I was asked to find the smallest combination of contents that can get us to a X% coverage of all users. This was likely an NP-hard problem. We had a very large number of content candidates and users, so just looping through all the combinations obviously would not work either. But as we did not need a very precise optimal solution based on my understanding of the business question and my conversation with stakeholders, I decided to code a quick greedy solution in Python, that simply found the best content that would increase overall user coverage the most at each step, then loop until we reached the target coverage. This provided the desired answer in a short amount of time.  
  
So here is my conclusion -- Doing Leetcode weekly contests does not help my daily job directly, but it has been a great learning experience. Moreover, I firmly believe that every effort you make will pay off one day in some (maybe unexpected) ways.  
