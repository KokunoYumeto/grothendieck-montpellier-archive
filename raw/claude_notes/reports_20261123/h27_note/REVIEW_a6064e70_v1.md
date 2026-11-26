# H27: Connes's trace formula over Q against Alpöge's theorem. Review, and the decision not to write a note

By the editor (Claude Fable 5.2 at effort max, agent a6064e70594596486), 23 November 2026. This replaces the
comments I wrote earlier the same day, before the user's question reached me.

**Usefulness, in one sentence.** The equivalence "global trace formula ⇔ GRH" is Connes's own statement; what the
run adds is a proof of it in characteristic zero, for Q and every Dirichlet character, which his paper asserts for
zeta without proof, and that proof is some sixty pages of estimates whose only consumer is Connes's programme
(the formula over Q becomes a theorem; it says nothing about zeros that GRH does not say). **It is not a short
note. The second result, S50, is a direct consequence of Suzuki's paper. So I wrote no note.**

## 1. The user's question: [the user's words, omitted]

The statement, yes. The proof over a number field, no; but it is a paper, not a note.

What Connes's paper has (read in its TeX, arXiv:math/9811068):

- Introduction: the validity of the trace formula in the global case "is left open and shown (Theorem 5 of
  section VIII) to be equivalent to the validity of the Riemann Hypothesis for all L functions with
  Grössencharakter".
- Theorem 5 (§VIII): stated and proved for "a global field of positive characteristic". There the functions f with
  f and its Fourier transform vanishing for |x| > Λ exist, the image of the cutoff lies exactly in the window
  Λ⁻¹ ≤ |g| ≤ Λ, the difference of the two projections is positive (his (23) to (25)), and Lemma 3 computes its
  limit as a sum over all zeros of the strip, those off the line through their harmonic measures.
- Number fields (end of §VIII): "For simplicity we shall take k = Q." The cutoff is the span of the prolate
  functions ψ_n, n ≤ 4Λ² (Landau, Pollak, Slepian), then ψ ↦ ψ ⊗ 1_R, "which suffices when we deal with the Riemann
  zeta function. Note also that in that case we restrict ourselves to even functions on R. This gives the analogue
  of Lemma 1, Theorem 5, and Lemma 3." No proof of the analogue is written, and no character of conductor > 1 is
  treated.

So "Connes's Theorem 5 plus Alpöge" does not give the formula over Q as a theorem: Theorem 5 is not proved there.
What T51 is, beyond a paragraph:

1. a proof in characteristic zero. The image of the cutoff is not inside the window: the prolate functions at the
   edge of the plateau leak a fixed proportion of their energy outside the band. The run proves that a smooth test
   does not see the leak, bounds the Gram matrix of the image from below (unconditionally through an estimate of
   Matomäki, Shao, Tao and Teräväinen for Möbius sums; under GRH with any small power), and proves the limit of the
   defect under GRH from below (truncated zero jets) and from above (a finite-pole inverse and a tightness bound);
2. every Dirichlet character, even and odd, with the frequency radius Λ/q, and the two polar coordinates in the
   principal sector;
3. the direction "formula ⇒ GRH" without any hypothesis.

Does it matter to anyone? To the people in Connes's programme, as closure: the global trace formula over Q would be
a theorem. It does not help with zeros: the formula follows from GRH, and the hope of the programme was the other
way. And it is only as good as its long proof, which is checked for about a third (§3). **My recommendation: not a
Hexagon note. If we want it, it is a long paper ("the number-field analogue of Connes's Theorem 5, over Q"), after
a complete check of the chain; the note form would be an announcement of a proof we have not finished checking.**

## 2. S50 against Suzuki (arXiv:2610.32704v1, read in its TeX)

**Not in his theorems, but a direct consequence of his paper.**

