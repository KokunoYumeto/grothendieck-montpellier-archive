# Shape map, revision 1: Navier–Stokes from the source, and the user's notes as hunches

Claude Fable 5.2, effort medium, no sub-agents. 13 November 2026, 02:54 UTC. The blind map
(`SHAPE_MAP_BLIND_FABLE_20261113.md`) is unchanged; S1–S7 and the carry-over numbers refer to it.

**Status.** Everything here is a reading of statements and of the passages listed; no proof was checked. The readings
of the user's notes are hunches, as the user asked. "Mine" marks a step I derived here and nobody checked.

## What was read for this revision

| Source | Read | Not read |
|---|---|---|
| NS reconstruction (`navier-stokes/sources/openai-source-faithful-20260920/upstream/reconstruction/sections/`) | pp. 1–6 in full (Theorem 1.1, §2); §3 "Correction and summation", Theorem 3.1, "Localization and completion"; Prop. 9.3 (statement), Def. 9.4, Prop. 9.5 with proof, Prop. 9.6 (statement), Prop. 9.9 (opening); Lemma 10.2 with most of its proof; the outline of all sections | §§4–8, appendices A–C, the proofs of 9.6 and 9.9, Lemmas 10.3–10.5. The task asked for the construction and the stage estimates in full; they were read in the outline's form (§3) and at the statements, not through §§4–9 line by line |
| `navier-stokes/README.md`, `RESEARCH_STATE.md`, `errata/D1.md` | in full | |
| `continuations/20260930-coupled-viscous-control/` | `README.md` in full; `source/infinite_status.tex` in full | `coupled_viscous_control.tex` (the entry file), `finite_stage/`, `infinite_modified/` bodies: fetched or listed, not read |
| `continuations/20260919-vacuum-hydrodynamics/README.md` | first quarter | the rest and the manuscripts |
| Perelman, math/0211159 (`src.tex`) | §3 (W, its scaling invariance, dW/dt), the statement of 10.1 and the RG remark after it | the rest |
| Local smoothing paper | Lemma 6.1 with proof, Remark 6.2, opening of Prop. 6.3 | §§2–5 |
| LM7 `sections/E_completed_pairs.tex` | statement tail and the whole proof of E.32 | |
| Andrews–Connes–La Gatta | Hypothesis LA with its two remarks; the lines on the scaling action (intro, §ss:transport heading) | |
| Yang–Mills | nothing new. The Balaban row below is from general knowledge of Balaban's papers, not from OpenAI's proof, which is unreleased | |

## 1. Navier–Stokes, read from the LaTeX

**What the result is (Theorem 1.1, p. 1).** For every ν > 0 there are a force f in C_c^∞(R³ × (0,∞)), a compact K, and
smooth u, p on R³ × [0,1) solving forced Navier–Stokes from u(·,0) = 0, supported in K, with sup_t ‖u(t)‖_{L²} < ∞ and
limsup_{t↑1} ‖u(t)‖_{L^∞} = ∞. The paper states this as alternative (C) of Fefferman's formulation, and (D) on the torus
by Corollary 10.6. The repository's README: the reconstruction's checks "concern transcription fidelity, not an
independent proof of the mathematics"; D1 is a transcription fix to the radicand of (10.20).

**The mechanism (§2, §3).**
- The force is defined as the residual R(u,p) of the equation. The task is to choose a blowing-up flow whose residual,
  with all derivatives, extends smoothly through t = 1.
- Leading flow: a self-similar vortex with ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h}, 0 < h < 1/100, τ = 1 − t; speeds ≍ τ^{−1/2−h};
  core energy ≍ τ^{1/2−3h} → 0. Re_r = O(1), Re_θ ≍ τ^{−h} → ∞.
- The background's residual in the annulus diverges. Oscillatory pulses with zero angular average are added; their
  averaged quadratic momentum flux ⟨w_a w_b⟩_θ cancels the leading stress (Prop. 7.5).
- A fixed four-step correction cycle (Prop. 9.6) then improves the residual. Stage j has residual order
  σ_j = 1/5 + j/10 → ∞. The bound on derivatives of order m carries q^{hσ_j − K_m}, with K_m independent of j;
  constants may depend on j and m.
- The stages are summed with cutoffs whose supports shrink with the stage (Lemma 5.4, Prop. 9.9), so the sum is
  locally finite for q > 0. Result (Theorem 3.1(iii)): |∂_x^α ∂_t^b R(u,p)| ≤ C q^N for every N, and the residual is
  identically zero in the exterior X ≥ X_ext, where the flow is an exact solution of the radial swirl heat equation.
- Lemma 10.2: every derivative of f converges uniformly as t ↑ 1, with all derivatives of the limits vanishing at 0.

**Its row.**
- **Scale parameter:** q ≍ τ + |z|^{1/D}, the similarity distance to the singular point (0,1); and the stage index j.
- **Tractable end:** q bounded below, where every derivative is bounded up to τ = 0 (Theorem 3.1(ii)). The hard end is
  q → 0.
- **The uniform bound:** the loss K_m does not grow with the stage, while the gain grows by 1/10 per cycle. This is
  weaker than a bound with constants uniform in j, and the shrinking cutoffs are what make it enough.
- **S1:** yes. **S2:** yes: after the pulses, the interaction is carried by the angular means and by five radial
  moment equations (8.25), two of which keep two integrals exactly zero (9.10). **S3:** yes: the force is supplied by a
  quadratic covariance of fields whose linear averages vanish. **S4:** yes: the axis, and the middle plane z = 0, where
  the profile is made slightly asymmetric so that the two amplification mechanisms do not fail at the same layer (§2.1).
  **S5:** yes: the forced statement. **S6:** yes: Daneri–Székelyhidi stress realization, Lifschitz–Hameiri wave
  dynamics, Córdoba–Martínez-Zoroa cascades (§1.1). **S7:** no.
- **Partial features:** Lean formalization claimed by OpenAI (not in this repository; the README says the independent
  analytic and Lean validation "remains unfinished"). No certified numerics in the part read. No normalizer
  recognition. Not conditional. A refutation.

**The user's continuation, and where its uniform bound is missing.** `infinite_status.tex` takes the
Alpöge–Buckmaster inviscid Boussinesq cascade (layers q, λ_q = λ_{q−1}^{Q_q}, Q_q = Q_* + q) and computes the cost of
keeping its fields unchanged at positive diffusion: at explicit plateau points,
|κΔθ_E| ≥ c κ λ_q^{9/8} and |εΔu_E| ≥ c ε λ_q^{9/8} λ_{q−1}^{−1/16}, both → ∞, and
|εΔω_E| ≥ c ε λ_q^{17/8} λ_{q−1}^{−1/16} for every pressure. So the unchanged-state extension has no continuous terminal
force. The README lists as unfinished: the modified infinite return, the all-stage signed force budget, the terminal
smooth extension. Proved there (README's statement, bodies not read): the finite third return at positive diffusion,
the exact fixed-diffusion scaling, the based-state interface, the complete annulus force, the force needed to reach a
based state.

The two halves of the repository therefore show S1 from both sides: OpenAI's manuscript has the stage-independent
loss; the continuation has an explicit per-stage cost that grows with the stage.

**Corrections to the blind map.** Its NS paragraph came from news. Two points change: the claim's mechanism is a
residual-correction cascade around a self-similar vortex, not an unstable-profile or computer-assisted argument; and
the Hou–Wang–Yang remark stays a summary.

## 2. The user's notes

### a. S1 as RG flow, and the Perelman-type device

Perelman's device (§3): W(g,f,τ) has "explicit insertions of the scale parameter", is "invariant under simultaneous
scaling of τ and g", and dW/dt is an integral of a square. Pseudolocality (10.1), in his words: a region that "looks
trivial (almost euclidean) on higher energy scale" cannot "suddenly become highly nontrivial on a slightly lower
energy scale".

| Item | Scale, its ends, the flow | The device that carries (or would carry) the uniform bound | Pseudolocality analogue |
|---|---|---|---|
| ETH | T ∈ {0, 1..Q}. T = 0 coupled; T ≥ 1 decoupled once the ≤ δn block measurements y_g = C_g x_g are fixed. One block-spin step, not a flow | deg H ≤ 3nR. In RG terms this is finiteness, not monotonicity: H has O(nR) coefficients, so finitely many evaluations at the decoupled end determine H(0). No monotone quantity in the part read | Holds by Definition 2.1(4): a clause sees other groups only through the measurements |
| Local smoothing | s = \|σ\|, the radius of the imaginary displacement, from b = 2Kh to 1; RG time x = log(s/b) | Lemma 6.1. The circular mean H(T,s) of a nonnegative supersolution of (−Δ_{T,σ} + V) is compared with radial harmonic functions, which are affine in log s; V enters only through ∫ s log(s/b) V ds ≤ M. For V = 0 this is concavity of the mean in log s: the superharmonic counterpart of the three-circles theorem, not a monotone quantity and not log-convexity. Remark 6.2: each passage loses one logarithm and this is sharp for scalar supersolutions | Holds in the form V(s) = C s^{−2} e^{−cs/h}: the potential is exponentially small above the wavelength scale |
| Yang–Mills | lattice spacing under block averaging; ultraviolet end asymptotically free; OpenAI's part is the infrared end (committee statement) | Balaban (general knowledge): stability bounds on the partition function uniform in the lattice spacing, proved by induction over scales with the running coupling as the inserted scale parameter. An induction with a marginal coupling, not a monotone functional | Not known from any source read |
| Navier–Stokes (OpenAI) | q → 0; parabolic scaling ℓ_r² ≍ τ, the same joint scaling as Perelman's (g,τ), broken slowly by h | stage-independent loss K_m against gain j/10; flatness q^N | Holds by construction: exact heat exterior, zero residual for X ≥ X_ext, bounded derivatives where q is bounded below |
| Navier–Stokes (continuation) | layer q, λ_q ↑ ∞ | missing. Statement a W-type functional would make: a weighted energy of (state, force) at layer q, with ℓ_q inserted, invariant under the fixed-diffusion similarity of `parabolic_similarity_body.tex`, non-increasing from layer q to q+1, and bounding the force and its derivatives. The candidate to test is the weighted energy identity of `force_reachability_body.tex` (not read) | Fails for unchanged fields at rate λ_q^{9/8} (`infinite_status.tex`); holds in the inviscid source (older layers affine on the new support) |
| Connes | window λ; the scaling action θ carries cutoffs at scale σ to scale λσ | missing: see below | Seen numerically (zeros found at λ² = 13 persist at 250, error ∝ ε_λ); not proved |
| S^6 | w, 0 < \|w\| < 216; q(Alb S₂) = iw/216 | L(t) = log N(P_t), a logarithmic potential with dd^c L = (1/12)δ_∞ − m_P (routes I4, unproved); its maximum gives the radius 216 | Not examined |
| LM7 | level n and coefficient level 3^n | the Mittag-Leffler condition: see below | Fails in E.32: every local and every finite-coefficient obstruction vanishes, the global one does not |
| TOTEX2 | stage of the AKR completion | missing (C.9) | Lead 7 is the analogue ("attachments cannot kill homology above the diagram dimension"); C.4 proves its hypothesis fails for allowed later attachments |
| CYCLOTOMIC E3 | nilpotent class r | missing; the return states the inverse-limit condition and the first obstruction in H¹(Δ, γ₃/γ₄) | Not examined |

So "S1 is RG flow" is literal for Yang–Mills, and for NS up to the anomalous exponent h. For local smoothing it is a
flow in log-radius with a concavity estimate. For ETH it is one block-spin step with an algebraic bound. None of the
completed items has a monotone functional in Perelman's sense in the parts read; each has an induction or a comparison
that loses a controlled amount per scale.

**LM7: the test of the Mittag-Leffler reading. It passes.**
- E.32 states: for the pair (E.32f), "every local obstruction and every finite-coefficient global obstruction
  vanishes", and there is no continuous section.
- Jannsen's sequence is 0 → lim¹_n H¹(G_Q, Z/3^n(2)) → H²_cts(G_Q, Z_3(2)) → lim_n H²(G_Q, Z/3^n(2)) → 0. A class whose
  finite-coefficient images all vanish lies in the lim¹ term. So the obstruction of E.32 is a lim¹ class. (Mine: the
  return cites Jannsen (2.2) and (1.6) for the comparison and keeps "phantom classes"; it does not name the term.)
- Where it comes from (mine, from the proof's complexes): the unramified part has finite H¹, so its lim¹ vanishes
  (E.32i). The residue part is the system ⊕_q [Z/3^n → Z/3^n], differential q − 1. Its H⁰ system is not
  Mittag-Leffler, because v_3(q − 1) is unbounded over the primes: the image of level n+k in level n keeps shrinking.
  The kernel (E.32e) is this lim¹.
- In the return's own terms the uniform bound is: c_q = −9(A_q b_q − B_q a_q)/(q − 1) is integral and tends to 0.
  The witness has c_{q_j} = −1 for all j.
- This is different from D.26, where the failure is cofinality of the system, not lim¹.

**Connes: a W-type functional in λ.** Hunch-level, mine.
- μ(λ) := ε_λ(1) = inf QW(f,f)/‖f‖² over f supported in [λ^{−1}, λ] is the analogue of Perelman's μ(g,τ). It is
  non-increasing in λ, because the windows are nested. That monotonicity is free and points the wrong way.
- The scale-normalized quantity is 𝒲(λ) := log ε_λ(1) − log δ_4(λ), with δ_4 the Fuchs rung. The lower half of
  Hypothesis LA for j = 1 is: 𝒲 is bounded below.
- Perelman-type statement: 𝒲(λ) is non-decreasing for λ ≥ λ_0. One computed value then gives the lower half for all
  larger λ. The same with ε_λ(j)/δ_{4j} for each j gives LA.
- First check: the paper's Table `tab:logbound` (ratio ε_λ(1)/(δ_4 log λ) between 4.9 and 8.8 "without upward trend").
  If the ratio to δ_4 alone is monotone on 5 ≤ λ² ≤ 300 the statement survives; if not, the candidate is
  ε_λ(1)/(δ_4 log λ) non-increasing, which gives the upper half with exponent 1 and not the lower half.
- The paper's remark stands against any easy version: a lower bound ε_λ ≥ cδ_4 implies QW_λ ≥ 0, hence RH.

### b. S2: almost-commutative geometry and the modular flow

- The shape matches in Connes's own paper: QW_λ = (finite-dimensional near-radical part, dimension ≈ 2λ²) ⊕ (strictly
  positive part). In M × F the finite part F carries the interaction over a commutative bulk. The difference: here the
  finite part's dimension grows with the scale.
- The scaling flow is present in the paper as θ: "the scaling action θ(f) transports the cutoff projections at scale σ
  into those at scale λσ". The proof of `thm:condpos` is a two-scale argument (σ and λσ) with margin log σ.
- The Bost–Connes identification σ_t(μ_n) = n^{it}μ_n and the modular reading were not found in the parts of the paper
  read; they rest on the card's sources.
- In the other items the interface is: ETH's measurement matrices C_g; NS's five moment equations; LM7's toric
  minimum (E.16). Only Connes's and NS's interfaces come with a scaling action on them.

### c. Holography, P¹, and class-two monodromy item by item

No holography source was read. In the repository, the vacuum-hydrodynamics continuation is the user's own
gravity-side reading of NS (README: exact Einstein constraint data from a velocity field, with Λ = −6/L²; a Rindler
shear response); only its opening was read.

Where the class-two object is in each item:

| Item | Class-two object | Basis |
|---|---|---|
| LM7 | E.20, E.26, E.28, E.31, E.32: Heisenberg quotients; obstruction 9α∪β with central corrections | read (CSV; E.32 proof) |
| FLAGGED | F17.2–F17.4: class-two monodromy detects bad reduction that homology misses | CSV rows |
| CYCLOTOMIC | E1–E3: the class-two quotient N₂ of a CM punctured elliptic curve; Δ fixes all of N₂; "the class-two shear" | CSV rows |
| S^6 | The monodromy group Γ lies in the stabilizer of a vector δ̂ in Sp₄(Z) (F10). That stabilizer is a Jacobi group SL₂ ⋉ Heisenberg (standard fact, mine). The period β is the central coordinate, and ξ = e^{−2πiβ} is the fibre coordinate of Γ\O₊ (routes 1.4). So the modulus w of the family sits in the centre of a class-two group | F10 read; the identification is mine |
| Local smoothing | In null coordinates the wave operator is 2∂_t∂_{s₀} + Δ_x, "the free Schrödinger operator" at fixed frequency in s₀ (§2.1). Its symmetry group is a Heisenberg group with s₀ central (mine). This is a class-two group, not a monodromy | §2.1 opening read |
| Connes | The pair (P_λ, P̂_λ) is the time–frequency pair; the uncertainty operator measures the Heisenberg relation. No monodromy found in the parts read. Bost–Connes itself is abelian (card) | intro read |
| NS | The quadratic covariance of zero-mean pulses (S3). Checked the parts read: no monodromy | read |
| ETH | Checked §2.1–2.4: none found | read |
| EXIT, TOTEX2 | Checked the CSV rows: the obstructions are abelian (meridian lattices; T₁ = Z/ε(L)); none found | CSV rows |
| Yang–Mills | no source | |

So the note tracks for LM7, FLAGGED, CYCLOTOMIC and S^6 as monodromy, for local smoothing and Connes as a Heisenberg
group without monodromy, and not for ETH, EXIT, TOTEX2.

### d. The tame relation as the scaling action, and carry-over 3

In the proof of E.32 the reading is exact:
- (E.32m): φ_q τ_q φ_q^{−1} = τ_q^q.
- The local residue complex is [Z/3^n → Z/3^n] with differential q − 1 (E.32j): Frobenius acting on inertia by q,
  minus the identity.
- H²_cts = R/dR with d(z)_q = (q − 1) z_q on families tending to zero (E.32d, k): the coinvariants of the scaling
  action on a restricted product over the primes.
- The obstruction is solvable exactly when division by q − 1 keeps the family tending to zero. That is a small-divisor
  condition; the divisors are 3-adically small where v_3(q − 1) is large.

Hunch (mine): this is the same shape as the cokernel on which Connes's scaling action realizes the zeros, a restricted
product over primes modulo the image of a scaling-type map. Nothing was checked beyond the shape.

**Carry-over 3, revised.** The tame-relation test of E.28 and E.31 is one step of the scaling at one prime: it checks
whether (E.32n), q{(q − 1)w + 9(A′_q b_q − B′_q a_q)}, can vanish. FLAGGED F17 and CYCLOTOMIC D15 need the same test in
the same Heisenberg quotient. The revision adds: any such test done prime by prime must be followed by the lim¹ check,
since E.32 shows the prime-by-prime answer can be yes while the global answer is no.

### e. One refinement step for S7

The candidates, from the CSV rows (FLAGGED rows cut at 300 characters):
- FLAGGED ZD11: the universal birational lifting claim is equivalent to the section conjecture for the curve.
  ZD10, ZCF6: the instance P¹ minus three points over Q is open.
- CYCLOTOMIC C7, C9: the admissible germs are exactly the noncuspidal ones; U₀₃(Q̄) injects equivariantly; equality is
  section surjectivity over all number fields. Cuspidal ⇔ nonzero cyclotomic centralizer (C4, C10).
- LM7 E.23 with E.29, E.31, E.32, E.34, E.36: sections of the Fermat cubic tower classified layer by layer, with exact
  fibres, an explicit local formula, and the inverse-limit term.

**Most refined: LM7.** The others state an equivalence or a criterion; LM7 states how far each section lifts and
what stops it.

Lifted to the others:
- **To ZD11.** The equivalence becomes graded: for each quotient (abelian, inherited class two, cuspidally central,
  intrinsic class two), "every section of that quotient lifts birationally" against "every section of that quotient
  comes from a point or cusp". E.29 shows the graded statement is false at inherited class two: over every rational
  toric pair whose tame residues have 3-order at most 9 there are exactly three section classes, far more than the
  rational points (rank zero, E.24). So the defect is infinite at class two and must die in the remaining layers: the
  rank-44 central kernel of E.36, where E.31 already gives classes that fail. Statement to test: no section class of
  E.32 outside the point and cusp classes survives the rank-44 lift.
- **To ZD10.** Its "smallest obstruction" should carry the lim¹ term: E.32 gives a pair with all finite-level
  obstructions zero and no section.
- **To C7 and C9.** The centralizer criterion can be run layer by layer. CYCLOTOMIC E1 has already done class two for
  the CM punctured elliptic curve: Δ fixes all of N₂, so the criterion does not separate anything there; E3 finds
  nonperipheral fixed elements for r ≥ 3. Together with E.29 this says that at class two neither lifting nor
  centralizers distinguishes points. Statement to test: the first obstruction of E3, in H¹(Δ, γ₃/γ₄), and the first
  layer after E.36 are the first place where both tests bite.
- **Back to LM7 from C9.** E.23 should be posed for germs (open subgroups of G_Q) with the Galois action on them, as
  C9 does; E.32 is stated for whole-G_Q sections only.

### f. Recorded for later

Lifting the Andrews–Connes–La Gatta uncertainty principle (U_λ = 2 − P_λ − P̂_λ, its two sectors, the Fuchs ladder) to
each item at its own scale. Not done. The entry point this revision found: the Heisenberg group is visible in local
smoothing (§2.1) and in the S^6 monodromy, which is where a time–frequency pair would be looked for first.

## Carry-overs changed by this revision

- **3:** revised in d: add the lim¹ check after any prime-by-prime tame test.
- **4:** sharper. "All finite stages lift" can fail to give a section for exactly one reason in E.32, the lim¹ term;
  in E.34 and CYCLOTOMIC D5 the groups in play are finite or H² vanishes, so Mittag-Leffler holds. D.13 and D.19 should
  be examined for which of the two failures they are: lim¹, or cofinality as in D.26.
- **5 and 6:** unchanged, with one fact added: Lemma 6.1 of local smoothing is a comparison in log-radius that provably
  cannot do better than one logarithm per passage (Remark 6.2). For Connes that budget is too large on the lower side:
  LA "is a statement about constants".
- **New, 8. NS → TOTEX2 C.9 and the continuation.** OpenAI's manuscript sums infinitely many stages without uniform
  constants, by a gain per cycle that is fixed and a loss that does not depend on the stage, with cutoffs shrinking
  per stage. C.9 (persistence through the union of AKR stages) and the all-stage force budget lack exactly a
  stage-independent loss. For the budget, `infinite_status.tex` gives the number to beat: λ_q^{9/8} per layer.
- **New, 9. LM7 → the continuation.** A per-stage cost that is finite at every stage and whose sum has no limit is the
  shape of E.32. The force budget should be posed as a limit statement from the start (terminal extension with all
  derivatives), not stage by stage.

# Revision 1a: the vacuum-gravity lessons

Claude Fable 5.2, effort medium, no sub-agents. 13 November 2026, 03:16 UTC (machine clock).

**Status.** A reading of the two lessons' statements; no proof was checked. "Mine" marks a step derived here and
checked by nobody. Two symbols collide: OpenAI's similarity parameter is written q_NS below, the lesson's
dimensionless wavenumber q_B = kρ_c.

**What was read** (repository KokunoYumeto/open-math-courses, `courses/GR-VAC/`):
- `README.md`: in full.
- Appendix A, `src/velocity-fields-and-vacuum-constraints.md`: §§1–2 and §7 in full, Exercise 2, all headings.
  Not read: §§3–6 (the tensor, the scalar equation, the data, the decoder), Exercises 1, 3–5.
- Appendix B, `src/gravitational-shear-and-the-fluid-limit.md`: §§1, 2 (opening), 3.2 (opening), 6 to the start of
  6.2, 7 (statement, 7.2), 8, 10, Exercise 5, all headings. Not read: §§3.1, 4, 5, 6.2 past its first paragraph, 7.1,
  Exercises 1–4.
- The cited papers (Bredberg–Keeler–Lysov–Strominger, Compère–McFadden–Skenderis–Taylor, Marolf–Rangamani,
  Choquet-Bruhat–Isenberg–Pollack) were not opened. What is said about them rests on the lessons' citations.

## 1. S1 for Navier–Stokes: is q_NS a radial position?

**What the lessons give.**
- The cutoff position fixes the viscosity. Appendix B: ρ_c = 2ν/c (S1). Appendix A: ν = cL r_c √f_c /(4r_h) with
  f_c = 1 − r_h⁴/r_c⁴ (C4), and every ν > 0 has exactly one r_c > r_h.
- The fluid limit is the parabolic scaling in frequency space. With q_B = kρ_c and w = ωρ_c/c (S11), §6.1 sets
  w = q_B² ζ with ζ bounded, and gets V_BY/a_src = iω/(−iω + νk²) + O(q_B²) (S30), the multiplier of
  ∂_t U − ν∂_z² U = f (S31). Here ζ = ω/(2νk²) (mine, from S11 and S1).
- The radial coordinate enters logarithmically: x = ρ_c log(ρ/ρ_c) (S37), and the mode equation is a wave equation on
  the half-line with potential W_k(x) = k² e^{2x/ρ_c} = (kρ)² (S38).
- Exercise 5's map (S55): r = (r_0/ℓ)R, X_i = (√r_0/ℓ)x_i, τ = x⁰/ℓ, with ds²_phys = (ℓ²/r_0) ds²_source.

**What follows (mine).**
- In W_k = (kρ)², changing k to λk is the same as shifting x by ρ_c log λ. So the scale of the fluid mode and the
  radial position are tied: scaling is translation in the logarithmic radial coordinate. The tie is broken only by
  the wall at x = 0, the cutoff.
- In (S55) the cutoff parameter r_0 carries the parabolic weights: r ∝ r_0, X ∝ √r_0, with the metric rescaled by
  r_0. Up to the Rindler boost this is X ↦ √λ X, τ ↦ λτ. It has the form of Perelman's joint scaling (metric and
  scale parameter rescaled together).
