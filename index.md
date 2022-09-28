---
title: Home
nav:
  order: 1
---

{% include section.html full=true %}
<video autoplay loop muted id="home-vid">
  <source src="/images/sequence.mp4" type="video/mp4">
</video>

{% include section.html full=false %}
# Welcome to IDEAS Lab

Welcome to the interdisciplinary research lab, [IDEAS](https://ideas.purdue.edu) (*Intelligent Design for Empathetic and Augmented Systems*) at Purdue Computer Science. Our research includes the design and implementation of scientific algorithms leveraging the "human in the loop" and their applications to computer graphics, robotics, AI, virtual environments, augmented intelligence, pedestrian and crowd dynamics, and medical / healthcare research.

Our research also focuses on building embodied computational models of human social behavior, developing component algorithms of an intelligent agent (from sensing, to decision-making, to actuating). Our long-term research goal is to create engaging, socially intelligent agents that can interact with humans in innovative ways through expressive multi-modal interaction.

Some recent work includes combining these methods with machine learning, computer vision, and physically-based modeling for Autonomous Driving, Affective Computing and Reconstructing Reality. In addition to publishing papers at the leading venues, we have a long history of developing software packages and transitioning our technology into industrial products.


{% include list.html component="card" data="tools" filters="group: home-thumbnails" style="medium" class="thumbnails md-3" %}


{% include section.html %}

<!-- # Research highlights

{% include list.html 
  data="citations" 
  component="citation" 
  filters="group: highlight"
  style="rich" 
%} -->


# Follow us

<div class="col-flex">
  <div class="col home-news">
    <div class="news-item">
    <div class="date">{{ '2022-09-15' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Paper accepted at MIG 2022</b>
       <i>(Learning Gait Emotions Using Affective and Deep Features)</i>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-08-20' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Paper accepted at WACV 2023 </b> (Placing Human Animations into 3D Scenes by Learning Interaction- and Geometry-Driven Keyframes)
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-08-15' | date: "%d %b %Y" }}</div>
    <div class="content">
      IDEAS Lab moved to <b>Purdue University</b>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-05-10' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Appointed as Senior Editor for IEEE Robotics and Automation Letter (RA-L)</b> in the area of <i>Planning and Simulation</i>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-5-10' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Grant Awarded by "TEDCO (Maryland Technology Development Corporation)"</b> for <a href="https://dost.cs.umd.edu/">Project Dost</a>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-3-10' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Best Paper Award (Honorable Mention)</b> in in IEEE VR 2022 for <i>ENI: Quantifying Environment Compatibility for Natural Walking in Virtual Reality</i>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-3-20' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Paper accepted at CVPR 2022</b> <i>(3MASSIV: Multilingual, Multimodal and Multi-Aspect dataset of Social Media Short Videos)</i>
    </div>
  </div>

  <div class="news-item">
    <div class="date">{{ '2022-10-01' | date: "%d %b %Y" }}</div>
    <div class="content">
      <b>Best Paper Award (Honorable Mention) in ISMAR 2021</b> for <i>Redirected Walking in Static and Dynamic Scenes Using Visibility Polygons</i>
    </div>
  </div>

  {%
    include link.html
    link="news"
    text="Read more"
    icon="fas fa-arrow-right"
    flip=true
  %}

  </div>

  <div class="col social">
    <a class="twitter-timeline" href="https://twitter.com/IDEASPurdue" data-height="700" data-width="330">Tweets by IDEAS Lab</a> 
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
  </div>
</div>
