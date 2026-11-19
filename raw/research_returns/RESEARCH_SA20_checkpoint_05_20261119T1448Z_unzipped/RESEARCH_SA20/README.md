# RESEARCH_SA20 working package

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

This is an active, INCOMPLETE research package. Read RESEARCH_SA20_report.md and PROGRESS_LEDGER.md for exact status. The current194-page PDF has passed strict compilation and visual QA. The outcome table states the remaining research tasks; this is not the final stopping report.

## Reproduce

Run the mathematics verification programs in code/ and agents/*/code/. Their exact outputs are in logs/ and agents/*/logs/. The finite certificates and the all-arity proofs serve different purposes; a finite cutoff is never claimed as a proof in arbitrary arity.

Run python3 code/assemble_records.py from this directory to assemble current CSV, TSV, and BibTeX records. Compile RESEARCH_SA20_paper.tex with LuaLaTeX and BibTeX, then LuaLaTeX twice; read the full log and render before delivery. The task-local build script handles the available LuaLaTeX runtime; no unreviewed PDF should replace the recorded version.

Downloaded original sources and manuscript scans are omitted from checkpoints; their URLs and access records are in the bibliography, reports and source manifests. The user-supplied source archive is also omitted. Checkpoints contain the entire current research work, not prior checkpoints.

The current PDF range extractor retrieves selected original cote119 pages without requiring a 145MB full download. Its selected-page order is recorded in logs/119_range_access.json for that completed retrieval.

Pending proof notes, if present, are research drafts outside the checked statement inventory. Their inclusion preserves work in progress; it does not promote their claims to proved results.
