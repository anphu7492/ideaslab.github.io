---
title: AI in mental health
---

# AI in Mental Health

![ai-mental-health](/images/research/ai-mental-health-banner.jpg)

### Overview
{:.left}
A new research collaboration seeking to break down that electronic divide with artificial intelligence-based tools, bringing together computer scientists from the Purdue University and behavioral health clinical experts. It has been estimated that around 15.5% of the population suffers from mental illness globally, and these numbers are rising continuously. There is, however, a worldwide shortage of mental health providers. This, combined with issues related to affordability and reachability, has resulted in more than 50% of the mental health patients remaining untreated. The mental health landscape became even bleaker during the COVID-19 pandemic. However, the rapid expansion of telemental health services, especially during the pandemic, has increased access to clinical care options and introduced the opportunity to use artificial intelligence (AI) based strategies to improve the quality of human-delivered mental health services. Telemental health is the process of providing psychotherapy remotely, typically utilizing HIPAA compliant video conferencing. Given that it relies a lot on technology, experienced human therapists face challenges engaging with patients due to unfamiliarity with the setup as well as other factors. For instance, in a telemental health session, the therapist has limited visual data (e.g., a therapist can only view the patient's face rather than full body language), so the therapist has fewer non-verbal cues to guide their responses. It is also more difficult for the therapist to estimate attentiveness since eye contact required during in-person sessions is replaced with the patient looking at a camera or screen. Video conferencing discussions may also appear more stilted, especially if there is inadequate internet connection or technological challenges. Such challenges make it difficult for a therapist to perceive the patient's several mental health indicators like engagement level, valence and arousal. Our collaboration has developed multimodal AI-based framework for modeling patient and caregive engagement and affect. This automated engagement tool will give feedback to the provider in real-time, ultimately enhancing provider engagement training and improving quality of care.

### Lead investigators
{:.left}
- [Aniket Bera (Purdue University)](https://www.cs.purdue.edu/homes/ab/)
- [Gloria Reeves (UM Baltimore)](https://www.medschool.umaryland.edu/profiles/Reeves-Gloria/)

### Collaborators/Co-investigators
{:.left}
- [Dinesh Manocha (UMD College Park)](https://www.cs.umd.edu/people/dmanocha)
- [Pooja Guhan (UMD College Park)](https://www.linkedin.com/in/pooja-guhan)
- [Jill RachBeisel (UM Baltimore)](https://www.medschool.umaryland.edu/profiles/RachBeisel-Jill/)
- [Kristin Bussell (UM Baltimore)](https://www.nursing.umaryland.edu/directory/kristin-bussell/)
- [Mark Kvarta (UM Baltimore)](https://www.medschool.umaryland.edu/profiles/Kvarta-Mark/)
- [Susan DosReis (UM Baltimore)](https://faculty.rx.umaryland.edu/sdosreis/)
- [Naman Awasthi (UMD College Park)](https://www.linkedin.com/in/naman-awasthi)
- [Kathryn McDonald (UM Baltimore)](https://www.linkedin.com/in/kathryn-mcdonald-65a139a4)

### Research
{:.left}
* We developed a novel framework that models telemental health session videos. Our algorithm takes into account different components of engagement defined in the psychology literature, namely - Affective and Cognitive engagement. These components are incorporated as the modalities in our multimodal framework.

* We developed a novel regression-based framework that can capture psychology-inspired cues capable of perceiving the different important psychological indicators useful for a psychotherapist, namely, patient engagement, valence, and arousal. Our focus in this work is to only understand the patient's mental health state and not of the therapist. The input to the proposed framework would be the patient’s visual, audio, and text data, while the output would be the desired psychological indicator (engagement/valence-arousal).

* We released a new dataset, MEDICA (Multimodal Engagement Detection In Clinical Analysis), to enhance mental health research, specifically towards understanding the engagement levels of patients attending the therapy sessions. To the best of our knowledge, there is no other multimodal dataset that caters specifically to the needs of mental health-based research. Additionally, while there are some image-based or sensory information-based datasets, there is no dataset that addresses the possibility of exploring engagement detection using visual, audio, and text modalities. MEDICA is a dataset that is a collection of around 1299 short video clips obtained from mock mental health therapy sessions conducted between an actor (who acts like a patient) and a real therapist, which is used by medical schools in their psychiatry curriculum.

### Media Coverage
{:.left}

* "[A New Meaning for Mental Health 'Screening'](https://today.umd.edu/new-meaning-mental-health-screening-ed611623-f53e-47b4-b689-5ece6f6a7e52)" Maryland Today
* "[Could a Virtual Friend Improve Your Mental Health? UMD Researcher Pioneers AI-Driven Virtual Reality ‘Emotional Assistant’](https://today.umd.edu/could-a-virtual-friend-improve-your-mental-health)" Maryland Today
* "[UMIACS Faculty Receive MPower Funding to Improve Mental Telehealth using AI](https://www.umiacs.umd.edu/about-us/news/umiacs-faculty-receive-mpower-funding-improve-mental-telehealth-services-using-ai)" UMIACS

### Technical Report
{:.left}
```
@article{guhan2022teleengage,
title={DeepTMH: Multimodal Semi-supervised framework leveraging Affective and Cognitive engagement for Telemental Health},
author={Guhan, Pooja and Awasthi, Naman and Das, Ritwika and Agarwal, Manas and McDonald, Kathryn and Bussell, Kristin and Manocha, Dinesh  and Reeves, Gloria and Bera, Aniket},
year={2022}
}
```
{:.left}

{%
  include link.html
  type="external"
  icon=""
  text="Paper link"
  link="https://arxiv.org/abs/2011.08690"
  style="button"
%}
{%
  include link.html
  type="youtube"
  icon=""
  text="Video"
  link="watch?v=0ApzgWysYGc"
  style="button"
%}

### Funding
{:.left}

- **State of Maryland: MPower Grant 2020** (Developing an Artificial Intelligence Tool to improve Caregiver Engagement for Rural Child Behavioral Health Services)
- **Maryland Department of Health** (The Resilience Project: Embodied Virtual Reality (VR) Agent Research to measure Adaptive Stress Response for individuals in a high-risk occupation)

{%
  include gallery.html
  style="rect"
  image1="images/research/ai-mental-health/umd.png"
  image2="images/research/ai-mental-health/umb.png"
%}