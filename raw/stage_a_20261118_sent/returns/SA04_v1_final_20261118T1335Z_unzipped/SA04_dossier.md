# SA04 dossier — Théorie des motifs (part 1 of 3)

## Status

**Work in progress; not a completed research dossier.** This bundle preserves all 380 indexed note entries and attaches available transcription excerpts for the scans listed in the index. It does not claim to have completed the required mathematical adjudication, cross-package deduplication, claims audit, state-of-the-art search, or bibliography verification.

## Scope and source inventory

The topic is Grothendieck's *Théorie des motifs*, archive cotes 11 and 12. The supplied topic map identifies cote 11 as *Formalisme des correspondances* (57 pages) and cote 12 as *Généralités (sous-groupes de Galois motiviques)* (167 pages). This run contains the following five Pro note packages:

- MPL_11_002-042: 82 indexed entries
- MPL_11_043-058+56: 107 indexed entries
- MPL_12_002-050: 9 indexed entries
- MPL_12_051-098: 79 indexed entries
- MPL_12_099-149: 103 indexed entries

There are **380 indexed entries** in total. The packet also contains two Codex note files (B12-01 and B12-02), five Pro transcriptions, and two Codex transcriptions. The topic map lists other related archive folders (cotes 10, 13, 14, 15, 16, 18, 19), but they are outside this part's transcribed scope.

## Stage 1 — entry preservation

All 380 rows of `NOTES_INDEX.tsv` are represented in `SA04_entries.tsv`, and each corresponding note block is preserved in `SA04_items.json` under a provisional stable item id. Where the index supplies scan numbers, the associated transcription page excerpt is included. The current mapping is deliberately one-to-one and **provisional**: the required cross-package merge, mathematical restatement, exact line locators, and agree/overstate/understate/misread verdicts have not been completed. Consequently all entry verdicts are marked `pending`; no entry is silently treated as adjudicated.

## Codex transcription leads (not part of the 380 indexed Pro entries)

The Codex notes explicitly flag several page-level qualifications. These are leads for later claim/problem extraction, not independently checked results:

- **B12-01:** scan 68 asks whether an algebra \(B\) is integral under the stated local hypotheses and says the general answer is unknown while recording affirmative special cases; scan 69 prescribes a duality verification and requests further development of cup-products in “absolute” cohomology; scan 85 asks whether a schematic-dominance property is preserved under every base change and states a locally noetherian case; scans 97–98 qualify parts of the weight/level discussion as conjectural or heuristic, with unresolved dependence on Weil conjectures and resolution of singularities in arbitrary characteristic.
- **B12-02:** scan 123 states Deligne's theorem conditionally modulo a “Lefschetz theorem” for fibre cohomology, with the word itself uncertain in the transcription; scan 134 records “référence introuvable !!” after the equality \(\cos(\pi/3)=1/2\). Scan 121 describes a problem historically as having remained open in the IHES seminar, but not as an unproved claim after the solution discussed there.

These page-level leads are quoted from the Codex note files. The corresponding page text still needs to be inspected in the transcription and the mathematical claims need separate checks.

## Stage 2 — claims map

Not completed. `SA04_claims.json` is an empty schema-valid list, not evidence that the manuscripts contain no claims. The claims must be extracted from the notes and transcriptions, then checked individually, including any computations and the exact hypotheses.

## Stage 3 — open problems

Not completed. `SA04_problems.json` is an empty schema-valid list. The preliminary directions file records only research leads, not a completed problem index or state-of-the-art review.

## Stage 4 — readings to check

No manuscript scans were supplied. `SA04_readings.tsv` therefore contains only its header. Mathematical suspicion cannot determine the ink; no transcription correction is made.

## Stage 5 — links

Not completed. `SA04_links.tsv` contains only its header. Cross-folder and published-work links require exact locators and verification.

## Stage 6 — research directions

`SA04_directions.md` contains five preliminary leads inferred from the topic map and supplied note headings. They are not ranked by novelty or tractability and none is developed.

## Literature and check events

No external work has yet been independently opened and verified; `SA04_references.bib` records this explicitly. `CHECK_EVENTS.tsv` contains its header only because reading the notes is not a check of the underlying mathematical statements. `progress.log` records the work performed in UTC.

## Counts

- Indexed note entries: **380**
- Provisional preserved items: **380**
- Entry verdicts: **380 pending**
- Adjudicated claims: **0**
- Indexed open problems: **0**
- Scan readings decided: **0** (no scans supplied)
- Verified external references: **0**
- Preliminary research directions: **5**

This bundle is a preservation and triage checkpoint, not the requested final `SA04.zip` research result. The remaining work is substantial and should not be represented as complete.
