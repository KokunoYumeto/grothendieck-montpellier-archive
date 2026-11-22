#!/usr/bin/env python3
"""Read-only delivery reconciliation; writes only its own JSON audit record."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
record = {
    "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "Artifact, numbered-statement, event, report, source-provenance and checkpoint reconciliation; no mathematical test or source retrieval",
    "mathematical_movement": False,
}
required = [
    "RESEARCH_SA22_paper.tex", "RESEARCH_SA22_paper.pdf",
    "RESEARCH_SA22_results.csv", "RESEARCH_SA22_references.bib",
    "RESEARCH_SA22_report.md", "PROGRESS_LEDGER.md", "CHECK_EVENTS.tsv",
]
record["required_artifacts"] = {
    n: {"exists": (ROOT / n).is_file(),
        "bytes": (ROOT / n).stat().st_size if (ROOT / n).is_file() else None}
    for n in required
}
rows = list(csv.DictReader((ROOT / "RESEARCH_SA22_results.csv").open()))
events = list(csv.DictReader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
ids = {r["id"] for r in rows}
seen = set()

def expand(path):
    if path in seen:
        return ""
    seen.add(path)
    def substitute(match):
        child = ROOT / match.group(1)
        if child.suffix != ".tex":
            child = child.with_suffix(".tex")
        return expand(child) if child.exists() else match.group(0)
    return re.sub(r"\\input\{([^}]+)\}", substitute, path.read_text())

source = expand(ROOT / "RESEARCH_SA22_paper.tex")
environments = list(re.finditer(
    r"\\begin\{(theorem|proposition|lemma|corollary|definition|example|question|remark)\}(.*?)\\end\{\1\}",
    source, re.S))
labels = []
unlabelled = []
unmarked = []
for match in environments:
    env, body = match.group(1, 2)
    found = re.findall(r"\\label\{([^}]+)\}", body)
    if not found:
        unlabelled.append({"environment": env, "opening": body[:180]})
        continue
    labels.append(found[0])
    status = re.search(r"\\status\{([^}]+)\}", body)
    heading = re.match(r"\s*\[([^\]]+)\]", body)
    if not status and not (heading and re.search(r"proved|known|refuted|open", heading.group(1), re.I)) and env != "question":
        unmarked.append(found[0])
record["canonical_register"] = {
    "rows": len(rows), "columns": list(rows[0]),
    "status_counts": dict(collections.Counter(r["status"] for r in rows)),
    "included_tex_files": len(seen), "numbered_environments": len(environments),
    "unlabelled_environments": unlabelled, "unmarked_environments": unmarked,
    "included_labels_missing_from_csv": sorted(set(labels) - ids),
    "csv_labels_not_included": sorted(ids - set(labels)),
    "duplicate_ids": [k for k, v in collections.Counter(r["id"] for r in rows).items() if v > 1],
    "missing_manuscript_locators": [r["id"] for r in rows if not r["manuscript_pages"].strip()],
    "missing_proof_locations": [r["id"] for r in rows if not r["where_proved"].strip()],
    "open_rows": [r["id"] for r in rows if r["status"] == "Open"],
}
event_ids = {e["statement_id"] for e in events}
event_text = json.dumps(events, ensure_ascii=False)
used_original_ids = ["SA22-0", "SA22-2", "SA22-5", "SA22-6", "SA22-7", "SA22-8", "SA22-9", "SA22-10"]
record["event_register"] = {
    "rows": len(events), "columns": list(events[0]),
    "current_statement_ids_without_events": sorted(ids - event_ids),
    "original_ids_missing_in_canonical_snapshot": [s for s in used_original_ids if not re.search(re.escape(s) + r"(?!\d)", event_text)],
    "note": "SA22-8 and SA22-9 cross-reference corrections were delegated to A567; pending component-to-canonical consolidation is not a new proof event",
}
report = (ROOT / "RESEARCH_SA22_report.md").read_text()
first_table = report.split("## Outcome table", 1)[1].split("## Individual thesis subjects", 1)[0]
record["report"] = {
    "first_line": report.splitlines()[0],
    "outcome_rows": sum(line.startswith("| ") for line in first_table.splitlines()) - 1,
    "individual_subject_rows": len(re.findall(r"(?m)^\| Subject \d+ \|", report)),
    "pour_memoire_rows": len(re.findall(r"(?m)^\| Pour mémoire \d+ \|", report)),
    "programs_not_yet_named": [p.name for p in sorted((ROOT / "code").glob("*.py")) if p.name not in report],
    "empty_program_summary_rows": [line.split("|")[1].strip() for line in report.splitlines() if line.startswith("| `code/") and "| {} |" in line],
}
bib = (ROOT / "RESEARCH_SA22_references.bib").read_text()
entries = [s for s in re.split(r"(?m)(?=^@)", bib) if re.match(r"@\w+\s*\{", s)]
record["merged_bibliography"] = {
    "entries": len(entries),
    "note": "Component access-marker corrections made at19:57:36UTC are intentionally not merged by this audit. Substring 'opened' alone is not evidence that the cited original was read.",
}
build = json.loads((ROOT / "logs/integrated_build_summary.json").read_text())
qa = json.loads((ROOT / "logs/paper_visual_qa.json").read_text())
pdf_hash = hashlib.sha256((ROOT / "RESEARCH_SA22_paper.pdf").read_bytes()).hexdigest()
record["typesetting"] = {
    "build_started_utc": build.get("started_utc"), "passes": len(build.get("passes", [])),
    "pdf_pages": qa.get("pdf_pages"), "rendered_page_count": len(qa.get("rendered_pages", [])),
    "overfull_count": build.get("overfull_count"), "overfull_above_2pt": build.get("overfull_above_2pt"),
    "undefined_warnings": build.get("undefined_warnings"), "missing_glyphs": build.get("missing_glyphs"),
    "rerun_warnings": build.get("rerun_warnings"),
    "pdf_build_qa_hashes_match": pdf_hash == build.get("pdf_sha256") == qa.get("pdf_sha256"),
    "changed_included_sources": [n for n, h in build.get("source_hashes_after", {}).items() if hashlib.sha256((ROOT / n).read_bytes()).hexdigest() != h],
    "visual_status": qa.get("inspection", ""),
}
archives = sorted(ROOT.parent.glob("RESEARCH_SA22_checkpoint_*.zip"))
latest = archives[-1]
with zipfile.ZipFile(latest) as z:
    names = z.namelist()
with zipfile.ZipFile(archives[-2]) as z:
    previous_names = set(z.namelist())
record["checkpoint"] = {
    "latest": latest.name, "bytes": latest.stat().st_size, "entries": len(names),
    "all_mandatory_paths": all(ROOT.name + "/" + n in names for n in required),
    "nested_zips": [n for n in names if n.endswith(".zip")],
    "excluded_source_directory_entries": [n for n in names if any(t in n for t in ("/literature/", "/sources/", "/upload/"))],
    "previous_checkpoint_paths_missing": sorted(previous_names - set(names)),
    "below_500MB": latest.stat().st_size < 500_000_000,
}
reviews = sorted((ROOT / "logs").glob("progress_review_*.json"))
review = json.loads(reviews[-1].read_text())
record["last_formal_review"] = {
    k: review.get(k) for k in ("review", "actual_utc", "movement", "consecutive_stagnant_reviews", "open_rows", "next_review_utc")
}
record["elapsed_seconds"] = time.perf_counter() - START
record["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT / "logs/C_delivery_provenance_audit.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "finished_utc": record["finished_utc"], "elapsed_seconds": record["elapsed_seconds"],
    "numbered_statements": len(rows), "events": len(events), "bib_entries": len(entries),
    "latest_checkpoint": latest.name, "mathematical_movement": False,
}, indent=2))
