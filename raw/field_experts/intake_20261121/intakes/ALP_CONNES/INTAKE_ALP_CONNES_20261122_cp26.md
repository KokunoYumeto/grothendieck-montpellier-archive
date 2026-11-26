# Intake of ALP_CONNES checkpoint 26 (prompt 55), by diff from checkpoint 24

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode) and is still going.

Return: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\ALP_CONNES_checkpoint_26_20261122T2240Z_unzipped\ALP_CONNES`.
Earlier intake: `INTAKE_ALP_CONNES_20261122_cp24.md` beside this file.

Masullo's draft is not a proof, and no result here is a fix of it. A is Alpöge's theorem.

## 0. Method, read and not read
- The diff baseline is `reviews/movement_review_19.tsv`, the run's full question snapshot taken at the checkpoint 24
  time (21:09 UTC); no separate cp24 register was kept.
  - Of 1019 rows, 36 are new and 11 changed; none were removed.
  - There are 10 new modules: G127-G134 and S52.
  - No module checked earlier changed: the cp24 \input list is a subset of the cp26 list.
- **Read in full:** every new and changed row (state and finding), movement review 20, and the proof of AC-G129.
- **Statements only:** AC-G127, G128, G130, G131, G132, G133, G134, S52.
- **Not read:** the proofs of G127, G128 and G130-G134, and the run's verifier programs. I did not run any program of
  the return.

## 1. What moved since checkpoint 24

All new results are in the cubic arithmetic branch at the coefficient prime 269, plus one abstract spectral example.

| row | result | our check |
|---|---|---|
| AC-G129 (QG596-598) | L = Q(∛269, ζ₅) of degree 12 has no 269-torsion in its class group: h_L = 189m with 269 ∤ m. Hence every nontrivial cubic class sector of M = L(√−3) vanishes. The proof uses no trust in PARI's class group: exact units, a 269-saturation matrix, an elementary regulator lower bound, and interval isolation of the analytic class formula, with the Hecke phase fixed by θ(1). | **targeted proof check, confirmed**, given Arb's interval run, which was not replayed. Our own recomputation: the five units are units (monic integral characteristic polynomials with constant term 1); the saturation matrix (QCC.5) and its determinant −3919610628 ≡ 208 mod 269 match exactly; R_U = 20872891.07; and a floating evaluation of h_L R_L/R_U gives 188.9999998, against the certified 189. |
| AC-G130 (QG599-603) | Strict Selmer vanishing over K = Q(√−3) for χ^(−j)(Ψ^σ ω_p^r κ)^(−1)c_p^(−e), with e + r ≡ 267 mod 268. This covers both primitive quartic characters Ψ mod 5, every original coefficient DVR, and every continuous residually trivial κ unramified away from 269. It is unconditional. | statement read |
| AC-G133, G134 (QG612-618) | The same at e + r ≡ 133 mod 268, through the ramified quartic reflection field (D_L = 3⁴5⁹269¹⁰, h = 1428m, 269 ∤ m). Together, 4·269^(m−1) sufficient labels at fixed weight and modulus 5·269^m. | statement read |
| AC-G131 (QG604-607) | The missing sextic class input D30935: h = 1008m, 269 ∤ m. | statement read |
| AC-G132 (QG608-611; QG535, 547, 551, 570, 571, 575, 579 changed) | Fresh e ≡ 133 native hosts, so actual M1-M5 and cotangent counting hold on all **eight** quadratic rows (conductors 4, 20, 1076, 5380; e ≡ 133 and 267). These rest on retained modularity, local-global and coefficient inputs. | statement read |
| AC-G127, G128 (QG588-595, 555) | An auxiliary quartic seed at the target weights. Under the retained inputs, the original quartic Type II points at e ≡ 133 and 267 are excluded, as G116 did for the quadratic ones. M4 follows only after actual M2 and native support. | statement read |
| AC-S52 (SQ28-31) | An explicit compact positive example with the exact rank-one commutator, in which the quotient norm still diverges (≥ 1/(√5 τ)). Compactness, strong convergence and the commutator therefore cannot give the S51 edge comparison without a quantitative rate. It is an abstract obstruction to a proof route, not a statement about the Weil operator. | statement read |

## 2. The four main gates
| gate | moved? |
|---|---|
| H04.4 (window inequality for the cubic Kummer character) | no; QG611 and QG619 say so |
| RH for the cubic character | no |
| T51's defect limit without zero location | no; review 20, Q1, unchanged |
| lower bound on a₂ (or the S48 ratio, or the S51 odd gap) | no. S52 shows a rate is needed |

Review 20 says "Movement: yes" (0 consecutive without movement), crediting G129/G130 as a new arithmetic family and
G131 as a smaller e ≡ 133 host gate. By the 17 Nov criterion this is side-row movement. The run is productive, and its
main questions are not converging.

## 3. My cp24 questions: what the run did
These questions were addressed to the next prompt. This run's prompt did not ask them, so absence is expected.
- **Lefschetz formula on the corrected Deninger space with spectral side AC-T46:** nothing new. Review 20 Q6 keeps the
  checkpoint 18 corrections, T15-T17, as its whole Deninger content.
- **Connes-Consani F₁ statements from A:** nothing new. Review 20 Q5: "A geometric arithmetic surface square, its
  global cohomology/intersection theory and polarized surface Riemann-Roch theorem remain unconstructed." The analytic
  Hodge inequality, the numerical square and the sheaf/Artin-Tate models are from before checkpoint 18.
- **A through the BC/BCM systems:** no new row. Review 20's follow-up row: "A does not imply a new phase transition,
  finite-order cubic RH, or local weight purity". KMS classification beyond the source needs the actual algebra.
- **The a₂ bound:** not proved. S52 rules out the rate-free operator route.

**Shown at checkpoint 26:** the class and unit certificates and the strict-vanishing towers above.
**Only spotted:** nothing new on the Connes-Consani-Deninger side.

## 4. For the next prompt (68 or its successor)
- Add the question that the Deninger and F₁ items are still unattacked.
- Add S52 as a constraint: any a₂ or odd-gap argument must supply a quantitative rate.
- The cubic branch now has certified 269-class data for five fields (G103, G114, G126, G129, G131, G133). It has strict
  vanishing for the χ₋₄, χ₋₂₀ and quartic mod-5 towers, and M1-M5 on eight rows. H04.4 is no nearer; what remains is
  the all-prime and all-family budget.

## 5. Outreach and Hexagon
- No new outreach.
- G129's method (a 269-coprimality certificate for h_L from units, saturation and interval isolation, without a full
  unit basis or trusting bnfinit) is standard in principle. As an exact certificate it is not ready for Hexagon until
  the Arb run is replayed and the literature (Belabas, Buchmann-style certification) is compared.

## 6. Not for GitHub
`input_material/` (others' LaTeX and Alpöge's remark), the .lean interface files, `evidence/ALPOGE_remark.txt`, and
the third-party texts listed in the cp24 intake.
