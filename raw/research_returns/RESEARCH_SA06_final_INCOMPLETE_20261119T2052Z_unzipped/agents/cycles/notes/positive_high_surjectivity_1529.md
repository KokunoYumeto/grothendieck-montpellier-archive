# Positive-characteristic higher ordinary surjectivity: current search and method boundary

**Saved:** 2026-11-19T15:29:59Z.  **Status:** research only; no new theorem in the remaining universal range and no scheduled-review movement claimed.

The current open surjectivity range is codimension (r\geq2\), local dimension (N\geq2r+2\), beginning with ((r,N)=(2,6)\).  The newly certified integral injectivity kernels do not answer this question.  The rational ordinary group over \(\overline{\mathbb F}_p\) is zero, so a rational counterexample would require a transcendental algebraically closed coefficient field.

## 1. Existing attempts read before the new search

I read `../../real_weil/POSITIVE_HIGH_RESTRICTION_RESEARCH.md` in full, particularly its formal-versus-actual distinction, its finite nilpotent obstruction analysis, and its actual divisor-family lifting lemma.  I also reread the complete high-range complex construction `../../real_weil/C3_high_range_surjectivity.tex`, including its incidence boundary and Hodge-family obstruction, and the positive-characteristic low-range slope argument `../../real_weil/C3_positive_characteristic_low_range.tex`.

The old first-order obstruction does not transfer to positive characteristic.  In the actual high-range complex model all fixed surface divisor factors already extend through the morphism to the product of surfaces.  In positive characteristic and (N\geq4\), C.3bh gives integral surjectivity for ordinary Picard restriction.  Thus every proposed target class of the literal form

\[
\prod_i c_1(D_i|_Y)\cdot\lambda,
\qquad\lambda\in\operatorname{Pic}(Y)_{\rm alg},
\]

lifts integrally by multiplying an actual ordinary source Picard preimage by the fixed divisor extensions.  This is a direct consequence of the already proved Picard theorem and needs no inference about formal higher cycle classes.  It is a limitation of that construction, not a universal positive theorem for higher cycles.

A different attempted extension would deform a K3 factor and use its zero-cycles instead of a divisor times a Picard point.  Then the simple first-order fixed-curve cylinder has zero ordinary (H^3\) on the K3 factor, so the existing mixed first-order obstruction no longer detects it.  Detecting a generic two-dimensional zero-cycle family would require an additional actual-family descent or algebraization argument.  No such argument has been proved here; the earlier problem with varying pointed étale neighbourhoods is not being suppressed.

## 2. Freshly opened primary algebraization sources

### Lüders, 2019

Full published primary PDF opened:

<https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/2019/0026/0002/MRL-2019-0026-0002-a008.pdf>

The article is *Algebraization for zero-cycles and the p-adic cycle class map*, *Mathematical Research Letters*, 26(2), 557–585.  I read the exact setup on p.557, Theorem 1.2 on p.558, Proposition 5.1 on p.568 and the conclusion/proof of Corollary 5.4 on pp.571–572.  The base is an excellent henselian discrete valuation ring, the scheme is smooth projective over it of relative dimension (d\), and the cohomology is in top degree (d\).  The theorem proves surjectivity at each finite thickening and a pro-epimorphism.  It does not, by itself, assert that one actual object realizes an arbitrary inverse-limit system, and it does not address an arbitrary singular local base or an ordinary fixed-product family.  The Chow interpretation carries the stated Gersten hypotheses, available in the relevant equicharacteristic setting.

Opened web records: `turn601918930view0`, `turn334679264view0`, `turn334679264view1`.  The article's full idelic proof was located; this note uses only the precise theorem and hypothesis scope and does not claim a new independent re-proof of its entire argument.

### Lüders, 2020 author version

Full primary author PDF opened:

<https://arxiv.org/pdf/1810.01347>

The opened version is arXiv:1810.01347v2, 19 June 2020, *Deformation theory of the Chow group of zero-cycles*.  I read the exact global assumptions and Theorem 1.1 on author p.1, the explicit scope explanation in Remark 1.4 on p.2, and Corollary 5.5 and its proof beginning on author p.15.  Its differential-form approach assumes either (A=k[[\pi]]\) in characteristic zero or (A=W(k)\) with perfect residue field of characteristic greater than two.  Its theorem concerns top-degree thickened zero-cycles over that smooth projective DVR family.  This is not an equicharacteristic-positive-characteristic theorem for the remaining local codimension-two restriction problem.  The finite-thickening/pro-category statement is not silently strengthened to exact algebraization of a prescribed compatible sequence.

