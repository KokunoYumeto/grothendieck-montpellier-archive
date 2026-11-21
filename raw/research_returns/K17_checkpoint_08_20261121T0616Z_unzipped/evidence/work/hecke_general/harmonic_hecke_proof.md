# Full compact-U3 harmonic Hecke spaces in degrees 7, 9 and 11

Status: exact finite algebraic calculation with a standalone certificate;
the present complete proof is awaiting independent whole-proof audit.
No new K-group conclusion or source-interface assertion is made here.
Author: `/root/tripod_integral`, GPT-6 Astra Pro, 2026-11-21 UTC.

## 1. The precise model

Retain E=Q(omega), omega²+omega+1=0, O=Z[omega], the positive standard
Hermitian form on E³, and the full lattice stabilizer K from
K17-U3-HECKE. That theorem's explicit Hermitian reduction proves class
number one, independently of the weight. Its integral stabilizer is
Gamma=mu6³ semidirect S3. Thus the entire algebraic modular-form space
of highest weight (k,0,-k) is the Gamma-invariant part of the harmonic
bidegree-(k,k) polynomial representation.

Use independent formal variables z=(z1,z2,z3) and w=(w1,w2,w3), and

    Delta = sum_i partial_zi partial_wi,
    rho(g)f(z,w) = f(g^{-1}z, conjugate(g)^{-1}w).

The formal variables are the complexification of the usual z and bar(z)
model. Consequently independent rational values of z and w are legitimate
linear evaluation functionals; no claim that these points lie on the real
unitary locus is needed.

For completeness the contraction from degree(k,k) to degree(k-1,k-1)
is surjective. Put R=sum zi wi. For F of bidegree(k-1,k-1), the polynomial

    sum_{j=0}^{k-1} c_j R^(j+1) Delta^j F,
    c_0=1/(2k+1),
    c_j=-c_(j-1)/((j+1)(2k+1-j))

maps to F. The product rule gives the coefficient
`(j+1)(2k+1-j)` of `R^j Delta^j F`, and the adjacent terms cancel.
The harmonic kernel therefore has dimension

    binom(k+2,2)^2-binom(k+1,2)^2=(k+1)^3.

It contains the highest-weight vector w1^k z3^k. Its highest-weight
irreducible representation has exactly this Weyl dimension, so this
kernel is precisely the irreducible representation of weight(k,0,-k).
This proves the model uniformly, not just for the previously checked k=5.

## 2. Every finite-group invariant is included

A monomial z^alpha w^beta is invariant under the diagonal sixth roots
of unity exactly when

    sum alpha_i = sum beta_i = k,
    alpha_i-beta_i divisible by6 for each i.

The differences need not be zero when k>=6. In particular the computation
does not discard the additional +/-6 terms. The same rule automatically
includes larger multiples of6 should this method be continued farther.

The simultaneous S3 action permutes the three pairs (alpha_i,beta_i).
For each orbit choose the sorted triple of pairs as its canonical label
and use the sum of its distinct monomials as basis vector. Distinct orbit
sums have disjoint monomial support and are therefore a basis of all
Gamma invariants, over Q or E. The saved lists enumerate every pair of
three-part compositions of k and impose precisely the displayed divisibility
condition. Thus their coverage is a finite exact enumeration of at most
78² candidates in the largest present degree, not a guessed ansatz.

Delta preserves this invariant space. Its matrix is computed from
`Delta(z^alpha w^beta)=sum_i alpha_i beta_i
 z^(alpha-e_i) w^(beta-e_i)`. The discovery program collects derivative
coefficients by orbit and divides by the target orbit size. The independent
certificate instead expands the monomials, reads the coefficient of one
canonical target monomial, and verifies that every permuted target monomial
has that same coefficient. This independently checks the orbit-sum
normalization.

The full matrix ranks and complete kernels are:

| k | e=k+1 | invariant degree(k,k) | invariant degree(k-1,k-1) | harmonic dimension |
|---:|---:|---:|---:|---:|
|5|6|5|4|1|
|7|8|11|8|3|
|9|10|22|16|6|
|11|12|37|29|8|

The k=5 row is a control and exactly reproduces K17-U3-HECKE. All saved
kernel columns are integral, killed by the saved Laplacian, and linearly
independent. Exact ranks show that their number is the full kernel dimension.
No assertion that these columns form a saturated integral lattice is used:
they are a complete characteristic-zero basis, which suffices for the
operator and its characteristic polynomial.

