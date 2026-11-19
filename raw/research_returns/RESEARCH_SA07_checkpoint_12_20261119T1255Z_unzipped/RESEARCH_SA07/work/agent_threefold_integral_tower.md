# Integral comparison on all threefold and CM geometric factors

Date: 2026-11-19. Agent: period_generation.
Status: proved and integrated as canonical E.2.26. The complete T3-1--T3-5
construction and all required primary-source maps have passed independent
root and elliptic_splitting audits. The full pure-category separation gate
remains open; this result has the precise dimension-at-most-three plus
all-CM scope stated below.

## T3-1. Exact arithmetic groups and sources

We retain the fixed embedding Qbar into C, the field Fcm, the quartic
splitting field P of x^4-x-1, and the element t0=(12)(34) of Gal(P/Q)
specified in E.2.17. In particular Gamma_Fcm maps onto the V4 subgroup of
Gal(P/Q). All Tate modules below are covariant homology Tate modules;
the Betti lattice is H_1(A(C),Z). Cohomology is its inverse dual.

For a geometrically simple non-CM abelian threefold A, the possibilities
for its geometric endomorphism algebra and its connected derived
Mumford--Tate group H_A in its actual H_1 representation are:

1. End^0(A)=Q: H_A=Sp(V_A,psi_A), of type C3.
2. End^0(A)=F a totally real cubic field: V_A has F-dimension two,
   psi_A=Tr_F/Q(Psi_A) for the unique F-alternating form Psi_A, and
   H_A=Res_F/Q SL_F(V_A).
3. End^0(A)=E an imaginary quadratic field: V_A has E-dimension three.
   For a fixed nonzero a in E with bar(a)=-a there is a unique Hermitian
   form h_A satisfying psi_A=Tr_E/Q(a h_A). Its signature is (2,1), up
   to interchange, and H_A=SU_E(V_A,h_A).

The remaining simple threefold case is a sextic CM field and is already
in the all-CM scope. These are actual embedded groups, rather than only
isogeny types. Moonen--Zarhin, arXiv math/9901113v2, Section2.3 and
Proposition2.4, author p9/PDF index8, explicitly gives this classification,
the trace-form identifications, Hg=U in the imaginary quadratic case,
and its signature (2,1). Section2.7, author p10, states Hg=the
endomorphism/polarization centralizer in prime dimension. The preceding
surface cases retain the exact groups and forms of E.2.25.

Each H_A is semisimple simply connected. All its Q-simple factors have
noncompact real points: Sp6(R), SL2(R)^3, and SU(2,1), respectively.
The full MT group in case3 is GU_E(V_A,h_A), because it contains the
Hodge group U and the rational scalar torus, and their product has the
same dimension ten as the connected group GU.

The arithmetic equality needed here is

    G_l(A)^0 = MT(A)_{Q_l}

under the actual Betti--etale comparison. The opened original arithmetic
source is Tankeev, *Cycles on simple Abelian varieties of prime dimension
over number fields*, Math. USSR-Izv.31(3)(1988),527--540. Theorem1 is on
p528 and assumes prime dimension d unequal to7. Its proof, Lemma3 and
the cases on pp532--539, gives the required semisimple dimensions:
8 in the imaginary quadratic threefold case,9 in the real cubic case,
and21 in the End^0=Q case. The natural inclusion of the arithmetic Lie
algebra into the MT Lie algebra is explicitly used on p532 and p533.
The imaginary quadratic full equality on p535 has the stated additional
hypothesis c_l^0 nonzero; we do not omit that hypothesis.

Here is an exact completion of the center step. Commelin2019,
Lemma4.18 and its proof, printedpp658--659, gives under the comparison

    Z(G_l(A)^0)^0 = Z(MT(A))^0_{Q_l}.

