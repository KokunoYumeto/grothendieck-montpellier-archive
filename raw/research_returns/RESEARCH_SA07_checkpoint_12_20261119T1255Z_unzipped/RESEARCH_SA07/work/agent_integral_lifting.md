# Fixed-field finiteness and global integral lifting

Agent: GPT-6 Astra / period_generation. Date: 2026-11-19.
This is a scratch proof/source record for the parent; no full-motive lift is claimed.

## IL-1. A finite skeleton for the fixed-field isogeny category

Let A be an abelian variety over a fixed number field k. Let I_k(A) be the
category of abelian varieties over k which are k-isogenous to A, with
k-homomorphisms, and evaluate its covariant free integral H1 at two
embeddings v,w:k -> C.

**Proved assertion.** There is a finite diagram D in I_k(A) such that
restriction gives a bijection between natural integral comparisons on
I_k(A) and comparisons on D.

Choose representatives B_1,...,B_s for the finitely many k-isomorphism
classes in I_k(A). This is Finiteness I, proved by Faltings; the opened
original Masser--Wüstholz paper states it precisely on printed p.1 and
gives its isogeny-estimate proof in Section7, pp.10--11. For each ordered
pair i,j choose a Z-basis of Hom_k(B_i,B_j). This group is free of finite
rank: after one complex embedding it injects into
Hom_Z(H1(B_i,Z),H1(B_j,Z)), because a homomorphism of complex tori is
determined by its action on the period lattice. A subgroup of a finite
free abelian group is finite free. Let D consist of the B_i and these
finitely many labelled basis maps.

For every B choose a k-isomorphism b_B:B -> B_i and set

    T_B = H1_w(b_B)^(-1) T_i H1_v(b_B).

A change of b_B differs by a k-automorphism of B_i, a Z-linear
combination of the labelled basis of End_k(B_i). Naturality for that
basis therefore proves independence of the choice. For a k-homomorphism
f:B -> C, the map b_C f b_B^(-1) is a Z-linear combination of the chosen
basis of Hom_k(B_i,B_j); the same computation proves
T_C H1_v(f)=H1_w(f)T_B. This constructs a natural integral comparison.
Its restriction is the original comparison; conversely naturality with
b_B forces this formula, so the extension is unique.

This assertion is about the entire fixed-k isogeny category in degree1.
It does not silently add all tensor powers or all algebraic cycle
operators to this finite graph. Additional finite labelled maps can of
course be included without changing the extension argument for the
isogeny category itself.

## IL-2. The full diagram over a fixed number field sees geometric quotients

This proves the exact descent direction needed to compare IL-1 with the
full pure integral correspondence diagram.

Fix embeddings v,w:k -> C and a tensor comparison T on the full diagram.
Its restriction to all finite étale schemes selects compatible maps
between geometric embedding sets. After choosing one extension of v to
an algebraic closure, these maps select one compatible extension of w.
Equivalently, in the global formulation E.2.3, T determines one
sigma in Gal(Qbar/Q) carrying v to w. Denote its actual étale transport
on the torsion of A by rho_A(sigma); for A/Q this is the usual Galois
representation.

For n>=1 and any cyclic subgroup H of A_v[n], choose a finite extension
L/k over which H is defined. Let B=A_L/H and q:A_L -> B be the quotient
isogeny. Regard B and A_L as k-schemes by composing their structural
maps with Spec L -> Spec k, and include the algebra

    A_L^0=h0(Spec L)

with its multiplication and its module actions. These are actual smooth
projective k-schemes and algebraic maps. The quotient q is a map over L,
and its graph in the open and closed diagonal component also defines the
required k-correspondence, precisely as in E.2.3.

The primitive idempotent selected by the chosen embedding L -> C picks
out A_v and B_v. Tensor compatibility on A_L=A times Spec L makes the
comparison on the A block exactly T_A. The Artin permutation carries the
selected block to the one whose kernel is sigma H. Naturality for q
therefore gives the commutative square on integral homology

    T_B q_* = (q_{sigma H})_* T_A.

Write Lambda_A=H1(A_v,Z), Lambda_B=H1(B_v,Z). The analytic torsion
identification Lambda_A/n Lambda_A -> A_v[n] sends x to x/n modulo the
period lattice. Under this identification the kernel H is exactly

    ker(q_* mod n)
      = {x mod n Lambda_A : q_*(x) belongs to n Lambda_B}.

