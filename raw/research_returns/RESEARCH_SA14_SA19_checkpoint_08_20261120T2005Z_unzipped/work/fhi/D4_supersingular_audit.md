# Independent audit of the supersingular Igusa calculation

**Reviewer:** `/root/fhi`. **Date:** 2026-11-20. **Conclusion:** the complete proof in `work/dgj/attempt_D4_supersingular.tex`, Steps 1–7, passes this independent audit. This review concerns the stated marked Artinian deformation problem over local Artinian (W(k))-algebras with algebraically closed residue field of characteristic two.

The resulting hull is

\[
 W(k)[[t,s,u,v]]/(s^4-ts^2-2s).
\]

The proof also establishes flatness of the torsion Picard scheme for every Artinian deformation of the supersingular Igusa surface. No assertion of representability of the unpointed deformation functor is needed: the four-parameter construction gives a hull.

## 1. Actual points and the canonical subgroup

The canonical connected–étale sequence and its dual give (M\simeq\mu_{2^\infty}\subset D=G^0\subset G=A[2^\infty]), and (D/M) is a connected BT group deforming the supersingular elliptic factor. The quotient assertion follows by dualizing the connected–étale sequence of (G^\vee), so it does not assume that an arbitrary finite flat subgroup quotient is again BT. Tate's paper supplies exactly the connected–étale and duality assertions needed over a complete noetherian local ring; an Artinian local base is such a ring.

The assertion that a BT homomorphism reducing to zero is zero is valid here. Its image lies in the infinitesimal formal kernel, which is killed by one fixed power of two, uniformly on test algebras. The source is two-divisible as an fppf sheaf. Hence the homomorphism vanishes. This is the same rigidity used in Katz's Lemma 1.1.3. Therefore the actions (+1) on (M) and (-1) on (D/M) follow from their reductions, without using eigenspace projectors involving division by two.

For (j(2^{-r})=[2^N]\widetilde e_{N+r}), all lifts exist by smoothness of (A). Their differences lie in the formal kernel; the fixed exponent (2^N) kills that kernel. Increasing (N) gives the same answer because (2\widetilde e_{N+r+1}-\widetilde e_{N+r}) is another formal-kernel point. Thus these are actual compatible (R)-points, not merely fppf-local points. Their reductions are the specified torsion points, and a further fixed power of two kills their formal-kernel multiples, so they lie in (G(R)). The same independence proves that they are fixed by the involution. The affine equation consequently forces \(\kappa=j(1)\in M(R)\).

The presentation

\[
 G=(D\oplus\underline{\mathbb Z[1/2]})/
       \{(-n\kappa,n):n\in\underline{\mathbb Z}\}
\]

is valid on arbitrary test schemes: one chooses locally a representative of a section of the constant étale quotient and subtracts the corresponding base section (j(r)). The kernel is precisely the displayed graph. Its subquotient with (M) in place of (D) is therefore a genuine sub-fppf-sheaf (H\subset G).

The BT effectivity argument is sufficient. Since multiplication by two is an epimorphism on both (M) and \(\mathbb Q_2/\mathbb Z_2\), it is an epimorphism on (H). For each (n),

\[
0\longrightarrow M[2^n]\longrightarrow H[2^n]
\longrightarrow (\mathbb Z/2^n)_R\longrightarrow0
\]

is exact. Each middle term is an fppf torsor under a finite locally free scheme over a finite étale scheme, hence is representable and finite locally free of rank (2^{2n}). The inclusions into (G[2^n]) are proper monomorphisms of finite schemes, hence closed immersions. The resulting height-two BT group has exactly the special-fibre inclusion of (F_0[2^\infty]).

Katz's full Serre–Tate theorem lifts both the elliptic curve and this specified homomorphism, rather than only an isogeny class. The lift (F\to A) is proper and quasi-finite because its only geometric fibre is a closed immersion. It is finite, and the cokernel of its structure-sheaf map vanishes by reduction and Nakayama. Thus it is a closed immersion.

