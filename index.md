---
layout: default
title: "Sugar Bear's Soft Spot"
description: "A Fuzzy Calculus bedtime story about little comforts, big dreams, and making a soft place for tomorrow's Bear. By Paul Carver Tiffany III. For Yvonne."
image:
  path: /social-preview.jpg
  width: 1774
  height: 887
  alt: "Sugar Bear's Soft Spot. Sugar Bear hugs his pillow beside Bunny in a warm, moonlit bedroom."
---
{% comment %}
Keep README as the book's single source. GitHub resolves its relative issue
links within the current repository; Pages needs that repository's full URL.
The .github directory is not published by Jekyll, so link back to its sources.
{% endcomment %}
{% capture book %}{% include_relative README.md %}{% endcapture %}
{% assign issues = site.github.repository_url | append: '/issues/' %}
{% assign github_files = site.github.repository_url | append: '/blob/' | append: site.github.source.branch | append: '/.github/' %}
{{ book | replace: '../../issues/', issues | replace: '.github/', github_files }}
