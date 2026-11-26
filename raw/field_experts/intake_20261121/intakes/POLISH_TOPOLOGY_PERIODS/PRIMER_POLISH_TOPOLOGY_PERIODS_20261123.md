# Primer: the mathematics of POLISH_TOPOLOGY_PERIODS as of checkpoint 26 (24 Nov 2026; updated from the cp19 primer)

**Checkpoint 26** (captured 23:33 UTC on 23 Nov) changed only Paper 2, now 250 pp. Papers 1 and 3-7 are byte-identical to checkpoint 19. The cp19 primer is kept in the integration backup folder.

This primer is by agent a9e9559d (Claude Opus 5.5 at effort high), for the main session to read after a compaction. It restates; it does not develop.

The run is prompt 91 and its continuation 91b, both GPT-6 Astra (ChatGPT Pro mode). The continuation started from checkpoint 13 at 13:48 UTC. Checkpoint 19 was saved at 18:18 UTC; checkpoints 14-18 never reached us. Only Papers 1 and 2 changed after checkpoint 13. The cp13 primer is kept in the integration backup folder.

**Papers at checkpoint 19:** `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_19_20261123T1818Z_unzipped/papers/`. The cp13 locators below still hold for Papers 3-7.

**Papers:** `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped/papers/0N_*/main.tex`. Labels below are TeX labels.

**Check labels**, as recorded in our intakes:
- `[cp26-TPC]`: targeted proof check by our cp26 intake;
- `[cp19-TPC]`: targeted proof check by our cp19 intake;
- `[cp12-TPC]`: targeted proof check by our cp12 intake;
- `[cp13-TPC]`: targeted proof check by our cp13 intake;
- `[cp13-COMP]`: computation by our cp13 intake;
- `[run]`: accepted by the run only;
- `[stmt]`: read by us at statement level only.

## Paper 1. Gluing Grothendieck's tubes (cotes 150-151), 56 pp.

- **thm:tubes, open-tube descent `[cp12-TPC]`.**
  - Setting: a poset I and a locally finite closed family (X_i) with X = ∪X_i, monotone in i, and X_i ∩ X_j = ∪_{k≤i,j} X_k.
  - Put R_i = ∪_{i≰k} X_k and W_i = N_i ∖ R_i, for open neighbourhoods N_i ⊃ X_i.
  - Statement: the W_i cover X, and the truncated Čech diagram of sheaf topoi (degrees ≤ 2) has bicolimit Sh(X). As synchronized pro-objects it is the constant pro-topos.
  - Mechanism, the cover: I_x = {i : x ∈ X_i} is finite and downward directed, so it has a least element i_0; then x ∉ R_{i_0}.
  - Mechanism, the rest: ordinary descent (Stacks 00AL, 00AN).
- **thm:stones, the prescribed incidence pieces do not suffice `[cp12-TPC]`.**
  - The chains {0} ⊂ R ⊂ C and {0} ⊂ R^2 ⊂ R^4.
  - Mechanism: build sheaves from functors on the cell poset o < p, n < u, d. Choose ray-to-u maps equal to 0 on V_02 and to 1 on V_12.
  - Every piece of the diagram sees only real cells or only nonreal cells, so the data agree on it.
  - A global sheaf would force both values on the punctured disk V_02 ∩ V_12, which is not a piece.
- **Further statements `[stmt]`:** thm:membership (pointwise groupoid criterion), thm:graph-meets, thm:truncation (exodromy; known in substance), thm:higher-comparisons, thm:exit-deployment, cor:holink-pushout, thm:singular-fibers (proper Hurewicz fibrations onto S^1 with a non-manifold fibre, PL and smooth).
- **Run status:** all 74 statements accepted at checkpoint 19. B6.3 was resolved as σ_1 from the repeated primary-source relation. The paper has 55 pp.; there is still no "Proof overview" section.

## Paper 2. Collars, cones, concordance and polynomial operations (cotes 119, 150, 153), 169 pp. at checkpoint 19

