# Fresh independent review: compressed KOH witnesses, F37

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 UTC. Verification type: full direct report and generated-fragment read, exact primary-definition match, and independent reconstruction of every compression/size/verification argument. No formal-kernel proof or numeric sampling was used.

Reviewed report: `agent_koh_compressed_witnesses.md`, SHA-256 `b9df165055555cc9b94e6bf7cc33ea24392f34e7c8c64632cfff579b049740c3`.

Reviewed generated fragment: `finding_F37.tex`, SHA-256 `33f01af531385aed861c32a5b20ff8b26d33378c6bb489afa3fd8db83c0beb07`.

**PASS for both exact texts. No mathematical correction required.** The input convention with explicitly listed rectangular rows is essential and is consistently retained. The result is a positive short-witness interpretation of this restricted actual coefficient, not a general ordinary Ehrhart model or a fully compact binary plethysm claim.

## 1. Full primary-definition match

I read the local v3 PPS primary text at the complete Definition 3.2, Remark 3.3, Proposition 3.4, Lemma 4.2 and its proof, Definition 4.4, Theorem 4.5 and its proof, and the surrounding fixed-order conventions. I also read §2.2's numerical-algorithm context. The report's page locators and version distinction are consistent with this text.

The source uses one child for each distinct part `j`, in increasing part order. Its column sum `mu'_1+...+mu'_j` equals the report's row sum `sum_s min(j,mu_s)`. Leaves have exactly `b=1`, and nonleaves have `b>=2`. The root and leaf-mark formulas, including the shift by half of `sigma`, agree exactly. The source fixes a depth-first leaf order; unary contraction preserves it. The v3 induction in Lemma 4.2 uses the corrected `k_(t−1)` subscript. The source counting theorem is treated as established literature, not as a new theorem of this investigation.

## 2. Repeat classification and exact inverse

For a partition of `b`, the sum of child `b`-parameters is its number of parts. This equals `b` only for `(1^b)`. In that case there is one child and direct substitution yields `a'=a−2(b−1)`, `b'=b`. Every other internal node has a positive total mass loss of at least one. This classifies every possible long mass-preserving chain; no other unary shape was omitted.

A run of length `h` reduces `a` by exactly `2h(b−1)`. Since `b>=2`, the intermediate values decrease monotonically, so checking the endpoint suffices. Recording the run immediately before a surviving nonrepeat vertex produces a unique placement, including above the skeleton root. A leaf cannot have a preceding nonempty run because such a run preserves a `b` value at least two. The explicit zero-count requirement at leaves therefore both matches the source and prevents redundant encodings.

The inverse procedure reconstructs every label from the initial type, the run lengths and the surviving partitions. The nonrepeat requirement makes every reconstructed run maximal. The source's fixed child order removes permutation ambiguity, even if two children happen to have equal numerical types. Ordered subtrees remain ordered. Thus the two procedures are mutually inverse on actual marked trees, not just on their leaf multisets.

## 3. Skeleton and arithmetic bounds

Telescoping the positive mass losses gives `sum losses=k−t`, because the root mass is `k`, each leaf mass is one, and every nonroot internal contribution cancels once. Thus the number of surviving internal vertices is at most `k−t`, and total surviving vertices at most `k`. This includes the `k=1` case, whose skeleton is one leaf with repeat count zero.

I independently checked the energy identity. For decreasing rows, the diagonal pairs contribute `mu_s` and the two ordered off-diagonal pairs ending at row `s` contribute `2(s−1)mu_s`, so

`sum_(r,s) min(mu_r,mu_s)=sum_s(2s−1)mu_s=b+2 beta(mu)`.

Multiplying the source's child formula by each multiplicity and summing therefore gives exactly `sum_j a_j b_j=ab−4 beta(mu)`. Validity supplies nonnegativity of every summand; hence each child product is bounded by its parent's product. All `a b` values are at most `nk`, all partitions have size at most `k`, and all run counts and marks have the stated logarithmic bit bounds. Telescoping the same energy identity makes `sigma` nonnegative (in fact divisible by four); testing the integral marking equations also automatically rejects a parity mismatch.

The resulting length bound `O(k^2 log(k+1)+k log(nk+1))` is valid. The proof does not expand a long chain or enumerate an integer of numerical size `n`.

## 4. A completely explicit canonical serialization exists

The report's canonical-field convention can, for example, be implemented with fixed widths computed from the input. Take a width `C=ceil(log2(k+1))` for each partition part, partition length and skeleton-node count, and a width `B=ceil(log2(nk+1))+1` for each repeat count and mark. Store the node count first, then for each preorder node its repeat count, partition length and decreasing positive part list; append the marks in the computed leaf order. All integers have exactly their prescribed width. Parse one complete rooted tree, require the number of records to match, and require the unused portion of a fixed polynomial-length witness to be zero.

This is one explicit implementation of the report's canonical serialization, not an extra hypothesis. Arity is determined by distinct part values, types are derived recursively, and leaf count is known before reading the marks. No choice of leading zeros, delimiters, node order, or redundant trailing records creates extra witnesses. The two widths and the number of records give precisely the report's bound.

## 5. Verifier and exact counting complexity

The verifier can scan the explicitly listed input rectangles, recover `n,k,r`, check all partition and size requirements, and reject malformed encodings before doing recursive arithmetic. There are at most `k` records with at most `k` listed parts each. Computing each `Q_j`, multiplicity, type, run update, leaf sum and marking inequality takes polynomial time in the input length. All intermediate integers have polynomial bitlength; their derived bounds can be checked directly. A tree of zero nodes or an incomplete child list fails the root/arity parse.

The explicit-list input length is at least `k`, and it includes the binary lengths of the numerical parts. Thus the witness length and verification time are bounded by fixed polynomials in that length. The exact compression bijection and the canonical serialization give one accepting witness per source marked tree. Combined with the source's exact counting theorem this proves the stated restricted #P result. No evaluation of the coefficient is needed before choosing the counted objects.

The conclusion is not transferred to an input containing only three compact numbers `n,k,r`. In particular it does not conflict with F34's wholly binary plethysm output-size obstruction. The source's numerical FP discussion is not silently treated as a polynomial-time binary-part algorithm here.

## 6. Literal long-tree example and scope

For `n=2s,k=2,r=2s`, the only internal choices are `(1,1)` and `(2)`. After `j` repeats the latter yields the single leaf `4s−4j`, so the unique leaf mark forces `j=s`. Counts greater than `s` would already violate the nonnegative type requirement. Thus there is exactly one marked source tree, with `s+2` vertices, while all three partitions are `(2s,2s)` and have logarithmic description length. The compressed skeleton has exactly two vertices and one binary run count. This verifies both uniqueness and the claimed literal-size obstruction, not merely an example of a large unmarked tree.

The final generated fragment retains all encoding, non-Ehrhart and nonstandard-basis limits. The cited Kahle–Michałek rectangular identification is on printed p.6 and belongs to the same equal-rectangle/two-row family; the known ordinary-Ehrhart obstruction does not contradict the positive tree witnesses.

Suggested events: `F37-KOH-GCT-REPORT-b9df1650` and `F37-KOH-GCT-FINAL-33f01af5`, full independent proof/source-definition review and exact final-fragment match, PASS. The full external KOH/O'Hara research theorem was cited and source-matched; no independent reproof of that theorem or formal-kernel certification is claimed.
