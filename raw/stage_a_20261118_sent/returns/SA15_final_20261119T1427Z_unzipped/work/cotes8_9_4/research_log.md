# Research log: cotes 8 (79–81), 9, 4

Run: SA15-20261119/cotes8_9_4. Reader: GPT-6 Astra Pro; effort setting not exposed.

The source package also contains cote 100. TOPIC.md excludes it from SA15, so its notes are inventoried separately and are not assigned substantive SA15 verdicts or claim status.

The supplied NOTES_INDEX.tsv has no rows for this package: its notes use `##` rather than `###` headings. Supplementary IDs retain the package name and use `##<ordinal>` to avoid inventing indexed source IDs.

Initial reading commands (before the reader utility was saved): inventory of `\\cotefile`/`\\scanpage` line markers; `sed -n '1,428p'` of the Pro transcription; `sed -n '1,290p'` of its notes. The combined tool output truncated, so the affected note spans and manuscript tail were reread in numbered, saved spans.

All locators refer to lines of the supplied diplomatic transcription, not lines measured on the absent scans. No proposed reading changes are adopted.

## Completion of the source census

All 148 in-scope `##` entries were read and given individual decisions in `make_items.py`; their assignment is not inferred from headings or keywords. There are 41 consolidated items. The other 201 headings belong to cote 100 and are explicitly inventoried as outside TOPIC. Only its two Stage 5 endpoints, scans 3 and 37, were substantively read. Its additional headings are not judged as Cristaux claims.

All cote 8:79–81, cote 9:1–29 and cote 4:1–12 text was read, including covers, stationery, canceled drafts and the endings of continuations. All four Codex note files and all four corresponding transcriptions were compared. Codex supplies independent textual corroboration, never an ink verdict. The complete in-scope doubts inventory was read. The additional root-package endpoint cote 8:78 was read in full for the direct continuation.

The claim map contains 82 claims and the problem index 26 problems. Questions resolved within the pages and withdrawn questions remain indexed with those statuses. There are 22 opened references; metadata-only openings are explicitly distinguished from mathematical text readings in `reference_evidence.json`. No original proof is claimed read merely because a later author cites it.

## Search record and exact-claim families

The four `outputs/search_sessions_*.json` files contain all 40 retrieval requests, including exact search strings, attempted opens, finds and screenshot attempts, with returned titles, URLs, source identifiers and available error metadata. These are a search history, not a bibliography. Full third-party excerpts were removed after extracting the metadata; the retained mathematical summaries are original concise paraphrases. Sources are cited by verified bibliographic key and exact locator in `reference_evidence.json`.

Every claim has a family in `claim_search_families.json`. The following records the common search work applied to each precise group of claims. Sharing a family means sharing the directly relevant literature investigation, not claiming that a broad subject match settles each member.

| Family | Claims and exact issue | Search sessions | Outcome and boundary |
|---|---|---|---|
| F01 | Co-Lie tensor/Tor, Postnikov class, representation lifting, low-degree comparison | S001–S008, S011–S012, S021–S022, S026, S033, S037 | Opened Bergh–Rydh B.4, Illusie obstruction exposition, Singla and Ginosar metadata; MathOverflow supplied a backwards lead to Sah/Ginosar. arXiv, zbMATH, Numdam and MathOverflow domain searches were attempted in S026. The (2,2) exception is independently certified. “Every M” in the H² comparison is restricted to the stated locally constant/covering hypotheses. |
| F02 | Reduced Dieudonné module, universal extension, F/V duality and truncated coefficient pairing | S003–S004, S008, S011–S012, S022, S027, S040 | Opened Oda and Berthelot–Messing; followed historical discussion in Illusie. S027 queried all requested discovery channels. The standard duality is established, while the finite index and Pro/Codex cancellation dispute are not identifiable uniquely. Nontrivial coefficient twists were separately computed. |
| F03 | Canceled torsor/chain-homotopy Gauss–Manin draft | S027, S011–S012, S032 | Numdam/Oda/Gauss–Manin search and Illusie’s Katz–Oda history identify the later direct construction. They do not certify the exact canceled lemma or repair its missing coherence data. |
| F04 | Virtual good reduction, equivariant K₀, finite inertia trace, Brauer recovery and elliptic test | S002–S004, S013, S021, S028, S030–S032, S038 | Opened the Serre–Tate scan but could not read its image-only body; opened Dembélé–Freitas–Voight and Illusie. S028 attempted the named discovery channels. No exact historical Tate example or full filtration-independent K₀ theorem was located. The independent elliptic counterexample is clearly separated from historical attribution. The Zp-valued trace has a direct commuting-Frobenius proof. |
| F05 | Ordinary full stratification, Frobenius descent, étale sheaves, connected–étale extensions | S012, S018–S020, S029, S032–S034, S040 | Opened Katz’s Serre–Tate local moduli and Caraiani’s Hasse discussion; followed the bibliography to the ordinary-crystals volume. S029 queried arXiv, MathOverflow, zbMATH and Numdam. Local formal extension data are settled; an exact necessity theorem for the full universal-deformation stratification was not found. |
| F06 | Polarization, Hasse line, positive determinant normalization, variance, biduality and reduction | S001, S016, S029, S032–S037 | Repeated exact determinant/Tate/polarization/Rosati searches, then opened Milne’s standard degree and Rosati results. They validate ingredients but do not identify the exact normalized unpolarized determinant as a named later theorem. The manuscript’s own scan 27 resolves its sign doubt; biduality and comparison remain separate checks. |
| F07 | Crystalline universal coefficients, duality, integral Lefschetz, torsion sequence, Serre example and lift comparison | S001–S002, S005–S008, S012–S013, S018–S025, S033–S036, S038 | Opened BMS, Illusie’s Bourbaki exposition and the 2012 Berthelot–Esnault–Rülling paper; followed Numdam bibliography backwards to Berthelot 1973 and Serre 1958. Direct zbMATH opens returned 403. The sufficiently ample theorem is verified; arbitrary-degree saturation is not inferred. The extra torsion term is independently derived, without claiming a new geometric counterexample. |
| F08 | Stable Frobenius, relative local systems, augmentation, unit roots and injectivity of v | S009–S020, S023–S025, S031, S033–S039 | Opened SGA 7 II XXII, Koblitz, and Illusie’s exact Katz–Messing report. Stable augmentation and trace congruence have precise matches. Relative base-change and constant-kernel hypotheses remain explicit. General all-degree v-injectivity is not certified by the special cases. |
| F09 | Generic positivity, rank growth and motivic level | S009–S020, S023–S025, S038–S039 | SGA 7 II XXI Theorem 1.4 exactly proves the large-degree positivity question. Koblitz Theorem 1’s prose leading-term statement plus Lemma 4 establishes unbounded generic stable rank, even though its displayed defect formula is missing from OCR. Coniveau divisibility is not promoted to the general converse motivic equivalence. |
| F10 | Full unit-F monodromy, every-open point-count consequences and n=1 boundary | S001–S002, S005–S006, S009–S010, S013–S019, S023, S029, S038–S039 | Opened Achter–Pries Proposition 4.8 and Stienstra–van der Put–van der Marel. Full monodromy on moduli of curves is not the fixed-X hypersurface theorem. No exact all-X result was located. Trace surjectivity and the n=1 permutation countertest are elementary independent checks. |

