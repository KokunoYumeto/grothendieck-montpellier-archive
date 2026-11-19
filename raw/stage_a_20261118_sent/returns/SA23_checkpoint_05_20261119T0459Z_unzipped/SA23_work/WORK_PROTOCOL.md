# SA23 work protocol

Controlling instruction: supplied `PROMPT(3).md`. Earlier `SA23_PROMPT.zip/PROMPT.md` differs only in checkpoint and disconnection handling. First checkpoint due 2026-11-19 01:59:45 UTC, then every 45 minutes while working. Do not include the supplied attachments or earlier checkpoint ZIPs in a checkpoint.

All locations use one-based physical lines in the supplied `.tex` file, alongside its cote and scan marker. Retain transcription disagreements; no ink is available to adjudicate them. The three API texts use their own printed page/section marks where no scan marker exists.

Each topic owner writes independent files in `parts/<owner>/`: `items.json`, `entries.tsv`, `claims.json`, `problems.json`, `readings.tsv`, `links.tsv`, `references.bib`, `check_events.tsv`, `search_log.jsonl`, `coverage.md`, `section.md`, `directions.md`, and computational programs with saved outputs. Save increments, not merely a final answer. Each indexed note receives a manually reasoned entry verdict based on reading the actual note and relevant transcription. Exact source passages and read logs make the work inspectable. A read log is not a mathematical verification event.

Item ID reservations: root 1–100; ega 101–200; bt 201–300; misc 301–400. Claims may use `C-SA23-<owner>-nnn`, problems `MP-SA23-<owner>-nn`; integration can renumber consistently. Every material claim, open flag, and computation must be captured; no automatic inference of correctness from headings or note summaries.

Preserve three evidence layers: manuscript wording; checked external source; present reconstruction. Earlier-run project links are only leads and must remain separate from archival and published links. Searches must be logged with exact query, sources/results, date, mapped claim IDs, and limits. Verified bibliography means the link or DOI was opened, not that every assertion in the work was proved in this run. Date current status to 19 November 2026; distinguish circulation/publication dates when verified.

Do not invent research-run settings. `who` records model GPT-6 Astra Pro, effort not independently exposed, run SA23-20261119 and owner. Check types must state what actually occurred; reading alone does not count as proof checking. Finite computations do not prove unrestricted assertions.
