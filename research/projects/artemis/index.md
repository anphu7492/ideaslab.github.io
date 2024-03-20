---
title: "Artemis"
redirect_from: "/research/artemis/"
---

<style type="text/css">
  table td {
    border: none !important;
    padding: none !important;
  }
</style>

# [ARTEMIS: AI-driven Robotic Triage Labeling and Emergency Medical Information System](#abstract)


<div class="embeded-video">
    <iframe width="720" height="405" src="https://www.youtube.com/embed/4FU4FRxNwmY?si=uBomhob13fTi9--T" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Abstract
{:.left}
Mass casualty incidents (MCIs) pose a significant challenge to emergency medical services by overwhelming available resources and personnel. Effective victim assessment is the key to minimizing casualties during such a crisis. We introduce ARTEMIS, an AI-driven Robotic Triage labeling and Emergency Medical Information System, to aid first responders in MCI events. It leverages speech processing, natural language processing, and deep learning to help with acuity classification. This is deployed on a quadruped that performs victim localization and preliminary injury severity assessment. First responders access victim information through a Graphical User Interface (GUI) that is updated in real-time. To validate our proposed algorithmic triage protocol, we used the Unitree Go1 quadruped. The robot identifies humans, interacts with them, gets vitals and information, and assigns an acuity label. Simulations of an MCI in software and a controlled environment outdoors were conducted. The system achieved a triage-level classification precision of over 74\% on average and 99\% for the most critical victims, i.e. level 1 acuity, outperforming state-of-the-art deep learning-based triage labeling systems. In this paper, we showcase the potential of human-robot interaction in assisting medical personnel in MCI events.

![artemis](/images/research/artemis/cover.png)

{:.left}
ARTEMIS System Architecture: a Unitree Go1 quadruped to be used for collecting patient vitals (Heart Rate, Respiratory Rate, $O_2$ Sat., Systolic and Diastolic Blood Pressure, etc.), chief complaints, and age. The Multi-Layer Perceptron (MLP) uses this to classify the patient's acuity level, which is then displayed on the GUI along with the patient's location and photograph.

<div class="column is-centered has-text-centered">
  <table>
    <tr>
      <td>
        <img src="/images/research/artemis/test.gif" alt="cars peace"/>
      </td>
      <td>
        <img src="/images/research/artemis/test2.gif" alt="cars peace"/>
      </td>
      <td>
        <img src="/images/research/artemis/spot.gif" alt="cars peace" />
      </td>
    </tr>
    <tr>
      <td>
        <img src="/images/research/artemis/test3.gif" alt="cars peace"/>
      </td>
      <td>
        <img src="/images/research/artemis/indoor.gif" alt="cars peace"/>
      </td>
      <td>
        <img src="/images/research/artemis/zoom.gif" alt="cars peace"/>
      </td>
    </tr>
  </table>
</div>

### Performance in Sim

The above animations showcase simulations performed in Gazebo Ros1 using Champ framework. 


![pose](/images/research/artemis/pose_detection.png)

### Pose detection

{:.left}
Example of robot demo run with an external view of the robot moving
(top) and a camera view from the robot’s perspective (bottom). The captures
from what the robot is seeing are sent over to first responders via the GUI

<!-- {:.left}
### Citation

{:.left}
```
@article{patel2023dronerf,
  title={DroNeRF: Real-time Multi-agent Drone Pose Optimization for Computing Neural Radiance Fields},
  author={Patel, Dipam and Pham, Phu and Bera, Aniket},
  journal={arXiv preprint arXiv:2303.04322},
  year={2023}
}
``` -->
