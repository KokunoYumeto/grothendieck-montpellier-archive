# A38 independent complete-proof review

- Date: 2026-11-21 UTC.
- Reviewer: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
- Outcome: PASS.
- Source SHA256: d7b29854fc840c976e7ca03a4fec4ad79df1e87196df1ed2cc899de53d49d19e.
- Reviewed checker SHA256: 106ceb42a28a665d5d91aeff9db95d65614545dbfb94cf97aa97f6d1290cb5f5.

The entire source and entire finite checker were read. The Artin--Schreier pole/genus/rank input and the previously checked A13 Frobenius polynomial imply the stated curve and Jacobian point counts. Opposite eigenvalue pairing and the beta recurrence give 16636 = 4*4159. The stated residues prove exact order 2079 of 2 modulo the prime4159. An independent short polynomial-arithmetic calculation checked the explicit (3,54) point, recurrence, primality, and all four residues; its output is retained beside this audit. The supplied full enumeration script was read, not rerun by this reviewer.

The three pairwise Weierstrass differences give all nonzero geometric 2-torsion points. Since the rational Jacobian order has exact 2-adic valuation two, its full rational 2-Sylow is elementary of order four. Consequently 2[W-R] has no 2-primary part, and it is nonzero precisely for a non-Weierstrass R. Its order is therefore exactly4159. Extension of constants cannot alter the order of a fixed geometric class or create another primary component.

The integral Rosati real-multiplication input is the complete A33 supplement previously independently checked at SHA87a2edb3d9a51b8018b3c04af15682d40fe5eb5d9ddaae45b7ae3f08f811f3f1. The theorem refutes universal canonical-prime forcing on the stated RM locus. It does not assert that these pointed examples are prescribed split-point images of a rank-one quintic transfer. The final paragraph correctly distinguishes failure of A29's sufficient criterion from failure of point separation. No formal proof-assistant verification is claimed.