The paper now has 23 input files. The topology part covers concordance components; the algebra part covers integer-valued polynomials.

### New at checkpoint 19: concordance spaces

All of these are `[stmt]` and `[run]`, with separate frozen reconstructions in the run. Notation: P(M) is the concordance (pseudoisotopy) space of M, with the bottom fixed and the top free.
- **pl_components_six.tex, thm:component-followup-all-PL-six.**
  - Statement: for every compact connected PL manifold M of dimension ≥ 6, stabilization gives π_0 P_PL(M) ≅ E(M) ≅ E(K) for any finite complex K ≃ M; no smoothing is assumed.
  - Mechanism (from the ledger): the Hatcher-Wagoner-Igusa sequence in the smoothable case, then a smoothable three-handle core and the stable square for nonsmoothable M (Pedersen 1975, Appendix 2, p. 149).
- **topological_three_sphere.tex, thm:three-sphere-higher-top-discrepancy.** P_TOP(S^3) ≃ ΩQ_4. π_0 = π_1 = π_2 = 0 for P_PL(S^3), while π_2 P_TOP(S^3) = Z/2, so PL → TOP is not a weak equivalence for S^3.
- **low_surface_components.tex, thm:low-concordance-components.** π_0 P_PL(B) = 0 for manifolds of dimension 0 or 1, balls, compact orientable surfaces other than S^2, and closed nonorientable surfaces other than RP^2.
- **elementary_extensions.tex, thm:elementary-extension-marked-automorphisms.** Marked definable automorphism spaces, and P_def(B), are invariant up to weak equivalence under elementary extension of the o-minimal structure.
- **outer_faces.tex.** The outer-face space has the homotopy type BP_TOP(B). There is a rational semialgebraic T^6 loop with no definable filling with local face witnesses.
- **The A130 subgroup.** An infinite-rank free abelian subgroup for closed orientable 3-manifolds with infinite π_1, via Lin-Xie-Zhang.
- **Open:** A124 (dimension-five injectivity), A135-A137.

### New at checkpoint 26: more concordance and partitions

All of these are `[stmt]` and `[run]`, from the Paper 2 abstract and ledger.
- **Dimension five:** stabilization on concordance components is surjective. Injectivity (A124) remains open.
- **Casson-Sullivan homomorphism:** surjective for oriented 3-manifolds with finite π_1, by Galvin's relative construction and the Hambleton-Milgram-Taylor-Williams surgery formula. It vanishes on the standard T^3.
- **RP^3:** joint odd germs identify the full component group as an abelian kernel of forgetting antipodal symmetry.
- **Comparisons:** ordinary TOP concordances are compared with joint PL families in low dimensions (four-dimensional comparison, realization and supported traces).
- **Partitions:** an intrinsic PL partition with saturated singular loci need not have conical charts (weak-filtration counterexamples). Coarsest embedded smooth partitions exist for arbitrary semialgebraic sets but depend on the embedding: the cusp t ↦ (t^2, t^3) versus the interval, `[cp26-TPC]`.
- **Tube results** A202, A207-A209; a mapping-cylinder theorem; boundary-bundle categories.
- **Open:** A124; A401/A402 and A701-A704 (comparisons pending); the seven-axiom comparison.

### New at checkpoint 19: algebra

- **thm:int-analytic-free and prop:analytic-one-branch.** Int(R) is free of countably infinite rank for every one-dimensional analytically irreducible Noetherian local domain; the tensor maps are isomorphisms and the plethory is unique. This is the S20 statement.
  - Credit: Elliott announced freeness for F_2[[T^2,T^3]] on MathOverflow 75202 on 26 Dec 2013, without a published proof.
  - Our posted note hexagon:2611.00937 v1 lacks this credit; v2 is in reports_20261123/s20_note/.
