#!/usr/bin/env python3
"""Clarify existing access records; this does not retrieve or re-read any source."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
NOW = datetime.datetime.now(datetime.timezone.utc)
CHANGES = {
    "B_references.bib": [
        (
            "Publisher metadata opened; original full text not obtained. Proof used here was opened in the Stacks Project, Theorem 59.82.7, tag 09ZI",
            "Not opened: original full text. Opened: publisher metadata and the replacement proof in the Stacks Project, Theorem 59.82.7, tag 09ZI. This does not constitute a direct reading of the original article",
        ),
        (
            "Required original theorem passage not obtained; Corollary 6.6.4 is identified by the opened proof and generalization in Bhatt--Mathew, Theorem 6.11",
            "Not opened: original full text, including the required theorem passage. Opened: the proof and generalization in Bhatt--Mathew, Theorem 6.11, which identifies the original Corollary 6.6.4. This does not constitute a direct reading of that corollary",
        ),
        (
            "Publisher's Lecture 1 excerpt opened; Proposition (1.1). First edition 1980; full first edition not accessed",
            "Opened: publisher's Lecture 1 excerpt, Proposition (1.1). Not opened: the full 1980 first edition. The excerpt reading is not a claim to have read the complete first edition",
        ),
    ],
    "A567_references.bib": [
        (
            "Publisher metadata opened; full text unavailable, hence no body theorem invoked",
            "Not opened: original full text. Opened: publisher metadata. No body theorem from the unavailable full text is invoked",
        ),
        (
            "Official bibliography and publisher metadata opened; full text was not accessible, so no internal theorem is invoked",
            "Not opened: original full text. Opened: official bibliography and publisher metadata. No internal theorem from the unavailable full text is invoked",
        ),
        (
            "Publisher metadata opened; body not accessible. The inertia theorem is used only through the opened complete proof in Stix (2012), Theorem 30",
            "Not opened: original full text. Opened: publisher metadata and the complete replacement proof in Stix (2012), Theorem 30. The inertia theorem is used only through that opened replacement proof",
        ),
        (
            "Preview opened: introduction Section 0.10 and contents of Chapter 12; no inaccessible body theorem is invoked",
            "Opened: preview, introduction Section 0.10 and contents of Chapter 12. Not opened: the remaining full text. No inaccessible body theorem is invoked",
        ),
    ],
}

record = {
    "started_utc": NOW.isoformat(),
    "scope": "Clerical source-access distinctions and a historical component-count correction, authorized by root; no source opening, mathematical check, or movement claim",
    "files": [],
}
for name, replacements in CHANGES.items():
    path = ROOT / name
    before = path.read_text()
    after = before
    applied = []
    for old, new in replacements:
        if old in after:
            assert after.count(old) == 1, (name, old)
            after = after.replace(old, new)
            applied.append({"old": old, "new": new})
        else:
            assert new in after, (name, "Neither expected original nor replacement note found")
    path.write_text(after)
    record["files"].append({
        "path": name,
        "sha256_before": hashlib.sha256(before.encode()).hexdigest(),
        "sha256_after": hashlib.sha256(after.encode()).hexdigest(),
        "replacements": applied,
    })

path = ROOT / "notes/C_report.md"
before = path.read_text()
old = "Idempotently preserves existing rows and adds C.33–C.36. The ledger now contains36 C-owned statements, including contributions to Part A."
count = len(list(csv.DictReader((ROOT / "C_results.csv").open())))
new = (
    "The initial reconciliation on19 November2026 preserved existing rows and added C.33–C.36; "
    "the ledger contained36 rows at that stage. The current C ledger contains"
    + str(count)
    + " rows as checked at "
    + NOW.strftime("%Y-%m-%d %H:%M:%S UTC")
    + "; later additions include the five constructible-category statements. "
    "This is a historical metadata count, not a new computation."
)
assert before.count(old) == 1, "Expected one historical count to clarify"
after = before.replace(old, new)
path.write_text(after)
record["files"].append({
    "path": "notes/C_report.md",
    "sha256_before": hashlib.sha256(before.encode()).hexdigest(),
    "sha256_after": hashlib.sha256(after.encode()).hexdigest(),
    "replacements": [{"old": old, "new": new}],
})
record["bibliography_notes_clarified"] = sum(len(v) for v in CHANGES.values())
record["historical_count_corrections"] = 1
record["current_C_rows"] = count
record["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
record["elapsed_seconds"] = time.perf_counter() - START
destination = ROOT / "logs/C_access_marker_cleanup.json"
destination.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in record.items() if k != "files"}, indent=2))
