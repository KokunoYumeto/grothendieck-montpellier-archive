# Cote 2: computations and targeted arguments

These are present-run checks. `computations.py` and `computations_output.json` give exact arithmetic, symbolic expansion, and finite diagnostics. A loop over small degrees is not presented as a proof for every degree. The arguments below establish the general identities actually used.

The first implementation expanded large SymPy powers and was interrupted before producing output. The completed implementation multiplies exact truncated coefficient vectors; its output is the checked artifact. No result from the interrupted attempt is used.

## R1. Koszul finite differences, including integral torsion

Let `e_j=(-1)^j binom(r,j)`. The r-th finite difference of a polynomial gives `Σ e_j j^k=0` for `k<r` and `(-1)^r r!` for `k=r`. For `ξ=1−O(-1)`, the Koszul product is `∏(1−jh)^{e_j}`. Its logarithm has first nonzero term `(-1)^(r−1)(r−1)!h^r`. In `Z[h]/h^(r+1)` this is the exact total class. Proving this identity first in a torsion-free universal ring licenses its integral polynomial specialization; no rationalization of the torsion example is performed.

For a line difference on a curve, `α²=0`. The ratio `∏((1+α−jh)/(1−jh))^{e_j}` is exactly `1+α Σ_j e_j/(1−jh)`. Truncating only by `h^(r+1)=0` gives `1+(-1)^r r!αh^r`. Thus 2-torsion α on a complex elliptic curve works for r=2 as well as the written r=3. Its K-class remains nonzero because projection after the constant-section pushforward is the identity. The rank term for O_X is nonzero, so the unrestricted positive-Chern-class N.B. needs rank zero. The abstract Z/5 diagnostic does not establish a geometric counterexample to every interpretation of scan12.

## R2. The chosen-family projective-space calculation

The relation `(L−1)^n=0` gives the coefficientwise homogeneous relation `P_n(ξ)=1`, where `P_n(z)=∏_(j=0)^n(1+jz)^((-1)^(n−j)binom(n,j))`. Its first nonzero coefficient is `(-1)^(n−1)(n−1)! z^n`. Hence degree n is Z/(n−1)! and detects noninjectivity for n≥3. For n=3 the rational expression is `(1+z)^3(1+3z)/(1+2z)^3`; its numerator minus denominator is `2z³+3z⁴`. The homogeneous ideal is `(2z³,3z⁴)=(2z³,z⁴)`, proving the asserted exact ring, not just a finite truncation. Adding the geometric rank-(n−1) class nL−1 imposes ξ^n=0. It is not already a positive sum of line powers: comparing the first two Chern-character moments would require n−1 integers a_j with Σa_j=Σa_j²=n; since a_j(a_j−1)≥0, all would be0 or1, a contradiction. This argument uses n≥3 and is only a family distinction, not a statement about Mackall's different universal functor.

## R3. Chern-ring product and factorial degree cutoff

For positive-degree homogeneous components a in degree i and b in degree j, the first Chern-character terms are `(-1)^(i−1)a/(i−1)!` and `(-1)^(j−1)b/(j−1)!`. Multiplication followed by the inverse triangular conversion gives `a⋆b=−(i+j−1)!/((i−1)!(j−1)!) ab`. This is verified universally before specialization, and matches SGA6 V(6.5.3), printed p349, which was inspected in the scan.

For the next-degree cutoff let m=n+1 and A^d=0 for all d≥n+2. The contribution of a pure class a in degree m to λ_t is `a Σ_(k≥1)(-1)^(k−1)k^n t^k`. Multiplication by a rank-n term contributes `(1+t)^n`; products with positive lower Chern classes have degree>m and vanish. For k>n, the coefficient is `(-1)^(k−1)n!a` by the same finite-difference identity. Thus the tail vanishes exactly when n!a=0. This proves the full-truncation version of scan25; vanishing of a single graded piece is not enough. The code checks the first several tails as an arithmetic certificate, not the general proof.

For the unshifted gamma expression, `γ_t(L)=1+Lt/(1−t)` while `γ_t(L−1)=1+(L−1)t`; evaluating L=1 already contradicts the literal unshifted ideal membership. No deleted argument is restored in the transcription.

## R4. Relative perfection and the limit of thickenings

For B_n=k[t]/(t^n), n≥2, the alternating maps t and t^(n−1) give an exact periodic free resolution of k. Both become zero after Hom(-,k), so Ext^q_Bn(k,k)=k for all q≥0. Over k[t], the two-term resolution gives only degrees0,1. Over B_1=k there is no Ext¹. These facts disprove finite-stage full faithfulness and demonstrate why relative and intrinsic perfection differ. They do not disprove the manuscript's colimit claim.

For noetherian A, the exact abelian category of I-power-torsion modules has the same derived category as complexes with I-torsion cohomology (Stacks0955). For finite endpoints, Yoneda extensions and relations between extensions can be represented with finite intermediate modules: take finitely many generators successively along the finite extension, and use noetherianity for kernels. Every such finite diagram is killed by a common power of I. This identifies the filtered Ext colimit with Ext_A. The same bounded-roof argument gives the finite coherent-complex comparison; restricting to underlying A-perfect objects is then legitimate. This is an affine/noetherian reconstruction, not proof of an unspecified unrestricted prescheme categorical limit.

More precisely, apply Stacks06UP, Lemma13.17.4, to the Serre subcategory of finite modules inside the abelian category of all I-power-torsion modules: a surjection onto a finite module is already onto on a finitely generated submodule. Do not apply that lemma to torsion modules inside all A-modules; that different inclusion fails its stated lifting hypothesis (A→A/I is the simplest warning).

