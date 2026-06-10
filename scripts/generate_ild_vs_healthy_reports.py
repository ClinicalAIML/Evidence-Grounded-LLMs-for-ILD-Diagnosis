
import os
import math
import json
import numpy as np
import pandas as pd
from scipy.stats import yeojohnson

# ── paths ────────────────────────────────────────────────────────────────────
BASE = "/NLST_lung_data/processed_file"
OUT_DIR = "/NLST_lung_data/llm_validation"
os.makedirs(OUT_DIR, exist_ok=True)

HEALTH_FILE = os.path.join(BASE, "Health_Radiomics_KeyFeatures.csv")
ILD_FILE    = os.path.join(BASE, "ILD_Radiomics_KeyFeatures.csv")
TRANS_FILE  = os.path.join(BASE, "transformation_summary.csv")
BOUNDS_FILE = os.path.join(BASE, "prediction_bounds.csv")
HEALTH_DEMO = os.path.join(BASE, "Health Demo.csv")
ILD_DEMO    = os.path.join(BASE, "ILD_demo_lab_data.csv")


# thresholds
STRONG_Z = 2.0
MILD_Z = 1.0

# ── load data ─────────────────────────────────────────────────────────────────
health = pd.read_csv(HEALTH_FILE)
ild    = pd.read_csv(ILD_FILE)

health = health.rename(columns={"No": "original_ID"})
ild    = ild.rename(columns={"ID": "original_ID"})

# ── merge demographics ────────────────────────────────────────────────────────
health_demo = pd.read_csv(HEALTH_DEMO).rename(columns={"No": "original_ID"})
health = health.merge(health_demo[["original_ID", "Gender", "Age"]], on="original_ID", how="left")

ild_demo = pd.read_csv(ILD_DEMO).rename(columns={"NO": "original_ID", "A1": "Gender", "A2": "Age"})
ild_demo["Gender"] = ild_demo["Gender"].map({0: "M", 1: "F"})
ild = ild.merge(ild_demo[["original_ID", "Gender", "Age"]], on="original_ID", how="left")

health["true_label"] = "Healthy"
ild["true_label"]    = "ILD"

# ── assign new unique IDs ─────────────────────────────────────────────────────
health["patient_ID"] = [f"{i+1:03d}" for i in range(len(health))]
ild["patient_ID"]    = [f"{i+len(health)+1:03d}" for i in range(len(ild))]

# ── combine ───────────────────────────────────────────────────────────────────
combined = pd.concat([health, ild], ignore_index=True)

feature_cols = [c for c in combined.columns
                if c not in ("patient_ID", "original_ID", "true_label", "Age", "Gender")]
combined = combined[["patient_ID", "original_ID", "true_label", "Age", "Gender"] + feature_cols]

combined = combined.drop(columns=[c for c in DROP_COLS if c in combined.columns])

combined.drop(columns=["original_ID"]).to_csv(os.path.join(OUT_DIR, "validation_combined.csv"), index=False)

# ── load reference stats ──────────────────────────────────────────────────────
trans  = pd.read_csv(TRANS_FILE).dropna(subset=["feature"])
bounds = pd.read_csv(BOUNDS_FILE).dropna(subset=["feature"])

trans_dict  = trans.set_index("feature").to_dict("index")
bounds_dict = bounds.set_index("feature").to_dict("index")

# ── helpers ───────────────────────────────────────────────────────────────────
def apply_transform(value, method, lam, mn):
    if method == "none" or pd.isna(method):
        return value
    if method == "log1p":
        return math.log1p(value) if value > -1 else np.nan
    if method == "boxcox":
        if mn <= 0:
            value = value - mn + 1e-6
        if lam == 0:
            return math.log(value) if value > 0 else np.nan
        return (value ** lam - 1) / lam if value > 0 else np.nan
    if method == "yeojohnson":
        arr = np.array([value], dtype=float)
        transformed = yeojohnson(arr, lmbda=lam)
        return float(transformed[0])
    return value


def z_score(value, method, lam, mn, ref_mean, ref_sd):
    t = apply_transform(value, method, lam, mn)
    if np.isnan(t) or ref_sd == 0:
        return np.nan
    return (t - ref_mean) / ref_sd


def range_label(value, lower, upper):
    if value < lower:
        return "below"
    if value > upper:
        return "above"
    return "within"


def within_interval(value, lower, upper):
    if pd.isna(value) or pd.isna(lower) or pd.isna(upper):
        return None
    return lower <= value <= upper


