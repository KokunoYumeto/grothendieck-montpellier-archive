# Author full-text match and isolated syntax check: F57 refinements

Date: 2026-11-21 UTC. Checker/author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not separately exposed.

## Exact complete targets read

- agent_pure_point_complex_trace.md: SHA256 5b408530f1d991b384d1ceb925a8e47d2c1029dffaad6f0143f919e6ac39fc13.
- finding_F57_pure_complex.tex: SHA256 fb184f00be88fbfdf5cd0ce59c52a24f526c5fe44f2f9e9719d202ba52e5b63a.
- agent_named_generator_positivity_gate.md: SHA256 309e3c80f4d78a14fc38fe74ac44881dc5e6cf27d60afe118b63f724cb853007.
- finding_F57_F58_source_gate.tex: SHA256 72e7b1717c8c3933d175753d08e5863ebb5d0af218c19d0f9378258f28701886.

The author directly reread both complete generated TeX fragments from disk and compared every theorem/proof/scope paragraph against the corresponding report. PASS. This is an author check, not an independent mathematical review. The pure-point report and final fragment separately have the groth agent's full independent PASS in agent_F57_pure_point_review.md; the named-generator source gate was sent to the theta agent and its independent review was pending when this record was written.

The pure-point fragment preserves the chosen positive square root, finite coefficient field, shift i=e-w, hidden-cancellation argument, arithmetic versus geometric half-Tate distinction, torus compact-cohomology degrees/twists, state-potential tensor proof, proper finite-type hypothesis, and inserted-trace exception. The v-v^-1 factor corollary is included with its explicit variable-to-weight condition.

The source-gate fragment preserves the exact signed Conjecture 3.4, published Figure 2 coefficient, distinction between Schur and right algebra sides, extra effective-generator membership premise, coordinate-cell condition, actual N# versus two-row scopes, signed positive-Laurent rescaling proof, and regular-specialization limitation. No proof of the complete source multiplication table is claimed.

## Isolated syntax check

Created the owned wrapper tex_check/gct_F57_refinements.tex from the already available paper preamble and the two fragments. The first invocation using the default TeX search environment stopped because article.cls was not found. The known existing check environment was then used: TEXMF=/usr/share/texlive/texmf-dist, the existing tex_check/pdflatex.fmt, and pdflatex with -interaction=nonstopmode -halt-on-error.

That invocation exited 0 and produced tex_check/gct_F57_refinements.pdf (five pages). There was no undefined control sequence or fatal TeX error. The isolated first pass predictably has unresolved external equation references/citations and first-pass internal-reference warnings; it does not contain the main bibliography. The default font-map warning is followed by explicit working map files and Type 1 fonts in the generated PDF.

This is a syntax/compilation check only. It does not claim final-paper reference resolution, full-paper layout QA, or proof-assistant verification. No master paper or master check/status artifact was edited.

## Final citation-only delta

At the parent's request, the pure report and fragment received exact Milne operation citations, with no mathematical change: Proposition 18.4(b), pp. 121–122; Theorem 22.1 and Remark 22.3(b), pp. 135–136; Theorem 24.1(a),(b), p. 144. The author read each complete primary context locally and directly checked the changed paragraphs. The final report is 84165e6ae2f50acac81f14c5e170634abb1b174c789d9e036a6c4057c67e93a9 and the final fragment is f325c80aeb83cf64fdcb83da05e559d257481b816e39db7041d4af1044c20155. The earlier whole-proof and compilation checks remain anchored to their historical hashes; this record adds only a citation-delta match to the final files.

## Final source-gate review deltas

The theta agent's complete source/report/fragment review found the mathematics and source implications correct and requested two cleanups: ordinary Markdown math delimiters in the report, and a precise statement that general basis mixing must be checked against the designated coordinate-submodule premise, with F58 still applicable if that premise is preserved. Those were applied. The independently agreed signed-class nonclosure example was also added with its full two-line proof and the explicit qualification that the F57 word trace is not an individual canonical constant covered by VIII Conjecture 3.4. The author reread these complete changed passages and checked the proof. Final source report d1357bcb46a6836ec2c83bc8bf3bf2e11cc728cf849a80fe00e98433e3f85a4d; final fragment f4ded9c74a63a1eda1dd0e20cc4011588d93bbd540ee890139afecbf5a3482cc. The original isolated compile predates these text deltas and is not silently relabeled as a final-hash compile.
