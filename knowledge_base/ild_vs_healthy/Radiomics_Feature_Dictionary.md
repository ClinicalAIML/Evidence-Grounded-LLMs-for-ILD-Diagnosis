# Radiomics Feature Dictionary for ILD vs Healthy

This file is built from a broader supporting-feature literature layer.
It is intended to help interpret radiomics-based report summaries, including papers not directly designed as ILD-vs-Healthy comparator studies.

## General principles
- Interpret radiomics as a pattern, not as isolated markers.
- Repeated multi-feature abnormality is stronger than one deviating feature.
- Feature interpretation evidence can come from subtype/severity/supporting studies, but should be down-weighted relative to direct comparator studies.

## Recurrently reported ILD-supporting feature patterns

### Traction bronchiectasis
- Recurrent count in supporting-feature papers: 4
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis
  - P040: Interstitial Lung Abnormality: Recognition and Perspectives
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis
  - P112: Diagnosis of Hypersensitivity Pneumonitis in Adults: An Official ATS/JRS/ALAT Clinical Practice Guideline

### Honeycombing
- Recurrent count in supporting-feature papers: 3
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P040: Interstitial Lung Abnormality: Recognition and Perspectives
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis
  - P136: Inter-observer agreement in identifying traction bronchiectasis on computed tomography: its improvement with the use of the additional criteria for chronic fibrosing interstitial pneumonia

### Diffuse centrilobular nodularity
- Recurrent count in supporting-feature papers: 2
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P040: Interstitial Lung Abnormality: Recognition and Perspectives
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis

### Traction bronchiectasis on HRCT
- Recurrent count in supporting-feature papers: 2
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P105: An Official ATS/ERS/JRS/ALAT Statement: Idiopathic Pulmonary Fibrosis: Evidence-based Guidelines for Diagnosis and Management
  - P117: Pathology of Asbestosis—An Update of the Diagnostic Criteria

### Ground-glass opacity pattern (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Reticular pattern (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Nodular pattern (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Linear scar pattern (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Subpleural line pattern (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### High percentage of lung volume classified as interstitial pattern (ILA score)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### High-certainty voxel probability for interstitial labels
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Reduced kurtosis of CT attenuation histogram (less peaked than healthy lungs)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Reduced skewness of CT attenuation histogram (less left-skewed than healthy lungs)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Increased mean lung attenuation (higher/less negative HU values than healthy lungs)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Kurtosis correlated with FVC (r=0.53), FEV1 (r=0.46), TLC (r=0.45), DLCO (r=0.37)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Mean lung attenuation negatively correlated with all PFTs
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### UIP-like fibrotic pattern on HRCT (reticular abnormality, traction bronchiectasis, honeycombing with basal/peripheral predominance)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P010: The natural history of progressive fibrosing interstitial lung diseases

### Extent of fibrosis >10% on HRCT
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P010: The natural history of progressive fibrosing interstitial lung diseases

### Increased extent of fibrosis on HRCT as criterion for disease progression
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P010: The natural history of progressive fibrosing interstitial lung diseases

### Possible UIP pattern on HRCT (high specificity 91-93% for histopathological UIP)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Total traction bronchiectasis score ≥4 (associated with higher PPV for UIP)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Basilar/subpleural reticulation
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Traction bronchiectasis presence and extent
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Honeycombing absence distinguishing possible from definite UIP
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Semi-quantitative CT (SQCT) score of ILD extent (Goh method, scored at 5 anatomical levels)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### ΔSQCT negatively correlated with ΔFVC (r=-0.487) in 12-24 month follow-up
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### ΔSQCT negatively correlated with ΔDLco (r=-0.298) in 12-24 month follow-up
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### HRCT detects interstitial abnormalities even when PFTs are normal
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### Peripheral and basilar predominant reticulation (probable UIP pattern)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

### Subpleural honeycombing (definite UIP pattern)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support ILD when part of a coherent abnormal multi-feature pattern.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

## Recurrently reported Healthy-supporting feature patterns