Indeed q(x/n) belongs to Lambda_B exactly under the displayed condition.
The integral invertibility of T_B now proves

    (T_A mod n)(H)=sigma H.

This works for every cyclic H, although the field L and the underlying
k-scheme depend on H.

**All-lines lemma, with proof.** An invertible r by r matrix over Z/n,
r>=2, which preserves every cyclic subgroup of (Z/n)^r is scalar.
Preservation of each coordinate line makes it diagonal. Invertibility
makes every diagonal entry a unit. Preservation of each line generated
by e_i+e_j makes its i-th and j-th entries equal. Thus it is a unit
scalar. These scalars are compatible on reduction as n varies.

Both T_A mod n and rho_A(sigma) mod n carry every H to sigma H.
Applying the lemma to their quotient gives the exact necessary condition

    T_A tensor Zhat = rho_A(sigma) lambda_A,
    lambda_A in Zhat^times.

The scalar multiplies the entire Tate module, not separate basis
directions. This is a necessary condition for a global comparison over
the FIXED number field k, obtained through actual finite-extension
descent. It is not a transferred counterexample over Qbar.

The objects just used leave the finite category of IL-1: B as a k-scheme
has [L:k] geometric components, and in the abelian restriction-of-scalars
version its H1 has dimension 2 dim(A)[L:k]. The rational realization is
an isogeny summand of H1(A) tensor h0(Spec L). All finite Artin extensions
are present in the full diagram, with unbounded degrees. IL-1 makes the
constraints finite for each one fixed field and fixed isogeny class,
while the explicit Artin-module maps show which further constraints the
full diagram contains.

The conclusion does not assert that the quartic sigma of E.2.6 violates
this condition for any non-CM A, and it supplies no full-category
counterexample. Finding such a violation, or constructing one integral
matrix for every A compatibly with all correspondences, remains part of
the precise E.2.3(d) gate.

## IL-3. Why finite strong approximation cannot by itself finish the limit

Here is an exact algebraic-group calculation, independent of any
unproved motivic realization.

Choose the explicit a in Zhat with a_2=0 and a_ell=1 for every odd prime
ell. A rational representative would be zero from its 2-adic component
and nonzero from every odd component, so a is not rational. Put
u(a)=[[1,a],[0,1]] in SL2(Zhat). For N>=2, let K_N be the subgroup
of SL2(Zhat) which preserves every cyclic subgroup of (Z/N! Z)^2.
The all-lines lemma identifies its reduction with scalar matrices.
Every coset u(a)K_N contains an integral matrix: choose an integer
a_N congruent to a modulo N! and use u(a_N).

Nevertheless

    SL2(Q) intersect intersection_N u(a)K_N = empty.

If B belonged to the intersection, u(a)^(-1)B would be scalar modulo
every N!, hence equal to lambda I in SL2(Zhat). Thus
B=lambda u(a). The diagonal entry lambda=B_11 is rational and a
profinite unit; the upper-right entry B_12=lambda a is rational.
Their quotient would put a in Q, a contradiction.

Consequently nonempty finite congruence conditions, even in the simply
connected group SL2, do not imply a rational solution to all the
conditions at once. This calculation refutes that particular inference;
the displayed cosets are not asserted to be the motivic transporter
over the quartic field.

## IL-4. Actual maximal groups in the abelian category

The universal derived group of all polarizable rational Hodge structures
has simply connected simple factors (Patrikis, Corollary3.2, p.5).
For the abelian-motive quotient the exact representation map matters:
Milne1994 Proposition1.21, pp.15--16, computes which central characters
occur in the symplectic representations. For type D^H only the vector
fundamental weight occurs; its central character has order2, and all
abelian representations factor through the corresponding double cover
of the adjoint group. This quotient need not be simply connected.
For types A,B,C,D^R the available symplectic representations form a
faithful family of the simply connected cover.

