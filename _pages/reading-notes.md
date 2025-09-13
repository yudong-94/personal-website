---
title: "Reading Notes"
permalink: /reading-notes/
layout: archive
author_profile: true
entries_layout: list
---

<div class="paginated-list" data-page-size="15">
{% assign rn_posts = site.categories["reading notes"] | sort: 'date' | reverse %}
{% for post in rn_posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
</div>