- OpenAI's q_NS ≍ τ ≍ ℓ_r² has the same weight as r_0. So q_NS can be read as a radial position in the coordinate
  sense of (S55): approaching the singular time is moving the cutoff parameter r_0 toward 0.

**Limits of the identification.**
- In physical units the cutoff does not move: (S57) keeps ν = cℓ for every r_0, and ρ_c = 2ν/c is fixed by ν. At
  fixed ν and c the blowup has k ~ 1/ℓ_r → ∞, so q_B = kρ_c → ∞ along fixed ζ (mine). The fluid limit of §6.1 is
  q_B → 0 with error O(q_B²). The blowup therefore runs out of the regime where Appendix B's response is
  Navier–Stokes, into the regime of the full response (S21). The first correction, −(3ν³/2c²)Δ²U in (S57), has
  relative size of order q_B².
- Appendix B is linear, one shear polarization, on flat Rindler space (Λ = 0). OpenAI's flow is an axisymmetric
  swirling vortex with two length scales (the exponent h) and a nonlinear mechanism. The lesson: "it is not a
  consequence of the nonlinear blowup theorem and does not describe a gravitational continuation of that singular
  solution."
- Appendix A is a map of snapshots, on a different background (Λ = −6/L²). Its dilation gives the exact fluid
  scaling law ν_V = d²ν with time unchanged (C44), a kinematic statement.
- So: the lessons support "the radial coordinate is the logarithm of the fluid scale, and the cutoff sets ν". They
  do not support "the similarity flow of the blowup is a radial flow in a solution of Einstein's equations". The
  README says the same: the conclusions "do not assert an Einstein regularization of the nonlinear Navier–Stokes
  blowup".

## 2. The two residuals

| | OpenAI's residual | Appendix A's residual (C46) |
|---|---|---|
| What it is | f = R(u,p), the momentum equation evaluated on a chosen flow | TF_h(∂_t h − 2cNK) = −2cN(K − (τ_*/4)h), the trace-free part of the metric evolution equation evaluated on the family of encoded snapshots |
| Type | a vector field on space-time | a trace-free symmetric tensor on the four-dimensional slice |
| Size | made flat: every derivative ≤ C q_NS^N | not small: "nonzero even outside the compact perturbation, where it contains φ^{−2}Ā_0" |
| What it measures | how far the chosen flow is from an unforced solution | that fluid time, inserted as Einstein time with zero shift, is the wrong identification of time and gauge |

- **Fluid residual into gravity: yes, linearly.** (C45) gives the time derivative of the data through
  q̇ = 2β_*²⟨ℒ_b V, ℒ_b V̇⟩, and V̇ is the right side of (C44), which contains f_V = d f(t, ξ/d). So OpenAI's force is
  carried into the time derivative of the constraint data.
- **Gravity residual into the fluid: no.** (C46) does not vanish for U = 0 and has no vector part to set against f.
  The lesson says it "specifies the exact defect of the displayed" map and does not exclude another map "involving
  additional dynamical variables".
- **What Appendix A does carry across the blowup:** (C47), ‖φ_t‖⁴_∞ ‖TF_E K_t^♯|_{w=0}‖_∞ ≥ β_* ‖S_{U(t)}‖_∞. With
  OpenAI's scales the strain grows at least like τ^{−1−h} (mine, from speeds τ^{−1/2−h} over ℓ_r ≍ τ^{1/2}), so this
  product of the data is unbounded as t ↑ 1. The lesson adds that this alone "gives no curvature-singularity
  theorem".
- The two residuals share the method (evaluate an equation on a chosen family and read the defect) and nothing else.

## 3. A monotone

**The candidate.** Theorem 2 of Appendix B: the energy
E_k(t) = ½∫_{−∞}^0 (c^{−2}|φ_t|² + |φ_x|² + k² e^{2x/ρ_c}|φ|²) dx is conserved on the half-line (S41, S44). On a
truncated region with the outgoing condition at x_0 it is non-increasing: dE_k/dt = −c|φ_x(x_0)|² ≤ 0 (§7.2).
There is a local law ∂_t e + ∂_x j = 0 with |j| ≤ ce (S46).

**Measured against Perelman's W.**
- Scale inserted explicitly: yes, k and ρ_c in the potential.
- Invariant under the joint scaling: yes away from the wall. E_k of φ equals E_{λk} of the profile shifted by
  ρ_c log λ in x (mine). The Neumann wall at x = 0 breaks it.
- Monotone: conserved, or decreasing by the flux through the horizon side.
- Gives a uniform bound: only in L². It bounds ‖φ_t‖₂ and ‖φ_x‖₂; ‖φ‖₂ may grow linearly in t (S45).

**The statement it would make** (mine; for the linear shear sector only). Drive the wall by a source that is a sum
of layers, a_src = Σ_q a_q, with layer q at wavenumber k_q. With the drive, the energy identity gains the work done
at the wall. Then:
- the work done by the force on all layers up to time t equals the energy stored plus the energy radiated toward
  the horizon, both non-negative;
- because the equation is linear and invariant in t and z, the same holds for every ∂_t^j ∂_z^m of the solution,
  with weights ω^{2j} k^{2m};
- so in this sector the all-stage force budget is finite, with all derivatives, exactly when the sums
  Σ_q k_q^{2m} ω_q^{2j} (work on layer q) are finite for all j and m.

That is the shape carry-over 9 asked for: a limit statement posed at once, with a non-negative quantity that the
scale shifts and time does not increase.

**What stops it.**
- Theorem 2 is for "the stated shear sector and zero boundary drive". The driven identity is not in the lesson.
- (S48): R_yy = ¼F_{ab}F^{ab} is quadratic, so a finite shear field does not solve the vacuum equation in the ansatz.
  The lesson: the theorem "supplies no nonlinear regularization theorem for the original forced Navier–Stokes
  solution".
- The continuation's cascade is nonlinear: an older layer's strain amplifies the newer one. A linear sector has no
  such transfer, so it cannot model the growth whose cost is λ_q^{9/8} per layer.
- The cascade lives at k → ∞, where by section 1 the shear response is no longer Navier–Stokes.
- The budget needs sup norms of all derivatives; the energy gives weighted L² norms.

So E_k is a Perelman-type device for the linear model and not, as it stands, for the force budget. The first check
is small: write the driven energy identity for (S38) with the wall source of (S21) and see whether the work term has
a sign.

**One structural link to revision 1.** (S38) is a one-dimensional equation in a logarithmic radial coordinate with
potential (kρ)². Lemma 6.1 of the local smoothing paper is also an equation in x = log(s/b) with potential
s²(V + ν²). In both, the scale is a translation in log-radius and the potential is what breaks the translation.
Local smoothing has only a concavity estimate there; the shear model has a conserved energy.

**Other monotone objects in the lessons.** Appendix A §4.2 is titled "Monotone construction" (heading only read; it
is the construction of the solution of the scalar constraint equation, monotone in an iteration, not in scale). (C47)
is an inequality, not a monotone quantity.

## 4. The user's notes on the card, against the lessons' content

- **The radial dimension is the RG scale: supported, in the lessons' own formulas.** The cutoff position sets ν
  (S1, C4); scaling is translation in x (section 1). The lessons do not use the words; a search of both for
  "renormali", "Wilson", "holograph" (outside one paper title), "Weyl", "anomal" finds nothing.
- **"The same scaling thingy": supported.** (S55) rescales r_0, X and the metric together.
- **The Weyl anomaly and anomaly inflow: not supported by these two lessons.** Neither appears. The workbench's
  `SLAB_COMPARATORS.md` is described in its README as covering an "anomaly-inflow scope"; it was not read.
- **P¹ and H³: not supported here.** Appendix B's background is flat five-dimensional Rindler space; Appendix A's has
  Λ = −6/L² with four spatial coordinates. Neither is H³ with boundary P¹(C).
- **Class two (S3):** (S48) is the lessons' instance. The first nonlinear term is quadratic in the field strength of
  the linear shear field and is invisible to the linear equation.

## Effect on the map

- **NS row, S1:** add the radial reading with its limit: q_NS has the weight of the cutoff parameter r_0 of (S55);
  at fixed ν and c the blowup leaves the fluid regime of the shear model (q_B → ∞).
- **Carry-over 8 (the missing device for the all-stage force budget):** one candidate now exists for a linear model,
  E_k with its scale covariance; the stoppers are listed in section 3.
- **The bridge.** It holds in this sense: the lessons give Navier–Stokes a radial coordinate in which its scaling is a
  translation, and a model with a conserved positive quantity in that coordinate. It does not yet reach the nonlinear
  cascade or the blowup regime.

# Revision 1b: the user's later hunches, checked

Claude Fable 5.2, effort medium, no sub-agents. 13 November 2026, 03:32 UTC (machine clock).

**Marks.** Known (source and place) / new and proved here / new and open (precise statement) / wrong. "Proved here"
is used only for short arguments written out below; nobody checked them. "Mine" marks my own step.

**What was read.**
- *La Longue Marche*, English reader (`reader/LaLongueMarche_English.tex`, 3 MB): searched by keyword; read §19
  (opening), §9 (opening), the passages at scans 24, 172–175 (cote 140-4) and 378 (cote 140-2).
  `notes/RESEARCH_TOPICS.md` in full (a map, used to locate).
- Archive returns: keyword search of the `*_unzipped` folders; read cote 147 scan 104, and the notes lines the search
  returned.
- Connes–Consani 2501.06560: lines 404–418, Prop. `ramiprop`, Cor. `ramicor` with proof, Remark `archimedeanplace`.
- Zeta workbench satellite 13: Theorem `thm:cueM-U3-trace-descent` (statement), the polynomials Ψ₁–Ψ₄, Prop.
  `prop:cueM-Psi2-not-SOS` with proof.
- v35: the boundary-defect definition and theorem (lines 7536–7572), the problem and "Principal conclusion"
  (8070–8090), the warning at 7516, the status table (8024–8050).
- **Abstract only** (arXiv listing, through a summarizing tool): Lehner–Pretorius 1006.5960, Caputa–Magán 1807.04422,
  Connes–Marcolli hep-th/0411114, McNamara–Vafa 1909.10355, CLPW 2206.10780.
- **Not opened; statements below are from general knowledge:** Nag–Verjovsky, Lochak–Schneps, Bakalov–Kirillov,
  Teschner, Brown 1102.1312 and 1512.06410, BHMR, Emparan–Suzuki–Tanabe, Adams–Chesler–Liu, Witten 2112.12828,
  Takesaki, Else–Nayak, Kaplan, Connes–Consani 2401.08401, Milne's *Arithmetic Duality Theorems*, Grover–Mezzadri–Simm
  2604.03051 itself.