def evidence_flag(z, raw_value, lower, upper):
    if pd.isna(z) or pd.isna(raw_value) or pd.isna(lower) or pd.isna(upper):
        return "unknown"

    in_range = within_interval(raw_value, lower, upper)

    if abs(z) >= STRONG_Z and not in_range:
        #return "statistical_shift and interval_outside"
        return "strong_outlier"
    if abs(z) >= STRONG_Z and in_range:
        return "statistical_shift_only"
    if abs(z) < STRONG_Z and not in_range:
        return "interval_outside_only"
    if abs(z) >= MILD_Z and in_range:
        return "mild_shift_within_interval"
    return "within_reference"


def direction_label(z):
    if pd.isna(z):
        return "unknown"
    if z > 0:
        return "high"
    if z < 0:
        return "low"
    return "neutral"


FEATURE_DESC = {
    "original_glcm_Contrast":              "GLCM Contrast (local intensity variation)",
    "original_glcm_Idmn":                  "GLCM Inverse Difference Moment Normalised (texture homogeneity)",
    "original_glcm_ClusterShade":          "GLCM Cluster Shade (texture asymmetry)",
    "original_glcm_ClusterProminence":     "GLCM Cluster Prominence (texture irregularity)",
    "original_glszm_GrayLevelNonUniformity":"GLSZM Gray Level Non-Uniformity (variation in gray-level distribution)",
    "original_glrlm_RunEntropy":           "GLRLM Run Entropy (run-length distribution randomness)",
    "original_glrlm_LongRunEmphasis":      "GLRLM Long Run Emphasis (prevalence of long uniform runs)",
    "original_ngtdm_Contrast":             "NGTDM Contrast (local texture contrast)",
    "original_ngtdm_Coarseness":           "NGTDM Coarseness (texture granularity)",
    "original_gldm_DependenceEntropy":     "GLDM Dependence Entropy (gray-level dependence complexity)",
    "original_gldm_HighGrayLevelEmphasis": "GLDM High Gray Level Emphasis (prevalence of high-intensity voxels)",
    "original_shape_Sphericity":           "Shape Sphericity (roundness of the lesion)",
    "original_shape_MeshVolume":           "Shape Mesh Volume (lesion volume, mm³)",
    "original_shape_VoxelVolume":          "Shape Voxel Volume (lesion volume by voxel count, mm³)",
}


def build_retrieval_query(age, gender, feature_table):
    important = []
    for f in feature_table:
        if f["evidence_flag"] in {"strong_outlier", "statistical_shift_only", "interval_outside_only"}:
            important.append(f"{f['feature_name']} {f['direction']} ({f['meaning']})")

    parts = [f"Age {age}", f"sex {gender}"]
    if important:
        parts.append("Important radiomics patterns: " + ", ".join(important[:8]))
    return ". ".join(parts) + "."


def build_llm_case_report(pid, age, gender, feature_table):
    lines = []
    lines.append("--- Patient Radiomics Evidence Report ---")
    lines.append(f"Patient demographics: Age {age}, Gender {gender}")
    lines.append("")
    lines.append("Interpretation rules for this report:")
    lines.append("- Features with high absolute z-score but raw value still within the healthy 95% interval should be treated as statistical shift only, which may indicate early or subtle changes but with less confidence than features that also fall outside the interval.")
    lines.append("- Patients with multiple features showing strong outlier evidence are more likely to have significant underlying pathology than those with only one or no such features.")
    lines.append("- Patients with more features within reference range are more likely to be healthy.")
    lines.append("- Final interpretation should rely on the overall multi-feature pattern rather than a single metric.")
    lines.append("")

    grouped = {
        "strong_outlier": [],
        #"statistical_shift and interval_outside": [],
        "statistical_shift_only": [],
        "interval_outside_only": [],
        "mild_shift_within_interval": [],
        "within_reference": [],
        "unknown": []
    }
    for feat in feature_table:
        grouped[feat["evidence_flag"]].append(feat)

    def add_group(title, items):
        lines.append(f"[{title}]")
        if not items:
            lines.append("- None")
            lines.append("")
            return
        for f in items:
            lines.append(
                f"- {f['feature_name']} ({f['meaning']}): "
                f"raw={f['raw_value']:.6g}, z={f['z_score']:.2f}, "
                f"healthy_interval=[{f['healthy_interval_low']:.4g}, {f['healthy_interval_high']:.4g}], "
                f"direction={f['direction']}, within_interval={f['within_healthy_interval']}"
            )
        lines.append("")

    add_group("Strong outlier evidence", grouped["strong_outlier"])
    add_group("Statistical shift only", grouped["statistical_shift_only"])
    add_group("Interval outside only", grouped["interval_outside_only"])
    add_group("Mild shift within interval", grouped["mild_shift_within_interval"])
    add_group("Within reference range", grouped["within_reference"])


    return "\n".join(lines)


