# New literature, 14-24 November 2026: what was announced or posted, for the intake pile

Written 24 Nov 2026 by Claude Opus 5.5 at effort high (agent ad02aef1504b7f644), for the main session 329fb1e6
(Claude Opus 5.5 at effort max) and the Fable conference on the pile. Rows in `LITERATURE_20261124.tsv`; running notes in
`<local>/Documents/agent_notes/ad02aef1504b7f644_NOTES.md`.

**How this was searched.** The two AI laboratory repositories through `gh api` (contents, history.md, commits since
1 Nov); the Hexagon API (`/api/v1/works`, every work published 14-24 Nov: 531 works, listed in the appendix); the arXiv
API for every paper first posted 13-23 Nov with primary or cross-list category math.AG, math.NT, math.AT, math.KT, math.CT,
cs.CC (596 papers, all titles read) and, for named problems only, 20 further mathematics categories (2,435 papers, filtered
by title and abstract for "conjecture / problem / counterexample / proof of"); the ECCC 2026 listing; DeepMind's blog;
Terence Tao's blog, the Lean community blog, Wikipedia's pages on the Millennium problems and on Alpöge's proof, and web
searches (standard and extended) for named problems. **Every item below was opened at its source** (paper, abstract page,
repository README or TeX); where only the abstract was read, the status says so. Nothing was checked mathematically here:
"status" reports what the sources say, not a verification of ours.

**Already known to us and only updated here:** Alpöge's RH/GRH (20 Nov), OpenAI's Navier-Stokes (8 Sep), the two VP ≠ VNP
preprints. What is new about them is in items 1-3.

---

## A. The ten things that matter most

### 1. VP ≠ VNP: two independent claims, with Lean, 23 Nov (GCT)

