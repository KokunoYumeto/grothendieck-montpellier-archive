# The two GRH proofs of 20 November 2026: our working-through, status as of 21 Nov 2026 20:10 UTC

On 20 Nov 2026 two proofs of generalized Riemann hypotheses appeared:
- **L. Alpöge**: RH, and GRH for Dirichlet L-functions. A note (https://alpo.ge/remark.pdf), with a Lean formalization
  whose `Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements.
- **A. M. Masullo**: GRH for the Hecke L-functions of every number field. A 940-page draft, announced by R. Vakil:
  https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

Both are unrefereed. That night we sent 21 research prompts (22-42) to GPT-6 Astra (ChatGPT Pro mode), asking how the two
results bear on the Grothendieck programme of this repository, on geometric complexity theory, and on each other. We
took the returns in as they landed. Results that need only Alpöge are marked as such; those that need Masullo are
marked conditional.

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
  and then Alpöge suffices. Others need number fields, and then they need Masullo: Koiran's Nullstellensatz in AM,
  Hooley's Artin conjecture, effective Chebotarev.
- **Zeta functions of schemes and motives** (35 ZETA_TWO):
  - Under Masullo, RH holds for every CM motive. The open part is the non-CM motives.
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
| 22 | ALPOGE_BRIDGES: ALPOGE RH bridges into the programme | [ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z](../../raw/research_returns/ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z_unzipped/) | [INTAKE_ALPOGE_BRIDGES_20261121.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121.md), [INTAKE_ALPOGE_BRIDGES_20261121_part2.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part2.md), [INTAKE_ALPOGE_BRIDGES_20261121_part3.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part3.md), [INTAKE_ALPOGE_BRIDGES_20261121_part4.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_20261121_part4.md), [INTAKE_ALPOGE_BRIDGES_cp03_20261121.md](intakes/ALPOGE_BRIDGES/INTAKE_ALPOGE_BRIDGES_cp03_20261121.md) |
| 23 | ALPOGE_GCT: ALPOGE GCT purity and plethysm | [ALPOGE_GCT_checkpoint_09_20261121T0547Z](../../raw/research_returns/ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/) | [INTAKE_ALPOGE_GCT_20261121.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121.md), [INTAKE_ALPOGE_GCT_20261121_part2.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part2.md), [INTAKE_ALPOGE_GCT_20261121_part3.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part3.md), [INTAKE_ALPOGE_GCT_20261121_part4.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_20261121_part4.md), [INTAKE_ALPOGE_GCT_cp03_20261121.md](intakes/ALPOGE_GCT/INTAKE_ALPOGE_GCT_cp03_20261121.md) |
| 24 | GCT_NSRH: GCT NONSTANDARD RH and purity by positivity | [GCT_NSRH_checkpoint_09_20261121T0545Z](../../raw/research_returns/GCT_NSRH_checkpoint_09_20261121T0545Z_unzipped/) | [INTAKE_GCT_NSRH_20261121.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121.md), [INTAKE_GCT_NSRH_20261121_part2.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part2.md), [INTAKE_GCT_NSRH_20261121_part3.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part3.md), [INTAKE_GCT_NSRH_20261121_part4.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_20261121_part4.md), [INTAKE_GCT_NSRH_cp03_20261121.md](intakes/GCT_NSRH/INTAKE_GCT_NSRH_cp03_20261121.md) |
| 25 | GCT_PLETH: GCT PLETHYSM through Grothendiecks lambda rings | [GCT_PLETH_checkpoint_09_20261121T0546Z](../../raw/research_returns/GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped/) | [INTAKE_GCT_PLETH_20261121.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121.md), [INTAKE_GCT_PLETH_20261121_part2.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part2.md), [INTAKE_GCT_PLETH_20261121_part3.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part3.md), [INTAKE_GCT_PLETH_20261121_part4.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_20261121_part4.md), [INTAKE_GCT_PLETH_cp03_20261121.md](intakes/GCT_PLETH/INTAKE_GCT_PLETH_cp03_20261121.md) |
| 26 | GCT_KRON: GCT KRONECKER through lambda operations on G-sets | [GCT_KRON_checkpoint_07_20261121T0415Z](../../raw/research_returns/GCT_KRON_checkpoint_07_20261121T0415Z_unzipped/) | [INTAKE_GCT_KRON_20261121.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121.md), [INTAKE_GCT_KRON_20261121_part2.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121_part2.md), [INTAKE_GCT_KRON_20261121_part3.md](intakes/GCT_KRON/INTAKE_GCT_KRON_20261121_part3.md), [INTAKE_GCT_KRON_cp03_20261121.md](intakes/GCT_KRON/INTAKE_GCT_KRON_cp03_20261121.md) |
| 27 | GCT_GINEQ: GCT GROTHENDIECK INEQUALITY and tensor norms | [GCT_GINEQ_final_20261120T2340Z](../../raw/research_returns/GCT_GINEQ_final_20261120T2340Z_unzipped/) | [INTAKE_GCT_GINEQ_20261121.md](intakes/GCT_GINEQ/INTAKE_GCT_GINEQ_20261121.md) |
| 28 | CX_GRH: GRH and ETH in complexity Koiran GCT V | [CX_GRH_final_20261121T0005Z](../../raw/research_returns/CX_GRH_final_20261121T0005Z_unzipped/) | [INTAKE_CX_GRH_20261121.md](intakes/CX_GRH/INTAKE_CX_GRH_20261121.md) |
| 29 | DELTA23: DELTA 2-3 reciprocity of frames on GT | [DELTA23_checkpoint_06_20261121T0329Z](../../raw/research_returns/DELTA23_checkpoint_06_20261121T0329Z_unzipped/) | [INTAKE_DELTA23_20261121.md](intakes/DELTA23/INTAKE_DELTA23_20261121.md) |
| 30 | AN_GRH: GRH ANABELIAN Hooley Chebotarev and cote 149 | [AN_GRH_final_20261121T0821Z](../../raw/research_returns/AN_GRH_final_20261121T0821Z_unzipped/) | [INTAKE_AN_GRH_20261121.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121.md), [INTAKE_AN_GRH_20261121_part2.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121_part2.md), [INTAKE_AN_GRH_20261121_part3.md](intakes/AN_GRH/INTAKE_AN_GRH_20261121_part3.md) |
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
| 41 | DEG_L: HODGE DEGREES ARE L VALUES Rallis and semiregularity | [DEG_L_checkpoint_06_20261121T0517Z](../../raw/research_returns/DEG_L_checkpoint_06_20261121T0517Z_unzipped/) | [INTAKE_DEG_L_20261121.md](intakes/DEG_L/INTAKE_DEG_L_20261121.md), [INTAKE_DEG_L_20261121_part2.md](intakes/DEG_L/INTAKE_DEG_L_20261121_part2.md) |
| 42 | GRH_NIGHT: GRH NIGHT everything that follows from the two proofs | [GRH_NIGHT_checkpoint_07_20261121T0617Z](../../raw/research_returns/GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped/) | [INTAKE_GRH_NIGHT_20261121.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121.md), [INTAKE_GRH_NIGHT_20261121_part2.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121_part2.md), [INTAKE_GRH_NIGHT_20261121_part3.md](intakes/GRH_NIGHT/INTAKE_GRH_NIGHT_20261121_part3.md) |
| 43 | ZETA_NEXT: ZETA NEXT effective class numbers Lambda schemes and the non-CM gate | [ZETA_NEXT_final_20261121T0340Z](../../raw/research_returns/ZETA_NEXT_final_20261121T0340Z_unzipped/) | [INTAKE_ZETA_NEXT_20261121.md](intakes/ZETA_NEXT/INTAKE_ZETA_NEXT_20261121.md) |
| 44 | BR_PENCIL: BR PENCIL border rank of det4 and per4 by multi-dimensional substitution | [BR_PENCIL_checkpoint_02_20261121T0429Z](../../raw/research_returns/BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped/) | [INTAKE_BR_PENCIL_20261121.md](intakes/BR_PENCIL/INTAKE_BR_PENCIL_20261121.md), [INTAKE_BR_PENCIL_20261121_part2.md](intakes/BR_PENCIL/INTAKE_BR_PENCIL_20261121_part2.md) |
| 45 | SIGN_NEXT: SIGN NEXT Grothendiecks Hodge-index route after the sign-only proof | [SIGN_NEXT_checkpoint_02_20261121T0430Z](../../raw/research_returns/SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped/) | [INTAKE_SIGN_NEXT_20261121.md](intakes/SIGN_NEXT/INTAKE_SIGN_NEXT_20261121.md), [INTAKE_SIGN_NEXT_20261121_part2.md](intakes/SIGN_NEXT/INTAKE_SIGN_NEXT_20261121_part2.md) |
| 46 | HODGE_DIVISION: HODGE DIVISION bounding the detector degree of Weil classes | [HODGE_DIVISION_checkpoint_12_20261121T1939Z](../../raw/research_returns/HODGE_DIVISION_checkpoint_12_20261121T1939Z_unzipped/) | [INTAKE_HODGE_DIVISION_20261121.md](intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121.md), [INTAKE_HODGE_DIVISION_20261121_part2.md](intakes/HODGE_DIVISION/INTAKE_HODGE_DIVISION_20261121_part2.md) |
| 47 | KTOWER: KTOWER the Galois action on the tower the K groups of Z and cote 149 | [KTOWER_checkpoint_06_20261121T2002Z](../../raw/research_returns/KTOWER_checkpoint_06_20261121T2002Z_unzipped/) | [INTAKE_KTOWER_20261121.md](intakes/KTOWER/INTAKE_KTOWER_20261121.md) |
| 48 | MAS_ARTIN: MAS ARTIN Masullo s central trace identity over Q the S Artin gate and the analytic premis | [MAS_ARTIN_checkpoint_06_20261121T2001Z](../../raw/research_returns/MAS_ARTIN_checkpoint_06_20261121T2001Z_unzipped/) | [INTAKE_MAS_ARTIN_20261121.md](intakes/MAS_ARTIN/INTAKE_MAS_ARTIN_20261121.md) |

## Left out
- **Copies of other people's work** that came back inside the returns. Link to the originals instead:
  - Masullo's PDF and its extracted text;
  - our full transcription of his draft, and our index of his statements, which quotes the opening of each one;
  - Alpöge's note, its text and his Lean files;
  - arXiv sources.

  Everything the runs derived from these is included.
- Images and packed archives.

Text written by AI is dedicated to the public domain under CC0 1.0.
