import os
import re
import json
import time
import argparse
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests
import pandas as pd
import numpy as np
from datetime import datetime



# =========================
# Config
# =========================
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "your own api key"

BASE_DIR = Path("ild_vs_healthy")
# FINAL_INPUTS_DIR = BASE_DIR / "final_llm_inputs"
# MANIFEST_PATH = FINAL_INPUTS_DIR / "manifest.json"

LABELS_CSV = Path("your label file")

# OUT_DIR = BASE_DIR / "eval_outputs/v1"
# OUT_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_MODELS = [
    "google/gemini-3-flash-preview",
    "openai/gpt-5-mini",
    "deepseek/deepseek-v3.2",
    "qwen/qwen3.6-plus",
    "amazon/nova-2-lite-v1"
]

SLEEP_SECONDS = 1.0
MAX_RETRIES = 3
TIMEOUT_SECONDS = 300

CLASS_LABELS = ["Healthy", "ILD"]


# =========================
# JSON parsing helpers
# =========================
def parse_text_to_json_and_mode(text: str) -> Tuple[Dict[str, Any], str]:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Empty or non-string content returned by model.")

    raw = text.strip()

    try:
        return json.loads(raw), "direct_json"
    except Exception:
        pass

    fenced_match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", raw, flags=re.DOTALL | re.IGNORECASE)
    if fenced_match:
        candidate = fenced_match.group(1).strip()
        return json.loads(candidate), "fenced_json"

    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end != -1 and end > start:
        candidate = raw[start:end + 1].strip()
        return json.loads(candidate), "embedded_json"

    raise ValueError("No valid JSON object found in model output.")


def parse_model_json_content(api_response: Dict[str, Any]) -> Tuple[Dict[str, Any], str]:
    message = api_response["choices"][0]["message"]
    content = message.get("content", "")

    if isinstance(content, dict):
        return content, "content_dict"

    return parse_text_to_json_and_mode(content)


# =========================
# Metrics
# =========================
def safe_div(num: float, den: float) -> float:
    return num / den if den else 0.0


def compute_binary_metrics(y_true: List[str], y_pred: List[str], positive_label: str = "ILD") -> Dict[str, Any]:
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == positive_label and p == positive_label)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t != positive_label and p != positive_label)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t != positive_label and p == positive_label)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == positive_label and p != positive_label)

    accuracy = safe_div(tp + tn, tp + tn + fp + fn)
    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    f1 = safe_div(2 * precision * recall, precision + recall)
    specificity = safe_div(tn, tn + fp)
    accuracy_healthy = safe_div(tn, tn + fn)

    return {
        "n": len(y_true),
        "total_accuracy": accuracy,
        "precision_ILD": precision,
        "acc_ILD": recall,
        "f1_ILD": f1,
        "acc_Healthy": specificity,
        "precision_Healthy": accuracy_healthy,
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
    }


# =========================
# OpenRouter call
# =========================
def call_openrouter(model: str, system_prompt: str, user_prompt: str, temperature: float = 0.0) -> Dict[str, Any]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set.")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "response_format": {"type": "json_object"},
        "plugins": [
            {"id": "response-healing"}
        ]
    }

    resp = requests.post(
        OPENROUTER_API_URL,
        headers=headers,
        json=payload,
        timeout=TIMEOUT_SECONDS
    )
    resp.raise_for_status()
    return resp.json()