Its proof uses actual maps. By Faltings, the centralizer of G_l(A)^0 in
End(V_l(A)) is the geometric endomorphism algebra; this yields the
inclusion of centers into the MT center (Lemma4.15). A faithful
representation N of MT(A)^ab is an abelian CM motive, by the full Hodge
realization theorem4.13 and Section4.16. Commelin takes a finitely
generated definition extension; its arithmetic image is MT(A)^ab,
by the CM MT theorem in Lemma4.17. The connected arithmetic image of
the original motive is unchanged: the algebraic part of a finitely
generated extension of a number field is finite, and regularity over
that algebraic part makes restriction of absolute Galois groups
surjective onto its Galois group. The resulting image in the original
arithmetic group therefore has finite index. Thus the map
G_l(A)^0 -> MT(A)^ab is surjective, proving
equality of connected centers. In the imaginary quadratic threefold
case this center has dimension two, so c_l^0 has dimension one and the
qualification in Tankeev p535 is fulfilled. In each of the three cases,
the natural inclusion of connected groups has equal Lie dimension and
therefore is equality. This verifies full arithmetic MT before the
adelic theorem is invoked. Lombardo2015, Theorem2.18, printedp6, is a
separately opened explicit statement of the same prime-dimensional MT
conclusion.

There is also a direct determinant check on this center calculation.
After extending the model field k to contain E and define its action,
Fite--Goodman2026, Theorem3.1, authorpp9--10 (equivalently Theorem1.1(i),
p2), constructs a CM elliptic curve B/k and gives, for each lambda|l,

    (Lambda^3 V_lambda(A) + Lambda^3 bar(V_lambda(A)))(-1)
       = V_l(B) tensor_Q_l E_lambda.

Here the plus sign denotes direct sum, and bar(V_lambda) is the
coefficient-conjugate character defined on p2 of that source. Thus the
two determinant characters are the two CM elliptic characters multiplied
by the common cyclotomic character. On Res_E/Q G_m the resulting torus
map is t -> t Norm_E/Q(t); over a splitting field its character matrix
is [[2,1],[1,2]], of determinant3. It is an isogeny of a dimension-two
torus. The actual CM theorem therefore gives dimension two for the
determinant image. This direct arithmetic map confirms the central
dimension; no motivic isomorphism is inferred merely from this Tate
isomorphism.

For every finite family of these abelian varieties (and surface/elliptic
factors), arithmetic MT holds for the product by Commelin2019,
Theorem10.5, printedp676. This statement identifies the actual joint
group. It does not assert that the joint group is the full product.

## T3-2. The actual joint derived group and its projection kernels

Let V be the direct sum of a finite family of the preceding non-CM
factors, let M=MT(V), and let H=M^der. There are surjective projections
M -> M_i and hence H -> H_i=M_i^der. The representation on V gives a
closed embedding H into product_i H_i. Thus H is a connected subdirect
subgroup of a product of semisimple simply connected groups.

We prove that H is simply connected. Over Qbar take the universal
cover pi:H^sc -> H and decompose H^sc into simply connected absolutely
simple factors S_j. For each absolutely simple factor T of any target
H_i,Qbar, the composite H^sc -> T is surjective. The images of the S_j
are commuting connected normal subgroups of T. Exactly one image can
be nontrivial, and its map S_j -> T is a central isogeny. Since T is
simply connected, that map is an isomorphism. Every S_j must map
nontrivially to at least one target T: otherwise its positive-dimensional
image under pi would be killed by the faithful embedding
H -> product H_i. Every element of ker(pi) therefore has trivial
coordinate in every S_j, since its image in the target attached to that
coordinate is trivial. Hence ker(pi)=1. This descends to Q.

Each Q-simple factor S of H maps nontrivially to some Q-simple H_i.
The map is surjective, because the image is connected and normal and
the projection H -> H_i is onto. Q-simplicity makes its kernel finite;
simple connectedness of the target makes it an isomorphism. Consequently
every Q-simple factor of H has noncompact real points and is one of the
explicit forms listed above or in E.2.25.

Let H_n be the joint derived group of the first n selected generators,
with H_0=1. The forgetting map p_n:H_n -> H_(n-1) is surjective. Over
Qbar it discards a subset of the simple factors of H_n and maps each
remaining factor isomorphically to one target simple factor. The kernel
factor set and its complementary factor set are Galois stable. Thus
there is a Q-defined direct product decomposition

    H_n = L_n x C_n,
    p_n|C_n:C_n -> H_(n-1) is an isomorphism,              (T3.1)

where L_n=ker(p_n) is connected semisimple simply connected. Write
j_n for the inverse isomorphism followed by C_n -> H_n. This gives an
actual rational section. Each Q-simple factor of L_n has noncompact
real points. The assertion includes L_n=1. This exact splitting is what
allows the subsequent approximation to preserve previously chosen
matrices even when the joint group has diagonal factors.

## T3-3. Independently supported derived subgroups in the arithmetic image

