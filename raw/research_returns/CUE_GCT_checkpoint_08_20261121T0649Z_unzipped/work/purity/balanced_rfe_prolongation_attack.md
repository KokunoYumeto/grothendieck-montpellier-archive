# Balanced-RFE prolongation and the width-three two-pair attack

Author: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.
Date: 2026-11-21. This is a working audit/attempt note, not an assertion that the full two-pair gate has been solved.

## Coordinate convention

Fix pairwise distinct nodes a_i over a characteristic-zero field, enlarged to its algebraic closure for geometry. Here B_k is the Zariski closure of evaluations of rational functions with both numerator and denominator degree at most k, and I_k is its prime vanishing ideal. Generic B_k points are t + sum_{j=1}^k z_j/(a_i-u_j). Balanced RFE, weighted common-center Lagrange SV, and unweighted common-center Lagrange SV must not be silently identified; the exact diagonal and center scalings are in P14/P16.

## Known prolongation background and exact specialized audit

Sidman and Sullivant (2009), Definition 1.1 and Theorems 4.1–4.2, relate derivatives, prolongations, and secant ideals in characteristic zero. The complete local proofs of Theorems 4.1–4.2 and Proposition 4.5 were read in the author preprint, pp.13–14, on 2026-11-21. The proof of Theorem 4.2 uses earlier Corollary 2.10 as input; no complete-paper verification is claimed. The following elementary rational-family argument is recorded as an audit, rather than reproving the published general theorem in the manuscript.

For a generic r of numerator/denominator degrees at most k-1, r(T)+z/(T-u) has numerator/denominator degrees at most k. If f belongs to I_k, differentiating in z at zero gives

    sum_i (partial_i f)(r(a))/(a_i-u) = 0.

The summands have distinct simple poles in u, so every residue is zero. Therefore partial_i f belongs to I_{k-1}. Constant directional derivatives obey the same inclusion. This first-order assertion does not need characteristic zero, but subsequent ordinary-derivative formulations retain characteristic zero here.

There is a stronger free-coordinate statement, useful for nonlinear individual degrees. Set u=a_i-epsilon and z=epsilon*s. At every other node the added term tends to zero, while at node i it is s. Thus the closure B_k contains the cylinder obtained from a B_{k-1} point by freely changing coordinate i. Consequently every coefficient of f as a polynomial in X_i lies in the balanced (k-1)-pair ideal on the remaining nodes. This statement is about a closure and is not a claim that every cylinder point has a nonsingular rational representation of the same degree.

The balanced one-pair variety has no nonzero linear equation: after removing the constant term, a linear equation would give a rational identity sum c_i/(a_i-u)=0, forcing all c_i=0. Its ideal is prime because the parameter domain is irreducible. Hence no nonzero product of linear forms belongs to I_1. P14 gives the stronger fact that no nonzero width-two ROABP belongs to I_1.

Balanced B_2 is the second secant cone of B_1: sums of two generic one-pole rational functions are precisely generic constant-plus-two-pole rational functions. Since I_1 has no linear form, Sidman–Sullivant Theorem 4.2 identifies the degree-three piece of I_2 with the first prolongation of the quadratic piece of I_1. Thus for homogeneous cubics, the condition that all first partials lie in I_1 is also sufficient. This sufficiency is a cited known secant theorem, not needed for I37's proposed direct argument.

## A proved local obstruction for multilinear cubics

Suppose a homogeneous multilinear cubic f lies in I_2 and a fixed coefficient cut U|V has exactly the three nonzero degree blocks 0,1,2 and total coefficient rank at most three. Each of the three blocks has rank one, so

    f = A(V) + L(U) B(V) + Q(U) M(V),

with L,M nonzero linear forms, B,Q nonzero quadratics, and A cubic. For a constant direction v on the U variables with v(L)=0, the directional derivative is v(Q) M. It belongs to I_1. Primeness and absence of linear equations force v(Q)=0. Therefore every directional derivative of Q along ker L is zero. In characteristic zero this implies Q=c L^2. Since Q is nonzero and multilinear while L is nonzero, a nonzero square coefficient of some U variable contradicts multilinearity. The block pattern 1,2,3 is excluded by exchanging U and V. Four nonzero degree blocks already force coefficient rank at least four.

This leaves the consecutive patterns {0,1}, {1,2}, {2,3}; it does not by itself exclude a whole width-three word. Missing-block decompositions and the central {1,2} pattern require further analysis. No general width lower bound is claimed from this local argument.

A further elementary constraint is that, in a nonzero cubic f in I_2, every pair of variables appearing in a monomial must occur with at least four different third variables. For fixed i,j, the coefficient vector c_{ijk} over k satisfies the three equations with weights 1, 1/(a_i-a_k), 1/(a_j-a_k). They follow from the translation and simple-pole identities for partial_i f and partial_j f in I_1. Every three columns of this 3-by-(n-2) matrix are independent, since a linear combination of the three rational functions has a numerator of degree at most two and cannot have three distinct zeros unless it is zero. This support constraint alone is insufficient: products of three linear forms can also have high pair codegree.

## Factor scope

For a multilinear polynomial, distinct nonconstant factors use disjoint variable sets, because individual degrees add in an integral domain. A factor inherits an ROABP in any fixed order by specializing the other factor's variables to values where it is nonzero. This permits irreducible-factor reduction in the multilinear setting. General factor width inheritance is false; see P-B22. The restricted observation must not be generalized to higher individual degrees.

## Current constructive handoff

Isolation proposed I37 for multilinear width-three words whose variable-dependent factors are all singular. The candidate uses the derivative inclusion above, I36's one-pair preservation of internal rank-two intervals, compatible endpoint gauges, a tridiagonal Hessian, and a path argument. Its proposed endpoint normalization was independently challenged and refined: first choose an active complement to the first row-kernel containing the nonzero endpoint row, and at the final cut choose the passive complement inside the final endpoint's kernel. Simply deleting arbitrary passive endpoint components would change the polynomial.

The complete I37 proof was subsequently independently read and passed at04:43:04 UTC. I38 further handles isolated invertible affine factors, with a complete independent reading at04:54:52 UTC. Longer full-rank runs and higher individual degrees remain separate gates. In particular, a rank-three factor can permit a passive state to persist through a longer excursion, and a nonlinear rank-two factor can have nonzero higher-order passive entries even though its tangent passive diagonal is zero. The affine singular-factor proof must not be extended to these cases without a new argument.
