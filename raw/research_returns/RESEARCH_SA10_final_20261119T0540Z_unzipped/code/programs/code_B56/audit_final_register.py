#!/usr/bin/env python3
"""Read-only audit of the actual included manuscript and result registers.

Only this subagent's audit report/output files are written. The root
manuscript, registers, bibliography and check-event aggregators are read.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import datetime
import hashlib
import json
import re
import time

started = time.perf_counter()
work = Path(__file__).resolve().parents[1]
root = work / "RESEARCH_SA10_paper.tex"
snapshot = {}
def read(path):
    if path not in snapshot:
        snapshot[path] = path.read_text()
    return snapshot[path]

included = []
seen = set()
missing_includes = []
def descend(path):
    if path in seen:
        return
    if not path.exists():
        missing_includes.append(str(path.relative_to(work)))
        return
    seen.add(path)
    included.append(path)
    text = read(path)
    for match in re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", text):
        name = match.group(1)
        child = path.parent / name
        if not child.suffix:
            child = child.with_suffix(".tex")
        descend(child)
descend(root)

id_pattern = r"[ABC]\d+\.(?:B)?\d+[a-z]?(?:\.\d+)*"
heading_pattern = re.compile(
    r"(?:\\(?:sub)*section\*?\s*\{|\\paragraph\*?\s*\{|"
    r"\\begin\{(?:result|theorem|lemma|proposition|corollary)\}\s*\[)"
    r"\s*(" + id_pattern + r")(?=[.;:\s(\-—])"
)
statements = defaultdict(list)
citations = defaultdict(list)
for path in included:
    text = read(path)
    for match in heading_pattern.finditer(text):
        statements[match.group(1)].append({
            "file": str(path.relative_to(work)),
            "line": text.count("\n", 0, match.start()) + 1
        })
    for match in re.finditer(r"\\(?:[A-Za-z]*cite[A-Za-z]*|nocite)\*?(?:\[[^\]]*\])*\{([^}]+)\}", text):
        for key in match.group(1).split(","):
            citations[key.strip()].append(str(path.relative_to(work)))

register_names = ["RESULTS_A.csv", "RESULTS_B.csv", "results_B56.csv",
                  "RESULTS_C.csv", "RESULTS_C1_B.csv"]
rows_by_id = defaultdict(list)
register_counts = {}
for name in register_names:
    text = read(work / name)
    rows = list(csv.DictReader(text.splitlines()))
    register_counts[name] = len(rows)
    for row in rows:
        rows_by_id[row["id"]].append({"register": name, **row})

event_names = ["CHECK_EVENTS_A.tsv", "CHECK_EVENTS_B.tsv", "CHECK_EVENTS_B56.tsv",
               "CHECK_EVENTS_C.tsv", "CHECK_EVENTS_C1_B.tsv", "CHECK_EVENTS_C4_B.tsv"]
events_by_id = defaultdict(list)
for name in event_names:
    text = read(work / name)
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        events_by_id[row["statement_id"]].append({"file": name, **row})
aggregate_events = defaultdict(list)
if (work / "CHECK_EVENTS.tsv").exists():
    for row in csv.DictReader(read(work / "CHECK_EVENTS.tsv").splitlines(), delimiter="\t"):
        aggregate_events[row["statement_id"]].append(row)
inherited_c_ids = []
if (work / "C_inherited_audit.tsv").exists():
    inherited_c_ids = [row["prior_id"] for row in csv.DictReader(
        read(work / "C_inherited_audit.tsv").splitlines(), delimiter="\t")]

bib_text = read(work / "RESEARCH_SA10_references.bib")
bib_starts = list(re.finditer(r"(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", bib_text))
bib_by_key = defaultdict(list)
for pos, match in enumerate(bib_starts):
    end = bib_starts[pos + 1].start() if pos + 1 < len(bib_starts) else len(bib_text)
    bib_by_key[match.group(2)].append(bib_text[match.start():end])
bib_missing_status = []
bib_cited_not_opened = []
for key in citations:
    for block in bib_by_key.get(key, []):
        if not re.search(r"(?i)\bnote\s*=", block):
            bib_missing_status.append(key)
        elif not re.search(r"(?i)\bopened\b|not opened|unavailable|not accessed", block):
            bib_missing_status.append(key)
        elif re.search(r"(?i)not opened|unavailable|not accessed", block):
            bib_cited_not_opened.append(key)

result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "Actual recursive TeX inputs; only numbered statement headings, not equation tags or older drafts.",
    "included_files": [str(path.relative_to(work)) for path in included],
    "missing_includes": missing_includes,
    "numbered_statements": len(statements),
    "register_counts": register_counts,
    "register_rows": sum(register_counts.values()),
    "missing_result_rows": sorted(set(statements) - set(rows_by_id)),
    "duplicate_result_rows": {k: len(v) for k, v in rows_by_id.items() if len(v) != 1},
    "register_ids_without_included_heading": sorted(set(rows_by_id) - set(statements)),
    "duplicate_statement_headings": {k: v for k, v in statements.items() if len(v) != 1},
    "missing_exact_source_check_events": sorted(set(statements) - set(events_by_id)),
    "missing_exact_aggregate_check_events": sorted(set(statements) - set(aggregate_events)),
    "inherited_C_audit_ids": len(inherited_c_ids),
    "inherited_C_ids_missing_exact_aggregate_event": sorted(set(inherited_c_ids) - set(aggregate_events)),
    "cited_keys": len(citations),
    "bibliography_keys": len(bib_by_key),
    "missing_bibliography_keys": sorted(set(citations) - set(bib_by_key)),
    "duplicate_bibliography_keys": {k: len(v) for k, v in bib_by_key.items() if len(v) != 1},
    "cited_bibliography_keys_missing_access_status": sorted(set(bib_missing_status)),
    "cited_bibliography_keys_explicitly_not_opened": sorted(set(bib_cited_not_opened)),
    "uncited_bibliography_keys": sorted(set(bib_by_key) - set(citations)),
    "statement_inventory": {k: {"heading": statements[k],
                                 "result_rows": len(rows_by_id[k]),
                                 "source_check_events": len(events_by_id[k]),
                                 "aggregate_check_events": len(aggregate_events[k])}
                            for k in sorted(statements)},
    "snapshot_sha256": {str(path.relative_to(work)): hashlib.sha256(text.encode()).hexdigest()
                        for path, text in snapshot.items()},
    "seconds": round(time.perf_counter() - started, 9)
}
(work / "FINAL_register_audit_B56.json").write_text(json.dumps(result, indent=2) + "\n")
summary = {key: value for key, value in result.items()
           if key not in {"statement_inventory", "snapshot_sha256"}}
print(json.dumps(summary, indent=2))

lines = ["# Read-only final statement/register audit", "",
         "AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, "
         "run /root/hypercovers_finite_sets. No priority claimed.", "",
         "Snapshot: " + result["utc"] + ". Runtime: " + str(result["seconds"]) + " seconds.", "",
         "The audit recursively follows the actual inputs of RESEARCH_SA10_paper.tex. "
         "It matches numbered theorem/statement headings against the five requested CSV registers "
         "and exact statement IDs in source and aggregated check events. Equation tags and older "
         "drafts are excluded. The script is read-only for all root and other-agent files.", "",
         "## Counts", "",
         f"- Included TeX files: {len(included)}.",
         f"- Numbered statement IDs: {len(statements)}.",
         f"- CSV rows: {sum(register_counts.values())}.",
         f"- Cited bibliography keys: {len(citations)}.",
         f"- Bibliography keys: {len(bib_by_key)}.", "",
         "## Mechanical findings", ""]
for key in ["missing_includes", "missing_result_rows", "duplicate_result_rows",
            "register_ids_without_included_heading", "duplicate_statement_headings",
            "missing_exact_source_check_events", "missing_exact_aggregate_check_events",
            "inherited_C_ids_missing_exact_aggregate_event",
            "missing_bibliography_keys", "duplicate_bibliography_keys",
            "cited_bibliography_keys_missing_access_status",
            "cited_bibliography_keys_explicitly_not_opened"]:
    lines.append("- " + key + ": `" + json.dumps(result[key]) + "`.")
lines += ["", "These checks verify recorded source-status labels and citation linkage; "
          "they do not claim a new independent opening of every cited source. "
          "The JSON inventory records every statement's exact source/result/event counts and "
          "SHA256 hashes of all inputs, so this snapshot is distinguishable from later integration changes.", "",
          "## Actual included files", ""]
lines += ["- `" + str(path.relative_to(work)) + "`." for path in included]
(work / "FINAL_register_audit_B56.md").write_text("\n".join(lines) + "\n")
