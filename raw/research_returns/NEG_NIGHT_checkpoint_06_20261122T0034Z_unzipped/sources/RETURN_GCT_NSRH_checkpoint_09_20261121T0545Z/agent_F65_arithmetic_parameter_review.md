# Fresh full review: F65 arbitrary fixed arithmetic parameter

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

Complete report: agent_joint_normalization_arithmetic_parameter.md, SHA256 5f79181a45048db296669d4f156bc8afaa4eaa53072f8be99c901c04fcf70109.

Complete fragment: finding_F65_arithmetic_parameter.tex, SHA256 1a2053313af1db0079a2b68af19c470874ef164f0ecea538a35edbd008404127.

Result: PASS, no correction. Both entire files were read directly and their complete proofs independently reconstructed. The fragment matches the report, including the eventual-equality hypothesis, all collision cases, the zero-object conclusion, continuous finite-image sufficiency, and separate dictionary.

## Mathematical reconstruction

For the three distinct roots beta,1,beta^-1 of d, finite power-sum uniqueness makes each visible root an actual eigenvalue with its specified Euler multiplicity. The root 1 has weight zero and coefficient +2, forcing the pure complex weight to be even. Positive coefficient +1 at beta then forces its integral point weight m to be even. Its inverse has weight -m.

When beta^2,beta,beta^-1,beta^-2 are distinct, their weights 2m,m,-m,-2m are all even. A pure complex of any fixed integral weight therefore gives all their permitted degrees the same parity. The mixed coefficient signs -1,+1,+1,-1 are impossible. No hidden-root or opposite-degree cancellation can evade this, because a fixed root of known point weight has one permitted cohomological degree.

The positive exponent differences are exactly 1,2,3,4. Thus the only remaining possibilities have orders 1,2,3 or4, including the previously separated beta=1,-1 cases. I checked each grouped power sum: order1 gives d=4,c=0; order3 cancels c identically; order2 gives 2(-1)^n-2; order4 gives beta^n+beta^-n-2(-1)^n. The last two have distinct weight-zero roots with both signs and fail purity.

For order1 or3, the four lines 1,1,beta,beta^-1 in degree zero give a pure weight-zero D, and C=0 suffices. Their finite image gives continuous arithmetic Galois actions even when ell divides the finite order. The finite-etale model consisting of one rational point and one degree-three point has exactly the stated geometric Frobenius spectrum. The geometric versus arithmetic inverse convention does not change this multiset.

Eventual equality is enough throughout: the finite Vandermonde matrix on consecutive large exponents is nonsingular. A pure complex with zero power traces has no hidden cohomology, including Jordan blocks, since each root is confined to a unique degree and its trace multiplicity is its positive algebraic multiplicity with one fixed sign.

## Primary source and dictionary checks

I freshly read the original BBD text at 5.1.5 and 5.1.8, printed pp125--127. It defines integral point weights by all complex conjugates and, on the smooth zero-dimensional point, pure weight w is exactly H^i pure of weight w+i. This is the exact hypothesis used here. The two VIII Figure2 source formulas and their right-parameter normalization had already been independently source-checked in agent_F65_joint_normalization_review.md; this supplement uses neither an ambient Figure1 coefficient nor a changed normalization.

The SGA3 torus, SGA6 perfect/representation K0 and cote90/cote133 references remain framework anchors. They do not provide the extra arithmetic comparison q_src=beta^n. The conclusion is a classification of two scalar sequences under that common fixed-parameter law. It does not assume raw pure traces were source axioms, identify canonical labels, or cover mixed complexes, operator insertions, separately retuned values or removal of a signed vanishing factor.

No new symbolic execution, compilation or visual-layout check is claimed for this review. No main paper or shared master log was edited.
