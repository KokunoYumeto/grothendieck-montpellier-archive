"""Pilot 1, step 0 (no API): DM01's own decisions on the marks where Hua has C's other alternative (20 Nov 2026, main
session, Claude Opus 5.5 at effort max). DM01 (GPT-6 Astra, ChatGPT Pro mode) decided each mark of cote 1 on the scan,
so its decisions on this class say who was right there, C or Hua, before any cheap model is tried.

Joins data/marks.tsv (dm_followup.py: run DM01, one row per mark of C, with what Hua has there) with DM01's decisions.tsv
page by page, in mark order, only where the two have the same number of marks on the page (as build_report.py does).
python -I -B pilot1_dm01_class.py -> ../data/pilot1_dm01_class.tsv"""
import collections
import csv
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data"
SPR = pathlib.Path("<project root>/grothendieck_archive_transcription_20261110/second_pass_returns")
dmd = max(SPR.glob("DM01_*_unzipped"), key=lambda p: re.search(r"(\d{8}T\d{4})Z_unzipped$", p.name).group(1))
dec = list(csv.DictReader(open(dmd / "decisions.tsv", encoding="utf-8"), delimiter="\t"))
marks = [m for m in csv.DictReader(open(DATA / "marks.tsv", encoding="utf-8"), delimiter="\t") if m["run"] == "DM01"]
dd, mm = collections.defaultdict(list), collections.defaultdict(list)
for d in dec:
    dd[int(d["scan"])].append(d)
for m in marks:
    mm[int(m["scan"])].append(m)
pairs = [(d, m) for s in sorted(dd) if len(dd[s]) == len(mm.get(s, [])) for d, m in zip(dd[s], mm[s])]
left_out = sorted(s for s in dd if len(dd[s]) != len(mm.get(s, [])))
print(dmd.name, "| decisions", len(dec), "| joined", len(pairs), "| pages left out (mark counts differ):", left_out)
rows = []
by = collections.defaultdict(collections.Counter)
for d, m in pairs:
    by[m["hua"]][d["decision"]] += 1
    by[m["hua"]]["struck" if m["in_deleted"] == "1" else "live"] += 1
    if m["hua"] == "Hua = C's other alternative":
        rows.append(dict(id=d["id"], scan=d["scan"], kind=m["kind"], in_deleted=m["in_deleted"], in_math=m["in_math"],
                         dm01_decision=d["decision"], dm01_reading=d["reading"], dm01_confidence=d["confidence"], crop=d["crop"],
                         hua_reading=m.get("hua_reading", ""), mark=m.get("mark", m.get("c_mark", ""))))
for h, c in sorted(by.items(), key=lambda kv: -sum(kv[1][k] for k in ("first", "alternative", "other", "undecided"))):
    n = sum(c[k] for k in ("first", "alternative", "other", "undecided"))
    print(f"{h:45s} n={n:4d} first={c['first']:4d} alternative={c['alternative']:4d} other={c['other']:3d} undecided={c['undecided']:4d}"
          f" | live {c['live']}, struck {c['struck']}")
with open(DATA / "pilot1_dm01_class.tsv", "w", encoding="utf-8", newline="") as fh:
    if rows:
        w = csv.DictWriter(fh, list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
print("class rows written:", len(rows))
