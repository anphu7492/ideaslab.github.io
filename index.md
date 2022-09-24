---
title: Home
nav:
  order: 1
---

{% include section.html full=true %}
<video autoplay loop>
  <source src="/images/sequence.mp4" type="video/mp4">
</video>

{% include section.html full=false %}
# Welcome to IDEAS Lab

Welcome to the interdisciplinary research lab, [IDEAS](https://ideas.purdue.edu) (*Intelligent Design for Empathetic and Augmented Systems*) at Purdue Computer Science. Our research includes the design and implementation of scientific algorithms leveraging the "human in the loop" and their applications to computer graphics, robotics, AI, virtual environments, augmented intelligence, pedestrian and crowd dynamics, and medical / healthcare research.

Our research also focuses on building embodied computational models of human social behavior, developing component algorithms of an intelligent agent (from sensing, to decision-making, to actuating). Our long-term research goal is to create engaging, socially intelligent agents that can interact with humans in innovative ways through expressive multi-modal interaction.

Some recent work includes combining these methods with machine learning, computer vision, and physically-based modeling for Autonomous Driving, Affective Computing and Reconstructing Reality. In addition to publishing papers at the leading venues, we have a long history of developing software packages and transitioning our technology into industrial products.


{% include list.html component="card" data="tools" filters="group: home-thumbnails" style="medium" class="thumbnails md-3" %}

<!-- {%
  include link.html
  type="github"
  icon=""
  text="See the template on GitHub"
  link="greenelab/lab-website-template"
  style="button"
%}
{%
  include link.html
  type="docs"
  icon=""
  text="See the documentation"
  link="https://github.com/greenelab/lab-website-template/wiki"
  style="button"
%}
{:.center} -->

{% include section.html full=true %}

<div class="glider-contain">
  <div class="glider">
    <div><img src="images/home/slide1.jpg"></div>
    <div><img src="images/home/slide2.jpg"></div>
    <div><img src="images/home/slide3.jpg"></div>
    <div><img src="images/home/slide4.jpg"></div>
    <div><img src="images/home/slide5.jpg"></div>
    <div><img src="images/home/slide6.jpg"></div>
  </div>

  <div role="tablist" class="dots"></div>
</div>
<!-- {% include banner.html image="images/banner1.jpg" %} -->

{% include section.html %}

# Research highlights

{% include list.html 
  data="citations" 
  component="citation" 
  filters="group: highlight"
  style="rich" 
%}

<!-- {% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{%
  include link.html
  link="research"
  text="See what we've published"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

{%
  include link.html
  link="tools"
  text="Browse our tools"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="resources"
  title="Our Resources"
  flip=true
  text=text
%}

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include link.html
  link="team"
  text="Meet our team"
  icon="fas fa-arrow-right"
  flip=true
%}
{:.center}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Our Team"
  text=text
%}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. -->

# Follow us

{% capture col1 %}
  <div class="social">
    <a class="twitter-timeline" href="https://twitter.com/anikbera?ref_src=twsrc%5Etfw" data-height="700" data-width="350">Tweets by anikbera</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
  </div>
{% endcapture %}
{% capture col2 %}

{% endcapture %}
{% include two-col.html col1=col1 col2=col2 %}