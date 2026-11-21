# What Alpöge's proof suggests about our programme

By the war-game agent (Claude Fable 5.2 at effort max), 20 November 2026, written about 22:30 UTC. The result is cited
as L. Alpöge, *Remark* (alpo.ge/remark.pdf, 20 Nov 2026), with its Lean formalization.

## What I did

- 19:58–20:14 UTC: listed the note's folder and the reports folder; read `README.md`, `LEAN_SCAN_20261120.tsv` and
  the (still empty) `ALPOGE_LEAN_MAP_20261120.md`; read all four pages of `remark.pdf`; created this folder. The
  account's weekly limit stopped me there. Nothing was written before the stop.
- 22:2x UTC, this file: composed from what I hold (the note as read, the step series of the brief, my war game and
  its hunches, the intakes of 14 November). No new reading, no command, no search. I opened no Lean file; the scan
  record is the main session's (Claude Opus 5.5 at effort max).
- Two readings of the note against the brief. Page 1 and step 8 give the chain of theta lifts the length √X (the
  brief's step 0 said "about X"). The exponent of step 2 is a/p + a/p³ + …, as the brief has it: suggestion 2 below
  derives exactly that series.

**Status words.** *Proved*: an elementary argument given here, checked by me only. *Sketched*: a mechanism with its
steps, not all verified. *Proposed*: a statement to test. Everything marked (mine) is from this pass.

## The suggestions, ranked

### 1. Δ is a reciprocity defect at the primes 2 and 3, and E.3 asks whether the pentagon implies the product formula. Sketched.

- **Statement (mine).** The frame sign of an element F of GT̂₀ is a unit u(F) in (Z/12)^× = {1, 5, 7, 11} (LM7_PUSH
  E.58, E.65, refereed by Claude Opus 5.5 at effort max; Galois elements have 1 or 11, the element of E.58 has 5 or
  7). Then Δ(F) = χ₁₂(u(F)), where χ₁₂ = χ₋₄·χ₋₃ is the quadratic character of Q(√3), the real subfield of
  Q(i, ω). So Δ = ε₂ + ε₃ modulo 2, with ε₂ the bit of u modulo 4 and ε₃ its bit modulo 3: a product formula over
  the two places where the harmonic and the equianharmonic point meet. Δ = 0 on Galois is then a reciprocity law,
  and the question "is Δ = 0 on GT̂" is: does the pentagon force that product formula for frames.
- **Checked by hand.** χ₁₂(1) = χ₁₂(11) = 1, χ₁₂(5) = χ₁₂(7) = −1, which is "equal bits" against "unequal bits".
  The Hilbert symbols of the two CM fields: (−1, −3) is +1 at 2, −1 at 3, −1 at ∞ (product +1); that quaternion
  algebra is the endomorphism algebra of the supersingular curve in characteristic 3, where j = 0 and j = 1728
  coincide; in characteristic 2 it is (−1, −1). This is numerology to test, not yet an identification of ε_p with a
  Hilbert symbol.
- **Steps of the note.** 3 and 5 (Gauss sums of order #μ_K as coefficients of θ on the #μ_K-fold cover; "the
  reciprocity law of y(c·c′) vs. y(c)·y(c′)"): the cocycle of the metaplectic cover is the power reciprocity law,
  and it is trivial on rational points. The (2,3,6)-triangle group of page 2 is the quotient Ẑ[ω] ⋊ C₆ of our
  tripod group, on which GT̂₀ acts; (2,4,4) gives Ẑ[i] ⋊ C₄. Step 2 (CM curve, inert primes).
- **Meets.** Cote 145 (frames "at P and the harmonic points"), cote 143 ("structure « locale »"), LM §§46–47; the
  successor of LM7_PUSH (S.1, S.9, S.11) and ORDER5_FRAME; the user's ghosts: an element with unequal bits passes
  each local test and fails the product formula.
- **How to check.** From the definitions of E.65: prove Δ = χ₁₂ ∘ u; express ε₂, ε₃ as local symbols (Hilbert or
  Kubota) of the pair of frames; evaluate on the element of E.58. Then one item for the Δ successor: prove or
  refute that the hexagon and pentagon imply ε₂ = ε₃. It would turn E.3 into a statement the field can read.

### 2. The multiplicity of step 2 is the divided-power structure of a formal group of height 2. Proved for formal groups; its use is proposed.

- **Statement (mine).** Let F be a one-dimensional formal group of height h over W(k), t a parameter, D the invariant
  derivation, f in W[[t]]. Then v_p(D^a f(0)) ≥ v_p(a!) − a/(p^h − 1) − O(log a). For h = 2 the gain is
  a·p/(p² − 1) = a/p + a/p³ + a/p⁵ + …, the exponent of the note. For h = 1 there is no gain, which is why the
  prime must be inert.
- **Proof.** D = d/dλ for the logarithm λ, so D^a f(0) = a!·c_a where f = Σ c_a λ^a. The exponential of F has
  coefficients e_n with v_p(e_n) ≥ −n/(p^h − 1) up to a bounded term (the logarithm is t + t^q/p + t^(q²)/p² + …,
  q = p^h, in the Lubin–Tate normal form), and the series with v_p(c_a) ≥ −a/(p^h − 1) form a ring containing
  W[[t]] composed with the exponential. Legendre's formula gives v_p(a!) = (a − s_p(a))/(p − 1).
- **Steps of the note.** 2. D^p ≡ 0 there is the vanishing of the p-power map on the Lie algebra, the Hasse
  invariant.
- **Meets.** Cote 54 scans 5–7: the extension S_A as an extension of p-Lie algebras, his boxed "t_A^∨ est muni de
  la puiss. p-ième nulle", and "comparer … avec ce que donne la dualité de Cartier". The crystals (cotes 4–9; the
  letter to Tate). The divided-power line of the war game: 136–137, 16 scan 14, 47 scan 9, hunch H8. From memory:
  Katz, "Divisibilities, congruences, and Cartier duality" (1981), has this exponent for Hurwitz numbers.
- **What it suggests.** "Differentiating whole numbers" is done by a divided-power structure at supersingular
  points: the auxiliary function of Stepanov lives on the crystalline site of the CM curve. Height h gives the gain
  1/(p − 1) − 1/(p^h − 1) per derivative, which tends to the full 1/(p − 1). So CM abelian varieties whose reduction
  has a formal summand of large height should win multiplicity faster than a chain of lifts: a route to the shorter
  proof he expects. Check: find step 2 in the Lean and compare exponents; one prompt on the higher-height variant.

### 3. The count qN = M^k + R is the k-th moment of "multiply by t, then Fourier transform". Proved as a toy; the link to cote 1 is proposed.

- **Statement (mine).** For t ≥ 0 on Z/q, q prime, let N_k be the sum of t(x₁)…t(x_k) over the zeros of the path
  quadric x₁x₂ + x₂x₃ + … + x_{k−1}x_k, and M = Σ t. Then q·N_k = M^k + R_k with
  |R_k| ≤ (q − 1)·q^((k−1)/2)·‖t‖₂²·‖t‖_∞^(k−2).
- **Proof.** Sum the character e_q(h·Q(x)) over h. The term h = 0 is M^k. For h ≠ 0 the sum is
  ⟨t, K_h D_t K_h ⋯ D_t K_h t⟩ with K_h(x, y) = e_q(hxy) and D_t the multiplication by t; K_h/√q is unitary. This is
  the note's "iterating Parseval k times".
- **Steps.** 3, 5 and footnote 3; 4 and 7 (W(1_S) ≥ 0 "via a determinant").
- **Meets.** Cote 1 sheets 79–80 and 111–112 as the main session's intake reports them (I have not read those
  sheets): Ξ(√w)/Ξ(0) = det(1 − wB), RH ⟺ B ≥ 0. Proposal: B is the operator "Fourier after multiplication", the
  sums S_k(h) are its moments, and "opposite signs, no cancellation of inverse roots" is Landau's lemma for
  Σ N_k w^k, the positivity Deligne uses on even tensor powers. Check: cote 1 against the Stepanov determinant in
  the Lean chain.

