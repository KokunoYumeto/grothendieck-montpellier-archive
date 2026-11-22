# Existing-log runtime audit (no reruns)

Date:2026-11-19. The exact audit start/end clock times were not separately recorded. This reporting audit inspected existing scripts, their retained outputs, named notes and timing records. It did not execute any of the audited scripts, rerun a mathematical certificate, or infer durations from file timestamps, HTTP timeouts, or a later similar run.

| Historical script/version | Actually retained runtime | Exact existing evidence and interpretation |
| --- | --- | --- |
| `code/part_a567_fetch_sources.py` | **Unrecorded** | `code/part_a567_fetch_sources.out` is0bytes. `sources/part_a567_fetch_sources.out` is597bytes and has7human-readable retrieval/cancellation lines, none timed. Script lines16,22–23 measure per-job durations, but no resulting timed records survive in these outputs. There is no retained whole-batch timer. The50-second argument is a network timeout, not elapsed-time evidence. |
| `code/part_a567_retrieval_metadata.py` | **Unrecorded** | `code/part_a567_retrieval_metadata.out` is3650bytes and preserves8API outcomes. Full metadata is `sources/part_a567_retrieval_metadata.json`; neither has a timing field. The script has no elapsed-time instrumentation. Its22-second argument is a timeout, not a duration. |
| `code/part_a567_legacy_ids.py` | **Unrecorded** | `code/part_a567_legacy_ids.out` is219bytes,3status lines. The script preserves21original IDs and lead mappings but has no elapsed-time instrumentation. |
| `code/part_a567_audit_update.py` | **Unrecorded** | `code/part_a567_audit_update.out` is243bytes,5status lines (29numbered statements,24citation keys,10review events at that historical run). No timing field or timer exists. It is a one-shot historical mutation and was not rerun. |
| `code/part_a567_ocr_sources.py` | **41.446637seconds** | `code/part_a567_ocr_sources.out`, line3, reads `Wall seconds 41.446637`. Lines1–2 record12Nakamura1990pages/28616characters and27Ihara–Nakamura1997pages/60472characters. Script line16starts `time.perf_counter()` after imports/job setup; line49prints the difference after rendering, OCR, output writing and temporary-directory cleanup. This is the retained internal wall duration for that document-processing block, not full interpreter-startup time or a mathematical verification runtime. |
| `code/part_a567_checks_initial.py` | **Unrecorded** | `code/part_a567_checks_initial.out` is4147bytes and ends with the recorded wrong-reflection failure. The final timer print at script line104was not reached. The initial timer exists at line9, but a start point alone gives no duration. |
| `code/part_a567_checks_second.py` | **Unrecorded** | `code/part_a567_checks_second.out` is4580bytes and preserves the line90unsimplified polynomial-expression equality failure and correction explanation. The final timer print at line104was not reached. No historical duration is recoverable from those saved records. |

The failed mathematical versions' scope and failure causes are already documented in `notes/part_a567_program_scope.md`, initial and second version subsections. The successful final main-check runtime0.236781seconds belongs only to `code/part_a567_checks.py`, not either failed version. Likewise `code/part_a567_timing_audit.json` contains later explicitly authorized timing-only runs of four different small scripts (collar, characteristic3, characteristic2, plumbing); none may be substituted for the seven rows above. `notes/runtime.json` records environment/setup facts and a project start time, not these program durations.

## Retained fetch-status text outside the excluded source cache

For archive completeness, the existing597-byte human-readable file `sources/part_a567_fetch_sources.out` said:

1. `hoshi_mochizuki_2011: downloaded; 405874 bytes; pdftotext succeeded.`
2. `mochizuki_2006: downloaded; 724608 bytes; pdftotext succeeded.`
3. `mochizuki_2007: downloaded; 235788 bytes; pdftotext succeeded.`
4. `alling_1981_preview: downloaded; 582613 bytes; pdftotext succeeded.`
5. `stukow_2004: downloaded; 98843 bytes; pdftotext succeeded.`
6. `bakalov_kirillov_2000: downloaded; 581984 bytes; pdftotext succeeded.`
7. `MilneEC2 and duplicatecote67 fetch cancelled by SIGINT after slow network transfer; no partial file written. Both remained opened viaweb forMilne andtranscription forcote67. Root separately fetchedcote67.`

Those are preserved historical outcomes, not measured durations. At root's explicit request, the entire597-byte existing log was also copied without modification to `code/part_a567_fetch_sources_source_log.out`; the empty historical `code/part_a567_fetch_sources.out` remains unchanged. Later actual source openings and status updates are separately recorded; this audit does not reset their current status. The machine-readable reporting crosswalk is `checks/part_a567_historical_runtime_audit.csv`. No mathematical or source-opening status changed in this audit.
