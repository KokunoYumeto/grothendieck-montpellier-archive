# Paper seeds: MAS_ARTIN checkpoint 15, with CX_GRH and GRH_NIGHT

Seed by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), 22 Nov 2026. The runs are GPT-6 Astra (ChatGPT Pro mode).

"Checked" means a targeted proof check by Claude Opus 5.5 at effort high, with the cited inputs taken as stated. Input A is Alpöge's theorem
(RH for zeta and Dirichlet L-functions). Input M is Masullo's unrefereed claim (GRH for Hecke L-functions of every
number field). The two are never merged.

The trace-route results of this run (MA-HM-001/003, MA-JP-004, MA-FT-002) and GRH_NIGHT MT-M20/M23 belong to the trace
formula cluster and are placed in Paper 1 of `<local>/Documents\reports_20261122\paper_seeds\SEED_ALP_CONNES.md`,
so that the cluster stays in one paper.

## Paper 1. Artin's conjecture for some S5 extensions, allowing a zero at the central point

### Main theorem
Let L/Q be Galois with group S5, unramified at 5, with complex conjugation and Frob_5 of cycle type (12)(34). Put
E = L^A5, F = L^F20 (degree 6), H = EF and B = ζ_H/ζ_F, a quadratic Hecke L-function over F.

Hypothesis R_B: B(σ) ≠ 0 for real σ in (0,1) with σ ≠ 1/2. A zero at 1/2 of any order is allowed.

Under R_B:
- Calegari's cuspidal GL5 representation ϖ matches the five-dimensional Artin representation W at every place;
- ord B = ord L(η_E) + ord L(ϖ) at 1/2;
- the nontrivial irreducible Artin representations of this extension are automorphic and their L-functions are entire.

The last line rests on MA-S5-001's account of Calegari's comparison. R_B is not proved for the family. Neither A nor M is
used. M would imply R_B, and A does not.

Inputs: Calegari's construction and comparison lemmas; Booker, Math. Ann. 363 (2015), Examples 1.4, Theorems 1.6-1.7
and Proposition 2.1; Cohen's idempotent theorem as Sanders (2020), Theorem 12.3. Sources are through the run, not
opened by us.

### Why it matters
The hypothesis is about real zeros of one explicit Hecke L-function and can be tested field by field. The new step is
that an excess zero at the centre would make an integer positive-definite function on a discrete real line, and
Cohen's theorem then allows only finitely many exceptional primes.

