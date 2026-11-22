# Independent complete proof review: F58 cell-specialization positivity

Reviewer: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

Reviewed complete report: agent_cell_specialization_positivity.md, SHA256 223bd6571a53270b82ae5d108b8cb4065c55a599eab32cb65cc4e5bbe3a66c37.

Verdict: **PASS.** No mathematical correction is needed. This is a fresh whole-proof and source-application review, not formal verification.

## Complete proof checks

1. A nonzero Laurent polynomial with nonnegative coefficients over an ordered subfield evaluates strictly positively at every positive real parameter. Negative exponents do not affect this. The report correctly uses finiteness of the Laurent sum and an injective coefficient-field embedding.

2. Row-coordinate invariance is exactly vanishing of all entries from the subset to its complement. The equivalence before and after positive specialization follows entry by entry. No semisimplicity hypothesis is required for this statement.

3. I independently reconstructed the equality between the source's all-algebra preorder and generator-graph reachability. A nonzero coefficient of a linear combination of words gives some word with nonzero coefficient; a nonzero word coefficient gives some nonzero path product. In the other direction each generator edge is a source preorder relation. Possible cancellation does not invalidate either implication. The argument is valid even without coefficient positivity; positivity is used to preserve the support graph under specialization.

4. The passage to a cellular subquotient uses exactly two coordinate invariant subsets, so the induced matrices are the indicated principal row-and-column block and still have nonnegative Laurent coefficients. Both the coordinate submodules and their quotient are free, so specialization commutes with this construction.

5. The generic-simple corollary uses only a proper coordinate invariant subset, not an arbitrary specialized decomposition. The stronger cell-partition statement follows directly from the unchanged strongly connected components, even when generic algebraic simplicity is absent.

6. I checked the actual Figure 21 application independently from the complete supplied source and primary PDF contexts. The unique top-to-bottom edge is \(v_{13}\to v_2\) for \(Q_2\), with coefficient \(D-4\). The top and bottom triples are each strongly connected, and only that connecting direction disappears at \(v=1\). The right generators \(P_i=DI-Q_i\) have the same off-diagonal support. At specialization \(s_i=P_i/2-I\), so the generated image agrees with the symmetric-group image.

7. The universal Conjecture 19.1(ii)–(iii) formulation is sound. Its generic six-dimensional cell has the induced subset basis of a cellular subquotient. Strict Laurent positivity on the tensor basis passes to that cell. Clause (iii) requires two distinct specialized cells within it, whereas the support theorem leaves its cell partition unchanged. This is a contradiction to the added positivity requirement, not to the source conjecture as stated.

8. The illustrative two-dimensional family is correct. The only invariant row lines for the all-ones matrix are its eigenlines \((1,1)\) and \((1,-1)\). The displayed second matrix preserves neither over the generic field, even after algebraic closure, but coincides with the first at \(v=1\). The specialized eigenspaces are non-coordinate and the support graph remains connected. This proves that ordinary reducibility at specialization alone is insufficient for the proposed obstruction.

## Source check

The complete definition in IV §2.4, pp.18–19, equation (17), explicitly defines a cellular submodule as one spanned by a subset of the designated basis and defines the cellular quotient basis by a set difference. The source's right-action convention was read.

Conjecture 19.1(ii)–(iii), pp.130–131, and Example 19.3, pp.133–135, were read in full relevant context. The statement on p.134 explicitly identifies the top row of Figure 21 as a specialized cellular submodule and the bottom row as the quotient; the review does not infer the coordinate condition merely from the word quasi-cell.

The generic simplicity is the cited Theorem 13.4, pp.74–75. I did not reprove its full classification. An optional independent exact character calculation gives the top and quotient class values \((3,-1,-1,0,1)\) and \((3,1,-1,0,-1)\), agreeing with the source's \((2,1,1)\) and \((3,1)\) labels. The obstruction itself does not depend on this additional computation.

The separate source/concrete audit is agent_rank4_cell_source_audit.md, SHA256 ff97552abb8444b2cc0c902fcea7c782e554e5717302190b17dacf95987a14c0.

## Exact scope and a harmless presentation refinement

The argument permits a basis over the regular local ring at \(v=1\), provided the named matrices lie in the stated nonnegative Laurent ring and the basis remains a basis at specialization. Its Laurent span then gives an abstract stable free lattice with the same generic representation and the same labeled special basis. There is no need to assert equality with the source's original global lattice.

The report correctly leaves arbitrary positive bases without the designated cell/quasi-cell structure open. It also leaves pointwise nonnegative rational or Laurent functions outside its hypothesis: \((v-v^{-1})^2\) is the precise example. Nothing here excludes a virtual character, a derived Euler trace, or a pure coefficient sheaf whose nonproper cohomological pushforward is mixed.

The generated final fragment has not yet been reviewed in this record. A later whole-fragment match must be recorded with its own exact hash.

## Complete generated-fragment match

I subsequently read the complete finding_F58.tex directly, SHA256
b099ca23f05312a58498b00ab68ff3d49548837b4db3a52fdeafd2ad39a6c870.
Whole-fragment verdict: **PASS**.

Every proof, the universal tensor-basis strengthening, the two-dimensional
counterexample, and the separate dictionary match the reviewed report.
The only substantive presentation addition is the explicit regular-local
basis paragraph already checked above: its Laurent span is an abstract
stable free lattice, with no unsupported identification with the original
global integral form. This addition is correct.

The final fragment continues to distinguish coefficientwise positive
Laurent entries from functions nonnegative on the positive real axis,
and the source's cellular comparison from an arbitrary positive basis.
No mathematical correction is requested.
