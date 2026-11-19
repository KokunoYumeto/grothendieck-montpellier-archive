# C27: Euler contraction and all finite arities for K(Z,2)

2026-11-19. Owner /root/automorphisms.
Full proof: sections/B_C3_bar_euler.tex.

## The integral Euler homotopy

Let U(M)=Gamma(M[2]) tensor Bar(Gamma(M[2])) for free M with basis.
Its signed Lyndon generators form a free graded PD/exterior algebra.
The differential reduces bar length by1. Its explicit bar contraction
kappa preserves every basis multidegree and raises bar length by1.

For each basis variable i construct a degree-1 special PD derivation h_i
such that d h_i+h_i d=E_i (the multiplicity Euler derivation).
Set h_i(y_j)=delta_ij x_i. Induct on bar length of the other free
generators g, defining

    R=E_i(g)-h_i(dg),   h_i(g)=kappa(R).

The already established identity on lower lengths makes R closed.
It has positive arity, hence d kappa(R)=R. Although h_i(g) can use
later generators, h_i(dg) uses only earlier ones: no circularity.
The commutator of the two odd special PD derivations is a special
even PD derivation; cross terms cancel on divided powers. Equality
on generators therefore proves the identity everywhere.

The derivation preserves total arity and all lower-arity PD
subalgebras. It descends to Q_m=U_m/(lower-arity decomposables).
On basis multidegree(n_i), multiplication by each n_i is nullhomotopic.
Thus an exponent1 component is actually contractible. Summing gives
m times identity nullhomotopic on all Q_m.

Root and D independently audited this construction, including
the use of the explicit contraction, the PD commutator,
the bar-length induction and descent to Q_m.
D then read and passed the complete written proof, including
the cut-set support, projective-dimension bound, Postnikov layers,
and actual extension of arbitrary earlier partial PD maps.

## Why higher torsion does not force this obstruction

For m>1, Q_m is free and supported in form degrees m..2m-1.
Its H^m is a subgroup of a free group but is killed by m, so is0.
All other H^q have q>=m+1.

A nonzero multidegree homology component uses at most floor(m/2)
distinct parameter basis vectors, because no exponent may equal1.
For P=K(Z,2), each basis vector in simplicial degree n has a two-cut-set
label. If n>m, any collection of at most floor(m/2) labels misses a
common cut position, so its whole multidegree component is degenerate.
Therefore N H^q(Q_m(P)) is supported at horizontal degrees<=m.
Each group has Z-projective dimension<=1, giving
pd_sAb H^q(Q_m(P))<=m+1<=q.

All positive derived-Hom groups of Q_m(P) to const Z vanish, by the
finite vertical cohomology filtration. In particular the mixed
extension obstruction H1 RHom is zero. No claim that the vertical
homology itself vanishes, or occurs only at prime powers, is used.
The Q6 mixed torsion found by D is compatible with this argument.

## Actual partial PD maps

Given arbitrary choices through arity m-1, signed Lyndon freeness
gives a well-defined map on the subalgebra-generated part V_m.
The extension class of 0->V_m->U_m->Q_m->0 lies in Ext1 of
cochain complexes with target A^(mw,*). Normalized projectivity
of Q_m's terms and horizontal acyclicity split it termwise.
Use B-C2/B-C3 on Q_m[-1], supported m+1..2m: vertical resolution
through2m and horizontal acyclicity in rows0..2m identify this
class with H1 RHom(Q_m,const Z)=0.
The strict simplicial cochain extension preserves all PD/algebra
identities througharitym because their decomposable outputs lie inV_m.

Thus all finite arity stages for K(Z,2) extend, retaining arbitrary
earlier choices, whenever the finite target bounds hold. If the
bounds hold at every m for one fixed w, dependent choice gives a
full map of the bar closure. Eventuality by itself gives no such
uniform w for arbitrary arity-dependent bounds.

## Remaining C3 gates

* Prescribed parameter-boundary maps are not handled.
* Coefficient-tail delayed closures must preserve S-linearity and
  map compatibility when target bounds grow faster than linearly.
* The normalization estimate uses K(Z,2); arbitrary high-dimensional
  sphere parameters require a different bound or actual-class argument.

No new numerical test was used: the proof is an explicit general
homotopy and exact cut-set argument. The exhaustive arity3 certificate
remains in B_bar_arity3_checks.json, while D's higher torsion examples
serve as a check that no false concentration assumption was imported.