# =========================
# Data loading
# =========================
def load_manifest(path: Path) -> List[Dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_labels(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "patient_ID" not in df.columns or "true_label" not in df.columns:
        raise ValueError(f"{path} must contain patient_ID and true_label columns.")
    df["patient_ID"] = df["patient_ID"].astype(str).str.zfill(3)
    df["true_label"] = df["true_label"].astype(str)
    return df[["patient_ID", "true_label"]]


def normalize_classification(x: Any) -> str:
    s = str(x).strip().lower()
    if s in {"healthy", "health", "hc"}:
        return "Healthy"
    if s in {"ild", "interstitial lung disease"}:
        return "ILD"
    return "UNKNOWN"

def normalize_model_output(parsed: Any) -> Dict[str, Any]:
    """
    Normalize model output into a dict with expected fields.
    Handles:
    - dict
    - single-item list containing dict
    - single-item list containing string
    - plain string
    """
    if isinstance(parsed, dict):
        return parsed

    if isinstance(parsed, list):
        if len(parsed) == 0:
            return {}

        # case: [{"classification": "ILD", ...}]
        if isinstance(parsed[0], dict):
            return parsed[0]

        # case: ["ILD"]
        if len(parsed) == 1 and isinstance(parsed[0], str):
            return {"classification": parsed[0]}

        # fallback: store raw list
        return {"raw_output": parsed}

    if isinstance(parsed, str):
        return {"classification": parsed}

    return {"raw_output": parsed}

# =========================
# Main evaluation loop
# =========================
def evaluate_model(
    model: str,
    manifest: List[Dict[str, Any]],
    labels_df: pd.DataFrame,
    limit: int = 0,
    temperature: float = 0.0
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = []
    labels_map = dict(zip(labels_df["patient_ID"], labels_df["true_label"]))

    items = manifest[:limit] if limit and limit > 0 else manifest

    if not items:
        raise ValueError("Manifest is empty.")

    static_system_prompt_path = Path(items[0]["static_system_prompt"])
    system_prompt = static_system_prompt_path.read_text(encoding="utf-8")

    for idx, item in enumerate(items, start=1):
        patient_id = str(item["patient_id"]).zfill(3)
        user_prompt_path = Path(item["user_prompt"])
        user_prompt = user_prompt_path.read_text(encoding="utf-8")

        truth = labels_map.get(patient_id, None)

        attempt = 0
        success = False
        last_error = ""
        parsed = {}
        api_response = {}
        parse_mode = ""

        while attempt < MAX_RETRIES and not success:
            attempt += 1
            try:
                api_response = call_openrouter(model, system_prompt, user_prompt, temperature)
                parsed, parse_mode = parse_model_json_content(api_response)
                success = True
            except Exception as e:
                last_error = str(e)
                if attempt < MAX_RETRIES:
                    time.sleep(SLEEP_SECONDS * attempt)

        if success:
            parsed = normalize_model_output(parsed)
            pred_label = normalize_classification(parsed.get("classification", "UNKNOWN"))
            confidence = parsed.get("confidence", None)

            usage = api_response.get("usage", {}) or {}
            row = {
                "model": model,
                "patient_id": patient_id,
                "true_label": truth,
                "pred_label": pred_label,
                "confidence": confidence,
                "parse_mode": parse_mode,
                "status": "success",
                "error_message": "",
                "prompt_tokens": usage.get("prompt_tokens", None),
                "completion_tokens": usage.get("completion_tokens", None),
                "total_tokens": usage.get("total_tokens", None),
                "cost": usage.get("cost", None),
                #"reasoning_summary": parsed.get("reasoning_summary", ""),
                "evidence_supporting_ILD": json.dumps(parsed.get("evidence_supporting_ILD", []), ensure_ascii=False),
                "evidence_supporting_Healthy": json.dumps(parsed.get("evidence_supporting_Healthy", []), ensure_ascii=False),
                #"uncertainties": json.dumps(parsed.get("uncertainties", []), ensure_ascii=False),
            }
        else:
            row = {
                "model": model,
                "patient_id": patient_id,
                "true_label": truth,
                "pred_label": "UNKNOWN",
                "confidence": None,
                "parse_mode": "",
                "status": "failed",
                "error_message": last_error,
                "prompt_tokens": None,
                "completion_tokens": None,
                "total_tokens": None,
                "cost": None,
                "reasoning_summary": "",
                "evidence_supporting_ILD": "[]",
                "evidence_supporting_Healthy": "[]",
                "uncertainties": "[]",
            }

        rows.append(row)

        if idx % 10 == 0 or idx == len(items):
            print(f"[{model}] processed {idx}/{len(items)}")

        time.sleep(SLEEP_SECONDS)

    results_df = pd.DataFrame(rows)

    eval_df = results_df[
        (results_df["status"] == "success") &
        (results_df["true_label"].isin(CLASS_LABELS)) &
        (results_df["pred_label"].isin(CLASS_LABELS))
    ].copy()

    if len(eval_df) > 0:
        metrics = compute_binary_metrics(
            y_true=eval_df["true_label"].tolist(),
            y_pred=eval_df["pred_label"].tolist(),
            positive_label="ILD"
        )
    else:
        metrics = {
            "n": 0,
            "accuracy": 0.0,
            "precision_ILD": 0.0,
            "recall_ILD": 0.0,
            "f1_ILD": 0.0,
            "specificity_Healthy": 0.0,
            "tp": 0, "tn": 0, "fp": 0, "fn": 0,
        }

    metrics.update({
        "model": model,
        "num_total_cases": len(results_df),
        "num_successful_calls": int((results_df["status"] == "success").sum()),
        "num_failed_calls": int((results_df["status"] == "failed").sum()),
        "sum_prompt_tokens": pd.to_numeric(results_df["prompt_tokens"], errors="coerce").fillna(0).sum(),
        "sum_completion_tokens": pd.to_numeric(results_df["completion_tokens"], errors="coerce").fillna(0).sum(),
        "sum_total_tokens": pd.to_numeric(results_df["total_tokens"], errors="coerce").fillna(0).sum(),
        "sum_cost": pd.to_numeric(results_df["cost"], errors="coerce").fillna(0).sum(),
    })

    return results_df, metrics

def to_python_types(obj):
    if isinstance(obj, dict):
        return {k: to_python_types(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_python_types(v) for v in obj]
    if isinstance(obj, tuple):
        return [to_python_types(v) for v in obj]
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj

def save_run_config(
    run_dir: Path,
    args,
    sleep_seconds: float,
    max_retries: int,
    temperature: float
) -> None:
    config_json = run_dir / "run_config.json"

    config_data = {
        "timestamp": datetime.now().isoformat(),
        "input_dir": args.input_dir,
        "out_dir": args.out_dir,
        "labels": args.labels,
        "limit": args.limit,
        "run_name": args.run_name,
        "models": args.models if hasattr(args, "models") else [],
        "sleep_seconds": sleep_seconds,
        "max_retries": max_retries,
        "temperature": temperature,
    }

    config_json.write_text(
        json.dumps(config_data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

# =========================
# Main
# =========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="*", default=DEFAULT_MODELS, help="OpenRouter model IDs")
    #parser.add_argument("--manifest", type=str, default=str(MANIFEST_PATH))
    parser.add_argument("--input-dir", type=str, default="final_llm_inputs")
    parser.add_argument("--out-dir", type=str, default="v1")
    parser.add_argument("--labels", type=str, default=str(LABELS_CSV))
    parser.add_argument("--limit", type=int, default=0, help="Only evaluate first N cases")
    parser.add_argument("--run-name", type=str, default="run1")
    parser.add_argument("--temp", type=float, default=0.0, help="Temperature for model sampling")
    args = parser.parse_args()

    FINAL_INPUTS_DIR = BASE_DIR / args.input_dir
    MANIFEST_PATH = FINAL_INPUTS_DIR / "manifest.json"

    manifest_path = Path(MANIFEST_PATH)
    OUT_DIR = BASE_DIR / "eval_outputs" / args.out_dir
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    labels_path = Path(args.labels)
    temperature = args.temp

    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")
    if not labels_path.exists():
        raise FileNotFoundError(f"Labels CSV not found: {labels_path}")

    manifest = load_manifest(manifest_path)
    labels_df = load_labels(labels_path)


    run_dir = OUT_DIR / args.run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    save_run_config(
        run_dir=run_dir,
        args=args,
        sleep_seconds=SLEEP_SECONDS,
        max_retries=MAX_RETRIES,
        temperature=temperature
    )

    metrics_rows = []

    for model in args.models:
        print(f"\n=== Evaluating model: {model} ===")
        results_df, metrics = evaluate_model(
            model=model,
            manifest=manifest,
            labels_df=labels_df,
            limit=args.limit,
            temperature=temperature
        )

        safe_model_name = model.replace("/", "__")
        results_path = run_dir / f"{safe_model_name}_case_results.csv"
        results_df.to_csv(results_path, index=False)

        metrics = to_python_types(metrics)
        metrics_rows.append(metrics)
        print(json.dumps(metrics, indent=2))

        misclassified_df = results_df[
            (results_df["status"] == "success") &
            (results_df["true_label"].isin(["Healthy", "ILD"])) &
            (results_df["pred_label"].isin(["Healthy", "ILD"])) &
            (results_df["true_label"] != results_df["pred_label"])
        ].copy()

        misclassified_ids_path = run_dir / f"{safe_model_name}_misclassified_ids.csv"
        misclassified_df[["patient_id", "true_label", "pred_label", "confidence"]].to_csv(
            misclassified_ids_path, index=False
        )

    metrics_df = pd.DataFrame(metrics_rows)
    metrics_path = run_dir / "model_metrics.csv"
    metrics_df.to_csv(metrics_path, index=False)

    print(f"\nSaved metrics: {metrics_path}")
    print(f"Saved per-case outputs under: {run_dir}")


if __name__ == "__main__":
    main()