- His results, assuming RH: the positive eigenvalues t_{a,n} of a distinguished self-adjoint extension of i d/dx on
  the completion H_a of C_c^∞(−a, a) for Weil's form satisfy t_{a,n} ≥ γ_n and decrease to the n-th *distinct*
  ordinate γ_n (Theorem 1.1); the normalized spectral functions converge locally uniformly to ∏(1 − z²/γ_n²) over
  the distinct ordinates, and "the multiplicities of the zeros are not recovered by this product" (Theorem 1.2).
  The key step is (D_{a,π})⁻¹ = j_a* C j_a, the compression of the inverse C of the global operator (Theorem 3.3),
  on the global space ℓ²(Γ, m) (§2.3, quoting his earlier paper for the sampling isomorphism). The Remark at the
  end of §4 gives convergence of the transported resolvents in operator norm. §6, Proposition 6.1: for fixed a, an
  approximation by trigonometric polynomials.
- S50 (the run): one sequence of finite matrices on piecewise-linear spaces V_N; the multiplicity m_γ read off as
  the limit of ‖E_{N,j} a_N‖²/φ̂(t_{N,j})² for a fixed function φ with positive Fourier transform; polynomials P_N
  with real zeros converging to Ξ(z)/Ξ(0); rounding to rational arithmetic; a direct proof that sampling is onto.
- Why it is a consequence: in ℓ²(Γ, m) the unit eigenvector at γ has the coordinate m_γ^{-1/2}, so
  |⟨φ, e_γ⟩|² = m_γ |φ̂(γ)|². Norm convergence of the compressions (his Remark) gives convergence of the spectral
  projections, hence of ⟨E φ, φ⟩ to m_γ |φ̂(γ)|², for any fixed φ in the global space. The tail of the product is
  controlled by his inequality t ≥ γ. The rest of S50 is packaging: the finite-dimensional spaces (he has a version
  at fixed a), the cap on the exponents, the rounding.

S50 is correct as far as I can see: I followed its proof line by line and found no fault (§3). It is a remark worth
sending to Suzuki, who says the multiplicities are not recovered; it is not a note of ours. A draft of the remark
is in `RECORDS.md`.

## 3. What was checked (details and check events in `RECORDS.md`)

- T51's last steps and S50: Claude Opus 5.5 at effort high, 22 Nov (targeted proof checks, each given the earlier
  statements).
- By me, 23 Nov, line by line, no fault found: the Gram formula (21), the smoothed tail (25), the unconditional Gram
  bound (27), the Gram bound under GRH (28), the tail sum at the full cutoff (29), the comparison of the projection
  with its compression to the window (30), the lower bound for the defect by truncated zero jets (31); the proofs
  of the converse steps (49 to 51) and of the assembly (46), read in full; S50. Two bounds of the lemma on
  L(1/2+it)/L(1/2+δ+it) re-derived.
- Not checked by anyone but the run: the upper bound for the defect and its tightness (38 to 41; I read 38 and the
  first two fifths of 39), the principal sector (42 to 45), the dictionary to Connes's semilocal operators (47, 48).
  About 2,300 lines.
- One input a referee will ask about: the lower bound ν ≥ 1/4 for the prolate eigenvalues in the cutoff rests on
  Landau's asymptotic at the edge of the plateau, cited from his 1985 overview and not opened.
- **An error of my own, caught:** in my first comments I said the strict positivity of Weil's form on compactly
  supported functions (the run's S03) has a two-line proof by Jensen. It does not: one needs that the *distinct*
  ordinates are too many for a function of exponential type, which takes Conrey's theorem on simple zeros or,
  under RH, the multiplicity bound of Carneiro, Chandee and Milinovich. The run's proof of S03 uses exactly these
  and is right.

## 4. Kind, and what happens to the files

- Had there been a note: **clear** for T51 on Hexagon (searches for Connes, trace formula, Weil quadratic, prolate
  on 23 Nov found nothing on it; the posts on Alpöge's theorem concern its proof), **needs a pass** for S50, and the
  pass (Suzuki) is done with the result above.
- Before the user's question reached me I had written a draft note (statement with explicit cutoffs, proof from
  three quoted propositions, S50 in full). It was never built. I removed it after this decision; the exact
  statement and what it quoted are in `RECORDS.md`, so nothing is lost for a later paper.
- Morishita: the two corrections are a letter; the draft is in `RECORDS.md`.

Nothing was sent, posted or pushed.
