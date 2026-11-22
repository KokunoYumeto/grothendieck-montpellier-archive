# Whole-proof review: Kronecker findings, first draft

Date: 2026-11-21. Reader: /root, GPT-6 Astra Pro, effort setting not exposed, GCT_POS.

Read the complete K-001–K-006 fragment, SHA256 `df8e9d3ff712b4b8edf697f8108d86e56e8c25155c1aab366291640cf61102e6`.

K-001: polynomial-ring source checked directly in Bremner–Hu arXiv:1112.2949v2, Introduction p.1. The constituent formulas and p=s=1 argument are correct by the given rational series.

K-002: exact certificate verifier independently executed: PASS, 44,620 covered multiset triples, 2,285 spectral orbits, four positive certificates, 2,281 Farkas exclusions. Suggested replacing the centralizer norm-minimization paragraph by diagonal-torus semistability, which gives the necessary balanced-mass condition directly. Coverage is explicitly only order-eight lifts.

K-003: whole stabilizer proof read; scalar partial centroid, rank-two configuration, congruence reduction and diagonal equations checked. Balanced free support and faithful character yield a smooth quotient point. No gap found.

K-004: whole proof read, including rank-two configuration, eight plane transformations, determinant quartic and centralizer. Quartic-elimination script independently run and matches all eight cases. Its use of Python division produces exact-valued floats for roots plus/minus one; requested conversion to SymPy integers before treating that script as an exact certificate. The symbolic hand argument remains valid.

K-005: whole proof read. The 13-component partial sum and its opposite phase are arithmetically consistent. The proof correctly withholds a global residue conclusion. P-F60/P-F65 are inherited dependencies whose whole-proof rechecks are assigned to the branch author.

K-006: whole proof read. Replacing one independent relation s=0 by 2s=0 doubles the finite character lattice; positivity and incidence independence checked algebraically. The all-n family has only a diagonal-stabilizer claim. The fixed-support argument has a finite seed check and dyadic valuation proof; full non-diagonal stabilizers remain open.

Outcome: no substantive proof gap found in the stated restricted conclusions. Exact-script correction and inherited-input verification remain explicit prerequisites for closing the corresponding certificate records.
