# H06b: field-expert gate on the present text of h06b_note.tex

Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e), 23 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5
at effort max). Text refereed: `h06b_note.tex` as fixed by the main session at 13:57 UTC (16 pages; its Sections 3–8
are unchanged from the text I read in full earlier today). The mathematics is by GPT-6 Astra (ChatGPT Pro mode). I
formed the verdict below before opening `GATE_H06b_ad855737_20261123.md` and `REVIEW_ad855737_v1.md`, and compared
afterwards (§4). I did not edit the note.

## 1. Overall verdict

**POST.** I found no mathematical error in Sections 3–6, and the cited theorems say what the note uses, at the
places cited. Three one-line edits are recommended in §3; none is a condition.

## 2. The five criteria

| Criterion | Verdict | Basis |
|---|---|---|
| 1. People would care | **Yes** | The question is Anderson–Ihara's (1988); only regular primes were known (Sharifi 2002 with Brown 2012); Sharifi wrote in 2019 that the irregular case is "a very interesting open question" (quotation as read at the source by ad855737; I did not open it). The note settles every Vandiver prime and every odd prime below 2^31. |
| 2. Format (HOW.md, eight boxes) | **Met** | Title names the question and whose it is; the abstract opens with Ihara, Anderson–Ihara, Sharifi and Brown; Section 1 has the theorem, its meaning, why it matters, credit, context and scope; Section 2 is headed "Proof overview"; open questions and provenance close it. No run names or paths. 16 pages, no overfull box (log of the main session's build). |
| 3. Background, Hexagon included | **Met** | The literature gate is ad855737's (sources opened, with hashes); my searches of this morning agree (regular case only; Hexagon: nothing). I opened Wake–Wang-Erickson 2017 and 2018, Fukaya–Kato and Hain–Matsumoto myself (§5). The statement on higher circular units in Section 1 is Anderson–Ihara's Theorem 2 (IV), as recalled by Ishii, p. 2 (confirmed today through a search summary of Ishii's text). |
| 4. The mathematics is checked | **Yes** | Sections 3–6 by me, as below; Sections 4–6 line by line by ad855737; Section 7 and Lemma 6.1 by the main session. I also read the proof of Lemma 7.1 and agree with it. |
| 5. It adds something | **Yes** | The first result at irregular primes, and the two lemmas that carry it (cup products against the class-two extension; separation by poles). |

## 3. The mathematics, section by section

**Section 3 (rational image, density, Levi normalization): correct.**
- Hain–Matsumoto, Proposition 8.3 and Theorem 8.4 (arXiv:math/0006158v2, opened): the Zariski closure of the image
  of G_{F,S} in Out 𝒫 is a negatively weighted extension of G_m by 𝒰, and the image of I¹G is Zariski dense in
  𝒰(Q_ℓ). For the line minus three points I¹ is the kernel of the cyclotomic character. It maps onto
  H = Gal(Ω_p/F_∞), and the outer action factors through Gal(Ω_p/Q) because Ω_p* ⊆ Ω_p. So ρ(H) is dense.
- The image b of γ is semisimple: its centralizer in 𝒰 is trivial because u^m ≠ 1 on every weight, so the unipotent
  part of b is 1 and b lies in a Levi torus. An element commuting with b lies in that torus, so Δ acts on s_m by
  ω^m. This is (3.2).
- Freeness of the graded Lie algebra is Brown's theorem in its outer form (the Deligne–Ihara conjecture).

**Lemma 4.1 (finite-level cup comparison): correct.** I re-derived every step.
- If all C_{e;a,b} vanish on D_α, then C_e = (γ − α)A with A alternating: S = (1+T₁)(1+T₂) − α is a coordinate
  because α ≡ 1 modulo the maximal ideal. Then r_e(γ)y − A is an eigenvector lifting w, so the extension splits
  over W.
- The cochain k = −(p^b/2)fg − ψ(p^b z) has dk(h₁,h₂) = p^b f(h₁)g(h₂): the central coordinate of a product is
  z₁ + z₂ + [x₁,x₂]/2, and the two summands give (f₁g₂ + f₂g₁)/2 and (f₁g₂ − f₂g₁)/2.
- On P_n the difference p^b f∪g − dk is k(δh′δ⁻¹) − χ(δ)²k(h′) = −ψ(p^b β_δ(t(h′))), since
  z(δhδ⁻¹) = δz(h) + β_δ(t(h)). It vanishes on W.
- H²(P_n, 𝒪/pⁿ(2))⁺ = V/(pⁿV + (B^{pⁿ} − 1)V) maps onto W*(2)/(pⁿ, (u²/α)^{pⁿ} − 1). If cups generate, p^b lies in
  the ideal (pⁿ, (u²/α)^{pⁿ} − 1) for every n, which is false. Repeated roots are covered.
- The restriction of C_e to D_α does not depend on the lift y (two lifts change C_e by a multiple of q_e(γ)), so
  the condition is intrinsic.

**Lemma 5.1 (separation of Magnus coefficients): correct.** I re-derived the argument.
- With assigned degrees 1 (odd) and 2 (even), the length-d part of ρ(g) is the image of the assigned-degree-d
  Magnus component under "odd letter ↦ linear part, even letter ↦ length-two part"; higher assigned degree gives
  higher length. Even eigenlifts have no linear part, by the character of Δ.
- The assigned-degree-two part of γ^j y_e γ^{−j} maps to z^j B_{e,0}, z = u^{m+n}; the element E_e gives
  q_e(z) B_{e,0;m,n} = C_{e;a,b}(u^m − 1, u^n − 1).
- Identity theorem: the test weights accumulate inside the open disc and the series are bounded, so vanishing on
  the grid gives an identity.
- Pole isolation: after T_{j+1} = (α_j + S_j)/(1+T_j) − 1 every denominator not selected is a unit of K₀[[S_J]]. I
  checked the three cases (same position and another root; a disjoint position; a position overlapping a selected
  pair on either side). The coefficient of ∏ S_j^{−k_j} is A_P · ∏ C(T_j, α_j/(1+T_j) − 1), a product of nonzero
  elements of a field.

**Section 6 (arithmetic hypotheses) at the cited places: the citations say what is used.** Opened as TeX or PDF
today:
- Wake–Wang-Erickson 2017 (arXiv:1510.01661v4), Proposition 2.2.6 and its proof: Ext¹_Λ(𝔛^#_{χ⁻¹}(1), Λ) = X_θ,
  Ext² = 0, rank one from the local units. Under finite X_θ the note's deduction (free after inverting p) is right.
  Running assumptions for N = 1: p ≥ 5, θ ≠ 1, ω². Corollary 5.1.2: X_θ = 0 gives Υ an isomorphism, and with X_χ(1)
  cyclic also ϖ; this is the sentence the main session added to the credit. Proof of Lemma 5.2.7: X_χ = 0 for
  χ = ω^{±1} by Stickelberger.
- Wake–Wang-Erickson 2018 (arXiv:1505.05128v3): Corollary 2.1.3 (0 → E_θ/C_θ → Λ/ξ → 𝔛_θ → X_θ → 0); the text after
  Conjecture 2.1.5 (X⁺ finite implies X⁻ pseudocyclic); Corollary 8.1.3(2), exactly the two hypotheses of (6.8) and
  the conclusion (6.9), with multiplicities handled in its proof (1 − x nilpotent).
- Fukaya–Kato (preprint of 15 Aug 2012): §6.1.5 (for N = 1 the assumptions are θ ≠ 1, ω², the excluded cases
  trivial); Conjecture 7.1.8, §7.1.9 and §7.1.10: surjectivity of ϖ gives, for every r ≥ 1, generation of the
  θ-part of H²(Z[1/p, ζ_{p^r}], Z_p(2)) by the symbols {1 − ζ^u, 1 − ζ^v}, and modulo p^r this is the class group.
- The remaining steps of Section 6 are right: the excluded and unit components are zero at every level; the even
  part of a symbol is the cup of the even parts, because the odd part of the p-units modulo pⁿ is cyclic; the
  maximal pro-p quotient of π₁(S_n) is P_n; the extension Ω_p is Iwasawa's.

**Recommended one-line edits (not conditions):**
1. Section 3, "Brown's theorem identifies the graded Lie algebra of 𝒰_p …": add the citation
   `\cite[Theorem 1.1 and its consequence, pp.~949--950]{Brown2012}`. The run's own text cited the outer-action
   form (Brown, arXiv:1904.00179, §§2.1–2.3) in the section that was replaced.
2. Section 1, "Anderson and Ihara described Ω_p* as the field generated by their higher circular p-units": give
   the locator, `\cite[Theorem 2 (IV)]{AndersonIhara1988}`, as recalled in `\cite[p.~2]{IshiiKernel2026}`.
3. Provenance: "What Section 1 says about [1] and [7] beyond the question itself … is from memory" can now read
   that the statement on higher circular units was confirmed through Ishii's account, and the rest is from memory.

## 4. Comparison with ad855737

Read after §§1–3 were written. Its review finds no mathematical error in Sections 4–6 and its corrections (the
check sentence, Sharifi 2019, the credit to Wake–Wang-Erickson 2017, the eigenlift locator) are in the present
text. We agree on every step both of us checked. What I add: Section 3 against Hain–Matsumoto, the three
denominator cases in the pole isolation, the independence of the pole condition from the lift, and edits 1–3. What
it has and I do not: Sharifi 2002, 2007, 2011 and 2019 and Ishii's two papers at the source, and the Hexagon
listings.

## 5. Not opened by me

Sharifi 2002 and 2019, Ishii, Brown, Anderson–Ihara, Iwasawa 1981, Sharifi's Iwasawa notes, Milne, Hart–Harvey–Ong.
The facts taken from Iwasawa, the notes and Hart–Harvey–Ong are standard and I know them to hold as stated: freeness
of Gal(Ω_p/F_∞) when μ = 0; Kummer duality between 𝔛⁺ and X⁻; Coleman's sequence for the local units; Vandiver's
conjecture below 2^31.

## 6. Check events

| Statement (note) | Date | Who | Type | Outcome |
|---|---|---|---|---|
| Section 3: density of ρ(H), Levi normalization (3.2) | 2026-11-23 | Claude Fable 5.2 at effort max (a49aabbf) | targeted proof check, Hain–Matsumoto Prop. 8.3 and Thm 8.4 opened | confirmed |
| Lemma 4.1 | 2026-11-23 | same | independent re-proof (cochain identity and edge class recomputed by hand) | confirmed |
| Lemma 5.1 | 2026-11-23 | same | targeted proof check, every step re-derived | confirmed |
| Section 6, module hypotheses (odd part free of rank one; even part cyclic) | 2026-11-23 | same | targeted proof check, WWE 2017 Prop. 2.2.6 and WWE 2018 Cor. 2.1.3, Conj. 2.1.5 opened | confirmed |
| Section 6, symbol surjectivity and finite-level generation, (6.8)–(6.12) | 2026-11-23 | same | targeted proof check, WWE 2018 Cor. 8.1.3(2) and FK §§6.1.5, 7.1.8–7.1.10 opened | confirmed |
| WWE 2017 Cor. 5.1.2 as cited in Section 1 | 2026-11-23 | same | read at the source | says what the note says |
| Lemma 7.1 | 2026-11-23 | same | targeted proof check (read) | confirmed; already checked by the main session and ad855737 |
| Lemma 6.1 | — | — | not checked by me | checked by the main session |
| Theorem 1.1 (a)–(c) | 2026-11-23 | same | used and rechecked: follows from the above with the cited theorems | confirmed; POST |