For a finite product A choose a number field k defining its models and
endomorphisms, and enlarge it so that every G_l(A) is connected. Such a
single extension for all l is the connectedness statement recalled in
Cadoret--Moonen Section1.1. Under MT, Cadoret--Moonen TheoremA(i), with
its definition in Section1.3, says that each image G_l is open in
M(Z_l), and for all but finitely many l it contains the commutator
subgroup of M(Z_l). All integral group schemes here are the closures
in the actual Betti lattice; outside a finite set they are the usual
smooth reductive models.

Serre2013, Theorem1 and Section3.1, printedpp544--545, applied to the
Tate modules of this product, gives a finite extension k'/k with

    rho(Gamma_k') = product_l rho_l(Gamma_k').            (T3.2)

The equality is in the actual profinite product, not just a statement
about each projection. Apply the integral MT theorem to this new field
as well. If k' is enlarged to a finite Galois field K/Q, its image is a
closed finite-index subgroup of the compact product in (T3.2), and is
therefore open in that product. It consequently contains a product of
open local subgroups which equals the full local image outside a finite
set. At a good prime l>=7, the group H(Z_l) is perfect, as proved below,
so

    H(Z_l)=[H(Z_l),H(Z_l)]
       is contained in [M(Z_l),M(Z_l)] and in G_l.

At the finitely many remaining primes, intersection of a local open
subgroup of M(Q_l) with H(Q_l) is open in H(Q_l). We have therefore
proved the following actual containment:

    rho(Gamma_K) contains a compact open product W in H(A_f),
    W_l=H(Z_l) outside a finite set.                     (T3.3)

Each element of W supported at any chosen local simple factor has an
actual preimage in Gamma_K. No assertion that M itself is adelically
open, or that its central torus is Hodge maximal, is needed.

### T3-3a. The finite and integral group facts at good primes

The reductions of the local simple factors are SL2(F_q), Sp4(F_l),
Sp6(F_l), SL3(F_l), or SU3(F_l). For l>=7 their projective quotients
are simple and their full groups are perfect. The opened primary
matrix proofs are Taylor, *The Geometry of the Classical Groups*,
Theorems4.4--4.5 for SL,8.7--8.8 for Sp, and10.15 for SU3 (the last
on printedpp122--123). The proof of10.15 explicitly shows that the
unitary transvections generate SU3 and that SU3 is perfect.

If a normal subgroup of any of these finite groups contains a
noncentral element, its image in the simple projective quotient is
the whole quotient. The remaining quotient is a quotient of the
center, hence abelian. Since the full group is perfect it has no
nontrivial such quotient, and the normal subgroup is the full group.

We give the needed lifting argument for SU3. Let O be the unramified
quadratic extension of Z_l, with involution bar, choose a trace-zero
unit theta, and use the Witt Hermitian matrix

    J = [[0,0,1],[0,1,0],[1,0,0]].

The upper unipotents are

    Q(a,b)=[[1,-bar(a),b],[0,1,a],[0,0,1]],
    a=x+y theta, b=-a bar(a)/2+z theta.                  (T3.4)

They have determinant1 and bar(Q)^t J Q=J. Both Q and Q^-1 have
polynomial entries of total degree at most2 in x,y,z; hence
Ad(Q) has total degree at most4. The matrix u=1+theta E13 is an
integral unitary transvection, with N=theta E13 and N^2=0.

Suppose a closed subgroup R of SU3(Z_l) maps onto SU3(F_l). Choose
g in R lifting the reduction of u, and write g=u(1+lB) modulo l^2.
Then

    g^l = u^l (1+l sum_(j=0)^(l-1) Ad(u^-j)B) mod l^2.

The adjoint expression is a polynomial in j of degree at most2.
The sums of1,j,j^2 vanish modulo l for l>=5. Since u^l=1+lN,
the first congruence layer of R contains N modulo l. Its conjugates
under R give an Ad(SU3(F_l))-stable subspace of su3(F_l).

For l>=7, interpolation in x,y,z in (T3.4) shows that this subspace
is stable under the adjoint actions of the six derivatives of the
upper and lower root groups:

    P_x=-E12+E23, P_y=theta(E12+E23), P_z=theta E13,
    M_x=E21-E32,  M_y=theta(E21+E32), M_z=theta E31.

