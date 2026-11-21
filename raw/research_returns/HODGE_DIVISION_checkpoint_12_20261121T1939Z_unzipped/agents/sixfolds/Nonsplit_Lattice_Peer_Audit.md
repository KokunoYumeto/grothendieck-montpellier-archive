# Independent whole-proof audit of D-E8-LAT-01--02

**Result: PASS in the stated Gaussian signed-determinant-three scope.**

Reviewer: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

I read the whole original307-line nonsplit_lattice_section.tex and then
reread the complete enlarged LAT02 after its primitive-projector
paragraph was inserted. The proof under review is at
agents/g34_eightfolds/e8_grr/nonsplit_lattice_section.tex. This audit
covers its universal argument, not merely sample matrices.

## LAT01: rational form and splitting the two hyperbolic planes

Landherr's published theorem supplies rational isometry from a
signature(3,3), signed-determinant-three Hermitian space to
H^2 perpendicular <1,-3>. I independently opened the original
four-page article and read the invariants on p246 and their
completeness argument in the first paragraph of p247. Equal global
determinant classes imply equal local norm-residue invariants; the
signature supplies the infinite invariant. The published result is
used only for existence of a rational isometry and the rational Witt
index, not for a hidden denominator estimate.

The anisotropic part has dimension2: <1,-3> has a nonzero isotropic
vector exactly if3 is a Gaussian norm, which it is not. Thus the
maximal isotropic plane has dimension2.

The intersection of that rational plane with the integral lattice
is primitive: if a nonzero Gaussian multiple of a lattice vector
lies in the rational plane, the vector itself does. Over the PID
Z[i], it has a basis extending to the lattice. The nondegenerate
pairing from its two-dimensional span to the quotient has rank2.
Smith normal form on the rectangular pairing block gives the
displayed B=diag(b1,b2) and the remaining zero block.

The determinant identity Delta=Norm(det B)*|det A| is correct.
The original integral changes of basis and their inverses do not
affect denominator bounds, regardless of their coordinate heights.

I recomputed the two rational changes in LAT.4. With conjugate-linear
first arguments,

- subtracting v(B*)^-1 F/2 from w removes its self-pairing;
- subtracting v(B*)^-1 E from z removes the remaining cross-pairing;
- multiplying the new w columns on the right by B^-1 gives the
  identity hyperbolic pairing.

The z self-pairing remains A. The inverse formulas LAT.5 are
correct. Any product of inverse diagonal factors is cleared by
Norm(det B), and the sole extra factor2 is explicit. Thus both
directions have clearing integer2*n_b.

## Binary integral reduction

A nonzero vector minimizing the positive integer |A(x,x)| exists
because the form is anisotropic over Q(i). Such a vector is primitive:
a common Gaussian divisor of norm greater than one would decrease
its nonzero absolute value. It therefore extends to a basis.

After a possible overall sign change, the first coefficient is
a>0. Gaussian nearest-integer reduction of the cross coefficient
gives both |z|^2<=a^2/2 and |Re z|+|Im z|<=a. Minimality implies
|c|>=a. If c>0, negative determinant would require |z|^2=ac+d>a^2,
a contradiction. Anisotropy rules out c=0. Consequently

d=a|c|+|z|^2,  a<=sqrt(d),  |c|<=d.

These are valid coefficient bounds on an integrally equivalent
binary matrix; no bound on the earlier lattice basis is needed.

## The five-variable small-zero argument

I independently reconstructed the full proof, including its
nonvanishing step.

The quadratic form A(p)-t^2 is integral on the four real coordinates
of p plus t. Its symmetric coefficient matrix has absolute-entry
sum S=2a+2|c|+4(|Re z|+|Im z|)+1<=9d.

The form is rationally isotropic because A is rationally isometric
to <1,-3>, so it represents1. Its Witt index is exactly1: a rational
totally isotropic plane would meet t=0 in a nonzero vector, giving
an isotropic vector of A. Here anisotropy over Q(i) is exactly the
absence of such rational four-coordinate vectors.

Choose a primitive integral zero x of minimum sup-norm M and move
a coordinate of absolute value M into the fifth position, changing
its sign if necessary. This is a relabeling for the proof and need
not preserve the original t-coordinate.

If M>Q0^4, with Q0=floor(sqrt(3S))+1, the stated pigeonhole argument
in four coordinates produces an integral vector

y=(k/M)x+e,  0<k<M,  ||e||_infinity<1/Q0.

It is not proportional to x. Indeed a rational multiple of a
primitive integral vector is integral only when its multiplier is
an integer, whereas k/M is strictly between0 and1.

The reflection numerator z0=Q(y)x-2B(x,y)y is an integral zero.
Substitution y=(k/M)x+e and Q(x)=0 gives the cancellation

z0=Q(e)x-2B(x,e)e.

If z0=0 and B(x,y) is nonzero, y is proportional to x. If B(x,y)=0,
then Q(y)=0, and x,y span a totally isotropic plane. Both cases are
excluded. Thus z0 is a nonzero integral zero.

Its norm is less than or equal to3SM/Q0^2, which is strictly less
than M. This contradicts minimality and proves M<=Q0^4.
Since S>=1, Q0<=2sqrt(3S), so M<=144S^2<=11664d^2.
Anisotropy of A makes the original t-coordinate nonzero, so the
same bound applies to its absolute value. Every inequality and
integer-rounding direction is correct.

