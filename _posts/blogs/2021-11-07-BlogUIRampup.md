---
title: "How I Ramped Up My Blog Site UI"
date: 2021-11-07
categories:
  - blog
tags:
  - learning
---

This weekend, I spent ~5 hours ramping up the UI of this personal website. Previously, it was using the default 'slate' Jekyll theme, which was set up directly from Github Pages settings. But now, it is using a custom Jekyll theme [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes/).  

### Some Background

I initially set up this website via [Github Pages](https://pages.github.com/) in 2018. I really love this neat way of publishing a website -- everything sits in a Github repo. You just need some simple clicks and it will read from markdown files and deploy them into a website. Of course, it can also read HTML, javascript, CSS, etc. But for me, who do not have much knowledge/experience on front-end languages, this is the easiest way to build a portfolio website.  

### The Challenge

However, there is always a trade off between simplicity and customizability. Spinning up a website with markdown pages are super straightforward, but it only has minimal functions -- no nav bar, no search, and pages are just linked together using a bunch of hyperlinks written in markdown. With more and more pages being added to the site, I started feeling that it became less organized and the UI did not look great :(  

### The Solution

The most obvious solution is to rewrite everything with html, javascript, and CSS. Unfortunately, I am not a front-end engineer and honestly, learning all these is a pain (that's why I've never really started visualizing data with d3.js).  
Then the best solution I can get to quickly is to use some custom Jekyll theme ([Github post](https://github.blog/2017-11-29-use-any-theme-with-github-pages/)). After some searches, I decided to try out the most popular Jekyll theme [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes/). Below are some steps I went through.

##### 1 - Installation

Following the [installation instruction](https://github.com/mmistakes/minimal-mistakes#remote-theme-method), I tried the 'remote theme method'. The first challenge I encountered was, I could not run `bundle`...... And the reason was my ruby version was too old. Makes sense as I had never used ruby lol. Then after a series of searches on stackoverflow, I was able to solve the problem. In short, ruby too old -> update with homebrew -> homebrew also too old -> uninstall and reinstall homebrew... So I successfully completed the steps listed, but got the email saying 'Page Build Failed'.  

I think I definitely messed up something with ruby, but I was not sure how to resolve it. But luckily I saw this in the instruction: `Looking for an example? Use the Minimal Mistakes remote theme starter for the quickest method of getting a GitHub Pages hosted site up and running. Generate a new repository from the starter, replace sample content with your own, and configure as needed.` So I used the theme starter, which essentially created a new github pages repo with the necessary setups of this theme. Then I went through the starter repo and compared it with my existing repo, and basically copied/modified every setting files that looks different. And it worked!  

With that being said, if you are setting up a brand new GitHub pages website, I would recommend just starting with [this remote theme starter](https://github.com/mmistakes/mm-github-pages-starter/generate) and then add files on top of it.  

##### 2 - UI Customization
Now that the website is deployed successfully with the new theme, let's do some customization.  
Going through the `_config.yaml` file, I updated the basic info of the site, including title, description, github and LinkedIn urls, bio photo, and Google Analytics setting. Of course, I also updated the about page.  

This theme also comes with very handy setup of navigation bar, category archives, and search by tags features. Therefore, I updated my `navigation.yml` file accordingly.  


##### 3 - Posts Re-organization

Last but not least, I need to reorganize my files under the new structure that it can read from. Again, looking at the website published with the starter repo, I was able to gain a good understanding of which pages would flow into the 'Recent Posts' thread, where the files should be located, and how I should structure the files. Then I understood I need to do the followings:
1. Move all posts to the `_posts` folder;
2. Update the file name to `YYYY-MM-DD-filename.md` format;
3. Add a header section to all the post files, specifying its title, date, category and tag -- this will enable the group by year / category / tag features;
4. Also as the theme automatically pulls the first few sentences on the thread as a preview, I need to adjust the first paragraph accordingly.  

This could takes a long time if I do it manually, as I already have over 200 posts (mostly with the weekly viz series). So it's the time to write some Python :)  
First let's import necessary packages:  
```
import glob
import os
import re
import numpy as np
import pandas as pd
```
Then let's read the files in the directory and rename the filenames. Originally, their names followed the pattern of `filename-YYYYMMDD.md`, so I need to parse the YYYYMMDD out of the file name, and append it at the beginning as YYYY-MM-DD format.  
```
dir = r'/Documents/GitHub/personal-website/_posts/projects/data_viz'
pattern = r'*[0-9]*'
for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    year = title[-8:-4]
    month = title[-4:-2]
    day = title[-2:]
    new_title = year+'-'+month+'-'+day+'-'+title
    os.rename(pathAndFilename, os.path.join(dir, new_title + ext))
```
Next, we need to bulk update the content of the files. More specifically, to add the header section and remove the redundant titles and previous/next hyperlinks I put at the end of each file (we don't need them anymore as this theme comes with a nice-looking previous/next navigator).  
```
def content_update(dir, filename):
    ### create new header ###
    date = filename[:10]
    # viz is a data frame I prepared that has two colums -- Date (YYYYMMDD) and Topic (topic of weekly viz)
    topic = viz[viz['Date'] == ''.join(date.split('-'))]['Topic'].values[0]
    new_title = 'Weekly Viz ' + date

    # create new header
    new_header = '---
title: "%s"
date: %s
categories:
  - data viz
tags:
  - data visualization
  - tableau
---
### *%s*
'%(new_title, date, topic)

    ### create new file content ###
    file = open(dir+'/'+filename, "r")
    content = file.read()
    # find the location of the old title which looks like '## Data Visualization -- YYYYMMDD'
    header_match = re.search('## Data Visualization --.*', content)
    # find the location of the nav links at the end
    end_match = re.search('--  \n\[⬅️Previous\]', content)
    # append the new header, remove everything before the old title ends, and after the old nav starts
    new_content = new_header + content[header_match.end():end_match.start()]

    ### replace file ###
    file.close()
    # opening the file in write mode
    fout = open(dir+'/'+filename, "w")
    fout.write(new_content)
    fout.close()
dir = r'Documents/GitHub/personal-website/_posts/projects/data_viz'
pattern = r'*[0-9]*'
for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
    filename = os.path.basename(pathAndFilename)
    content_update(dir, filename)
```

These code snippets helped me migrating my 200+ posts quickly.

### Final Thoughts

Revamping the site UI has been on my to do list for a while. As we are approaching the end of the year, I finally spent some time making the updates. I am pretty happy with the new look, and it is a good learning experience. But there is much more I can add -- this custom theme also offers the capability of further customizing the layouts, adding comments features, sidebar navigation, [etc](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/). I am sure it would be fun to explore some of those applications.  

I hope this post is helpful for your own portfolio site :)  
