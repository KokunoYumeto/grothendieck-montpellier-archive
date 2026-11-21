# Independent review of signed-even spectral theorem F24

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro, effort not exposed. Date:21 November2026.

Read the entire `agent_signed_even_tensor_audit.md`, SHA256 `ad289da7a5d28024fa1841339383b053b361c5dcc98e10b9d0c3332a75f8c9d5`. Independently reconstructed its argument and all countermodels. Result: PASS.

Read the whole generated `finding_F24.tex`, SHA256 `4079cab04eec46d08b39ecd648cbef0b5543a611515b2f77d2551673f09fafd1`. Its theorem, proof, finite-extension refinement and limitations match the checked argument. Mathematical result: PASS. The complex-i counterexample currently includes k=2, where the two displayed positive roots coincide; that case needs multiplicity2, or the unbounded set may start at k=6. Root has been told and intends the latter harmless refinement. No mathematical claim depends on k=2.

The top-radius coefficient lemma uses a nonnegative augmentation for even powers plus a Vandermonde proof that the formal power is nonzero; it does not rely on a false zero-divisor-free assertion. Smaller-radius tensor terms cannot cancel a top-radius root. At least one positive top coefficient survives addition of the output positive spectral sum. The fixed-k spectral-radius limit removes constants before the unbounded-k limit; the displayed error exponent is correct.

After a field extension e, the theorem bounds only the powered visible spectrum, grouped first. Retaining one top-radius class on an unbounded even-k subsequence gives the original radius bound. The q,-q counterexample disproves omission of this hypothesis. All embeddings require real transported coefficients and their own visibility condition; a lower bound requires actually visible reciprocal roots.

The complex-i counterexample is exact in every characteristic: the even-path bilinear form has a triangular invertible matrix, giving Q^(2m-1)+Q^m-Q^(m-1) zeros. For k congruent2 mod4 its weighted sign supplies the negative high-radius terms and the permitted error. Thus the real-coefficient hypothesis has genuine content in this stated theorem.

The integer-Euler application remains a theorem about visible eigenvalues only. It does not recover spectra cancelled between cohomological degrees and supplies no path-output sign automatically.
