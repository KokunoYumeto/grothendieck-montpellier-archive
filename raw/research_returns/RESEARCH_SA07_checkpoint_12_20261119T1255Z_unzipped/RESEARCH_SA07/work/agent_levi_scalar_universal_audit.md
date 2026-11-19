# Universal audit of the Levi scalar evaluator

19 November 2026. Independently audited `work/calc_levi_scalar_rows.py` without modifying it or duplicating the separate numerical certificate. This audit proves its decorated cup/cap evaluation and composition formulas for every admissible complementary genus s. It does not assert completeness of the selected mixed rows or the all-genus kernel inclusion.

## S1. Exact encoded tensors

Use V=<a,b> direct-sum W, with symplectic basis a,b,x_1,y_1,...,x_s,y_s, and <a,b>=<x_h,y_h>=1. Integer vectors 0,1 encode a,b and 2h,2h+1 encode x_h,y_h. The routine `pair(x,y)` is exactly this alternating form. A negative key entry -j-1 is the fixed vector j. A nonnegative label occurs twice; in increasing slot order it encodes the oriented cup

    Omega_W = sum_(h=1)^s (x_h tensor y_h - y_h tensor x_h).

Different labels mean independent copies of this sum. Permuting a cup reverses its sign precisely when the order of its two slots is reversed; the input generator records that sign in `permute`. A cap (i,j) means applying <slot_i,slot_j>. `canonical_caps` sorts each cap and inserts its exact alternating sign, then sorts the product of scalar factors. Its operation changes no contraction.

`scalar_diagram` requires the caps to be a perfect matching of all tensor slots. Thus every cup slot belongs to one cup and one cap; every fixed-vector slot belongs only to one cap. The graph whose edges are these cups and caps is therefore a disjoint union of alternating cycles and paths. Every path has exactly two fixed-vector endpoints, including the path consisting of a single cap between two constants.

## S2. Paths, loops, and the exact genus polynomial

Expand each cup independently by choosing a handle h and one of its two orientations. A cap between nonzero basis vectors can be nonzero only when both vectors belong to the same symplectic handle and are the opposite basis vectors. Hence the handle index propagates along the entire graph component.

For a path containing cups, its two fixed endpoints force its handle. A distinguished endpoint a or b forces zero because the cup is confined to W. Two W endpoints in distinct handles also force zero. For endpoints in the same W handle, there is at most one compatible orientation assignment; the routine leaves the possible zero from identical endpoint basis vectors, and every orientation sign, to the exact product of `pair`. This is why it retains the actual endpoint handle rather than collapsing all fixed vectors to one handle.

For a component with no fixed endpoints, every slot lies on an alternating cycle. All its cups must have the same handle, and there are exactly s choices. After that handle is fixed there are two compatible orientation assignments. If the component has r cups and r caps, reversing every orientation changes the cup coefficients by (-1)^r and the cap products by (-1)^r. The two contributions therefore have the same sign, giving +2 or -2. The routine computes this sign by assigning any one handle, here handle 1, to the loop and summing its orientations.

Different components have independent handle choices. Equal handle values on distinct components are permitted, so the count is s^number_of_loops, not a falling factorial. Assigning handle 1 to all loops during the one-handle sign calculation is valid because no cap joins distinct components. Paths may also use handle 1 without affecting this independence.

It follows term by term that

    actual contraction in W of genus s = coefficient * s^loops,

where `(coefficient,loops)` is the returned pair. The coefficient already includes each loop's factor +2 or -2. A direct constant-to-constant cap is evaluated by `pair` without introducing a genus factor. This proves the formula for every s at which all named endpoint vectors exist; it uses neither interpolation nor a stable-range independence assertion.

The stored inputs have at most four cups, so there are at most four loops. The length-five coefficient array in `evaluate` is therefore sufficient. Summing the exact contributions proves its polynomial output. The five-detector matrix uses the same formula with eight slots and four caps, so its entries are exact genus polynomials as well.

For rows asserted at every s>=3, fixed endpoint test vectors must belong to the first three W handles. The current tests use at most the first two. A test involving x_4 or y_4 would require s>=4 unless it is replaced by an explicitly summed invariant test. This scope condition was sent to the implementer.

## S3. The literal two derivation compositions

For any derivation D of the ordinary completed free Lie algebra, put

    T_D = sum_i (x_i tensor D(y_i) - y_i tensor D(x_i)).

Contracting the first slot of T_D with an input z by <first,z> returns D(z). Let delta correspond to x wedge y wedge z with convention

    delta(t)=<t,x>[y,z]+<t,y>[z,x]+<t,z>[x,y].

Then T_delta is exactly minus the alternating tensor on (x,y,z). The `wedge_sign=-parity(perm)` line implements this equality, including the two terms of each bracket.