### Retrieval limits that affect conclusions

- The Ginosar publisher page returned 403; the institutional record was opened. The complete exception list is read in Singla, not claimed to have been read in the original Sah or Ginosar proof.
- Direct zbMATH records 0436.14007 (Illusie) and 0268.14007 (Berthelot) returned 403. Domain searches were still attempted and are recorded; no inaccessible review is cited as read.
- The large de Rham–Witt PDF, the full SGA 7 II PDF and the Mexico volume exceeded the web reader’s size limit. Smaller author chapter PDFs supplied both SGA 7 chapters. The 2012 primary paper supplied the Serre construction’s later use, with the original-read limitation retained.
- The Serre–Tate and Katz–Messing PDFs yielded image-only body pages. Screenshot requests returned text placeholders without inspectable image content. Their original proofs are not marked read. The Katz–Messing statement was checked in Illusie’s contemporaneous §2.5, with its smooth-projective scope.
- Koblitz’s numerical defect displays are missing from OCR. A later targeted reread found an explicit prose leading-term statement and the generic-transfer lemma, sufficient for the manuscript’s unboundedness claim. No stronger unread defect estimate is reported.
- The attempted arXiv 2609.06554 opening returned a disabled/error response. It is not used as a verified source.

These limits do not convert “not located under the recorded search” into “open in mathematics” or “never developed.” Class C is used for partly matched formulations with an explicit remaining scope issue; class F is reserved for claims that the textual witnesses do not identify uniquely. There are no unsought claim fates.

## Check discipline and files

`check_events.tsv` records source-fidelity checks separately from independent proofs, targeted proof audits, finite computations and statements merely carried as background. All original calculation scripts and their JSON/text outputs are present. Finite test ranges are never called general proofs. Exact algebraic proofs in `proofs.md` provide the quantified arguments where available.

The independent elliptic counterexample, the trace-integrality proof and the extra preceding-degree torsion derivation were not supplied as examples by the earlier notes; they are labeled as checks made in this run. No proposed Stage 6 direction is developed beyond what is necessary to check or refute an existing manuscript claim.

There are no explicit links to La Longue Marche, Les Dérivateurs, S6 or named external research runs in the in-scope notes of this package. No such project link is invented. The two cote 100 comparisons are retained solely as earlier-run structural leads with both endpoints read, outside the Cristaux claims census. The absent section 7 reference is recorded but is not entered as a checked two-endpoint link.

The plain `his_statement` fields give a concise report of the displayed statement; short literal French phrases are retained where available. They do not insert a missing manuscript proof. Exact source wording and cancellation status remain in the cited diplomatic line ranges.

Inspection commands also used `rg`, `sed`, `nl`, `cat`, and one inline Python JSON-key/search-request inspection. These are read-only source/output inspections, not undocumented mathematical computations. The manually authored serializers preserve judgments and locators; they do not infer verdicts from headings.

## Final editorial and cross-audit verification

`code/final_polish_and_validate.py` rewrites the link and reading prose in full, expands all linked source IDs, points the cote 8:78 continuation to root item `P78-I060`, and checks all joins and source assignments. Its report is `outputs/final_validation.json`. It also sharpens P894-C024 to refer to the order of the automorphism group and P894-C031 to reject the universal perfect-field quantifier. These edits change no diplomatic transcription. Repeated source-log rows introduced by serializer reruns were deduplicated; real distinct readings remain recorded.

`root_cross_events.tsv` records 38 independent targeted proof checks of the root package, with the exact `P78-C*` IDs and explicit boundaries on each check. The review covers all eighteen sections of `proof_audit_root.md`, including its revised completion, open-inertia and Borel arguments. Cited classification, comparison and invariant-field theorems are not relabeled as independent re-proofs. `outputs/root_cross_audit.json` records the reviewed file hash.

`project_leads.tsv` is deliberately empty apart from its header. `project_leads_audit.md` explains the verified absence of named context-project endpoints in the in-scope notes. The two cote 100 references remain checked folder links, not invented project links.
