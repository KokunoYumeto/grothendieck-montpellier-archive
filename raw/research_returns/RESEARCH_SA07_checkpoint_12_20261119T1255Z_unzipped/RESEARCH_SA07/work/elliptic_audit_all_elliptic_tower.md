# Independent audit of E.2.24: the all-Qbar elliptic integral tower

Auditor: elliptic_splitting, OpenAI GPT-6 Astra, 19 November 2026.
Audited file: work/agent_all_elliptic_integral_tower.md, ET-4–ET-6.
Verdict: pass for the complete stated diagram of arbitrary elliptic
curves, CM abelian varieties, geometric product-isogeny lattices,
Artin objects and their actual algebraic correspondences.

The proof supplies a single actual quartic-swapping sigma, rather than
separate finite-family elements. It does not supply the extra simple
non-CM abelian factors or every pure object.

## 1. Finite models and the actual conjugation intertwiner

Every chosen elliptic model has finitely many conjugates, so the
finite geometric-isogeny collection can be enlarged to a finite
Gamma_Q-stable collection. A finite Galois K defines representatives
and the finitely many actual isogenies phi_i:cE_i to E_pi(i).
Lombardo's adelic theorem then applies over K; its geometric
hypotheses were independently opened and visually verified in the
E.2.23 audit. No new stronger open-image theorem is required.

Let c_i be actual complex conjugation on Betti homology and put
C_i=phi_i,* c_i. Naturality of Galois transport gives

    rho_cE_i(gamma)c_i = c_i rho_E_i(c gamma c)

for gamma fixing K. Since phi_i is defined over K, its Tate map
intertwines rho_cE_i(gamma) with rho_E_pi(i)(gamma). Composing gives
the exact displayed ET4.1. Consequently conjugation by c on the
actual image is theta(g)_i=C_i^-1 g_pi(i) C_i.

The subgroup Gamma_K intersect Gamma_Qcm is normal in Gamma_K.
Because K/Q is Galois and c is central on Qcm, every [gamma,c]
belongs to it. Thus g theta(g)^-1 is an actual element of its image
N. These identities establish the arithmetic group maps used in all
the following local arguments.

## 2. Swapped and fixed classes

For a swapped pair i,j, choosing g supported at i produces an N-element
supported at i,j. Commuting it with h supported only at i leaves
[g,h] only at i; normality of N makes this an element of N. Therefore
the already proved supported derived-subgroup argument supplies
independent local open factors. The same procedure works for j.

For a fixed class, C_i is an antilinear endomorphism of the real
uniformizing plane, z to a conjugate(z), with a nonzero. Hence its
square is positive scalar |a|² and its real trace is zero. Algebraically
that square is phi_i c(phi_i), an element of End(E_i)=Z. Its degree
is (deg phi_i)², and multiplication by m has degree m². Positivity
therefore fixes m=deg phi_i, proving all signs in ET4.3:

    C_i²=dI, trace C_i=0, det C_i=-d.

These are identities of the actual rational homology matrix, so they
remain true over Q_l even when d has no square root there. In
particular C_i is nonscalar over every Q_l. Away from 2d and the
finite denominator set, its reduction is also nonscalar: a scalar
matrix with trace zero in odd characteristic would be zero, contrary
to its unit determinant.

## 3. The nonsplit local construction stays in the actual image

For nonscalar C choose a root matrix X=E12 or E21 not commuting with C.
The exact map

    f(t)=(I+tX)C(I-tX)C^-1

is polynomial of degree at most two because X²=0. For sufficiently
small t it takes values in the actual supported subgroup R, and
f'(0)=X-Ad_C(X) is nonzero. Let W be the Q_l-span of all its conjugates
under the chosen congruence group. Conjugation by I+tE12 or I+tE21
is polynomial in t of degree at most two. Interpolation at three
small distinct parameters extracts the first derivative, so W is
stable under brackets with both E12 and E21. It is therefore an
ideal of sl2. In characteristic zero, the eigenspace decomposition
for ad(H), followed by [E12,E21]=H, proves that every nonzero ideal
is all sl2. This applies also over Q_2.

Choose three conjugates with independent derivatives. Their product
F(t1,t2,t3) has image in R and invertible derivative. In the coordinates
(a-1,b,c) of a determinant-one matrix, the remaining entry is
(1+bc)/a; these are valid near identity. Thus the coordinate expression
is Jx+P(x), where J is invertible and P begins at degree two.

To make the local inverse assertion explicit, bound the finitely
many coefficients of J^-1 P. On a sufficiently small closed
l-adic ball B, its difference quotient has norm strictly below one.
It also maps B into a smaller ball. For each y in B, the map
x to y-J^-1 P(x) maps B to itself and is a strict contraction.
Completeness gives a solution of F(x)=Jy. Therefore the actual image
contains the open neighborhood J(B). This proves openness directly,
without replacing R by an unproved group having the same Lie algebra.

