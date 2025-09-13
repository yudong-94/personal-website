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

{% if pinned and pinned.size > 0 %}
### Featured
{% for post in pinned %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
{% endif %}

{% assign groups = others | group_by_exp: 'post', "post.date | date: '%Y'" %}
{% assign groups_sorted = groups | sort: 'name' | reverse %}

<nav class="year-nav">
  <strong>Jump to year:</strong>
  {% for group in groups_sorted %}
    <a href="#{{ group.name }}">{{ group.name }}</a>{% unless forloop.last %} · {% endunless %}
  {% endfor %}
  <hr />
  </nav>

<div class="paginated-list" data-page-size="3">
{% for group in groups_sorted %}
  <section class="year-section">
    <h2 id="{{ group.name }}">{{ group.name }}</h2>
    {% assign posts_sorted = group.items | sort: 'date' | reverse %}
    {% for post in posts_sorted %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
  </section>
{% endfor %}
</div>
