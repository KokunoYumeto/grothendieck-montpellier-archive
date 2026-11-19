# C21: a global common partial model with uniform horizontal bounds

2026-11-19, GPT-6 Astra (OpenAI), agent /root/topos.
Reserved statement identifier C21. This theorem narrows the remaining
construction problem; the object P below is not asserted admissible.

## Theorem

Let k be a commutative ring, S=Gamma_k(T), and let A,B be generalized
strict PD theories whose rows satisfy the uniform eventual acyclicity
condition of manuscript scan119. There is a simplicial nonnegative
bigraded strict PD differential S-algebra P, with maps P->A and P->B
preserving all specified structures, such that:

1. P has free k-modules in every simplicial, weight and cochain degree.
2. For every d, all rows P^(w,q), q<=d, are simplicially acyclic when
   w>=mu_P(d), for one finite bound independent of simplicial degree.
3. In every simplex and every weight, H^0(P)=S.
4. After base change to k_(p)=k tensor_Z Z_(p), the coefficient map is
   a quasi-isomorphism through cochain degree d whenever d<2p-1.
   This bound is uniform in the simplex and weight. If k_(p) is
   torsionfree over Z_(p), it suffices that d<2p.
5. More generally, through degree d the vertical coefficient comparison
   is an isomorphism after inverting (floor((d+1)/2))!. Thus all vertical
   defects in that fixed range are supported at finitely many primes.

If A,B satisfy q<=w, P can be chosen to satisfy that support condition.
No vertical exactness hypothesis on A,B is needed for this construction.

## Horizontal cells, including their relative boundary

Let K(n)=DK(k[n]) be the simplicial k-module whose normalized complex
is k concentrated in homological degree n. Let D(n+1)=DK(D_(n+1)k),
where the normalized disk has k in degrees n+1,n and differential 1.
There is a degreewise split inclusion K(n)->D(n+1); its quotient has
normalized complex k[n+1]. This explicitly retains the boundary: the
new quotient is a sphere, not an acyclic parameter.

For a simplicial module M and a positive weight w, let F_(q,w)(M)
be the free strict PD differential S-algebra on a copy of M in
cochain degree q and a second copy in degree q+1, of common weight w,
with the vertical differential the identity from the first to second.
Its universal property is

    Hom_PD-DGA(F_(q,w)(M),X)=Hom_sMod(M,X^(w,q)).

Given a normalized row cycle z in N_n(X^(w,q)), the corresponding
map K(n)->X^(w,q) defines a cell attachment

    X -> X amalg_(F_(q,w)(K(n))) F_(q,w)(D(n+1)).

The new normalized element has boundary z. Thus this attachment kills
the chosen row homology class. At each simplex the module inclusion is
split with a free complement, so the algebra extension is free on a set
of independent vertical disks in degrees q,q+1. No old algebraic
relation is changed.

If X already maps to A and B, and both A^(w,q),B^(w,q) are simplicially
acyclic, each image of z has a normalized primitive. Choose these
primitives independently. They extend the two maps from K(n) to
D(n+1). The universal property extends both PD differential algebra
maps; the images of the degree-q+1 generators are the differentials
of the chosen degree-q images. This needs acyclicity only in row q.

## Construction of P

Start with S, mapped by the specified coefficients into A and B.
Choose

    W(q)>=max(1,q+1,mu_A(q),mu_B(q)).

The q+1 term may be omitted if no support condition q<=w is desired.
At stage q, attach simultaneously one cell for every normalized cycle
in every row X^(w,q) with w>=W(q), in every homological degree n>=0.
Repeat countably many times, so that cycles created by an attachment
are killed at a later round. The filtered colimit has exact normalized
row complexes in those weights, including H_0. Indeed every cycle is
represented at a finite round and is killed at the next round; filtered
colimits of modules are exact and commute with normalization.

Do this successively for q=0,1,2,... . When q>0, the new generators
have cochain degrees at least q, so the stage does not change any row
of degree less than q. The final filtered colimit P therefore has
the asserted horizontal bounds, with

    mu_P(d)=max_(0<=q<=d) W(q).

Each cell map extends the maps to A and B, so the colimit does also.
Each simplex algebra is the free graded PD algebra over S on all the
independent vertical disks added there. In particular all terms are
free over k. Every new generator has positive weight, so the
k-augmentation extends by zero. If w>=q+1 was imposed, every generator
satisfies the support inequality, which products and divided powers
preserve.

## Exact vertical range

An even-to-odd disk has algebra Gamma(x) tensor Lambda(y), dx=y, and
splits into its constants plus the identity pairs

    gamma_m(x) -> gamma_(m-1)(x)y,  m>=1.

It is universally acyclic onto k. For an odd-to-even disk, with odd
q>=1, the algebra Lambda(x) tensor Gamma(y), dx=y, has pairs

    x gamma_(m-1)(y) --m--> gamma_m(y),  m>=1,

in cochain degrees m(q+1)-1 and m(q+1). Over Z_(p), every pair with
m<p is an identity pair up to a unit. The first possible non-unit
pair begins at degree p(q+1)-1>=2p-1. Hence, through any degree
d<2p-1, the augmented disk is universally exact, including its
outgoing differential. Over a p-torsionfree coefficient module the
kernel of that first multiplication by p is zero, so the first
cohomology can occur only in degree p(q+1)>=2p.

The statement after inverting floor((d+1)/2)! follows by the same
calculation: every pair meeting degrees <=d has m<=floor((d+1)/2)
unless its two terms already lie above that range. Finite tensor
products preserve this exact range, by the split identity-pair
decomposition below the first possible defect and first-quadrant
degree considerations. Infinite tensor products are filtered colimits
of finite ones, and exact filtered colimits preserve the result.
Tensoring with the coefficient S and taking a fixed weight preserve
the calculation. It is independent of the number of simplexwise
generators, so all stated bounds are uniform in the simplex and weight.

Only the degree-zero even-to-odd disks affect cochain degree zero,
and each contracts onto its constants over every k. The other disks
start in positive degree. The same tensor argument therefore proves
H^0(P_n)=S in every simplex and every weight.

## Consequence and remaining gate

For each prime p choose a p-power N_p>=W(0). The elementary source
G_(N_p) maps to P_(p), by the same marked degree-zero lift used in C09,
because P^(N_p,0) is acyclic. Thus this construction recovers local
admissible common sources, but does not solve their nonuniform initial
weight problem.

A sufficient next step would replace P_(p) by an admissible local
extension C_p, retaining its maps to A_(p),B_(p), while leaving all
cochain degrees below a bound tending to infinity with p unchanged.
C18 exhibits such a correction-degree bound for a single independent
odd disk. It does not supply the required boundary-relative simplicial
lifts for the cell construction above. Infinite-prime arithmetic
descent must also be verified after such a coherent replacement; it
has not been asserted here.

## Independent audits and integration

2026-11-19: root and automorphisms independently audited the full proof
and found no gap. Both explicitly checked the relative boundary in the
PD cell pushout, the exact filtered-colimit argument, and the general-
coefficient Tor shift in degree 2p-1. The formal statement and full proof
are integrated as C21 in sections/C_repairs.tex. They do not imply that
P itself satisfies the vertical eventual condition at the small primes.
