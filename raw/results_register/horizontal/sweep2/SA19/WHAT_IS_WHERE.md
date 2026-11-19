# SA19: what is where

Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 2 part 2, 18 Nov 2026. Built from this folder's PLACEMENT, OBJECTS, FLAGS,
DEPENDS, CLAIM_LINKS and UNIT_LINKS (sweep 1 and sweep 2). Items are in mathematical order.

How to read the links: 'Uses' and 'Used by' come from DEPENDS.tsv, with the basis in brackets (his page: the page
refers to or builds on it; our note: a note links them; proof: the mathematics requires it). Claim links are
item-level unless a row says 'decided on the scan': 'known' means the item's subject is established in the cited
literature, not that each of his claims was checked one by one. Companion units come from
UNITS_DRAFT_20261118.tsv, which does not yet cover every folder.

SA19 is cotes 43-44 (Jacobiennes): generalized Jacobians and class field theory, duality for commutative group schemes,
local cohomology and local Jacobians, formal groups (cote 43); the letter of cote 44 (via the shared package
MPL_16+47+54+44, items 11-14 and 20, the same objects as SA18's). The register's run ANABELIAN_A1_SUCCESSOR cites cote 43
for its generalized-Jacobian statement B.68.

| # | Item | Entries | Status |
|---|---|---:|---|
| 1 | SA19-6: formal groups, Witt rings and power-series operations; ind-completion and socle  | 14 | his notes; known |
| 2 | SA19-1: generalized Jacobians and geometric class field theory: modulus, ray class group | 30 | his text; known |
| 3 | SA19-5: local cohomology and local relative Jacobians: rings attached to chains of prime | 20 | his construction |
| 4 | SA19-2: duality for commutative group schemes over local fields and over curves: the sit | 45 | his text; known in substance |
| 5 | SA19-7: classification sketches and gluing constructions for categories of curves (cote  | 7 | his sketches |
| 6 | SA19-14: duality of abelian varieties, the universal vector extension, intermediate Jacob | 23 | = SA18-14 |
| 7 | SA19-13: the Fourier transform of abelian varieties (cote 47): kernels and inversion, det | 21 | = SA18-13 |
| 8 | SA19-3: cote 47's Fourier test and the seven theorems of cote 44, read against Oda: Dieu | 21 | the notes' reading |
| 9 | SA19-11: integral models and local duality (= SA18-11) | 23 | = SA18-11 |
| 10 | SA19-12: abstract Lefschetz algebras and the standard conjectures (= SA18-12) | 20 | = SA18-12 |
| 11 | SA19-20: orbit calculations in tensor squares (cote 16, scans 25-29) (= SA18-20) | 5 | = SA18-20 |
| 12 | SA19-4: reused typescripts: homotopy of Thom complexes (Atiyah), Stiefel manifolds, a mu | 15 | reused typescripts |
| 13 | SA19-8: the dossier as a document: reading conventions, author flags, withdrawals, title | 13 | documents |

## SA19-6: formal groups, Witt rings and power-series operations; ind-completion and socle filtrations

- **Status:** his notes; known. Formal groups, Witt rings, power-series operations.
- **Where (his pages):** cote 43, scans 32-38, 40-43, 45-48, 195-208.
- **Where (our notes):** work:K43-03 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-03/out/K43-03_mathnotes.md`; work:K43-10 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-10/out/K43-10_mathnotes.md`; codex:K43-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-03/out/K43-03_notes.md`; codex:K43-10 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-10/out/K43-10_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA19-1 (proof), SA19-2 (proof).
- **His claims:** 4 entries: known Witt vectors; Dieudonné; Lazard.
- **Companion units (15):** — Exact sequences and an extension class; — A limiting construction and comparisons; — Title sheet ...

## SA19-1: generalized Jacobians and geometric class field theory: modulus, ray class groups, norms, reciprocity, ideles, S-units; the planning question on the 1983 injectivity argument

- **Status:** his text; known. Generalized Jacobians and geometric class field theory (Rosenlicht; Serre, Groupes algébriques et corps de classes, 1959).
- **Where (his pages):** cote 43, scans 8, 13, 85, 94, 102, 106, 109, 112-113, 116-117, 119-120, 128, 132-133.
- **Where (our notes):** MPL_43_094-142 (23) in `grothendieck_archive_transcription_20261110/returns/MPL_43_094-142_unzipped/MPL_43_094-142_notes.md`; work:K43-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-01/out/K43-01_mathnotes.md`; codex:K43-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-01/out/K43-01_notes.md`.
- **Across topics:** SA14 (Picard), SA16 (elliptic curves).
- **Uses:** SA19-6 (proof). **Used by:** SA19-5 (proof), SA19-2 (proof).
- **His claims:** 8 entries: proved in a run (same statements) ANABELIAN_A1_SUCCESSOR:B.68 (generalized Jacobian J_m, J_m[n] exact and étale, the Abel map on abelianized pi_1; his_places cite cote 43, scans 113, 132-133); known Rosenlicht; Serre, Groupes algébriques et corps de classes (1959).
- **Flags (2):** suspected misreading: 'Si l'inégalité est vérifiée, alors F est plat' is false as written (R06's counterexample R+k over k[[t]]: lengths 2 and 1, not flat), while equalit | a link across folders: geometric class field theory (modulus, norms, reciprocity) on the early sheets of cote 43, and the generalized-Jacobian questions of the Pro packag
- **Companion units (10):** odulus and class groups; Norms and a first reciprocity statement; Norm-one groups and units ...

## SA19-5: local cohomology and local relative Jacobians: rings attached to chains of primes, simplicial and cosimplicial coefficients, purity, double duality

- **Status:** his construction. Local cohomology and local relative Jacobians attached to chains of primes; the K43-04 Codex return for scans 49-63 is unfinished.
- **Where (his pages):** cote 43, scans 64, 72, 77, 131-132, 143-144, 274.
- **Where (our notes):** work:K43-04_2 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-04_2/out/K43-04_mathnotes.md`; work:K43-05 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-05/out/K43-05_mathnotes.md`; work:K43-06 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-06/out/K43-06_mathnotes.md`; codex:K43-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-05/out/K43-05_notes.md`; codex:K43-06 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-06/out/K43-06_notes.md`.
- **Uses:** SA19-1 (proof). **Used by:** nothing recorded.
- **His claims:** 5 entries: no proof or refutation found in the register or the topic.
- **Companion units (13):** rings attached to chains; a graded algebra and path-indexed maps; local cohomology in the Zariski setting ...

## SA19-2: duality for commutative group schemes over local fields and over curves: the site, Ext groups, Cartier-Serre-Pontryagin squares, supports, completion limits, henselization

- **Status:** his text; known in substance. Duality for commutative group schemes over local fields and over curves (Serre; Milne, Arithmetic Duality Theorems).
- **Where (his pages):** cote 43, scans 94, 96-98, 100, 104, 106-107, 114, 117, 123, 125, 128, 130, 133, 135-136, 138, 140, 145-156, 158-159, 161-165, 167-174, 176, 183.
- **Where (our notes):** MPL_43_094-142 (26) in `grothendieck_archive_transcription_20261110/returns/MPL_43_094-142_unzipped/MPL_43_094-142_notes.md`; work:K43-02_2 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-02_2/out/K43-02_mathnotes.md`; work:K43-07_2 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-07_2/out/K43-07_mathnotes.md`; work:K43-08 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-08/out/K43-08_mathnotes.md`; codex:K43-08 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-08/out/K43-08_notes.md`.
- **Across topics:** SA14 (Picard), SA18 (abelian varieties).
- **Uses:** SA19-1 (proof), SA19-6 (proof). **Used by:** nothing recorded.
- **His claims:** 24 entries: known Serre (local class field theory, proalgebraic groups); Milne, Arithmetic Duality Theorems.
- **Companion units (12):** first two lines: Ext with support; Hom computations; Ext table ...

## SA19-7: classification sketches and gluing constructions for categories of curves (cote 43, scans 178-184)

- **Status:** his sketches. Classification and gluing for categories of curves (cote 43, scans 178-).
- **Where (his pages):** cote 43, scans 178, 180-193.
- **Where (our notes):** work:K43-09 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-09/out/K43-09_mathnotes.md`; codex:K43-09 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-09/out/K43-09_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 2 entries: no proof or refutation found in the register or the topic.
- **Companion units (10):** and — classification sketches; — categories and a proposed gluing construction; — extending the construction ...

## SA19-14: duality of abelian varieties, the universal vector extension, intermediate Jacobians and the seven theorems of cote 44 (= SA18-14)

- **Status:** = SA18-14. See SA18.
- **Where (his pages):** cote 44, scans 2-9.
- **Where (our notes):** MPL_16+47+54+44 (16) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`; work:K44-01 (6) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K44-01/out/K44-01_mathnotes.md`; codex:K44-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K44-01/out/K44-01_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA19-13 (his page), SA19-11 (proof), SA19-3 (our note).
- **His claims:** 8 entries: no proof or refutation found in the register or the topic.

## SA19-13: the Fourier transform of abelian varieties (cote 47): kernels and inversion, determinant lines, Chern classes, Riemann-Roch and integrality (= SA18-13)

- **Status:** = SA18-13. See SA18 and REPORTS/cote47_scan009_chi_factor.md.
- **Where (his pages):** cote 44, scans 3-11.
- **Where (our notes):** MPL_16+47+54+44 (21) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** SA19-14 (his page). **Used by:** SA19-3 (our note).
- **His claims:** 5 entries: known since Mukai (1981).

## SA19-3: cote 47's Fourier test and the seven theorems of cote 44, read against Oda: Dieudonne modules, Frobenius and Verschiebung, Cartier duality, alpha_p subgroups (with SA18-5, SA18-13, SA18-14)

- **Status:** the notes' reading. Cote 47 and the seven theorems of cote 44 read against Oda.
- **Where (his pages):** cote 43, scans 2-9, 94, 106-107, 117-118, 128, 130, 132-133.
- **Where (our notes):** MPL_43_094-142 (21) in `grothendieck_archive_transcription_20261110/returns/MPL_43_094-142_unzipped/MPL_43_094-142_notes.md`.
- **Uses:** SA19-13 (our note), SA19-14 (our note). **Used by:** nothing recorded.
- **His claims:** 2 entries: no proof or refutation found in the register or the topic.
- **Companion units (4):** odulus and class groups; Norms and a first reciprocity statement; Norm-one groups and units ...

## SA19-11: integral models and local duality (= SA18-11)

- **Status:** = SA18-11. See SA18.
- **Where (his pages):** cote 44, scans 9-10, 14, 16, 19, 21, 23, 26, 37, 39, 41, 43, 52, 54.
- **Where (our notes):** MPL_16+47+54+44 (23) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** SA19-14 (proof). **Used by:** nothing recorded.
- **His claims:** 3 entries: no proof or refutation found in the register or the topic.

## SA19-12: abstract Lefschetz algebras and the standard conjectures (= SA18-12)

- **Status:** = SA18-12. See SA18.
- **Where (his pages):** cote 44, scans 3, 5, 14-17, 33-34, 40, 42, 44-51.
- **Where (our notes):** MPL_16+47+54+44 (20) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** nothing recorded. **Used by:** SA19-20 (his page).
- **His claims:** 2 entries: open the standard conjectures.

## SA19-20: orbit calculations in tensor squares (cote 16, scans 25-29) (= SA18-20)

- **Status:** = SA18-20. See SA18.
- **Where (his pages):** cote 44, scans 25, 27, 29.
- **Where (our notes):** MPL_16+47+54+44 (5) in `grothendieck_archive_transcription_20261110/returns/MPL_16+47+54+44_unzipped/MPL_16+47+54+44_notes.md`.
- **Uses:** SA19-12 (his page). **Used by:** nothing recorded.
- **His claims:** 0 entries: no proof or refutation found in the register or the topic.

## SA19-4: reused typescripts: homotopy of Thom complexes (Atiyah), Stiefel manifolds, a multiplicity lemma and flatness, proper pushforward, Euler characteristics, depth, soft and fine sheaves

- **Status:** reused typescripts. Atiyah on Thom complexes, Stiefel manifolds; used as paper.
- **Where (his pages):** cote 43, scans 101, 103, 105, 108, 110, 115-116, 118, 121, 126, 129, 137, 141.
- **Where (our notes):** MPL_43_094-142 (15) in `grothendieck_archive_transcription_20261110/returns/MPL_43_094-142_unzipped/MPL_43_094-142_notes.md`.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 5 entries: no proof or refutation found in the register or the topic.
- **Flags (1):** suspected misreading: 'Si l'inégalité est vérifiée, alors F est plat' is false as written (R06's counterexample R+k over k[[t]]: lengths 2 and 1, not flat), while equalit

## SA19-8: the dossier as a document: reading conventions, author flags, withdrawals, titles, sheet counts

- **Status:** documents.
- **Where (his pages):** cote 43, scans 49, 70-71, 75, 77, 98, 100-101, 103, 139, 178, 180, 184; cote 44.
- **Where (our notes):** MPL_43_094-142 (4) in `grothendieck_archive_transcription_20261110/returns/MPL_43_094-142_unzipped/MPL_43_094-142_notes.md`; codex:K43-01 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-01/out/K43-01_notes.md`; codex:K43-03 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-03/out/K43-03_notes.md`; codex:K43-04 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-04/out/K43-04_notes.md`; codex:K43-05 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-05/out/K43-05_notes.md`; codex:K43-06 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-06/out/K43-06_notes.md`; codex:K43-08 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-08/out/K43-08_notes.md`; codex:K43-09 (1) in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K43-09/out/K43-09_notes.md`; and 2 more sources.
- **Uses:** nothing recorded. **Used by:** nothing recorded.
- **His claims:** 1 entries: no proof or refutation found in the register or the topic.
- **Companion units (5):** local cohomology in the Zariski setting; the proposed local relative Jacobian; the Weil-cohomology alternative ...
