---
layout: page
title: "活動レポート"
permalink: /reports/
description: "CoderDojo 京都四条 の活動レポート一覧。これまでの開催の様子をご紹介します。"
---

これまでの開催の様子をご紹介します。次回開催の参考にどうぞ。

{% if site.posts.size == 0 %}

> 📝 まだ活動レポートが投稿されていません。最新の開催情報は [開催情報ページ]({{ '/events/' | relative_url }}) と [Doorkeeper]({{ site.links.doorkeeper }}) からご確認ください。

{% else %}

<div class="report-list">
{% for post in site.posts %}
  <article class="report-item">
    <p class="report-meta">
      <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%Y年%-m月%-d日" }}</time>
      {% if post.event_no %} ／ 第{{ post.event_no }}回{% endif %}
      {% if post.participants %} ／ ニンジャ {{ post.participants }}名 参加{% endif %}
    </p>
    <h3 class="report-title">
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h3>
    {% if post.excerpt %}
    <p class="report-excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>
    {% endif %}
    <p><a href="{{ post.url | relative_url }}">続きを読む →</a></p>
  </article>
{% endfor %}
</div>

{% endif %}
