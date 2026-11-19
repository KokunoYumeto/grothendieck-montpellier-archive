# Extension to all geometric elliptic isogeny classes

Work proof, separated from the already integrated E.2.23 until independent
audit. It constructs one quartic-swapping element with actual integral
transport on all abelian varieties geometrically isogenous to products
of arbitrary elliptic curves and CM abelian varieties. It does not supply
the extra simple non-CM abelian factors in E.2.21 or every pure motive.

## ET-4. Openness over Fcm for every finite geometric elliptic family

Let E_1,...,E_r/Qbar be geometrically non-CM, pairwise geometrically
nonisogenous. Enlarge their finite collection of geometric isogeny classes
to a finite Gamma_Q-stable collection; this is possible since each model
has finitely many conjugates. Choose one representative in each class.
Complex conjugation permutes these classes by an involution pi. For every
i choose an actual isogeny phi_i:cE_i -> E_pi(i). Let K/Q be finite Galois,
defining every representative and every chosen phi_i. The product Tate
representation on Gamma_K is

    rho: Gamma_K -> Delta ⊂ product_i GL_2(Zhat),

with common cyclotomic determinant. By the opened Lombardo Theorem1.1
(one factor: Serre1972), G=rho(Gamma_K) contains a principal product
congruence subgroup. Put N=rho(Gamma_K ∩ Gamma_Qcm); it is closed and
normal in G, and contained in S=product_i SL_2(Zhat).

### Exact comparison for conjugation and the chosen isogenies

Let c_i:H_1(E_i(C),Q)->H_1(cE_i(C),Q) be the actual antiholomorphic
conjugation map, and let C_i=phi_i,* c_i. Thus C_i is a rational linear
isomorphism from the i-th homology to the pi(i)-th homology. With actual
integral Betti bases, C_i is integral with nonzero determinant. The maps
on Tate modules are its completed rational extension. Since phi_i is
defined over K, for gamma in Gamma_K the exact formula is

    C_i rho_i(c gamma c) C_i^-1 = rho_pi(i)(gamma).       (ET4.1)

Indeed c transports E_i to cE_i, gamma fixes both models, and phi_i
intertwines the gamma-actions. This is the actual naturality diagram,
not an arbitrary identification of the two elliptic representations.
Consequently the automorphism theta of G induced by conjugation by c is

    theta(g)_i=C_i^-1 g_pi(i) C_i.

Because K/Q is Galois, [gamma,c] belongs to Gamma_K. Because actual c
is central on Qcm, it also belongs to Gamma_Qcm. Thus

    g theta(g)^-1 belongs to N for every g in G.         (ET4.2)

All root groups used next are elements of the independently supported
product congruence subgroup already contained in G.

### Swapped conjugate classes

Suppose pi(i)=j≠i. If g is supported at factor i and prime l, then the
element in (ET4.2) has components g at i and C_j^-1 g^-1 C_j at j.
Its commutator with an independently supported h at (i,l) has components
[g,h] at i and identity everywhere else. It lies in N by normality.
The supported-root/diagonal proof of E.2.23 shows that the derived group
of a principal congruence subgroup contains another such subgroup, and
SL_2(Z_l) is perfect for l≥5. Hence N contains a supported open subgroup
at every prime and the full supported factor at all sufficiently large
primes. The same argument applies to j.

### Fixed conjugate classes: the actual matrix is noncentral

Suppose pi(i)=i. In complex uniformization C_i is an antilinear map
z↦a conjugate(z), so C_i²=|a|² I. Algebraically this square is
phi_i c(phi_i) in End(E_i)=Z, and its positive integer is deg(phi_i):
its degree is (deg phi_i)², whereas multiplication by m has degree m²,
and the analytic square is positive. Thus, with d=deg(phi_i),

    C_i²=d I, trace(C_i)=0, det(C_i)=-d.                (ET4.3)

In particular C_i is noncentral over every Q_l. No square root of d
in Q_l is assumed. Outside finitely many primes it is an integral unit
matrix and its reduction is nonscalar: scalar trace zero in odd
characteristic would force zero determinant. Equation (ET4.2) supplies
the supported commutators [g,C_i^-1] in N.

### Explicit local openness at the exceptional primes

This paragraph proves the needed local assertion without importing a
Lie-algebra-to-group lifting theorem. Let C be any nonscalar matrix in
GL_2(Q_l). Let R be a closed subgroup, normal under a principal
congruence group B_l(a), and containing [g,C] for every sufficiently
deep supported g in that group. Choose X among E12,E21 with
Z=X-Ad_C X≠0; one works since a matrix commuting with both is scalar.
For t sufficiently l-adically small,

    f(t)=[I+tX,C]

