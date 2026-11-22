# A nonzero twisted divisor cup product on a smooth cubic surface

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA06, root. Written 19 November 2026 after checkpoint15. This auxiliary calculation does not by itself prove a local Chow-kernel theorem.

## 1. Exact claim and explicit smooth surfaces

Let k be algebraically closed of characteristic p, let W be the smooth cubic surface specified below, put A=O_W(1)=−K_W, and let D be its displayed line. We compute

μ_D:H⁰(W,A)→H¹(W,Ω¹_W⊗A), a↦a c₁(O_W(D)),

where the Chern class is the algebraic dlog class. The target has dimension four, and the map has rank two, including in characteristics two and three.

For p≠3 use the Fermat surface x₀³+x₁³+x₂³+x₃³=0. Its partial derivatives 3x_i² have no common projective zero. Make the invertible coordinate change u=x₀+x₁, v=x₂+x₃, s=x₁, t=x₃. Its equation is

F=u³−3u²s+3us²+v³−3v²t+3vt²=uQ₀+vQ₁.

The line D is u=v=0, with Q₀|D=3s² and Q₁|D=3t².

For p=3 use F=us²+vt²+u²t+v²s. Again D is u=v=0, with restricted quadratics s²,t². Its gradient is (s²−ut,t²−vs,−us+v²,−vt+u²). A zero coordinate at a common gradient zero forces all coordinates zero. Otherwise normalize u=1. The equations give s=v²,t=v⁻¹,v⁵=1; at these points F=4v⁴=v⁴≠0. Hence W is smooth over the algebraic closure, not just at its rational points.

## 2. The duality calculation

The cubic conormal sequence twisted by A is

0→O_W(−2A)→Ω¹_{P³}(1)|W→Ω¹_W(A)→0.

The restricted Euler sequence is

0→Ω¹_{P³}(1)|W→O_W⁴→O_W(A)→0.

Its map on H⁰ is the coordinate-basis isomorphism. The hypersurface sequence on P³ gives H¹(O_W(nA))=0 for every integer n and H²(O_W(nA))=0 for n≥0. Thus H¹ and H² of the middle conormal term vanish. The connecting map and Serre duality give

H¹(Ω¹_W(A))≅H²(O_W(−2A))≅H⁰(O_W(A))∨.

Twisting the tangent normal sequence by −2A gives

0→T_W(−2A)→T_{P³}|W(−2A)→O_W(A)→0.

Both H⁰ and H¹ of its middle term vanish. The Euler sequence reduces H¹-vanishing to the dual of the same coordinate-basis isomorphism. Hence its boundary δ₁:H⁰(A)→H¹(T_W(−2A)) is an isomorphism. Multiplication by a∈H⁰(A) takes δ₁(b) to δ₂(ab), where δ₂:H⁰(2A)→H¹(T_W(−A)) comes from the tangent normal sequence twisted by −A.

Up to the one fixed sign of the contraction convention, the Serre pairing of μ_D(a) with δ₁(b) is the trace of c₁(O_W(D)) contracted with δ₂(ab), in H²(O_W(−A))=k.

## 3. Direct calculation of the line-bundle obstruction

The normal sequence for D⊂W⊂P³, twisted by −A, is

0→O_D(−2)→O_D²→O_D(2)→0,

with last map (a₀,a₁)↦a₀Q₀|D+a₁Q₁|D. It is surjective because the two quadratics have no common zero. Consequently

H¹(O_D(−2))≅H⁰(O_D(2))/⟨s²,t²⟩.

The class of st is a basis. Let λ_D be the quotient functional normalized by λ_D(st)=1; it kills s² and t².

For q∈H⁰(W,2A), extend q to a quadratic on P³. In the total space of O_{P³}(1), the first neighborhood defined by F+τq=0 has conormal O_W(−A) and deformation class δ₂(q). Local lifts of the ideal of D have equations u+τa₀,v+τa₁. Substitution gives exactly q|D modulo the two Q_i|D. Thus the embedded-line obstruction is its class in H¹(O_D(−2)), with no factor of two or factorial.

The image under H¹(O_D(−2))→H²(O_W(−A)) is the line-bundle obstruction, namely contraction of δ₂(q) with c₁(O_W(D)). This equality follows directly by lifting the local defining equations: their differences on double overlaps are the normal cocycle; its divisor-sequence boundary is the failure of the lifted transition units on triple overlaps. This is the dlog/Atiyah contraction, with the same fixed sign. It introduces no characteristic-dependent factor.

