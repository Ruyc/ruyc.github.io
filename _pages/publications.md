---
layout: page
permalink: /papers/
title: PAPERS
description: <a href = 'https://dblp.org/pid/02/41-2.html'>[dblp]</a><br>  (αβ)indicates alphabetical author order. * indicates equal contribution.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<br>

<div class='h2'>Journal</div>

<div class="publications">

{% bibliography --query @*[howpublished=journal]* %}

</div>

<br>

<div class='h2'>Conference</div>

<div class="publications">

{% bibliography --query @*[howpublished=conference]* %}

</div>

<br>


<div class='h2'>Working Papers</div>

<div class="publications">

{% bibliography --query @*[howpublished=preprint]* %}

</div>