The two brackets

    [P_x,M_x]=diag(-1,0,1),
    [P_x,M_y]=theta diag(-1,2,-1)

together with these six matrices form an F_l-basis of su3(F_l).
Thus the conjugate span is a nonzero ideal of that Lie algebra.
After quadratic scalar extension it is sl3, which is simple in
characteristic greater than3. The first congruence layer is therefore
all of su3(F_l). The exact power congruence

    (1+l^m X)^l = 1+l^(m+1) X mod l^(m+2), m>=1,

gives every subsequent layer. Smoothness identifies those layers
with su3(F_l). Induction shows that R surjects modulo every l^m;
closedness gives R=SU3(Z_l).

The same argument for SL3 uses the elementary roots1+tEij; their
conjugate logarithms span sl3. For SL2 over an unramified local field
F_v, use transvections with every residue parameter in F_q: the
first congruence layer contains all residue multiples of E12 and its
conjugates, hence sl2(F_q) as an F_l-vector space. The l-th-power
congruence then gives all layers. This extends the E.2.25 argument
from quadratic residue fields to the cubic RM fields here. For Sp6
the identical transvection method applies: the conjugate logarithms
v -> psi(v,u)u span the symplectic Lie algebra in odd characteristic.
Indeed under sp(V) isom Sym^2(V), these are squares u^2, which span
Sym^2(V) because 2uv=(u+v)^2-u^2-v^2. Thus the first layer is full
and the same power congruence gives all layers. This also reproves
the already used Sp4 lifting statement.

Finally the closed commutator subgroup of each integral good-prime
group surjects modulo l, by finite perfectness, and the lifting
argument just proved makes it the whole integral group. This proves
the asserted integral perfectness without assuming that finite
perfectness alone passes to an infinite congruence tower.

### T3-3b. Complex conjugation on every actual factor

Enlarge the finite family of geometric isogeny classes to a finite
Gamma_Q-stable family. For each class choose an actual isogeny
phi_i:cA_i -> A_(pi(i)), where c is the fixed complex conjugation.
On Betti homology set C_i=phi_(i,*) c_i and let C be their block
direct sum. Choose K finite Galois defining all these maps.
For gamma in Gamma_K the exact naturality equation is

    C_i rho_i(c gamma c) C_i^-1 = rho_(pi(i))(gamma).

With one consistent ordering of the direct sum this defines the
automorphism theta=Ad(C) of M and H. Reversing C only replaces
theta by its inverse and gives the same commutator argument.
The Hodge homomorphism satisfies

    C h(z) C^-1=h(bar(z)).                               (T3.5)

Moreover C^2 is block diagonal with algebraic endomorphisms, so it
centralizes M: theta is an involution on M and on H.

On a theta-fixed Q-simple factor S of H, theta cannot be the
identity. Otherwise (T3.5) in the corresponding adjoint quotient
would say h_ad(z)=h_ad(bar(z)). On the unit circle this is
h_ad(z)=h_ad(z)^-1, forcing the homomorphism from a connected torus
to be trivial. On the real weight torus h is central, so the entire
h_ad would be trivial. The image of M in this nontrivial adjoint
factor is generated as a Q-group by h_ad, contradicting its
nontriviality. This argument uses the actual adjoint quotient map
M -> S^ad obtained from the product decomposition of H^ad.

For precision at every finite place, write S=Res_F/Q T, where T is
absolutely simple over its centroid F. The automorphism theta
permutes the places of F over l. If it fixes such a place while
acting nontrivially on F, it acts nontrivially on the centroid F_v
of the local Lie algebra. If it fixes F, theta is an F-automorphism
of T; identity after the faithful scalar extension F -> F_v would
force identity over F. Hence every fixed local simple factor has
a nontrivial automorphism. The other local factors are permuted
in pairs.

Outside finitely many primes the models, C, all factor projections,
and these automorphisms are integral and smooth, and the fixed
factor automorphisms remain nontrivial on the Lie algebra modulo l.
For a nontrivial fixed finite factor, some g has g theta(g)^-1
noncentral. Indeed if all these elements were central, their
assignment would be a homomorphism from a perfect group into its
center, hence trivial, so theta would fix every finite point. The
root matrices above (degree at most2, and degree1 for SL/Sp) then
show by interpolation that its differential fixes their Lie
generators. This contradicts the nontrivial reduced differential.
For a nontrivial unramified centroid automorphism use the residue
parameters in the same root matrices; fixing every root point
would force that residue-field automorphism to be the identity.

