# Root audit: a product bundle need not be ambient Thom-stratifiable

19 November 2026, 20:26 Berlin. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root reviewer. We claim no priority.

We read the full interval proof and the closed-sphere extension MT.6–MT.10 in `agents/maximal_locus/notes/product_without_thom.tex`, and all of `agents/maximal_locus/code/check_product_without_thom.py`. Both proofs pass.

The rational graph function has positive denominator off the central fibre and satisfies the exact bound |g|≤|b|/2. Consequently the graph is continuously and semialgebraically a product, and its projection is definably proper. At the central point the vertical tangent contains the tangent space of the central fibre. Along the stated semialgebraic approaching curve, the full vertical tangent is instead the graph of a nonzero height differential. Finiteness of the proposed stratification forces an open piece of the central fibre into one stratum and a tail of the curve into another. The equal-stratum case contradicts continuity of the constant-rank kernel bundle. The distinct-stratum case contradicts Thom's tangent-kernel inclusion. This covers arbitrary finite compatible target refinements and does not assume that the central fibre was a union of strata in advance.

For the R³-base, S²-fibre version, the central tangent vector has height derivative 1−x1²>0. The definable curve of kernel subspaces has a Grassmannian limit over every real closed field: orthogonal projection matrices have definable bounded entries, their limits remain idempotent symmetric matrices, and their trace retains the same integer rank. No ordinary sequential compactness is used.

Root rerun: 12 exact algebra checks PASS in **0.09250224501010962 seconds**. Output: `logs/root_product_without_thom.json`. The agent's initial and extended timings remain distinct. The checker verifies finite algebraic identities and tangent-vector calculations; it does not enumerate stratifications. The proof handles the quantifier over every stratification.

We reopened Giménez Conejero–Lê–Nuño-Ballesteros, *Thom condition and monodromy*, original full publisher text, <https://link.springer.com/article/10.1007/s13398-022-01353-y>, for the definition conventions (root turn642999607view0). We do not claim a historical novelty result.

This closes a proposed method, not the original A.5 question. The maximal bundle locus of the constructed map is the entire base, which is definable. We explicitly do not credit this as original-row or main-gate movement.
