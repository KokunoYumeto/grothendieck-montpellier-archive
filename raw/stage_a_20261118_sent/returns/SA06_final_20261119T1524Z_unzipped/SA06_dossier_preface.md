# SA06 — Théorie des motifs, part 2

## Consolidated dossier of cotes 14 and 15

**Assessment date: 19 November 2026.** This dossier consolidates every one of the **437 entries in the supplied NOTES_INDEX.tsv**, read against its corresponding transcription, together with the assigned Codex continuations and claims encountered in those texts. The mathematical record consists of the final item, claim, problem, reading and link tables. The narrative explains their structure and the findings that most change how these folders should be used. Earlier run identities survive in source-entry IDs; all cross-package mergers and compound redirects are documented in `MERGE_MAP.json`.

The folders preserve several distinct programmes, not a finished theory of motives with one recoverable definition. Cote14 develops effectivity, a particular Albanese equivalence relation, proposed odd-cycle representatives, finite-field cycle arguments, a 1965 Lefschetz programme, Picard/Albanese correspondences, ampleness and local-cycle questions. Cote15 develops normed Deuring categories and Brandt groupoids, Weil-number and CM-lattice constructions, real motivic gerbes, and the comparison of integral, crystalline, Betti and de Rham fibre objects. Reused algebra, analysis, topology and Lie-theory sheets contain substantial mathematics but have their own provenance.

Several conclusions govern the consolidation:

1. **The chosen cycle equivalence relation changes the theorem.** The 1965 letter's quotient by algebraic equivalence is stronger than the later cohomological standard-conjecture formulation. Its literal whole-cycle Lefschetz and affine-vanishing assertions have counterexamples. Numerical semisimplicity and cohomological hard Lefschetz do not remove those counterexamples.
2. **Integral inverses are a separate problem from rational inverses.** The Albanese H¹ inverse and the Picard/top-odd inverse are distinct questions. Recent counterexamples and parity obstructions address different sides; an isogeny argument supplies denominators, not an integral cycle for free.
3. **A band, a neutralization, a torsor and a chosen isomorphism are different data.** The scalar μ_n computation in the Deuring construction does not establish the whole gerbe. Frobenius invariance of classes does not establish coherent descent. Lang's theorem does not provide a canonical comparison in an arbitrary pro-category.
4. **There are exact own-publication matches.** They include the Brauer divisor-sequence argument, several SGA3/SGA4 passages, and Grothendieck's own correction of the naive generalized-Hodge formula. These matches are supported by theorem locators and hypotheses, rather than titles alone.
5. **The modern comparisons have a precise limit.** Nori–Ayoub comparison, Nori arithmetic descent and pure semisimplicity are substantial theorems in their specified settings. They do not identify every handwritten M, establish a general motivic t-structure, prove geometric connectedness, or solve the period and effectivity questions.
6. **Mathematical refutation does not decide the ink.** Every suspicious sign, exponent, quantifier and cancellation remains a scan alarm. No manuscript reading was changed in this run.

Each of these conclusions is developed below with exact claim IDs, scoped proofs and opened sources. A correction of an earlier note is not automatically a correction of Grothendieck: it may correct the note's quantifier, its context transfer, its source boundary or a literal transcription reading.

## Corpus, authority and coordinates

The original attached archive was unpacked once. Its already unpacked inner folders were used directly. The supplied `second_pass/` directory contains no checks for this part, so no second-pass reading was presumed missing or invented. The Pro and Codex texts are witnesses, and their disagreements are recorded. There are no manuscript scans. Images inspected during literature checking are pages of published sources, not images of the Montpellier manuscripts.

| Supplied indexed package | Indexed entries | Principal material |
|---|---:|---|
| MPL_14_002-044 | 97 | Effectivity, Albanese equivalence, Tate's trick, 1965 Serre letter; reused algebra and affine geometry |
| MPL_14_087-132 | 94 | Correspondences, ampleness, local cycle groups, Lefschetz and boundedness; SGA/EGA and group-scheme fragments |
| MPL_15_034-086 | 74 | Normed Deuring categories, quaternionic examples, Brandt groupoids, positive involutions; analytic leaves |
| MPL_15_087-138 | 110 | Weil numbers, CM lattices, real gerbes, Artin–Tate comparisons; Codex generator and analytic continuations |
| MPL_15_170-194r | 62 | Fibre-functor agenda, Brauer/cohomology fragment, polarization and comparisons; reused projectivity and Lie theory |
| **Total** | **437** | Every indexed entry has exactly one final verdict row |

