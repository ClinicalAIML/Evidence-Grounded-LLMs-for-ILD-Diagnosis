# Final Evidence Abstract

## Direct core evidence count
- Direct core papers: 4
- Supporting feature papers: 66

## Most consistent direct evidence supporting ILD
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

## Most consistent direct evidence supporting Healthy
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

## Common weak or non-specific signals from the broader supporting layer
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

## Bottom-line interpretation rule
For final ILD-vs-Healthy case classification:
1. Give highest weight to direct comparator evidence from the direct core layer.
2. Use the supporting feature layer to interpret radiomics patterns, not to overrule direct evidence.
3. Prefer coherent multi-feature abnormality over isolated deviations.
4. Treat age and sex as contextual support only.
5. Reduce confidence when the report relies on weak, unstable, or non-specific feature patterns.
