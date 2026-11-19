"""Sweep 2: split the script findings into the three families the sub-agents take, and write their input files.
Claude Opus 5.5 at effort max, 18 Nov 2026."""
import sys, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core

OUT = core.OUT
FAM = {
    "tower": ["LM1_GROUP_SCHEMES_rerun_20261112", "LM2_LOOP_EQUATIONS", "LM4_FINITE_GROUP_ACTIONS", "LM4_SUCCESSOR",
              "LM7_PUSH", "LM8_LIE_APPROXIMATIONS", "LM8_PUSH", "DELTA_ON_GT", "GT_TOWER_CHECK", "EXIT_ONE_TYPE",
              "EXIT_TOWER", "LM7_FERMAT_TOWER"],
    "sections": ["FLAGGED_149", "ANABELIAN_149_PUSH", "ANABELIAN_SUCCESSOR", "ANABELIAN_A1", "ANABELIAN_A1_SUCCESSOR",
                 "CYCLOTOMIC_KERNEL", "LM5_MULTI_GALOIS_TOPOI", "LM6_POINTS_AS_SECTIONS", "LM7_FERMAT_TOWER", "LM7_PUSH",
                 "FERMAT_SUCCESSOR", "SECTIONS_OVER_Q", "SECTION_GHOSTS", "GT_TOWER_CHECK"],
    "homotopy": ["TOTAL_ASPHERICITY", "TOTEX", "TOTEX2", "PRETOT", "FREX", "DER_FOLLOWUP", "POLES", "REVLOC",
                 "DER_LOCALIZERS", "GALOIS", "PATHS", "BISITE", "STRATA", "RESIDUE", "CATHOT", "FINMON", "INDLOCAL",
                 "S2COUNT"],
}


def run_of(t):
    return t.split(":", 1)[0]


def load(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


cx = load(OUT / "tools" / "crossrun_edges.tsv")
sc = load(OUT / "tools" / "status_conflicts.tsv")
po = load(OUT / "tools" / "analysis_proved_on_unproved.tsv")
cy = load(OUT / "tools" / "cycles_detail.tsv")
cp = load(OUT / "tools" / "cluster_pairs.tsv")
for fam, runs in FAM.items():
    d = OUT / f"sub_{fam}"
    d.mkdir(exist_ok=True)
    rs = set(runs)

    def w(name, rows, cols=None):
        if not rows:
            open(d / name, "w", encoding="utf-8").write("(none)\n")
            return
        cols = cols or list(rows[0].keys())
        with open(d / name, "w", encoding="utf-8", newline="") as f:
            ww = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
            ww.writeheader()
            ww.writerows(rows)
    w("INPUT_crossrun_edges.tsv", [x for x in cx if run_of(x["from"]) in rs and run_of(x["to"]) in rs and x["kind"] != "answers prompt item"])
    w("INPUT_status_conflicts.tsv", [x for x in sc if run_of(x["from"]) in rs or run_of(x["to"]) in rs])
    w("INPUT_proved_on_open.tsv", [x for x in po if run_of(x["proved"]) in rs and x["uses_status"] != "Refuted"])
    w("INPUT_proved_on_refuted_crossrun.tsv", [x for x in po if run_of(x["proved"]) in rs and x["uses_status"] == "Refuted" and x["cross_run"] == "yes"])
    w("INPUT_cycles.tsv", [x for x in cy if set(x["runs"].split(",")) <= rs])
    w("INPUT_similar_pairs.tsv", [x for x in cp if run_of(x["a"]) in rs and run_of(x["b"]) in rs])
    print(fam, {p.name: sum(1 for _ in open(p, encoding="utf-8")) - 1 for p in sorted(d.glob("INPUT_*.tsv"))})
