# R43: independent check of the marked generic-minimum algorithm

Reviewer: `/root/prime_arithmetic`; model label exposed to this session: GPT-6 Astra Pro. Date: 2026-11-21. Scope: the complete R43 statement and proof in `sections/effective_generic.tex`, including its input marking, comparison map, orientations, and extraction of algebraic witnesses. Outcome: **passes with its stated explicit-input hypotheses**.

## Component representatives lose no possible class

R42 gives finitely many projective Hilbert-product spaces with actual universal families. Absolute irreducible decomposition and a finite incidence graph compute their geometric connected components. Every nonempty component over an algebraic closure of a number field has an algebraic point, and such points can be found by exhaustive finite equation-solving operations. Finitely many chosen points, their cycle supports, and their multiplicities lie in one finite extension.

B01 gives constancy of the fundamental cycle class on every geometric connected component, including flat boundary fibers. The leading-degree label is constant as well. Passing to complex points adds no geometric connected components. Thus selected algebraic cycles represent all possible pairs (class, degree) under the input bound, including cycles originally parameterized by transcendental complex points. This is the essential finite reduction and it is used correctly.

## Compatible triangulation and the marking comparison

I read the full primary theorem in the saved source `work/text/basu_semialgebraic_triangulation.txt`: Basu, *Algorithmic semi-algebraic geometry and topology*, Theorem 4.5, printed p.14. It supplies an effective finite semialgebraic triangulation of a closed bounded semialgebraic set compatible with any finite list of semialgebraic subsets, so each subset is a union of images of open simplices. It also supplies the semialgebraic homeomorphism, rather than merely abstract Betti numbers.

The Hermitian-projector model of complex projective space is compact and semialgebraic: Hermitian matrices P with P²=P and trace1 are exactly rank-one orthogonal projectors. Equations for the projective variety and its subvarieties can be translated into this model by real-algebraic quantifier elimination. All input coefficients and the explicit marking graph are real algebraic.

Including images of all simplices and their faces from the old marking makes every open simplex of the new triangulation lie over one old open simplex. Closure then puts the images of its vertices in the closure of that same carrier. The proposed arbitrary choices of vertices of the respective vertex carriers consequently form a valid simplicial map F. On each simplex, the continuous comparison h₀⁻¹h and |F| lie in one closed old simplex, which is convex; the straight-line homotopy is coherent on shared faces. This proves F*τ is the specified target, rather than an unnamed isomorphic class. All carrier choices are finite semialgebraic tests.

## Fundamental cycles and effective orientation

Compatibility with each support and its singular locus gives the support as a subcomplex. The singular locus of an integral complex surface has real dimension at most2, so the oriented top-dimensional chain has no codimension-one singular-boundary contribution. The complex orientation of its smooth locus supplies the integral fundamental cycle, with actual generic multiplicities added afterward.

For each top-dimensional simplex, the semialgebraic homeomorphism is differentiable with full rank on a nonempty open semialgebraic locus. Otherwise, after finite smooth stratification, every image stratum would have smaller dimension, contradicting that the image has the full dimension of the simplex. The regular locus of the surface has algebraic complex coordinate projections that are étale locally. Their existence, the derivative limit predicates, and nonzero determinant conditions are first-order real-algebraic conditions; a real algebraic sample point and its orientation sign can be found effectively. Thus the orientation step does not require a numerical oracle or an uncomputed comparison of periods. The same argument orients the real eight-dimensional ambient fundamental class.

## Exact minimum and actual witnesses

Finite simplicial boundary matrices compute integral homology. The cap product with the oriented fundamental class carries the marked rational degree-four cocycle to the correct rational degree-four homology class by Poincaré duality. Exact rational linear algebra decides every candidate equality zᵢ−zⱼ=N t∨. Enumerating all 1≤N≤C and all component representatives is finite. The supplied upper bound ensures at least one equality, while the component argument ensures the least successful maximum of multiplier and degrees is the true minimum. The chosen universal fibers already provide equations for cycles over an explicit finite extension; no search for new algebraic cycles is needed after the comparison.

No claim is made that an abstract unnamed Betti basis or an unspecified Hodge vector is executable input. The explicit semialgebraic comparison map and rational cocycle are indispensable hypotheses and are present in R43.
