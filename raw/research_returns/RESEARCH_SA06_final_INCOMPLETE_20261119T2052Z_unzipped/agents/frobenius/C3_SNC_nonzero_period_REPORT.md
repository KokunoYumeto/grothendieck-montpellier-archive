# Audited research model: nonzero triple periods and component Picard exclusion

Status at 2026-11-19T18:23:59.585248+00:00: **audited auxiliary only, unregistered and not integrated into the manuscript** at the parent's explicit direction. No ordinary Chow class is asserted to survive. These results are method/case refinements and do not reset the main-gate review clock.

## Complete findings

For every prime p, the two explicit constant quadrics in NP.1 meet in a smooth elliptic quartic. A generic hyperplane contributes four marked triple points and two conic edges. The affine equation Q1 Q2 H − G6 gives an algebraizable normal isolated threefold germ. Blowing up the origin and then the first two Weil components gives a regular projective resolution with three rational exceptional components: the36-point blowup of the first quadric, the12-point blowup of the second, and P². The marked double curves and four triples are unchanged. A positive exceptional divisor D with coefficients M+2,M+1,M has ample negative restriction for M sufficiently large.

The dual complex has H2_Q of dimension three. Each corresponding elliptic period q_j−q_1 is nontorsion. NP.9 strengthens this: none belongs to the rational image of the component Picard groups on the elliptic edge. The proof uses the complete (2,2) Koszul restriction, the irreducible ordered Abel fibre C^23, and the full generic S24 action, including characteristics dividing24!.

These conclusions show that the sufficient period hypotheses of C.3bq are additional even on actual negative SNC exceptional surfaces with rational components. They do not compute the quotient by arbitrary proper perfect-family relations. Variable-unit higher K-families, coherent totalization corrections and endpoint-zero classes remain outside the Picard-span exclusion.

## Proofs and exact source scope

- C3_SNC_nonzero_period_model_RESEARCH.tex: NP.1–NP.8, the complete geometric and nonzero-period construction.
- C3_SNC_period_Picard_span_RESEARCH.tex: NP.9, the separate complete component-Picard-image exclusion.
- C3_SNC_nonzero_period_SOURCE_AUDIT.md: complete primary-read ledger and the deliberately unused Artin-contraction source. The actual affine equation avoids contraction entirely.
- C3_SNC_nonzero_period_references.bib: one new canonical entry, Stacks0B44 fibrewise ampleness. Other keys reuse exact already-owned bibliography entries.

## Independent audits actually received and read

- Root complete NP.1–8 and separate NP.9 reconstruction: notes/ROOT_SNC_NONZERO_PERIOD_MODEL_REVIEW.md and corresponding events; full mathematical/source PASS in the recorded limited scope.
- Real_weil complete NP.1–8 proof/source/code-output audit: agents/real_weil/C3_SNC_nonzero_period_model_independent_REVIEW.md; completion18:15:50UTC. No fresh Kollár opening or program rerun claimed by that reviewer.
- Cycles complete NP.1–9 proof/source/code-output audit: agents/cycles/C3_SNC_nonzero_period_independent_REVIEW.md; completion18:22:23UTC. Fresh Kollár local charts, Stacks ampleness and projective cohomology read. No independent program rerun.

The author read allthree complete review files. The only post-audit textual changes remove a stale pending-audit heading, add the exact requested projective-space cohomology citation and clarify the C_12 edge label. No proof claim was added after those passes.

## Computation and build evidence

The exact finite program code/check_SNC_nonzero_period_model.py completed19 checks at18:11:45.763918UTC in0.05856967400177382seconds. Full output is output/SNC_nonzero_period_model_certificate.json. It checks only gradient determinants, equations, node counts, degree weights and the finite dual chain complex; it does not certify geometry, genericity, nontorsion, family equivalence or Chow survival.

The first NP.1–8 standalone completed18:14:53.115857UTC in4.04366693799966seconds, four pages124152bytes, no warnings; allfour renders were actually viewed by18:16:58UTC. The combined NP.1–9 standalone completed18:23:06.808283UTC in4.570816070001456seconds, five pages144664bytes, allcommands0 and no warnings. Allfive combined renders were actually viewed by18:23:21UTC, with no layout defect. The final small C_12 wording repair will receive the final rebuild recorded in the same combined builder metadata.

Final typographic C_12 edge-label repair rebuild: 2026-11-19T18:23:59.629441–18:24:04.250989UTC, runtime4.62148253700434seconds; allfive commands0, five pages144685bytes, no warnings. Current machine-readable metadata: output/SNC_nonzero_period_combined_build.json. The changed fourth page was rendered and actually inspected by18:24:15UTC, clean. The preceding allfive-page visual pass and the original four-page proof build are separately recorded above. No mathematical change was made.

## Scope after the certified C.3bt reduction (2026-11-19T18:49:40.819495+00:00)

C.3bt was promoted at 18:48:51.902100 UTC after root and both complete peer audits. Its marked edge-family construction removes the entire component restriction kernel without a dual-complex cohomology or triple-period condition. All three components in NP.1–NP.8 are rational smooth projective surfaces, hence their rational component Albanese kernels vanish. Therefore this particular algebraizable strict-local threefold model has **B² of its puncture, with rational coefficients, equal to zero** by C.3bt. The nonzero periods and NP.9 component-Picard-span exclusion remain valid. They now explicitly demonstrate that these period and Picard conditions are unnecessary for C.3bt; they do not obstruct the actual proper-perfect-family quotient. NP.1–NP.9 remain audited auxiliary results, unregistered and outside the manuscript at the parent's direction. This consequence is an application of C.3bt, not a new main-gate reduction or a separate movement claim.