### Normal parenchyma classification (CNN-learned features)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Low percentage of lung volume affected by interstitial patterns
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Low certainty scores for interstitial pattern labels
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### High kurtosis (sharply peaked histogram)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Strong left skewness of attenuation histogram
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Lower mean lung attenuation (more negative HU, approximately -798 to -819 HU from prior literature)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Histogram more peaked than Gaussian normal distribution
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Normal lung attenuation range (HU -1400 to 200) used to represent normal lung appearance
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P031: Holistic classification of CT attenuation patterns for interstitial lung diseases via deep convolutional neural networks

### CNN softmax probability distribution favoring normal class in healthy slices
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P031: Holistic classification of CT attenuation patterns for interstitial lung diseases via deep convolutional neural networks

### No ILA on CT (no changes affecting >5% of any lung zone)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis

### Absence of traction bronchiectasis or honeycombing
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis

### Normal FVC, TLC, and DLCO
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P049: Interstitial Lung Disease in Relatives of Patients with Pulmonary Fibrosis

### Denoised images show more uniform attenuation in NL tissue (more homogeneous pixel values)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P070: Classification of parenchymal abnormality in scleroderma lung using a novel approach to denoise images collected via a multicenter study

### NL tissue appears more uniformly dark after denoising, reflecting absence of pathological texture
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P070: Classification of parenchymal abnormality in scleroderma lung using a novel approach to denoise images collected via a multicenter study

### Fewer oscillatory texture patterns in NL regions after denoising
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P070: Classification of parenchymal abnormality in scleroderma lung using a novel approach to denoise images collected via a multicenter study

### NL correctly classified at 89.7% ROI-level using denoised texture features
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P070: Classification of parenchymal abnormality in scleroderma lung using a novel approach to denoise images collected via a multicenter study

### Low CNN fibrosis score (log fibrosis score <0.60, corresponding to <1.8% fibrotic area)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P094: MUC5B variant is associated with visually and quantitatively detected preclinical pulmonary fibrosis

### Low %HAA values
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P094: MUC5B variant is associated with visually and quantitatively detected preclinical pulmonary fibrosis

### Absence of reticular, honeycombing, or traction bronchiectasis patterns on CT
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P094: MUC5B variant is associated with visually and quantitatively detected preclinical pulmonary fibrosis

### Absence of intralobular reticular opacities
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Absence of ground-glass opacities
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Absence of irregular septal thickening
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Absence of honeycombing
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Visual ILA score of 0
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Low DTA score (median 0.6)
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P123: Development and Progression of Radiologic Abnormalities in Individuals at Risk for Familial Interstitial Lung Disease

### Higher MMP3 (stromelysin-1) levels in controls vs IPF
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P134: Peripheral blood proteomic profiling of idiopathic pulmonary fibrosis biomarkers in the multicentre IPF-PRO Registry

### Higher creatine kinase B and M (CKB/CKM) in controls
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P134: Peripheral blood proteomic profiling of idiopathic pulmonary fibrosis biomarkers in the multicentre IPF-PRO Registry

### Higher AGER (advanced glycosylation end product receptor) in controls
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P134: Peripheral blood proteomic profiling of idiopathic pulmonary fibrosis biomarkers in the multicentre IPF-PRO Registry

### Higher sonic hedgehog protein (SHH) in controls
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P134: Peripheral blood proteomic profiling of idiopathic pulmonary fibrosis biomarkers in the multicentre IPF-PRO Registry

### Higher carbonic anhydrase 6 (CA6) in controls
- Recurrent count in supporting-feature papers: 1
- Interpretation: may support Healthy status when no coherent ILD-like pattern is present.
- Example source papers:
  - P134: Peripheral blood proteomic profiling of idiopathic pulmonary fibrosis biomarkers in the multicentre IPF-PRO Registry

## Weak or unstable feature patterns

### Ground-glass pattern (very few training samples: 137 points, 9 scans)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Nodular pattern (very few training samples: 116 points, 7 scans)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Linear scar pattern (very few training samples: 195 points, 8 scans)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Subpleural line pattern (relatively few training samples: 413 points, 19 scans)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Reticular pattern sometimes misclassified as subpleural line or nodular
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Normal parenchyma sometimes confused with centrilobular emphysema
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Features learned from smoker cohort only, limiting generalizability to non-smoker ILD
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P005: Classification of Interstitial Lung Abnormality Patterns with an Ensemble of Deep Convolutional Neural Networks

