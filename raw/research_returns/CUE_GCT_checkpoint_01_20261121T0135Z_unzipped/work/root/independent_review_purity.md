# Targeted whole-proof review of G-01--G-06

Date: 2026-11-21T01:00:44.957376+00:00
Reviewer: /root/purity_zero_status; GPT-6 Astra Pro; effort not exposed; run CUE_GCT-20261121-purity.
Method: read each complete statement and proof in `work/root/findings.tex`; rederive each algebraic and geometric implication while checking conventions. This is a targeted proof review, not a claim of formal certification or an independently constructed proof predating access to the supplied proof.

## G-01

The Burnside-ring partitions and the regular C2 counterexample are correct. The subset operation linearizes to the trivial representation whereas exterior square of the permutation representation is the sign character, so the claimed distinction is substantive. The special lambda-ring formulas are correct. Precision requested: the torus-character calculation must be made first for the universal defining representation of GL_r and then pulled back along G -> GL_r; an arbitrary group G (including the displayed C2) need not have a diagonal torus detecting its representations. This is a repair of the written justification, not a counterexample to the result.

## G-02

For i >= 2, specialization y=1 and algebraic independence of elementary symmetric polynomials prove the claim. Precision requested: state i >= 2 explicitly, or handle i=1 separately, because the written list of earlier operations includes x=lambda^1(x). The mathematical terminal-index correction for the nontrivial operations is verified.

## G-03

PASS. The even/odd binomial sums are both 2^D, their class difference is (1-L)^(D+1), and gamma^1 of a rank-zero class is itself. Thus the product belongs to the claimed filtration piece. The constant-weight multiplicities differ. Expanding (1-exp(c))^(D+1) establishes the Chern-character truncation. D=0 also works. The associated-bundle caution correctly avoids asserting nonisomorphism on every base scheme.

## G-04

PASS. The image of the orbit coefficient homomorphism lies in the torsion-free coordinate ring of GL_N, hence is Z-flat. Polynomiality gives the finite matrix and homogeneity the grading. An invertible maximal-rank block and vanishing larger minors reduce the matrix to diag(I_r,0) after inverting the chosen minor. Both kernel and image are direct summands there. This justifies only degree-d compatibility and correctly excludes an all-prime equality between reduced orbit closures and total-space fibers.

## G-05

PASS. Independently retrieved and read Beauville's primary author-hosted statement: https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf, printed p.46, Proposition 3.1(a), web ref turn359884138search12. It gives the linear determinantal representation for a noneffective degree g-1 line bundle. Such bundles exist by the stated dimension comparison; the genus-zero case is correct. Smooth plane forms are a dense open subset, linear substitutions belong to the orbit closure because invertible endomorphisms are dense, and therefore all ternary forms are contained. A weight with zeros after the third position cannot use any coefficient variable involving later basis directions, since all polynomial weights are nonnegative. A nonzero polynomial in the ternary coefficient coordinates cannot vanish on the full ternary affine space. Hence the determinant ideal has no highest-weight vector of at most three rows, and complete reducibility gives multiplicity equality. This is stronger than occurrence absence and correctly applies to every competing orbit closure in the ambient space.

## G-06

Dimension computation and the exactly-four-row conclusion are correct, subject to one group-action convention repair. With the ordinary direct-product law, (P,Q) acting as PAQ is not a left action; it is an action of the opposite second factor. Preferred repair: use H={(P,Q):det P=det Q}, action A_i -> PA_i Q^(-1), with scalar stabilizer (cI,cI). Then A1=I forces Q=P; a distinct-eigenvalue A2 forces P diagonal; the stated A3 forces scalar P. The common scalar subgroup gives the universal stabilizer lower bound, and the exhibited tuple shows the generic stabilizer has dimension one. Group dimension is 2n^2-1, so orbit dimension is 2n^2-2 and image dimension at most 2n^2+2. The codimension expression binom(n-1,3) is correct. Restriction of an orbit-closure point lands in the closure of determinantal quaternary forms by continuity. Pulling back a nonzero equation is injective on the four-variable coefficient polynomial ring. A GL4 highest-weight vector extends to a GL_N highest-weight vector in the chosen Borel convention; later-variable raising operators annihilate it. G-05 excludes lengths at most three, leaving exactly four. The warning that the equation may still vanish on the padded permanent is necessary and present.

## Overall outcome

No substantive gap found in G-03--G-05 or in the geometric conclusion of G-06. G-01, G-02, and G-06 require the above precise wording/convention repairs before a final PASS event for the written proofs. No claim of historical novelty was assessed.

## Revision recheck — 2026-11-21T01:06:11.687342+00:00

The revised G-01, G-02, and G-06 statements and complete proofs were reread. The three requested precision repairs have been incorporated and pass this targeted proof review. No unresolved gap remains in G-01 through G-06 identified by this review. This is a targeted whole-proof review, not a formal certification or an independent reproof.
