# Independent whole-source review: A28 recovered canonical-class criterion

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Reviewed final source: `work/row_audit/A28_RECOVERED_CANONICAL_CRITERION.tex`.
SHA256: `2b33638f1ac4b8b854fc6ceecbd80eae14285e66aed2cdc359ce97ea4ef08801`.

PASS. The complete displayed statement and its interpretation were read, and the complete original successor final A.26 statement and proof were read in `recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`. The result is explicitly credited as recovered and rechecked, not a new prime-level theorem.

The old theorem already works in every characteristic: for an odd prime r different from p, inversion in the p-power orbit and a cyclic quotient detecting the canonical class imply that every nontrivial reduced character L-value is nonzero. The proof uses c1(chi)=chi(kappa)c1(chi inverse), and failure would give c1=-1 at both inverse characters and force chi(kappa)=1. Faithfulness on a prime cyclic group supplies the contradiction. The source theorem supplies existence of a detecting quotient when kappa is not in rG; its argument proves the more explicit every-detecting-surjection assertion stated in A28.

The connected Lang-pullback and prescribed split fibre were checked against the complete construction and connectedness argument in A12. In characteristic two with rational Weierstrass W, K is linearly equivalent to 2W, so multiplication by two identifies the canonical detecting condition with detection of W-P in G/rG. The prime cyclic unit group has a unique involution, making even ord_r(2) equivalent to inversion being a power of two. The warning for general composite modulus is correct: the doubling subgroup modulo15 is {1,2,4,8}, which does not contain14. Two rational Weierstrass points differ by a2-torsion class, so every odd quotient kills that difference. Rank-one curves have the two rational branch points established in A26. At a Weierstrass prescribed point, kappa=0, and the condition gives no witness.

Two editorial issues found in the first draft were reported and corrected: a sentence had said the complete proof was given here although it is retained and cited, and an undefined variable b had survived in the interpretation paragraph. The final narrow corrections were read and pass. Neither issue affected the mathematics.

This review does not infer a missing prime divisor from Hooley density, nor nonexistence of actual witnesses from failure of the sufficient detecting-class condition. No final paper files were edited.
