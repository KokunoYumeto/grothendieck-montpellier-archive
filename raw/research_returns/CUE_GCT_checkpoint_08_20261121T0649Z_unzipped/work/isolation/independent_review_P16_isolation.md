# Independent complete proof review of P-16

Outcome: PASS; one display-delimiter typo requested, with no mathematical repair.
Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I.
Time: 2026-11-21T04:16:02+00:00.
Reviewed SHA256: `f149b565fe48c9062dde7c27f48996d3452eaf7089a4361b2463648d0b6878ac`.

I read the complete standalone proof and rederived every mathematical step. The four pole sets have sizes2d,d,d,2d, distinct moduli except the middle pair, and the middle pair has distinct dth powers. All poles are simple, all indicated numerators are nonzero there, and the radical/cyclotomic field bound is (2d)^2*phi(2d), at most72 when d3.

The identity P2*P3=-P1-P4 gives R1*R2+R1*R4+R3*R4=0 exactly. Each rational function decays as T^-d, so residues annihilate powers0 throughd-2, precisely the polynomial part of a generic numerator-degree-k/linear-denominator rational function. The sign in evaluating L_i is negative. Clearing denominators extends the identity from genuine linear denominators to all defined constant-denominator cases without incorrectly claiming termwise vanishing of degree-k polynomial parts.

The ordered E12/E23 unit word has exactly the three stated quadratic path pairs. The four variable groups are disjoint and every residue nonzero, so Q is a nonzero multilinear polynomial. P14's balanced RFE1,1 hitting theorem rules out width2 in every variable order. The displayed cut inside group2 independently gives three linearly independent degree-separated left and right polynomials in that particular order. Multilinear reversal permutes each coefficient basis, preserves all coefficient-cut ranks, and has the explicit generically invertible xI+rhoE word. Reciprocal rational evaluation transfers the ideal identity with its dense-open qualifications intact.

The Lagrange normalization D_b=A'(b), the sign in D_b*SV2_b, the numerator/denominator degrees1/2, and the final diagonal scaling are correct. H has degree16, minimum width exactly3, and the displayed factors have nonzero generic determinant D_b^3 X_b^3. P14 with common slope1 proves the centered map nonzero. Its balanced rational corollary also applies to these full-rank factors, so the construction does not create a balancedRFE2 counterexample. No monotonicity-of-factor-width inference is made.

The only requested repair is the plain closing `]` after the displayed residue evaluation, which should be `\]`. No finite computation was rerun in this review. The HMM Proposition2.2 convention was already primary-audited earlier in the session; no new source reopening is claimed here.
