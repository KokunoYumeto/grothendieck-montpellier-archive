# Odd C2 status

Complete author proof D-OC2-01–04 is frozen in
`odd_c2_all_fields_section.tex`; complete root and independent peer reviews have
passed. The peer report is ODD_C2_PEER_AUDIT.md; only status text changed after the frozen mathematical audit. This excludes the transitive ordinary PSp4(q) normal-core
configuration for every odd q >= 5 in the nonselfdual-original sixfold
inducing problem, with all scalars, compatible outer operators and factor
permutations. It imposes no determinant condition and permits a larger
inducing field. It does not assert arbitrary intransitive mixtures.

The separate complete finite proof is `finite_odd_c2_section.tex`.
Its scope is the full universal cover Sp4(5), and center-positive
PSp4(7)/PSp4(9). Eight complete official tables, 485 selected rows and
37502 spectra passed the exact checker. The all-q theorem uses the full
q5 endpoint; it does not need the partial q7/q9 finite coverage as an
exhaustive theorem premise.

The published Dabbaghian-Abdoly2006 input is the complete ordinary
character table RESTRICTED TO unipotent classes. It is not the incomplete
generic full Sp4 odd table and not merely unipotent characters. All43
nontrivial row types and six nonidentity unipotent classes yield258
all-q inequalities via nonnegative rational coefficients at q=7+x.
The exact degree floors and four exceptional nonreal Weil types are
also checked.

Four indexed restriction identities conflicted with the paper's direct
Table2 rows. The initial strict test failed; an exploratory diagnostic
also printed an invalid PASS label despite reporting mismatches. Both
issues were corrected before using the result. The failure is retained
in failed_indexed_identity_crosscheck.json, the diagnostic is explicitly
labelled noncertificate, and direct Table2 rows now match all60 Sp4(5),
52 PSp4(7),74 PSp4(9) ordinary rows with one global class permutation per
table. No mathematical correction was fitted from these finite values.

New check_all_fields.py passes universal rational inequalities,
symbolic shear/Heisenberg identities, and a finite F27 descent witness
with Galois order equal to characteristic: all531441 natural vectors,
exactly81 fixed vectors, nonsingular Moore/trace pairings, and three
fixed dual weights with eight length-three orbits. This finite test does
not replace the universal written descent proof.

Exact primary URLs and retrieval boundaries are in SOURCES.md and the
bibliography. Parent handles final persistence and integration.

Written UTC: 2026-11-21T19:47:24.795761+00:00

Root integration and final hashes: research/e825_c2_exceptional_integration.json.
