# A-015. The separate exterior-iterate question on scan133/006 is refuted

This supplements A-003's product counterexample. Use exactly its field, group, quadratic-form convention and split Green ring:

`k=algebraic closure of F₃`, `G=C₃`, `x=[J₃]`, `y=[J₂]`,

`x²=3x`, `xy=2x`, `y²=x+1`,

`λ_t(x)=1+xt+xt²+t³`, `λ_t(y)=1+yt+t²`.

The symmetric object `X` is the permutation module `J₃` with its invariant dot-product form; `H(J₂)` is hyperbolic. Take the actual symmetric object

`A=X⊥H(J₂)`.

Its underlying class is `a=x+2y`, of rank seven. Forgetting symmetric forms commutes with every exterior operation.

## The exact universal polynomial

The special-lambda iterate polynomial for `λ³(λ² a)` is

`Q_(3,2)=e₁²e₄−2e₂e₄−e₁e₅+e₆+e₃²`,

where `e_i=λⁱ(a)`. Here is a finite universal verification independent of any Green-ring example. In six indeterminates, `e₃[e₂]` is the sum of products attached to three distinct edges of the complete graph on those six indices. The possible degree patterns and coefficients of their monomial symmetric functions are

| Pattern | Coefficient |
|---|---:|
| `(3,1,1,1)` |1|
| `(2,2,1,1)` |2|
| `(2,2,2)` |1|
| `(2,1,1,1,1)` |6|
| `(1,1,1,1,1,1)` |15|

They correspond respectively to a star, a path, a triangle, an adjacent pair plus a disjoint edge, and a matching. Expanding the displayed elementary polynomial gives these same five coefficients. `check_iterate_defect.py` verifies the equality of every monomial coefficient using integer arithmetic. Specialization to six variables is injective in symmetric-function degree six, since every partition of six has at most six parts. Thus this is the universal polynomial identity, not only a test at one numerical alphabet.

## Evaluation in the actual split Green ring

Multiplication of the exterior series gives

`λ_t(a)=(1+xt+xt²+t³)(1+yt+t²)²`,

whose coefficients from degree zero through seven are

`1, x+2y, 6x+3, 10x+2y+1, 10x+2y+1, 6x+3, x+2y, 1`.

In particular, `λ²(a)=6x+3`. The degree-three coefficient of

`(1+xt+xt²+t³)⁶(1+t)³`

is `441x+7`: the degree-three coefficient of the first factor is `270x+6`, its degree-two coefficient is `51x`, and its degree-one coefficient is `6x`, giving `(270x+6)+3(51x)+3(6x)+1`.

The universal polynomial above, evaluated at the seven displayed exterior coefficients, is instead

`445x−4y+3`.

Consequently

`λ³(λ²(a))−Q_(3,2)(a)=4+4y−4x=−4(x−y−1)`.

The split Green group is free abelian on `1,y,x`, so this difference is nonzero. Because the forgetful map commutes with every exterior power, the corresponding iterate identity also fails on the actual symmetric object `A` in the literal split quadratic Grothendieck ring of `BC₃`. The coefficients are integers in that group, not scalars reduced modulo three. The exact quotient sends `x→3`, `y→2` and kills this difference, just as it kills the product defect of A-003.

Thus both universal questions on scan133/006 have separate explicit negative answers for its stated split ring: A-003 for multiplication, and A-015 for iterated exterior powers. The modern theorem for the exact/metabolic quotient remains compatible with both counterexamples through the explicitly given quotient map.
