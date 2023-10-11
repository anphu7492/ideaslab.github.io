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
{:.bigger}
Welcome to the interdisciplinary research lab, [**IDEAS**](/) (*Intelligent Design for Empathetic and Augmented Systems*) at Purdue Computer Science. Our research includes the design and implementation of scientific algorithms leveraging the “human in the loop” and their applications to robotics, computer graphics, AI, virtual environments, augmented intelligence, pedestrian and crowd dynamics, and medical / healthcare research.

Our research also focuses on building embodied computational models of human behaviors, and developing component algorithms of an intelligent agent (from sensing, to decision-making, to actuating). Our long-term research goal is to create engaging, socially intelligent agents that can interact with humans in innovative ways through expressive multi-modal interaction.

Some recent work includes combining these methods with machine learning, computer vision, and physically-based modeling for Multi-Agent Dynamics, Heterogenous Robotics, Autonomous Driving, Affective Computing and Virtual Reality. In addition to publishing papers at the leading venues, we have a long history of developing software packages and transitioning our technology into industrial products.


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
  <div class="col col-2 home-news">
    <div class="news-item">
      <div class="date">{{ '2023-06-21' | date: "%d %b %Y" }}</div>
      <div class="content">
        Three IDEAS papers were accepted at <b>IROS 2023</b>! With this, in 2023, IDEAS published a total of five papers in the top robotics venues (ICRA+IROS)!
      </div>
    </div>
    
    <div class="news-item">
      <div class="date">{{ '2023-05-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        <b>Prof. Bera</b> awarded the Ross-Lynn Research Scholar Grant
      </div>
    </div>
    
    <div class="news-item">
      <div class="date">{{ '2023-05-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        <a href="/coverage"><b>IDEAS robotics</b> covered by multiple media outlets like NPR, Bloomberg, ABC News, etc.</a>
      </div>
    </div>
    
    <div class="news-item">
      <div class="date">{{ '2023-02-13' | date: "%d %b %Y" }}</div>
      <div class="content">
        <b>IDEAS research</b>  was covered in <a href="https://www.purdue.edu/newsroom/releases/2023/Q1/youve-got-to-have-heart-computer-scientist-works-to-help-ai-comprehend-human-emotions.html">Purdue news</a>
      </div>
    </div>
    <div class="news-item">
      <div class="date">{{ '2023-01-19' | date: "%d %b %Y" }}</div>
      <div class="content">
        <b>IDEAS research</b>  was covered in <a href="https://www.npr.org/sections/health-shots/2023/01/19/1147081115/therapy-by-chatbot-the-promise-and-challenges-in-using-ai-for-mental-health">NPR news</a>
      </div>
    </div>
    <div class="news-item">
      <div class="date">{{ '2023-01-06' | date: "%d %b %Y" }}</div>
      <div class="content">
        <b>Paper accepted at ICRA 2023</b> for
        <i>EWareNet: Emotion Aware Human Intent Prediction and Adaptive Spatial Profile Fusion for Social Robot Navigation</i>
      </div>
    </div>
    <div class="news-item">
        <div class="date">{{ '2023-01-06' | date: "%d %b %Y" }}</div>
        <div class="content">
          <b>Paper accepted at ICRA 2023</b> for
          <i>AZTR: Aerial Video Action Recognition with Auto Zoom and Temporal Reasoning</i>
        </div>
    </div>
    <div class="news-item">
        <div class="date">{{ '2022-11-05' | date: "%d %b %Y" }}</div>
        <div class="content">
          <b>Best Paper Award in ACM SIGGRAPH MIG 2022</b> for
          <i>Learning Gait Emotions Using Affective and Deep Features</i>
        </div>
    </div>
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
    
    {%
      include link.html
      link="news"
      text="Read more"
      icon="fas fa-arrow-right"
      flip=true
    %}

  </div>

  <div class="col col-2 social">
    <a class="twitter-timeline" href="https://twitter.com/IDEASPurdue" data-height="700" data-width="330">Tweets by IDEAS Lab</a> 
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
  </div>
</div>
