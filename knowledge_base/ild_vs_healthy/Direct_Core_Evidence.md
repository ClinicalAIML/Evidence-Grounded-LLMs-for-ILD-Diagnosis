# Direct Core Evidence for ILD vs Healthy

## 1. Purpose
This file contains only the most direct literature evidence for distinguishing ILD from Healthy subjects.

Selection rule:
- task_type == ild_vs_healthy
- direct_relevance in {medium, high}
- healthy_controls_included == yes

Number of direct core papers: 4

---

## 2. Core evidence set overview

### Task types
- ild_vs_healthy (4)

### Direct relevance
- medium (4)

### Healthy controls included
- yes (4)

---

## 3. Most recurrent patterns supporting ILD
- Ground-glass opacity pattern (CNN-learned features) (1)
- Reticular pattern (CNN-learned features) (1)
- Nodular pattern (CNN-learned features) (1)
- Linear scar pattern (CNN-learned features) (1)
- Subpleural line pattern (CNN-learned features) (1)
- High percentage of lung volume classified as interstitial pattern (ILA score) (1)
- High-certainty voxel probability for interstitial labels (1)
- High CT attenuation patterns (HU -160 to 240) associated with consolidation and nodules (1)
- Low CT attenuation patterns (HU -1400 to -950) associated with emphysema (1)
- CNN-learned deep features from three attenuation-scaled CT channels (1)
- Emphysema perfectly classified using low-attenuation range features (1)
- Ground glass opacity patterns captured in normal attenuation range (1)
- Statistical texture features distinguishing LF, GG, HC from NL (1)
- Run-length parameters elevated in fibrotic and ground-glass regions (1)
- Co-occurrence parameters differentiating abnormal parenchymal patterns (1)
- 58 texture features computed per pixel; 45 selected (original) or 38 selected (denoised) via multinomial logistic regression for disease classification (1)
- Higher CNN-based quantitative HRCT fibrosis score (% lung volume classified as fibrotic) (1)
- Reticular abnormality on CT (1)
- Honeycombing on CT (1)
- Traction bronchiectasis on CT (1)
- Lower-lobe predominant subpleural fibrotic changes consistent with UIP pattern (1)
- Higher percent high attenuation area (%HAA) on HRCT (1)

---

## 4. Most recurrent patterns supporting Healthy
- Normal parenchyma classification (CNN-learned features) (1)
- Low percentage of lung volume affected by interstitial patterns (1)
- Low certainty scores for interstitial pattern labels (1)
- Normal lung attenuation range (HU -1400 to 200) used to represent normal lung appearance (1)
- CNN softmax probability distribution favoring normal class in healthy slices (1)
- Denoised images show more uniform attenuation in NL tissue (more homogeneous pixel values) (1)
- NL tissue appears more uniformly dark after denoising, reflecting absence of pathological texture (1)
- Fewer oscillatory texture patterns in NL regions after denoising (1)
- NL correctly classified at 89.7% ROI-level using denoised texture features (1)
- Low CNN fibrosis score (log fibrosis score <0.60, corresponding to <1.8% fibrotic area) (1)
- Low %HAA values (1)
- Absence of reticular, honeycombing, or traction bronchiectasis patterns on CT (1)

---

## 5. Weak or unstable signals even within direct evidence
- Ground-glass pattern (very few training samples: 137 points, 9 scans) (1)
- Nodular pattern (very few training samples: 116 points, 7 scans) (1)
- Linear scar pattern (very few training samples: 195 points, 8 scans) (1)
- Subpleural line pattern (relatively few training samples: 413 points, 19 scans) (1)
- Reticular pattern sometimes misclassified as subpleural line or nodular (1)
- Normal parenchyma sometimes confused with centrilobular emphysema (1)
- Features learned from smoker cohort only, limiting generalizability to non-smoker ILD (1)
- Micronodule patterns difficult to separate from healthy/normal images (1)
- Holistic image classification accuracy only 68.6% vs 87.9% for patch-based (1)
- Healthy and micronodule classes frequently confused in confusion matrix (1)
- Single static CT slice features insufficient for micronodule classification (1)
- Honeycomb (HC) texture features showed poor classification rates (<20%) and were not improved by denoising (1)
- Features derived from original (non-denoised) images showed higher false-positive rates for NL classification (1)
- Pixel-level features susceptible to noise variation across scanner platforms and dose protocols (1)
- 2D-only features; 3D texture features not computed due to 10mm slice intervals (1)
- %HAA had lower AUC (0.80) and lower specificity (62%) compared to CNN fibrosis score (1)
- %HAA not significantly associated with MUC5B risk variant (1)
- Male sex not independently associated with quantitative fibrosis score in regression (1)
- MUC5B variant association with deep-learning-detected subclinical fibrosis did not reach significance in subgroup analysis (p=0.18) (1)
- TERT variant not associated with PrePF in this cohort (1)

---

## 6. Practical interpretation
These papers should be treated as the strongest direct evidence base for the downstream ILD-vs-Healthy classification task.
However, even within this direct evidence layer:
- single features should not be over-weighted,
- age and sex remain contextual rather than decisive,
- and radiomics should be interpreted as a coherent multi-feature pattern.