### T3-3c. Actual commutators and the Fcm kernel

Put U0=Gamma_K intersect Gamma_Qcm, and N=rho(U0). This is a
compact normal subgroup of rho(Gamma_K). Actual c is central on
Qcm, so for every gamma in Gamma_K,

    [gamma,c] in U0,
    g theta(g)^-1 in N.                                 (T3.6)

Unlike the multiplier-only surface case, we do not assert that all
of N is contained in H: a joint CM torus can have a residual finite
action. We will construct supported subgroups of H inside N.

At a good prime, (T3.3) supplies independently supported elements
of each full local factor. On a fixed factor, (T3.6), normality,
the noncentral finite commutator just proved, finite projective
simplicity and the lifting argument show that N contains the whole
supported integral factor. On a pair of factors exchanged by
theta, g theta(g)^-1 has two supported coordinates. Commuting
this element with an element supported in its first coordinate
gives a commutator supported only in that first factor. The closed
subgroup generated by these elements is the whole factor by
perfectness. The second factor follows in the same way.

At an exceptional prime, use an open supported subgroup from
(T3.3). If a local simple factor is fixed, the tangent vectors of

    exp(tX) theta(exp(tX))^-1

at t=0 are (1-theta)X. Matrix exponentials converge for sufficiently
small t. They lie in the actual classical group: the exponential
preserves the defining bilinear or Hermitian form and has
determinant1 for trace-zero X; for a quaternion factor use reduced
trace and reduced norm after a splitting-field extension. Its
initial nonzero tangent vector and its conjugates under a local
open subgroup span a nonzero Lie ideal, hence the whole local
simple Lie algebra. Choose finitely many such actual curves whose
tangent vectors form a basis. Their product map has invertible
differential at zero. The p-adic inverse-function/contraction
argument used explicitly in E.2.25 gives an actual open
neighborhood of1 contained in N on this supported factor.

For a pair of exchanged local factors, take a second commutator
with elements supported in the first factor. Its tangents are
(1-Ad(h))X. As the simple Lie algebra has zero center, conjugates
of these vectors span it, giving the same open neighborhood.
The constructions are supported at individual primes and local
factors, so finite products and closedness give a compact open
product subgroup of H(A_f) contained in N.

The closed derived subgroup of U0 is contained in Gamma_Fcm:
U0 fixes every CM field E, and its restriction to the abelian
extension E^ab/E kills every commutator. Compactness gives the
exact equality

    rho(closure[U0,U0])=closure[N,N].                    (T3.7)

The latter contains the full good integral factors, by their
perfectness. At each exceptional prime the closed derived subgroup
of a local open subgroup is open: its Lie algebra is the perfect
semisimple Lie algebra, and the same finite analytic commutator
map proves openness. Consequently

    rho(Gamma_K intersect Gamma_Fcm)
      contains a compact open subgroup of H(A_f).       (T3.8)

The entire image need not be contained in H. Every subsequent use
of (T3.8) uses this containment or its intersection with a specified
derived kernel.

If the original finite family was enlarged to its Galois orbit,
project the group of that enlarged family back to the original
joint derived group. The projection splits over Q by T3-2; on
finite adeles it is a direct-product projection and is open.
The image of the supported compact open subgroup is therefore
compact open in the original H(A_f), and its elements still
have actual preimages in the same Galois group. Thus (T3.8)
holds for the original finite family as well.

## T3-4. Rational approximation with previously fixed matrices

Let sigma in Gamma_Fcm have fixed conjugate targets for the first n
generators. E.2.11 supplies an actual rational tensor comparison T0
on the full rational abelian category with the prescribed all-CM
comparison alpha(sigma), the prescribed Artin action, and Tate1.
For the joint finite representation the completed difference

    a=T0^-1 rho(sigma)

belongs to H_n(A_f). Here is the exact group map establishing this
membership. Let D be the kernel of the full abelian-to-CM Tannaka
restriction. Its image in M_n is connected semisimple, by the
kernel theorem used in E.2.11. The quotient of M_n by this image
is a quotient of the CM protorus, hence is a torus. It follows in
both directions that image(D)=M_n^der=H_n. The difference fixes
the CM point at every l, so its finite projection lies in H_n(Q_l).
Its entries and inverse are integral outside the finitely many
denominators of T0, establishing membership in H_n(A_f). This
does not assert that every adelic point of a quotient lifts.

