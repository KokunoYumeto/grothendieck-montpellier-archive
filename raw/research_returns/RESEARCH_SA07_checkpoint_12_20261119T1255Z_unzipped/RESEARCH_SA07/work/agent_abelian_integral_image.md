# Exact integral abelian image and an explicit excluded Galois element

This work note continues E.2.9 and E.2.14. It uses the same concrete
full geometric integral diagram, with all actual torsion-free Betti
lattices of abelian varieties over finite number fields, underlying-Q
schemes, Artin algebra/module maps, all algebraic correspondences,
tensor operations, and the specified direct-summand lattices. The
absolute-Hodge abelian version includes the corresponding absolute
Hodge tensors and their etale realizations. It does not equip an
arbitrary rational category with an unspecified integral model.

Let G_ab,Z be the tensor automorphism group of this Betti diagram
over Q. Restriction to the finite Artin algebras defines

    art:G_ab,Z -> Gamma_Q=Gal(Qbar/Q).

The precise Artin idempotent maps and their inverses are E.2.3.
Write I_ab for its image. The full pure integral automorphism
group restricts to this abelian diagram, so its Artin image is a
subgroup of I_ab.

## AI-1. The Artin kernel is exactly the global weight sign

There is an exact central extension of abstract groups

    1 -> {1,w} -> G_ab,Z -> I_ab -> 1,

where w acts by (-1)^m on every pure weight-m summand.
In particular every fibre over a Galois element has at most two
elements, differing by this one common sign on H_1.

Proof. For g with art(g)=1, the block descent of E.2.3 allows the
E.2.9 quotient argument on every abelian variety over Qbar:
all its geometric cyclic quotients are defined over some finite
extension, whose underlying-Q objects and Artin module maps
belong to the diagram. Hence on positive-dimensional A,

    T_A tensor Zhat = lambda_A I.

Products and the two factor injections/projections force one
common lambda for every A, exactly as in E.2.14. Since T_A is
an integral matrix, its diagonal entry is an integer n, and
all off-diagonal entries are zero by injectivity Z -> Zhat.
Its inverse is integral, so n=1 or -1. The same n applies on
every geometric embedding block. On H^r of every abelian
variety the action is n^r, because integral cohomology is the
exterior algebra on H^1. The Artin action is the identity.
Tensor operations and labelled projectors determine all
remaining components. Thus g is 1 or w.

Conversely w is an actual tensor automorphism: pure weights
add under tensor product, negate under duality, and every
morphism respects weight. It preserves every integral lattice,
fixes the Artin and Tate objects, and is natural for all
correspondences. It is nontrivial on H_1 of an elliptic curve.
The weight decomposition also makes it central. Two elements
with the same Artin restriction have quotient in this kernel,
proving the final assertion.

No finiteness or compactness of an inverse system of integral
automorphism sets is used.

## AI-2. The uniform CM-field restriction

Let Qtr be the compositum in R of all finite totally real fields.
Then

    Qcm=Qtr(i),
    I_ab is contained in Gal(Qbar/Qtr).

Consequently every element of I_ab restricts to either the
identity or the one actual complex conjugation on all of Qcm;
the same choice applies to all finite CM fields.

Proof of the restriction. For a finite totally real F and an
embedding F -> Qbar, E.2.5 supplies a finite diagram over F
which separates its distinct real embeddings. The underlying-Q
objects and Artin algebra A_F are in the present diagram.
The exact module-block construction in E.2.3 turns g with
Artin element sigma into an integral comparison of that
finite diagram at the inclusion of F and at sigma|F.
The separation statement forces sigma|F to be the inclusion.
Thus sigma fixes Qtr pointwise.

For the field equality, every finite totally real F has CM
extension F(i), so Qtr(i) is contained in Qcm. Conversely a
CM field K is a totally imaginary quadratic extension of
its maximal totally real field K+. It has a presentation
K=K+(sqrt(-delta)) with delta totally positive in K+:
take any nonzero c-anti-invariant b in K, and put delta=-b^2.
All embeddings of delta are positive. Therefore every
conjugate of sqrt(delta) is real, so sqrt(delta) belongs
to Qtr, and K is contained in Qtr(i). This proves equality.
An automorphism fixing Qtr sends i to i or -i; the latter
map is exactly actual complex conjugation on Qtr(i).
This supplies the required uniformity without choosing
independent signs for different fields.

