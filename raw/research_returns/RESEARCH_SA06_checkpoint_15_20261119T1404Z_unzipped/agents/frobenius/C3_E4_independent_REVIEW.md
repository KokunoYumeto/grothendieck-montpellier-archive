# Independent audit of the strict-local cone and arithmetic support extensions

Date: 19 November 2026, 04:40 UTC. We record a targeted independent proof audit by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/frobenius`. We did not edit the reviewed fragments. This review does not claim priority.

## C.3e–g: strict-local cone statements

We read the full `research/sections/C3_local.tex` and independently reconstructed the cycle argument. No mathematical correction was identified.

For a pointed étale neighbourhood \(T\to C\) with exactly one geometric point over the vertex, the pullback of the cone blow-up is étale over \(\operatorname{Tot}(L^{-1})\). Therefore its map \(q_T\) to the smooth projective base is smooth of relative dimension one and the exceptional divisor is a section \(i_T\) with normal bundle \(L^{-1}\). More precisely, \(\mathcal O(i_T(V))=q_T^*L^{-1}\). If the pullback of a cycle \(\alpha\) vanishes off the section, localization gives \(q_T^*\alpha=(i_T)_*\beta\); refined section pullback then gives \(\alpha=-L\beta\). Conversely the projection formula gives \((i_T)_*\beta=-q_T^*(L\beta)\). Thus the kernel is exactly the Lefschetz image, integrally, at every stage. The argument requires neither a line-bundle identification of the entire étale pullback nor surjectivity onto its Chow group.

The algebraic-equivalence version is covered by an exact primary reference: Fulton (1998), Proposition 10.3, pp. 185–186, preserves algebraic equivalence under the four operations used; Example 10.3.4, p. 186, explicitly gives localization modulo algebraic equivalence. We also checked directly that a curve-parameter correspondence on the open complement can be closed in the ambient space times its smooth projective parameter curve. Taking its refined fibres lifts the algebraic-equivalence witness before ordinary localization is applied. Fulton, Proposition 1.8, p. 21, and Corollary 6.3, p. 103, give the ordinary localization and self-intersection formulas.

The strict-henselian step is justified by finite witnesses. Cycles, the finite rational functions in a rational equivalence, and the curve and correspondence in an algebraic equivalence descend to one pointed étale stage. The punctured local scheme uses codimension inherited from the local cone; its smaller maximal chain length after deleting the closed point is not a reason to reindex those groups.

For C.3f, \(P=(u:v:w:1)\) with the stated algebraically independent coordinates is a geometric generic point over \(\overline{\mathbf Q}\). A hypothetical relation with a cycle supported on the fixed hyperplane can be spread from \(\mathbf C\) to \(\overline K\), specialized there, descended to a finite extension of \(K=\overline{\mathbf Q}(V)\), and traced. The resulting diagonal decomposition has support on \(V\times H\) and \(D\times V\), even when the supported cycle varies over \(K\). Both correspondences kill \(H^{2,0}\), whereas a nonzero multiple of the diagonal does not. Thus this stronger support assertion avoids any need to descend an individual divisor class. The plane quartic through the two points is smooth because its three diagonal coefficients are nonzero. Flat compatibility of its Gysin map produces the non-torsion cone class. This is a rational-equivalence / algebraically-trivial-subgroup example; the fragment correctly states that its image modulo algebraic equivalence is zero.

The C.3g dimension range is correct: with \(n=N-1\), the prescribed range gives \(2r\ge n+2\), so the non-top case lies inside the Nori range \(r<n<2r\). The top case uses the Calabi–Yau Fermat hypersurface and the same \(H^{n,0}\) diagonal-support obstruction. It does not assert a nonzero class modulo algebraic equivalence in the top case.

## E.4l–p: actual support and all-twist complexes

We read the full `research/agents/real_weil/E4_actual_support.tex`, and opened the cited primary Geisser, Flach–Morin, and Milne sources. No mathematical correction was identified in the reviewed scope.

### Full purity in twists at least two

Geisser (2004), Proposition 5.1, printed p. 789, explicitly asserts the full integral purity quasi-isomorphism \(\mathbf Z(n-1)[-2]\to Ri^!\mathbf Z(n)\) when \(n\ge\operatorname{cd}_p(U_{\mathrm{et}})\), under the historical Bloch–Kato hypothesis. We checked the definition immediately preceding the proposition and its proof. The bound concerns all étale schemes over the generic fibre, hence all finite separable extensions of the local field. For \(K=\operatorname{Frac}(\mathbf Z_{\(p\)}^h)\), the completed-field equivalence and the usual local cohomological dimension bound give the required uniform value two. This includes \(p=2\). Thus the stated result is stronger than the merely truncated purity theorem in the introduction and really applies here.

We also checked Flach–Morin (2018), Lemma 7.7, pp. 1543–1545, including its proof. The proof constructs the diagram by cones of multiplication by each \(p^r\), applies the finite-coefficient comparison and truncation, and identifies the special-fibre logarithmic de Rham–Witt complex. The argument can be made at each level; it does not infer levelwise isomorphisms merely from an isomorphism of pro-objects. Geisser, Corollary 4.4, p. 786, supplies the cohomological vanishing hypothesis in this smooth trait case. For the perfect zero-dimensional special fibre, the positive-degree logarithmic differential terms vanish. Milne (2006), II, Lemma 1.3 and its proof, printed p. 150, explicitly gives cohomological dimension at most one for the strict-henselian generic field. Thus the truncation of \(Rj_*\mu_{p^r}^{\otimes n}\) can be removed here.

### Twist-zero and negative local terms

Milne, II, Proposition 1.1(a), p. 149, gives \(R\Gamma(R,j_!F)=0\) and the shift by one for its support. This verifies the extra \(p\)-primary term in each negative twist, after including the coefficient shift by \([-1]\). The prime-to-\(p\) summands have the ordinary tame-inertia purity shift. The real correction does not affect a support at a finite closed point.

For twist zero, the local cohomology sequence gives degree-three support equal to the character group of the units. The proof retains the support subscript in Milne's duality pairing on p. 152; the imperfect PDF extraction of Theorem 1.8 must not be used to remove it. The vanishing of \(H^2(K,\mathbf Q/\mathbf Z)\) follows by duality and the zero inverse limit of the finite roots-of-unity groups in a \(p\)-adic field. The unit decomposition gives the stated tame and wild groups, including the separate factor of order two at \(p=2\). Globally, the annihilator of diagonal complex conjugation gives exactly the totally real character group. Its index is two when a finite prime has been removed, so the asserted boundary surjectivity is justified.

### Twist one and coherence

Milne, II, Proposition 2.1 and Remark 2.2(a), pp. 163–165, give the Brauer group and the higher real terms. Flach–Morin, Propositions 6.10–6.11, p. 1522, identify the chosen coefficient complex with \(\phi_*\mathbf G_m[-1]\) and remove those real terms. When the removed set is nonempty, the real invariant is surjective because one removed finite place may carry invariant \(1/2\). Its kernel is the sum-zero subgroup \(B_S\), as claimed.

The exact sequence \(0\to\Lambda_S\to V_S\to B_S\to0\) holds integrally: correct the integral sum of any rational lift by subtracting it from one coordinate. The cone therefore has the advertised unit group in degree one and free lattice in degree two. We checked the asserted uniqueness and restrictions in the derived category: \(\operatorname{Ext}^{a}_{\mathbf Z}=0\) for \(a\ge2\), \(\operatorname{Ext}^1(\Lambda_S,E_S)=0\) because \(\Lambda_S\) is free, and \(\operatorname{Ext}^1(\mathbf Q/\mathbf Z,B_S)=0\) because \(B_S\) is divisible. These facts eliminate precisely the possible off-diagonal maps used in the argument. Coordinate inclusions and the zero maps out of the proper correction give a coherent explicit cone model.

For all other twists, the proper correction is fixed once and then composed with actual restriction maps. A cochain representative of that single arrow and functorial representatives of restrictions give the indicated coherent mapping cones. Modulo \(m\), the rational correction is zero, and derived reduction commutes with derived global sections because it is the cone of multiplication by \(m\). This proves all the finite-coefficient comparisons with the stipulated Artin–Verdier coefficients. Localization cancels the identical correction on the two opens. Boundedness follows from the proper calculation and the bounded local support terms. The text appropriately does not assert finite generation, equivalence to every open Weil–étale topos, or a multiplicative theory on arbitrary arithmetic schemes.

## Opened primary-source ledger

| Source | Exact checked location | Opened URL |
|---|---|---|
| Fulton (1998), *Intersection Theory*, 2nd ed. | Proposition 1.8, p. 21; Corollary 6.3, p. 103; Proposition 10.3 and Examples 10.3.2, 10.3.4, pp. 185–186 | https://djvu.online/file/Pl4avuZzLcI6I (primary book scan/OCR) |
| Geisser (2004), *Motivic cohomology over Dedekind rings* | Theorem 1.2, p. 774; Corollary 4.4, p. 786; Proposition 5.1 and proof, p. 789 | https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf |
| Flach–Morin (2018), *Weil-étale cohomology and zeta-values of proper regular arithmetic schemes* | Propositions 6.10–6.11, p. 1522; Lemma 7.7 and its full proof, pp. 1543–1545 | https://ems.press/content/serial-article-files/26429 |
| Milne (2006), *Arithmetic Duality Theorems*, 2nd ed. | II, Proposition 1.1, p. 149; Lemma 1.3, p. 150; local pairing, p. 152, and Theorem 1.8, p. 153; Proposition 2.1 and Remark 2.2(a), pp. 163–165 | https://www.jmilne.org/math/Books/ADTnot.pdf |

The norm-residue theorem and the proper Flach–Morin global number-ring computation are used as established cited inputs, not independently reproved in this targeted audit. Their broader source audit belongs to the owning agent's reference ledger.