# ── generate reports ──────────────────────────────────────────────────────────
feature_cols_final = [c for c in combined.columns
                      if c not in ("patient_ID", "original_ID", "true_label", "Age", "Gender")]

records = []

for _, row in combined.iterrows():
    pid        = row["patient_ID"]
    age        = row["Age"]
    gender     = row["Gender"]

    gender_str = str(gender) if pd.notna(gender) else "unknown"
    age_str    = int(age) if pd.notna(age) else "unknown"

    raw_lines = []
    raw_lines.append("--- Patient Radiomics Report ---")
    raw_lines.append(f"Patient demographics: Age {age_str}, Gender {gender_str}\n")

    feature_table = []

    for feat in feature_cols_final:
        if feat not in trans_dict:
            continue

        raw_val = row[feat]
        if pd.isna(raw_val):
            continue

        info   = trans_dict[feat]
        method = info.get("transform", "none")
        lam    = info.get("lambda", None)
        r_mean = info.get("ref_mean")
        r_sd   = info.get("ref_sd")
        mn = info.get("ref_mn", None)
        desc   = FEATURE_DESC.get(feat, feat)

        z = z_score(raw_val, method, lam, mn, r_mean, r_sd)

        lo, hi = np.nan, np.nan
        if feat in bounds_dict:
            lo = bounds_dict[feat]["lower_2.5pct"]
            hi = bounds_dict[feat]["upper_97.5pct"]

        flag = evidence_flag(z, raw_val, lo, hi)
        in_range = within_interval(raw_val, lo, hi)
        direction = direction_label(z)

        # split desc into feature_name + meaning
        if "(" in desc and ")" in desc:
            feature_name = desc.split("(")[0].strip()
            meaning = desc.split("(")[1].split(")")[0].strip()
        else:
            feature_name = desc
            meaning = desc

        feature_table.append({
            "feature_key": feat,
            "feature_name": feature_name,
            "meaning": meaning,
            "raw_value": float(raw_val),
            "z_score": float(z) if not pd.isna(z) else None,
            "healthy_interval_low": float(lo) if not pd.isna(lo) else None,
            "healthy_interval_high": float(hi) if not pd.isna(hi) else None,
            "within_healthy_interval": None if in_range is None else bool(in_range),
            "direction": direction,
            "evidence_flag": flag
        })

        interval_str = f"[{lo:.4g}, {hi:.4g}]" if not pd.isna(lo) and not pd.isna(hi) else "[unknown]"
        raw_lines.append(
            f"{desc}: {raw_val:.6g}, z score: {z:.2f}, 95% interval: {interval_str}, evidence flag: {flag}"
        )

    # sort features by |z|
    feature_table = sorted(
        feature_table,
        key=lambda x: abs(x["z_score"]) if x["z_score"] is not None else -1,
        reverse=True
    )

    raw_prompt = "\n".join(raw_lines)
    retrieval_query = build_retrieval_query(age_str, gender_str, feature_table)
    llm_case_report = build_llm_case_report(pid, age_str, gender_str, feature_table)

    records.append({
        "patient_ID": pid,
        "age": age_str,
        "gender": gender_str,
        "raw_prompt": raw_prompt,
        "retrieval_query": retrieval_query,
        "llm_case_report": llm_case_report,
        "feature_table": feature_table
    })

# save
prompts_df = pd.DataFrame([{
    "patient_ID": r["patient_ID"],
    "age": r["age"],
    "gender": r["gender"],
    "retrieval_query": r["retrieval_query"],
    "llm_case_report": r["llm_case_report"]
} for r in records])

csv_path = os.path.join(OUT_DIR, "Radiomics_report_flag.csv")
json_path = os.path.join(OUT_DIR, "Radiomics_report_flag.json")

prompts_df.to_csv(csv_path, index=False)
with open(json_path, "w") as f:
    json.dump(records, f, indent=2)

print(f"Saved CSV: {csv_path}")
print(f"Saved JSON: {json_path}")
print(f"Total reports: {len(records)}")
print("\nSample LLM case report:\n")
print(records[0]["llm_case_report"][:2500])
