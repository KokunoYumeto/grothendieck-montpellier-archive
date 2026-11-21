# Independent whole audit of D-A2-01–03

**Result: PASS.** The full written proof, exact arithmetic and source scope support the stated exclusion of every normal central product of rank-three linear or unitary simple quotients with q≥3. PSL3(2) remains outside the statement.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed.
- Run: HODGE_DIVISION.
- Review: 2026-11-21, approximately 18:36–18:41 UTC.
- Whole proof: `research/a2_cores/a2_section.tex`.
- Frozen reviewed SHA-256: `023b4ca317b31a385e69a569100e34bc702c05e485d4788b8c11a399aeab0af4`.
- Canonical status-only update: `7ca6bcfa77cfe087b22a4511eadd7f51e9acf442ee895e8c2ae28e6ee3958035`; the entire canonical file was reread at 18:44 UTC and the mathematical proof remains checked.
- Bibliography hash: `332e081f19b24bc4d5af0dc7e59e4a2a55b224c2f9e4b577cc8f2bd25ab20573`.
- Full author extractor, generic checker, finite exporter and finite checker were read. The numerical outputs were independently reconstructed from the original frozen inputs.

## Complete proof

The generic estimate treats the first column correctly as a whole central class family. Its value becomes the degree only after setting the central parameter a=0; this identity was independently checked in every row. Every other class-length polynomial has strictly positive noncentral size throughout the stated range. The rectangular tables parameterize complete families, and the phase-wise triangle inequality is valid for all admissible parameter values. Coefficient positivity after q=q0+x proves the all-field inequality; it is not a finite specialization argument. The lower degree bounds 30 and 42 are conservative even when q0 itself fails the particular congruence condition.

The cover argument uses the complete exceptional multiplier list, with PSL3(4) the only exception in the q≥3 range. The generic bound passes to central quotients by lifting their representations. The previously proved commutator argument gives 3a/16 for every compatible outer normalizer; a nonidentity scalar commutator gives the stronger half-degree bound. The proof does not assume the outer group is cyclic in the generic case.

The small outer inventories are complete: C2, C2, C4 and S3 for PSL3(3), PSU3(3), PSU3(4) and PSU3(5), respectively. Every cyclic outer subgroup is represented by a retained table. Cyclic extension rescaling handles nonsplit power relations. PSL3(4) uses the separately whole-reviewed L34--1–3 isoclinism/conjugation argument and all 36 published bicyclic extensions. No central kernel is assumed characteristic.

The central-product proof is valid with arbitrary factor types and fields. The quasisimple factors and their generated matrix algebras are intrinsic, so a normalizer permutes the factors and acts by compatible intertwiners. Tensor convolution preserves a support lower bound from any nonscalar factor. The weighted-cycle argument gives at least one quarter for a nontrivial factor permutation. Every nonidentity scalar has full actual moving rank.

The actual intermediate-cover factorization forces genus zero and at least twelve effective branches if the period image has dimension nine. The universal support bound then gives e≤24; at least two factors have e≥36, and a single generic factor has degree at least30 or42. A single small factor has quarter support, forcing e≤6. At e=6 integrality gives total moving rank at least24, greater than18. Thus every case is excluded. No essential self-duality, field-equality or determinant restriction has been inserted.

## Independent exact reconstruction

`audit_a2_cores.py` and `audit_a2_cores.json` contain the independent reconstruction.

- Generic input SHA-256: `4df14adc254b80d4d7a03ea18e9449c1e05c1ba72f2ad8b713067c8f252b01a2`.
- All four immutable original Julia files were independently reparsed and matched to the retained expressions, degrees and class lengths.
- All **46 nontrivial row types and 386 noncentral coefficient inequalities** pass using the reviewer's sparse Fraction polynomial parser.
- Small input SHA-256: `3f356063efc3a3987126ddbbb6d12b0540fd71151f93eb4e83f4c3f6c26607e8`.
- All **47 tables, 1,603 selected rows, 141,024 nonscalar spectra and 34 normal core fusions** pass.
- Row selection uses exact restriction inner products, not the author's selected indices or spectrum output. Fusions are checked for identity kernel, element orders, full normal-class unions and compatibility with prime power maps. Linear characters verify the claimed cyclic quotient orders.
- Actual runtime: **4.334442 seconds**, PASS.

The Fourier routine was originally written by this reviewer and was subsequently also reused by the root's Python checker. This audit therefore uses an independently written driver and restriction selection, but does not misdescribe that shared helper as a third independent Fourier algorithm. The author's original GAP eigenvalue calculation remains a separate arithmetic implementation.

## Data provenance finding

An initial reviewer assertion that every finite table had ATLAS provenance failed on `(4^2x3).L3(4)`: its actual source string is construction by `PossibleCharacterTablesOfTypeV4G`. The other 46 tables explicitly identify ATLAS provenance. This was a source-label finding, not a numerical counterexample. The author added the accurate provenance paragraph before this frozen review.

The constructed universal table is redundant. The complete eight cyclic-center core tables already cover every projective irreducible representation by L34--3 and independently give minimum degree6. The proof does not depend on a nonexistent stored universal-to-quotient fusion. The universal table is retained only as an auxiliary consistency check.

## Primary source scope

Simpson–Frame, Canadian Journal of Mathematics25(1973),486–494, DOI10.4153/CJM-1973-049-7, was freshly opened in the original publisher PDF. The complete invoked construction text in §§1–2 (pp486–487,489), the whole §4 restriction argument (pp490–491), §5 (p491), and §7 notation (p493) were read. Tables1a and1b on pp487–488 supply the complete special-linear/special-unitary class and character families; Table2 onp492 supplies the projective table. The unitary notation SU(3,q²) uses the same prime-power parameter q as modern SU3(q). The exact primary URL is:

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0DA5E003E1F9E8B176D638EFD3080556/S0008414X00050513a.pdf/the-character-tables-for-sl3-q-su3-q2-psl3-q-psu3-q2.pdf

The official complete-table inventory was freshly read at https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/ . It distinguishes the four full ordinary tables from unipotent-only tables. The original retained commit `87231738271ed548f62e7f1c98ff2bbfc1ed30d3` explicitly records the corrected parameter ranges, central characters, mixed-torus phase and unitary class representative. Those correction notes were read directly in all affected source files. The theorem uses this corrected official implementation and does not claim that the uncorrected printed entries were certified. Geck1990 §3 is the cited correction source; its full original article was not newly read in this audit, matching the bibliography's explicit limitation.

HHM Chapter5 Table1 and the complete preceding paragraph on numberedp35 were freshly read in the retained author text. They list PSL3(4) and SL3(2) as the exceptional multipliers in these two families. Thus only PSL3(4) needs exceptional-cover handling in the stated q≥3 domain. The separate L34 source and new whole-proof checks are recorded in `l34_normalizers/README.md` and the sibling's independent report.

No new classification of character tables or Schur multipliers is claimed. The new results are the exact all-parameter inequalities, complete normalizer application, and actual period-rank contradiction.
