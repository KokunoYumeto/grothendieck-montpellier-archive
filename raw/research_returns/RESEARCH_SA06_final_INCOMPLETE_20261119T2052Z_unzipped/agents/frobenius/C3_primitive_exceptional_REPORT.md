# Primitive exceptional-boundary proof for C.3bl

## Result and exact scope

The complete auxiliary proposition is proved in `C3_primitive_exceptional_boundary.tex`, equations PB.1–PB.18. It applies to the regular projective local model with exceptional divisor

\[
V=\mathbb P^m\times\prod_{i=1}^{r-1}W_i\times C,
\qquad m\ge0,
\]

where the $W_i$ are smooth cubic surfaces, the conormal is the external product of their hyperplane bundles with $\mathcal O(1)$ and $K_C$, and the actual projection to the projective/cubic factors survives on the resolution. A nil line bundle times one divisor from each cubic is nonzero on the puncture whenever its designated relative Milnor differential cup is nonzero. The proof removes **the entire exceptional image**, retaining all torsion in the curve Picard group and all Smith invariant factors.

The lemma alone does not construct an ordinary family or a principal cut with zero target endpoint. The separately audited combined C.3bl, owned by real_weil, supplies those geometric conditions. We do not infer a rational kernel from these exact-order-(p) constructions.

## Complete proof architecture

1. The relative ordinary Milnor sheaf has exponent (p), a canonical quotient to the rank-one conormal differential module, and the exact actual-line-product formula, including characteristic two. Rost localization proves the needed preceding Milnor cohomology groups divisible, so relative classes reducing to zero have unique lifts.
2. The integral cellular Chow decomposition retains the entire curve Picard group. An elementary positive-adjoint calculation proves (b^2) injective on the required rational free lattice for all (m\ge0), including its weight-zero endpoint. This removes every free/numerical part of the exceptional kernel. Smith form then writes its entirety as (\sum v_jQ_j), with (b v_j=d_jw_j) and (d_jQ_j=0) in (\operatorname{Pic}^0(C)).
3. The designated coherent cup factors through the **free integral** quotient

   \[
   \bigotimes_i\bigl(\operatorname{Pic}(W_i)/\mathbb Z A_i\bigr).
   \]

   Each (A_i) is primitive because it pairs to one with a line. The selected multidegree of a (b)-multiple inserts an (A_i), so this quotient kills the entire (b)-image and its saturation. Euler cohomology gives (\mu_{A_i}=0), proving the factorization in every characteristic. No Smith denominator or factorial is inverted.
4. The canonical actual extension (\widetilde K=\mathcal O(-V)\otimes q^*L_T^{-1}) replaces a nonexistent projection to the curve. Every curve line bundle lifts by the finite-obstruction/formal-existence/approximation argument. The unique relative degree-two class of (\widetilde K\widetilde Q) has a differential independent of the chosen lift: changing it gives a cup with two degree-one curve cohomology factors, hence zero. It is an additive map from the divisible group (\operatorname{Pic}^0(C)(k)) to a (p)-killed coherent group, hence vanishes.
5. The actual Chow projection formula expresses every possible boundary as the sum of the saturated terms from step 3 and the curve terms from step 4. Finite pointed-etale descent permits the integral Milnor–Bloch ring comparison on a smooth finite-type model. Its restriction to the fixed first jet, and uniqueness of relative lifts, give the contradiction. No Bloch formula on a nonreduced scheme is used.

## Independent audits and retained earlier proof

The root read every step of PB.1–PB.18, its final integral-quotient replacement, and the exact source statements; its complete receipt is `notes/ROOT_PRIMITIVE_EXCEPTIONAL_BOUNDARY_REVIEW.md`. Cycles completed its full final receipt at **15:18:49 UTC** in `agents/cycles/C3_primitive_exceptional_boundary_independent_REVIEW.md`. Real_weil completed its full final receipt at **15:19:15.098348 UTC** in `agents/real_weil/C3bl_primitive_boundary_independent_REVIEW.md`. Both peers explicitly include (m=0), all characteristics, and the actual finite-stage argument.

The original complete proof in `C3_primitive_exceptional_boundary_draft.tex` uses a Witt lift to a torsion-free coherent module to prove the saturation claim. That proof also passed the independent audits and is retained unchanged. The final Step 3 is shorter and removes the Witt-lifting dependency by using the free integral Picard quotient. This is a proof simplification, not a withdrawal of the earlier argument. The original compiled wrapper is retained as `output/C3_primitive_exceptional_Witt_check.pdf`.

