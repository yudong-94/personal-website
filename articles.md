---
title: "Articles"
permalink: /articles/
layout: archive
author_profile: true
entries_layout: grid
show_excerpts: true
---
{% assign posts = site.categories.blog %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}