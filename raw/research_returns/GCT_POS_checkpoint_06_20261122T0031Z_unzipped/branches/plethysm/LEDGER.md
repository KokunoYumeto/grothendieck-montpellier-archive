# Plethysm branch ledger — 2026-11-21

## Completed

- **PNEW-001**: smallest-rank primitive-dyadic witness is n=4, x=19, with 2W=1/8>0=f. This is an inherited P-F35 corollary, not a new discovery. Exact p=s=23 rerun confirms the full analytic calibration.
- **PNEW-002–005**: newly sharpened near/far increments and starting mass give **n0=79000** for p(f_n)>2^(n/8), s(f_n)>=2^(n/8). Full proofs, exact rational margins, author whole-proof reread and independent /root/nonstandard whole-proof PASS.
- **PNEW-006**: inherited P-F32 exterior identity, reproved in its needed form, gives new finite residue comparisons: 2W9(7)=782264335828/64>binom(35,21), and 2W9(6)=1819142906755/64>f9(6)=1. At n=15,x=60, the symmetric ambient bound is below 2^866 while 2W exceeds 2^881, giving p(f15)>60 and s(f15)>=60. Additional n10 witnesses are in the certificate.
- **PNEW-007**: h(s)=f15(7s), ordinary input inner(3), outer(35), output(7^15), has h(1)=1, p(h)>7 and s(h)>=7. Top exterior power proves the initial value; integer cyclotomic recurrence proves 2W15(49)>2^875 while the symmetric dimension bound is <2^766. The odd-dilation paired-constituent argument is fully supplied. A second exact witness at s=2 is also included.
- **PNEW-008**: outer determinant padding preserves that positive-initial ray's entire canonical graded algebra. Input lengths grow while all intrinsic grading stabilizers remain bounded. This refutes the effective/intrinsic quotient growth converse. It makes no unqualified claim about raw GL stabilizers of differently twisted Cartan-cone presentations.
- **PNEW-009**: new fixed-rank, fixed-inner-representation theorem: for m=dim S_mu(C^n)>n, strict saturation exceptions in the original exact raw-bit shells, conditioned on nonzero initial coefficient, have exponentially small density. Full elementary polynomial sublevel and shell-counting proof, with the full branching-cone and finite chamber theorems explicitly cited and checked at Baldoni–Vergne §5.1. Author and independent root whole-proof reviews passed; primary branching statements independently checked twice. Constants depend on the fixed embedding, so varying-rank SH(b) stays open.
- Full inherited P-F19,23,24,26,27,28,30,31,56 proof chain read and assembled; statement-level predecessor inputs needed here were upgraded by whole-proof reading. P-F57 original dominance proof also read. Standard classical background theorems remain precisely cited background.
- P-F12/PL-Q22 numerator erratum rechecked, with direct KM coefficient derivation. Broad fixed-rank P-F14/P-F15 and finite-coding P-F63 proofs wholly rechecked against GCT VI §§3.4.1–3.4.2.

## Positive-formula addendum completed after the standalone paper

- **PNEW-010:** the actual G-040 transfer cokernel, with `m=2r`,
  `b=r(r+1)+1`, has at least `2^(r-1)` minimal homogeneous generators in
  its trivial-isotypic component over the proposed invariant polynomial
  algebra. This obstructs a polynomial-size literal dense cover, not a
  compressed counting formula. The grading, finite Schur-piece dictionary,
  and exact certificate are in `uniform_positive_gate.tex` and
  `certificates/uniform_positive_gate.json`. Independent root whole-proof
  review and replay passed.
- **PNEW-011:** the scalar frame-point Cox ring is the known Grassmannian
  Pluecker ring (Castravet–Tevelev, Remark 3.9), with the full permutation
  action and Picard grading proved explicitly in `cox_six_dictionary.tex`.
  For six points its scalar Specht multiplicities are exactly
  `p_{mu,(c-k)}^((5c-6k),c)`. The arbitrary flag-tail problem remains separate.
  Independent root whole-proof review passed.
- **PNEW-012:** an explicit binary-size compilation of the known
  Pak–Panova–Swanson two-row-output formula gives 330 fixed tagged bounded
  polytopes over all `mu` of size 6, at most 45 per shape and 11 variables,
  with every real variable in `[0,3n]`. Full proof:
  `outer_six_scalar_positive.tex`; all matrices and evaluators are retained.
  Checks passed for 2,717 positive-count comparisons, 5,214 full-output
  coefficients at `n=0,1,2,3`, 242 direct matrix-polytope counts, and 44
  dimension identities. Independent root whole-proof/script review and
  replay passed. This resolves the scalar/two-row subrange, not all output
  partitions or stable two-row tails.

## Remaining positive-formula scope

Uniform compressed positive formulas for the full G-040 varying-parameter
family and arbitrary outer-six flag tails remain open. The scalar compilation
is a precise smaller solved range, and the dense-cover obstruction does not
exclude a different positive counting construction.

## Remaining density scope

**Narrow SH(b), exactly conditioned raw-length shells with all inputs varying:** neither proved nor refuted. PNEW-009 proves the fixed-embedding version, but its constants are not uniform in the rank or inner partition. The positive initial exception and all natural cubic determinant twists lie in the inherited P-F48 exponentially sparse families. No logarithmic-overhead map from arbitrary ordinary plethysm inputs to exceptions has been constructed. Raw presentation-dependent determinant-character converse requires a normalization; only the explicit intrinsic/effective statement is refuted.

## Files and checks

`PLETHYSM_STANDALONE.tex` assembles the full chain and companion sections. `PLETHYSM_STANDALONE.pdf` compiled to 58 pages with PNEW-009 included. All pages were inspected as contact sheets and the new density pages 55–57 at full resolution; no clipping or layout defects were found. The exact certificate script verifies 663 inverse-factor identities and eight strict inequalities, with no floating-point inference. `certificates/plethysm_exact.json` holds complete rational data. The auxiliary `exact_exterior_7.cpp` gives exact f9(7)=0 by Weyl alternation; this extra computation is not needed for the finite witness proof.

Independent threshold review: `../../reviews/quantitative_refinement_nonstandard_review_79000.md`. Root read PNEW-006–007 in full; PNEW-008 remains explicitly limited to the intrinsic quotient convention. Independent fixed-density review: `../../reviews/fixed_rank_density_root_review.md`. The first, looser constant draft is retained solely as review provenance; the active theorem is79000.

## Implications

The new threshold and certificates strengthen the explicit quantitative ordinary plethysm refutation. They give no new P versus NP separation, algorithmic lower bound, or refutation of all GCT obstruction programmes. The narrow density clause is logically separate; the broad density refutation relies on actual product closure and additive finite input specifications, which ordinary plethysm triples lack.
