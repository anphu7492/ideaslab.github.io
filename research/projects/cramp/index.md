---
title: "DroNeRF"
redirect_from: "/research/dronerf/"
---

# [Optimizing Crowd-Aware Multi-Agent Path Finding through Local Broadcasting with Graph Neural Networks](https://arxiv.org/pdf/2309.10275)


<!-- <div class="embeded-video">
    <iframe src="https://www.youtube-nocookie.com/embed/p3i2XjWnOFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div> -->

<!-- demo video -->
<video width="100%" controls>
  <source src="/images/research/cramp/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<!-- <image alt="dronerf" src="/images/research/cramp/path_compare.jpg" width="50%" class="center"/> -->

### Abstract
{:.left}
Multi-Agent Path Finding (MAPF) in crowded environments presents a challenging problem in motion planning, aiming to find collision-free paths for all agents in the system. MAPF finds a wide range of applications in various domains, including aerial swarms, autonomous warehouse robotics, and self-driving vehicles. Current approaches to MAPF generally fall into two main categories: centralized and decentralized planning. Centralized planning suffers from the curse of dimensionality when the number of agents or states increases and thus does not scale well in large and complex environments. On the other hand, decentralized planning enables agents to engage in real-time path planning within a partially observable environment, demonstrating implicit coordination. However, they suffer from slow convergence and performance degradation in dense environments. In this paper, we introduce CRAMP, a novel crowd-aware decentralized reinforcement learning approach to address this problem by enabling efficient local communication among agents via Graph Neural Networks (GNNs), facilitating situational awareness and decision-making capabilities in congested environments. We test CRAMP on simulated environments and demonstrate that our method outperforms the state-of-the-art decentralized methods for MAPF on various metrics. CRAMP improves the solution quality up to 59% measured in makespan and collision count, and up to 35% improvement in success rate in comparison to previous methods.

{:.left}
### Citation

{:.left}
```
@misc{pham2024optimizingcrowdawaremultiagentpath,
      title={Optimizing Crowd-Aware Multi-Agent Path Finding through Local Communication with Graph Neural Networks}, 
      author={Phu Pham and Aniket Bera},
      year={2024},
      eprint={2309.10275},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2309.10275}, 
}
```
