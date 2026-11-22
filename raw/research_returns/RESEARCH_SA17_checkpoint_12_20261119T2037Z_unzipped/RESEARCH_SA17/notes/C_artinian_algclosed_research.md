# C.3 finite-dimensional coefficient algebras over algebraically closed fields

Draft saved at 2026-11-19T16:47:43Z in sections/C_finish_artinian_algclosed_draft.tex, 251 lines. Root and dieudonne asked for independent audit. The source is deliberately unincluded during checkpoint07 freeze; draft catalog/check files are under notes/.

## Construction and scope

For a finite-dimensional commutative local k-algebra R of dimension c, k algebraically closed char>2, a rank-n R-free rational O_m,R-module of coefficient degree≤d is a k-tuple of size cn recording the R-action B_i and C_d(k)^*-action T_a. The products and commutation equations are polynomial. Underlying R-freeness is exactly existence of an invertible S intertwining B_i with n copies of the fixed regular multiplication matrices. Polynomial elimination makes this a constructible condition on the canonical tuple domains. No matrix-orbit quotient remains.

Idempotent summands remain R-projective, hence R-free because R is local. Thus the ordinary joint-centralizer idempotent test exactly filters indecomposables in the desired category. Coefficient degree is preserved under arbitrary basis change and gives no duplicates across d.

A specialized free tuple yields an actual R-basis: solve the linear intertwiner space and find a nonzero determinant value on a finite scalar grid. Coaction matrices are then computed over R. Use Hom_R(M,R), never Hom_k(M,k): R need not be Gorenstein. Type loci are polynomial by introducing this basis, R-matrix entries, a bilinear form matrix, the intertwining equations and det(residue B)≠0 as auxiliary polynomial conditions, then eliminating. For actual forms, solve the linear system and use the determinant grid again.

The additive category has split idempotents, finite Krull–Schmidt decompositions and finite-dimensional k-endomorphism algebras with nilpotent radicals. Every residue division algebra is k and each adjoint involution fixes k. QSS gives the same free split-WG basis as over k itself: symmetric self-dual U; hyperbolic H(U) with underlying2U for alternating type; and hyperbolic nonself-dual pairs. Tensor and exterior operations are over R and are computed after extracting R-bases, then converted back to full k-tuples for canonical decomposition. The bounds d+e and jd remain valid. Finite products of local algebras give every finite-dimensional commutative k-algebra. Any nonsingular symmetric form over such R is split by residue diagonalization and a finite nilpotent inverse-square-root polynomial.

## Primary sources actually opened/rechecked

Sergeichuk, Canonical matrices for linear matrix problems, author version https://arxiv.org/pdf/0709.2485 : §1.4, Theorems1.3,2.2,2.3, Remark2.1. Exact field-access scope and finite canonical parameter domains were independently audited in checks_C_templates_audit.tsv.

Quebbemann–Scharlau–Schulte, Quadratic and Hermitian Forms in Additive and Abelian Categories, J.Algebra59 (1979), https://webhomes.maths.ed.ac.uk/~v1ranick/papers/quebbemann2.pdf : original reopened, definition of additive duality pp265–266; split Grothendieck convention p267; reduction Theorem2.2/Corollary2.3 pp269–270; transfer Proposition2.4 and self-dual type Proposition2.5 p271; hypotheses(i)–(iii) and Theorems3.2–3.3 pp272–273. The proof requires no abelian category and no Frobenius/Gorenstein hypothesis on R. It is applied to the R-dual category, not the k-dual of its ambient k-representation category.

No historical priority is claimed. The classification is a newly assembled application of those established canonical-matrix and categorical-form theorems. The broad arbitrary-nonfield-base question remains outside this finite-dimensional algebra scope.

## Promotion and bounded example

The three main statements passed independent full written audits by root and dieudonne. Equation tags are now C.3.A1–A5, with canonical-section references corrected to T2/T5/T9. Final section is `sections/C_finish_artinian_algclosed.tex`; catalog and own checks are `results_C_artinian_algclosed.csv` and `checks_C_artinian_algclosed.tsv`. Independent dieudonne checks remain in `checks_C_artinian_algclosed_audit.tsv` without duplication.

The appended C:artinian_algclosed_example uses R=k[a,b]/(a,b)^2. Its k-dual has socle dimension1 while R has dimension2, whereas Hom_R(R,R)=R. The rank-two mu2 action is obtained from diag(1,-1) by P=[[1,a],[b,1]], with R-Gram form P^{-t}P^{-1}. The bounded certificate actually ran at 16:56:17Z, testing characteristic3/5/7/11, ranks1/2/3, twelve centralizers, 168 recovered basis elements, and four scrambled-basis recoveries. This certificate is explicitly not the full symbolic classifier.
