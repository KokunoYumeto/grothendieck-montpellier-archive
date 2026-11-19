# Ordinary pushouts do not give automatic common targets

2026-11-19. GPT-6 Astra (OpenAI), automorphisms parallel agent.
This refutes automatic admissibility for arbitrary marked choices.
It does not rule out special choices, derived pushouts, or full C3.

Let p be an odd prime and k=Z_(p). Take both target theories to be
the standard F. There are two strict simplicial PD-DGA maps from
G_p into F, described on cumulative coordinates by

$$
z\longmapsto U^{[p]},
\qquad
z\longmapsto T^{[p]}-(T-V)^{[p]}.
$$

Both have the required endpoints0,T^[p]. In higher simplicial
degrees apply the same formula to each cumulative coordinate;
the free marked-module property gives the simplicial maps.
The second formula is simply the reflected p-series, not a
nonhomogeneous perturbation. Both maps preserve weights.

Consider their ordinary PD-DGA pushout. After rationalization,
in simplicial degree one it is the relative de Rham algebra over
Q[T] of

$$
R=\mathbb Q[T,U,W]/(U^p+W^p-T^p),\qquad W=T-V.
$$

Indeed rational PD structures are the usual factorial divided
powers, so the pushout imposes the indicated degree-zero
relation and its differential. This is exactly the presentation
of the algebraic de Rham complex of the quotient ring.

Put

$$
L=U+W,\qquad
Q=\sum_{j=0}^{p-1}(-1)^jU^{p-1-j}W^j,
$$

so LQ=T^p in R. Define the homogeneous one-form

$$
\theta=T^pQ\,dL.
$$

It is closed even before inverting T. Differentiating LQ=T^p
gives L dQ+Q dL=0. Wedge with dL and multiply by Q to obtain
T^p dQ wedge dL=0, which is d theta=0. The same calculation
holds in the integral PD pushout, since the ordinary relation
U^p+W^p=T^p follows by multiplying the PD relation by p!.
The weight of theta is2p.

After inverting T, write u=U/T and w=W/T. The relative ring
is Q[T,T^-1,u,w]/(u^p+w^p-1), and

$$
\theta=T^{2p}\,d\log(u+w).
$$

The unit u+w has a logarithmic differential which is not exact.
Here is a direct residue certificate, avoiding a genus formula.
Extend scalars to a characteristic-zero field containing the
p distinct roots of -1. Compactify the curve u^p+w^p=1
with homogeneous coordinates [U':W':Z], where Z is a new
homogenizing coordinate, not the invertible coefficient T.
At a point at infinity different from [-1:1:0], choose
W'=1 and Z=t. There is a formal solution
U'=beta(1-t^p)^{1/p} with beta^p=-1 and beta not equal to -1.
Then u+w=(U'+W')/Z=(beta+1)t^-1+O(t^{p-1}), so its logarithmic
differential has residue -1. The derivative of a Laurent
series has residue zero. Hence dlog(u+w) cannot be exact.

Every T^r theta, r>=0, remains nonexact after this localization
and scalar extension. Thus the original pushout has nonzero
vertical H1 in unbounded weights. Rationalization is flat, so
the rational certificate also detects failure over Z_(p).
This holds for arbitrarily large p and already in form degree1;
it is not a high-degree p-torsion defect.

For p=2 the analogous equation is
U^2+(V-T)^2=T^2. The integral form
T^2(U dV-(V-T)dU) is closed; after adjoining i and inverting T
it is a nonzero multiple of the logarithmic differential of
(V-T)+iU. It gives the same failure.

The two marked maps are simplicially homotopic in the appropriate
acyclic mapping space. Their ordinary pushout nevertheless has
the preceding defect. Consequently a proof based on homotopy
invariance needs an actual derived PD pushout or a justified
strict replacement; the ordinary pushout cannot stand in for it.
