# Intake of ALPOGE_GCT (prompt 23, "purity and plethysm: P versus NP through GCT"), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), root plus delegated agents; the run's own files say its reasoning
effort is not exposed. Work file: `agent_notes\a0805369bae2ebddc_NOTES.md` (mirror:
`agent_notes\20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md`).

## 0. Return read and scope

- Return folder: `research_returns\ALPOGE_GCT_checkpoint_01_20261120T2347Z_unzipped` (checkpoint 01, assembled
  00:47 CET on 21 Nov after about 45 minutes of work; the only ALPOGE_GCT folder present when I started). The run is
  still going: its ledger names P-F13 (fixed-embedding multigraded branching rings, generator-degree bounds) as in
  progress and unchecked. Everything below is about checkpoint 01.
- Prompt as sent: `TO_SEND\PRO\1_Archive_research_by_topic\SENT\23_ALPOGE_GCT_purity_and_plethysm\PROMPT.md` (read
  in part: the opening, the step series, the source list and the bridges list).
- **Read in full, with the proof:** P-K1 (cited), P-F1, P-F2, P-F3, P-F4, P-F5, P-F6, P-F7, P-F8 (`work/positivity.tex`);
  P-F9, P-F10, P-F11, P-F12 (`work/positivity_bounds.tex`, `positivity_modular.tex`, `positivity_ph3.tex`); PL-01 to
  PL-08 and PLE-F5, PLE-F6, PLE-F7 (`work/plethysm.tex`); C-GRH-01, C-GRH-02, C-GRH-03, C-SAT-01, C-COUNT-01
  (`work/complexity.tex`, lines 1-260).
- **Read at the level of the statement** (QUESTIONS.tsv row and state only): the bridge findings B3.x, B4.x, B5.x,
  B7.x; C-COUNT-02, C-COUNT-03, C-SIZE-01, C-PIT-01, C-SIGN-01; the cited K-theory, metric, tensor-norm and
  Hilbert/Quot material.
- Sources checked against: Mulmuley GCT VI (`supplied_sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`):
  Definition `dintropos1` (positivity index, l. 760-768), Definition `dintroposform` (positive form, l. 880-889),
  Theorem `tquasiplethysm` (= Thm 1.6.1), PH1 (`hph1plethysmintro`, l. 1304-1330), PH2 and PH3 for plethysm
  (l. 1451-1497), the remark "PH2 may also follow from PH3" (l. 3955-3962).

## 1. Verdicts on the main results (the positivity GCT can still ask for)

**P-K1, the literal homogeneous PH1 is false (cited: Kahle-Michałek, Theorem 5 and Remark 6).**
Check: computation, plus a reading of the stretching convention. I recomputed
φ(s) = p_{(4s),(3)}^{(7s,5s)}, the multiplicity of S_{(7s,5s)} in Sym^{4s}(Sym^3 C^2), as the difference of q-binomial
coefficients (Cayley-Sylvester), for s = 0..24. It equals (s + r(s))/3 with r = (3,−1,1,0,2,−2) of period 6, and
also ⌊s/3⌋ + 1_{2|s}. φ(1) = 0 and −φ(−1) = 1, which no rational polytope's Ehrhart quasi-polynomial allows (the
interior count at s = 1 would exceed the closed count). The stretch (λ, π) → (sλ, sπ) with the inner μ = (3) fixed
is exactly the convention of GCT VI, PH1 (l. 1304-1330). **Confirmed** as a statement; the KM paper itself was not
on hand, so its locator is carried as background.

**P-F1, a two-dimensional shifted polytope on that ray, minimal.** Targeted proof check, plus computation.
The generating-function identity (1+T^4)/((1−T^2)(1−T^3)) was redone by hand, the unimodular change
(a,b,z) ↦ (2a+3b+4z, a+b, z) checked, and the polytope count P_s matched φ(s) for s = 0..24. The minimality
proof (no eventually one-dimensional model in any ambient lattice: the affine hull stabilizes, the integer points
form v₀ + sw + tv, the endpoints of the t-interval are eventually affine with slope difference 1/3, and the jumps
+2 at s ≡ 5 and −1 at s ≡ 0 mod 6 exclude both cases b ≤ 1 and b > 1) was read step by step. **Confirmed.**