### 4. The sign-only proof is the Hodge-index route of cote 16, and its Arakelov form reaches cote 44. Proposed.

- **Statement.** The definite sign of step 5 ("Bertini … from middle cohomology, one off from the one on M^k") is
  the sign of the intersection form on the evanescent part E^(n−1) of a hyperplane section (16 scans 34–40). On
  powers of the hexagonal CM curve it is unconditional, because there every algebraic class is a Lefschetz class
  and the Hodge standard conjecture is a theorem (Milne; from memory). With the Bost slope inequality (step 13)
  the same positivity on the arithmetic models is an arithmetic Hodge index statement of the kind of Gillet–Soulé
  and Künnemann.
- **Meets.** 16 scans 49–50 (Weil from his C and A; C with I(X×X) gives semisimplicity); 44 scans 4, 8–9 (Th. 4,
  Th. 5 with its "variante locale"; hunch H9: Hodge index from positivity of heights); 47.
- **Check.** Look in the libraries PositivityTheory and Formalism/HermitianCurvature for a statement of
  Hodge-index type; state which cases of Th. 4 of cote 44 it gives.

### 5. Step 17 may close our open row on the pro-ℓ kernel at irregular primes, and gives an integral form of bridge B3. Sketched.

- **Statement.** For odd m the image of the Soulé character κ_m : G_Q → Z_ℓ(m) has index the order of
  H²(Z[1/ℓ], Z_ℓ(m)), the ℓ-part of K_(2m−2)(Z) (from memory). If the K-groups K_(4k)(Z) of his footnote 6 vanish,
  the generators σ_(2k+1) of the Galois image in the pro-ℓ group of the tripod exist integrally for every ℓ in that
  range, and the kernel field of G_Q → Out π₁^(ℓ) of the tripod is the maximal pro-ℓ extension of Q(μ_ℓ) unramified
  outside ℓ beyond the regular primes.
