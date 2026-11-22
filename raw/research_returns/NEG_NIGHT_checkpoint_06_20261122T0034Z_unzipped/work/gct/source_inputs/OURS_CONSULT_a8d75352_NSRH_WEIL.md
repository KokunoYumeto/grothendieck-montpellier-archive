# Consult: do the split-zero structures supply GCT_NSRH's missing Weil object, and what does Weil positivity change?

By the GCT_NSRH intake agent (Claude Opus 5.5 at effort high, a8d75352), for the main session (Claude Opus 5.5 at effort
max), 21 Nov 2026, about 17 UTC.

**What I worked from:**
- `consults/BRIEF_COMMON_20261121.md`;
- `TRANSLATION_SPLIT_ZERO_20261121.md`, §0–3 and §11–14;
- prompt 54, item 10 (`SENT/54_NEG_NIGHT_…/PROMPT.md`, lines 129–145);
- my four GCT_NSRH intakes (`field_experts/intake_20261121/intakes/GCT_NSRH/`, parts 1–4 and cp03). The GCT_NSRH finding ids
  below (F…) are the run's; the run was GPT-6 Astra (ChatGPT Pro mode), effort not exposed.

**Computations:** `consult_checks.py`, in my scratchpad
(`C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\scripts\`).
The scratchpad is not durable; copy the script if it is needed.

**Status marks:**
- [standard]: a known fact, with a citation;
- [run]: a GCT_NSRH finding, with the check my intake gave it;
- [proved here];
- [computed] (by the script above);
- [open].

## Q1. What GCT_NSRH lacked, and the two candidates

### The missing object, stated exactly

GCT_NSRH's sign-only criterion is F03, refined in F04, F17, F24 and F32; my intake confirmed it [run, checked]. It proves
purity of a spectrum A from a trace system t_n on A^d(F_{q^n}) with three properties:
- (S1) a pointwise bound |t_n(x)| ≤ B·q^{na/2};
- (S2) an opposite path-output sign at an unbounded set of even path lengths;
- (S3) a bounded dual system.

F50 [run; my intake confirmed it with a full recomputation] shows that (S2) can always be produced. Encode any finite Weil
space C as J_ψ(C) = 𝓛_ψ(x²) ⊗ (C ⊗ G_ψ^∨)[1]. Then (S1) together with (S3) is equivalent to the purity of C itself. So the
criterion has force only on a trace system whose stalk weights are known independently of its cohomology.

**The "finite Weil object" of prompt 54, item 10(b), is this.** It is a finite-dimensional ℓ-adic space V with a Frobenius
F and endomorphisms E₁, …, E_{r−1} satisfying the defining relations of the nonstandard Hecke algebra Ȟ_r (GCT IV,
Def. 11.1), such that for every word w and every extension degree n,

  Tr(w(E)·F^n | V) = Tr_M(w(P))|_{v = q^{n/2}},

with the right side the actual trace on the nonstandard tensor module M (F26's "exact comparison"). GCT_NSRH proved that
**no such object exists**:
- **F42** [run, checked]: Tr(P₁^k) = 40·D^k, with D = (v + v^{−1})². At v = q^{n/2} this has 2k + 1 distinct roots q^{(k−j)n}.
  One finite F has finitely many eigenvalues, so it cannot carry unbounded k, even with scalar, sign or Tate shifts.
- **F26** [run, checked]: the normalized trace 24 + 16/D² is not a finite exponential polynomial in n.
- **F48, F51–F55** [run, statement level]: even "retuned" algebraic families F(v) with Spec F(b^n) = Spec F(b)^n are forced to
  monomial spectra, so they cannot have the nonsemisimple nonstandard algebra as their full Frobenius centralizer.

**What survives** [run]:
- word-dependent objects (F45: a Chow motive K_w on products of P¹ for each word, with trace T_w(q^{n/2}));
- fixed-parameter objects (F46, F48: v = q^{1/2} fixed, Frobenius not retuned with n);
- completed objects with unbounded cohomology (F35, F41).

**"PH1 beyond rank three"**, in the sense the run reached, is this:
- strict positivity of the named generators fails from rank four on a simple module (F57), with cell compatibility (F58),
  and under iterated tensor products (F67);
- for algebra words in the C⊗C cone it also fails at rank four (my INT-NSRH-4, computed in my intake part 3);
- only IV's and VIII's signed/factored forms (±(v − v^{−1})^a f with f positive) remain open there.
- The homogeneous Ehrhart PH1 of GCT VI is refuted separately (Kahle–Michałek, Thm. 5; F34) [standard; run].

### Candidate (i): the separated zeta sheet Σ_J (N(J) + 1)^{−s} of G(O_K)

**What it counts.** N(J) + 1 is the number of elements of the based quotient (O_K/J)₊ = G(O_K/J) (note, §0 and §3.7). Over a
finite field the same count is |G(F_Q)| = Q + 1 = #P¹(F_Q) [standard].

**Finding Q1-i-a [proved here]: the separated sheet adds one weight-0 line, and F42 and F26 apply to it unchanged.**
- For any finite-type X/F_q, the based count is #X(F_{q^n}) + 1 = Tr(F^n | RΓ_c(X̄, Q_ℓ) ⊕ Q_ℓ). This is the
  Grothendieck–Lefschetz trace formula [standard, SGA 4½ Rapport 3.2] plus the trivial line.
- So every based-count sequence is a classical count plus the constant 1.
- If a family of based counts had a common finite Frobenius space, so would the classical counts, with one eigenvalue
  removed. F42's root count (2k + 1, unbounded) and F26's non-Laurent obstruction are unaffected by adding or removing the
  constant 1.
- So the separated sheet does not supply the missing object.

**Finding Q1-i-b [proved here; computed]: what it does see is the quantum integer.**
- D(v = Q^{1/2}) = (Q + 1)²/Q = |G(F_Q)|²/Q (`consult_checks.py`).
- So δ = [2]_v at v = √Q is the separated count of F_Q, Tate-normalized, and Tr P₁^k = 40·|G(F_Q)^{2k}|/Q^k.
- This is F45's word motive (P¹)^{2k}, written as based quotients.
- **The separated sheet reproduces the word-dependent realization; it does not unify the words.**

**Finding Q1-i-c [proved here]: no number-field GRH acts on the separated sheet's zeros.**
- Over O_K the separated sheet has no Euler product. The weight w = N + 1 is not multiplicative (note, §3.7: only w − 1 = N
  is, for the smash product).
- By the Hurwitz shift (note, §0) it is Σ_k C(−s, k)·ζ_K(s + k). For K abelian, GRH (A) controls each ζ_K(s + k), but not the
  zeros of the sum. The note's §14.4 records that RH does not put the zeros of the separated sheet on the line.
- So the "setting where GRH is a theorem" is not reached through this sheet. In any case, the nonstandard traces are
  finite-field (Tate) objects, where purity is Deligne's theorem, or trivial (F45: all eigenvalues q^j).

### Candidate (ii): G(R)-semimodule coefficients (Clifford diagrams over a Boolean skeleton)

**What they are** (note, §3.1). A G(R)-semimodule is a functor M from a finite join-semilattice L to R-modules (Clifford's
theorem). For G(R)^n, L is the Boolean lattice P([n]). Take R = Q_ℓ and add a Frobenius on every fibre, compatible with the
structure maps: this is a diagram of Weil spaces over L.

**The natural additive trace** is the Möbius sum Tr_μ(F^n | M) = Σ_{l∈L} μ_L(0, l)·Tr(F^n | M_l). On P([a]) this is
Σ_I (−1)^{|I|} Tr(F^n | M_I). This is where the sign comes from in item 10(a): the fixed locus of −1 in G(R) is the Boolean
pair, so the sign-invariant part of a diagram is its support pattern l ↦ [M_l ≠ τ]. All signs are carried by μ_L.

**Finding Q1-ii-a [proved here; computed]: VIII's signed normalization is exactly a Boolean Möbius sum of effective fibres.**
- Σ_{I⊆[a]} (−1)^{|I|} v^{a−2|I|} = (v − v^{−1})^a. This is the binomial theorem, checked for a ≤ 5.
- Hence ±(v − v^{−1})^a·f(v), with f ∈ N[v, v^{−1}], the form of GCT VIII's Conjectures 2.7 and 3.4 (and IV Remark 11.19), is
  the Möbius trace of the diagram on P([a]) whose fibre at I is the graded space with character f(v)·v^{a−2|I|}. All fibres
  are effective; the overall ± is a parity shift.
- So the split-zero coefficients are a natural home for VIII's conjectural positivity: **"f positive" becomes "the fibres of
  a Boolean diagram are effective".**
- F57's escape (the two-parity Tate complex E₊ ⊕ E₋[−1]) is the case a = 1.

**Finding Q1-ii-b [proved here]: diagrams do not escape F42.**
- A finite diagram of finite-dimensional Weil spaces has a Möbius trace that is a finite signed sum of traces. That is a
  finite exponential polynomial with a fixed finite root set.
- F42's argument (generating-function poles) applies verbatim, so no single finite diagram carries all words.
- Infinite skeletons are F35 and F41's completed route, with its dual gate.

**Finding Q1-ii-c [proved here]: the reformulation is vacuous unless the skeleton and fibres are designated.**
- Every Laurent polynomial with integer coefficients is a difference of two effective ones, so it is the Möbius trace of a
  diagram on P([1]).
- Content arises only if the skeleton P([a]), the exponent a, and the fibres are fixed by the nonstandard structure, as
  VIII's canonical basis and its cells would fix them.

**What (ii) gives for PH1 beyond rank three** [open; a precise target]. Find, for the rank-four algebra Ȟ₄, a canonical
Boolean diagram per structure constant whose skeleton exponent is VIII's a and whose fibres are effective. That is VIII's
Conjecture 3.4 restated as an effectivity statement about G(R)-semimodule coefficients. The rank-four obstructions F57,
F58, F67 and INT-NSRH-4 exclude a = 0 (strict positivity); they do not exclude a ≥ 1.

### Answer to 10(b)

| Candidate | Supplies the common finite Weil object? | What it does give |
|---|---|---|
| The classical sheet | No | It is F45 |
| The separated sheet | No (it is the classical sheet plus a weight-0 line) | — |
| The semimodule coefficients | No (F42 applies) | The coefficient category in which VIII's signed positivity reads as effectivity, at the cost of designating the Boolean skeleton |

None of them places the structure constants in a setting where number-field GRH acts: the objects are finite-field/Tate
objects throughout.

## Q2. What Weil positivity being a theorem changes for the sign-only criterion

**Status.** Weil positivity holds for ζ and for Dirichlet L-functions (A): RH ⟺ Weil's quadratic form is positive
semidefinite [standard: Weil 1952; Bombieri, "Remarks on Weil's quadratic functional", 2000]. In TRACE_DET's form (DET-16,
confirmed by my intake): the explicit-formula kernel k(t) = e^{−|t|/2}(G_ζ(e^{|t|}) − b(e^{|t|})) is of positive type.

**Finding Q2-a [proved here]: no hypothesis of F03, F24, F32 or F50 is a number-field statement.**
- (S1)–(S3) concern trace functions on A^d(F_{q^n}) and their finite or countable spectra.
- Their geometric verification uses SGA 4½ and Weil II, or nothing (F50's Gaussian case proves |g| = √q without weights).
- Weil positivity for ζ and Dirichlet L does not enter any of them, so none becomes newly checkable through it.

**Finding Q2-b [proved here]: Weil positivity is the number-field form of the sign-only mechanism itself.**
- F03's mechanism says opposite sign, then no cancellation, then the exponential rate is bounded by the remainder.
- In the number-field explicit formula, the analogue of "the positive spectral sum cannot cancel" is W(g ∗ g̃) =
  Σ_ρ |ĝ(ρ)|² ≥ 0 (TRACE_DET MAS-04, confirmed).
- The analogue of F02 (a pole at the top root) is Landau's lemma (TRACE_DET STEP6-03, statement level).
- With A, both hold for ζ and Dirichlet L.
- F32's reciprocal-finiteness theorem (a bounded visible dual forces a finite spectrum) shows where the two settings differ:
  ζ's dual ρ ↦ 1 − ρ̄ = ρ (under RH) has unbounded support. So the number-field case lies outside F32's admissible class, and
  the sign-only criterion with finite or admissible spectra cannot be applied to ζ.
- What A proves is the **positivity** half; the **finiteness** half of the GCT_NSRH criterion has no number-field
  counterpart.

**Finding Q2-c [proved here, from F08 and F12]: Weil positivity does not transfer to GCT's positivity targets.**
- GCT's targets are positivity of structure constants in a designated basis (gate E): a cone condition.
- Weil positivity is a positive semidefinite Hermitian form.
- F08 [run, checked] is the exact obstruction: a pure geometric realization with a positive definite Gram form and an
  effective integral basis can still have a negative structure constant (on two points, b₂² = 3b₂ − 2b₁).
- F12 shows that the numerical side (Gram positivity of Reynolds projectors) is already available without any RH.

**Finding Q2-d [proved here, from F14, F20, F45]: purity is never GCT_NSRH's obstruction.**
- Every realization the run found (Satake summands, word motives, Cayley Weil data) is Tate or pure by construction.
- The nonstandard "RH", in the form GCT needs it, is an effectivity statement, not an eigenvalue-size statement. No form of
  RH or GRH, number-field or function-field, supplies effectivity.

**What A does change for this line** [standard]. A-dependent complexity statements (Koiran, Bürgisser; note §12 and §14) are
a different strand, the support-from-counts mechanism, not GCT's nonstandard purity.

## Q3. Does GCT's nonstandard purity fit the shape of §11?

**Answer.** Yes, at the collision of the rank-three nonstandard algebra. That is the one place where GCT_NSRH found a
canonical positive form degenerating.

**Finding Q3-a [computed; it rests on F19 and F47 as my intake checked them].**
- The center of Ȟ₃ is locally C = R[x]/(x(x − Δ)), with Δ = z₁ − z₂ (F19; I spot-checked the R3-A model in my part 1).
- Its trace form in the basis {1, x} has Gram matrix [[2, Δ], [Δ, Δ²]] and determinant Δ².
- It is positive definite whenever Δ is real and nonzero, and of **corank one** at Δ = 0, with kernel the line spanned by x
  (`consult_checks.py`).
- F47 [run; its radical claim confirmed by my intake] says the same for representations: a positive Hermitian realization
  with self-adjoint generators kills the 4-dimensional radical M₂(εC), exactly the null direction.

**Finding Q3-b [computed]: the degeneracy divisor is on the unit circle.**
- Δ = (v − 1)²(v + 1)²(v² − v + 1)(v² + v + 1)/(v² + 1)⁴.
- Its zeros are v = ±1 (double) and the primitive cube and sixth roots of unity, all with |v| = 1.
- On the real axis v > 0, the only zero is v = 1, the fixed point of the bar involution v ↦ v^{−1}.

**The translation into the note's terms.**

| Note | GCT_NSRH |
|---|---|
| s ↦ 1 − s | the bar involution v ↦ v^{−1} |
| invariant coordinate u | D = (v + v^{−1})² |
| anti-invariant v = 2s − 1 | v − v^{−1} |
| v² = 1 + 4u | (v − v^{−1})² = D − 4 |

- Δ contains (v − v^{−1})² = D − 4: the anti-invariant squared, as in the note's §2 split.
- **The null direction is the radical line x = z₁ − z** (the square-zero ε at v = 1) of the collision center. Its "supported
  zero" is the bar-fixed point v = 1, where Ȟ₃ specializes to the diagonal symmetric-group algebra and loses its
  4-dimensional radical (my part 1, R3-A).

**The limit of the fit [proved here].**
- The unit-circle location in Q3-b is cyclotomic. The non-semisimple specializations of Hecke-type algebras lie at roots of
  unity: the zeros of Poincaré-type polynomials [standard: Gyoja–Uno].
- So it is a structural fact, not a new RH. It carries no zero to a symmetric locus beyond what the cyclotomic factors
  already give.
- The shape does not reach GCT's positivity target. The positive form here is a trace form (a Gram matrix), and F08 is
  again the gap between a positive form and positive structure constants.
- **Open:** whether the canonical bases of VIII, at rank four, carry a family of such forms whose corank-one degenerations
  sit exactly on VIII's quasi-cell refinements. That is what F58's c₀ = (v − v^{−1})² arrow suggests: the same
  anti-invariant square vanishing at v = 1. That would be the Carathéodory–Fejér shape in GCT. It is untested.

## Summary in the project's terms

- **Prompt 54, 10(b):**
  - The separated sheet: no; it adds a weight-0 line, and F42 and F26 stand.
  - The semimodule coefficients: no as a common object (F42 stands). Yes as the exact coefficient category for VIII's
    ±(v − v^{−1})^a·f: a Boolean Möbius sum of effective fibres. This gives a target for "PH1 beyond rank three" with
    a ≥ 1, which F57, F58, F67 and INT-NSRH-4 do not exclude.
- **Prompt 54, 10(a):** the sign-invariant part of the sign-only argument over G(R) is the support pattern. The sign lives in
  μ_L. Finiteness (F42) and effectivity (F08) remain the two gates.
- **Weil positivity (A):** it is the number-field form of the sign-only positivity half, and is now true for ζ and Dirichlet
  L. It enters no GCT_NSRH hypothesis and does not transfer to the cone targets (F08).
- **The §11 shape:** it fits at Ȟ₃'s collision. The trace form is corank one at v = 1; the null line is the radical x; the
  degeneracy divisor is on |v| = 1 (cyclotomic).
