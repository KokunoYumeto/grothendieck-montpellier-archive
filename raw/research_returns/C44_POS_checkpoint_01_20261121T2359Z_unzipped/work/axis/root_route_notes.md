# Root axis route notes

GPT-6 Astra Pro; effort not exposed; C44_POS; 22 November 2026.

## Ordered route boundaries

1. A05 establishes existence of a mixed-characteristic lift of the exact embedded axis. It does not put a prescribed algebraic class into the generic Hodge filtration. Ambient nonliftable classes are removed by the A01 variable projector; no nonliftable support is being substituted for a nonliftable class.
2. H9-T13 already kills the proposed ambient elliptic tensor test. A02 extends the graph obstruction to every map to any abelian variety via Albanese factorization. A general correspondence remains possible but requires comparison of its pullback positive form with the actual signed cup product. The predecessor JAC-P20 audit already records the Milne 2022 Proposition4.2 dependency; it is not a new proof here.
3. A03 gives the correct finite-field potential-Tate-root test on even axis cohomology. Algebraic classes already have slope r=m-1. An odd-pencil Newton witness cannot eliminate them.

## New explicit-cycle attack

A04 computes a nonzero positive axis subspace from contained abelian fibres, including supersingular products. The smoothness bound N<=d_T is essential: without it the formal Gram matrix could have a negative eigenvalue, but that parameter range cannot occur for a smooth axis.

For general disjoint smooth Z_i of dimension r in X of dimension 2r+2, let a_i=(L_h^2)^(-1)[Z_i]. On a smooth axis B_N in |Nh|^2 containing the Z_i, w_i=[Z_i]_B-N^(-2)kappa*a_i has signed Gram diag(P_i(N))-(-1)^r N^(-2)G. Here P_i(N)=sum_j(-1)^j(r-j+1)N^(r-j) int_Zi c_j(N_Zi/X)h^(r-j), G_ij=int_X a_i a_jh^2. The leading diagonal is positive; therefore every fixed finite collection gives a positive definite span for sufficiently large N. This is not uniform in the cycles and does not prove the fixed-axis statement. Agent axis_independent is developing the exact quantitative version A06.

## Additional p-adic signature route under examination

Ancona Theorem8.1 and Ancona-Marmora Theorem3.2 apply to relative Chow-motive blocks equipped with a quadratic form polarizing their complex realization. For CM blocks with supersingular special fibre, the negative index is divisible by four. This could prove positivity of a suitable rank-two axis block, but A05 does not lift the necessary projector or CM action. An arbitrary Frobenius projector of the special axis has not been lifted. Hence there is presently no application to all axes.

A generic sign-change-invariant complete intersection in E^n with two divisors of multidegree (2,...,2) has large character cohomology; it does not automatically yield a rank-two block. For the all-odd sign character, equivariant Euler characteristic gives n! sum_{j=0}^{n-2} 2^j(n-j-1)/j!, e.g. 16080 for n=6, so the naive small-rank strategy fails. This numerical observation is exploratory, not an asserted theorem in the paper.

## Scaling attempt and why it does not close the gate

Pulling a fixed axis and cycle back by multiplication [N] scales both the prescribed-centre Chern bounds and the polarization. The asymptotic A06 condition is not made easier: the cycle varies with N, and all terms in its intersection comparison scale compatibly. Thus high-power positivity for a fixed centre cannot be applied to an isogeny pullback of an arbitrary fixed-axis class.