Milne2004, Proposition3.12 and its proof pp.26--29, gives a cofinal
enlargement by actual abelian varieties in which each derived simple
factor has covering index1 or2. Its Lemma3.16 checks closure under
products using the precise derived-group maps; type D^H factors remain
the indicated double covers. Noot2006 Theorem2.9 p.14 and
Theorem2.12 pp.15--18 formulate the same maximal weak-Mumford--Tate
lifts. Noot's later simply connected geometric p-adic lifts are not
claimed there to come from abelian varieties in the D^H cases.

Thus the known quotient from the universal Hodge group to the universal
abelian-motive group does not transfer simple connectedness: its kernel
contains exactly the central characters excluded by these symplectic
representations. The precise original calculations above, rather than a
categorical separation assertion, justify the limitation.

## IL-5. Rational relative-period lifting: exact missing real point

**Superseded gate, 2026-11-19 06:56 UTC.** The missing real point
described below has now been constructed in
work/agent_real_abelian_lift.md and integrated as E.2.11, with
independent audits by elliptic_splitting and the parent. The exact
Hasse argument therefore supplies a rational abelian lift of the
prescribed CM comparison. The historical reduction below records
what had to be proved; its sentence that X(R) has not been supplied
is no longer the current status. Simultaneous integral transport
on the full geometric diagram remains unproved.

Use the absolute-Hodge abelian categories in Milne2004 and the Betti
groups

    pi:G_AV,B -> G_CM,B,
    D=ker(pi).

Theorem3.13, printed p.26, proves that D and its period-torsor twist are
countable products of simple groups of covering index1 or2. Proposition3.5,
printed p.24, and Corollary1.14, printed p.9, prove the corresponding
global H1 injection into all local H1 classes.

Our E.2.6 provides a particular rational CM point g_sigma. Its fibre
X=pi^(-1)(g_sigma) is the exact torsor whose rational point would lift
that CM comparison. At every finite prime ell, the usual Galois action
on étale cohomology, transported through Betti--étale comparison,
supplies a point of X(Q_ell). Its CM restriction is precisely
g_sigma tensor Q_ell by the s=1 formula in MilneCM2020 Theorem9.10.

We have not supplied X(R). Its obstruction is the concrete connecting
class delta_R(g_sigma) in H1(R,D); it must be checked before the cited
Hasse injection can produce a rational point. Milne2004 Remark3.31
concerns a de Rham group mapping to a twisted Artin group; its maps
have not yet been identified with this Betti-CM fibre. Even a rational
point of X would leave IL-2's simultaneous integral constraints to be
proved. No Hasse-principle statement here is being promoted to an
integral or full-pure-motive lifting theorem.

## Source access and checks

* Masser--Wüstholz, MPI/91-28, original primary PDF:
  https://archive.mpim-bonn.mpg.de/id/eprint/1497/1/preprint_1991_28.pdf .
  Opened 14-page scan; printed p.1 defines Finiteness I; Section7
  printed pp.10--11 contains the quantitative finiteness proposition
  and proof. Web refs turn707998898view0, turn655330826view0.
* Milne, Shimura Varieties and Motives, original author version:
  https://jmilne.org/math/articles/1994bP.pdf .
  Opened Proposition1.21 and proof printed p.15; rational condition
  and Lemma1.24 p.16; web ref turn655330826view2. Corrected 2018
  version Seattle2.pdf preserves theorem numbering.
* Milne, Periods of Abelian Varieties, author submitted 2002/2003
  version, https://www.jmilne.org/math/articles/2004cP.pdf .
  Opened Proposition3.5 pp.23--24, Proposition3.12 and Theorem3.13
  printedp.26, proof pp.26--29; web ref turn655330826view1.
  The later published article is Compositio Math.140 (2004),1149--1175;
  locators above refer to the explicitly consulted author version.
* Noot, Lifting systems of Galois representations associated to
  abelian varieties, author PDF dated2Oct2006:
  https://irma.math.unistra.fr/~noot/publications/pp-jrms.pdf .
  Opened Theorems2.9,2.12 and Corollary2.15, and the limitations of
  the later simply connected lifts in Corollary5.11.
* Patrikis, arXiv1302.1803v2, Corollary3.2 p.5 opened:
  https://arxiv.org/pdf/1302.1803 .

IL-1--IL-3 were proved directly above on 2026-11-19, with their scopes
kept distinct through the displayed restriction and descent maps.
No finite numerical search is used as evidence for the global integral
transporter, and no unproved lifting theorem is stated.
