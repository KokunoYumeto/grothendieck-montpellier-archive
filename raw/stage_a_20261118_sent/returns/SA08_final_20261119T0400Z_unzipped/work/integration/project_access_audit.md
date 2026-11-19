# Bounded project-target access audit

Date: 19 November 2026. Checker: GPT-6 Astra Pro; effort not exposed by runtime; SA08/early.

**Conclusion:** The exact external targets were not resolved by this bounded available-file search. This is an access limit, not evidence that the documents are unavailable everywhere. The reported project links remain provenance-only; no new mathematical implication or two-endpoint result was accepted.

The check covered La Longue Marche, Les Dérivateurs, README sections S6/S11, WG2, PATHS, PRETOT/TOTASPH, and the named `136.modern.tex`, `ps6.tex` and `RESULTS_STATE.md` context files. Exact title/filename searches returned no matches. One simpler retry per target family returned prior prompts mentioning those projects or unrelated fuzzy candidates, not the target documents themselves. Those snippets were not used as source evidence.

There were five search calls and 21 query objects. The ranked retries were deliberately bounded (20,20 and10 records); continuation streams were not exhausted. No target document was read, no attached source was opened through Library, and no Library item was changed. Unrelated snippets and other file contents have been omitted from the retained audit.

| Query | Mode | Batch |
|---|---|---|
| "La Longue Marche" | Title/filename | 1 |
| "Les Dérivateurs" | Title/filename | 1 |
| "README.md" | Title/filename | 1 |
| "WG2" | Title/filename | 1 |
| "PATHS" | Title/filename | 1 |
| "PRETOT" | Title/filename | 2 |
| "TOTASPH" | Title/filename | 2 |
| "136.modern.tex" | Title/filename | 2 |
| "ps6.tex" | Title/filename | 2 |
| "RESULTS_STATE.md" | Title/filename | 2 |
| Longue Marche | Short/content retry | 3 |
| Derivateurs | Short/content retry | 3 |
| README S6 | Short/content retry | 3 |
| README S11 | Short/content retry | 3 |
| WG2 | Short/content retry | 3 |
| PATHS A.5 | Short/content retry | 4 |
| PRETOT | Short/content retry | 4 |
| TOTASPH | Short/content retry | 4 |
| 136.modern | Short/content retry | 4 |
| ps6.tex | Short/content retry | 4 |
| RESULTS_STATE | Short/content retry | 5 |

Exact request options and aggregate outcomes are retained in `project_access_audit.json` and `logs/early_project_library_search_001.json` through `_005.json`. These are access metadata only.

Suggested dossier sentence: “The exact external targets were not resolved by a bounded search of the available files; their reported links therefore remain provenance-only, without a verified second endpoint.”
