"""Sweep 2: the links that cross the four sweep-1 scopes (which no sweep-1 agent saw whole), and the input files for
the sub-agents. Claude Opus 5.5 at effort max, 18 Nov 2026."""
import sys, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import BYTAG

OUT = core.OUT
SCOPE = {}
for r in ["LM4_SUCCESSOR", "LM8_PUSH", "EXIT_TOWER", "LM4_FINITE_GROUP_ACTIONS", "DELTA_ON_GT", "GT_TOWER_CHECK",
          "LM8_LIE_APPROXIMATIONS", "LM5_MULTI_GALOIS_TOPOI", "LM1_GROUP_SCHEMES_rerun_20261112", "LM2_LOOP_EQUATIONS",
          "EXIT_ONE_TYPE", "CYCLOTOMIC_KERNEL"]:
    SCOPE[r] = "tower"
for r in ["FLAGGED_149", "ANABELIAN_149_PUSH", "ANABELIAN_SUCCESSOR", "ANABELIAN_A1", "ANABELIAN_A1_SUCCESSOR",
          "LM6_POINTS_AS_SECTIONS", "LM7_FERMAT_TOWER", "LM7_PUSH", "FERMAT_SUCCESSOR", "SECTIONS_OVER_Q", "SECTION_GHOSTS"]:
    SCOPE[r] = "sections"
for r in core.RUNS:
    if r.startswith("S6_") or r == "Q03_DEPOSIT":
        SCOPE[r] = "s6"
    elif r == "FINMON":
        SCOPE[r] = "none (FINMON is not in the register)"
    elif r not in SCOPE:
        SCOPE[r] = "derivateurs"


def run_of(t):
    return t.split(":", 1)[0]


cx = list(csv.DictReader(open(OUT / "tools" / "crossrun_edges.tsv", encoding="utf-8"), delimiter="\t"))
X = [dict(x, from_scope=SCOPE[run_of(x["from"])], to_scope=SCOPE[run_of(x["to"])]) for x in cx]
cross = [x for x in X if x["from_scope"] != x["to_scope"]]
print("cross-run edges", len(X), "crossing sweep-1 scopes", len(cross))
print(collections.Counter((x["from_scope"], x["to_scope"], x["kind"]) for x in cross).most_common(40))
cols = ["from", "from_status", "from_scope", "to", "to_status", "to_scope", "kind", "field", "how", "evidence"]
with open(OUT / "tools" / "crossscope_edges.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(sorted(cross, key=lambda x: (x["from_scope"], x["to_scope"], x["from"])))
# per sub-agent inputs
TS = {"tower", "sections"}
two = [x for x in cross if {x["from_scope"], x["to_scope"]} == TS and x["kind"] != "answers prompt item"]
dl = [x for x in cross if ("derivateurs" in (x["from_scope"], x["to_scope"]) or "FINMON" in x["from"] + x["to"])
      and x["kind"] != "answers prompt item"]
for name, rows in (("sub_sections/INPUT_crossscope_tower_sections.tsv", two),
                   ("sub_homotopy/INPUT_crossline_and_finmon.tsv", dl)):
    with open(OUT / name, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(rows, key=lambda x: (x["from"], x["to"])))
    print(name, len(rows))
fin = [x for x in X if "FINMON" in x["from"] + x["to"]]
print("FINMON cross-run edges:", len(fin), collections.Counter(run_of(x["to"]) if x["from"].startswith("FINMON") else run_of(x["from"]) for x in fin).most_common())
