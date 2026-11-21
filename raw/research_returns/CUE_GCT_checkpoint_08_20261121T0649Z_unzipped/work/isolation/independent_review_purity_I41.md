# Independent whole-proof review of I-41

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity. Actual review completed 2026-11-21 05:53:33 UTC.

**PASS** after a complete reading and independent rederivation of `I41_weight_two_connectors.tex`, original submitted SHA256 `0a97f64199a9263a940feaaa6d7127861aa081883d081c76185d1b1693353075`. The author corrected the reported harmless `dim` typesetting typo in (I.136) before the final hash capture; the repaired display was inspected, and the observed repaired hash was `03c52ba74fa80e6fc796e771ec54be3dd9c861fbb31430e80eb751ccbff52ca5`. No mathematical repair was requested.

## 1. Factor reduction and minimal representation

The passage to an irreducible annihilated factor is valid because the rational target is a field and multilinear factors use disjoint variable sets. Specialization on all other sets preserves the width bound in the induced order. Minimum/maximum degree additivity proves homogeneity of every factor. The translated product separates into rational functions on disjoint variable sets; each ratio is scalar in E(s), and comparison of highest homogeneous parts makes that scalar one. I40 gives nonnegative factor weights, whose sum is at most the original weight after dropping unused variables. Thus an irreducible weight-two case is the only remaining one.

The fresh minimal cores, rather than an arbitrary inherited representation, are essential and are correctly used. Every interior cut has rank at least two, and the first/last one-variable cuts have rank exactly two. A rank-one strict internal interval has the cited polynomial outer factorization and would split the scalar into two nonconstant factors carrying the first and last variables, contradicting irreducibility. Hence all such intervals have rank two or three, the first/last internal factors are singular, and I40 bounds each full-rank run by two.

## 2. Canonical anchors in every characteristic

A two-factor full-rank run saturates the exact determinant budget at 0,3,6, with right determinant weight zero at its end. A zero-weight highest-weight line is group-fixed by the standard representation input, also verified in the separate Bruhat audit. Its decomposable exterior line determines its subspace, so the two bounding rank-three support spaces are SL2-stable. Contraction gives the actual neighboring support spaces, and odd tensor-power weights/Weyl pairing force them to have dimension two.

I checked the integer-character parity argument and the exclusion of weights plus/minus q with q>1: all four weights in that two-space tensor V would be nonzero and any stable subspace would have even dimension. For q=1 the standard two-dimensional module applies in arbitrary characteristic. A stable three-plane in V tensor V must contain both extreme weight lines; its unipotent orbit then forces the middle vector e01+e10. This identifies the plane as Gamma^2 V even in characteristic two.

The left anchor is exactly the displayed 2-by-3 affine matrix. Constant normalization of the two full-rank cores gives identity constant terms and only first-superdiagonal linear entries by torus weights. It does not falsely identify their unipotent modules. At the right cut the weight-two pairing is antidiagonal with three nonzero coefficients. Expanding the right Gamma^2 plane and reversing the next residual basis gives the displayed 3-by-2 right anchor. This is the actual dual pairing; Gamma^2 is never assumed self-dual in characteristic two.

## 3. Connector and all rank-preservation claims

I multiplied the canonical anchors with the unit upper-triangular middle matrix and independently obtained

`d1*d2*v^2 + d1*d3*v*(C+u) + d2*d3*(u^2+A*u+A*C-B)`.

It is homogeneous quadratic with u^2 coefficient d2*d3 nonzero. One-pole substitution gives a unique double pole at the left-anchor node; all other terms have at most a simple pole there. Thus the determinant survives in every characteristic.

Each singular factor retains rank two at its transcendental coordinate; full-rank cores have constant nonzero determinant. In the second compound, the singular factors are rank one. The pivot factorization reduces every nonzero interval product to surviving endpoint factors and scalar connectors. Zero- or one-full-rank connectors depend on at most three coordinates and use the previously checked dominance lemma. Every two-full-rank connector has precisely the saturated canonical shape just proved. Nonzero univariate pivots remain nonzero. The same formal center simultaneously preserves every interval rank; the text correctly does not claim preservation of every minor.

The endpoint simplification is valid: the first and last internal factors are rank two in the minimal representation. Pairwise dominance preserves a nonzero entry of the row/first-anchor and last-anchor/column products. Rank preservation makes the subsequent action injective on each persistent two-dimensional active space. Thus both active endpoint projections survive, without an unsupported four-variable endpoint claim.

## 4. Gauges, Hessian, and path conclusion

The cited compatible-space normalization uses only the preserved {2,3} rank profile. After endpoint shears, constants are P or I, with P at both internal ends and I-runs of length at most two. The first-derivative identities give all indicated active (1,2) zeros, and the singular affine determinant coefficient gives the passive (3,3) zero only at singular factors.

Differentiating the formally zero gradient along the one-pole parameters yields H*1=H*h=H*h^2=0 in every characteristic, with z invertible in the parameter field. Multilinearity kills the Hessian diagonal. Any intervening P kills a passive contribution, while the remaining active contribution vanishes by the triangular derivative blocks; otherwise the entry is the departure/arrival product. This gives bandwidth at most three. The Vandermonde system on at most three future columns is invertible for distinct h-values in every characteristic. Symmetry and row induction therefore make the entire Hessian zero.

In each putatively nonzero state path, the last departure from active state one before first reaching active state two has only passive stays between it and its arrival. A singular stay would already be zero. Otherwise that departure/arrival product is the relevant zero Hessian entry. Initial/final passive endpoint variants are covered by the same reasoning, and a final active-state-one output is excluded by q1=0. Thus every output path vanishes, proving the contradiction.

## 5. Ten-variable extension and finite grid

The degree interval is 3 through 7. P17 covers cubics, reversal covers degree7, and a translated quartic has only a possible cubic leading coefficient. The coefficient-matrix limit retains the width bound, so the cubic result makes the quartic translation-invariant of weight2. Reversal covers degree6. For a quintic, any nonconstant translation term has an already excluded lower degree, and its highest coefficient retains width at most three; thus the quintic is translation-invariant of weight0 and I40 applies. The lowest homogeneous-component theorem then gives the nonhomogeneous multilinear result.

The denominator-safe grid is the already reviewed I40 argument, with selector degrees at most n and three-amplitude total degree at most D. Its size and field threshold are unchanged. The new proof explicitly uses the balanced common center and does not promote itself to ordinary unweighted centered SV2 or arbitrary slopes.

## Scope of this review

I37-I40 and P17 are used at their previously independently checked scopes; the standard Jantzen representation input was freshly read during the I40 review and is not represented as new research here. I also suggested retaining the short known Bruhat/two-dimensional convention checks in the background audit to respect the manuscript's no-reproof preference. This event is a complete mathematical proof reading and rederivation, not a formal verification certificate or a historical-priority claim.