For a noetherian nilpotent thickening, the finite I-adic filtration of a coherent module has coherent factors on the reduced support; additivity and exact-category dévissage identify G0. Ambient regularity is required to identify this with perfect K0, not for the coherent filtration. Forgetting support is different: the exact sequence `0→O_A1 --t→ O_A1→k→0` kills the point class in G0(A1).

## R5. Induction, tensor powers, and polarization

For C3 normal in S3, conjugation by a transposition exchanges χ and χ^−1, giving `Res Ind χ=χ⊕χ^−1`, not two copies of χ. The underlying vector spaces do agree. Restriction of k[Z] along1→Z is infinite dimensional, disproving finite-free preservation without finite index. The projection-formula isomorphism is `g⊗(v⊗w)↦(g⊗v)⊗gw`; the inverse sends `(g⊗v)⊗w` to `g⊗(v⊗g^−1w)`. These respect the balancing relations and the action. Associativity of the symmetric-group induction product follows from transitivity through the three-block subgroup; commutativity follows from conjugation by a block swap. Tensor words in a local basis split into orbits with Young stabilizers and trivial stabilizer representations, proving the local replacement condition on scan19.

The printed polarization identities follow by expansion with the scalars on their specified sides. An unrestricted bimodule replacement is subtler. With A=C, conjugation J, usual left action and conjugate right action on F=C, Φ(x,y)=xy satisfies the usual bimodule sesquilinearity; at x=y=1 the final complex formula has right side0 and left side4. This is a counterexample under those stated conventions only: the absent conditions(1)–(4) could impose centrality and exclude it.

## R6. Curves, surfaces, normalization, and large twists

For finite flat f of smooth proper curves, preservation of Euler characteristic gives `deg(f_*E)=deg E+n(1−g_X)−nδ(1−g_Y)`, including inseparable f. The determinant identity with the norm gives the integral line bundle; the half-canonical expression is only rational. Frobenius therefore has `deg(F_*O_X)=(p−1)(g−1)`.

For a curve mapping onto C in a smooth surface, multiplying the degree≤2 Todd and Chern-character expressions gives `ch1=nδC` and `ch2=f_*d−n f_*K_X/2+nδ CK_Y/2`. Conversion using `c2=c1²/2−ch2` gives exactly the live formula on scan44. For normalization, `0→O_C→ν_*O_Ctilde→Q→0` gives `ch2(ν_*O_Ctilde)=ch2(O_C)+[Q]` and hence `c2(O_C)=c2(ν_*O_Ctilde)+[Q]`. A reduced rational nodal plane cubic has C²=9, CK_P2=−9, and lengthQ=1; the written normalization-genus expression gives8, while the divisor resolution gives9 for O_C.

For a smooth projective f of relative dimension d, selecting codimension d+j in `ch(E) exp(nc1(L)) td(T_f)` gives degree at most d+j in n after pushforward. Relative Serre vanishing identifies this with the direct image for n≫0 under the stated hypotheses. This is rational polynomiality and supplies no integral control of torsion.

## R7. Elementary ring and support checks

For a UFD, a fraction integral over A cannot have a negative prime valuation: in its monic equation the leading term would have uniquely smallest valuation. This re-proves the normality assertion. Integrality is transitive by the finite-module criterion; after localization, clearing finitely many denominators in an integral equation shows integral closure localizes. Every nonconstant element of k(t) has a pole at a closed point of P1, so the intersection of all valuation rings containing k is k, whose fraction field is smaller than k(t).

For D(t)⊔V(t)→A1, each component is an immersion, hence the map is radicial and surjective, but the source is disconnected while the target is connected; the small étale topoi therefore cannot be equivalent. This does not contradict the integral universal-homeomorphism theorem. For algebraically closed k and K=k(t), the small étale sheaf Gm/k is constant with value k×; its inverse image remains that constant sheaf, whereas the representable Gm/K has K× as sections. These are two different base-change operations.

## R8. The integral free case and the two answered lambda questions

For one rank-n geometric generator with determinant inverted, use the symmetric Laurent ring `B=Z[l_1,...,l_n,(l_1...l_n)^−1]^(S_n)`. Put `t_j=l_j−1`. The elements `g_i=e_i(t_1,...,t_n)=γ^i(x−n)` give `B=Z[g_1,...,g_n,(1+g_1+...+g_n)^−1]`. Give g_i weight i. In the splitting ring, every element is an integral linear combination of Laurent line monomials m. For such a monomial, `γ_u(m−1)=1+(m−1)u`, and m−1 has t-adic order≥1. The binomial expansion, including negative integral coefficients, therefore places every γ^r(b−ε(b)) in t-adic order≥r. The symmetric-polynomial theorem identifies intersection with that filtration with the weighted filtration on B; the inverted determinant has constant term1. Conversely each g_i lies in Fγ^i by definition. Thus the two filtrations agree integrally, and grγB is polynomial in the initial forms of g_i. Several generators follow by using disjoint variable sets.

Passing to an augmented lambda quotient carries the defining gamma filtration onto the quotient filtration. This proves the scan29 generation assertion under its explicit ring-generation hypothesis. The determinant identity is proved in the same universal ring by `c1(λ^n x)=Σ_j c1(l_j)=c1(x)` and then specializes along lambda maps. A ring map that omits exterior-operation compatibility need not obey it; this is why the scan29 abbreviated relation list cannot replace the full definition on scan28.
