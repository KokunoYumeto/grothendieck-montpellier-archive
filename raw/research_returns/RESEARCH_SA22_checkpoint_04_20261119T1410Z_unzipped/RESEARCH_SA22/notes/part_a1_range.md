# A.1 graph-range consequence of the A.2(b) proof

Owner: part_c_algebra, at root's request, 19 November 2026.

Complete proof: `sections/part_a1_range.tex`.

## Proven scope

The unbordered construction on each fixed stable graph, with the normalized marked compact components fixed or varying, external markings remaining cusps, and actual toric seam identifications as the phase variables.

For edge squared-length variables s, copy s_e to both branches of the edge, including the two distinct branches of a loop at the same vertex. If A_v denotes this incidence map and S_v the component cap potential, then

`Psi(s)=sum_v S_v(A_v s)`

has gradient `log|q_e|=log r_a+log r_b`. Its Hessian is `sum A_v^T Hess(S_v) A_v`, which is positive definite because the total incidence map is injective. Its recession function is `K_Gamma(p)=sum_v K_v(A_vp)`. The same bounded-sublevel and infinite-inward-slope proof as A.2(b) yields exact image

`{q_e nonzero : sum p_e log|q_e| < K_Gamma(p) for every nonzero p>=0}`.

Phases are independent and give a real-analytic diffeomorphism onto this proper open subbundle. The tangent map is an isomorphism. All the statements are equivariant. Radial interpolation in log coordinates to the canonical s_e=1 tensor circles gives a common strong deformation retract of this subbundle and the entire nonzero-tensor bundle. Therefore their inclusion is a homotopy equivalence and induces an isomorphism on (orbifold) fundamental groups. On a fixed normalization, this is the identity on the phase torus's Z^E.

## Smallest cases

- (0,4), two normalized spheres, one node and two cusp markings on each: exact `0<|q|<16`, since each one-active cap radius ranges through `(0,4)`.
- (1,1), rational normalization with node branches0,1 and markinginfinity: one loop edge, potential `S(s,s)`, exact `0<|q|<1`. The support at branch weights(1,1,0) is0 because the extremal half-planes each have radius1. This is sharper than the general individual Koebe bounds.

## Necessary conventions and exclusions

An actual toric seam identification has phase in S1. If fully marked Fenchel–Nielsen twists are kept in R, a full Dehn twist changes the marking but not the tangent tensor. One must quotient by the corresponding twist subgroup, or use a matching lifted phase target, to state a diffeomorphism. The text explicitly says this.

This argument alone does not identify bordered fibers with full external cap domains fixed. Holding external lengths fixed is insufficient: changing internal node lengths generally changes the external cap domains. The later `part_a1_bordered.tex` completes this issue: external-only admissibility can fail already on the four-holed sphere; the joint edge-and-leg potential gives an exact tensor/shadow range, and its uniquely reconstructed cap shapes give the full fixed-domain image criterion. The last paragraph of the range fragment now points to those proved results.
