#!/usr/bin/env python3
"""Record a human-visible independent text review, with reviewed file hashes.

Read a JSON array on standard input. Each item has unit, paths, finding, action.
This helper records an inspection already performed; it does not perform one.
All recorded paths are relative to the edition folder.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "records" / "INDEPENDENT_TEXT_REVIEW.tsv"
FIELDS = ["review_id", "unit", "reviewer", "reviewed_files", "sha256", "finding", "action"]


def main():
    items = json.load(sys.stdin)
    rows = []
    if DESTINATION.exists():
        with DESTINATION.open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
    for item in items:
        paths = item["paths"]
        for name in paths:
            path = Path(name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("Review paths must be ZIP-relative")
        rows.append({
            "review_id": f"ROOT-TEXT-{len(rows)+1:03d}",
            "unit": item["unit"],
            "reviewer": "GPT-6 Astra; independent root review",
            "reviewed_files": "; ".join(paths),
            "sha256": "; ".join(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths),
            "finding": item["finding"],
            "action": item["action"],
        })
    with DESTINATION.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"record": "records/INDEPENDENT_TEXT_REVIEW.tsv", "rows": len(rows)}))


if __name__ == "__main__":
    main()