The assigned Codex material is K14-02/03/04/05/06/08 and B15-01/02/03, K15-01/02/08. Those leads receive item and claim coverage as needed, but no invented NOTES_INDEX rows. A package boundary is not a mathematical boundary: the letter beginning at14/044 continues on045–047; Proposition2.1 beginning at14/058 continues on059–061; the Deuring generator discussion at15/060–061 continues in B15-01 at063. Conversely, adjacent scans can be unrelated reused paper. Page numbers on a typescript, archival marginal numbers and scan numbers are kept separate.

The following table accounts for every folder in TOPIC.md while respecting the part boundary. Catalogue page totals are metadata, not counts of supplied mathematical leaves or authorial page totals.

| Cote | Catalogue topic | Catalogue pages | Treatment here |
|---:|---|---:|---|
| 10 | Catégories tensorielles | 197 | Other part; orientation only |
| 11 | Formalisme des correspondances | 57 | Other part; orientation only |
| 12 | Généralités, sous-groupes de Galois motiviques | 167 | Other part; no absent definition imported |
| 13 | Groupe de Galois motivique | 51 | Other part; orientation only |
| 14 | Cycles algébriques; Hodge, Tate, Lefschetz, Weil | 131 | Assigned Pro and Codex corpus consolidated |
| 15 | Théorie arithmétique; théorie de Galois des motifs | 227 | Assigned Pro and Codex corpus consolidated |
| 16 | Correspondences and Poincaré–Hodge algebras | 55 | Other part; particular external endpoints read for links |
| 18 | Motifs et théorie de Hodge | 61 | Other part; particular external endpoints read for links |
| 19 | Topos | 95 | Other part; orientation only |

The catalogue's 1965 date for cote15, an administrative date on reused paper, or the date of a later publication is not assigned to every surrounding leaf. Exact dates are reported where the witness supplies them. In particular, the cote14 letter is dated27 August1965; the later letter to Mumford about the box-cycle obstruction is dated20 November1968. First circulation and publication dates are separated in the reference audit.

### How to use the tables

`SA06_entries.tsv` is the closed coverage ledger: its source IDs are the supplied stable package-and-entry IDs. `SA06_items.json` merges the same objects, questions and readings while distinguishing historical assertions from ideas of earlier runs. `SA06_claims.json` records the author's claims and the explicitly labelled modern comparisons needed to judge the notes. Its `his_statement` is a brief transcription quotation or a transparent description of an incomplete clause, not a silently reconstructed theorem. Its `statement` gives the strongest formulation justified after the stated qualifications.

Line locators refer to physical, one-based lines of the specified supplied complete transcription unless an individual external page file is explicitly named. Pro fragments in the original notes sometimes used different per-page numbering; those locators are not passed off as physical lines of the combined file. The source-read audits identify the files and ranges inspected. For an external endpoint the archive, internal path and exact range are retained, with hashes where materialized.

The claim field `status_on_pages` describes the historical source and any explicit literal defect; `class` describes the literature fate. They answer different questions. A conjecture may still be open on the page but refuted later, or a cancelled argument may have a valid later theorem. ClassA means an exact match in his own subsequent publication; B an established later development; C a partial or qualified development with its remaining gap; D an unmatched development after the recorded bounded search, without a novelty inference; E standard mathematics or an independently checked standard correction; F a formulation not identifiable from the supplied words. Historical first-publication priority is not manufactured to justify classE.

`SA06_problems.json` is an index of *his open steps*, including questions later solved, refuted or corrected. Its count is not a count of currently open research conjectures. The historical formulation, a plausible modern formulation, the current source evidence and the historical reason for abandonment are separate fields. Where no source explains why work stopped, the record says so; a mathematical gap is not offered as a biographical explanation.

The proof supplements and exact programs carry the arguments that cannot fit in a short ledger cell. `CHECK_EVENTS.tsv` distinguishes actual source comparison, targeted proof checking, independent re-proof, exact computation, background use and refutation. An opened bibliography entry is not a checked proof. The ranked directions specify future tasks and their first finite steps; none is presented as newly developed research from this consolidation.

## The folders in their surviving mathematical order

The following sections follow each sequence's objects and questions before drawing cross-project comparisons. Locally authored counts and integration notes have been replaced by the final global counts at the end of this dossier.
