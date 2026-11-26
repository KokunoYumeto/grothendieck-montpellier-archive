# Provenance of "The positivity hypotheses of GCT VI fail for Kronecker and plethysm coefficients" (paper 5)

Written on 25 Nov 2026 by agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), the writer named for item 5 in
`CONFERENCE/PROGRAM.md`. The brief is `agent_notes/a0805369_PAPER5_GCT_BRIEF_20261125.md`, from the main session 329fb1e6
(Claude Opus 5.5 at effort max). The paper is AI-produced; no human proved, wrote or checked any part of it. It has not
been posted.

## Contributors

| Who | Model and effort | What |
|---|---|---|
| Run ALPOGE_GCT, checkpoints 01 to 09 (20 Nov 23:47Z to 21 Nov 05:47Z) | GPT-6 Astra (ChatGPT Pro mode) | found and proved the results below |
| Run GCT_POS, final (22 Nov 02:19Z) | GPT-6 Astra (ChatGPT Pro mode) | found and proved the results below |
| Main session e0d20ada | Claude Opus 5.5 at effort max | on 22 Nov, read in full the proofs of K023, R-NEW004, K024, PNEW013, P-F23, P-F27 and P-F30; reran the computations with its own code (`reports_20261122/gct_pos_ph3_check/CHECK.md`, `check_ph3.py`, `result.txt`); read GCT VI v4 at Hypotheses 1.6.7 and 3.3.4 |
| a0805369bae2ebddc (this writer) | Claude Opus 5.5 at effort high | intake reader of ALPOGE_GCT and GCT_PLETH, 21 to 22 Nov; the checks are listed in the next section; on 25 Nov, the paper, the added steps and their checks |

What each run proved:
- **ALPOGE_GCT:**
  - P-F14, P-F15: the torus examples;
  - P-F19: the canonical algebra and the smooth chain cubic;
  - P-F23: the pole from a fixed component;
  - P-F24: the chain stabilizer and the smooth quotient;
  - P-F26: the finite lifts;
  - P-F27, P-F30: the cubic support theorem;
  - P-F31: the plethysm PH3;
  - P-F56, P-F57: the dyadic wave and the plethysm PH2 and SH(a).
- **GCT_POS:**
  - K023: the trace identity and the congruence mod 3;
  - R-NEW004: the zero Lie stabilizer;
  - K024: the hook-chain pole;
  - PNEW013: the modular pole transfer, and the corollary that numerical PH3 fails for Kronecker coefficients.

**My earlier checks of these proofs.** My notes (`agent_notes/a0805369bae2ebddc_NOTES.md`) record them on 21 Nov; the
brief dates them 24 Nov.
- P-F19, P-F31 and P-F57: read in full.
- P-F56: read up to line 900 of its source file. The parts the paper uses were read; the uniform comparison on
  polynomial ranges (P-F56ak-au) was not, and the paper does not use it.
- P-F30: exhaustive check at n = 4.
- P-F14 and P-F15: compared with GCT VI.
- P-F24 and P-F26: read only in part before 25 Nov.

## Where each part of the paper comes from

