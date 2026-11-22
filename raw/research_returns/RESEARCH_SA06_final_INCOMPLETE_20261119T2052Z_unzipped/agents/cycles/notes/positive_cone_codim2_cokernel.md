# A restricted projective cokernel inside positive-characteristic local surjectivity

**19 November 2026, 15:44 UTC. Research reduction only.** No numbered result, universal reduction, new counterexample, or scheduled-review movement is claimed. The matching kernel comparison is in Frobenius's C3_cone_codim2_kernel_RESEARCH.md; that complete note was read here.

Let \(k\) be algebraically closed of characteristic \(p>0\). Let \(V/k\) be smooth connected projective of dimension \(n\geq5\), and let \(L\) be very ample with normal, degree-one-generated full section ring \(S\). Choose a smooth connected \(H=(s=0)\in|L|\). Let \(X\) be the puncture of the vertex strict henselization of \(\operatorname{Spec}S\), and let \(Y=X\cap(s=0)\). The local dimension is \(N=n+1\geq6\).

Write \(J^2(W)=\operatorname{CH}^2(W)_{\mathrm{alg}}\), with actual fixed-product proper-curve families. Then the certified cone rigidity argument gives a natural comparison

\[
\operatorname{coker}\bigl(J^2(V)_{\mathbb Q}\longrightarrow
J^2(H)_{\mathbb Q}\bigr)
\simeq
\operatorname{coker}\bigl(J^2(X)_{\mathbb Q}\longrightarrow
J^2(Y)_{\mathbb Q}\bigr).
\]

## Exact geometry and ordinary subgroups

For the source this is the setting of C.3ax. For the target, its proof applies directly to the standard graded hyperplane quotient \(S/(s)\). One need not assert that this quotient is the full normal section ring of \(H\). The degree-one blow-up charts are the total space of \(L_H^{-1}\), the puncture is regular, the exceptional fibre is the smooth zero section \(H\), and the projection to \(H\) is an actual retraction. KST finite detection, the fixed nilpotent-thickening comparison after inverting \(p\), rational Chern character, and actual-family localization use these properties. This is the geometric argument spelled out in Frobenius's matching kernel note.

For \(W=V,H\), C.3ax's actual-family localization and its two quotient descriptions give

\[
J^2(X_W)_{\mathbb Q}
=
\frac{J^2(W)_{\mathbb Q}}
 {J^2(W)_{\mathbb Q}\cap L_W\operatorname{Pic}(W)_{\mathbb Q}}.
\]

For completeness, a class of \(\operatorname{CH}^2(W)_{\mathbb Q}\) whose punctured image is ordinary algebraically trivial has image in \(B^2(W)_{\mathbb Q}\) equal to \(L_Wb\) for some \(b\in B^1(W)_{\mathbb Q}\). Subtracting \(L_W\) times a divisor representative of \(b\) gives an ordinary algebraically trivial projective lift. This uses whole actual curve families and closure/refined fibre compatibility, not a varying henselized parameter product.

The denominator equals \(L_W\operatorname{Pic}^0(W)(k)_{\mathbb Q}\). Indeed \(L_WD\) algebraically trivial has zero \(\ell\)-adic cycle class for \(\ell\ne p\); hard Lefschetz makes multiplication by \(L_W\) injective on \(H^2(W,\mathbb Q_\ell(1))\) when \(\dim W\geq3\). The Kummer sequence and finite generation of the Néron--Severi group then give \(D\in\operatorname{Pic}^0(W)(k)_{\mathbb Q}\). The other inclusion follows from the ideal property of ordinary algebraic equivalence.

Étale weak Lefschetz on \(H^1\) identifies the reduced Picard varieties up to isogeny. Hence
\(\operatorname{Pic}^0(V)(k)_{\mathbb Q}\to
\operatorname{Pic}^0(H)(k)_{\mathbb Q}\)
is surjective (in fact an isomorphism). Consequently the whole target denominator
\(L_H\operatorname{Pic}^0(H)(k)_{\mathbb Q}\)
already lies in the restriction image of \(J^2(V)_{\mathbb Q}\).
Taking cokernels proves the displayed comparison. An injectivity assertion for multiplication by \(L\) on \(\operatorname{Pic}^0\) is not required for this cokernel argument.

## A source-scope correction retained explicitly

An initial message described full \(\operatorname{Pic}(V)\to\operatorname{Pic}(H)\) as an arbitrary-characteristic isomorphism for every smooth ample divisor. That stronger formulation was withdrawn before any theorem registration. The full primary SGA 2, Exposé XII, Corollary 3.6 was opened at

<https://arxiv.org/pdf/math/0511279>

and read on recomposed printed p.121, PDF index128 (original marginal pp.153--154). It explicitly imposes the negative coherent-cohomology vanishings on \(H\); smoothness and ampleness alone do not supply Kodaira vanishing in characteristic \(p\). The exact statement and following Corollary3.7 were read in web records turn238213028view0 and turn235768559view0. The independent current published treatment of *Lefschetz theorems in flat cohomology and applications*, Corollary3.4.5 and Example3.4.6, also retains additional hypotheses; its full HTML was opened and those passages read (turn238213028view1, turn235768559view1). None of that stronger full-Picard assertion is used above: the reduced Picard **isogeny** is sufficient.

## What this does not accomplish

This comparison embeds a global higher Chow weak-Lefschetz question in the local problem for split cones. It neither proves projective ordinary codimension-two surjectivity nor shows that arbitrary local germs reduce to these cones. The first remaining local pair \((r,N)=(2,6)\) already includes smooth projective fivefolds with smooth ample fourfold sections. A solution still needs an actual cycle-level theorem or a counterexample, not the already available formal or ordinary cohomological comparison.

