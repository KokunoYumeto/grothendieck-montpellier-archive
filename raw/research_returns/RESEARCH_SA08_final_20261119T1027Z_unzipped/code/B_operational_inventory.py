"""Document existing operational programs and receipts without executing them.

This program reads the saved source files, logs and registers only. It performs
no download, mathematical experiment, registry update, typesetting or approval.
The generated inventory includes this documentation program itself.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()

# Descriptions were checked against the actual source, not inferred from names.
# Counts in this table are either explicitly identified static payloads or named
# persisted receipts; they are not claims that a historical script was rerun.
ROWS = [
    ("Source acquisition and inspection", "fetch_sources.py",
     "Fetch explicitly supplied name=URL pairs, save the response bytes, and print one JSON success/failure receipt per request. It does not identify the publication or inspect its mathematics.",
     "sources/<supplied name>; logs/A_source_fetch_01.jsonl through A_source_fetch_06.jsonl and the other named fetch receipts in the request table below.",
     "The complete surviving request table below records byte counts and per-request seconds; these are separate requests, not a total elapsed runtime."),
    ("Source acquisition and inspection", "unpack_arxiv_sources.py",
     "Extract previously downloaded arXiv tar/gzip source files into confined source directories, with path-traversal checks, and list extracted files.",
     "sources/<archive stem>/; logs/A_new_filtered_sources_unpack.jsonl; logs/source_unpack_magidson2024.jsonl.",
     "Zakharov: 6 files, 0.003355455002747476 s; Antieau: 4 files, 0.002945379001175752 s; Magidson: 5 files, 0.01585413300199434 s. These are extraction times, not download times."),
    ("Source acquisition and inspection", "extract_scans.py",
     "Print selected scan-number blocks from the attached transcription files, retaining original filename and one-based line number for each line.",
     "Standard output; original inputs are input/RESEARCH_SA08_transcriptions/transcriptions/*transcription.tex. Exact locators were copied into proof/source notes.",
     "A separate execution count and runtime are not recorded."),
    ("Source acquisition and inspection", "B_archive_fetch.py",
     "Fetch the Montpellier archive catalogue, save its HTML, and print contexts containing 136 plus script URLs for the documentary dating check.",
     "sources/B_archive_catalogue.html; logs/B_archive_fetch.txt.",
     "The final JSON line records 244048 bytes and 5.58734708799966 s. Catalogue retrieval is not evidence dating the mathematical leaves."),
    ("Source acquisition and inspection", "B_download.py",
     "Fetch May 1970, Steenrod–Epstein 1962 and the Pursuing Stacks arXiv source bundle, preserving response type, hash and download receipts.",
     "sources/B_may1970.pdf, B_steenrod_epstein1962.pdf, B_pursuing_stacks_source.tar; logs/B_source_downloads.json.",
     "Three successful request records; individual bytes and durations appear in the source-receipt table below."),
    ("Source acquisition and inspection", "B_download_additional.py",
     "Concurrently fetch Cenkl–Porter 1982 and Mandell 2001, then extract PDF text with pdftotext.",
     "sources/B_cenkl_porter1982.pdf/.txt and B_mandell2001.pdf/.txt; logs/B_additional_downloads.json.",
     "Two successful records: 420657 bytes / 8.993040687997564 s and 454285 bytes / 9.821948320000956 s. Durations include text extraction; no overall concurrent wall time is recorded."),
    ("Source acquisition and inspection", "B_fetch_c3_source.py",
     "Fetch a specified arXiv source archive, extract only TeX/BibTeX/text files with confined paths, and preserve hash, extracted filenames and retrieval status.",
     "sources/B_quillen_pd.tar and B_quillen_pd_source/; sources/B_caradot_lin2025.tar and B_caradot_lin2025_source/; logs/B_quillen_pd_fetch.json and B_caradot_lin2025_fetch.json.",
     "Dokas–Frankland–Ikonicoff: 155324 bytes, 1 extracted text file, 6.759984792999603 s. Caradot–Lin v1: 84394 bytes, 1 extracted text file, 6.537299870000425 s. The initial receipt says scope not yet read; subsequent reading is separately documented."),
    ("Source acquisition and inspection", "B_fetch_cote136.py",
     "Attempt a streamed full download of original cote 136, with SHA-256 accumulation and a completion receipt only after end of stream.",
     "Attempted sources/B_original_cote136.pdf, subsequently retained as B_original_cote136.partial by the range reader; logs/B_cote136_fetch.txt. The intended logs/B_cote136_receipt.json is absent.",
     "No completed-fetch count or runtime is recorded; the stdout file is empty. This is not recorded as a successful full-PDF acquisition. Selected original scans were obtained separately."),
    ("Source acquisition and inspection", "B_fetch_literature.py",
     "Fetch an explicitly supplied primary-source URL, save a SHA-256 receipt, and run pdftotext for PDF responses.",
     "sources/B_<requested publication>.pdf/.txt; individual logs/B_*_fetch.json receipts listed below.",
     "Nine surviving individual request receipts are listed below. One was a wrong article reached through an incorrect URL and was relabelled by B_label_misfetch.py; it is not counted as an opened Cenkl–Porter source."),
    ("Source acquisition and inspection", "B_fetch_pdf_ranges.py",
     "Read the remote cote 136 PDF through cached HTTP byte ranges; traverse its page tree to copy only specified original scans into small PDFs.",
     "sources/B_range_cache/; sources/B_cote136_scans142_145.pdf, B_cote136_scansomega.pdf, B_cote136_scans182.pdf; logs/B_cote136_ranges*.json and .txt.",
     "Completed runs: scans 142–145, 7 new ranges / 1835008 bytes / 59.75233911300165 s; scans 174,176,178,180, 10 new ranges / 2621440 bytes / 105.43540739499804 s; scan 182, 2 new ranges / 524288 bytes / 18.868229032999807 s. Earlier interrupted/retried transcripts retain individual range times but no completed-run runtime; see the range table below."),
    ("Source acquisition and inspection", "B_fetch_relative_literature.py",
     "Fetch or reuse five selected references for the local relative-repair search, verify PDF headers, extract text, and record blocked requests and cache hits distinctly.",
     "sources/B_menichi2001_fiber.pdf/.txt, B_scheerer_tanre1991_tame.pdf/.txt, B_scott2005_hopf.pdf/.txt, B_hanke2009_stable_rank.pdf/.txt; logs/B_relative_literature_fetch.json.",
     "Latest receipt: 3 already-downloaded checks, 1 new download and 1 HTTP 403 failure (Anick). Exact per-entry durations below. Cache-check durations are not original download times; the latter are not preserved in this overwritten receipt."),
    ("Source acquisition and inspection", "B_fetch_serre1953.py",
     "Fetch the opened Serre 1953 primary finiteness source, verify the PDF signature, extract text and preserve the exact opened scope in the receipt.",
     "sources/B_serre1953_classes.pdf/.txt; logs/B_serre1953_fetch.json.",
     "767254 bytes; 10.171391184998356 s, including text extraction. Chapter I §6.1 and Chapter II §6 Proposition 8 are the recorded scope."),
    ("Source acquisition and inspection", "B_inspect_sources.py",
     "Safely unpack the downloaded Pursuing Stacks bundle, print its member inventory, and extract text from the downloaded May and Steenrod–Epstein PDFs.",
     "sources/B_pursuing_stacks/; sources/B_may1970.txt and B_steenrod_epstein1962.txt; logs/B_source_inventory.txt.",
     "The saved inventory lists 22 extracted files. Runtime is not recorded."),
    ("Source acquisition and inspection", "B_label_misfetch.py",
     "Rename the wrongly requested 1984 PDF/text as Butler–Erbe and annotate its existing download receipt with the actual first-page identification and exclusion from the SA08 argument.",
     "sources/B_butler_erbe1984_misfetch.pdf/.txt; amended logs/B_cenkl_porter1984_cubical_fetch.json.",
     "One mistaken source identity corrected; the script enumerates two file suffixes. Its correction runtime is not recorded. The 9.128421449997404 s in the receipt belongs to the earlier download, not relabelling."),
    ("Source acquisition and inspection", "B_ocr_primary.py",
     "Render a requested PDF page range at 120 dpi and OCR the rendered pages concurrently with Tesseract, solely to locate passages for subsequent image checking.",
     "notes/B_scan_images/B_may1970_ocr-*.png; sources/B_may1970_ocr_8_18.txt; logs/B_may1970_ocr_8_18.json.",
     "PDF pages 8–18 inclusive (11 pages); 87.89117174000057 s. The OCR output is not an independent mathematical verification."),
    ("Source acquisition and inspection", "C_fetch_manuscript.py",
     "Fetch exact cote 136 scans through HTTP ranges, reading the existing B cache without modifying it and writing its own C cache and page subsets.",
     "sources/C_range_cache/; sources/C_cote136_half_algebra.pdf and C_cote136_uniqueness.pdf; logs/C_cote136_half_algebra.json and C_cote136_uniqueness.json.",
     "Scans 348,350,352: 1572864 new bytes, 57.844757042999845 s. Scans 100,117,119,121: 2621440 new bytes, 93.25417175099938 s. Receipts include the individual range calls."),
    ("Source acquisition and inspection", "C_fetch_more_sources.py",
     "Concurrently fetch and unpack the exact arXiv sources for Berger–Fresse, Guillén–Navarro–Pascual–Roig and Porter–Suciu; preserve an archive or gzip fallback and a retrieval table.",
     "sources/C_berger_fresse*, C_monoidal_models*, C_porter_suciu*; logs/C_more_sources_fetch.tsv.",
     "Three OK rows: 135660 bytes / 7.705 s, 102952 bytes / 7.643 s, 155015 bytes / 7.412 s. The script's byte field can refer to decompressed fallback text; it is not uniformly a wire-byte measure. Overall concurrent runtime is not recorded."),
    ("Source acquisition and inspection", "C_fetch_shuffle_source.py",
     "Fetch the primary Melançon–Reutenauer shuffle article, verify its PDF signature and preserve the selected §4 locator and hash.",
     "sources/C_melancon_reutenauer1989.pdf; logs/C_shuffle_source_fetch.json.",
     "949029 bytes; 7.429747215999669 s; printed pp. 589–590 / PDF pp. 13–14 recorded."),
    ("Source acquisition and inspection", "C_fetch_sources.py",
     "Fetch the Christensen–Holm arXiv source and author PDF, recording separate success/failure rows.",
     "sources/C_christensen_holm_source.tar and C_christensen_holm.pdf; logs/C_source_fetch.tsv.",
     "Two successes: 19411 bytes / 9.723 s and 450583 bytes / 5.645 s."),
    ("Source acquisition and inspection", "C_read_cartan.py",
     "Render the 12 article pages of the exact Cartan 1976 PDF at a 2000-pixel maximum dimension and OCR them with Tesseract English.",
     "logs/C_cartan_pages/p-*.png; sources/C_cartan1976_ocr.txt; logs/C_cartan_ocr_run.txt.",
     "12 pages; 17.639 s. The receipt expressly requires image checking for mathematical formulas."),

    ("Registers and documentation", "B_register_results.py",
     "Create the initial B-01–B-13 statement register and its initial independent-check events, including references back to the supplied claims.",
     "notes/B_results.csv; notes/B_CHECK_EVENTS.tsv; logs/B_register_results.txt.",
     "The saved stdout records 13 initial statement rows. Runtime is not recorded. This historical script overwrites those registers; it must not be used to regenerate their later appended state."),
    ("Registers and documentation", "B_record_followup_checks.py",
     "Idempotently append the later B source inspections and independent A-006–A-025 audits without repeating an existing event identifier.",
     "notes/B_CHECK_EVENTS.tsv; referenced audit notes include B_A006_audit.md and B_A017_audit.md.",
     "The source enumerates 13 intended event identifiers. A separate insertion-count receipt and runtime are not recorded; the source count is not a claim that all 13 were newly inserted on every execution."),
    ("Registers and documentation", "B_record_c3.py",
     "Idempotently add the B-owned C3 auxiliary results and exact proof, source and independent-audit events. The header retains the earlier two-result description, but the actual payload is broader.",
     "notes/B_results.csv; notes/B_CHECK_EVENTS.tsv; covers C14, C15, C19, C20, C22, C23, C25, C27, C33 and C34 plus subsequent audits.",
     "Current source payload: 10 result rows and 32 event specifications. No per-run insertion count or runtime is recorded. Existing rows/events are checked before appending."),
    ("Registers and documentation", "B_build_corrections.py",
     "Build the B correction register from exact attached-file/line locators and find proof paragraph locators in the B TeX fragments.",
     "notes/B_CORRECTIONS.tsv; reads sections/B_automorphisms.tex, B_abstract_completion.tex and B_dating.tex.",
     "15 correction rows in the source payload and saved register; runtime is not recorded."),
    ("Registers and documentation", "B_format_audit_note.py",
     "Repair inline mathematical delimiters in B_A017_audit.md while preserving display-math blocks; this is a formatting utility.",
     "notes/B_A017_audit.md, edited in place.",
     "Number of replacements and runtime are not recorded."),
    ("Registers and documentation", "C_record_B605.py",
     "Append the finite-rank half-algebra classification statement, its proof-check event and the corresponding findings summary.",
     "notes/C_results.csv; notes/C_CHECK_EVENTS.tsv; notes/C_findings.md.",
     "Source payload: 1 result row and 1 check-event row, plus prose. A separate execution count and runtime are not recorded."),
    ("Registers and documentation", "C_record_C11.py",
     "Record the Tor obstruction proof and cite the previously executed binomial-gcd certificate; it does not rerun the certificate.",
     "notes/C_CHECK_EVENTS.tsv; references logs/C_finite_obstructions.txt.",
     "Source payload: 2 event rows. Runtime of this recorder is not recorded; the mathematical program's quoted runtime belongs to that separate computation."),
    ("Registers and documentation", "C_record_b6_sources.py",
     "Append B603/B604 results, five source/proof events, one exact-input correction and the source-search narrative for cup-i, Cartan and integral uniqueness leads.",
     "notes/C_results.csv; notes/C_CHECK_EVENTS.tsv; notes/C_CORRECTIONS.tsv; notes/C_source_searches.md.",
     "Source payload: 2 result rows, 5 events and 1 correction. Recorder runtime is not recorded. Download/OCR times quoted in the prose are credited to their own scripts above."),
    ("Registers and documentation", "C_record_rechecks.py",
     "Append the refined scan-360 comparison, finite-certificate rerun citation, independent C09 audit and failed finite-prime reduction record.",
     "notes/C_CHECK_EVENTS.tsv.",
     "Source payload: 4 event rows. Recorder runtime is not recorded."),
    ("Registers and documentation", "C_update_proofs.py",
     "Replace the earlier rational C07 argument with the proved all-nonzero-ring strict-equalization counterexample, and synchronize its findings note.",
     "sections/C_part.tex; notes/C_findings.md.",
     "One named theorem/proof and its matching note are replaced by the source. Separate edit counts and runtime are not recorded. It is a historical proof-integration script, not a new proof test."),
    ("Registers and documentation", "D_make_records.py",
     "Rebuild D-agent statement/event registers from already completed proofs and saved finite checks; include independent B/A audits and correction events.",
     "logs/D_results.csv; logs/D_CHECK_EVENTS.tsv.",
     "Saved registers have 23 statement rows and 45 event rows. Runtime is not recorded. The source expressly says it does not assert new checks."),
    ("Registers and documentation", "register_A023.py",
     "Write the additional numerical-tail pairing result and its proof, independent audit and finite-certificate references.",
     "notes/A_additional_results.csv; notes/A_additional_CHECK_EVENTS.tsv.",
     "Source payload: 1 result and 3 event rows. Runtime is not recorded."),
    ("Registers and documentation", "register_A025.py",
     "Write the rational-specialization result and record independent proof checks for A-025 and the supplied earlier claim identifier.",
     "notes/A_specialization_results.csv; notes/A_specialization_CHECK_EVENTS.tsv.",
     "Source payload: 1 result and 4 event rows. Runtime is not recorded."),
    ("Registers and documentation", "register_A_corrections.py",
     "Write exact attached-input locators and proved corrections for Part A, the shared shadow claims and the relevant leads.",
     "notes/A_CORRECTIONS.tsv.",
     "23 correction rows in the source payload and saved register; runtime is not recorded."),
    ("Registers and documentation", "consolidate_corrections.py",
     "Normalize and merge the four independently maintained correction schemas without modifying the attached inputs; emit machine-readable and Markdown tables.",
     "RESEARCH_SA08_corrections.tsv; notes/CORRECTIONS_table.md; logs/corrections_merge_03.json.",
     "The saved merge receipt records 75 corrections from A, B, C and D registers; runtime is not recorded."),
    ("Registers and documentation", "update_registers.py",
     "Merge the root A results with all maintained result/event fragments; optionally concatenate bibliography fragments or preserve an already approved bibliography.",
     "RESEARCH_SA08_results.csv; CHECK_EVENTS.tsv; RESEARCH_SA08_references.bib unless --preserve-bibliography; logs/register_update*.json and registers_01.json.",
     "logs/register_update_39_final_checks.json records 118 statements, 352 events and 4 bibliography fragments, with bibliography_preserved=true. Runtime is not recorded; its UTC stamp is not a duration."),
    ("Registers and documentation", "audit_registers.py",
     "Compare canonical statement IDs with numbered labels in the paper's actually included fragments; report duplicate IDs, duplicate labels and either direction of unmatched entries.",
     "logs/register_audit.json and the preserved register_audit_*.json snapshots.",
     "logs/register_audit_39_final_checks.json records 118 rows and 118 labels, with all four discrepancy lists empty. Runtime is not recorded."),

    ("Report and formal-review maintenance", "update_report_03.py",
     "Refresh the checkpoint-three report from approved PDF metrics, correction tables and the then-current mathematical gate descriptions.",
     "RESEARCH_SA08_report.md; logs/report_update_03.json.",
     "Receipt: 88 statements, 68 approved PDF pages, 21 reviewed pages. Runtime is not recorded."),
    ("Report and formal-review maintenance", "update_report_04.py",
     "Refresh checkpoint four, integrate verified corrections and computation summaries, and state the finite-prime C3 theorem and remaining integral gate.",
     "RESEARCH_SA08_report.md; logs/report_update_04.json; also invoked inside later report updaters.",
     "Standalone receipt: 94 statement rows, 75 corrections, 82 PDF pages, 28 inspected pages. Runtime is not recorded."),
    ("Report and formal-review maintenance", "update_report_05.py",
     "Run update_report_04.py, then add checkpoint-five mathematical-program records, inspected-source scope, proof-gate changes and typesetting repairs.",
     "RESEARCH_SA08_report.md; logs/report_update_05.json, a stream of two JSON objects.",
     "Receipt stream includes 105 statements, 75 corrections, 99 PDF pages and 47 inspected pages, followed by checkpoint_update=5. Runtime is not recorded."),
    ("Report and formal-review maintenance", "update_report_06.py",
     "Run the checkpoint-five updater, add the arity/conditional-descent computations and the checkpoint-six C3 and formal-review state.",
     "RESEARCH_SA08_report.md; logs/report_update_06.json and report_update_06_final.json, each retaining nested updater receipts.",
     "Saved streams record 114 statements, 75 corrections, 116 PDF pages and 65 inspected pages, followed by checkpoint_update=5 and 6. Runtime is not recorded."),
    ("Report and formal-review maintenance", "update_report_last.py",
     "Run the earlier updater chain, consolidate C33–C36/source-search scope and the C35 mathematical certificate, and, only with --final and the binding review, mark the report final/INCOMPLETE and insert this operational inventory.",
     "RESEARCH_SA08_report.md; reads notes/OPERATIONAL_PROGRAMS.md, logs/C_rational_saturation_countercheck.json and logs/PROGRESS_REVIEW_03.json; later stdout receipts, if any, identify the final counts.",
     "This inventory does not claim a final invocation has already completed. Its execution count and runtime are not recorded here. C_rational_saturation_countercheck.py remains in the mathematical-program list, not the operational list."),
    ("Report and formal-review maintenance", "record_review_01.py",
     "Record the first formal three-hour review only when due and only once; append the complete status/movement reasoning to the ledger and save the stop-rule state.",
     "PROGRESS_LEDGER.md; logs/PROGRESS_REVIEW_01.json.",
     "One numbered review is recorded; qualifying_movement=true and consecutive_no_movement_reviews=0. Runtime is not recorded; scheduled/actual UTC timestamps are not durations."),
    ("Report and formal-review maintenance", "record_review_03.py",
     "Record the binding third formal review only at or after 10:21 UTC, require the prior no-movement count of one, append the conservative gate assessment, and prohibit overwriting an existing review.",
     "PROGRESS_LEDGER.md; logs/PROGRESS_REVIEW_03.json when executed; reads PROGRESS_REVIEW_02.json.",
     "The script's intended final state is two consecutive no-movement reviews and stop_required=true. The review-state table below reports only files actually present at inventory time. Runtime is not recorded."),

    ("Build, PDF QA and packaging", "build_paper.py",
     "Configure a workspace-local LuaLaTeX format/cache, optionally regenerate BibTeX before the first pass, then execute TeX/BibTeX passes with logged exit codes and per-command durations.",
     "RESEARCH_SA08_paper.pdf and generated TeX intermediates; logs/typeset_*.txt; logs/build_driver_18.jsonl through build_driver_39.jsonl.",
     "The build table below gives every saved driver command count, exit code and measured command duration. Earlier build text logs preserve diagnostics but do not themselves supply total runtimes. Failed builds are retained, not counted as successful outputs."),
    ("Build, PDF QA and packaging", "typeset_probe.lua",
     "Probe the selected TeX cache path, print the resolved TEXMFCACHE value, check that the directory exists, and test a temporary file write followed by removal.",
     "logs/typeset_probe.txt and typeset_probe_02.txt; temporary probe.tmp is removed after a successful write.",
     "Two saved probe outputs: the initial version failed on an unavailable iswritablefile call; the revised version records lfsdir=true and a successful write. Runtime is not recorded."),
    ("Build, PDF QA and packaging", "qa_paper.py",
     "Parse real build diagnostics, reject unresolved warning/overflow conditions, locate prior overflow and new-content anchors, render the selected pages and montage images, and create an unapproved QA record.",
     "logs/pdf_qa/<build stem>/qa_record.json, page-*.png and montage-*.png; auxiliary pdf_qa_*.json summaries.",
     "The QA table below records all persisted page/render counts and the recorded review state. Rendering alone does not approve a PDF. Runtime is not recorded."),
    ("Build, PDF QA and packaging", "approve_pdf.py",
     "Record a caller's completed visual inspection only if the reviewed-page set equals the rendered set and the PDF hash still matches; hash every included TeX fragment and the bibliography.",
     "The selected logs/pdf_qa/<build>/qa_record.json and logs/PDF_QA_APPROVED.json.",
     "The approval snapshot below records the actual approved build, page count and inspected-page count. Runtime is not recorded. This program neither performs nor substitutes for image inspection."),
    ("Build, PDF QA and packaging", "make_package.py",
     "Create a never-overwritten checkpoint/final ZIP with exact-byte SHA-256 manifest; require approved PDF/source hashes and all mandatory deliverables; for --final require the binding stop review and an INCOMPLETE first line.",
     "../RESEARCH_SA08_checkpoint_*.zip or the supplied final name; PACKAGE_MANIFEST.json inside each ZIP; logs/checkpoint_03_package.json and checkpoint_05_package.json.",
     "Checkpoint 03 receipt: 394 entries, 42233182 bytes. Checkpoint 05 receipt: 679 entries, 85624809 bytes. Creation timestamps are recorded, but runtime is not recorded. The exclusions cover fetched publications/original scans, original attachments, earlier ZIPs and transient files; approved QA images are retained."),
    ("Build, PDF QA and packaging", "B_operational_inventory.py",
     "Read existing program sources, named receipts and registers; assemble this inventory and a source-hash coverage receipt without rerunning any inventoried program.",
     "notes/OPERATIONAL_PROGRAMS.md; logs/B_operational_inventory.json.",
     "Its own exact runtime and program/category counts are recorded in logs/B_operational_inventory.json. It adds no mathematical result, source download, build or approval."),
    ("Build, PDF QA and packaging", "final_audit.py",
     "Verify the final report, result/event registers, bibliography access markers, binding stop state and approved PDF/source hashes; require every saved program filename to appear in the report. This is a release consistency audit, not a mathematical proof or visual inspection.",
     "logs/FINAL_AUDIT.json, produced after the final report is assembled; reads the final report/registers, register_audit.json, PROGRESS_REVIEW_03.json and PDF_QA_APPROVED.json.",
     "The intended release inputs contain 24 requested outcome rows, 118 statement/label rows, 352 events, 68 marked bibliography entries, 124 PDF pages, 47 approved source hashes and 76 reviewed pages. Actual validation counts, individual check results and runtime will be recorded in logs/FINAL_AUDIT.json; no completed execution is claimed by this inventory."),
]

MATHEMATICAL = {
    "A_binomial_obstruction.py", "A_exterior_pd_bar.py", "A_model_comparison.py",
    "A_numerical_differentials.py", "A_numerical_tail_pairings.py", "A_t0_sphere2.py",
    "B_audit_numerical_lattices.py", "B_bar_arity3_checks.py", "B_check_fermat_pushout.py",
    "B_check_prime_pd_ideal.py", "B_finite_checks.py", "B_pd_square_next_obstruction.py",
    "B_pd_square_normalization.py", "C_bar_boundary_countercheck.py", "C_finite_obstructions.py",
    "C_rational_saturation_countercheck.py", "C_signed_shuffle_checks.py",
    "D_A3_cocycle_check.py", "D_bar_closure_check.py", "D_bar_indecomposables.py",
    "D_bar_mixed_counterexample.py", "D_derived_binomial_weight2.py",
    "D_elementary_source_checks.py", "D_filtered_lattice_gate.py", "D_finite_pd_checks.py",
    "D_first_stage_obstruction.py", "D_lifting_counterexample.py", "D_pd_cancellation_warning.py",
    "D_shift_quadratic_checks.py", "D_tail_H3_certificate.py", "D_tail_differential_H2.py",
    "D_tail_differential_image.py", "D_tail_integral_horizontal.py", "D_tail_integral_modp.py",
    "D_tail_vertical_multidegree.py", "D_tail_vertical_threevars.py",
}


def escaped(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, data):
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
        *["| " + " | ".join(escaped(x) for x in row) + " |" for row in data],
    ])


def json_stream(path):
    decoder = json.JSONDecoder()
    text = path.read_text().strip()
    output = []
    while text:
        value, end = decoder.raw_decode(text)
        output.extend(value if isinstance(value, list) else [value])
        text = text[end:].lstrip()
    return output


programs = sorted(p for p in (ROOT / "code").iterdir() if p.suffix in {".py", ".lua"})
operational = {row[1] for row in ROWS}
assert len(operational) == len(ROWS), "Duplicate operational entry"
assert not operational & MATHEMATICAL
assert {p.name for p in programs} == operational | MATHEMATICAL, "Unclassified or missing program"
stamp = datetime.now(timezone.utc).isoformat()
chunks = [
    "### Scope and evidence conventions\n\n"
    f"Inventory snapshot: {stamp}. This records all {len(operational)} operational programs in `code/`, "
    f"including the inventory writer, separately from the {len(MATHEMATICAL)} mathematical programs described in the computation record "
    "(including the final C35 certificate). Every program filename below was checked against its saved source. "
    "Generated `__pycache__/*.pyc` files are not additional programs. No download, research computation, registry writer, "
    "typesetter, approval or packaging command was executed to prepare this inventory.\n\n"
    "All paths below are relative to `SA08_work/` unless prefixed by `../`; programs are under `code/`. "
    "Counts labelled **source payload** describe the saved program, not a new execution. Durations are copied from "
    "existing receipts; **not recorded** means no duration for that operation was found in its preserved output. "
    "File timestamps, UTC review/creation stamps and download timeout settings are never treated as runtimes. "
    "Separate or concurrent request durations are not added and called wall time. Source-download success does not "
    "establish that a theorem was opened or applicable; those scopes remain in the bibliography and source notes. "
    "Fetched third-party full texts and archive images remain excluded from the distribution package; their receipts are included."
]
for category in dict.fromkeys(row[0] for row in ROWS):
    entries = [row for row in ROWS if row[0] == category]
    chunks.append("### " + category + "\n\n" + table(
        ["Program", "Actual purpose", "Output / receipt references", "Recorded counts and runtime"],
        [("`" + name + "`", purpose, outputs, counts) for _, name, purpose, outputs, counts in entries],
    ))

# Generic root fetch requests, including successful responses that required
# later publication-identity verification.
root_receipts = sorted({
    *list((ROOT / "logs").glob("A_*fetch*.jsonl")),
    *list((ROOT / "logs").glob("source_fetch*.jsonl")),
})
fetch_rows = []
for path in root_receipts:
    for record in json_stream(path):
        fetch_rows.append((path.name, record.get("file", "not recorded"), record.get("bytes", "not recorded"),
                           record.get("seconds", "not recorded"), record.get("error", "response saved")))
chunks.append("### Generic source-fetch run receipts\n\n"
              "These are the surviving `fetch_sources.py` request records from the root run. Their original JSON also retains the requested/final URL and response type.\n\n" +
              table(["Receipt under logs/", "Response saved under sources/", "Bytes", "Seconds", "Outcome"], fetch_rows))

b_literature_stems = [
    "B_cartan1954_exp7", "B_cenkl1989", "B_cenkl_porter1984_ast",
    "B_cenkl_porter1984_cubical", "B_cenkl_porter1984_true", "B_dold_puppe1961",
    "B_goerss_jardine", "B_roby1963", "B_sullivan1977",
]
# There are nine one-off B_fetch_literature receipts; Serre has its own program.
assert len(b_literature_stems) == 9

source_rows = []
for receipt in ["B_source_downloads.json", "B_additional_downloads.json", *[s + "_fetch.json" for s in b_literature_stems], "B_relative_literature_fetch.json"]:
    path = ROOT / "logs" / receipt
    for record in json_stream(path):
        name = record.get("name", Path(record.get("file", "not recorded")).name)
        status = record.get("status", "response saved" if "bytes" in record else "not downloaded")
        if "error" in record:
            status += ": " + record["error"]
        if "corrected_file" in record:
            status += "; relabelled " + Path(record["corrected_file"]).name + "; unrelated article"
        source_rows.append((receipt, name, record.get("bytes", "not recorded"),
                            record.get("seconds", record.get("runtime_seconds", "not recorded")), status))
chunks.append("### B download and one-off source receipts\n\n"
              "These are individual persisted receipts. The three `already_downloaded` rows measure only cache reads and hashing; "
              "their original download durations are **not recorded in the surviving latest receipt**. The Anick failure is retained.\n\n" +
              table(["Receipt under logs/", "Requested file / source", "Bytes", "Recorded seconds", "Recorded outcome"], source_rows))

range_rows = []
for name in ["B_cote136_ranges.txt", "B_cote136_ranges_retry.txt", "B_cote136_ranges_selected.txt", "B_cote136_ranges_strict.txt"]:
    path = ROOT / "logs" / name
    records = []
    for line in path.read_text().splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "start" in record:
            records.append(record)
    range_rows.append((name, len(records), sum(x["bytes"] for x in records),
                       ", ".join(str(x["seconds"]) for x in records),
                       "59.75233911300165 s; completed scans 142–145" if "strict" in name else "not recorded; no completion receipt in this transcript"))
chunks.append("### Preserved range-fetch retries\n\n"
              "These earlier transcripts are separate from the three completed-range JSON receipts. The rows count only complete range records actually written to each transcript; "
              "reused blocks and unlogged interrupted transfers are not inferred.\n\n" +
              table(["Transcript under logs/", "Logged complete ranges", "Logged bytes", "Per-range seconds", "Whole-run duration / completion"], range_rows))

build_rows = []
build_command_count = 0
for path in sorted((ROOT / "logs").glob("build_driver_*.jsonl")):
    records = json_stream(path)
    build_command_count += len(records)
    build_rows.append((path.name, len(records), ", ".join(str(x["code"]) for x in records),
                       "; ".join(str(x["seconds"]) for x in records),
                       "; ".join(x["log"] for x in records)))
chunks.append("### Build-driver receipts\n\n"
              "Each duration belongs to the command in the same position in the saved receipt; commands and arguments remain in the JSONL. "
              "These are measured subprocess runtimes, **not** a complete elapsed-time total for the research or build session. "
              "Nonzero exit codes preserve failed attempts.\n\n" +
              table(["Driver receipt under logs/", "Commands", "Exit codes in order", "Command seconds in order", "Diagnostic logs under logs/"], build_rows))

qa_rows = []
for path in sorted((ROOT / "logs/pdf_qa").glob("*/qa_record.json")):
    record = json.loads(path.read_text())
    reviewed = record.get("visual_review", "not recorded")
    state = "passed explicit recorded inspection" if reviewed.startswith("Passed") else reviewed
    qa_rows.append((str(path.relative_to(ROOT)), record["pages"], record["rendered_page_count"], record["overfull_after"], state, "not recorded"))
chunks.append("### PDF-QA receipt snapshots\n\n"
              "A rendered page count is not an inspection count unless the saved review field records inspection. "
              "The exact PDF hash and full page lists remain in each JSON; earlier unapproved renderings remain unapproved.\n\n" +
              table(["QA record", "PDF pages", "Rendered pages", "Overfull boxes", "Saved review state", "Runtime"], qa_rows))
approved = json.loads((ROOT / "logs/PDF_QA_APPROVED.json").read_text())
chunks.append("At this inventory snapshot, `logs/PDF_QA_APPROVED.json` names `" + approved["build_log"] + "`, "
              f"{approved['pages']} PDF pages and {approved['rendered_page_count']} inspected rendered pages; "
              f"{len(approved.get('source_sha256', {}))} included source files have recorded hashes. "
              "The approval UTC is `" + approved.get("approval_utc", "not recorded") + "`. "
              "The approval runtime is **not recorded**. Later approved builds, if any, require their own receipt and cannot inherit this approval.")

review_rows = []
for n in range(1, 4):
    path = ROOT / "logs" / f"PROGRESS_REVIEW_{n:02d}.json"
    if not path.exists():
        review_rows.append((path.name, "not present at inventory snapshot", "not recorded", "not recorded"))
        continue
    record = json.loads(path.read_text())
    count = record.get("consecutive_no_movement", record.get("consecutive_no_movement_reviews", "not recorded"))
    when = record.get("recorded_utc", record.get("actual_utc", "not recorded"))
    review_rows.append((path.name, when, count, "not recorded"))
chunks.append("### Formal-review receipt state\n\n"
              "The second review has a saved receipt but no separate `record_review_02.py` in `code/`; this inventory does not invent one.\n\n" +
              table(["Receipt under logs/", "Actual UTC stamp", "Consecutive no-movement reviews", "Runtime"], review_rows))

chunks.append("### Coverage and provenance limitations\n\n"
              "All operational Python/Lua files in `code/` are enumerated above. The D run's source searches and opened-scope inventories are retained in "
              "`logs/D_source_searches.tsv`, `logs/D_global_repair_source_searches.tsv`, `logs/D_late_source_inventory.tsv` and "
              "`logs/D_sources_do_not_package.tsv`; there is no separate D-prefixed download program in `code/` to enumerate. "
              "This is a program inventory, not a claim that every interactive shell command or tool request had a standalone script. "
              "A later final-report or ZIP operation may postdate this snapshot; its new receipt supplies its own counts. "
              "No missing download duration, build wall time, edit count or packaging runtime has been reconstructed from timestamps.")

text = "\n\n".join(chunks) + "\n"
destination = ROOT / "notes/OPERATIONAL_PROGRAMS.md"
destination.write_text(text)
receipt = {
    "snapshot_utc": stamp,
    "output": str(destination.relative_to(ROOT)),
    "operational_programs": len(operational),
    "mathematical_programs_separately_reported": len(MATHEMATICAL),
    "source_programs_total": len(programs),
    "root_fetch_request_records": len(fetch_rows),
    "B_download_request_records_in_supplement": len(source_rows),
    "build_driver_receipts": len(build_rows),
    "build_commands_with_recorded_durations": build_command_count,
    "QA_receipt_snapshots": len(qa_rows),
    "unclassified_programs": [],
    "program_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in programs},
    "inventory_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "runtime_seconds": time.perf_counter() - START,
    "method": "Read existing source and receipts only; only this inventory writer executed, with no earlier operational or mathematical program rerun.",
}
(ROOT / "logs/B_operational_inventory.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({k: v for k, v in receipt.items() if k != "program_sha256"}, indent=2))