Suppose the first n-1 transport matrices have already been fixed
as integral matrices S. Because rho(sigma) has exactly these
matrices, p_n(a)=T0,previous^-1 S is rational. It belongs to
H_(n-1)(Q): it is a rational matrix which satisfies the defining
Q-equations in every completion. Set

    b=j_n(p_n(a)) in H_n(Q),
    b^-1 a in L_n(A_f).                                 (T3.9)

Let K_n be a finite Galois model field, containing the fields
needed for this finite family, and freeze the current restriction
of sigma to K_n. The exact stabilizer of this frozen cylinder and
the previous matrices is

    Kappa_n = Gamma_Fcm intersect Gamma_Kn
                intersect ker(rho_previous).

By (T3.8), applied to the enlarged finite family and field, its
image intersects L_n(A_f) in a subgroup containing a compact open
subgroup U of L_n(A_f). To see the exact implication, intersect
the supported open subgroup in H_n(A_f) furnished by (T3.8) with
ker(p_n)=L_n(A_f). Every element in that intersection has an
actual preimage in Gamma_Fcm intersect Gamma_Kn and acts trivially
on all previous Tate modules, so that preimage is in Kappa_n.
Shrink U so it lies in the stabilizer of the integral lattice.

D.4.1 applies to L_n: it is semisimple simply connected and all
its Q-simple factors have noncompact real points. Hence
L_n(Q) is dense in L_n(A_f). Choose

    l in L_n(Q) intersect (b^-1 a U),
    h=b l in H_n(Q).

Then p_n(h)=p_n(a), and h=a u for some u in U. The rational tensor
map T=T0 h therefore has exactly the old matrices S, and its
completion is rho(sigma)u. Since u is the image of an actual
k in Kappa_n, this completion is rho(sigma k). It carries the
new source lattice onto the fixed target lattice at every prime.
Both T and T^-1 have rational entries integral at every prime;
Q intersect Zhat=Z makes T an actual integral isomorphism. If
L_n=1, equation(T3.9) already makes a rational and the same
argument applies with u=1. This is an exact lifting step preserving
all previously fixed matrices.

## T3-5. One specified global element and every geometric lattice

Enumerate the geometric isogeny classes of simple non-CM abelian
varieties of dimension at most3 over Qbar. Choose the model and
polarization of each class by the fixed height/lexicographic
algebraic-data enumeration used in E.2.25. On each model choose
the integral Betti basis by the period-norm rule there: an
algebraic basis of regular differentials embeds the homology
lattice as a full lattice in C^g; minimize the sum of squared
norms of an ordered Z-basis and break finite ties lexicographically
in the real period coordinates. A first available basis gives a
finite norm bound, and a full lattice has only finitely many
vectors within that bound, proving existence of the chosen basis.
No decision or computability claim is made about this selection.

Start with the nonempty compact set

    C0={sigma in Gamma_Fcm : sigma|P=t0}.

Let K_n be an increasing finite Galois exhaustion of Qbar,
enlarged at stage n to define the selected models, conjugate
targets, and maps used above. In the current compact fibre choose
the first finite K_n-cylinder meeting it. This freezes all target
models in that cylinder. T3-4 produces at least one integral
matrix for the next generator in the cylinder while retaining
every previous matrix. Enumerate integer matrices by entry
height and lexicographic order and choose the first one which
is realized in that cylinder. The resulting fibre C_n is compact
and nonempty. The nested intersection is nonempty. Since the
selected finite cylinders specify the restriction to every K_n
and their union is Qbar, the intersection contains exactly one
sigma_*. This specifies an actual element of Gamma_Fcm with
sigma_*|P=t0 and actual integral transports on all the enumerated
generators.

For every CM abelian variety use its actual algebraic isomorphism
alpha_A from E.2.6; its completed map is rho_A(sigma_*). Products
carry the direct-sum matrices. If q:B -> A is any geometric
isogeny from such a product, put

    L_A=q_*^-1 H_1(A(C),Z) inside H_1(B(C),Q).

For some m,

    Lambda_B subset L_A subset (1/m)Lambda_B,
    L_A/Lambda_B = ker(q) inside B[m].

