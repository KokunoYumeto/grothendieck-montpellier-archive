"""Sweep 1, scope `sections`: the check events of this sweep (CHECK_EVENTS.tsv).
Written by Claude Opus 5.5 at effort max (sweep 1, scope sections), 18 Nov 2026. usage: python -I -B tools/checks.py"""
import csv, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent.parent
WHO = "Claude Opus 5.5 at effort max, sweep 1, scope sections"
D = "2026-11-18"
EV = [
 ("FERMAT_SUCCESSOR:A.9", "computation", "confirmed: y^2-xy-4y=x^3-4x^2 has discriminant -1664 and (0,0) has exact order 7 (exact rational arithmetic, tools/y1_7_check.py); so Y1(7)(Q) is nonempty"),
 ("LM6_POINTS_AS_SECTIONS:E.10", "computation", "confirmed, as FERMAT_SUCCESSOR A.9; refutes the claim Y1(7)(Q)=empty of Steklov's preprint (as the row says)"),
 ("FERMAT_SUCCESSOR:A.3", "computation", "confirmed the constant: the Tate parameter of the Legendre curve at lambda=0 is q=(lambda^2/256)(1+lambda+O(lambda^2)) (inverting j at lambda=1e-3..1e-9, 60 digits, tools/tate_constant_check.py); hence the cusp class -8kappa(2)+2l kappa(u) for lambda=u^l"),
 ("FERMAT_SUCCESSOR:A.4", "targeted proof check", "confirmed the mechanism: v_2(q)=2l v_2(u)-8 is prime to l for every odd l, so the cusp class is not divisible by l at 2; the l=5 tame matrices were not recomputed"),
 ("LM6_POINTS_AS_SECTIONS:E.8", "refuted, with the refined statement", "the cusp-divisibility step of its proof is false (FERMAT_SUCCESSOR A.4, checked above); the statement survives with the repaired proof FERMAT_SUCCESSOR A.3-A.6 (refined statement: FERMAT_SUCCESSOR A.6, Serre level 2)"),
 ("LM6_POINTS_AS_SECTIONS:E.12", "targeted proof check", "second sentence confirmed: for even n the plus curve X^n+Y^n+Z^n=0 has no real point, so no real section (Pal 2011 Thm 2.4, as cited by SECTION_GHOSTS E.157) and none over Q; sentences 3-4 rest on Tool (1) by the row's own words; first sentence re-proved in FERMAT_SUCCESSOR A.11 (not read)"),
 ("LM7_FERMAT_TOWER:E.19", "targeted proof check", "statement-level consistency with E.17: E.17 is about the rank-two toric quotient, E.19 about the pro-3 abelianization; no contradiction"),
 ("FLAGGED_149:D7", "targeted proof check", "statement level: a composite row; its DVR assertion is true (re-proved and extended by ANABELIAN_A1_SUCCESSOR B.102), its arbitrary-valuation converse is false; 'Refuted' covers only the extension"),
 ("FLAGGED_149:ZCF2", "targeted proof check", "proof text read at the citations of ZCF6 (CF_Z_agent.tex 105-109, 715-722, 935-940): ZCF6 is cited as what remains open, not used as a premise"),
 ("FLAGGED_149:ZCF11", "targeted proof check", "as ZCF2: ZCF6 not a premise"),
 ("FLAGGED_149:ZCF12", "targeted proof check", "as ZCF2: ZCF6 not a premise"),
 ("LM7_PUSH:A.17", "targeted proof check", "statement-level consistency with A.5 and A.18: A.5's mixed tame inertia example is class two only and has no metabelian lift (A.18); no contradiction"),
 ("SECTION_GHOSTS:C.4", "targeted proof check", "statement read: its 'A.7' is GT_TOWER_CHECK A.7, so the register edge to SECTION_GHOSTS A.7 (Open) is false"),
 ("SECTION_GHOSTS:E.2", "targeted proof check", "statement read: E.1 is named only to place the pending GT_TOWER_CHECK A.4.57 outside E.2's list; no open premise"),
 ("ANABELIAN_A1_SUCCESSOR:B.102", "targeted proof check", "statement level: consistent with FLAGGED_149 D7 (proves its DVR part; the converse fails without the value-group condition, B.99)"),
 ("SECTION_GHOSTS:E.191", "targeted proof check", "statement level only: proves Delta|GT^=0 for GT_TOWER_CHECK A.7's character; whether this is the CM parity of LM7_PUSH E.3/E.65 and FERMAT_SUCCESSOR C.15 is not checked"),
]
TOOL1 = ["LM6_POINTS_AS_SECTIONS:" + x for x in ("B.7", "B.15", "B.19", "B.29", "B.30", "B.32", "B.33", "B.35", "B.38", "B.39", "B.40", "B.41", "F.31")] + ["FERMAT_SUCCESSOR:A.20", "FERMAT_SUCCESSOR:A.31"]
for t in TOOL1:
    EV.append((t, "targeted proof check", "hypotheses only (the row's own printed qualification or notes): proved using the stipulated, unrefereed p-adic local section theorem (Tool (1), OpenAI preprint of 6 Oct 2026); recorded as Proved in the register; proof not read"))
with open(HERE / "CHECK_EVENTS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["statement", "date", "who", "type", "outcome"])
    for t, ty, oc in EV:
        w.writerow([t, D, WHO, ty, oc])
print(len(EV), "events")
