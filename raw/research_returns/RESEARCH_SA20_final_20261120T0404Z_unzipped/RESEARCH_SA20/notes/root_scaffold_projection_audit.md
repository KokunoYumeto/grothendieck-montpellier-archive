# Root audit of the finite-scaffold scope note

We read the complete final note
`agents/maximal_locus/notes/scaffold_format_gate_0340.tex`, including the
explicit inverse added after our first review, and the complete checker
`agents/maximal_locus/code/check_scaffold_projection_loss.py`.

The final note's SHA256 is
`2cc1e602cf1c9f5086dc3597f1790a58de62301ba607de0469ee5f8cfa1b1aa0`.
Our independent execution at 2026-11-20T03:49:25.588048+00:00 passed
21 of 21 exact rational/symbolic checks in 0.23258528400037903 seconds.
The actual output is `logs/check_scaffold_projection_loss_root.json`;
the author's separate original output remains preserved.

## Mathematical review

The finite marked-pair pool argument uses a finite valid Hardt and
triangulation system whose additional coefficients are existentially
quantified. Its transfer across models is therefore a sentence of the
fixed complete theory, not an assumption that an arbitrary coefficient
tuple belongs to every model. The finite polyhedral-pair labels are
field-independent by the previously audited relative definable
Hauptvermutung and finite ordered-field certificates.

The diagnostic square homeomorphism has positive vertical slopes,
matching formulas at the diagonal, and the displayed explicit inverse.
The side estimates give the uniform bounds
`|h_x(y)-y| <= x` near the left side and
`|h_x(y)-y| <= 1-x` near the right side. Substitution through the inverse
gives the same bounds for inverse displacement. These are order-field
epsilon-delta proofs of joint continuity, so ordinary topological
compactness over a non-Archimedean field is not used. The earlier
compact-square shortcut has been removed.

The diagonal is a bisection of both coordinate projections. The folded
graph is not: the first projection already forces the candidate map,
and its second projection has three distinct preimages of one half.
The ambient homeomorphism preserves the first projection and all four
sides, which makes the loss of the second projection explicit.

We checked the finite identities and ranges by executing the code.
Continuity, the all-model transfer, and the absence of a bisection use
the mathematical arguments above rather than finite testing.

## Scope

We accept the note as an unnumbered method and scope record. It does not
prove that relations of the special metric form in SF.4 realize this
diagnostic graph. It does not refute definability of the controlled
homeomorphism relation. It does not prove or refute the finite angular
certificate pool in A5.019. No original row changes and no named main
gate is proved strictly smaller; no qualifying movement is recorded.
