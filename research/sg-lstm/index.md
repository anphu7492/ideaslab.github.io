---
title: SG-LSTM: Social Group LSTM for Robot Navigation Through Dense Crowds
---

# [SG-LSTM: Social Group LSTM for Robot Navigation Through Dense Crowds](https://arxiv.org/abs/2303.04320)


<!-- <p style="text-align:center;">
<img src="/images/research/sg-lstm-cover1.jpeg" alt="drawing" width="500"/>
<br>
<img src="/images/research/sg-lstm-cover2.jpeg" alt="drawing" width="600"/> -->
<!-- </p> -->

<!-- ![affect2mm](/images/research/sg-lstm-cover1.jpeg) -->


<p style="text-align:center;">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/p3i2XjWnOFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</p>

![affect2mm](/images/research/sg-lstm-cover2.jpeg)

### Abstract
{:.left}

As personal robots become increasingly accessible and affordable, their applications extend beyond large corporate warehouses and factories to operate in diverse, less controlled environments, where they interact with larger groups of people. In such contexts, ensuring not only safety and efficiency but also mitigating potential adverse psychological impacts on humans and adhering to unwritten social norms become paramount. In this research, we aim to address these challenges by developing a cutting-edge model capable of predicting pedestrian movements and interactions in crowded environments. To this end, we propose a novel approach called the Social Group Long Short-term Memory (SG-LSTM) model, which effectively captures the complexities of human group behavior and interactions within dense surroundings. By integrating social awareness into the LSTM architecture, our model achieves significantly enhanced trajectory predictions. The implementation of our SG-LSTM model empowers navigation algorithms to compute collision-free paths faster and with higher accuracy, particularly in complex and crowded scenarios. To foster further advancements in social navigation research, we contribute a substantial video dataset comprising labeled pedestrian groups, which we release to the broader research community. To thoroughly evaluate the performance of our approach, we conduct extensive experiments on multiple datasets, including ETH, Hotel, and MOT15. We compare various prediction approaches, such as LIN, LSTM, O-LSTM, and S-LSTM, and rigorously assess runtime performance. This research represents a significant step towards enabling personal robots to operate seamlessly and cooperatively in human-populated environments while ensuring their positive and socially acceptable integration into society.

### Annotated Dataset
![affect2mm](/images/research/sg-lstm-dataset-preview.png)

* [Download SG-LSTM Dataset](https://www.cs.purdue.edu/homes/bhaskarr/sg_lstm_dataset.html)

If you use this dataset, please cite it as:

*R. Bhaskara, M. Chiu, and A. Bera, “SG-LSTM: Social Group LSTM for Robot Navigation Through Dense Crowds.” arXiv, Mar. 07, 2023. doi: 10.48550/arXiv.2303.04320.*


### Publications
{:.left}

{%  include list.html 
    data="citations" 
    component="citation" 
    filters="tags: ~Robot navigation"
    style="" 
%}