- **prop:elliott-explicit-witnesses `[cp19-TPC]`.** For the cusp: g = f/t^2, h_2 = ((g^2+g)/t)^2, h_1 = g + t h_2, and X^2 + X = t^2 h_1 + t^3 h_2. For the residue extension: k_2 = q + q^2, k_1 = α q^2 + α^2 q, and X^2 + X = t k_1 + α t k_2.
- **thm:nonflat-forest-plethory `[cp19-TPC]`.**
  - Construction: S = F_2[x_v, y_v]/(x_v^2, y_v^2, y_v − x_v y_{v0} y_{v1}) over countably many binary trees, with deg x = −1, deg y = 1, and R = S_{≤0}.
  - Mechanism: R → S is an epimorphism (Lazard-type balancing). (R :_S N^k) = R. Q = X^4 + X^2 kills R. The Hermite splitting gives Ω(R,S) = R[X]_{<4} ⊕ Q·S[X], so all tensor maps are isomorphisms, while S is not flat (a faithfully flat epimorphism would be an isomorphism).
- **The arbitrary Noetherian base criterion** (binary injectivity forces all tensor isomorphisms, characterized by effective local coefficient rings and one-branch completions) and **the valuation-conductor criteria** (B075-B078): `[run]`. B059's literal ambient clause is refuted by an infinite-residue example.

### Collars and cones (unchanged since checkpoint 13)

### Collars and cones

- **result-1, fibrewise collar and cone automorphisms are contractible** (Alexander trick) `[stmt]`.
- **result-2, parametrized strict collars are contractible** `[stmt]`.
- **result-7: Col(X,B) ≃ BP_def(B)** `[stmt]`. Grothendieck's I b) is false for B = (S^1)^6.
- **result-3, the torus** `[stmt]`.
  - Statement: π_0 P_CAT((S^1)^d) = F_2[t^{±1}]/F_2·1 for d ≥ 6.
  - Source: Igusa, LNM 1046 (1984), Thm 8.a.2, pp. 149-150, dimension ≥ 6.
- **result-12, the strict-cone choice space has the homotopy type BP_def(B)** `[stmt]`. So II b) is false, and II c) holds for base-fixed rigidifications.
- **result-13, the eleven arrows `[stmt]`.**
  - Equivalences: PB → PBCR, PB → EPCR, the identity, PBCR → EPCR, EPCR → EPC.
  - Failures: PB → EP (both), PBCR → PBC, PBC → EPC, PBC → PB, EPC → EP.
- **cp13 convention, result-cone-parametrizations `[cp13-TPC]`.**
  - Statement: with ψ_0 base-fixed, the base-setwise parametrizations of a fixed cone form G_Y × Homeo_def(Y).
  - Mechanism: h = ψ_0^{-1}ψ, a = h|_Y, k = h∘C(a^{-1}) ∈ G_Y.
  - Consequence: under the literal base-setwise convention, A.105, A.109, A.111 and A.112 are refuted. The normalized replacements `P02-A1xx-normalized` (notes/paper02_collar_refined_statements.md) require base-fixed parametrizations; the outcome table is unchanged `[run]`.

### Comparison and partitions

- **A.160, PL = definable concordance families over every o-minimal real closed field** `[run]`.
- **result-14, the intrinsic PL partition** `[run]`. The King 1985 comparison is open.

### Polynomial operations

Notation: Ω(R,S) = {f ∈ S[X] : f(R) ⊂ R}, and θ_n : A^{⊗n} → Ω_n.

- **result-20 (B082), the universal coefficient-syzygy criterion** `[stmt]`, `[run]`.
  - Statement: for any unital inclusion R ⊂ S, form C = ∪_d (R :_S D_d(R)) with D_d the Vandermonde ideal.
  - The first test is that R → C be an epimorphism, which is equivalent to a finite matrix presentation c = YMZ.
  - Then Tor-invariants U_q, V_q, W_q of F = C[X] and E = im(F → App(R, C/R)), with transgressions δ_0, δ_1, decide unique coaddition and comultiplication.
