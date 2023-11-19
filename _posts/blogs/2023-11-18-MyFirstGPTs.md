---
title: "My First GPTs"
date: 2023-11-18
categories:
  - blog
tags:
  - gpt
  - coding
  - website
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

In my [previous post](https://yudong-94.github.io/personal-website/blog/BlogUpdateWithGPT/), I delved into the exciting realm of OpenAI's latest offerings, setting the stage for an even more intriguing exploration this week. Today, I'm excited to share my hands-on experience with custom GPTs, showcasing both successes and learning curves.

### *Credit Card Advisor*: A Simple Text-based GPT

My first venture was into a text-based GPT, driven by my recent credit card research experience. I navigated through sites like NerdWallet and WalletHub, sparking the idea of a GPT that tailors credit card recommendations to individual needs and preferences.

The GPT creation process, streamlined through the 'GPT Builder' in the 'Create' tab, was remarkably user-friendly, guiding me through each step. I enabled 'Web Browsing' capability for this GPT, so it searches the web but also summarizes and formats the information neatly.

Curious to see it in action? Experience the the Credit Card Advisor [here](https://chat.openai.com/g/g-8gOkzaczl-credit-card-advisor).  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/credit_card_gpt_setup1.jpg" alt="Credit Card Advisor GPT Setup 1" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/credit_card_gpt_setup2.jpg" alt="Credit Card Advisor GPT Setup 2" width="300" height="400">
</div>

### *Purrfect Tales Illustrator*: Blending External API with DALLE3

Next, I ventured into combining GPT with external APIs and DALLE3. Utilizing the 'Configure' tab, I integrated the whimsical [meowfacts](https://github.com/wh-iterabb-it/meowfacts) API, which serves random cat facts. The GPT then collaborates with DALLE3 to transform these facts into charming four-panel comic strips.

Discover the creativity of the [Purrfect Tales Illustrator](https://chat.openai.com/g/g-YiCtRzp8i-purrfect-tales-illustrator), aptly named by GPT itself.

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/cat_fact_gpt_setup.jpg" alt="Cat Fact GPT Setup" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/cat_fact_gpt_outcome.jpg" alt="Cat Fact GPT Example" width="300" height="400">
</div>

### *Hyrule Villager*: Elevating API Integration

To challenge the GPT further, I interacted with the [Hyrule-Compendium-API](https://github.com/gadhagod/Hyrule-Compendium-API), which contains info of one of my faviorate games '*The Legend of Zelda: Breath of the Wild*'. This GPT automatically picks up any item or regions the user mentioned and passes it to the API to collect info. It then masquerads as a Hylian villager, weaves the API responses into humorous stories.  

Chat with the Hyrule Villager [here](https://chat.openai.com/g/g-0IWi7Ue96-hyrule-villager).  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/hyrule_villager_gpt_setup.jpg" alt="Hyrule Villager GPT Actions Setup" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/hyrule_villager_gpt_outcome.jpg" alt="Hyrule Villager GPT Example" width="300" height="400">
</div>

### *Data Analysis Report Creator*: Merging Knowledge Base with Code Interpreter

Intrigued by GPT's potential in data analysis, I created a GPT equipped with a Code Interpreter. In this GPT, I provided instructions on data analysis practices. I also uploaded an analysis report template and some examples to the knowledge base, and asks the GPT to generate a report in DOCX following the format (but please note that it fails to follow the format from time to time, and I still need to do more prompt engineering).

Despite its impressive capabilities, I observed notable gaps in its ability to produce statistically sound and business-actionable analyses. These insights, which I'll detail in a future post, highlight the need for further advancements in AI-driven data science.

Test the Data Analysis Report Creator [here](https://chat.openai.com/g/g-PwcNwRMyE-data-analysis-report-creator) and see its capabilities for yourself.  

<div class="container">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/data_analysis_gpt1.jpg" alt="Data Analysis Report Creator Example" width="300" height="400">
  <img src="https://yudong-94.github.io/personal-website/assets/images/gpt-screenshots/data_analysis_gpt2.jpg" alt="Data Analysis Report Creator Result" width="300" height="400">
</div>

### Conclusion  

Not all my experiments turned into GPTs:   
* I tried to set up 'Actions' with more comprehensive APIs like the Google Slides API, but had no luck there given the complexity.
* I also tried the Zapier action, which is also presented in the OpenAI DevDay demo. Due to privacy and security concerns, I was a bit hesitate to actually build any GPT on top of it.  

This exploration has been a phenomenal learning experience, igniting my enthusiasm to delve deeper into the world of GPTs.