## AI-3. Exact abelian image over Gamma_Fcm

Let Fcm be the compositum of K^ab for all finite CM fields,
as in E.2.6, and put Gamma_Fcm=Gal(Qbar/Fcm).
For an abelian variety A/Qbar, let Lambda_A=H_1(A(C),Z).
The canonical comparison

    kappa_A,n:Lambda_A/nLambda_A -> A[n](C),
    [x] -> [x/n],

and the fixed inclusion Qbar -> C define an actual map

    rho_A(sigma):Lambda_A tensor Zhat
                   -> Lambda_(sigma A) tensor Zhat.

The following equality of subsets of Gamma_Fcm is proved:

    I_ab intersect Gamma_Fcm
       = { sigma in Gamma_Fcm :
           rho_A(sigma)(Lambda_A)=Lambda_(sigma A)
           for every abelian variety A/Qbar }.

On the right, Lambda is included into its profinite completion.
Thus the condition is about an actual integral lattice, not
merely an isomorphism of profinite lattices.

Necessity. E.2.9 and the product maps give, for any integral
comparison with Artin restriction sigma,

    T_A tensor Zhat = rho_A(sigma) lambda

with one common lambda in Zhat^times. On one CM elliptic
curve C, E.2.6 gives the actual integral CM comparison alpha_C
with alpha_C tensor Zhat=rho_C(sigma). Hence
alpha_C^-1 T_C is an integral matrix whose profinite
completion is lambda I. Its integral inverse forces
lambda=+1 or -1. Thus every rho_A(sigma) is the completion
of an integral isomorphism, as required. This argument
does not prescribe the CM restriction of the putative
comparison: it proves that only the two global weight
signs of the canonical CM restriction are possible.

Sufficiency. Suppose sigma belongs to the right-hand set.
Define T_A to be the restriction of rho_A(sigma) to Lambda_A.
It is the unique integral isomorphism with the displayed
profinite completion. Equivalently it suffices to require
rho_A(sigma)(Lambda_A) subset Lambda_(sigma A): the resulting
integer matrix has determinant a unit at every prime,
so its determinant is +1 or -1 and the inclusion is onto.

For every homomorphism f:A -> B defined over Qbar, the
etale identity

    rho_B(sigma) f_* = (sigma f)_* rho_A(sigma)

restricts to the same equality of integral Betti matrices,
because the map between these finite-free Hom groups and
their profinite completions is injective. The same argument
applies to product injections/projections and all tensor
maps. On H^r use the exterior power of the H^1 map (and the
inverse-dual convention for cohomology). Its etale completion
is the actual Galois map in every degree, by the etale cup
product and the canonical exterior algebra identification.

Every algebraic correspondence has its functorial etale
cycle class, so its naturality equation holds after
completion at every prime and hence as an equation over Q
between the Betti realizations. The absolute-Hodge version
uses the same defining compatibility of its etale tensor
components. Therefore all labelled projectors commute
with the constructed maps. They preserve the specified
summand lattices: for a saturated convention use
p(V_Q) intersect Lambda, and for an image convention use
p(Lambda); in each case the equation with p gives exactly
the target lattice. Tensor and dual constructions retain
integrality.

On a finite Artin algebra use the actual integral
permutation e_u -> e_(sigma u). On underlying-Q objects
from A/L, the Betti realization is the direct sum over
u:L -> Qbar. Define its map blockwise by the corresponding
T_(u A). The A_L-module equations and diagonal tensor
projector sum e_u tensor e_u are preserved. Enlarging L
or changing a finite model gives the same maps, because
the transition maps obey the already verified naturality.
Thus the exact descent construction of E.2.3 produces
an element of G_ab,Z with Artin restriction sigma.

Since sigma fixes Qab subset Fcm, the Tate etale action is
the identity. The constructed plus comparison fixes the
single integral Tate object and agrees with canonical
alpha on CM objects by equality of their completions.
Its other possible lift is the global weight sign, by AI-1.
This proves both sufficiency and the equality of sets.

This result removes a separate tensor-coherence obligation
from the abelian subproblem once actual all-A integrality
has been established. It does not establish that integrality
for the quartic place-pair, and it does not extend an abelian
comparison to further full pure-motive objects.

