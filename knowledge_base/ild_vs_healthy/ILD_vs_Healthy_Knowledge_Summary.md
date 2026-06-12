# ILD vs Healthy Knowledge Summary

## 1. Purpose
This knowledge summary is derived from structured summaries of 151 papers.
Successfully summarized papers: 151
Failed or unresolved papers: 0
High-value papers retained for core evidence synthesis: 6

This file is intended to support evidence-based distinction between ILD patients and healthy subjects using age, sex, and radiomics-based report summaries.

---

## 2. How this knowledge base should be used
- Age and sex are contextual variables, not decisive evidence.
- Radiomics should be interpreted as a multi-feature pattern rather than isolated markers.
- A single abnormal feature should not be treated as diagnostic.
- Missing or weakly transferable evidence should reduce confidence.
- Papers that are not directly about ILD-vs-healthy discrimination should be down-weighted.

---

## 3. Corpus overview

### Task type distribution
- other (93)
- prognosis (24)
- subtype (18)
- severity (9)
- ild_vs_healthy (7)

### Direct relevance distribution
- low (145)
- medium (6)

### Evidence strength distribution
- moderate (79)
- weak (53)
- unclear (11)
- strong (8)

### Healthy-control inclusion
- no (138)
- yes (13)

---

## 4. Most recurrent patterns supporting ILD
The following signals appeared repeatedly in higher-value literature summaries and should be treated as supportive evidence patterns, not as standalone diagnostic rules.

- Ground-glass opacity pattern (CNN-learned features) (1)
- Reticular pattern (CNN-learned features) (1)
- Nodular pattern (CNN-learned features) (1)
- Linear scar pattern (CNN-learned features) (1)
- Subpleural line pattern (CNN-learned features) (1)
- High percentage of lung volume classified as interstitial pattern (ILA score) (1)
- High-certainty voxel probability for interstitial labels (1)
- Reduced kurtosis of CT attenuation histogram (less peaked than healthy lungs) (1)
- Reduced skewness of CT attenuation histogram (less left-skewed than healthy lungs) (1)
- Increased mean lung attenuation (higher/less negative HU values than healthy lungs) (1)
- Kurtosis correlated with FVC (r=0.53), FEV1 (r=0.46), TLC (r=0.45), DLCO (r=0.37) (1)
- Mean lung attenuation negatively correlated with all PFTs (1)
- High CT attenuation patterns (HU -160 to 240) associated with consolidation and nodules (1)
- Low CT attenuation patterns (HU -1400 to -950) associated with emphysema (1)
- CNN-learned deep features from three attenuation-scaled CT channels (1)
- Emphysema perfectly classified using low-attenuation range features (1)
- Ground glass opacity patterns captured in normal attenuation range (1)
- Non-dependent ground-glass abnormalities affecting >5% of any lung zone (1)
- Reticular abnormalities affecting >5% of any lung zone (1)
- Diffuse centrilobular nodularity (1)
- Non-emphysematous cysts (1)
- Honeycombing (1)
- Traction bronchiectasis (1)
- Pulmonary parenchymal architectural distortion (definite fibrosis pattern) (1)
- Subpleural reticular changes (1)
- Statistical texture features distinguishing LF, GG, HC from NL (1)
- Run-length parameters elevated in fibrotic and ground-glass regions (1)
- Co-occurrence parameters differentiating abnormal parenchymal patterns (1)
- 58 texture features computed per pixel; 45 selected (original) or 38 selected (denoised) via multinomial logistic regression for disease classification (1)
- Higher CNN-based quantitative HRCT fibrosis score (% lung volume classified as fibrotic) (1)

---

## 5. Most recurrent patterns supporting Healthy status
These patterns appeared repeatedly as features more compatible with healthy lungs or with lack of coherent abnormality.

