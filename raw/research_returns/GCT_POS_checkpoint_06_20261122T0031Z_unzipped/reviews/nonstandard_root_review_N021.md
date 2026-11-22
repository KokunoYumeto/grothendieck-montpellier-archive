# Complete root review of N-021

Date: 22 November 2026 UTC. Reviewer: `/root`; model: GPT-6 Astra Pro; effort setting: not exposed; run: GCT_POS.

**PASS within the stated finite-reduction scope.** The complete proof in `branches/nonstandard/dimension_degree_cutoff.tex`, including N-115–N-126, the symmetric-unimodal variant, and the unary-budget NP consequence, was read. The later scope clarifications were also read. The entire implementation `dimension_exponent_compression.py` was inspected and replayed; it returned `PASS_MECHANISM_NOT_GLOBAL_OPTIMIZATION` in approximately 0.122 seconds.

The distinction between a pair occurrence and its two monomial copies is maintained. Fixing all matchings from one existing solution produces a consistent integer system with row norm at most four and constants bounded by four times the original exponent bound. The matching is not asserted to be universal. Reducing nonpivot variables modulo the nonzero pivot determinant preserves integrality of the solved pivot variables, including negative determinant. Consistency handles every dependent row. Hadamard and adjugate bounds give the displayed uniform box. Merging exponents preserves score because coefficients add without cancellation.

Strict unit entries and prescribed zero slots cannot acquire new pair occurrences. Bar and finite label/opposite symmetries give additional matching equations of no larger norm. The proof preserves the specified common exponent lattice. General compression does not preserve unimodality; the separate symmetric-unimodal estimate applies to every table in that class by its interval support and coefficient mass.

For unary B, at most B additional pairs and binary exponents of length O(B + log(d0+1) + log(B+1)) form a polynomial certificate. Sparse binary-coefficient multiplication verifies associativity without expanding large coefficients into separate copies. The basis and finite symmetry data are part of the explicit input. No claim for a binary budget or efficient optimization is inferred.

The replay checks a two-label associative table with remote exponents, its exact score/bar/unit preservation, a dependent-row system, and all 132 rank-three source constants. It confirms d0=5, absolute mass4443 including19 unit entries, maximum mass576, the general bound43656·4^7276 with14568 binary digits, and the symmetric-unimodal bound9327. It does not enumerate the enormous finite search or compute its optimum.

The complete independent proof review by `/root/plethysm_proof` was read at `reviews/nonstandard_plethysm_review_N021.md`; it agrees and correctly treats the input extraction as a previously certified input rather than its own numerical replay.

## Primary-source credit

Papadimitriou, C. H. (1981). On the complexity of integer programming. *Journal of the ACM, 28*(4),765–768. https://doi.org/10.1145/322276.322287. Root opened the primary journal scan at https://ii.uni.wroc.pl/~aje/WordEq2015/papers/Papadimitriou.pdf and read Lemma1, printed p.766, and the main theorem with its proof, p.767. These credit the standard determinant/small-witness method. N-021 proves its particular monomial-matching application directly.

No global minimizing dimension ring, uniqueness, canonical categorical choice, or E(4) construction has been proved. The theorem's integral trace hypothesis does not automatically cover N-019's rational-coefficient table.
