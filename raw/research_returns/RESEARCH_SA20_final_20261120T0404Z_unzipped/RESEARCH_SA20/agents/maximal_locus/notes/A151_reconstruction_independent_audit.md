# A151 reconstructed authored-text and exact-code audit

Auditor: `/root/maximal_locus2`, GPT-6 Astra, OpenAI.
Date:20November2026.
Source: `agents/singularities_duality/part_angular_tent_counterexample.tex`.
Final source SHA256: `119337c2561171d0958f8bebce88cc7c390657dce56666632b3936e18e109e1a`.
Code: `agents/singularities_duality/code/check_A151_exact.js`.
Code SHA256: `7e944f4b8f5de4eec6195bbef83e9f07185c19aee6bc3fa58b67fa981dbdb4e8`.
Verdict: **FULL AUTHORED MATHEMATICAL PASS; independent exact-code rerun 26/26 PASS.**

I read all 334 lines /12,888 characters of the initially reconstructed TeX and the complete54-line code, then reread the two corrected/additional passages in the final source. The reconstruction contains the complete original mathematical argument and the positive radial-collapse addendum.

The only requested wording correction was the antecedent after alpha=theta composed with h: it is h(boundary Q_rho), not alpha(boundary Q_rho), that avoids the parameter origin and outer boundary. This is corrected in the final source. The positive fact that the radial homotopy g_t remains homeomorphic for every t<1 has also been restored, with the strictly increasing radial-function proof.

Checked details include the amplitude identity and bound; exact four affine shear pieces and inverse; slopes7/8 through9/8; dimension-independent Euclidean forward and inverse constants; exact supremum-distance formula; the distinct graph-Hausdorff comparison; local angular lower bound; preservation of interior points by any parameter homeomorphism; positive amplitude on a fixed compact loop; finite subdivision and telescoping on the original loop; last-ray-exit surjectivity; exact factorization's graph-Hausdorff necessity; the relative nullhomotopy; the general radius-r0 collapse and its uniform bound; and the square-circle/round-circle semialgebraic bi-Lipschitz conjugacy.

The final positive construction has K0=(1-r0)^(-1)+2/r0, hence forward bound epsilon*K0=3/2 at r0=1/2. It preserves the based and spatial conditions. Its intermediate parameter maps are homeomorphisms for t<1, but the final map is not; this does not contradict the negative exact-reparameterization result.

I executed the actual recovered Node program into an owned output file:
`agents/maximal_locus/notes/A151_exact_independent_rerun.json`.
Observed result:26 checks, all_pass=true, elapsed0.001496613 seconds.
The arithmetic certificate uses exact normalized BigInt rational operations and symbolic univariate polynomial comparisons. Its output correctly limits its scope to finite algebra. The compactness, boundary-invariance, closest-graph-point, finite-subdivision and last-ray arguments are supplied by the written proof, not inferred from the tests.

No nonzero concordance class or obstruction to homotopy regularization is asserted. The theorem is a method obstruction for the given representative and has its explicit nullhomotopy and noninjective regularization.
