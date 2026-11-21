# Independent audit of the level-one U(3) and weight-13 GL(2) computations

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro, 2026-11-21 UTC.
Reasoning effort: not exposed.

**Verdict: PASS for the local/coefficient-space model and the exact numerical
computations.** The separate global packet-coverage theorem and the source
translation to the K-group criterion are retained as separate obligations.
This report does not infer K12 vanishing from a finite computation alone.

I read every line of `compute_u3_weight5.py` and
`compute_gl2_weight13.py`, all scalar output fields, and the complete schema
of every saved neighbor. I reran both calculations. I then wrote and ran
`tripod_independent_check.py`, which reads only their JSON outputs, imports
neither original program, and uses only Python's standard library. That
checker reconstructs the harmonic equation, all neighbor identities, the
theta coefficients by norm enumeration, eta products by a different exact
recurrence, both Hecke matrices, both characteristic polynomials, and their
integer evaluations and prime factorizations.

## 1. The definite Hermitian lattice really has class number one

Let O be the Eisenstein integers with norm N(a+b omega)=a^2-ab+b^2.
Its hexagonal Voronoi cell has vertices of squared distance 1/3 from O.
Thus every complex number can be reduced modulo O to squared absolute
value at most 1/3. This also proves that O is norm-Euclidean and hence
a principal ideal domain.

For a positive integral unimodular Hermitian O-lattice of rank three,
choose a Hermitian Korkine-Zolotarev basis. This exists by successively
choosing shortest primitive vectors in the lattice and its orthogonal
projections, and extending over the PID. Write a,b,c for its successive
Gram-Schmidt squared lengths. Reducing the coefficient of the second
vector along the first gives a vector of norm at most b+a/3. Minimality
of the first gives b >= 2a/3. Applying the same argument to the projected
rank-two lattice gives c >= 2b/3. Consequently

    1 = det(L) = abc >= 8a^3/27.

The first length a is a positive integer, so a <= 3/2 implies a=1.
An integral vector of norm one splits off orthogonally: subtract its
integral Hermitian pairing from any lattice vector. Its orthogonal
complement is again integral unimodular. In rank two the same reduction
gives det >= 2a^2/3, forcing its integral first minimum to be one.
The remaining rank-one norm is then one. Thus the lattice is O^3.

Every finite adelic translate of the standard selfdual lattice gives
an integral unimodular global lattice by intersection, and the preceding
argument identifies it with O^3 by a rational unitary isometry. Hence
the double-coset class number at the full lattice stabilizer is one.
There is no unexplained replacement of a connected parahoric by the
full stabilizer in this lattice argument.

The integral automorphism group is exactly mu_6^3 semidirect S_3.
Indeed a column of an integral unitary matrix has norm one, a sum of
three nonnegative integral norms; it therefore has exactly one unit
coordinate and two zero coordinates. Orthogonality forces distinct
positions for the three columns.

## 2. The full invariant coefficient space is one dimensional

The complex harmonic polynomials of bidegree (5,5) on C^3 carry the
irreducible compact unitary representation of highest weight (5,0,-5).
This follows also from the usual contraction decomposition of
Sym^5(C^3) tensor Sym^5((C^3)^dual): the trace-free highest component
has that highest weight. Its dual has the same highest weight, so the
coefficient-space dual convention does not alter the model here.

For a monomial z^alpha conjugate(z)^beta of this bidegree, invariance
under each of the three independent sixth roots of unity requires
alpha_i-beta_i divisible by six. Both exponents lie between zero and
five, so alpha_i=beta_i. Invariance under S_3 therefore reduces the
problem exactly to symmetric degree-five polynomials in
x_i=z_i conjugate(z_i). There are five partition monomials. The complex
Laplacian becomes

    sum_i (x_i d^2/dx_i^2 + d/dx_i).

Its symmetric degree-four target has dimension four. The independent
checker builds the matrix directly and exhibits a four-by-four minor
equal to -360. Thus its kernel has dimension one, without relying on
a numerical nullspace calculation or assuming surjectivity.

The exact invariant vector has coefficients 2,-25,20,320,-360 on
the partition monomials (5),(4,1),(3,2),(3,1,1),(2,2,1), respectively.
The checker verifies every Laplacian coefficient is zero. Its value
at (1,0,0) is two. Class number one identifies the entire algebraic
modular-form space at this weight and level with this invariant line.

## 3. The neighbor lists are complete right-coset representatives

At p=7 take pi=3+omega; at p=13 take pi=4+omega. In both cases N(pi)=p.
For each projective line ell in F_p^3, the data give an integral
three-column matrix U satisfying

    U^* U = p I,     rank(U mod pi)=1,     image(U mod pi)=ell.

These identities are checked entry by entry in Eisenstein integer
coordinates. Since U and U^* are integral and U inverse equals U^*/p,
all pi-elementary divisors of U are zero or one. Rank one modulo pi
forces them to be (0,1,1). Therefore g=U/pi is unitary and has
elementary divisors (-1,0,0) at pi. At the conjugate prime its elementary
divisors are (0,0,1), and away from p it is integral invertible.

