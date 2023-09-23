---
title: "DroNeRF: Real-time Multi-agent Drone Pose Optimization for Computing Neural Radiance Fields"
redirect_from: /research/dronerf
---

# [DroNeRF: Real-time Multi-agent Drone Pose Optimization for Computing Neural Radiance Fields](https://arxiv.org/abs/2303.04322)


<!-- <div class="embeded-video">
    <iframe src="https://www.youtube-nocookie.com/embed/p3i2XjWnOFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div> -->

![dronerf](/images/research/dronerf/dronemain.jpg)

### Abstract
{:.left}

We present a novel optimization algorithm called **DroNeRF** for the autonomous positioning of monocular camera drones around an object for real-time 3D reconstruction using only a few images. Neural Radiance Fields, or NeRF, is a novel view synthesis technique used to generate new views of an object or scene from a set of input images. Using drones in conjunction with NeRF provides a unique and dynamic way to generate novel views of a scene, especially with limited scene capabilities of restricted movements. Our approach focuses on calculating optimized pose for individual drones while solely depending on the object geometry without using any external localization system. The unique camera positioning during the data capturing phase significantly impacts the quality of the 3D model. To evaluate the quality of our generated novel views, we compute different perceptual metrics like the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM). Our work demonstrates the benefit of using an optimal placement of various drones with limited mobility to generate perceptually better results. 

### Citation
{:.left}

```
@article{patel2023dronerf,
  title={DroNeRF: Real-time Multi-agent Drone Pose Optimization for Computing Neural Radiance Fields},
  author={Patel, Dipam and Pham, Phu and Bera, Aniket},
  journal={arXiv preprint arXiv:2303.04322},
  year={2023}
}
```
