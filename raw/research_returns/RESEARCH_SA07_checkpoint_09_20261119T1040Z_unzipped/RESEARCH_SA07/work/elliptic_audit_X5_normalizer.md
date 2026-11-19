# Independent audit of F.3.22: all-prime X5 normalizer proof, Steps 2–5

Auditor: OpenAI GPT-6 Astra, elliptic_splitting agent, inherited effort. Date: 19 November 2026. Audited file: `work/LM6_A22_X5_all_primes.tex`. Requested scope: the exact Hodge–Tate character relations, simultaneous conjugation, special representative, and projection within the actual arithmetic image. **Verdict: these steps pass.** This audit does not replace the separate finite Lie-algebra certificate or the last-puncture quotient audit.

## 1. Hodge–Tate characters and the relation lattice

Let ell be 1 modulo 5, E=Q(zeta_5), and fix iota:E→Q_ell. The smooth affine and infinity charts displayed in the proof verify good reduction because ell differs from 2 and 5. The principal polarization gives the exact products chi_1 chi_4=chi_2 chi_3=chi_ell: a nonzero pairing on V_a×V_b is possible only when a+b=0 modulo 5, and perfection then gives the asserted nondegenerate pairings.

The local Hodge–Tate map used is the functorial decomposition of Tate1967, §4.1 Theorem3 and Corollary2, printed pp179–180. I independently opened the complete primary scan at https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf (turn893273403view0; exact passages turn349211598view0/1). Dualizing Tate's displayed formula for Hom(T(G),C) gives the covariant exponent-one summand Lie(B)⊗C_ell(1). The automorphism on the cotangent forms dx/y and x dx/y has eigenvalues zeta_5 and zeta_5²; its differential on the tangent space has the same eigenvalues, since pullback on cotangent vectors is the transpose of the tangent map. At the place zeta_5↦iota(zeta_5)^b, the two indices are therefore {b,2b}. These are exactly {1,2},{2,4},{4,3},{3,1}.

Every finite extension has a place over each of the four places of E, and restriction to a finite local extension preserves these Hodge–Tate exponents. A finite-image character becomes trivial over a finite extension, so all its exponents vanish. Consequently a finite-image monomial product with exponent vector n has equations

\[
 n_1+n_2=n_2+n_4=n_4+n_3=n_3+n_1=0.
\]

Their integral kernel is Z(1,−1,−1,1), which is already an exact trivial relation by the polarization. Thus no further finite-image relation appears on any open arithmetic subgroup. This argument uses all four local places of the same global representation, not four independent choices of global characters.

For multiplicities (m_1,m_4,m_2,m_3) of (x_1,y_1,x_2,y_2), the character being chi_ell³ means that (m_1−3,m_2,m_3,m_4−3) belongs to that kernel. With all multiplicities nonnegative and sum six, this gives (j,j,3−j,3−j), 0≤j≤3. It proves exactly the balanced degree-six space in (X5.3). The identical relation-lattice argument applies to the integral exponent differences occurring in the finite-dimensional derivation space.

## 2. Four actual conjugates, with one common arithmetic element

The maximal geometric pro-ell quotient is characteristic in the geometric fundamental group, so it gives the displayed actual arithmetic extension over Q. The original normalizer image H is open in G_K, hence in G_Q. Choosing actual lifts of gamma_b gives actual closed conjugate procyclic groups A_b and actual normalizing subgroups N_b. On abelianization inner changes of lift disappear.

The equation gamma_b t gamma_b^{-1}=t^b implies the claimed inverse exponent: if v∈V_a, then t^b gamma_b(v)=gamma_b t(v)=iota(zeta_5)^a gamma_b(v), so gamma_b(v) lies in V_{a b^{-1}}. These are all four lines. The normal core of the finite intersection G_E∩intersection_b H_b is open; its fixed field is a finite Galois L/Q. For each b and each sigma∈G_L, surjectivity N_b→H_b supplies a lift lying in N_b∩p^{-1}(G_L). The four lifts can differ. Their outer action is the same sigma, which is all the argument requires.

## 3. The special representative and four tangency equations

