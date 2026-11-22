# Independent whole-proof review of AM-R-017

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
22 November 2026 UTC; inherited reasoning effort is not separately exposed.

**Result: PASS in the stated source-level and fixed-family scope.**
I read all 324 lines of `work/research/explicit_t_primes_and_central_class_input.md`,
all 71 lines of its exact certificate, and replayed that certificate.
I also read the literal `Primes.Ok` conditions in
`AbelianHostFieldConditions.lean`206–238 and the definitions
`vT=divs(piT)`, `vTbar=divs(conj(piT))`, `vG=divs(conj(piG))`
at196–200. The orientation used for T in the finding is correct.

## Arithmetic and primality

The factored divisors in R17.2 multiply to the stated `586 L` and
`44 L`. The exact replay checks every required small prime by trial
division, `F | T-1`, `F^2>T`, each full power, and each coprimality
test. No probable-prime oracle occurs in the replay.

I opened the primary FLINT documentation at
<https://flintlib.org/doc/algorithms/number-theory/primality-proving.html>
and read Theorem 1 and its proof, lines199–200 of the retrieved page
(tool reference `turn853592822view0`). Its factored-divisor criterion
is exactly the one used. Independently, for any prime p dividing a
candidate T, each witness forces the entire required prime power in
F to divide p-1; hence F divides p-1. A composite T would have a
prime divisor at most sqrt(T), contradicting p>F>sqrt(T).

The norm, congruence and ideal-coprimality proof is sound. A common
prime ideal divisor of pi_T and its conjugate lies over T and
divides their sum 2A, contradicting gcd(T,2A)=1. Complete splitting
and the product equality then give exactly f selected exponent-one
prime ideals with residue field F_T. The `piT_Kq` caveat is necessary
and has been retained. The numerical size inequalities do not
prove `spread_le`; the finding correctly says so.

## Rational stabilizer

The monomial-group proof uses all complex embeddings and actual
integrality. For a nonzero entry x, the integral absolute norm and
the upper bounds |tau(x)|<=1 force equality at every embedding.
The finite bounded subset of the Minkowski lattice containing all
powers of x proves that x is a root of unity. The unitary row norm
then forces one nonzero entry per row, and orthogonality forces a
permutation. Thus Gamma=mu(E)^a semidirect S_a is exact.

The roots-of-unity calculation is also correct for both already
proved fields: their Galois groups have exponent42 and their
conductors have no additional possible 2- or7-power. Roots of
orders29,5 or13 would produce a cyclotomic quotient with exponent
divisible by4. Thus mu(E)=mu28.

For the vector (1,b,...,b^(a-1)), an element stabilizing its
projective mu28-orbit has translation stabilizer of a proper
consecutive interval in a cyclic group of order greater than a.
The unique gap of length greater than one proves that stabilizer
is trivial (with a=1 immediate). Distinct coordinate classes force
the monomial permutation to be the identity; injectivity of
mu28 reduction forces all diagonal roots equal. This proves
Gamma intersect P_u=mu28 I and Gamma intersect H_u={1}, including
the simultaneous conditions at the other T places.

The replay checked b=2 by every power 2^(28j), j=1,...,a, for both
actual ranks. No assertion about a primitive root or the complete
factorization of T-1 is needed.

## Central descent, source input and mass

With the explicitly stated conjugate-linear-first Hermitian
convention, the real matrix coefficient transforms by omega_infty
under a central rational root. The finite Steinberg coefficients
have central character one. The product condition R17.12 is
therefore exactly the descent condition for m and for its
conjugate F. Character restriction from F_T^times onto mu28 is
surjective, and the kernel has more than one element. Hence every
prescribed restriction has a nontrivial extension, including the
trivial restriction. All f T characters can be chosen nontrivial.

The actual source function has right H_u invariance and its
dilation sum is zero. Reading that equality as a full `RamT`
record still needs the source dictionary; the statement retains
that distinction. Its maximal29 invariance is genuine. There is
no class-number-one assumption: the function is on a single
adelic class and descends through its exact central stabilizer.

The support-class measure is vol(H)/28=d_T^(-f)/28. Independent
Schur orthogonality at infinity and G gives precisely

\[
             \|F\|^2=(28d_T^f d_\rho d_G)^{-1}.
\]

The explicit projective-level indices have zero11 valuation,
as verified by the exact replay. This does not make their
Archimedean size negligible; the finding retains that cost.

For comparison with DO035, note the harmless character-name
conversion: R017 uses `F_T=nu_R^(-1)`, whereas DO035 defines its
filter with `F_T=nu_D`. Set `nu_D=nu_R^(-1)`. The resulting
filtered vector is `sum_s nu_R(s) f_(su)`; all norm and scalar
formulas agree. This is a naming conversion, not an omitted
complex conjugation.

The result does not claim a nonzero theta lift for this particular
maximal29 input. Its compact projection issue, the exact raw
kernel, row lattices, MainX mass and unchanged `Fields.Kq` gate
remain explicit. I found no mathematical correction required.
