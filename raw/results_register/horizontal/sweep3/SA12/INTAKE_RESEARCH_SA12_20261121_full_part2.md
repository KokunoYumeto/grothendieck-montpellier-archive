# Full intake of RESEARCH_SA12, part 2 (ids 220-438 of the ledger list)

Intake by agent a3c8d7ded052a745e, Claude Opus 5.5 at effort max (in sweep 3 the SA12 reader B, who read cote 29
scans 141-217). Started 21 Nov 2026, 23:49 UTC, at the coordinator's word (the user, 21 Nov ~23:5x UTC: [the user's words, omitted]). The run: RESEARCH_SA12, GPT-6 Astra (ChatGPT Pro mode), final return of 20 Nov 23:10 UTC (it opens
"INCOMPLETE": the two-review stopping rule ended it; 603 pages, 487 register rows).

- **Return:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped`.
- **My list:** the 219 ids 220-438 of `field_experts/INTAKE_LEDGER.md` section 9, row RESEARCH_SA12 (218 rows of part D,
  "D:fixed-boundary-uniform-different" to "D:wild-units", and L6b). Reader A (a203d72b) takes ids 1-219.
- **Earlier intake:** `INTAKE_RESEARCH_SA12_20261120.md` (checkpoint 23; it read 11 part-D rows with proofs, none of mine).
- **Method.** For each id: the register row and the labelled statement with the proof that follows it in the cited
  source file (extracted by a work script, `extract.py`, run with python -I -B from my work folder, never inside the
  return). The check type is stated plainly per row: targeted proof check, independent re-proof, computation, carried as
  background without fault found (known results), or "statement read only" where I did not check the proof.
- **Events:** `INTAKE_RESEARCH_SA12_20261121_full_part2_CHECK_EVENTS.tsv` (statement_id, date, who, type, outcome).
- **Work file:** `agent_notes/a3c8d7ded052a745e_NOTES.md`.
- **Times.** The section headings give the UTC times at which the rows' events were written, taken from my
  transcript and the file times (clock read 22 Nov 00:27 UTC). Headings written before that read carried estimated times
  ahead of the clock (up to "10:30 UTC"); they were corrected on 22 Nov at about 00:35 UTC.

## 1. Rows, in the order of the list

### 1.1 Rows 220-253, with 314, 325, 377, 384, 385, 391 (read with their proofs; events written 21 Nov 23:52 - 22 Nov 00:02 UTC)

All these rows were read with their proofs in the cited source file. "Rests on" names rows of the run that the proof
uses and that I did not re-check at that row (mine are checked at their own row numbers).

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 220 | D:fixed-boundary-uniform-different | proved | tame horizontal different e-1, R_hor.f^*A <= nD.A, added to the projection identity | confirmed |
| 385 | D:surface-uniform-different | proved | M-matrix A, projection identity (D.UB.9), adjunction bound (D.UB.8), Galois conjugacy | confirmed (independent re-proof) |
| 384 | D:surface-uniform-conductor | proved | (D.UB.10) plus the tube lemma c <= 2M | confirmed; (D.UB.12) rests on (D.PG.1), row 365 |
| 221 | D:fixed-determinant-finite-Hom | proved u.s.h. | the four perturbation identities from (D.FH.5)-(D.FH.6) and h delta h = 0; Hom terms give (D.FH.3) | confirmed (independent re-proof) |
| 222 | D:fixed-different-unbounded-rational-chain | refuted (a proposed bound) | uv = y^N in char 2, A_{2m}, e = 1, delta = 1, chain of 2m (-2)-curves | confirmed (independent re-proof) |
| 223 | D:fixed-elliptic-cone-unitary-geometric-periods | proved u.s.h. | matrix identities, determinants, injectivity, symbol algebra of exact order m | confirmed; rests on D:elliptic-cone-Heisenberg-covers |
| 224 | D:fixed-formal-curve-fibre-bound | proved | Eisenstein lifts, Beauville-Laszlo at every level, common discriminant, transposition count | confirmed |
| 225 | D:fixed-henselian-algebraization | known | Artin 1969; the normal-domain deductions | background, no fault |
| 226 | D:fixed-local-quotient-alternating-count | proved u.s.h. | l-adic H^1 bound, pronilpotent generation, count (D.LQ.7)-(D.LQ.8) | confirmed; rests on rows 290, 293 and D:finite-puncture-local-orbit-factorial-count |
| 227 | D:fixed-partial-resolution-unit-atlas | proved u.s.h. | rank-one splitting, (D.FR.6) degree windows, composition and identity witnesses | homological core confirmed; slope bookkeeping rests on 8 rows |
| 228 | D:fixed-tensor-boundary-comparison | proved | I_P kills kernel and cokernel (contraction identity) | first assertion confirmed; Kummer-chart part rests on D:tame-boundary-summed-index |
| 229 | D:fixed-vs-valuation | proved | char 2 involution of P1xP1, blow-up chart, invariant field, e = 1 with inseparable residue degree 2 | confirmed (independent re-proof) |
| 230, 231 | D:formal-cone-fixed-boundary, D:formal-cone-mixed-boundary | proved u.s.h. | partial resolution to a Q-factorial projective surface, tameness at new curves, projective case; d > max(0,4g-4) | reduction confirmed; rests on rows 253, 272-273, 306-307, 349 |
| 232 | D:formal-retraction-cone-cover | proved u.s.h. | linearization obstructions in N^(1-n), Frobenius base change | confirmed (independent re-proof) |
| 233 | D:formal-retraction-tame | proved u.s.h. | pullback to the section cone, purely inseparable descent of tameness | confirmed; rests on row 253 |
| 234 | D:formal-torus-lift | proved | k^* acts trivially on the finite H^1(U,G); Hopf flatness; torsor E -> G_m | confirmed (two cited inputs) |
| 253 | D:graded-cone-tame | proved | weight decomposition, e = n/g prime to p, residue extension a finite-group fixed field | confirmed |
| 235 | D:full-bundle-cycle-degree | proved u.s.h. | Hartogs injectivity, h^1 bound, Riemann-Roch | confirmed given (D.OC.2) |
| 236 | D:full-order-scaled-separability | proved u.s.h. | Casimir, J kills the supported defect, chart rescaling | confirmed (independent re-proof) |
| 237 | D:generated-Morita-unit-Isom-openness | proved u.s.h. | contraction S = u^d T, intrinsic jet equations, openness | mechanism confirmed; inputs from other rows |
| 238 | D:generated-fixed-determinant-unit-openness | proved u.s.h. | determinant ratio a unit, adjugate pole bound, etale Isom, clopen classes | confirmed; rests on D:intrinsic-integral-unit-Hom-jets |
| 239 | D:generic-fibre-generation | proved u.s.h. | e(b'/b) divides m_E e_E; bounded inertia images; proper or tame curve | confirmed |
| 240 | D:generic-surface-controlled-boundary | proved | point-image exceptional divisors give isolated points; transversality and Abhyankar | confirmed; rests on row 241 |
| 241 | D:generic-surface-finite-punctures | proved | finite-cover Bertini with a fixed geometric generic tower | confirmed (Stacks lemmas cited) |
| 314 | D:normal-finite-puncture-quantitative-transfer | proved | degree-one inflation and precomposition injective | confirmed |
| 242 | D:generically-finite-projective-target | proved u.s.h. | Stein factorization to a projective normal target | confirmed (independent re-proof) |
| 243 | D:global-arbitrary-quotient-symplectic-orthogonal-crowns | proved u.s.h. | period two from the multiplier; exponent arithmetic | confirmed; rests on row 245 |
| 244 | D:global-finite-puncture-hereditary-bounded-local-period | proved u.s.h. | different transitivity, wild Riemann-Hurwitz, factor product | curve side confirmed; rests on two rows outside my list |
| 245 | D:global-finite-puncture-hereditary-semilinear-local-period | proved u.s.h. | as 244; obstruction killed by r and q-1 | as 244 |
| 246 | D:global-finite-puncture-projective-growth | proved | detector curve, local types, injective precomposition | mechanism confirmed; rests on the complete-local SNC count |
| 249 | D:global-projective-finite-puncture-closure | proved | finite proper descent count |P|^a | confirmed |
| 252 | D:global-unrestricted-projective-simple-products | proved | m_S <= |S|^(C kappa), LMT, Goursat | confirmed |
| 391 | D:tame-detecting-curve-local-pairs | proved | DVR extension keeps tameness; three local sources | confirmed; breaks rest on row 376 (D:surface-curvewise-conductor) |
| 247, 251 | D:global-original-boundary-projective-growth, D:global-tame-projective-controlled-closure | proved | as 246 with divisorial local pairs; transfer | confirmed; rest on row 286 |
| 248 | D:global-periodic-reflexive-boundedness | proved | Frobenius scaling, exceptional c_1, mu_max bound | confirmed given Langer (cited) |
| 377 | D:surface-fixed-rank-representation-growth | proved | Lang on End(E), Bezout on f-cycles | confirmed |
| 250 | D:global-quadratic-representation-bound | proved | O(f r^2)-equation witness scheme, clopen classes, D^m components | mechanism confirmed |
| 325 | D:polynomial-monad-diagrams | proved | perturbation lemma as in 221 | confirmed |

No error found in these 40 rows. Two observations for the record:
- **D:graded-cone-tame (253) with D:formal-torus-lift (234)** is the engine of every tameness result at exceptional
  curves in part D: every finite cover of the punctured completed graded surface cone, in any characteristic p, is
  tame at the radial valuation. The proof is short and complete given Gabber's finiteness of H^1(U,G) for the
  punctured spectrum (ILO XXI) and Hopf-algebra flatness. A literature search is needed before calling it new.
- **D:global-quadratic-representation-bound (250)**: q^{C r^2} for GL_r(F_q) local systems on a punctured normal
  proper surface in the defining characteristic, by counting irreducible components of an O(f r^2)-equation witness
  scheme. It feeds every crown-multiplicity estimate of part D.

### 1.2 Rows 254-263, with 266, 270, 351, 421 (read with their proofs; 22 Nov, 00:02-00:05 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 255 | D:hereditary-Cartier-parameter-jets | proved | (x^b,y^b) = O(-bC) from local generators; C^2 = tC_0^2; adjunction bound (D.HC.4) | confirmed; (D.HC.3), (D.HC.5) quoted from D:canonical-module-two-level-recovery |
| 254 | D:hereditary-Cartier-generation-budget | proved u.s.h. | subcycle inequality stable under point blowups (p_a(rho^*B_0-kE) = p_a(B_0)-k(k-1)/2); Cauchy-Schwarz; Frobenius cycling x_a <= rp(-C^2)/(p-1) | confirmed |
| 256 | D:hereditary-base-generation | proved u.s.h. | only the final step used projectivity; H(B) replaces it | confirmed; rests on row 331 |
| 270 | D:iterated-fibration-generation | proved u.s.h. | Stein factorization, generic projectivity under finite covers, purely inseparable base change, radicial pullback | confirmed; rests on row 331 |
| 266 | D:intrinsic-Hom-fixed-loss-jets | proved | pencil sequence, J kills H^1(O(-jC)), x^l and y^l kill H^1(H((d-k)C)), lifting (D.HJ.3) | confirmed (independent re-proof) |
| 257 | D:hereditary-canonical-Hom-arrow-window | proved | exponents (1,1), (p,1), (1,p) in 266 | confirmed |
| 351 | D:reflexive-pullback-uniform-generation | proved | automatic adjunction: deg_B L <= 2p_a(B)-1; criterion via 2p_a = 2 + kappa.m + B^2 and even (-2)-lattices | confirmed (CFHR lemma cited) |
| 258 | D:hereditary-fixed-determinant-cycle-chart | proved | -C^2 <= n(-C_0^2); Cauchy-Schwarz; Frobenius cycling; r+1-section chart | confirmed |
| 259 | D:hereditary-generation-cycle-Hom-budget | proved u.s.h. | cycling with W; h^1(O_bW) <= p_g; chi(O_bW) | confirmed |
| 260 | D:hereditary-ordinary-unit-determinants | proved u.s.h. | |H^1(U_A,mu_n)| <= n^(2p_g+v) via purity and 2 sum g + b_1 <= 2h^1(O_E); multidegree count | confirmed |
| 261 | D:hereditary-ordinary-unit-finite-cycle-Hom | proved u.s.h. | section bounds and the perturbation transfer of 221 | confirmed |
| 421 | D:weak-cycle-Artinian-full-realization | proved | weak hypotheses re-checked at each use: induction on H^1(O_Z(-jZ)), Hartogs from injective boundaries | confirmed; base theorem cited |
| 262 | D:hereditary-weak-cycle-relative-realization | proved | W satisfies (D.WR.1) from uniform generation and H^2 = 0 | confirmed |
| 263 | D:hereditary-wreath-permutation-count | proved u.s.h. | Hom bound, nonabelian Shapiro, tower sums with T_i m_i <= N | confirmed; rests on D:arbitrary-cover-ordinary-hereditary-growth |

No error found in these 14 rows.

### 1.3 Rows 264-289 so far, with 339, 361, 380 (read with their proofs; 22 Nov, 00:05-00:09 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 285 | D:local-divisor-tame-central-H2 | proved | Leray terms n^v, n^(2 sum g), n^(e+h); Cartan-Leray; inflation injective since Hom(N, mu_n) = 0 | confirmed (independent re-proof) |
| 264 | D:horizontal-residue-order-at-node | proved | D'_a = Spec k[[z]]; Kummer theory and Hensel | confirmed (independent re-proof) |
| 265 | D:integral-antinef-energy-cycle | proved | lattice minimizer, repair at -1 entries, propagation, rounding bound B/2, Q <= 2c^2 E + B | confirmed (independent re-proof) |
| 339 | D:punctured-cover-antinef-cycle | proved | (D.IC.1) on the minimal resolution; chi(O_tD) | confirmed; rests on row 340 |
| 267 | D:intrinsic-integral-unit-Hom-jets | proved u.s.h. | contraction j -> pj-c, pN-c > N, uniqueness, finite presentation | confirmed |
| 269 | D:intrinsic-small-linear-permutation-images | proved | subgroups generated by log_2 M elements; pair count; arithmetic | confirmed (independent re-proof) |
| 268 | D:intrinsic-linear-orbit-alternating-count | proved u.s.h. | (D.IM.1) for each source; polylogarithmic D_N | confirmed; rests on two alternating theorems |
| 271 | D:klt-threefold-boundary | proved u.s.h. | finite local images (Carvajal-Rojas-Stabler, Theorem A) and the tower argument | confirmed (published input cited) |
| 275 | D:lc-exceptional-configurations | proved | discrepancy identities, cycle sum, nodality | confirmed; the known lc classification re-proved in every characteristic |
| 273 | D:lc-cusp-tame | proved | cover is lc; nonzero image in pi_1(E) = Z^ forces a cyclic core with discrepancy -1; delta = e-1 | confirmed |
| 272 | D:lc-core-valuative-tame | proved | componentwise tameness and Kummer persistence | confirmed |
| 274 | D:lc-elliptic-tame | proved | d(us^e)^dz computation; discrepancy -1 on positive genus; delta = e-1 | confirmed (independent re-proof) |
| 361 | D:schroer-elliptic | proved | discrepancy -1 on R_i; D.B = D.R_0 = D.R_1 = 1 recomputed; pi_1(U) = Q(T,T-U) | confirmed |
| 380 | D:surface-mixed-boundary | proved u.s.h. | Q-factorial projective partial resolution (re-derived); tameness at new curves | confirmed; rests on rows 365, 273 |
| 276 | D:lc-surface-boundary | proved | char 0 / char p cases; finite proper descent | confirmed |
| 277 | D:linear-SNC-refinement-centres | proved u.s.h. | genus drop per centre, low chains of length <= 2, root count | confirmed (independent re-proof) |
| 281 | D:local-Picard-prime-to-p-generators | proved | Pic(Y) ->> Pic(E), injective mod n, Pic(E)/n = (Z/n)^b | confirmed |
| 289 | D:local-fixed-tensor-cyclic-atlas | proved | non-MCM source lifting, image bound, Nakayama, twisted Lang, Bezout | mechanism confirmed |
| 278 | D:local-Brauer-zero-projective-growth | proved | root gerbe of fixed generators; floor recurrence into a fixed alphabet | mechanism confirmed |

No error found in these rows.

### 1.4 Rows 279-295, with 342, 373, 411 (read with their proofs; 22 Nov, 00:09-00:12 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 279 | D:local-Brauer-zero-surface-transfer | proved | connectedness of the slice (Grothendieck), descent fibres <= |G|^a | confirmed; rests on row 278 |
| 280 | D:local-Eisenstein-linear-atlas | proved | derivative weights with distinct residues mod e, truncation eN > 2d, factorial-free Newton | confirmed |
| 284 | D:local-branch-data-linear-complexity | proved | products of 280 charts | confirmed |
| 282 | D:local-bounded-central-obstructions | proved | finitely many classes, cocycles factor through finite quotients | confirmed (independent re-proof) |
| 373 | D:strict-local-open-cohomology-finite | proved | constructibility of R^q j_* (Gabber); sections = closed stalk | confirmed |
| 283 | D:local-bounded-scalar-simple-product | proved | open normal subgroups are punctured complete local domains | hypothesis check confirmed; rests on D:bounded-scalar-projective-growth |
| 291 | D:local-pair-coefficient-root-comparison | proved | residue orders: h_a divides m_i(a) by reciprocity at the node; per = lcm m_i | residue part confirmed; gerbe identification read |
| 292 | D:local-pair-unbounded-horizontal-root-atlas | proved | spectral Riemann-Hurwitz; horizontal points as marks | statement read, proof partly checked |
| 286 | D:local-divisorial-tame-projective-growth | proved | assembly: classes x tuples x allocations x weighted components, sum b_i J_i = O(f r^2) | confirmed; rests on rows 292, 423 |
| 287 | D:local-field-character-crossed-H1 | proved u.s.h. | cyclic cohomology vanishing, five-term sequence, Kummer | confirmed (independent re-proof) |
| 288 | D:local-fixed-rank-representation-growth | proved | specialization of row 410 | confirmed |
| 290 | D:local-p-linear-H1 | proved | Artin-Schreier into H^(F=1); socle; Matlis duality; test ideal (cited) | confirmed |
| 411 | D:unit-reflexive-linear-cohomology | proved | mu_max(F) <= 0, dual bound, h^0 <= r, h^2 by duality, h^1 by Riemann-Roch (cited) | confirmed |
| 342 | D:punctured-surface-all-characteristics-H1 | proved | Leray with j_*M the fixed sheaf; local bound; descent; Shapiro; crown criterion | confirmed; prime-to-p part rests on row 376 |
| 293 | D:local-permutation-orbit-energy | proved u.s.h. | permutation embedding and composition count | confirmed (independent re-proof) |
| 294 | D:local-purity-boundary | proved u.s.h. | generic point of the branch locus and local purity | confirmed (independent re-proof) |
| 295 | D:local-reflexive-constructible-atlas | proved | windows, uniform poles, (J3) by Serre duality, lifting | key steps confirmed |

No error found in these rows.

### 1.5 Rows 296-308, with 317, 337, 378, 403, 432 (read with their proofs; 22 Nov, 00:12-00:14 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 296 | D:local-surface-reduction | proved | connected slice; free-product descent with dense image | confirmed |
| 297 | D:local-tame-p-linear-H1 | proved | uniform Jacobian test ideal for all Kummer covers R_n; one n for all classes | new steps confirmed |
| 298 | D:log-fibration-criterion | proved u.s.h. | Hoshi's log homotopy sequence (cited); index argument as in 239 | confirmed |
| 378 | D:surface-map-all-boundaries | proved | Stein factorization, purely inseparable base change, row 298 | reduction confirmed; rests on row 379 |
| 337 | D:proper-log-finite-generation | proved | valuative tameness of Kummer etale covers; AHLS 2026 Th. 3.5.1 | background (unrefereed input, not opened) |
| 299 | D:log-regular-boundary | proved | Hoshi's comparison and row 337 | confirmed given 337 |
| 300 | D:meromorphic-unit-jet-contraction | proved | t -> pt-2b contraction; uniqueness; inverse products | confirmed (independent re-proof) |
| 317 | D:one-curve-coefficient-root-gerbe | proved | (D.UJ.2) by the Gysin sequence: gcd(n,d) n^(2g) | formula confirmed; gerbe/anchor construction read |
| 301 | D:mixed-fixed-boundary | proved u.s.h. | as 230 for arbitrary Y | confirmed |
| 303 | D:mutation-surfaces | proved | full inertia at each b_i dies along the horizontal strict transform | confirmed (independent re-proof) |
| 403 | D:torsion-first-obstruction-cover | proved u.s.h. | Frobenius and Artin-Schreier torsors kill the class; genus formula | confirmed (independent re-proof) |
| 304 | D:negative-curve-equality-finite-wild | proved u.s.h. | degrees qs(n-1)d > 2g(C')-2; a = -2 gives torsion | confirmed |
| 432 | D:wild-genus2-finite-inertia | proved u.s.h. | divisors on w^2+w=z^5, N = omega^-1, F^2 = 0 on H^1(O), degrees 8(n-1) | confirmed |
| 306 | D:negative-curve-linearization | proved u.s.h. | torsors of lifts, obstruction group (O), graded isomorphism, (N) | confirmed (independent re-proof) |
| 305 | D:negative-curve-finite-wild | proved u.s.h. | pulled-back obstruction degrees under (Q) | confirmed |
| 307 | D:negative-curve-tame | proved u.s.h. | rows 306 and 253 | confirmed |
| 308 | D:nominal-orbits | proved | least supports via transpositions; orbit form; finite fixed sets | confirmed (independent re-proof) |

No error found in these rows.

### 1.6 Rows 302, 309-316, 321, 326, 330 (22 Nov, 00:14-00:16 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 302 | D:moving-line-polynomial-background | proved u.s.h. | plane-model step (very ample aH, primitive element, degree bounds) | statement read, proof partly checked |
| 309 | D:non-natural-alternating-primitive-models | proved u.s.h. | (m l)^2 <= 4N; c_0 = 64; trivial socle centralizer | key bounds confirmed; catalogue cited |
| 310 | D:nonnormal-bounded-centre-projective-growth | proved | PSL homomorphisms inject into PGL-torsor classes; descent | confirmed |
| 311 | D:nonnormal-controlled-boundary-quantitative-transfer | proved | transfer via row 240 and descent | confirmed |
| 312 | D:nonnormal-finite-puncture-quantitative-transfer | proved | normalization descent; rows 241, 314 | confirmed |
| 313 | D:nonsplit-automorphism-wreath-lifts | proved | monolithic embedding; crown bound from the bijection | statement read, proof partly checked |
| 315 | D:normal-subgroup-projective-crowns | proved u.s.h. | - | statement read only |
| 316 | D:normalization-Frobenius-saturation | proved | trace-dual Frobenius bases, pi^M B in A.B^q | confirmed (independent re-proof) |
| 321 | D:one-variable-residue-primitive | proved | p-rank one; primitive v with dv != 0 | confirmed (independent re-proof) |
| 326 | D:prime-to-p-index-boundary | proved | reduction to row 327 and Carvajal-Rojas-Yasuda | confirmed |
| 330 | D:projective-generic-normalization | proved | as row 378 with row 239 (2) | confirmed |

No error found in these rows.

### 1.7 Rows 318-320, 327 (22 Nov, 00:16-00:17 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 318 | D:one-curve-radial-tame-generators | proved | extension of Gal(C'/C) by cyclic inertia; 2u(g-1)+3 <= (2g+3)u | confirmed |
| 327 | D:prime-to-p-index-tame | proved u.s.h. | index-one cover Gorenstein lc; discrepancy formula | structure confirmed |
| 320 | D:one-curve-wild-swap-cover | proved (an obstruction example) | Sym^2 C in char 2: e = 1, residue k(x)/k(x^2), D^2 = 1-g | confirmed (independent re-proof) |
| 319 | D:one-curve-unbounded-period-projective-count | proved | coefficient classes <= d q^(2g) | statement read, proof partly checked |

No error found in these rows.

### 1.8 Rows 332-336: Proposition 5 of 29/197 and two obstructions (22 Nov, 00:17-00:18 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 333 | D:prop5 | proved | R1-R4 at one level, common level by quasi-compactness of B, reconstruction under local generation | confirmed; agrees with my sweep-3 reading of 29/191-197 (c29b_c31.md item 12) |
| 335 | D:prop5-counterexample | refuted (the unqualified construction) | chain of lines over A^1, E_n of degree 2 over D(t), descent datum needing every level | confirmed (independent re-proof); Prop. 5 itself is unwritten on 29/197 |
| 334 | D:prop5-completion | proved | open-closed finite-fibre realization map gives clopen B_J neighbourhoods | key step confirmed |
| 332 | D:pronilpotent-obstruction | proved (an obstruction) | small, not finitely generated, finite pronilpotent quotients | confirmed (independent re-proof) |
| 336 | D:proper-curve-arithmetic-defect | proved | trace discriminant degree, normalization, Riemann-Hurwitz | confirmed (independent re-proof) |

No error found in these rows. Rows 333-335 settle what the manuscript left as "Prop 5 ....." on 29/197: the
filtered reconstruction needs quasi-compactness of the realization base (or clopen descent), and the leaves' warning
that the stack need not be generated by global sections is exactly the gap.

### 1.9 Rows 323, 324, 328, 329, 354 (22 Nov, 00:18-00:19 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 324 | D:persistent-first-neighborhood | proved (an obstruction to the finite-cone method) | sufficient condition = Tango's injectivity criterion | statement read, proof partly checked (rests on Brenner, cited) |
| 323 | D:permutation-matrix-model-count | proved | models times Hom counts under (D.MO.2) | counting confirmed |
| 328 | D:primitive-defining-characteristic-orbit-models | proved | (D.PM.2) from row 269 with D = O(log^2 N) | statement read, proof partly checked |
| 354 | D:residual-inseparability-bound | proved | separable base change argument | confirmed (independent re-proof) |
| 329 | D:projective-base-generation | proved u.s.h. | fibre image N; quotient of Gal(F) | statement read, proof partly checked (to be completed) |

No error found in these rows.

### 1.10 Rows 331, 340, 357, 369, 370 (22 Nov, 00:19-00:20 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 331 | D:projective-image-corollaries | proved | Stein factor, radicial base change, row 329 | reduction confirmed; rests on row 329 |
| 340 | D:punctured-cover-linear-energy | proved | contraction formulas E'^2 = E^2 + a^2, p_a + a(a-1)/2 | confirmed; rests on row 341 |
| 357 | D:root-stacks | proved | Cadman chart [W_a/H]; arrows t -> zeta t | confirmed; agrees with my sweep-3 reading of 29/200-201 |
| 369 | D:sparse-DVR-normalized-different-complexity | proved | cutoff 2 Lambda + 2; Bezout | confirmed |
| 370 | D:split-first-neighborhood-finite-wild | proved u.s.h. | jet cone with r = 2 | confirmed; rests on D:finite-jet-cone-cover |

No error found in these rows.

### 1.11 Rows 360, 363, 365, and an addendum to 384 (22 Nov, 00:20-00:21 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 360 | D:schroer-all-genera | proved u.s.h. | linear transition u = t/z: formal neighbourhood of R_i is the zero section of O_C(-c_1) | confirmed |
| 363 | D:single-curve-Cartier-module-jet-recovery | proved | setup on etale resolution covers | statement read, proof partly checked |
| 365 | D:single-curve-residue-tameness | proved | (D.PG.1) on the minimal Z: projection identity, -e_i F_i^2 >= d f_i, Riemann-Hurwitz on the separable part | confirmed (independent re-proof) |
| 384 | D:surface-uniform-conductor (addendum) | proved | (D.UB.12) from (D.PG.1) by Galois conjugacy | now fully confirmed |

No error found in these rows.

### 1.12 Rows 343, 346, 349, 362 (22 Nov, 00:21-00:23 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 343 | D:pure-root-rational-tail-obstruction | refuted (an inference: rational tails need not be fillable) | char 2: z^2 = t+x^3, cusp C', chart t = s^2(y^2+s); Artin-Schreier u^2+u = 1/t pulls back with v^2+v = (1+y^3+sy)/(s y^2 (y^2+s)), wild e = 2 along R | confirmed (independent re-proof) |
| 346 | D:radial-tame-cover-one-curve | proved | Abhyankar models; (h^*C)^2 = e^2 (C')^2 = tC^2 | confirmed |
| 349 | D:rational-tree-Qfactorial | proved u.s.h. | Z by the M-matrix argument; Pic injectivity on thickenings; p^a-torsion of 1+I; det M multidegree correction | mechanism confirmed; final descent to the local ring not read |
| 362 | D:single-curve-Brauer-residue-cover | proved | Pic(U)/n = Z/gcd(n,d) and the Gysin count give n^(2g); etale splitting cover of degree m | confirmed |

No error found in rows 346, 349 and 362; row 343 is the run's own refutation, confirmed.

### 1.13 Rows 322, 338, 341, 344, 345, 347, 348, 350, 352, 353 (22 Nov, 00:27-00:37 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 322 | D:original-boundary-matrix-alternating-count | proved u.s.h. | local inputs (faithful diag(A,1), permutation matrices); H^1 bound (D.OBM.8) by Leray; uniform-l Frattini; injectivity on finite sets | confirmed; the global count rests on row 391 and two rows outside my list |
| 338 | D:psl2-bounded-conductor-covers | proved | invariant J_q, degree, stabilizers, lower numbering G_1 = F_q, G_2 = 1, normalizer, Goursat | confirmed (independent re-proof) |
| 341 | D:punctured-cover-linear-resolution | proved | d/e monotone in towers; maximum principle; A_(N-1) Jacobian: delta >= floor(N/2); chain sum 93 lambda nc | confirmed; the counts rest on row 424 |
| 344 | D:quadratic-cyclic-Frobenius-witnesses | proved | (x^p, y^p) kills coker(F^*M -> F^[*]M); witness effectivity by Nakayama | confirmed |
| 345 | D:quadratic-growth-alternating-obstruction | proved | dimension bound n <= 8a; Ext^1 <= 2 dim U dim V; counts (A5)-(A6), (A2); m_n = 2^(n^2) > \|A_n\|^s | confirmed (independent re-proof) |
| 347 | D:radial-tame-cyclic-H2 | proved u.s.h. | tame stalks; Leray; curve bounds by the trace surjection; five-term injectivity | confirmed |
| 348 | D:rank-period-generating-root-anchor | proved u.s.h. | blowup symbol c(u,w); node algebra with m/h simples; multiplicity M/m; graph count | confirmed; two SNC lemmas outside my list used |
| 350 | D:reduction-cycle-full-module-correspondence | known (Kahn, Gavran) | (D.KR.8)-(D.KR.11), existence, uniqueness, tangent comparison; the duality step read | reconstruction confirmed |
| 352 | D:relative-Artin-module-realization | proved | Tor vanishing; ADS lifting (cited); idempotent lifting and conjugacy | confirmed |
| 353 | D:relative-Noether-different-jets | proved | factorization through R (x)_S M; jet lifting; colon (L1) | confirmed (independent re-proof) |

No error found in these rows.

### 1.14 Rows 355, 356, 358, 359, 364, 366, 367, 368 (22 Nov, 00:37-00:40 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 355 | D:residual-twisted-Frobenius-transport | proved u.s.h. | deg B_a = p delta_a - delta_(a+1) in {0..p-1}; Frobenius and etale pushforward; the torsor-translation example (1+nj)(1+n) | confirmed (independent re-proof) |
| 356 | D:residual-twisted-spectral-category | proved | central extension of cyclic by cyclic is abelian; character torsor; H^2(curve, G_m) = 0; components n/m of degree m | confirmed (independent re-proof) |
| 358 | D:saturated-boundary-two-sided-slopes | proved | normalization at C_i meet Z by normality; carries c_j <= p-1; slope recursion around finite cycles | confirmed; windows from row 395 |
| 359 | D:scaled-separable-action-Newton | proved u.s.h. | identity (D.SN.11) by expansion; quadratic convergence N_j; exact averaging | confirmed (independent re-proof) |
| 364 | D:single-curve-Cartier-parameter-ideal | proved u.s.h. | ampleness; Chevalley's lemma; general pair generates; Omega_(K/k) of rank 2 gives separability | confirmed (independent re-proof) |
| 366 | D:single-sector-root-compression | proved u.s.h. | descent of End(A_u) (characters in a coset of hZ/n); offsets c + h l and carries | confirmed; algebraization via row 317 |
| 367 | D:skew-Morita-Frobenius-effectivity | proved u.s.h. | changes to a theorem outside my list: weights, invariance of x, y, C, error orders, a-fold iterate | changes confirmed; base theorem not rechecked |
| 368 | D:sparse-DVR-linear-atlas | proved | flatness of the box basis; Jacobian stratum; Newton; existence; isomorphism witnesses; counts | confirmed; degree bound read |

No error found in these rows.

### 1.15 Rows 371, 372, 374-376, 379, 381-383, 386-390 (22 Nov, 00:40-00:44 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 371 | D:stable-root-anchor-canonical-comparison | proved | (D.BA.5) z.lambda = sum lambda(v_i)u_i; trace self-duality; P-stable reflexive anchor; composition-trace pairing | confirmed |
| 372 | D:strict-Cartier-separating-parameters | proved u.s.h. | M-matrix minimizer positive; as row 364 with several components | confirmed (independent re-proof) |
| 374 | D:superperfect-quadratic-obstruction | proved | H_2(T_n) = 0; H^2(T_n,V) <= 5 dim V; tail cohomology; dim V >= n/6; counts; non-generation | confirmed (independent re-proof); (SP5) cited (GKKL) |
| 375 | D:surface-bounded-centre-simple-product | proved | order of PSL_r(q) >= q^(r^2/4); Q(S_H,T_H) ->> H | confirmed; rests on rows 383, 393 and one row outside my list |
| 376 | D:surface-curvewise-conductor | proved | surjection pi_1(V) ->> Q; uniform breaks from row 384; Hu-Teyssier cited | confirmed (cited theorems not opened) |
| 379 | D:surface-map-to-curve | proved | algebraic closedness and separability of K/F; flatness; U meets every fibre | confirmed; rests on row 420 |
| 381 | D:surface-residual-genus-bound | proved | adjunction bounds; Riemann-Hurwitz for the separable part | confirmed (independent re-proof) |
| 382 | D:surface-tame-central-obstructions | proved | multiplicativity along composition series; obstruction classes; H_B | confirmed (independent re-proof) |
| 383 | D:surface-tame-cross-characteristic-H2 | proved | inflation injective (pro-p N); Cartan-Leray; Leray for the resolution; Hu-Teyssier cited | confirmed (cited theorem not opened) |
| 386 | D:symplectic-orthogonal-simple-product | proved | scalar kernels; order of S >= q^(r^2/8) in all four rows | confirmed; rests on one row outside my list |
| 387 | D:tame-GLn | proved u.s.h. | eigenvector lifting by the projector; classification by character multiplicities | confirmed (independent re-proof) |
| 388 | D:tame-boundary-summed-index | proved | normality of R_n; h(x,0) != 0; x-denominators; diagonal lattice; index sum | confirmed; register lists the row as its own dependency |
| 389 | D:tame-canonical-Euler | proved | slope recursion of the character bundles; corrections via row 388 | confirmed; gluing at Sigma read |
| 390 | D:tame-canonical-linear-cohomology | proved | determinant, Riemann-Roch, chi(E) >= -Cr; slope bounds; h^0, h^2 | confirmed (independent re-proof); register lists the row as its own dependency |

No error found in these rows.

### 1.16 Rows 392-400: the tame counting theorems (22 Nov, 00:44-00:46 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 392 | D:tame-field-permutation-crowns | proved u.s.h. | crown arithmetic k <= order(A)^(c_R); generator bound | confirmed; count from row 400 |
| 393 | D:tame-global-quadratic-representation-bound | proved | local basis of L_c; canonical decomposition; count p^(C f r^2) | new steps confirmed; witness effectivity as in row 250 |
| 394 | D:tame-hereditary-projective-count | proved u.s.h. | Gysin count with d' = u delta/e; weighted component bound | confirmed; rests on rows 399, 423 |
| 395 | D:tame-parabolic-boundedness | proved | Chern-class cycling; ch_2 >= -Cr; slope bounds; finitely many Hilbert polynomials | confirmed; Langer cited |
| 396 | D:tame-parabolic-fixed-rank-growth | proved | weight recursion; edge criterion; Lang uniqueness; Bezout | confirmed |
| 397 | D:tame-projective-automorphism-crowns | proved u.s.h. | crown arithmetic | confirmed; count from row 398 |
| 398 | D:tame-projective-semilinear-count | proved u.s.h. | cover identities; obstruction count (row 347); factorial calculation | confirmed |
| 399 | D:tame-resolution-hereditary-linear-count | proved u.s.h. | twist by -heC'; thresholds in multiples of e; line lists; (D.TH.10) | confirmed |
| 400 | D:tame-resolution-semilinear-count | proved u.s.h. | inflation of determinant classes; Ev = ta absorbs the field order | confirmed; register lists the row as its own dependency |

No error found in these rows.

### 1.17 Rows 401, 402, 404-408 (22 Nov, 00:46-00:49 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 401 | D:tame-sufficient | known (SGA 7 XIII 2.1.10-11) | sketch read | background; citation not opened |
| 402 | D:tame-surface-all-characteristics-H1 | proved | Artin-Schreier-Lang sequence; F_p- versus k-dimension; local bounds at Sigma | confirmed |
| 404 | D:twisted-connected-anchor-minimal-slopes | proved u.s.h. | e(F') - e(F) = chi(Q); the inverse transform; slope window | confirmed (independent re-proof) |
| 405 | D:twisted-deck-Frobenius-semilinear-model | proved u.s.h. | T^d = F_q^*; fixed frames; semilinear descent | confirmed (independent re-proof); register lists the row as its own dependency |
| 406 | D:twisted-period-independent-normal-depth | proved u.s.h. | window width linear in m; Hom-layer thresholds; (D.TD.12) | confirmed; endpoints of (D.TD.14) not re-derived |
| 407 | D:uniform-H1-obstruction | proved | H^1 of products of perfect two-generated groups <= dim M; certificate rerun | confirmed (independent re-proof and computation) |
| 408 | D:uniform-comparable-reduction-cycle | proved u.s.h. | componentwise -Z.H; the three cases of (D.CR.13); budgets | confirmed (independent re-proof) |

No error found in these rows. The certificate of row 407 was rerun from a copy in my work folder: 2,803,802 assertions passed in 0.7 s.

### 1.18 Rows 409, 410, 412-420, 422, 423 (22 Nov, 00:49-00:52 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 409 | D:uniform-local-growth-all-dimensions | proved | free-product count with relative conjugations | confirmed (independent re-proof) |
| 410 | D:uniform-local-representation-growth | proved | Lang fixed vectors; Artinian constancy (L8); orbit and Krull argument; D^m components | confirmed |
| 412 | D:unitary-unbounded-scalar-obstruction | proved u.s.h. | Heisenberg pair in SU_m(q); cocycle zeta^(ba'); exact order m; explicit m | confirmed (independent re-proof) |
| 413 | D:unpointed-Eisenstein-witness | proved | b_00^e = 0; unpointed disc automorphisms; Newton | confirmed (independent re-proof) |
| 414 | D:unramified-field-permutation-crowns | proved u.s.h. | twisted Shapiro; crown arithmetic; monolithic primitive | confirmed; count from reader A's half |
| 415 | D:unramified-permutation-linear-crowns | proved u.s.h. | Shapiro bijection; normalizer multiplicity; crown arithmetic | confirmed; count from reader A's half |
| 416 | D:unramified-semilinear-determinant-budget | proved u.s.h. | purity, Leray, proper base change; 2g_t generators | confirmed (independent re-proof) |
| 417 | D:vertical-boundary-all-dimensions | proved | regular generic fibre in all dimensions; SGA 1 X 2.9; row 239 | confirmed |
| 418 | D:vertical-fibration-exact | proved u.s.h. | sections through f-smooth points over strictly henselian traits | confirmed (independent re-proof) |
| 419 | D:vertical-fibration-models | proved u.s.h. | birational surjectivity; finite proper descent | confirmed (independent re-proof) |
| 420 | D:vertical-fibration-multiplicity | proved u.s.h. | e(b'/b) divides m_b; finite inertia images; open subgroup argument | confirmed (independent re-proof) |
| 422 | D:weak-cycle-generated-determinant-lifting | proved u.s.h. | H^1 vanishing on layers; lifting sections and line isomorphisms | confirmed (independent re-proof) |
| 423 | D:weighted-affine-component-bound | proved u.s.h. | coordinate powering of rank prod w_i; system of parameters and hyperplanes | confirmed (independent re-proof); register lists the row as its own dependency |

No error found in these rows.

### 1.19 Rows 424-438 (22 Nov, 00:52-00:56 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 424 | D:weighted-exceptional-chain-compression | proved | ADE shape of noncore blocks; harmonic weights; constants 31, 93, 95 | confirmed (independent re-proof) |
| 425 | D:weighted-fixed-determinant-normal-presentation | proved u.s.h. | twist, generating presentation, Hom-layer sizes O(m s^2) | confirmed |
| 426 | D:weighted-fixed-residual-bundle-deformations | proved u.s.h. | two-chart gluing family; perturbation lemma; weighted degrees | confirmed; register lists the row as its own dependency |
| 427 | D:weighted-graded-boundary | proved u.s.h. | combination of row 428 with the mixed-boundary theorems | confirmed |
| 428 | D:weighted-graded-extraction | proved u.s.h. | O_C(-1) model; Eisenstein extension; toric charts; Q-factoriality by norms | confirmed |
| 429 | D:weighted-normal-layer-background-budget | proved u.s.h. | weighted component arithmetic with the background block | confirmed (independent re-proof) |
| 430 | D:weighted-normal-layer-budget | proved u.s.h. | weighted component arithmetic | confirmed (independent re-proof) |
| 431 | D:wild-GLn | refuted (wild GL_n comparison) | diagonal cocycles distinguished by determinant | refutation confirmed (independent re-proof) |
| 433 | D:wild-genus2-pro2 | proved | purity; nilpotent Frobenius on H^1(C',O) | confirmed; first step via row 365 |
| 434 | D:wild-genus2-single-curve | refuted (a single smooth curve need not be tame) | the example by hand, identity (I) expanded; certificate rerun (26 assertions) | example confirmed (independent re-proof and computation) |
| 435 | D:wild-genus2-source | proved | both source charts; (C')^2 = -2; Frobenius on C'; discrepancy -2 | confirmed (independent re-proof) |
| 436 | D:wild-swap-exact-image | proved u.s.h. | image of wild inertia of order exactly 2; d <= 2g+2 | confirmed |
| 437 | D:wild-units | refuted (wild unit comparison of 31/044) | norm t^p/(1 - t^(p-1)); Hilbert 90 | refutation confirmed (independent re-proof) |
| 438 | L6b | known with derivation | five-term sequence for the resolution | confirmed |

No error found in these rows. The three refuted rows (431, 434, 437) are the run's own refutations; each counterexample holds. I did not compare 431 and 437 with the scan 31/044 (I did not read cote 31 in sweep 3).

## 2. Counts by check type

Computed by `final_counts.py` (my work folder, python -I -B) from the events file: 225 events for all 219 ids of my list;
no id is missing. Six ids carry two events (343; 384, whose second event is the addendum of section 1.11; 315 and 329, read again in section 8; 407 and 434,
each an independent re-proof plus a computation).

| type | events | ids, by their strongest event |
|---|---|---|
| computation or formal certificate | 2 | 2 (407, 434; both also re-proved independently) |
| independent re-proof | 65 | 63 |
| targeted proof check | 145 | 144 |
| carried as background without fault found | 3 | 3 (225, 337, 401) |
| statement read, proof partly checked | 9 | 7 (292, 302, 313, 319, 324, 328, 363) |
| statement read only | 1 | 0 (315 was read in full in section 8) |

The two computations are reruns of the run's own certificates, from copies in my work folder, never inside the return:
`parts/D/code/check_uniform_h1_obstruction.py` (2,803,802 assertions, exit 0) and
`parts/B/code/check_wild_genus2_curve.py` (26 assertions, exit 0). The seven rows still read only partly are
listed for a later pass; 329 (D:projective-base-generation), on which rows 256, 270 and 331 rest, and 315 were completed in section 8.

## 3. Refutations

I found no error in any of the 219 rows and refuted nothing. The run marks six rows of my half "Refuted"; in each its
counterexample holds:

- 222 D:fixed-different-unbounded-rational-chain;
- 335 D:prop5-counterexample (with 333-334 it settles the unwritten Proposition 5 of 29/197, consistent with my sweep-3
  reading of that page);
- 343 D:pure-root-rational-tail-obstruction (the characteristic-2 cusp cover);
- 431 D:wild-GLn and 437 D:wild-units (the wild comparisons, through t -> t/(1+t) on k[[t]] in characteristic p; the
  run ties 437 to 31/044, which I did not read in sweep 3, so the comparison with the ink is not made here);
- 434 D:wild-genus2-single-curve (a single smooth genus-two exceptional curve with a wild quasi-etale double cover;
  identity (I) and both charts checked by hand, certificate rerun).

The run's further obstruction examples were also confirmed: D:pronilpotent-obstruction, D:one-curve-wild-swap-cover
with 436, D:fixed-vs-valuation, 345 and 374 (alternating and superperfect products), 407 (uniform H^1 without finite
generation), 412 (no uniform scalar exponent from unitary forms).

## 4. Corrections and errata

**In the run.** No mathematical error found. Register errata only: rows 388, 390, 400, 405, 423 and 426 list
themselves among their own dependencies (depends_on). In row 406 the endpoints of the window (D.TD.14) are written
with a Frobenius spread (p-1)gamma_m on each side; I did not re-derive that constant, and the proof uses only that the
width is linear in m, which any rank-independent Frobenius instability bound gives.

**In my own files, corrected on 22 Nov.** The section headings 1.1-1.11 and the work-file stamps carried estimated
times ahead of the clock; they now give the transcript and file times. The events written before midnight UTC (the
first 29) now carry the date 2026-11-21. Two row references were wrong and are fixed: row 391 rests on row 376
(D:surface-curvewise-conductor), not 380; the event of D:hereditary-Cartier-generation-budget names row 351
(D:reflexive-pullback-uniform-generation), not "the row 349 area". The loose rows 343, 346, 349 and 362 now stand
under heading 1.12.

## 5. What is new

I made no literature search (the reading limit had passed), so nothing here is asserted to be new in the literature.
Most of the run's proved rows in my half are its own assembly of known tools (Lang, Katz, Langer's boundedness and
Riemann-Roch, Hu-Teyssier's conductor and Betti bounds, Lucchini-Marion-Tracey's crown estimates, Grothendieck
existence), and their main counting theorems (393, 394, 398-400, 410) rest partly on rows of reader A's half. The
explicit objects that look most likely to be new, and are fully checked here, are:

- the characteristic-two example 433-435: S: b^2 + (t^5 + t^2 a^2) b + a^5 = 0 with one smooth genus-two exceptional
  curve, C^2 = -1, and its wild quasi-etale double cover T, whose resolution is the Frobenius cover of the same curve
  with (C')^2 = -2; pi_1(U_T)^(2) = 1 and pi_1(U_S)^(2) = Z/2;
- the symmetric-square example with exact wild image of order two and d(Gamma_R) <= 2g+2 (D:one-curve-wild-swap-cover,
  436);
- the graded-cone tameness engine D:graded-cone-tame with D:formal-torus-lift, and its extraction 428.

## 6. Hexagon readiness

The five tests of `field_experts/HEXAGON_CANDIDATES.md`: complete; self-contained; stable, with a literature search
done; checked (an intake targeted check plus an independent re-proof or a computation); of interest now.
No row of my half passes all five, because no literature search has been made for any of them.

| candidate | complete | self-contained | literature search | checked | of interest |
|---|---|---|---|---|---|
| 433-435, the wild genus-two example | yes | yes | not done | yes (re-proof, certificate rerun) | yes (formal linearity cannot be dropped) |
| D:one-curve-wild-swap-cover (320) with 436 | yes | yes | not done | yes (re-proof of 320, targeted check of 436) | yes |
| D:graded-cone-tame (253) with D:formal-torus-lift (234) | yes | yes | not done | targeted checks only; an independent re-proof is still needed | yes (key engine) |

The first is the nearest: it needs only the search (Artin's wild Z/2 quotients in characteristic two and the
Lorenzini-Schroer work on wild quotient singularities are where to look first).

## 7. Open dependencies outside my half

Rows of my half rest on these statements, which I did not check (most are among reader A's ids 1-219):
D:alternating-compressed-local-orbits, D:finite-puncture-local-orbit-factorial-count, D:exceptional-degree-linear-core,
D:contract-zero-cost-blocks, D:SNC-general-Brauer-geometry, D:SNC-general-residual-category,
D:SNC-general-projective-quadratic-count, D:canonical-order-Morita-conductor,
D:finite-Morita-Frobenius-object-effectivity, D:bounded-centre-projective-growth, D:bounded-scalar-projective-growth,
D:Kummer-uniform-Frobenius-defect, D:filtered-linear-curve-resolution, D:filtered-polynomial-diagrams,
D:compressed-skew-Frobenius-unit-jets, D:coherent-full-root-coefficient-gerbe,
D:bounded-graph-projective-crown-reduction, D:finite-jet-unit-Isom, D:etale-resolution-semilinear-count,
D:etale-resolution-hereditary-linear-count, D:fixed-boundary-small, D:Qfactorial-partial-resolution,
D:finite-cone-wild-bound, D:local-complete-Lang, and those listed in the work file (D:bounded-period-hereditary-
projective-growth, D:curve-fixed-local-growth-numerical, D:controlled-one-curve-gerbe-anchors, D:finite-formal-cone-cover,
D:elliptic-cone-Heisenberg-covers, D:Brauer-zero-projective-representation-growth, D:canonical-module-two-level-recovery,
D:Artinian-full-neighbourhood-realization, D:cover-uniform-Noether-different, D:cover-uniform-canonical-defect,
D:arbitrary-cover-ordinary-hereditary-growth, D:finite-local-images-arbitrary). Cited literature was not opened in this
intake (past the reading limit), notably Hu-Teyssier (rows 376, 383), Langer (390, 395), Lucchini-Marion-Tracey
(392, 397, 414, 415), GKKL (374), SGA 7 XIII (401), Chatzistamatiou-Rulling (L6b).

## 8. Second pass (22 Nov, 00:58-00:59 UTC)

| # | row | run's status | my check | verdict |
|---|---|---|---|---|
| 329 | D:projective-base-generation | proved | one base open for all quotients (smooth base change, fpqc descent of etaleness); wild inertia images bounded by (m_E)_p c_D; projective fixed-boundary group of a cover | confirmed; rests on rows 354, 239 and D:fixed-boundary-positive (reader A's half) |
| 315 | D:normal-subgroup-projective-crowns | proved u.s.h. | bounded-index normal subgroup; restriction count q^((A a t + 1) r^2); extension cost of order S to the power a-1; crown inequality | confirmed; the lift bijection comes from row 313 (partly checked) |

No error found. Rows 256, 270 and 331, which rest on 329, are thereby checked through that dependency as well.

## 9. Second pass on the seven partly checked rows (22 Nov, 01:00-01:04 UTC)

At the coordinator's word (22 Nov): the proofs of 292, 302, 313, 319, 324, 328 and 363 read in full, with their cited
sources opened where freely available (arXiv LaTeX sources, downloaded to my work folder, never into the return).

| # | row | my check | sources opened | verdict |
|---|---|---|---|---|
| 292 | D:local-pair-unbounded-horizontal-root-atlas | uniformity in N_a: genus and marks O(m_i); normalized weights; one coefficient slot per marked pair (p after Frobenius) | Borne arXiv:math/0604458 (Prop. 3, Thm. 4); Borne-Vistoli arXiv:1001.0466 (main theorem); Crainic arXiv:math/0403266 (section 2) | confirmed; SNC presentation rows in reader A's half |
| 302 | D:moving-line-polynomial-background | primitive element; ordered divisors and Artinian lifting; exact complement condition; trace-dual degrees; chart count | Stacks tags standard, not opened | confirmed; compression lemma in reader A's half |
| 313 | D:nonsplit-automorphism-wreath-lifts | wreath cocycle identity; normalization of transports; conjugacy; monolithic embedding | none needed | confirmed (independent re-proof) |
| 319 | D:one-curve-unbounded-period-projective-count | class count; presentation budgets; E independent of f; row 429 | none needed | confirmed; anchors and unit-Isom rows in reader A's half |
| 324 | D:persistent-first-neighborhood | phi^*C = eC'; retraction below order e; h^*e_Y = 0; Frobenius injectivity | Brenner arXiv:math/0402179, Prop. 2.1 | confirmed (independent re-proof) |
| 328 | D:primitive-defining-characteristic-orbit-models | faithful F_p-representation of PGammaL_d; induction; Maroti's trichotomy; D^4 | Maroti 2002 not opened (statement matches the published theorem) | confirmed (independent re-proof) |
| 363 | D:single-curve-Cartier-module-jet-recovery | specialization to etale covers via row 364 | none needed | confirmed; the recovery theorem is in reader A's half |

No error found. After this pass (232 events in all, superseding the counts of section 2) no row of my half is left at "statement read" or "partly checked": by strongest
event, 2 computation, 66 independent re-proof, 148 targeted proof check, 3 carried as background (225, 337, 401).

## 10. Literature search for the wild genus-two example (rows 433-435) (22 Nov, 01:05-01:13 UTC)

**The object.** In characteristic two, S: b^2 + (t^5 + t^2 a^2) b + a^5 = 0 is a normal Gorenstein surface germ whose
resolution has one smooth exceptional curve C (y^2 + y = x^5, genus two, C^2 = -1, discrepancy -3). Its double cover T,
etale off the singular point, is fiercely ramified along C (e = 1, purely inseparable residue extension of degree two,
different exponent one). The resolution of T has one curve C', the Frobenius twist of C, with (C')^2 = -2 and
discrepancy -2. Then pi_1(U_T)^(2) = 1 and pi_1(U_S)^(2) = Z/2. The weighted-homogeneous germ S_0: b^2 + t^5 b + a^5 = 0
has the same resolution graph, and its covers are tame along C by D:graded-cone-tame. So the example shows that the
tame behaviour of a single smooth exceptional curve depends on the formal neighbourhood, not on the graph.

**Searched** (22 Nov, web searches of arXiv and the journal literature; the LaTeX or PDF opened where named):
- wild quotients of smooth germs: Artin, Wild Z/2 actions in dimension two (Proc. AMS 1975), and Coverings of the
  rational double points in characteristic p (1977); Lorenzini-Schroer, Moderately ramified actions in positive
  characteristic (arXiv:1904.08371, Math. Z. 2020); Ito-Schroer, Wild quotient surface singularities whose dual graphs
  are not star-shaped (arXiv:1209.3605); Lorenzini-Schroer, Discriminant groups of wild cyclic quotient singularities
  (arXiv:2101.08090, ANT 2023). In all of these the source of the wild cover is a smooth germ, and the exceptional
  curves of the quotient are rational trees.
- wild covers between singular germs: Matsumoto, mu_p- and alpha_p-actions on K3 surfaces in characteristic p
  (arXiv:1812.03466, JAG 2023), section 6, on Z/p- and alpha_p-coverings of rational double points. These have rational
  exceptional curves.
- tameness theorems: Carvajal-Rojas-Schwede-Tucker, Fundamental groups of F-regular singularities via F-signature
  (arXiv:1606.04088; LaTeX opened: the local fundamental group of a strongly F-regular singularity is finite of order
  prime to p); Carvajal-Rojas-Staebler, the local etale fundamental group of KLT threefold singularities (arXiv:2004.07628;
  tame and finite for p > 5); arXiv:1707.08611 (the local etale fundamental group of a log terminal surface germ is
  finite). These exclude such covers only inside the klt and F-regular ranges. S, with discrepancy -3, lies outside
  even the log-canonical range.
- Cutkosky-Srinivasan, Local fundamental groups of surface singularities in characteristic p, Comment. Math. Helv. 68
  (1993), 319-332 (doi 10.1007/BF02565822). This is the paper most likely to contain a related phenomenon. Its keywords
  are local fundamental groups and Brieskorn singularities. I could not reach its text: the GDZ copy offers only a
  viewer page, zbMATH refused the request, and claude_tools/find_paper.py found no copy on disk (default literature
  roots, regex "Cutkosky...Srinivasan | local fundamental groups of surface singularities", 240 s limit, no match).
- Hexagon (hexagonmath.org/search), at the user's word. I searched "singularity", "wild ramification", "fundamental
  group surface" and "Artin-Schreier". Nothing relevant came up; the nearest work is Kisin, Serre's conjecture on the
  Artin character for a regular local ring (28 Oct 2026), which concerns group actions on regular local rings.

**Verdict.** In the sources searched, this example is not known: no source gives a quasi-etale double cover of a
normal surface singularity with a single smooth exceptional curve of positive genus that is wild along that curve, and
none gives these equations. Wild quasi-etale covers as such are classical (Artin 1975, 1977), but always with smooth
sources or rational double points. The verdict is "new, provisionally". It becomes final only after Cutkosky-Srinivasan
1993 has been read, since the singularities it studies are the right kind.

**Hexagon readiness, revised.** The example is complete and self-contained. It is checked: I re-proved it by hand and
reran its certificate. It is of interest now, and the literature search is done except for one paper. It is the
nearest Hexagon candidate; posting waits only on reading Cutkosky-Srinivasan 1993.
