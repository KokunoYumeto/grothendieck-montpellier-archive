# R40--R41: independent algorithm check and exact source locators

Date: 2026-11-21. Checker: GPT-6 Astra Pro; inherited effort not exposed; GHOSTS `/root/prime_arithmetic`. Source reviewed in full: `work/root_exact_algorithm.md`. Polished proof written and reread in `sections/exact_algorithm.tex`.

## Verdict

The procedure is valid with the explicitly stated cycle-input model and the codimension-two Tate theorem stipulated by the task. It returns a least complexity, not merely a certificate bound. The existence proof terminates but does not furnish a useful complexity estimate.

The input must contain the explicit universal families or effective maps from parameter points to cycles on the supplied bounded parameter space. Merely supplying equations for an unrelated parameter scheme would not determine its represented cycles. An abstract Betti or l-adic vector is deliberately excluded as target input.

## Full reasoning checked

1. Frobenius is semisimple on H1 and hence on H4. On H4(2), the geometric Tate subspace is exactly the sum of root-of-unity eigenspaces. Poincare pairing restricts nondegenerately because reciprocal eigenvalues stay either both roots of unity or both outside that set.

2. Frobenius data require no hidden oracle. For dimension four the zeta numerator and denominator each have degree128, from the even/odd sums of the binomial Betti numbers. Point counts over extensions of degrees1 through256 determine the rational zeta function by linear equations: two rational functions of these degree bounds with the same series through degree256 have numerator difference of degree at most256 vanishing through that degree, so are equal. Weil weights isolate H1. Exterior-power algebra yields H4(2). The root-of-unity test is finite: each root has algebraic degree at most70, hence order m satisfies phi(m)<=70; the elementary prime-power formula gives phi(m)^2>=m/2 and m<=9800.

3. Effective cycles over finite extensions span the geometric Tate subspace by the stipulated Tate input. Intersection numbers are rational, so their matrix rank is the same over Q and Q_l. Enumerate finite prefixes and stop when their Gram matrix has rank r. Do not greedily discard classes with zero self-intersection: graph surfaces provide many such classes. Nondegeneracy and spanning imply that some prefix reaches rank r; a nonsingular principal submatrix supplies r basis cycles.

4. For explicit surface cycles on a smooth fourfold, the derived-tensor Euler characteristic equals their intersection number. Each structure sheaf has Chern character beginning in codimension two, so in HRR only the product of the fundamental terms contributes to degree four. This is valid for improper intersections. Compute with locally free resolutions or affine-cover resolutions and coherent Hilbert polynomials, not an unjustified globally free resolution on a projective variety. Extend bilinearly over cycle multiplicities.

5. Each geometric connected component of the supplied bounded parameter space has one constant cycle class. Absolute decomposition, incidence connectivity, and closed-point search over finite extensions are finite polynomial-algebra tasks. The supplied universal family converts the point into an explicit cycle. Its degree and r rational intersections are computable. The finite list is exhaustive even if several components give the same class.

6. The target's r rational intersection numbers come from its actual rational cycle formula. Searching all N<=C and all ordered pairs of component labels, then minimizing max(N,Dplus,Dminus), returns precisely the minimum. The bound hypothesis guarantees at least one successful pair; nondegenerate testing makes every success cohomologically valid.

7. The simultaneous-realization version uses the explicitly stipulated identification of numerical and homological equivalence. No rationality test for arbitrary l-adic vectors is hidden in the method.

8. R41 gives a finite table on the domain of GOOD places only: B03/B04 supply the constant generic minimum outside their finite excluded set, and R40 evaluates the finitely many remaining good places. The target's explicit cycle specializes after a finite extension; geometric minima are unchanged by residue-field extension. The finite exceptional integer and generic exact minimum are inputs, not quantities silently computed by R41. If C0=1, the positive-multiplier convention and specialization give value1 everywhere, so b0 is unnecessary.

## Exact primary locators read

- The attached Milne report, `work/text/HEXAGON_2611.00244v1_Milne_report.txt`, Theorem3.1 and section3.2: the full Tate theorem for finite-field abelian varieties, used under the task's accepted 2026 theorem-input convention. The full source proof is not independently rebuilt here.
- John Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Inventiones Mathematicae2(1966),134--144, section2 pp138--139: the semisimplicity argument and its use on the Tate module. Theorem2(a), printedp140: Q[Frobenius] is the center of the semisimple rational endomorphism algebra. The article's main theorem is about homomorphisms; it is NOT cited as the general codimension-two Tate theorem. Primary article PDF: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf . Read the exact argument and statements in this run.
- William Fulton, *Intersection Theory*, second edition(1998), Theorem15.2 and Corollary15.2.1, printedpp286--288; the latter is the Hirzebruch--Riemann--Roch formula used above. The exact primary book text and formula were read in an indexed scan. Its full general Riemann--Roch proof remains classical background.

## Scope limitations retained

This is not a uniform runtime bound, and the supplied bounded parameter-space equations may be extremely large. It does not compute the local target vector from an abstract flat section. A separate proposed Betti triangulation route would require its own precise effective topology assumptions and source review, so it was not asserted in the polished theorem.
