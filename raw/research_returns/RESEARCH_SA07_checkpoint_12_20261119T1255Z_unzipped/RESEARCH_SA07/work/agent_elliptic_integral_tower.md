# Actual simultaneous integral transport for the elliptic diagram

This is work in progress for the explicit quartic pair. The full
pure-motive and all-abelian problems retain their stated scope. No
claim here extends the construction to arbitrary higher-dimensional
geometric abelian simple factors.

## ET-1. Finite-family image over Fcm is open: proved

Let E_1,...,E_r be non-CM elliptic curves defined over Q, pairwise
nonisogenous over Qbar. Choose actual integral Betti bases and their
compatible adelic Tate bases. Write

    rho : Gamma_Q -> Delta ⊂ GL_2(Zhat)^r,
    Delta={(g_i): det(g_i)=det(g_j) for all i,j},
    S=SL_2(Zhat)^r, G=rho(Gamma_Q), N=rho(Gamma_Qcm).

Then rho(Gamma_Fcm) is an open subgroup of S.

### Exact open-image input

For r≥2, Lombardo, *An explicit open image theorem for products of
elliptic curves*, Theorem 1.1 and Remark 1.2, author PDF p.1, proves
G has finite index in Delta. The original author PDF was reopened:
https://web.dm.unipi.it/lombardo/files/ProductsEC.pdf
(web reference turn654579176view0). The bar over K in the geometric
hypotheses is lost in text extraction but was already visually checked
in the D-section source audit. The exact needed hypotheses are geometric
non-CM and pairwise geometric nonisogeny, and the adelic theorem includes
the prime 2. For r=1 use the already opened Serre1972 Theorem3 p.299.

Since G is a compact image it is closed; finite index therefore makes
it open. In particular it contains a product congruence neighborhood

    K(M)=product_{i,l} B_l(v_l(M)),
    B_l(a)=ker(SL_2(Z_l)->SL_2(Z/l^a)), B_l(0)=SL_2(Z_l),

for some positive integer M. Its elements may be supported at a single
factor and a single prime; this support property is used below.

### Actual complex conjugation gives independent roots

Let c be actual complex conjugation and C=rho(c). Every component is
an involution of determinant -1. The image of c is central on Qcm,
so [gamma,c] belongs to Gamma_Qcm for every gamma in Gamma_Q.
Consequently [g,C] belongs to N for every actual g in G.

Fix i,l. At odd l, C_i,l is conjugate to diag(1,-1) by an element
P in GL_2(Z_l): its plus/minus kernels are the complementary integral
summands defined by (1±C)/2. At l=2 it is so conjugate by P in GL_2(Q_2).
Choose a large enough a so that both P U(l^a Z_l) P^-1 and
P L(l^a Z_l) P^-1, supported only at (i,l), are contained in K(M).
This only costs finitely many powers of 2 for the possible denominators.
Conjugation by diag(1,-1) inverts both root parameters. Thus

    [U(t),diag(1,-1)]=U(2t),
    [L(t),diag(1,-1)]=L(2t).

These are actual supported elements of N after conjugation by P.
For l not dividing 2M, take a=0 and obtain the full two root groups,
which generate the complete embedded SL_2(Z_l) factor.

At a remaining prime, the roots of some depth b suffice. For x,y in
l^b Z_l with 1+xy a unit, the exact identity

    U(x)L(y)U(-x/(1+xy))L(-y(1+xy))
       =diag(1+xy,(1+xy)^-1)

puts every diagonal with first entry in 1+l^(2b)Z_l in the generated
group. Indeed fix x=l^b and take y=(d-1)/l^b. Gauss decomposition

    [[a,b0],[c0,d0]]=L(c0/a) diag(a,a^-1) U(b0/a)

then puts all B_l(2b) there. The same conclusion after conjugation by
P contains some B_l(k) in the original integral basis. To see this
with denominators explicitly, choose d with l^d P and l^d P^-1
integral; P^-1(B_l(k+2d)-I)P has entries in l^k Z_l. Thus the
conjugated compact open neighborhood contains an ordinary congruence
neighborhood. All elements have remained in the actual image N.

The image N is closed. It contains each supported factor obtained
above, and hence the closure of their finite products, namely an open
product subgroup S_0 of S. Also N⊂S because Qcm contains Qab and
the determinant is cyclotomic. Thus N is open in S.

### Passing to the CM-abelian kernel preserves openness

Let D be the closure of [Gamma_Qcm,Gamma_Qcm]. Every K^ab Qcm/Qcm
is abelian for a CM field K, by abelian base change, and Fcm is their
compositum. Hence

    D ⊂ Gamma_Fcm.

The compact surjection Gamma_Qcm -> N sends D onto the closed
commutator subgroup N': images of commutators give one inclusion,
compactness of the image and continuity give the other. We show N'
contains an open product subgroup, using the supported subgroups S_0.

