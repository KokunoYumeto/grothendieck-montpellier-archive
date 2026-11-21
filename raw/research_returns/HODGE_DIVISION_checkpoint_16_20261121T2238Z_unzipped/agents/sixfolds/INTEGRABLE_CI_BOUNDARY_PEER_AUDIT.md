# Independent whole-proof audit of the integrable CI boundary

**PASS, in its explicitly limited counterexample scope.**

Reviewer: `/root/sixfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. Actual proof/code and independent computation checks: 2026-11-21, completed 21:46:34 UTC.

I read the entire parent proof `research/ci_integrable_cross_minor_boundary.md`, SHA `fbf93493e62b5ee9517d17b43186e40461f5f5f05f38079d7c469e748edaf804`, and every line of its adjacent exact program, then the actual saved output. No author's file was edited.

## Whole mathematical check

I independently expanded both column wedges. The six coefficients are exactly the stated p and q, each is decomposable, and their mixed wedge is −4/5. The same coefficient is the determinant of the four-column matrix, so its rows are actual independent formal linear parameters.

Taking the four squared linear parameters gives a genuine zero-dimensional complete intersection. Differentiation gives the stated gradient 2 diag(ell) J. This uses actual functions; no nonintegrable matrix is being substituted. The quotient is the tensor product of four square-zero one-variable algebras, with the sixteen squarefree monomials as basis and embedding dimension four.

Every scalar cross minor vanishes for precisely the two reasons in the proof. If the pairs share an index, both terms contain a squared parameter. If they are disjoint, the coefficient ratios agree within the complementary pair, so the scalar coefficient is zero. These two cases cover every ordered pair of two-subsets, including coincident pairs.

The actual Jacobian determinant and mixed wedge have coefficient −64/5 on the nonzero top squarefree monomial. Multiplying that monomial by any parameter gives zero, so the socle assertion is direct in this explicit algebra. The passage from vanishing scalar minors to a zero Jacobian is therefore false even for an integrable complete-intersection gradient.

I also checked the generator-change boundary statement. A change of minimal regular generators transforms the bracket forms by the invertible second exterior power modulo the ideal, so vanishing of all coefficient cross minors is preserved; the mixed wedge changes by the determinant unit. If a generator triple satisfied the E836 commuting condition, the new cross minors would kill its mixed wedge term by term, contradicting that invariant nonvanishing. Thus this example does not belong to that sufficient presentation family.

None of this solves either matrix-order companion equation. It supplies neither a flat module deformation nor a weakly semiregular balanced object. The root proof explicitly says this, and I retain that limitation. The finding is a boundary/counterexample to an overstrong inference, not main-gate movement.

## Independent exact check

I wrote `audit_integrable_ci_boundary.py` without importing the parent program or any of its helpers. It uses rational `Fraction` arithmetic, an explicit 24-term determinant, squarefree bit-mask multiplication, and a separate ordinary-polynomial differentiation routine. Its actual PASS output is `audit_integrable_ci_boundary.json`.

The independent checks comprise all 36 ordered scalar cross minors, all sixteen actual-gradient entries, the two decomposable wedge squares, the mixed wedge/determinant, and the nonzero socle coefficient and its four annihilations. Actual internal elapsed time: 0.0011249119997955859 seconds. No broader computation, source theorem, module solution, or document compilation is claimed.

The algebra above prompted a separate investigation of stronger companion-matrix constraints; any later theorem from that investigation is distinct from this counterexample audit.
