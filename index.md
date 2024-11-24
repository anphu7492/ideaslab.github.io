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
Welcome to the interdisciplinary research lab, IDEAS (Intelligent Design for Exploration and Augmented Systems), housed within Purdue Computer Science. Our lab is dedicated to advancing state-of-the-art in robotics, computer vision, AI, and virtual environments. Our research bridges multiple domains, with a strong emphasis on leveraging human-centered insights and machine intelligence to tackle real-world challenges in robotics, computer vision/graphics, and artificial intelligence.

####  Research Themes
{:.bigger}
Our research spans the following key areas:
1. **Motion Planning**: We develop advanced motion planning algorithms that address real-world challenges, including navigating difficult terrains, dynamic obstacle avoidance, and multi-agent coordination. Our approaches integrate geometric methods with learning-based models to enable autonomous systems, such as ground and aerial robots, to operate robustly in complex and unstructured environments.
2. **Neural Models for Planning and Prediction**: Leveraging physics-informed neural networks and generative models, we focus on enhancing the adaptability and decision-making of intelligent agents. This includes designing algorithms for planning under uncertainty, modeling human behaviors, and predicting motions in dynamic and interactive settings.
3. **Computer Vision and Graphics**: Our lab also works on computer vision and graphics through projects in human motion generation, scene generation, 3D modeling, and generative models. This includes synthesizing realistic human movements for character animation, reconstructing 3D environments from multimodal sensor data, and generating immersive virtual scenes for applications in VR/AR and autonomous systems.
4. **Human-Agent Interaction and Simulation**: We also work on embodied computational models of human behavior, enabling agents to understand and predict human intent, behaviors, and social dynamics. These agents can engage in expressive, multi-modal interactions in virtual environments, robotics, and real-world human-machine collaboration scenarios.
5. **Field and Aerial Robotics**: Our lab addresses the challenges of deploying robots in diverse operational domains, from field robotics that navigate rugged terrain to aerial systems for surveillance, delivery, and exploration. We combine reinforcement learning, computer vision, and physics-based modeling to enhance autonomy and situational awareness in these systems.
6. **Generative AI and Machine Learning**: We explore generative AI models for tasks such as motion synthesis, environmental modeling, and data augmentation. This includes employing diffusion models and other generative techniques to create realistic simulations, support planning in complex environments, and design virtual agents for interactive applications.

#### Mission and Long-Term Goals
{:.bigger}
Our mission is to develop intelligent systems that seamlessly integrate sensing, decision-making, and actuation to navigate and interact with complex, dynamic environments. Our research enables AI, robotics, and virtual agents to better understand human behavior and intent, fostering collaborative and socially aware interactions. These technologies have transformative implications for industries such as healthcare, transportation, entertainment, and defense.

We aim to ensure our research has both academic impact and practical utility. Our lab's innovations have led to advancements in human-robot collaboration, multi-agent systems, autonomous driving, and immersive virtual environments.

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
