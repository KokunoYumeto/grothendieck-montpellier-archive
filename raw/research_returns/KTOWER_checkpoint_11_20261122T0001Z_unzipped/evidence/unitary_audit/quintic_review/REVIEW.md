# Independent order-five class bound and strict-group comparison

Reviewer: `/root/unitary_audit`, GPT-6 Astra Pro. Effort setting is not exposed.
Date: 2026-11-21 UTC. No Lean kernel execution or class-group recomputation.

## Independent whole-proof review: class-group bound

Read the entire `evidence/main_gate/order_five_length_bound.tex`, SHA-256
`65dcdf5622466d68c0ab803e854fc22f1ebd213fe604f6e5787ff024a8543d2e`.
KT-ORDER-FIVE-LENGTH-ONE passes. The analytic class-number factor is exactly
16 for a totally real quintic field. The four primitive even L-values give
a further factor 1/16. Thus the regulator lower bound produces 25/256,
and the stated rational estimate is strictly below 1/6.

Extension and norm identify Cl(F){p} with the invariants of Cl(Q(mu_p)){p}
under Gal(Q(mu_p)/F), because the extension degree is prime to p. The
trivial character component vanishes by norm to Q. The four nontrivial
characters are integral Teichmuller summands, and their Z_p lengths add
exactly to v_p(h(F)), which is at most one. This is a class-group result;
the proof itself makes no Selmer or K-group length inference.

## Exact primary source scope

R. Schoof and L. C. Washington, *Quintic Polynomials and Real Cyclotomic
Fields with Large Class Numbers*, Mathematics of Computation 50 (1988),
543-556. Author PDF: <https://reneschoof.github.io/sw.pdf>.
SHA-256: `dfb47b92b4b530c8083f31d8ad09993aced8f445387e9ee425e1745e72c91a29`.

The PDF is scanned and has no useful extracted text. I visually read
printed pages 543-547, including the complete Section 2 setup, entire
Theorem (2.2) proof on pp. 545-546, complete Corollary (2.6) proof on
p. 546, and complete Corollary (2.7) proof on p. 547. The Euclidean
logarithm-lattice covolume is sqrt(5) times the ordinary regulator, exactly
as used in Corollary (2.6). Corollary (2.7) applies to every cyclic quintic
field of conductor f and gives R >= log^4(f/2)/25. It precedes the special
Lehmer family in Section 3. Its imported earlier geometric product bound
M=16 is identified as Pohst's result; that earlier paper was not audited
here. The displayed h=1566401 example at conductor 641491 is explicitly
stated on printed p. 544; no independent computation is claimed.

Louboutin's primitive-even-character theorem and its complete relevant
proof were already independently read in this agent's sextic review.
Their exact scope and source hashes remain in
`../sextic_review/REVIEW.md` and its manifest. The small-prime
Hart-Harvey-Ong verification remains a carried input.

## New strict-group comparison: author scope

The separate `../quintic_strict_cyclicity.tex` proves a p-torsion injection
from the rational strict negative Tate Selmer group into the equivariant
Hom from the ordinary cyclotomic class group modulo p. Global and local
H0 vanish because the residual character has nontrivial order five.
At primes away from p, inertia invariants of the divisible coefficient
module are p-divisible, preserving unramifiedness on passing to finite
coefficients. At p, full local vanishing is preserved. Prime-to-p
inflation-restriction and class field theory then give the precise
character omega^(-e), without an inverse-character ambiguity.

The class bound therefore gives p-rank at most one. The carried VK-PT
comparison is a full group duality, so the finite strict Selmer group and
the corresponding finite K-primary group are cyclic. It is not a proof
that their common exponent is one or that they vanish.

For this application I reread the entire accepted K17 VK-PT/VK-LOCAL
theorem and proof, K17.tex lines 788-898, equations K5-K7. Its foundational
inputs remain carried. The new proof explicitly treats all positive even
weights: if r=v_p(e), the cyclotomic coefficient on G_Q(mu_p) first becomes
nontrivial at the chunk of exponent p^(r+2), rather than uniformly at p^2.

The previously checked Urban branch supplies a separate minus-eigenspace
class over the auxiliary quadratic field. If the rational plus-eigenspace
group survives, the total ordinary extension group has dimension at least
two. Thus the rational p-rank bound does not discharge the one-dimensional
total Selmer assumption of the inspected R=T theorem. Its other exact
weight, flag, and divisible-length hypotheses also remain in place.

The new strict-group proof was written and then read in full by its author.
Independent whole-proof reviews were requested from root and geometry;
this author record does not preempt their actual conclusions.