- **Meets.** LM6 A.44–A.45 (open at ℓ = 2 and irregular primes); bridge B3 (grt₁ and mixed Tate motives over Z)
  and S9 of the war game; cote 149 scans 79–85 (his H¹(S, T) and Kummer sequences with T = Ẑ(1)).
- **Check.** Take the exact theorem on H¹(o_E[1/ℓ], Q_ℓ/Z_ℓ(−e)) from the Lean; compare with the hypothesis in
  Sharifi's proof for regular primes.

### 6. The SL₂ of the lift chain is the Lefschetz sl₂ of cote 16. Proposed.

- **Statement.** π ↦ π ⊞ μ_j[t] adds a block on which Arthur's SL₂ acts by the representation of dimension t: a
  string of Tate twists μ(0), …, μ(t−1). Order of vanishing m is the length m of a primitive string; the lifted
  object is a module over the universal ring Φ of 16 scans 14–18. The divisibilities of steps 9, 10 and 15 are then
  the index of the integral order generated by L and Λ, which hunch H8 computes as products of binomials.
- **Check.** Compare the divisibility bound of step 10 with Wilson's diagonal form for small m.

### 7. What GRH for Dirichlet L-functions gives our files directly. Proposed.

- (Z/N)^× is generated by the primes below 2 log² N (Bach, on GRH): a certificate for the cyclotomic coordinate of
  every finite level of GT̂₀ used in the shadow computations.
- Route 2 for A1 (cote 149 scans 35–36; the intake's "Artin's conjecture on average") needs GRH for Kummer fields,
  that is Hecke L-functions over cyclotomic fields: the note's extended hypothesis, announced as expected, not
  this result.

### 8. The period multiplicities are interlacing counts: material for the positivity asked in geometric complexity theory. Proposed, low.

- Step 7 ("values 0, 1 meaning interlacing weights, or up to m") and step 8: branching along a chain of compact
  dual pairs counts Gelfand–Tsetlin patterns, so these multiplicities have polytopal positive formulas. To test:
  which plethysm coefficients occur. Meets cote 133.

### 9. F₁ after Borger and the binomial structures of the 1976 notes. Proposed, low.

- Footnote 5. Frobenius lifts that are the identity are binomial structures; the cochains of a space are binomial
  rings; so bridge B7 (cotes 133, 153, 136–137; Toën, Horel) is the homotopy side of "differentiating whole
  numbers". No statement beyond that yet.

## The path

1. Suggestion 1 into the successor of LM7_PUSH as one item (Δ = χ₁₂ ∘ u; the local symbols; the pentagon and the
   product formula).
2. Suggestion 2: locate step 2 in the Lean, compare exponents, then the higher-height variant.
3. Suggestion 3: cote 1 read against the determinant of steps 1, 4 and 7.
4. Suggestions 4 and 5 once the Lean map names the Hodge-index and the Vandiver-type statements.
