# Independent whole audit of D-HES-F

**Result: PASS, with the character-table provenance stated exactly.** This finite theorem is independent of the unresolved Gluck–Magaard 1998 source premise in the separate all-rank draft.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed.
- Run: HODGE_DIVISION; 2026-11-21, approximately 18:41–18:45 UTC.
- Whole proof: `agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex`.
- Reviewed SHA-256: `d78c8d11ff04e161193ee6b4f513fe590073a7d19120a5954a7e2fb8322db3fe`.
- Final citation-only revision: `2df001a02737dda0ff6bbec37bc1e61fd8754bb74128ed1473dc35aa48caa870`; the added citations and bibliography were checked at 18:46 UTC. No mathematical or input change occurred.
- Complete input: `sp2n2_character_inputs.json`, SHA-256 `5d3539d84b4988ac34c2703cbc81369b2840e50e3d74ea3afbb2db31f974e615`.

## Whole mathematical proof

The proof correctly applies the complete character bound to every nonidentity core operator. The triangle inequality gives maximum eigenspace multiplicity at most `(a+|trace|)/2`, hence projective moving rank at least a/5. This inequality is invariant under arbitrary scalar rescaling.

The groups in the statement are centerless simple groups with trivial outer group and trivial Schur multiplier. Thus an operator preserving a factor is, up to scalar, its core operator. For a product of different groups, only isomorphic simple factors can be permuted. On each permutation cycle the coordinate-change argument concentrates the twists on one factor; diagonalizing their product yields a weighted cyclic permutation of basis words. There are a constant words, and every other word orbit has length at least two. Each weighted cycle contributes at most one vector to a chosen eigenspace. This proves the quarter-support bound without assumptions on scalar phases or eigenvalue collisions. Tensor convolution preserves the a/5 support fraction. Trivial factor representations are excluded by the faithful image hypothesis.

Every factor character is real. The resulting unique invariant bilinear-form line on the full irreducible core representation is preserved by the entire normalizer. If its multiplier were trivial, every inducing-group trace would be real, contradicting inclusion of the original imaginary quadratic character field in the inducing character field. Equality of these fields is never assumed. Since a genus-zero generating tuple has product one, at least two inertias have nontrivial multiplier. Their fixed spaces are totally isotropic and have dimension at most e/2 for either a symmetric or an alternating form.

The actual intermediate-cover variation factorization, not a bare Hurwitz dimension count, rules out intermediate genus at least one for rank-nine image. In genus zero it requires at least twelve genuine branch points and total moving rank 2e+6. Two nontrivial multiplier entries cost at least e and the other ten cost at least 2e. Thus e≤6, contrary to every factor degree being at least35. This checks the full stated scalar, outer, mixed-type, factor-permutation and larger-inducing-field scope. No determinant, primitivity or tensor-indecomposability assumption was inserted.

## Independent arithmetic reconstruction

The independent driver `audit_higher_even_symplectic_finite.py` uses only the complete original input and this reviewer's prior cyclotomic polynomial reducer. It imports neither the author's verifier nor the author's output. Actual execution completed in **0.585070 seconds**, PASS:

| Core | All rows | Nonidentity entries of nontrivial rows | Minimum degree | Exact maximum ratio |
|---|---:|---:|---:|---:|
| Sp8(2) | 81 | 6,400 | 35 | 3/5 |
| Sp10(2) | 198 | 38,809 | 155 | 17/31 |
| Sp12(2) | 477 | 226,576 | 651 | 11/21 |
| Total | 756 | 271,785 | | |

All row degrees, row lengths, group orders, degree-square and class-size sums, character reality, rational triangle inequalities and exact maxima were reconstructed. The three maxima are attained at involutions with respective values −21, −85, −341 in the minimum-degree rows. The output is `audit_higher_even_symplectic_finite.json`. The newly added Sp12 table was checked in full; it was not inferred from the earlier two-table computation. The author's separate GAP exporter checks full row orthogonality; this independent driver does not claim a second construction of the character tables or a second full orthogonality calculation.

## Precise source boundary and corrected failure

An initial reviewer assertion that every table had ATLAS provenance failed on Sp12(2). Its actual official CTblLib source string attributes the computation to Christoph Köhler using group-theoretic and character-theoretic methods. Sp8(2) and Sp10(2) retain ATLAS source strings. The updated independent checker verifies these three exact strings individually. This was a provenance-label failure, not a failed character inequality. The author corrected the theorem's source paragraph before the frozen review above. No separate refereed publication or reconstruction of Köhler's table is claimed.

The complete tables are official CTblLib inputs. The mathematical conclusion is unconditional on the separate GM1998 estimate, while retaining the ordinary explicit character-table input boundary. The original proof of these tables has not been reproduced by either arithmetic checker.

The official table record was freshly opened and read at https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/S12%282%29.html . It gives exactly477 classes, the order208114637736580743168000, and the Köhler provenance string above. The page is generated from CTblLib1.3.10 on6May2025; the retained local numerical package is1.3.11. These versions are not conflated. The corrected final bibliography retains the absence of a separately verified refereed construction source.

The simple-group multiplier and outer-group facts were freshly read during the preceding HES audit in Gluck–Magaard, *Absolute Fourth Moments*, author p25, and the complete exceptional multiplier list of Hiss–Husen–Magaard Chapter5 Table1, numbered p35. Their use here is unaffected by the moment hypotheses elsewhere in the first paper. The exact primary locators and previous fresh-reading event remain in `HIGHER_EVEN_SYMPLECTIC_PEER_AUDIT.md`; they are not reported as a new reading at this timestamp.

No TeX compilation is claimed. The theorem, exact source boundary, and actual finite computation have all been checked within the scopes above.
