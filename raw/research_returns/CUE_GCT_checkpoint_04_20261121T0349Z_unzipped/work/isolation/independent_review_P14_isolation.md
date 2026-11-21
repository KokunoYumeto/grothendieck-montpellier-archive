# Independent complete proof review of P-14

Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I

Actual review completion: 2026-11-21T03:26:42+00:00

Reviewed in full: work/purity/P14_rank_one_bridges.tex.

**Outcome: PASS.**

I rederived the endpoint rank-one updates and checked the telescoping normalization to identity constant factors. The nested coefficient-row spaces retain actual coefficient rows of support at most the number of dimension increases, hence at most w-1. The Lagrange selector specialization therefore detects every nonzero scalar bridge.

The pivot identity A=UV/a is exact for each rank-one layer. Clearing all pivots yields the displayed polynomial product identity. Adjacent bridges may share a reset variable, but each bridge becomes a nonzero polynomial under the same generator; their product remains nonzero in the parameter domain. No variable-disjointness of different scalar bridges is assumed. All pivot denominators have nonzero zero-amplitude specialization.

The scalar theorem implies coefficient-row equality by constant linear annihilators, with scalar extension when required. The t, selector and total-amplitude degree bounds give the stated Newton-simplex sampling count in every characteristic; w=1, n=1, and D=0 are covered.

For the rational version, the exact Lagrange identity after c_i=1/A'(a_i) scaling yields t+sum b_j/(y_j-a_i). The change b_j=z_j A(y_j) is dominant on a nonempty open set. Generic degree-K denominators are separable over an algebraic closure in every characteristic, and partial fractions give the converse image-closure inclusion. Clearing a common nonzero denominator preserves all constant linear annihilators. Thus the rational coefficient-span assertion follows.

The width-two conclusion and the K=0 unipotent counterexample check. The generic factor-rank promise implies the stated interval profile for nonzero scalar output. I did not independently reopen the newly cited AGKS2015 author version, so this event certifies only my complete mathematical reading/rederivation of P14, not an additional source audit. No numerical or machine-formal certificate is claimed.