- **result-28, the infinite-rank patching lemma `[cp12-TPC]`.**
  - Statement: if R = V ×_D k with V → D onto and α ∈ Aut(D^{(I)}), then M_α ⊕ M_{α^{-1}} ≅ R^{(I⊔I)}.
  - Mechanism: the Whitehead identity diag(α, α^{-1}) = E(α)E(−α^{-1})E(α)W, whose column-finite elementary lifts are automorphisms over V.
- **result-29, the finite-conductor theorem `[cp12-TPC]`.** Posted as hexagon:2611.00937, with Int(R) free.
  - Statement: if V is a DVR with finite residue field and π^m V ⊂ R ⊂ V, then Int(R) is projective, hence free (Kaplansky).
  - Step 1: B = Int(R,V) has a Newton basis, built from a minimizing ordering (Bhargava).
  - Step 2: B/JB ≅ the locally constant functions R → V/J. The digit polynomial δ = (X^Q − X)/π satisfies v(δx − δy) = v(x − y) − 1. The indicators are ∏(1 − (δ^j − c_j)^{Q−1}), raised to the power Q^m.
  - Step 3: A/JB ≅ the locally constant functions R → R/J, which are free (choose one child class at each level).
  - Step 4: A is the patching of the two along α; apply result-28.
  - Corollary (S20 note): Int(D) is free for every one-dimensional analytically irreducible Noetherian local domain. This refutes Elliott's Conjectures 2.10, 2.15 and 2.17 (Comm. Algebra 39 (2011), pp. 11-12 of arXiv:1105.0142v1).
- **result-30, the branch criterion** `[stmt]`. For a one-dimensional Noetherian local domain with finite residue field and finite normalization T, all θ_n are isomorphisms iff T is local.
- **result-51** `[cp12-TPC]`. Elliott's two rings are flat (indeed free). Explicit witnesses are in the S20 note §8.

### Corrections and open rows

- **Correction for authors:** the Elliott conjectures (CORRECTIONS_FOR_AUTHORS.md). It resolves a conjecture and is not an erratum.
- **Open:** 195 rows unverified; King 1985.

## Paper 3. Strong transcendence (cote 18, sheet 11), 84 pp.

