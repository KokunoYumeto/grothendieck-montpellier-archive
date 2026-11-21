# Independent complete-proof checks of A15 and A16

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed;
/root/effective_galois.

## A15: PASS

Source read in full:
work/gt_certificates/positive_rank_theta/A15_COMPOSITE_BRIDGE.tex

SHA256 at review:
7ffd115c4fa2584a584e994cdaf8b0cf07241ce3505132ac8467a6a901d503a8

All five steps, the arithmetic table, the several-point criterion and the
primary-projection limitation were read. No mathematical gap was found.

1. A separable degree-two genus-two to genus-one map in characteristic two
   has different of degree two. Wild ramification forces exactly one ramified
   point, with different exponent two. The Deuring–Shafarevich calculation
   f_C-1=2(f_E-1)+1 gives f_C=2f_E, excluding rank one.

2. In the odd cyclic group, the elements of orders given by its distinct
   prime factors lie in independent primary factors. Their subset products
   are distinct. The expanded projector therefore gives exactly 2^r simple
   zeros and the same number of simple poles, spread over two disjoint free
   deck orbits. The resulting function is separable, since it has simple zeros.
   The inequality n>(2^r-1)^2 holds for every odd n>1, including r=1,2.

3. The Castelnuovo–Severi induction has the correct indices. If the prior
   field has index d/s and adjoining another degree-d function has relative
   degree a, the new index is d/(as), while its index over that rational
   subfield is as. The written genus bound is exactly
   a(s-1)^2+(a-1)(as-1)<= (as-1)^2.
   The generated field cannot be the whole function field, by genus n+1.
   Its residual degree e is a nontrivial power of two.

4. The action on the intermediate curve is faithful because any kernel order
   divides both e and odd n. It is free because a stabilizer of odd prime
   order would partition a fibre divisor of degree e into orbits of that
   prime length. Thus its genus and quotient genus must both be one.
   A zero of the induced function has reduced fibre, and each of the two
   original deck orbits maps injectively to the intermediate curve. The
   fibre therefore has at most two points, forcing e=2.
   The separable quadratic involution is normalized and hence centralized
   by the odd deck group. Its quotient induces the forbidden separable
   double cover of a genus-one curve by C.

5. The Frobenius normalization of an odd-order theta point is correct.
   Each nontrivial cohomology eigenspace is a line, with doubling of
   characters. Theta and its negative force zero arrows in the corresponding
   orbits. The stated unit condition covers all primitive orbits.
   The group-ring projector vanishes precisely at nonprimitive characters;
   odd denominators preserve the 2-primary decomposition. The primitive
   factor therefore has zero 2-rank.

The several-theta-point assertion is an exact equivalence for a fixed cyclic
subgroup: a cycle of semilinear maps of lines has zero stable part if and only
if at least one arrow is zero. Distinct cyclic subgroups cannot be conflated
with this coverage condition. The examples 15,21,35,45,33,105 and their orders
of 2 were checked arithmetically in the read; they are only unit-group examples.

Primary source locators independently opened:

- Poonen, Gonality of modular curves in characteristic p, Proposition 2.1,
  Lemma 2.2 and Corollary 2.3, author p.3.
  https://math.mit.edu/~poonen/papers/gonality.pdf
  Web reference turn182210809view0.
- Anbar–Beelen–Nguyen, A new tower with good p-rank meeting Zink's bound,
  Theorem 1, equation (1), author p.3.
  https://backend.orbit.dtu.dk/ws/files/123787793/p_rank_abn.pdf
  Web reference turn182210809view1.

The new proof supplies the needed Castelnuovo–Severi induction explicitly.
The external Deuring–Shafarevich theorem is used as a cited input, not claimed
to have been re-proved.

## A16: PASS

Source read in full:
final/proof_sources/composite_theta_example.tex

SHA256 at review:
b7ca247121441bf3e46229602ee6b12d8dc16c6d5766ce0e838f2d4bc8237845

The entire proof, computation-scope paragraph and smaller degree-five
comparison were checked. No final source was edited.

The reciprocal Artin–Schreier model has poles of orders three and one,
so the genus and rank are two and one. The exact differential dX/X^2 has
divisor 2P; hence the explicit one-fold Frobenius twist of the Raynaud
theta translate is retained correctly over F8.

The norm identity and nonzero conjugate evaluation give a zero of order 15
at R and no other finite zeros. The unique pole has order 15 because
X^5Y has that order while A has pole order at most 14. The norm certificate
coefficients agree with the displayed proof. I read the complete independent
SymPy verifier and its saved PASS output; I did not claim this reading as
a separately authored arithmetic implementation.

Geometric exact order is checked, including proper divisors. Order three
is excluded by l(3P)=l(2P)=2. A function with divisor 5(R-P) would, after
scaling, be Y+a2*X^2+a1*X+a0. Its norm has coefficient one at X, whereas
(X+z^2)^5 has coefficient z. This excludes order five even over the
algebraic closure.

The odd Kummer cover is étale and geometrically connected. The local
parameter t=X^2/Y has valuation one at P, and the residue of t^15*F is one:
the leading term reduces to (X^5/Y^2)^7, whose residue is one from the
curve equation. Thus the asserted pointed model is justified. F4096 contains
F8 and all 15th roots of unity, and the genus is 16.

The two doubling orbits of units modulo 15 are exactly the displayed two
orbits. The primitive factor has dimension 8 and rank zero. The conductor-3
factor is ordinary by A10. The order-five norm coefficient condition forces
X=1 on every geometric order-five theta point. The trace of z+1 to F2 is
one, so no such point is F8-rational. Each nonzero power of M^3 is rational,
and the theta embedding and its Frobenius twist preserve rationality.
All conductor-five arrows are therefore bijective. Its dimension and rank
are four. The resulting total rank is 1+2+4=7, not one; the whole new
factor has positive rank six. Applying A15 is valid, and does not replace
primitive rank zero by whole-new rank zero.

For the degree-five comparison, the norm of Y+X+1 is indeed
X^5+X^4+X+1=(X+1)^5. The point and conjugate evaluations, pole order five,
and exact order five follow as stated. The reciprocal model still has
poles of orders three and one. The branch point at X=0 gives
div(X)=2(Q_5-P_5), hence identical prime-to-two abelian Kummer classes,
while the theta cover separates. This proves the comparison without
an unproved minimal-degree claim.
