# Two analytic comparison routes: exact hypotheses still missing

Date: 2026-11-21. Author: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

Status: new source/hypothesis audit after MA-RB-010. Neither route reduces the arithmetic gate MA-RB-008. No new theorem or equivalent-gate proposition is asserted.

## Analytic strong multiplicity one, with the unknown Artin denominator removed

A direct application to A and L_W would have to address the permitted poles of the latter. There is a concrete way to avoid that preliminary problem: compare the two degree-12 functions

F_1(s) = zeta_H(s),     F_2(s) = A(s) C(s) zeta_F(s).

The settled identity B = zeta_H/zeta_F = C L_W gives F_2/F_1 = A/L_W. Both functions have classical meromorphic continuation with only their possible pole at 1, and their factors satisfy the verified finite-image Ramanujan bounds. The already checked equality of the A and W gamma factors gives the same degree-12 archimedean type. This construction therefore does not assume Artin holomorphy for W. At a common good prime their first Dirichlet coefficients differ by exactly 4 on Omega and by zero off Omega: this follows immediately from the coefficient of T in the settled local ratio ((1+T)/(1-T))^2. No character certificate was rerun.

The applicable candidate source is Farmer–Pitale–Ryan–Schmidt, arXiv:1305.3972v2 (10 May 2025), Theorem 2.3, printed p.12. Its prime-closeness condition (2.20), defined on p.11, includes convergence for every sigma > 1 of

sum_p p |a_p-b_p|^2 (log p) p^(-sigma),

as well as a finite liminf after multiplication by sigma-1. In the present construction this is, apart from finitely many harmless terms,

16 sum_(p in Omega) (log p) p^(-epsilon),     epsilon = sigma-1 > 0.

Consequently this candidate requires convergence for every epsilon > 0. The known zero density of Omega and sum_(p in Omega) 1/p < infinity do not provide it. On the remaining comparison-failure branch, even convergence at epsilon = 1/2 would contradict MA-RB-002: it would imply convergence of the positive Euler logarithm of D_Omega on Re s > 1/2 and hence the already excluded abscissa <= 1/2 branch. Thus the source hypothesis is missing for an exact, identified reason. The newer liminf formulation must not be confused with ordinary density-one agreement. The older displayed stronger condition sum_(p<=X) p log p |a_p-b_p|^2 = O(X) would, for this integral discrepancy, already force Omega finite by taking X equal to each exceptional prime.

Only the exact analytic axioms, Theorem 2.3 and its prime-closeness definitions were inspected here. Its complete proof is not certified or invoked with an unmet hypothesis. Source: Farmer, D. W., Pitale, A., Ryan, N. C., & Schmidt, R. (2025). *Multiplicity one for analytic L-functions and applications* (arXiv:1305.3972v2), sections 2.1 and 2.6–2.7, pp.4–5 and11–12. https://arxiv.org/pdf/1305.3972 . The arXiv history explicitly dates v2 to10 May2025; the publisher lists the final article in2026, DOI10.1017/S0305004126102011. This audit uses the stated arXiv version.

## A GL5 converse theorem needs additional entire twists

Booker–Krishnamurthy Theorem1.1 applies to an admissible GL_n collection with automorphic central character, but requires the complete twisted functions to be entire of finite order and satisfy the specified functional equations for every unitary isobaric GL_(n-1) representation unramified at all finite places. For n = 5 these are GL4 twists. This quantifier is not supplied by the finite list of known S5 Rankin products in MA-RB-006.

Already the allowed isobaric twist 1 boxplus 1 boxplus 1 boxplus 1 makes the required completed function equal to the fourth power of the completed L_W. Its entireness is not established by the present input A: the factorization B = C L_W allows poles of L_W at zeros of the quadratic Dirichlet factor C. A locates those zeros but does not prove cancellation. The other arbitrary GL4 twists require substantially more analytic information. The theorem therefore does not construct the missing comparison from the available functional equations and meromorphic continuation alone.

Source: Booker, A. R., & Krishnamurthy, M. (2016). *A converse theorem for GL(n)*, Theorem1.1 and Remarks(1)–(3), author PDF pp.1–2. https://people.maths.bris.ac.uk/~maarb/papers/gln.pdf . These exact hypotheses and the isobaric definition were read. No complete proof review or application of the converse theorem is claimed.

## Scope

These checks address Euler/analytic comparison rather than adding further induced-character, Schur or Rankin order inequalities. Neither produces an actual missing estimate, an automorphic or residual Galois realization, or exclusion of the shared real zero. They are retained as precise failed applications; the current smaller arithmetic gate remains MA-RB-008.
