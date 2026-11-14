#!/usr/bin/env python3
"""Validate and append a reviewer's explicit NOTES-to-decision mappings.

Input rows are documentary judgments made after reading each concern and its
named decisions. This helper neither chooses candidates nor creates scan reviews.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from edition_core import read_tsv, write_tsv

EDITION = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input")
    p.add_argument("--reviewer", choices=["root", "middle", "late", "pipeline"], required=True)
    args = p.parse_args()
    data = json.loads(Path(args.input).read_text())
    concerns = {r["concern_id"]: r for r in read_tsv(EDITION / "records/NOTES_COVERAGE.tsv")}
    decisions = {r["id"]: r for r in read_tsv(EDITION / "CHECK_DECISIONS.tsv")}
    out = EDITION / "records" / ("NOTES_CROSSWALK_" + args.reviewer + ".tsv")
    old = read_tsv(out) if out.exists() else []
    present = {r["concern_id"]: r for r in old}
    for row in data:
        cid = row["concern_id"]
        concern = concerns[cid]
        ids = row["decision_ids"].split()
        if not ids or not row["reason"].strip():
            raise SystemExit("Explicit decision IDs and a reason are required: " + cid)
        if any(i not in decisions or decisions[i]["key"] != concern["key"] for i in ids):
            raise SystemExit("Unknown decision or wrong source page: " + cid)
        item = dict(concern_id=cid, decision_ids=" ".join(dict.fromkeys(ids)), reason=row["reason"],
                    concern_sha256=concern["concern_sha256"], reviewer="GPT-6 Astra / " + args.reviewer,
                    reviewed_utc=datetime.now(timezone.utc).isoformat())
        if cid in present:
            if any(present[cid].get(k) != item[k] for k in ("decision_ids", "reason", "concern_sha256")):
                raise SystemExit("Conflicting earlier mapping requires explicit revision: " + cid)
            continue
        old.append(item)
        present[cid] = item
    write_tsv(out, old, ["concern_id", "decision_ids", "reason", "concern_sha256", "reviewer", "reviewed_utc"])
    print(json.dumps(dict(reviewer=args.reviewer, mapped_concerns=len(old))))


if __name__ == "__main__":
    main()