The right cosets of the negative minuscule double coset are classified
by the line pi*g*O_pi^3 modulo pi*O_pi^3. The checker lists all lines
independently as (1,a,b), (0,1,a), (0,0,1) and verifies that every one
occurs exactly once. There are 57 and 183, respectively. This proves
completeness from exhibited matrices and the elementary-divisor
classification; it does not depend on an unproved bound for an integer
search or on the discovery program finding every norm-p vector.

For completeness the discovery bound is valid as well: if
a^2-ab+b^2 <= p, completing the square bounds both |a| and |b| by
2 sqrt(p/3). The chosen box is larger than that bound. Its phase
normalization identifies only the six common unit multiples, which
preserve the projective line.

## 4. Representation action and Satake normalization

Use the actual representation convention

    (rho(g)f)(z) = f(g inverse z).

Changing a right-coset representative g to g gamma for gamma in the
integral stabilizer leaves rho(g)f unchanged, since f is invariant.
For g=U/pi, evaluating at the first unit vector gives the three first-row
norms of U divided by p. Thus the program's evaluation is precisely

    lambda_p = [sum_neighbors f(N(U_1,1),N(U_1,2),N(U_1,3))] / (2 p^5).

The use of rows here matters. First-column values are not invariant
under the arbitrary right changes of the chosen orthonormal basis and
would not compute this operator. The original code uses the correct
rows. As an independent check, I verified the full eigenvector identity
at five other integral vectors at each prime, using exact Eisenstein
dot products. The mathematical proof that evaluation determines the
operator is the invariant-line calculation and coset completeness,
not those extra point checks.

Initially these representatives give the inverse minuscule operator
at pi. Complex conjugation carries them to representatives for the
positive minuscule operator at the same chosen split factor. It
preserves the invariant polynomial, and at the first unit vector gives
the same row norms. Hence the positive and negative operators have
the same scalar on this line. Equivalently one can use the positive
operator at the conjugate place.

For Haar measure giving the maximal compact volume one, the Satake
transform of the positive GL3 minuscule characteristic function is
p times the standard trace. I freshly read Gross, *On the Satake
isomorphism*, section 2's measure convention and all of section 3
through equations (3.13)-(3.14), printed pages 3 and 6-8. In particular
(3.14) with n=3,i=1 gives exactly this factor. Primary:
https://people.math.harvard.edu/~gross/preprints/sat.pdf . Fresh web
retrieval `turn396569473view0`, exact formula `turn460047228view0`,
full adjoining passage `turn392910988view0`. A direct-download attempt
returned HTTP403; the web retrieval was successful and read.

Thus if t_p is the normalized Satake trace, then

    p^6 t_p = p^5 lambda_p = A_p,
    A_7=157899,  A_13=6110859.

These equalities have no hidden stabilizer-volume factor: the Hecke
operator is the sum over the actual distinct right cosets, and class
number one identifies each with its displayed rational unitary matrix.

## 5. The GL2 space and series are the claimed full space

Put a=theta for the Eisenstein norm lattice, b=eta(3z)^9/eta(z)^3,
and D=eta(z)^6 eta(3z)^6. I freshly opened and read the full paragraph
"Modular forms on Gamma1(3)" in Clery-van der Geer, *Generating Picard
modular forms by means of invariant theory*, arXiv:2110.00849v2,
printed page 12. It states that the graded ring is C[theta,psi^3],
where psi=eta(3z)^3/eta(z), and identifies odd weight with the character
chi_-3 on Gamma0(3). Hence a and b have weights one and three and
precisely that odd character. The same primary paper, Remark15.2,
printed page33, identifies D as a weight-six cusp form on Gamma0(3).
Primary https://arxiv.org/pdf/2110.00849 ; fresh retrieval
`turn396569473view1`, exact paragraph `turn460047228view1`, exact
Remark15.2 `turn392910988view1`. The full PDF was downloaded to
`clery_vandergeer_2022.pdf` and converted locally to text.

D has no zero in the upper half-plane because eta has none. Its
q-order at infinity is one. The eta transformation under z maps to
-1/(3z) shows D|_6 W_3=-D with the normalized Fricke operator, so its
order at the other cusp is also one. Gamma0(3) has just these two cusps.
Division by D therefore identifies S_13(Gamma0(3),chi_-3) with
M_7(Gamma0(3),chi_-3), with no introduced interior or cusp poles.
The polynomial-ring description gives the exact three-element basis

    D*a^7,  D*a^4*b,  D*a*b^2.

Their leading orders are one, two and three, with coefficient one.
Independently, the valence bound at weight seven is 7/3, so vanishing
of the first three coefficients in M7 already forces zero; this is
a second dimension bound, not an appeal to a few matching coefficients.

The theta coefficient is 6 times sum_{d|n} chi_-3(d), by norm-ideal
factorization in the Eisenstein PID and its six units. The independent
checker also obtains these coefficients by enumerating lattice elements
of norm at most55 and verifies their equality. It constructs both eta
products by their logarithmic derivative recurrence instead of the
original binomial product algorithm. Every division in that recurrence
is checked to be exact. The saved series and leading matrix agree.

