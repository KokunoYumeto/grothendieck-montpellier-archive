# Our record of Masullo's draft: located defects, repairs and the open gate (21 Nov 2026)

Compiled by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e) from two research runs, GRH_NIGHT and
ALPOGE_BRIDGES, both GPT-6 Astra (ChatGPT Pro mode), and from our intakes of them. The draft is A. M. Masullo, *The
Music of the Primes* (940 pages, posted 20 Nov 2026,
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf). It is cited here by page,
equation and statement number only; no text of the draft is reproduced.

"Checked on the page" means that the intake (Claude Opus 5.5 at effort high) rendered that PDF page and compared the
statement with the run's reading. "Statement level" means that the run's finding was read as stated, not re-proved by
us.

| draft locator | what the run found | repair | finding ids | our check |
|---|---|---|---|---|
| Lemma 9.3.2.4, p. 425 | the general local zero count O(log\|T\|) for Mellin transforms of every φ ∈ S_E(G) is false: Mφ(s) = e^{s²} sin(s²) has about (2T+1)/π zeros in a unit box. The proof's Jensen step needs a lower bound at the centre, and only an upper bound is derived | for arithmetic φ the standard count for each fixed Hecke L-function holds (NT-Z10) | GRH_NIGHT MT-M01, MT-M04 | checked on the page; counterexample verified |
| Lemma 9.3.2.5, pp. 425-426 | the quotient by the convolution ideal φ ∗ S_E(G) has no Schauder basis of Mellin jets: the ideal is not closed (Gaussian counterexample, even for one simple zero or none) | the closed-ideal quotient; canonical block synthesis and an adapted absolute basis, unconditionally | MT-M05, MT-M06, MT-M18, MT-M19 | MT-M05 checked on the page; MT-M06/M18/M19 statement level |
| Theorem 9.3.2.6, p. 426 | the proof uses W_{≤T} ⊂ W_{≤T′} for T < T′; the inclusion goes the other way, and the projectors converge to the projection onto the common kernel, not to the identity | complementary projections onto the closed span of the Riesz vectors | MT-M02, MT-M03 | checked on the page |
| Theorem 11.1.2.1(2), p. 480 | cutoff strictness fails: in the Q trivial-character sector with S = {∞} and one-prime index steps, both cut-off closures are equal for every Λ > 1; minimal lift norms diverge like L^{(s−1)/2} | strictness needs a bounded-lift condition, absent here | MT-M34 (with MT-M31, MT-M32, MT-M35) | statement checked on the page; the core lemma checked; the identification of the source spaces (MT-M31/M32) statement level |
| (11.3.2.2), p. 495, with (12.2.1.2), p. 505, and (12.2.2.2), p. 508 | the orbital indentation is identically zero under the draft's own measure conventions (Def A.2.3.6, p. 549; Def A.3.2.1, pp. 559-560), so the normalization fails and the lifted kernel is zero | the indicator of the fundamental domain R>0 × Ẑ^× for Q; normalized compact projections; genuine Q^× indentations. A single compatible nonnegative indentation is excluded as a repair (MT-M37) | ALPOGE_BRIDGES F-SM-19, F-SM-20; GRH_NIGHT MT-M36, MT-M37 | checked on the page; found independently by the two runs |
| §12.3-§12.4, Theorem 12.4.1.1, pp. 514-519 | **Updated 21 Nov from MAS_ARTIN checkpoint 02.** The prime-carrying intertwiner is built in Meyer's common space (MA-MEY-001 to 003). Under the interior premise (all zeros in the open narrow strip) the operator transport gives the draft's identity as lim Tr(M_ρ C_g P_G) = A₀(h) + B(h) − P(h) (MA-HM-004). The remaining "full narrow return" (factorization through the narrow completion for every width and every test with g(0) = 0) is **equivalent to RH** for the function concerned, because the narrow completion annihilates every exterior zero-jet block (MA-HM-003) | the route needs an independent narrow-return estimate, a translation bound on the narrow completion obtained without zero location, which by Weil's criterion is a positivity statement; none is located in the draft | MAS_ARTIN MA-MEY-001-003, MA-HM-003, MA-HM-004; the earlier F-SM-21, F-SM-22, MT-M33 | MA-HM-003 checked in full by us; the rest statement level |
| p. 500, before (12.1.1.7) | P_m is the projector onto a single singular-value eigenspace, and the text asserts P_m T P_m → T in 𝒮_p (p = 1, 2); the individual projectors do not exhaust T | the cumulative sums Σ_{m≤N} P_m T P_m → T, which is what the next paragraph uses | MAS_ARTIN MA-POS-004 | checked by us on the PDF text layer |
| Thm 5.3.2.1(1), p. 243; Def 5.3.4.1, p. 259 | an outer cutoff does not map into the stated codomain 𝒮₀₀ | — | MAS_ARTIN MA-LA-002 | statement level |
| (12.4.1.5)-(12.4.1.7) | false intermediate equalities, with a limited cancellation; annular limits depend on the path, also for thin boundary smoothings; centered and uncentered orbital sums differ | the relative cutoff rate and the full class of compact h with h(1) = 0 | MAS_ARTIN MA-LA-001, 003, 004, 005, 007 | statement level |
| Lemma C.3.2.2, pp. 695-696 | valid as stated; it needs a nuclear lift A₀ through the injection, and range inclusion alone is not enough | — | MAS_ARTIN MA-LA-006 | statement level |
| positivity, whole draft | no identified use of faithful full-jet positivity, so the MT-M20/M23 obstruction does not hit an identified step; the single-square observation of §1.7.2, p. 35, is verified and extended | — | MAS_ARTIN MA-POS-001 to 003 | statement level |

