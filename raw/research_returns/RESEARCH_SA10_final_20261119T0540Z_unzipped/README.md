# RESEARCH_SA10

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November2026. No priority claimed.

Start with `RESEARCH_SA10_report.md` for the complete outcome table, exact scopes, source/correction record, computation catalog and publication checks. The mathematical deliverable is `RESEARCH_SA10_paper.pdf`, with its LuaLaTeX source and all directly included proof files beside it. There are74 numbered results, one per row in `RESEARCH_SA10_results.csv`.

`CHECK_EVENTS.tsv` records actual checks, including inherited statement IDs. `PROGRESS_LEDGER.md` preserves dated running gate updates and checkpoint events. `FINAL_register_audit_B56.md` is the statement/citation/register consistency audit. `qa/` and `PDF_VISUAL_*.md` contain rendered-page and visual inspection records; `logs/build_summary.json` contains final build metrics.

## Rebuilding

On a complete LuaLaTeX installation, run `lualatex RESEARCH_SA10_paper.tex`, `bibtex RESEARCH_SA10_paper`, then LuaLaTeX twice. `code/build_paper.py` records the task-local fallback used in this environment. It detects missing support packages and expects their task-local location; `code/fetch_tex_support.py` records how that location was populated. The generated `.bbl` is included, so a normal installation can also use the supplied bibliography output directly. No fetched research article is needed to compile the paper.

The final-proof inputs are `sections_A.tex`, `B_levels.tex`, `B56.tex`, `C_sections.tex`, their explicitly included C assistance files, and `unresolved.tex` (its retained historical filename now contains the completed verification/scope section). `C_sections.tex` is a complete generated deliverable; rebuilding the paper does not require regenerating it from Markdown.

All saved programs and their outputs appear in the original directories and are indexed in `PROGRAM_AUDIT.md`; the final `code/programs/` mirror puts the auxiliary code directories under the requested `code/` tree while retaining the original paths used in the paper and historical logs. The mirror is a delivery copy, not a second source of truth. Paths containing the original scratch prefix are historical run locations, not required installation paths.

## Historical records

Working notes, individual contribution reports and failed-build logs are retained to document how gates were closed. Their earlier pending-status language is historical. The final report, main paper, aggregate results and final audit govern the delivered conclusions. In particular, `code/update_working_report.py` is an archived working-stage generator and must not be used to replace the final report; use `code/finalize_report.py` for the final assembly.

The final archive excludes the user-supplied attachments, manuscript scans and fetched full-text research sources. Bibliography entries, exact locators, source manifests, failed-access records and all original mathematical work are included. Every earlier checkpoint archive remains separate.
