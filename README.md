# Evidence-Grounded LLMs for Interstitial Lung Disease Classification

This repository contains code, prompt templates, feature definitions, and reproducibility materials for an evidence-grounded large language model (LLM) workflow for interstitial lung disease (ILD) diagnosis using radiomics semantic translation and local retrieval-augmented generation (RAG).

The workflow supports two classification tasks:

1. **ILD versus Healthy**
   Binary classification of radiographically healthy controls versus patients with multidisciplinary discussion-confirmed ILD.

2. **IPF versus non-IPF ILD**
   Binary subclassification of ILD patients into idiopathic pulmonary fibrosis (IPF) versus non-IPF ILD.

The project is designed to bridge quantitative CT radiomics and language-based clinical reasoning by converting predefined radiomics features into structured, clinically interpretable text descriptors and combining them with curated literature evidence retrieved from a local knowledge base.

---

## Repository Scope

This repository provides:

* Radiomics feature panel definitions for both diagnostic tasks
* Healthy-reference normalization and semantic translation logic
* ILD versus Healthy feature-level evidence flag rules
* IPF versus non-IPF healthy-reference deviation rules using an overall ILD median threshold
* Local RAG knowledge base construction and retrieval scripts
* LLM system prompts and user prompt templates
* Model output parsing and diagnostic performance evaluation scripts
* Example de-identified input and output files

This repository does **not** include patient-level clinical data, raw CT images, DICOM files, NLST imaging data, private hospital data, copyrighted full-text articles, or API keys.

---

## Study Overview

The workflow consists of five major stages:

1. **Healthy-reference construction**
   A large radiographically healthy CT reference cohort is used to estimate stable feature-level reference distributions.

2. **Radiomics semantic translation**
   Task-specific radiomics feature panels are transformed into structured natural-language descriptors. For the ILD versus Healthy task, feature-level deviations are categorized using predefined evidence flags. For the IPF versus non-IPF task, feature values are expressed as healthy-reference robust z scores and interpreted using an internal overall ILD median threshold.

3. **Literature knowledge base construction**
   ILD guidelines, radiomics studies, imaging-AI studies, and LLM/RAG methodology papers are summarized into structured evidence chunks.

4. **Local retrieval-augmented generation**
   For each patient, a retrieval query is generated from clinical variables and radiomics descriptors. Relevant local evidence chunks are retrieved and inserted into the LLM prompt.

5. **LLM classification and evaluation**
   Multiple LLM families are queried using locked prompts. Outputs are parsed into structured JSON labels and evaluated using accuracy, sensitivity, specificity, PPV, NPV, macro-F1, and majority-vote ensemble rules.

---

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
├── .gitignore
│
├── configs/
│   ├── ild_vs_healthy_features_20.json
│   ├── ipf_vs_nonipf_features_22.json
│   ├── ild_feature_flag_rules.json
│   └── ipf_overall_ild_median_threshold_rules.json
│
├── prompts/
│   ├── ild_vs_healthy_system_prompt.txt
│   ├── ipf_vs_nonipf_system_prompt.txt
│   ├── ild_vs_healthy_user_prompt_example.txt
│   └── ipf_vs_nonipf_user_prompt_example.txt
│
├── scripts/
│   ├── 01_build_healthy_reference.py
│   ├── 02_generate_ild_vs_healthy_reports.py
│   ├── 03_build_ipf_healthyref_direction_stats.py
│   ├── 04_generate_ipf_vs_nonipf_reports.py
│   ├── 05_build_literature_knowledge_base.py
│   ├── 06_build_local_rag_prompts.py
│   ├── 07_run_llm_classification.py
│   ├── 08_evaluate_model_outputs.py
│   └── 09_majority_vote_ensemble.py
│
├── knowledge_base/
│   ├── README.md
│   ├── evidence_schema.json
│   ├── example_paper_summary.json
│   └── example_retrieval_chunk.json
│
├── examples/
│   ├── example_patient_ild_vs_healthy.json
│   ├── example_patient_ipf_vs_nonipf.json
│   ├── example_model_output.json
│   └── example_metrics.csv
│
└── docs/
    ├── radiomics_feature_panels.md
    ├── rag_workflow.md
    ├── prompt_appendix.md
    └── online_supplement.pdf
