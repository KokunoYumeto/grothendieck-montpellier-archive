# Additional Part A audit: finite gate closed

AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, 19 November 2026. No priority claim.

Canonical proof: `parts/supports/supports_transfer.tex`, statements SA21-A26, SA21-A27a, SA21-A27 and SA21-A28. Separate metadata: `supports_results.csv` and `supports_CHECK_EVENTS.tsv` in this folder. The original working copy `supports_transfer.tex` in this folder is superseded by that canonical fragment.

The split-poset transfer is proved for arbitrary ordered sets. For finite L, the exact class with orthomodular Sigma_M(L) is the class of conditional lattices: every bounded-above pair has a least upper bound and every bounded-below pair has a greatest lower bound. The proof covers disconnected and unbounded posets. It closes the parent's finite gate without extrapolating the earlier census.

Sufficiency uses the finite bounded chain-type theorem only after adjoining two new endpoints to the split conditional lattice. A closed subset in the original quotient space is the trace of its closure in the larger space. Each resulting interval trace is a bounded interval, a lower ray, an upper ray or the whole quotient space. Maximal orthogonal families have the same polar as those blocks, with minimal or maximal endpoints handling the rays. Necessity constructs a nonprincipal MacNeille cut from any missing bounded join, a maximal interval basis in its closed quotient set, and an explicit separating quotient. Missing meets are dual.

The opened source is Jenča's original arXiv:2206.08113v1 LaTeX and PDF. Exact dependencies are Theorem4.10(a implies b), p10, and Theorem3.3, p5. Corollary4.5, p8, incorrectly drops boundedness: two disjoint two-element chains refute it. We check that finite counterexample and give a direct proof of the corrected bounded formula. The finite theorem is not claimed for arbitrary infinite posets.

The program `code/check_conditional_lattices.py` tests every naturally labelled order through n=6, using the root's `supports_core.py` for polar computation. Counts are total / conditional-and-OM / nonconditional-and-nonOM: n0:1/1/0; n1:1/1/0; n2:2/2/0; n3:7/7/0; n4:40/39/1; n5:357/320/37; n6:4824/3637/1187. There are no mismatches. All1225 nonconditional cases have the cut, mutual polars, maximal basis and non-spanning separator checked. Every isomorphism type occurs; counts are not the full counts of all labelled orders.

The split transfer is separately checked on all51 naturally labelled orders through n4, including every quotient pair, every closed set and orthocomplement. The connected unbounded six-crown and triangle face poset each have26 supports and are orthomodular. Complete runtime:4.230855seconds. Output: `code/conditional_lattices_output.jsonl`; its final result is also isolated in `code/conditional_lattices_summary.json`.
