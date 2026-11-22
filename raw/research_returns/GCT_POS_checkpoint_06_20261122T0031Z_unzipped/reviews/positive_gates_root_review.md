# Whole-proof review: PNEW-010 and PNEW-011

Date: 2026-11-21. Reviewer: `/root`, GPT-6 Astra Pro, effort not exposed, run GCT_POS.

## Scope and outcome

Read the complete files `branches/plethysm/uniform_positive_gate.tex` and
`branches/plethysm/cox_six_dictionary.tex`, every displayed argument, the complete
supplementary script, and the whole inherited GCT_PLETH G-015/G-016 file
`work/root/general_fiber_model.md`. Outcome: PASS within the explicitly stated
scope. These statements do not resolve the positive-formula questions.

PNEW-010 uses the actual total grading of the G-040 transfer. Its lowest target
degree has no domain contribution, so its invariant subspace survives in the
minimal-generator quotient. The displayed subsets give distinct monomials in
the polynomial invariant algebra Q[e2,...,em]. The rank bound 2^(r-1), with
m+b=r^2+3r+1, is therefore an all-parameter lower bound on explicit homogeneous
covers. It is not a counting-complexity lower bound. The Pieri calculation of
the finite Schur pieces has nonzero transfer scalar b-i, and the stable
balanced-space substitution satisfies all partition and ideal-exponent
conditions. The negative trace of an m-cycle excludes only a permutation basis.

For PNEW-011, the additive invariant-ring argument extends over the codimension
two missing last-column locus. The explicit q-coordinate map and transverse
valuation comparison identify the actual Picard components and permutation
action. Independent bookkeeping gives exceptional coefficient equal to column
weight minus c, last column weight (m-2)c-mk, and Pluecker degree (m-1)c-mk.
Interlacing forces the unique GL_m shape (q,c). The signed Pluecker-relation
example and the distinction between scalar sections and flag line-bundle
sections are correct. The Cox-ring identification itself is known: Castravet
and Tevelev, Remark 3.9, arXiv math/0505337v2, printed p. 9; primary PDF opened
and the remark inspected in this run. No novelty is assigned to that theorem.

## Computation

Executed the complete supplementary script unchanged. All monomial lower-bound
checks for r=2,...,16, all 17,527 Pluecker monomial degree checks, and all 103
uniform-exceptional-degree checks passed. Receipt:
`reviews/uniform_positive_gate_root_replay.json`. This is an independent replay
and source reading, not an independently written implementation or a formal
proof-assistant certificate.

## Input boundary

The original balanced-chart input T-032 and classical Borel-Weil/Schur-Weyl
theorems retain their inherited attribution. This review reads the full G-015
transport proof used here; it does not relabel every classical input as a new
re-proof. The recent restriction literature in the final comparison paragraph
was inspected by the authoring agent; its precise primary references are
recorded there and remain literature attribution, not a no-other-formula claim.
