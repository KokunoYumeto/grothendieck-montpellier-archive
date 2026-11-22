# Independent audit of the proposed A131 effective concordance models

Auditor: tensor_and_finite. Date: 2026-11-19, 18:41 UTC.

Status: **PASS for the exact PL and semialgebraic effective-model theorem stated below.** This is an independent audit of `agents/singularities_duality/logs/A131_recursive_models_spec.md`, not an original-task closure decision. A115 and A116 are used in their already-audited form. Arbitrary o-minimal higher-family comparison and PL-to-SA weak equivalence are separate issues.

## 1. Exact conclusion and finite input

Given a finite abstract simplicial complex K, realized at standard rational basis vertices, there is a uniform finite algorithm describing two computable simplicial groups G_PL(K) and G_SA(K). Their q-simplices are exactly the PL, respectively semialgebraic, concordances over the field A of real algebraic numbers on (|K| x I) x Delta^q, jointly in all variables, preserving the whole parameter, fixing the bottom pointwise, and preserving the top setwise. K being a closed manifold is a promise needed only for subsequent manifold comparisons; no manifold recognition occurs in the algorithm.

Each group has a decidable subset of natural numbers as its canonical-code set in every degree, decidable code equality, and total computable group operations, faces and degeneracies. A115 and A116 identify their weak homotopy types with the corresponding full PL and SA concordance simplicial groups over every real closed field. Those results justify real algebraic coefficients; no assertion that rational coefficients realize all simplices or all parameterized families is needed or made.

The entire computable Kan complex is an explicit model of the whole space. For each r, a uniform algorithm also enumerates a complete countable presentation of its entire pi_r, including pi_0. This is a genuine effective presentation, not a finite decomposition, a finite presentation, a word-problem algorithm, or a claimed PL-to-SA equivalence.

If the initial object is a closed semialgebraic B, use a finite semialgebraic triangulation and its abstract K. The theorem takes that finite K as input. It does not purport to read an arbitrary noncomputable real parameter supplied as a black box. For a definable B in a general o-minimal expansion, the audited pi_0 comparison may still apply, but A116 does not replace arbitrary higher definable families by SA families.

## 2. Why validity is a finite decidable predicate

A real algebraic number can be coded by a primitive irreducible integer polynomial with positive leading coefficient and an ordinal among its real roots. Polynomial factorization, root isolation, arithmetic, order and equality are effective. Canonical algebraic-number codes can therefore be recognized and enumerated. Only countably many finite strings occur.