For sigma in filtration six, choose a rational Malcev representative whose generator corrections start in degree seven. It acts trivially on V and therefore on the cyclotomic multiplier. Its image of the boundary element is conjugate to that element. Let log z=omega+terms of degrees≥3.

The homogeneous free-Lie centralizer of omega is Q_ell omega. To verify the proof's short argument, take the least associative word of a nonzero homogeneous Lie element commuting with omega. Both least words are Lyndon words. Vanishing of the leading commutator forces the two words to commute as words, so they are powers of a common primitive word. A Lyndon word is primitive; hence the degree is two and its leading word agrees with that of omega. Subtract the matching scalar multiple of omega. Any remaining leading word would have to agree again, a contradiction. This establishes the required centralizer without an assumption on the original procyclic generator.

Comparison of a boundary conjugator in degrees three and four gives W_1=0 and W_2=c omega. Multiplication by exp(−c log z) leaves its action on z unchanged and removes W_2. The comparisons in degrees five through seven then kill W_3,W_4,W_5. Thus the boundary correction starts in degree six and preserves the degree-six outer filtration. The resulting leading derivation kills omega. Another such leading representative differs by ad(w), w∈L_6 with [w,omega]=0, hence by zero. This uniqueness also proves GSp-equivariance, since GSp takes omega to a nonzero scalar multiple.

For each b the selected normalizer lift of the same sigma acts on its generator by a unit theta. The nonzero first linear coefficient and trivial action on V give theta=1 exactly, so that lift centralizes the generator. For the boundary-fixing representative, the resulting conjugacy equation has W_{b,1}=c_b v_b. Multiplication by exp(−(c_b/a_b)log u_b) removes it without changing the conjugacy equation. This operation is legitimate in the rational Malcev completion even when a_b is not a unit in Z_ell. Successively, the centralizer of the degree-one generator v_b kills W_{b,2},...,W_{b,5}. Degree seven then gives D_sigma(v_b)∈[v_b,L_6]. All four equations constrain the one unique special derivation D_sigma. No choice of a simultaneous normalizer section has been introduced.

## 4. Projection inside the actual image

I visually read the original Nakamura1996 pages115–117 in the retained scans `work/sources_audit_next/Nakamura1996_images/page18.png`, `page19.png`, `page20.png`. Corollary(4.2) and table(4.3), p115, give the nonzero degree-six arithmetic quotient; p116 explicitly preserves the graded arithmetic image under finite base extension and proves surjectivity in Lemma(4.5); equations(4.7.1)–(4.7.2), p117, give the exact equivariant quotient and actual curve-image map. The similitude power in degree six is chi_ell³. The End(J)=Z premise of the separate centralizer statement is not used in these displayed maps.

The leading-image map from G_L∩G_Q(6) is a continuous group homomorphism into the additive degree-six vector space. Its image M is compact and therefore closed. Closure under integer multiples extends by continuity to Z_ell multiples. Conjugation by G_L preserves the source and, by uniqueness of the special representative, acts on M through the displayed diagonal character action.

The kernel of each nontrivial quotient character relative to chi_ell³ is closed with empty interior: otherwise it would be open and the quotient character would have finite image, contradicting Section1 above. A finite union of these kernels does not cover compact G_L. Choose tau outside them. The polynomial spectral projector e(Ad tau) is defined over Q_ell and equals one on the desired eigenspace and zero on every other occurring eigenspace. Multiplying by ell^r makes every coefficient integral. Because Ad(tau) preserves M, the resulting finite Z_ell-linear combination ell^r e(Ad tau)m remains in M itself. Its quotient image is ell^r q_6(m), which remains nonzero. Since M was defined as the actual image, this element has an actual preimage sigma_0 in the original arithmetic filtration subgroup.

Every member of M already satisfies the four linear tangency conditions, so projection has not lost them. This proves the requested arithmetic-image step and does not replace that image by its Q_ell-span, Lie closure, or a formal Galois element.

## 5. Scope

The audited Steps2–5 pass as written. No correction to their Hodge–Tate indexing, conjugation inverse, finite base-change operation, inner-conjugator removal, or spectral projection is needed. The proof's remaining finite calculation and proper-curve quotient are separate dependencies already under the other agent's and parent's audits.
