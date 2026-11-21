# Independent complete proof review: G-18

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Review completed and recorded: 2026-11-21T03:27:01Z.

Scope: the complete revised work/root/g18_fragment.tex, including the generic-padding argument that also covers rectangular directions; its G-17 enhancement and degree-bound dependencies were previously read in full. The newly cited Mukai source passages were checked by the root agent, not reopened in this review. This is an independent-agent proof reading and rederivation, not formal verification or external certification.

## Result

**PASS.** No mathematical correction requested.

1. The weighted Fermat form has nonzero coefficients, hence is smooth in characteristic zero. Smoothness excludes both repeated components and a product of distinct positive-degree hypersurface components, since such components intersect in projective three-space. The infinitesimal stabilizer calculation uses distinct mixed monomials for \(m\ge3\), leaving only scalar infinitesimal transformations. Its projective stabilizer is therefore finite.

2. Varying the padding line while holding the nonlinear Fermat factor and auxiliary extremal vector fixed stays inside both enhanced cones. The original balanced tensor supplies a point in the stable open. The finite union of the proper fixed-point loci of the nonidentity projective Fermat automorphisms cannot contain this open. For a padding line outside that union, unique factorization forces every projective automorphism of the padded form to stabilize both factors, so its PGL stabilizer is trivial. This argument genuinely works when the auxiliary representation is trivial: it removes the earlier nonrectangular restriction.

3. If an SL4 element takes the enhanced tensor to a scalar multiple, it stabilizes the padded-form line. Thus it lies in the center. The exponent \(ns-|\eta|=4\nu_4\) makes the center act trivially on the ambient representation, so the scalar must equal one. Stability gives closed orbits for the tensor and all its nonzero scalar multiples.

4. The positive degrees of ambient invariant generators that are nonzero at the common tensor have gcd one. If the gcd were \(q>1\), multiplying the tensor by a primitive \(q\)th root would leave every generator, and therefore every invariant, unchanged. Closed-orbit separation would contradict the preceding no-scaling property. Products of these particular generators remain nonzero in both quotient rings.

5. The numerical semigroup estimate is correct. With smallest generator \(a_0\le\beta\), the residue graph modulo \(a_0\) is reachable from zero. A shortest path has at most \(a_0-1\) edges and weight below \(\beta^2\). Adding multiples of \(a_0\) covers every integer at least \(\beta^2\). This supplies common nonzero invariants in every such degree, including the \(a_0=1\) case.

6. Since \(E\ge\beta^2\), the common degrees \(E+r\) and \(2E-r\) give the claimed injections in both domains and the all-residue sandwich. I checked the degree identities exactly. The binomial ratio equals \(k(k+1)(k+2)/(u(k+u)(k+u+1))\), is at least \(k/(4u)\) for \(k\ge u+1\), and is strictly above \(Q_D\) at the displayed threshold \(k\ge4uQ_D+1\).

7. The permanent parametrization has degree \(ns+|\eta|=p\): the independent pencil and padding coefficients contribute \(n\), followed by the \(s\)th Veronese, while the independent dual matrix contributes \(|\eta|\). The image-degree argument and enlarged dimension bound yield the stated reverse threshold. The inequality \(n\ge\sqrt2m\) implies the required strict reverse comparison by a margin \(2m-3>0\).

8. Standard graded Hilbert asymptotics for the common Veronese, combined with the same sandwich in every residue, give one leading coefficient across all integers with error \(O(j^{q-2})\). The quotient formula has exponent \(v-u=c_m-2n^2+1\) and coefficient \(e(B_P)e(B_D)^{-1}(u-1)!/(v-1)!\,E^{u-v}>0\). The lower dimensions are positive, including \(\eta=0\). At exponent zero, dimension alone does not determine the gap sign.

## Occurrence corollary checked from the final statement

For a fixed partition direction with at most four rows, directions outside the strict region have no positive multiplicity gap at any stretch: use G-05 if \(\nu_4=0\), and G-14 (or the stronger G-15 strip) if \(\nu_1\le as\). In the strict region the determinant multiplicity is positive for every \(j\ge\beta^2\). Consequently no occurrence obstruction persists to arbitrarily large stretches of a fixed four-row direction. This is not a uniform bound for directions that change with the degree and does not exclude finite-degree occurrence obstructions.
