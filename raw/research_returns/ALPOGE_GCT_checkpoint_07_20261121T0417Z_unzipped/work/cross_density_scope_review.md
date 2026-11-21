# Independent review of P-F48

Reviewer: /root/bridges, GPT-6 Astra Pro, inherited/undisclosed effort.

I read the complete written proof in positivity_density_scope.tex and independently reconstructed every count and representation identity. PASS, with no correction required.

The exact shell populations have nonzero denominator for every N>=12: odd N=2u+1 has2^(u-1) identity-outer triples; even N=2u+4 has at least2^(u-2) triples ((3),(a),(3a)), and the highest-weight multiplicity is exactly1. Both bounds imply2^(N/2-4), with equality of the exponents in the even case.

The inner determinant exponent is3m/n+qm, which is integral. Applying the outer highest-weight determinant twist at every stretch s and cancelling the target twist gives precisely f_n(rs), including q=b=0. The bit estimates count disjoint actual partition entries. The target supplies n copies of ell(r), the first outer part another copy, the remaining m-1 outer parts ell(b), and all n positive inner parts ell(q) when q>0. Thus the exponent N/4 is valid uniformly for n>=4 and all boundary cases. Parameter collisions only improve the upper bound.

Dividing the at-most-N numerator bounds by the exact-shell lower bound gives exactly the stated exponential estimates in both populations. The unscaled zero follows from the already checked P32 exterior range, and the final warning correctly distinguishes all realized positive stretches from positivity of a constituent away from its own residue class.

I freshly read the original GCT VI PDF: printedp9 input encoding (PDFp12), printedp25 narrow SH(b) exact N (PDFp28), and printedp51 unified SH(b) at most N (PDFp54). They support the source-scope claims verbatim. No fixed-rank/shape conditioning is inserted. This is an independent whole-proof review, not a finite search.

## Correction to the first source-scope PASS

Complexity's subsequent self-read found that unified Section3.4 uses rank-augmented cost n+L, explicitly on printedp53. My initial audit read the three directly cited pages but omitted this dependent encoding definition. Therefore that initial source-scope PASS was too broad. The narrow exact-shell mathematical proof is unaffected. I freshly read Sections3.3–3.4, including printedp53, and verified the augmentation. I also flagged that padding ambient rank makes distinct unified inputs, even though it does not make distinct narrow triples; at most N such lifts add only a polynomial factor. The correction event is preserved in the ledger, and final approval awaits the patched separate population proof.

## Corrected whole-proof review: PASS

I reread the entire final draft after the separate unified population and all ambient-rank lifts were added. The exact source cost is n+L. Stable Schur-character specialization preserves the target coefficient at each stretch once the target height fits; all padded h>=n are admissible, and at most N such ranks fit the cost. The narrow numerator bounds may therefore be multiplied by N. Rank-one examples of narrow length N-1 give denominator >=2^((N-1)/2-4)>=2^(N/2-5), for N>=13. This gives precisely32N^2 2^(-3N/10) and32N^2(N+1)^3 2^(-N/4). Both population claims now pass, with the correction history retained. Only a harmless duplicate phrase “are as displayed” remains in the opening prose; no mathematical gap.
