# DP_MULT research package

Run DP_MULT_20261121; 21 November 2026, UTC. Early event records preserve their original date labels; exact later timestamps use UTC.

The authoritative mathematical deliverable is DP_MULT.tex. QUESTIONS.tsv records each treated question; CHECK_EVENTS.tsv records actual proof/source/computation checks; LEDGER.md records progress and remaining gates; IMPLICATIONS.md states the programme consequences; TRANSCRIPTION_NOTES.tsv holds five exact-line mathematical emendation candidates, with original-page evidence distinguishing source slips from transcription errors.

This is a working checkpoint until the final ZIP is explicitly issued. The broad new-construction question about fewer theta lifts remains open, although the local bound is proved and the literal unchanged-interface proposal is refuted. Newly integrated proof reviews and final PDF layout are being reconciled.

The research directory preserves complete mathematical derivations, source-interface reviews, failed approaches, check records and reproducible exact-arithmetic code. INPUT_MANIFEST.tsv fingerprints the original attachments and their once-unpacked contents. AUTHOR_SOURCE_MANIFEST.tsv and the successive verification JSONs record the 1029 targeted modules: 526 checked in the recorded full sweep and 503 directly extracted from the original14-part author archive with exact member and byte hashes. No Lean compilation is claimed. External source PDFs, manuscript source images, full archive parts and build caches are inputs/intermediates rather than redistributed report artifacts; exact URLs, paths and hashes permit recovery. The supplied attachments remain the input source of record.

Build the paper with a standard current pdfLaTeX installation, running twice for cross-references. Run `python3 research/check_formal_bounds.py` for the finite arithmetic diagnostics. The script `research/verify_author_archive.py` compares recovered modules with the original split archive without unpacking the whole archive; its command-line help explains the required input directories.