**P-F2, every explicit positive rational Hilbert series is one shifted polytope count.** Targeted proof check. The
selector variables e_i (one of them equals 1), the slack u with h_i values, and Σ a_j x_j = s − i count exactly
Σ h_i [T^{s−i}] ∏(1−T^{a_j})^{-1}; the polytope is bounded and of size linear in the expanded data. **Confirmed.**
It is elementary; its value is that it turns every positive form into a shifted (inhomogeneous) counting model.

**P-F9, P-F10.** Targeted proof check, **confirmed**. P-F10 (weighted plane, indices exactly ab−a−b) is the clean
statement that a fixed smooth pure geometry carries unbounded indices once the grading varies.

**P-F11, a positive rational form gives positivity index ≤ h + 128 r³ A³ (A = modular index).** Targeted proof check
of every estimate: pole orders, |1−ζ^{a}| ≥ 2 sin(π/d) ≥ 4/d, the bounds on u_a(z), the Cauchy bound
|C_{ζ,j}|/c ≤ 2D^{r−j} with D = 16rA², the comparison (**) of binomial coefficients, the total error ≤ 2/7 at
p₀ = 128 r³A³, the reduction to gcd 1, and the numerator shift. **Confirmed.** The point: the period (an lcm,
possibly exponential) is not needed; the modular index A suffices.

**P-F12, PH3 implies PH2 for the stretching families, with an explicit bound.** Targeted proof check. The lower bound
f(Lk+i₀) ≥ N_{i₀} binom(k+r−1, r−1) against the Weyl growth O(n^{d_λ}) forces r ≤ d_λ + 1 ≤ dim G + 1, and P-F11 then
bounds p(f) polynomially in dim G and A. This proves, for plethysm (GCT VI, Problem 1.1.2) and for Kronecker (Problem
1.1.1 through restriction GL_a × GL_b → GL_{ab}), what GCT VI states only as "PH2 may also follow from PH3" (l. 3962).
**Confirmed.**

**The erratum in P-F12 (PL-Q22): GCT VI, Theorem 1.6.1(d), as printed, is false.** Checked against the source:
Theorem `tquasiplethysm`(d) states a positive form (h₀ + … + h_d t^d)/∏(1−t^{a(j)})^{d(j)} with Σ d(j) = d + 1 where
d is the degree of the quasi-polynomial, h₀ = 1; Definition `dintroposform` has the same restriction. For the KM ray
(degree 1): a numerator 1 + cT over two factors needs c = 0 and both weights > 1 (φ(1) = 0), then the weights are 2 and
3 (φ(2) = φ(3) = 1, and equal weights fail at T²), and then the coefficient of T⁴ is 1, not φ(4) = 2. I redid each
step. **Confirmed.** The correct statement (Cohen-Macaulay T free over an h.s.o.p.) has an unrestricted numerator of
degree < Σ a(j). This is a genuine correction to the GCT VI text; KM do not state it in this form as far as the run's
citations show (not checked against KM itself).

**PLE-F5, PLE-F6, PLE-F7: the obstructing ray is the Hilbert function of a Kleinian quotient.** Targeted proof check
of each. The group generated by a = diag(ζ₆, ζ₆^{-1}) and b = (x,y) ↦ (iy, ix) has order 12, lies in SL₂ (both
determinants 1), so it is the binary dihedral group of order 12 and A²/Γ is the D₅ Du Val singularity
Z² = UV² + 4U⁴ (my identification; the run does not name it). The relation and invariance of U, V, Z were checked by
hand; the Hilbert series with degrees halved is (1+t⁴)/((1−t²)(1−t³)) = Σ φ(s)t^s. PLE-F6: the rescaled ray φ(qs) is
a homogeneous Ehrhart function exactly when gcd(q,6) > 1 (both constructions and the reciprocity exclusion checked).
PLE-F7: H_c of the quotient is Q_ℓ(−2) in degree 4 only, IC = Q_ℓ[2], and #X(F_Q) = Q² by the character sum
(checked). **All confirmed.** Meaning: a normal surface with rational singularities and pure even Tate cohomology (as
pure as A² itself) has the PH1-violating Hilbert function; purity cannot force homogeneous Ehrhart counting.

