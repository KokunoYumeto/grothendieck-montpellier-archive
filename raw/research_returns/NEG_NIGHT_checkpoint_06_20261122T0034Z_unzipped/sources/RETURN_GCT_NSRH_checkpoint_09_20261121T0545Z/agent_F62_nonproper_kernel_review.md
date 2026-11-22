# Independent full review: F62 nonproper flag kernel

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited effort is not exposed. Date: 2026-11-21 UTC.

## Verdict and exact targets

**PASS.** The entire report and complete original generated fragment were read and independently reconstructed; the sole subsequent mathematical delta, an explicit proof that the outer localization triangle is also nonsplit, has been read and checked in both final files.

- Final report `agent_nonproper_torus_kernel.md`: SHA256 `b70ed1e87088267222e206f1e1fec8147f288f816846462f5d495b902f87398a`.
- Final fragment `finding_F62.tex`: SHA256 `6fd83439f9c710c3a34d8bd052a429367ed0bf0b0b38facc0605eb247c151ec8`.
- Previously whole-read targets were report `cbf501c0cfccb8b4fae051d5ba509dde74b362ecd2918e9d58592ea7f9df4934` and fragment `4215805fa8300b88769f5973833b245941de160469fe86e9978445a8ab425d43`.

This is a full proof/source-scope and report-to-fragment review, not a new compilation or visual-layout audit. No computation substitutes for the geometric argument.

## 1. Actual operation and rank-one relation

The standard kernel j_!E on pairs of distinct points of P1 is a genuine constructible object. Convolution on the product has the stated diagonal unit. Both triple products identify with the same ordered path correspondence; composition, base change and projection formula supply the actual natural identifications and their associativity coherence. The proof is not merely a calculation in trace functions.

For the square, the intermediate point avoids one endpoint over the diagonal and two endpoints off it. The diagonal family is a Zariski locally trivial affine-line bundle, with its canonical top compact Tate line. Compact base change and the open/closed triangle therefore give NP7 with the displayed shift [-2] and twist (-1).

The finite-extension count is (Q-1)h+Q times the diagonal indicator. Scaling h by v^-1, v squared equal to Q, gives T squared equal to (v-v^-1)T+1. This matches the ordinary Hecke convention; any required half step is an arithmetic coefficient choice and is not called a geometric integral Tate twist.

## 2. Torsor orientation and Chern class

Given distinct lines x,z, the decomposition k squared equal to x direct sum z makes a third distinct line the graph of a unique nonzero map x to z. This proves the actual torsor identification and fixes its line bundle as Hom(L_x,L_z)=O(1,-1), rather than its dual. The construction commutes with base change. The PGL2 description is consistent but is not needed to infer the line-bundle orientation.

I independently computed the Gysin sequence of the diagonal. Its class is h_x+h_z; the first Gysin map is injective and the top one is an isomorphism. Thus O has ordinary cohomology E in degree zero and E(-1) in degree two, with no other cohomology. In H squared with twist one, c1(L)=h_x-h_z=2h_x is nonzero. Characteristic-zero ell-adic coefficients ensure this remains nonzero in characteristic two.

## 3. Actual extension map and both nonsplittings

The compactification P(O direct sum L) uses the lines convention. Its hyperplane class restricts to zero on P(O) and to -c1(L) on P(L). The unit and hyperplane maps therefore give the exact restriction matrix [[1,0],[1,-c1(L)]]. Subtracting the first target row and changing the sign of the remaining target cancels the identity block and produces NP14. The sign change is explicitly an isomorphism of triangles, not a hidden choice of an unoriented Chern class.

The sheaf cohomology of the relative compact pushforward is E in degree one and E(-1) in degree two. The nonzero boundary in Ext squared prevents its canonical two-degree truncation from splitting.

I checked the independent ordinary-base hypercohomology certificate. In RΓ(O,-), the map from the degree-two E(-1) of E(-1)[-2] to the degree-two E(-1) of E is an isomorphism. The only remaining cohomology of K is E in degree one and E(-2) in degree four. A constant split fiber complex would instead have one line in each of degrees one through four. The dimensions two and four therefore differ. The text correctly distinguishes ordinary cohomology on the base of a relative compact pushforward from compact cohomology of the total space.

Restriction of a proposed scalar direct-sum convolution relation to O contradicts this calculation. Its pointwise trace functions can still agree at every extension; this is exactly the distinction demonstrated.

