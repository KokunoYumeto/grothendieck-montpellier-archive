# Further independent-agent plethysm checks and KL source verification

Reviewer: `/root/bridges`; model GPT-6 Astra Pro; effort inherited/undisclosed; date 20 November 2026 UTC. Reviewed the full updated proofs of PLE-F5, PLE-F6 and PLE-F7, including the new intersection-complex argument. These are independent-agent targeted proof checks, not formal certification. Earlier checks are in `cross_plethysm_review.md` and `cross_plethysm_checks.tsv`.

## PLE-F5: normality and nonsaturated weighted support

**PASS.** The proof correctly places `Frac(B)` inside `Frac(A)` for `B=A^Gamma` and `A=F[x,y]`. An element of `Frac(B)` integral over `B` is integral over `A`, hence belongs to `A`; as a fraction of invariants it remains fixed by the group, so belongs to `B`. This uses only integral closedness of the polynomial ring and does not need an unjustified equality of fraction fields.

The Hilbert function is zero only in positive degree one and positive in every degree at least two. Its support contains two and three, so generates `Z`, while `2·1` is supported and `1` is not. Normality therefore coexists with nonsaturation of this **weighted degree support**. The manuscript correctly distinguishes this projection of grading data from the full grading of a normal toric semigroup algebra.

## PLE-F6: exact rescaling classification

**PASS.** For even `q`, the interval `[0,q/3]` gives `floor(qs/3)+1`. For odd `q` divisible by three, putting `k=q/3`, the interval `[1/2,k+1/2]` has `ks+1` lattice points for even `s` and `ks` for odd `s`. Both include the value at zero.

The exclusion of higher-dimensional rational polytopes is rigorous: after clearing denominators of an affinely independent simplex, the integer barycentric points with nonnegative coefficients summing at most `t` are distinct and lie in the `Mt` dilation. Their count grows as `t^d`, contradicting the ray's linear growth when `d≥2`. A point has bounded count, so any model must have dimension one.

For odd `q` with `3∤q`, the formula extends uniquely as a quasi-polynomial to negative integers, and reciprocity would force the relative-interior count at scale one to be `ceil(q/3)` while the whole-polytope count is `floor(q/3)`. This is impossible. Relative interior, rather than ambient interior, is the correct notion and is used. The three cases exhaust all positive integers `q`. No uniform rescaling bound for arbitrary plethysm data is claimed.

## PLE-F7: ordinary compact support and point count

**PASS.** The assumption `q≡1 mod12` supplies the two roots of unity and excludes characteristics two and three. The invariant calculation remains valid in this field and after algebraic closure. The quotient morphism is finite because its two coordinate generators are integral over the invariant ring.

The Chinese-remainder interpolation and averaging argument proves that each geometric fiber is one orbit. At the sheaf level, functions on a transitive finite orbit have one-dimensional invariants; the canonical unit map is therefore the required constant subsheaf. Since `ell∤12`, the averaging idempotent splits this sheaf. Exact finite pushforward and compact-support composition then give the invariant part of affine-space compact-support cohomology. The top class of the origin is fixed by every group element, so the invariant part is the whole one-dimensional top group. Passing through the finite coefficient system is legitimate: the identified groups are finite and their transition maps are the usual surjections. All constructions are over `F_q`, preserving Frobenius.

The separate elementary point count is valid for every odd prime power `Q`, including characteristic three, where no use of the order-twelve quotient model is made. For nonzero `u`, its contribution above the constant `Q` is `−chi(u)`, and the sum of the nonzero quadratic character values vanishes. The `u=0` contribution is exactly `Q`. Thus the count is `Q^2`.

## PLE-F7: intersection-complex upgrade

**PASS.** The Jacobian has no zero away from the origin: its equations imply `Z=0`, `UV=0` and `V^2+16U^3=0`, whence `U=V=0` in odd characteristic. The origin's preimage under the quotient is set-theoretically `{0}`, as follows from `x^2y^2=0` and `x^6−y^6=0`.

Comparing the localization triangles before and after finite pushforward, and then taking the averaging summand, yields the stated local-support complex. Purity for the smooth origin in `A^2` gives `Q_l(−2)[−4]`, with invariant origin class. For `K=Q_l,X[2]`, the point stalk has only degree `−2` and the costalk only degree `+2`. Together with the smooth-locus computation, these establish perversity. The strict vanishing at degree zero rules out perverse subobjects and quotients supported at the origin, hence identifies `K` with the intermediate extension.

The shift is correct: perverse-normalized intersection cohomology with compact support is nonzero in degree two, where it is `Q_l(−2)`; ordinary compact-support cohomology is nonzero in degree four. The owner added an explicit sentence that the isomorphism extends the identity on the smooth locus, so uniqueness makes it Frobenius-equivariant. This is needed to state the Tate structure without leaving the Weil structure implicit.

The final interpretation is correctly limited: purity, normality and a positive free-module Hilbert description do not themselves force homogeneous Ehrhart counting. The example does not refute a construction that identifies each graded multiplicity space with specified cohomology and supplies the additional effective structure required by the flip.

## Exact cohomological primary locators verified

- Stacks Project Proposition 59.55.2, tag `03QP`: geometric stalks and vanishing of higher finite direct images. URL https://stacks.math.columbia.edu/tag/03QP; ref `turn339865612view0`.
- Milne, *Lectures on Étale Cohomology*, version 2.21: Theorem 16.1 (purity), Example 16.3 (affine-space acyclicity), Proposition 18.4(d) (proper-support composition spectral sequence), Theorem 24.1(a,b) (trace-normalized point class and duality). URL https://www.jmilne.org/math/CourseNotes/LEC.pdf; refs `turn339865612view1`, `turn883833682view2`–`turn883833682view4`. These statements cover the finite coefficients used in the proof.
- BBD, *Faisceaux pervers*: Corollaries 1.4.24–1.4.25, printed p.55, for the intermediate-extension criterion; equations (4.0.1)–(4.0.2), printed p.102, for middle-perversity bounds. Original scanned volume with OCR: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/BBD-pervers-2x.pdf; refs `turn195845697view0`–`turn195845697view3`. Proposition 1.4.23 on p.54 is the adjacent truncation formula, not the best citation for the no-subobject/no-quotient criterion.

## Verified KL replacement locator

Use T. J. Haines, *A proof of the Kazhdan–Lusztig purity theorem via the decomposition theorem of BBD*, author manuscript, https://math.umd.edu/~tjh/KL_purity1.pdf. Theorem 2.0.1, p.2, states odd stalk vanishing and the even-degree Frobenius eigenvalues. Theorem 5.0.4, p.7, gives

`P_(y,w)(t)=sum_i dim H^(2i)(IC(X_w))_(yB) t^i`

with unshifted intersection-complex normalization. These exact statements were read directly (refs `turn229311512view1`, `turn306079886view1`, `turn306079886view4`). They suffice for the finite-Weyl positivity claim in the split reductive setting. Do not infer Frobenius semisimplicity from the eigenvalue statement. The original KL1980 Theorem 4.3 was not directly inspected; it should not carry a source-page verification event from this reviewer.

All source checks above rechecked the statements and the aspects used by these proofs. They did not independently re-prove the full étale-cohomology, perverse-sheaf, or KL theorems.
