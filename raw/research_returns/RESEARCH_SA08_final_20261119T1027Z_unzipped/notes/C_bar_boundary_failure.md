# C31: an admissible target with a nonextendable prescribed bar boundary

2026-11-19, agent /root/topos. Root proposed the bounded-arity admissible
strengthening of the initial vertically acyclic example. Root and B
independently audited the algebraic construction and the obstruction.

## Construction

Let k=Z_(2), P=K(k,2), and S=Gamma_k(T), with coefficient weight1.
Take the even-to-odd PD Poincare algebra

    D(P)=Gamma_k(P a) tensor Lambda_k(P x), da=x, dx=0,
    form(a)=0, form(x)=1, weight(a)=weight(x)=1.

Its parameter arity is the total number of a/x inputs. Let V be its
quotient by parameter arities at least3. This is a differential PD
quotient: d preserves arity, products add it, and higher divided powers
multiply it. Its only parameter weights are0,1,2.

At each simplex D(P) is a tensor of ordinary even-to-odd PD disks.
In every positive fixed arity the Poincare complex splits integrally:
a rank-one positive-arity piece is gamma_m(a)->gamma_(m-1)(a)x with
unit coefficient, and for a basis multidegree one contracts its first
nonzero factor. These splittings commute with arbitrary coefficient
base change. Hence V->k is universally a vertical quasi-isomorphism,
and every term is flat. The splitting need not be simplicially natural.

Let G_4 be C09's elementary source with marked generator of weight4.
It exists over k since4 is a power of2. Define

    A=G_4 tensor_k V.

The coefficient map S->A comes from G_4. This is a strict augmented
simplicial PD-DGA with flat terms and support form<=weight. Its vertical
complex resolves S in every simplex and every weight, universally,
by the two Poincare splittings. For each d, weights W>=4(d+1)+2 make
all rows A^{W,q}, q<=d, horizontally acyclic: the finite convolution
uses V-weights0,1,2, and every contributing G_4 row has weight at least
4(q'+1), where it is acyclic. Flatness and Eilenberg--Zilber preserve
acyclicity after tensoring with a V row. This verifies all generalized
admissibility hypotheses with a concrete uniform bound.

Below weight4, G_4 has only constant coefficient terms in form degree0.
In particular

    A^{2,2}=Lambda^2 P.

The map P->A^{1,1} sending a parameter to its x is simplicial and
vertically closed. It defines a map on the original odd disk of U_1(P):
send its odd x to this x and its even differential y to0.

## Failure already at arity two

In U_1(P), arity2/form2 is P tensor P, represented by words [y_u|y_v].
The product of its arity-one odd elements is

    x_u shuffle x_v = [y_u|y_v]-[y_v|y_u].

Any multiplicative simplicial extension U_1(P)->A must therefore give
h:P tensor P->Lambda^2 P with

    h(u tensor v-v tensor u)=u wedge v.

Equivalently h is a retraction of the alternating inclusion
alt:Lambda^2P->P tensor P. Such a retraction cannot exist in simplicial
modules. Eilenberg--Zilber gives H_*(P tensor P)=k[4], whereas
H_3(Lambda^2P)=k/2k is nonzero. A retraction would inject this latter
group into the zero third homology of P tensor P.

## Full finite certificate for the nonzero group

For K(Z,2), label basis elements in simplicial degree n by their two
cut positions. A pair is nondegenerate in the square functor exactly
when its cut sets cover every position. Therefore N Lambda^2 K(Z,2)
has only two nonzero terms, both Z^3, in degrees3 and4. Use bases

  degree3: 12 wedge13, 12 wedge23, 13 wedge23;
  degree4: 12 wedge34, 13 wedge24, 14 wedge23.

Literal alternating vertex deletion gives the differential

    [ 0 -1  1 ]
    [ 1  1  0 ]
    [ 0 -1 -1 ].

Its determinant is-2, and a2-by-2minor is a unit. Its Smith invariants
are1,1,2, so H3=Z/2 and H4=0. The independent value-string program
code/C_bar_boundary_countercheck.py constructs every relevant face,
checks d squared, primitive image/rank for the tensor square, the
alternating chain map, and this determinant/minor certificate. The
complete finite record is logs/C_bar_boundary_countercheck.json.
Latest successful run:0.07904140599930543 seconds. It independently
agrees with B's earlier cut-set/Smith computation.

## Exact scope

This is an actual admissible flat target over Z_(2) in which a prescribed
closed parameter of weight1 has no full bar extension, already in
arity2. It does not contradict C27--C29: the required finite row bounds
are not satisfied at that low weight. It is not a counterexample to
C3, which is proved over Z_(2). Nor does it rule out coefficient-delayed
closures, new source presentations, or different common-source methods.
It refutes the automatic source-boundary step based solely on vertical
exactness, even when eventual horizontal acyclicity is also available.
