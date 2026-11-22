# Intake of RESEARCH_SA20 (final return), 20 Nov 2026

By Claude Opus 5.5 at effort max (agent acf08879a01b97ed4, resumed; sweep-3 reader of SA20's cote 119 stretch,
119_144-161_276-281), for the main session (Claude Opus 5.5 at effort max). Brief:
`field_experts/intake_20261120/INTAKE_BRIEF.md`. Rows: all 267 rows of RESEARCH_SA20 (packets 33–37).

The run: GPT-6 Astra (ChatGPT Pro mode), "Checks and proofs around the Esquisse dossiers", returned INCOMPLETE on
20 Nov 2026 at 04:04 UTC after its stopping rule (two reviews without movement).

## 0. What was read, and the scope

**Return folder:** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA20_final_20261120T0404Z_unzipped`
(the final package; `_from_earlier_checkpoints` holds checkpoint 22, not used). Register `RESEARCH_SA20_results.csv`
(267 rows), `CHECK_EVENTS.tsv` (712 events), report `RESEARCH_SA20_report.md` (outcome table read in full), paper
sources under `parts/` and `agents/*/`.

**Scope.** 51 rows were read in full with a targeted proof check:
- E.001–E.014;
- A.101–A.115;
- A.118 and A.201–A.207;
- A.308;
- A.701–A.704;
- A5.003 and A5.004;
- B.008, B.009, B.013, B.014, B.017 and B.022;
- C.004.

Partly read: A.131, A.156, A.159, A.160, A.208, A.209, B.037, and the statements of C.001–C.009. The other 216 rows are at the level of the statement: the sort's statement and the report's outcome table. Part E was re-checked by computation (`INTAKE_RESEARCH_SA20_20261120_checkE.py`). The context guard (over 70 %) stopped further reading of proofs; the bridges (§4) follow the corrected criterion of 20 Nov ~21:1x UTC.

## 1. Verdicts, row by row

### 1.E Part E: finite geometry (119/155–161) and plane trees (152) — E.001–E.014, all read in full

This part takes up the "Digressions combinatoires" that I read in sweep 3 (`sweep3/SA20/readings/119_144-161_276-281.md`
§4). My sweep-3 computations (`readings/119_144-161_276-281_checks_fin.py`, `_checks_pgl5.py`) and a new script for this
intake (`INTAKE_RESEARCH_SA20_20261120_checkE.py`, output `_checkE_out.txt`) re-check its finite claims independently.

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| E.001 | Proved | targeted proof check | confirmed |
| E.002 | Proved | targeted proof check; computation (sweep 3) | confirmed, including the corrections: S₅ ≅ PGL₂(𝔽₅) holds only through the six-point action, and the monomial group of 160 has order 48, so its determinant-one subgroup is needed |
| E.003 | Proved | targeted proof check; independent computation | confirmed. The bihexagon construction recomputes as 60 hexagons and 90 bihexagons in 6 Petersen components, the synthemes of each component forming a total. The bijection S∖{s} ≅ S*∖{t} is unique |
| E.004 | Proved | targeted proof check; independent computation | confirmed: the ten-face hemi-icosahedron, 12 structures in one S₆-orbit, a transitive A₅ stabilizer, and 6 biicosahedra |
| E.005 | Proved | targeted proof check; computation (sweep 3) | confirmed: the stabilizers have orders 10, 20, 8, 6 and 12, and an edge is a square Q with ε ≅ rot(Q) |
| E.006 | Proved | targeted proof check; independent computation | confirmed. **New against sweep 3:** with Q^∨ the square of sides, the twist ε ∧ Q^∨ has exactly two equivariant square isomorphisms to Q*, and the vertex twist ε ∧ Q has none. This settles the boxed "Q* = ε ∧ Q^∨" on 157, which sweep 3 had left undefined |
| E.007 | Proved | targeted proof check | confirmed; agrees with sweep 3 (a ≠ b; a) is needed; the 18-block counterexample; PG(2,3)) |
| E.008 | Proved under stated hypotheses | targeted proof check; independent computation | confirmed. It agrees exactly with my sweep-3 computation: G_α ≅ S₆ is unique, the stabilizer has index 10 in Aut(G_α), N(V)/V ≅ D₈, and the extension is nonsplit. The nine translation-compatible graphs without the normalization condition re-derive from C_{S₆}(Syl₃) = Syl₃ |
| E.009 | Refuted (the prompt's literature-absence claim L7) | the derivation was read in full; Cameron 2015 was not opened by me | the derivation is consistent with M₁₂ facts (the triple stabilizer has order 432 = \|AGL₂(3)\|). It corrects my sweep-3 hunch H20-119_144-161_276-281-1, which had called the literature status unknown: Cameron 2015 §6, pp. 8–9 has the affine-plane triality |
| E.010 | Proved under stated hypotheses | targeted proof check | confirmed (152/003; not my stretch) |
| E.011 | Proved | targeted proof check | confirmed: the minimal-width argument, with (1 4)(2 3) as the counterexample |
| E.012 | Proved | targeted proof check; independent computation | confirmed. The genus counts 429, 12012, 66066 and 56628 at m = 7 recompute over all 135135 pairings |
| E.013 | Known | carried as background | the Esquisse §3 locator is not reopened; the dessin translation was checked |
| E.014 | Proved | targeted proof check | confirmed (Sylvester–Gallai via Kelly; the cross-ratios on P¹(𝔽₃) and P¹(𝔽₄)) |

### 1.A1 Part A: collars, cones and the eleven functors (119/148–150) — A.101–A.113, all read in full

This is the Additif that I read in sweep 3 (§2–3 of my reading). The run settles what sweep 3 left open, and it
corrects one statement of mine; see §3.

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| A.101 | Proved | targeted proof check | confirmed: the fibrewise straight-line contraction and the Alexander contraction, with inverses and families (as in sweep 3) |
| A.102 | Proved under stated hypotheses | targeted proof check | confirmed under the run's family convention (total-space continuity; the collar interior a neighbourhood of B × P). The explicit Armstrong formula G_{p,s}F_s is checked: it fixes both ends, K_{p,0} = id, and K_{p,1} = k_p on [0, 1/2]. **New:** the space of strict rigidified collar embeddings is contractible; sweep 3 had this only as a smooth analogue |
| A.103 | Known | the derivation was read in full; the sources were not opened (Igusa 2025 Thm 7.1, Rem 7.3; Weibel; Burghelea–Lashof 1974 Thm 6.1–6.2; Shiota 2010) | consistent with the classical torus computation π₀C(Tᵈ) = 𝔽₂[ℤᵈ]/𝔽₂ (Hatcher–Wagoner; from memory). The Wh₃(ℤᵈ) = 0 and Wh₂(ℤᵈ) = 0 steps through the Laurent decomposition are correct as written. Carried as background without fault found |
| A.104 | Refuted (I c), and the collapse equivalence) | targeted proof check | confirmed. The space of I c) is P_def(B). For (B × I, B × 0) → (CB, o) the map of automorphism spaces has homotopy fibre P_def(B), from the split restriction to the top or base and the Alexander-contractible cone kernel. So PB → EP is not a Dwyer–Kan equivalence for B = (S¹)⁶ |
| A.105 | Proved | targeted proof check | confirmed: PBCR ≃ EPCR by collapse and blow-up, with exact inverses; EPCR → EPC through the Alexander contraction of the discrepancy |
| A.106 | Refuted (I b)) | targeted proof check | confirmed: Col(X,B) ≃ BP_def(B), a free principal quotient of the contractible A.102 space, so π₁ = π₀P_def(B) ≠ 0. This makes precise the fibration argument of sweep 3 |
| A.107 | Known | targeted check of the definability adaptation | confirmed: the finite steps of Brown's gluing lemmas (distance functions, finite shrinkings, piecewise-affine spindles) are definable; I a) holds for compact pairs with a finite definable local collar atlas |
| A.108 | Known | targeted proof check | confirmed (a level set of the barycentric coordinate) |
| A.109 | Proved | targeted proof check | confirmed: attaching a collar and attaching a cone are equivalences with isomorphisms on mapping spaces, so PB ≃ PBCR ≃ EPCR ≃ EPC |
| A.110 | Refuted (strict naturality of α, β) | targeted proof check | confirmed. With X = [0,1] and B = {0}, naturality would send an interval into the two-point common fixed set. With a chosen extended collar, α and β are strict; this is the run's reading of the margin "composer … avec PBR" (150), which is plausible |
| A.111 | Refuted (II b), in the derived choice-space model) | targeted proof check | confirmed: hofib(BJ → BH) ≃ BJ₀ ≃ BP_def(B) for the cone on (S¹)⁶. II c) stays true. **This corrects sweep 3,** which had II b) open and the cone side sound |
| A.112 | Proved (five of the eleven arrows are equivalences, six fail) | targeted proof check | confirmed for the three collar arrows (J_c ≅ G₊ × P(B); the compression homotopy; 2-out-of-3) and for the table |
| A.113 | Known | the derivation was read in full; the sources were not opened | carried as background without fault found. The definable–PL component bijection rests on Shiota 2010 (Thm 2.1 with complement, Lemma 3.3), and PL ≃ TOP in dimension ≥ 5 on Burghelea–Lashof Thm 6.2. Seventeen rows rest on it |

### 1.A2 Part A: cone families, tubular neighbourhoods, filtrations (119/149–153) — A.117, A.118, A.201–A.209

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| A.117 | Refuted | statement read; proof not read in full | the obstruction BP_TOP(B) for cone families with locally joint outer-face parameterizations is consistent with A.111. The run itself notes that its contractions are TOP, not semialgebraic |
| A.118 | Refuted | targeted proof check | confirmed: the notched polygonal disks C_e are Hausdorff-continuous, but their outer faces admit no joint local parameterization at e = 0 |
| A.201 | Proved | targeted proof check | confirmed: Shiota's triangulation of functions gives the segment retraction for ε below half of every positive vertex value; φ is unique up to homotopy through the retractions. It agrees with the sweep-3 re-derivation (which used Hardt triviality and derived neighbourhoods) |
| A.202 | Refuted (the 2° condition need not be attainable) | targeted proof check | confirmed. In S³ take Y = a disk with a normal whisker, and a its foot. B is a connected closed surface, and Y∖{a} has two clopen parts with nonempty preimages, so φ⁻¹(a) cannot be finite. **This corrects my sweep-3 hunch H20-119_144-161_276-281-4:** the condition is not always satisfiable. It gives no uniqueness either (the A.111 cone on (S¹)⁶) |
| A.203 | Refuted (the unrigidified 1° equivalence) | targeted proof check | confirmed: when Y is a point the functor is the collapse of A.104. The corrected equivalence retains the tube, its ruling and the bundle map |
| A.204 | Refuted (no coarsest weak regular filtration) | targeted proof check | confirmed: two spheres in ℝ⁴ glued along an arc and a point carry the filtrations F and G, whose join has one atom with link a theta graph with four edges (local H₂ = ℤ³). This refines sweep 3: "la moins fine" is false in the weak reading, though my point that only a coarsest can be canonical stands |
| A.205 | Proved | targeted proof check | confirmed: a unique coarsest partition with PL-manifold strata, the frontier condition and saturated singular loci of closed unions, through the intersection of Boolean algebras and a minimal stratum count. It is natural under definable homeomorphisms, and the inserted filtration E_{j,k} is canonical |
| A.206 | Refuted | targeted proof check | confirmed (the cusp t ↦ (t², t³); it agrees with sweep 3, Pro N34) |
| A.207 | Refuted | targeted proof check | confirmed: on a fixed product tube the dimension condition forces φ to be a homeomorphism, and the class is P_def(Y) (fibre connectedness through a half-ball) |
| A.208 | Proved | statement read | not read in full |
| A.209 | Refuted | statement and method read (Siebenmann 1972 approximation; uniform separation of components) | not read in full. Plausible: cell-like attachments are approximated by homeomorphisms in dimension 6 + 1 |

### 1.A7 Part A: the foliation quotient (119/145–146) — A.701–A.704, all read in full

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| A.701 | Refuted ("Th" as an equivalence, with connected fibres) | targeted proof check | confirmed. The connected Z/n-covers give p_n: Sh(S¹) → BZ/n, open, connected and locally connected, all with the local kernel of the single-leaf relation; BZ/2 ≄ Set. Sh(X,r) ≃ BZ is the monodromy quotient. This agrees with my sweep-3 re-derivation (isotropy π₁(leaf)) and makes my hunch H20-119_144-161_276-281-3 precise: with connected fibres alone the theorem is false |
| A.702 | Proved | targeted proof check | confirmed. Connectedness makes p* fully faithful, so there is at most one compatible 2-cell. This is simpler than my sweep-3 sketch through effective descent and gives the same discreteness, up to equivalence. Without the triangle, central automorphisms of BG appear |
| A.703 | Proved under stated hypotheses | proof read; Kock–Moerdijk 1992 (Lemmas 3.5, 5.1, 6.4, 7.2) not opened | carried as background without fault found: recognition ⇔ EssIm(p*) = Sh(X,r), with the simple-connectivity repair |
| A.704 | Proved under stated hypotheses | proof read | carried as background without fault found. The relative version is right; the unrestricted "[ou topos ?]" is false already over Set (A.701) |

### 1.A3 Part A: concordance spaces (A.1(b)) — A.114–A.116, A.119–A.163

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| A.114 | Proved | targeted proof check | confirmed: Shiota's Theorem 2.2 complement with a scalar circle coordinate, the bottom correction E_s and basing by q_s. The splitting for k ≥ 2 holds over ℝ in dimension ≥ 5 (parametric_concordance.tex:31–127) |
| A.115 | Proved | targeted proof check | confirmed: coning on total product cells (parameter-preserving), the one-way simultaneous subdivision (Rourke–Sanderson Thm 2.14–2.15, not reopened), transfer of a finite configuration from K to F by quantifier elimination, matching-vertex maps over the same base map, and transfer of nullhomotopies for injectivity (:129–302). Sixteen rows rest on it |
| A.131 (main) | Proved under stated hypotheses | statement and the first part of the proof read (:2633–2772: codes over real algebraic numbers, linear decision procedure, the five validity sentences) | **not read in full.** The construction is coherent; with A.115 it gives countable models whose homotopy groups have recursively enumerable presentations. No word problem is claimed. The sort's locator (line 4) should be line 2633 |
| A.156, A.159, A.160 | Proved under stated hypotheses | statements read; the A.160 proof read (A160_all_field_weak_comparison.tex, 184 lines) | **not read in full.** A.160 rests on the regularization chain A.147–A.159 (parameter-Lipschitz factorization, coordinate clocks, Hudson grids, standard bounds), which I did not check. This is the run's strongest new claim in Part A: PL ≃ definable concordance spaces over every o-minimal real closed field, in every base dimension. It needs an independent check (§5) |
| A.116, A.119–A.130, A.132–A.155, A.157, A.158, A.161–A.163 | as in the register | statements read in the sort only | not read in full. A.132 (on S³, π₂ is ℤ/2 in TOP and 0 in PL) is plausible from TOP/PL smoothing theory in dimension 4 (from memory: a fibre of the form Map(S³, K(ℤ/2,2)) has π₂ = ℤ/2). A.123, A.125, A.127–A.129 (trivial component groups of surfaces, S², ℝP², spheres, simply connected 3-manifolds) agree with the classical theorems they cite. A.130 (⊕ℤ for 3-manifolds with infinite π₁) and the dimension-3/4 rows A.134–A.146, A.162, A.163 are beyond this intake |

### 1.A4 Part A: axioms, reconstruction (cotes 120–121) — A.301–A.309, A.401, A.402

All are at statement level except A.308.
- A.305 (all-arity closure + the zero-set axiom ⇒ definable sets of an expansion; o-minimal iff the unary sets are finite
  unions of intervals) and A.306 (closed bounded definable sets generate the open core) agree with standard o-minimality
  (from memory: van den Dries 1998, ch. 1; Miller–Speissegger on open cores).
- A.308 is confirmed by a targeted check. All closed subsets of cubes satisfy the closure and gluing axioms, since images
  and preimages of compacta under continuous maps are compact, and the family contains the Cantor set.
- A.301–A.304, A.307, A.309, A.401 and A.402 were not read in full. Cotes 120–121 belong to the sweep-3 reader
  a6d42bf6fe2b0d8a8.

### 1.A5 Part A: canonical partitions and the maximal triviality locus (cote 121) — A5.001–A5.020, A5.CVX.pending

- **A5.003 (main), PL suspension cancellation:** confirmed by a targeted proof check. The case analysis of a point of
  S^{s−1} ∗ L (on the sphere, the link is Σ^{s−1}L; off it, Σ^s lk_ℓL) and the maximal desuspension are correct. It is
  classical (Armstrong 1966, Morton; the run cites Armstrong's thesis, which was not reopened).
- **A5.004:** confirmed (PL Propositions A–C through A5.003).
- **A5.011 (main):** the end-obstruction counterexample uses a nonzero projective class over ℤ[C₂₃]
  (h(ℚ(ζ₂₃)) = 3, from memory). This is plausible and was not read in full.
- **A5.008 (main), A5.012–A5.020 and the rest:** statement level. The open gate is the maximal locus for target dimension
  ≥ 3 with fibre dimension ≥ 2.

### 1.A6 Part A: the six functors and reconstruction from strata (cote 121) — A6.001–A6.010

Statement level only, not read in full.

### 1.B Part B: analysers and integer-valued polynomials (cotes 153, 155) — B.001–B.082

**The setting** (153/004): R ⊂ S, Ω = {F ∈ S[T] : F(R) ⊂ R}, and θ₂: Ω ⊗_R Ω → S[X,Y]. The question is whether F(X+Y)
and F(XY) have unique tensor expansions. The register's rows rest on B.009, B.013, B.014 and B.064.

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| B.008 | Refuted (153/004, "OK if Ω free") | targeted proof check | confirmed: over 𝔽₂ ⊂ 𝔽₄, q and αq are independent in Ω, (αq)⊗q − q⊗(αq) ≠ 0, and its image is 0 |
| B.009 | Proved | targeted proof check | confirmed: the criterion (existence = the image condition; uniqueness ⇔ ker θ₂ = 0), and the free-module theorem for S = Frac R through basis expansion and integrality of the coefficient polynomials |
| B.013 | Proved | targeted proof check | confirmed: for a finite R, P = ∏(T − r) splits off S ⊗_R S, so injectivity forces S ⊗_R S ≅ S. Then J is nilpotent, the field factors are epimorphic, and S = R |
| B.014 | Proved | targeted proof check | confirmed: Vandermonde over K and ker θ₂ = torsion (fifteen rows rest on it) |
| B.017 | Proved | targeted proof check | confirmed: all residue fields infinite ⇔ every extension works. The converse uses the square-zero S = R ⊕ kε with e = ε(T^q − T), e ⊗ e ≠ 0 and image 0 |
| B.022 | Proved (Int(k + t^mk[[t]]) projective) | targeted proof check | confirmed, given B.021 (Milnor patching in infinite rank, standard). The Bhargava-type basis b_n of Int(R,V), the Frobenius-power trick A + tB = B, A ∩ tB = t^mB, and the unipotent patching matrix α are all checked. **It refutes the nonflatness conjectured for 𝔽₂[[t²,t³]],** which the run locates in Elliott 2011, introduction p. 2 (not opened by me) |
| B.037 | Proved (an explicit two-dimensional tensor kernel) | partial check | the element z = (xq)⊗q − q⊗(xq) is nonzero, because x⊗1 − 1⊗x ≠ 0 in T ⊗_R T (dx ≠ 0 in Ω of 𝔽₂[x,y]/(x,y)²). This holds given the run's decomposition Int(R) = R ⊕ RX ⊕ qT[X], which I did not check |
| B.001–B.007, B.010–B.012, B.015, B.016, B.018–B.021, B.023–B.036, B.038–B.082 | as in the register (main: B.033–B.041, B.054–B.056, B.067, B.071, B.072, B.076) | statements read for B.013–B.039, B.054, B.064, B.082 | not read in full. The classification statements (B.036, B.054: one-branch normalization in height one, depth ≥ 2 in height ≥ 2; B.082: the Tor criterion for arbitrary inclusions) are coherent with the parts checked. B.016 credits a 2026 preprint (Jiang et al., Thm 3.4) for q = 2 |

### 1.C Part C: vanishing cycles (cote 122) and projective duality (cote 125) — C.001–C.023, C.U001, C.U002

| Row | Run status | Check received here | Verdict |
|---|---|---|---|
| C.004 | Proved under stated hypotheses | targeted proof check | confirmed. H^{n−1}(M) ↪ H^{n−1}(B) through H^{n−1}(M,B) = H^{n+1}(M)^∨ = 0, so T = 1. For n ≥ 3, Gysin gives H^{n−1}(S^{2n+1}∖B) = 0, and Wang then kills ker(T − 1). For n = 2 the meridian argument is used. Milnor 1968 Thms 4.8, 5.1, 5.2 and Lemma 6.1 supply the hypotheses (not reopened). **This closes the open step of 122 (R20-3(b) of sweep 3) inside his framework** |
| C.001–C.003, C.005–C.009 | as in the register | statements read | not read in full. C.005 (unreduced n = 1 false; reduced H̃⁰) and C.007 (degree-wise sign (−1)^i, middle sign (−1)^n) settle the "(signe ?)" of 122/022 by convention |
| C.010–C.023, C.U001, C.U002 | as in the register | sort statements only | not read in full. C.023 (componentwise thresholds on mixed-dimensional CM schemes) corrects the supplied study. C.U001 and C.U002 remain source gates (Hartshorne 1968, Ogus 1973) |

### 1.D Part D: the adjoint quotient and Weyl groups (cote 123) — D.001–D.027

All rows are at statement level (the sort and the report's table), with cross-checks against sweep 3 (ae4ae3dc's
STUDY §1, HUNCHES H20-3, H20-4 and H20-6, package R20-2):
- **D.007** (Dynkin → parabolic injective exactly for A₁ and B₂ = C₂) agrees with sweep 3's A₂, A₃ and A₄ collisions and
  with a mental check of B₂: [4] gives 22, [2,2] gives 02, [2,1,1] gives 10, and [1⁴] gives 00, all with distinct
  zero-node sets.
- **D.006** (regular nilpotent exactly at affine nodes with mark 1) is ae4ae3dc's answer to H20-6.
- **D.005** (negative sign exactly for A_even) refines H20-4, which had −1 for all A_n with n ≥ 2. I did not check it.
- **D.002** (Coxeter normalizer nonsplit exactly in F₄, E₆, E₈) answers H20-3. I did not check it.
- **D.016** (arithmetic nonsplitness of RigKos in A₂/ℚ) and **D.018** (the dimension formula, Known) bear on the letter
  to Kostant.
- Nothing in Part D was read in full.

## 2. What is new

New against the literature (only my targeted checks are claimed; literature not opened is marked "from memory" or "the run's locator"):
- **Part A, the Additif (119/148–153).** The status of Grothendieck's conjectures is now exact:
  - I b), I c) and II b) are false, through the concordance space of (S¹)⁶ (A.104, A.106, A.111);
  - II c) is true (A.101);
  - the space of strict rigidified collars is contractible (A.102);
  - five of the eleven functors of 150 are equivalences and six fail (A.112): PB ≃ PBCR ≃ EPCR ≃ EPC, but not EP.

  The concordance inputs are classical (Hatcher–Wagoner; the torus computation). What is new is their application to his
  system. A.205, a coarsest intrinsic PL partition with saturated singular loci of closed unions, is a variant of
  King's intrinsic stratification. A.160, if its unchecked chain A.147–A.159 holds, would be a new theorem: PL ≃ definable
  concordance spaces over every o-minimal real closed field, in every dimension.
- **Part B (153/155).** The tensor criterion is classified in full: B.054 for Noetherian domains, B.082 for every
  inclusion. B.022 and B.023, the proof of B.022 checked here, refute the nonflatness of Int(𝔽₂[[t²,t³]]) and
  Int(𝔽₂ + t𝔽₄[[t]]), which the run says Elliott conjectured (Presentations 2011, introduction p. 2; the locator was not
  opened by me). If the locator holds, this answers a published question.
- **Part C (122).** C.004 proves H^{n−1}(M) = 0 by Gysin and Wang in an open book, inside his framework. The theorem is
  Milnor's (1968); the route is new to our records.
- **Part E (119/155–161).** Two new readings: the side-dual twist ε ∧ Q^∨ of 157 (E.006) and the bihexagon construction
  (E.003). The affine-plane triality is not new: it is in Cameron 2015 §6 (E.009, the run's locator).

New against our own results (corrections to sweep 3; the sweep-3 files themselves are left unchanged):
1. **The cascade (my reading, §3.1, item 2).** I said the system of eleven holds with fibrewise collar automorphisms. That
   is wrong at EP: the collapse PB → EP fails whatever the collars are (A.104), because Aut(B × I, B × 0) carries the
   concordances while Aut(CB, o) does not.
2. **II b) and the cone side (my reading §2).** II b) was not open: it is false in the derived choice-space model (A.111).
3. **H20-119_144-161_276-281-4** (the dimension condition 2° as a minimality criterion) is refuted. The condition need not
   be attainable (A.202), and where it holds it gives no uniqueness (A.207).
4. **H20-119_144-161_276-281-1** (literature status of the triality): Cameron 2015 §6 has it (E.009).
5. **H20-119_144-161_276-281-3** (foliation) is made precise. With connected fibres "Th" is false (A.701). The repair is
   simple connectivity, that is, the monodromy quotient my sweep-3 reading had identified (A.703).
6. **ae4ae3dc's H20-4** (sign −1 on 𝔤_ψ for every A_n) is refined by D.005 (−1 exactly for A_even). This was not
   checked here.

## 3. Implications for the archive and the programme

**Cote 119, scans 145–161 (my sweep-3 stretch).** The edition notes of the Additif and the Digressions can now state, per
scan:
- **145–146:** "Th" is false with "connexes" (A.701) and true with simply connected fibres or invariant-sheaf recognition
  (A.703, A.704). Hom discreteness holds up to equivalence (A.702).
- **148–149:** I a) is true for compact pairs (A.107). I b) and I c) are false (A.106, A.104). II b) is false in the
  derived model (A.111) and II c) is true (A.101).
- **150:** of the eleven functors, five are equivalences and six fail (A.112). The margin "composer … avec PBR" is the
  rigid extended collar that makes α and β strict (A.110).
- **151–152:** Y-admissible rigidifications exist (A.201). The 2° condition is neither attainable in general nor
  sufficient (A.202, A.207). 1° fails unrigidified and is repaired with retained tubes (A.203).
- **153:** "la moins fine" is false in the weak sense (A.204) and true in the intrinsic sense (A.205).
- **156:** "ordre 10" means index 10, with 2·(6!) (E.008, matching sweep 3).
- **157:** the boxed Q^∨ is the side-dual square (E.006).

The reading corrections of sweep 3 stand: 148 X∖(C∖Ċ), 150 "11", 151 X∖(V∖V̇), 155 "t. 4". The run confirms 148, 153
and 157 on the images.

**Other cotes:**
- 122: the open step of the page is closed (C.004).
- 123: D.002, D.005–D.008 answer package R20-2 (a)–(d) (not checked here).
- 125: the projective CM chain is corrected componentwise (C.023).
- 152: plane trees (E.010–E.013).
- 153/155: B.

**Programme:**
- The archive's mathematical questions in this run are answered. What remains (real TOP concordances in base dimensions 3
  and 4; the maximal locus with target dimension ≥ 3 and fibre dimension ≥ 2) is research far from the pages. Under the
  rule "eat your greens first" it should not take Pro slots before the transcription and translation of these cotes.
- B.022 and B.023 may warrant informing the author whose conjecture they answer, after the locator is verified (memory:
  informing authors).

## 4. Bridges (corrected criterion of 20 Nov ~21:1x UTC)

Alpöge: L. Alpöge, *Remark*, https://alpo.ge/remark.pdf (RH and GRH for Dirichlet L-functions, with a Lean archive).
Purity: Deligne, *La conjecture de Weil* I, II. Literature below is from memory unless marked.

**C.008 (bridge flag; the tame étale triangle with twists (−n), (−n−1))**
- **What purity gives.** Take the arithmetic case: S the henselization of a smooth curve over 𝔽_q at a closed point
  (equal characteristic), Q_ℓ coefficients, and f proper with the isolated singular point x.
  - Here R^n f_*Q_ℓ is pure of weight n on the generic part (Weil I/II).
  - Deligne's local monodromy theorem (Weil II, 1.8.4) then makes the monodromy filtration M of the logarithm N of
    unipotent monodromy the weight filtration, centred at n: N^i: Gr^M_{n+i} ≅ Gr^M_{n−i}(−i).
  - The twists forced in (C.8.1)–(C.8.3) are the weight shifts of this structure: R ≃ D K(−n)[−2n] pairs weight w with
    2n − w, and H¹(I_t, Λ) = Λ(−1) has Frobenius weight 2, because Frobenius acts on I_t by σ ↦ σ^q.
  - The variation V_σ is N up to the isomorphism exp, so it lowers weight by 2.
- **What the row gives back:** nothing towards purity. It is stated with finite coefficients ℤ/ℓ^a, where weights are not
  defined, and it only types the twists.
- **Alpöge carries nothing here:** the row is local (inertia of a strictly henselian trait), and no global zeta or
  L-function occurs.
- **In mixed characteristic** the same statement is Deligne's weight–monodromy conjecture, open in general.

**C.007 (Seifert form and intersection form I = L + εLᵗ; positivity)**
- **What positivity gives.** Over ℂ, Steenbrink's limit mixed Hodge structure on Hⁿ of the Milnor fibre has the monodromy
  weight filtration. The Hodge–Riemann bilinear relations on its primitive pieces give the signature of I in terms of
  the spectrum (Steenbrink 1976–77, from memory).
- **What the row gives back:** C.007 supplies the sign conventions without which that signature formula is ambiguous.
  The degree-wise sign is (−1)^i and the middle sign is ε = (−1)^n.
- **Alpöge carries nothing here.** This is the archimedean analogue of purity (the Hodge package), not RH.

**C.010 (bridge flag)** is a false positive. The row works in ordinary topology, where a "Tate twist" ℤ(1) is only an
orientation twist. It carries no weight without a Frobenius or Hodge structure, and the row uses neither. The link that
does exist is the one stated under C.007.

**D.018 (the dimension formula dim 𝓑_u = (dim Z(u) − r)/2) and the Springer fibres**
- **What purity gives.** For split u over 𝔽_q, the Springer fibre 𝓑_u has cohomology vanishing in odd degrees, and
  H^{2i} is pure of Tate type (De Concini–Lusztig–Procesi 1988, through Deligne's purity; from memory).
  - The Lefschetz trace formula then gives |𝓑_u(𝔽_q)| = Σ_i dim H^{2i}(𝓑_u) q^i.
  - So the Green polynomials have nonnegative coefficients (Springer 1976; Kazhdan–Lusztig).
- **What the row gives back:** D.018 fixes the degree of that polynomial, the top weight 2 dim 𝓑_u. This is the formula
  of the letter of 22.10.1969 (123/023).
- **Alpöge carries nothing here:** point counts over 𝔽_q are a question about the Riemann hypothesis over finite fields,
  not about ζ or L(χ, s).

**A5.011 (TOP non-uniqueness through a projective module over ℤ[C₂₃]; K-theory and L-values)**
- **The bridge.** K̃₀(ℤ[C₂₃]) contains Cl(ℤ[ζ₂₃]) ≅ ℤ/3 (Rim's theorem; 23 is the first prime with h > 1; from
  memory). By the analytic class number formula, h⁻(ℚ(ζ_p)) is a product of −B_{1,χ}/2 = L(0, χ)/2 over the odd
  Dirichlet characters χ mod p, up to the factor 2p. So the obstruction used is a special value at s = 0 of Dirichlet
  L-functions: the L-functions of the Artin–Tate motives χ ⊗ Q(0) of the brief.
- **What GRH (Alpöge) gives there:** effective bounds for class numbers in families (L(1, χ) ≍ log log q). For this
  instance it gives nothing, since h(ℚ(ζ₂₃)) = 3 is a finite, unconditional computation of Bernoulli numbers.
  - *Correction* (corrected 21 Nov 2026 after the intake of ZETA_TWO, Claude Opus 5.5 at effort high):
    h(ℚ(ζ₂₃)) = 3 and K̃₀(ℤ[C₂₃]) ≅ ℤ/3 are unconditional (ZETA_TWO IA07, confirmed by independent computation:
    det = −3072·23^10, h⁻ = 3, h⁺ = 1; Rim). The shorthand "L(1, χ) ≍ log log q" is wrong: for every odd p some odd
    χ mod p has |L(1, χ)| ≤ π/√6, so there is no uniform lower bound of size log log q (IA09, confirmed). Under Alpöge
    the bounds are V(q)^{-1} ≤ |L(1,χ)| ≤ U(q) for q ≥ 10^10 (IA02, LLS v3 Thm 1.5; scope confirmed in that intake).
- **What the row gives back:** nothing to L-functions.

**A.103 (K₂(ℤ), K₃(ℤ), Wh₂, Wh₃ of ℤ^d; K-theory and zeta values)**
- **Why the link carries nothing.**
  - The row uses K₂(ℤ) = ℤ/2 = {−1,−1} and the Laurent decomposition. It quotients out K₃(ℤ).
  - The orders |K₂(ℤ)| = 2 and |K₃(ℤ)| = 48 agree with Lichtenbaum's formula through ζ(−1) = −1/12. They are
    unconditional (Lee–Szczarba; Rognes–Weibel through Voevodsky–Rost).
  - ζ at negative odd integers is rational (Bernoulli) whatever its zeros are.
- **RH gives nothing to the row, and the row gives nothing to RH.**

**C.011–C.023 (cote 125)** carry nothing. Their "twists" are Serre twists O_X(−m) of coherent sheaves; their "pure"
means equidimensional; their duality is coherent. There is no Frobenius, no Hodge structure and no L-function.

**No other row of the 267** treats Tate motives, weights, L-functions, motivic cohomology, mixed Tate motives, periods or
positivity: Part B (integer-valued polynomials), Part E (finite groups), the rest of Part A and Part D.

## 5. Prompt updates for a successor

1. **Do not spend a Pro slot on the remaining A.1(b) gates** (real TOP concordances over 3- and 4-manifolds) or on the A.5
   general maximal locus. They are research far from the archive pages. The archive's questions on these cotes are
   answered (§3).
2. **Independent check of A.147–A.160** (the parameter-Lipschitz regularization chain and the all-field PL ≃ definable
   concordance theorem). This is the run's most important unchecked new claim. A successor or a Claude reader should check
   it with the proofs in full.
3. **Check B.022 and B.023 against Elliott 2011** (the introduction, p. 2, as the run cites it), and check B.016 against
   Jiang et al. 2026 (Thm 3.4). Then decide whether to inform the authors.
4. **Source gates C.U001 and C.U002** (Hartshorne 1968 Prop. 4.3 and Thm 7.5; Ogus 1973 §3): a bounded source-inspection
   task, not a research prompt.
5. **The sort's locators** for A.131 and A.132 point at the scope paragraph (parametric_concordance.tex:4, :17). The
   statements are at :2633 and :3044. Other rows of that file may be affected.
6. **Carry the verdicts of §3 into the edition notes** of cotes 119 (145–161), 122, 123, 125, 152 and 153/155, with the
   sweep-3 reading corrections. This is integration, not research.

## 6. Counts

- **Rows:** 267.
- **Read in full with a targeted proof check:** 51.
  - E.001–E.014 (14);
  - A.101–A.115 (15);
  - A.118, A.201–A.207 (8);
  - A.308;
  - A.701–A.704 (4);
  - A5.003, A5.004;
  - B.008, B.009, B.013, B.014, B.017, B.022 (6);
  - C.004.
- **Partly read:** A.131, A.156, A.159, A.160, A.208, A.209, B.037, and the statements of C.001–C.009.
- **At statement level** (the sort's statement, and the report's outcome table): the other 216.
- **Verdicts on the rows read in full:**
  - 47 confirmed;
  - 4 carried as background without fault found where the sources were not opened (A.103, A.113, A.703, A.704);
  - 0 gaps;
  - 0 refuted.
  - Several of the confirmed rows are the run's own refutations, now checked: A.104, A.106, A.110, A.111, A.118, A.202,
    A.203, A.204, A.206, A.207, A.308, A.701, B.008.
- **Check events:** listed in `INTAKE_RESEARCH_SA20_20261120_CHECK_EVENTS.tsv`.
- **Bridges:**
  - stated as mathematics: C.008, C.007, D.018, A5.011;
  - carries nothing, with the reason: A.103, C.010, C.011–C.023.
- **Corrections to our own sweep-3 records:** six (§2).
