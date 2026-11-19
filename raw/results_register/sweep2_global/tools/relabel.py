"""Sweep 2: apply the relations I verified by reading to GRAPH_EDGES.tsv (keyword-rule relations are otherwise marked
unverified). Claude Opus 5.5 at effort max, 18 Nov 2026. Run after resolve.py."""
import sys, csv, re
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core

P = core.OUT / "GRAPH_EDGES.tsv"
rows = list(csv.DictReader(open(P, encoding="utf-8"), delimiter="\t"))
cols = list(rows[0].keys())
R27 = "sweep 2 read: the refutation is of the prompt's paraphrase R27 (relative-only 'pinned'); LM5's row stands"
R8 = "sweep 2 read: E.100 refutes the unqualified reading of its prompt row R8; this row stands"
R18 = "sweep 2 read: C.14 corrects the prompt's paraphrase R18; this row stands (no commuting third-derived lift)"
V = {  # (from, to or to-prefix) -> (kind, note)
    ("ANABELIAN_149_PUSH:F.31", "LM5_MULTI_GALOIS_TOPOI:"): ("names", R27),
    ("ANABELIAN_149_PUSH:F.37", "LM5_MULTI_GALOIS_TOPOI:F.50"): ("strengthens", "sweep 2 read: F.37 extends LM5 F.50 (Q^ab) to Q^solv, with pinned closed-point-preserving"),
    ("SECTION_GHOSTS:E.100", "LM7_FERMAT_TOWER:E.25"): ("strengthens", "sweep 2 read: for even n no section of the geometrically pro-2 abelian extension (E.25: a D8 pullback with no real section)"),
    ("SECTION_GHOSTS:E.100", "LM6_POINTS_AS_SECTIONS:"): ("names", R8),
    ("SECTION_GHOSTS:E.100", "LM7_FERMAT_TOWER:E.32"): ("names", R8),
    ("SECTION_GHOSTS:E.100", "LM8_LIE_APPROXIMATIONS:F.21"): ("names", R8),
    ("FERMAT_SUCCESSOR:C.14", "LM6_POINTS_AS_SECTIONS:"): ("names", R18),
    ("FERMAT_SUCCESSOR:A.9", "LM6_POINTS_AS_SECTIONS:E.10"): ("restates", "sweep 2 read: both refute Y1(7)(Q) = ∅ with (0,0) of order 7 on y²−xy−4y = x³−4x² (Steklov Thm 5.14)"),
    ("LM7_PUSH:B.2", "LM7_FERMAT_TOWER:E.19"): ("names", "sweep 2 read: B.2 refutes the exclusion proposed in Lead 1; E.19 (the cusp sections are pairwise nonconjugate) stands"),
    ("PRETOT:E.5", "TOTAL_ASPHERICITY:G.3"): ("refines", "sweep 2 read: E.5 refutes the converse of G.3, not G.3"),
    ("PRETOT:E.5", "TOTAL_ASPHERICITY:G.5"): ("names", "sweep 2 read: both are counterexamples in the same direction"),
    ("ANABELIAN_149_PUSH:B.9", "FLAGGED_149:B5"): ("names", "sweep 2 read: B.9 refutes the literal lead L4 of its prompt; FLAGGED_149 B5 stands"),
    ("ANABELIAN_SUCCESSOR:F.7", "ANABELIAN_149_PUSH:F.45"): ("uses", "sweep 2 read: F.45 is an input of F.7's refutation"),
    ("ANABELIAN_A1:B.51", "ANABELIAN_SUCCESSOR:F.18"): ("refines", "sweep 2 read: a negative answer for one henselian field in F.18's open range (F.18 is Open)"),
    ("ANABELIAN_A1_SUCCESSOR:B.51", "ANABELIAN_SUCCESSOR:F.18"): ("refines", "sweep 2 read: as ANABELIAN_A1 B.51"),
    ("GT_TOWER_CHECK:A.3", "EXIT_TOWER:E.49"): ("corrects", "sweep 2 read: repairs two label comparisons of E.49's written proof; the statement stands"),
    ("INDLOCAL:C.27", "PRETOT:F.4"): ("corrects", "sweep 2 read: an independent corrected proof; the statement stands"),
    ("INDLOCAL:C.27", "PRETOT:F.1"): ("corrects", "sweep 2 read: an independent corrected proof; the statement stands"),
    ("ANABELIAN_A1:B.23", "ANABELIAN_SUCCESSOR:A.86"): ("checks", "sweep 2 read: confirms the counterexample A.86"),
    ("LM4_SUCCESSOR:A.28", "LM7_PUSH:E.58"): ("names", "sweep 2 read: 'not a counterexample to R2'"),
}
KEYWORD = {"refutes", "corrects", "strengthens", "refines", "checks", "restates"}
n_v = n_u = 0
for r in rows:
    hit = None
    for (a, b), v in V.items():
        if r["from"] == a and (r["to"] == b or (b.endswith(":") and r["to"].startswith(b))) and r["kind"] in KEYWORD | {"names"}:
            hit = v
            break
    if hit:
        r["kind"], r["how"] = hit[0], hit[1]
        n_v += 1
    elif r["kind"] in KEYWORD and "relation from the words" in r["how"] or (r["kind"] in KEYWORD and r["how"].startswith("prompt row")):
        r["how"] += " (keyword rule; unverified)"
        n_u += 1
with open(P, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("relabelled", n_v, "marked unverified", n_u)