- Normal parenchyma classification (CNN-learned features) (1)
- Low percentage of lung volume affected by interstitial patterns (1)
- Low certainty scores for interstitial pattern labels (1)
- High kurtosis (sharply peaked histogram) (1)
- Strong left skewness of attenuation histogram (1)
- Lower mean lung attenuation (more negative HU, approximately -798 to -819 HU from prior literature) (1)
- Histogram more peaked than Gaussian normal distribution (1)
- Normal lung attenuation range (HU -1400 to 200) used to represent normal lung appearance (1)
- CNN softmax probability distribution favoring normal class in healthy slices (1)
- No ILA on CT (no changes affecting >5% of any lung zone) (1)
- Absence of traction bronchiectasis or honeycombing (1)
- Normal FVC, TLC, and DLCO (1)
- Denoised images show more uniform attenuation in NL tissue (more homogeneous pixel values) (1)
- NL tissue appears more uniformly dark after denoising, reflecting absence of pathological texture (1)
- Fewer oscillatory texture patterns in NL regions after denoising (1)
- NL correctly classified at 89.7% ROI-level using denoised texture features (1)
- Low CNN fibrosis score (log fibrosis score <0.60, corresponding to <1.8% fibrotic area) (1)
- Low %HAA values (1)
- Absence of reticular, honeycombing, or traction bronchiectasis patterns on CT (1)

---

## 6. Weak, unstable, or non-specific signals
These features or patterns were repeatedly flagged as weak, non-specific, unstable, or insufficient alone.

- Ground-glass pattern (very few training samples: 137 points, 9 scans) (1)
- Nodular pattern (very few training samples: 116 points, 7 scans) (1)
- Linear scar pattern (very few training samples: 195 points, 8 scans) (1)
- Subpleural line pattern (relatively few training samples: 413 points, 19 scans) (1)
- Reticular pattern sometimes misclassified as subpleural line or nodular (1)
- Normal parenchyma sometimes confused with centrilobular emphysema (1)
- Features learned from smoker cohort only, limiting generalizability to non-smoker ILD (1)
- Corrected mean lung attenuation showed lower correlation with PFTs than uncorrected mean lung attenuation (1)
- Diffusing lung capacity showed least correlation with all histogram features (1)
- All histogram features insensitive to textural changes such as ground-glass, reticular abnormality, and honeycombing (1)
- Correlations reduced in multicenter non-spirometrically controlled setting vs single-center studies (1)
- Scanner manufacturer variability substantially affected attenuation measurements (1)
- Micronodule patterns difficult to separate from healthy/normal images (1)
- Holistic image classification accuracy only 68.6% vs 87.9% for patch-based (1)
- Healthy and micronodule classes frequently confused in confusion matrix (1)
- Single static CT slice features insufficient for micronodule classification (1)
- Focal or unilateral ground-glass attenuation (classified as indeterminate, not ILA) (1)
- Focal or unilateral reticulation (classified as indeterminate) (1)
- Patchy ground-glass abnormality <5% of lung (classified as indeterminate) (1)
- Lymphocyte telomere length <10th percentile (associated with ILA but not statistically significant for ILD in multivariable analysis) (1)
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

## 7. Interpretation notes repeatedly emphasized across papers
These notes are especially important for downstream LLM reasoning.