It continues F. Calegari, "The Artin conjecture for some S5-extensions", Math. Ann. 356 (2013) 191-207, Theorems 1.1,
1.2 and 4.7 and Lemmas 4.8-4.10 (through the run's locators, source not opened). Open his Theorem 1.2 and state
exactly which hypothesis this removes before claiming an improvement.

### The argument, in order
| result | content | proof file and lines | check by us |
|---|---|---|---|
| MA-S5-001 | k = β−b−n ≥ 0, and k = 0 iff all-place comparison | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5.tex` 49-150 | checked given Calegari's lemmas |
| MA-S5-004 | exceptional-prime asymptotic when k > 0 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5.tex` 471-560 and following | checked to line 560 |
| MA-LD-001 | the quotient divisor lies on the critical line | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\booker_route.tex` 38 to the next paragraph | checked given Booker |
| MA-FQ-001 | the atomic function is positive definite | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5_crystal.tex` 11 to the next paragraph | checked |
| MA-FQ-002 | locally finite cosets are progressions | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5_coset.tex` 12 to the next paragraph | checked given Sanders |
| MA-FQ-003 | only finitely many prime frequencies | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5_crystal_rigidity.tex` 11-119 | checked |
| MA-FQ-004 | k = 0 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5_crystal_rigidity.tex` 121-172 | checked given the rows above |
| MT-S506, with A | for every S5 extension, possible poles of irreducible factors in the strip are at zeros of ζ or L(η_E), so on the line by A | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` from 25778 | checked earlier given the induction table |

Separate conditional remark: under M, R_B holds and all the factors in the family satisfy GRH.

Programs: `checks/s5/` in the return, for the auxiliary cone result only. Not run by us.

### Research question
Prove the theorem without R_B. The gate at checkpoint 15 is MA-RB014, an envelope and integer-cap inequality on
nonreal zero backgrounds (`<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\s5_nonreal_background.tex` from 44, statement start read). MA-RB016 shows that the
induced spin Rankin-Selberg partner gives no new inequality.

Routes not tried, as far as we read (suggestions by Claude Opus 5.5 at effort high): certified computation of R_B on explicit fields; extending
the positive-definite argument to a real pole away from 1/2.

Workbench: Artin conjecture.

## Paper 2. Exactly which Riemann hypothesis factoring polynomials needs

### Main theorem (A, plus one named zeta function)
Let r be an odd prime and p ≠ r a prime. Assume A. RH for ζ of Q(p^(1/r)) is equivalent to RH for ζ of Q(ζ_r, p^(1/r)),
since ζ_E = ζ_K (ζ_F/ζ)^(r−1). If it holds, an auxiliary prime of size O(r⁴ log²(rp)) exists and F_(p^r) is constructed
deterministically in polynomial time in r and log p. Without A, a supplied F_(p^r) gives the maximal Teichmüller unit
in F_p[T]/Φ_r and conversely.

### Why it matters
It replaces a blanket GRH by one pure-field zeta function for each bad prime, and says what Alpöge's theorem already
removes. It continues Evdokimov, ANTS I (1994) 209-219; Bach-Sorenson, Math. Comp. 65 (1996), Theorem 5.1; Lenstra
(1991), Theorems 5.1-5.2 (through the runs' locators, sources not opened).

### The argument, in order
All checks in this table are targeted checks of 21 Nov by Claude Opus 5.5 at effort high, recorded under `<local>/Documents\field_experts\intake_20261121\intakes\CX_GRH` and `<local>/Documents\field_experts\intake_20261121\intakes\GRH_NIGHT`.

| input | results | proof file and lines | check by us |
|---|---|---|---|
| none | CX-R02, CX-K04 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 194-219, 515-534 | checked |
| none | CX-ALG-017, 018 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` 14011-14066, from 14067 | checked |
| none | CX-ALG-023 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` 14621-14722 | checked at checkpoint 02 |
| A, then RH of one pure field | CX-ALG-024 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` 14723-14826 | checked at checkpoint 02 |
| A | CX-R01, K03 | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 163-192, 480-508 | checked |
| A | Miller with Bach's cutoff; nonresidues; primitive roots (N01-N04) | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 793-901 | checked |
| A | nonresidues for r dividing p−1 (N13); algebra splitting case (ii) (N14) | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 1386-1480, 1483-1789 | new steps checked |
| A | MT-A01, the adelic statement of A | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` from 15734 | checked at checkpoint 02 |
| M | HN in AM (K01, K02); PH level (K05) | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 339-478, 540-638 | checked as implications |
| M | auxiliary field (N11); factoring in (d^log d log q)^O(1) (N15) | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` 944-1041, 1792-2077 | N15 checked modulo its three cited algorithms |
| M and PF26 | polynomial-time transfer | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` 15371-15500 (CX-ALG-027), from 15501 (028) | 027 transfer checked; 028 read in part |

PF26 is OpenAI's unrefereed preprint of 4 Oct 2026, "Deterministic Polynomial Factorization over Prime Fields".
The paper keeps the four input classes in separate sections.

Programs: none for the main theorem.

### Research question
Construct F_(p^r) from A alone when r does not divide p−1 and r² divides p^ord_r(p) − 1. The gate is one order-r
Kummer Hecke character. Route not tried (suggestion by Claude Opus 5.5 at effort high): the window inequality AM-H04 for that character.

**Status of this question, 23 Nov 2026** (GRH_ALGORITHMS and its finishing run 67c, GPT-6 Astra (ChatGPT Pro mode), to
finishing checkpoint 04; intake by Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7): partly settled.
- From A alone, for each fixed r and each fixed valuation b = v_r(p^d − 1) (d = ord_r p), F_(p^r) is constructed in time
  C_{r,b}(log p)^{c_{r,b}} (GRH-P125/P126, after Pila).
- Unconditionally, it is constructed in time polynomial in r, log p, L and C_L, where C_L is Φ_d(p) with its 2-, r- and
  ℓ-primary parts removed for every prime ℓ ≤ L with r ∤ ℓ − 1 (GRH-P144/P145, after Bach-von zur Gathen-Lenstra).
- Open: the uniform case with growing valuation and cofactor.

The checks, with the files, are in
`field_experts/intake_20261121/intakes/GRH_ALGORITHMS_FINISH/INTAKE_GRH_ALGORITHMS_FINISH_20261123_cp04.md`.

Workbench: GRH and complexity.

## For both papers

LaTeX to attach: the proof files above; arXiv:1112.1152 (Calegari, identifier from memory) and arXiv:1308.3067v2
(Booker).

Never to GitHub:
- Masullo's PDF and every text extract or page image of it (GRH_NIGHT `work/evidence/masullo*` and `MASULLO_*.txt`);
- GRH_NIGHT `work/evidence/ALPOGE_remark.txt`;
- MAS_ARTIN `evidence/pf26.txt`, `evidence/pf26_pages/`, `evidence/pf26_p35.png`, `evidence/pf26_analytic-44.png`,
  `evidence/pf26_analytic-45.png`;
- other authors' papers and sources in either return.

No literature search was made, Hexagon included.
