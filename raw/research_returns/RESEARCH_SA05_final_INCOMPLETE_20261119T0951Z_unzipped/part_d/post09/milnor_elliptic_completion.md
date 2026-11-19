# Non-root-of-unity Frobenius in an actual degree-one Milnor completion

19 November 2026. This is a concrete instance of the already established
ordinary/completed distinction. It is not a counterexample to
independence of realization primes and does not change the B1 gate.

Let k be the algebraic closure of F_2, let

    E: y^2 + y = x^3,

with origin O at infinity, and put K=k(E). The projective cubic is
smooth: the three partial derivatives of y^2 z + y z^2 - x^3 are
x^2, z^2, y^2, which have no common projective zero. It has the three
F_2-points O, (0,0), (0,1).

## Divisors and completion

The genus-one divisor-class identification gives an equivariant exact
sequence

    0 -> M=K^*/k^* -> Div^0(E) -> E(k) -> 0.

For completeness, the class of P-O identifies P with Pic^0(E): for a
degree-zero line bundle L, Riemann--Roch applied to L(O) gives its
unique effective degree-one divisor P. The kernel of the divisor map
on functions is k^*, because E is proper and connected.

The rational origin gives Div^0(E) the permutation basis [P]-[O]
indexed by P not equal to O. Every basis element has a finite
Frobenius orbit. Thus M is an actual Frobenius-stable subgroup of a
countable direct sum of finite permutation lattices.

Multiplication by three on E is surjective on k-points: its derivative
at the origin is the nonzero scalar three=one in characteristic two,
so it is a nonconstant morphism of proper curves. Reduction modulo
3^r and inverse limits therefore give

    0 -> T_3 E -> Mhat_3 -> Div^0(E)hat_3 -> 0.

The connecting maps on E(k)[3^r] are multiplication by three, hence
surjective. The left term is nonzero. Indeed P=(0,0) is a nonzero
point of order three: its tangent line y=0 intersects the cubic three
times at P, so the divisor of y is 3P-3O. The degree-one divisor-class
identification shows P-O is not zero. Surjectivity of multiplication
by three gives a compatible sequence of division points of exact
orders 3^r. Such a sequence is a nonzero element of T_3E. The inverse
limit is 3-torsion-free, because 3x=0 implies x_r=3x_(r+1)=0 at
every level; it consequently remains nonzero after tensoring Q_3.

Since k^* is 3-divisible, M/3^rM is canonically
K^*/(K^*)^(3^r). Hence Mhat_3 is precisely the 3-adic completion of
the actual Milnor group K_1^M(K), not an abstract module model.

## Frobenius without a normalization ambiguity

Use the arithmetic coefficient Frobenius of Schreieder's equation
(1.1), author p.1, in *Remarks on Milnor K-theory and Tate's
conjecture for divisors*. Under the equivariant divisor-class map it
acts on E(k) by

    phi(x,y)=(x^2,y^2).

There is a direct group-law calculation of phi^2. At a generic point
(x,y), the tangent line has slope x^2 and equation
Y=x^2 X+y^2. Its third intersection with E has coordinates
(x^4,y^4): substituting the line in the cubic shows that the third
x-coordinate is the square of its slope, while
x^6+y^2=(y^2+y)^2+y^2=y^4. Three collinear points sum to O, so

    [2](x,y)=(x^4,y^4+1),     phi^2=[-2].

This equality on a dense open extends to the elliptic-curve
endomorphisms. Therefore phi^2+2=0 on the nonzero T_3E submodule
of the completed Milnor group. Every Frobenius eigenvalue there,
after extending the coefficient field if necessary, satisfies
lambda^2=-2. Such a number is not a root of unity. For geometric
Frobenius F=phi^(-1), the equation is instead F^2=-1/2. Both
conventions give the same non-root-of-unity conclusion.

The assertion is about the nonzero stable Tate-module subspace; it
does not silently require the quadratic roots to lie in an arbitrary
chosen coefficient field. The fully elementary nonvanishing argument
above uses only the explicit three-torsion point. We retain just this
prime-three instance, which already proves the claimed distinction.

The formal example in Part B's note, Section 7, serves a separate
purpose: its extra eigenline exists only at the coefficient prime
three. This elliptic example is a genuine geometric illustration of
completion, and makes no claim of such a prime-specific discrepancy.

## Source and audit scope

The arithmetic Frobenius convention was independently rechecked in
the retained primary Schreieder text, equation (1.1), author p.1.
The standard divisor-class and group-law facts used here have been
spelled out above; no new numerical database or computer calculation
is used. Part B first checked the divisor/completion construction and
both Frobenius orientations, then read the complete actual note. Its
written audit passed the Riemann--Roch identification, the three-torsion
and division argument, the Tor transitions, and the tangent identity

    X^3+x^4X^2+x^2X+y^4+y^2 = (X-x)^2 (X-x^4).

The arithmetic divisor action agrees with coefficient Frobenius.
Following that audit, the unnecessary all-odd-primes sentence was
removed, so the note uses only the explicit prime-three construction.

Root independently read the complete actual note at 09:40 UTC and
passed the divisor-class, permutation, completion, nonvanishing and
tangent/Frobenius arguments. This was a written proof check, not a
primary-source reread or a computation rerun.

## Exact finite certificates

The smooth projective gradient ideal and all three F_2 points were
already certified in
`part_b/code/characteristic_brauer_counterexample.py`, with its retained
output `part_b/output/characteristic_brauer_counterexample.txt`. The
gradient Groebner basis is x^2,y^2,z^2, so there is no projective
common zero over any field extension, not merely over F_2.

The new program `post09/code/check_elliptic_tangent.py` was executed
at 09:41:42 UTC. Its eight exact F_2 polynomial checks passed in
0.059082 seconds. It verifies the tangent factorization modulo the
curve relation, the third intersection point, preservation of the
curve by Frobenius and doubling, and phi^2=[-2]. Output is
`post09/output/elliptic_tangent_certificate.json`; it also records
hashes of the existing point/smoothness script and output. The
infinite completion and Tate-module nonvanishing remain the written
proof above. No finite calculation is represented as proving them.
