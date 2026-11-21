# Whole-proof audit of A11, with A10

Date: 2026-11-21. Independent checker: GPT-6 Astra Pro, `/root/effective_galois`; effort not exposed.

Reviewed source: `work/gt_certificates/positive_rank_theta/POSITIVE_RANK_THETA.tex`, including the complete four-step A11 proof after the explicit Frobenius-label normalization and direct Prym-image revision. I also read the complete A10 proof.

## Verdict

**A11: PASS. A10: PASS.** These are complete mathematical proof checks, not formal verification. A11 supplies a sufficient prime-power bridge and does not establish the existence of a theta point meeting its order condition.

## A11: symmetry, relative Frobenius and the cover

For a smooth curve in characteristic two the locally exact differential bundle B on the relative Frobenius twist is a line bundle with B squared equal to the canonical bundle. In genus two it has degree one. Riemann–Roch and Serre duality therefore give h0(B tensor L)=h0(B tensor L inverse), so theta is symmetric.

If L has exact odd order n, Frobenius pullback retains that order: its kernel on prime-to-two torsion is trivial, for example by composing pullback with norm, which is multiplication by two. Tensoring the relative Frobenius sequence by L is exact. The degree-zero line bundles L and F*L are nontrivial, so their H0 groups vanish and their H1 groups are one-dimensional. Theta incidence therefore makes the resulting H1 map zero, rather than merely noninvertible.

The revised proof explicitly chooses e with 2e congruent to1 modulo n and M=(F*L)^e on the original curve. Then M squared is F*L, while F*(M^(2))=M squared; injectivity of F* on n-torsion gives M^(2)=L. Thus the two zero maps are literally the semilinear arrows indexed1->2 and -1->-2 in the cohomology of the Kummer cover defined by M. This resolves the possible ambiguity between the original curve and its Frobenius twist. Exact-order n makes this Kummer cover geometrically connected.

The proof initially constructs the cover over an algebraic closure. Over a finite field, M, a trivialization of M^n, the roots of unity and the cover all descend to a finite constant extension. A further finite extension makes a chosen point above P rational; because the deck group is constant, the whole fibre above P then splits. These are permitted covers in A1's finite-field covering formulation.

## A11: primitive characters and the Prym

Every nontrivial eigenspace H1(C,M^i) is a line, including the imprimitive indices; the primitive sum is the sum over units modulo n. Multiplication by2 has at most two orbits under the hypothesis <2,-1>=U_n, represented by1 and-1. Each orbit has a zero arrow, so an iterate of Frobenius kills the entire primitive sum. The stable Frobenius rank, hence its 2-rank, is zero.

For n=ell^r and a=sigma^(n/ell), the order-ell subgroup has quotient D_(n/ell). Its nontrivial characters are exactly those with ell not dividing i, which are exactly the primitive conductor-n characters. Thus the whole relative Prym, not just a smaller subfactor, has 2-rank zero. The dimension check gives phi(n). One can justify the cohomological factor identification by the usual pullback/norm projectors: their denominators are powers of ell, so the product isogeny has odd degree and preserves the Frobenius decomposition in characteristic two.

For comparison, if n has two distinct prime divisors, the corresponding relative quotient has additional proper-conductor blocks. A single exact-order-n theta incidence need not kill them. The text's least-common-multiple argument correctly shows why no nontrivial deck element can be trivial on every proper-conductor character in that case.

## A11: lifting a hypothetical collision and the degree-two contradiction

The A1 covering condition applies after the finite constant extension and supplies Q_n above Q with delta=[Q_n-P_n] of 2-primary order. It is important that the condition ranges over all prime-to-two covers and finite constant extensions, as established in A01; it is not restricted to covers of prime degree.

The revised argument does not rely on an unspecified integral splitting of Jacobians. The point (a-1)delta belongs to the connected image of a-1, which equals the relative Prym, and remains 2-primary. Since a 2-rank-zero abelian variety has no nonzero geometric 2-power torsion, it vanishes.

The associated principal divisor aQ_n+P_n-Q_n-aP_n has four distinct support points: the deck action is free and the fibres above distinct P and Q are disjoint. It gives an actual degree-two function. A degree-two purely inseparable extension of a rational function field over an algebraically closed field of characteristic two is again rational; the genus n+1>=4 therefore forces this degree-two map to be separable.

Uniqueness of the hyperelliptic pencil makes a descend to an automorphism of P1. Its action is nontrivial because the kernel has order at most two, whereas a has odd prime order. Over the algebraic closure the induced automorphism has a fixed point. Its fibre has at most two points, so the odd-order group acts trivially on that fibre and fixes a point of D_n. This contradicts the free deck action.

Thus every step needed for the claimed separation consequence works, including the arithmetic model, the P-split lift and the prime-power conductor condition.

## A10: no geometric point of order three for a nonordinary genus-two base

Nonordinarity makes Frobenius nonbijective on H1(O), so its kernel H0(B) is nonzero. Since B has degree one, B=O(W) for a point W and 2W is canonical. Theta is therefore C-W. A nonzero order-three class on it would supply a function with unique pole of exact order3 at W. Riemann–Roch gives h0(2W)=h0(3W)=2, excluding that pole order. Absence of both nontrivial order-three theta incidences makes the two Frobenius arrows bijective, so the degree-three new factor is ordinary. This conclusion concerns the new factor; a nonordinary base still makes the entire covering curve nonordinary.

## Refinements incorporated during review

I proposed and the author incorporated the explicit M=(F*L)^e normalization and the direct image(a-1) argument. These tighten the presentation; no failure of the prime-power mechanism was found. The full revised proof was reread before recording PASS.