## 3. Swap, coefficient conjugation, and the rational operator

Let C act on polynomials by interchanging z and w. It preserves the
Laplacian and every finite-group invariant space. The kernel basis is
chosen in its plus and minus eigenspaces. The respective dimensions are
1+0, 2+1, 4+2 and 5+3 for k=5,7,9,11. The certificate checks the swap
action on every basis coefficient, rather than inferring it from a count.

Let g=U/pi be one of the previously proved complete negative-minuscule
neighbor representatives, with U*U=pI and rank(U mod pi)=1. Since

    g^{-1}=U*/bar(pi),    bar(g)^{-1}=U^t/pi,

the scaled action on a bidegree(k,k) polynomial is

    p^k rho(g) f(z,w) = f(U* z, U^t w).                    (G.1)

Thus every transformed polynomial has Eisenstein integer coefficients
when f does. The complete operator is the sum over all57 or183 distinct
right cosets. It preserves the full Gamma-invariant harmonic space:
the Hecke correspondence preserves Gamma invariance, and unitary change
of variables preserves harmonicity. Hence the following finite evaluation
calculation determines the entire operator on the proved full space.

There is also an exact direction check in all dimensions. One has

    C rho(g) C = rho(bar(g)).

Conjugation converts the complete negative-minuscule coset set to the
positive-minuscule coset set. Therefore their matrices are conjugate by C,
so their full characteristic polynomials agree. This does not assume
the operators are scalar, and does not merely compare their traces.
In the rational-coefficient polynomial basis the coefficientwise conjugate
matrix is exactly the positive operator. If the negative operator is
M=M0+omega M1 and C=diag(epsilon_i), the checked identity is

    C M0 C=M0-M1,       C M1 C=-M1.                         (G.2)

In particular its characteristic polynomial has rational coefficients.
Writing delta=1+2omega, so delta²=-3, replace each C-minus basis vector
by delta times that vector. This gives an explicit rational matrix:
same-sign entries have M1=0; opposite-sign entries satisfy M1=2M0,
and become -3M0 in a plus row/minus column or M0 in a minus row/plus
column. The certificate checks these identities entry by entry.

The characteristic polynomial is in fact integral. The scaled operator
in (G.1) preserves the O-lattice of all invariant harmonic polynomials
with coefficients in O. This is a full finite free O-lattice, since O
is a PID. Its characteristic polynomial therefore lies in O[X]; (G.2)
places it in Q[X], and O intersect Q is Z. The numerical certificate
also verifies integrality of every characteristic-polynomial coefficient.

## 4. Exact interpolation is an identifying map, not an approximation

For a saved harmonic basis h1,...,hd choose d pairs of integral triples
(z_r,w_r), and set A_(r,j)=h_j(z_r,w_r). The entire point list and the
integer matrix A are saved. Its exact determinant is nonzero. Evaluation
on these points is therefore injective on the full invariant harmonic
space.

For each p the program computes

    B_(r,j)=sum_U h_j(U* z_r,U^t w_r)=B0_(r,j)+omega B1_(r,j).

All operations here are additions and multiplications of Eisenstein
integer pairs. No interpolation error, numerical tolerance or approximate
linear algebra is present. The matrix identity

    A M0=B0,       A M1=B1                              (G.3)

uniquely determines the scaled Hecke operator because A is invertible and
the operator is already proved to preserve the space. The independent
certificate does not trust the symbolic solve: it recalculates A, its
determinant and all B values, then verifies (G.3) using exact fractions.
Two additional point pairs at each prime check the same operator identity
independently of the identifying points; these are checks on implementation,
not substitutes for the completeness and preservation proof.

The full neighbor input is pinned by SHA256
`3759b83dad147e55157f340f913560dfaea51bc0277d44a1a900d0d6136d79ef`.
The certificate additionally verifies every unitary Gram matrix, every
rank-one reduction, and exact coverage of P²(Fp). The earlier class-number
and elementary-divisor proof identifies this finite set with the actual
Hecke correspondence.

Finally the independent certificate derives each characteristic polynomial
by the Faddeev--LeVerrier recurrence over exact fractions, verifies the
terminal Cayley-Hamilton zero matrix, and multiplies out the reported
polynomial factors. It does not invoke Sympy or either discovery program.