For D of degree six, T_D has one root slot 0 and tail slots 1,...,7. T_delta has root E[0] and two tail slots E[1],E[2]. In D composed with delta, D acts on each of the two delta tail letters. The old delta root is retained, the replaced letter is contracted against the D root by <0,E[j]>, and D's seven-letter tail is inserted in its place. This is the first loop in `bracket_plans`.

For delta composed with D, the D root remains 0. Delta acts on each of the seven D tail letters. Its root is contracted by <E[0],j>, and its two-letter tail is inserted. This is the second loop. The ordinary derivation bracket is D delta - delta D, so the extra minus sign in the second loop is exact. No derivative of a tensor root is taken: that root records the argument slot of the resulting operator. Both compositions produce a nine-slot tensor, one root and eight tail letters, as required for a degree-seven derivation.

The labels 8,9,10 are the three actual delta inputs, and slot 11 is the scalar test vector. The glue cap and the four subsequent output caps therefore form a perfect matching of all twelve original slots. Combining repeated cap patterns by their coefficients is an exact linear operation.

## S4. The R and cyclic ES rows

The five terms in `rterms` specify the fixed opened R functional as four oriented caps on the first eight slots of a nine-slot derivation tensor, leaving its last slot as the output vector. `plans_R` substitutes the literal bracket plans into these caps and pairs the remaining vector against slot 11. Thus it evaluates the designated scalar R([D,delta]) row. The separate literal expansion audit already verifies the source coefficients; this audit checks their symbolic all-genus substitution map.

The ES map first contracts the root slot with the first tail slot. The remaining seven tail letters are an element of the cyclic coinvariant quotient. An arbitrary chosen six-slot chord pairing and one test-vector pairing is made into a functional on that quotient by summing all seven cyclic rotations. This sum is exactly seven times the characteristic-zero cyclic average. Therefore it is well-defined on the cyclic quotient and has the same kernel as its averaged functional.

`plans_ES` performs precisely this orbit sum on `output[2:]`, after contracting `(output[0],output[1])`. Its three chord caps and final test cap exhaust the seven output positions. The delta alternation was already supplied by all six permutations in `bracket_plans`, so these are actual scalar functionals on an exterior input and a cyclic-coinvariant output. Repeated terms are summed with their correct multiplicities, including cyclic words with nontrivial stabilizer.

Every selected R or ES row is consequently a necessary equation for the actual mixed normalizer map, for every allowed s. Completeness of the selected rows is a separate linear-algebra issue and is not inferred from this proof.

## Verdict

The universal cup/cap evaluator, `canonical_caps`, literal bracket composition signs, R substitution, cyclic ES orbit sum, and five-detector evaluation pass. The proof applies symbolically in s. It supplies no uncomputed row, rank, Smith normal form, or all-genus kernel inclusion.

## S5. Final standalone identity and arithmetic implication (F.3.32)

The final self-contained 330-line program `work/check_all_genus_single_line.py` was read in full. It reconstructs every input, detector and mixed row without a stored matrix or pickle. Modular pivots only select independent rows: each rational nullspace basis is checked against every original integer equation, giving the matching upper rank bound. The Dynkin and cyclic projectors are checked exactly, with the fixed-width matrix-product bounds explicit. The pure-detector determinant is

    3538944 s^5(s-2)(s-1)^4(s+1)^3(2s-1)(2s+1)^5(2s+3),

nonzero for every integer s>=3. Together with the opened invariant-space dimension this proves the actual twelve-vector specialization.

I separately loaded the selected matrices and verified every one of the 36 defects of N M=d L K, the ranks of L and J, and L J=0. Cancelling the common polynomial factor independently gives the same literal reduced denominator d0=9(2s+3)(4s^2+6s-1) and the same 21 numerator entries as the final standalone code. The latter is nonzero over every Q_l for every integer s>=3. Thus Mv=0 implies LKv=0 without requiring completeness of the seven selected necessary rows.

I then ran the entire standalone program afresh. It exited successfully and reported internal wall time 18.531897790 seconds. Full output: `work/generation_all_genus_single_line_independent.output.txt`. Program SHA256: 7d11658b85e6ee10a86c18ea8c8758dd9bc4ee8eb2fc4b82195a07b14187f653. All 36 exact polynomial defects were zero.

The full final work proof `work/F3_32_integrated_text.tex` was independently read. I visually reopened original MSS2026 p.11 and checked the five R coefficients and the Johnson-image exact sequence. The actual stabilization maps carry their vanishing to the required genus. F.3.30's full-Sp detector implication converts ker L to the two actual geometric brackets and hence q=0; the initial Levi projector preserves actual U and q. The F.3.31 full-cover/normalizer/full-log composite is then contradicted. No projected vector is treated as an individual Galois element. Finally, the UT3(Z/l^m) maps prove the asserted cusp intersection with the common pro-prime kernel is trivial.

Final verdict: F.3.32 passes, including the stated original CM common-kernel conclusion.
