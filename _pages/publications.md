---
layout: page
permalink: /papers/
title: PAPERS
description: <a href = 'https://dblp.org/pid/02/41-2.html'>[dblp]</a><br> ❈ indicates alphabetical author order
years: [2023,2022,2021]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