**P-F3 to P-F8.** Targeted proof check, **confirmed**: P-F3 (Haar projector, det(I+tP) = (1+t)^m: a positive
determinant exists for every coefficient but costs the whole Hom space), P-F4 (C₂: pointwise nonnegative virtual
character with a −1 coefficient), P-F5 (Sym²: GL₂ → GL₃ is not the block embedding), P-F6 (split Grothendieck group of
a semisimple graded category gives Z_{≥0}[v,v^{-1}] structure constants; the triangulated version does not), P-F7
(Boolean finite étale schemes: pure, smooth, proper, even Tate, and #SAT-complete), P-F8 (strict multiplicity
inequality obstructs containment; the converse fails; in the BIP no-occurrence range both multiplicities are > 0).

**PL-01 to PL-08 (archive identities).** Targeted proof check, **confirmed**; PL-07 redone (S₄, (2,2): character
(2,0,2,−1,0), cube average 1). PL-01 refutes the SA17 study's "checked" line on cote 133, scan 19 (see section 5).

**C-GRH-01, C-GRH-02, C-GRH-03, C-SAT-01, C-COUNT-01.** Targeted proof check, **confirmed**. C-GRH-01 is the classical
factorization ζ_K = ∏ L(s,χ) for abelian K (Washington, *Cyclotomic Fields*, Thm 4.3); C-GRH-03 (x³ − 2) is correct.

**Not read in full:** the B-, remaining C- findings (statement level only; no fault seen in the statements).

Counts: 33 findings checked in full and confirmed (counting the erratum separately); 0 refuted; 0 gaps; about 25 at
statement level.

## 2. What is new

- Against the literature: P-F11 and P-F12 (PH3 ⇒ PH2 with the bound p(f) < (d_λ+1)A + 128(d_λ+1)³A³) are, to my
  knowledge, not in print; GCT VI states only that PH2 "may follow" from PH3 (l. 3962). The erratum to GCT VI
  Thm 1.6.1(d) is new as an explicit statement. P-F1's minimality in an arbitrary ambient lattice extends KM
  Theorem 5 (one variable). PLE-F5 to F7 (the KM ray as the Hilbert function of the D₅ quotient, with pure cohomology)
  are new as a construction; each step is elementary. P-F2, P-F3 to P-F8, P-F9, P-F10 and PL-01 to PL-08 are short
  and elementary; some are folklore (PL-07 is a standard Kronecker example; PL-02's non-specialness agrees with
  Bouc-Rökaeus). The run makes no priority claim, rightly.
- Against tonight's other runs: GCT_PLETH found the same scan-19 counterexample (its A-001 = PL-01 here) and the same
  Witt-descent failure (A-005 = PL-08), independently. GCT_PLETH's G-009 to G-011 (terminating positive polytope
  formulas from finite presentations) are the same idea as P-F2 from the other end. The two runs agree.
- Against our own results: our bridges ledger (`reports_20261120\alpoge_rh\bridges\QUESTIONS.tsv`, Q07) has Koiran's
  HN ∈ AM as "not settled"; C-GRH-01/C-GRH-03 locate exactly why (see 3).

## 3. Scope of the two proofs

- Alpöge (Dirichlet GRH, a theorem): used by C-GRH-01 (Dedekind GRH for abelian fields) and C-GRH-02 (Miller and Bach
  rational-field witness bounds). Both within scope. No positivity finding (P-, PL-, PLE-) uses RH or GRH; the run
  says so, correctly.
- Masullo (Hecke GRH for every number field, conditional): **not used anywhere in ALPOGE_GCT**; the word does not
  occur. This leaves one consequence unstated. Koiran's HN ∈ AM needs an effective prime ideal theorem for arbitrary
  number fields (Koiran, Theorem 9 and Corollary 1). Dedekind GRH for all number fields gives it, so Masullo would give
  HN ∈ AM **conditionally**, and with it the GCT V conditional PH bound for h.s.o.p. construction (GCT V, Thm 2.10 and
  3.4). Write it as conditional on Masullo, never as a theorem.