> Earlier text of the §12.3-§12.4 row (kept, 21 Nov): "with h(2) = 1 and A₀(h) = P(h) = 0, the global zero trace is
> log 2/√2 while the unchanged S = {∞} local trace limit is 0, so no trace-preserving transport of the unchanged kernel
> works; a multiplicative compact Dirac replacement is not compact; narrow Euler transport vanishes off the Euler line |
> **open:** a global-to-local intertwiner that carries the prime contributions | F-SM-21, F-SM-22, MT-M33; open rows
> R-MAS-KERNEL (ALPOGE_BRIDGES) and Q-MAS-GEOMETRIC-NARROW (GRH_NIGHT) | statement level".
| Theorem 13.3.1.2, p. 522 | a heading with no statement; the footnote reads "Insert statement" | M is cited from §1.2-§1.2.3, pp. 12-16 | CX_GRH, ALPOGE_BRIDGES, AN_GRH, ZETA_TWO | checked by the runs on the page |

**Further proved facts about the framework** (statement level unless marked):
- **MT-M20 (checked in full by us, given MT-M18/M19):** a faithful positive-definite Hilbert completion of the full
  zero-jet quotient, on which every C_{h∗h♯} is positive, exists iff GRH holds and every zero is simple.
- **MT-M23 (checked):** for every nonabelian Galois L/K, ζ_L has infinitely many multiple zeros (Hu-Kaneko-Martin-
  Schildkraut, Thm 1.1), so no such completion exists for ζ_L. Scalar trace positivity (MT-M19, under GRH) survives.
- **MT-M21, M22, M24:** the draft's smooth quotient is Meyer's zeta-summation quotient (Meyer, Duke 2005;
  arXiv:math/0311468).
- **MT-M26-M28:** trace class on fixed-character strips and on full adelic wide strips (unconditional), and on every
  positive-width narrow strip (under M).
- **F-SM-13:** the numerical statement of Theorem 12.5.1.1, pp. 519-520, holds for Q and every allowed test function,
  from Alpöge's theorem.

**Summary (updated 21 Nov from MAS_ARTIN checkpoint 02).** The analytic infrastructure of Chapters 9-12 contains several literal errors, each repairable and largely repaired. The prime-carrying operator transport is now built, and gives the explicit formula as an operator trace identity on narrow strips under the zero-location premise. The step that would turn this into zero location, the full narrow return, is equivalent to RH itself (MAS_ARTIN MA-HM-003). No independent narrow-return input is located in the draft. Nothing found refutes the draft's main claim; its central step, as reconstructed, carries no independent leverage on where the zeros are.

> Earlier summary (kept): "The central geometric trace identity, the narrow-strip equality of the geometric side with the spectral side for compact tests vanishing at norm one, proved without using where the zeros are, is the open gate. Nothing found refutes the draft's main claim."
