# Product-K3 Hodge calculation: proof and source audit

Date: 2026-11-19. Author/reviewer: frobenius. This auxiliary result is a proved Hodge input; it does not certify the prospective high-range local-geometric construction.

## Exact scope

For a jointly Hodge-generic tuple of s quartics containing lines, we require NS rank two, End_Hdg(T_i)=Q, and Hom_Hdg(T_i,T_j)=0 for i unequal to j. Such tuples exist by the local period description and countable proper Hodge-locus avoidance. Pairwise independence is included in the selected complex embedding. No assertion is made for every embedding of a merely coefficientwise Q-generic tuple.

The joint Hodge group of the transcendental spaces and the CM elliptic H1 is the product of the SO20 factors and the norm-one CM torus. A proper subdirect Lie algebra would identify two standard representations. The D10 representation input is justified by the exact opened Milne passages below, with the elementary observation that the only diagram involution fixes the vector node. The rational intertwiner descends because it solves linear equations over Q. No rational isometry of the quadratic forms is assumed in advance.

For the selected Kunneth tensor (tensor_i H2(W_i)) tensor H1(C), each nonempty transcendental support gives simple constituents of level 2|I|+1. The NS factors and the three isogenous elliptic factors produce multiplicities. We do not call a summand with these multiplicities simple. The resulting maximal level-one statement applies to the selected tensor, not every other summand in H^(2s+1) of the whole product.

Poincare duality converts the selected cycle component for any smooth proper curve P into H1(P)(-s) -> K. This proves uniformity for every proper parameter, including ones not defined over the original countable field.

## Opened sources

The five sources in C3_N6_Hodge_references.bib and their exact read locators are reused: Brevik–Nollet Theorem 1.1/Corollary 1.3(c), author p.2; Huybrechts Local Torelli Proposition 6.2.8 and section 6.2.4, author pp.107–108; CDK Theorem 1.1/Corollary 1.3, author p.2; Zarhin Theorem 2.2.1/Example 2.2.3, original p.211, with proof pp.212–213; Beauville Lemma 2/Example 3, published pp.106–107. The exact local downloads, hashes, opened markers and limitations remain in C3_N6_Hodge_source_audit.md and its manifest.

New primary source: James S. Milne, Reductive Groups, version 2.00 (10 March 2018), https://www.jmilne.org/math/CourseNotes/RG.pdf. Full 139-page PDF opened. Web retrieval refs: turn897850559view0 (full), turn578713123view0 (21.4), turn578713123view1 (highest-weight and Lie-algebra paragraphs), turn813176186view0 (18.26–18.27). Exact printed pages:

- 18.26–18.27, pp.91–92: standard orthogonal torus, weights and D_n roots.
- 20.3–20.4, pp.102–103: highest-weight classification/uniqueness.
- 20.33, p.108: universal simply connected group of a semisimple Lie algebra and equivalence of homomorphisms.
- 21.4, p.112: outer automorphisms of the split simply connected group are diagram automorphisms.

The direct urllib download returned HTTP 406; the complete primary PDF was nevertheless successfully opened through the web tool. This is recorded as a download failure, not a source-access failure. The 2022 Algebraic Groups book was also opened as a fallback, but is not used for any citation in this fragment.

## Status and remaining work

The auxiliary Hodge assertion and its all-parameter consequence are proved in C3_product_Hodge_inputs.tex. The parent and real_weil must independently check the prospective incidence-boundary/countable-subgroup geometry before a higher-range local restriction theorem is marked proved. This audit makes no claim about the C4 residual integral splitting problem.