## 6. Exact GL2 Hecke matrices and arithmetic evaluations

At these split primes chi_-3(p)=1. The coefficient formula is

    [q^n]T_p f = a_(pn) + p^12 a_(n/p),

with the last term zero unless p divides n. The first three coefficients
and the lower-triangular leading matrix with diagonal one determine
each column uniquely because the basis is complete. I verified all
available further coefficients as well: through n=7 at p=7 and n=4
at p=13. In particular the n=7 check includes the second Hecke term.
The independent implementation uses only integer triangular elimination.

The characteristic polynomials are

    P_7(X)=(X-40250)^2 (X+153502),
    P_13(X)=(X-1284050)^2 (X+9397582).

Their expanded coefficients agree with both saved matrices and their
direct trace, principal-minor and determinant formulas. All reported
integer evaluations and prime factorizations pass exact multiplication,
and each listed factor passes trial-division primality. At p=7,

    P_7(7^12+1)*(7^12+7^6+1-A_7)
      = 2^15 3^19 7 13^5 37 43^3 47^3 61 271^3.

The largest prime factor is271. The independent p=13 calculation
gives the saved factorization and the two-prime common divisor has
prime support {2,3,7,13,37,47}. No bound on coefficient fields is
needed: a congruent eigenvalue forces divisibility of the characteristic
polynomial evaluated at the comparison integer.

Numerically A_7-7^6=40250 and A_13-13^6=1284050, so the U3 obstruction
factor agrees with the repeated GL2 factor at these primes. This is
only an exact numerical identity here; this audit does not infer an
endoscopic identity or exclusion of every cuspidal GL3 representation
from two local eigenvalues.

## 7. Scope and reviewed hashes

The class-number, invariant-line, full-neighbor, Satake-factor and GL2
space claims above are mathematical proofs, supplemented by exact finite
checks. They justify the two local computations on the stated spaces.
I also read the entire separate `work/hecke_coverage/u3_coverage_proof.md`,
but its global KMSW and ramified-local proof is undergoing a distinct
primary-source audit. The exact statement connecting these spaces with
the manuscript's admissible-representation alternatives and the final
K12 criterion remains the parent's source-interface proof. No broader
coverage is silently inferred in this report.

Original script hashes:

- U3: `6c712599833e9d7209626f856d1e1ba9b95530e352cad38698a16afda5be5b28`.
- GL2: `531b4311313fe5afc90f537a51e7167bffae30b85f87de93d99ee2f37087d182`.

Saved exact-output hashes:

- U3: `3759b83dad147e55157f340f913560dfaea51bc0277d44a1a900d0d6136d79ef`.
- GL2: `e06bd004449d6b0a822b6d02d765cea03f43ed040724dc02de36419b887fd101`.

No mathematical correction to either calculation is requested. The
positive/inverse Hecke convention should remain explicit in the final
proof.

## Addendum: clean seven-matrix theorem

I wrote and then read the entire clean translation
`u3_hecke_section.tex`, including the added contraction-surjectivity
formula and the smaller complete neighbor-orbit calculation. The product
rule gives the claimed coefficients `(j+1)(11-j)` in the contraction
formula, so the kernel has dimension216; the highest-weight vector and
Weyl dimension identify exactly the stated irreducible representation.
The displayed four-by-five Laplacian matrix agrees with a separate direct
monomial calculation and has first four-column determinant64800.

For the smaller neighbor proof, all p+1 lines in the last two coordinates
have rational block-unitary representatives fixing e1 by the already
proved rank-two class-number assertion. The remaining coordinate line
has the displayed diagonal phase representative. For first coordinate
one, the image of the sixth roots of unity is all nonzero residues at7
and the square subgroup at13. This proves the stated disjoint orbits
and their multiplicities. Evaluation at e1 is constant under the integral
subgroup preserving its complex line, since the coefficient polynomial
has equal holomorphic and antiholomorphic degree. Any two rational
representatives of the same adelic right coset differ on the right by
the integral stabilizer, so there is no further dependence on a basis
choice. The seven literal matrices then give every remaining value.

The new `u3_orbit_certificate.py` is a second standalone standard-library
certificate requiring no input file. I read it in full and ran it. It
checks every Gram and reduction identity, proves finite orbit coverage
by exact set equality, verifies the harmonic equation, and reproduces
both weighted sums and prime factorizations. It passes. This agrees
with the independent full240-neighbor data-only checker.

The new TeX and bibliography compile in a standalone document. After
two line-breaking repairs, the draft-mode compile returned zero with
no warnings or overfull/underfull boxes. The final source was then
read in full; subsequent changes only made the conjugated unitary
representative and the word 'scalar' explicit. The theorem keeps
global packet coverage and the K-group interface separate. The
findings in this addendum are self-checks of the clean theorem, with
independent whole-proof review requested from the parent and sibling.