```

---

## Diagnostic Tasks

### Task 1: ILD versus Healthy

The ILD versus Healthy task uses a 20-feature original-image radiomics panel designed to capture global departure from radiographically healthy lung. Features include shape, first-order, GLCM, GLSZM, GLRLM, NGTDM, and GLDM descriptors.

Each feature is compared against the healthy reference distribution and assigned one of five evidence flags:

* `strong_outlier`
* `statistical_shift_only`
* `interval_outside_only`
* `mild_shift_within_interval`
* `within_reference`

These flags are used to guide the LLM’s interpretation of radiomics evidence. Strong outliers receive the highest weight, whereas within-reference features are not considered evidence of ILD.

### Task 2: IPF versus non-IPF ILD

The IPF versus non-IPF task uses a 22-feature multiscale radiomics panel designed to capture UIP/IPF-related architecture, including:

* macroscopic lung shape distortion
* density-distribution extremes
* texture heterogeneity
* reticulation and run-length patterns
* honeycomb-scale small zones
* patchwork dependence heterogeneity
* NGTDM busyness and coarseness
* directional wavelet texture

For this task, all patients are already diagnosed with ILD. Therefore, healthy-reference deviation is not interpreted as simple disease abnormality. Instead, each feature is scaled against the healthy reference distribution, and patient-level directional signals are assigned using an internal overall ILD median threshold.

---

## Radiomics Standardization

Radiomics values are standardized using a radiographically healthy reference distribution.

For approximately normal transformed features:

```text
z = (g(x) - mean_reference) / SD_reference
```

For nonnormal features, empirical reference intervals or robust statistics are used.

For the IPF versus non-IPF task, the healthy-reference robust z score is defined as:

```text
healthy_reference_robust_z = (patient_value - healthy_median) / healthy_IQR
```

The patient-level signal is then assigned by comparing this value with the overall ILD median healthy-reference z score for that feature.

---

## Literature Knowledge Base and Local RAG

A curated local literature knowledge base is constructed from ILD guidelines, radiomics studies, imaging-AI studies, and LLM/RAG methodology papers.

Each paper is summarized using a structured schema including:

* study population
* diagnostic task
* imaging modality
* reference standard
* healthy control inclusion
* ILD subtype coverage
* radiomics features
* clinical features
* evidence supporting ILD
* evidence supporting healthy lung
* evidence supporting IPF
* evidence supporting non-IPF ILD
* limitations
* external validation
* applicability to the current task

Evidence chunks are organized into four layers:

1. **Direct Core Evidence**
2. **Supporting Radiomics Evidence**
3. **Supporting Clinical Evidence**
4. **Cautionary Evidence**

At inference time, each patient’s clinical and radiomics report is used to retrieve relevant local evidence chunks. Retrieved evidence is inserted into the prompt under predefined headings. No internet search or external browsing is performed during inference.

---

## Prompting Workflow

Each LLM input consists of:

1. a fixed task-specific system prompt
2. a patient-specific user prompt

The system prompt defines:

* task definition
* allowed classification labels
* radiomics interpretation rules
* clinical interpretation rules
* evidence hierarchy
* cautionary rules
* output JSON schema

The user prompt includes:

* patient demographics
* structured clinical context
* semantic radiomics report
* retrieved direct evidence
* supporting radiomics evidence
* supporting clinical evidence
* cautionary evidence

Ground-truth labels are never included in case-level prompts.

---

## Output Schema

### ILD versus Healthy

```json
{
  "patient_id": "string",
  "classification": "ILD or Healthy",
  "confidence": 0.0,
  "evidence_supporting_ILD": [],
  "evidence_supporting_Healthy": [],
  "uncertainties": [],
  "reasoning_summary": "string"
}
```

### IPF versus non-IPF ILD

```json
{
  "patient_id": "string",
  "classification": "IPF or Other",
  "confidence": 0.0,
  "evidence_supporting_IPF": [],
  "evidence_supporting_Other": [],
  "uncertainties": [],
  "reasoning_summary": "string"
}
```

Only the final `classification` field is used for performance evaluation. Explanatory fields are retained for audit and error analysis.

---

## Evaluation Metrics

The following metrics are computed:

* accuracy
* sensitivity
* specificity
* PPV
* NPV
* macro-F1
* confusion matrix counts
* model-specific misclassified cases
* majority-vote ensemble accuracy

For the IPF versus non-IPF task, IPF is treated as the positive class.

---

## Installation

Create a Python environment:

```bash
conda create -n ild-llm-rag python=3.11
conda activate ild-llm-rag
pip install -r requirements.txt
```

Create a local environment file:

```bash
cp .env.example .env
```

Add your API key if using OpenRouter or other LLM providers:

```text
OPENROUTER_API_KEY=your_api_key_here
```

Do not commit `.env` files to GitHub.

---

## Example Workflow

### 1. Build healthy reference

```bash
python scripts/01_build_healthy_reference.py
```

### 2. Generate ILD versus Healthy case reports

```bash
python scripts/02_generate_ild_vs_healthy_reports.py
```

### 3. Generate IPF versus non-IPF case reports

```bash
python scripts/04_generate_ipf_vs_nonipf_reports.py
```

### 4. Build local RAG prompts

```bash
python scripts/06_build_local_rag_prompts.py
```

### 5. Run LLM classification

```bash
python scripts/07_run_llm_classification.py
```

### 6. Evaluate results

```bash
python scripts/08_evaluate_model_outputs.py
```

### 7. Majority-vote ensemble

```bash
python scripts/09_majority_vote_ensemble.py
```

---

## Data Availability

This repository does not provide raw CT images, hospital clinical data, patient-level data, or restricted NLST imaging files. Users should obtain access to source imaging datasets through the appropriate institutional or public data access mechanisms.

Example files in this repository are synthetic or de-identified and are provided only to demonstrate input and output formats.

---

## Privacy and Security

Before using this code with clinical data, users should ensure that all data handling complies with institutional review board requirements, data use agreements, and local privacy regulations. Do not upload protected health information, patient identifiers, raw DICOM files, or private API keys to public repositories.

---

## Citation

If you use this repository, please cite the associated manuscript:

```text
Evidence-Grounded Large Language Models for Diagnosis of Interstitial Lung Diseases:
Bridging Quantitative Radiomics and Clinical Context via Semantic Translation.
```

A formal citation will be added after publication.

---

## License

This repository is released for academic research use. Please see `LICENSE` for details.
