# C24: signed shuffle freeness and relative bar base change

2026-11-19, GPT-6 Astra (OpenAI), agent /root/topos.
This is the relative algebraic part of the bar route. It does not prove
extension of a prescribed map from an original odd disk to its bar closure.

## 1. Primary input and the signed extension

Opened primary author PDF: Guy Melancon and Christophe Reutenauer,
*Lyndon words, free algebras and shuffles*, Canadian Journal of Mathematics
41 (1989),577--591,
https://reutenauer.math.uqam.ca/wp-content/uploads/2024/04/LyndonWordsFreeAlgebras-Shuffles1989.pdf.
Section4, printed589--590, gives the following unsigned triangularity:
if a word has decreasing Lyndon factorization w=l_1^n_1 ... l_t^n_t,
then the shuffle product of those factors has leading word w with
coefficient product(n_i!), and all other words are lexicographically
smaller. Its corollary identifies the unsigned integral shuffle algebra
as a free divided-power algebra. We use the triangular statement and
derive the signed version below, rather than silently importing it.

Let an ordered alphabet have assigned parities, and give its word module
over Z the Koszul-signed shuffle product. Its divided powers on even
positive words are shuffle powers divided by n!. They are integral:
permutation of the n labelled even blocks acts freely on the shuffles
and preserves the sign. The PD identities follow over Q and hence over
the torsionfree integral word module. The structure then base changes
to every commutative ring. Odd elements square to zero.

Let L_even,L_odd be the even and odd Lyndon words. Then the signed
shuffle algebra is freely generated as a graded PD algebra by:

* the even generators l for l in L_even;
* the even generators ll (concatenation squares) for l in L_odd;
* the exterior odd generators l for l in L_odd.

Proof. Use the unique decreasing Lyndon factorization of each word w.
For an even factor l of multiplicity n use gamma_n(l). For an odd factor
of multiplicity n=2m+epsilon, use gamma_m(ll) shuffle l^epsilon. Multiply
these expressions in decreasing factor order.

The unsigned triangularity implies that no word above w can occur.
It also identifies the shuffles giving w: there are already product(n_i!)
obvious permutations of whole identical Lyndon blocks, so the exact
unsigned coefficient says there are no other maximal shuffles. In the
odd case the concatenation-square blocks force the order within each
pair of copies of l. The resulting signed count is the signed count
of shuffling m ordered blocks of two odd objects, with at most one
additional odd object.

For signed (a,b)-shuffles of odd objects write B(a,b) for the sign sum.
The recursion B(a,b)=B(a-1,b)+(-1)^a B(a,b-1), with boundary values1,
gives

    B(2a,2b)=binom(a+b,a),
    B(2a+1,2b)=B(2a,2b+1)=binom(a+b,a),
    B(2a+1,2b+1)=0.

Consequently the maximal signed coefficient for m two-blocks is
product_(j=1)^m B(2j-2,2)=m!, and the optional single block contributes
B(2m,1)=1. Dividing by m! gives leading coefficient1. Even Lyndon
factors similarly have maximal coefficient n!, canceled by their PD
denominator. Thus the displayed PD/exterior monomials form an integral
unitriangular basis of the word module. They are exactly the monomial
basis of the claimed free graded PD algebra, proving the result.

The basis is compatible with inclusions of ordered alphabets. In
particular a split inclusion of graded free modules gives, after choosing
an extending ordered basis, a free graded PD algebra extension of their
signed shuffle algebras.

## 2. Relative bar property

Let M->N be a split inclusion of free modules in positive even cochain
degrees, with free quotient. All generators may carry additional
positive weights. Use the positive bar closure of D029:

    C(M)=Gamma(M) tensor B(Gamma(M)),

with total cochain degree internal degree minus bar length. Its bar
letters therefore have odd parity and positive cochain degree. The
augmentation C(M)->k is a quasi-isomorphism, by D029's explicit
coefficient-insertion contraction.

Choose a basis for M and extend it to one for N. The divided-power
monomial alphabet of Gamma^+(M) is a subset of that for Gamma^+(N).
The signed Lyndon basis above proves that C(N) is free as a graded
PD C(M)-algebra: its extra generators are the extra coefficient
generators and the extra even/odd signed-Lyndon generators of the bar.
In particular it is free as a graded C(M)-module.

Filter this free module by the total bar length of its new-generator
basis monomials; old C(M) factors do not count toward this filtration.
The bar differential removes one letter, either by moving the first
letter into the coefficient or by multiplying adjacent letters.
In its expansion in the signed Lyndon basis, total bar length is
preserved. Thus the differential of a new basis monomial is a sum of
old coefficients times new basis monomials of strictly smaller bar
length. The coefficient generators have differential zero. The
filtration quotients are direct sums of shifts of C(M), with its
own differential. Therefore C(N) is a semifree, hence K-flat,
DG module over C(M). This argument works over every base ring.

The map C(M)->C(N) is a quasi-isomorphism, since both augment
quasi-isomorphically to k. Its cone is consequently an acyclic
K-flat C(M)-module. Tensoring an acyclic K-flat module with an
arbitrary DG module is acyclic: resolve the latter by a K-flat
module, and compare using the two K-flat properties. It follows
that for every strict PD differential algebra map C(M)->A,

    A -> A tensor_(C(M)) C(N)

is a quasi-isomorphism of underlying complexes. The tensor is the
ordinary PD pushout, because the displayed free graded PD extension
makes the pushout a free graded PD A-algebra on the same generators.
The conclusion is universal under base change and preserves weights.

For a degreewise split inclusion of free simplicial modules, the same
argument applies in every simplex. A compatible basis across simplices
is not needed to prove this objectwise quasi-isomorphism: the bar map
itself is functorial, while the extending basis is only used to verify
K-flatness separately in each simplex.

## 3. Exact limit of the result

C24 settles the relative vertical base-change property for the positive
bar closure. It does not produce the input map C(M)->A from a prescribed
map on the original odd disk, and it does not establish horizontal
eventual acyclicity for a succession of these relative attachments.
D030 proves the first arity of the target extension under stated
finite bounds; higher mixed arities and earlier-boundary compatibility
still require proof. No global C3 comparison is claimed.

## 4. Exact finite certificate

code/C_signed_shuffle_checks.py checks all4956 unitriangular columns
for every parity choice on two letters through length8 and three
letters through length5. It also checks integral divided-power
coefficients and vanishing odd squares. All cases pass. The exact
receipt is logs/C_signed_shuffle_checks.json, runtime0.083071112s.
This corroborates the signed combinatorics; the general proof is above.

## 5. Independent audits and formal integration

Root and shadows_coalgebras independently audited the full argument and
also opened the primary unsigned source. Both passed all parts of the
signed leading-term proof and the relative K-flatness argument. The full
statement and proof are now sections/C_bar_relative.tex, C24. The exact
limitations in Section3 remain unchanged.