The independent combined C.3bl read was completed at **15:22:35 UTC**, separately from the auxiliary audits; see `C3bl_full_higher_integral_independent_REVIEW.md`. The safe-range C.3bk has its own complete independent proof and receipt and does not depend on this auxiliary.

## Opened primary sources and exact uses

All source entries preserve their opened markers. The new entry is `frPrimitiveProjectiveCohomology` in `C3_primitive_exceptional_references.bib`.

| Primary source | Exact locator and use | Reading status |
|---|---|---|
| Stacks, projective-space cohomology | Lemmas 30.8.1–30.8.2, Tag01XS; Euler/hypersurface cohomology and base change | Full statements/proofs freshly read during this auxiliary audit |
| Stacks, Picard thickenings | Lemma37.4.1, Tag0C6R; individual square-zero Picard obstruction | Full statement/proof freshly reread; prior C.3az input retained |
| Stacks, formal existence | Lemma30.24.3, Tag0885; compatible actual invertible systems | Full statement/proof freshly reread; invertibility away from the closed fibre checked separately by properness |
| Stacks, completion and approximation | 15.51.14/0AH2; 16.12.1/07GC; 32.10.3(2)/0B8W; 15.13.3/0H74 | Previously opened/read in full for C.3az; scope rechecked here; both peers/root freshly reopened all four for this lemma |
| Rost (1996) | Proposition4.1(3), Section5, Corollary6.5, Proposition8.6, Section12, pp351,356–360,370,382–383 | Fresh full exact inputs read in the immediately preceding all-degree divisibility audit; unused erroneous/corrected passages kept separate |
| Kerz (2009) | Definition2.1, Theorems7.1/7.5, author pp3,21–22 | Fresh exact statement/scope read in this run; ordinary Milnor symbols and infinite residue fields verified |
| Braunling (2013) | Section3, full ring-product diagram(22), published pp557–558 | Fresh complete diagram and neighboring construction read in this run; no nonreduced comparison inferred |
| Huybrechts, cubic hypersurfaces | Chapter4, Proposition2.4, p178 | All-characteristic cubic blow-up input already opened/audited in C.3bi/bj |
| Jiang (2023), Stacks | Theorems2.4/2.8(3); Lemma42.36.2 Tag02TX | Previously opened integral point-blow-up/projective-bundle formulas; actual external-product ring is derived by iteration |

URLs are in the corresponding bibliography entries. No unsupported originality or priority claim is made.

## Exact finite certificate and compilation

`code/check_primitive_exceptional_quotient.py` verifies the integral quotient matrix (\mathbb Z^7/\mathbb ZA\simeq\mathbb Z^6), its unit minor, and the identity (\Psi b=0) on every basis column in twelve cases (1\le s\le3), (0\le m\le3). The run began **15:20:04.996177 UTC**, ended **15:20:05.031213 UTC**, and took **0.035037787 seconds**. All twelve cases pass. Full exact JSON is `output/C3_primitive_exceptional_quotient.json`; the deterministic multiplication-column hashes and dimensions are retained. This bounded check is not the proof of the all-(s,m) statement.

`code/finalize_primitive_boundary.py` reproduces the final auxiliary from the retained Witt draft and preserves the earlier wrapper. `code/build_primitive_exceptional.py` builds with the shared LuaLaTeX format and extracts only cited bibliography entries, recording their origins. The current-source five-pass run began **15:20:44.786739 UTC**, ended **15:20:49.355083 UTC**, and took **4.567887240 seconds**: every return code is zero, seven pages, 176646 bytes, no overfull boxes or undefined citations. Its remaining underfull boxes occur in bibliography formatting. The later heading-only identification with C.3bl does not change the mathematical proof; the combined master receives its own final build and visual QA.

Two initial wrapper failures were corrected before the successful builds: an undefined `bigboxtimes` macro and a missing `end{gathered}`. Their actual tool outputs/timings were recorded; the second failed run and all later build records are retained by the builder's timestamped history. No failed build is presented as a successful validation.

## Next research gate

The positive-characteristic **rational** high-range restriction question remains separate. The pre-existing finite K0 detection along a principal centre detects classes on the whole divisor, but does not lift supported perfect classes there from exceptional coherent classes on the regular source. The present exponent-(p) Milnor construction does not bridge that gap after rationalization.
