---
title: "Data Viz"
permalink: /data-viz/
layout: archive
author_profile: true
entries_layout: list
---
{% assign cat_posts = site.categories["data viz"] %}
{% assign pinned = cat_posts | where: "pin", true %}
{% assign others = cat_posts | where_exp: "p", "p.pin != true" %}
{% assign sorted_others = others | sort: "date" | reverse %}
{% assign posts_to_show = pinned | concat: sorted_others %}

{% for post in posts_to_show %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}