I requested the additional outer-triangle proof because the Chern class directly controls NP14 rather than NP7. The final added proof is correct: compactify Z in Y times P1, with closed boundary the union of the two sections. This boundary is proper with finite geometric fibers, so it has no higher direct images. Localization gives R squared f_!E=E_Y(-1). Splitting NP7 would decompose this as j_!E_O(-1) direct sum i_*E_X(-1), with both summands nonzero. The constant rank-one sheaf on connected Y has endomorphism ring E and no nontrivial idempotent. This proves NP7 itself nonsplit, independently of the coefficient-triangle nonsplitting. The report and fragment now keep both arguments distinct.

## 4. The source scalar factors and relative products

For two independent copies, the Tate twist (1) gives Q^-1(Q-1)^2=Q+Q^-1-2=(v-v^-1)^2. This is the exact IV c0 coefficient D-4. The objects and maps are actual products of the two torsor compact pushforwards and their localization triangles; derived tensor product supplies the signs and coherence.

The relative product is still nonconstant. Restricting one base factor to a rational point gives K tensored with the two-dimensional total fiber complex. Its ordinary-base hypercohomology has total dimension four, whereas the proposed constant four-dimensional fiber complex would have total dimension eight. Tensoring with the projective-plane cohomology multiplies both dimensions by three and preserves the contradiction.

For VIII, the chosen point object is compact cohomology of Gm squared times P2, twisted by two and shifted by one. Its trace is exactly minus Q^-2(Q-1)^2(1+Q+Q squared), matching the displayed source coefficient under the explicitly stated substitution of the deformation variable by Q. The minus sign is the odd shift and the denominator is the integral Tate twist. The positive factor v squared plus one plus v^-2 is the trace of RΓ(P2,E)(1), with its ordinary hyperplane Lefschetz maps. No identity of designated nonstandard canonical labels or unknown structure-constant objects is inferred.

## 5. Powers, tensor inverses and remaining scope

Products of the torsors carry the tensor product localization cubes. Normalizing a copies by the arithmetic line with eigenvalue q^-a/2 gives the required fiber character. For even a this is an integral Tate twist; for odd a it is only the specified arithmetic coefficient line of odd integer weight.

The finite derived tensor-invertibility obstruction is correct. Over a field total cohomology dimensions multiply under tensor product. An invertible bounded complex must therefore have one-dimensional total cohomology, while the compact torus object has dimension two, and its powers dimension two to the a. Pullback to a geometric point also excludes an inverse of the relative K. Thus scalar division is not implemented by tensor-inverting this actual object in the stated finite category.

The comparison limits are explicit: ordinary ambient convolution is constructed, while a nonstandard quadratic, canonical-label comparison, special cell-refinement operation and general normalized positivity are not. Euler vanishing at v=1 does not kill the underlying four-dimensional torus cohomology. The relative extension data and its composition compatibility cannot be replaced by an equality of traces. The compact pushforwards are mixed, so none of this contradicts the pure-point criterion or the strongest bounded ordinary-Hecke theorem.

## 6. Exact primary-source scope

In this review I reread the original local Milne text for Theorem17.10 pp116-117, Section23 pp138-140 including Theorems23.2 and23.3, and Remark24.2(b) p145. The projective bundle uses the same lines convention. The report's option to construct over the smooth projective Y and restrict to O avoids extending the stated projective-base framework without explanation. The sheaf-level splitting follows from the actual unit/hyperplane map and proper-base-change fiber check, not from a bare equality of global cohomology ranks.

The original supplied IV source text around Example19.3's c0 definition and the exact VIII Figure2 formula and surrounding signed-factor scope were reread. The VIII displayed coefficient is exactly the one claimed; no full table recomputation is asserted. The previous complete compact-support, Kunneth, Gysin and trace audits provide the remaining already inspected Milne locators.

The dictionary separates EGA locally free sheaves, actual six-operation maps, SGA5 trace formulas, symmetric coefficient gradings and virtual Euler classes. It does not assert a lambda-ring structure on a noncommutative kernel algebra, mistake equal traces for an isomorphism, or attribute this new comparison to an archive manuscript. No new archive locator is needed.

## 7. Final match record

Every proof and source qualification in the entire generated fragment was matched to the report, including the separate dictionary. The sole requested mathematical precision has now been added with a complete proof and checked at both final hashes above. No remaining mathematical correction is required.