Opened records: `turn601918930view1`, `turn334679264view3`.  The published 2019 idelic theorem has the broader equicharacteristic scope; the two versions are not conflated.

## 3. Current conclusion

The new sources supply genuine finite-thickening algebraization in their top-degree smooth-DVR setting.  Neither hypothesis fits the first remaining pair without a new geometric reduction.  A cycle on the exceptional divisor is not generally a product of line bundles, and a compatible sequence of K-theory classes is not a compatible sequence of bounded coherent objects.  No surjectivity theorem, counterexample, or claim of literature-wide openness is inferred from this search.

## 4. Further attempts after checkpoint 17

**15:44 UTC; research only.** The accompanying positive_cone_codim2_cokernel.md records the exact restricted cone comparison with a global ordinary codimension-two restriction cokernel. It also records the correction from an overbroad full-Picard assertion to the sufficient reduced-Picard isogeny. This is not a reduction of arbitrary local germs.

For an ordinary codimension-two family on a regular target \(Y\), the union of its moving supports has dimension at most \(\dim Y-1\). Thus one can try to lift a divisor-sized support and apply the proved ordinary Picard theorem on that support. This does not yet work: the support is generally singular. Putting it inside a principal hypersurface and lifting its equation extends an ambient support, but does not make that hypersurface or its puncture regular. An alteration of the support need not extend to an alteration or correspondence through the source \(X\). No source establishing this missing step was found. Real-Weil independently confirmed this exact distinction.

The elementary Cayley/join shift does not turn the existing low-range generic zero-cycle examples into a high-range example. If a projective variety of dimension \(d\) contributes an ordinary cycle in codimension \(i\), the usual join/Cayley degree and dimension shifts preserve the relevant difference \(N-2r=d-2i+2\). For a top cycle \(i=d\), this difference remains in the already low range. A high-range application would first require a genuinely lower-codimension ordinary class with the needed primitive obstruction; that is precisely additional mathematical input.

Finally, a finite parameter cover can sometimes annihilate a coherent obstruction involving the parameter's \(H^1\), but it cannot annihilate a nonzero fibrewise \(H^2\) obstruction merely by base change. Conversely, replacing an actual bundle by a multiple of its \(K_0\)-class is not an operation that automatically kills the bundle's deformation obstruction. These observations prevent the finite/pro K-theory theorems from being silently promoted to actual fixed-product higher-cycle lifting. No universal vector-bundle or higher-cycle algebraization theorem is asserted.

## 5. Explicit suspension and alteration limits, 16:12 UTC

A tempting regular-source construction takes a Calabi--Yau hypersurface T in projective space and replaces it by P^m times T, retaining the nonzero ordinary target class in the Segre cone quotient. The obstruction is Cartier, not the existence of the target cycle: T's defining equation has bidegree (0,e), whereas a principal homogeneous equation on the Segre cone requires bidegree (a,a). Multiplication by a P^m section supplies that degree at the cost of a reducible divisor with intersections in the puncture. It therefore fails the required regular-target condition. The usual incidence/Cayley repair shifts codimension along with dimension and returns to the already known low interval. No high-range counterexample follows.

There is a second precise problem with a proposed alteration repair of the support method in Section 4. A proper alteration can make the divisor-sized support regular and can arrange boundary components on a regular proper model. Such a component is generally proper over the local base with a positive-dimensional exceptional fibre. It is not thereby the regular puncture of a local ring whose principal divisor is the desired support. Thus the proved local ordinary Picard theorem cannot be applied to it without a further argument. Replacing a proper alteration by an asserted finite regular alteration would be an unsupported strengthening. No actual ambient/support extension theorem was established.

The separate note positive_torsion_lifting_1606.md proves the exact divisible-group criterion for torsion lifting and records the additional coniveau, quotient and ordinary-equivalence issues in the opened torsion cycle sources. It does not identify integral and rational surjectivity unconditionally. The completed kernel results and their finite relative Milnor detectors remain distinct from this cokernel problem.