The actual Galois action on ker(q) agrees with the reduction of
the selected integral transport on B. Hence that rational
transport carries L_A exactly onto the corresponding lattice
for sigma_*q. It induces the integral isomorphism

    T_A=(sigma_*q)_* T_B q_*^-1

whose completion is the actual etale Galois transport. This
constructs every specified geometric isogeny lattice, not merely
one lattice in each rational isogeny class.

Independence of q, compatibility with products, all isogenies,
all algebraic correspondences, tensors, exterior powers and
specified projectors follow by comparing their actual etale
equations and using injectivity of rational matrices into their
completions. The same argument applies to every labelled
polarization, with the one Tate line fixed. On Artin objects
the map is the actual permutation x -> sigma_*x. On objects
over arbitrary finite model fields the primitive idempotents of
the Artin algebra select their conjugate blocks exactly as in
E.2.3; thus the geometric construction descends with all its
specified morphisms to the rational base category and then to
the prescribed quartic pair.

This yields a single plain integral comparison on the diagram
generated by all geometric abelian factors of dimension at most3,
all CM abelian varieties of arbitrary dimension, their actual
geometric isogeny quotient lattices and products, algebraic
correspondences and specified tensor/projector constructions,
and all Artin objects. The labelled real Frobenius witness of
E.2.7 still separates the two real places under that enrichment.
The argument does not yet construct transports on arbitrary
simple non-CM factors of dimension at least4 or on the full pure
category. The original E.2 full-category place-separation gate
is therefore retained.

## Source access and exact remaining review obligations

Opened and read in this run:

- Moonen--Zarhin, arXiv math/9901113v2, Sections2.3--2.4 authorp9,
  Section2.7 authorp10; local moonen_zarhin_low1999.pdf/.txt.
- Tankeev1988, original English translation, Theorem1 printed528,
  Lemma3 and proof pp532--535, type-I cases pp535--539. Web PDF
  retrieval works with getFT.phtml?jrnid=im&paperid=1338&what=fullteng.
  The displayed formulas at Theorem1 were lost in the indexed OCR;
  screenshot redirects and direct downloads failed. Only the
  explicitly read case proof and inclusion/dimension statements
  are used, with Commelin4.18 supplying the center equality.
- Commelin2019, Lemmas4.15--4.18 pp658--659 and Theorem10.5 p676;
  local commelin_products2019.pdf/.txt.
- Serre2013, definition of independence p542, Theorem1 and
  Section3.1 pp544--545; local serre_independence2013.pdf/.txt.
- Cadoret--Moonen, TheoremA(i), Sections1.1--1.3; original local
  cadoret_moonen_integral.pdf/.txt, rechecked here.
- Fite--Goodman2026 arXiv2504.03860v3, Theorem1.1(i)p2,
  Proposition2.7pp6--7, Theorem3.1/proof pp9--10; local
  fite_goodman_threefold2026.pdf/.txt. The direct determinant
  construction is a separate check, not required after4.18.
- Taylor, author corrected *The Geometry of the Classical Groups*,
  Theorems4.4--4.5,8.7--8.8,10.15, and explicit Q(a,b) pp121--122;
  local taylor_classical2021.pdf/.txt.

Independent review already received: the parent passed the connected
subdirect simply connected group and split projection proofs;
elliptic_splitting passed the SU3 lifting lemma in
work/elliptic_audit_su3_lifting.md and then independently passed the
full T3-1--T3-5 construction and listed primary sources. Its one
wording correction was Commelin's finitely generated definition
extension, now stated exactly above. Root has now independently passed the full proof, including the exact
Taylor finite-group pages, Commelin center correction, and frozen-matrix
step, and assigned canonical E.2.26. The complete proof is integrated in
output/RESEARCH_SA07/sections/E_integral_image.tex.

The exact finite certificate is
work/code_generation/verify_threefold_groups.py, with captured output
in the corresponding .out file. It proves the unitary inverse/form/
determinant identities, degree-four adjoint polynomial, the eight
root/Cartan matrices with an explicit minor equal to -1, the
degree-two transvection power formula, the rank-21 symplectic
transvection span, and the determinant-three CM torus map. The first
run stopped at an overrestrictive asserted list of possible nonunit
minors; direct inspection gave the stronger exact unit minor -1,
and the assertion was corrected to that value. The subsequent runs
passed. The certificate does not substitute finite computation for
the openness, arithmetic source, or approximation proofs.
