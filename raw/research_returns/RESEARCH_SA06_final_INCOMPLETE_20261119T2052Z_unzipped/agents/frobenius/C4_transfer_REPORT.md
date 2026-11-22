# C.4aa: countermodel to unrestricted graph transfer

**Status: proved method limitation; no main-gate movement.** The full proof is in `C4_transfer_countermodel.tex`. Root independently passed the proof, source application, and complete twelve-case certificate before the 11:32:15 UTC tool-clock reading on 19 November 2026.

The three primitive covectors are `(1,0)`, `(0,1)`, and `(2,1)`. Their squared forms admit no common orthogonal graph summand over the localization at 2 at any positive integral level. The proof reduces all levels by the coordinate homotopy from C.4z and then uses the function `t²` on the quotient `Z/4`: closure forces zero, whereas the third profile contributes twice an odd unit.

EGFS's current Mumford survey, Proposition 2.29 and Corollary 2.30, realizes these exact arbitrary integral positive-semidefinite monodromies in an algebraic family of principally polarized abelian surfaces. The theta divisor is already an effective integral minimal curve class on every geometric fibre. Hence algebraicity alone cannot imply that common graph splitting for an arbitrary monodromy cone. Pairwise disjoint monodromy images do not fix the transfer: this countermodel also has that property.

The exact primary URL is <https://arxiv.org/html/2507.15695v2>. We opened and read Proposition 2.29, Corollary 2.30, and the full converse Proposition 5.3. The header/manuscript date discrepancy is retained in `C4_transfer_references.bib`.

Code: `code/check_graph_transfer_countermodel.py`. Output: `output/check_graph_transfer_countermodel.json`, started 11:19:49.980558 UTC, elapsed 0.000579633 seconds. All twelve terminal cases pass. The finite computation does not substitute for the written proof at arbitrary levels.

The original residual splitting problem for nonprincipally polarized abelian surfaces is unchanged. The correlated rank-two cone could require special geometry beyond an unrestricted graph-transfer principle; no such transfer is claimed here.