- Features are learned by deep CNNs (not hand-crafted radiomics), so individual feature interpretability is limited (1)
- Grad-CAM activation maps confirm CNNs focus on lesion locations, not background (1)
- ILA score defined as percentage of lung volume classified as any interstitial pattern with certainty >95% (1)
- AUC of 0.863 for detecting visually defined ILA vs. non-ILA in 114 subjects (1)
- Normal parenchyma class was labeled both adjacent to and distant from lesions, only in clearly normal areas (1)
- CNN features capture local texture patterns at secondary pulmonary lobule scale (~30mm ROI) (1)
- Sharp reconstruction kernel (B50) yielded better classification performance than soft kernel (B35) (1)
- Population is exclusively smokers from COPDGene; ILA may represent pre-ILD rather than established ILD (1)
- In healthy subjects, CT attenuation histogram is sharply peaked (high kurtosis) and left-skewed relative to Gaussian distribution (1)
- IPF lungs show reduced kurtosis, reduced skewness, and increased mean lung attenuation compared to normal lungs, attributed to increased soft tissue and decreased gas (1)
- Kurtosis alone provided predictive ability nearly equivalent to all three histogram features combined for FVC, FEV1, and TLC (1)
- Mean lung attenuation values in IPF patients (~-703 HU) are higher (less negative) than healthy subjects (~-798 to -819 HU from prior studies) (1)
- Histogram features are first-order statistics and do not capture texture information such as honeycombing or ground-glass opacity (1)
- Attenuation correction algorithm did not significantly improve correlations with PFTs (1)
- Exclusion of suboptimal scans (motion artifact, hypoventilation) moderately improved correlations (1)
- Three CT attenuation rescaling ranges used as CNN input channels analogous to RGB (1)
- Features are CNN-learned and not hand-crafted; clinical interpretability is limited (1)
- Emphysema strongly separable due to distinct low-attenuation signature (1)
- Normal vs micronodule confusion suggests healthy classification is not robust (1)
- Paper notes understanding clinical meaning of learned features is future work (1)
- Holistic (whole-slice) approach is weakly supervised; no explicit radiomic feature extraction (1)
- CT features were assessed qualitatively by up to three readers, not via automated radiomic extraction (1)
- ILA defined as changes affecting >5% of any lung zone; indeterminate scans were excluded from ILA classification (1)
- ILD defined as ILA plus definite fibrosis on CT, OR ILA without definite fibrosis combined with TLC <80% or DLCO <70% predicted (1)
- Physiologic decrements (TLC <80% or DLCO <70%) had >9-fold increased odds of ILA (OR 9.6, 95% CI 3.1-29.8) (1)
- MUC5B promoter variant (rs35705950) independently associated with ILA and ILD in multivariable analyses (1)
- Age was significantly higher in relatives with ILA vs. without (median 61 vs. 58 years, p=0.01) (1)
- Sex was not significantly associated with ILA or ILD in this cohort (1)
- Adding PFT decrements, telomere length, and MUC5B genotype to age/sex/smoking improved ILA prediction AUC from 0.66 to 0.82 (1)
- Denoising with Aujol's algorithm reduced noise-driven texture variability, improving NL classification most substantially (1)

---

## 8. Practical decision logic for downstream classification
When classifying a subject as ILD or Healthy:

1. Check whether the report describes a coherent abnormal multi-feature pattern rather than isolated deviations.
2. Treat age and sex as supportive context only.
3. Give more weight to repeated radiomics abnormalities that recur across higher-value studies.
4. Reduce confidence when the evidence depends on:
   - a single feature,
   - a low-relevance paper,
   - a paper without healthy controls,
   - weakly transferable preprocessing pipelines,
   - or unclear evidence strength.
5. If the report mostly indicates near-reference or non-coherent feature behavior, Healthy becomes more plausible.
6. If the report shows repeated heterogeneity / complexity / reduced homogeneity patterns consistent across multiple features, ILD becomes more plausible.

---

## 9. Cautions
- This knowledge base supports classification assistance, not autonomous diagnosis.
- Literature-derived radiomics associations may not transfer perfectly across cohorts, scanners, segmentation pipelines, or normalization methods.
- Some papers in the corpus are only indirectly relevant; only higher-value papers should strongly influence classification.
- Radiomics alone is not equivalent to disease truth.

---

## 10. Recommended output schema for downstream case classification
For each subject, the downstream model should produce:
- classification: ILD or Healthy
- confidence: 0 to 1
- evidence_supporting_ILD
- evidence_supporting_Healthy
- uncertainties
- reasoning_summary