This map is an isomorphism. It is the boundary of

0→O_W(−A)→O_W(D−A)→O_D(−2)→0.

Adjunction gives D²=−1 and A·D=1. Ampleness gives H⁰(O_W(D−A))=0 since A·(D−A)=−2. Serre duality gives H²(O_W(D−A))=H⁰(O_W(−D))∨=0. The cubic hypersurface sequence gives χ(O_W)=1. Surface Riemann–Roch then gives χ(O_W(D−A))=1+(D−A)·D/2=0, so H¹(O_W(D−A))=0 as well. The division by two here is in an integer Euler-characteristic formula, not in k.

The Serre-dual bilinear form of μ_D is therefore, up to a common nonzero scalar,

(a,b)↦λ_D((ab)|D).

In the basis (u,v,s,t), its only nonzero entries are (s,t) and (t,s). Its rank is exactly two in every characteristic. In particular μ_D(s) evaluated at t is nonzero.

## 4. Intended local application and outstanding checks

The proposed construction uses V=P^m×W×C, where C is the ordinary plane quartic of C.3bf/bg, with L=O(1)⊠A⊠K_C and m≥1. A deformation of C by τ ell H has a Picard extension whose vector image is the span of the canonical-section coefficients in ell. A coefficient with nonzero s or t restriction to D can have nonzero product with c₁(D) by the calculation above. The divisor D extends to the actual resolution because its projection to W is retained.

The first unresolved local case is m=1,r=2,N=5. Separate proof obligations remain: choose a smooth incidence divisor and verify the contracted regular punctures; show the relative K₂ class survives the nonsplit thickening and the K₁(V) boundary; realize the Picard kernel by actual proper-curve families; and show that nonzero relative K₀ detects the codimension-two Chow product. Integral Adams-weight separation in characteristic five is a proposed last step, not yet a proved replacement. This note establishes only the twisted line cup-product calculation.


## 5. Independent audit, finite certificate, and exact follow-up sources

The Frobenius collaborator independently read the complete proof and passed the embedded-divisor obstruction, semiregularity isomorphism, Serre duality and all-characteristic rank calculation; its full review is agents/frobenius/C3_cubic_line_cup_independent_REVIEW.md. Root ran code/check_cubic_surface_line_cup.py at14:21:08.341662UTC:17exact checks passed in0.20215913099673344seconds. Full stdout is code/check_cubic_surface_line_cup.out and the structured output is logs/cubic_surface_line_cup_certificate.json. A preliminary program incorrectly demanded every coordinate square belong to the specialized gradient ideal, stronger than the radical statement in the proof; that assertion was replaced by the valid fourth-power membership test. A subsequent serialization issue was fixed by converting the integer Gram matrix to native integers. Neither preliminary issue changes the mathematical claim.

For the proposed K-theory bridge, root freshly opened Geisser and Hesselholt (2011), TheoremA, printedp29, at https://math.mit.edu/~larsh/papers/025/bounded.pdf. It gives bounded p-primary relative groups for nilpotent ring extensions. We also opened Iwasa and Kai (2021), Isomorphisms up to bounded torsion between relative K0-groups and Chow groups with modulus, DOI10.1017/S1474748020000055, published22-page PDF, and read Definition3.9, Lemma3.10 and its entire proof (p1960), plus Theorem4.2 and its proof (pp1961–1962). The first gives the integral Adams eigenvalues on the coniveau graded pieces of a regular finite-dimensional scheme; the second supplies the ordinary cycle map to those graded pieces. We do not use the paper’s separate relative-modulus main theorem, whose affine-neighborhood hypothesis is not supplied here. Stacks Section42.56, Lemma42.56.1 and Remark42.56.2, was freshly opened for the second Adams ring operation and its pullback compatibility, including the perfect-complex construction when2is invertible. The original Soulé1985 input is cited by Iwasa–Kai; this root pass does not claim to have opened Soulé.

Queries in this pass included Adams operations topological filtration K0 regular scheme acts k^i integral graded Gillet Soule; K theory nilpotent extension relative groups bounded p torsion Geisser Hesselholt; and the local Picard/henselian Chow searches recorded in the root Picard audit. No claim of novelty is inferred from those searches.
