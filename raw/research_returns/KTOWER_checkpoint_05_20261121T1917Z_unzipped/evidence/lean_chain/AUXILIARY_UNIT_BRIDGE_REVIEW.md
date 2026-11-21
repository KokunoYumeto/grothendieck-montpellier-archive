# Auxiliary-unit Selmer bridge and rational positive root

**PASS.** Read the entire 255-line `main_gate/auxiliary_unit_selmer_bridge.tex`, including KT-RATIONAL-POSITIVE-ROOT-UNIT. The new arguments preserve the auxiliary quadratic sign and use the local conditions actually displayed. No comparison to an unspecified deformation condition is claimed.

For a nontrivial cyclotomic exponent, the primitive character has conductor `|D|p`. Evaluating the inverse-indexed Stickelberger element on `χ ω^(−a)` gives `B_(1,χ ω^a)`, with precisely the inverse shown. CRT supplies `c≡1 mod p` and `χ(c)=−1`, making the additional annihilator factor a unit. The integral coefficient calculation is correct before restriction to the abelian subfield. It does not require `p∤φ(|D|)`. For a=0, the separate quadratic class-number/norm argument is valid and avoids a potentially zero imprimitive Euler factor.

The mirror character is `ξ=ω α^−1` for `α=χ ω^(a+1)`. The Kummer pairing therefore has exactly the displayed orientation. An everywhere unramified radical has valuations divisible by p and maps equivariantly to the p-torsion class group. The kernel is a unit class. Its odd part comes only from p-primary roots of unity, whose character is ω; ξ differs from ω because its auxiliary quadratic sign is negative. This proves the mirror injection and vanishing.

For the strict residual cohomology, restriction is exact because `[L:Q]=2(p−1)` is prime to p. Over L the coefficient module is trivial; local strictness at p and unramifiedness elsewhere give a class-group homomorphism. Its equivariance sees the character `χ ω^(−a)`, rather than its inverse. The transition to divisible coefficients uses global H⁰=0 from odd complex conjugation and divisible local invariants at every required place. At p, the nonzero residual exponent kills H⁰; for a=0 the invariants are either 0 or the whole divisible group. This verifies both the finite/divisible equivalence and the exceptional a=0 case. The resulting groups all have negative auxiliary quadratic sign, while the original untwisted target has positive sign.

For the positive-root lemma, normalized Kummer congruences reduce every allowed even b to `b0∈{2,4,...,p−3}` without a bound on the original weight. The Bernoulli unit kills the class component `ω^(1−b)` by the carried Herbrand implication. In the S-unit Kummer sequence for `Q(μ_p)`, inverting its unique principal prime over p adds only a trivial-character quotient. The ordinary odd unit component consists only of ω. Hence the required odd character `ω^(1−b)`, distinct from ω, has neither a unit contribution nor a class-group contribution. Twisting by `ω^(b−1)` and taking exact invariants gives precisely `H¹(G_Q,{p},F_p(ω^b))=0`, with no strict local condition at p. It does not kill the negative rational coefficient without its reflected input.

## Exact imported-source scope

Independently opened the accessible Washington book OCR and checked its title/copyright pages, §6.2 definition (p.93), Lemma 6.9 statement and short proof (p.94), Theorem 6.10 statement (p.94), and the concluding descent to an arbitrary abelian field (pp.99–100). The actual book is the **1982 first edition**, ISBN 0-387-90622-3, despite the hosting title saying 1997. The theorem has the required arbitrary-abelian-field scope. The preceding Gauss-sum proof is imported, not claimed freshly verified.

Source: https://www.scribd.com/document/1057328338/Graduate-Texts-in-Mathematics-83-Lawrence-C-Washington-auth-Introduction-to-Cyclotomic-Fields-Springer-Verlag-New-York-1997

The remaining Kummer/reflection/Herbrand inputs are the explicitly carried K17 results; no new claim of their Lean compilation is made.
