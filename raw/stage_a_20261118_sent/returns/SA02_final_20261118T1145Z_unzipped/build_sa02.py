#!/usr/bin/env python3
"""Validation/packaging helper for SA02; source archives are supplied separately."""
import csv, json, os, zipfile
ROOT=os.path.dirname(__file__)
def read_tsv(p):
    with open(os.path.join(ROOT,p),encoding="utf-8") as f:
        return list(csv.DictReader(f,delimiter="\t"))
entries=read_tsv("SA02_entries.tsv")
with open(os.path.join(ROOT,"SA02_items.json"),encoding="utf-8") as f: items=json.load(f)
with open(os.path.join(ROOT,"SA02_claims.json"),encoding="utf-8") as f: claims=json.load(f)
with open(os.path.join(ROOT,"SA02_problems.json"),encoding="utf-8") as f: problems=json.load(f)
assert len(entries)==389, len(entries)
assert len(items)==389, len(items)
assert len({r["entry_id"] for r in entries})==389
assert len({x["id"] for x in items})==389
assert all(r["item_id"] for r in entries)
print(f"validated entries={len(entries)} items={len(items)} claims={len(claims)} problems={len(problems)}")
