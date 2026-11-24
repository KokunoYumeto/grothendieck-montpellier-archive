# Alpöge's proof of RH and GRH for Dirichlet L-functions (20 November 2026): our working-through, status as of 22 Nov 2026 01:46 UTC, corrected 25 Nov 2026

On 20 Nov 2026 **L. Alpöge** proved RH, and GRH for Dirichlet L-functions: a note (https://alpo.ge/remark.pdf), with
a Lean formalization whose `Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements. GRH for the
Hecke L-functions of a general number field remains open.

That night we sent 21 research prompts (22-42) to GPT-6 Astra (ChatGPT Pro mode), asking how the new results bear on
the Grothendieck programme of this repository and on geometric complexity theory. We took the returns in as they
landed. Results that need only Alpöge's theorem are marked as such. Results that need GRH for Hecke L-functions are
stated as conditional on it, and it is open.

Earlier versions of this page also treated a draft announced the same day, claiming GRH for all Hecke L-functions, as
an input. Our check found its decisive step (§§12.3-12.4) equivalent to RH, so it is not a proof (MAS_ARTIN, finding
MA-HM-003), and found no correct result in it that is not already in the literature or a consequence of Alpöge's
theorem; it is no longer used. The dated intakes, reports and prompts below are kept as they were written.

Who did what:
- the runs: GPT-6 Astra (ChatGPT Pro mode);
- the intakes (checks): Claude Opus 5.5 at effort high;
- the Hodge sketch and the Δ answer: Claude Fable 5.2 at effort max;
- this page: Claude (Claude Opus 5.5 at effort max).

No human has checked any of it. Corrections are welcome as GitHub issues.

## The result to look at first
**[A sign-only proof of Deligne's purity theorem](deligne_sign_only/)** (prompt 32, HODGE_SIGN). It works out
Alpöge's footnote 3 into a complete proof of Weil I 1.6 and Weil II 3.3.1. The proof uses the trace formula, Katz's
generic weak Lefschetz, Parseval for a bilinear character sum and tensor powers, and no monodromy. It has had one AI
check, and the literature is not yet searched.

## What the intakes found so far

The intakes are in [`intakes/`](intakes/), each with its check events.

- **The positivity hypotheses of geometric complexity theory** (23 ALPOGE_GCT, 25 GCT_PLETH):
  - Theorem 1.6.1(d) of Mulmuley's GCT VI fails as printed. On the Kahle-Michałek plethysm ray the generating function
    is the Hilbert series of the D₅ Kleinian singularity, $(1+t^4)/((1-t^2)(1-t^3))$.
  - The Cohen-Macaulay form holds.
  - PH3 implies PH2 for the stretching families, with an explicit polynomial bound.
  - The homogeneous Ehrhart form of PH1 fails, and a minimal two-dimensional shifted polytope repairs it.
- **Border rank** (27 GCT_GINEQ): an exact reduction that needs no norms,
  $\min_{0\ne u\in U_{n,b}}\mathrm{BR}(u)=\mathrm{BR}(T_b)$, hence $\mathrm{BR}(T_n)\ge\binom nb^s+\mathrm{BR}(T_b)-1$.
  It gives border rank ≥ 39 for the 4×4 determinant and permanent. The literature check is pending.
- **Complexity** (28 CX_GRH): which form of GRH each conditional result needs. Some need Dirichlet characters only,
  and then Alpöge suffices. Koiran's Nullstellensatz in AM no longer needs GRH: it follows from the recent zero-free
  half-plane results (hexagon:2611.01018, with Baldwin-Sivek, arXiv:2611.06705, and Frei-Sofos-Widmer,
  arXiv:2610.18491). Hooley's Artin conjecture and effective Chebotarev in its GRH form still assume GRH for Hecke
  L-functions (open), and stay conditional.
- **Zeta functions of schemes and motives** (35 ZETA_TWO):
  - Assuming GRH for Hecke L-functions (open), RH holds for every CM motive. The non-CM motives are open even then.
  - Under Alpöge, an off-line zero of a non-CM elliptic L-function cannot be hidden inside $\zeta_E$.
  - Alpöge alone removes the Siegel-zero condition from Wei's bound for CM heights.
  - The naive "RH for every Λ-scheme" is false: $\mathrm{Spec}\,\mathbf Z[1/p]$ has zeros $2\pi ik/\log p$ on
    $\mathrm{Re}\,s=0$. The conjectured correct form makes every bad-fibre factor a product of
    $(1-\zeta p^{j-s})^{\pm1}$.
- **Grothendieck's texts** (32 HODGE_SIGN, 29 DELTA23):
  - Cote 44, Th. 5 (scan 004) fails as written. The counterexample is $\mathbf P^2\times\mathbf P^2$ with the
    flag-threefold pencil, and the correction comes from the nodal fibres.
  - The sign in Alpöge's step 5 is Grothendieck's evanescent part $E^{n-1}$ (cote 16, scans 034 and 036).
  - The Δ invariant on $\widehat{GT}$ reduces to one statement of our SECTION_GHOSTS run (E.190.4), by sextic
    reciprocity.
- **Alpöge's step 2** (34 DP_MULT): the bound of the divided-power step is sharpened, to slope
  $1/(p-1)-1/(p^h-1)$ with a constant loss of $h-1$.

Errors found in published papers are listed in [`ours/OUTSIDE_PAPERS_ERRATA.md`](ours/OUTSIDE_PAPERS_ERRATA.md). The
authors get a note from us before anything else is done with them.

## Our own texts
In [`ours/`](ours/):
- the bridges paper of 20 Nov (`BRIDGES_20261120.tex`), with its question list and ledger;
- our map of Alpöge's Lean archive;
- the Hodge sketch ("one theta machine, two signatures");
- the Δ sextic answer;
- the errata table.

## The split zero, counting with the basepoint, and GCT at rank three (21 Nov)
The project's split-zero programme read in standard terms, and what it gave together with the two GRH proofs and
Connes and Consani's F_{1²} (arXiv:2609.00299). In [split_zero/](split_zero/):
- [TRANSLATION_SPLIT_ZERO_20261121.md](split_zero/TRANSLATION_SPLIT_ZERO_20261121.md): the programme in the terms of
  algebraic geometry, GCT and analytic number theory;
- [SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md](split_zero/SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md): the
  split zero in Connes and Consani's terms. Counting with the basepoint makes ζ the unit of counting, and GCT's
  nonstandard Riemann hypothesis at rank three becomes Alpöge's theorem plus a categorification (sections 5-14);
- [consults/E4_RANK_FOUR_20261121.md](split_zero/consults/E4_RANK_FOUR_20261121.md): GCT VIII's canonical basis at rank
  three. Our consult finds that the unimodality clause of its positivity conjecture fails for six constants, and that
  every structure constant is a sign-twisted Tate count (found by our consult and checked by us; not yet re-run
  independently);
- [consults/CONSULT_a157422a_COUNTING_CONSTRUCTION.md](split_zero/consults/CONSULT_a157422a_COUNTING_CONSTRUCTION.md):
  the closed form over Z[D] and the dimension rings;
- [H22_note/](split_zero/H22_note/): a short note on the semiring with an adjoined zero (spectrum, modules, projectives);
- the other consults, the extraction of the corpus, and every script, with its output.

## The runs

| Prompt | Run | Newest return | Our intake |
|---:|---|---|---|
| 1 | RESEARCH_SA06: SA06 Motifs II cotes 14-15 night  SENT | [RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z](../../raw/research_returns/RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped/) | not yet |
| 2 | RESEARCH_SA05: SA05 Motifs I cotes 11-12 15 night  SENT | [RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z](../../raw/research_returns/RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z_unzipped/) | not yet |
| 3 | RESEARCH_SA15: SA15 Cristaux cotes 4-9 100 night  SENT | [RESEARCH_SA15_checkpoint_37_20261120T0635Z](../../raw/research_returns/RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped/) | not yet |
| 4 | RESEARCH_SA07: SA07 Motifs III periods cote 18 night  SENT | [RESEARCH_SA07_checkpoint_12_20261119T1255Z](../../raw/research_returns/RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped/) | not yet |
| 6 | RESEARCH_SA10: SA10 Stratified spaces cotes 150-151 night  SENT | [RESEARCH_SA10_final_20261119T0540Z](../../raw/research_returns/RESEARCH_SA10_final_20261119T0540Z_unzipped/) | not yet |
| 7 | RESEARCH_SA21: SA21 Formes cote 156 night  SENT | [RESEARCH_SA21_final_20261119T1242Z](../../raw/research_returns/RESEARCH_SA21_final_20261119T1242Z_unzipped/) | not yet |
| 8 | RESEARCH_SA08: SA08 de Rham cote 136 night  SENT | [RESEARCH_SA08_final_20261119T1027Z](../../raw/research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped/) | not yet |
| 9 | RESEARCH_SA09: SA09 de Rham cotes 137-138 night  SENT | [RESEARCH_SA09_final_20261119T1146Z](../../raw/research_returns/RESEARCH_SA09_final_20261119T1146Z_unzipped/) | not yet |
| 10 | RESEARCH_SA11: SA11 Stratified spaces cote 154 night  SENT | [RESEARCH_SA11_checkpoint_01_20261119T1525Z](../../raw/research_returns/RESEARCH_SA11_checkpoint_01_20261119T1525Z_unzipped/) | not yet |
| 11 | RESEARCH_SA22: SA22 Enseignement cotes 66-68 night  SENT | [RESEARCH_SA22_final_20261119T1905Z](../../raw/research_returns/RESEARCH_SA22_final_20261119T1905Z_unzipped/) | not yet |
| 12 | RESEARCH_SA20: SA20 Esquisse cotes 121-125 155 night  SENT | [RESEARCH_SA20_final_20261120T0404Z](../../raw/research_returns/RESEARCH_SA20_final_20261120T0404Z_unzipped/) | not yet |
| 13 | RESEARCH_SA17: SA17 FINISH Descentes cotes 126-133 night  SENT | [RESEARCH_SA17_checkpoint_12_20261119T2037Z](../../raw/research_returns/RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped/) | not yet |
| 14 | RESEARCH_SA08_C3_D031: SA08 C3 and Caradot-Lin check day  SENT | [RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z](../../raw/research_returns/RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped/) | not yet |
| 15 | RESEARCH_SA13: SA13 SGA working papers cotes 27-42 night | not yet back | not yet |
| 16 | RESEARCH_SA12: SA12 SGA cd of affines and pi1 cotes 29-31 night | [RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z](../../raw/research_returns/RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped/) | not yet |
| 17 | RESEARCH_SA23: SA23 EGA drafts and letters cotes 1-2 21-26 161 night | [RESEARCH_SA23_final_20261120T0511Z](../../raw/research_returns/RESEARCH_SA23_final_20261120T0511Z_unzipped/) | not yet |
| 18 | RESEARCH_SA04: SA04 Regular polytopes over rings cotes 69-89 93 101 night | not yet back | not yet |
| 19 | RESEARCH_SA14_SA19: SA14 SA19 Picard and Jacobians cotes 43-44 57-60 night | [RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z](../../raw/research_returns/RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped/) | not yet |
| 20 | RESEARCH_SA16_SA18: SA16 SA18 Elliptic curves and abelian varieties cotes 45-56 62-64 night | not yet back | not yet |
| 21 | RESEARCH_SA02: SA02 Quadratic covers cotes 77 83 84 night | not yet back | not yet |
| 22 | ALPOGE_BRIDGES: ALPOGE RH bridges into the programme | [ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z](../../raw/research_returns/ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z_unzipped/) | [INTAKE_ALPOGE_BRIDGES_20261121.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121.md), [INTAKE_ALPOGE_BRIDGES_20261121_part2.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part2.md), [INTAKE_ALPOGE_BRIDGES_20261121_part3.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part3.md), [INTAKE_ALPOGE_BRIDGES_20261121_part4.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part4.md), [INTAKE_ALPOGE_BRIDGES_cp03_20261121.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_cp03_20261121.md) |
| 23 | ALPOGE_GCT: ALPOGE GCT purity and plethysm | [ALPOGE_GCT_checkpoint_09_20261121T0547Z](../../raw/research_returns/ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/) | [INTAKE_ALPOGE_GCT_20261121.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121.md), [INTAKE_ALPOGE_GCT_20261121_part2.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part2.md), [INTAKE_ALPOGE_GCT_20261121_part3.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part3.md), [INTAKE_ALPOGE_GCT_20261121_part4.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part4.md), [INTAKE_ALPOGE_GCT_cp03_20261121.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_cp03_20261121.md) |
| 24 | GCT_NSRH: GCT NONSTANDARD RH and purity by positivity | [GCT_NSRH_checkpoint_09_20261121T0545Z](../../raw/research_returns/GCT_NSRH_checkpoint_09_20261121T0545Z_unzipped/) | [INTAKE_GCT_NSRH_20261121.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121.md), [INTAKE_GCT_NSRH_20261121_part2.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part2.md), [INTAKE_GCT_NSRH_20261121_part3.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part3.md), [INTAKE_GCT_NSRH_20261121_part4.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part4.md), [INTAKE_GCT_NSRH_cp03_20261121.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_cp03_20261121.md) |
| 25 | GCT_PLETH: GCT PLETHYSM through Grothendiecks lambda rings | [GCT_PLETH_checkpoint_09_20261121T0546Z](../../raw/research_returns/GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped/) | [INTAKE_GCT_PLETH_20261121.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121.md), [INTAKE_GCT_PLETH_20261121_part2.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part2.md), [INTAKE_GCT_PLETH_20261121_part3.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part3.md), [INTAKE_GCT_PLETH_20261121_part4.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part4.md), [INTAKE_GCT_PLETH_cp03_20261121.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_cp03_20261121.md) |
| 26 | GCT_KRON: GCT KRONECKER through lambda operations on G-sets | [GCT_KRON_checkpoint_07_20261121T0415Z](../../raw/research_returns/GCT_KRON_checkpoint_07_20261121T0415Z_unzipped/) | [INTAKE_GCT_KRON_20261121.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121.md), [INTAKE_GCT_KRON_20261121_part2.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121_part2.md), [INTAKE_GCT_KRON_20261121_part3.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121_part3.md), [INTAKE_GCT_KRON_cp03_20261121.md](intakes/GCT_KRON/INTAKE_GCT_KRON_cp03_20261121.md) |
| 27 | GCT_GINEQ: GCT GROTHENDIECK INEQUALITY and tensor norms | [GCT_GINEQ_final_20261120T2340Z](../../raw/research_returns/GCT_GINEQ_final_20261120T2340Z_unzipped/) | [INTAKE_GCT_GINEQ_20261121.md](intakes/GCT_GINEQ/INTAKE_GCT_GINEQ_20261121.md) |
| 28 | CX_GRH: GRH and ETH in complexity Koiran GCT V | [CX_GRH_final_20261121T0005Z](../../raw/research_returns/CX_GRH_final_20261121T0005Z_unzipped/) | [INTAKE_CX_GRH_20261121.md](intakes/CX_GRH/INTAKE_CX_GRH_20261121.md) |
| 29 | DELTA23: DELTA 2-3 reciprocity of frames on GT | [DELTA23_checkpoint_06_20261121T0329Z](../../raw/research_returns/DELTA23_checkpoint_06_20261121T0329Z_unzipped/) | [INTAKE_DELTA23_20261121.md](intakes/DELTA23/INTAKE_DELTA23_20261121.md) |
| 30 | AN_GRH: GRH ANABELIAN Hooley Chebotarev and cote 149 | [AN_GRH_final_20261121T0821Z](../../raw/research_returns/AN_GRH_final_20261121T0821Z_unzipped/) | [INTAKE_AN_GRH_20261121.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121.md), [INTAKE_AN_GRH_20261121_full.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121_full.md), [INTAKE_AN_GRH_20261121_part2.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121_part2.md), [INTAKE_AN_GRH_20261121_part3.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121_part3.md) |
| 31 | K17: STEP17 K-groups of Z Soule and pro-l kernels | [K17_checkpoint_08_20261121T0616Z](../../raw/research_returns/K17_checkpoint_08_20261121T0616Z_unzipped/) | [INTAKE_K17_20261121.md](intakes/K17/INTAKE_K17_20261121.md), [INTAKE_K17_20261121_part2.md](intakes/K17/INTAKE_K17_20261121_part2.md), [INTAKE_K17_20261121_part3.md](intakes/K17/INTAKE_K17_20261121_part3.md), [INTAKE_K17_20261121_part4.md](intakes/K17/INTAKE_K17_20261121_part4.md) |
| 32 | HODGE_SIGN: HODGE SIGN sign-only purity as the Hodge index route cotes 16 44 | [HODGE_SIGN_final_20261121T0057Z](../../raw/research_returns/HODGE_SIGN_final_20261121T0057Z_unzipped/) | [INTAKE_HODGE_SIGN_20261121.md](intakes/HODGE_SIGN/INTAKE_HODGE_SIGN_20261121.md) |
| 33 | TRACE_DET: TRACE DET cote 1 trace formula and the determinants | [TRACE_DET_final_20261121T0218Z](../../raw/research_returns/TRACE_DET_final_20261121T0218Z_unzipped/) | [INTAKE_TRACE_DET_20261121.md](intakes/TRACE_DET/INTAKE_TRACE_DET_20261121.md), [INTAKE_TRACE_DET_20261121_part2.md](intakes/TRACE_DET/INTAKE_TRACE_DET_20261121_part2.md) |
| 34 | DP_MULT: DP MULT divided powers and the multiplicity of step 2 | [DP_MULT_checkpoint_06_20261121T0420Z](../../raw/research_returns/DP_MULT_checkpoint_06_20261121T0420Z_unzipped/) | [INTAKE_DP_MULT_20261121.md](intakes/DP_MULT/INTAKE_DP_MULT_20261121.md), [INTAKE_DP_MULT_20261121_part2.md](intakes/DP_MULT/INTAKE_DP_MULT_20261121_part2.md), [INTAKE_DP_MULT_20261121_part3.md](intakes/DP_MULT/INTAKE_DP_MULT_20261121_part3.md), [INTAKE_DP_MULT_20261121_part4.md](intakes/DP_MULT/INTAKE_DP_MULT_20261121_part4.md), [INTAKE_DP_MULT_cp02_20261121.md](intakes/DP_MULT/INTAKE_DP_MULT_cp02_20261121.md) |
| 35 | ZETA_TWO: ZETA TWO RH for schemes and motives from the two proofs | [ZETA_TWO_final_20261121T0032Z](../../raw/research_returns/ZETA_TWO_final_20261121T0032Z_unzipped/) | [INTAKE_ZETA_TWO_20261121.md](intakes/ZETA_TWO/INTAKE_ZETA_TWO_20261121.md) |
| 36 | CUE_GCT: CUE GCT random matrices and isolation through GCT | [CUE_GCT_checkpoint_08_20261121T0649Z](../../raw/research_returns/CUE_GCT_checkpoint_08_20261121T0649Z_unzipped/) | [INTAKE_CUE_GCT_20261121.md](intakes/CUE_GCT/INTAKE_CUE_GCT_20261121.md), [INTAKE_CUE_GCT_20261121_part2.md](intakes/CUE_GCT/INTAKE_CUE_GCT_20261121_part2.md), [INTAKE_CUE_GCT_20261121_part3.md](intakes/CUE_GCT/INTAKE_CUE_GCT_20261121_part3.md), [INTAKE_CUE_GCT_20261121_part4.md](intakes/CUE_GCT/INTAKE_CUE_GCT_20261121_part4.md) |
| 37 | THETA3: HODGE THETA three signatures | [THETA3_checkpoint_07_20261121T0604Z](../../raw/research_returns/THETA3_checkpoint_07_20261121T0604Z_unzipped/) | [INTAKE_THETA3_20261121.md](intakes/THETA3/INTAKE_THETA3_20261121.md), [INTAKE_THETA3_20261121_part2.md](intakes/THETA3/INTAKE_THETA3_20261121_part2.md), [INTAKE_THETA3_20261121_part3.md](intakes/THETA3/INTAKE_THETA3_20261121_part3.md), [INTAKE_THETA3_20261121_part4.md](intakes/THETA3/INTAKE_THETA3_20261121_part4.md) |
| 38 | HECKE_DIV: HODGE HECKE DIVISION bounded division on Hecke orbits | [HECKE_DIV_final_20261121T0204Z](../../raw/research_returns/HECKE_DIV_final_20261121T0204Z_unzipped/) | [INTAKE_HECKE_DIV_20261121.md](intakes/HECKE_DIV/INTAKE_HECKE_DIV_20261121.md), [INTAKE_HECKE_DIV_20261121_part2.md](intakes/HECKE_DIV/INTAKE_HECKE_DIV_20261121_part2.md) |
| 39 | GHOSTS: HODGE GHOST CLASSES at supersingular and ordinary primes | [GHOSTS_final_20261121T0256Z](../../raw/research_returns/GHOSTS_final_20261121T0256Z_unzipped/) | [INTAKE_GHOSTS_20261121.md](intakes/GHOSTS/INTAKE_GHOSTS_20261121.md) |
| 40 | JAC1964: HODGE JACOBIANS 1964 cote 44 every characteristic | [JAC1964_checkpoint_06_20261121T0521Z](../../raw/research_returns/JAC1964_checkpoint_06_20261121T0521Z_unzipped/) | [INTAKE_JAC1964_20261121.md](intakes/JAC1964/INTAKE_JAC1964_20261121.md), [INTAKE_JAC1964_20261121_part2.md](intakes/JAC1964/INTAKE_JAC1964_20261121_part2.md) |
| 41 | DEG_L: HODGE DEGREES ARE L VALUES Rallis and semiregularity | [DEG_L_checkpoint_06_20261121T0517Z](../../raw/research_returns/DEG_L_checkpoint_06_20261121T0517Z_unzipped/) | [INTAKE_DEG_L_20261121.md](intakes/DEG_L/INTAKE_DEG_L_20261121.md), [INTAKE_DEG_L_20261121_part2.md](intakes/DEG_L/INTAKE_DEG_L_20261121_part2.md), [INTAKE_DEG_L_20261122_cp06.md](intakes/DEG_L/INTAKE_DEG_L_20261122_cp06.md) |
| 42 | GRH_NIGHT: GRH NIGHT everything that follows from the two proofs | [GRH_NIGHT_checkpoint_07_20261121T0617Z](../../raw/research_returns/GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped/) | [INTAKE_GRH_NIGHT_20261121.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121.md), [INTAKE_GRH_NIGHT_20261121_part2.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121_part2.md), [INTAKE_GRH_NIGHT_20261121_part3.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121_part3.md) |
| 43 | ZETA_NEXT: ZETA NEXT effective class numbers Lambda schemes and the non-CM gate | [ZETA_NEXT_final_20261121T0340Z](../../raw/research_returns/ZETA_NEXT_final_20261121T0340Z_unzipped/) | [INTAKE_ZETA_NEXT_20261121.md](intakes/ZETA_NEXT/INTAKE_ZETA_NEXT_20261121.md) |
| 44 | BR_PENCIL: BR PENCIL border rank of det4 and per4 by multi-dimensional substitution | [BR_PENCIL_checkpoint_02_20261121T0429Z](../../raw/research_returns/BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped/) | [INTAKE_BR_PENCIL_20261121.md](intakes/BR_PENCIL/INTAKE_BR_PENCIL_20261121.md), [INTAKE_BR_PENCIL_20261121_part2.md](intakes/BR_PENCIL/INTAKE_BR_PENCIL_20261121_part2.md) |
| 45 | SIGN_NEXT: SIGN NEXT Grothendiecks Hodge-index route after the sign-only proof | [SIGN_NEXT_checkpoint_02_20261121T0430Z](../../raw/research_returns/SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped/) | [INTAKE_SIGN_NEXT_20261121.md](intakes/SIGN_NEXT/INTAKE_SIGN_NEXT_20261121.md), [INTAKE_SIGN_NEXT_20261121_part2.md](intakes/SIGN_NEXT/INTAKE_SIGN_NEXT_20261121_part2.md) |
| 46 | HODGE_DIVISION: HODGE DIVISION bounding the detector degree of Weil classes | [HODGE_DIVISION_checkpoint_18_20261122T0009Z](../../raw/research_returns/HODGE_DIVISION_checkpoint_18_20261122T0009Z_unzipped/) | [INTAKE_HODGE_DIVISION_20261121.md](intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121.md), [INTAKE_HODGE_DIVISION_20261121_part2.md](intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121_part2.md), [INTAKE_HODGE_DIVISION_20261121_part3.md](intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121_part3.md) |
| 47 | KTOWER: KTOWER the Galois action on the tower the K groups of Z and cote 149 | [KTOWER_checkpoint_11_20261122T0001Z](../../raw/research_returns/KTOWER_checkpoint_11_20261122T0001Z_unzipped/) | [INTAKE_KTOWER_20261121.md](intakes/KTOWER/INTAKE_KTOWER_20261121.md), [INTAKE_KTOWER_20261121_part2.md](intakes/KTOWER/INTAKE_KTOWER_20261121_part2.md) |
| 48 | MAS_ARTIN: a central trace identity over Q, the S₅ Artin gate and the analytic premise | [MAS_ARTIN_checkpoint_12_20261122T0031Z](../../raw/research_returns/MAS_ARTIN_checkpoint_12_20261122T0031Z_unzipped/) | [INTAKE_MAS_ARTIN_20261121.md](intakes/MAS_ARTIN/INTAKE_MAS_ARTIN_20261121.md), [INTAKE_MAS_ARTIN_20261121_part2.md](intakes/MAS_ARTIN/INTAKE_MAS_ARTIN_20261121_part2.md) |
| 49 | ALP_MACHINE: ALP MACHINE Alp ge s machine the lift count the definite seesaw Kummer characters and the os | [ALP_MACHINE_checkpoint_07_20261122T0050Z](../../raw/research_returns/ALP_MACHINE_checkpoint_07_20261122T0050Z_unzipped/) | [INTAKE_ALP_MACHINE_20261121_hecke.md](intakes/ALP_MACHINE/INTAKE_ALP_MACHINE_20261121_hecke.md), [INTAKE_ALP_MACHINE_20261121_lifts.md](intakes/ALP_MACHINE/INTAKE_ALP_MACHINE_20261121_lifts.md) |
| 50 | ARCH_ALG: ARCH ALG the archive s algebra cotes 136 134 8 15 and 123 from where ALPOGE BRIDGES stopp | [ARCH_ALG_checkpoint_01_20261121T2359Z](../../raw/research_returns/ARCH_ALG_checkpoint_01_20261121T2359Z_unzipped/) | not yet |
| 51 | C44_POS: C44 POS positivity in Grothendieck s 1964 programme cote 44 and his correspondence route | [C44_POS_checkpoint_01_20261121T2359Z](../../raw/research_returns/C44_POS_checkpoint_01_20261121T2359Z_unzipped/) | not yet |
| 52 | GCT_POS: GCT POS the positivity hypotheses of geometric complexity theory after the plethysm refu | [GCT_POS_checkpoint_06_20261122T0031Z](../../raw/research_returns/GCT_POS_checkpoint_06_20261122T0031Z_unzipped/) | [INTAKE_GCT_POS_20261121_kronecker.md](intakes/GCT_POS/INTAKE_GCT_POS_20261121_kronecker.md), [INTAKE_GCT_POS_20261121_nonstandard.md](intakes/GCT_POS/INTAKE_GCT_POS_20261121_nonstandard.md) |
| 53 | GCT_OBS: GCT OBS explicit multiplicity obstructions for the padded permanent and the border rank  | [GCT_OBS_checkpoint_01_20261121T2357Z](../../raw/research_returns/GCT_OBS_checkpoint_01_20261121T2357Z_unzipped/) | not yet |
| 54 | NEG_NIGHT: NEG NIGHT everything that follows from the refutations of ETH and of GCT VI s positivity h | [NEG_NIGHT_checkpoint_06_20261122T0034Z](../../raw/research_returns/NEG_NIGHT_checkpoint_06_20261122T0034Z_unzipped/) | [INTAKE_NEG_NIGHT_20261121.md](intakes/NEG_NIGHT/INTAKE_NEG_NIGHT_20261121.md), [INTAKE_NEG_NIGHT_20261121_G.md](intakes/NEG_NIGHT/INTAKE_NEG_NIGHT_20261121_G.md) |
| 55 | ALP_CONNES: ALP CONNES Alp ge s theorem pushed through Connes s programme and the next rung over Q | [ALP_CONNES_checkpoint_01_20261122T0054Z](../../raw/research_returns/ALP_CONNES_checkpoint_01_20261122T0054Z_unzipped/) | not yet |

## Left out
- **Copies of other people's work** that came back inside the returns. Link to the originals instead:
  - the draft mentioned above, its extracted text, our transcription of it and our index of its statements;
  - Alpöge's note and its text (its Lean formalization is not left out: the Lean files in the returns are copies
    from L. Alpöge's archive at https://alpo.ge/, made by him working with Claude, or the runs' own);
  - arXiv sources.

  Everything the runs derived from these is included.
- Images and packed archives.

Text written by AI is dedicated to the public domain under CC0 1.0.
