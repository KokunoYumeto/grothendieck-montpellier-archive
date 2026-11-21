# Independent whole-proof review: A25

- Date: 2026-11-21.
- Reviewer: GPT-6 Astra Pro; reasoning effort not exposed; `/root/effective_galois`.
- Source: `work/row_audit/LANG_PAIRING_RANK_BOUND.tex`.
- SHA256: `1d34480ea1946946765da65b993a7684218d9aa3213bb1f0f18b39b716cbe5a5`.
- Scope: complete statement, proof, thresholds table, asymptotic statement, and final scope paragraph.
- Outcome: **PASS**. No mathematical gap found. This is a mathematical review, not formal proof-assistant verification.

## Proof checks

The principal polarization identifies the dual torsion module, producing a perfect alternating pairing on the four-dimensional odd-prime torsion space. A rational subspace of dimension at least three cannot be isotropic. A nontrivial pairing value between rational points has exact prime order, and Frobenius equivariance forces r to divide Q-1. Thus Q=2^v has v divisible by the order of 2 modulo r.

I re-read the exact A12 inequalities. The weaker ordinary positivity test already implies |H| > 2 sqrt(Q) |J(F_Q)|/(sqrt(Q)-1)^2; the floor in LW.1 gives the same strict real positivity condition because Q+1 is integral. The Weil lower bound yields |H| > Q^(3/2) when Q is at least 16. Geometric torsion gives |G[r]| at most r^4 and |G[3r]| at most 81r^4 for r different from 3.

All four integer starting comparisons at 11,17,29,41 are correct. Increasing odd r by two multiplies the polynomial side by less than two, and the exponential side by eight in the primitive case or 2^(3/2) in the signed case. These ranges force Q at least 16 under the hypothetical rank-three case. The resulting contradiction gives rational rank at most two for every successful specified prime-level Lang test.

Solving the full LW.2 inequality gives the factor 2sqrt(Q)+1. Using |G[r]| at most r^2 and |G[3r]| at most 81r^2 gives the square-root thresholds and the exact factor 1/9. The stated asymptotics follow from the genus-two Weil estimate. The ordinary variant replaces 2sqrt(Q)+1 by 2sqrt(Q). The conclusion is correctly restricted to these sufficient numerical tests and is not extended to theta nonexistence or truncated prime-power subgroups.

## Exact primary source reopened

J. S. Milne, *Abelian Varieties*, author version 2 January 2022, Section 16, p.29 (perfect pairing of Galois modules) and Lemma 16.2(e), p.30 (alternating pairing supplied by a line bundle), including the displayed proof.

https://jmilne.org/math/xnotes/AVs.pdf

Web references: `turn395851678view0`, `turn150653761view0`, `turn377915328view0`.

No separate computational certification is claimed for the elementary integer comparisons; they were checked as part of reading the proof. No final source files were edited.
