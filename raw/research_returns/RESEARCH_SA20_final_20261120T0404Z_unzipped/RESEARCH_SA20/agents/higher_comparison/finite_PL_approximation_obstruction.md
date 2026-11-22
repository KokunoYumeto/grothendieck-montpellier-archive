# A finite-PL approximation limitation

19 November 2026. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode),
agent `/root/higher_comparison`. This is a method limitation, not an
obstruction to the PL–semialgebraic concordance comparison.

## Exact statement and proof

Let F be an ordered field. If a continuous piecewise affine map
p:[0,1]→F has at most N affine pieces, for a positive ordinary integer N,
then its uniform distance from x↦x² is at least 1/(8N²). Equivalently,
there is an x∈[0,1] at which |x²−p(x)|≥1/(8N²).

Indeed, one affine segment [a,b] has length b−a≥1/N. Write m=(a+b)/2
and e(x)=x²−p(x). Since p is affine on [a,b],

    e(a)+e(b)−2e(m)=(b−a)²/2.

If all three absolute errors were less than (b−a)²/8, the absolute
value of the left side would be less than (b−a)²/2, a contradiction.
At least one of a,m,b therefore has absolute error at least
(b−a)²/8≥1/(8N²). This uses only ordered-field arithmetic.

In particular, over a non-Archimedean real closed field and for a
positive infinitesimal ε, **no finite PL map** is ε-close to x↦x².
For every ordinary finite N, ε<1/(8N²). Allowing vertices and slopes in
the larger field does not change the argument.

The map x↦x² is itself a semialgebraic homeomorphism of [0,1]. It is
semialgebraically isotopic to the identity, with endpoints fixed,
through

    H_s(x)=(1−s)x²+s x,  0≤s≤1.

For x<y, H_s(y)−H_s(x)=(y−x)((1−s)(x+y)+s)>0; endpoints are 0 and 1.
The map (x,s)↦(H_s(x),s) is a continuous bijection of the closed bounded
rectangle, and its inverse is definably continuous by definable
compactness (or directly from the monotone quadratic equation).
Thus this example does not contradict ordinary Hauptvermutung,
isotopy comparison, or any claimed concordance weak equivalence.

## Consequence for the attempted compactness route

A pointwise existence theorem for a PL representative up to definable
isotopy does not imply finite PL approximations at every positive
field-valued tolerance. In particular, ordinary real approximation
cannot be transferred by model-theoretic compactness into one uniform
finite graph format that works for all positive tolerances over all
elementary extensions. The desired family comparison needs an
isotopy or extension argument that retains the homeomorphism and
parameter conditions; infinitesimal C⁰ density is unavailable.

This also pinpoints why a radius of local contraction that depends on
the chosen graph format cannot be combined circularly with PL
approximations whose complexity increases as the radius shrinks.
