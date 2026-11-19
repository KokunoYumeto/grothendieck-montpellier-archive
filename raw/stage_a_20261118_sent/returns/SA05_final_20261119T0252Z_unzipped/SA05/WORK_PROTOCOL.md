# SA05 work protocol

Primary task: attached PROMPT(4).md. Deliver a single SA05.zip containing all requested stages. The older zipped prompt differs only in checkpoint and interruption rules; use the separate attached prompt.

Source paths are relative to the workspace: `sources/notes/NOTES_INDEX.tsv`, `sources/notes/pro/`, `sources/notes/codex/`, `sources/texts/pro/`, `sources/texts/codex/`. Original sources are excluded from deliverable ZIPs. Physical line numbers refer to the supplied UTF-8 files, counting from 1. A locator must include the filename and scan as well as line(s); Pro and Codex physical line numbers are not interchangeable.

All judgments require actual reading of entry and passage. Automation may expose and validate coverage, never generate a verdict from headings or keywords. Compare quotations and quantifiers. Distinguish Grothendieck's manuscript, reused typescripts or offprints (with their actual author), earlier-run ideas, and current reconstruction. Context outside this part has no direct witness unless an attached transcription contains it. Do not manufacture a locator.

Use JSON items with the fields requested in PROMPT. For multiple substantive claims bundled into one indexed entry, one source may support several items; the entry verdict points to its main item and names additional item IDs in the reason. Conversely consolidate actual duplicates. Record source-level coverage and claims explicitly.

Each claim requires a literature search and a search-ledger entry linking query, searched venue, outcome, opened URLs, and claim IDs. An opened reference is `verified` only to the extent actually viewed: identify whether metadata, abstract, theorem text, or full text was checked. A reference cannot certify a stronger theorem than the viewed content. Use primary mathematical sources for conclusions; MathOverflow is a lead or search record. Searches may be batched by exact mathematical family, but each claim must be mapped to the relevant searches and exact result.

Check-events columns: statement_id, date, who, type, outcome. Use the user's exact event types. Provenance review is recorded as `carried as background without fault found` with an explicit note that this does not assert mathematical proof. Record mathematical targeted proof checks, re-proofs, computations, and refutations separately. Do not assign a stronger event type than occurred.

Write work progressively under `SA05/work/<owner>/`. Store all runnable programs and their saved outputs under that owner's directory, including computations. Save source read ledgers (files/line intervals actually read) and reference/search ledgers. Root maintains final files, progress.log and timed checkpoints. Do not upload independently. Do not include supplied attachment bytes in checkpoints or final ZIPs.

Final class letters: A own later published result; B developed by others; C partly developed with precise residual; D no development found in recorded searches (never proof of absence); E established before manuscript; F exact claim cannot be identified from supplied pages. Date present status 2026-11-19, with literature verified only as available on that date.

Temporary ID allocation: root items/claims/problems 1–999; cote11a 1001–1999; cote11b 2001–2999; cote12c 3001–3999. Root can perform a documented final renumbering and cross-package merge. Items SA05-<n>, claims SA05-C<n>, problems MP-SA05-<nn>. Links or research directions outside the topic must be kept in their own table and attributed to prior runs.
