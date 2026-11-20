"""Where the three Claude models agree with each other but not with DM01 (20 Nov 2026, main session, Claude Opus 5.5 at
effort max). Reads pilots_api_20261120/<set>/scores.tsv and items.tsv; P1 (readings offered) only.
python -I -B pilot12_agree.py full_v2 -> <set>/AGREE.tsv"""
import collections
import csv
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
SET = sys.argv[1] if len(sys.argv) > 1 else "full_v2"
D = pathlib.Path(__file__).resolve().parent.parent / "pilots_api_20261120" / SET
sc = [r for r in csv.DictReader(open(D / "scores.tsv", encoding="utf-8"), delimiter="\t") if r["design"] == "p1"]
items = {r["id"]: r for r in csv.DictReader(open(D / "items.tsv", encoding="utf-8"), delimiter="\t")}
by = collections.defaultdict(dict)
for r in sc:
    by[r["id"]][r["model"]] = r
rows = []
tab = collections.Counter()
for i, ms in by.items():
    it = items[i]
    ans = {m: ms[m]["answer"] for m in ms}
    vals = list(ans.values())
    same = len(set(vals)) == 1
    maj = collections.Counter(vals).most_common(1)[0]
    ref = it["dm01_decision"]
    ref_ans = it["alts"].split(" || ")[0] if ref == "first" else it["dm01_reading"] if ref == "alternative" else "neither" if ref == "other" else "undecided"
    agree_ref = {m: ms[m]["verdict"] == "right" for m in ms}
    cat = ("all three agree, same as DM01" if same and all(agree_ref.values()) else
           "all three agree, not DM01" if same else
           "two agree, same as DM01" if maj[1] == 2 and any(agree_ref[m] for m in ms if ans[m] == maj[0]) else
           "two agree, not DM01" if maj[1] == 2 else "all differ")
    tab[(cat, it["in_class"])] += 1
    rows.append(dict(id=i, scan=it["scan"], cls=it["in_class"], kind=it["kind"], deleted=it["in_deleted"], dm01=ref, dm01_reading=it["dm01_reading"],
                     alts=it["alts"], haiku=ans.get("haiku", ""), sonnet=ans.get("sonnet", ""), opus=ans.get("opus", ""), category=cat,
                     zoom_word=it["zoom_word"], left=it["left"][-60:], right=it["right"][:60]))
with open(D / "AGREE.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, list(rows[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows(rows)
for (cat, cl), n in sorted(tab.items()):
    print(f"{cat:35s} {'Hua class' if cl == '1' else 'others':9s} {n}")
print()
for r in rows:
    if r["category"] == "all three agree, not DM01":
        print(f"{r['id']} scan {r['scan']:>3} cls={r['cls']} {r['kind']:6s} DM01={r['dm01']:11s} '{r['dm01_reading'][:18]}' models='{r['opus'][:18]}' alts=[{r['alts'][:40]}]")