## 5. Exact characteristic polynomials

Write P_(e,p)(X) for the characteristic polynomial of the scaled operator
p^(e-1)T_p. Its positive and negative versions agree by section3. Gross's
normalized Satake formula gives T_p^+=p times the standard trace, so the
scaling is exactly p^e times the normalized Satake trace.

For e=8:

    P_(8,7)  = (X+2702301)
               (X²-9958830X-15191091292671),
    P_(8,13) = (X+153697821)
               (X²-841096230X+74635873683999849).

For e=10:

    P_(10,7) = (X-14535507)
               (X²+571295802X+259067515101993801)
               (X³-1127229705X²+269867622745258587X
                   +21764201659661735207968293),

    P_(10,13)= (X+109076012133)
               (X²+106910299722X+2996591715398898111321)
               (X³-422499415185X²+52678214627106136408587X
                   -1658111541578384339481222489985827).

For e=12:

    P_(12,7) = (X+12221224701)
               (X³-42517894041X²+288396328713382721979X
                   -463507446167295652333685832939)
               (X⁴+2939150868X³-79381481904803039850X²
                   +303898318630502425871984942580X
                   +8681328863742961883955067744457913482097),

    P_(12,13)= (X+21649300719981)
               (X³-33123036335481X²-228653307502980173933740101X
                   +3302349716440899212738561798170057697781)
               (X⁴+48903137840436X³+2568930841937762809121509110X²
                   +39746045119592037993985794601727262212436X
                   +940042707779377699684081382859793759142653810554146961).

These are exact product decompositions; irreducibility of the displayed
factors is not needed or claimed by the standalone certificate. All full
expanded coefficient lists, operator matrices and evaluation matrices are
also in `harmonic_hecke_exact_data.json`.

## 6. Comparison integers and exact common divisors

For each p define E_(e,p)=p^(2e)+p^e+1 and V_(e,p)=P_(e,p)(E_(e,p)).
Both full integer values are saved for every e. The exact common divisors
are

    gcd(V_(8,7),V_(8,13))
       = 2^13 3^13 *23*401*809*13687,

    gcd(V_(10,7),V_(10,13))
       = 2^28 3^26 *43*241*1847*9496386083,

    gcd(V_(12,7),V_(12,13))
       = 2^28 3^39 *13^4*47*28447*300455201.

The certificate evaluates each polynomial by integer Horner arithmetic,
recomputes the gcd, multiplies every stated factor, and proves primality
of every listed factor by trial division through its integer square root.
The largest such search ends below100000, so it is a small exact check.
No probable-prime assertion or unproved full factorization is being used.

These are statements about the specified complete U3 coefficient spaces.
Using them in an arithmetic unit criterion requires the separate source
interface and global packet coverage. If one uses p=7 or13 as an auxiliary
prime for residue characteristic ell, the requirement ell!=p must also
be retained. No assertion of new Vandiver verification or of K16, K20,
or K24 vanishing is made here. In particular the factor9496386083 is
larger than2^31 and must not silently be covered by a smaller published
Vandiver computation.

## 7. Reproduction and actual checks

Files in `work/hecke_general/`:

- `compute_harmonic_hecke.py`: exact discovery, using Sympy for rational
  kernels, solves and polynomial factoring.
- `harmonic_hecke_exact_data.json`: complete frozen basis/operator data,
  including the k=5 control.
- `harmonic_hecke_certificate.py`: standalone standard-library verifier.
- `harmonic_hecke_certificate.json`: successful complete replay report.
- `harmonic_k7_exact_exploration.json`, `harmonic_k9_exact_exploration.json`,
  `harmonic_k11_exact_exploration.json`: individual discovery records.
- `comparison_gcd_exploration.json`: comparison values and factorizations.

Both implementations have run successfully on every degree and prime.
The independent certificate directly reconstructed all finite bases and
Laplacians, verified full kernel dimensions and exact evaluation injectivity,
recomputed every transformed value, checked coefficient conjugation and
the rational real-form change, and verified every characteristic polynomial
and common-divisor factorization. The author has read the complete proof
and both complete programs, reconstructed the representation and coset
arguments, and rerun the final standalone certificate. Independent whole-proof
review remains separate from this author readback. This is not a Lean proof
or an audit of the arithmetic source interface.