For l≥5 and a full SL_2(Z_l) factor, the identity

    [diag(2,1/2),U(t)]=U(3t)

and its lower-root version put all root elements in the derived group,
since 3 is a unit. Thus the full factor is perfect. Enlarge the finite
bad-prime set to include 2 and 3. In each remaining supported factor
take B_l(a)⊂N, with a≥1, and a≥2 at l=2. For d=1+l^a,

    [diag(d,d^-1),U(l^a t)]
       =U(l^(2a)(2+l^a)t).

The upper and lower roots in the derived subgroup have depth 2a for
odd l and 2a+1 for l=2. The preceding explicit root/diagonal/Gauss
calculation gives an open congruence subgroup. Once more, these are
independently supported elements and N' is closed, so their product
is an actual open subgroup of S. Therefore rho(Gamma_Fcm) contains
that subgroup and is itself open in S.

This argument uses the inclusion D⊂Gamma_Fcm, not an unproved equality
between the two groups.

## ET-2. Countable compact selection: exact argument to audit

Let P be the S4 splitting field of x^4-x-1 and H=P^(V4). From E.2.6,
P∩Fcm=H, so restriction Gamma_Fcm -> Gal(P/H)=V4 is surjective.
Fix a double transposition t that exchanges the chosen two quartic
embeddings. Enumerate representatives E_n/Q of all geometric non-CM
isogeny classes that have a model over Q, and choose actual integral
Betti bases once and for all.

Start with the nonempty compact coset C_0 of elements restricting to t.
Suppose C_n imposes rho_Ei(sigma)=S_i in SL_2(Z) for i≤n.
It is a coset of the compact kernel of those maps and the finite P-map.
Apply ET-1 to E_1,...,E_(n+1). The image of Gamma_Fcm intersect Gamma_P
is closed and finite index in the open image of Gamma_Fcm; hence it
contains a product congruence subgroup. Its subgroup fixing the first
n full Tate matrices therefore has an open image in the last factor.
Consequently rho_E(n+1)(C_n) is an open coset in SL_2(Zhat).
Density of SL_2(Z) in SL_2(Zhat) supplies an integral S_(n+1) in that
coset. Its inverse image C_(n+1) is nonempty compact and nested.
Compactness gives sigma in the intersection, preserving the quartic t.

The density is elementary: SL_2(Z/m) is generated by upper and lower
elementary matrices. Over each local factor Z/l^a, a unimodular column
has a unit entry, and elementary row operations plus a determinant-one
swap reduce it; the needed diagonal is a product of elementary matrices.
Chinese remaindering their parameters gives the same assertion over
Z/m, and each elementary matrix lifts to SL_2(Z).

For a fully specified choice one can order integral SL_2 matrices by
entry height and lexicographic order, choose the first one in each
nonempty image coset, and then use the fixed finite Galois exhaustion
and first extendible branch convention of E.2.17 in the final compact
intersection. No claim of a decision procedure is made.

## ET-3. Actual quotient-lattice and tensor extension: to audit

For each representative E_n, the restriction of its actual completed
Galois map is S_n on its actual Betti lattice. For any product A_0 of
these representatives and any CM abelian variety, use the direct sum
of these S_n and the canonical s=1 CM comparison of E.2.6. They all
have the same actual completed transport because sigma lies in
Gamma_Fcm. Their reductions transport every finite subgroup H⊂A_0
to sigma H. Hence the actual quotient map q:A_0->B=A_0/H induces
a unique lattice isomorphism on B through the enlarged lattice
q_*^-1 Lambda_B, as described below; this extends to every geometric
isogeny-class lattice.

More explicitly write V=H_1(A_0,Q), identify H_1(B,Q) with V via q_*,
and put L_B=q_*^-1 Lambda_B. Then Lambda_A0⊂L_B⊂(1/m)Lambda_A0
for m killing H. The quotient L_B/Lambda_A0 is exactly H under
v↦v mod Lambda_A0 in the analytic torus. The completed action equals
actual Galois action on this finite quotient, so it carries L_B onto
the corresponding conjugate lattice. Multiplication by q_* then gives
an integral map with completed map rho_B(sigma). Independence of the
chosen q is forced by injectivity of Hom_Z(lattices) into its completion.

All homomorphism, product, algebraic-correspondence, tensor, polarization
and specified projector equations follow from their actual etale
equations and faithful comparison, exactly as in E.2.16. On cohomology
use inverse dual maps; exterior powers give all degrees, Tate is fixed.
Finite-model underlying-Q Artin blocks are permuted by sigma and the
constructed maps on the corresponding geometric factors, as in E.2.3.
The intended category is generated by the listed E_n/Q, **all** their
geometric finite quotients and product isogeny lattices, all CM abelian
varieties and all Artin objects, with the actual correspondences of
that full subdiagram. No assertion identifies this category with all
abelian motives or all pure motives.
