# Coverage of the misc assignment

Status: complete for the assigned Pro package of 53 indexed entries and both cote 161-6 Codex transcriptions, as of 19 November 2026. The completed cote 161-1/161-2 assignment is stored separately under `parts/groupes`.

## Source coverage

| Source | Physical lines read | Role |
|---|---:|---|
| `sources/notes/pro/MPL_68_033-056+162-1+162-6_notes.md` | 1–346 | All53 indexed note entries, individually collated to their actual transcription passages |
| Corresponding Pro `doubts.md` | 1–312 | All supplied doubts, cancellation qualifications and limits |
| `sources/texts/pro/MPL_68_033-056+162-1+162-6_transcription.tex` | 1–966 | All21 included cote68 leaves; scans33,34,36–46,48,50–56 |
| `sources/notes/codex/K161-6-01_notes.md` | 1–23 | All additional lead notes |
| `sources/texts/codex/K161-6-01_transcription.tex` | 1–712 | Entire first cote161-6 transcription, including diagrams and cancelled passages |
| `sources/notes/codex/K161-6-02_notes.md` | 1–21 | All additional lead notes |
| `sources/texts/codex/K161-6-02_transcription.tex` | 1–727 | Entire second cote161-6 transcription, including scratch calculations, diagrams and whole-block cancellations |
| `sources/texts/codex/K161-3-01_transcription.tex` | 34–49;75–90;186–222 | Additional exact endpoints read solely for the checked product-topos crosslink; full ownership belongs to spaces |

Read logs preserve file hashes and ranges. Some initial note reading preceded the logging helper; the missing early note range and final doubt range were re-read and logged during completion. These logs are evidence of source access, not automatic proof-check events. No scan files were accessed, and no second-pass files were substituted for the supplied text.

The package title mentions162-1 and162-6, but neither appears as actual archival transcription content. The supplied notes explicitly identify them as context from Hua's modernizations. Their absence is recorded in SA23-301 and345 and the isolated project-lead table. No borrower identification, document content or date is invented for them.

## Counts and merges

All 53 indexed entries have one verdict: 44 entries kept, eight merged into a true repetition, and one corrected. They yield 45 indexed-note items, SA23-301–345. Eight additional Codex subject items, SA23-1201–1208, bring the complete part to 53 items without adding verdict rows. The merges preserve every source-entry ID. Repeated scope notes, exponential recap, unrestricted-functor recap, withdrawn equivalence recap, orientation existence recap, boundary-sign recap and literary witnesses are merged only where they concern the same object or question. The three literary textual witnesses remain distinct within their merged documentary item.

The completed claim map has74 claims:51 classB,20 classC and3 classF. Page statuses are26 stated without proof,20 proof sketched,11 false as stated,15 open on the pages,1 corrected by himself later with both occurrences, and1 proved there. Some classC claims combine a correct core with a false broad wording; the proof/check field states the precise distinction. ClassB does not assert historical priority. No inaccessible exact original is marked verified.

There are 23 authorial problem records, four editorial verification tasks, 58 reading alarms, seven ranked directions, and 29 bibliographic records. The links table contains verified archival/published endpoints and separately labelled earlier-project leads; `project_links.tsv` isolates the latter. The final counts are recorded in `counts.json` and checked against the serialized records by `validate_final_parts.py`.

## Literature coverage and limits

Every one of the74 claim IDs is mapped to at least one actual, preserved query in `search_log.jsonl`. Searches covered arXiv, MathOverflow, Numdam, EGA, SGA references, author bibliographies, Grothendieck's published/retrospective texts and zbMATH-targeted queries. Exact primary sources were followed after broad searches; named-channel search alone is not presented as proof.

Strong exact matches include EGAIV4 Proposition16.8.8, Yuan's arbitrary-module Ga classification, Zhao's checked2022 Corollary2.4, Freed's orientation torsor, Knudsen–Mumford's graded lines, Lafforgue's product-topos slide47, Colin–deMesmay's graph-isotopy theorem and Yagasaki's principal restriction-bundle result. Ji2023 and Liedtke–Satriano2025 were inspected as precise near matches whose hypotheses do not settle the all-base arithmetic icosahedron assertion.

