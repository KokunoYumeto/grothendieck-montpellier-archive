# Remaining unrestricted C1 and residual C3 arithmetic — 2026-11-19T18:08:53.217773+00:00

This is an exploratory record, not a numbered theorem or counted gate reduction. We continue the two main questions.

## Opened primary sources

- Koji Uchida, Remarks on Grothendieck Rings, Tohoku Math. J.19(1967),341–348, full PDF opened at https://www.jstage.jst.go.jp/article/tmj1949/19/3/19_3_341/_pdf/-char/ja . Theorem1 concerns the ordinary Grothendieck group over regular domains of prime characteristic; Section2 gives order examples and warns against a false extension. It supplies neither an arbitrary-base Swan-kernel criterion nor the missing converse to modular-locus regularity. We do not apply a regular-domain assertion to the shallow singular ring.
- Barthel–Benson–Iyengar–Krause–Pevtsova, Lattices over finite group schemes and stratification, arXiv2307.16271v2, https://arxiv.org/pdf/2307.16271 . Intro/TheoremA and scope read: classification of tensor ideals of a derived lattice category over arbitrary Noetherian rings. The underlying category is relevant, but tensor-ideal classification does not itself compute K0, its exact generic kernel, or individual indecomposable objects. No new C1 implication inferred.
- Rogers–Schlichting, On the presentation of the Grothendieck–Witt group of symmetric bilinear forms over local rings, arXiv2311.03962v3, https://arxiv.org/pdf/2311.03962 . Introduction and Theorems1.2/1.3 read. Explicit unit generators with square, hyperbolic and Steinberg relations compute ordinary symmetric GW over local commutative rings with residue field notF2. This is more explicit than an unspecified isometry quotient, but is not by itself the equivariant modular answer or a noncommutative residual hermitian presentation.
- N. Grenier-Boley, Harrison's criterion, Witt equivalence and reciprocity equivalence, author manuscript https://www.math.uni-bielefeld.de/LAG/man/204.pdf . Intro and precise specialized scope read: quadratic-field unitary and canonical quaternion cases, not arbitrary division algebras with involution. Full later derivation not yet audited and not used as a theorem.

## Next arithmetic route

The perfect-field geometric indices are already explicit finite Galois orbits, but the current answer retains division and hermitian arithmetic. Investigate whether an explicit scalar-generator presentation with proved elementary relations for every finite-dimensional division algebra with involution, together with finite matrix extraction rules for tensor/exterior multiplicity forms, removes that residual group gate. A formula naming GW(D,sigma) does not suffice. A tautological presentation whose relations are all unknown high-rank isometries also does not suffice. The key missing step is a proved low-rank chain presentation valid for noncommutative epsilon-hermitian forms, with the alternating exception treated separately, and a genuinely explicit way to obtain all residual division data. No algorithm for arbitrary field arithmetic or quadratic solvability is silently assumed.

## Current smallest C1 instance

A=Z3[zeta3], pi=zeta3−1, R=A⋉F3 remains unsettled. All nine constant A[C3] lattices are classified, scalar/diagonal directions cancel, and every tested rank-three curvature primary has length0 modulo the target truncation. This is no proof that every class cancels. The active new route uses C3×C3 simultaneous directions and must survive the Mackey normalizer terms on induction to a symmetric group.