- **Anthropic** (`anthropics/formal-math`, folder `vp-vnp/`, commit 918c8e27, 23 Nov 20:04 UTC; also Hexagon
  [2611.00954](https://hexagonmath.org/abs/2611.00954v1), 23 Nov, sponsor "Anthropic"). Claim (README): "For every field,
  circuits for the Hamiltonian cycle polynomial, and for the permanent outside characteristic 2, need more than
  m^(c (log m)^(1/3)) gates for all large m. The same holds for approximating circuits. So VP is a proper subset of VNP, and
  VNP is not contained in the closure of VP." Found by "an internal research Claude model" (Anthropic names no model and
  no effort setting); paper and Lean written by AI; "no human mathematician has checked the proof". **Lean covers:**
  `Statement.lean` (Mathlib-only) states `MainTheorem`, `MainTheoremApprox`, `Separation`, `SeparationClosure` and the
  real permanent bound; `Solution.lean` proves them; Comparator plus the nanoda kernel in CI. The root README's project
  table was not updated with a `vp-vnp` row (it still lists zeta23, 3sum-apsp, eth only).
- **OpenAI** (`openai/math`, `preprints/VP-and-VNP-are-different-November-23-2026`, commit e07100d3, 24 Nov 01:14 UTC;
  history.md entry "November 23, 2026 ... This result was obtained on November 6, 2026"). Theorem 1.1 (TeX
  `build/Paper.tex`, read): over every field, border circuits for the explicit VNP family
  f_n(Z) = sum_x c_x Z_{1,x_1}...Z_{n,x_n} (c_x counting accepting paths of a universal machine) need
  exp(Omega((log n)^{5/4})) gates, "even measuring approximation in degree n only"; Corollary 1.2 transfers it to the
  Hamiltonian cycle polynomial, to the permanent outside characteristic 2, and to (border) determinantal complexity: the
  padded permanent lies outside the determinant orbit closure for N up to exp(c (log m)^{5/4}). The paper says it gives "no
  explicit module of equations or representation-theoretic obstruction". **Lean covers:** `lean/OAI/Computability/VPVNP/
  ClassSeparation.lean`, theorem `vp_ne_vnp` for every field, in the exact (non-border) binary-gate model, over about 1,000
  library files; the README calls it "the Lean proof of the exact VP–VNP separation", so the border statement of
  Theorem 1.1 is, as far as the README says, not what the Lean states.
- **Status:** both unrefereed; no human check announced for either; press calls them unverified
  ([casrai.org](https://casrai.org/news/anthropic-claude-authored-vp-vnp-proof-unverified-lean-2026)).
- **Bears on GCT** directly: two different proofs, with different exponents (Anthropic 4/3 in log m in the exponent,
  OpenAI 5/4), of the orbit-closure separation that the GCT runs treat as open; OpenAI's corollary is stated in
  determinant-orbit-closure form, which is the GCT formulation.

### 2. Alpöge's RH and Dirichlet GRH (20 Nov): what has appeared since (ALPOGE, ZETA_GRH)

The claim (alpo.ge/remark.pdf, opened): RH and GRH, with the expectation of ERH "with more time"; Lean archive
alpo.ge/lean.tar.gz parts 01-14. **Scope checked at the source**: Sutherland's verification page
([math.mit.edu/~drew/grh](https://math.mit.edu/~drew/grh/), updated 24 Nov) states five theorems: RH for Mathlib's zeta and
three GRH statements for every Dirichlet character (no zeros with real part above 1/2; zeros in the critical strip on the
line; separately for primitive characters); "Dedekind zeta functions, Hecke L-functions and automorphic L-functions in
general" are **not** covered. Kernels accepting it: Lean's default and paranoid kernels, leanchecker, nanoda, lean4lean
(five modules with a raised step limit), con-leche and con-ron against the challenge statements; one `lake comparator`
run (v4.36.0) was still running at the last update. Lean FRO and Mathlib Initiative joint statement 21 Nov
([blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). No natural-language proof by the author.

**New since 20 Nov (all opened at Hexagon or arXiv):**
- Rubinstein, *The Alpöge–Claude proof of the RH explained for the Riemann zeta function*
  ([Hexagon 2611.00832](https://hexagonmath.org/abs/2611.00832v1), 23 Nov): the analytic step reduces to a one-sided bound
  for a smoothed prime-power sum on long intervals, derived from one inequality (M); (M) is "taken from the Lean
  development" and is being written up (work in progress).
- Slijepčević, *Outline of Alpöge's proof of the GRH* ([2611.00812](https://hexagonmath.org/abs/2611.00812v1), 21 Nov,
  ~100 pp.): positivity reduces to one-sided bounds on windows [Y, Y^{3/2}] for Riesz-weighted Chebyshev functions twisted
  by a primitive character; these come from hermitian lattices attached to theta lifts over auxiliary abelian CM fields;
  losses are controlled by bounds, polynomial in the conductor, for Tate-Shafarevich groups of Tate twists, proved by
  Eisenstein congruences; the Galois representations needed are built by theta lifts.
- Chenxin Huang (Harvard), *An Arakelov-theoretic perspective ... after Calegari-Dimitrov-Tang*
  ([2611.00833](https://hexagonmath.org/abs/2611.00833v1), 23 Nov): the argument is an instance of Bost's slope method in
  the CDT form; inputs: a zero estimate (equidistribution of special cycles) and a quantitative arithmetic
  Hilbert-Samuel theorem; "We do not claim a proof".
- Jaswal, reader's guide to the Lean archive ([2611.00799](https://hexagonmath.org/abs/2611.00799v1), 21 Nov); R. Zhang
  (IHÉS), sources and provenance, 76 pp. ([2611.00809](https://hexagonmath.org/abs/2611.00809v2), 21 Nov, v2);
  twinheterodox, two simplification notes conditional on the arithmetic inputs
  ([2611.00828](https://hexagonmath.org/abs/2611.00828v1), [2611.00839](https://hexagonmath.org/abs/2611.00839v1), 21 and
  23 Nov); Park, AST audit of the 17.37M-line archive (175,187 files; 4.22M lines of new proof engine)
  ([2611.00881](https://hexagonmath.org/abs/2611.00881v1), 23 Nov).
- **Spin-offs that prove new things from it:** see items 6 (Bost's conjecture), 7 (K_{4m}(Z)) and 8 (Weil II).
- **Disputes:** Granville on the clarity of the 4-page sketch; Radziwiłł on the lack of human understanding (both as
  reported on [Wikipedia](https://en.wikipedia.org/wiki/Alp%C3%B6ge's_proof_of_the_Riemann_hypothesis)); a PhilArchive
  preprint claiming the Lean is vacuous/circular could not be opened (HTTP 403) and is not listed as an item.

### 3. Unforced Navier-Stokes and Euler blow-up, Alpöge-Buckmaster(-Coiculescu), 19-20 Nov (SWEEP3; no direct cluster)

- **Navier-Stokes** ([github.com/tristanbuckmaster/navier-stokes](https://github.com/tristanbuckmaster/navier-stokes),
  created 20 Nov; paper 79 pp., text extracted and read): "there exist smooth, compactly supported, divergence-free
  initial data on R^3, and smooth divergence-free initial data on the torus T^3, for which the solutions of the
  three-dimensional Navier-Stokes equations without force blow up in finite time", disproving Fefferman's (A) and (B).
  Blow-up through a backward discretely self-similar solution at rate (T-t)^{-1/4} in H^1. Theorem 1.1: one such smooth
  profile implies blow-up; Theorem 7.1: a profile exists near a "certificate". **The certificate is not released** (hash
  3f7a335b...c5 given); its verification is an Arb/FLINT interval computation outside Lean. **Lean covers** the
  implications certificate ⇒ profile ⇒ breakdown (`breakdown_on_space`, `breakdown_on_torus`, the cell-layer and fractional
  variants), conditional on data not in the package; the 20 Nov patched package "was not rebuilt". Status: unrefereed,
  conditional on an unreleased computation.
- **Euler** (arXiv [2611.26772](https://arxiv.org/abs/2611.26772), 19 Nov; repository
  [mcoiculescu/EulerBlowupPublic](https://github.com/mcoiculescu/EulerBlowupPublic); TeX read): Theorem 1.1, an odd
  divergence-free u_0 ∈ C^∞(T^3) whose maximal classical solution is smooth up to a finite T_* with
  ∫_0^{T_*} ||curl u||_∞ = ∞, bounded velocity, |curl u(t,0)| → ∞, and smooth limits away from the origin. **Lean covers**
  Theorem 1.1 with no `sorry` and only the three standard axioms, in one-to-one correspondence with the paper's numbered
  results (`spine.json`, `VerifySpine.lean`); the periodic Beale-Kato-Majda criterion is not formalized (Corollary 8.3 is
  proved around it). The paper's provenance section says the first unforced proof was written by Anthropic models and
  rewritten with Claude and Codex, and that an OpenAI paper on the unforced Euler equations preceded it.
- Follow-ups by Jaswal on Hexagon: blow-up data are dense in L^∞, H^1, C^α (α < 5/6) for Euler
  ([2611.00769](https://hexagonmath.org/abs/2611.00769v1), 21 Nov) and, given an Alpöge-Buckmaster profile, in L^p (p < 3)
  and H^s (s < 1/2) for Navier-Stokes ([2611.00874](https://hexagonmath.org/abs/2611.00874v1), 23 Nov).
- Context: Tao's post of 20 Nov ranks the three Alpöge results by how "digested" they are: Euler first, Navier-Stokes
  second ("more work needs to be done to create a proper, professionally written proof"), GRH third
  ([post](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)).

### 4. The Tate conjecture: abelian fourfolds (Broe-Jiang, 23 Nov) and a claim over finite fields (Sun, 20 Nov) (HODGE, AG_POLISH)

- Broe, Jiang, arXiv [2611.30237](https://arxiv.org/abs/2611.30237) (abstract read): the Tate conjecture for non-CM,
  non-ordinary abelian fourfolds over positive-characteristic function fields; with their earlier papers, the Tate
  conjecture for all abelian fourfolds over finitely generated fields. Along the way: l-adic monodromy of abelian
  fourfolds in characteristic p by mixed-characteristic lifts and convergent/overconvergent crystalline monodromy;
  Zarhin's minuscule weights conjecture up to dimension 4; a characteristic-p Mumford-Tate variant; reduction to Markman's
  results on the Hodge conjecture. Unrefereed. **HODGE**: the Tate analogue of the abelian-fourfold Hodge cases (Weil
  classes, Markman) the HODGE runs work around; **AG_POLISH**: uses crystalline monodromy.
- Yunhao Sun, arXiv [2611.28178](https://arxiv.org/abs/2611.28178) (abstract read): claims Kahn's criterion
  Ω_l(Z_l) ∈ DM^eff_ét(k) via the Dwyer-Greenlees equivalence, hence "the Tate conjecture at positive characteristics"
  (over finite fields). An extraordinary claim in a short note; no outside assessment found; treat as unverified until
  someone reads it. **HODGE / AG_POLISH**: if right it settles Tate over finite fields, and with it much of what our
  motives-in-characteristic-p material leaves conditional.

### 5. NL = UL (Hoza, ECCC TR26-323, 20 Nov) and deterministic linear-time MST (ECCC TR26-339, 23 Nov) (SWEEP3; GCT marginally)

- Hoza ([TR26-323](https://eccc.weizmann.ac.il/report/2026/323), abstract read): an explicit weight-assignment generator
  with seed length O(log(wn)) whose weights are min-isolating for at least one seed; by Reinhardt-Allender, NL = UL.
  Unrefereed; a short, "remarkably simple" construction.
- Khanna, Putterman, Song ([TR26-339](https://eccc.weizmann.ac.il/report/2026/339)): the deterministic comparison
  complexity of minimum spanning tree is linear, hence (Pettie-Ramachandran) a deterministic linear-time MST algorithm;
  first improvement since Chazelle 2000. Unrefereed.
- Both are Boolean/algorithmic results; they bear on GCT only as the month's other complexity landmarks.

### 6. Bost's conjecture on slopes of tensor products (Sihan Chen, Hexagon 23 Nov; Chen-Yuan, arXiv 21 Nov) (ALPOGE, AG_POLISH, ZETA_GRH)

- Sihan Chen, [Hexagon 2611.00911](https://hexagonmath.org/abs/2611.00911v1): proves Bost's conjecture on the additivity
  of maximal slopes under Hermitian tensor products over the integers of any number field; key estimate: a rectangular
  Specht lattice with fixed rows and a boxes has log covolume per rank O(√a); "discovered while reconstructing Levent
  Alpöge's proof of the Riemann hypothesis". Unrefereed.
- Huayi Chen, Yijun Yuan, arXiv [2611.28474](https://arxiv.org/abs/2611.28474): tensor semistability for Hermitian adelic
  vector bundles over proper adelic curves (countable fields of characteristic 0), through the same Specht-lattice
  covolume estimate. Unrefereed.
- Bearing: the slope method is the frame in which Chenxin Huang reads the Alpöge argument (item 2); a classical open
  problem of Arakelov geometry closed as a by-product.

### 7. K_{4m}(Z) = 0 through degree 120, from Alpöge's "Step 17" (Hexagon 21 and 24 Nov) (ALPOGE, LONGUE_MARCHE)

- Mok, Zheng, [Hexagon 2611.00998](https://hexagonmath.org/abs/2611.00998v1) (24 Nov): K_{4m}(Z) = 0 for 1 ≤ m ≤ 30,
  "unconditional", combining cyclotomic and étale reductions with "the pointwise strict Selmer bound from the Lean work of
  Alpöge and Claude" and exact Hecke-determinant tests; Pintar, [2611.00829](https://hexagonmath.org/abs/2611.00829v3)
  (21 Nov, v3): the same through degree 104, "assuming the arithmetic construction in Alpöge's Step 17".
- Bearing: vanishing of all K_{4k}(Z) is equivalent to Vandiver's conjecture (Kurihara, Soulé); these give its
  eigenspaces of small index at every prime, resting on the Lean archive. Our own Hexagon note on the Anderson-Ihara
  question ([2611.00939](https://hexagonmath.org/abs/2611.00939v1)) holds at every prime satisfying Vandiver, so it is a
  direct neighbour (LONGUE_MARCHE: Galois action on π_1 of P^1 minus three points).

### 8. Our Weil II note has an outside expositor (Dingxin Zhang, arXiv 23 Nov) (ALPOGE, ZETA_GRH, HODGE)

- Dingxin Zhang, arXiv [2611.30749](https://arxiv.org/abs/2611.30749): "An expanded, AI-generated account appeared on
  Hexagon, where it was posted by F. Alderliefste. This note gives an exposition of the proof presented there." The account
  is our [Hexagon 2611.00789](https://hexagonmath.org/abs/2611.00789v1) (21 Nov; the proof produced by GPT-6 Astra (ChatGPT
  Pro mode), checked by Claude Opus 5.5 at effort high and independently by Claude Fable 5.2 at effort max), writing out
  Alpöge's footnote-3 proof of Deligne's weight bound. Bearing: the first outside human reading of one of our posts in this
  line; the conference should read his note for corrections.

### 9. Anabelian and nonabelian Chabauty: Kim's dimension inequality, Mordell by Chabauty-Kim, m-step solvable anabelian (LONGUE_MARCHE)

- Zehavi, arXiv [2611.18218](https://arxiv.org/abs/2611.18218) (first listed 13 Nov; abstract read): Kim's conjectural
  dimension inequality dim H^1_f(G_{Q,Σ}, U_n^ét) < dim(U_n^dR/F^0) for n large, for every curve of genus ≥ 2 over Q with
  a rational point and every odd prime of good reduction, via noncommutative Iwasawa theory. Unrefereed.
- Jit Wu Yap, [Hexagon 2611.00576](https://hexagonmath.org/abs/2611.00576v1) (18 Nov): "a new proof of the Mordell
  conjecture over the rational numbers via the Chabauty-Kim method"; obtained by prompting GPT Astra 6 in September (the
  poster names no effort setting), "sent to experts in the community". Unrefereed.
- Yu Mao, arXiv [2611.24495](https://arxiv.org/abs/2611.24495) (18 Nov): an open homomorphism G_K^{m+2} → G_L^{m+2} of
  maximal (m+2)-step solvable quotients of number-field Galois groups induces φ_m arising uniquely from a field embedding
  (m ≥ 2); sharpens the Mao-Saïdi cyclotomic criterion.
- Bearing: Kim's programme is the arithmetic descendant of the section conjecture of the Longue Marche; Zehavi plus Yap
  together would make Faltings over Q a consequence of the unipotent fundamental group, which is the Grothendieck
  anabelian picture.

### 10. Named problems closed this week outside our fields (SWEEP3)

All unrefereed; abstracts read.
- Chow, Dietmann: G(k) ≍ k in Waring's problem ([2611.29821](https://arxiv.org/abs/2611.29821), 22 Nov).
- Yutian Li: the regular n-gon minimizes the first Dirichlet eigenvalue among simple polygons of given area with at most
  n sides, every n ≥ 3, i.e. Pólya's polygonal Faber-Krahn conjecture ([2611.27968](https://arxiv.org/abs/2611.27968),
  20 Nov).
- Fei Xue: the Reinhardt conjecture (the smoothed octagon has the least optimal lattice packing density among centrally
  symmetric convex disks), 430 pp. ([2611.21470](https://arxiv.org/abs/2611.21470), 16 Nov).
- Shengmin Zhang (Peking): the Galois-McKay conjecture, by verifying the inductive condition for all simple groups and
  the Navarro-Späth-Vallejo reduction ([Hexagon 2611.00967](https://hexagonmath.org/abs/2611.00967v1), 24 Nov).
- Aprodu, Farkas, Park: genus-10 W(E_6)-covers of P^1 give a 9-dimensional family of counterexamples to Green's
  conjecture on syzygies of canonical curves and to the Green-Lazarsfeld secant conjecture
  ([2611.21197](https://arxiv.org/abs/2611.21197), 16 Nov). (Also AG_POLISH.)
- Landi: Ambro's conjecture (lower semicontinuity of minimal log discrepancies), hence Shokurov's bound mld ≤ dim
  ([2611.30971](https://arxiv.org/abs/2611.30971), 23 Nov). (Also AG_POLISH.)

---

## B. Our fields, item by item

### Hodge theory, algebraic cycles, motives (HODGE, AG_POLISH)

- **HLRV conjecture**, Qiyue Tang, [Hexagon 2611.00441](https://hexagonmath.org/abs/2611.00441v1) (15 Nov): "We prove
  the Hausel-Letellier-Rodriguez-Villegas conjecture on the mixed Hodge polynomials of generic semisimple GL_n character
  varieties." Posted on behalf of someone else, "human understanding: none" declared; one-line abstract. Unrefereed,
  unassessed. HODGE (mixed Hodge structures of character varieties, P=W neighbourhood).
- **Brosnan-Fakhruddin conjecture** for H = R^m f_* Z / tors of a smooth projective family, Mark Kisin,
  [Hexagon 2611.00535](https://hexagonmath.org/abs/2611.00535v1) (16 Nov): essential dimension at p of H/p^n ≥ dimension of
  the period image for p^n large, via geometric Sen operator vs Higgs field and integral Hodge-Tate theory. HODGE,
  AG_POLISH (p-adic Hodge theory).
- Pastrana, Villaflor, *Hodge cycles of Klein hypersurfaces*, arXiv [2611.29763](https://arxiv.org/abs/2611.29763)
  (22 Nov): infinitely many new cases of the Hodge conjecture for Klein varieties; the exceptional part is finite. HODGE.
- Ottem, arXiv [2611.31152](https://arxiv.org/abs/2611.31152) (23 Nov): a quartic double solid whose desingularization has
  an integral cohomological decomposition of the diagonal but no Chow decomposition. HODGE (integral Hodge/Chow gap).
- Colmez, Nizioł, Shao, arXiv [2611.27054](https://arxiv.org/abs/2611.27054) (20 Nov): a family of elliptic curves over an
  open disc whose total space violates the C_st conjecture in degree 1; C_st holds for a smooth proper family over a small
  disc iff its period map is constant. AG_POLISH (p-adic comparison, crystalline/semistable).
- Molin, arXiv [2611.28988](https://arxiv.org/abs/2611.28988) (21 Nov): a free action of the potentially semistable
  derived deformation ring on the Π-part of p-adic cohomology of GL_n over CM fields, confirming a prediction of
  Venkatesh. HODGE/ZETA_GRH (motivic action conjectures).
- Feld, [Hexagon 2611.00625](https://hexagonmath.org/abs/2611.00625v1) (19 Nov): Gersten exactness for K(R; Z/N),
  R excellent regular local of dimension 2, N invertible, ramified mixed characteristic allowed. AG_POLISH (Gersten,
  Bloch-Ogus side of motives).
- Spencer G. Taylor, arXiv [2611.19346](https://arxiv.org/abs/2611.19346) (14 Nov): higher Chow groups of arbitrary
  finite-type separated schemes represented in SH, Borel-Moore counterpart of Bachmann-Elmanto-Morrow. Garkusha, arXiv
  [2611.18212](https://arxiv.org/abs/2611.18212) (13 Nov): Frobenius and perfection in framed motives over imperfect
  fields. AG_POLISH / DERIVATEURS (motivic homotopy).
- Mok, Xu, [Hexagon 2611.00721](https://hexagonmath.org/abs/2611.00721v1) (20 Nov): Vasconcelos' conjecture (finite
  projective dimension of Ω_{S/k} ⇒ reduced complete intersection) in characteristic 0 and a precise char-p statement.
  AG_POLISH.
- Jovinelly, Lehmann, Riedl, arXiv [2611.25068](https://arxiv.org/abs/2611.25068) (18 Nov): projective globally F-regular
  varieties are rationally chain connected. AG_POLISH.
- Hu, Wu, arXiv [2611.17847](https://arxiv.org/abs/2611.17847) (13 Nov): for every odd-order finite abelian A ≠ 0, a
  smooth projective surface with infinite π_1 and trivial étale π_1, Kobayashi hyperbolic with Stein universal cover.
  LONGUE_MARCHE (topological vs étale fundamental group).
- Hacon, Wang, arXiv [2611.29683](https://arxiv.org/abs/2611.29683) (22 Nov): termination of klt flips with scaling for
  compact Kähler klt pairs; "based on the AI generated papers [OAI1] and [OAI2]". Yoon-Joo Kim, arXiv
  [2611.29056](https://arxiv.org/abs/2611.29056) (21 Nov): exposition of OpenAI's proof that the base of a Lagrangian
  fibration of a compact hyper-Kähler manifold is P^n. SWEEP3 (outside checks of OpenAI's October releases).
- Höhn, [Hexagon 2611.00920](https://hexagonmath.org/abs/2611.00920v1) (23 Nov): Chern-pure hyper-Kähler manifolds: (n,b)
  is one of nine pairs, matched with tight spherical designs (E_8, Leech). HODGE (cohomology of hyper-Kähler).
- Jordan, [Hexagon 2611.00628](https://hexagonmath.org/abs/2611.00628v2) (19 Nov): Christol's conjecture for non-resonant
  globally bounded hypergeometric series of height two, including Christol's 1987 test case. SWEEP3 (periods,
  G-functions).

### L-functions beyond Dirichlet, arithmetic (ZETA_GRH)

- Baiying Liu (Purdue), [Hexagon 2611.00741](https://hexagonmath.org/abs/2611.00741v1) (20 Nov): for every number field K
  and unitary Hecke character ω, L_K(s, ω) ≠ 0 for Re s > θ_G ≈ 0.8733326374459050; the same for Artin L-functions and
  L-functions of finite-dimensional unitary Weil representations. **This is the "beyond Dirichlet" zero-free region the
  ZETA_GRH runs should compare with**: Alpöge's Lean covers Dirichlet only; OpenAI's October #003 strip Re s > 7/8 = 0.875
  (as described in Park, [Hexagon 2611.00912](https://hexagonmath.org/abs/2611.00912v1)) is for Dirichlet and Hecke
  L-functions over Q(√-3). Unrefereed.
- Dieulefait, [Hexagon 2611.00622](https://hexagonmath.org/abs/2611.00622v1) (19 Nov): if ρ_1 ⊗ ρ_2 (2-dimensional,
  Lie-irreducible, potentially modular) is attached to a regular L-algebraic cuspidal Π on GL_4 over a totally real field,
  then ρ_1, ρ_2 are modular and Π ≅ π_1 ⊠ π_2 (converse to Ramakrishnan). ZETA_GRH (functoriality inputs).
- Wan, Xiang, Xu, arXiv [2611.29641](https://arxiv.org/abs/2611.29641) (22 Nov): the BSD formula for CM elliptic curves
  over Q of analytic rank one (92 pp.). ZETA_GRH.
- Chudnovsky, arXiv [2611.30820](https://arxiv.org/abs/2611.30820) (23 Nov): ineffective measure
  |h_0 + Σ h_i log a_i| ≥ C H^{-n-ε} for multiplicatively independent positive rationals, exponent best possible; Lean 4
  sources attached. SWEEP3.
- Raymond, [Hexagon 2611.00460](https://hexagonmath.org/abs/2611.00460v1) (17 Nov): Λ ≤ 0.107964910079 for the de
  Bruijn-Newman constant, using OpenAI's 7/8 theorem; superseded if Alpöge's RH stands (RH ⇔ Λ ≤ 0; Rodgers-Tao Λ ≥ 0).
- Mazur, Rubin, Shlapentokh, arXiv [2611.19103](https://arxiv.org/abs/2611.19103) (14 Nov): the first-order theory of
  the ring of integers of any abelian extension of Q is undecidable. Pasten, Vidaux, arXiv
  [2611.24748](https://arxiv.org/abs/2611.24748) (18 Nov): abc over a quadratic field K ⇒ Z Diophantine in K. SWEEP3.
- Yuwen Zhou, arXiv [2611.22290](https://arxiv.org/abs/2611.22290) (17 Nov): with O(log p) bits of advice depending on
  p, discrete logarithms in groups of order p reduce in polynomial time to a Diffie-Hellman oracle, removing Maurer's
  smoothness proviso; "Developed with Claude Fable 5.2 and Claude Opus 5.5" (the paper names no effort setting). SWEEP3.

### Geometric complexity theory, border rank (GCT)

- Items 1 and 5 above.
- Yilin Liu, [Hexagon 2611.00972](https://hexagonmath.org/abs/2611.00972v1) (24 Nov): asymptotic rank of a three-tensor
  with local ranks ≤ d is ≤ d^{ω_F/√3}, answering Alman-Li; equality with the largest local rank D when the others are
  ≤ D^{√5/4}. Unrefereed, "human understanding: none" declared. GCT (asymptotic rank, Strassen).
- Yilin Liu, [Hexagon 2611.00994](https://hexagonmath.org/abs/2611.00994v1) (24 Nov): border circuit size > 2^{n^δ} for the
  row-ordered noncommutative permanent and determinant over every field; transfers "OpenAI's stretch theorem". GCT.
- Yilin Liu, [Hexagon 2611.00634](https://hexagonmath.org/abs/2611.00634v1) (19 Nov): polynomial-size hitting sets for
  ROABPs under unknown affine change of variables (orbit PIT). GCT.
- Dawar, Dwivedi, Pago, Seppelt, arXiv [2611.23541](https://arxiv.org/abs/2611.23541) (17 Nov): depth hierarchies for
  symmetric algebraic circuits. Kalai, Kumar, Volk, arXiv [2611.21201](https://arxiv.org/abs/2611.21201) = ECCC TR26-326
  (16 Nov): Möbius-pseudorandomness for algebraic circuits, including determinant and permanent. GCT (restricted models).

### Homotopy theory, derivators, categories (DERIVATEURS)

- Barthel, Mann, Ray, Schlank, Senger, Weinstein, Zhou, arXiv [2611.27879](https://arxiv.org/abs/2611.27879) (20 Nov,
  130 pp.): predictions of Hopkins' chromatic splitting conjecture in coheight 1; a map of K(h-1)-local E_∞-rings admits a
  retract when p-1 ∤ h-1, an isomorphism for h = 2, p odd; methods from p-divisible groups and p-adic geometry.
- Enomoto, [Hexagon 2611.00805](https://hexagonmath.org/abs/2611.00805v2) (21 Nov, v2 with formalization): an essentially
  small hereditary extriangulated category with no fully faithful extriangulated functor into any triangulated category.
  DERIVATEURS (enhancements vs triangulated structure).
- Nishimura, arXiv [2611.29239](https://arxiv.org/abs/2611.29239) (22 Nov): a fourfold Toda bracket ⟨ν², 2, η², ν⟩ not
  defined although both threefold sub-brackets contain 0 (answers Isaksen). Guès, arXiv
  [2611.31031](https://arxiv.org/abs/2611.31031) (23 Nov): tame homotopy theory and the Goodwillie tower. Joyce, arXiv
  [2611.24690](https://arxiv.org/abs/2611.24690) (18 Nov, 312 pp.): an ∞-category approach to A_∞-algebras and
  categories. DERIVATEURS.

### Crystalline and p-adic cohomology (AG_POLISH)

- Colmez-Nizioł-Shao (above). Ishizuka, Shimada, arXiv [2611.22214](https://arxiv.org/abs/2611.22214) (17 Nov): fiber
  sequence between the p-th Nygaard graded piece of absolute prismatic cohomology and the Frobenius-Witt cotangent complex;
  compares Mao's and Bhatt-Mathew's regularity criteria. Fersi, arXiv [2611.20395](https://arxiv.org/abs/2611.20395)
  (16 Nov): local logarithmic Cartier transform modulo p^n (Shiho's approach). Qi, Taylor, arXiv
  [2611.23162](https://arxiv.org/abs/2611.23162) (17 Nov): normal form for invertible semilinear maps; explicit category
  of isocrystals over a finite field. Broe-Jiang (item 4) uses overconvergent crystalline monodromy.

### Other named problems (SWEEP3; abstracts read; all unrefereed)

El-Zahar-Erdős conjecture disproved (Liu, Meng, [2611.24735](https://arxiv.org/abs/2611.24735), 18 Nov); van Emde
Boas-Kruyswijk conjecture on the Davenport constant disproved for n = 2k, k ≥ 3 odd (Gao, Geroldinger, Wang, Zeng,
[2611.24775](https://arxiv.org/abs/2611.24775), 18 Nov); Stanley's conjecture on leading Ehrhart coefficients of the
Birkhoff polytope (Liu, Tang, [2611.25973](https://arxiv.org/abs/2611.25973), 19 Nov); Casselman's comparison conjecture
(Xiao, Yu, [2611.25367](https://arxiv.org/abs/2611.25367), 19 Nov); the Broué-Malle-Michel symmetrising trace conjecture
for all complex reflection groups (Chavli, Chlouveraki, Pfeiffer, Psaromiligkos,
[2611.21912](https://arxiv.org/abs/2611.21912), 16 Nov); Petty's polar projection problem (Zhang,
[2611.17926](https://arxiv.org/abs/2611.17926), 13 Nov); dynamical Manin-Mumford for Hénon automorphisms (Gauthier,
Zhang, [2611.28843](https://arxiv.org/abs/2611.28843), 21 Nov); Rayleigh's clamped-plate conjecture in dimensions 4 and 5
(Dai, Sun, Zhang, [2611.29957](https://arxiv.org/abs/2611.29957), 23 Nov); Voiculescu's normal dilation conjecture
disproved (Tang, [2611.21495](https://arxiv.org/abs/2611.21495), 16 Nov); Stein's equidissection conjecture (Krachun,
[2611.20240](https://arxiv.org/abs/2611.20240), 15 Nov); the Birkhoff problem for monomorphism categories (Schlegel,
[2611.20099](https://arxiv.org/abs/2611.20099), 15 Nov); Terao's freeness conjecture fails over F_121 (Tsujie,
[Hexagon 2611.00999](https://hexagonmath.org/abs/2611.00999v1), 24 Nov); the strong AJ conjecture fails for a hyperbolic
prime knot, 8_11 (Acuña, [Hexagon 2611.00686](https://hexagonmath.org/abs/2611.00686v1), 20 Nov); a smooth flexible
closed sphere in R^3, Lean-formalized main theorem (Boyang Hu, [Hexagon 2611.00534](https://hexagonmath.org/abs/2611.00534v1),
16 Nov); the Geiss-Leclerc-Schröer open orbit conjecture (Bob Smith, [Hexagon 2611.00923](https://hexagonmath.org/abs/2611.00923v1),
23 Nov); sorting in o(N log N) on a multitape Turing machine (Tal, [ECCC TR26-331](https://eccc.weizmann.ac.il/report/2026/331),
22 Nov).

---

## C. The laboratories' releases, complete lists for 14-24 Nov

- **github.com/openai/math**: one release. 23 Nov (commit e07100d3, merged 24 Nov 01:30 UTC as PR #5): *VP and VNP are
  different* with TeX source and Lean (item 1). history.md has no other entry after 29 Oct (the CM Hodge Comparator
  namespace fix). The preprints folder holds 752 entries; only this one is dated November. Commits since 10 Nov: these two
  only.
- **github.com/anthropics/formal-math**: one release. 23 Nov (commit 918c8e27, PR #51 merged 21:43 UTC): `vp-vnp/` (item 1).
  No other commit since 27 Oct (`eth/`). The Alpöge RH archive is not in this repository (it is at alpo.ge and
  `leanprover-community/riemann-hypothesis`, per Wikipedia), nor are the Euler and Navier-Stokes packages (in the
  authors' own GitHub repositories, item 3).
- **Google DeepMind** (blog, November posts): *Finding faster quantum algorithms with agents and formal verification*,
  23 Nov (arXiv [2611.09822](https://arxiv.org/abs/2611.09822), first posted 6 Nov; Lean library
  `google-deepmind/formal-quantum-computation`; cost reductions such as 11.8× for an inertial-confinement-fusion circuit
  and 290× for an arcsin routine, each proved in Lean). No mathematics announcement in our fields. Just before the window:
  *AlphaProof Code*, 10 Nov (Lean verification of the Signal protocol's compiled code, over six million lines of Lean).
  The other November posts are model and science releases (Gemini 4 Neon, Hydrogen, Carbon; Genie 4; AlphaGenome 2; ...).
- **Hexagon**: 531 works published 14-24 Nov (appendix). By subject: math.NT 167, math.CO 90, math.AG 28, math.PR 25,
  math-ph 20, ..., cs.CC 10. Eleven are ours (sponsor user Alderliefste): 2611.00742, 00789, 00851, 00936, 00937, 00938,
  00939, 00940, 00987, 00993, 00996.

## D. Just before the window (context only)

Soulé, *On the abc conjecture* (arXiv 2611.05217, 3 Nov): Vojta's conjecture for genus-two curves and a weak abc by
adelic intersection theory (Parshin, Moret-Bailly) (AG_POLISH, ZETA_GRH). KITP shepherding committee's third statement on
OpenAI's quantum Yang-Mills existence proof (9 Nov): an independent team led by Gross verified existence; the mass gap
remains open. Bang, Cheskidov, arXiv 2611.18151 (13 Nov): sharp finite-time blow-up for unforced axisymmetric Euler
without swirl from multiscale data. Tsimerman's Fields Medal (ICM Philadelphia, 23 Jul 2026), described in Pila's arXiv
2611.30644 (23 Nov).

## E. Not covered

The arXiv API was rate-limited at the end (author searches failed); categories outside the 26 searched (physics, most of
cs) were not swept. The Lean Zulip and X/Mastodon were not read beyond what Tao's post and Wikipedia quote. The
PhilArchive dispute of Alpöge's Lean (NIEIOT-2) returned 403. No mathematical check of any item was made here.

---

## Appendix: every Hexagon work published 14-24 Nov 2026 (531; listing level: identifier, date, subject, sponsor, title)

Only the works named in sections A-C were opened (abstract and metadata via the Hexagon API).

- 2611.00264 | 2026-11-17 | math.NT | Zeng Chunping | Wieferich co-occurrence along exponential sequences: a weighted tail estimate and its application to (⋆′)
- 2611.00319 | 2026-11-16 | math.CO | Jensen Kohlmeyer | The Zarankiewicz number z(13,15;3,4)
- 2611.00433 | 2026-11-15 | math.AG | Shankar Sivarajan | An explicit determinantal formula for Sinkhorn limits of matrices and tensors
- 2611.00434 | 2026-11-15 | math.NT | Elleard Felix Webster Heffern | Aigner's Three Monotonicities from Fibonacci Matrices and Six Snake Pieces
- 2611.00436 | 2026-11-15 | math.NT | Ramin Takloo-Bighash | Subrings and cotypes of truncated polynomial rings
- 2611.00437 | 2026-11-17 | math.NT | Elleard Felix Webster Heffern | Hyperbolic Collision Invariants and Certified Odd-Even Tiers toward Markoff Unicity
- 2611.00438 | 2026-11-15 | math.MP | Daniel Wang | Electric-field hotspot packing and power channels in dielectric media
- 2611.00439 | 2026-11-15 | cs.CC | David Niedbala Giraudin | An edge comparison with constant 3/2 and the coefficient 6/sqrt(2 pi) for the average sensitivity of polynomial threshold functions
- 2611.00440 | 2026-11-15 | math.NT | twinheterodox | Growth criteria for reciprocal series with nonincreasing weights
- 2611.00441 | 2026-11-15 | math.AG | Qiyue Tang | A proof of the HLRV conjecture
- 2611.00442 | 2026-11-15 | math.MG | Sihan Chen | The Barker--Larman problem in dimension three A counterexample to the Barker--Larman problem in dimension three
- 2611.00443 | 2026-11-15 | math.NT | Filip Najman | Automorphisms of the modular curves $X_\Delta(N)$
- 2611.00444 | 2026-11-15 | math.LO | Dr. András Pongrácz | Self-embedding monoids and the existential Thomas conjecture
- 2611.00445 | 2026-11-15 | math.QA | G. Militaru | Solutions of the set-theoretic quantum Yang--Baxter equation arising from posets
- 2611.00446 | 2026-11-15 | math.OA | Teo Banica | Karlsson matrices and the kagome lattice
- 2611.00447 | 2026-11-15 | math.PR | Brice Pouly | Sharp Poisson approximation and second-order correction for long multiplicative runs
- 2611.00448 | 2026-11-15 | math.LO | John Hessler | Points from Processes: Vakarelov’s Dynamic Mereotopology and Whitehead’s Point-Free Program
- 2611.00449 | 2026-11-15 | math.CO | Yair Lavi | Vector Packing and Sharp Bounds for Matrices of Bounded Rank
- 2611.00450 | 2026-11-15 | math.RT | Qiyue Tang | The inductive Alperin–McKay condition for $G_2(q)$ and ${}^3D_4(q)$
- 2611.00451 | 2026-11-15 | math.GR | Qiyue Tang | Further cases of the inductive Alperin–McKay condition
- 2611.00452 | 2026-11-15 | math.CO | Yuda Chen | Constructions and explicit power savings for point--unit-circle incidences
- 2611.00453 | 2026-11-15 | math.FA | Samir Hamad | A midpoint locally uniformly rotund Banach space with the Daugavet property
- 2611.00454 | 2026-11-15 | math.SG | Zhen Gao | Ekeland–Hofer capacities and convex duality: ordinary and real spectral invariants
- 2611.00455 | 2026-11-15 | math.NT | Frank Vega | Colossally Abundant Numbers and Nicolas' Second Criterion
- 2611.00456 | 2026-11-15 | math.GR | Teo Banica | Flat linearity of uniform groups
- 2611.00457 | 2026-11-15 | math.NT | FELIPE MARTINS SANTOS | SeqImpar and SeqPar: Analytic Characterizations of the Zeros of the Riemann Zeta and Dirichlet Beta Functions and a Criterion Equivalent to the Riemann Hypothesis
- 2611.00458 | 2026-11-15 | math-ph | Yuri Ximenes Lecca | Axiomatic Foundations of Astrophysical Systems: Model-Independent Obstructions Between Equations of State, Observables, and Field Equations
- 2611.00459 | 2026-11-15 | math.NT | Elias  De Jesús | Realizer Bounds and Repetition Constraints at the First Coefficient Crossing in the 3x + 1 Problem
- 2611.00460 | 2026-11-17 | math.NT | Dale James Raymond | A computer-assisted bound Λ ≤ 0.107964910079 for the de Bruijn–Newman constant
- 2611.00461 | 2026-11-15 | math.NT | Changxia Lin | A Central-Commutator Regge Seed: BCC Sublattices, Face-Matched Hinges, and Quaternionic Spectral Gaps
- 2611.00462 | 2026-11-15 | math.NT | Sunay Venkat | Algebraically independent counterexamples with rational-power separation
- 2611.00463 | 2026-11-15 | math.NT | Sunay Venkat | Integer-power separation does not force rational-dilation separation
- 2611.00464 | 2026-11-15 | quant-ph | Tejasvi Singh Tomar | Undistillability of Werner states from three, four and five copies
- 2611.00465 | 2026-11-15 | math.PR | Tejasvi Singh Tomar | Essential enhancements of site percolation in every dimension and on periodic lattices
- 2611.00466 | 2026-11-15 | quant-ph | Tejasvi Singh Tomar | Equality cases and every-copy results for the Werner endpoint inequality
- 2611.00467 | 2026-11-15 | math.PR | Tejasvi Singh Tomar | Certified upper bounds for the Chvátal–Sankoff constant
- 2611.00468 | 2026-11-15 | math.PR | Tejasvi Singh Tomar | Homological percolation in characteristic two: the Ising gauge case
- 2611.00469 | 2026-11-15 | math.CO | Tejasvi Singh Tomar | Certified upper bounds for two sum-difference exponents
- 2611.00470 | 2026-11-15 | math.CV | Tejasvi Singh Tomar | An explicit bound below 2/π for the maximum term of an entire function
- 2611.00471 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | Upper and lower bounds for the Schur–Siegel–Smyth trace problem
- 2611.00472 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | New lower bounds for Romanoff's constant
- 2611.00473 | 2026-11-15 | math.NT | Shawn Krisman | The sum of the reciprocal cubes of the Fibonacci numbers is irrational
- 2611.00474 | 2026-11-15 | math.CO | Tejasvi Singh Tomar | An upper bound for the connective constant of the square lattice
- 2611.00475 | 2026-11-15 | math.MG | Tejasvi Singh Tomar | A lower bound for Moser's worm problem with rotations and translations
- 2611.00476 | 2026-11-15 | math.PR | Tejasvi Singh Tomar | A certified upper bound for the beat the average game
- 2611.00477 | 2026-11-15 | math.MG | Tejasvi Singh Tomar | An upper bound of 2√2 for the three-dimensional sofa problem in a snake-shaped corridor
- 2611.00478 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | A lower bound for the essential minimum of the Zhang–Zagier height
- 2611.00479 | 2026-11-15 | math.CA | Tejasvi Singh Tomar | Bounds for the weak type (1,1) constant of the centred maximal operator over squares
- 2611.00480 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | A lower bound for the smallest limit point of the absolute Mahler measure of totally positive algebraic integers
- 2611.00481 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | An upper bound for the smallest limit point of the absolute Mahler measure of totally positive algebraic integers
- 2611.00482 | 2026-11-15 | math.NT | Tejasvi Singh Tomar | Bounds for the smallest limit point of the areal Mahler measure of totally positive algebraic integers
- 2611.00483 | 2026-11-15 | math.CV | Tejasvi Singh Tomar | A lower bound for the Bohr radius of the bidisc
- 2611.00484 | 2026-11-15 | math.CA | Tejasvi Singh Tomar | Bounds for the sign uncertainty constant in dimension one
- 2611.00485 | 2026-11-15 | math.DS | Tejasvi Singh Tomar | Complex central configurations of the planar five-body problem at special masses
- 2611.00486 | 2026-11-15 | math.CO | Qiyue Tang | Schur Nonnegativity of Double-Wiring Cluster Variables
- 2611.00487 | 2026-11-15 | math.RT | Rui Chen | Unramified multiplicity one spherical pairs
- 2611.00488 | 2026-11-15 | math.CO | Qiyue Tang | An Irredundant Test for Circular Positivity
- 2611.00489 | 2026-11-15 | math.AG | Qiyue Tang | A Counterexample to the Realizability Conjecture for Surface Classes
- 2611.00490 | 2026-11-15 | math.NT | Qiyue Tang | Density-One Uniqueness for Markoff–Hurwitz Solutions
- 2611.00491 | 2026-11-15 | math.NT | Shawn Krisman | The reciprocal cube sums of Lucas sequences of quadratic units are irrational
- 2611.00492 | 2026-11-15 | math-ph | Zeng Chunping | From Four-Dimensional Wilson Lattice Gauge Theory to Quantum Yang--Mills Theory: Construction with Proofs from Certified Assumptions, and the Record of Its Independent Validation
- 2611.00493 | 2026-11-15 | math.NT | Qiyue Tang | Vieta invariants and Markoff–Hurwitz orbits
- 2611.00494 | 2026-11-15 | math.DG | Anton Kalmykov | An unconditional estimate and the structure of the Bäcklund orbit
- 2611.00495 | 2026-11-15 | math.NA | Ivan BESEVIC | Geometric Root Calculators: Radical supports of orders five and nine and real-degree enclosures in the Pandrosion rectangle
- 2611.00496 | 2026-11-15 | math.NT | FELIPE MARTINS SANTOS | Geometric Equivalence of the Riemann Hypothesis
- 2611.00497 | 2026-11-15 | math.PR | Alberto Gandolfi | Towards a conformal field theory of critical percolation. I. The bulk stress tensor and Ward identities.
- 2611.00499 | 2026-11-17 | quant-ph | Marc Sperzel | Double-Pulsar Drag Bounds Dissipative Sources of Diósi–Penrose Decoherence
- 2611.00500 | 2026-11-17 | math.NT | Xuebin Liang | On the Diophantine equation $ab + bc + ca = N$ and Euler's idoneal numbers
- 2611.00502 | 2026-11-16 | math.GT | Peter Kronheimer | Spherical space forms in K3: an instanton parity argument
- 2611.00503 | 2026-11-16 | math.QA | Teo Banica | Maximal torus theory for crossed product quantum groups
- 2611.00504 | 2026-11-16 | math.PR | Man Huang | Stationary prediction from finite calibration: obstructions and sharp history rates under interval catastrophes
- 2611.00505 | 2026-11-17 | math.FA | Qiyuan Ma | Orthogonal bases of symmetric unitary matrices in odd dimensions and the mixed-unitary rank of the symmetric Werner–Holevo channel
- 2611.00506 | 2026-11-16 | cs.FL | SUNGBIN HONG | A uniform 7/48 cubic upper bound for reset thresholds
- 2611.00507 | 2026-11-16 | math.CA | Anton Kalmykov | Closed-Form Adiabatic Asymptotics of the Solution of the Amsler Equation
- 2611.00508 | 2026-11-16 | math.GM | liang zhang | An Algebraic Proof of Hilbert Nullstellensatz over Rationals
- 2611.00509 | 2026-11-16 | math.NT | Travor Zihao Liu | Pair correlation of $L$-zeros and Hooley's conjecture
- 2611.00510 | 2026-11-16 | math.NT | yi li | A DETAILED FINITE-CARRY PROOF OF A CONJECTURE ON PERMUTATION BINOMIALS IN CHARACTERISTIC TWO
- 2611.00511 | 2026-11-16 | math.ST | Samuil Petkov | The planar data-selection constants $F(2,n)=2n/(2n-1)$, including $F(2,3)=6/5$ and $F(2,2)=4/3$
- 2611.00512 | 2026-11-17 | math.CO | Dave Goel | The Hibi–Li (2016) conjecture is fully resolved
- 2611.00513 | 2026-11-17 | math.CO | Dave Goel | The Hibi–Li (2016) conjecture is fully resolved, and other miscellanea
- 2611.00514 | 2026-11-16 | math.NT | Jensen Kohlmeyer | Consecutive primes at distance 122,290
- 2611.00515 | 2026-11-16 | math.NT | David Niedbala Giraudin | A lower bound 0.11096505 for Romanoff's constant
- 2611.00516 | 2026-11-16 | math.NT | David Niedbala Giraudin | An admissible 232 465 000-tuple with few long pairs, and H_5 <= 4 817 211 684
- 2611.00518 | 2026-11-16 | math.DG | Sihan Chen | The dimension-free symmetric Gaussian isoperimetric profile: finite attainment and critical rank
- 2611.00519 | 2026-11-16 | math.CV | Dave Goel | Sheil-Small's (1974) covering problem has a positive answer, and other miscellanea
- 2611.00520 | 2026-11-16 | math.CO | Dave Goel | Flow reconfiguration with one modulus for all graphs, and Cereceda's conjecture for bipartite 2-degenerate graphs
- 2611.00521 | 2026-11-16 | math.CO | Dave Goel | Integer and modular flow reconfiguration: the moduli up to six, chords, and large moduli
- 2611.00522 | 2026-11-16 | math.CO | Dave Goel | Nowhere-zero flow reconfiguration in every finite abelian group of order at least 3024
- 2611.00523 | 2026-11-16 | math.CO | Dave Goel | Diameters of the order and chain polytopes of a connected poset
- 2611.00524 | 2026-11-17 | math.OA | K. MAHESH KRISHNA | Modular Kittaneh Numerical Radius Inequalities
- 2611.00525 | 2026-11-16 | math.CO | Dave Goel | The Lee (2026) conjecture on the diameters of order and chain polytopes fails in both directions, and other miscellanea
- 2611.00526 | 2026-11-16 | math.RA | Dave Goel | Improving Razmyslov's (1974) bound: the Nagata–Higman index is at most n² − 2 for n ≥ 3
- 2611.00527 | 2026-11-17 | math.RA | Dave Goel | Improving Razmyslov's (1974) bound: the Nagata–Higman index is at most n² − 2 for n ≥ 3, and other miscellanea
- 2611.00528 | 2026-11-16 | math.OA | Cédric ARHANCET | Quantitative similarities for amenable algebras of two-by-two matrix-valued functions
- 2611.00529 | 2026-11-16 | math.NT | Qiyue Tang | Three Properties of Markov–Hurwitz Equations
- 2611.00530 | 2026-11-16 | math.NT | Sarvagya Jain | Smooth Numbers in Arithmetic Progressions with Uniformity in the Residue Class
- 2611.00531 | 2026-11-16 | math.GR | G. Militaru | Which groups are automorphism groups of racks?
- 2611.00532 | 2026-11-17 | math-ph | Yuri Ximenes Lecca | Cohesive 2-Topoi: Foundational Aspects and Nonabelian Differential Cohomology
- 2611.00533 | 2026-11-16 | math.CA | Antony Lewis | Even Asymptotic Expansions and Uniform Hard-Edge Approximations for Wigner $3j$ and $6j$ Symbols at Fixed Rank
- 2611.00534 | 2026-11-16 | math.DG | Boyang Hu | Smooth isometric bending of a closed sphere
- 2611.00535 | 2026-11-16 | math.AG | Mark Kisin | Essential dimension of geometric local systems
- 2611.00536 | 2026-11-16 | math.NT | Jensen Kohlmeyer | Consecutive primes at distances 123,662 and 125,318
- 2611.00538 | 2026-11-16 | math.MP | Francesco Grotto | Phase Transition and Spontaneous Translation Symmetry Breaking in Negative Temperature Point Vortex Ensembles
- 2611.00540 | 2026-11-16 | math.CO | Dave Goel | Wills' (1981) conjecture holds if and only if the dimension is at most 4
- 2611.00541 | 2026-11-16 | math.CO | Dave Goel | Wills' (1981) conjecture holds if and only if the dimension is at most 4, and other miscellanea
- 2611.00542 | 2026-11-17 | math.RA | Qiyuan Ma | The relations of a Lie subalgebra considered by Tao: a complete presentation
- 2611.00543 | 2026-11-17 | math.MP | Zeng Chunping | From Four-Dimensional Wilson Lattice Gauge Theory to Quantum Yang--Mills Theory, with a Conditional Mass-Gap Theorem
- 2611.00544 | 2026-11-17 | math.DG | Dave Goel | The Osserman (1990) conjecture is fully resolved
- 2611.00546 | 2026-11-17 | math.DG | Dave Goel | The Osserman (1990) conjecture is fully resolved, and other miscellanea
- 2611.00547 | 2026-11-17 | math.FA | Dave Goel | The Matsaev (1971) conjecture is false for every p ≠ 2
- 2611.00548 | 2026-11-17 | math.FA | Dave Goel | The Matsaev (1971) conjecture is false for every p ≠ 2, and other miscellanea
- 2611.00549 | 2026-11-20 | math.DS | Manvir Jaswal | Obtuse rational lattice triangles
- 2611.00550 | 2026-11-18 | math.NT | Oleksiy Babanskyy | Sun's supercongruence for two Apéry-like binomial sums
- 2611.00551 | 2026-11-18 | math.NT | Oleksiy Babanskyy | Sun's supercongruence for two Apéry-like binomial sums at discriminant -20
- 2611.00552 | 2026-11-18 | math.CO | Oleksiy Babanskyy | An upper bound for three-sunflower-free families of four-element sets
- 2611.00553 | 2026-11-18 | math.OC | Tiancheng Xu | Robust Strictly Positive Real Synthesis for Polynomial Polytopes
- 2611.00554 | 2026-11-18 | math.CO | Oleksiy Babanskyy | Cyclotomic Weight Chambers for Reverse-Complement-Invariant Minimum Decycling Sets
- 2611.00555 | 2026-11-18 | math.NT | Oleksiy Babanskyy | Cyclotomic Digit-Reversal Thresholds: Explicit Slopes, Effective Periods, and Uniform Families
- 2611.00556 | 2026-11-18 | math.GR | Roy van Rijn | Counterexamples to the Mathieu Property: From Explicit Quotient Constructions to a General Classification
- 2611.00557 | 2026-11-18 | math.OC | Tiancheng Xu | A Fifth-Order Hurwitz Interval Polynomial Family Without a Degree-Four Weak Strictly Positive Real Numerator
- 2611.00558 | 2026-11-18 | cs.DS | Jennifer Voitle | A self-contained proof of the exponent threshold 0.4875754036 for worst-case Subset Sum
- 2611.00559 | 2026-11-18 | math.LO | Zhenyu Sun | Algorithmic and Provable Precision of Monotone Approximations
- 2611.00560 | 2026-11-18 | math.NA | Ivan BESEVIC | The Simultaneous Rectangle for Systems, without Homotopy: All the Solutions of a Polynomial System, Each in a Certified Ball, with a Proof That None Is Missing
- 2611.00561 | 2026-11-18 | math.FA | Samir Hamad | Daugavet renormings via poor subspaces
- 2611.00562 | 2026-11-18 | math.CO | Samuil Petkov | A Full-Sequence Quantitative Gap Between the Chromatic and Cochromatic Numbers of a Random Graph
- 2611.00563 | 2026-11-18 | math.CO | Samuil Petkov | Obligatory triple systems: atoms, spectra and decompositions
- 2611.00564 | 2026-11-18 | math.CO | Samuil Petkov | Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284
- 2611.00565 | 2026-11-18 | math.RA | Samuil Petkov | The repeated-pair symmetric nonnegative inverse eigenvalue problem in dimension five
- 2611.00566 | 2026-11-18 | math.PR | Samuil Petkov | A sharp lower bound for entropy first-passage skewness in a three-state Markov ring
- 2611.00567 | 2026-11-18 | math.DS | Jason Turner | Inclusions and invariant forms of Svinin's recurrences
- 2611.00568 | 2026-11-18 | math.CV | Quanyu Tang | On meromorphic functions sharing three values IM and one value CM
- 2611.00569 | 2026-11-18 | math-ph | Mihaly A. Csirik | Unique continuation for the Pauli-Fierz Hamiltonian
- 2611.00570 | 2026-11-18 | math.NT | David Niedbala Giraudin | An upper bound 0.4893562 for the upper density of the integers p+2^k
- 2611.00571 | 2026-11-18 | math.NT | David Niedbala Giraudin | The 2-adic valuation of the symmetric Prouhet-Tarry-Escott constant at sizes 13 and 15
- 2611.00572 | 2026-11-18 | math.NT | Zeng Chunping | The Tower Side of the DIC Audit: Semistable Towers, the Barrier $\kappa\le\frac13$, and the Conductor--Discriminant Constant
- 2611.00573 | 2026-11-18 | math.CA | Paolo Leonetti | Representation of Degrees of Convergence by Nonadditive Measures
- 2611.00574 | 2026-11-18 | math-ph | Zhenyu Sun | Schwinger–Strebel measures for planar four-point correlators
- 2611.00575 | 2026-11-18 | quant-ph | Soo-Jong Rey | Hybrid Quantum Algorithms for Summary Statistics of Nonlinear PDEs with Random Initial Data
- 2611.00576 | 2026-11-18 | math.NT | Jit Wu Yap | An Averaged Iwasawa Approach to Mordell over Q
- 2611.00577 | 2026-11-18 | math.AP | Xi Chen | Infinite cascades for the defocusing cubic nonlinear Schr\"odinger equation on the square torus
- 2611.00579 | 2026-11-18 | math.NT | Ryuya Hora | GPF-Tribonacci sequences admit no uniform linear bound
- 2611.00580 | 2026-11-18 | math.MP | Patrick Lopatto | Uniform Spectral Gap for the AKLT Model on the Square Lattice
- 2611.00581 | 2026-11-18 | math.NT | Liam Kruer | Sharp growth and gap exponents for admissible sequences
- 2611.00582 | 2026-11-18 | math.CO | Liam Kruer | Anti-concentration of the chromatic number of a dense random graph
- 2611.00583 | 2026-11-18 | math.CV | Liam Kruer | The sharp constant in the Erdős maximum-term problem
- 2611.00584 | 2026-11-18 | math.LO | Liam Kruer | A finite-color partition relation for ω₁²
- 2611.00585 | 2026-11-18 | math.LO | Liam Kruer | Relative independence of the simultaneous chromatic number at ℵ₁
- 2611.00586 | 2026-11-18 | math.MG | Sebastien Palcoux | A Universal Square-Root-of-Six Bound for Kissing Numbers
- 2611.00587 | 2026-11-18 | math.AG | Ryan Hackbarth | Plane Algebraic Curve Families from Normalized Zeta Series: Prime-Base Extensions and Composite Breakdown
- 2611.00588 | 2026-11-18 | math.MG | Sihan Chen | Convex-body volume counterexamples: Convex-body volume counterexamples to hyperplane equipartition
- 2611.00589 | 2026-11-18 | math.AC | Jason Turner | Cluster monomials and finite type
- 2611.00590 | 2026-11-18 | math.CA | Oleksiy Babanskyy | Sup-norm stability radii for a nodal face of the $B_3$ spherical discriminant
- 2611.00591 | 2026-11-18 | math.NT | Manvir Jaswal | The rational points of the non-split Cartan modular curve of level 25
- 2611.00592 | 2026-11-18 | math.FA | Cédric ARHANCET | Spectral measures for subfactors and Lie groups
- 2611.00593 | 2026-11-19 | math.NT | Roy van Rijn | Pointwise representation counts for Eisenstein restricted sums
- 2611.00594 | 2026-11-19 | quant-ph | Marc Sperzel | Spontaneous X-rays Exclude Gaussian Covariant Classical–Quantum Gravity
- 2611.00595 | 2026-11-19 | math.GT | Roy van Rijn | Prime Knots with Augmentation-Rank Gaps at Unbounded Bridge Number
- 2611.00596 | 2026-11-19 | math.PR | Roy van Rijn | The Dimension-Degree Boundary for Gaussian Moment Vanishing
- 2611.00597 | 2026-11-19 | math.NT | Hernandez Juan | Integrality and polynomiality in Somos recurrences
- 2611.00598 | 2026-11-19 | math.NT | Sunay Venkat | Ramanujan primes and primes of exponent one in products of consecutive integers
- 2611.00599 | 2026-11-19 | math.NT | Sunay Venkat | Equal prime divisors in disjoint blocks of consecutive integers
- 2611.00600 | 2026-11-19 | math.NT | twinheterodox | An asymptotic lower bound for the number of irrational even beta values
- 2611.00601 | 2026-11-19 | math.NT | twinheterodox | Two shorter intervals of even Dirichlet beta values
- 2611.00602 | 2026-11-19 | math.NT | Danny Plymesser | Counting powerful products of consecutive integers
- 2611.00603 | 2026-11-19 | math.RT | Teo Banica | Invariant tensor dimensions as Hamburger moments
- 2611.00604 | 2026-11-19 | math.CO | Viktor Diakin | Three Roles and One Bit: All Optimal Tables and Equality Graphs
- 2611.00605 | 2026-11-19 | math.NT | twinheterodox | Uniform intervals for irrational even beta values
- 2611.00606 | 2026-11-19 | math.RA | Jason Turner | A Candidate Proof of the Fixed-Cartan Root Property for c-Vectors
- 2611.00607 | 2026-11-19 | math.NT | David Niedbala Giraudin | Old and new Drinfeld cusp forms of level t in characteristic 2: the weights k = 2^m + 1
- 2611.00608 | 2026-11-19 | math.MP | Zeng Chunping | The Assumption Package of the Yang–Mills Construction: Formal Definitions and Derivations
- 2611.00610 | 2026-11-19 | math.CO | Rob Sullivan | A strengthening of some results of the paper "Structured sunflowers and canonical Ramsey properties"
- 2611.00611 | 2026-11-19 | math.NT | Zeng Chunping | Power-saving bounds for balanced radical triples via small Pell discriminants
- 2611.00612 | 2026-11-19 | math.CO | Yair Lavi | Counterexamples to coefficient conjectures for plane Penrose polynomials
- 2611.00613 | 2026-11-19 | math.NT | twinheterodox | The alternating sum of reciprocal Fibonacci cubes is irrational
- 2611.00614 | 2026-11-23 | math.MP | Aiden Smith | THE INEQUALITY I2 < 2I1 FOR THE SKYRME PROBLEM AND THE EXISTENCE OF A MINIMISER OF DEGREE TWO
- 2611.00615 | 2026-11-19 | math.NT | twinheterodox | Irrational values of Dirichlet series with periodic coefficients
- 2611.00616 | 2026-11-19 | math.OA | Teo Banica | Spectral measure blowup for Hadamard subfactors
- 2611.00617 | 2026-11-19 | math.NT | David Niedbala Giraudin | Sums of three composite triangular numbers
- 2611.00618 | 2026-11-19 | math.NT | David Niedbala Giraudin | A Chebyshev bound for the constant in the Prouhet-Tarry-Escott problem
- 2611.00619 | 2026-11-19 | cs.CC | Yuwen Zhou | Circle configurations and the hardness of promise graph and hypergraph coloring
- 2611.00620 | 2026-11-19 | math-ph | Robert R. MacGregor | On sequential ideal measurements in the exceptional Jordan algebra
- 2611.00621 | 2026-11-19 | math.NT | Zeng Chunping | Complete modulus locking in the exceptional set of the abc conjecture
- 2611.00622 | 2026-11-19 | math.NT | Luis Dieulefait | Modularity of the factors of an automorphic tensor product
- 2611.00623 | 2026-11-19 | math.NT | twinheterodox | The weight-three Lambert sum at the golden ratio is irrational
- 2611.00624 | 2026-11-19 | math.NT | twinheterodox | Irrational values of Dirichlet series with growing period
- 2611.00625 | 2026-11-19 | math.KT | Niels Feld | Gersten exactness with invertible coefficients for excellent regular local surfaces
- 2611.00626 | 2026-11-19 | math.MG | Antoine Olivier | An explicit formal dual for every configuration $\Gamma(C,C^\perp)$ of Bierbrauer–Edel's definition, and formal isoduality of the packings in dimensions 18, 28 and 30
- 2611.00627 | 2026-11-19 | cs.CC | Mohamed Fradj | Thermodynamic saturation and prescribed window barriers for Kleinian-code graded spaces
- 2611.00628 | 2026-11-19 | math.AG | David Jordan | Christol’s Conjecture for Non-Resonant Globally Bounded Hypergeometric Series of Height Two
- 2611.00629 | 2026-11-19 | math.SP | Jason Davies | The equilateral triangle maximises the first Steklov eigenvalue among triangles
- 2611.00630 | 2026-11-19 | math.CO | Jason Davies | The shortest word containing every permutation of ten symbols as a subsequence has length 83
- 2611.00631 | 2026-11-19 | math.QA | Gerald Höhn | An Extremal Vertex Operator Algebra of Central Charge c=64
- 2611.00632 | 2026-11-19 | math.NA | Teo Banica | Numerical evidence for the almost Hadamard conjecture
- 2611.00633 | 2026-11-19 | cs.CC | Jason Davies | Parameterised complexity of graph homomorphism to odd cycles
- 2611.00634 | 2026-11-19 | cs.CC | Yilin Liu | Black-box identity testing for affine orbits of read-once oblivious algebraic branching programs
- 2611.00635 | 2026-11-19 | cs.FL | Dave Goel | The Černý (1969) conjecture holds for quasi-Eulerian automata of degree one
- 2611.00636 | 2026-11-19 | math.NT | Paul Pollack | Daboussi's elementary proof of the prime number theorem, reconsidered
- 2611.00637 | 2026-11-19 | math.CO | Abhinav Nellore | Hadamard matrices of orders 668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948 and 1964
- 2611.00638 | 2026-11-19 | math.NT | twinheterodox | A height criterion for irrational weight-three Lambert sums
- 2611.00639 | 2026-11-19 | math.NT | twinheterodox | A weighted reciprocal Lucas sum lies outside ℚ(√5)
- 2611.00640 | 2026-11-19 | math.QA | Andrew Riesen | Vertex operator algebras from Flohr's second family realising doubles of near-group categories $\mathbb{Z}_n+n$ for even $n$
- 2611.00641 | 2026-11-19 | math.QA | Sebastien Palcoux | Grothendieck rings of complex fusion categories: rank 2
- 2611.00642 | 2026-11-19 | math.QA | Sebastien Palcoux | Grothendieck rings of complex fusion categories: rank 3
- 2611.00643 | 2026-11-19 | math.NT | twinheterodox | The sum of the reciprocal Mersenne cubes is irrational
- 2611.00644 | 2026-11-19 | math-ph | Runze Zhong | Uniform Spectral Gap and Stability for the Spin-2 Square-Lattice AKLT Model with Free Boundaries
- 2611.00645 | 2026-11-19 | math.QA | Sebastien Palcoux | Grothendieck rings of complex fusion categories: rank 4
- 2611.00646 | 2026-11-19 | math-ph | MengHan Tsai | Can moving the mouths of a self-supporting wormhole make a shortcut? A no-shortcut theorem in a two-dimensional loop model
- 2611.00647 | 2026-11-19 | math.CV | Ryan Hackbarth | Fourier Epicycles and Antisymmetric Signed-Area Conservation in Normalized Riemann Zeta Terms
- 2611.00648 | 2026-11-19 | math.CT | Zhenyu Sun | Finite model spaces and coherent sheaf models
- 2611.00649 | 2026-11-19 | math.AG | Hernandez Juan | A note on tropical convexity
- 2611.00651 | 2026-11-19 | math.MP | Alberto Gandolfi | Towards a conformal field theory of critical percolation. II. Scalar responses and null identities
- 2611.00652 | 2026-11-19 | cs.DS | Yilin Liu | Deterministic almost-linear time for general matching and network flow
- 2611.00653 | 2026-11-19 | math.CO | Luis Ferroni | Ehrhart positivity for polypositroids
- 2611.00654 | 2026-11-19 | math.PR | Igor Kortchemski | BKT asymptotics for the quenched free energy of hierarchical pinning
- 2611.00655 | 2026-11-19 | math.RA | Jesus Vilela Jato | Flip-connectivity of octonion bracketing classes
- 2611.00656 | 2026-11-19 | cs.IT | Samuil Petkov | State complexity of rare-switching tracking: universal bounds and sharp counter tradeoffs
- 2611.00657 | 2026-11-19 | math.PR | Samuil Petkov | Entropy Production under Hidden-State Reduction: Exact Safety and Non-Testability
- 2611.00658 | 2026-11-19 | math.PR | Samuil Petkov | Complete positivity and equilibrium realizations of reversible observations
- 2611.00659 | 2026-11-19 | math.ST | Samuil Petkov | The exact FDR–FNR frontier and a separable gap under one-factor Gaussian dependence
- 2611.00660 | 2026-11-19 | math-ph | Samuil Petkov | A four-state Markovian Mpemba effect in which every triplet test fails
- 2611.00661 | 2026-11-19 | math.PR | Samuil Petkov | Observation cost of nonequilibrium in nonnormal networks: a matched exponent for an explicit four-state generator
- 2611.00662 | 2026-11-19 | math.PR | Samuil Petkov | Spectral outliers of self-coupled covariance matrices with exact zero weights
- 2611.00663 | 2026-11-19 | math.ST | Samuil Petkov | Finite-resolution information about a common clock: alias depth, holding-time loss, and the sampled Ehrenfest chain
- 2611.00664 | 2026-11-19 | math.RT | Rui Chen | A counterexample to a stability question for unramified multiplicity one symmetric pairs
- 2611.00665 | 2026-11-19 | cs.DS | Yilin Liu | Exact minimum-cost arborescences under a single arc failure
- 2611.00666 | 2026-11-19 | math.NT | Sinisa Slijepcevic | Non-existence of non-Eulerian irregular Diophantine quadruples
- 2611.00668 | 2026-11-19 | math.AG | Jiarui Fei | Schubert Cox Rings and Root Operators
- 2611.00669 | 2026-11-19 | math.MG | Fabrice Baudoin | Gradient structures on metric measure spaces
- 2611.00670 | 2026-11-19 | math.CO | William Howe | Sharp packing bounds for Poly-5 and Handy-Octs
- 2611.00671 | 2026-11-19 | math.SP | Lüwei Dong | Maximizing the First Positive Neumann Eigenvalue of Simple Pentagons
- 2611.00672 | 2026-11-19 | math.NT | Roy van Rijn | Pointwise Correlations of Quadratic Form Values and Splitting Semigroups
- 2611.00673 | 2026-11-19 | math.NT | Roy van Rijn | Exact Sumsets of Primitive Quadratic Norms
- 2611.00674 | 2026-11-20 | math.CO | Alessandro Baravelli | The Unfair 0–1 Polynomial Conjecture for Trinomial Factors
- 2611.00675 | 2026-11-20 | math.AG | David Niedbala Giraudin | A residue obstruction for the family F_2 with (m,n)=(3,5): the degree pair (75,125) in the plane Jacobian problem
- 2611.00676 | 2026-11-20 | math.CO | Alexandre Couret | Reconstructing three-point supports from their ordered convolution squares
- 2611.00677 | 2026-11-20 | math.CO | Arthur | Regular induced subgraphs in bounded independent-edge arrays
- 2611.00678 | 2026-11-20 | math.NT | Mathieu Dutour Sikiric | Algorithms for computing iso-Delaunay domains
- 2611.00679 | 2026-11-20 | math.MG | Sihan Chen | Solutions to Bianchi's covariogram problem and Kobayashi's Fourier zero-set problem for \(C^2_+\) convex bodies
- 2611.00680 | 2026-11-20 | math.MG | William Howe | All 97 Chaos Tiles duos in a single 66-tile arrangement
- 2611.00681 | 2026-11-20 | math.CO | William Howe | The edge sums of seven double-six domino frames
- 2611.00682 | 2026-11-20 | math.NT | William Howe | Two primitive Gaussian Fermat–Catalan identities
- 2611.00683 | 2026-11-20 | math.CO | William Howe | Hanoi tilings with a prescribed number of bottom squares
- 2611.00684 | 2026-11-20 | math.PR | Alexander Dabrowski | Convex, time-decreasing functions need not preserve semimartingales
- 2611.00685 | 2026-11-20 | math.AG | David Niedbala Giraudin | A residue obstruction for the whole family F_2 in the plane Jacobian problem
- 2611.00686 | 2026-11-20 | math.GT | RJ Acuna | The strong AJ conjecture for hyperbolic prime knots is false
- 2611.00687 | 2026-11-20 | math.NT | Tomislav Pejkovic | Root separation in one-parameter families of integer polynomials
- 2611.00688 | 2026-11-20 | math.CO | William Howe | Counting triangles with interlacing rows
- 2611.00689 | 2026-11-20 | math.CA | William Howe | Character coefficients for integrals of odd products of hyperbolic tangents
- 2611.00690 | 2026-11-20 | math.SP | Lüwei Dong | Maximizing the First Positive Neumann Eigenvalue of Pentagons and Hexagons
- 2611.00691 | 2026-11-20 | math.SP | Jason Davies | The equilateral triangle is the extremal triangle for the lowest Robin eigenvalue, for every boundary parameter
- 2611.00692 | 2026-11-20 | math.NT | Tomislav Pejkovic | Root separation for polynomials over $\mathbb{F}_q[T]$
- 2611.00693 | 2026-11-20 | math.NT | Shawn Krisman | Irrationality of odd q-zeta values at real quadratic units
- 2611.00694 | 2026-11-20 | math.NT | John Tripodo | Sharp finite cases of the Erdős–Surányi interval-product problem: g(4) = 5 and g(5) = 6
- 2611.00695 | 2026-11-20 | math.NT | Shawn Krisman | $t^{\log t}$ is transcendental for almost all integers $t$
- 2611.00696 | 2026-11-20 | math.OC | Yilin Liu | Linear-size sparsification from self-concordant barriers
- 2611.00697 | 2026-11-20 | math.GN | Lucas Alves de Almeida | Mosaic spaces generated by continua and by Peano continua: answers to three questions recorded by Lavallee
- 2611.00698 | 2026-11-20 | math-ph | Lior Isthmus | A two-chirality twistor correspondence for smooth Lorentzian Ricci-flat germs
- 2611.00699 | 2026-11-20 | math.NT | Danny Plymesser | Powerful values of quadratic polynomials
- 2611.00700 | 2026-11-20 | math.CA | Dave Goel | Erdős's 1974 distance-product volume problem resolved: the ball is always the unique maximizer in d ≥ 2
- 2611.00701 | 2026-11-20 | math.CA | Dave Goel | Erdős's 1974 distance-product volume problem resolved: the ball as unique maximizer, sharp inradius stability, and other miscellanea
- 2611.00702 | 2026-11-20 | math.NT | Shawn Krisman | Linear independence of reciprocal and reciprocal-cube sums of Lucas sequences
- 2611.00703 | 2026-11-20 | math.NT | Shawn Krisman | Products of two logarithms and arithmetic holonomy bounds
- 2611.00704 | 2026-11-20 | math.NT | Shawn Krisman | Many odd-power reciprocal sums of Lucas sequences are irrational
- 2611.00705 | 2026-11-20 | math.ST | Shankar Sivarajan | An explicit determinantal formula for limits of iterative proportional fitting with a binary variable
- 2611.00707 | 2026-11-20 | math.CO | P. Graham | Existence of locally toroidal regular 4-polytopes
- 2611.00708 | 2026-11-20 | math.PR | Christopher Long | The exact Poisson–binomial comparison in every dimension
- 2611.00709 | 2026-11-20 | math.AG | David Niedbala Giraudin | The degree pair (126,84) in the plane Jacobian problem: the point (16/3,10) is not a regular corner
- 2611.00710 | 2026-11-20 | math.AG | David Niedbala Giraudin | The degree pair (84,126) in the plane Jacobian problem: exclusion of the shape with final corner (19/7,5)
- 2611.00711 | 2026-11-20 | math-ph | Shipei Hu | A Finite-Regulator Variational–Stochastic Programme: Geometry, Gauge Fields, Matter, and the Arrow of Time
- 2611.00712 | 2026-11-20 | math.QA | Hernandez Juan | Quantum affine representations and cluster characters
- 2611.00713 | 2026-11-20 | math.AG | David Niedbala Giraudin | A shape of maximal degree 150 in the plane Jacobian problem: the point (18/5,8) is not a regular corner
- 2611.00714 | 2026-11-20 | math.AG | David Niedbala Giraudin | The starting corner (7,35) in the plane Jacobian problem: the point (18/7,4) is not a regular corner
- 2611.00715 | 2026-11-20 | math.NT | David Niedbala Giraudin | A remark on the independence step in Shkredov's approach to Zaremba's conjecture
- 2611.00716 | 2026-11-20 | math.NT | ESRAFIL ALI MOLLA | Rational points on intersections of cubic and quadric hypersurfaces in $28$ variables
- 2611.00717 | 2026-11-20 | math.AG | David Niedbala Giraudin | The degree pair (56,140) in the plane Jacobian problem: exclusion of the shape with starting corner (7,21) and final corner (13/7,3)
- 2611.00718 | 2026-11-20 | math.OC | Tiancheng Xu | Counterexamples to Robust Strictly Positive Real Synthesis for High-Order Interval Polynomials
- 2611.00719 | 2026-11-20 | math.OC | Tiancheng Xu | All-Order Robust Strictly Positive Real Synthesis for Wide-Interval Polynomial Families
- 2611.00720 | 2026-11-20 | math.CO | David Niedbala Giraudin | The ordered 2x2 corner pattern: a removal exponent of at least 9/2, and other partial results
- 2611.00721 | 2026-11-20 | math.AC | Yiqi Xu | Vasconcelos' conjecture on the module of differentials
- 2611.00722 | 2026-11-20 | math-ph | Teo Banica | Quantum permutations and the Standard Model algebra
- 2611.00723 | 2026-11-20 | math.NT | Hernandez Juan | Cases of the Agashe–Ribet–Stein Conjecture
- 2611.00724 | 2026-11-20 | math.AG | David Niedbala Giraudin | The degree pair (88,132) in the plane Jacobian problem: exclusion of the shape with starting corner (11,33) and final corner (19/4,8)
- 2611.00725 | 2026-11-20 | math-ph | Antony Lewis | Semiclassical Asymptotics of Wigner 3j and 6j Symbols at Growing Rank: Phase Horizons and Turning Connections
- 2611.00726 | 2026-11-20 | math.DS | Joshua Boorstein | Complete periodicity of perpendicular billiards in rational triangles of prime denominator
- 2611.00727 | 2026-11-20 | math.CO | P. Graham | The Heawood family is not the complete list of excluded minors for Colin de Verdière invariant at most 5
- 2611.00729 | 2026-11-20 | math.CO | Jason Davies | Peaceable queens on boards of size 16 to 20
- 2611.00730 | 2026-11-20 | math.CO | twinheterodox | Boxes with cyclic tiling groups have one layer or size 2 × 2 × 4
- 2611.00732 | 2026-11-20 | math.PR | Christopher Long | Extremizers of the expected missing mass under an entropy constraint
- 2611.00733 | 2026-11-20 | math.AG | David Niedbala Giraudin | Two shapes of maximal degree 135 in the plane Jacobian problem: exclusion of the degree pairs (135,90) and (90,135) with corners (9,36) and (17/9,4)
- 2611.00734 | 2026-11-20 | math.AG | Shankar Sivarajan | The maximum likelihood degree of no-three-way interaction models
- 2611.00735 | 2026-11-20 | math.PR | Heng Ma | On the Monotonicity of the Speed of Biased Random Walks on GW Trees
- 2611.00736 | 2026-11-20 | math.NT | Christopher Long | Algebraic Exponential Integrals: Transcendence and Linear Relations
- 2611.00737 | 2026-11-20 | math.NT | Christopher Long | A Linear Kontsevich–Zagier Theorem for Compact Exponential Periods on the Affine Line
- 2611.00738 | 2026-11-20 | math.NT | Christopher Long | A Polynomial Kontsevich–Zagier Theorem for Compact Exponential Periods on the Affine Line
- 2611.00739 | 2026-11-20 | math.GN | Luke Hammer | Common Periodic Points of Commuting Interval Maps
- 2611.00740 | 2026-11-20 | math.CO | P. Graham | A counterexample to the cocircuit diameter conjecture
- 2611.00741 | 2026-11-20 | math.NT | Baiying Liu | Mixed character moments and a zero-free half-plane for unitary Hecke L-functions
- 2611.00742 | 2026-11-20 | math.CV | user Alderliefste | The $(3,4,\infty)$ family of complex six-spheres. V. Complex fourfolds from the family
- 2611.00743 | 2026-11-20 | math.NT | Tomislav Pejkovic | On several conjectures concerning p-adic continued fractions
- 2611.00744 | 2026-11-20 | math.CA | Jamie Martin | Half-line density and the structure of crystalline measures
- 2611.00745 | 2026-11-20 | math.PR | Teo Banica | Planar rotators with Hadamard couplings
- 2611.00746 | 2026-11-20 | math.CO | Liam Kruer | A ZFC counterexample to Taylor's conjecture on finite subgraphs
- 2611.00747 | 2026-11-20 | math.NT | Liam Kruer | A divisor-closed criterion for Behrend sequences
- 2611.00748 | 2026-11-20 | math.NT | Liam Kruer | Harmonic dyadic shifts and short sums of factorial divisors
- 2611.00749 | 2026-11-20 | math.CO | Liam Kruer | A counterexample to the Erdős triangle–four-cycle asymptotic
- 2611.00750 | 2026-11-20 | math.NT | Liam Kruer | Infinitely many exceptions to a prime-square representation problem of Erdős
- 2611.00751 | 2026-11-21 | math.CO | Liam Kruer | Four-cycles one edge above the extremal threshold
- 2611.00752 | 2026-11-21 | math.NT | Liam Kruer | An Explicit Removal Estimate for Reciprocal-Sum-Free Sets
- 2611.00753 | 2026-11-21 | math.NT | Liam Kruer | The sharp deficit in primitive signed reciprocal relations
- 2611.00754 | 2026-11-21 | math.NT | Liam Kruer | The sharp asymptotic for distinct multiples in an interval: a Lean formalization
- 2611.00755 | 2026-11-21 | math.NT | Liam Kruer | Erdős 1057 / JSP-000877: mathematical account of the submitted proof
- 2611.00756 | 2026-11-21 | math.CO | Liam Kruer | A counterexample to Erdős problem 1068
- 2611.00757 | 2026-11-21 | math.CA | Liam Kruer | An exact algebraic construction for Erdős's interpolation minimum
- 2611.00758 | 2026-11-21 | math.NT | Liam Kruer | Balanced additive complements with bounded representation functions
- 2611.00759 | 2026-11-21 | math.CV | Liam Kruer | Cofinite derivative zeros at the order-one threshold
- 2611.00760 | 2026-11-21 | math.DS | Chih-Yao Wu | Centered Cocircular Central Configurations for Homogeneous and Logarithmic Potentials
- 2611.00761 | 2026-11-21 | math.NT | Liam Kruer | A uniform square-root lower bound for non-unique sums and a resolution of Erdős problem 14
- 2611.00762 | 2026-11-21 | math.CO | Liam Kruer | Size Ramsey numbers at high average degree
- 2611.00763 | 2026-11-21 | math.CO | Liam Kruer | A counterexample to Erdős problem 108 via arc graphs
- 2611.00764 | 2026-11-21 | math.NT | Liam Kruer | Infinitely many decreases in the thresholds for sums of distinct powers
- 2611.00765 | 2026-11-21 | math.NT | Liam Kruer | The three parts of Erdős Problem 12: counting functions and reciprocal sums
- 2611.00766 | 2026-11-21 | math.CO | Liam Kruer | Subexponential bounds for distinct-distance subsets
- 2611.00767 | 2026-11-21 | math.NT | Liam Kruer | Small maximal integer Sidon sets by finite phase colorings
- 2611.00768 | 2026-11-21 | math.NT | Liam Kruer | Completeness of two floor-doubling sequences
- 2611.00769 | 2026-11-21 | math.AP | Manvir Jaswal | Density of blow-up data and regularity at the blow-up time for the three-dimensional Euler equations
- 2611.00770 | 2026-11-21 | math.CO | P. Graham | The Turán density of the tight five-cycle
- 2611.00771 | 2026-11-21 | math.CO | P. Graham | Monotone classes of bounded game chromatic number have bounded arboricity
- 2611.00772 | 2026-11-21 | math.CO | Liam Kruer | Vertex-critical four-chromatic graphs with no small critical edge set
- 2611.00773 | 2026-11-21 | math.NT | Liam Kruer | A periodic-summand characterization for Erdős problem 335
- 2611.00774 | 2026-11-21 | math.NT | Liam Kruer | An exact formula for fork-free sets of integers and the irrationality of their density
- 2611.00776 | 2026-11-21 | math.NT | Liam Kruer | Erdős problem 859: a refutation of the logarithmic density law
- 2611.00777 | 2026-11-21 | math.SP | Lüwei Dong | The Square Maximizes the First Nonzero Steklov Eigenvalue Among Convex Quadrilaterals
- 2611.00778 | 2026-11-21 | math.CO | Liam Kruer | Matching order for Erdős problem 790
- 2611.00779 | 2026-11-21 | math.CO | Liam Kruer | Erdős problem 706 and uniform multiscale refinements
- 2611.00780 | 2026-11-21 | math-ph | Shankar Sivarajan | Free fermions from integer arithmetic: a Galois-theoretic test for free-fermionic spectra
- 2611.00781 | 2026-11-21 | math.NT | Liam Kruer | Asymptotically full minimal signed unit-fraction identities
- 2611.00782 | 2026-11-21 | math.NT | Liam Kruer | Recurring differences from overlapping arithmetic progressions
- 2611.00783 | 2026-11-21 | math.LO | Liam Kruer | Erdős problem 597 and finite-target independence
- 2611.00784 | 2026-11-21 | math.LO | Liam Kruer | A set mapping with small intersections and no large free set
- 2611.00785 | 2026-11-21 | math.NT | Liam Kruer | Erdős 196: A permutation of the natural numbers with no monotone four-term arithmetic progression
- 2611.00786 | 2026-11-21 | math.CO | Liam Kruer | A locally sparse graph with superlinear Ramsey growth
- 2611.00787 | 2026-11-21 | math.NT | Liam Kruer | Two smooth summands for every large integer
- 2611.00788 | 2026-11-21 | math.NT | Yilin Liu | Failure of the Li–Liu spectral hypothesis R under Dirichlet GRH
- 2611.00789 | 2026-11-21 | math.AG | user Alderliefste | A short proof of Deligne's bound for Frobenius eigenvalues, after Alpöge
- 2611.00790 | 2026-11-21 | math.RT | Jiarui Fei | Crystal Structures on Theta Bases
- 2611.00791 | 2026-11-21 | math-ph | Shankar Sivarajan | Rational points on Baxter's curve and roots of unity in the eight-vertex model
- 2611.00792 | 2026-11-21 | math.AP | Xi Chen | On finite-time blow-up of the 2D inviscid Boussinesq equations
- 2611.00793 | 2026-11-21 | math.CO | P. Graham | A base-r simplex that is not Ehrhart positive
- 2611.00794 | 2026-11-21 | math.CO | P. Graham | The seventh ternary density Hales–Jewett number
- 2611.00795 | 2026-11-21 | math.DS | P. Graham | Combinatorial periods of asymmetric billiard trajectories in the regular pentagon
- 2611.00796 | 2026-11-21 | math.CO | P. Graham | The Heawood family is not the complete list of excluded minors for 4-flat graphs
- 2611.00797 | 2026-11-21 | math.MG | P. Graham | A four-dimensional 4-reptile simplex
- 2611.00798 | 2026-11-21 | math.NT | Wren Aquila | Hooley's twisted cancellation below level $4/15$ does not force primes
- 2611.00799 | 2026-11-21 | math.NT | Manvir Jaswal | The Riemann hypothesis for Dirichlet L-functions [after Levent Alpöge]
- 2611.00800 | 2026-11-21 | math.NT | Sabah noori | Holes and Islands of Visible Points on the Triangular Lattice: Midpoint Bond Graphs and Prime-Sieve Bounds
- 2611.00802 | 2026-11-21 | math.ST | Man Huang | Separate fits and joint compatibility in heterogeneous coverage: finite-label models with shared calibration
- 2611.00805 | 2026-11-21 | math.CT | Haruhisa Enomoto | An extriangulated category with no triangulated embedding
- 2611.00807 | 2026-11-21 | math.NT | Shawn Krisman | The product $\log(1+1/N)\log(1+2/N)$ and rational conics through two logarithms
- 2611.00808 | 2026-11-21 | math.NT | Adam Henriksson | Balanced semiprimes in short intervals under the Riemann hypothesis
- 2611.00809 | 2026-11-21 | math.NT | Robin Zhang | A preliminary note on Alpöge's proposed proof of the generalized Riemann hypothesis
- 2611.00812 | 2026-11-21 | math.NT | Sinisa Slijepcevic | Outline of Alpöge's proof of the generalised Riemann hypothesis
- 2611.00813 | 2026-11-21 | math.AC | Christopher Long | Factorial Moments in Two Variables: Exact Leaf Transport and Trace Orthogonality
- 2611.00814 | 2026-11-21 | math.PR | Christopher Long | Optimal coupon packages and stochastic improvement of uniform group drawings
- 2611.00815 | 2026-11-21 | math.CO | Hernandez Juan | Proofs of two conjectures of Fomin and Pylyavskyy
- 2611.00816 | 2026-11-21 | math.RT | Jiarui Fei | Cluster-Crystal Realization of KR Cartan Algebras
- 2611.00817 | 2026-11-21 | math.DG | Sihan Chen | Pu's inequality for non-reversible Finsler metrics
- 2611.00818 | 2026-11-21 | math.AG | Teo Banica | Noncommutative curves and surfaces in small degree
- 2611.00819 | 2026-11-21 | math-ph | Shipei Hu | A Stochastic Molecular Mechanism for the Thermodynamic Arrow of Time: Least Action, Equilibrium, and Dissipative Variational Dynamics
- 2611.00820 | 2026-11-21 | math.PR | Igor Kortchemski | The speed of biased random walk on leafless Bienaymé trees is monotone
- 2611.00821 | 2026-11-21 | math.NT | Chenglong Yu | The maximal rank of an even hyperbolic lattice with nonzero exceptional lattice
- 2611.00822 | 2026-11-21 | math.NT | Matija Kazalicki | Atkin--Swinnerton-Dyer congruences for Kummer twists of Hauptmoduln
- 2611.00824 | 2026-11-21 | math.DG | Wenchang Yang | Smooth Isometric Embeddings of Closed Manifolds into $\mathbb{R}^{s_n+5}$ in High Dimensions
- 2611.00825 | 2026-11-21 | stat.TH | John Hessler | Reconstructing the Simulmatics 1960 Simulation: Mathematics, Methods and a Partial Replication
- 2611.00826 | 2026-11-21 | math.CV | Quanyu Tang | The Br\"uck conjecture and the growth of entire solutions of a differential equation
- 2611.00827 | 2026-11-21 | cs.CC | Frank Vega | An $83/84$ approximation for three-occurrence Horn formulas above the Unique Games thresholds
- 2611.00828 | 2026-11-21 | math.NT | twinheterodox | Three simplifications in the Alpöge–Claude argument for Dirichlet GRH
- 2611.00829 | 2026-11-21 | math.KT | Leo Pintar | Vanishing of $K_{4k}(\mathbb{Z})$ through degree 104 from Alpöge’s Step 17
- 2611.00830 | 2026-11-23 | math.CO | Jason Davies | $\gamma(Q_{35})=19$ and certified queen domination numbers up to $n=46$
- 2611.00831 | 2026-11-23 | math.RA | Teo Banica | Easiness over characteristic zero fields
- 2611.00832 | 2026-11-23 | math.NT | Michael Rubinstein | The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function
- 2611.00833 | 2026-11-23 | math.NT | Chenxin Huang | An Arakelov-theoretic perspective on the Alpöge–Claude argument on RH, after Calegari-Dimitrov-Tang
- 2611.00834 | 2026-11-23 | math.NT | Louis P. Slothouber | The Egami–Matsumoto conjecture: a natural boundary of the Goldbach generating series
- 2611.00835 | 2026-11-23 | math.NT | Sean Litsey | A bound for the irrationality exponent of real elliptic periods
- 2611.00836 | 2026-11-23 | math.MG | Peter Graham | The Thomson problem for N = 10
- 2611.00837 | 2026-11-23 | math.CO | Peter Graham | A quadratic lower bound for intervals in the Hales–Jewett theorem
- 2611.00838 | 2026-11-23 | math.RA | Peter Graham | A counterexample to the E-derivation part of the LNED conjecture
- 2611.00839 | 2026-11-23 | math.NT | twinheterodox | Auxiliary primes and interpolation points in the Alpöge–Claude argument for Dirichlet GRH
- 2611.00840 | 2026-11-23 | math.ST | Peter Graham | A counterexample on two kinds of positive dependence
- 2611.00841 | 2026-11-23 | math.NT | Sean Litsey | An irrationality measure for $\zeta(5)$
- 2611.00842 | 2026-11-23 | math.CO | Peter Graham | The Harborth constant of Cp ⊕ Cp for every prime p ≥ 11
- 2611.00843 | 2026-11-23 | math.RA | Peter Graham | No post-Lie algebra structures on pairs of perfect and nilpotent Lie algebras
- 2611.00844 | 2026-11-23 | math.CO | Peter Graham | Counterexamples to the conjectured characterization of Hamiltonian degree sequences in digraphs
- 2611.00845 | 2026-11-23 | math.MG | Peter Graham | The convex uniform 5-polytopes: a computer-assisted classification
- 2611.00846 | 2026-11-23 | math.CO | Christopher Long | The unique shortest rank-state cycle in Beggar-My-Neighbour: Six tricks and 38 individual plays
- 2611.00847 | 2026-11-23 | math.NT | Sean Litsey | Irrationality measures for $a\zeta(3)+b\pi^4$ and $\zeta(3)/\pi^4$
- 2611.00848 | 2026-11-23 | math.NT | Sean Litsey | Irrationality measures for dilogarithms of rational numbers
- 2611.00849 | 2026-11-23 | cs.DS | Nuutti Kuosa | Finding Two Connected Factors of a Finite Dynamical System in Quasipolynomial Time
- 2611.00850 | 2026-11-23 | math.NT | Wren Aquila | The mean square of the Goldbach error at every large endpoint
- 2611.00851 | 2026-11-23 | math.CV | user Alderliefste | The $(3,4,\infty)$ family of complex six-spheres. I. Periods, moduli and the two ends
- 2611.00852 | 2026-11-23 | math.NT | Zhongpai  Gao | Second Moments of Hecke Traces and Vertical Sato–Tate
- 2611.00853 | 2026-11-23 | math.CO | Peter Graham | A counterexample to a lit-only sigma-game conjecture
- 2611.00854 | 2026-11-23 | math.AP | Peter Graham | KPP fronts in the 1-1-1 ABC flow speed up linearly in every direction
- 2611.00855 | 2026-11-23 | math.CO | Peter Graham | A lattice parallelepiped with no unimodular triangulation
- 2611.00856 | 2026-11-23 | math.GR | Peter Graham | Connected quandles that refute Hayashi's conjecture
- 2611.00857 | 2026-11-23 | math.OC | Peter Graham | Competitive equilibrium can fail near equal budgets for three additive agents
- 2611.00858 | 2026-11-23 | math.CO | Peter Graham | Graceful 4-coloring of planar graphs is NP-complete
- 2611.00859 | 2026-11-23 | math.PR | Peter Graham | A counterexample to the very sparse greedy conjecture for random hitting sets
- 2611.00860 | 2026-11-23 | math.CO | Peter Graham | A proof of Geneson's continuous gluing conjecture
- 2611.00861 | 2026-11-23 | math.RA | Peter Graham | Faithful local dynamics on every finite acyclic graph
- 2611.00862 | 2026-11-23 | math.CO | Peter Graham | A subdivided 6-clique breaks a conjectured sum bound for independent monophonic-position colorings
- 2611.00863 | 2026-11-23 | math.CO | Peter Graham | Counts of maximal matchings in a graph need not be log-concave
- 2611.00864 | 2026-11-23 | math.CO | Peter Graham | The queueing polynomial is convex
- 2611.00865 | 2026-11-23 | math.GR | Peter Graham | A classification of solvable spinning-switches puzzles
- 2611.00866 | 2026-11-23 | math.CO | Peter Graham | A conjecture of Hopkins on golden Rado numbers
- 2611.00867 | 2026-11-23 | math.MG | Peter Graham | No holeless tetrad of four congruent pentagons
- 2611.00868 | 2026-11-23 | math.CO | Peter Graham | A graph whose zero-forcing polynomial is not unimodal
- 2611.00869 | 2026-11-23 | math.LO | Konstantin Slutsky | Orbit equivalence universality of the unitary group and the classification of II1 factors
- 2611.00870 | 2026-11-23 | math.NT | Peter Graham | Sharp linear bounds for the EKG sequence
- 2611.00871 | 2026-11-23 | math.CO | Peter Graham | Cyclic sieving for q-Kreweras numbers in the exceptional types
- 2611.00872 | 2026-11-23 | math.CO | Peter Graham | Greedy play can require more colors in the coloring game
- 2611.00873 | 2026-11-23 | math.CO | Peter Graham | A Steiner triple system with a broken chromatic spectrum
- 2611.00874 | 2026-11-23 | math.AP | Manvir Jaswal | A remark on the density of blow-up data for the Navier–Stokes equations
- 2611.00876 | 2026-11-23 | math.OA | Teo Banica | The magic of free spheres
- 2611.00877 | 2026-11-23 | math.CO | Peter Graham | The three-color Ramsey number of the 10-vertex path
- 2611.00878 | 2026-11-23 | math.CO | Hernandez Juan | Resolutions of conjectures on surface webs
- 2611.00879 | 2026-11-23 | math.CT | Ryuya Hora | The shape of mathematical universes
- 2611.00880 | 2026-11-23 | math.NT | Yutong Zhang | Proof of a conjectural formula of Guillera for $1/\pi^2$
- 2611.00881 | 2026-11-23 | math.NT | gilheum park | Full-Archive AST Stratification, Pinned Mathlib Boundary Audit, and Deep Hub Decompilation of the 17.37M-Line Alpöge-Claude Riemann Hypothesis Formalization
- 2611.00882 | 2026-11-23 | quant-ph | Joseph Shunia | The entropy photon-number inequality without an energy assumption
- 2611.00883 | 2026-11-23 | math.NT | Igor Zhuk | Total-Collapse Primes of Polynomial Maps over $\mathbb{F}_p$: Eighteen Families and Two Related Sequences
- 2611.00884 | 2026-11-23 | math.NT | Filip Najman | Isolated and sporadic points on $X_1(N)$ and $X_0(N)$
- 2611.00885 | 2026-11-23 | math.NT | Anton Vynohradov | Goldbach numbers in intervals of length $2\log^2 x$ under the Riemann hypothesis
- 2611.00886 | 2026-11-23 | cs.CC | Nuutti Kuosa | Division of Explicit Finite Dynamical Systems Is NP-Complete
- 2611.00887 | 2026-11-23 | math.NT | Jit Wu Yap | Elliptic Lehmer Bounds over Global Fields
- 2611.00888 | 2026-11-23 | math-ph | Lior Isthmus | Global wave completion and recognition of smooth twistor sources
- 2611.00889 | 2026-11-23 | math.CO | George Turcas | Integral zero-sum incidence identities and Davenport constants in rank three
- 2611.00890 | 2026-11-23 | math.CO | Dömötör Pálvölgyi | Transitive sets and Graham's radius conjecture
- 2611.00891 | 2026-11-23 | math.NT | Brice Pouly | An explicit bound below one half for a quartic Liouville correlation
- 2611.00892 | 2026-11-23 | math.DS | Brice Pouly | Sharp inequalities and stability for real profiles on arithmetic progressions
- 2611.00893 | 2026-11-23 | math.NT | Brice Pouly | Simultaneous quadratic probes: reconstruction thresholds and marked Poisson limits
- 2611.00894 | 2026-11-23 | math.NT | Brice Pouly | Reconstruction and sign prediction from sampled prime factors
- 2611.00895 | 2026-11-23 | math.NT | Brice Pouly | Small roots of split quadratic congruences and fundamental units in a quartic family
- 2611.00896 | 2026-11-23 | math.AG | David Niedbala Giraudin | The shapes of maximal degree 147 with starting corner (6,15) in the plane Jacobian problem
- 2611.00897 | 2026-11-23 | math.AG | David Niedbala Giraudin | Two shapes of maximal degree 147 in the plane Jacobian problem: exclusion of the degree pairs (147,98) and (98,147) with corners (7,42) and (13/7,6)
- 2611.00898 | 2026-11-23 | cs.DM | Prasanna Ramakrishnan | Elections with Condorcet Dimension 4
- 2611.00899 | 2026-11-23 | math.GN | Lucas Alves de Almeida | The Double Midset Conjecture for Metric Continua
- 2611.00900 | 2026-11-23 | math.AG | Teo Banica | Italian projective geometry goes free
- 2611.00901 | 2026-11-23 | math.CO | John Tripodo | There is no symmetric configuration $59_8$
- 2611.00902 | 2026-11-23 | math.NT | Seon-Woo Hong | Exact p-adic Valuations of Algebraic Binomial Coefficients and Transfer-Operator Enumeration of Separated Permutations: Resolutions of Open Problems in OEIS A387569, A392059, and A179967
- 2611.00903 | 2026-11-23 | math.NT | Trevor Cappallo | Subadditivity of the smooth number counting function for every smoothness bound
- 2611.00904 | 2026-11-23 | math.NT | Wren Aquila | Three isolated primes in the ternary Goldbach problem
- 2611.00905 | 2026-11-23 | math.NT | Nevil Wrigley | On Green's Problem 55: a Gowers-type norm on $\F_p^n \times \F_p^n$
- 2611.00906 | 2026-11-23 | math.CO | Teo Banica | Quantum partial permutations in action
- 2611.00907 | 2026-11-23 | math.DG | Igor Zelenko | A length-minimizing curve with discontinuous velocity in a smooth sub-Riemannian structure
- 2611.00910 | 2026-11-23 | math.NT | Yilin Liu | Sign changes of Kloosterman sums on moduli with at most three prime factors
- 2611.00911 | 2026-11-23 | math.NT | Sihan Chen | Tensor semistability from rectangular Specht lattices
- 2611.00912 | 2026-11-23 | math.NT | gilheum park | Reverse-Engineering OpenAI #003 and the Classical Riemann Barriers: Attribution Boundaries, Exact Stationary Points, Unimported Cubic Sieve Induction, Z[sqrt(921)] Farkas Duality, and Architectural Comparison with hexagon:2611.00881
- 2611.00913 | 2026-11-23 | math.MG | Alexander Kolpakov | Sharp dimension bounds for right-angled hyperbolic polytopes
- 2611.00914 | 2026-11-23 | math.NT | Yilin Liu | Upper bounds for nearly equal largest prime factors of consecutive integers
- 2611.00915 | 2026-11-23 | math.CO | Dave Goel | Xia's equations for the Higman–McLaughlin (1961) conjecture: exact solution counts when the norm equation is replaced by its sum
- 2611.00917 | 2026-11-23 | math.FA | Dave Goel | When is the Gohberg–Krupnik (1992) lower bound for aI+bH sharp? Exactly when Re(ab̄) = 0, for 1.2336… ≤ p ≤ 5.2807…, p ≠ 2
- 2611.00918 | 2026-11-23 | math.FA | Dave Goel | When is the Gohberg–Krupnik (1992) lower bound for aI+bH sharp? Exactly when Re(ab̄) = 0, for 1.2336… ≤ p ≤ 5.2807…, p ≠ 2. An expanded version, with other miscellanea
- 2611.00919 | 2026-11-23 | math.CO | Henry Shing | First differences of real-rooted integer polynomials and simplicial complexes
- 2611.00920 | 2026-11-23 | math.AG | Gerald Höhn | Chern-Pure Hyperkähler Manifolds and Tight Spherical Designs
- 2611.00921 | 2026-11-23 | math.NT | Shawn Krisman | Products of two $p$-adic logarithms at prime powers
- 2611.00922 | 2026-11-23 | math.CO | Samuel Korsky | Avoiding Isosceles Triangles in the Integer Grid
- 2611.00923 | 2026-11-23 | math.RT | Bob Smith | A proof of the open orbit conjecture
- 2611.00925 | 2026-11-23 | math.CV | Dave Goel | Springer's 1951 conjecture on inverse coefficients settled: true at every odd order, false at every even order from four on
- 2611.00927 | 2026-11-23 | math.PR | Quanyu Tang | Unconditional irreducibility of characteristic polynomials of symmetric Rademacher matrices
- 2611.00928 | 2026-11-23 | math.DS | Aapo Lipponen | Certificates of Absence: Validated Converse KAM for Flux Surfaces in Coil-Defined Fields
- 2611.00929 | 2026-11-23 | math.NT | Meng Tong | A computable Goldbach shift for a sequence of doubled squares
- 2611.00931 | 2026-11-23 | math.GT | Diaaeldin Taha | Closed Formulas for Masur–Veech Polynomials
- 2611.00932 | 2026-11-23 | cs.FL | Антон Борисов | Breaking the 7/48 n^3 Barrier for Synchronizing Automata
- 2611.00933 | 2026-11-23 | math.OC | Raimundo Julián Saona Urmeneta | Proper and Optimal Scoring Rules for Risk-Averse Agents
- 2611.00934 | 2026-11-23 | math.CA | khaled Alhamadi | The Polylogarithm as a Liouville Fractional Integral and a Related Fractional Differential Equation
- 2611.00935 | 2026-11-23 | math.NT | Jesus Vilela Jato | Collision Primes of J₀(23): Forced Congruences, Exceptional Local Factors, and a Pre-Registered Test of the Murty–Van Hirtum Constant
- 2611.00936 | 2026-11-23 | math.AG | user Alderliefste | A very ample counterexample to Kodaira vanishing on a surface, answering a question of Raynaud
- 2611.00937 | 2026-11-23 | math.AC | user Alderliefste | Integer-valued polynomials over a one-dimensional analytically irreducible local domain form a free module: Elliott's non-flatness conjectures fail
- 2611.00938 | 2026-11-23 | math.NT | user Alderliefste | Divisibility of invariant derivatives on formal groups of every height, on a question of Katz
- 2611.00939 | 2026-11-23 | math.NT | user Alderliefste | The question of Anderson and Ihara on the pro-p Galois action on the projective line minus three points, at every prime satisfying Vandiver's conjecture
- 2611.00940 | 2026-11-23 | math.GR | user Alderliefste | Relation (IV) of Nakamura and Schneps holds on the profinite Grothendieck-Teichmüller group, with an application to the two elliptic points of the modular curve
- 2611.00941 | 2026-11-23 | math.CO | Hernandez Juan | The lattice of rainbow bases
- 2611.00942 | 2026-11-23 | math.NT | twinheterodox | Higher weighted Lucas sums and even q-beta values
- 2611.00943 | 2026-11-23 | math.GR | Yotam  Shomroni | Expansion in powers of Suzuki groups
- 2611.00944 | 2026-11-23 | math.AG | David Niedbala Giraudin | A shape of maximal degree 135 in the plane Jacobian problem: exclusion of the complete chain (9,36), (9,24), (11/3,8)
- 2611.00945 | 2026-11-23 | math.CO | Nuutti Kuosa | How Many Cycle Lengths Can a Unique Quotient Require?
- 2611.00946 | 2026-11-23 | math-ph | Antti Hippeläinen | Balanced and superbalanced holographic entropy inequalities with arbitrarily large contraction scaling
- 2611.00947 | 2026-11-23 | math.AG | Shankar Sivarajan | The boundary structure of the maximum likelihood eliminant of $3\times3\times3$ tables
- 2611.00948 | 2026-11-23 | math.NT | Hernandez Juan | Freeness of the square root of the inverse different
- 2611.00949 | 2026-11-23 | math.NT | pengcheng chen | Short representations and counting with distinct odd unit fractions
- 2611.00950 | 2026-11-23 | math-ph | Shankar Sivarajan | Resurgence of the finite-$N$ Curie--Weiss model: metastability, the spinodal, and Lee--Yang zeros
- 2611.00951 | 2026-11-23 | cs.CG | Pedro Machado Manhães de Castro | Finding most likely Delaunay triangulations of imprecise points is NP-hard
- 2611.00952 | 2026-11-23 | math.NT | Scott Kominers | Completing the Kim–Kim–Oh Classification of Minimal-Rank $n$-Universal Lattices for $2\le n\le 8$
- 2611.00953 | 2026-11-23 | math.NT | Scott Kominers | Kim's universal octonary form over real quadratic orders
- 2611.00954 | 2026-11-23 | cs.CC | Anthropic | VP $\neq$ VNP over every field
- 2611.00956 | 2026-11-23 | math.NT | Santiago Pineda | Weighted distribution of residual indices and the contribution of higher-degree primes
- 2611.00958 | 2026-11-24 | math.MG | Alexander Kolpakov | On the second smallest ideal right-angled hyperbolic four-polytope
- 2611.00959 | 2026-11-24 | math.NT | Wren Aquila | Conditional results at $N-p$: higher divisor sums, band-prime cofactors, and a conditional reduction
- 2611.00960 | 2026-11-24 | math.MP | Soo-Jong Rey | Dilaton-Axion Wormhole Partition Function Away from the BPS Endpoint
- 2611.00961 | 2026-11-24 | math.AP | Troy Winarski | A Lean-Verified Alternative Proof of the Pressure-Flux Estimate in Navier–Stokes Lemma 10.5
- 2611.00963 | 2026-11-24 | math.AG | Qiyue Tang | Counterexamples to Walther's ideal equality
- 2611.00964 | 2026-11-24 | cs.CG | Pedro Machado Manhães de Castro | How Many Delaunay Cells Does a Segment Cross for Random Sites on a Manifold?
- 2611.00965 | 2026-11-24 | math.RT | Bob Smith | Generalized cluster structures and simple modules
- 2611.00967 | 2026-11-24 | math.GR | Shengmin Zhang | A Proof of the Galois–McKay Conjecture
- 2611.00968 | 2026-11-24 | math.NT | Teo Banica | Quantum algebra thoughts on the Riemann hypothesis
- 2611.00969 | 2026-11-24 | math.IT | Zhongpai  Gao | Time Reversal and the Memory Cost of Prediction
- 2611.00970 | 2026-11-24 | math.NT | Samuel A. HAMBLETON | The Goodspeed Function: Classification, Left-Tail Geometry, and Arithmetic Nodal Waves
- 2611.00971 | 2026-11-24 | math.NT | Louis P. Slothouber | Natural boundaries of prime-pair Dirichlet series
- 2611.00972 | 2026-11-24 | cs.CC | Yilin Liu | A uniform exponent bound for asymptotic tensor rank
- 2611.00973 | 2026-11-24 | math-ph | Qidong He | Columnar order in a system of $2\times2\times2$ hard cubes on $\mathbb{Z}^3$
- 2611.00975 | 2026-11-24 | math.QA | Bob Smith | On reachability in Hernandez–Leclerc categories
- 2611.00976 | 2026-11-24 | math.GT | Danny Calegari | Leopard spots, CM points, and class numbers
- 2611.00977 | 2026-11-24 | math.CO | Samuel Korsky | A Linear Lower Bound for the Extensible No-Three-in-Line Problem
- 2611.00978 | 2026-11-24 | math.CO | Samuel Korsky | Forcing and Avoiding Monochromatic Pairs $\{x + y,xy\}$
- 2611.00979 | 2026-11-24 | math.CO | Samuel Korsky | Lower Bounds for Self-Avoiding Walks
- 2611.00982 | 2026-11-24 | math.PR | Dario Trevisan | The Mean-Field Limit of High-Dimensional Euclidean Matching
- 2611.00983 | 2026-11-24 | math.PR | Guillaume Barraquand | Convergence of the one-particle quantum symmetric simple exclusion process to the KPZ equation
- 2611.00985 | 2026-11-24 | math.CT | Kotaro Kamiya | Bayesian Updating with Contextful Arrows
- 2611.00986 | 2026-11-24 | math.QA | Sebastien Palcoux | Grothendieck rings of complex fusion categories: rank 5
- 2611.00987 | 2026-11-24 | math.NT | user Alderliefste | Constructing finite fields of prime degree from small cyclotomic cofactors and at fixed valuation, after Bach, von zur Gathen, Lenstra, and Pila
- 2611.00988 | 2026-11-24 | math.NT | David Niedbala Giraudin | A conditional bound H_2 <= 19284 from the sharp minorant of the 182 argument
- 2611.00989 | 2026-11-24 | math.GT | David Niedbala Giraudin | The knot 17nh_0010647 is not smoothly slice
- 2611.00990 | 2026-11-24 | math.RT | Jason Turner | A counterexample to a question of Geiss, Leclerc and Schröer
- 2611.00991 | 2026-11-24 | math.NT | Filip Najman | The rational torsion of $J_1(p)$ is generated by differences of rational cusps
- 2611.00993 | 2026-11-24 | math.RA | user Alderliefste | Spectrum, semimodules and projectives of the inverse semiring $R_0$ of Faul, Goswami, Joubert and Manuell
- 2611.00994 | 2026-11-24 | cs.CC | Yilin Liu | Stretched-exponential circuit lower bounds for the noncommutative permanent and determinant
- 2611.00995 | 2026-11-24 | math.NT | Zeng Chunping | Windows, Oscillation, and the Critical Line for Dirichlet L-Functions
- 2611.00996 | 2026-11-24 | math.NT | user Alderliefste | A finite arithmetic test for simplicity of the Riemann zeros, after Suzuki
- 2611.00997 | 2026-11-24 | math.LO | Peter Zhang | Weak double extension set theory is inconsistent
- 2611.00998 | 2026-11-24 | math.KT | Huimin Zheng | Vanishing of $K_{4m}(\mathbb{Z})$ through degree $120$
- 2611.00999 | 2026-11-24 | math.CO | Shuhei Tsujie | A counterexample to Terao's conjecture for free hyperplane arrangements over  $\mathbb{F}_{121}$