The original Ladegaillerie1984 article was not opened; its bibliographic identity and attribution were checked in later primary literature and bibliographies, and its mathematical characterization was checked through the opened later independent proof. Original1974 C.R. notes were not obtained. Some zbMATH direct access returned403. No exact original SGA product-proposition locator was inspected, so no number is invented. EGA's complete original French PDF was successfully downloaded and the named passages read. Récoltes note94 was read in an HTML transcription, not collated to ink; an incomplete PDF download was not used. These are precise source limits, not claims of historical nonexistence or unresolved mathematics.

The official Montpellier catalogue independently recognizes the literary title, but offers the alternatives Récoltes et Semailles or Réflexions mathématiques tentatively. Its catalogue dates and full-dossier page counts are not transferred to individual leaves. The visible82 on the literary verso is treated as pagination.

## Computations and preservation

`computations/check_misc.py` and its saved output contain exact finite exp/log checks, the corrected intertwiner coefficients, dual-number derivation and automorphism counterexamples, the rank3 base-change calculation, exhaustive two-element torsor checks, boundary-convention signs, all six cap-rotation images, all three marked trigonometric identities, all three omitted neighbour-cap distances, the squared-length quadratic, exact enumeration of120 icosahedron automorphisms with60 rotations, cyclotomic invariants, and ribbon-boundary/genus counterexamples. Every final assertion in the script passed. A discarded first attempt had assumed an unavailable NetworkX import; the final enumeration uses independent backtracking and SymPy. It is not represented as a formal proof assistant certificate.

`check_events.tsv` records documentary collation, mathematical re-proofs, exact-source comparison, finite computation and refutation as separate events. `refinements.json` gives explicit refined-statement IDs for false literal readings. It does not classify every source reading as a proof. The run model is GPT-6AstraPro; the effort setting was not independently exposed and is not invented.

External full texts and raw search responses are kept under `external/` for exclusion from the final deliverable archive. The concise search audit, exact URL/locator reference ledger, mathematical dossiers, scripts and saved computation outputs remain in the deliverable part. Parent integration owns final saving and checkpoints; this part performs no Library mutation.

## Additional Codex subject provenance

The final provenance pass adds eight subject items, SA23-1201–1208, for the already fully read cote 161-6 passages and claims 040–074. Their sources arrays are empty because they do not derive from indexed Pro note entries. There are therefore 53 subject items in this part, of which exactly 45 arise from the 53 indexed notes. The 53 entry-verdict rows and 74 claims are unchanged. Every claim records its source-assertion origin and distinguishes the present reconstruction in its proof field. The literal-source origin audit below separates 23 authorial problems from four editorial tasks.

## Authorial-origin audit

The final literal-source audit separates four editorial verification tasks from the authorial problem index: former MP-SA23-misc-02,08,17,27 become ED-SA23-misc-02,08,17,27. All underlying claims, proofs, searches, and reading alarms remain. The source respectively supplies a qualification, a deliberately dispensable check, three unproved assertions, and a bundle-identification margin; none is an explicit author question. There are now **23 authorial problems and four editorial tasks**. The earlier count of 27 is the historical pre-audit register, not the final problem total. The remaining source cues include actual questions, deferred proofs, canceled doubts, and unfinished displayed calculations. `problem_origin_audit.json` records each decision; `problem_editorial_redirects.json` records stable redirects.

## Literal quotation audit

All 74 claim statements now quote the supplied transcription literally. The previous English gloss remains in the separate `source_paraphrase` field. The manually selected lines and exact fragments are recorded in `quotation_audit.json`; the audit retains uncertainty/deletion macros and explicitly records when an inner sentence belongs to a canceled block. The selections were made from the already fully read passages. No statement, verdict, or mathematical classification was inferred automatically from a heading or keyword. `final_validation.json` records the successful quotation, reference, search-map, identifier, direction, and count checks for this part and Groupes.
