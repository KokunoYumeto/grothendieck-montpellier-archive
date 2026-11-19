# C25: mixed cubic extension after arbitrary quadratic choices

2026-11-19. Owner /root/automorphisms.

The complete proof is sections/B_C3_bar_arity3.tex, deliberately
kept separate from the checkpoint05 included files while they are frozen.

## Natural quotient, not a rank-one extrapolation

For U(P)=Gamma(P[2]) tensor B(Gamma(P[2])), let V3 be the arity3
part of the PD subalgebra generated in arities1,2.
C24's free signed Lyndon basis makes a given partial map through2
induce a unique well-defined map on V3. The basis need not be
simplicial: uniqueness on the intrinsic generated subalgebra
gives compatibility with all simplicial maps.

The quotient Q3=U3/V3 is, in forms3,4,5:

    T^3(P)/<abc-bac+bca> -> P tensor Gamma^2(P) -> Gamma^3(P),
    [abc] |-> a tensor bc - c tensor ab, then multiplication.

Coefficient factors are decomposable; in length2 the signed
shuffle identifies [a|b2] and [b2|a]. The form6 coefficient
Gamma^3(P) is entirely in V3 and must not be counted a second time.

For a free basis the three patterns give:

* aaa: 0 -> Z --3--> Z;
* aab: Z --(1,-2)--> Z^2 --(2,1)--> Z;
* abc: Z^2 --[[1,1],[0,-1],[-1,0]]--> Z^3 --(1,1,1)--> Z.

The last two complexes are exact, with primitive kernel columns.
Thus Q3 has sole vertical H5=P/3, naturally via
gamma3(a) |-> a mod3 and mixed products |->0.
Naturality uses the PD sum formula and n^3=n modulo3.
The argument is over Z. Over rings with 3-torsion, the aaa
two-term complex has an additional kernel in degree4, so one
must not copy this sole-homology conclusion without qualification.

## Actual extension of the prescribed mixed terms

The normalized terms of Q3 are projective. If A at weight3w is
vertically a resolution of const Z through6 and has horizontally
acyclic rows0..6, then all termwise Ext1(Q3^i,A^i) vanish.
Hence Ext1 in the abelian category of cochain complexes is
H1 of the ordinary Hom total complex.

Apply B-C2/B-C3 from B_C3_hyperext.tex to Q3[-1], supported4..6:
this H1 is Ext6_sAb(P/3,const Z).
For P=K(Z,2), N(P/3)=Z/3[2] has projective dimension3 in
Ch_nonnegative(Z), so Ext6=0.
The prescribed V3 map therefore extends strictly to U3.
All algebra/PD identities landing inarity3 were already
forced on V3, so this is the required partial PD-DGA map.

This is stronger than nullhomotopy of a standalone disk:
it retains arbitrary choices in the previous two arities.
It remains a finite-arity result, not global C3.

## Exact finite certificate

code/B_bar_arity3_checks.py
logs/B_bar_arity3_checks.json

All integer checks pass, runtime0.03768844400110538sec.
The receipt includes every shuffle relation matrix, quotient
projection and section, an explicit unimodular relation basis,
all induced differentials, maximal minors and cokernel orders.
It checks the exhaustive patterns aaa,aab,abc, not a numerical sample.

## Independent discovery and audit

Root and D independently reached the same multivariable
indecomposable complex before integration. D is now investigating
arity4; this file owns C25 and its complete certificate.
The written C25 proof was independently audited in full by root
and D. Both passed the exact quotient, natural homology,
ordinary/derived extension comparison and partial PD-map conclusion.
