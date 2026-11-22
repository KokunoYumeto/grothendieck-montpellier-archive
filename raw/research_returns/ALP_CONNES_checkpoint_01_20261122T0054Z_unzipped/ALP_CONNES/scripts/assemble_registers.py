#!/usr/bin/env python3
"""Merge source registers, preserving check events and explicit open gates."""
from pathlib import Path
import csv
import json

root = Path(__file__).resolve().parents[1]
schemas = {
    "CHECK_EVENTS.tsv": ["statement_id", "date_utc", "who", "model", "effort", "run", "type", "outcome", "detail"],
    "QUESTIONS.tsv": ["id", "source_locator", "question", "state", "finding_or_gate"],
}
receipt = {}
for target, columns in schemas.items():
    pattern = "*_events.tsv" if target.startswith("CHECK") else "*_questions.tsv"
    paths = sorted([*root.joinpath("modules").glob(pattern), *root.joinpath("reviews").glob(pattern)])
    rows = []
    seen = set()
    for path in paths:
        with path.open(newline="") as source:
            reader = csv.DictReader(source, delimiter="\t")
            if reader.fieldnames != columns:
                raise ValueError(f"Unexpected columns in {path}: {reader.fieldnames}")
            for row in reader:
                if None in row:
                    raise ValueError(f"Malformed row in {path}")
                key = tuple(row[c] for c in columns)
                if key not in seen:
                    seen.add(key)
                    rows.append(row)
    if target == "QUESTIONS.tsv":
        ids = [row["id"] for row in rows]
        if len(ids) != len(set(ids)):
            raise ValueError("Conflicting duplicate question IDs")
    with root.joinpath(target).open("w", newline="") as dest:
        writer = csv.DictWriter(dest, columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    receipt[target] = {"rows": len(rows), "sources": [str(p.relative_to(root)) for p in paths]}
root.joinpath("evidence/register_assembly.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
