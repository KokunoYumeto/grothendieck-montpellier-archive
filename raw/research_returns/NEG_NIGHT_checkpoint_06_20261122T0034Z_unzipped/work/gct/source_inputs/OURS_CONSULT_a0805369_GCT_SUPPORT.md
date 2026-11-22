# Consult: GCT read through supported and unsupported zeros, and isolation-type routes to positivity

Agent a0805369bae2ebddc: Claude Opus 5.5 at effort high, the intake agent for GCT_PLETH and ALPOGE_GCT. Written for the
main session (Claude Opus 5.5 at effort max), 21 Nov 2026, at the user's word.

**Read for this consult:**
- `consults/BRIEF_COMMON_20261121.md`;
- `TRANSLATION_SPLIT_ZERO_20261121.md`, §0 and §7-§14;
- from the ALPOGE_GCT final return (`research_returns\ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped\supplied_sources\`):
  - GCT VI (`LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`): PH0 (l. 1585-1600), Theorem `tintrosat`
    (l. 1033-1047), PH1 to PH3 (l. 1304-1497, 2763-2812);
  - Bürgisser-Ikenmeyer-Panova (`LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/main.tex`), l. 265-400.

**My earlier intakes, reused:** `field_experts\intake_20261121\intakes\ALPOGE_GCT\` and `...\GCT_PLETH\`, parts 1-4.

**Status tags:**
- [standard]: published, with locator;
- [proved here]: with the proof given in this file;
- [computed]: with the script;
- [intake]: checked in our intakes, with the check named there;
- [statement level]: a run's result that no intake has proved;
- [open].

---

## Q1. Checking the three translations

### (a) "PH1 (canonical-basis positivity) = no supported zeros (a cancellation-free formula)": correct in part, mislabelled

**What the sources say.** GCT VI separates two hypotheses.
- **PH0** (Observation `obslusztig`, l. 1585-1600): the homogeneous coordinate rings of the canonical models have
  quantizations with Kashiwara-Lusztig canonical bases. "Positivity here refers to ... its multiplicative and
  comultiplicative structure constants are nonnegative." That is canonical-basis positivity. GCT VII and VIII
  conjecture the nonstandard analogue.
- **PH1** (Hypothesis `hph1plethysmintro`, l. 1304-1330; the general form at l. 2763 onward) is the *counting*
  statement. It says three things:
  1. the stretching function is the Ehrhart quasipolynomial of a polytope P = {Ax ≤ b}, with A independent of
     (λ, π) and b *homogeneous linear* in (λ, π);
  2. the ambient dimension and the bit lengths of the entries of A are polynomial in the input;
  3. membership has a polynomial-time separation oracle.

  GCT VI states that PH0 implies PH1 for Littlewood-Richardson coefficients (l. 1609).

**The correction.** Canonical-basis positivity is PH0, not PH1. PH1 is a cancellation-free formula *of a prescribed
shape and size*.

**In split-zero terms** [proved here].

*Proposition 1.* Let f = |W| for a finite set W. In G(ℕ), the sum ⊕_{w∈W} 1 is τ if W = ∅ and a nonzero element
otherwise, because ℕ is zero-sum-free. So the value predicate (f ≠ 0) and the support predicate (≠ τ) agree: f has no
supported zeros.

*Proof.* A sum of positive integers is zero only when it is empty. ∎

So the "no supported zeros" part of PH1 holds for every #P-type formula. On its own it is weak.
- Every plethysm and Kronecker coefficient has *some* cancellation-free formula of exponential size [intake]:
  - ALPOGE_GCT P-F2: every positive rational Hilbert series is one shifted polytope count;
  - GCT_PLETH G-009 to G-011: a terminating positive polytope formula for every plethysm coefficient and every
    canonical-map image rank, with no polynomial size bound.
- PH1's content is therefore the other two parts:
  - **homogeneity.** This fails: P-K1, Kahle-Michałek Theorem 5 [intake: φ(s) recomputed for s ≤ 24]. It is repaired
    by shifted polytopes (P-F1, P-F2) [intake];
  - **polynomial size.** This is open in general. Known cases [intake, by computation]:
    - outer degree ≤ 5 (GCT_PLETH G-012, T-037, G-036);
    - varying-outer-degree families: stable hooks G-037; two-row tails with a fixed second part, G-038 to G-040
      (statement level).

**Correct translation.** PH1 = "a cancellation-free formula (no supported zeros) whose witnesses are the lattice
points of a homogeneous, polynomial-size polytope". PH0 is "no supported zeros in the structure constants of a
canonical basis". Both are dual to the ETH §6 mechanism of note §7.3. In §6 the tests are allowed to cancel, and the
counted set is arranged so that cancellation does not happen. In PH0 and PH1 the formula never cancels at all.

### (b) "Bürgisser-Ikenmeyer-Panova = no unsupported entries of the determinant's multiplicity function in the relevant range": correct only if "relevant range" means the permanent's support

**The theorem** [standard]: Bürgisser, Ikenmeyer, Panova, *No occurrence obstructions in geometric complexity theory*,
J. Amer. Math. Soc. 32 (2019), Theorem 1.1 (label `th:main`, l. 380-386 of the attached source). Let n ≥ m²⁵ and
λ ⊢ nd. If λ occurs in ℂ[Z_{n,m}], where Z_{n,m} is the orbit closure of the padded permanent X₁₁^{n−m} per_m, then λ
also occurs in ℂ[Ω_n]. The source writes Ω_n for the determinant's orbit closure, denoted Det_n at l. 269; the
reduction at l. 338-344 compares ℂ[Det_n] with ℂ[Z_{n,m}].

**In split-zero terms.**
- Write m_Z(λ) and m_D(λ) for the multiplicities in degree d, lifted to G(ℕ), with τ for "does not occur".
- BIP says: **supp(m_Z) ⊆ supp(m_D)**, for n ≥ m²⁵. Wherever the padded permanent's function is supported, the
  determinant's is supported.
- It does **not** say that m_D has no τ entries among all λ ⊢ nd with ℓ(λ) ≤ m². The determinant orbit closure has
  vanishing multiplicities there.
- An occurrence obstruction is a λ where m_Z(λ) ≠ τ and m_D(λ) = τ. BIP proves there are none, in this range.

**Correction to note §8.3:** replace "the determinant's multiplicity function has no unsupported entries there" by
"the determinant's multiplicity function has no unsupported entries on the support of the padded permanent's".

The rest of §8.3 is right. After BIP only multiplicity obstructions remain: both entries supported, values compared.
ALPOGE_GCT P-F8 [intake] adds two precise points:
- a strict inequality m_Z(λ) > m_D(λ) obstructs containment;
- the converse (from all weak inequalities to containment) is false.

In the BIP range, any multiplicity obstruction has both entries strictly positive.

### (c) "P-F57's refutation of PH2/SH/PH3 = the failure of the saturation/LP route to the support question": right about the route, wrong about the support question

**The LP route** [standard]. GCT VI, Theorem `tintrosat` (l. 1033-1047): a *saturated* integer program (P nonempty ⇒
an integer point exists, with the Ehrhart quasipolynomial strictly saturated) is solvable in polynomial time. The
flip's plan has three steps:
1. PH1 gives the polytope;
2. SH gives saturation, exactly in the "almost always" form SH(b) and up to a polynomial index in SH(a);
3. so positivity of the structure constant is decided by linear-programming feasibility of the rational polytope.

In split-zero terms, saturation says that the support of the integer count equals the support of its rational
relaxation (the monotone shadow of the relaxation), after a polynomial shift.

**What failed in P-F57** [intake: proof check of P-F57 and of P-F56 to its line 900; computations `pf57.py`, `pf30.py`,
`q4.py`].
- **The family:** f_n(s) = dim of the degree-(n/g)s SL_n-invariants of n-ary cubics. This is the plethysm ray μ = (3),
  λ = (n/g), π = det^{3/g}, with g = gcd(n,3).
- **The Fourier decomposition:** f_n(s) = Σ_ρ ρ^{−s} P_ρ(s), a sum over the poles ρ of its Hilbert series H_n(t). Its
  constituents q_r are the interpolating polynomials on the residue classes r mod L, where L is the least period.
- **What P-F56 and P-F57 prove.**
  1. The poles whose order has two-part 2^{n−1} are simple, and their Fourier component is a constant, the dyadic wave
     W_n: q_r(X) − q_{r+L/2}(X) = 2W_n(r) (P-F56d).
  2. For every c < 1/4 and all large n there is an x ≈ 2^{cn} with 2W_n(x) ≥ 2^{n⁴/24 − 2n³ − 1}, while
     f_n(x) ≤ 2^{(c/6)n⁴ + O(n³ log n)}.
  3. So at that argument the constituent q_{x+L/2}, evaluated off its own residue class, equals f_n(x) − 2W_n(x) < 0.
     By the exact definitions of GCT VI (Definitions 1.2.2, 1.2.4), p(f_n) > x and s(f_n) ≥ x.
- **In split-zero terms** [proved here, from P-F56d and P-F57]:
  - The true count f_n(x) is a small nonnegative number.
  - Written as its sum of pole contributions, it is a **near supported zero**: a sum of supported terms of modulus at
    least 2^{n⁴/24 − O(n³)} that cancel down to at most 2^{(c/6)n⁴ + O(n³ log n)}.
  - PH2 and SH(a), in GCT VI's literal form, assert that no such cancellation survives a polynomial shift: every
    constituent is individually positive at every integer argument after the shift.
  - P-F57 shows the cancellation survives up to an exponential shift.
  - PH3's failure (P-F19, P-F31) is the same phenomenon one level up: the pole that carries the cancelling wave has
    order 2^{n−1} (P-F31), and the canonical h.s.o.p. must have a member of that degree (P-F19).
- **What did not fail.**
  - P-F57 does not show that the *support* of f_n is hard. The run proves, at statement level:
    - P-F54: every allowed stretch s ≥ ⌈g(10n)²⁰⁰/n⌉ occurs, for n ≥ 33;
    - P-F62: inputs that are positive from the start and realize every stretch, still with exponential strict indices.
  - So the support question on these families has a polynomial answer, while the certificate the flip wanted fails.
    GCT VI's saturation (a positivity condition on the interpolating constituents at all integers, including off their
    own residue class) is strictly stronger than "the support of f equals the support of its relaxation beyond a
    polynomial threshold".
  - **Corrected translation:** P-F57 refutes the saturation certificate (no cancellation among pole contributions after
    a polynomial shift), and with it the LP route as GCT VI designed it. It does not refute "support = relaxed support
    beyond a polynomial threshold" on this family, which P-F54 supports at statement level.
  - The density clause SH(b), "almost always zero index", is not touched: P-F48 shows these families are exponentially
    sparse in both of GCT VI's input populations [statement level]. ALPOGE_GCT P-F63 refutes the broad, product-closed
    3.3.2(b) only under an explicit coding convention [statement level].

---

## Q2. Is there an isolation-type route to positivity or nonvanishing?

**The template** [standard].
- Valiant-Vazirani (Theoret. Comput. Sci. 47 (1986)): pairwise-independent hashing h makes |W ∩ h⁻¹(0)| = 1 with
  probability ≥ 1/(8n) for every nonempty W ⊆ {0,1}^n, so NP ⊆ RP^{⊕P}.
- Mulmuley-Vazirani-Vazirani (Combinatorica 7 (1987), the isolating lemma): random weights from [2N] make the
  minimum-weight member of any family of subsets of [N] unique, with probability ≥ 1/2.
- ETH §6 (note §7): code-structured parity rows, chosen so that no supported zero occurs on the counted set.

In each case a family of cheap tests, each of which may cancel, is chosen so that on the relevant set some test does
not cancel. That is a distance property.

### 2.1 Isolation reads the shadow, not the value [proved here]

*Proposition 2.* Let g = Σ_{t∈T} ε(t) with signs ε(t) = ±1, so T is the term set of a signed formula. Give the terms
random weights w(t) from [2|T|]. Then, with probability ≥ 1/2, the generating polynomial
G(y) = Σ_t ε(t) y^{w(t)} has a nonzero lowest coefficient whenever T ≠ ∅. So isolation decides T ≠ ∅, the monotone
shadow of note §9.1. It does not decide g = G(1) ≠ 0.

*Proof.* Apply the MVV lemma to the family of singletons {t}: the minimum weight is attained once with probability ≥ 1/2,
and its coefficient is ±1. The shadow and the value differ: the Kronecker coefficient g((1,1),(1,1),(1,1)) = 0, while
its character formula (1/2)Σ_{σ∈S₂} χ(σ)³ has the two terms 1 and −1. That is a supported zero (ALPOGE_GCT PL-07
[intake, recomputed]). ∎

So isolation applied to a *signed* GCT formula answers the wrong question. Signed formulas include:
- characters for Kronecker coefficients;
- the Weyl-alternated vector-partition formula P-F42c for plethysm;
- localization sums.

### 2.2 What a working family would have to be

There are two shapes of route.

**(A) Combinatorial.** A cancellation-free witness set: a #P formula g = |W(λ,μ,ν)| with polynomial-size, polynomially
checkable witnesses. That is PH1 without homogeneity. Given W, VV hashing supplies the family with the distance
property automatically, and positivity lands in NP. Nothing beyond the formula is needed. So for GCT the
isolation-type route *is* the positive-formula problem.
- For Kronecker coefficients this is open: "no known counting interpretation", BIP l. 403-404, citing Stanley.
- Evidence against #P formulas for nearby signed quantities: Ikenmeyer-Pak-Panova, *Positivity of the symmetric group
  characters is as hard as the polynomial time hierarchy*. They show that χ^λ(μ)², the character squared, is not in #P
  unless the polynomial hierarchy collapses. [standard; the exact theorem number should be checked before it is
  quoted; not opened here.]
- For plethysm, GCT_PLETH has such formulas in bounded outer degree and in the varying-degree families above.

**(B) Algebraic.** Random evaluation of invariants (Schwartz-Zippel), a "random point is semistable" test.
- It decides *asymptotic* positivity: whether g(sλ, sμ, sν) > 0 for some s ≥ 1, i.e. membership in the moment polytope.
  That is known to be in NP ∩ coNP (Bürgisser, Christandl, Mulmuley, Walter, *Membership in moment polytopes is in NP
  and coNP*, SIAM J. Comput. 46 (2017) [standard; locator to be checked]).
- It does not decide g at s = 1.
- The gap between the two is saturation, which is exactly what P-F57 shows to be exponential (in GCT VI's measure) on
  the cubic plethysm family.

### 2.3 Tests against the known obstructions [proved here, from cited hardness results]

*Proposition 3.* Suppose there is a family of polynomial-time tests T_h with:
- g = 0 ⇒ T_h = 0 for every h;
- g > 0 ⇒ Pr_h[T_h ≠ 0] ≥ 1/poly.

If this works for Kronecker positivity in the encoding of Ikenmeyer-Mulmuley-Walter, then NP ⊆ RP. The same holds for
plethysm positivity at fixed inner degree three.

*Proof.* Kronecker positivity is NP-hard under polynomial-time many-one reductions: Ikenmeyer, Mulmuley, Walter,
*On vanishing of Kronecker coefficients*, Comput. Complexity 26 (2017), as cited by ALPOGE_GCT P-K3, including
unary-encoded partitions. The plethysm case is Fischer-Ikenmeyer, Theorem 3.1, as cited in P-K3. Composing the reduction
with the test family gives an RP algorithm for an NP-hard problem. ∎

So an isolation route that is cheap and uniform on all inputs is excluded unless NP ⊆ RP. A working route must be
restricted to a family, as GCT's targets are:
- rectangular Kronecker coefficients;
- the BIP range;
- inner degree three with growing n.

Or it must give up uniformity.

### 2.4 Where isolation already works: the dyadic pole is the MVV argument run in reverse [proved here, as a reading of P-F30 + P-F23]

Line them up:
- **MVV:** a unique minimum-weight matching ⇒ the lowest term of the weighted determinant is ±y^{w_min} ⇒ the
  determinant polynomial is nonzero.
- **ALPOGE_GCT:**
  - P-F30 [intake: proof check of the q > 0 case; exhaustive computation for n = 3, 4 in `pf30.py`]: the extremal
    determinant order 2^{n−1} is attained by a *unique* support (the chain cubic). This is the isolation lemma.
  - P-F23 [intake: proof check]: a unique top-dimensional, generically smooth fixed component ⇒ the leading residue is
    e_Y/det(1−g | N*) ≠ 0. This is "unique minimizer ⇒ nonzero lowest coefficient".
  - P-F31 [intake]: the pole exists.
  - P-F56 and P-F57: its wave dominates every other residue.
  - At n = 4 the residue product matches Salmon's classical series, phase included [computed, `pf57.py`].

So an isolation-type argument exists, and the runs used it, in the *negative* direction: to certify cancellation (large
indices), not positivity.

**The positive analogue** [open as a general route; standard in special cases]. Positivity follows from a localization
formula when a unique fixed point, or a unique face, contributes in an extremal degree. That is the face-reduction
phenomenon for Littlewood-Richardson and branching coefficients on regular faces of the cone: Derksen-Weyman, Roth, and
Ressayre's reduction theorems [standard; exact locators to be checked, not opened here]. On such faces the multiplicity
equals a smaller one, with no cancellation.
- Inside the cone, many fixed points contribute with signs and isolation fails.
- That is also where Proposition 3 bites: a uniform cheap test there would give NP ⊆ RP.
- **The concrete route this leaves for GCT:** for the rectangular Kronecker family of prompt 52 (item 1, the core
  `TO_SEND\PRO\_staging_20261121\cores\CORE_52_GCT_POS.md`), classify the fixed components (P-F60, P-F65). Where a
  unique component carries an extremal residue, that residue certifies either a large index (as for plethysm) or, on a
  face, an exact positive value. This is item 1(a)-(b) of prompt 52.

**Summary of Q2.** A §6- or VV-type family for a GCT structure constant has to be one of three things:
- (A) a polynomial-size positive formula, which is PH1 without homogeneity, plus free hashing;
- (B) random-evaluation tests, which decide only asymptotic positivity;
- a localization formula with a unique extremal contribution, which works on faces and, in reverse, for the dyadic pole.

A uniform cheap family on all inputs is excluded unless NP ⊆ RP (Proposition 3). In note §9's language:
- isolation and VV read the monotone shadow and need a formula with no supported zeros;
- ETH §6 reads values and needs supported zeros to be absent *on the counted set*;
- GCT's signed formulas have supported zeros, so route (A) must first remove them. That is the open #P-formula problem.

---

## Q3. With A proved (and GRH beyond the abelian case via M), which of these runs' results that assumed RH or GRH are now unconditional?

Searched in my intakes and the ALPOGE_GCT complexity section (`work/complexity.tex`, read in full for C-GRH-01 to
C-GRH-03).

| Result | Its analytic input | Status now |
|---|---|---|
| ALPOGE_GCT **C-GRH-01**: the Dedekind ζ_K of every subfield of a cyclotomic field has its nontrivial zeros on Re s = 1/2 | GRH for Dirichlet L-functions, via ζ_K = ∏_χ L(s,χ) | **unconditional [A]** [intake: proof check; classical factorization, Washington, *Cyclotomic Fields*, Thm 4.3] |
| ALPOGE_GCT **C-GRH-02**: Miller's compositeness witness ≤ 2(ln m)²; units below 3(ln m)² generate (ℤ/mℤ)^× | RH and GRH for Dirichlet L-functions (Bach §6, Thms 2-3, pp. 372-373) | **unconditional [A]** [intake: proof check] |
| ALPOGE_GCT **P-F47**: the explicit prime bound p ≤ (φ(n) log n)² in the Fermat-evaluation support result | GRH for Dirichlet L-functions, through Lamzouri-Li-Soundararajan's explicit least prime in progressions | **unconditional [A]**; an unconditional polynomial version via Xylouris was already given [intake: statement level] |
| **Koiran, HN ∈ AM** (Theorem 2), as analysed in ALPOGE_GCT Q-C-KOIRAN | an effective prime ideal theorem for arbitrary number fields (Koiran §5, Thm 9, Cor. 1) | **conditional on [M]**; C-GRH-03 (x³ − 2) shows the abelian case does not suffice [intake]. Project id CX-K02. |
| **GCT V, Thm 2.10 → Thm 3.4** (an h.s.o.p. in PH) and **Thm 4.10** (EXPH for the succinct determinant variety) | Koiran's theorem | **conditional on [M]**. Thm 4.1 needs, besides, equations computable in exponential time; GRH does not remove that. |
| **Bach, Thm 4** (number-field bounds) | Hecke L-functions over general bases | **conditional on [M]** |
| GCT V's derandomization results (Thms 1.7, 4.7, 4.9, 5.11) | strengthened hitting sets and border lower bounds, not GRH | **unchanged**; no GRH involved |

**Not GRH-dependent at all:**
- GCT_PLETH: none of its findings use RH or GRH. Q-ALPOGE and Q-MASULLO stayed input gates.
- ALPOGE_GCT's whole positivity chain: P-F1 to P-F31, P-F56, P-F57, P-F60. Its purity statements (PLE-F7, P-F10) use
  Deligne's Weil II, a theorem since 1980, not RH for ζ.
- The OpenAI ETH theorem and its consequences in ALPOGE_GCT (C-SAT-01, C-COUNT-01 to 03, C-PIT-01) are a separate
  premise, not RH.

**One reading for note §14.2** [a formulation]. In these runs GRH entered only where counts had to decide support at
polynomial scale: Miller's witnesses, Bach's generators, Koiran. That is note §12's "GRH lets the B coordinate be read
off ring-side counts". The GCT positivity questions (PH0 to PH3, SH) never reduced to it. Their analytic content is
Weil-type purity (GCT VII and VIII), or the combinatorial cancellation analysed in Q1(c).
