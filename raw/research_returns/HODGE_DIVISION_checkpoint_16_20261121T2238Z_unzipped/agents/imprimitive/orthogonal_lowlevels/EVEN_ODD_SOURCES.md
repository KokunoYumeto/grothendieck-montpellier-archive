# D-OL16–18: exact sources and dependency boundaries

Date2026-11-21, author `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`.

## New use of previously available primary sources

**D. E. Taylor, The Geometry of the Classical Groups.** Author's complete corrected book at `https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf`, local `cache/TaylorClassicalGroups.pdf`, SHA-256 `825201a4831659f957bf30156f04e85ab3746c01d942c670284071c68b41e30e`. Published1992 book, author corrected edition headed April2021. The edition distinction is preserved; printed pagination is used.

- Theorem7.4 and its entire proof, printed pp57–59, freshly read in this derivation. It extends the ordered-pair isometries even for degenerate pair spans. The ambient space is nondegenerate, so its stated radical condition is automatically satisfied.
- Lemma10.2, Corollary10.3 and the complete following hyperbolic decomposition on pp116–117, freshly read here, together with the finite-field norm-surjectivity paragraph. These supply an isotropic E-line and opposite E-line in the Hermitian case.
- Finite-field quadratic classification pp138–140 was fully read earlier in this run and is reused with its exact finite odd-field scope. Its anisotropic dimension bound is two. No classification of complex characters is imported at this step.
- Theorems11.47–11.48 with full proofs pp161–162 were freshly read for the immediately preceding D-OL14–15 proof and its checks; the exact large-dimensional perfectness statement is reused here, including characteristic three.

Primary web opening in this derivation: `turn718939291view0`. Full theorem/proof text was read from the retained local corrected edition; the web opening reconfirmed title/version/content.

**Larsen–Shalev–Tiep, The Waring problem for finite simple groups, Annals174(2011),1885–1950.** DOI `10.4007/annals.2011.174.3.10`. Complete published PDF `https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf`, retained sibling source `agents/g34_eightfolds/bireflection/sources/LST2011_Waring_published.pdf`, SHA-256 `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`.

Theorem4.3.6, equation(4.3.2), pp1917–1918; full proof pp1918–1923; Remark4.3.7 p1923; group conventions p1907. These complete passages were read and visually checked earlier in this run for HOS16/OL10 and subsequently reused in OL12–15. The identical ordinary-inflation interface is used here: the character is an ordinary character inflated to the finite spin cover, the natural support is restricted to `mu2={1,−1}`, and no faithful-character hypothesis is required. Threshold567 equals `7·9²`. This is not a theorem about spin characters automatically descending; the ordinary boundary remains explicit.

**Li–Xia, published Memoirs, Section2.2.2 Table2.1 p14.** The full semilinear natural-normalizer coverage and represented-central-quotient argument are the already fully reviewed D-OL07 proof, with exact source scope. The present proof does not introduce a new outer-automorphism classification or omit mixed field/diagonal/graph lifts.

**Guralnick–Larsen–Tiep, Inventiones235(2024),151–210, Theorem3.7 pp165–167.** Full published degree bound and proof read in the earlier OL whole-source audit. We use only the ordinary `k=1` consequence `a≥q^(d−4)(q−1)`. No spin degree assertion is silently substituted.

## New elementary proofs, not cited as known results

- Trace reconstruction of symmetric or Hermitian E-forms for a nonsquare projective involution, with both multiplier signs.
- The explicit orthogonal two-plane radical matrices and their full Heisenberg multiplication law.
- Generation by two opposite two-plane radicals, reduced concretely to the reviewed opposite-line generation proof.
- Complete fixed-rank-two orbit count under the actual Levi Omega(W), including determinant/spinor correction and affine quadratic Gauss estimates.
- Both central-character alternatives: pair inverse characters when the center reverses; use the Weyl-basis trace when the center is fixed. All multiplicity operators remain present.
- The square-scalar skew-similitude case, including the negative sign in the dual-weight action.
- Complete projective-prime normalization and the all-order impossibility of a square root of a projective reflection in even dimension.
- Actual source generation: at most twelve projective reflections would force a common nonzero natural fixed space for the perfect Omega group.

The explicit carrier construction and full matrix-algebra classification are D-HOS01, already independently checked in this run. Only its elementary Weyl basis is reused; the fixed-space trace is rederived for the new involution, and its fixed-point-free hypothesis is not assumed.

## Exact supplementary computation and attempts

`check_orthogonal_even_odd.py` first executed PASS at22:36:05.066817UTC in0.172769615s. After status/typographic/nonempty-scope edits only, the final run passed at22:36:42.479978UTC in0.184052911s. It certifies the full symbolic 8D radical isometry and group law, both nonsquare cases overF3 on all6,561 X parameters, all81 fixed X and80 nonzero fixed dual rank-two maps in each case, and6,561 exact Weyl position/phase identities. Every rational endpoint is checked. These finite witnesses do not replace the universal arguments.

There was no mathematical or certificate assertion failure. Two preliminary `apply_patch` requests failed because their context string did not exactly match the written line; the third applied the intended clarification that an anti-isometry acts as minus itself on the polar-identified dual. These were text-patch failures, not numerical counterexamples. The pre-freeze clarification is present in the final written proof.