This is a complete universal proof. It does not rely on guessing a
constant from a finite enumeration, nor on an unlocated version of
Cassels' theorem.

## Binary isometry and both denominator directions

For v=p/t of norm1, put ell=v* A and u=(-ell2,ell1). Direct algebra
gives orthogonality, det(v,u)=1, and u*Au=det A=-d. Both v and u
have denominators dividing |t|.

Because d/3 is a rational Gaussian norm,3d is a positive integral
Gaussian norm. At every rational prime3mod4 its valuation is even;
factorization in Z[i] therefore gives beta with Norm(beta)=3d.
For alpha=beta/3, Norm(alpha)=d/3 and alpha^-1=bar(beta)/d.

The matrix T_A=(v,u/alpha) has Gram diag(1,-3). Its entries are
cleared by d|t|. Its determinant is alpha^-1, so its inverse is
alpha times its adjugate. The first inverse row has denominator
dividing |t|, the second denominator dividing3|t|. Hence3d|t|
clears both directions.

The displayed integral sign-repair matrix has determinant1 and
sends -diag(1,-3) to diag(1,-3). It introduces no new denominator.

Combining the two-sided changes therefore gives

q=(2n_b)(3d|t|)=6Delta|t|<=69984Delta*d^2<=69984Delta^3.

The wording correctly distinguishes a numerical upper bound for a
suitable clearing integer from a universal divisible clearing
integer. This distinction is maintained in LAT02.

## LAT02: source normalization and actual isogenies

For two lattices, P=T_T*T_S^-1 is an exact rational Hermitian
isometry. Taking N=q_S*q_T makes both NP and NP^-1 integral.
The bound N<=69984^2(Delta_S Delta_T)^3 follows directly.

For a compatible integral alternating form E and an integral
Gaussian action, h(x,y)=E(x,iy)+iE(x,y) is Hermitian with the stated
convention. In an O-basis and its induced integral basis, the
alternating determinant is (det h)^2. Thus |det h| equals the
product of polarization elementary divisors. The argument does not
leave an unknown rational polarization scale.

I also checked the new source-projector paragraph. The central
idempotent is the sum of the two complex character idempotents.
Its trace coefficients are rational algebraic integers, hence
integers. A reflection has rank-one negative space, so
e=epsilon*(1-s)/2 is a primitive self-adjoint idempotent in
Mat8(Q(i)). Consequently2|G|e is integral in the group algebra.

For the unimodular Jacobian lattice L, Lambda_S=W intersect L is
primitive. Every integral functional on it extends to L; unimodularity
and orthogonal projection imply that its polarization dual is eL.
Thus M Lambda_S^# is contained in Lambda_S for M=2|G|.
Every elementary divisor divides M, and Delta_S<=M^6.
The actual central automorphism iI preserves the image and its
integral lattice, verifying maximal-order stability.

At corresponding marked periods, NP gives an actual K-linear
isogeny and pulls back theta_T to N^2 theta_S. Top intersection
gives deg(phi)=N^12 Delta_S/Delta_T. An effective codimension-three
cycle has dimension3, so its pushed-forward theta degree is exactly
N^6 times its source degree. A rational K-isogeny preserves the
nonzero Weil projection. These are actual cycle and polarization
statements.

For a target of fixed conductor f, fO Lambda lies between fLambda
and Lambda, hence has index at most f^12. Its polarization volume
is at most f^12 Delta_T. Substitution gives N bounded by
69984^2 M^18 f^36 Delta_T^3. The subsequent identity isogeny pulls
back the original target polarization exactly and adds no further
degree factor. The proof properly retains fixed-conductor scope.

## Exact computation performed

The independently written nonsplit_lattice_certificate.py checks
generic symbolic binary complement, determinant and norm identities;
the reflection-numerator identity and its error-vector cancellation;
the exact five-variable symmetric-matrix convention; the sign
repair; the constants11664 and69984; and the generic binary
alternating/Hermitian determinant-square identity.

It actually ran and passed. An initial structural SymPy matrix
equality test did not simplify equivalent expressions automatically;
I replaced that comparison by entrywise symbolic simplification.
The simplified difference is zero. This was a checking-code issue,
not a change to any mathematical statement.

The written proof establishes the all-lattice and all-rank assertions.
The symbolic certificate has only the precise scope just listed.

## Primary-source record and limits

Landherr, Äquivalenz Hermitescher Formen über einem beliebigen
algebraischen Zahlkörper, Abhandlungen aus dem Mathematischen Seminar
der Universität Hamburg11(1935),245--248, DOI10.1007/BF02940728.

Primary article:
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf

Publication independently verified through the journal's own archive:
https://abhandlungen.math.uni-hamburg.de/archiv.php?vol=11

The determinant norm-residue and signature invariants on p246 and
the completeness proof on p247 were independently read.
Retrievals turn983683505view0 and turn879827771search0.
The DOI resolver did not return a page in my run; no claim of a
successful publisher landing-page inspection is made.

The conclusion is confined to Gaussian signed determinant class3.
It does not establish a comparable bound for arbitrary imaginary
quadratic fields or every determinant class. It supplies the explicit
fixed-lattice transport needed once a detector on the E8 source has
been proved.

