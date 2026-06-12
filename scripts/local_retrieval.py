import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple


# =========================
# Paths
# =========================
BASE_DIR = Path("ild_vs_health")
MERGED_DIR = BASE_DIR / "merged"
CURATED_DIR = BASE_DIR / "curated"
RETRIEVAL_DIR = BASE_DIR / "retrieval_units"
OUTPUT_DIR = BASE_DIR / "final_llm_inputs"

PATIENT_REPORTS_JSON = Path("/NLST_lung_data/llm_validation/Radiomics_report.json")

JSONL_INPUT = MERGED_DIR / "paper_summaries.jsonl"
DIRECT_CORE_CHUNKS = RETRIEVAL_DIR / "direct_core_chunks.jsonl"
SUPPORTING_CHUNKS = RETRIEVAL_DIR / "supporting_feature_chunks.jsonl"

FINAL_EVIDENCE_MD = CURATED_DIR / "Final_Evidence_Abstract.md"
DIRECT_CORE_MD = CURATED_DIR / "Direct_Core_Evidence.md"
FEATURE_DICT_MD = CURATED_DIR / "Radiomics_Feature_Dictionary.md"
STATIC_SYSTEM_PROMPT_TXT = OUTPUT_DIR / "static_system_prompt.txt"


# =========================
# Config
# =========================
DEFAULT_TOP_K_DIRECT = 2
DEFAULT_TOP_K_SUPPORTING = 4
DEFAULT_TOP_K_WEAK = 2
MIN_SCORE_THRESHOLD = 0.01

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "by",
    "is", "are", "was", "were", "be", "this", "that", "these", "those", "as",
    "at", "from", "it", "its", "their", "into", "than", "then", "using", "used",
    "may", "can", "should", "not", "no", "yes", "only", "more", "most", "less",
    "higher", "lower", "increase", "increased", "decrease", "decreased", "patient",
    "age", "sex", "gender", "report", "feature", "features", "healthy", "interval",
    "raw", "value", "score"
}


# =========================
# Generic helpers
# =========================
def ensure_directories() -> None:
    RETRIEVAL_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def normalize_str(x: Any) -> str:
    if x is None:
        return ""
    return str(x).strip()