- More than either proof (Artin, GL₂, automorphic): nothing claimed. The OpenAI "ETH is false" theorem is used as a
  supplied premise (C-SAT-01 and the C-COUNT findings); it is neither of our two proofs and should be labelled as the
  third premise wherever these findings travel.
- No statement claims more than its input gives. C-GRH-03 rightly blocks the tempting overreach (restricting HN to
  abelian solution fields).

## 4. How the findings bear on the open problems, and the attack they open

1. **The flip's positivity is now one hypothesis, PH3, plus construction.** P-K1 retires homogeneous PH1. P-F1 and P-F2
   show that shifted counting survives. P-F12 shows PH3 (small modular index) implies PH2 with an explicit polynomial
   bound. So the positivity GCT can still ask for is: (i) PH3 for the plethysm and Kronecker stretching rings
   T(a) = S^H of GCT VI Thm 1.6.1(c); (ii) a uniform construction of the positive form, in the compressed input
   (PL-Q21: the bound is in dim G, which can be exponential in the bit length of μ).
   **Attack.** The modular index of the positive form attached to an h.s.o.p. θ₁..θ_r of T is max deg θ_j. PH3 is
   therefore a degree bound for a homogeneous system of parameters of an invariant ring. That is the subject of
   Derksen-type degree bounds (H. Derksen, "Polynomial bounds for rings of invariants", Proc. AMS 129 (2001): the null
   cone is cut out by invariants of degree bounded by a polynomial in the degrees and dimension, for a reductive group
   acting linearly), and of their sharpened forms for semi-invariants (Derksen-Makam). The next step is to transport
   such a bound to T = S^H, where S is the section ring of a flag variety (not a polynomial ring), with the stretching
   grading. A positive answer gives PH3 in the expanded parameters, and with P-F12, PH2.
2. **What the exact obstacle to "purity ⇒ positivity" is.** PLE-F7 and P-F10 place it exactly. The cohomology of
   Proj T or Spec T can be as pure as affine space, while the Hilbert function still breaks PH1 and has indices as
   large as you like. Purity controls the eigenvalues of Frobenius. It does not control the grading weights. The next
   attack is to look for weight-graded positivity instead. Ask whether the stretching grading of T is the weight
   grading of a G_m-action whose fixed-point (Białynicki-Birula) decomposition is pure. Then the Hilbert series would
   be a sum of positive pieces with denominators from the tangent weights at the fixed points, and the modular index
   would be bounded by the largest tangent weight. That is a concrete PH3 route through geometry, and it is where
   Alpöge's step 8 (one order of multiplicity per theta lift) would have to act if it acts at all.
3. **The right reciprocity.** The KM ray obeys Stanley reciprocity for the Gorenstein ring T: its series satisfies
   H(1/t) = t·H(t), checked from (1+t⁴)/((1−t²)(1−t³)). It does not obey Ehrhart reciprocity. A successor statement of
   PH1 should state counting with the canonical-module reciprocity of a Cohen-Macaulay T: φ(−s) = (−1)^{dim} times the
   Hilbert function of ω_T. In Grothendieck's terms that is local duality (SGA 2, Exp. V; Hartshorne, *Local
   Cohomology*). A shifted model should be required to match it.
4. **GCT obstructions (P-F8, PL-06).** The live test is strict comparison of actual quotient multiplicities, i.e. ranks
   of H_λ for the Hadamard-Howe map. GCT_PLETH's G-011 and R-008/R-009 attack exactly this.
5. **Koiran gate.** Unconditionally open; conditionally closed by Masullo (see 3).

## 5. Integration (edits to make; none made outside this folder)

