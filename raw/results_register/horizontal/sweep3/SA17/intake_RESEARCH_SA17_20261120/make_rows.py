"""Row list and check events of the intake of RESEARCH_SA17 cp12 (Claude Opus 5.5 at effort max, agent
ac8bd2a26d00b4f37, 20 Nov 2026). Reads the sorted register; writes the row table (markdown) and the check-event TSV.
It neither imports nor runs anything from the return.
usage: python -I -B make_rows.py <SORTED/RESEARCH_SA17.tsv> <rows.md out> <CHECK_EVENTS.tsv out>"""
import csv
import sys

WHO = "Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37, intake of RESEARCH_SA17 cp12)"
DATE = "2026-11-20"
T, R, C = "targeted proof check", "independent re-proof", "carried as background without fault found"
CP02 = "checked in the intake of 19 Nov (cp02); statement and proof unchanged in cp12 (section files diffed)"

V = {
    "A:main-counterexample": (T, "confirmed: P = alpha_p(R^h_(t)) over F_p[t] satisfies 1-8 with actual 7 (vacuous: no actual finite modular pair over F_p[[t]], by the epsilon*f Artin-Schreier test) and is not representable; the etale equalizer step cites de Jong-Olander Thm 2 (not opened)"),
    "A:hensel-remaining-gate": (T, "confirmed: conditions 4-8 for P, the non-existence of actual modular finite pairs, non-representability by henselian ZMT; fppf refinement Stacks 37.48.2 not opened"),
    "A:hensel-fpqc": (T, "confirmed: strict-local separability tensor e=(u^-1 x 1)(1+tc), b in A by A:fpqc-local-integral, propagation through D=(B x B_q)^h faithfully flat, then etale gluing"),
    "A:fpqc-finite-module": (T, "confirmed"),
    "A:fpqc-indecomposable-basechange": (T, "confirmed (Hensel idempotent lifting, Br of a separably closed field is 0, D_i x_k K local)"),
    "A:fpqc-local-integral": (T, "confirmed; hand test: purely inseparable b over a separably closed field admits no such tensor"),
    "A:fpqc-hensel-kernel": (T, "confirmed"),
    "A:pro7-representability": (T, "confirmed in structure (induction on dimension, formal models by 5 and 4, 7_pro gives etale open immersions, necessity); the gluing step rests on A:formal-gluing and the base case on A:comparison, not read"),
    "A:local-models-suffice": (T, "confirmed (noetherian induction with 8 over R/I^N and the uniform Artin-Rees lemma; charts by the etale corollary; Stacks 02WW, 03KV, 0417 cited, not opened)"),
    "A:uniform-AR": (R, "confirmed: Artin-Rees K cap I^N R^d in IK, then Nakayama twice; direct-summand case by adding the complement"),
    "A:etale-finitefibres-qc": (T, "confirmed in its logic (degree bound from the generic points); Stacks 086R and 07RY not opened"),
    "A:L1-general": (T, "confirmed: M(T,eta) lies in the open part U of the Artinian formally etale locus; U -> F is an etale chart onto an open subscheme; no local models assumed"),
    "A:actual-pro-generization": (T, "confirmed"),
    "A:fpqc-open-formal-descent": (T, "confirmed"),
    "A:generic-thickening-reflection": (T, "confirmed"),
    "A:L2-counterexample": (T, "confirmed: H(R)={x: x^p=0, x in tRx} over F_p[[t]] satisfies 1-3, 5, 6, 8 and strengthened 4 (Krull on R/(tx)); fails 7 (zero section modular at the closed point, not at the generic point: test K[eps])"),
    "A:artinian-base": (T, "confirmed except the step through A:comparison, not read"),
    "A:Murre-F8": (T, "confirmed; N.I=0 not used"),
    "A:unramified-corollary": (T, "confirmed: hypotheses matched with Murre 294 Thm 1 (F1)-(F8)"),
    "A:8-literal": (T, "confirmed (reread; unchanged since cp02)"),
    "A4:derivation-orbits": (T, "confirmed (stabiliser GL_r(S); orbit closed by Kostant-Rosenlicht; torsor under Res GL_r trivial; converse by density or counting)"),
    "A4:finite-rank-equivalence": (T, "confirmed"),
    "A4:infinite-orbits": (T, "confirmed (joint nilpotence of the R_i by the cycle construction; nil-semigroup step proved; flat modules over Artinian local rings free)"),
    "A4:finite-descent-theorem": (T, "confirmed: (a) every free rank over A'_n, (b) Krull and Mittag-Leffler over the completion, (c) flat base change over Artinian A; the three quantifiers kept apart"),
    "B:finite-PD": (R, "confirmed by hand: basis 1,x,y,x^2,xy,y^2,u,v,uv; the generating-function divided powers satisfy additivity, scalar, product and composition identities for every p; tau maps to uv, nonzero; the run's program not run"),
    "B:crystal-counterexamples": (T, "refutation confirmed: cp02's checks (p tau = 0, d tau = 0, phi(tau) = 0, Hom = 0, bases outside the positive classes) plus tau != 0 through B:finite-PD"),
    "A:NR-counterexample": (C, CP02), "A:NR-density": (C, CP02), "A:ind-thickening": (C, CP02),
    "A:artinian-tests": (C, CP02), "A:etale-corollary": (C, CP02), "A:completion-descent": (C, CP02),
    "A:nonfinite-descent": (C, CP02), "A4:flatclosure": (C, CP02), "A4:boundary": (C, CP02),
    "A4:all-primes": (C, CP02 + "; recomputed there for p = 2, 3, 5, 7"), "B:Kummer": (C, CP02),
    "C:local_charzero_counterexample": (C, CP02), "C:isoclinism_counterexample": (C, CP02),
    "C:formal_Frobenius_counterexample": (C, CP02),
    "D:rank": (C, "checked at statement level against my readings of cote 130 in the cp02 intake; D.tex changed only inside D:local"),
    "D:height": (C, "as D:rank"),
    "A:polarized-descent": (C, "SGA 1 VIII 7.7-7.8, not opened; standard"),
}
SHORT = {T: "targeted check, confirmed", R: "independent re-proof, confirmed", C: "carried (checked earlier or standard)"}

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
md = ["| Row | Run's status | This intake |", "|---|---|---|"]
for x in rows:
    rid = x["row_id"]
    st = " ".join(x["run_status"].split())[:60]
    if rid in V:
        md.append(f"| {rid} | {st} | {SHORT[V[rid][0]]} |")
    else:
        md.append(f"| {rid} | {st} | not read in full: statement level |")
open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(md) + "\n")
with open(sys.argv[3], "w", encoding="utf-8", newline="\n") as f:
    f.write("statement_id\tdate\twho\ttype\toutcome\n")
    for x in rows:
        if x["row_id"] in V:
            typ, out = V[x["row_id"]]
            f.write(f"{x['row_id']}\t{DATE}\t{WHO}\t{typ}\t{out}\n")
n = sum(1 for x in rows if x["row_id"] in V)
print("rows", len(rows), "with check events", n, "statement level", len(rows) - n)
missing = [k for k in V if k not in {x["row_id"] for x in rows}]
print("verdict keys not in the register:", missing)
