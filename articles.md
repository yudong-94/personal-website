---
title: "Articles"
permalink: /articles/
layout: archive
author_profile: true
entries_layout: grid
show_excerpts: true
---
<div class="paginated-list" data-page-size="12">
{% assign posts = site.categories.blog %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>
