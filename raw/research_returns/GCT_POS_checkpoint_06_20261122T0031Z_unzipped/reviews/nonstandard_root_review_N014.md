# Whole-proof review: N-014

- Date: 2026-11-21, 22:03 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; GCT_POS.
- Type: targeted proof check (entire proof), primary-source comparison and exact symbolic check.
- Outcome: **PASS**, as a defect of the literal printed order prescription.

I read all of `viii_label_order.tex` and the relevant complete source passages: VIII §2.3 defining the order through a single highest weight, and §3.3 steps(1)–(3); VII §7.2.2 including its computational qualification. Primary arXiv PDFs confirm the printed-page locators: VIII p.11 and pp.20–21; VII pp.48–49.

I re-read the N-010 model/decomposition proof used by N-014. For the module `M4⊗M22`, the actual P-generators are the displayed A-matrices of shape22. Independent SymPy multiplication verifies `J P_i=(D I-P_i)J` and `det(J)=D-1`. The tensor-product decomposition and the already checked complete list of pairwise distinct simples imply that its multiplicity space has exactly the two maximal weights `(4,22)` and `(22,4)`. They are incomparable in the product root order. The two extra summands when four-row ordinary modules are present are dominated by these, so the defect persists in a faithful realization. The equal-weight pairs in the two-row realization independently violate antisymmetry if the printed iff-rule is imposed on distinct labels.

No nonstandard duality conjecture is used to prove the multiplicity-space decomposition. Such a conjecture is needed only if one gives that space its proposed nonstandard quantum-group name. Antichain orders and total refinements are explicitly alternative definitions; N-014 does not show that every repaired construction fails.