- **thm:main, the dimension table `[cp12-TPC]`.**
  - Setting: N = M ⊕ c^*M, with joint group J ⊂ G × G; N_2 is the kernel of the first projection. Put v = dim N_2 − dim(N_2 ∩ B^-), with 0 ≤ v ≤ u.
  - Statement: the image-closure dimensions of α, β, γ, φ, ψ, (α,β) are g, u, b+v, u, u+v, g+v. These bound the transcendence degrees unconditionally (André's motivated torsor) and equal them under period genericity of N.
  - Consequence: the prediction holds iff v = u; if v < u, five predicted degrees are false.
  - Mechanism (lem:parabolic, prop:images, cor:central): B_J = J ∩ (B × B^-), and B_J^0 → B^0 is onto with kernel of dimension n_B. ψ-fibres are B_J-cosets. γ-fibres are S_γ = J ∩ (U × B^-), of dimension u + n_B. (a,s)-fibres are S_K = J ∩ (1 × B^-).
- **cor:real, the counterexample `[cp12-TPC]` and recomputed.**
  - Statement: h^1(y^2 = x^3 − x + 1) over Q has (g,b,u,v) = (4,3,1,0).
  - Mechanism: real Frobenius gives conj(F) = F_∞(F), so trdeg k(γ) ≤ 3 < 4 and trdeg Q(ψ) ≤ 1 < 2.
- **thm:other `[stmt]`.** Five items: Howe's ordinary curve at 5; the Cartier restricted-Lie formula D_a^p = H_p D_a − (K_p + aH_p)V; a non-geometric (3,0)+(0,3) Hodge structure; integral Betti functors; Z[√−5] CM.
- **Refinement:** B.4.1 (equalizer normality only under centralization and compatibility).
- **Correction for authors:** Bhowmik-Pathak Thm 1.11 `[cp12-TPC]`. Counterexample: τ = i, f = E_4, g = j, F_0 = 1 + E_2E_6/E_4^2.
- **Open:** 52 rows.

## Paper 4. Conformal surgery and algebra (cotes 66-68), 40 pp.

- **thm:single-cap, one positive cap determines all lengths, cusps included `[cp12-TPC]`.**
  - On a common cap, F_i = w^{i a_i}, so dF_2/F_2 = r · dF_1/F_1 on the universal cover.
  - The holonomy is faithful and free of rank ≥ 2, so it fixes no pair; hence F_1 has a simple zero or pole at an ordinary point, and r = ±1.
  - Then F_2 = cF_1^{±1}, and the double-pole coefficients (1 + λ^2)/2 agree, with λ = ℓ/2π.
- **thm:radius-map `[stmt]`, `[run]`.**
  - Statement: for active lengths, x_i = (ℓ_i/2π)^2 ↦ log r_i is a real-analytic diffeomorphism onto the convex set {y : a·y < H_X(a)}, where H_X is the Strebel/Liu weighted reduced-modulus support function.
  - It is the gradient of a strictly convex function.
- **thm:radius-limit `[stmt]`; the three-point cases `[cp13-TPC]`, `[cp13-COMP]`.**
  - Statement: as the lengths diverge in a fixed ratio a, the caps converge to the characteristic discs of Q_a.
  - On the sphere with marks 0, 1, ∞: the slit domain, of radius 4; the half-plane, of radius 1; the lens |z| < 1, Re z < 1/2, of radius 4/(3√3).
- **thm:collar-shape (new at cp13); the equation clauses `[cp13-TPC]`.**
  - Statement: after removing a collar, g' = e^{2u}g with Δu = e^{2u} − 1 and ∂_n u = k_g; the area is −2πχ; constant-width cuts give u > 0 and length > L·cosh d.
  - A sign-change family exists: a_1 = 1 + ½cos(2πns/L_1).
  - There is a numerical example on the 2π pant with n = 10^4, ε = 10^{-14}.
- **thm:eigen `[cp12-TPC]`.**
  - Statement: R = Z[x,y,z]/(x^2 + yz − 1), σ = (x y; z −x). σ^2 = 1, but the eigenmodules are not invertible: their fibre at (2, x−1, y, z) is F_2^2.
  - Correct hypotheses: a Dedekind base, or 2 invertible and Spec R connected.
- **thm:comparisons, thm:algebraic-summary `[stmt]`.** Lie comparison counterexamples over F_2 and Z; local Hurewicz; Artinian descent; the double-fibre Picard functor; Pauly's Nori example; the subject-21 henselian results.
- **Open:** 292 rows; the nodal-q reconstruction and the abelian-fourfold input are hypotheses; four collar scopes are held.

## Paper 5. The relative-position surface (cote 154), 41 pp.

- **thm:main `[cp12-TPC]` (counting only).**
  - Statement: for n tame pseudolines, not all concurrent, X_2 ≅ #^{n+1+4Σ k c_{2k+1}} RP^2. Here c_j counts relative positions through exactly j old vertices.
  - Counts: f_2 = F(1), f_1 = 2F'(1) + 2b, f_0 = F'(1) + b, so χ = F(1) − F'(1) − b.
- **thm:identities `[stmt]`.** F(−1) = 1 − n and F'(−1) = b, from the extension-complex comparison and Sturmfels-Ziegler 1993.
- **thm:examples `[stmt]`, `[run]`.** Two six-line arrangements with c_3 = 4 and c_3 = 10 give 23 and 47 crosscaps.
- **thm:comparison `[stmt]`.** B(M) ≃ #^{n+1} RP^2; the dual quadrangulation embeds.
- **Open:** C.06, identity with Grothendieck's gluing.

## Paper 6. Tensor divided-power categories (cote 137) and clean dessins, 31 pp.

All `[stmt]` and `[run]` (43 rows accepted by the run).
- thm:bare: invertibility of α_{q,0} is independent of the bare axioms, and composition fails (over F_2 and F_3).
- prop:coherence: the counit and coassociativity equations give a category, and conversely.
- thm:walking: the all-ring essential image is the kernels of δ_L(C). Known for targets with kernels (Hua 2611.00125v2, pp. 165-166).
- thm:reconstruction: the cosimplicial ring Map(X_n, Z) is recovered from the natural divided-power action.
- thm:rank-perfect: uniform rank bounds; perfect = pseudo-coherent with bounded Tor amplitude (standard).
- thm:dessins: the cellwise holomorphic groups are nontrivial only for the one-loop sphere, the n-ray sphere, and the Z/4g map with C_2. The combinatorial core is Mulase-Penkava 1998.

## Paper 7. Interval supports and oriented maquettes, 45 pp.

All `[stmt]` and `[run]`.
- thm:interval: Σ(M(L)) is orthomodular iff L is a conditional lattice (finite L). It is Boolean iff the nonisolated elements form a chain (arbitrary L).
- thm:tests: Boolean and atom tests for orthosets. The Boolean part is Jenča 2026, Thm 3.2.
- thm:events: distributive principal ideals correspond to binary-conflict prime event structures.
- thm:cw: oriented regular CW data, in all dimensions (Björner 1984 plus a signed-boundary argument).
- Refuted: extension uniqueness, refined by SA21-B-extension-Zorn and SA21-B-deployment-unique.
- Open: Jenča's Corollary 4.5 published page; the contre/atelier bridge; 18 unverified rows.

## Open rows, totals at checkpoint 19 (cp26 update below)

| Status | Rows (of 1,028) |
|---|---|
| original rows accepted (by the run's ledger) | 436 |
| supplemental results accepted (outside the 1,028) | 9 |
| in-scope original rows open | 591 |
| excluded by the user | 1 (D002) |

QUESTIONS.tsv per paper:

| Paper | Proved | Unverified | Other |
|---|---|---|---|
| 1 | 74 | — | — |
| 2 | 132 | 131 | scoped, refuted, refined and open rows besides |
| 3 | 126 | 52 | — |
| 4 | 22 | 292 | 38 scoped |
| 5 | 17 | — | 8 scoped |
| 6 | 43 | — | — |
| 7 | 21 | 18 | 43 scoped, 2 refuted |

**At checkpoint 26:**
- 463 original rows accepted, 12 supplemental results, 564 open, 1 excluded.
- Paper 2 in QUESTIONS.tsv: 161 proved, 106 unverified.

**Corrections for authors** (CORRECTIONS_FOR_AUTHORS.md):
- New at checkpoint 26: Galvin, Compositio 2026 (Lemma 4.9's Sq inequality reversed; Prop. 2.23's ΣX_+ should be Σ(X/∂X)), `[cp26-TPC]`.
- New at checkpoint 26: Galvin's thesis (Q_8 missing from the case list), `[cp26-TPC]`.
- New at checkpoint 26: Orson-Powell-Randal-Williams (Remark 8.2, k ≥ 0 should be k ≥ 1, checked at the source; the L^s/L^q target notation).
- New at checkpoint 26: Stasica 2003 (a proof-step counterexample), `[cp26-TPC]`.
- New at checkpoint 26: Delfs-Knebusch 1984 (notation).
- Elliott, as before.
- Elliott: a resolution of his conjectures, with credit for his 2013 announcement.
- Bhowmik-Pathak, Thm 1.11.
- Boyle-Chen, Thm A.6: the displayed generator is not end-fixing; the group has order ≤ 2 (`[cp19-TPC]` at the source).
- Bonahon's 2000 draft, Thm 3.12.
- Walsberg, Lemma 7.23 proof.

The gates per paper are listed above; the finishing items are in `claude_math_notes/PROMPT_UPDATES.md`, last section.