## G. Grothendieck's own statements

| Topic | Passage and location | What it settles |
|---|---|---|
| Finer and finer approximations; the minimum level (S1, S7) | Cote 140-4, scans 172–175, ms pp. 734–735, around (371)–(374). If one proved "the nonexistence of splittings of (371) other than those 'coming from the points at infinity', the theorem of Fermat would be proved for U_n, even without having established the 'anabelian yoga'". This might come from "finer and finer 'approximations' of Π₁(U_n) and of the extension structure (371)". "Each new refinement of the 'Lie approximations' of M₀,₃ should lead to a reexamination". "It is imperative to start from Lie approximations at least as fine as" that of the section, "the 'minima' approximation in which one can express 'algebraically' the tower of Fermat curves" | S7 and the layer-by-layer method of LM7 E.23–E.36 are his programme, stated by him. He names the tractable end (the minimum approximation) and the direction of refinement. He gives no condition for passing to the limit |
| Cuspidal against other sections | Same passage: the sections sought are those "distinct from the 'splittings at infinity'", "or again" those for which the centralizer of Γ_Q⁺ = Ker χ is trivial | CYCLOTOMIC C4, C10 and A6 (cuspidal ⇔ nonzero cyclotomic centralizer) is his criterion; the returns prove it |
| Sections at the punctures | Cote 140-2, scan 72, ms p. 34, §9 "Tangential structure at the s ∈ S", margin "[The sections of extensions 'of the second type']" | Tangential sections are in the manuscript in 1981, as sections of Π_{D_i^*} → Π_{D_i} |
| The real place | Cote 140-2, scan 378 (margin pp. 376–377): in Γ_Q "the only elements of order 2 are the conjugates of τ", with centralizer {1, τ}; and "the datum of a discretification (not oriented) α^♮ over the arithmetization a, amounts to the datum of an Archimedean valuation on the algebraic closure" of Q, modulo complex conjugation | He identifies the choice of a discrete structure with the choice of the archimedean place. This is his form of "smooth to discrete lives at ∞" (H2, H6) |
| Finite levels to the limit | Cote 140-4, scan 24 (ms p. 659): "the projective limit of the 𝒢_i in the category of schemes exists … it is perhaps not absurd to pass to the limit outright, and to work with this group scheme — not of finite type" | He passes to the limit for affine group schemes, where the limit exists. Nothing found on lim¹ or Mittag-Leffler: the search for "Mittag" in the reader returns nothing |
| The Teichmüller tower | Cote 140-2, scan from ms p. 102, §19 "Teichmüller tower": the surfaces U_{g,ν} and their automorphism groups | The tower is there. **Generation by levels ≤ 2, the pentagon, the hexagon and the Lego game are not in La Longue Marche:** the reader has no occurrence of "pentagon", "hexagon" or "Lego" |
| Generators and relations for all Π₁M_{g,I} | Cote 147, scan 104 (ms p. 51): "Programme: Déterminer … tous les groupoïdes Π₁M_{g,I}, avec leur dépendance fonctorielle" through the normalization morphisms, margin "par 'gén. et relations' — définis en termes purement algébriques" | The Lego programme in its 1980s archive form: all the groupoids, with the boundary (MD-graph) morphisms. No statement that two levels suffice was found in the pages searched |

The two-level principle and the pentagon and hexagon are in *Esquisse d'un Programme* (1984), which is not in the
corpus named for this task. So for the tower the corpus settles the programme, not the generation statement.

## H2. The archimedean place

**The three passages, as read.**
- Cor. `ramicor`: the smallest set outside which π_χ is unramified is C(χ) ∪ {∞}. The proof shows that a finite S
  without ∞ leaves a point whose fibre is a single element.
- Remark `archimedeanplace`: the fibre over C_∞ is G/χ(−1); "This element of the Galois group is the complex
  conjugation", and the quotient is the set of archimedean places with its Galois action.
- Line 412: H³(Spec Z, G_m) is one copy of Q/Z; "Due to the presence of the real archimedean place with Brauer group
  Z/2Z, there is a subtlety when dealing with higher cohomology groups."

**The test.**
- **E.25: the same object. Known mathematics, identification proved here.** κ₂(−1) is the quadratic character of
  Q(i)/Q. As a character of Ẑ* it has conductor 4 and value −1 at −1, so it is one of Connes–Consani's covers π_χ with
  G = Z/2 and χ(−1) the generator: its fibre over C_∞ is one point. The cup κ₂(−1) ∪ κ₂(−1) is the class of the
  quaternion algebra (−1,−1), whose invariant at ∞ is the non-zero element of Br(R) = Z/2. So the map is restriction
  to the decomposition group at ∞, the group generated by χ(−1), and the target is the Z/2 of line 412. E.25's own
  note says the same in group terms: both lifts of real conjugation square to the non-trivial central element.
- **E.18: the same group, different coefficients. New and open.** E.18's class lies in H²(C₂, H₁(U₄(C), Z₂)), and C₂ is
  again the decomposition group at ∞. But the coefficient module is the homology of a curve, and Connes–Consani's
  covers are abelian covers of X_Q with no curve in them. Statement to test: there is a version of π_χ with
  coefficients in a Galois module M such that the fibre over C_∞ computes Ĥ^*(C₂, M); for M = H₁(U₄, Z₂) its degree-two
  part contains E.18's class.
- Both are archimedean, and unlike E.32 neither needs a limit: they are visible at a finite level.

## H8. "Real line, complex plane, transcendental space"

**(a) Periods. Known.** 2πi, log p and the ζ(n) are periods in the sense of Kontsevich–Zagier, and each is exact as a
pairing between de Rham and Betti classes: 2πi for H¹(G_m); log p for the Kummer 1-motive [Z → G_m], 1 ↦ p, with
period matrix ((1, log p), (0, 2πi)); ζ(n) for the motivic π₁ of P¹ minus three points. Grothendieck's period
conjecture says the transcendence degree of the periods of a motive equals the dimension of its motivic Galois
group; it is open. In our items: LM7 C.7 is "the actual toric Kummer 1-motive" and D.1 the Kummer homomorphism; S^6
has M = −(3/π) log 6, a ratio of two periods of a 1-motive (routes 2.1, unverified).
- The precise form of the hunch that holds: a period is exact as a point of the torsor of isomorphisms between two
  cohomology theories. "One dimension up" is literal for 2πi and log p, where the torsor is under G_m or its extension
  by G_a. For ζ-values the torsor has the dimension of the motivic Galois group, not one more. **Wrong** as "always
  one dimension"; **known** as "exact in the period torsor".

**(b) Arithmetic topology.**
- Artin–Verdier duality has dimension 3 and H³(Spec Z, G_m) = Q/Z: **known**, and stated at line 412 of 2501.06560.
  Primes as knots and the orbits C_p: the local paper has the periodic orbits C_p and the mapping torus of Frob_p
  (Prop. `mappingtorus1`, cited in the proof read); the length log p is from 2401.08401, not opened.
- **v35's boundary defect with Z = {∞}. New and open, with one obstacle named.** v35 does not mention Artin–Verdier
  (no occurrence in the file). The statement to test: on the Artin–Verdier site of Spec Z ∪ {∞}, with j the inclusion
  of Spec Z and i the point ∞, v35's B_j(F) = i^*Rj_*F is the Galois cohomology complex of R with coefficients in the
  generic stalk, and its theorem D_Z B_j(F) ≃ B_j(D_U F)[−1] is local Tate duality at R, a duality of dimension 2 with
  values in Br(R) = Z/2. The shift by one is the difference between the 3-dimensional Spec Z and its 2-dimensional
  boundary. The obstacle: v35's theorem is for D^b_c with six operations; at the real place the cohomology of C₂ is
  unbounded (Z/2 in infinitely many degrees), so B_j is not bounded unless Tate-modified cohomology is used. That is
  the "subtlety" of line 412. Standard background, not opened: Milne ADT II.2–3.

**(c) The logarithm's Riemann surface. Known.** The universal cover of C* is the torsor on which log is exact; its
deck group is Z(1) = 2πiZ.

**Each S1 item's radial coordinate.**

| Item | Coordinate | Of kind (c)? |
|---|---|---|
| Local smoothing | x = log(s/b), s the radius in the σ-plane | Yes, the real part of log on C*; the angle is averaged |
| NS, gravity side | x = ρ_c log(ρ/ρ_c), with (ρ, x⁰) the boost-polar coordinates of (S3) | Yes, in Lorentzian signature: log of X + cT. Its imaginary period is the thermal circle (standard; not in the lessons) |
| NS, OpenAI | q_NS ≍ τ | A power, not a logarithm; its logarithm is the similarity time |
| Connes | log u on R₊* with du/u; log λ | Yes |
| LM7 | the Kummer coordinates κ_p, with values in Ẑ(1) | Yes, the profinite form: the same torsor after completion |
| S^6 | c with w = e^{−πic}; classification by c mod 2 | Yes: c is the logarithm of the modulus, and 2Z is the deck group |
| ETH | T | No |
| TOTEX2 | stage | No |
| Yang–Mills | logarithm of the scale, through the running coupling | From general knowledge only |

So "every radial dimension of S1 is a logarithmic coordinate" is **wrong for ETH and TOTEX2** and holds for the rest.

## H3. Sum of squares on a cover, not after descent

**What the proposition says.** On the phase cover (a = √u, b = √v, ρ = √w, phase δ), Ψ_s is a Hermitian sum of
squares (`eq:cueM-U3-Hermitian-square`). Ψ₂^♯ is not a sum of squares in R[u,v]: its Gram matrix in (1,u,v) is unique
and has leading minor −55/12.

**Proved here (mine).** A real polynomial of degree two is non-negative on R² exactly when its Gram matrix is positive
semidefinite. So the proposition is equivalent to: Ψ₂^♯ takes negative values somewhere on R². It is non-negative only
on the image of the cover (u, v, w ≥ 0). The descended certificate is therefore not a plain sum of squares but a
weighted one, Ψ = σ₀ + uσ₁ + vσ₂ + …, where the terms with odd powers of a = √u give u times a square. The obstruction
is that the image of the cover is a proper semialgebraic set.

**Against Weil positivity.**
- Function fields: **known**. Weil's positivity is the Hodge index theorem on C × C; positivity is a statement about
  squares on the surface and descends to correspondences.
- Q: **new and open**, and it is the known missing object (the analogue of C × C). In Andrews–Connes–La Gatta the
  nearest structure is the semilocal space: QW_λ is a positive Sonin term plus a compact pair term "without definite
  sign" (line 1221 of the TeX). So on that space positivity is a square up to a compact piece; no cover on which it is
  a sum of squares outright is given.

**Against E.32, and the formal statement that would make them the same.**
- Candidate statement: "a certificate exists on the cover (or at each finite level), the set of certificates is
  acted on by the deck (or scaling) group, and the obstruction to an invariant certificate is a class in H¹ of that
  group."
- **It does not hold for the sum-of-squares case. Wrong.** For a finite deck group acting on a convex set of
  certificates, averaging gives an invariant one; the H¹ vanishes. The certificate descends, in the weighted form.
  What fails is only its shape.
- **It holds for E.32**, where averaging is division by q − 1 and cannot be done uniformly: that is the lim¹ class of
  revision 1.
- So the two are the same only at the level "local or covering data fine, global datum not". The mechanism differs:
  the sum-of-squares obstruction is in degree zero (which isotypic part of the deck group carries the certificate),
  E.32's is one degree up.

## H1. Nielsen complexity to Teichmüller and fusion

| Link | Mark | Basis |
|---|---|---|
| Caputa–Magán: the complexity functional "can be written as the Polyakov action of two dimensional gravity", equivalently the geometric action on Virasoro coadjoint orbits | Known | abstract only; the exact cost function was not read |
| Diff(S¹)/PSL₂(R) inside T(1) = QS(S¹)/PSL₂(R) | Known | not opened |
| GT acts on the universal Ptolemy–Teichmüller groupoid | Known | not opened |
| Bakalov–Kirillov: the Lego–Teichmüller game is equivalent to Moore–Seiberg data | Known | not opened; cited in our own archive notes (cotes 146, 147) |
| Teschner: quantum Teichmüller theory and Liouville theory | Known | not opened |

**The open link.** Does the RG subgroup of the cosmic Galois group map into a group acting on the motivic π₁ of
P¹ minus three points, or on GT?
- **A map exists, non-canonically. Known, from general knowledge of the papers (not opened beyond the abstract).**
  Connes–Marcolli's group is U ⋊ G_m with Lie(U) free on one generator e_{−n} in each degree n ≥ 1, and the RG is the
  one-parameter subgroup generated by e = Σ e_{−n}. They identify U ⋊ G_m non-canonically with the motivic Galois
  group of mixed Tate motives over Z[i][1/2]. Mixed Tate motives over Z are a full subcategory, which gives a
  canonical surjection onto their Galois group, and by Brown that group acts faithfully on the motivic π₁ of
  P¹ minus three points. The composite sends the RG generator into the Lie algebra that the hexagon and pentagon
  constrain.
- **A canonical map: new and open.** The identification is a choice, so the image of e is not determined. The
  natural test (do the periods of the physical theory lie in the multiple zeta values, so that the action factors
  through mixed Tate motives over Z?) is known to fail in general for Feynman periods (Brown–Schnetz, from memory).
  Precise statement to test: for which renormalizable theories does the cosmic Galois action on the counterterms
  factor through the motivic Galois group of mixed Tate motives over Z.

## H4. Black holes