is an actual element of R, a polynomial matrix function of t with
f(0)=I and derivative Z. The Q_l-span W of Ad_h Z, h in B_l(a), is
all sl2(Q_l). To verify this, W is stable under every such Ad_h.
Conjugation by I+tE12 and I+tE21 is polynomial of degree at most2 in t.
Interpolation at three distinct sufficiently small t shows W is stable
under brackets with E12 and E21, hence is an sl2 ideal. The elementary
relations [H,E12]=2E12, [H,E21]=-2E21, [E12,E21]=H show sl2 over a
characteristic-zero field has no proper nonzero ideals.

Choose h_1,h_2,h_3 in B_l(a) with Ad_hj Z linearly independent. The
polynomial map

    F(t1,t2,t3)=product_{j=1}^3 h_j f(t_j) h_j^-1

takes a neighborhood of 0 into R and has invertible derivative at0.
Use coordinates (matrix11-1,matrix12,matrix21) near the identity of
SL2; the fourth entry is determined by determinant1 and matrix11 being
a unit. In these coordinates write F(x)=Jx+P(x), J invertible and P
having no constant or linear term. On a sufficiently small ball,
J^-1 P is Lipschitz with constant less than1 and maps the ball into a
strictly smaller ball. For each y in that ball the iteration

    x_(n+1)=y-J^-1 P(x_n)

converges in the complete l-adic ball and solves F(x)=Jy. Thus the
actual image contains an open neighborhood of I, and R is open.
Applied to the supported fixed factor of N, this proves local openness
at every exceptional prime, including2 and nonsplit C.

### Full factors at all remaining primes, with the lifting proof

For l≥5 outside the finite exceptions, G contains the full supported
SL2(Z_l), N is normal under it, and C modl is nonscalar. At least one
commutator [g,C] is noncentral modulo l. Otherwise conjugation by C
would fix every upper/lower unipotent modulo its sign; trace2 forbids
the negative sign, and commuting with both roots forces C to be scalar.

Here is the finite simple-group input explicitly. SL2(F_l) is perfect:
[diag(2,1/2),U(t)]=U(3t), the analogous lower identity, and generation
by the two root groups prove this for l≥5. Its quotient PSL2(F_l) acts
faithfully and doubly transitively on P1(F_l). The point stabilizer has
the normal abelian translation subgroup U, whose conjugates generate
the group. A nontrivial normal subgroup is transitive, because its
orbits form an invariant partition for a primitive faithful action.
Write every group element as a product of an element of that normal
subgroup and an element of the point stabilizer. In the quotient all
conjugates of U then have the same image. That image generates the
quotient and is abelian; perfectness forces the quotient to be trivial.
This proves simplicity of PSL2(F_l). Therefore the normal image of N
in SL2(F_l) contains PSL2 modulo the center. Its quotient has order at
most2 and is again trivial by perfectness. The reduction of N is full.

For clarity, full reduction lifts without an additional assumption.
Let R be any closed subgroup of SL2(Z_l) surjecting modulo l. Choose
g in R with g≡U(1) modl and write g=U(1)(I+lB) modulo l². In g^l,
the first-order error is l times the sum of Ad_U(-j)(B), 0≤j<l.
Its entries are polynomials in j of degree at most2. The sums of
1,j,j² vanish modulo l for l≥5. Thus

    g^l ≡ I+lE12 mod l².

Conjugation by lifts in R of the standard lower root and interchange
matrix spans E12,E21,H in the first congruence quotient. Then

    (I+l^n X)^l ≡ I+l^(n+1) X mod l^(n+2), n≥1,

gives every next congruence layer. Successive approximation and
closedness give all of SL2(Z_l). Hence N contains the full supported
factor at every sufficiently large prime.

### Actual product and the Fcm kernel

The independently supported open/full factors just obtained generate,
after closure, an open product subgroup of S contained in N. The
closed derived subgroup of Gamma_K∩Gamma_Qcm lies in Gamma_K∩Gamma_Fcm,
since every CM abelian extension becomes abelian over Qcm. Its image
is the closed derived subgroup of N. The same supported small-prime
and perfect large-prime calculation as E.2.23 shows this derived image
is open in S. We have proved, for the original finite subfamily as well
by projection,

    rho_(E_1,...,E_r)(Gamma_K ∩ Gamma_Fcm)
          is open in product_i SL2(Zhat).             (ET4.4)