- **SA17 study** (`SA17_STUDY_cote133_lambda.md`, section "Cote 133, scans 19-29", subsection "Scan 19: λ- and
  σ-operations", the **Checked** line): replace "at order 2 the two descriptions agree ..." with: "Wrong as an
  equivariant statement. In the Burnside ring of C₂, for the free orbit E: E² = 2E, ε²(E) = 1 (2-subsets),
  σ²(E) = E + 1; the boxed 2λ²(E) + E = E² fails (fixed-point marks 2 and 0). Only the cardinality identity
  2·binom(d,2) + d = d² holds. The true identities are Sym²E ≅ ε²E ⊔ E and, for λ_t := σ_{−t}^{-1}, λ²(E) = E − 1, which
  linearizes to Λ²C[E] = sgn. Found independently by ALPOGE_GCT (PL-01) and GCT_PLETH (A-001), 21 Nov 2026; checked in
  this intake." Same file, SA17-21, "Open: the λ-ring question for his split WG(S)": add "the opposite-series Burnside
  structure is not special either (PL-02: C₂ × C₂, ψ² not multiplicative); scan 8: exterior powers do not descend to
  the Witt group (PL-08: ⟨1,−1⟩ ↦ ⟨−1⟩ over R)".
- **Reading of cote 133** (scans 19 and 8): as above. Scan 19's boxed identity is right in K₀ of vector bundles (and in
  representation rings), wrong for finite G-sets with unsigned subsets.
- **Bridges ledger** `reports_20261120\alpoge_rh\bridges\QUESTIONS.tsv`, row Q07 (Koiran): add "ALPOGE_GCT C-GRH-01:
  Alpöge gives Dedekind GRH for abelian fields only; C-GRH-03 (x³−2) shows HN needs non-abelian fields. Conditional on
  Masullo (Hecke GRH, every number field): HN ∈ AM (Koiran Thm 2). State unchanged: not settled unconditionally."
- **GCT VI erratum**: record in the GCT notes (and in a successor prompt) that Thm 1.6.1(d) and Def. `dintroposform`
  must drop "Σ d(j) = d + 1 with numerator degree d"; the KM ray is a counterexample (P-F12, PL-Q22).
- **Successor prompts.** The prompts 30-36 in `TO_SEND\PRO\1_Archive_research_by_topic\` that concern GCT positivity
  should take: PH1 is replaced by shifted counting plus Stanley reciprocity; PH3 ⇒ PH2 is proved (P-F12); the
  target is PH3 through h.s.o.p. degree bounds (item 4.1) and through weight gradings (4.2). I did not open prompts
  30-36; the main session should place this where a GCT prompt exists.

**Language of algebraic geometry.** ALPOGE_GCT does not restate P-F1, P-F2, P-F9 to P-F12 in Grothendieck's language;
its algebraic-geometry part covers only the bridges (integral group schemes, Hilbert and Quot schemes). The
translation, short: the stretching function is the Hilbert function of the graded ring T = ⊕ T_n, and Proj T is a
projective scheme with rational singularities (GCT VI 1.6.1(c)). An h.s.o.p. of degrees a_j is a finite surjective
morphism Proj T → P(a_1, …, a_r) to a weighted projective space (graded Noether normalization, EGA IV 5 / EGA II 6).
Cohen-Macaulayness makes T a free graded module over the polynomial ring on the parameters, which gives the positive
form. The modular index is the largest weight of that weighted projective space. PH3 asks for a finite projection to a
weighted projective space of polynomially bounded weights. Reciprocity is Grothendieck local duality for the
canonical module.

## 6. Prompt updates for the successor of ALPOGE_GCT

- State as settled: P-K1, P-F1, P-F2, P-F11, P-F12 and the Thm 1.6.1(d) erratum (cite this intake). Do not re-prove.
- Main question for the successor: prove PH3 for an explicit infinite family of plethysm stretching rings (for
  example two-row output, where Pak-Panova-Swanson give positive formulas, then three-row), by bounding h.s.o.p.
  degrees of T(a). Then go to the uniform construction in compressed input.
- Ask for the geometric route of 4.2 explicitly: a G_m-action whose weight grading is the stretching grading, with a
  Białynicki-Birula decomposition; compute it for the KM ray, where the D₅ quotient gives the answer.
- Ask that every positivity finding be restated in the language of graded Noether normalization, weighted projective
  spaces, canonical modules and local duality (section 5).
- Ask the run to state Masullo's conditional consequences separately (Koiran, GCT V Thm 2.10/3.4, Bach Thm 4).
- P-F13 (multigraded branching, generator degrees) is in progress: it is the right next gate and should be carried.