Uniqueness is also justified. A competing elliptic subgroup (F') has the same multiplicative BT subgroup: dualizing its inclusion identifies its multiplicative part with the unique rank-one étale quotient of (G^\vee). The marked reduction fixes this identification. Smoothness of (F') allows the lifts defining (j) to be taken in (F'); hence its BT subgroup contains (H). The equal ranks at every finite level make the inclusion an isomorphism. Serre–Tate full faithfulness then identifies the two elliptic subgroups and their maps to (A).

## 2. Graph classification

For \(\rho:A\to E=A/F\), the factorization \(1-\sigma=a\rho\) and \(\rho a=[2]_E\) give an fppf epimorphism

\[
E\times F\longrightarrow A,\qquad(e,f)\longmapsto a(e)+f.
\]

Its kernel is exactly the graph of \(h=-a|_{E[2]}:E[2]\to F[2]\). It reduces to zero; its étale projection is therefore zero by invariance of maps to an étale scheme under nilpotent thickenings. Thus (h) factors through \(\mu_2\), and Cartier duality identifies it with a unique point \(Q\in E^\vee[2](R)\) reducing to zero.

Conversely, quotienting (E\times F) by this graph gives the required abelian scheme and involution. The graph is invariant because (-1=+1) on (E[2]). The special-fibre quotient identification is induced by ((e,f)\mapsto(2e,f)). In the quotient, (a(e)=[(e,0)]); its recovered map \(-a|_{E[2]}\) is precisely the original (h), with the sign in the draft correct. The canonical-subgroup uniqueness removes ambiguity in the inverse construction.

## 3. Norm equation and hull

The morphism \(\widehat A\to\widehat E\) is formally smooth. A formal-variety section through the origin gives independent formal coordinates (u) and (1+v\in\widehat F\simeq\widehat{\mathbb G}_m). No homomorphism section is required. Its norm is a principal unit (n(t,q,s,u)) with (n(t,q,s,0)=1). Katz's pushout description gives the canonical norm contribution (2c_0=q), so the affine condition is

\[
q\,n(t,q,s,u)(1+v)^2=1.
\]

The derivative with respect to (q) at the closed origin is one. Formal implicit elimination therefore removes (q), including over the nonreduced two-torsion base. One may first lift (n-1\in(u)) to a power series, eliminate (q), then impose the equation (g_E(t,s)), which is independent of (q).

Forgetting the origin is formally smooth because the lifted cover is smooth and its origin can be lifted through a small extension. Its tangent map is injective as well as surjective: changes of origin alter (c) by \((1-\sigma)d\), whose derivative vanishes in characteristic two. Marked group automorphisms reducing to the identity are trivial by rigidity. This proves the hull assertion, while allowing nontrivial higher-order actions of changes of origin.

## 4. Exact quartic and algebraization

The deformation chart (y^2+txy+y=x^3) is valid: the four coordinate-change parameters have an invertible Jacobian on the four coefficients normalized away. The remaining parameter is (a_1=t); its discriminant is (t^3-27), a unit at the closed origin.

With (s=x/y) and (w=1/y), the equation is

\[
w^2+(1+ts)w=s^3.
\]

There is a unique formal solution (w\in(s^3)). The fixed-point ideal of inversion is generated by (s(2+ts+w)); the second coordinate contributes a multiple because (w\in(s)). The exact identity

\[
(w-1)(w+2+ts)=s^3-ts-2
\]

and the fact that (w-1) is a unit give the ideal equality

\[
(s(2+ts+w))=(s^4-ts^2-2s).
\]

The latter polynomial is distinguished and monic of degree four over (W(k)[[t,u,v]]). Weierstrass division therefore gives the asserted free basis (1,s,s^2,s^3).

The algebraization does not assume effectivity of an arbitrary unpolarized formal abelian family. Both elliptic factors have actual Weierstrass families, the two-torsion point is an actual section, and the graph quotient is an actual abelian scheme. Compatible formal points near a fixed closed-fibre point are effective in an affine neighborhood over the complete base. The involution is free since its proper fixed locus has empty closed fibre. Multiplication by two factors through the graph quotient, yielding a finite isogeny to (E\times F); pulling back a product ample bundle and tensoring with its involution pullback supplies an equivariant ample bundle. The finite étale quotient is consequently an algebraized projective family.

## 5. Torsion Picard flatness and the published claim

The exact dual sequence has involution (-1) on (E^\vee) and (+1) on (F^\vee). Fppf division by two makes its fixed subgroup a torsor under (E^\vee[2]) over (F^\vee). Cyclic line-bundle descent makes \(\operatorname{Pic}^{\tau}\) a torsor under \(\mu_2\) over that fixed subgroup. The cocycle obstruction is a base unit and is killed fppf locally by adjoining a square root; an (R)-point on that torsor is neither asserted nor required. The norm identity places the descended bundle in the torsion Picard functor. Therefore \(\operatorname{Pic}^{\tau}\to F^\vee\) is finite locally free of degree eight, and it is flat over (R).

This is compatible with nonsurjective tangent maps at points on a nontrivial nonsmooth torsor. Chai's proof of Theorem 2.4(iii), pp. 6–7, infers nonflatness from unequal tangent behavior of two components related by such a torsor. That inference does not hold. The separate ordinary audit already records an explicit finite flat \(\mu_2\)-torsor displaying the claimed tangent discrepancy. The present audit independently checks the full supersingular construction; it does not promote the erroneous inference into an obstruction.

## Primary sources checked

* J. Tate, *p-Divisible Groups* (1967), §1.3–1.4, pp. 160–161; §2.2 Proposition 1 and equation (4), pp. 162–164; §2.3, p. 166. <https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf>. Opened in this review, reference `turn965698584view0`.
* N. Katz, *Serre–Tate Local Moduli* (1981), Lemmas 1.1.1–1.1.3, pp. 141–143; Theorem 1.2.1 and proof, pp. 143–146; the ordinary pushout recovery, pp. 150–152. <https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf>. Primary PDF and extracted text read directly; the full-faithfulness statement explicitly includes a specified special-fibre homomorphism and its BT lift.
* C.-L. Chai, *Mumford’s example of non-flat Picτ*, 6 March 2008, Theorem 2.4 and its proof, pp. 6–7. <https://www2.math.upenn.edu/~chai/papers_pdf/mumford_ex_v2.pdf>. Reopened in this review, references `turn965698584view1`, `turn868286625view0`.

This audit is a mathematical verification of the written proof and its source hypotheses. Finite symbolic tests support the displayed identities but do not replace the BT, descent, or deformation arguments.
