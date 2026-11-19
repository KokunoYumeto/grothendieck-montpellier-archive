import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
pat = re.compile(r"(\Delta|Δ|Delta)(?![A-Za-z])")
gt = re.compile(r"GT|Grothendieck.Teichm|E\.3\b|E\.65|E\.49|pentagon|CM parity|parity", re.I)
rows = [r for r in core.ROWS if pat.search(r["statement"] + " " + r["notes"]) and gt.search(r["statement"] + " " + r["notes"])]
print(len(rows), collections.Counter(r["run"] for r in rows).most_common())
with open(core.OUT / "sub_delta_INPUT_rows.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["tag", "status", "statement", "depends_on", "ret"])
    for r in rows:
        w.writerow([r["tag"], r["status"], r["statement"][:400], r["depends_on"][:200], r["ret"]])