### Corrected mean lung attenuation showed lower correlation with PFTs than uncorrected mean lung attenuation
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Diffusing lung capacity showed least correlation with all histogram features
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### All histogram features insensitive to textural changes such as ground-glass, reticular abnormality, and honeycombing
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Correlations reduced in multicenter non-spirometrically controlled setting vs single-center studies
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### Scanner manufacturer variability substantially affected attenuation measurements
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P006: Quantitative CT Indexes in Idiopathic Pulmonary Fibrosis: Relationship with Physiologic Impairment

### HRCT fibrotic pattern (UIP-like vs other) showed differential FVC decline rates but overlapping mortality risk over longer follow-up
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P010: The natural history of progressive fibrosing interstitial lung diseases

### Non-UIP fibrotic patterns associated with lower short-term mortality but similar long-term risk
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P010: The natural history of progressive fibrosing interstitial lung diseases

### Inconsistent with UIP pattern (poor PPV of 22.7% for histopathological UIP)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Peribronchovascular distribution (common but not specific)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Ground glass opacities (common inconsistent feature, low specificity for UIP)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Mosaic perfusion/air trapping (inconsistent feature with limited predictive value)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Upper-mid lung predominance (inconsistent feature with limited predictive value)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Diffuse micronodules (least associated with UIP on biopsy)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### Consolidation (least associated with UIP on biopsy)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P011: The use of pretest probability increases the value of high-resolution CT in diagnosing usual interstitial pneumonia

### No significant correlation between SQCT change and functional decline in whole cohort
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### Correlation only significant in 12-24 month subgroup, not in <12 or >24 month subgroups
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### Low concordance between OMERACT PFT criteria and HRCT progression (Cohen's kappa 0.197)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### Low PPV (20%) of functional progression for radiological progression
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### DLco change less specific for ILD due to confounding by pulmonary vasculopathy and emphysema
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P012: Longitudinal change during follow-up of systemic sclerosis: correlation between high-resolution computed tomography and pulmonary function tests

### CT scan honeycombing not associated with microscopic honeycombing (kappa = -0.005)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

### Zonal and axial distribution had only fair inter-reader agreement (kappa ~0.24-0.25)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

### UIP diagnosis on CT had only fair-to-moderate inter-reader agreement (kappa = 0.31)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

### Ground-glass opacity assessment had moderate inter-reader agreement (kappa = 0.39)
- Recurrent count in supporting-feature papers: 1
- Interpretation: should not be heavily weighted in classification.
- Example source papers:
  - P015: CT Scan Findings of Probable Usual Interstitial Pneumonitis Have a High Predictive Value for Histologic Usual Interstitial Pneumonitis

## Recurrent interpretation notes

- No age- or sex-based radiomics analysis is performed. (2)
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
- HRCT pattern classification (UIP-like vs other fibrotic patterns) was used as a stratification variable, not a quantitative radiomic feature (1)
- UIP-like pattern associated with greater annual FVC decline (-214.6 vs -160.1 mL/year) and higher 52-week mortality than other fibrotic patterns (1)
- HRCT features used were qualitative radiological descriptors, not extracted radiomic texture or intensity features (1)
- FVC decline >10% predicted was the primary prognostic marker, not imaging features per se (1)
- Paper focuses on clinical progression metrics (FVC, mortality) rather than radiomics-based classification (1)
- PPV of HRCT patterns is highly dependent on population prevalence (pretest probability) of histopathological UIP (1)
- Possible UIP pattern has high specificity but variable PPV depending on prevalence setting (1)
- Age (≥60 years), male sex, and traction bronchiectasis score ≥4 combined into a UIP score model improved PPV (1)
- Inconsistent with UIP pattern could not be combined with any clinical features to reliably rule in UIP (1)
- Study compares ILD subtypes (UIP vs non-UIP), not ILD vs healthy subjects (1)
- Traction bronchiectasis scored per lobe (0-3 scale) summed across 6 lobes for total score (1)
- SQCT is a visual semi-quantitative score, not a quantitative radiomic feature (1)
- FVC decline is more specific for ILD than DLco in SSc (1)
- DLco variation may reflect both ILD and pulmonary vasculopathy progression (1)
