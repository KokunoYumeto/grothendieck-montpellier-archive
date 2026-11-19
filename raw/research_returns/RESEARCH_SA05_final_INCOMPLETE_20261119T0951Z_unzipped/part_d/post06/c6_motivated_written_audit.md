# Conditional motivated C6 theorem: written proof and source audit

Recorded 19 November 2026, after the complete root and Part C written audits and integration at 07:50 UTC. This note concerns the sufficient finite-field-rank implication, not a converse or an unconditional solution of general C6.

## Exact deliverables and conclusion

The source fragment is `part_d/c6_motivated_rank_reduction.tex`, with labels `c:motivated-unramified-rank-reduction`, `c:motivated-abelian-strata-unramified`, and `c:motivated-rank-reduction-scope`. Part C integrates it. The earlier algebraic fragment is `part_d/c6_rank_conjecture_reduction.tex`; its hypotheses have been corrected to require a fixed homogeneous rational algebraic correspondence whose action is idempotent, without requiring an idempotent in the Chow ring.

Assuming independence of homological equivalence over the algebraic closure of the residue field, in the precise formulation equivalent to van Dobben de Bruyn's correspondence-rank conjecture, every rational Andre motivated motive over a number field has coefficient-prime-independent ranks of all powers of local monodromy and coefficient-prime-independent unramifiedness at the original place. No weight-monodromy hypothesis is introduced. No arbitrary absolute-Hodge class is asserted to be motivated.

## Operator audit

I read `root_motivated_operator_note.md` and `root_rank_diagram_note.md` completely and independently reread Andre's printed pages 10--14. On a primitive Lefschetz string, the factorial formula for the Hodge involution gives its square equal to one and conjugation of the raising operator to the normalized lowering operator. The factor formula of Lemma 1.3.2 then gives partial lowering operators from a whole-product Hodge involution. The grading operator yields factor-degree projections by interpolation. The finite Weyl operator recovers each factor involution with the degree sign on the input, hence on the right. The ordering matters, already for the projective line.

Global Hodge involutions are finite rational expressions in algebraic Lefschetz maps and inverses of Hard-Lefschetz isomorphisms. Iterated primitive projection is valid degree by degree. The displayed equality on Andre's printed page 11 between two differently normalized star conjugations is not used: direct evaluation on the projective plane distinguishes coefficients one and two. The needed normalized identities instead follow from the explicit formula on page 10 and are independently computed in the retained exact tests.

For a motivated correspondence represented by a pushforward of an algebraic class multiplied by the Hodge involution of another class, external multiplication, the whole-product factor-star expression, diagonal pullback, multiplication and pushforward have the required degree and Tate-twist balance. This avoids any assumption of an algebraic generic Kunneth projector and any unproved tensor-product comparison for the weight spectral sequence.

## Geometric and graph audit

A finite Galois extension permits all required semistable alterations simultaneously. Replacing each alteration by the disjoint union of its conjugates gives the needed semilinear action. No integral descent of the model is claimed. Saito's Lemmas 3.2--3.3 explicitly supply the transport maps and direct-sum alteration argument. For inertia, the residue action is trivial and the stratum maps are algebraic; permutation signs are included.

Transfers use pullback and degree-normalized pushforward. Their image projector is imposed at the level of E2 cohomology. In particular, a transferred Hard-Lefschetz map is inverted only on those image subspaces, never on the whole cohomology of an alteration. Equations imposing the image subspace and the inverse graph replace chain-level inverses. A projector need not be idempotent on E1.

The image of an output projection restricted to the kernel of a finite constraint map has dimension equal to the rank of the stacked constraint/output matrix minus the constraint rank. The separate cohomology-map block formula reduces these ranks on E2 to finite E1 block ranks. All such blocks are rational algebraic correspondences. Projective-space padding first aligns degrees and twists and then aligns dimensions by degree-zero factors; thus the published rank conjecture applies literally to one correspondence on a finite disjoint union.

For a final monodromy power, the row is shifted by twice that power and the Tate twist is shifted by its negative. Monodromy is used as the spectral-sequence operator, not treated as a generic motivic degree-zero arrow. Distinct Frobenius weights give E2 degeneration and a canonical generalized-weight splitting. Its compatibility with monodromy makes the rank on the abutment the sum of the computed graded ranks, without the weight-monodromy conjecture or semisimplicity of Frobenius.

If one realization is unramified, the common ranks give zero monodromy for every coefficient prime. Inertia then factors through one finite quotient. The same algebraic E1 calculation applied to each element minus one gives identity on the associated graded. A finite-order operator which is unipotent in characteristic zero is the identity. This proves descent to the original place without a trace formula for motivated projectors.

## Field of definition and semisimplicity

Andre section 1.1 fixes the base field K; section 2.1 and Definition 1 use smooth projective K-schemes, algebraic cycles, and ample line bundles there. Thus the literal category has K-defined presentations. If one instead starts with an invariant presentation over a finite Galois extension, its auxiliary scheme with its actual ample bundle can be viewed over K, and the trace of the componentwise operator is the sum of the conjugates. Dividing by the extension degree yields the invariant operator. This does not require replacing the polarization by a different one.

The abelian-strata corollary requires actual algebraic abelian-type presentations for every stratum of all auxiliary alterations. The current abelian Tate input gives homological equals numerical equivalence on all products in that category. Jannsen (1992), Theorem 1, printed pages 448--449, proves numerical semisimplicity unconditionally; the exact proof including Lemmas 1--2 was opened and read. The additional equivalence of cycle relations supplies the realizations needed here. A common numerical image projector has coefficient-prime-independent trace/rank. No positivity of an arbitrary geometric primitive form is inferred from category membership.

## Independent checks and boundaries

Root read the complete written fragment, the operator and graph proofs, Saito's complete section 2.4 and Lemmas 3.2--3.3, and the exact van Dobben implication proof. Part C independently read the full 311-line fragment, the same relevant primary construction proofs, and Andre's definition. Both passed. Root's retained exact computations test 21 primitive strings, 100 tensor cases, and 96 rank-diagram cases; they are supporting certificates, not substitutes for the proofs.

The result remains a sufficient-conjecture implication. The reverse direction would require a geometric realization of arbitrary finite-field correspondence ranks in the monodromy of pure number-field motives. Neither formal Weil--Deligne linear algebra nor an arbitrary compact rigid motive is such a realization.

## Primary source locators

- Andre (1996), section 1.1, printed page 10; Proposition 1.2, pages 11--12; complete Lemma 1.3.2, page 13; section 2.1 and Definition 1, pages 13--14. Original: https://www.numdam.org/item/PMIHES_1996__83__5_0.pdf.
- Saito (2003), author version June 9: Corollary 1.2.6, page 16; Corollary 2.2.4; complete section 2.4, pages 33--36; complete Lemmas 3.2--3.3 and Theorem 3.1 proof, pages 36--39; Lemma 3.7. Original: https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf.
- Van Dobben de Bruyn (2020), Theorem 1, page 3; Definition 4.1, Remarks 4.2--4.4 and Theorem 4.6, pages 15--17; complete Theorem 5.1 proof and Corollary 5.2, pages 17--18. Original: https://arxiv.org/pdf/1808.00119.
- Jannsen (1992), Theorem 1 and complete proof, pages 448--449. Original: https://epub.uni-regensburg.de/26642/1/jannsen10.pdf. DOI: 10.1007/BF01231898.