This remains true for any further finite extension of K: intersection
has finite index, its image is compact and finite index in the open
image, and hence is open. Thus all later finite-model enlargements
in the global construction are allowed.

## ET-5. Countable selection with varying conjugate targets

Enumerate one model E_n/Qbar from every non-CM geometric isogeny class.
Use the fixed countable ordering of algebraic numbers to enumerate short
Weierstrass models and retain first representatives. For each model,
including its finitely many conjugates when needed, choose an oriented
Betti basis canonically: among all oriented bases (w1,w2) of the period
lattice for dx/y, minimize |w1|²+|w2|², then the lexicographic tuple
(Re w1,Im w1,Re w2,Im w2). There are finitely many lattice pairs in
every bounded ball, so this gives one basis. Its orientation is
Im(conjugate(w1)w2)>0. The periods determine unique homology cycles.

Let P and t=(12)(34) be as in E.2.23. Begin with its nonempty compact
coset C_0 in Gamma_Fcm. At stage n choose a finite Galois field K_n/Q,
increasing with n, containing P, the first n models, a stable finite
class-orbit enlargement and the chosen isogenies in ET-4. Require also
that K_n contain the nth member of the fixed finite Galois exhaustion
of Qbar. All choices can be fixed by the first containing field and
first isogeny in the countable algebraic-data enumerations; no effective
recognition claim is made.

Suppose the previous nonempty compact set has fixed actual integral
transport matrices on E_1,...,E_(n-1), together with its earlier finite
field restriction. Partition it by restriction to K_n and select the
first nonempty finite cylinder, denoted C'_n. Its target models cE_i
(here c is the selected K_n-embedding, not complex conjugation) and
their oriented integral bases are now fixed. Pick any sigma_n in this
cylinder for the proof of nonemptiness. Its stabilizer is exactly

    H_n=Gamma_Fcm ∩ Gamma_Kn ∩ intersection_(i<n) ker rho_Ei.

Indeed for k in Gamma_Kn, actual transport satisfies
rho_Ei(sigma_n k)=rho_Ei(sigma_n) rho_Ei(k); the target is fixed, so
equality of the previous matrices is equivalent to rho_Ei(k)=I.

By ET4.4 the image of Gamma_Fcm∩Gamma_Kn on the first n classes is
open. Therefore rho_En(H_n) contains an open congruence subgroup:
the product neighborhood in the finite-family image contains each
deep last-factor element with earlier factors precisely identity.
The possible matrices from the fixed source lattice of E_n to the
fixed target lattice of sigma_n E_n form the open coset

    rho_En(sigma_n) rho_En(H_n) ⊂ SL2(Zhat).

The determinant is one because sigma_n fixes all roots of unity and
the bases are oriented. By the elementary density proved in E.2.23,
this coset contains an integral SL2 matrix. Choose the first by height
and lexicographic order and intersect C'_n with its inverse image.
The result C_n is nonempty compact and nested. Their intersection
contains a single sigma: nonemptiness is compactness, and uniqueness
follows because the fixed K_n restrictions exhaust Qbar. This sigma
still restricts to t on P, lies in Gamma_Fcm, and its actual transport
is integral on every E_n simultaneously.

## ET-6. Extension to the entire elliptic-and-CM diagram

For any product of the representatives and a CM abelian variety, use
the direct sum of the integral actual transports and the canonical
idele1 CM comparison from E.2.6. For an arbitrary geometric isogeny
q:B->A, the exact superlattice L_A=q_*^-1 Lambda_A contains Lambda_B,
and L_A/Lambda_B is the finite kernel of q. Actual torsion transport
shows the rational direct-sum comparison carries L_A onto the
conjugate superlattice. Thus (sigma q)_* T_B q_*^-1 is an integral
comparison on A with completion exactly rho_A(sigma). Completion
injectivity supplies independence of q and coherence for every
homomorphism, algebraic correspondence, tensor, polarization and
specified projector. Cohomology uses inverse dual and exterior maps.
Tate is fixed, and every finite-model Artin block is sent e_u→e_sigma u
with its actual geometric component map, as in E.2.3/E.2.16.

This proves a single global integral comparison on the diagram of all
abelian varieties geometrically isogenous to products of arbitrary
elliptic curves and arbitrary CM varieties, with all its geometric
isogeny-class lattices and all Artin objects. Its restriction to the
quartic field identifies the two specified embeddings on that entire
diagram. Place-labelled real Frobenius is excluded exactly as in E.2.7.
The all-abelian/full-pure gate remains the extension to the additional
objects in the original diagram; no higher-dimensional open-image or
integral lifting assertion has been substituted for that extension.