## 4. Good-prime full factors and congruence lifting

For l at least five outside the exceptional set, N is normal under
the full supported SL2(Z_l). Some commutator with C is noncentral
modulo l: otherwise C would conjugate every root unipotent to itself
up to sign; trace two excludes the negative sign, and centralizing
both root groups forces a scalar matrix.

I checked the finite-group argument. PSL2(F_l) is faithfully doubly
transitive on P1: its point stabilizer contains the translations,
which act transitively on the remaining points. A nontrivial normal
subgroup is therefore transitive. With B a point stabilizer this gives
G=NB. The translation subgroup U is abelian and normal in B, so all
its conjugates have the same image in G/N. Since they generate G,
that quotient is abelian. Perfectness follows from the upper and
lower root commutator formulas, hence G/N is trivial. This proves
the simplicity needed here. A normal subgroup of SL2 surjecting
to PSL2 has quotient of order at most two; perfectness again makes
it the full SL2.

For the lift from F_l, take g=U(1)(I+lB) modulo l². In g^l the
first-order error is l times the sum of Ad_U(-j)(B), j=0,...,l-1.
Every entry of the summand is a polynomial in j of degree at most
two. The three sums of 1,j,j² vanish modulo l for l at least five,
so g^l=I+lE12 modulo l². Conjugating by lifts of a lower root and
the interchange matrix supplies all sl2 in the first congruence
layer. The binomial formula

    (I+l^n X)^l = I+l^(n+1)X mod l^(n+2)

then supplies the next layer for every n at least one. Products and
closedness give every successive approximation, hence all SL2(Z_l).
This checks the actual subgroup conclusion at every sufficiently
large prime, rather than only surjectivity of its reduction.

The independently supported local groups form an open product after
closure. The closed derived subgroup of Gamma_K intersect Gamma_Qcm
lies in Gamma_K intersect Gamma_Fcm, since Fcm/Qcm is abelian.
Its image is the closed derived subgroup of N by compactness.
The same local derived computation therefore proves ET4.4.
Further finite-model enlargements preserve openness: their images
are compact finite-index subgroups of the already open image.

## 5. Fixing conjugate targets before selecting integral matrices

The countable isogeny-class enumeration is valid over Qbar. The
specified shortest oriented lattice basis exists because only
finitely many lattice vectors lie in a bounded ball. An oriented
integral basis is symplectic in dimension two. Since sigma fixes
all roots of unity, its actual completed matrix between the selected
source and target bases has determinant one.

At stage n, restriction to the finite Galois field K_n fixes the
target model of every previous curve and of E_n. If sigma_n is
one point in the selected nonempty cylinder, any other point is
sigma_n k with k fixing K_n. Actual transport composition gives
rho_E_i(sigma_n k)=rho_E_i(sigma_n)rho_E_i(k). Thus all previous
full matrices are fixed exactly when k is in their entire adelic
kernels. This proves that the cylinder is the exact right coset
sigma_n H_n displayed in ET-5.

The open finite-family image contains a product congruence
neighborhood, hence the image of H_n on E_n contains a neighborhood
with all earlier coordinates exactly identity. The possible next
matrices therefore form an open coset in SL2(Zhat). Density of
SL2(Z), already proved via elementary matrices, supplies an integral
matrix in that coset. Its preimage is nonempty and compact.
Nested compactness gives sigma in every stage, while the prescribed
K_n restrictions determine it uniquely because they exhaust Qbar.
The original quartic permutation remains fixed throughout.

## 6. Coherent extension to every stated object

For q:B to A an actual geometric isogeny, identify rational Betti
homology via q_*. The superlattice q_*^-1 Lambda_A contains Lambda_B
with finite quotient exactly ker q, using the usual analytic
uniformization. The comparison on B completes to the actual Galois
map, so it carries that finite kernel to sigma(ker q), and consequently
the superlattice to the conjugate superlattice. Hence
(sigma q)_* T_B q_*^-1 is an actual integral comparison on A.

Every such comparison has the prescribed completion rho_A(sigma).
Injectivity of integral maps into their completions gives independence
of the isogeny presentation and all compatibility equations. For
algebraic correspondences, the actual Galois equation on étale cycle
classes transports to the Betti equation by comparison; abelian
cohomology is torsion-free, so no equality is lost in this passage.
Products, exterior powers, inverse duals, Tate, polarizations and
specified projectors are compatible for the same reason. The
underlying-Q Artin components are permuted by this very sigma and
use the already constructed maps on their geometric factors.

Thus ET-6 holds for the entire stated elliptic-and-CM diagram,
including all its geometric isogeny lattices, not merely one
representative per isogeny class.