For PL, a graph code is a finite union of closed simplices with algebraic vertices in coordinates (z,z',t). One need not require the input simplices to form a simplicial complex. Membership in a simplex is expressed with barycentric variables lambda_i >= 0, sum lambda_i = 1 and coordinate equations v = sum lambda_i v_i. The vertex entries are constants, so every variable appears linearly. Domain membership is a finite rational semilinear formula. Both projection bijections, preservation of the domain and top, and the bottom identity are first-order linear formulas. Equality of two graph unions is another such formula.

Linear quantifier elimination is effective over the computable ordered field A. A direct algorithm puts a Boolean formula in disjunctive normal form, splits disequalities into strict inequalities, substitutes equalities when possible, and eliminates one existential variable from each conjunction by Fourier-Motzkin lower/upper-bound comparisons, with strictness carried along. Universal quantifiers are handled by negation. All scalar order tests are decidable in A. This gives a terminating finite validity/equality algorithm, however expensive.

Both projection bijections imply joint PL homeomorphism without an additional recognition oracle. Each projection restricted to any graph simplex is affine and injective, hence has an affine inverse onto its image simplex. The finitely many projected simplices cover the domain. Intersect their faces and triangulate the resulting finite polyhedral cover: on every piece the graph map and inverse are affine and compatible. The finite closed-cover pasting lemma supplies continuity, also in the relative order topology over A. In particular this step does not misuse ordinary compactness of a noncomplete real closed field.

For SA, finite polynomial Boolean graph formulas over A are enumerated. In addition to bijectivity and the boundary/parameter rules, the complete joint map and complete joint inverse must satisfy epsilon-delta continuity. Squared Euclidean distances express these tests in the ordered-field language. Real closed field quantifier elimination decides the finite sentences. Merely fibrewise continuity would be insufficient; the specification correctly requires joint continuity.

## 3. Why all operations really terminate

Inverse swaps z and z'. Composition is the graph formula

    exists y: Gamma_h(x,y,t) and Gamma_g(y,z,t).

An order-preserving map alpha:[m]->[q] acts by the integral affine map of simplices: replace t by alpha_*(s) and retain the new domain constraints. This covers degeneracies as well as faces; alpha need not be injective. The complete source and target of the resulting map both retain s.

In the PL case, these operations yield closed bounded semilinear graphs. A finite arrangement of their algebraic supporting hyperplanes decomposes them into finitely many algebraic convex polytopes. Barycentric or pulling triangulation produces algebraic simplex graph codes. Thus a code is known to exist before the output search begins. Enumerating raw codes, checking validity, and testing equality to the operation's finite graph formula therefore halts. No isotopy decision or unspecified homeomorphism construction is hidden in this search.

Length-lexicographic ordering of finite strings gives each code only finitely many predecessors. A raw valid code is canonicalized by checking those predecessors. For an operation formula, the first equal valid candidate found in the full enumeration is canonical. Equality of graphs then makes the group and simplicial identities literal identities of codes. In the SA case, closure under the displayed finite formulas and the verified continuity conditions proves the same termination.

The inclusion PL->SA is a total computable simplicial homomorphism obtained by translating graph simplices into linear formulas. This describes the whole comparison map without asserting an inverse or a weak equivalence.

## 4. Moore convention, including r=0

Let N_n = intersection_{i=1}^n ker d_i for n>=1 and N_0=G_0. Put Z_0=G_0 and Z_r=intersection_{i=0}^r ker d_i for r>=1. Then

    pi_r(|G|,1) = Z_r / d_0 N_{r+1}.

For r=0 this is the group of components. For r>=1 it is the usual homotopy group, and is abelian.

The simplicial identities give d_j d_0 u = d_0 d_{j+1}u = 1 for every required j, so d_0 N_{r+1} lies in Z_r. Conjugating u by s_0 z proves normality in Z_r, since the faces d_i u for i>=1 are trivial. With the standard two-face homotopy convention, a simplex w with d_0w=x, d_1w=y and d_iw=1 for i>=2 gives

    u = w (s_0 y)^(-1),    u in N_{r+1},    d_0u = xy^(-1).

Conversely u in N_{r+1} with d_0u=xy^(-1) gives w=u s_0y. The Kan property identifies this relation with homotopy of the spherical simplices. For r=0, the same normalization turns an edge into an element of ker d_1; Kan filling composes edge paths, and yields the same quotient. Pointwise multiplication of cycles is the usual homotopy-group operation.

The original May reference uses the opposite normalization, intersection of ker d_0 through ker d_{n-1}, with differential d_n. Apply its theorem to the reversed simplicial group: in degree n take d_i^rev=d_{n-i} and s_i^rev=s_{n-i}. Reversal of barycentric coordinates identifies its realization with |G|, and gives exactly the convention above. This avoids a silent index conversion.

## 5. Exact algorithmic output, and its limits

Membership in N_n and Z_r is decidable: only finitely many computable faces are compared with the identity code. Boundaries are the computably enumerable image of the decidable set N_{r+1}. Boundary membership, and therefore equality in pi_r, is semidecidable by enumerating fillers. No terminating negative answer follows from this construction, and no claim that every example has an undecidable word problem is being made either.

The complete countable presentation has generators x_z for all z in Z_r, multiplication relations x_z x_w=x_(zw), the identity relation, and boundary relations x_(d_0u)=1 for every u in N_{r+1}. The generator set is decidable and the relators have a uniform computable enumeration from (K,r). Since the boundary image is already a normal subgroup, these relations give exactly the Moore quotient. For r>=1, abelianizing this presentation changes nothing and yields an explicit countable integer relation matrix. For r=0 the group presentation must be retained, since components need not commute.

There is also a total horn-filling algorithm: check the finite horn compatibility conditions, then enumerate canonical simplices until their prescribed faces match. The simplicial-group Kan theorem ensures termination. This does not provide a sphere-filling algorithm that halts on nonboundaries.

The whole Kan complex, rather than just its groups, is supplied. Degeneracy is decidable by testing the finitely many identities a=s_i d_i a. Consequently its nondegenerate simplices and finite attaching face data give a recursive CW realization. Higher operations and the action of components remain encoded in the actual simplicial group. The presentations are consequences of this independently computable model, not a renaming of an unknown quotient indexed by unverified isotopies.

## 6. Executed finite certificate

Program: `agents/tensor_and_finite/code/check_A131_pl_codes.py`.
Output: `agents/tensor_and_finite/logs/check_A131_pl_codes.json`.
Run 2026-11-19 18:38 UTC: **30 tests PASS**, elapsed 0.830809 seconds.

The program treats a substantial rational subclass: B=point, q=0,1,2, triangulated graph codes with nondegenerate source and target projections. It does not implement general algebraic-number arithmetic or full RCF QE. All implemented arithmetic is exact Fraction arithmetic. The independent validity mechanism checks all vertices against the prism, the parameter/bottom/top constraints, exact source and target simplex volumes, pairwise intersection dimensions, and agreement of the induced affine maps on all intersection vertices. Exact total volume plus disjoint interiors and closedness certifies coverage: a missing point in the prism would have a relatively open missing neighborhood of positive full-dimensional measure. The affine overlap tests certify single-valuedness in both directions.

Composition actually intersects the intermediate cells and computes a pulling triangulation. Simplicial operators actually take affine inverse images of cells and triangulate them. Equality is checked on the common refinement, not by sampling points.

Positive cases include h(x,t)=x+(1/2)min(x,1-x,t,1-t), four triangles; its square, ten triangles; both inverse identities; a twelve-triangle subdivision giving the same graph; a nontrivial interval homeomorphism and its degeneracy; d_0s_0=d_1s_0=identity; and s_0s_0=s_1s_0. The genuine two-parameter family h(x,t)=x+(1/2)min(x,1-x,t_0,t_1,t_2) has eleven tetrahedra and all three faces equal to the identity. Five defective codes are rejected: a missing cell, a changed parameter, an image outside the prism, a disagreement along an overlap, and a moving bottom.

These are finite operational certificates. They do not prove the infinite Moore theorem or a word-problem decision, and they do not convert algebraic realizability into rational realizability.

## 7. Opened primary sources and exact locators

1. J. Peter May, *Simplicial Objects in Algebraic Topology*, 1967, original textbook scan, University of Rochester faculty mirror:
   https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/May-simp-ocr.pdf
   Opened 2026-11-19 18:36–18:37 UTC. Browser `turn480312691view0`; exact theorem search `turn925561412view0/1`; screenshots `turn646969073view0/1/2`.
   - Theorem 17.1, printed pp.67–68: every simplicial group is Kan.
   - Proposition 17.2, printed p.68: simplex multiplication induces the homotopy-group multiplication.
   - First Proposition 17.3, p.68: pi_q is abelian for q>=1.
   - Second Proposition 17.3, pp.68–69: normalized Moore complex and normal boundary subgroup. The duplicate 17.3 is in the printed original.
   - Proposition 17.4, p.69: Moore homology equals all simplicial homotopy groups.
   - Theorem 16.6, p.65: comparison with homotopy groups of geometric realization.
   - PDF zero-based image indices40–41 contain printed pp.66–69; index38 contains pp.64–65. These images were actually opened, not inferred from later quotations.
2. P. Goerss and J. Jardine, *Simplicial Homotopy Theory*, original 1999 text, 2009 reprint, faculty-hosted complete PDF:
   https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf
   Opened 2026-11-19 18:33–18:35 UTC, `turn868046114view0` (prior initial `turn698965437view0`). Lemma I.3.4 (Moore), printed p.12, PDF index26, includes the group-theoretic horn-filling proof. Proposition I.11.1, printed p.60, PDF index74, is an alternative realization comparison locator.

The source claims used here are only the short standard simplicial-group and realization results at these precise places. The finite-code argument and its computability analysis are proved above rather than attributed wholesale to either book.

## 8. Final TeX draft audit and independent program rerun

At 18:45 UTC I read the complete 398-line draft `agents/singularities_duality/logs/A131_recursive_models_draft.tex`. Mathematical audit: **PASS**. The draft's alternative algebraic-number encoding (integer polynomial plus rational interval containing exactly one root) is also valid. Replacing each such coefficient by a fresh variable with its unique-root constraint reduces arithmetic/equality/sign questions to rational RCF sentences; this is not circular, because the cited QE algorithm takes finite integer polynomials as input. Arithmetic output searches halt by closure of the real algebraic field.

Two presentational repairs were sent to the author: close the initial B-membership display before “i.e.”, and explicitly include affine-hull equations and ambient extensions of face hyperplanes when making the common subdivision. The latter handles projected simplices with different affine spans. Neither changes the statement or introduces a new hypothesis. The author was also reminded that finite-piecewise PL is the stipulated convention.

The singularities_duality agent independently read the entire finite checker, checked the projection-volume/intersection argument, and reran all 30 tests successfully in 0.842377 seconds. This is a separate human-style proof audit and executable rerun, with the finite scope unchanged. No assertion that the displayed nonidentity simplices represent nonzero homotopy classes is made.
