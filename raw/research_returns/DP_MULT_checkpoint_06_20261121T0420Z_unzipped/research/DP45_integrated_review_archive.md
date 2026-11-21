# DP45: integrated proof preservation check

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Event **ABA-CE46**. Full integrated fragment read at **02:40:24 UTC**; closing version check **02:40:45 UTC**. No main-paper edits.

**PASS.** I read the entire integrated proposition, full proof and following scope paragraph, and compared their mathematical content with my complete DP45 memo and author check ABA-CE42. This is an author-side preservation check, not the separate independent review already supplied by `/root/formal_bound` and root.

- Entire integrated fragment SHA-256: `2c84dc722e5c45ae37c79f51b30ca6e0fc4dbe6ee545ad48972076e89f7597b0`.
- Complete proposition and proof SHA-256: `7101975d1a26036d670d979bcb12fd8bf5c9f10052643f894da22b607459b979`.
- Frozen copy: `late_proof_snapshots/DP45_integrated_complete_checked.tex`.
- Metadata: `late_proof_snapshots/DP41_DP43_DP45_integrated_check_metadata.json`.
- Exact entire fragment occurrences in the current main paper: **one**.

The integrated proof retains connectedness before applying displays, using the unital degree-six field action on any nonzero étale quotient and the dimension contradiction. It retains the actual Witt idempotents over every `R/p^n`, locality and free summands, semilinear Frobenius cycling, the nonzero Witt localization after inverting `p`, and equal ranks summing to six. The exact equivariant Hodge sequence gives each component of `Q` as either `IP` or `P`; the monomial invertible normal map then supplies units. Compatible generator choices over all levels preserve an integral primitive tangent basis rather than merely an isogeny normal form.

Both mod-seven Frobenius orderings and their initial selected block are correct. The dual action is explicitly precomposition and retains eigenvalues, while the dual Hodge type is complementary. The exact numerator sums, simplified slopes, strict mean deficit and last-direction excess agree with the memo. The added statement of **optimal affine loss three** follows directly from the newly checked DP43 with `h=6`, `m=3`; its hypotheses have all been established here.

The Tate references retain the correct distinction between §1.4 p.160 and the connected–étale sequence (4) on p.164. The external Zink/FGA inputs are preserved with their existing precise source context. The proposition removes the conditional integral rank-one-display hypothesis for this concrete Jacobian; its closing paragraph correctly leaves the global theta-cost interface unresolved.
