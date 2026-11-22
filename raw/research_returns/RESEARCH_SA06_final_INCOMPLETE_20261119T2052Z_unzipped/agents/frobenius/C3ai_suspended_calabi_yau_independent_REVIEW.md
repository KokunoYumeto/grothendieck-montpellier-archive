# Independent complete-proof audit: C.3ai

**Outcome: passed.** Full typed proof read by frobenius on 2026-11-19; final certification at tool clock 09:26:20 UTC. Reviewed source file: `research/agents/cycles/suspended_calabi_yau.tex`. This review also covers its k=0 case, C.3ah, in `regular_ambient_calabi_yau.tex`.

## Statement and dimensions

For r≥1 and r+2≤N≤2r+1, the substitutions d=2r−N+2, k=N−r−2 give d≥1, k≥0, r=d+k and N=d+2k+2. The Fermat degree e=d+2 makes T a smooth Calabi–Yau d-fold. The suspended Fermat V has dimension n=d+2k. The regular ambient strict-local ring has dimension N, and its principal divisor is the strict-local cone on V.

## Integral correspondence identity

Each incidence resolution Z_i is the projective bundle of the direct sum of the tautological line on T and a trivial rank-k bundle. It has fibres P^k, dimension d+k, and codimension r in T×V. The notation with homogeneous coordinates is compatible with this bundle and does not choose a nonexistent global trivialization of O_T(−1).

For k>0, the two paired linear systems a_j=λ_i b_j force a_j=b_j=0 in their intersection, since λ_0≠λ_1. Hence the two joins meet scheme-theoretically in T. This avoids both vertices, so both incidence resolutions are isomorphisms there. Their tangent directions in the paired-coordinate 2k-space are complementary; their common tangent directions are precisely those of T. In T×V×T the intersection defining the composite is consequently the diagonal T with multiplicity one. Thus transpose(Γ_1)∘Γ_0=Δ_T integrally, not only cohomologically. For k=0 the explicit diagonal convention gives the same identity.

## Generic-point relation and Hodge contradiction

The selected P is geometric generic over Qbar and o is Qbar-rational. Their difference is represented by an actual connected proper curve family. The incidence correspondence preserves ordinary algebraic triviality; its restriction to such a parameter is a projective bundle, so there is no flat-family issue.

A hypothetical hyperplane relation can be descended from C to the algebraic closure of Qbar(T) by specializing its finite cycle/rational-function data, then to a finite field extension. Norm gives a nonzero integer multiple of the generic relation over Qbar(T). Closing the cycle β on T×V gives B of codimension r−1. Localization produces precisely

`b Γ_0 = H B + b(T × (Γ_0)_*[o]) + Θ`,

with Θ supported on a proper source divisor. In particular, the constant correspondence is not incorrectly claimed to have that support.

On H^(d,0)(T), the constant and source-divisor terms vanish. B has degree shift (k−1,k−1), so its image is H^(d+k−1,k−1)(V), in total degree n−2. If k=0 the second Hodge index is negative. If k≥1, weak Lefschetz identifies this below-middle group with projective-space cohomology, and the off-diagonal part vanishes because d>0. The explicit integral correspondence inverse forces Γ_0 to be injective on cohomology, giving the contradiction. All degrees and both endpoint conventions are consistent.

## Local passage and source vanishing

The Fermat gradient gives an isolated vertex singularity. The normal, projectively normal hypersurface cone has a section ring generated in degree one. The previously independently audited strict-cone injection C.3e therefore applies to the nonzero rational hyperplane-quotient class. Flat pullback of the actual proper curve family to the fixed puncture preserves ordinary algebraic triviality and yields a non-torsion target class.

The map C→R is geometrically regular, R is Noetherian and henselian, and the base has dimension zero. Skalit Corollary 6.4(i) therefore gives CH^r(Spec R)=0 integrally; localization gives CH^r(X)=0.

## Primary source and certificate checks

Reopened C. Skalit, *Regular morphisms and Gersten's conjecture*, arXiv:1710.00303v1, 1 October 2017, full primary PDF https://arxiv.org/pdf/1710.00303. Corollary 6.4(i), author p.27, including its hypotheses and proof via Theorem 4.5, was read. Web references: turn610205893view2, turn876918694view1. Local primary copies already exist at `research/sources/skalit2017.pdf` and `.txt`.

The owner's finite certificate reports 20 exact paired-coordinate substitution/tangent checks and 210 range/dimension/Hodge-degree checks, runtime 0.102797986 seconds, all passed. I inspected its summary and the mathematical formulas; I did not independently rerun that certificate. The proof above, not the finite range, establishes all dimensions.

No mathematical correction was required. No claim about C.3aj is inferred from this separate audit.
