# Full intake of RESEARCH_SA07 (cp12), statement by statement, 21-22 Nov 2026

By Claude Opus 5.5 at effort max, agent a922466087ec53798, at the main session's word (the user, 21 Nov: [the user's words, omitted]). The run: GPT-6 Astra (ChatGPT Pro mode). Return:
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped/`.
Earlier intake: `INTAKE_RESEARCH_SA07_20261120.md` (same agent). Its 28 checked rows are carried into
`INTAKE_RESEARCH_SA07_20261121_full_CHECK_EVENTS.tsv` with their original dates; the ids there are plain register ids.

Status: every one of the 186 register ids has a check event (22 Nov 2026). 126 of them were checked or recomputed, 60
were read only at the level of the statement, and those are marked so. Counts by type: 76 targeted proof checks (some
"in part", which the event says), 24 independent re-proofs, 9 computations or certificates, 17 carried as background
without fault found, and 60 statement read only.

## 1. Checked before (20 Nov), carried over

A.1.1-A.1.3, A.2.1-A.2.7, A.3.1-A.3.4, A.4.1-A.4.9, A.5.1, A.5.3, C.1.1, C.3.1, F.2.1: see the earlier intake, section 1.

## 2. Rows checked in this full intake

### The twelve rows the run marks refuted (22 Nov), all read with their proofs

- **B.1.3.** Targeted proof check, confirmed. For `ℓ ≠ p` the Tate functor of a `p`-divisible group is 0. In equal
  characteristic, `μ_{p^∞}` over `F_p((t))` has `T_p = 0`, so the functor is not faithful. Both literal readings of
  `5′` (18:5) fail.
- **B.4.4.** Targeted proof check, confirmed. Take the unramified `Z_ℓ`-tower times the Tate line, so that
  `u = (r_ℓ, χ_p)`. The two towers are disjoint (the cyclotomic one is totally ramified, by Eisenstein), so the image
  contains `Z_ℓ` and is not virtually pro-`p`. So the proalgebraic version of "`π/Ker u` est un groupe analytique
  p-adique" (18:6) fails. Its finite levels stay analytic.
- **D.5.2.** Targeted proof check, confirmed. For `K = Q(√−5)` and `I = (2, 1 + √−5)` (not principal), `C/O` and `C/I`
  are Galois conjugate by CM theory. Their integral homology modules `O` and `I` are not isomorphic, while the rational
  and local comparisons exist. So the integral comparison of 18:55 fails.
- **D.5.3.** Checked in part. The Euclidean orbit-closure lemma (Baire) is checked. The `Q(−2)` counterexample to
  openness (18:61) I re-derived myself: the image of `χ²` is the closed subgroup of squares in `Ẑ^×`, of infinite index,
  hence not open. The elliptic equivalence was read at statement level only.
- **E.1.2.** Targeted proof check, confirmed. Take the Legendre curve over `Q̄(t)` and two places that differ by an
  automorphism acting on torsion as `u(2a)`, with `a = lim Σ_{m<n} m!` in `Ẑ`, not an integer. Naturality under all
  cyclic isogenies would force `a ∈ Z`. So no natural integral Betti isomorphism exists, although every finite piece
  has one.
- **E.1.3.** Independent re-proof, confirmed. The embeddings `exp(1/n!)` and `exp(1/n! + 2πi s_n/n!)` are compatible
  and both send `t` to `e`. Integral path sets have an empty inverse limit; profinite ones do not (compactness).
- **E.2.1.** Targeted proof check, confirmed. Analytic continuation along a polygon from `e` to `e + 1` that avoids `Q̄`
  defines a second place, and parallel transport makes the whole integral Betti diagrams tensor-isomorphic. So plain
  integral tests do not separate places (15:207, "faux").
- **E.3.3.** Checked in part. Its mechanism is checked: move the Hodge structure of the whole category by a real point
  of `ker ε` that commutes with `f_∞`, with the rational non-CM curve `y² = 4x³ − 4x − 1`. The Lie-lifting step was read
  at statement level.
- **E.3.4.** Checked in part. The lift through the injective cotangent map is checked; the last step was read at
  statement level.
- **F.3.7.** Targeted proof check, confirmed. `P¹_R` refutes `H^*(X(R)) = H^*(X(C))^{conj}`. The raw centralizer `R^×`
  (Tate) is not compact. Modulo the weight image, `Z(C)` is compact through the Cartan involution of a polarization.
- **F.3.11.** Targeted proof check, confirmed. A character of `∏ F_2` trivial on the dense subgroup `⊕ F_2` is
  discontinuous (it needs a Hamel basis), and twisting by it gives an abstract semilinear action that is not a descent
  datum.
- **G.2.2.** Independent re-proof of the counterexample, confirmed. At `τ = i`, `E_6(i) = 0`, so the `E_2` term of
  `E_4 + E_2E_6/E_4` vanishes and the transcendence degree is 2, against the bound 3. I have not opened the printed
  hypotheses of Bhowmik-Pathak 2024, Theorem 1.11.


### Parts A-F beyond the refuted rows (22 Nov): the check each row received is in the TSV; the main points

- **A.3.5, A.3.6.** Targeted proof checks, confirmed.
  - A.3.5: a rational relation `τ̄ = R(τ)` forces `R∘R = X` and a Möbius relation, that is, an isogeny to the conjugate.
    Otherwise the dependence is a symmetric irreducible `P` of bidegree at least `(2, 2)`.
  - A.3.6: the group of `E × Ē` is `{det g_1 = det g_2}`, of dimension 7, and the flag map is surjective, so the period
    conjecture gives transcendence degree 2. The gate remains open.
- **A.4.10-A.4.40 (the routes to 18:13 c).**
  - Computations by hand or script:
    - the q-coefficient `a_2²/4 − a_3/3 − h` (A.4.10);
    - the projector and the `S` matrix (A.4.11);
    - `V_a ≅ G_m³`, which generates `GL_2` (A.4.12);
    - the restricted `p`-th power `D_a^p = H_p D_a − (K_p + aH_p)V`, which my script `check_A431.py` verifies for
      `p = 5, 7, 11` (A.4.15, A.4.31);
    - the 3-torsion lift polynomial `243t⁸ − 54t⁴ − 9t² − 1`, from `t² = r/3` (A.4.17);
    - the 3-adic valuations by Kummer's theorem (A.4.22);
    - the symmetric-square period matrix (A.4.36).
  - Re-proved: the mock-modular coefficient `a = −(m²/d)h` (A.4.23), the operator defect `k(b − a)` (A.4.25), the
    G-function ODE and monodromy (A.4.27), the Gaussian invariance (A.4.29) and the lattice criterion `|h − a| ≠ c`
    (A.4.34).
  - Checked through their classical mechanism: A.4.14 (maximal compact subgroup), A.4.16 (torsion values of the
    completed zeta), A.4.18, A.4.20 (canonical lifts have CM), A.4.21 (the `p`-adic analogue of 18:13 c fails for
    ordinary curves) and A.4.30.
  - Read in part or at statement level: A.4.13 (Bakker-Tsimerman applicability), A.4.19, A.4.24, A.4.26, A.4.28,
    A.4.33, A.4.35 and A.4.39; and A.4.32, A.4.37, A.4.38, A.4.40.
- **Part B.** B.1.1 and B.4.1-B.4.3 are checked; B.3.1 and B.3.2 are checked through the `2πi` factor and `ᾱ = α f_∞`.
  B.1.2, B.1.4, B.1.5, B.2.1-B.2.3, B.3.3 and B.3.4 are known `p`-adic Hodge theory, carried as background without
  fault found.
- **Part C.**
  - Checked: C.1.2, C.1.3, C.2.1, C.2.2, C.3.2, C.4.1, C.4.2; C.3.3 in part.
  - Re-proved: C.1.4 (`τ = i·2^{1/3}`, `End = Q`, Hodge cocharacter of weights `±3`) and C.5.1.
  - C.1.5 is checked: a Hodge pair whose period is the non-computable number `1 + Σ_{n∈H} 4^{−n}` (`H` the halting set)
    is not geometric.
- **Part D.**
  - D.1.2 re-proved (the `(n − 1)d` bound). D.1.1, D.3.1 and D.5.4 (necessity) checked.
  - D.3.2 and D.4.1 are known (Serre 1972; strong approximation).
  - D.2.1, D.4.2, D.5.1 and D.6.1 read at statement level.
- **Part E.**
  - Checked: E.1.1, E.1.4 (in part), E.2.3, E.2.6, E.2.9 (in part) and E.3.2.
  - Re-proved: E.2.7 (interlacing quadratic Artin objects), E.3.1 (`j(E_a) = 1728a`) and E.2.4 (totally real
    subfields of ring class fields have elementary abelian 2-group).
  - E.2.2, E.2.5, E.2.8, E.2.10-E.2.31 (except E.2.16 and E.2.22, also statement level) read at statement level only.
- **Part F.**
  - Checked: F.1.1, F.1.2, F.1.5, F.1.6, F.3.5, F.3.14.
  - Re-proved: F.1.3 (the factor `(2πi)^{d−r}`, 1 for `r = d`, the "Ouf !" of 18:25), F.1.4 (the sign `(−1)^p`), F.3.3
    and F.3.9 (a transversal has dimension `p`; the frozen label `n − p` is right only for `n = 2p`). F.3.2 was checked
    by hand computation.
  - Known: F.3.1, F.3.4, F.3.6, F.3.8 and F.3.12.
  - F.3.10, F.3.13, F.3.15-F.3.36 (except F.3.24, also statement level) read at statement level only.
- **Part G.** G.2.1 and G.2.3 (the printed sources for H4) read at statement level only.

## 3. Refuted or corrected

- **Refuted by this intake: none.** No step of the run that I checked was false.
- **The run's twelve refutations of statements on the pages, and of one printed bound (G.2.2), are confirmed.** Two are
  confirmed in part: D.5.3 and E.3.3-E.3.4, as section 2 says.
- **Corrections to our own files:**
  - R2 of the prompt: the converse is false (C.3.1).
  - R5 of the prompt and the sweep-3 check event at 18:9: the conventions agree, and the graded formula on line 14 is
    off by 2 (F.2.1).
  - Lead A: the condition is `M ≅ c^*M` (A.3.3).
  - The 20 Nov intake events used ids `RESEARCH_SA07 cp12 X`, which the ledger did not count; this file uses the plain
    register ids.

## 4. What is new

New against our files, beyond the 20 Nov intake (section 2 there):
- the `p`-adic counterpart of 18:13 c is false for ordinary curves (A.4.21);
- the explicit restricted-Lie formula at every good `p` (A.4.31), certified here for `p = 5, 7, 11`;
- a non-computable non-geometric Hodge pair (C.1.5);
- countable and uncountable fields where integral Betti functors fail to separate places, with explicit embeddings
  (E.1.2, E.1.3, E.2.1);
- the CM obstruction `O` against `I` over `Q(√−5)` to the integral comparison of 18:55 (D.5.2);
- the counterexample to Bhowmik-Pathak 2024, Theorem 1.11 (G.2.2).

The run claims no priority, and I have made no literature search for these beyond what the run records.

## 5. Errata

- In the run: none found in the rows checked.
- In our files: the three corrections of section 3.
- In the literature: Bhowmik-Pathak 2024, Theorem 1.11, as consulted by the run (G.2.2), and the two hazards in
  Spence 2018 for Masser's formula (A.4.5, noted 20 Nov).

## 7. Second round (22 Nov): the rows read at statement level

The new events are appended to the TSV; each old event is kept. Level of each of the 186 ids after this round, by its
highest event:
- targeted proof check: 92
- statement read only: 40
- independent re-proof: 25
- carried as background without fault found: 20
- computation or formal certificate: 9

- **Raised in this round.**
  - E.2.2: the CM endomorphism recovers the complex structure, so `v(j) = w(j)`.
  - E.2.5: CM-type sign patterns separate the embeddings of a totally real field.
  - E.2.8: a finite isogeny skeleton.
  - E.2.10: `a = (0, 1, 1, ...)` in `Ẑ`, so the nested cosets meet no point of `SL_2(Q)`.
  - E.2.11: in part.
  - E.2.12: representability; in part.
  - E.2.13: every `T` in `SL(H_1)` acts on the admissible closure but does not extend across the `Q`-isogeny.
  - E.2.14, E.2.15 and E.2.16, E.2.18: proofs read.
  - E.2.17: local data at 3; in part.
  - E.2.21: the imaginary quadratic case.
  - E.2.22: the integral surjectivity of Jacobians onto abelian varieties, and Belyi.
  - F.3.16: the Fermat-quartic cover data recomputed.
  - F.3.23: normal core and homology.
  - F.3.35: carried as background (source theorem).
  - F.3.36: re-proved for dimension at most 4 in characteristic 0.
  - G.2.1 and G.2.3: they agree with my literature check of 19 Nov and with the SA15 files.
  - G.2.2: checked against the printed arXiv v1 hypotheses (next item).
- **G.2.2 against the printed paper.** I downloaded the LaTeX source of arXiv:2408.00271v1 (18 pages, "to appear in Acta
  Arithmetica") to `agent_notes/a922466087ec53798_work/bp2024/`.
  - Theorem 1.11 there assumes: `f` a non-constant meromorphic modular form; `g` a non-constant modular function;
    `f̃` a non-constant meromorphic quasi-modular function of depth at least 1; algebraic Fourier coefficients;
    `f(τ) ≠ 0`, `f̃(τ) ≠ 0`; `τ` not a pole. It asserts transcendence degree at least 3.
  - The run's `f̃ = E_4 + E_2E_6/E_4` has weight 4. If "quasi-modular function" means weight 0, then
    `f̃ = 1 + E_2E_6/E_4²` (my example) gives the same failure at `τ = i`, with `f̃(i) = 1`.
  - So the printed v1 statement is false under either reading. The 23-page journal version is not checked.
- **Lead H4.** G.2.3 locates the reconstruction question in his May 1966 letter to Tate (cote 6). That is earlier than
  Nice 1970 and than cote 18 (c. 1969-1972), so "18:5 is the earliest written form" is refuted, provided the quoted
  sentence is checked against the cote-6 transcription.
- **Open point for a checker (E.2.23-E.2.26).** Each of these rows needs one `σ*` in `Gal(Q̄/F_cm)` that swaps the two
  real roots of `x⁴ − x − 1` and acts integrally on every lattice of the class at the same time.
  - The splitting field has group `S_4 ≅ PGL_2(F_3)`. If it is the projective 3-division field of some `E/Q`, then
    `ρ_E(σ*)` mod 3 must map to `(12)(34)` in `PSL_2(F_3) ≅ A_4`. That is possible, since `det = χ = 1`.
  - The simultaneous choice over all such entanglements is the crux of these rows. I have not read their proofs
    (lines 1290-3190 of `E_integral_image.tex`).
- **Still at statement level after this round (40 rows):** A.4.32, A.4.37, A.4.38, A.4.40, A.5.2, D.2.1, D.4.2, D.5.1, D.6.1, E.2.19, E.2.20, E.2.23, E.2.24, E.2.25, E.2.26, E.2.27, E.2.28, E.2.29, E.2.30, E.2.31, F.3.10, F.3.13, F.3.15, F.3.17, F.3.18, F.3.19, F.3.20, F.3.21, F.3.22, F.3.24, F.3.25, F.3.26, F.3.27, F.3.28, F.3.29, F.3.30, F.3.31, F.3.32, F.3.33, F.3.34.
  - These are the long anabelian and integral-image proofs: Nakamura's universal quotients, Hain weights, the Johnson
    detector and the simultaneous integral comparisons.
  - Each rests on primary inputs that I have not opened. They are the next work, best for an agent that has read
    Nakamura 1996 and the LM6 material.

### Later in the second round (22 Nov)

- **Raised further:**
  - A.4.37: the `h`-law re-proved through Vélu, `f*ξ′ = Nξ − S_C ω`.
  - A.5.2: re-proved, the image `{1, −3 − 2√2}` against an infinite cyclic subgroup.
  - D.5.1: re-proved, the cocycle laws and the fpqc datum `z_12`.
  - D.4.2: confirmed, by Baire and the `SL_2` counterexample.
  - D.2.1: dimensions confirmed. The fibre is 5-dimensional, and 4-dimensional with the determinant fixed. The
    mathematics supports reading 4 for his uncertain "≤ 5|4" over `k(π)`.
  - F.3.13: confirmed, the closed equations for `Aut(ω_A)`.
- **Levels now, by the highest event of each of the 186 ids (215 events in all):** targeted proof check 95; statement read only 34; independent re-proof 28; carried as background without fault found 20; computation or formal certificate 9.
- **Still at statement level (34):** A.4.32, A.4.38, A.4.40, D.6.1, E.2.19, E.2.20, E.2.23, E.2.24, E.2.25, E.2.26, E.2.27, E.2.28, E.2.29, E.2.30, E.2.31, F.3.10, F.3.15, F.3.17, F.3.18, F.3.19, F.3.20, F.3.21, F.3.22, F.3.24, F.3.25, F.3.26, F.3.27, F.3.28, F.3.29, F.3.30, F.3.31, F.3.32, F.3.33, F.3.34.
  - Their proofs rest on primary inputs I have not opened: Nakamura 1996 for the universal arithmetic quotients,
    Hain's weights, the Johnson homomorphism, Bost's slope method (A.4.32, A.4.38, A.4.40), and the simultaneous
    integral comparisons E.2.23-E.2.31.
  - F.3.32 claims to settle the "full CM common-kernel subgroup assertion" of LM6 A.22 by an exact polynomial
    certificate, with F.3.29 and F.3.30 as inputs. That claim matters for the Longue Marche programme. It should go to
    the Longue Marche or anabelian field expert, with Nakamura 1996 and the run's `code/` certificate.

## 8. Third round (22 Nov): the rows that rest on primary sources

Sources opened. They are kept in `agent_notes/a922466087ec53798_work/` and were fetched from open hosts; there is no
PDF where LaTeX exists.
- Nakamura, "Coupling of universal monodromy representations of Galois-Teichmüller modular groups", Math. Ann. 304
  (1996). This is a GDZ scan; I viewed printed pp. 115-117.
- Bost, "Algebraic leaves of algebraic foliations over number fields", Publ. IHES 93 (2001), Numdam, Theorem 2.3.
- Herblot, "Algebraic points on meromorphic curves", arXiv 1204.6336v1, LaTeX: the main theorem and the density
  proposition.
- Bhowmik-Pathak, arXiv 2408.00271v1, LaTeX (second round).

A disk search with `find_paper.py` was started; it was still running when this section was written.

- **E.2.23, the single Galois element: checked, and my open point is resolved.** The run never needs `ρ_E(σ) = I`. It
  imposes exact integral values `ρ_{E_i}(σ) = S_i ∈ SL_2(Z)` one isogeny class at a time:
  - each value is a closed condition;
  - each `S_{n+1}` is chosen in a nonempty open coset, by density of `SL_2(Z)` in `SL_2(Ẑ)`, using the openness
    `(E.2.23i)` of `ρ(Γ_{F_cm})` in `SL_2(Ẑ)^r`;
  - compactness then gives `σ`.

  So any entanglement between the splitting field `P` and division fields is absorbed into the coset. I also re-derived
  `P ∩ F_cm = P^{V_4}`: the `S_3` resolvent field is a cyclic cubic extension of the CM field `Q(√−283)`, hence lies in
  `F_cm`, while `P` over `Q(√−283)` has group `A_4`, which is not abelian. So `(12)(34)` is attainable.
- **E.2.24-E.2.26: carried.** They follow the same pattern. Their open-image inputs (Commelin 2019, Cadoret-Moonen 2020,
  Lombardo 2015, Mayle-Wang 2024) are cited and were not opened by me.
- **A.4.32: confirmed against Herblot.** Her main theorem with `r = 2` (the leaf is not algebraic, A.4.15) and `ρ = 2`
  (the theta parametrization), and her density proposition with the same weights `[K_𝔭:Q_p] log p/(p − 1)`, give
  `β ≤ 1 − 1/(4d)`.
- **A.4.15: the input is now checked too.** Bost 2001, Theorem 2.3, is the restricted-Lie criterion exactly as cited.
- **F.3.20: checked in part against Nakamura 1996.** Every cited statement is on the printed pages as the run says:
  - Corollary 4.2 (`r_{0,3}(m) ≤ r_{g,n}(m) ≤ r_{1,1}(m)`);
  - table (4.3), with `r_{0,3}(6) = 1`;
  - Lemma 4.5 (surjectivity of `Φ_C`, with no `End(J) = Z` premise);
  - Corollary 4.6;
  - (4.7.1)-(4.7.2), with `GSp` acting on `gr^m` through `χ^{m/2}`.

  Steps 2-3 (weights, Faltings) are also checked. Step 4, the split-CM obstruction through Nakamura 1995, was not read.
  - A bridge to purity: Nakamura's proof of Lemma 4.5, and the run's step 2, use that `gr^i` of the lower central series
    of the pro-ℓ fundamental group is pure of weight `−i`. That is Weil purity for `H^1` of curves.
- **A.4.38: checked in part.** The period-kernel rank 2 and the kernel statement are checked. The rank bound rests on
  Waldschmidt 1988, Theorem 4.1, which I did not open.
- **Levels now (222 events):** targeted proof check 99; independent re-proof 28; statement read only 27; carried as background without fault found 23; computation or formal certificate 9.
- **Still at statement level (27):** A.4.40, D.6.1, E.2.19, E.2.20, E.2.27, E.2.28, E.2.29, E.2.30, E.2.31, F.3.10, F.3.15, F.3.17, F.3.18, F.3.19, F.3.21, F.3.22, F.3.24, F.3.25, F.3.26, F.3.27, F.3.28, F.3.29, F.3.30, F.3.31, F.3.32, F.3.33, F.3.34.
  - For these I propose a routing. The F.3 rows (F.3.15-F.3.34, apart from those checked above) build toward F.3.32,
    which goes to the Longue Marche expert ae4ae3dc. They are one argument and should go with it, together with
    Nakamura 1996 (on disk now) and Hain 1997, "Infinitesimal presentations of the Torelli groups" (JAMS 10).
  - E.2.19, E.2.20 and E.2.27-E.2.31 are long diagonal and profinite constructions on the integral image. They need a
    full read of `E_integral_image.tex`, lines 510-1093 and 3190-4749.
  - A.4.40 rests on Bost-Chambert-Loir 2008 and Herblot.
  - D.6.1 is a scope statement, not a theorem.

## 9. Fourth round (22 Nov): E.2.19, E.2.20, E.2.27-E.2.31 (full read of `E_integral_image.tex`) and A.4.40

- **E.2.19: confirmed, proof read in full.** For `K = Q(i)`, the scalar idele with component `−1` at 5 and `1`
  elsewhere has norm 1. It is congruent to 4 mod 15, so its ray class mod 15 is not trivial (no unit `±1, ±i` matches
  it), and it lies in every `Ô_f^×`. The main theorem of CM then gives an actual integral comparison on the
  `Q(i)`-CM diagram whose scalar is not one global sign.
- **E.2.20: confirmed.** The steps are: Hilbert 90 for `r = s/c(s)`; `Nm_{F/Q}(t) = aλ`; `art_Q(λ)` trivial on every
  `Q(ζ_m)^+`, which forces a global sign. The explicit obstruction is the CM 4-fold of type `Φ_1` over
  `Q(ζ_15)^+(i)`. I checked numerically that the roots of `X⁴ − X³ − 4X² + 4X + 1` lie in the stated intervals and
  that `3 − 2t` is negative only at the identity embedding.
- **E.2.27: confirmed, proof read in full.** I recomputed the commutator matrix and the Cayley-Hamilton
  non-stalling step, and checked the trace exclusions of every word, the integral classes on every cover, and the
  absence of cusp inertia.
- **E.2.28: confirmed, proof read in full.**
  - `Γ_N` is residually finite.
  - `Â/A` is a `Q`-vector space, so the complements are conjugate.
  - The normalizer is `Γ_N Z_N`, by Smith normal form.
  - The invariant label cycles give surjective transitions, hence one compatible conjugator, with no compactness used
    on nonclosed sets.
- **E.2.29: checked in part.** I recomputed the `A_5` cover data (genus 9; ranks 61, 43, 18). The displayed values
  are consistent: `q(γb) = 60 qNb ≠ 0` while `q(P) = 0`. The matrix `N` comes from the run's script, and the lift uses
  Bleher-Chinburg-Lubotzky's Gaschütz corollary; I checked neither.
- **E.2.30: checked in part.** The proper-homology analogue of E.2.28: the setup is checked. The self-normalizing claim
  and `H_int ⊊ H_c` were not read in full.
- **E.2.31: checked in part.** I checked the transfer `π_*π^! = e` (by unimodularity), the surjective compatible sets,
  the fixed points of `⟨(12345)⟩` with `g(C/H) = 1`, and the non-integrality of `z_0 = av`. The final non-membership
  step was not read.
- **A.4.40: checked in part against Bost-Chambert-Loir** (arXiv math/0702593, LaTeX). Their proposition on the size of
  foliation leaves gives exactly the run's lower bound at `p`-closed unramified places. With the run's equality at the
  other places and the density of A.4.32, A-analyticity fails. The run's own upper-bound argument was not read.

**Levels now (230 events):** targeted proof check 107; independent re-proof 28; carried as background without fault found 23; statement read only 19; computation or formal certificate 9.

**Still at statement level (19):** D.6.1, F.3.10, F.3.15, F.3.17, F.3.18, F.3.19, F.3.21, F.3.22, F.3.24, F.3.25, F.3.26, F.3.27, F.3.28, F.3.29, F.3.30, F.3.31, F.3.32, F.3.33, F.3.34.
- The F.3 normalizer chain (and F.3.32) is with the Longue Marche expert ae4ae3dc.
- D.6.1 is a scope statement, not a theorem.

## 6. Hexagon readiness (the five tests of field_experts/HEXAGON_CANDIDATES.md)

- **G.2.2, the counterexample to Bhowmik-Pathak 2024, Theorem 1.11.** It is a candidate, one gate away from test 2.
  - Test 1 (complete): passes. The counterexample is explicit, `E_6(i) = 0`.
  - Test 4 (checked): passes in part. I re-derived the counterexample independently; the run's own proof is the
    targeted check.
  - Test 2: now passed for arXiv v1 (printed hypotheses opened 22 Nov; the statement fails under both readings).
  - Test 3: still open; it needs the 23-page Acta Arithmetica version, which may already be corrected.
  - Test 5 (of interest now): yes, for the authors. In the first place it is a note to them (memory informing-authors).
- **C.1.5, a polarized Hodge pair outside the geometric image by non-computability.** It passes test 1 and has a
  targeted check. Test 3 needs a literature search: non-motivic Hodge structures are known to exist by other arguments,
  and whether this explicit computable-period obstruction is new is not known to me.
- **A.2.6, the explicit refutation of Grothendieck's "forte" list on 18:11.** It passes tests 1 and 4. Test 3 waits on
  the successor of RESEARCH_SA07, and test 2 needs the motivated-motive inputs cited with locators.