## AI-4. A concrete nonliftable Galois element, also prescribing the quartic swap

Use the Q-defined elliptic curve

    E:y^2=x(x-1)(x-3)

from E.2.13. In any integral Betti basis, its 5-adic Galois
representation has image GL_2(Z_5).

Here is a complete proof of this image statement. At 3 the
given integral equation has c4=112 a unit and discriminant
576 of valuation two, so it is minimal with multiplicative
reduction. The reduction y^2=x^2(x-1) has an ordinary node
at the origin, with tangent lines split by the unramified
quadratic extension of Q_3. Over that extension it is a
Tate curve with parameter q of valuation two, because
j(q)=q^-1+744+... and v_3(j(E))=-2.

Tate uniformization identifies its 5^n-torsion with the
classes generated by zeta_(5^n) and q^(1/5^n) in
Qbar_3^times/q^Z. Over the maximal unramified extension
all prime-to-3 roots of unity and all 5^n-th roots of units
are available. The Kummer character of q is therefore
twice the tame 5-adic character of a uniformizer. Since
two is a 5-adic unit, inertia has the entire root subgroup

    U(Z_5)={ [[1,t],[0,1]] : t in Z_5 }

in a Tate basis, not only one element modulo five.

At the good prime 7, direct point counting gives #E(F_7)=4.
Its Frobenius polynomial is T^2-4T+7, with discriminant
3 modulo five, a nonsquare. Hence the representation
modulo five is irreducible. For H=rho_5(Gamma_Q), choose
g in H carrying the U-fixed primitive line to a different
line modulo five. The two fixed primitive vectors form
a Z_5-basis. In this basis U and gUg^-1 are the full
upper and lower root groups: their respective off-diagonal
parameters differ from t by a unit because the basis
determinant is a unit. Upper and lower elementary matrices
generate SL_2 over the local ring Z_5. For completeness,
an SL_2 matrix has a unit in its first column; elementary
row operations first make the top-left entry a unit,
then clear the lower-left entry and the upper-right entry.
The remaining diagonal diag(u,u^-1) is itself a product
of elementary matrices, as follows from

    U(u) L(-u^-1) U(u) = [[0,u],[-u^-1,0]]

and the same expression at u=1. Thus H contains SL_2(Z_5).
The determinant is the surjective cyclotomic character,
so H=GL_2(Z_5).

Next let N=Gamma_Qcm. Actual complex conjugation c is
central on Qcm, so [gamma,c] belongs to N for every
gamma in Gamma_Q. On T_5(E), c is an involution with
determinant -1. Since two is invertible, its projectors
(1+c)/2 and (1-c)/2 give a Z_5-basis in which c=diag(1,-1).
The already proved image GL_2(Z_5) supplies every upper
root element, and

    [U(t),c]=U(2t)

shows that rho_5(N) contains the entire upper root group.
It is normal in GL_2(Z_5), so it contains the lower root
group as well. Therefore rho_5(N) contains SL_2(Z_5).