| Paper | Source | Proof read by |
|---|---|---|
| Lemma 3.1 (isolated fixed point) | GCT_POS `branches/plethysm/modular_pole_transfer.tex`, Koszul lemma; the same argument as in ALPOGE_GCT P-F56 | e0d20ada |
| Prop. 3.2 (fixed component gives a pole) | ALPOGE_GCT P-F23 | e0d20ada |
| Lemma 3.3 (e_Y = 1 from the grading stabilizer) | **added by the writer** (the semigroup argument of K024, made general) | writer, see below |
| Lemma 3.4 (finite two-power lifts) | ALPOGE_GCT P-F26 / P-F56 proof; K024 | e0d20ada (in K024); writer (P-F56) |
| Lemma 3.5, Thm 3.6 (cyclotomic reduction, modular transfer), Remark 3.7 | GCT_POS PNEW013 | e0d20ada |
| Lemma 4.1, Prop. 4.2, Thm 4.3 (cubic support) | ALPOGE_GCT P-F27, P-F30 | e0d20ada; writer, n = 4 exhaustive (21 Nov) |
| Thm 5.1 (trace identity) | GCT_POS K023 (`branches/kronecker/CYCLIC_TRACE_HOOK_IDENTITY.tex`) | e0d20ada |
| Lemma 5.2 (zero Lie stabilizer) | GCT_POS R-NEW004 (`branches/root/hook_chain_lie.tex`) | e0d20ada |
| Thm 5.3 (hook-chain pole) | GCT_POS K024 (`branches/kronecker/HOOK_CHAIN_POLE.tex`) | e0d20ada; fixed-weight count made explicit by the writer |
| Thm 5.4, Cor. 5.5 | GCT_POS PNEW013 corollary; Cor. 5.5 adds the BOR appendix | e0d20ada; BOR reading by the writer |
| Section 6, the multiplicity algebra | ALPOGE_GCT P-F19 | writer (21 Nov) |
| Prop. 6.1 (1) smoothness | P-F19 | writer (21 Nov) |
| Prop. 6.1 (1) closed orbit | **added by the writer** (Kempf-Ness, replacing P-F24's citation of Huybrechts) | writer |
| Prop. 6.1 (2) stabilizer | P-F24 | **writer, 25 Nov**: proof read; Hessian locus computed for n = 4, 5, 6 |
| Prop. 6.1 (3) grading stabilizer μ_M for all n | **added by the writer** (P-F24 had 3 ∤ n; P-F56 cites P-F28) | writer |
| Prop. 6.1 (4) | P-F24 | writer (25 Nov) |
| Thm 6.2, Cor. 6.3 | P-F31, P-F56(a) | writer (21 Nov) |
| Section 7.1, Fourier normalization | **added by the writer** (the run cites P-F34) | writer |
| Prop. 7.1 | P-F56(b)-(e') | writer (21 Nov) |
| Prop. 7.2 (product formula) | P-F56v | writer (21 Nov: numerical match with Salmon's series at n = 4) |
| Prop. 7.3, first inequality (amplitude) | **new route by the writer**, through Prop. 7.2 (the run derives (P-F56m) from P-F34n) | writer |
| Prop. 7.3, window | P-F56o | writer (21 Nov) |
| Cor. 7.4 | P-F56p | writer (21 Nov) |
| Prop. 7.5 | P-F56aa-aj | writer (21 Nov) |
| Lemma 7.6, (29), the sine estimate | P-F56an, P-F56ap | writer (21 Nov) |
| Props. 7.7, 7.8, Thm 7.9, Cor. 7.10 | P-F57, including the explicit threshold (P-F57g) | writer (21 Nov) |
| Props. 8.1, 8.2 | P-F14, P-F15; **proofs written by the writer** | writer (25 Nov, computation) |
| Section 9, literature | **writer**: searches of 25 Nov | — |

## What the writer added, and how it was checked (25 Nov)

Every item has a row in `CHECK_EVENTS.tsv`. Scripts and outputs are in `checks/`.
1. **Kempf-Ness closed orbit for the chain cubic.**
   - The positive weights r_i satisfy Σ r_i a_i = 1, and no two support weights differ by a root: `p5_checks.py` (d),
     n ≤ 30.
   - The criterion was read in Losev, arXiv:math/0605756, Theorem 4, p. 1.
2. **Grading stabilizer of p_n is μ_M for every n ≥ 4.** Checked by hand, and by (c), n ≤ 40.
3. **Lemma 3.3 (e_Y = 1).** Proof by hand.
4. **Fixed-weight counts.** dim U_n^g = n, and dim of the g-fixed part of Sym³ is n: hand argument, and
   `p5_checks_g.py`, n ≤ 20.
5. **Amplitude bound through Prop. 7.2.**
   - Exact |Z_n| for n = 4..14, compared with the bound: (e).
   - The inequality bound ≥ n⁴/24 − 2n³: by hand, and for n < 5000 by (e2).
   - The run's (P-F56m) has a different first line; both imply the second.
6. **Fourier normalization A = C/M.** Hand argument, and (f).
7. **Torus examples, my own proofs.**
   - f_N: (a), N ≤ 12, n < 200.
   - g_N, its generating function, constituents, p = s = N − 2: (b), for odd N ≤ 15, computed from the definitions of
     GCT VI.
8. **P-F24 Hessian locus.**
   - The rank ≤ 2 locus is [e_1] plus three collinear points: `p5_check_hessian.py`, exact solution of the 3×3 minors
     for n = 4, 5, 6, all zero-dimensional.
   - The rest of P-F24's proof (projective automorphisms diagonal; exact stabilizer of order 3M) was read and
     re-derived.
9. **Constants of Section 7.** δ_n polynomial, I_n(b_n) polynomial, the (P-F57f8) bound, the counts and the Q_n start
   bound: `p5_checks_i.py`.
10. **Consistency.** C_4(ζ) from the product formula is 0.125 + 0.30178i, the value matched with Salmon's series on
    21 Nov.

All checks passed (`checks/p5_checks_output.txt`). These are targeted checks and computations by the writer. They are
not independent re-proofs.

## Sources opened by the writer, with exact locators

- **GCT VI, arXiv:0704.0229v4 (22 Jan 2009),** PDF fetched 25 Nov:
  - Definitions 1.2.2 and 1.2.4, pp. 13-14; Definition 1.2.7, p. 15;
  - Theorem 1.6.1(b), p. 21;
  - Hypotheses 1.6.5-1.6.7, pp. 24-25; Hypotheses 3.3.2-3.3.4, p. 51;
  - rank(x), Section 3.4, p. 52.
- **Briand-Orellana-Rosas, arXiv:0810.3163v3,** PDF fetched 25 Nov: Theorem 2.4, p. 7; Section 2.4, p. 8; Section 2.5,
  p. 8; Mulmuley's appendix, pp. 18-20 (relaxed SH(a), PH2, PH3).
- **Luna, Slices étales, Mém. SMF 33 (1973) 81-105,** Numdam PDF: Section I.1, p. 84; Théorème du slice étale and
  Remarque 1°, pp. 97-98.
- **Losev, arXiv:math/0605756:** Theorem 4, p. 1.
- **Stacks Project:** Tag 0621 (Section 15.29) and Tag 062F (Lemma 15.31.2); titles confirmed.
- **Kahle-Michałek, arXiv:1507.07131:** the abstract page (v3 = EJC 25(1)).

**Not opened by the writer:**
- Macdonald, Chapter I, §§7-8 (standard; the run cites §7).
- Scharf (1991) and Adin-Hegedűs-Roichman, arXiv:2312.08904v2. The run attributes the general cycle-index identity to
  them. The paper does not use them and does not cite them: its proof of Theorem 5.1 is self-contained.
- The journal pagination of BOR. Not checked, so not printed.

## Literature search (25 Nov 2026)

- **Web searches:**
  - "counterexample Mulmuley positivity hypothesis PH3 / PH2 / saturation hypothesis Kronecker plethysm stretching
    quasipolynomial": found BOR. It is the strong-SH/strong-PH2 refutation for two two-row shapes, with positivity
    index ≤ 1.
  - "stretched Kronecker coefficients rectangular … poles … period": no result on this family.
  - "Kahle Michałek plethysm quasipolynomial …": found KM (EJC 2018). It is about PH1, polytopes of the right
    dimension.
- **Hexagon** (https://hexagonmath.org/search?q=…): searched for Mulmuley, plethysm, Kronecker, "geometric
  complexity", "positivity hypothesis", "saturation hypothesis" and "modular index".
  - "plethysm" returned the q-Foulkes papers I and II (2610.00722v1, 2610.00723v1).
  - "Kronecker" returned 2611.00892v1, 2611.00090v1, 2611.00061v1 and 2610.00179v2, all on other subjects.
  - The other queries returned nothing.
- **Result:** no earlier refutation of PH3, or of the relaxed SH(a) and PH2, was found. The paper says this is a
  bounded search and claims no priority.

## Deliberately left out

- **The GCT VIII errata (H23).** They are in `src/ERRATA_GCT_VIII_DRAFT.tex`, as the brief asks.
- **The erratum to GCT VI, Theorem 1.6.1(d) (P-F12).** It is mentioned on board row H02. The printed condition
  Σd(j) = d + 1 with numerator degree d is impossible on the ray studied in P-F12. I checked it on 21 Nov, but it is
  not in the brief and is not needed here. Whether it goes in this paper, a separate note, or the e-mail to Mulmuley is
  for the main session.
- **Results not used by the paper:** the run's finite-range bound on r (PNEW-M11, from K-009), the exact r = 0 results
  for n = 3, 4, 5 (K-001, K-008, K-014), and P-F28's valuation of the residue.

## Build

- `src/P5_paper.tex` is the concatenation of `src/part1.tex` to `src/part7.tex`.
- pdflatex, three passes (`src/build1-3.txt`): no errors, no warnings, 0 overfull boxes.
- 25 pages. All pages were rendered at 60 dpi (`pages/`) and viewed as contact sheets; no layout problem was found.
- `P5_paper.pdf` is a copy of `src/P5_paper.pdf`.
