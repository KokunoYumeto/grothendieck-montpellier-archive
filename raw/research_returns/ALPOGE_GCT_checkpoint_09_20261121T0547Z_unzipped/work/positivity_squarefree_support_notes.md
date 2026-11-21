# P-F29: the complementary squarefree-support exclusion

Author/checker: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Theorem file: `work/positivity_squarefree_support.tex`.

The proposition treats only supports consisting of cubes and three-distinct-variable monomials. Under the same rational-span hypothesis as P-F27, it bounds the two-power determinant character strictly below `2^(n−1)`, without assuming full rank or that the matrix lift has that order.

The proof includes all cube columns in a rational rank basis. Any nonzero maximal minor must use the cube rows. Expanding those columns removes an odd factor `3^l`, leaving a square zero-one minor whose column lengths are at most `sqrt(3)`. Cramer's rule makes the denominator of the all-ones vector divide the chosen minor, so its two-part controls the determinant character. Hadamard's inequality is proved in the text by orthogonalization. When there are no cubes and the matrix has full rank, the common column sum three supplies an additional odd factor three. These bounds are strictly smaller than the target two-power in every case, including the empty residual minor.

Combined with P-F27 and its connected-graph extension, every remaining singular boundary representative must have both a square-linear monomial and a genuine three-variable monomial, and its square-linear graph must be disconnected in every eligible lift eigenbasis. The theorem does not classify the interaction between those graph components and the triple columns.

I reread the entire final proof at 2026-11-21T01:14:14Z and reconstructed every case. Root separately read the complete proof and reported PASS. An independent sibling review was requested from `/root/complexity`; the sibling's own ledger records its actual outcome. There is no external nonstandard theorem or historical-priority claim in this elementary determinant argument.

## Exploratory computation, kept distinct from proof

The actual C++ search is `work/search_cubic_support.cpp`; its actual stdout was copied from the returned tool chunks into `work/search_cubic_support_results.txt`. It completed 387,123 candidate matrices, including duplicates and rank-deficient candidates, for `3<=n<=14`. These consist of all single-column replacements of the chain matrix and 30,000 seeded random attempts per n with two through five column replacements. The choices can repeat a column, so an attempt need not change that many distinct columns.

For every full-rank candidate containing a genuine triple column, the script tested the two-adic order of the all-ones class by exact Bareiss determinants and Cramer numerators. It printed no candidate reaching `2^(n−1)`. This finite search does not enumerate all supports, all rank-deficient lattices, or all singular polystable forms. It is not used as a proof of P-F29 or a global support classification. The determinant computations use signed 64-bit integers; at n<=14 the relevant minors and products are bounded well below that range by the column-length bounds, including the single replacement column of ones in Cramer's rule.