Let N' be the closure of the abstract commutator subgroup
of N. Since Fcm/Qcm is abelian, N' is contained in
Gamma_Fcm. Compactness and continuity give the exact
image identity

    rho_5(N')=closure([rho_5(N),rho_5(N)]).

Indeed the image of N' is compact and contains every
commutator of the image; conversely every element of
N' is a limit of products of commutators and its image
is the corresponding limit. SL_2(Z_5) is perfect:
with D=diag(2,1/2), the formula [D,U(t)]=U(3t)
puts every upper root element in its commutator subgroup,
and conjugation gives every lower root element. The
generation just proved finishes. Thus rho_5(Gamma_Fcm)
contains SL_2(Z_5). Its determinant is one because
Qab is contained in Fcm, proving

    rho_5(Gamma_Fcm)=SL_2(Z_5).

Define the particular 5-adic number

    a=sum_(n>=1) 5^(n!).

It is not rational. If a=r/s with integers r,s and 5 not
dividing s, let a_N be the N-th partial sum. Then the
nonzero integer r-s a_N is divisible by 5^((N+1)!),
while its ordinary absolute value is at most C*5^(N!)
for a fixed C and all large N. This is impossible.
Consequently there is sigma in Gamma_Fcm with

    rho_5(sigma)=U(a),

and this sigma does not belong to I_ab: AI-3 would make
U(a) an integral matrix. Equivalently, AI-3 necessity
gives T_E=+/-U(a) after completion, also impossible.
The same element cannot be the Artin restriction of a
full pure integral comparison, by restriction to the
abelian diagram.

It can moreover be chosen to restrict to the required
quartic root swap. Let L be the S4 splitting field of
x^4-x-1 and H=L^(V4), as in E.2.6. The proven
intersection L intersect Fcm=H gives a surjection
Gamma_Fcm -> Gal(L/H)=V4. Its joint image with rho_5
is a closed subgroup of V4 times SL_2(Z_5) surjecting
onto both factors. Goursat's direct quotient construction
identifies any failure to be the full product with a
common nontrivial quotient of these two groups:
take the kernels of the two factor projections in the
joint image and quotient each factor by its kernel.
The first quotient is abelian, whereas the second is
a quotient of the perfect group SL_2(Z_5), so both
quotients are trivial. The joint image is the product.
Choose sigma with coordinates ((12)(34),U(a)).

To specify one such sigma completely, fix the following finite
Galois exhaustion and branch rule. Enumerate all nonconstant
integer polynomials by increasing maximum of degree and
coefficient height, breaking ties lexicographically in their
coefficient tuples. Let R_n be the finite set consisting of
all roots of the first n polynomials, all coordinates of
E[5^n], and all roots of x^4-x-1. Put Omega_n=Q(R_n).
These are nested finite Galois fields, and their union is Qbar.
Order R_n by the lexicographic order on (real part, imaginary
part) in the fixed complex embedding. This orders Gal(Omega_n/Q)
lexicographically by the corresponding permutation tuples.
Let K be the nonempty compact subset of Gamma_Q consisting of
elements fixing Fcm and having the prescribed V4 and U(a)
images. Recursively choose the first element of
Gal(Omega_n/Q) which extends the preceding choice and whose
inverse-image cylinder intersects K. Such a choice exists at
every stage. The resulting nested nonempty compact cylinders
have intersection consisting of exactly one element, because
the Omega_n exhaust Qbar. This defines the asserted sigma.
The rule uses extendibility in K and makes no computability
claim.

This excludes an actual extension of the quartic embedding
pair. It does not exclude every extension, so it does not
decide the place-pair question. In particular, the example
is not counted as a new resolution of E.2.9's necessary
Tate constraint.

## Exact sources opened and used

* Brian Conrad, Math248B Modular curves, author course PDF,
  https://virtualmath1.stanford.edu/~conrad/248BPage/handouts/modularcurves.pdf .
  Opened Section19, printedp44: Galois-equivariant Tate
  uniformization, all split multiplicative curves, and
  j(q)=q^-1+744+... . Web refs turn490780926view0,
  turn109148156view1/3. The Kummer calculation above
  derives the needed valuation-two inertia image explicitly.
* Brian Conrad and Siman Wong, Remarks on mod-l^n
  representations, l=3,5, Journal of Number Theory78
  (1999),253-270, original author-hosted journal PDF,
  https://virtualmath1.stanford.edu/~conrad/papers/remarkpaper.pdf .
  Opened printedp266/PDFindex13, including the full
  argument from Tate inertia and irreducibility to the
  two elementary root groups. Web refs turn490780926view1,
  turn109148156view2, screenshot turn681580385view0.
  The proof above uses valuation two, a 5-adic unit,
  and includes the precise Kummer calculation rather than
  silently replacing it by the source's valuation-one case.
* CM and integral comparison inputs are the exact opened
  sources and derived maps in E.2.3, E.2.5, E.2.6, E.2.9.
  No new global lift theorem is assumed.

## Scope for review

Root independent audit passed AI-1--4 on 2026-11-19 before
checkpoint05, including direct opening of Conrad Section19
p44 and Conrad--Wong pp265-266. The exact finite point count,
valuation inputs and root-group identities pass in
work/code_generation/verify_numberfield_descent.py; its output
is attached there. Proposed paper identifiers are E.2.15 for
AI-1--2, E.2.16 for AI-3, and E.2.17 for AI-4.

AI-1 and AI-2 are structural consequences for every element
of the actual abelian integral image. AI-3 proves a
necessary-and-sufficient description of its intersection
with Gamma_Fcm, including the tensor/coherence construction.
AI-4 exhibits an excluded element with the quartic swap.
The remaining main question is whether any other element
with that swap lies in the full pure integral Artin image.

## AI-5. An exact criterion for every remaining abelian Artin candidate

Proved work result, 19 November 2026, 07:54 UTC; independent audit pending.
Keep the concrete full geometric integral diagram and all coefficient
conventions of AI-1--3.

Let

  D=mu_2(Zhat)={lambda in Zhat^times : lambda^2=1}
    =product over primes ell of {1,-1},

and put

  Sigma = {sigma in Gamma_Qcm : there exists lambda in D such that
            lambda rho_A(sigma)(Lambda_A)=Lambda_(sigma A)
            for every abelian variety A/Qbar}.

Then the full abelian Artin image is exactly

  I_ab = Sigma disjoint-union c Sigma,

where c is the fixed actual complex conjugation. The lattice equality
in this definition may be replaced by inclusion. For each sigma in
Sigma the sign pattern lambda is unique modulo the one diagonal
global sign {1,-1}. There are precisely two integral abelian lifts
of each such sigma, as in AI-1.

### AI-5.1 Necessity, including the common sign pattern

AI-2 shows that any sigma in I_ab restricts to 1 or c on all Qcm.
The actual analytic conjugation maps on the Betti groups of all
Q-defined schemes give an integral tensor automorphism with Artin
restriction c: on an underlying-Q object they conjugate the complex
variety and carry the u-component to the cu-component, and the
ordinary functoriality of singular cohomology respects every
Q-defined correspondence, cup product and labelled Artin algebra.
Its square is the identity. Composing with it reduces the remaining
case to sigma in Gamma_Qcm.

For such sigma, E.2.9 and E.2.14 give one common
lambda in Zhat^times with

  T_A tensor Zhat = rho_A(sigma) lambda

on every geometric H1 block, where T_A is the covariant homology
component of the given comparison.

Take the fixed CM elliptic curve C:y^2=x^3-x over Q and its labelled
endomorphism [i]:(x,y) -> (-x,iy), defined over Q(i). The field
Q(i) is contained in Qcm and is fixed pointwise by sigma.
Thus the Artin-selected component T_C is an integral automorphism
of the same lattice Lambda_C commuting with [i]_*.
This lattice is a rank-one torsion-free module over Z[i]; the
Euclidean property of Z[i] makes it free. In a basis (e,ie),
the matrix of [i]_* is J=((0,-1),(1,0)). Solving TJ=JT gives

  T_C=((r,-s),(s,r)), r,s in Z.

Its determinant is r^2+s^2. Since T_C is unimodular, this
nonnegative integer is 1, so det(T_C)=1.

Every root of unity lies in Qcm: cyclotomic fields are CM for
orders greater than two, and the remaining roots are rational.
Consequently the cyclotomic character chi(sigma)=1. The Weil
pairing identifies det rho_C(sigma) with chi(sigma), so taking
determinants in the completed comparison gives

  1=det(T_C)=lambda^2 det rho_C(sigma)=lambda^2.

This proves lambda in D and the claimed lattice condition.
The same determinant argument, or the principal polarization
identifying exterior-square H1(C) with the integral Tate line,
also proves that the given comparison fixes the Tate object.
No separate positivity or real-Hodge assumption has been added.

### AI-5.2 Sufficiency with all signs and all correspondences

Let sigma and lambda satisfy the displayed definition of Sigma.
Define T_A to be the restriction of lambda rho_A(sigma) to the
actual Z-lattice. An inclusion already yields a unimodular
integer matrix: its completion is invertible at every prime,
so its integer determinant is a unit at every prime and hence
is 1 or -1.

For a homomorphism f:A -> B, the completed naturality equation
is

  (lambda rho_B(sigma)) f_*
    = (sigma f)_* (lambda rho_A(sigma)).

It therefore holds on the actual lattices, by injectivity of
integer matrices into their profinite completions. Product
inclusions and projections, finite-model changes and all
extension-field Artin module maps satisfy the same equations.

For contravariant cohomology use exactly

  eta_A=(T_A^{-1})^vee.

If g_A denotes the actual completed Galois map on H1-homology,
its cohomology map is (g_A^{-1})^vee. Hence eta_A has completion
lambda^{-1}(g_A^{-1})^vee. Since lambda^2=1, lambda^{-1}=lambda.
On H^r(A), compatibility with exterior powers and cup product
gives the actual Galois cohomology map multiplied by lambda^r.
Define the Tate component to be the identity, and the Artin
component by e_u -> e_(sigma u).

An algebraic correspondence of codimension d+j from a
d-dimensional abelian variety carries H^r into H^(r+2j),
with the corresponding Tate twist when expressed as a
weight-preserving motivic map. Its source and target factors
are lambda^r and lambda^(r+2j), which agree because
lambda^2=1. Its actual etale cycle class already satisfies
Galois naturality. Thus the constructed completed maps
satisfy the precise correspondence equation, which descends
to the rational Betti equation by faithful completion.

The same check covers tensor words, duals and Tate twists:
the parity of the number of H1 factors equals their weight
modulo two; Tate twists change weight by an even integer.
Every homogeneous motivic correspondence has equal weight
on source and target, so the two lambda factors coincide.
In the absolute-Hodge abelian version, the defining etale
tensor components give the same equation, and each
weight-zero tensor has an even number of odd-weight factors.
All specified integral maps remain integral because their
component maps have already been constructed over Z.

For labelled projectors p, commutation with p carries the
saturated lattice p(V_Q) intersect Lambda onto its target,
and likewise carries the image convention p(Lambda) onto
its target. Tensor products and duals preserve these
integral maps. For a finite model A/L, use the maps T_(uA)
on the direct-sum blocks indexed by u:L -> Qbar. Together
with e_u -> e_(sigma u), these preserve the Artin algebra,
its module maps, and the diagonal tensor projector
sum e_u tensor e_u. The construction is independent of
the finite model by the homomorphism/correspondence
naturality just checked. E.2.3 now descends the maps to
an actual element of G_ab,Z with Artin restriction sigma.

The ordinary Tate comparison has cyclotomic scalar 1 for
sigma, and the lambda factors have even degree, so the
declared identity Tate map is compatible with every
polarization. This completes sufficiency on the full
specified geometric abelian diagram.

Multiplication by the actual conjugation comparison supplies
the second coset c Sigma. These cosets are disjoint because
c acts nontrivially on i in Qcm. Conversely AI-2 and the
necessity argument put every element in one of them.

### AI-5.3 Uniqueness and the exact residual scope

If lambda and mu both satisfy the criterion for the same
sigma, their constructed integral comparisons have ratio
with trivial Artin restriction. AI-1 makes that ratio
the identity or global weight sign. On any positive-rank
H1 block this says mu/lambda=1 or -1 as one element of
Zhat, rather than an independently chosen sign at each
prime. Thus the class

  delta(sigma)=[lambda] in D/{global 1,-1}

is determined by sigma. Composition of the actual completed
maps shows delta is a group homomorphism on Sigma:
rho_(tau A)(sigma) rho_A(tau)=rho_A(sigma tau), and
the scalar factors multiply. This does not require an
inverse-limit lifting theorem.

For sigma in Gamma_Fcm, the canonical integral CM comparison
of E.2.6 makes lambda a global sign by the CM-anchor argument
of AI-3. Thus this criterion specializes exactly to E.2.16.

This result characterizes all abelian Artin candidates,
including their only possible local sign ambiguity. It
does not prove Sigma={1}, identify a nonidentity element
of Sigma swapping the quartic places, or extend any such
abelian comparison to the full pure diagram. The main
full-pure separation question remains open. In particular,
this refinement is not itself counted as main-gate movement
at the 07:55 review.

## AI-6. Ring-class restrictions and an actual non-global local sign for one CM field

Proved work result; independent audit requested. This is a scoped result
about the geometric diagram generated by all elliptic curves with one
fixed imaginary-quadratic CM field, together with all Artin objects.
It does not assert that the constructed element belongs to Sigma of
AI-5, which tests all abelian varieties.

### AI-6.1 The additional restriction already supplied by ring-class tests

Every sigma in Sigma fixes every imaginary-quadratic ring class field
pointwise. Indeed, let R=K(j(E)) be any such field. The labelled finite
diagram in E.2.2 is a diagram over R. View all its objects as underlying-Q
schemes, add the Artin algebra A_R and its module maps, and select the
identity embedding block. A global integral comparison with Artin
restriction sigma sends that block to the sigma|R block by E.2.3.
E.2.2 forces sigma|R to equal the identity or actual conjugation.
Since sigma fixes K contained in Qcm and c acts nontrivially on K,
only the identity remains.

Let R_all be the compositum of these ring class fields and Qcm.
Thus Sigma is contained in Gamma_R_all. This is an explicit
Artin-block consequence of the previously proved separating
diagrams, not a passage from ring class fields to all ray fields.

### AI-6.2 Exact intersection for one imaginary-quadratic field

For every imaginary-quadratic K,

  K^ab intersect Qcm = Qab.

First Qab lies in K^ab because K/Q is abelian, so adjoining K
to an abelian Q-extension remains abelian over K. It also lies
in Qcm, since every cyclotomic field is CM (apart from the
rational cases) and Qab is their union.

For the reverse inclusion put L=K^ab intersect Qcm. Both fields
are Galois over Q, so L/Q is Galois. The group
G=Gal(K^ab/Q) has the abelian index-two subgroup
A=Gal(K^ab/K), and actual c has order two and lies outside A.
Thus G is generated by A and c. Complex conjugation is central
on Qcm, so its image is central in the quotient Gal(L/Q).
The image of A is abelian; centrality of c therefore makes
the whole quotient abelian. Consequently L lies in Qab,
proving the equality.

This proof also specifies the actual field map relevant below:
the restriction Gal(K^ab/K) -> Gal(Qab/K) corresponds under
global class field theory to the idele norm K -> Q.

### AI-6.3 A fixed non-global scalar and a genuine Galois extension

Take K=Q(i), and define lambda in mu_2(Zhat) by

  lambda_5=-1,   lambda_ell=1 for every prime ell other than 5.

Use its scalar image s in A_(K,f)^times, and set its infinite
component to 1. Define

  g_K=Artin_K(s) in Gal(K^ab/K).

The idele norm is exactly 1: at each rational prime ell the
product of the local scalar norms is lambda_ell^[K:Q]
=lambda_ell^2=1, and the infinite norm is 1. Compatibility
of Artin maps with norms gives g_K|Qab=1.

By the intersection equality, g_K and the identity on Qcm
agree on K^ab intersect Qcm. They extend to an automorphism
of K^ab Qcm which is g_K on the first field and the identity
on the second. Extend it to Qbar. Thus there exists an actual
sigma in Gamma_Qcm with sigma|K^ab=g_K.

To specify one extension without a choice parameter, use the
fixed finite Galois exhaustion Omega_n and ordered Galois
groups from E.2.17. The compatible-extension set just proved
nonempty is compact. Recursively take the first restriction
to Omega_n extending the previous choice whose cylinder meets
this set. The nested cylinders define one sigma. No
computability assertion is made.

The element g_K is nontrivial. For the ray modulus (15), the
class of s in (Z[i]/15)^times is the rational class 4:
it is 1 modulo 3 and -1 modulo 5. The exact ray-class
sequence has kernel the image of Z[i]^times={1,-1,i,-i}.
Only the unit 1 is 1 modulo 3, and it is not -1 modulo 5.
Thus the class of s is not in that kernel, and its Artin
action on the modulus-15 ray class field is nontrivial.
In particular sigma is not in Gamma_Fcm.

On the other hand g_K fixes every ring class field of K.
For the order O_f=Z+f Z[i], the scalar idele s belongs to
the subgroup of local units hat(O_f)^times. Equivalently,
in Cox's ideal description the congruence of s modulo f
is a rational unit, which is killed by the subgroup
P_(K,Z)(f) defining the ring class quotient. Its image in
Pic(O_f) and hence in the corresponding ring class Galois
group is trivial for every f.

### AI-6.4 The actual comparison on the entire fixed-K CM diagram

Let A/Qbar be any elliptic curve with End^0(A)=K, with an
arbitrary labelled embedding of K into its endomorphisms.
The two possible CM types have reflex field K; their reflex
norm maps are the identity and conjugation. Both send the
rational scalar idele s to the same lambda.

Milne CM2020 Theorem9.10, printedp78, applies to the actual
sigma chosen above and s, and gives a unique K-linear
quasi-isogeny alpha_A:A -> sigma A satisfying

  alpha_A(lambda x)=sigma x for every x in V_f(A).

Thus alpha_A on completed homology is precisely

  alpha_A^hat = rho_A(sigma) lambda^{-1}
              = lambda rho_A(sigma).

This is an isomorphism of actual Tate lattices. To see that
alpha_A is an actual isomorphism of abelian varieties, write
alpha_A=f/m with f an honest homomorphism. Tate-integrality
at every prime dividing m implies f kills A[m], so f
factors through [m] and alpha_A is an honest morphism.
The inverse has the same integrality and is also honest.
This is exactly the E.2.6 quotient argument, now with the
explicit non-global scalar present.

There is no dependence on the choice of the labelled copy
of K: the two reflex norms give the same scalar lambda,
and completed homology determines the quasi-isogeny.
For any homomorphism f:A -> B between fixed-K CM elliptic
curves, the identity

  alpha_B f = (sigma f) alpha_A

holds after completion by Galois naturality and cancellation
of the one scalar lambda, and therefore holds as an actual
homomorphism. On products take products of alpha_A; the
same identity treats isogenies, their quotient lattices,
all factor maps and any repeated or conjugately labelled
CM types. For any further actual abelian lattice in the
K-isotypic isogeny class, the same quasi-isogeny formula,
or naturality for a chosen isogeny followed by the
Tate-integrality argument, constructs its integral map.

For cohomology take inverse duals. The completed map on
degree r is the actual Galois map multiplied by lambda^r.
Every algebraic correspondence shifts degree by an even
integer, so its two scalar factors agree. Its etale
cycle-class equation gives the exact Betti naturality.
The same proof covers absolute-Hodge tensors in this
abelian diagram, tensor words, duals and all specified
projector lattices. Norm(s)=1 and chi(sigma)=1 also give
polarization multiplier 1 directly from Milne
Remark9.11(c), p78. Tate is fixed.

Finally include ALL finite Artin schemes, with maps
e_u -> e_(sigma u). For a fixed-K CM object defined over
an arbitrary finite L, its underlying-Q realization is
the sum of its u-components. Each uA is still a K-CM
curve, because K/Q is quadratic and is stable under
every embedding; its type may be either of the two
already treated. Use alpha_(uA) on the u-block, landing
in the sigma u-block. The preceding naturality verifies
every Artin module action and every defining morphism,
and the idempotent diagonal sum e_u tensor e_u is
preserved. Changes of finite model commute by the
same equations. E.2.3 therefore gives one genuine
integral tensor comparison on the full fixed-K CM/Artin
diagram, with Artin restriction sigma and local sign
pattern lambda.

This is an actual non-global sign example, not merely
a collection of local lattices. It shows exactly why
the fixed imaginary-quadratic CM subcategory and its
ring class fields do not suffice to replace the local
sign pattern by one global sign. No comparison on
all other CM types, all abelian varieties, or the full
pure category has been constructed here.

### AI-6.5 Primary source check

Milne, Class Field Theory v4.03 (6August2020), full
296-page author PDF reopened at
https://www.jmilne.org/math/CourseNotes/CFT.pdf .
TheoremV.1.7 with proof, printedpp150-151, gives the
exact global-unit kernel in the ray-class sequence.
PropositionV.5.2 and the norm-compatibility diagram
immediately after its proof, p178, and TheoremV.5.3
pp178-179 give the Artin map and the norm/restriction
identity. Exact web refs turn422291376view0 and
turn422291376view2.

Milne CM2020 local primary Theorem9.10 and
Remark9.11(a)-(c), printedp78, reread in full;
the normalization is alpha(N_Phi(s)x)=sigma x.
The two-type substitution N_Phi(lambda)=lambda
has been made explicitly. Cox1989 Theorem9.18
pp190-192 supplies the ring-class ideal congruence
quotient already opened and visually checked for
E.2.4. No unverified statement about all ray fields
has been substituted for that ring-class quotient.
