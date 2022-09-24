---
title: Tools
# nav:
  # order: 5  # comment out to hide
  # tooltip: Software, datasets, and more
---

# <i class="fas fa-tools"></i>Tools

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{% include search-info.html %}

{% include section.html %}

## Featured

{% include list.html component="card" data="tools" filters="group: featured" %}

{% include section.html %}

## More

{% include list.html component="card" data="tools" filters="group: more" style="small" %}


{% capture text %}
<div class="date">{{ "3/10/2022" | date: "%d %b %Y" }}</div>

🏆 Best Paper Award (Honorable Mention) in IEEE VR 2022 for ENI: Quantifying Environment Compatibility for Natural Walking in Virtual Reality

{%
  include link.html
  link="research"
  text="Read more"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.left}
{% endcapture %}

{%
  include feature.html
  image="images/papers/ENI.jpg"
  link="research"
  title="Best Paper Award at IEEE VR 2022"
  text=text
%}

{% capture text %}
<div class="date">{{ "10/1/2021" | date: "%d %b %Y" }}</div>
🏆 Best Paper Award (Honorable Mention) in ISMAR 2021 for Redirected Walking in Static and Dynamic Scenes Using Visibility Polygons (🎉 Awarded 3 Virtual Reality awards in 2021 🎉)
{:.left}
{% endcapture %}

{%
  include feature.html
  image="images/papers/walk_polygons.jpg"
  link="research"
  title="Best Paper Award at ISMAR 2021"
  text=text
%}



{% capture text %}
<div class="date">{{ "4/1/2021" | date: "%d %b %Y" }}</div>

🏆 Best Paper Award in IEEE Virtual Reality 2021 for Text2Gestures: A Transformer-Based Network for Generating Emotive Body Gestures for Virtual Agents

{:.left}
{% endcapture %}

{%
  include feature.html
  image="images/papers/text2gesture.jpg"
  link="research"
  title="Best Paper Award at IEEE VR 2021"
  text=text
%}

{% capture text %}
<div class="date">{{ "4/1/2021" | date: "%d %b %Y" }}</div>

🏆 Honorable Mention in IEEE Virtual Reality 2021 for ARC: Alignment-based Redirection Controller for Redirected Walking in Complex Environments

{:.left}
{% endcapture %}

{%
  include feature.html
  image="images/papers/ARC.jpg"
  link="research"
  title="Best Paper Award at IEEE VR 2021"
  text=text
%}