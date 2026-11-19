# SA14 research protocol

Run: SA14-20261119. Sources: the supplied SA14_Picard.zip, extracted once into ../sources. The attached PROMPT governs scope. No scans or second-pass files are supplied. No ink decisions may be made and no source transcription may be modified.

Start: 2026-11-19 13:00 UTC (initial reads); checkpoint clock base 2026-11-19 13:01:52 UTC (first recorded clock). Due checkpoints every 45 minutes: 13:46:52, 14:31:52, etc. Root alone saves checkpoint ZIPs and final ZIP. Source inputs and previous checkpoint ZIPs are excluded.

Line locators are one-based physical lines of the exact supplied .tex file, not reconstructed manuscript line numbers. Always name the source file for an absolute line range. Scan numbers are the supplied \\scanpage values, not internal manuscript page numbers. These distinctions must appear in final dossier.

All note verdicts must be authored after reading the actual note and the relevant transcript passage. Scripts may prepare packets, calculate, join, validate and count; they may not infer verdicts from headings or keywords. All transcript text in every file must be read to find claims absent from notes.

Keep manuscript statements, current literature results, earlier runs' ideas and our reconstructions separate. Correcting a note is allowed; correcting the transcription without ink is forbidden. Non-supplied project/cote endpoints cannot be described as verified: put them in an explicitly quarantined lead record.

Part directories own their files. Each part supplies: entries.tsv, items.json, claims.json, problems.json, readings.tsv, links.tsv, directions.md, references.bib, CHECK_EVENTS.tsv, search_log.tsv, read_log.tsv, synthesis.md, scripts/ and outputs/. JSON fields follow the attached prompt. Added provenance fields are permitted. Save progressively, not only at completion.

Entry verdict vocabulary: kept; merged; corrected; withdrawn; rests on a misreading. Reasons must be individual and evidence based, not generic. Items use prompt kinds and check vocabulary (agrees / overstates / understates / misreads / not on the page). A note about another project is an earlier-run idea or contextual comparison, not automatically a manuscript claim.

Claim IDs: C-SA14-nnn. Root will reconcile IDs after semantic consolidation. Bibliographic keys must be unique descriptive keys. References are verified only if the URL or DOI was actually opened. Record actual search queries, platforms, useful hits, negative results and matching limits. Search claims in sensible related groups but explicitly map each claim to the search events. Distinguish first circulation from publication; do not manufacture circulation dates.

Check events columns: statement_id, date, who, type, outcome. Who: GPT-6 Astra Pro; effort not exposed; SA14-20261119; agent name. Reading a source is a documentary concordance event only, labelled 'used and rechecked in this run' with explicit outcome 'text concordance, not mathematical proof'; do not call it a proof check. Mathematical proof checks need actual reasoning; computations need saved code and output. Every item/claim/reference used must have a truthful event.

Root will audit schemas, 440-entry bijection, all topic folders, source IDs, cross references, bibliography, claim-search mappings, calculation outputs and claims in prose. Completion requires all applicable work in the prompt, with unavoidable source uncertainties represented precisely, never silently filled.
