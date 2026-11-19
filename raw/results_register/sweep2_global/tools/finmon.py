"""Sweep 2: place FINMON (695 rows, absent from the register) in the outline of sweep 1 and link it to the
finite-models cluster. Claude Opus 5.5 at effort max, 18 Nov 2026. Writes FINMON_PLACEMENT.tsv, FINMON_MERGES.tsv."""
import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core

OUT = core.OUT
rows = [r for r in core.ROWS if r["run"] == "FINMON"]
P4 = "II. Homotopy"
C4 = "II.4 Finite models of homotopy types"
S1 = "II.4.1 Finite posets, categories and monoids of given type; size minima"
S2 = "II.4.2 The finite-category tests: faithfulness, fullness, conservativity, finite representatives"
S3 = "II.4.3 Maps into S^2 from finite categories: countability"
C1 = "II.1 Small categories: filtered, exact, total, quasi-filtered; truncated totality"
S13 = "II.1.3 Shapes whose Cat-, groupoid- and group-valued colimits are homotopy colimits"
C2 = "II.2 Test categories and fundamental localizers"
S211 = "II.2.11 Path categories and categorical loop spaces (VII)"


def place(r):
    i, s = r["id"], r["statement"]
    low = s.lower()
    part = re.split(r"[.:(\-]", i)[0]
    note = ""
    if r["status"] in ("Explanatory",) or re.match(r"(rem|A\d|B\d|C\d|D\d|E\d|F)\b", i) and re.search(r"\b(checked|audit|reproduced|both .* proofs)\b", low):
        note = "working or explanatory row" if r["status"] == "Explanatory" else "task row (a check of a supplied result)"
    if i.startswith("F:C26") or "INDLOCAL C.26" in s or "C.26" in i:
        return (C2, S211, "read", "audit of INDLOCAL C.26 (finite five-arrow pointed category, IX tests)")
    if i.startswith("F:C27") or "C.27" in i:
        return (C1, S13, "read", "audit of INDLOCAL C.27 and PRETOT F.1/F.4 (Cat-valued colimits)")
    if part in ("E4",) or "s2" in low and ("continuum" in low or "uncountable" in low or "[bm,s" in low) or i == "cor:E-uncountable":
        return (C4, S3, "read", "maps into S^2: continuum many (= S2COUNT A.M1, CATHOT D.6)")
    if part == "F" or i.startswith("F-"):
        return (C4, S2, "script (part F: his finite-test claims)", note)
    return (C4, S1, "script (parts A-E: types realized by finite monoids and categories; size minima)", note)


pl = []
for r in rows:
    ch, sec, how, note = place(r)
    pl.append(dict(tag=r["tag"], part=P4, chapter=ch, section=sec, how_placed=how, note=note, status=r["status"]))
with open(OUT / "FINMON_PLACEMENT.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(pl[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(pl)
M = [
    ("FINMON:C3", "CATHOT:G.17", "refines", "FINMON C3 proves the exact minimum 49 arrows for a poset of type RP^2 (with a stronger statement for all H1-torsion posets); CATHOT G.17 left a_pos(RP^2) in [28, 49] open. The interval closes at its upper end."),
    ("FINMON:C3", "CATHOT:G.16", "refines", "the RP^2 poset entry of CATHOT G.16's size table becomes the exact value 49."),
    ("FINMON:E1-KZ2-category", "CATHOT:G.17", "refines", "CATHOT G.17 asks whether K(Z,2) has a finite categorical or finite monoid model: FINMON E1 answers no for both (rational cup nilpotence); the FINMON rows are marked Refuted because they refute the existence claim."),
    ("FINMON:E1-KZ2-monoid", "CATHOT:G.17", "refines", "as above, for finite monoids."),
    ("S2COUNT:A.M1", "FINMON:E4", "same", "the six-element (Sweeney) monoid with BM ~ wedge of S^n (n >= 2) and continuum many classes [BM, S^2]: S2COUNT A.M1 and FINMON E (E4, cor:E-uncountable) prove it independently; FINMON also step-audits OWN_RESULTS Proposition 4.1 (the CATHOT expert, Claude Fable 5.2 at effort max). It answers CATHOT D.6 no."),
    ("S2COUNT:A.M1", "FINMON:cor:E-uncountable", "same", "as above."),
    ("FINMON:E5", "RESIDUE:A.5", "stronger", "FINMON E5 assigns exact types to all 1565 iso/op classes of monoids through order 6; RESIDUE A.5 (orders <= 5, 273 iso classes: 1, 2, 7, 35, 228) finds the rectangular band (the five-element sphere monoid) as the only non-1-type. Consistent: 1565 = 1+2+6+27+156+1373 (monoids up to isomorphism or anti-isomorphism, OEIS A058133) and 1, 2, 7, 35, 228 are OEIS A058129; FINMON's report uses the same five-element sphere band."),
    ("FINMON:C1", "CATHOT:G.11", "same", "FINMON C1 reproduces the unique three-object nine-arrow RP^2 category (prompt R6 = CATHOT G.11-G.13) and the four seven-arrow S^3 categories (prompt R7, the CATHOT expert's enumeration)."),
    ("FINMON:B4-CP2", "FINMON:B:CP2-minimum23", "same", "the headline: the least finite monoid with BM ~ CP^2 has 23 elements (two explicit models; every order <= 22 excluded)."),
    ("FINMON:C2-CP2", "FINMON:C2-CP2", "same", "open: the least number of arrows of a finite category of type CP^2 lies in [17, 22] at checkpoint 20 (programme map: same)."),
    ("FINMON:D1", "CATHOT:G.17", "refines", "FINMON D1: an explicit finite Q8 category whose classifying space has a CW model of dimension <= 8 and nonzero Wall class, so no finite CW model: a finite category need not have finite type. Bears on G.17's classification question."),
]
with open(OUT / "FINMON_MERGES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["canonical tag", "member tag", "relation", "reason"])
    for m in M:
        w.writerow(m)
print(len(pl), collections.Counter(p["section"] for p in pl).most_common())
