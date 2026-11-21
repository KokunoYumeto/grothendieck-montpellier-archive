# F61 author proof and fragment check

Author/checker: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

This is an author check, not an independent review and not formal verification.

## Frozen targets

- Full report: agent_pure_rank3_kernel_lift.md
- Report SHA256: e512ccd4d2734771f3828a8e24753700b8765b5d3d3fc00027b4cb44173910df
- Complete fragment: finding_F61.tex
- Fragment SHA256: 57df6090bff3c62dd51793b7b4a889f660e4395e203933e233ecd837aedde5d7

## Mathematical author check

The report was reconstructed from the explicit full-Tate and half-step formulas. I checked the cohomological degree and BBD weight in each summand, the Euler parity, the fixed positive square-root convention, the continuous-unit qualification, the convolution tensorator, and the pure-tensor associator/unit/symmetry diagrams.

I checked the exact 64-state potentials against the actual matrices, including both off-diagonal N(delta) entries. I reread all quadratic ordered-overlap and degree-five maps in F56 and checked that every intermediate coefficient object used in those maps is even. I retained the half-step restriction to even grading shifts and the exclusion of an isolated odd central coefficient.

I read the complete F53 tensor and Gaussian transport, symmetry correction, weights and unit context before deriving the split-complex extension. I checked its tensor comparison on each shifted homogeneous summand and its weight calculation. The image statement is derived, not perverse-degree-zero for multidegree objects.

I then read the entire generated fragment directly in two consecutive file ranges, including the statement, all proofs, examples, scope and separate Grothendieck paragraph. It matches the report's mathematical content; no new assertion was added in the fragment. The full-Tate extension of the F57 mixed-sign obstruction follows by the same even-weight parity proof and is explicitly scoped to that pure-word comparison.

## Syntax check actually performed

The isolated wrapper tex_check/gct_F61.tex uses the established paper-style preamble and inputs only the complete fragment. I ran:

    env TEXMF=/usr/share/texlive/texmf-dist pdflatex -fmt=pdflatex.fmt -interaction=nonstopmode -halt-on-error gct_F61.tex

from GCT_NSRH_work/tex_check. It exited with code 0 and generated gct_F61.pdf, five pages. The log contains expected missing standalone bibliography and cross-reference warnings on this first isolated pass; there was no hard TeX error. This is a syntax compile, not a visual layout review or validation of the master paper's cross-references.

## Independent review

Requested from /root/grothendieck_dictionary on the frozen report; the complete fragment was supplied for a subsequent direct match. No independent verdict is invented in this author record.

## Final bar and coefficient-field delta

At the parent's request, the final report is now SHA256 f48551682261cf37efe0160e23fffd103245d013a079a1b1778d8694efd5816a, and the complete fragment is SHA256 765a660843a8954a309b63291976b29fe96e80a99c0471ad44f0f5c1c63cc9f1.

The delta makes E explicitly a finite ell-adic coefficient field with trivial-Frobenius multiplicity spaces and adds the full formal-bar proof. I reread the complete F56 formal-bar supplement, then directly checked the new report and fragment sections: full-Tate duality, the half-step [2(t_b-t_a)] correction, order-preserving tensorator and naturality, both double-dual coherence identities, entry-weight preservation, shifted-context inverse-map scope, and the distinction from transpose adjoints and Gaussian Verdier duality. The rest of the previously whole-read fragment is unchanged apart from the statement and scope sentences announcing this proved addition.

I reran the same isolated syntax compile on the final fragment. Exit code 0; five-page PDF; expected unresolved external references and bibliography only. This second compile resolves the concrete risk introduced by the new TeX formulas; it is not a new visual or independent mathematical verification.

The final hashes were sent to the independent reviewer, whose verdict remains separately recorded.