def normalize_lower(x: Any) -> str:
    return normalize_str(x).lower()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def read_optional_text(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


# =========================
# Stage-2 compatible paper filtering
# =========================
def is_success(row: Dict[str, Any]) -> bool:
    return normalize_lower(row.get("status")) == "success"


def has_feature_content(row: Dict[str, Any]) -> bool:
    def norm_list(xs):
        if xs is None:
            return []
        if isinstance(xs, list):
            return [normalize_str(x) for x in xs if normalize_str(x)]
        if isinstance(xs, str):
            xs = xs.strip()
            return [xs] if xs else []
        return []

    return (
        len(norm_list(row.get("radiomics_features_supporting_ILD"))) > 0
        or len(norm_list(row.get("radiomics_features_supporting_Healthy"))) > 0
        or len(norm_list(row.get("feature_interpretation_notes"))) > 0
        or len(norm_list(row.get("weak_or_unstable_features"))) > 0
    )


def is_direct_core_paper(row: Dict[str, Any]) -> bool:
    if not is_success(row):
        return False

    task_type = normalize_lower(row.get("task_type"))
    direct_relevance = normalize_lower(row.get("direct_relevance"))
    healthy_controls = normalize_lower(row.get("healthy_controls_included"))

    return (
        task_type == "ild_vs_healthy"
        and direct_relevance in {"medium", "high"}
        and healthy_controls == "yes"
    )


def is_supporting_feature_paper(row: Dict[str, Any]) -> bool:
    if not is_success(row):
        return False

    task_type = normalize_lower(row.get("task_type"))
    evidence_strength = normalize_lower(row.get("evidence_strength"))

    return (
        task_type in {"ild_vs_healthy", "subtype", "severity", "other"}
        and evidence_strength in {"moderate", "strong"}
        and has_feature_content(row)
    )


# =========================
# Retrieval-unit builders
# =========================
def norm_list(xs: Any) -> List[str]:
    if xs is None:
        return []
    if isinstance(xs, list):
        return [normalize_str(x) for x in xs if normalize_str(x)]
    if isinstance(xs, str):
        xs = xs.strip()
        return [xs] if xs else []
    return []


def build_direct_chunk(row: Dict[str, Any]) -> Dict[str, Any]:
    ild_feats = norm_list(row.get("radiomics_features_supporting_ILD"))
    healthy_feats = norm_list(row.get("radiomics_features_supporting_Healthy"))
    weak_feats = norm_list(row.get("weak_or_unstable_features"))
    notes = norm_list(row.get("feature_interpretation_notes"))

    text_parts = [
        f"Paper ID: {row.get('paper_id', '')}",
        f"Title: {row.get('title', 'unclear')}",
        f"One-sentence takeaway: {row.get('one_sentence_takeaway', 'unclear')}",
        f"Population summary: {row.get('population_summary', 'unclear')}",
    ]

    if ild_feats:
        text_parts.append("ILD-supporting features: " + "; ".join(ild_feats))
    if healthy_feats:
        text_parts.append("Healthy-supporting features: " + "; ".join(healthy_feats))
    if weak_feats:
        text_parts.append("Weak/non-specific features: " + "; ".join(weak_feats))
    if notes:
        text_parts.append("Interpretation notes: " + "; ".join(notes))

    return {
        "chunk_id": f"{row.get('paper_id')}_direct_summary",
        "paper_id": row.get("paper_id"),
        "layer": "direct_core",
        "chunk_type": "paper_summary",
        "title": row.get("title", "unclear"),
        "task_type": row.get("task_type", "unclear"),
        "healthy_controls_included": row.get("healthy_controls_included", "unclear"),
        "evidence_strength": row.get("evidence_strength", "unclear"),
        "text": "\n".join(text_parts),
    }


def build_supporting_chunks(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    chunks = []
    paper_id = row.get("paper_id")
    title = row.get("title", "unclear")

    ild_feats = norm_list(row.get("radiomics_features_supporting_ILD"))
    healthy_feats = norm_list(row.get("radiomics_features_supporting_Healthy"))
    weak_feats = norm_list(row.get("weak_or_unstable_features"))
    notes = norm_list(row.get("feature_interpretation_notes"))

    for i, feat in enumerate(ild_feats, start=1):
        chunks.append({
            "chunk_id": f"{paper_id}_ILD_{i}",
            "paper_id": paper_id,
            "layer": "supporting_feature",
            "chunk_type": "supports_ild",
            "title": title,
            "evidence_strength": row.get("evidence_strength", "unclear"),
            "text": f"Paper {paper_id} ({title}) reports an ILD-supporting feature pattern: {feat}. "
                    f"Takeaway: {row.get('one_sentence_takeaway', 'unclear')}"
        })

    for i, feat in enumerate(healthy_feats, start=1):
        chunks.append({
            "chunk_id": f"{paper_id}_HEALTHY_{i}",
            "paper_id": paper_id,
            "layer": "supporting_feature",
            "chunk_type": "supports_healthy",
            "title": title,
            "evidence_strength": row.get("evidence_strength", "unclear"),
            "text": f"Paper {paper_id} ({title}) reports a Healthy-supporting feature pattern: {feat}. "
                    f"Takeaway: {row.get('one_sentence_takeaway', 'unclear')}"
        })

    for i, feat in enumerate(weak_feats, start=1):
        chunks.append({
            "chunk_id": f"{paper_id}_WEAK_{i}",
            "paper_id": paper_id,
            "layer": "supporting_feature",
            "chunk_type": "weak_or_nonspecific",
            "title": title,
            "evidence_strength": row.get("evidence_strength", "unclear"),
            "text": f"Paper {paper_id} ({title}) identifies a weak or non-specific pattern: {feat}. "
                    f"Takeaway: {row.get('one_sentence_takeaway', 'unclear')}"
        })

    for i, note in enumerate(notes, start=1):
        chunks.append({
            "chunk_id": f"{paper_id}_NOTE_{i}",
            "paper_id": paper_id,
            "layer": "supporting_feature",
            "chunk_type": "interpretation_note",
            "title": title,
            "evidence_strength": row.get("evidence_strength", "unclear"),
            "text": f"Paper {paper_id} ({title}) provides an interpretation note: {note}. "
                    f"Takeaway: {row.get('one_sentence_takeaway', 'unclear')}"
        })

    return chunks


def build_retrieval_units(rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    success_rows = [r for r in rows if is_success(r)]
    direct_rows = [r for r in success_rows if is_direct_core_paper(r)]
    supporting_rows = [r for r in success_rows if is_supporting_feature_paper(r)]

    direct_chunks = [build_direct_chunk(r) for r in direct_rows]
    supporting_chunks = []
    for row in supporting_rows:
        supporting_chunks.extend(build_supporting_chunks(row))

    return direct_chunks, supporting_chunks


# =========================
# Retrieval scoring
# =========================
def tokenize(text: str) -> List[str]:
    text = normalize_lower(text)
    tokens = re.findall(r"[a-zA-Z0-9_\-]+", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def jaccard_score(query_tokens: List[str], doc_tokens: List[str]) -> float:
    q, d = set(query_tokens), set(doc_tokens)
    if not q or not d:
        return 0.0
    inter = len(q & d)
    union = len(q | d)
    return inter / union if union else 0.0


def overlap_score(query_tokens: List[str], doc_tokens: List[str]) -> float:
    q, d = set(query_tokens), set(doc_tokens)
    if not q:
        return 0.0
    return len(q & d) / len(q)


def weighted_score(query_tokens: List[str], doc_tokens: List[str], text: str) -> float:
    base = 0.75 * overlap_score(query_tokens, doc_tokens) + 0.25 * jaccard_score(query_tokens, doc_tokens)

    text_l = text.lower()
    bonus = 0.0
    for kw in [
        "heterogeneity", "homogeneity", "entropy", "texture", "contrast",
        "radiomics", "healthy", "ild", "kurtosis", "cluster", "shade",
        "prominence", "gray", "high", "low", "asymmetry", "irregularity"
    ]:
        if kw in text_l:
            bonus += 0.008
    return base + bonus


def score_chunks(query: str, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    query_tokens = tokenize(query)
    scored = []

    for chunk in chunks:
        doc_tokens = tokenize(chunk["text"])
        score = weighted_score(query_tokens, doc_tokens, chunk["text"])
        if score >= MIN_SCORE_THRESHOLD:
            scored.append({**chunk, "score": round(score, 6)})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


def retrieve_evidence(
    query: str,
    direct_chunks: List[Dict[str, Any]],
    supporting_chunks: List[Dict[str, Any]],
    top_k_direct: int,
    top_k_supporting: int,
    top_k_weak: int
) -> Dict[str, Any]:
    direct_scored = score_chunks(query, direct_chunks)
    supporting_scored = score_chunks(query, supporting_chunks)

    direct_top = direct_scored[:top_k_direct]
    supporting_top = [
        c for c in supporting_scored
        if c["chunk_type"] in {"supports_ild", "supports_healthy", "interpretation_note"}
    ][:top_k_supporting]
    weak_top = [
        c for c in supporting_scored
        if c["chunk_type"] == "weak_or_nonspecific"
    ][:top_k_weak]

    return {
        "query": query,
        "direct_evidence": direct_top,
        "supporting_evidence": supporting_top,
        "cautionary_evidence": weak_top,
    }


# =========================
# Patient report helpers
# =========================
def build_full_feature_appendix(feature_table: List[Dict[str, Any]]) -> str:
    lines = ["[Structured feature table]"]
    for feat in feature_table:
        lines.append(
            f"- {feat.get('feature_name', feat.get('feature_key', 'unknown'))} "
            f"({feat.get('meaning', 'unknown')}): "
            f"raw={feat.get('raw_value')}, "
            f"z={feat.get('z_score')}, "
            f"healthy_interval=[{feat.get('healthy_interval_low')}, {feat.get('healthy_interval_high')}], "
            f"within_interval={feat.get('within_healthy_interval')}, "
            f"direction={feat.get('direction')}, "
            f"evidence_flag={feat.get('evidence_flag')}"
        )
    return "\n".join(lines)


def build_case_block(patient: Dict[str, Any]) -> str:
    patient_id = patient.get("patient_ID", patient.get("patient_id", "unknown"))
    age = patient.get("age", "")
    gender = patient.get("gender", patient.get("sex", ""))

    llm_case_report = normalize_str(patient.get("llm_case_report", ""))

    parts = [
        "[Patient]",
        f"patient_id: {patient_id}"
        # f"age: {age}",
        # f"sex: {gender}",
        "",
        #"[LLM-ready radiomics report]",
        llm_case_report if llm_case_report else "- Missing llm_case_report",
    ]
    return "\n".join(parts)


def format_evidence(items: List[Dict[str, Any]], title: str) -> str:
    lines = [f"[{title}]"]
    if not items:
        lines.append("- None")
        return "\n".join(lines)

    for i, item in enumerate(items, start=1):
        lines.append(f"{i}. ({item['paper_id']} | score={item['score']}) {item['text']}")
    return "\n".join(lines)


def build_static_system_prompt(final_evidence: str) -> str:
    return f"""You are an elite academic pulmonologist, thoracic radiologist, and expert in machine learning and radiomics. You are good at ILD patient classification, focusing on distinguishing ILD patients vs Healthy individuals according to the combination of clinical demographics and IBSI-standardized quantitative CT radiomic features. The radiomic features have been robustly normalized against a healthy baseline (the National Lung Screening Trial cohort).

Use the provided evidence in a layered way:
1. Give highest weight to [Direct Core Evidence].
2. Use [Supporting Feature Evidence] to interpret radiomics patterns.
3. Use [Cautionary Evidence] to avoid overinterpreting weak or non-specific features.

Rules:
- Do not rely on a single feature.
- Final judgment must consider the overall multi-feature pattern.
- If evidence is mixed or incomplete, reduce confidence.
- Radiomics alone can support classification, but weak or ambiguous signals should lower confidence.

Output JSON with exactly these fields:
- patient_id
- classification: ILD or Healthy
- confidence

[Final Evidence Abstract]
{final_evidence}
"""


def build_sample_user_prompt(patient: Dict[str, Any], retrieved: Dict[str, Any]) -> str:
    patient_block = build_case_block(patient)

    return f"""{patient_block}

{format_evidence(retrieved['direct_evidence'], 'Direct Core Evidence')}

{format_evidence(retrieved['supporting_evidence'], 'Supporting Feature Evidence')}

{format_evidence(retrieved['cautionary_evidence'], 'Cautionary Evidence')}
"""




# =========================
# Main
# =========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--patient-json", type=str, default=str(PATIENT_REPORTS_JSON))
    parser.add_argument("--topk-direct", type=int, default=DEFAULT_TOP_K_DIRECT)
    parser.add_argument("--topk-supporting", type=int, default=DEFAULT_TOP_K_SUPPORTING)
    parser.add_argument("--topk-weak", type=int, default=DEFAULT_TOP_K_WEAK)
    parser.add_argument("--limit", type=int, default=0, help="Only process first N patients; 0 means all")
    args = parser.parse_args()

    topk_direct = args.topk_direct
    topk_supporting = args.topk_supporting
    topk_weak = args.topk_weak

    ensure_directories()

    patient_path = Path(args.patient_json)
    if not patient_path.exists():
        raise FileNotFoundError(f"Patient JSON not found: {patient_path}")

    if not JSONL_INPUT.exists():
        raise FileNotFoundError(f"Missing paper summaries: {JSONL_INPUT}")

    paper_rows = load_jsonl(JSONL_INPUT)
    direct_chunks, supporting_chunks = build_retrieval_units(paper_rows)

    write_json(DIRECT_CORE_CHUNKS, direct_chunks)
    write_json(SUPPORTING_CHUNKS, supporting_chunks)

    patients = load_json(patient_path)
    if args.limit and args.limit > 0:
        patients = patients[:args.limit]

    final_evidence = read_optional_text(FINAL_EVIDENCE_MD)
    static_system_prompt = build_static_system_prompt(final_evidence)
    write_text(STATIC_SYSTEM_PROMPT_TXT, static_system_prompt)

    manifest = []

    for patient in patients:
        patient_id = normalize_str(patient.get("patient_ID", patient.get("patient_id", "unknown")))
        retrieval_query = normalize_str(patient.get("retrieval_query", ""))
        if not retrieval_query:
            retrieval_query = normalize_str(patient.get("llm_case_report", ""))

        retrieved = retrieve_evidence(
            retrieval_query,
            direct_chunks,
            supporting_chunks,
            topk_direct,
            topk_supporting,
            topk_weak
        )

        rag_package = {
            "patient_id": patient_id,
            "retrieval_query": retrieval_query,
            "patient_payload": patient,
            "final_evidence_abstract": final_evidence,
            "retrieved_evidence": retrieved
        }

        user_prompt = build_sample_user_prompt(patient, retrieved)
        rag_package = {
            "patient_id": patient_id,
            "retrieval_query": retrieval_query,
            "patient_payload": patient,
            "retrieved_evidence": retrieved
        }

        patient_dir = OUTPUT_DIR / patient_id
        patient_dir.mkdir(parents=True, exist_ok=True)

        rag_json_path = patient_dir / f"{patient_id}_rag_package.json"
        user_prompt_path = patient_dir / f"{patient_id}_user_prompt.txt"

        write_json(rag_json_path, rag_package)
        write_text(user_prompt_path, user_prompt)

        manifest.append({
            "patient_id": patient_id,
            "rag_package": str(rag_json_path),
            "user_prompt": str(user_prompt_path),
            "static_system_prompt": str(STATIC_SYSTEM_PROMPT_TXT)
        })

    write_json(OUTPUT_DIR / "manifest.json", manifest)

    print(f"Processed patients: {len(manifest)}")
    print(f"Saved manifest: {OUTPUT_DIR / 'manifest.json'}")
    print(f"Saved static system prompt: {STATIC_SYSTEM_PROMPT_TXT}")
    print(f"Direct retrieval units: {DIRECT_CORE_CHUNKS}")
    print(f"Supporting retrieval units: {SUPPORTING_CHUNKS}")

if __name__ == "__main__":
    main()
