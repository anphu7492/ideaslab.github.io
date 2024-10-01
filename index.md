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
      <div class="date">{{ '2024-06-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS has <b>three papers accepted at IROS 2024</b>.
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-02-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS has <b>four full papers at CVPR 2024</b>.
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-02-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS Lab published 5 papers in ICRA 2023 and IROS 2023.
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-01-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        Team JARVIS not only represented Purdue University for the first time at the finals of the prestigious NASA Suits competition but also brought home the "Pay it Forward" award for our exceptional team spirit and helping attitude!
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-01-30' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS has <b>one paper at AAAI 2024</b>.
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-01-20' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS Lab along with the Krach Institute for Tech Diplomacy at Purdue to develop a course on "Human-Machine Teaming".
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2024-01-20' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS organized Multi-modal Affective and Social Behavior Analysis and Synthesis in Extended Reality (MASSXR) workshop at IEEEVR 2024.
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2023-11-20' | date: "%d %b %Y" }}</div>
      <div class="content">
        IDEAS lab co-organized ACM SCA (Symposium of Computer Animation) 2023
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2023-11-20' | date: "%d %b %Y" }}</div>
      <div class="content">
        Our Lab IDEAS's Research on AI-driven Human-centric Robotics was recently featured by WRTV / ABC News
      </div>
    </div>

    <div class="news-item">
      <div class="date">{{ '2023-11-20' | date: "%d %b %Y" }}</div>
      <div class="content">
        Our Lab IDEAS's Research (and other industry and academic researchers working on this very necessary yet complicated AI for mental health space) discussed in NPR article
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