- BHMR (fluid equations from Einstein's equations), Emparan–Suzuki–Tanabe, Adams–Chesler–Liu: **known**, not opened.
- Lehner–Pretorius, abstract only: the horizon becomes "a sequence of 3-dimensional spherical black holes joined by
  black string segments", the segments are again unstable, and they "will reach zero radius in finite asymptotic
  time".
- **Is the cascade of the form of OpenAI's stages? Wrong.** OpenAI's stage j is an order of approximation of one
  flow at all times (residual order 1/5 + j/10); it is not a generation in time. The Lehner–Pretorius cascade is a
  sequence of generations, each a rescaled copy of the last, summing to a finite time.
- **It is of the form of the continuation's layers. New and open.** The Alpöge–Buckmaster layers (λ_q = λ_{q−1}^{Q_q})
  and the cascades of Córdoba–Martínez-Zoroa cited in OpenAI's §1.1 are generations in time. The difference to check:
  the black-string ratio is fixed per generation (from general knowledge of the paper; the abstract does not give
  it), the fluid layers are super-exponential.
- **A finite-time fluid singularity derived from a black-hole cascade, or the reverse: none found. Open.** The
  derivations run from gravity to the fluid equations, not between singular solutions. The GR-VAC lessons say
  explicitly that they do not do this.

## H6. One class seen from a D+1 invertible theory

The hunch, as corrected by the user: every smooth-to-discrete or finite-to-limit obstruction in the map is one class,
one degree up, and v35's chain (cone → perfect complex → determinant line → relative invertible theory) makes it an
invertible theory in one more dimension. Else–Nayak and Kaplan are the known lattice case and are not what is marked
here. v35's own conclusion, for the record: "The interesting bridge is not the assertion that anomaly inflow, Verdier
duality, and RG flow are one operation. It is the existence of a composable chain"; three arrows are "established
constructions", the fourth "the substantive research problem".

| Case | A class one degree up in a cone or telescope? | Does v35's chain give an invertible theory? | Mark |
|---|---|---|---|
| E.32's lim¹ | **Yes.** The derived limit is the fibre of (1 − shift) on the product, Milnor's telescope, and lim¹ is its H¹. E.32's class sits in H² and comes from lim¹ of H¹ (revision 1). The first half of the hunch holds here | **Not as it stands.** The complex [R → R], d = (q − 1), is not perfect: R is the module of 3-adic sequences tending to zero. No determinant line exists. Each prime's piece [Z₃ → Z₃] is perfect with determinant of size 3^{v₃(q−1)}; the product over primes diverges, which is the same failure | New and open. Statement: find a category in which the residue complex is dualizable and compute its determinant; the perfect part RΓ(Z[1/3], Z₃(2)) already has one, with H¹ = Z/3 (E.29) and H² = 0 (E.32g) |
| Weil positivity, λ → ∞ | **For the zeros, yes; for positivity, none found.** 2501.06560, after line 412: the spectral realization is "the action of the idele class group on H¹(Y_Q, η)", a relative group, citing Connes–Marcolli Theorem 4.116 (not opened). Hypothesis LA is an inequality between two ladders, not a class | The determinant would be the zeta function as a determinant of the scaling flow on that H¹. v35 lists exactly this as its missing clause | New and open |
| NS all-stage force budget | **None found.** The obstruction is a rate (λ_q^{9/8} per layer). Candidate formal statement (mine): the forces realizing the first q layers on K × [0, t_q] form a projective spectrum of Fréchet spaces under restriction; a smooth terminal force is an element of its limit; the obstruction to extending stage data lies in the derived functor Proj¹ of the kernel spectrum (the functional-analytic lim¹) | No determinant in sight | New and open |
| Sum of squares after descent | **No.** By H3 the obstruction is in degree zero, and the H¹ of the deck group vanishes by averaging | Not applicable | Wrong for this case |
| Type III against type II | **Yes, in the known theory (general knowledge, not opened).** The modular flow is a canonical class of one-parameter groups up to inner cocycles (Connes's cocycle theorem); the crossed product is where it becomes inner. In K-theory the crossed product by R shifts degree by one (Connes–Thom). v35's third line, C*-extension → [∂] ∈ KK¹ → bulk–boundary index, is this shape | In CLPW the added generator is the observer's Hamiltonian, and the result is type II₁ with entropy defined up to a constant (abstract). So the crossed product plays the role of the bulk in the sense that it adds one generator that trivializes the class. That it is an invertible theory in the sense of v35's chain is not shown anywhere I read | New and open |

**Across the cases.** The hunch's first half (a class one degree up) holds for E.32 and for the crossed product, is
unformulated for LA and the force budget, and fails for the sum-of-squares case. Its second half (v35's chain) holds
in none of them as it stands; in E.32 it fails at a named step, perfectness. "One class" across the cases is **open**:
nothing read relates E.32's class to the modular class.

One fact from v35's own table bears on it: "Every homomorphism Q → Z is zero; only the normalized real trace survives
the UHF limit" (status: no-go theorem). That is a finite-to-limit obstruction already proved in v35, and it is again a
divisibility statement, like E.32's division by q − 1.

Does the crossed product play the role of the D+1 bulk? In the sense above (it adds the generator that makes the flow
inner, and shifts K-theory by one): yes, known. As an invertible field theory: open.

## H5. The cobordism conjecture

**Statement (abstract only):** "any proposed quantum theory of gravity with non-trivial cobordism classes belongs to
the Swampland"; the argument rests on the absence of global symmetries, and trivializing the classes requires
defects.

**For anomalies (from general knowledge of the paper).** A non-trivial cobordism class of the internal space would be
a conserved charge of a global symmetry. So each class must be killed by a defect or the symmetry gauged. With no
global symmetries there are no 't Hooft anomalies left to match; gauge anomalies must cancel, by inflow from the
defects where needed.

**Beside v35's table.**
- v35's row "Anomalies violate Poincaré/Verdier duality: rejected as stated; anomalies obstruct gauge-invariant
  descent or trivialization of an anomaly line" agrees with the conjecture's logic: the class is trivialized by
  adding an object, not by breaking duality.
- v35's row "'t Hooft anomaly classes are matched" along RG is the statement without gravity. The conjecture is the
  statement with gravity: the classes vanish. v35's table has no row for this difference. That is a gap to fill in
  the separate run, not a claim checked here.
- Bordism appears in two roles that should be kept apart: in Freed–Hopkins (v35 line 7048) bordism groups classify
  the anomaly theories; in McNamara–Vafa the bordism classes of configurations are the charges.

## Effect on the map

- **S7:** Grothendieck's passage at cote 140-4, scans 172–175, is the source statement of S7. Add it to the S7 entry.
- **S4 and the real place:** add the archimedean identification for E.25 (H2), and Grothendieck's "discretification =
  archimedean valuation" (cote 140-2, scan 378).
- **Carry-over 3 and 4:** E.32 is a telescope class (H6, first row); the tame test followed by the lim¹ check is the
  finite and the limit part of one derived limit.
- **Not carried:** the sum-of-squares obstruction does not belong with E.32 (H3).
- **New statements to test, in order of how small the first check is:** the degree-two remark on Ψ₂^♯ (evaluate it at
  one point outside the image of the cover); the boundary defect at ∞ against local Tate duality at R; the Proj¹
  formulation of the force budget; a dualizable category for E.32's residue complex.

# Revision 2: the open items pushed, and eight further connections

Claude Fable 5.2, effort medium, no sub-agents. 13 November 2026, 03:41 UTC (machine clock).

**Outcomes.** Known (source and place) / new and proved (with the proof) / new and open (statement and first check) /
wrong. "Proved" means a short argument or an exact computation given here; nobody checked it. Scripts:
`rev2.py` and `rev2b.py` in the session scratchpad (full paths in `KNOWLEDGE_HANDOFF_SHAPE_MAP.md`).

**Read for this revision.** Table `tab:logbound` and Fact `fact:logbound` of 2611.13129; satellite 13 line 695 (the
coordinate w); Lehner–Pretorius 1006.5960 (abstract, Table I and the passages on generations, from the arXiv PDF).
**Not opened; from general knowledge:** Milne's *Arithmetic Duality Theorems*, Brown–Schnetz, Conway–Sloane,
Cheng–Duncan–Harvey 1307.5793, Balaban, Connes math/9811068, Connes–Consani 2004.08879, Grover–Mezzadri–Simm,
Penington, Almheiri–Engelhardt–Marolf–Maxfield, Bost–Connes, Connes–Marcolli math/0504085, Casini–Huerta–Myers,
Kapustin–Sopenko, Tseytlin, Myers–Sinha, Henningson–Skenderis. OpenAI's Yang–Mills proof is unreleased.

## A. The open items of 1b

**A1. Ψ₂^♯ outside the image of the cover. New and proved.** Exact values: Ψ₂^♯(4,0) = −217/24, Ψ₂^♯(3,0) = −13/6,
Ψ₂^♯(0,−1) = −97/24. With w = (1 − u + 2v)/2 (satellite 13, line 695) these points have w = −3/2, w = −1 and v = −1:
outside the image, where u, v, w are squared moduli. Inside, Ψ₂^♯(0,0) = 47/24 and Ψ₂^♯(1,0) = 10/3. So the
obstruction of the proposition is that Ψ₂^♯ is negative off the image; the certificate that descends is a weighted
sum of squares.

**A2. The boundary defect at ∞ and Tate duality. New and proved for the Tate complex; its place in Artin–Verdier
duality is known (Milne, not opened).**
- Statement. Let G be a finite group, M a finite G-module, M^∨ its Pontryagin dual. Put
  B(M) = Cone(C_*(G,M) → C^*(G,M)), the cone of the norm map from group chains to group cochains (the Tate complex).
  Then B(M)^∨ ≃ B(M^∨)[−1], and on cohomology Ĥ^r(G,M)^∨ ≅ Ĥ^{−r−1}(G,M^∨).
- Proof. Pontryagin duality exchanges chains and cochains: C^*(G,M)^∨ ≅ C_*(G,M^∨) and C_*(G,M)^∨ ≅ C^*(G,M^∨), and
  the dual of the norm map is the norm map. Dualizing the triangle C_* → C^* → B gives B(M)^∨ as the fibre of the
  norm map for M^∨, which is B(M^∨)[−1]. Taking cohomology gives the second statement, which is classical Tate
  duality for finite groups.
- This is v35's theorem D_Z B_j(F) ≃ B_j(D_U F)[−1] with the same shift, for Z = {∞}, G = C₂ = Gal(C/R), extension by
  zero read as chains and direct image as cochains. The unboundedness named in 1b is handled because B is the
  two-sided Tate complex.
- What stays open: that the six operations of v35 exist on the Artin–Verdier site with this j_!. In Milne's
  treatment cohomology with compact support of an open of Spec Z is defined with Tate cohomology at the real place
  (from memory), which is this B.

**A3. The Proj¹ formulation of the force budget. Wrong (my own 1b candidate).** For the spectrum of spaces
C^∞(K × [0, t_q]) under restriction, the restriction maps are surjective (smooth functions extend), so Proj¹ vanishes
and the limit is C^∞(K × [0, T)). Every compatible family of stage forces is a smooth force on [0, T). The terminal
extension is the further condition that all derivatives stay bounded as t ↑ T. That is a uniform bound, not a
derived-limit class. So the force budget is of S1's kind and not of E.32's.

**A4. A determinant for E.32. Perfect part: known, and checked against the return's numbers. Residue part: new and
open; first check negative.**
- Perfect part. RΓ(Z[1/3], Z₃(2)) has H⁰ = 0, H¹ = Z/3 (E.29) and H² = 0 (E.32g). Its determinant has size 3. The
  3-adic zeta value at −1 is (1 − 3)ζ(−1) = (−2)(−1/12) = 1/6, of 3-adic absolute value 3. The two agree, as the
  main conjecture for Q (Mazur–Wiles; not opened) says they must.
- Residue part. The complex is [R → R] with d = diag(q − 1) on R, the 3-adic sequences tending to zero. In the
  derived category of 3-complete modules the dualizable objects are the perfect complexes (general knowledge), and R
  is not finitely generated. The formal determinant ∏(q − 1) does not converge 3-adically. No category was found in
  which it does.
- Statement to test: the determinant of the whole of RΓ_cts(G_Q, Z₃(2)) should be defined relative to the perfect
  part, as a line whose "size" is the divergent product, regularized by the 3-adic zeta function.

**E.18 and a coefficient version of π_χ. Proved in the abelian case; open for H₁(U₄).** By Remark
`archimedeanplace` the lift of the point c is "uniquely determined up to sign", so c has isotropy {±1}, acting
through χ(−1). For a module M on which Ẑ* acts through χ, the cohomology of that isotropy group is H^*(C₂, M). That
is immediate. For M = H₁(U₄, Z₂) the Galois action does not factor through the abelianized Galois group (the
Jacobian has complex multiplication, and complex conjugation does not commute with it; general knowledge), so M is
not a coefficient system in the paper's abelian framework. Open: a non-abelian version of the cover.

**The cosmic Galois action and mixed Tate motives over Z. Known: it fails for φ⁴ (Brown–Schnetz, from memory, not
opened).** A φ⁴ graph at eight loops has a period whose motive involves a K3 surface and a modular form, so it is
not mixed Tate; the periods through low loop orders are multiple zeta values. So a factorization through the
motivic Galois group of mixed Tate motives over Z cannot hold for φ⁴ at all loop orders. Brown's own "cosmic Galois
group" of motivic periods (1512.06409, not opened) is the object that replaces it.

**Lehner–Pretorius generations against the Alpöge–Buckmaster layers. Different forms; one remark proved.**
- Table I of 1006.5960 gives string-segment radii 0.148, 0.05, 0.02 at times 203.1, 223, 227 for generations 2, 3,
  4 (errors 1 % to 20 %; the fourth from one low-resolution run). The radius ratio is about 1/3 and the time gaps are
  20 and 4. That is a roughly fixed ratio per generation: discrete self-similarity.
- The fluid layers have λ_q = λ_{q−1}^{Q_q} with Q_q = Q_* + q ≥ 200: the ratio grows with the stage.
- Proved (one line): under the Navier–Stokes scaling u ↦ λu(λx, λ²t) the force scales as λ³f(λx, λ²t). An exactly
  self-similar forced cascade at fixed ν therefore has a force growing like λ_q³ at layer q, unless the force
  vanishes at small scales. A fixed-ratio cascade of the black-string kind cannot be carried to forced
  Navier–Stokes with a bounded force by scaling alone. This is why OpenAI's construction needs the anomalous exponent
  h and a residual that is flat.

**The driven energy identity for (S38). New and proved.** Let φ solve (S38) with the wall condition
φ_x(t,0) = s(t). Then dE_k/dt = Re(φ̄_t(t,0) s(t)), by (S44). With zero initial data, the total work
∫₀ᵗ Re(φ̄_t(τ,0) s(τ)) dτ equals E_k(t) ≥ 0. So the total work up to any time is non-negative; the rate has no sign.
For a sum of layers the works add only up to cross terms between layers with the same k.

**𝒲(λ) against Table `tab:logbound`. The test is not available; the monotone form is not supported.**
- Every entry of the table is an upper bound for the true ratio ("by the min-max principle each entry is an upper
  bound"). A lower bound for 𝒲 cannot be tested on it.
- The column ε^N_λ(1)/δ₄(λ) reads 7.06, 8.11, 9.49, 9.17, 9.31, 9.76, 11.16, 10.46, 11.12, 9.66, 12.27, 13.83,
  18.07, 16.08, 19.02 for λ² = 5 … 300. It rises overall and falls four times; the entries are computed at
  different N and the paper says the large-λ ones are "the most overestimated".
- The paper's own reading: the ratio grows more slowly than log λ (fitted exponents 0.73, 0.54, 0.37 as N/λ²
  increases). So "𝒲 non-decreasing" is consistent with the trend and unproved; a clean test needs the ratios at one
  fixed N/λ² or extrapolated in N.

## B. Connections not yet treated

**B1. Niemeier.**
- PGL₂(5) permutes the six A₄ components of the A₄⁶ Niemeier lattice, through the glue code over F₅: **known**
  (Conway–Sloane, ch. 16, table of Niemeier lattices: G₁ of order 2, G₂ = PGL₂(5); from memory).
- The umbral group for X = A₄⁶, lambency 5, is GL₂(5)/2 with quotient PGL₂(5) (Cheng–Duncan–Harvey; from memory):
  **known**.
- **The module, checked by exact character computation. New and proved, at the level of rational characters.**
  - Over the **standard S₅** (the stabilizer of one marked point), the character of H₂(Δ₀,₆) is 24 at the identity,
    −1 on the 24 five-cycles and 0 on the other 95 elements. That is the character of the module induced from
    F₂₀ (the normalizer of a five-cycle) of its 4-dimensional module, with or without the sign twist. So over Q,
    H₂(Δ₀,₆) is six copies of a 4-dimensional module permuted by S₅ ≅ PGL₂(5): the shape of A₄⁶ ⊗ Q.
  - Over the **transitive PGL₂(5) ⊂ S₆** (the one permuting the six marked points as P¹(F₅)) it is not: the
    character is −8 on fixed-point-free involutions, 3 on elements of type (3,3), 1 on six-cycles. A module that
    permutes six summands has trace 0 on every element fixing no summand, so no choice of lift repairs this.
  - So the six components do **not** correspond to the six marked points. They correspond to the six Sylow
    5-subgroups of the S₅ that fixes one marked point, that is, to the six pentagonal structures on the other five
    points. The passage from the six points to the six components is the outer automorphism of S₆.
- **The lattice. New and proved, given EXIT P4d2.** The cycle lattice H₂(Δ₀,₆) ⊂ Z¹⁰⁵ with the standard form has
  determinant 5⁸ · 11¹⁰ · 13⁵ (computed as the Gram determinant of the orthogonal lattice of coboundaries, on a basis
  of 81 non-tree edges; this uses P4d2's statement that all 81 Smith entries are 1). It is not unimodular, and its
  determinant is not that of A₄⁶ (5⁶). With this form it is neither a Niemeier lattice nor A₄⁶.
- Holy constructions and Kneser neighbours: **new and open; no evidence found.** First check done: the determinant
  above. Next check: whether the six rank-4 summands are defined over Z, and the form on each.

**B2. Lattice to continuum gap.**
- **E.32 is a no-gap statement. New and proved.** In E.32, H² = R/dR with d = diag(q − 1) on R. The witness
  z = (q_j − 1)_j is not in dR (it would need w_{q_j} = 1 for all j, which does not tend to zero). It is in the
  3-adic closure of dR: its truncation to the first J primes is d of a finitely supported family, and the remainder
  has norm at most 3^{−J}. So the class of E.32 lies in closure(im d)/im d. Equivalently: d is injective and
  inf |q − 1|₃ = 0, so d has no gap, while every finite truncation has one. The return's own phrase: "the denominator
  is the actual image of d, with no closure added".
- **The common statement.** For a tower of systems, each with an operator d_n with closed range and a gap g_n > 0,
  the limit operator has closed range exactly when inf g_n > 0. If the gaps close, closure(im d)/im d is non-zero.
  For lattice gauge theory d is the Hamiltonian on the orthogonal complement of the vacuum; for E.32 it is Frobenius
  minus one. This is the direction "every finite level fine, the limit not". **Known** as functional analysis; the
  identification with E.32 is the new part.
- The reverse direction (finite-level classes that die in the limit) occurs when classes at finite level are
  killed by later maps: in E.32's own proof the groups H²(G_S, T_n) and the classes at each finite support die.
  For lattice gauge theory the analogue is finite-volume states whose energy does not survive the limit; from
  general knowledge, not checked.
- **Non-uniqueness of subsequential infinite-volume limits. Not a Mittag-Leffler failure.** Existence of limits
  along subsequences is compactness: an inverse system of non-empty compact sets has a non-empty limit. Having more
  than one limit point is the size of the limit set, not a lim¹ class. Whether OpenAI's result leaves uniqueness open
  could not be read: the proof is unreleased.

**B3. Semilocal Weil positivity as a limit.**
- **RH in the positivity form is not a derived-limit statement. Proved (one line).** The windows are nested and
  their union is dense; if QW_λ ≥ 0 for every λ then QW ≥ 0. Positivity passes to the limit with no obstruction.
- **What the limit does carry is a closing gap, as in B2.** If QW_λ > 0, its lowest eigenvalue ε_λ is positive at
  each λ and tends to zero like e^{−4πλ²}, while the global form has an infinite-dimensional radical. Hypothesis LA
  fixes the rate (ε_λ(j) against δ_{4j}(λ)). So Andrews–Connes–La Gatta, E.32 and the lattice gap share the form
  "a gap at every finite level, closing at a prescribed rate". **New and open** as a common statement; the rates are
  e^{−4πλ²} and |q − 1|₃.
- Positivity for λ ≤ √2 (the coordinator's citation) and the CUE finite-N moments against ζ were not read.

**B4. The plunge region and islands.**
- **Known correspondence (from memory, not opened):** the eigenvalues of the time–band limiting operator in the
  plunge region are what produce the logarithmic entanglement entropy of free fermions on an interval; the entropy
  is a sum over those eigenvalues, and the width of the plunge region carries the coefficient of the logarithm
  (Landau–Widom; Gioev–Klich). So the plunge region corresponds to the bulk entropy term.
- **Where a correspondence with the island formula fails:** the island formula extremizes area plus bulk entropy
  over a surface. In the parts of 2611.13129 read there is no area term and no extremization over the window: λ is
  fixed, and the variational principle minimizes QW_λ over functions. **Wrong** as an identification; the entropy
  half is known.
- The figure "(2/π²) log" for the width was not found in the parts read.

**B5. The absorption spectrum. Wrong as stated; the corrected statement is in the paper.** The near-radical part of
QW_λ is the finite-λ form of the **image** of the map ℰ, not of its cokernel: the intro says the minuscule
eigenvectors are reproduced by the ℰ-images of the zero-integral prolate vectors, and that ℰ maps into the radical of
QW. The link to absorption is on the image side: the Mellin transform of ℰ(f) is ζ times the Mellin transform of f
(standard; consistent with Theorem `thm:mellintheta`), so every function in the image vanishes at the zeros. The
cokernel, where Connes's spectral realization lives, corresponds to the complementary, strictly positive part.

**B6. Modular flow and RG. Known in special cases; no general theorem found.**
- Bost–Connes: the Hamiltonian is log n, so the time evolution is generated by the logarithm of the multiplicative
  scale, by construction; the modular group of a KMS_β state is that evolution rescaled by β. **Known.**
- Vacuum modular flow is geometric for a wedge (boosts; Bisognano–Wichmann) and, in a conformal theory, for a ball
  (Hislop–Longo; Casini–Huerta–Myers map it to a thermal state). **Known**, from general knowledge.
- Every type III factor has a canonical scaling flow on its type II core (Connes–Takesaki). **Known.**
- A theorem that the modular flow of a KMS state is an RG flow in general: none known to me. The entropic
  c-theorems use strong subadditivity and Lorentz invariance, not such an identification. **New and open.**

**B7. Anomalies of infinite systems. New and open, with a precise candidate.** (Kapustin–Sopenko not opened.)
- For a finite matrix algebra every automorphism is inner. For the quasi-local algebra of a half-chain, a limit of
  matrix algebras, there are outer automorphisms, and the approximately inner ones modulo the inner ones form
  closure(Inn)/Inn: the same "closure of the image modulo the image" as E.32 (B2).
- A homomorphism of G into outer automorphisms has an obstruction to lifting in H³(G, U(1)) (Eilenberg–MacLane;
  for operator algebras Jones and Sutherland; general knowledge).
- Candidate statement: the anomaly index of a locality-preserving symmetry is this H³ obstruction for the map from G
  to the outer automorphisms of the half-chain algebra, and it exists only in the infinite system because that group
  is a closure-modulo-image term of the tower. First check: read Kapustin–Sopenko's definition against it.
- v35's no-go row (only the real trace survives the UHF limit) is the K-theoretic side of the same limit.

**B8. Holographic c-functions. Partly known; the identification of the monotones is open.** (None opened.)
- Known: Perelman's F is the low-energy string effective action with f the dilaton (Perelman §1; Tseytlin), a
  central-charge action for the σ-model. The holographic Weyl anomaly is the logarithmic term of the on-shell bulk
  action (Henningson–Skenderis). The holographic a-function agrees with the anomaly coefficient at fixed points and
  is monotone under the null energy condition (Myers–Sinha).
- These involve two different flows: the worldsheet RG, under which the target metric moves by Ricci flow, and
  radial evolution in the bulk. The same action appears in both: its gradient flow is the first, and its on-shell
  value as a function of boundary data generates the second.
- Open: a theorem deriving the holographic monotone from the monotonicity of F, or the reverse.

## What revision 2 changes in the map

- **One form now covers four items.** E.32, the lattice gap, the closing of ε_λ and (as a candidate) the anomalies
  of infinite systems are all "closed range with a gap at every finite level; in the limit the gap closes and
  closure(im)/im is non-zero". This is sharper than S1's "missing uniform bound": it says which uniform bound (the
  gap of one operator) and what the obstruction is.
- **Two items leave that form.** The Navier–Stokes force budget is a boundedness condition with no class (A3). The
  sum-of-squares obstruction is in degree zero (A1, 1b).
- **The boundary defect at ∞ is the Tate complex**, with v35's shift (A2).
- **The Niemeier connection** holds over Q for the stabilizer S₅ and fails for the transitive PGL₂(5); the six
  components are pentagonal structures, not marked points; the natural lattice is not A₄⁶ or a Niemeier lattice.
- **Dropped:** the Proj¹ formulation; the cokernel reading of the near-radical part; the island identification;
  a factorization of the cosmic Galois action through mixed Tate motives over Z for φ⁴.

# Revision 3: four new returns

Claude Fable 5.2, effort medium, no sub-agents. 13 November 2026, 12:39 UTC (machine clock).

**Status.** All four returns are by GPT-6 Astra (ChatGPT Pro mode). **None is refereed.** Every item below is
"claimed by the return" unless it says otherwise. I read reports, not proofs.

**What was read.**
- TOTAL_EXACT_2: the final message (`RETURN_TEXT_20261113.md`): the table, §§1–2 in full, the start of §3, the table
  of §4. Not read: §§5–6.
- LM8, checkpoint 16 (INCOMPLETE): the task matrix (first third), sections E, F, G, the head of the residual table.
- LM7_PUSH, checkpoint 04 (INCOMPLETE, still running): the lead table, the section "Derived limits and local
  applications".
- LM4 (INCOMPLETE, still running): the first rows of the obligation table, two passages found by search.
- `pro_intake_20261113/IMPLICATIONS.md` did not exist when this was written.

## (a) The new items

| # | Item, in the literature's terms | Source | Form |
|---|---|---|---|
| T1 | For the category C_δ of finite ordered 3-uniform hypergraphs with positive predimension δ(U) = 2\|U\| − 3\|E(U)\| and strictly closed embeddings: every category of elements of a set-valued functor is aspherical (C_δ is total), and for the three vertex inclusions v₁,v₂,v₃ of a point into one hyperedge the map D_R(g) = (gv₂ − gv₁, gv₃ − gv₁) is objectwise injective, so the first left derived functor of the colimit is T₁(Q_R) ≅ R for every non-zero ring R, with projective dimension 1 | TOTEX2 A.24, A.34 | derived colimit |
| T2 | The strict chain filtered ⊊ exact ⊊ total ⊊ quasi-filtered | TOTEX2 D.1 | derived colimit |
| T3 | Totality is proved through the Fraïssé limit M: ⟨G_B, G_C⟩ = G_{B∩C}, every open subgroup of G = Aut(M) is the pointwise stabilizer G_B of a finite closed B, and an arbitrary functor is replaced, by two homotopy-final comparisons, by fixed points S^{G_B} of a continuous discrete G-set | TOTEX2 A.30, A.32, §2 | the Galois part |
| T4 | The repaired AKR construction has non-zero H₂ for every admissible choice | TOTEX2 C.1 | (closes C.9) |
| L1 | H¹ commutes with the inverse limit for compact pro-prime towers and for finite-dimensional rational BCH towers; "a fully explicit noncompact pro-discrete tower has H1 zero at every stage and Z2/Z in the limit" | LM8 F.15 | lim¹; closure(im)/im (Z is dense in Z₂) |
| L2 | The unrestricted global integral class-two section set: H²_cts is "the actual cokernel of the diagonal map multiplying the q-coordinate by 5^{v5(q−1)}" on 5-adic sequences tending to zero; "replacing its image by its closure loses information"; a Chebotarev construction gives a cup class zero at every finite coefficient level and non-zero integrally | LM8 F.21 | closure(im)/im |
| L3 | With a fixed finite ramification set S, the class-two set is Z₅⁶ and each non-empty integral fibre is unique | LM8 F.20, F.22 | the same, killed |
| L4 | Over Z[1/30], every class-four fibre has 125 elements, and these "merge after rationalization" | LM8 F.22 | integral against rational |
| L5 | "The literal inverse limit of all shrinking-annulus sheaf topoi is degenerate; the corrected covering-germ category retains the classifying topos" (BZ) | LM8 E.10–E.13 | the Galois part against the full topos |
| L6 | An order-486 quotient with m = 0, f = [X,Y] "passes every finite condition but violates the global coefficient congruence" r = (χ² − 1)/24: a finite GT-shadow that is not the reduction of a GT element | LM8 E | finite level against global; a congruence, so integral against rational |
| L7 | An exact metabelian solution "invisible in every pro-prime and universal S3 quotient but detected at order 75"; and, for the arithmetic normalizer criterion, "the common kernel of all such [maximal pro-prime] quotients remains a genuine residual problem" | LM8 A.22, G | pro-p against profinite |
| P1 | For the intrinsic rank-44 coefficient the first derived limit is non-zero; an actual pair has "a nonzero intrinsic obstruction with every local and finite-coefficient image zero" | LM7_PUSH A.1–A.4, A.13 | lim¹ |
| P2 | The Milnor term's "vanishing is equivalent to bounded nonzero Smith valuations of the residue differentials" | LM7_PUSH, derived limits | closure(im)/im, as a criterion |
| P3 | "Taking total cardinalities of invariants is refuted by two explicit coefficient lattices with identical total cardinalities and identical finite-S H2 orders but different derived limits" | LM7_PUSH | lim¹ is invisible to sizes |
| P4 | Neither phantom "dies after any finite extension" | LM7_PUSH C.4 | lim¹ is stable under finite base change |
| P5 | A total evaluator is impossible "both for finite-coefficient queries and for the explicit finite-program input family with a known convergence modulus" | LM7_PUSH A.5 | lim¹ is not decidable from finite data |
| P6 | At 17, an integral target with the local cusp restriction and a class-three lift "but no class-four or higher lift" | LM7_PUSH A.6, B.4 | a finite-depth obstruction (S7's layers), not a limit |
| F1 | Discrete recognition and the pro-p forms are proved; "Full profinite recognition is refuted by the marked type (0,4) extension D.29 and the closed genus 2 extension D.30, both torsion-free of index 2" | LM4 item 6 | pro-p against profinite |
| F2 | An order-3 automorphism has a proper fixed subgroup with the same maximal pro-3 quotient | LM4 (passage found by search) | pro-p against profinite |

Two points on the brief. Its summary says full profinite compatibility in LM4 is "open"; the report's table says
full profinite recognition is **refuted** (D.29, D.30), with conjugacy in the full loop group undecided. And the
A₅ endomorphism and the mixed-prime counterexample of the brief were not found in the part of LM4 I read; they stand
on the coordinator's summary.

## (b) The refined pattern, framework by framework

| Framework | Where the obstruction lives | What kills it | What does not | Items |
|---|---|---|---|---|
| 1. Derived colimit over a category | T₁ = colim₁, a copy of R; projective dimension 1 | filteredness; a finite-family Ramsey property with common successors (checkpoint C.12) | asphericity of every category of elements (totality); connectedness; a change of coefficient ring | T1, T2 |
| 2. Derived limit over a tower | lim¹ of H^{i−1}, equal to closure(im d)/im d | compactness of the stages (L1); finite dimension over Q (L1); a fixed finite set of primes (L3); bounded Smith valuations (P2) | finite base change (P4); vanishing at every finite level and every place (L2, P1); equality of sizes (P3); any finite computation (P5) | L1, L2, P1–P5, E.32 |
| 3. The Galois part against the full topos | the full sheaf category degenerates in the limit or is too large | passing to coverings (L5), or to continuous sets of the automorphism group (T3) | — | L5, T3 |
| 4. Pro-p against profinite | the kernel of the map from the profinite group to the product of its maximal pro-p quotients; visible only in finite quotients of mixed order (75) | restriction to one prime | checking every prime separately (L7, F1, F2) | L7, F1, F2 |
| 5. Integral against rational | torsion in H¹ and denominators (5³ classes; division by 24) | tensoring with Q | — | L4, L6 |

**What this does to S1–S7 and B1–B4.**
- **B2 is confirmed twice more and sharpened (claimed).** LM8 F.21 is E.32 at the prime 5, with the sentence
  "replacing its image by its closure loses information". LM7_PUSH states the criterion I wrote in B2 as a theorem:
  the Milnor term vanishes exactly when the Smith valuations are bounded. L1's Z₂/Z is the smallest instance.
- **B2 gains three properties** from P3–P5: the class is invisible to cardinalities, survives finite extensions, and
  cannot be computed from finite data. The first one settles a point left open in revision 2 (A4) and in 1b (H6):
  a determinant in the sense of a size cannot see this class. So the second half of the user's D+1 hunch is **wrong
  for framework 2 if the determinant is a size**; it stays open for a finer notion.
- **S7 moves.** Section sets of compact towers have no lim¹ (L1). So the wall shared by the returns (section
  surjectivity for P¹ minus three points) is not of framework 2. The lim¹ classes arise for integral coefficients
  with unrestricted ramification, a non-compact module. What is left for S7 is framework 4, as LM8 says of its own
  residue: "the common kernel of all such quotients". This corrects revision 1, e, where I asked that FLAGGED ZD10
  "carry the lim¹ term": that holds for the integral H², not for the profinite section set.
- **S1 for TOTEX2 is settled.** The blind map's row (stages of the AKR completion, C.9 open) is closed by T4, and the
  main question is answered in the negative by T1. Carry-over 7 (attack the Ramsey implication C.14) is superseded.
- **S3 (quadratic invariants) extended.** T1's proof is a counting inequality 2u > 3r from positivity of the
  predimension: a private vertex exists. The obstruction comes from three arrows, and pairs are harmless (condition
  IV holds). In LM the obstruction first appears at class two. In both, pairs or the abelian level are fine and the
  first failure is at the next arity.
- **S5 contradicted in one place.** The blind map said the stronger statement with an identity (Ramsey) was the way
  in for TOTEX2. The return refuted the target statement directly, with one explicit category.
- **B1, B3, B4:** unchanged.

**One statement that covers frameworks 1 and 2 (mine).** Both are the first cohomology or homology of the index
category with coefficients in a diagram. Over a tower it is lim¹ and needs non-compact coefficients. Over C_δ it is
non-zero for every coefficient ring, finite fields included, because the index category is not filtered. So
compactness kills the class over a chain, and only the shape of the index category kills it in general.

## (c) Speculation, each with its test

1. **Exactness is a Ramsey property.** For categories of finite structures with a Fraïssé limit M, abelian colimits
   are exact exactly when the class has the Ramsey property, that is, when Aut(M) is extremely amenable
   (Kechris–Pestov–Todorcevic). Support: ordered graphs are Ramsey and exact (checkpoint C.13); C_δ is a Hrushovski
   class, the standard source of failures of Ramsey expansions (Evans–Hubička–Nešetřil, cited by the return; from
   memory). *Test, a candidate prompt for GPT-6 Astra:* decide exactness and totality for three categories: finite
   sets with injections; finite linear orders with increasing injections; C_δ with the order forgotten. The first is
   exact over Q and not over F_p (coinvariants of symmetric groups; my expectation), which would also tie framework
   1 to framework 5.
2. **The Weil form has a Milnor sequence.** Hypothesis LA is the analogue of P2: "the ratios ε_λ(j)/δ_{4j}(λ) are
   bounded above and below" is a bounded-valuation condition, with the prolate rungs as the valuations. *Test:*
   write the tower of windows as a tower of complexes whose differential has singular values ε_λ(j), and check that
   its lim¹ vanishes exactly under LA. Ours first (small); then a candidate prompt.
3. **The section-conjecture residue is the mixed-prime kernel.** A section of the arithmetic fundamental group of
   P¹ minus three points over Q whose image in every maximal pro-p quotient is a point or cusp section is itself
   one. *Test, a candidate prompt:* the first mixed quotient, of order 75 (LM8 A.22), and LM4's D.29 and D.30;
   state it against the known failures of the pro-p section conjecture (Hoshi; from memory).
4. **Undecidability is the reason four returns stop at one wall.** P5 says a lim¹ class cannot be evaluated from
   finite queries. If the remaining statement of S7 had a part of that kind, no finite computation in the returns
   could reach it. By the correction above the profinite section set has none; so this speculation predicts that the
   remaining wall is decidable level by level and hard only in the limit over mixed quotients. *Test:* the same
   prompt as 3.
5. **The limiting topos and Gabber's remark.** L5 (the sheaf limit degenerates, the coverings survive) and the
   remark in Connes–Consani 2501.06560 that Artin–Verdier duality holds on the site of abelian extensions say the
   same thing: the duality lives on the Galois part. *Test:* check whether the Tate complex of revision 2, A2, is
   computed by the covering part alone. Ours.
6. **Framework 1 is dual to framework 2.** The Pontryagin dual of T₁(Q_R) is a first derived limit over the
   opposite of C_δ with compact coefficients. So T1 gives a derived limit of compact modules that does not vanish,
   over an index category that is not a chain. *Test:* write the dual diagram for R = F_p and compute. Small; ours.

**The three tests to run first:** 1 (it would say when total implies exact), 3 (it relocates S7's wall), and the
referee's check of P2 against E.32, L2 and L3 (it is the criterion the whole of B2 rests on).

# Revision 4: the links against their sources; the obstruction in each framework; Yang–Mills as a test

Claude Fable 5.2, effort high, no sub-agents. 13 November 2026, 13:54 UTC (machine clock). Successor of the agent
that wrote the blind map and Revisions 1–3.

**Status.** Marks used: **proved (source)**: a theorem in a source I opened, statement read; **proved here**: a short
argument of mine, checked by nobody; **claimed**: a GPT-6 Astra return, unrefereed, with what was read of its proof;
**open**: with its test; **speculation**: marked, with its test. A negative is about a route I checked. Literature
is paraphrased; quotation marks are used for the user's words, the returns' words, titles and terms.

**What governs the D+1 part.** The user's statements of 13 November (session transcript, 13:38–13:46 UTC; read from
the transcript, in the user's words):
- "if you're going to ask me how the shape of any potential resolution to this, it's going to be shaped like anomaly
  inflow. That's what I think may be the case. And the obstruction is going to be shaped like Poincaré invariance
  violation. That's my hunch. That's all it is."
- "discrete to smooth being mapped, like going through infinity. That combined with what I just said is where I think
  some sort of answer may go, but this is vague."
- "the D+1 thing I just mean the shape of that, the resolution of an anomaly in the sense of a ['t Hooft] anomaly
  ... But this step 1 would be to make precise the obstruction in the way that the obstruction maps to these
  problems." Callan–Harvey and Freed–Hopkins–Lurie–Teleman are "probably underrepresented as a solution type".
- "the hunch for a resolution when the problem isn't even well stated yet isn't necessarily the thing you should be
  focusing on."
- ER = EPR (Susskind, Maldacena, Van Raamsdonk) as the same resolution shape in gravity and quantum mechanics.
- "The suspicion, not the claim. It's called a conjecture"; "I'm not saying everything is anomaly inflow."

So this revision does step 1 first (sections 2 and 3). The resolution shape is treated as a conjecture at the
precision stated (section 4), tested on Yang–Mills as the user asked (section 5), and restated per problem
(section 6).

## 1. What was opened for this revision

**Returns and project files.**
- LM7_PUSH checkpoint 04, `sections/F_root.tex`: F.1–F.5, statements and proofs, every step followed; `C_agent.tex`
  C.7 with proof.
- LM7 (zip of 13:14 UTC), `sections/E_completed_pairs.tex`: the statement of E.32.
- LM8 checkpoint 16: F.15 (statement, proof of surjectivity and of the compact case), F.21 (statement), G.20
  (statement, first two attacks).
- LM4 (13:14 UTC), the report only: the rows of items 6, D.b, D.d; the sections on D.26–D.30 and D.27; the passage
  on the A₅ endomorphism.
- `pro_intake_20261113`: IMPLICATIONS, INTAKE_TOTEX2, PUSH_ITEMS in full; INTAKE_LM8 head and selected rows.
- `expert_conference_20261113`: AGENDA; the round-1 talks of the shape-map agent, the Dérivateurs expert and the
  LM7 reviewer in full, the intake's talk §§3–5; the round-2 replies of the shape-map agent (in full), the
  Dérivateurs expert and the LM7 reviewer (first part of each).

**Literature, as e-print TeX** (all under `Free or receipted\free\arxiv-eprints-shape-20261113\ep_<id>\`):

| Source | Read |
|---|---|
| Freed–Hopkins 1604.06527 | the main theorem (label `thm:110`), §8.4.5–8.4.6 on the anomaly theory of free fermions |
| Freed–Teleman 1212.1692 | the introduction's paragraph on relative theories; the first definition (label `thm:1`) and the text after it up to the conformal example |
| Freed–Hopkins–Lurie–Teleman 0905.0731 | the introduction's paragraph on Chern–Simons as an anomalous theory; the paragraph before §9.3 |
| Freed 1404.7224 | located only (lines 345, 576–582) |
| Córdova–Freed–Lam–Seiberg 1905.09315 | abstract; the lines of §"Synthesis via anomaly inflow" |
| Gaiotto–Kapustin–Komargodski–Seiberg 1703.00501 | introduction (lines on inflow and on the mixed anomaly); the passage around eq. `anomaly` (θ → θ + 2π); the passage around eq. `inflow`; searched for "five", "5d", "bulk" |
| Else–Nayak 1409.5436 | abstract |
| Kapustin–Sopenko 2401.02533 | abstract; §§ "Anomalous symmetries in quantum mechanics" and "... of quantum spin chains" up to the Proposition |
| Kechris–Pestov–Todorcevic math/0305241 | the statement of the main correspondence (introduction) |
| Moore 1106.3127 | the theorem on the convex Ramsey property, all six conditions |
| Evans–Hubička–Nešetřil 1801.01165 (sparse graphs) | abstract; Theorems `38`, `CorC0`, the Corollary on `Aut(M_F)`, the remark on general predimensions |
| Evans–Hubička–Nešetřil 1705.02379 | abstract (a different paper: free amalgamation classes with a free order are Ramsey) |
| Brown 1102.1312 | abstract, the main theorem (label `intromaintheorem`) |
| Connes–Marcolli hep-th/0411114 | Proposition `SNmotives`, Proposition `motgal` and the paragraph after it |
| Brown–Schnetz 1006.4064 | abstract; lines 123, 233, 1693–1715 |
| Brown 1512.06409 | abstract |
| Cheng–Duncan–Harvey 1307.5793 | the table rows for A₄⁶ |
| Tseytlin hep-th/0612296 | abstract |
| Bakalov–Kirillov math/9809057 | abstract |
| Klebanov–Witten hep-th/9905104 | lines 549–608 (the two quantizations) |
| Witten 2112.12828; Chandrasekaran–Longo–Penington–Witten 2206.10780 | abstracts |
| Van Raamsdonk 1005.3035; Maldacena–Susskind 1306.0533 | abstract; the lines defining ER = EPR |
| Kim 1510.05818 (arithmetic Chern–Simons) | abstract; §"boundaries", first page |
| Harpaz–Schlank 1110.0164 | abstract and introduction lines on homotopy fixed points |
| Connes–Consani 2501.06560 | line 415 (Gabber) re-read |
| Downloaded, not read | 1011.5819, hep-th/0308031, hep-th/9912012, gr-qc/9406019, 2209.07471 (abstract only), 1909.10355, 1807.04422 |

**Yang–Mills** (in `...\arxiv-eprints-shape-20261113\kitp_ym\`): the committee's statement of October 2026 (two
pages, in full); its second statement of 3 November (one page, in full); the Yang–Mills group's assessment of
10 November, `assessment-1.pdf` (35 pages): Part I, pp. 1–13, read; Part II not read beyond the opening of §9. Also
the README of the public repository `scottnarmstrong/yang-mills-informalization`.

**Not opened; what is said of them is from general knowledge:** Jannsen 1988; Milnor 1962; Bost–Connes 1995;
Callan–Harvey 1985; Serre, *Cohomologie galoisienne*; Isbell–Mitchell; Oberst; Guichardet 1972; Hoshi 2010;
Mochizuki; Stix; Nakamura; Kechris–Rosendal; Angel–Kechris–Lyons; Gray; Mazzeo; Milne; Córdova–Freed–Lam–Seiberg II.
**Not reopened** (the predecessor's readings stand as he marked them): Perelman, the Navier–Stokes sources, the
GR-VAC lessons, Andrews–Connes–La Gatta, the zeta workbench, S⁶, Lehner–Pretorius, v35, *La Longue Marche*.

## 2. The links, each with its statement and status

### 2.1 Anomalies and inflow (H6, B7, the card's D+1 section)

| Link | Precise statement | Status |
|---|---|---|
| An anomaly is an invertible theory one dimension up | An anomalous n-dimensional theory F with anomaly α is a map from the trivial theory to the truncation of an invertible (n+1)-dimensional theory α: on a closed n-manifold X, α(X) is a line and F(X) is an element of it; on a closed (n−1)-manifold the state space is defined up to tensoring with a line | **A definition in the literature** (Freed–Teleman, first definition and the text after it; FHLT introduction; read). Dimensions and sizes cannot see α: its spaces are one-dimensional and its partition functions non-zero |
| Classification | Deformation classes of reflection-positive invertible n-dimensional extended topological theories with symmetry group H_n correspond to the torsion of [MTH, Σ^{n+1} I_Z] | **Proved (Freed–Hopkins, main theorem)**, statement read. For free fermions the anomaly theory's class is a conjecture there (their `thm:124`) |
| Lattice form | A symmetry acting locally but not on-site on the edge of a (d+1)-dimensional phase has an obstruction class in H^{d+1}(G, U(1)) | Else–Nayak, abstract only |
| B7: anomalies of infinite chains | For a homomorphism α: G → (locality-preserving automorphisms of a spin chain), restrict to a half-chain by a map β that is a homomorphism only modulo conjugation by local unitaries; the resulting class [ω] ∈ H³(G, U(1)) is independent of choices | **Proved (Kapustin–Sopenko, definition and Proposition read).** The construction is the Eilenberg–MacLane obstruction for a homomorphism of G to automorphisms modulo inner ones, so Revision 2's candidate holds in its first half. That the image lies in closure(Inn)/Inn rests on "automorphisms of UHF algebras are approximately inner" (not opened). They also state that the index does not depend on the Hamiltonian |
| Type III against type II | The type II∞ algebra is the crossed product of the type III₁ algebra by its modular group; entropy is then defined up to a state-independent constant | Witten, abstract (read). For the de Sitter patch: type II₁, entropy equal to generalized entropy up to a constant (CLPW, abstract) |
| Anomalies in the space of couplings | 't Hooft anomalies extend to scalar couplings treated as background fields, and the same (d+1)-dimensional classical theory describes them by inflow | Córdova–Freed–Lam–Seiberg, abstract and §"Synthesis via anomaly inflow" (read) |
| Callan–Harvey | Not opened (not on arXiv). GKKS use the name for coupling to a higher-dimensional theory | — |

### 2.2 Derived limits over a tower (E.32, B2, frameworks 2 and 5)

**(a) LM7_PUSH F.1–F.3, the criterion behind B2. Claimed; the proof was read here step by step and I found no gap.**
Setting: L a number field, S finite containing ℓ and ∞, M a finite-rank Z_ℓ-lattice with G_{L,S}-action,
A_v = M(−1) at v ∉ S, D_v = Frob_v − 1 on A_v, R_A the families (a_v) tending to zero, D = (D_v).
- F.1: the localization triangle RΓ_cts(G_{L,S}, M) → RΓ_cts(G_L, M) → [R_A → R_A][−1]. The twist (−1) and the shift
  come from purity at each closed point (support complex M_n(−1)[−2], Milne II; cited by the return).
- F.2: 0 → coker(lim P_n → lim E_n) → lim¹ H¹(G_L, M/ℓⁿ) → lim¹ P_n → 0, with
  lim¹ P_n = (R_A ∩ ∏ D_v A_v) / D R_A.
- F.3: lim¹ H¹(G_L, M/ℓⁿ) = 0 ⟺ the tower P_n is Mittag-Leffler ⟺ the valuations of the non-zero Smith entries of
  the D_v are bounded ⟺ the groups H⁰(F_v, A_v ⊗ Q_ℓ/Z_ℓ) modulo their divisible parts have bounded orders.
- What I checked beyond following it: (F.2.2) is closure(im D)/im D inside R_A (truncate a family to finitely many
  places); it is torsion-free (if ℓz = Da with a → 0 then z = D(a′) with a′ → 0, using that ker D_v is saturated);
  the step "bounded exponents kill the left term" uses that H²_cts(G_{L,S}, M) is a finitely generated Z_ℓ-module,
  which the return proves inside F.3. The LM7 reviewer read statements only, so this reading is the first of the
  proof; it is not a referee's check.

**(b) A corollary. Proved here, given F.3.** *lim¹ H¹(G_L, M/ℓⁿ) = 0 if and only if G_L acts on M(−1) through a finite
group.* Proof. If the image is finite, only finitely many matrices Frob_v − 1 occur up to conjugacy, so the
valuations are bounded. If the image ρ(G_L) ⊂ GL(M(−1)) is infinite, then for every n the open subgroup of elements
≡ 1 mod ℓⁿ is infinite; pick g ≠ 1 in it and m with g ≢ 1 mod ℓ^m. The set of elements ≡ 1 mod ℓⁿ and ≢ 1 mod ℓ^m is
open, closed and conjugation-invariant, so by Chebotarev it contains Frobenius elements; for those D_v ≠ 0 and every
non-zero Smith entry has valuation ≥ n. ∎ It agrees with F.5 of the return (Z₃(1), Z₃(1)[D], W: finite image, no
class; T, V, 𝒦, Λ²V: infinite image, a class) and with F.4 (Z₃(1)² against Z₃(1) ⊕ Z₃(2)).

**(c) The other properties.**

| Statement | Status |
|---|---|
| E.32: H²_cts(G_Q, Z₃(2)) ≅ ℛ/dℛ, d = diag(q − 1); a pair of Kummer classes has a class-two section iff the corrections c_q are integral and tend to zero | Claimed (LM7); statement read here; the predecessor read the proof |
| LM8 F.15: H¹_cts(G, lim P_n) → lim H¹_cts(G, P_n) is onto always and bijective when the P_n are compact | Claimed; the proof of both parts read here and it is correct as written; also followed by the intake |
| LM8 F.21: the same as E.32 at 5, with the class obstructing an actual pair of sections | Claimed; statement read here; proof followed by the intake |
| The class survives every finite extension (PUSH C.7) | Claimed; proof read here: the phantom group is torsion-free and cor ∘ res is multiplication by the degree. Correct given the residue presentation |
| Sizes do not determine the class (PUSH F.4) | Claimed; proof read here; correct given F.3 |
| No total evaluator from finite data (PUSH A.11, A.12) | Claimed; not read |
| Jannsen's sequence 0 → lim¹ H¹ → H²_cts → lim H² → 0 | Used by the returns (Jannsen, Prop. 1.6 and Thm 2.2, as they cite it); not opened |

**(d) Descent along the cyclotomic tower (the LM7 reviewer's proposal). The finite-level identity is proved here from
two standard inputs; the limit statement is open.** Let Δ₃ = G_{Q(μ_{3^∞})} and Γ = Gal(Q(μ_{3^∞})/Q) ≅ Z₃^×. Inputs
(not opened): cd₃ Δ₃ ≤ 1 (Serre, CG II §3.3); cd₃ Γ = 1. Then in the Hochschild–Serre sequence for a finite
3-primary M_n only E₂^{1,1} survives in degree two: H²(G_Q, M_n) = H¹(Γ, H¹(Δ₃, M_n)), the Γ-coinvariants of
X_n = H¹(Δ₃, M_n). Open, to be written out: with X = lim X_n, H²_cts(G_Q, M) = X/(γ − 1)X, and the phantom group
of (a) is closure((γ − 1)X)/(γ − 1)X, non-zero because X is not finitely generated over Z₃[[Γ]] when all
ramification is allowed. Test: item 3 of section 7.

**(e) Correction to Revision 3, (b), "S7 moves".** Revision 3 said that because compact towers have no lim¹, the
wall S7 is not of framework 2. The precise picture, from F.15 as read and from the LM7 reviewer's reply:
- Along the nilpotency tower of a pro-ℓ group there is no lim¹: a compatible family of section classes is a section
  class (F.15, compact case).
- Inside each nilpotency class r, the obstruction group H²_cts(G_Q, gr_r) carries a lim¹ over the coefficient tower
  ℓⁿ with unrestricted ramification (E.32 at r = 2; LM7 E.44 at every r ≥ 3, claimed; known to me through the LM7 reviewer's talk). It removes
  candidate sections with infinitely many ramified primes, and it is the obstruction to actual sections (F.21,
  PUSH A.4).
- With ramification in a fixed finite S nothing of this kind occurs (LM8 F.20, LM7 E.34).
- So framework 2 is part of S7 at every layer. What is left of the wall beyond it is selection at finite depth
  (LM7 E.38, E.43; PUSH at 17) and the non-final family of quotients (2.4 below).

### 2.3 Derived colimits over an index (framework 1)

| Statement | Status |
|---|---|
| C_δ is total, and T₁(Q_R) ≅ R for every ring R ≠ 0 (TOTAL_EXACT_2 A.24, A.30–A.34) | Claimed; the proof was followed by the intake (effort high); not refereed by the expert |
| lim^i over A^op of Hom(M, R/Z) = Hom(T_i(M), R/Z) | Proved (intake; rechecked by the Dérivateurs expert; standard) |
| For an order class, Aut of the Fraïssé limit is extremely amenable iff the class is Ramsey | **Proved (Kechris–Pestov–Todorcevic)**, statement read |
| Aut of a Fraïssé structure is amenable iff its age has the convex Ramsey property, also in the form with finitely many colourings and any ε | **Proved (Moore)**, theorem read |
| Hrushovski's sparse graphs: Aut(M₀) and Aut(M_F) are not amenable and have no precompact Ramsey expansion; the same for general predimension constructions under minor non-triviality | **Proved (Evans–Hubička–Nešetřil 1801.01165)**, statements read. This is the paper Revision 3 meant. 1705.02379 is a different one |
| Aut(M_δ) is not amenable | Derived twice independently from A.18 (the intake's direct argument, checked by the Dérivateurs expert; here, by a minimax and Moore's condition with two colourings). Unrefereed; A.18 itself is claimed. Moore's theorem is for Fraïssé structures, so the second route needs the closed embeddings made into embeddings by an expansion of the language |
| FI (finite sets, injections) is Q-exact and F_p-exact for no p | Derived three times independently (shape-map agent, Dérivateurs expert, here by L1 below); by hand, no second reader outside the three |

**Proved here (short).**
- **L1.** If an object B of A has an automorphism σ of prime order p and ⟨σ⟩ acts freely on every A(B, C) (true when
  arrows are monic), then colim_A is not exact on functors to F_p-spaces. Proof: with P = F_p[A(B, −)], the sequence
  P → P → P with maps 1 + σ* + … + σ*^{p−1} and 1 − σ* is exact at the middle objectwise (free F_p[C_p]-modules), and
  its colimit is F_p → F_p → F_p with both maps zero. ∎ So a Z-exact age consists of rigid structures, as an
  extremely amenable group forces. The unordered form of C_δ fails at p = 2 and 3 for this reason alone.
- **L2.** If the age has the extension property for partial automorphisms (EPPA), every finite family of parallel
  arrows α_i: a → b has a rational affine equalizer: take c ⊇ b in which every partial automorphism of b extends,
  and β = the average over Aut(c) of g ∘ (b ⊂ c); then β α_i = β α_1 for all i. With Isbell–Mitchell's criterion over
  Q (not opened) the age is Q-exact. EPPA also gives amenability (Kechris–Rosendal, as cited by EHN; not opened).
- **L3. The age K_E of finite linear orders with an equivalence relation is not exact over Z, nor over any ring in
  which 2 is not invertible.** Let b be two inequivalent points x < y and c be x₁ < y₁ < x₂ < y₂ with the x's
  equivalent and the y's equivalent. Among the four arrows b → c take α₁ = (x₁, y₁) and α₄ = (y₁, x₂). For d in K_E
  choose a linear order ≺ on its classes and put f(u, v) = 1 if the class of u precedes that of v, else 0. For
  every g: c → d, f(gα₁) + f(gα₄) = 1. So for β = Σ n_j g_j with Σ n_j = 1: f(βα₁) + f(βα₄) = 1, and βα₁ = βα₄
  would give 2 f(βα₁) = 1. Hence no affine equalizer; and directly, for D: P_c → P_b, g ↦ gα₁ − gα₄, the kernel
  has no element of augmentation 1, so colim does not preserve the exactness of ker D → P_c → P_b. ∎ K_E is rigid;
  its group is amenable and not extremely amenable (from memory of the Kechris–Pestov–Todorcevic theory: the
  universal minimal flow is the space of orderings of the classes). Over Q an equalizer exists by averaging two
  equalizers of the Ramsey expansion with opposite class orders (sketch, not written out).
  - This is the candidate the Dérivateurs expert named as the test of C1 ("exact ⟺ every diagram of non-empty
    compact Hausdorff spaces has a point"): it does not refute C1.
  - It is a rigid, amenable age that is not Z-exact, the case the intake asked for. Its failure is at the prime 2
    only (the two orders of a pair of classes), not a closing gap.

### 2.4 Pro-p against profinite (framework 4)

- LM8 A.22 (claimed; re-derived by the intake): the involution comes from an idempotent e of Z₅[ζ₃][[·]], a
  component of the completed group algebra of the abelianization on which x, y act through characters of order 3;
  e maps to 0 in every pro-ℓ quotient.
- LM4 D.26–D.30 (claimed; report only): a torsion-free extension of F̂₃ by C₂ whose multiplier is −1 at the prime 3
  and +1 at the others (Haran's example, realized with a type (0,4) marking), and a genus-2 analogue. LM4's report
  also gives an endomorphism of F̂₂ (x ↦ x, y ↦ wyw⁻¹) that is the identity on the abelianization, hence an
  automorphism of every maximal pro-p quotient, with image of order 3 in a quotient A₅.
- LM8 G.20 (open in the return): with R the kernel of π → ∏_ℓ P_ℓ, the remaining statement is R^{s(Δ)} = 1.
- **The form of the failure.** Three readings agree (the intake, the LM7 reviewer, this one): the family of
  maximal pro-ℓ quotients is not final among the finite quotients; the missing part is a direct summand indexed by
  pairs (ℓ, χ) with χ a character of order prime to ℓ, or a sign in ∏_ℓ{±1} modulo the diagonal. It is a
  degree-zero failure, visible in one finite quotient (order 75; 18; A₅). A first-derived object enters only for
  sections: the sections of Π with a given image in Π/N, N = ker(π̄ → ∏_ℓ π̄^{(ℓ)}), are governed by the non-abelian
  H¹(G_Q, N) twisted by the section (the shape-map agent's reading; both hold, of different objects).

### 2.5 The Galois part, towers of spaces, arithmetic topology

| Statement | Status |
|---|---|
| LM8 E.10–E.11: the limit of the sheaf topoi of shrinking punctured discs is empty; the covering germ is BZ and its fibre functors are the tangent rays | Claimed; proof followed by the intake |
| A tower (A_n) is a sheaf on N with the down-set topology; with j: N → N ∪ {∞} (∞ closed, its only neighbourhood the whole space), i*Rj_*A = R lim A and Cone(j_!A → Rj_*A) = i_* R lim A. So lim¹ is H¹ of v35's boundary defect at the point at infinity of the tower | **Proved here** (the stalk of R^q j_* at ∞ is H^q(N; A) = lim^q) |
| For Γ = Z acting on M through γ: M^{hΓ} = fib(1 − γ) and M_{hΓ} = cofib(1 − γ) = M^{hΓ}[1] | Standard (the two-term complex) |
| Tate complex: B(M)^∨ ≃ B(M^∨)[−1] (Revision 2, A2) | The predecessor's proof; re-read, correct for finite G and finite M |
| Artin–Verdier duality on the site of abelian extensions | Reported by Connes–Consani as a private communication of Gabber (line 415); no proof in the paper |
| Arithmetic Chern–Simons with boundary | Kim: X_S is treated as a 3-manifold whose boundary is a union of tori, one per prime of S; a 3-cocycle gives a (1/n)Z/Z-torsor over the local data, which the paper presents as the arithmetic counterpart of the Chern–Simons line bundle (abstract and §"boundaries", read). A bulk-and-boundary form of framework 2 exists in the literature, for finite coefficients and finite S |
| Homotopy fixed points and rational points | Harpaz–Schlank: the étale homotopy type over K with its Galois action, and a notion of homotopy fixed points, give obstructions to rational points (abstract, read) |

### 2.6 Renormalization, motives, moonshine, Teichmüller (S1, H1, B1, B8)

| Link | What the source says | Effect |
|---|---|---|
| Perelman's entropy and the central charge | Tseytlin (abstract): to one loop the σ-model RG flow is Ricci flow and Perelman's functional is the metric–dilaton action extremized in the dilaton; a generalization to all orders equals minus the central charge at fixed points | B8's first sentence is confirmed from the source |
| Two quantizations in AdS | Klebanov–Witten: in a range of masses both falloffs z^{Δ₊} and z^{Δ₋} give consistent theories (lines 577–608) | Confirms the source fact behind "alternative quantization"; the j_! ↔ j_* reading stays a statement to prove |
| Brown | MT(Z) is spanned by the motivic π₁ of P¹ minus three points; the motivic ζ(n₁,…,n_r) with n_i ∈ {2,3} are a basis (abstract, main theorem) | Confirmed |
| Connes–Marcolli | U* is non-canonically isomorphic to the motivic Galois group of mixed Tate motives over the 4-cyclotomic integers Z[i][1/2], and equally over Z[ζ₃][1/3]; they say it is premature to relate the two categories directly (Props `SNmotives`, `motgal`, read) | **Correction** to the card and to 1b, H1: the identification does not single out Z[i][1/2] |
| Brown–Schnetz | Counterexamples to Kontsevich's point-count conjecture inside φ⁴: for a graph with 8 loops the count is given modulo pq² by a modular form of a singular K3. They leave open that the piece of the motive carrying the period could still be mixed Tate (line 1702) | **Correction** to Revision 2 ("known: it fails for φ⁴"): what is proved concerns point counts of the graph hypersurface. That the period is not a multiple zeta value is not proved there. The statement "the cosmic Galois action of φ⁴ factors through MT(Z)" is open, with this evidence against |
| Cheng–Duncan–Harvey | For A₄⁶: G = GL₂(5)/2, Ḡ = PGL₂(5) (table, read) | B1's second line confirmed |
| Bakalov–Kirillov | The set of ways to glue a surface from spheres with holes, with a finite list of moves and relations, is a connected and simply connected 2-complex (abstract) | **Correction** to the card's wording. This is the two-level principle as a theorem: finite levels determine the tower because π₀ and π₁ of that complex vanish. It is a case where the lowest-degree class is zero |

Links whose sources I did not reopen keep the predecessor's status: Navier–Stokes (Revisions 1, 1a), the
Andrews–Connes–La Gatta rows (B3–B5), the sum-of-squares row (H3, A1), H4, H5, H8, G, B4, B6.

## 3. Step 1: the obstruction in each framework, as a 't Hooft-type class

**The template, from the sources of 2.1.** (i) A "symmetry": a group or category acting on the stage-wise
solutions, or acting on an object only up to its inner automorphisms. (ii) The obstruction to an honest (global,
invariant, on-site) realization, a class one degree up in a group of invertible objects: H²(G, U(1)) for a
projective representation, H³(G, U(1)) for a chain (Kapustin–Sopenko), a torsor, a line, a central extension.
(iii) Matching: the class does not change along the deformations allowed. (iv) Only then: the object one dimension
up of which the class is the boundary value.

| Framework | (i) The symmetry and the data to make global | (ii) The class and its group | (iii) Matching | Status |
|---|---|---|---|---|
| **Coefficient tower** (E.32, F.21, PUSH A.4) | G_Q acting through an abelian-level section s₁; to lift s₁ through the central extension by M = gr_r. After 2.2 (d): Γ = Gal(Q(μ_{3^∞})/Q) acting on the torsor of lifts over Q(μ_{3^∞}), which is non-empty | s₁*[extension] ∈ H²_cts(G_Q, M) = H¹(Γ, H¹(Δ₃, M)): classes of M-gerbes on BG_Q, or of torsors on BΓ. The phantom part is lim¹ = closure(im)/im | Zero at every finite coefficient level and at every place. Invariant under finite extension of the field (C.7) and under commensurable change of lattice (F.5). Not invariant under bounding the ramification: with finite S it is zero. Non-zero iff G acts on M(−1) through an infinite group (2.2 b) | Claimed, with the proofs read as in 2.2 |
| **Index category** (C_δ) | The arrows of A; by A.33, G = Aut(M_δ) with its open subgroups. Data: a compatible family in an A^op-diagram of compact groups or compact convex sets | T₁(M) = H₁(A; M), dually lim¹ over A^op = classes of families of torsors with every fibre trivial. For C_δ: T₁(Q_R) = R | The same class over every ring R ≠ 0 (A.3), and an ℓ¹-gap ≥ 1 at every object (A.18): matching in the strongest form. There is no passage to a limit in it: "objectwise to global" (shape-map agent, round 2) | Claimed; proof followed by the intake |
| **Sections** (S7) | The outer action G_k → Out(π̄). A section is a lift to an honest action; a rational point is a fixed point and gives one; a cusp gives one for each tangent direction | Layer by layer, classes in H²(G_k, gr_r π̄); in homotopy terms, the obstructions to homotopy fixed points of the étale homotopy type, in H^{n+1}(G_k, π_n) | Being geometric descends from a finite extension (standard, not opened). The lim¹ part of each layer matches as in the first row | The 't Hooft form is a restatement, **proved here** as such (a section of Π = Aut(π̄) ×_{Out} G_k is a lift of the outer action, π̄ being centre-free). The homotopy-fixed-point form: Harpaz–Schlank, abstract only |
| **Half-chains** (B7) | G acting by locality-preserving automorphisms | [ω] ∈ H³(G, U(1)) | Independent of the Hamiltonian | Proved (Kapustin–Sopenko) |
| **Pro-p against profinite** | A family of pro-ℓ data, one for each ℓ, to be the image of one profinite datum | For elements and automorphisms: none; a summand (ℓ, χ ≠ 1) or a sign in ∏_ℓ{±1}/{±1}. For sections: H¹(G_Q, N) twisted. For LM4's involutions: the obstruction to lifting an outer C₂-action to an involution | Visible in one finite quotient | Claimed (LM8, LM4); the form as in 2.4 |
| **Integral against rational** | A rational class to be integral | Ext¹ and Tor₁: the Bockstein of 0 → Z → Q → Q/Z → 0. In the home field the same split appears: the classifying group of Freed–Hopkins is a torsion subgroup | — | Standard |
| **The real place** (E.25, E.18) | Complex conjugation | (−1, −1) ∈ H²(C₂, ·), non-zero at ∞ and at 2 | A finite-level class | Proved in 1b, with the card's correction |
| **The Galois part** (E.10–E.11) | Local monodromy Ẑ(1), with G_k acting through χ | No obstruction class: the limit topos is empty by a covering argument. The fibre functors of the covering germ form a torsor under Ẑ(1); over k the sections at a rational cusp form a torsor under H¹(G_k, Ẑ(1)) = (k^×)^∧ | — | Claimed. For chains the same fact is a lim¹ (EXIT reviewer and shape-map agent, round 2) |
| **Weil positivity, λ → ∞** | The scaling action θ, which moves the window | None found for positivity: it passes to the limit (Revision 2, B3). On the spectral side the zeros are the spectrum of scaling on an H¹ (Connes–Consani, as read in 1b) | — | As in Revision 2 |
| **Navier–Stokes force budget** | Parabolic scaling, broken slowly by h | None found by the Proj¹ route (Revision 2, A3) | — | As in Revision 2 |
| **Sum of squares after descent** | The deck group of the phase cover | None: averaging kills H¹; the certificate lies in another isotypic part | — | As in 1b, A1 |

**"First-derived", "invisible to sizes".** I adopt the amendments the conference reached (intake, round 1;
shape-map agent, round 2): the class is the lowest non-zero degree of the cone of the comparison between the
underived and the derived functor; over a tower, or for a module of projective dimension one, that degree is one.
"Invisible to sizes" is two statements: bounded size kills the class (A.20; F.3; a finite S), and the sizes of the
stages do not determine it (PUSH F.4). The 't Hooft template has the same feature: which H^{n+2}(G, π_n) carries the
first obstruction depends on which homotopy group of the automorphisms is the first non-trivial one.

## 4. The conjecture about the shape, at the precision stated

The user's conjecture has two halves: a potential resolution is shaped like anomaly inflow; the obstruction is
shaped like a violation of Poincaré invariance, with discrete and smooth meeting through infinity. Below, for each
half, the precise analogues found, each with status and test. Nothing here raises the conjecture to a claim.

### 4.1 The obstruction half: a symmetry broken by a direction at infinity

| Analogue | Precise statement | Status | Test |
|---|---|---|---|
| **Spontaneous breaking: Bost–Connes** | For β > 1 the extremal KMS_β states are a torsor under Ẑ^× = Gal(Q^ab/Q), indexed by the embeddings Q^ab → C; for β ≤ 1 the state is unique | Bost–Connes 1995, not opened; as on the card | — |
| **The same torsor three times** | Embeddings Q^ab → C correspond, Ẑ^×-equivariantly, to topological generators of Ẑ(1) (send σ to the system σ⁻¹(e^{2πi/n})). So the extremal states of Bost–Connes, the orientations of the inertia Ẑ(1) at a cusp, and the restriction to Q^ab of Grothendieck's identification of a discretification with an archimedean valuation (cote 140-2, scan 378) are one torsor. Complex conjugation acts on it by −1 | **Proved here** (one line), given Bost–Connes | Write it out with the Galois action on tangential base points (ours, small) |
| **The tangential base point** | For a section s of the pro-3 group N ⋊ G_Q: the centralizer of s(Ker χ) in N is the inertia group of a unique cusp if s is cuspidal and trivial otherwise (PUSH B.4; CYCLOTOMIC C10; Grothendieck, cote 140-4). The unbroken subgroup is Ker χ, and the quotient Ẑ^× acts on the direction by scaling | Claimed (two returns); statements only | Full profinite form: LM8 G.20 |
| **Continuous against finite symmetry in E.32** | The phantom class exists iff G acts on the direction-twisted module M(−1) through an infinite group; D_v = Frob_v − 1 acts on M(−1), the twist being the inertia Ẑ(1), that is the module of directions at the prime | **Proved here given F.3** (2.2 b); the twist is purity (F.1) | The referee's reading of F.3 |
| **Almost invariant vectors** | For a unitary representation without invariant vectors, the 1-coboundaries are closed iff there are no almost invariant vectors (Guichardet, not opened). For time translations on the orthogonal complement of the vacuum: a mass gap ⟺ H¹ of the translation group is Hausdorff. So "no gap" is a class of the form closure(im)/im for the translation group itself, the form of 2.2 (d) | Standard, from memory; the link to B2 is **mine** | Open the source; state it for the Osterwalder–Schrader Hamiltonian of section 5 |
| **Index categories** | Exactness follows from extreme amenability (every flow has a fixed point). For C_δ there is not even an invariant measure. In the sparse-graph case the flow without invariant measure is the space of orientations of the graph, and a point of the universal minimal flow has an extremely amenable stabilizer when a precompact Ramsey expansion exists (KPT; EHN) | Proved in the sources for graphs; for C_δ derived from A.18 | Item 1 of section 7 |
| **Yang–Mills** | Section 5: the committee's assessment names the breaking of Euclidean symmetry by the lattice, and its possible spontaneous breaking in the limit state, decided by a flux at infinity | Read in the assessment | Section 5 |

Where the route was checked and the half does not apply: the mixed-prime rows (no symmetry is broken; a family is not
final), the sum-of-squares row, the integral-against-rational rows.

### 4.2 The resolution half: an object one dimension up

| Framework | The object, where one exists | Status | Test |
|---|---|---|---|
| Coefficient tower | (a) R lim, where the class is an honest class: Milnor, Jannsen. (b) The point at infinity of the tower: lim¹ = H¹(i*Rj_*) (2.5). (c) The cyclotomic direction: the problem is unobstructed over Q(μ_{3^∞}) and the class is H¹ along BΓ (2.2 d). (d) The residue presentation: H¹ over the Frobenius circles of the stalks M(−1)[−2] (F.1) | (a), (b) proved; (c) proved at finite level, open in the limit; (d) claimed, read | Item 3 of section 7 |
| Index category | L colim. Candidate in the shape of 4.1: a Ramsey expansion A* → A (a choice of order or orientation), over which colimits are exact; T₁ over A would then be computed from the comma categories of A* → A | The candidate is **speculation** | Item 1 (e) of section 7 |
| Sections | The homotopy fixed points of the étale homotopy type: sections are its components | Harpaz–Schlank, abstract | Restate S7's rows in those terms (ours) |
| Half-chains | The (d+1)-dimensional phase of which the chain is the edge | Else–Nayak, abstract | — |
| Type III | The crossed product by the modular flow | Witten, abstract | — |
| Mixed primes | None needed: enlarge the index to all finite quotients | 2.4 | Item 2 of section 7 |
| Weil positivity, Navier–Stokes, sums of squares | None found | Routes as in Revisions 1b and 2 | — |

### 4.3 ER = EPR: where a boundary-and-bulk or an entanglement-and-geometry form exists

- **The source statements.** Van Raamsdonk: classically connected spacetime is tied to entanglement of the
  underlying degrees of freedom, and disentangling two regions pulls them apart (abstract). Maldacena–Susskind: the
  Einstein–Rosen bridge between two black holes is created by EPR-like correlations between their microstates.
  Both are conjectures in their own field.
- **Per framework.**
  - Coefficient tower: a boundary-and-bulk form exists: Spec Z as a 3-manifold with the primes as boundary tori
    (Kim, read; Connes–Consani, read by the predecessor), and the cyclotomic direction of 2.2 (d). No
    entanglement form was found in the sources opened.
  - Half-chains: the bulk phase and its edge (Else–Nayak).
  - Type III against type II: an entanglement-and-geometry form: the entropy of the crossed-product algebra agrees
    with the generalized entropy A/4G + S_out up to a constant (CLPW, abstract).
  - Weil positivity: an entanglement form for the prolate operator (the plunge region and the logarithmic entropy
    of free fermions; Revision 2, B4, from memory); no geometric side in the parts of 2611.13129 read.
  - Yang–Mills: inflow at θ = π (section 5); nothing about entanglement in the committee's documents.
  - Index categories, mixed primes, sums of squares: none found.

## 5. Yang–Mills as a test case

### 5.1 What exists and what I opened

- The October statement (two pages) is the document the blind map read: custody, Wilson's lattice, Balaban's
  renormalization group, the continuum limit, mass gap and confinement open, 1147 pages of proof.
- Newer, beside it: the second statement of 3 November (procedure only); the **assessment of 10 November**
  (`yang-mills-group/YM`, `docs/assessment-1.pdf`, 35 pages), which contains mathematics; the Lean source, released
  on 11 November by that README's account (`yang-mills-group/OpenAI-YM-20261028`); a public outline and a 278-page draft manuscript written
  from the Lean (`scottnarmstrong/yang-mills-informalization`; README read, manuscript not read).
- The user's "two-page summary": the October statement has two pages; the assessment's first page is its summary of
  results. I read both, and Part I of the assessment (pp. 3–13).

### 5.2 What the assessment reports (its judgment; the group says it does not yet fully understand the proof)

- **Result.** A relativistic theory satisfying the Wightman axioms, constructed as a scaling limit of
  four-dimensional Wilson lattice gauge theory, for every simple compact gauge group. Not proved: uniqueness of the
  infinite-volume limit; a mass gap.
- **Ultraviolet limit at fixed volume (Thm 4.1).** Along chosen sequences of spacings a_N → 0 and volumes L_p, with
  β/log(1/a) → 11 C_g/(24π²), the renormalized lattice correlations of gauge-invariant local observables converge,
  for test functions supported away from coincident points. The proof makes the sequence Cauchy by an explicit
  renormalization-group map for the marginal terms, following Balaban, with a gauge fixing invariant under the
  lattice symmetries, and bounds on irrelevant terms that propagate.
- **Infinite volume (Thm 5.1).** Only subsequential, by Arzelà–Ascoli from bounds uniform in the volume; the input
  specific to the construction is control of the renormalized observables uniformly in the spacing.
- **Phases (§6.1–6.2).** A subsequential limit decomposes as an integral of component theories over a compact space
  with a probability measure; each component satisfies the Osterwalder–Schrader axioms with clustering and is
  reconstructed to a Wightman theory with a unique vacuum. Clustering of the mixture would make all components
  equal; it is not proved.
- **Euclidean invariance (§6.3).** The lattice leaves a finite symmetry group. Three steps: a gauge fixing that
  preserves the lattice symmetries, by averaging over symmetry-breaking choices; a divergence-free stress tensor
  with local Ward identities (the stress flux around a point generates translation, eq. 13); and a proof that the
  invariance is not spontaneously broken in the limit state, which follows if the stress-energy flux decays fast
  enough at infinity, shown by reflection positivity in several orthogonal planes.
- **Trace anomaly (Thm 7.1).** The centred trace Θ of the stress tensor has a two-point function with
  r⁸ log²(1/r) ⟨Θ Θ⟩ → 3 dim g/4: non-zero although the classical trace vanishes.
- **Open (§8).** Convergence and uniqueness of the infinite-volume limit; a probability measure for the continuum
  theory; a uniform mass gap; Wilson loops and the area law; one-particle states.

### 5.3 The obstruction there, stated precisely

1. **Ultraviolet (a → 0).** A uniform bound along the scale: S1 of the blind map, now from a source (the assessment names
   control of the renormalized observables, uniform in the spacing, as the input). Reported as achieved. No class is involved.
2. **Infrared (L → ∞).** Existence by compactness; the set of limit points is not shown to be one point. Revision 2
   (B2) said this is the size of a limit set and not a lim¹ class; the assessment's account agrees, and it settles
   what Revision 2 could not read: uniqueness is open.
3. **Symmetry.** The discretization breaks the Euclidean group to a finite group, and the question in the limit is
   whether the continuous symmetry is restored or spontaneously broken; the answer is decided by a flux through
   infinity. In this problem the user's description of the obstruction is the committee's own account of the
   difficulty, and "discrete to smooth through infinity" is the third step of §6.3.
4. **The gap (B2's "lattice gap").** For the Hamiltonian H ≥ 0 of a component theory with vacuum Ω: a mass gap ⟺ 0
   is isolated in the spectrum of H ⟺ H has closed range on Ω^⊥ ⟺ (Guichardet's criterion, 4.1) the first cohomology
   of the time-translation group with values in Ω^⊥ is Hausdorff. So the open mass-gap question is the question
   whether a class of the form closure(im)/im for the translation group vanishes. This is the precise form of B2's
   row; the assessment says the construction gives no evidence for or against a gap. (The equivalences are standard;
   the criterion was not opened.)

### 5.4 The 't Hooft form in pure Yang–Mills (Gaiotto–Kapustin–Komargodski–Seiberg), checked in the source

- **In the source.** Under θ → θ + 2π the action with a background 2-form field B for the Z_N centre symmetry
  changes by (2πi(N−1)/2N) ∫ B ∪ B. At θ = π, where CP is a symmetry, this is a mixed 't Hooft anomaly between CP
  (time reversal) and the 1-form centre symmetry; at θ = 0 there is none. By matching: if the theory at θ = π
  confines, then CP is spontaneously broken or the vacuum carries a non-trivial theory; so along θ ∈ (0, π] either
  CP breaks at π, or the gap closes, or there is a first-order transition to a topologically ordered state.
- **Inflow in the source.** The paper names anomaly inflow (Callan–Harvey) and writes an inflow action for the
  theory reduced on a circle: iπ ∫ a ∪ A ∪ B on an auxiliary four-manifold bounding the three-dimensional space. A
  five-dimensional invertible theory for the four-dimensional anomaly is not written in this paper as far as a
  search of its TeX for "five", "5d" and "bulk" shows. The (d+1)-dimensional treatment with θ as a background field
  is Córdova–Freed–Lam–Seiberg (first paper: abstract and inflow section read; the companion on four-dimensional
  gauge theories not opened).
- **Against the assessment.**
  - The construction is at θ = 0 (Wilson action), where the source says there is no mixed anomaly. So the anomaly
    neither constrains nor contradicts what was constructed.
  - The centre symmetry acts on line operators. The construction has local fields only; Wilson loops are open
    question 4. So the class cannot yet be stated for the constructed object.
  - What it gives is a constraint on the open questions in the neighbouring theory: at θ = π a unique CP-invariant
    confining vacuum with a gap is excluded. In the assessment's own structure (a measure on a space of component
    theories) this would appear as at least two components exchanged by CP.

### 5.5 Does the conjectured shape align with the committee's findings?

- **The obstruction half: yes, and literally.** The difficulty the assessment singles out for the passage from
  lattice to continuum is the violation of Euclidean (after reconstruction, Poincaré) invariance by the
  discretization, resolved in a limit state by a statement at infinity; and the open questions are about pure
  phases and uniqueness, the structure of spontaneous breaking. Caveat: here the symmetry in question is spacetime
  symmetry itself. The case shows the description is right at home; it does not test its transfer to other
  frameworks.
- **The resolution half: the summary reports no object one dimension up.** Route checked: Part I of the assessment.
  What it reports is that the would-be term vanishes: by the Ward identity the variation of a correlation under
  translation is a stress flux through a surface, and the flux through infinity is shown to decay. The bookkeeping
  has the form of inflow (a symmetry variation equal to a boundary term one codimension up), with the outcome
  "no inflow from infinity". I did not read the Lean source or the manuscript, so this is a statement about the
  summary.
- **Where a D+1 form exists for Yang–Mills.** The θ = π anomaly with its inflow (5.4), which bears on the open
  infrared questions. The renormalization group itself works on the lattice together with the scale as an extra
  coordinate; that is the shape of S1 and of holographic renormalization on the card, and is not a statement of the
  summary (**speculation**; test: T-YM-3 below).
- **The trace anomaly** is the one anomaly the assessment reports: a symmetry of the smooth classical action
  (scale invariance) that the limit does not have, with a universal coefficient. It is the remnant of the cutoff in
  the limit. Its D+1 form in the literature is the holographic Weyl anomaly (Henningson–Skenderis, not opened), for
  conformal theories with a dual, not for pure Yang–Mills.
- **Verdict as evidence.** One half of the conjecture is confirmed in the committee's words in the one problem
  where Poincaré invariance is the actual symmetry; the other half is neither confirmed nor contradicted by the
  summary, and has a precise place to be tested: the open infrared questions, in the forms of 5.3 (4) and 5.4.

## 6. The conjecture in each problem's own context, and the global pattern

| Problem | The obstruction, precisely | Symmetry and its "direction" | One-dimension-up object | Status |
|---|---|---|---|---|
| LM7 E.32, LM8 F.21, PUSH A.4 | closure(im)/im of Frob − 1 on restricted families; equivalently (open in the limit) the non-Hausdorff part of the Γ-coinvariants | Γ = image of χ, acting by scaling on the module of directions Ẑ(1) | the cyclotomic tower; R lim | claimed, proofs read as in 2.2 |
| Sections of P¹ minus three points (S7) | lifts of the outer Galois action; per layer a class in H², with its lim¹ part; plus the non-final family across primes | G_Q; fixed points are rational points, and cusps with a tangent direction | homotopy fixed points | restatement proved; the conjecture itself open |
| C_δ (total, not exact) | T₁ = R with uniform gap | Aut(M_δ), not amenable; directions = orientations (graph case) | L colim; candidate: a Ramsey expansion | claimed; candidate is speculation |
| Half-chains | H³(G, U(1)) | G acting locally, not on-site | the bulk phase | proved in the sources |
| Yang–Mills, existence | uniform bounds in the spacing; Euclidean invariance of the limit state | Euclidean group; flux at infinity | none reported; RG scale (speculation) | assessed by the committee |
| Yang–Mills, mass gap and uniqueness | closure(im)/im for the time-translation group; pure phases | translations; at θ = π, CP and the centre | at θ = π: the inflow theory | open |
| Weil positivity | a closing gap ε_λ at a prescribed rate (Hypothesis LA); no class found for positivity | scaling θ, broken by the window | none found | open |
| Navier–Stokes budget | a uniform bound (all derivatives bounded at the terminal time); no class by the Proj¹ route | parabolic scaling, broken by h | none found | open |
| Mixed primes; sums of squares | a non-final family; a different isotypic part: degree zero | none broken | none needed | claimed / proved in 1b |
| Real place | (−1, −1), a finite-level class | complex conjugation = −1 on the torsor of 4.1 | the Tate complex | proved in 1b, Revision 2 |

**The global pattern, as it stands after the checks.**
1. Where the obstruction has been made precise, it is of one of four kinds.
   - **A. A phantom class**: the non-Hausdorff part closure(im)/im of H¹ of a one-parameter "direction" (the
     tower N, the Frobenius or cyclotomic Γ, time translations) acting without a gap. Zero at every finite stage;
     invariant along the tower; non-zero exactly when the direction acts through an infinite group without a
     uniform gap (proved for the arithmetic case given F.3; Guichardet's criterion for unitary actions). Instances:
     E.32, F.21, PUSH A.4, Z₂/Z, the mass-gap question.
   - **B. A robust class of the index**: present at every object with a uniform gap; the symmetry group is not
     amenable. Instance: C_δ. (With finite automorphism groups in the index a third, torsion, variant occurs: FI,
     K_E; lemmas L1, L3.)
   - **C. Degree zero**: the family of stages is not final, or the datum sits in another sector. Instances: mixed
     primes, sums of squares, LM7 D.13 and D.19 (LM7 reviewer).
   - **D. Honest finite-level classes**: the real place; the tame and finite-depth obstructions.
   Beside these stand the problems where only a uniform bound is missing and no class has been found
   (Navier–Stokes, Hypothesis LA, the ultraviolet limit of Yang–Mills).
2. The obstruction half of the conjecture fits kinds A and B and Yang–Mills: in each the obstruction is to an
   invariant object for a symmetry, and it is decided at infinity (the accumulation of Frobenius elements at 1; the
   universal minimal flow; the flux at infinity). It does not fit kind C, by the routes checked.
3. The resolution half has proved instances in kind A (R lim; the point at infinity of the tower; the cyclotomic
   direction at finite level) and in the home field (anomalies), a restatement for sections (homotopy fixed
   points), a candidate for kind B, and nothing for kind C, where no extra dimension is needed.
4. So the refined conjecture, in one sentence at the user's precision: *where a finite-to-limit obstruction is a
   class (kinds A and B), it is the obstruction to an invariant solution for a symmetry acting on the stage-wise
   solutions, valued one degree up along the symmetry's own direction, and adjoining that direction as a dimension
   absorbs it.* Proved instance: the coefficient tower at finite level (2.2 d). Home instance: anomaly inflow.
   Open: the limit form of 2.2 (d); kind B; the mass gap.

## 7. The tests, in order of value

1. **Exactness against amenability and Ramsey** (candidate GPT-6 Astra prompt; the conference's FRAISSE_EXACT). For
   the category A of embeddings of a Fraïssé age, prove or refute each:
   - (a) A is Z-exact if and only if every A^op-diagram of non-empty compact Hausdorff spaces has a point (the
     Dérivateurs expert's C1). Known: ⟸ (A.14). The first candidate counterexample K_E is not Z-exact (L3).
   - (b) A is Q-exact if and only if it has the Reiter property (equivalently, by Moore, Aut(M) is amenable). Known:
     EPPA ⟹ Q-exact (L2); FI and K_E are Q-exact (K_E by a sketch); BZ shows the statement needs finite hom-sets.
   - (c) A is F_p-exact if and only if it is Q-exact and p divides no index [U : G_F] of an open subgroup over a
     pointwise stabilizer of which it is a finite extension. Known: ⟹ in the cases of L1; the Dérivateurs expert's
     form of the condition.
   - (d) For K_E: is it total, and what is the category of elements for the stabilizer of a class (the expert's
     settling computation)?
   - (e) For C_δ: the comma categories of the forgetful functor from a Ramsey expansion by orientations, and T₁
     computed from them (the candidate of 4.2).
   - Inputs to cite in the prompt: Kechris–Pestov–Todorcevic; Moore's theorem with its six conditions;
     Evans–Hubička–Nešetřil 1801.01165 (non-amenability; no precompact expansion); Isbell–Mitchell.
2. **The mixed-prime section statement** (candidate GPT-6 Astra prompt; LM8_PUSH). For X = P¹ ∖ {0, 1, ∞} over Q,
   Π → G_Q, N = ker(π̄ → ∏_ℓ π̄^{(ℓ)}); Π/N is the fibre product of the Π^{(ℓ)}, so a section of Π/N is a family
   (s_ℓ). Prove or refute:
   - (M0) if s is a section of Π and every s_ℓ is the section of a rational point x_ℓ (or of a cusp), then the x_ℓ
     are all equal;
   - (M1) a section of Π with the same image in Π/N as a point or cusp section is conjugate to it; equivalently the
     twisted H¹(G_Q, N) is trivial.
   - Known and to be cited: at the abelian level there is no relation between primes, and s_ℓ^{ab} determines x_ℓ
     (elementary; checked here); pro-ℓ injectivity (Mochizuki, not opened); non-geometric pro-p sections exist for
     some curves (Hoshi, not opened), so the hypothesis is needed at each prime; LM8 A.22, G.20; LM4 D.26–D.30 and
     its A₅ endomorphism.
   - First computation (the shape-map agent's floor question Q3, made concrete): the sector (ℓ, χ) = (5, order 3).
     It is the pro-5 abelianized fundamental group of the twisted Fermat cubic a u³ = t, b v³ = 1 − t, with
     (a, b) = (x₃, 1 − x₃) modulo cubes. A point above t = x₅ exists iff x₅/x₃ and (1 − x₅)/(1 − x₃) are cubes.
     Compute the sections of that quotient lifting (s_{x₃}, s_{x₅}) for x₃ ≠ x₅.
3. **The bounded-valuation criterion and its descent form** (the referee; then a prompt item for the successor of
   LM7_PUSH).
   - The referee checks F.1–F.3 (read here without a gap found), the corollary 2.2 (b), and C.7.
   - To prove: H²_cts(G_Q, M) = X/(γ − 1)X with X = lim H¹(Δ₃, M/3ⁿ); the phantom group is the non-Hausdorff part;
     X is finitely generated over Z₃[[Γ]] when the ramification is bounded and not otherwise; the same for
     Z₅(3) (PUSH_ITEMS, F.12).
4. **The regimes as one statement** (IMPLICATIONS P5, amended). For diagrams of Banach or compact groups: over a
   directed index only kinds A and D and the Mittag-Leffler case occur; a uniform-gap class (kind B) needs a
   non-directed index; kind C is detected by empty comma categories (the Dérivateurs expert's reply). A known fact
   to cite: over N the lim¹ of countable groups is zero or uncountable (Gray; not opened).
5. **Yang–Mills** (ours; reading, not a prompt).
   - T-YM-1: in the manuscript and the Lean, locate the flux-decay step of §6.3 and write it as a boundary term at
     infinity; say which lattice symmetries are exact at finite spacing.
   - T-YM-2: state the mass gap for the Osterwalder–Schrader Hamiltonian as Hausdorffness of H¹ of time
     translations, with Guichardet's theorem opened.
   - T-YM-3: say whether the renormalization-group hierarchy of the proof has a formulation on the lattice times
     the scale direction with an evolution equation along the scale.
   - T-YM-4: at θ = π, the statement the anomaly forces on the space of component theories.
6. **The torsor of directions** (ours, small): the equivariant bijection of 4.1 written out, with tangential base
   points.
7. **v35's boundary defect on the tower** (ours, small): check that its duality theorem specializes to
   i*Rj_* = R lim and to Pontryagin duality between lim and colim.
8. **S7 in homotopy-fixed-point terms** (ours): restate the rows of the returns with Harpaz–Schlank's objects.

## 8. What Revision 4 changes in the map

- **Checked against sources:** the anomaly and inflow links, B7, the Ramsey and amenability links, Brown,
  Connes–Marcolli, Brown–Schnetz, Cheng–Duncan–Harvey, Tseytlin, Bakalov–Kirillov, Klebanov–Witten, the crossed
  product, ER = EPR, GKKS, and the Yang–Mills documents (three now, one with mathematics).
- **Corrections:** Revision 3's "S7 is not of framework 2" (2.2 e); Revision 2's "it fails for φ⁴" (2.6); the
  card's Z[i][1/2] and its wording of Bakalov–Kirillov (2.6); Revision 3's citation of Evans–Hubička–Nešetřil
  (2.3); Revision 2's "could not be read" on uniqueness of the infinite-volume limit (5.3).
- **New and proved here:** the corollary 2.2 (b); L1, L2, L3; lim¹ as the boundary defect of the tower; the torsor
  of 4.1; S7 as a lifting problem for an outer action; the finite-level descent identity.
- **New statements from sources:** the bounded-valuation criterion with its proof read; the mass gap as a
  closure(im)/im class of the translation group; the arithmetic Chern–Simons torsor as an existing
  bulk-and-boundary form; the committee's account of Euclidean invariance.
- **The central statement** now reads as in section 6, with four kinds of obstruction and the conjecture confined
  to the kinds where it has instances.
