# Targeted audit of the root Pfluger OCR inventory

19 November2026,17:35–17:39UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; agent `part_c_algebra`.

## Conclusion and exact scope

**The165 `frontmatter` values in `code/root_pfluger_public_ocr_inventory_output.json` are raw non-user OCR source-cache payloads, not authored analysis.** They are1600-character text prefixes associated with individually identified source records. Authored/derived results—source identities, years, match counts, errors and timings—are separate fields and must remain unchanged. This classification concerns the deliverable's purpose; it makes no copyright-status judgment about the old issues.

Only this JSONfile and its exact-name `.txt` companion were inspected. No other file was proposed for normalization; no source request, mathematical check or original utility rerun occurred. Neither reviewed input has been modified by this assessment.

The JSON has166result records. Exactly165contain `frontmatter`, each1600characters, totaling264,000characters and453,090UTF-8bytes. Record140is the original HTTP500error and has no frontmatter field; it is untouched. Every successful record has integer `matched_terms:0` and an empty `excerpts` array. The aggregate remains182catalogue records,166eligible OCRfiles,166requested files, one error, no candidate files, and original total elapsed469.04178680599944seconds.

## File identity and the TXT distinction

| Existing file | Bytes | SHA256 | Proposed action |
|---|---:|---|---|
| `code/root_pfluger_public_ocr_inventory_output.json` |900912|`2b339aee5d5c46ba07cdb29d27910f73402b42697d196b84d0e46dfd16c8bf27`|Replace only165listed raw frontmatter strings after authorization.|
| `code/root_pfluger_public_ocr_inventory_output.txt` |704|`db3f638df477371c8c4872bc04a5809b183135e40a346c2b78a237076e5d407b`|Retain byte-for-byte.|

The TXTcompanion is **not an exact duplicate** or a JSONsource payload. It contains eight original progress-record lines and the terminal aggregate summary. These are useful execution outputs, including historical elapsed times. It contains no frontmatter OCR and should not be normalized. The initial read correctly distinguished its multi-record format from a single JSONdocument; `matched_terms` was likewise confirmed to be an integer count, not a list.

## Exact field-level plan

The complete proposal is `checks/part_c_root_ocr_frontmatter_plan.json`, SHA256 `a9b418e6a3fae5e242d43992635e6cb0f780197de4f59e74fda1504219575c5e`. It lists `/results/i/frontmatter` for every index0through165except140, with each record's identifier, field length, UTF-8byte length and SHA256. No source body is repeated in the plan.

The proposed replacement retains the same `frontmatter` key but replaces its raw string with a provenance object containing `kind`, exact external raw-cache path, original JSONpointer, original character count, original UTF-8byte count and original fieldSHA256. The raw backup would be the exact900,912-byte original JSONfile at `/workspace/scratch/9c53b536a97f/source_reading/root_pfluger_ocr_frontmatter/root_pfluger_public_ocr_inventory_output.json`. That backup has not yet been created or claimed as verified.

Before any write, a deterministic normalizer must verify the whole-file hash and all165field hashes; save and verify the exact original bytes outside the project; preserve every unselected JSONvalue; and verify deep equality after masking only the165selected frontmatter fields. It must separately verify that the704-byte TXTcompanion remains unchanged. A new manifest must record original/replacement hashes and the normalization-only runtime without altering any original timing value.

All existing identifiers, filenames, titles, dates/years, URLs, source byte counts/hashes, statuses, cached/saved values, `frontmatter_years`, match counts, excerpts arrays, errors, exclusions, aggregate counts and elapsed times remain exactly as recorded. No theorem or original-source access status changes.

## Relation to the earlier bounded hygiene pass

The earlier general inventory explicitly left these bounded diagnostic prefixes outside its first normalization proposal. This new targeted review addresses their aggregate source-cache role at the parent's request. It does not reclassify the separately useful derived diagnostics as raw literature. Moving just the prefixes into the external cache preserves their reproducibility while retaining every result needed to assess the failed-source inventory.

`code/part_c_root_ocr_frontmatter_plan.py` actually ran at17:38:20.717930UTC with measured elapsed0.016578356000536587seconds. It read only the two reviewed inputs, wrote this separate plan/output, made zero network requests and ran zero mathematical checks. The exact proposal was sent to the parent; input mutation awaits explicit authorization.
