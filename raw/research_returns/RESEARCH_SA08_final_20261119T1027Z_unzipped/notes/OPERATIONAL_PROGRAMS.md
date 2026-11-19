### Scope and evidence conventions

Inventory snapshot: 2026-11-19T10:27:13.986175+00:00. This records all 51 operational programs in `code/`, including the inventory writer, separately from the 36 mathematical programs described in the computation record (including the final C35 certificate). Every program filename below was checked against its saved source. Generated `__pycache__/*.pyc` files are not additional programs. No download, research computation, registry writer, typesetter, approval or packaging command was executed to prepare this inventory.

All paths below are relative to `SA08_work/` unless prefixed by `../`; programs are under `code/`. Counts labelled **source payload** describe the saved program, not a new execution. Durations are copied from existing receipts; **not recorded** means no duration for that operation was found in its preserved output. File timestamps, UTC review/creation stamps and download timeout settings are never treated as runtimes. Separate or concurrent request durations are not added and called wall time. Source-download success does not establish that a theorem was opened or applicable; those scopes remain in the bibliography and source notes. Fetched third-party full texts and archive images remain excluded from the distribution package; their receipts are included.

### Source acquisition and inspection

| Program | Actual purpose | Output / receipt references | Recorded counts and runtime |
|---|---|---|---|
| `fetch_sources.py` | Fetch explicitly supplied name=URL pairs, save the response bytes, and print one JSON success/failure receipt per request. It does not identify the publication or inspect its mathematics. | sources/<supplied name>; logs/A_source_fetch_01.jsonl through A_source_fetch_06.jsonl and the other named fetch receipts in the request table below. | The complete surviving request table below records byte counts and per-request seconds; these are separate requests, not a total elapsed runtime. |
| `unpack_arxiv_sources.py` | Extract previously downloaded arXiv tar/gzip source files into confined source directories, with path-traversal checks, and list extracted files. | sources/<archive stem>/; logs/A_new_filtered_sources_unpack.jsonl; logs/source_unpack_magidson2024.jsonl. | Zakharov: 6 files, 0.003355455002747476 s; Antieau: 4 files, 0.002945379001175752 s; Magidson: 5 files, 0.01585413300199434 s. These are extraction times, not download times. |
| `extract_scans.py` | Print selected scan-number blocks from the attached transcription files, retaining original filename and one-based line number for each line. | Standard output; original inputs are input/RESEARCH_SA08_transcriptions/transcriptions/*transcription.tex. Exact locators were copied into proof/source notes. | A separate execution count and runtime are not recorded. |
| `B_archive_fetch.py` | Fetch the Montpellier archive catalogue, save its HTML, and print contexts containing 136 plus script URLs for the documentary dating check. | sources/B_archive_catalogue.html; logs/B_archive_fetch.txt. | The final JSON line records 244048 bytes and 5.58734708799966 s. Catalogue retrieval is not evidence dating the mathematical leaves. |
| `B_download.py` | Fetch May 1970, Steenrod–Epstein 1962 and the Pursuing Stacks arXiv source bundle, preserving response type, hash and download receipts. | sources/B_may1970.pdf, B_steenrod_epstein1962.pdf, B_pursuing_stacks_source.tar; logs/B_source_downloads.json. | Three successful request records; individual bytes and durations appear in the source-receipt table below. |
| `B_download_additional.py` | Concurrently fetch Cenkl–Porter 1982 and Mandell 2001, then extract PDF text with pdftotext. | sources/B_cenkl_porter1982.pdf/.txt and B_mandell2001.pdf/.txt; logs/B_additional_downloads.json. | Two successful records: 420657 bytes / 8.993040687997564 s and 454285 bytes / 9.821948320000956 s. Durations include text extraction; no overall concurrent wall time is recorded. |
| `B_fetch_c3_source.py` | Fetch a specified arXiv source archive, extract only TeX/BibTeX/text files with confined paths, and preserve hash, extracted filenames and retrieval status. | sources/B_quillen_pd.tar and B_quillen_pd_source/; sources/B_caradot_lin2025.tar and B_caradot_lin2025_source/; logs/B_quillen_pd_fetch.json and B_caradot_lin2025_fetch.json. | Dokas–Frankland–Ikonicoff: 155324 bytes, 1 extracted text file, 6.759984792999603 s. Caradot–Lin v1: 84394 bytes, 1 extracted text file, 6.537299870000425 s. The initial receipt says scope not yet read; subsequent reading is separately documented. |
| `B_fetch_cote136.py` | Attempt a streamed full download of original cote 136, with SHA-256 accumulation and a completion receipt only after end of stream. | Attempted sources/B_original_cote136.pdf, subsequently retained as B_original_cote136.partial by the range reader; logs/B_cote136_fetch.txt. The intended logs/B_cote136_receipt.json is absent. | No completed-fetch count or runtime is recorded; the stdout file is empty. This is not recorded as a successful full-PDF acquisition. Selected original scans were obtained separately. |
| `B_fetch_literature.py` | Fetch an explicitly supplied primary-source URL, save a SHA-256 receipt, and run pdftotext for PDF responses. | sources/B_<requested publication>.pdf/.txt; individual logs/B_*_fetch.json receipts listed below. | Nine surviving individual request receipts are listed below. One was a wrong article reached through an incorrect URL and was relabelled by B_label_misfetch.py; it is not counted as an opened Cenkl–Porter source. |
| `B_fetch_pdf_ranges.py` | Read the remote cote 136 PDF through cached HTTP byte ranges; traverse its page tree to copy only specified original scans into small PDFs. | sources/B_range_cache/; sources/B_cote136_scans142_145.pdf, B_cote136_scansomega.pdf, B_cote136_scans182.pdf; logs/B_cote136_ranges*.json and .txt. | Completed runs: scans 142–145, 7 new ranges / 1835008 bytes / 59.75233911300165 s; scans 174,176,178,180, 10 new ranges / 2621440 bytes / 105.43540739499804 s; scan 182, 2 new ranges / 524288 bytes / 18.868229032999807 s. Earlier interrupted/retried transcripts retain individual range times but no completed-run runtime; see the range table below. |
| `B_fetch_relative_literature.py` | Fetch or reuse five selected references for the local relative-repair search, verify PDF headers, extract text, and record blocked requests and cache hits distinctly. | sources/B_menichi2001_fiber.pdf/.txt, B_scheerer_tanre1991_tame.pdf/.txt, B_scott2005_hopf.pdf/.txt, B_hanke2009_stable_rank.pdf/.txt; logs/B_relative_literature_fetch.json. | Latest receipt: 3 already-downloaded checks, 1 new download and 1 HTTP 403 failure (Anick). Exact per-entry durations below. Cache-check durations are not original download times; the latter are not preserved in this overwritten receipt. |
| `B_fetch_serre1953.py` | Fetch the opened Serre 1953 primary finiteness source, verify the PDF signature, extract text and preserve the exact opened scope in the receipt. | sources/B_serre1953_classes.pdf/.txt; logs/B_serre1953_fetch.json. | 767254 bytes; 10.171391184998356 s, including text extraction. Chapter I §6.1 and Chapter II §6 Proposition 8 are the recorded scope. |
| `B_inspect_sources.py` | Safely unpack the downloaded Pursuing Stacks bundle, print its member inventory, and extract text from the downloaded May and Steenrod–Epstein PDFs. | sources/B_pursuing_stacks/; sources/B_may1970.txt and B_steenrod_epstein1962.txt; logs/B_source_inventory.txt. | The saved inventory lists 22 extracted files. Runtime is not recorded. |
| `B_label_misfetch.py` | Rename the wrongly requested 1984 PDF/text as Butler–Erbe and annotate its existing download receipt with the actual first-page identification and exclusion from the SA08 argument. | sources/B_butler_erbe1984_misfetch.pdf/.txt; amended logs/B_cenkl_porter1984_cubical_fetch.json. | One mistaken source identity corrected; the script enumerates two file suffixes. Its correction runtime is not recorded. The 9.128421449997404 s in the receipt belongs to the earlier download, not relabelling. |
| `B_ocr_primary.py` | Render a requested PDF page range at 120 dpi and OCR the rendered pages concurrently with Tesseract, solely to locate passages for subsequent image checking. | notes/B_scan_images/B_may1970_ocr-*.png; sources/B_may1970_ocr_8_18.txt; logs/B_may1970_ocr_8_18.json. | PDF pages 8–18 inclusive (11 pages); 87.89117174000057 s. The OCR output is not an independent mathematical verification. |
| `C_fetch_manuscript.py` | Fetch exact cote 136 scans through HTTP ranges, reading the existing B cache without modifying it and writing its own C cache and page subsets. | sources/C_range_cache/; sources/C_cote136_half_algebra.pdf and C_cote136_uniqueness.pdf; logs/C_cote136_half_algebra.json and C_cote136_uniqueness.json. | Scans 348,350,352: 1572864 new bytes, 57.844757042999845 s. Scans 100,117,119,121: 2621440 new bytes, 93.25417175099938 s. Receipts include the individual range calls. |
| `C_fetch_more_sources.py` | Concurrently fetch and unpack the exact arXiv sources for Berger–Fresse, Guillén–Navarro–Pascual–Roig and Porter–Suciu; preserve an archive or gzip fallback and a retrieval table. | sources/C_berger_fresse*, C_monoidal_models*, C_porter_suciu*; logs/C_more_sources_fetch.tsv. | Three OK rows: 135660 bytes / 7.705 s, 102952 bytes / 7.643 s, 155015 bytes / 7.412 s. The script's byte field can refer to decompressed fallback text; it is not uniformly a wire-byte measure. Overall concurrent runtime is not recorded. |
| `C_fetch_shuffle_source.py` | Fetch the primary Melançon–Reutenauer shuffle article, verify its PDF signature and preserve the selected §4 locator and hash. | sources/C_melancon_reutenauer1989.pdf; logs/C_shuffle_source_fetch.json. | 949029 bytes; 7.429747215999669 s; printed pp. 589–590 / PDF pp. 13–14 recorded. |
| `C_fetch_sources.py` | Fetch the Christensen–Holm arXiv source and author PDF, recording separate success/failure rows. | sources/C_christensen_holm_source.tar and C_christensen_holm.pdf; logs/C_source_fetch.tsv. | Two successes: 19411 bytes / 9.723 s and 450583 bytes / 5.645 s. |
| `C_read_cartan.py` | Render the 12 article pages of the exact Cartan 1976 PDF at a 2000-pixel maximum dimension and OCR them with Tesseract English. | logs/C_cartan_pages/p-*.png; sources/C_cartan1976_ocr.txt; logs/C_cartan_ocr_run.txt. | 12 pages; 17.639 s. The receipt expressly requires image checking for mathematical formulas. |

### Registers and documentation

| Program | Actual purpose | Output / receipt references | Recorded counts and runtime |
|---|---|---|---|
| `B_register_results.py` | Create the initial B-01–B-13 statement register and its initial independent-check events, including references back to the supplied claims. | notes/B_results.csv; notes/B_CHECK_EVENTS.tsv; logs/B_register_results.txt. | The saved stdout records 13 initial statement rows. Runtime is not recorded. This historical script overwrites those registers; it must not be used to regenerate their later appended state. |
| `B_record_followup_checks.py` | Idempotently append the later B source inspections and independent A-006–A-025 audits without repeating an existing event identifier. | notes/B_CHECK_EVENTS.tsv; referenced audit notes include B_A006_audit.md and B_A017_audit.md. | The source enumerates 13 intended event identifiers. A separate insertion-count receipt and runtime are not recorded; the source count is not a claim that all 13 were newly inserted on every execution. |
| `B_record_c3.py` | Idempotently add the B-owned C3 auxiliary results and exact proof, source and independent-audit events. The header retains the earlier two-result description, but the actual payload is broader. | notes/B_results.csv; notes/B_CHECK_EVENTS.tsv; covers C14, C15, C19, C20, C22, C23, C25, C27, C33 and C34 plus subsequent audits. | Current source payload: 10 result rows and 32 event specifications. No per-run insertion count or runtime is recorded. Existing rows/events are checked before appending. |
| `B_build_corrections.py` | Build the B correction register from exact attached-file/line locators and find proof paragraph locators in the B TeX fragments. | notes/B_CORRECTIONS.tsv; reads sections/B_automorphisms.tex, B_abstract_completion.tex and B_dating.tex. | 15 correction rows in the source payload and saved register; runtime is not recorded. |
| `B_format_audit_note.py` | Repair inline mathematical delimiters in B_A017_audit.md while preserving display-math blocks; this is a formatting utility. | notes/B_A017_audit.md, edited in place. | Number of replacements and runtime are not recorded. |
| `C_record_B605.py` | Append the finite-rank half-algebra classification statement, its proof-check event and the corresponding findings summary. | notes/C_results.csv; notes/C_CHECK_EVENTS.tsv; notes/C_findings.md. | Source payload: 1 result row and 1 check-event row, plus prose. A separate execution count and runtime are not recorded. |
| `C_record_C11.py` | Record the Tor obstruction proof and cite the previously executed binomial-gcd certificate; it does not rerun the certificate. | notes/C_CHECK_EVENTS.tsv; references logs/C_finite_obstructions.txt. | Source payload: 2 event rows. Runtime of this recorder is not recorded; the mathematical program's quoted runtime belongs to that separate computation. |
| `C_record_b6_sources.py` | Append B603/B604 results, five source/proof events, one exact-input correction and the source-search narrative for cup-i, Cartan and integral uniqueness leads. | notes/C_results.csv; notes/C_CHECK_EVENTS.tsv; notes/C_CORRECTIONS.tsv; notes/C_source_searches.md. | Source payload: 2 result rows, 5 events and 1 correction. Recorder runtime is not recorded. Download/OCR times quoted in the prose are credited to their own scripts above. |
| `C_record_rechecks.py` | Append the refined scan-360 comparison, finite-certificate rerun citation, independent C09 audit and failed finite-prime reduction record. | notes/C_CHECK_EVENTS.tsv. | Source payload: 4 event rows. Recorder runtime is not recorded. |
| `C_update_proofs.py` | Replace the earlier rational C07 argument with the proved all-nonzero-ring strict-equalization counterexample, and synchronize its findings note. | sections/C_part.tex; notes/C_findings.md. | One named theorem/proof and its matching note are replaced by the source. Separate edit counts and runtime are not recorded. It is a historical proof-integration script, not a new proof test. |
| `D_make_records.py` | Rebuild D-agent statement/event registers from already completed proofs and saved finite checks; include independent B/A audits and correction events. | logs/D_results.csv; logs/D_CHECK_EVENTS.tsv. | Saved registers have 23 statement rows and 45 event rows. Runtime is not recorded. The source expressly says it does not assert new checks. |
| `register_A023.py` | Write the additional numerical-tail pairing result and its proof, independent audit and finite-certificate references. | notes/A_additional_results.csv; notes/A_additional_CHECK_EVENTS.tsv. | Source payload: 1 result and 3 event rows. Runtime is not recorded. |
| `register_A025.py` | Write the rational-specialization result and record independent proof checks for A-025 and the supplied earlier claim identifier. | notes/A_specialization_results.csv; notes/A_specialization_CHECK_EVENTS.tsv. | Source payload: 1 result and 4 event rows. Runtime is not recorded. |
| `register_A_corrections.py` | Write exact attached-input locators and proved corrections for Part A, the shared shadow claims and the relevant leads. | notes/A_CORRECTIONS.tsv. | 23 correction rows in the source payload and saved register; runtime is not recorded. |
| `consolidate_corrections.py` | Normalize and merge the four independently maintained correction schemas without modifying the attached inputs; emit machine-readable and Markdown tables. | RESEARCH_SA08_corrections.tsv; notes/CORRECTIONS_table.md; logs/corrections_merge_03.json. | The saved merge receipt records 75 corrections from A, B, C and D registers; runtime is not recorded. |
| `update_registers.py` | Merge the root A results with all maintained result/event fragments; optionally concatenate bibliography fragments or preserve an already approved bibliography. | RESEARCH_SA08_results.csv; CHECK_EVENTS.tsv; RESEARCH_SA08_references.bib unless --preserve-bibliography; logs/register_update*.json and registers_01.json. | logs/register_update_39_final_checks.json records 118 statements, 352 events and 4 bibliography fragments, with bibliography_preserved=true. Runtime is not recorded; its UTC stamp is not a duration. |
| `audit_registers.py` | Compare canonical statement IDs with numbered labels in the paper's actually included fragments; report duplicate IDs, duplicate labels and either direction of unmatched entries. | logs/register_audit.json and the preserved register_audit_*.json snapshots. | logs/register_audit_39_final_checks.json records 118 rows and 118 labels, with all four discrepancy lists empty. Runtime is not recorded. |

### Report and formal-review maintenance

| Program | Actual purpose | Output / receipt references | Recorded counts and runtime |
|---|---|---|---|
| `update_report_03.py` | Refresh the checkpoint-three report from approved PDF metrics, correction tables and the then-current mathematical gate descriptions. | RESEARCH_SA08_report.md; logs/report_update_03.json. | Receipt: 88 statements, 68 approved PDF pages, 21 reviewed pages. Runtime is not recorded. |
| `update_report_04.py` | Refresh checkpoint four, integrate verified corrections and computation summaries, and state the finite-prime C3 theorem and remaining integral gate. | RESEARCH_SA08_report.md; logs/report_update_04.json; also invoked inside later report updaters. | Standalone receipt: 94 statement rows, 75 corrections, 82 PDF pages, 28 inspected pages. Runtime is not recorded. |
| `update_report_05.py` | Run update_report_04.py, then add checkpoint-five mathematical-program records, inspected-source scope, proof-gate changes and typesetting repairs. | RESEARCH_SA08_report.md; logs/report_update_05.json, a stream of two JSON objects. | Receipt stream includes 105 statements, 75 corrections, 99 PDF pages and 47 inspected pages, followed by checkpoint_update=5. Runtime is not recorded. |
| `update_report_06.py` | Run the checkpoint-five updater, add the arity/conditional-descent computations and the checkpoint-six C3 and formal-review state. | RESEARCH_SA08_report.md; logs/report_update_06.json and report_update_06_final.json, each retaining nested updater receipts. | Saved streams record 114 statements, 75 corrections, 116 PDF pages and 65 inspected pages, followed by checkpoint_update=5 and 6. Runtime is not recorded. |
| `update_report_last.py` | Run the earlier updater chain, consolidate C33–C36/source-search scope and the C35 mathematical certificate, and, only with --final and the binding review, mark the report final/INCOMPLETE and insert this operational inventory. | RESEARCH_SA08_report.md; reads notes/OPERATIONAL_PROGRAMS.md, logs/C_rational_saturation_countercheck.json and logs/PROGRESS_REVIEW_03.json; later stdout receipts, if any, identify the final counts. | This inventory does not claim a final invocation has already completed. Its execution count and runtime are not recorded here. C_rational_saturation_countercheck.py remains in the mathematical-program list, not the operational list. |
| `record_review_01.py` | Record the first formal three-hour review only when due and only once; append the complete status/movement reasoning to the ledger and save the stop-rule state. | PROGRESS_LEDGER.md; logs/PROGRESS_REVIEW_01.json. | One numbered review is recorded; qualifying_movement=true and consecutive_no_movement_reviews=0. Runtime is not recorded; scheduled/actual UTC timestamps are not durations. |
| `record_review_03.py` | Record the binding third formal review only at or after 10:21 UTC, require the prior no-movement count of one, append the conservative gate assessment, and prohibit overwriting an existing review. | PROGRESS_LEDGER.md; logs/PROGRESS_REVIEW_03.json when executed; reads PROGRESS_REVIEW_02.json. | The script's intended final state is two consecutive no-movement reviews and stop_required=true. The review-state table below reports only files actually present at inventory time. Runtime is not recorded. |

### Build, PDF QA and packaging

| Program | Actual purpose | Output / receipt references | Recorded counts and runtime |
|---|---|---|---|
| `build_paper.py` | Configure a workspace-local LuaLaTeX format/cache, optionally regenerate BibTeX before the first pass, then execute TeX/BibTeX passes with logged exit codes and per-command durations. | RESEARCH_SA08_paper.pdf and generated TeX intermediates; logs/typeset_*.txt; logs/build_driver_18.jsonl through build_driver_39.jsonl. | The build table below gives every saved driver command count, exit code and measured command duration. Earlier build text logs preserve diagnostics but do not themselves supply total runtimes. Failed builds are retained, not counted as successful outputs. |
| `typeset_probe.lua` | Probe the selected TeX cache path, print the resolved TEXMFCACHE value, check that the directory exists, and test a temporary file write followed by removal. | logs/typeset_probe.txt and typeset_probe_02.txt; temporary probe.tmp is removed after a successful write. | Two saved probe outputs: the initial version failed on an unavailable iswritablefile call; the revised version records lfsdir=true and a successful write. Runtime is not recorded. |
| `qa_paper.py` | Parse real build diagnostics, reject unresolved warning/overflow conditions, locate prior overflow and new-content anchors, render the selected pages and montage images, and create an unapproved QA record. | logs/pdf_qa/<build stem>/qa_record.json, page-*.png and montage-*.png; auxiliary pdf_qa_*.json summaries. | The QA table below records all persisted page/render counts and the recorded review state. Rendering alone does not approve a PDF. Runtime is not recorded. |
| `approve_pdf.py` | Record a caller's completed visual inspection only if the reviewed-page set equals the rendered set and the PDF hash still matches; hash every included TeX fragment and the bibliography. | The selected logs/pdf_qa/<build>/qa_record.json and logs/PDF_QA_APPROVED.json. | The approval snapshot below records the actual approved build, page count and inspected-page count. Runtime is not recorded. This program neither performs nor substitutes for image inspection. |
| `make_package.py` | Create a never-overwritten checkpoint/final ZIP with exact-byte SHA-256 manifest; require approved PDF/source hashes and all mandatory deliverables; for --final require the binding stop review and an INCOMPLETE first line. | ../RESEARCH_SA08_checkpoint_*.zip or the supplied final name; PACKAGE_MANIFEST.json inside each ZIP; logs/checkpoint_03_package.json and checkpoint_05_package.json. | Checkpoint 03 receipt: 394 entries, 42233182 bytes. Checkpoint 05 receipt: 679 entries, 85624809 bytes. Creation timestamps are recorded, but runtime is not recorded. The exclusions cover fetched publications/original scans, original attachments, earlier ZIPs and transient files; approved QA images are retained. |
| `B_operational_inventory.py` | Read existing program sources, named receipts and registers; assemble this inventory and a source-hash coverage receipt without rerunning any inventoried program. | notes/OPERATIONAL_PROGRAMS.md; logs/B_operational_inventory.json. | Its own exact runtime and program/category counts are recorded in logs/B_operational_inventory.json. It adds no mathematical result, source download, build or approval. |
| `final_audit.py` | Verify the final report, result/event registers, bibliography access markers, binding stop state and approved PDF/source hashes; require every saved program filename to appear in the report. This is a release consistency audit, not a mathematical proof or visual inspection. | logs/FINAL_AUDIT.json, produced after the final report is assembled; reads the final report/registers, register_audit.json, PROGRESS_REVIEW_03.json and PDF_QA_APPROVED.json. | The intended release inputs contain 24 requested outcome rows, 118 statement/label rows, 352 events, 68 marked bibliography entries, 124 PDF pages, 47 approved source hashes and 76 reviewed pages. Actual validation counts, individual check results and runtime will be recorded in logs/FINAL_AUDIT.json; no completed execution is claimed by this inventory. |

### Generic source-fetch run receipts

These are the surviving `fetch_sources.py` request records from the root run. Their original JSON also retains the requested/final URL and response type.

| Receipt under logs/ | Response saved under sources/ | Bytes | Seconds | Outcome |
|---|---|---|---|---|
| A_antieau_fetch.jsonl | antieau2025_source.tar | 50331 | 5.628 | response saved |
| A_derived_binomial_fetch.jsonl | derived_binomial_source.tar | 100899 | 10.187 | response saved |
| A_doldpuppe_fetch.jsonl | doldpuppe1961.pdf | 8989529 | 154.739 | response saved |
| A_kareem_fetch.jsonl | kareem2018.pdf | 1092443 | 11.0 | response saved |
| A_porter_suciu_fetch.jsonl | porter_suciu_source.tar | 46056 | 8.52 | response saved |
| A_roby_fetch.jsonl | roby1963.pdf | 12417978 | 226.473 | response saved |
| A_source_fetch_01.jsonl | horel_arxiv_source.tar | 22793 | 6.437 | response saved |
| A_source_fetch_01.jsonl | horel.pdf | 487612 | 6.202 | response saved |
| A_source_fetch_01.jsonl | cartan.pdf | 225341 | 44.432 | response saved |
| A_source_fetch_01.jsonl | kageyama2211.tar | 39703 | 5.353 | response saved |
| A_source_fetch_01.jsonl | kageyama2405.tar | 29765 | 4.277 | response saved |
| A_source_fetch_02.jsonl | eudml_cartan.html | 33724 | 8.134 | response saved |
| A_source_fetch_02.jsonl | toen_source.tar | 105176 | 5.779 | response saved |
| A_source_fetch_02.jsonl | mandell2006.pdf | 680443 | 13.359 | response saved |
| A_source_fetch_03.jsonl | gdz_cartan_volume.html | 5909 | 5.415 | response saved |
| A_source_fetch_04.jsonl | gdz_manifest.json | 510845 | 5.671 | response saved |
| A_source_fetch_05.jsonl | cartan1976.pdf | 1243069 | 6.185 | response saved |
| A_source_fetch_06.jsonl | synthetic_hilbert_source.tar | 51142 | 6.257 | response saved |
| A_source_fetch_06.jsonl | ekedahl_source.tar | 43180 | 5.184 | response saved |
| A_sullivan_fetch.jsonl | sullivan1977.pdf | 8032592 | 132.511 | response saved |
| A_zakharov_fetch.jsonl | zakharov2026_source.tar | 30942 | 7.516 | response saved |
| source_fetch_magidson2024.jsonl | magidson2024_source.tar | 987539 | 6.838 | response saved |

### B download and one-off source receipts

These are individual persisted receipts. The three `already_downloaded` rows measure only cache reads and hashing; their original download durations are **not recorded in the surviving latest receipt**. The Anick failure is retained.

| Receipt under logs/ | Requested file / source | Bytes | Recorded seconds | Recorded outcome |
|---|---|---|---|---|
| B_source_downloads.json | B_may1970.pdf | 13555177 | 7.776005150000856 | response saved |
| B_source_downloads.json | B_steenrod_epstein1962.pdf | 4559420 | 6.027831764000439 | response saved |
| B_source_downloads.json | B_pursuing_stacks_source.tar | 591565 | 5.2046600979992945 | response saved |
| B_additional_downloads.json | B_cenkl_porter1982 | 420657 | 8.993040687997564 | response saved |
| B_additional_downloads.json | B_mandell2001 | 454285 | 9.821948320000956 | response saved |
| B_cartan1954_exp7_fetch.json | B_cartan1954_exp7.pdf | 1449220 | 24.06583759300338 | response saved |
| B_cenkl1989_fetch.json | B_cenkl1989.pdf | 1026193 | 7.103141175000928 | response saved |
| B_cenkl_porter1984_ast_fetch.json | B_cenkl_porter1984_ast.pdf | 490914 | 8.978226180002821 | response saved |
| B_cenkl_porter1984_cubical_fetch.json | B_cenkl_porter1984_cubical.pdf | 1220359 | 9.128421449997404 | response saved; relabelled B_butler_erbe1984_misfetch.pdf; unrelated article |
| B_cenkl_porter1984_true_fetch.json | B_cenkl_porter1984_true.pdf | 1372081 | 5.208861807001085 | response saved |
| B_dold_puppe1961_fetch.json | B_dold_puppe1961.pdf | 8989529 | 181.6618537100003 | response saved |
| B_goerss_jardine_fetch.json | B_goerss_jardine.pdf | 2411067 | 10.161564750000252 | response saved |
| B_roby1963_fetch.json | B_roby1963.pdf | 12417978 | 222.16552633500032 | response saved |
| B_sullivan1977_fetch.json | B_sullivan1977.pdf | 8032592 | 142.55891178399906 | response saved |
| B_relative_literature_fetch.json | menichi2001_fiber | 228605 | 0.0007351949971052818 | already_downloaded |
| B_relative_literature_fetch.json | scheerer_tanre1991_tame | 739146 | 0.0022901429983903654 | already_downloaded |
| B_relative_literature_fetch.json | scott2005_hopf | 133442 | 0.0016670410041115247 | already_downloaded |
| B_relative_literature_fetch.json | anick1989_hopf | not recorded | 5.1006405020016246 | not_downloaded: <HTTPError 403: 'Forbidden'> |
| B_relative_literature_fetch.json | hanke2009_stable_rank | 348546 | 8.385121977997187 | downloaded |

### Preserved range-fetch retries

These earlier transcripts are separate from the three completed-range JSON receipts. The rows count only complete range records actually written to each transcript; reused blocks and unlogged interrupted transfers are not inferred.

| Transcript under logs/ | Logged complete ranges | Logged bytes | Per-range seconds | Whole-run duration / completion |
|---|---|---|---|---|
| B_cote136_ranges.txt | 1 | 262144 | 8.072074284998962 | not recorded; no completion receipt in this transcript |
| B_cote136_ranges_retry.txt | 14 | 3472680 | 7.6287948960016365, 5.64234759700048, 5.529539783001383, 9.18423371300014, 8.628835941999569, 10.904543805001595, 7.476160644000629, 13.042302404999646, 5.636949196999922, 5.754192184002022, 7.692205374001787, 11.98746504400333, 5.92621796000094, 6.514051489000849 | not recorded; no completion receipt in this transcript |
| B_cote136_ranges_selected.txt | 11 | 2883584 | 7.119623284001136, 7.3329394979991775, 13.969619653002155, 6.299268865001068, 6.3866839639995305, 6.406195472001855, 13.171343759000592, 9.871541371001513, 6.521677140000975, 5.476879226000165, 8.114054197998485 | not recorded; no completion receipt in this transcript |
| B_cote136_ranges_strict.txt | 7 | 1835008 | 7.50640560699685, 10.751826281000831, 7.769372317998204, 7.607676532999903, 6.290484674002073, 12.566808731000492, 7.224460261000786 | 59.75233911300165 s; completed scans 142–145 |

### Build-driver receipts

Each duration belongs to the command in the same position in the saved receipt; commands and arguments remain in the JSONL. These are measured subprocess runtimes, **not** a complete elapsed-time total for the research or build session. Nonzero exit codes preserve failed attempts.

| Driver receipt under logs/ | Commands | Exit codes in order | Command seconds in order | Diagnostic logs under logs/ |
|---|---|---|---|---|
| build_driver_18.jsonl | 4 | 0, 0, 0, 0 | 8.311058919000061; 0.007255909000377869; 7.9375497170003655; 8.191532549997646 | typeset_build_18.txt; typeset_build_18_bibtex.txt; typeset_build_18_pass2.txt; typeset_build_18_pass3.txt |
| build_driver_19.jsonl | 3 | 0, 0, 1 | 7.805860057997052; 0.008533563999662874; 7.822800437999831 | typeset_build_19.txt; typeset_build_19_bibtex.txt; typeset_build_19_pass2.txt |
| build_driver_20.jsonl | 1 | 1 | 7.652118777998112 | typeset_build_20.txt |
| build_driver_21.jsonl | 5 | 0, 0, 0, 0, 0 | 0.006987716002186062; 7.312232371001301; 0.006634303997998359; 7.212360207999154; 7.361516995999409 | typeset_build_21_bibtex_preflight.txt; typeset_build_21.txt; typeset_build_21_bibtex.txt; typeset_build_21_pass2.txt; typeset_build_21_pass3.txt |
| build_driver_22.jsonl | 5 | 0, 0, 0, 0, 0 | 0.008776473998295842; 8.202984890001972; 0.007323440000618575; 8.230807773001288; 8.163461978998384 | typeset_build_22_bibtex_preflight.txt; typeset_build_22.txt; typeset_build_22_bibtex.txt; typeset_build_22_pass2.txt; typeset_build_22_pass3.txt |
| build_driver_23.jsonl | 5 | 0, 0, 0, 0, 0 | 0.008012596001208294; 8.114136949003296; 0.006921546999365091; 7.440242976001173; 7.582798121999076 | typeset_build_23_bibtex_preflight.txt; typeset_build_23.txt; typeset_build_23_bibtex.txt; typeset_build_23_pass2.txt; typeset_build_23_pass3.txt |
| build_driver_24.jsonl | 5 | 0, 0, 0, 0, 0 | 0.00824353400093969; 7.630672207000316; 0.007493426001019543; 8.272944095999264; 7.5240210670017404 | typeset_build_24_bibtex_preflight.txt; typeset_build_24.txt; typeset_build_24_bibtex.txt; typeset_build_24_pass2.txt; typeset_build_24_pass3.txt |
| build_driver_25.jsonl | 5 | 0, 0, 0, 0, 0 | 0.007050203999824589; 7.522213965999981; 0.007956623001518892; 7.415097729997797; 7.612763184999494 | typeset_build_25_bibtex_preflight.txt; typeset_build_25.txt; typeset_build_25_bibtex.txt; typeset_build_25_pass2.txt; typeset_build_25_pass3.txt |
| build_driver_26.jsonl | 5 | 0, 0, 0, 0, 0 | 0.009418109999387525; 7.839924817999417; 0.006686813001579139; 7.32968621100008; 7.464099854001688 | typeset_build_26_bibtex_preflight.txt; typeset_build_26.txt; typeset_build_26_bibtex.txt; typeset_build_26_pass2.txt; typeset_build_26_pass3.txt |
| build_driver_27.jsonl | 2 | 0, 1 | 0.02555802700226195; 8.055889161001687 | typeset_build_27_bibtex_preflight.txt; typeset_build_27.txt |
| build_driver_28.jsonl | 1 | 2 | 0.005687209999450715 | typeset_build_28_bibtex_preflight.txt |
| build_driver_29.jsonl | 4 | 0, 0, 0, 0 | 8.537215929998638; 0.008105549000902101; 9.10545172699858; 7.792883302998234 | typeset_build_29.txt; typeset_build_29_bibtex.txt; typeset_build_29_pass2.txt; typeset_build_29_pass3.txt |
| build_driver_30.jsonl | 5 | 0, 0, 0, 0, 0 | 0.007973628002218902; 8.117114804001176; 0.007334666999668116; 7.525052846998733; 7.834966105998319 | typeset_build_30_bibtex_preflight.txt; typeset_build_30.txt; typeset_build_30_bibtex.txt; typeset_build_30_pass2.txt; typeset_build_30_pass3.txt |
| build_driver_31.jsonl | 2 | 0, 1 | 0.008599890003097244; 8.72740098900249 | typeset_build_31_bibtex_preflight.txt; typeset_build_31.txt |
| build_driver_32.jsonl | 4 | 0, 0, 0, 0 | 9.244026267999288; 0.00826121700083604; 8.641620314996544; 8.518964495000546 | typeset_build_32.txt; typeset_build_32_bibtex.txt; typeset_build_32_pass2.txt; typeset_build_32_pass3.txt |
| build_driver_33.jsonl | 5 | 0, 0, 0, 0, 0 | 0.007523009997385088; 8.552538355001161; 0.008309775002999231; 8.290880746997573; 8.669905956001458 | typeset_build_33_bibtex_preflight.txt; typeset_build_33.txt; typeset_build_33_bibtex.txt; typeset_build_33_pass2.txt; typeset_build_33_pass3.txt |
| build_driver_34.jsonl | 2 | 0, 1 | 0.008975674001703737; 8.06431133300066 | typeset_build_34_bibtex_preflight.txt; typeset_build_34.txt |
| build_driver_35.jsonl | 1 | 1 | 8.683538147000945 | typeset_build_35.txt |
| build_driver_36.jsonl | 4 | 0, 0, 0, 0 | 8.61517003300105; 0.0077721970010316; 8.40916836100223; 8.23054832300113 | typeset_build_36.txt; typeset_build_36_bibtex.txt; typeset_build_36_pass2.txt; typeset_build_36_pass3.txt |
| build_driver_37.jsonl | 5 | 0, 0, 0, 0, 0 | 0.00831686000310583; 8.69808035299502; 0.008657976999529637; 8.901834634998522; 8.731192018000002 | typeset_build_37_bibtex_preflight.txt; typeset_build_37.txt; typeset_build_37_bibtex.txt; typeset_build_37_pass2.txt; typeset_build_37_pass3.txt |
| build_driver_38.jsonl | 5 | 0, 0, 0, 0, 0 | 0.008971964001830202; 9.262260863004485; 0.008063691995630506; 8.792478065995965; 9.068876841003657 | typeset_build_38_bibtex_preflight.txt; typeset_build_38.txt; typeset_build_38_bibtex.txt; typeset_build_38_pass2.txt; typeset_build_38_pass3.txt |
| build_driver_39.jsonl | 5 | 0, 0, 0, 0, 0 | 0.007625024001754355; 9.120987257003435; 0.0074536059983074665; 8.996545387999504; 9.526797516002262 | typeset_build_39_bibtex_preflight.txt; typeset_build_39.txt; typeset_build_39_bibtex.txt; typeset_build_39_pass2.txt; typeset_build_39_pass3.txt |
| build_driver_40.jsonl | 5 | 0, 0, 0, 0, 0 | 0.007967519995872863; 9.679727522998292; 0.021025481997639872; 9.828241245995741; 9.269689228000061 | typeset_build_40_bibtex_preflight.txt; typeset_build_40.txt; typeset_build_40_bibtex.txt; typeset_build_40_pass2.txt; typeset_build_40_pass3.txt |

### PDF-QA receipt snapshots

A rendered page count is not an inspection count unless the saved review field records inspection. The exact PDF hash and full page lists remain in each JSON; earlier unapproved renderings remain unapproved.

| QA record | PDF pages | Rendered pages | Overfull boxes | Saved review state | Runtime |
|---|---|---|---|---|---|
| logs/pdf_qa/typeset_build_14_pass3/qa_record.json | 58 | 19 | 0 | awaiting explicit image inspection | not recorded |
| logs/pdf_qa/typeset_build_15_pass3/qa_record.json | 60 | 19 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_16_pass3/qa_record.json | 60 | 19 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_17/qa_record.json | 60 | 19 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_18_pass3/qa_record.json | 68 | 21 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_25_pass3/qa_record.json | 82 | 27 | 0 | awaiting explicit image inspection | not recorded |
| logs/pdf_qa/typeset_build_26_pass3/qa_record.json | 82 | 28 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_30_pass3/qa_record.json | 99 | 47 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_36_pass3/qa_record.json | 116 | 65 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_39_pass3/qa_record.json | 124 | 76 | 0 | passed explicit recorded inspection | not recorded |
| logs/pdf_qa/typeset_build_40_pass3/qa_record.json | 124 | 76 | 0 | passed explicit recorded inspection | not recorded |

At this inventory snapshot, `logs/PDF_QA_APPROVED.json` names `logs/typeset_build_40_pass3.txt`, 124 PDF pages and 76 inspected rendered pages; 47 included source files have recorded hashes. The approval UTC is `2026-11-19T10:26:37.287001+00:00`. The approval runtime is **not recorded**. Later approved builds, if any, require their own receipt and cannot inherit this approval.

### Formal-review receipt state

The second review has a saved receipt but no separate `record_review_02.py` in `code/`; this inventory does not invent one.

| Receipt under logs/ | Actual UTC stamp | Consecutive no-movement reviews | Runtime |
|---|---|---|---|
| PROGRESS_REVIEW_01.json | 2026-11-19T08:21:12.976475+00:00 | 0 | not recorded |
| PROGRESS_REVIEW_02.json | 2026-11-19T09:21:58.135316+00:00 | 1 | not recorded |
| PROGRESS_REVIEW_03.json | 2026-11-19T10:21:10.134853+00:00 | 2 | not recorded |

### Coverage and provenance limitations

All operational Python/Lua files in `code/` are enumerated above. The D run's source searches and opened-scope inventories are retained in `logs/D_source_searches.tsv`, `logs/D_global_repair_source_searches.tsv`, `logs/D_late_source_inventory.tsv` and `logs/D_sources_do_not_package.tsv`; there is no separate D-prefixed download program in `code/` to enumerate. This is a program inventory, not a claim that every interactive shell command or tool request had a standalone script. A later final-report or ZIP operation may postdate this snapshot; its new receipt supplies its own counts. No missing download duration, build wall time, edit count or packaging runtime has been reconstructed from timestamps.
