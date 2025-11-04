---
title: "Modeling Shifts in U.S. Energy Discourse: A Text Analysis of Media and Regulatory Communications "
date: 2025-04-22
categories:
  - blog
tags:
  - data science
  - machine learning
  - llm
header:
  teaser: /assets/images/article_covers/ds_agent_cover.jpg
excerpt: "I tested Google’s Data Science Agent in Colab—here’s what it got right (and where it failed)."
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

---



---
title: "Modeling Shifts in U.S. Energy Discourse: A Text Analysis of Media and Regulatory Communications "
excerpt: "Using NLP and topics modelling to uncover trends in energy policy communication, especially during the 2024-2025 political transition." 
---
A lot of changes are underway in the energy sector. With energy-hungry data centers and changes in priorities for clean energy, these changes are often reflected in the media. 

## Data 
The data is from a collection of news articles from Febuary - July 2024 to  Febuary - July 2025. One of the goals is to compare 2024 to 2025 so similar time period were taken. The corpus includes media sources from across the spectrum, left and right leaning, with a slight technical focus. The sources include The New York Times, EnergyWire, Politico and many others.
In total there are 4874 articles. 


##Modelling
We can use an LDA model using BoW as a baseline. Latent Dirchlet Allocation (not do be confused with Linear Discriminant Analysis) is a probabilistic topic modelling technique. It applies unsupervised learning on text data, meaning it find structure/patterns in unlabelled data. LDA generated topics, taking words and classifying them into distinct themes. Since this is a probabilistic model, we need to ensure that it is producing cohesive topics, the number of topics matters a lot for this. We can evalutating this by eyeballing the produced topics, but another technique used is the coherence metric. A topic's coherence score measures the co-occurrence frequency of each word pair from a topic’s top n words against each individual’s word’s frequency across the corpus. This aims to quantify how coherent a given topic is. 

