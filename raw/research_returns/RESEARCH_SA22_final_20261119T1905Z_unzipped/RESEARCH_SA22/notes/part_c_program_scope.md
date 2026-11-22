# Program scope, finite counts, and recorded runtime

Recorded 2026-11-19T12:50:16+00:00 by GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed; part_c_algebra agent).

Each program listed below was actually run. Existing exhaustive checks and floating-point diagnostics were not rerun merely to increase a count. The three short scripts without saved runtimes were rerun once to measure the missing wall time. Internal times start after imports; wall times include interpreter startup, so the columns should not be used to compare algorithmic speed.

| Program (under `code/`) | Arithmetic and scope | Complete tested count | Seconds | What the computation does not prove |
|---|---|---|---:|---|
| part_c_finite_checks.py | Exact integers; exhaustive specified C4 and S3 systems | C4:8 chains,20 symmetry atoms,400 convolution atom pairs,64 alignments,16 torsion pairs; S3:30 profiles per factor,900 rearrangement pairs | 0.041654345 (internal) | A complete certificate for these finite examples and their counterexample values; not a classification of all finite groups. |
| part_c_extensions.py | Exact integers; two specified extensions of C2 | Each extension:4 chains,6 symmetric atoms,36 convolution pairs,16 alignments,8 kernel pairs;2 extension systems total | 0.000707238 (internal) | Certifies nonuniqueness via C4 and C2xC2; not a classification of all extensions. |
| part_a2b_checks.py | Float64 scipy loggamma/digamma; fixed seed22021119 | 1209 Hessians (1200 random+9 specified),30 finite-difference Jacobians,600 monotonicity pairs | 0.383141997 (internal) | Diagnostic evidence only, with no implication of general positivity/injectivity. The analytic proof is A2b-energy and A2b-image. |
| part_a1_cut_checks.py | Exact rational constants in one analytic welding | 2 assertions: derivative interval is strictly negative; endpoint derivatives differ | 0.049863184 (wall) | Certifies the finite arithmetic; collar holomorphicity and failure of a pointed-disc antiisomorphism are proved in the manuscript. |
| part_a1_bordered_checks.py | Exact Fraction arithmetic; one two-jet contradiction | 4 assertions: original jets,nonzero determinant,unique candidate coefficients,zero forced squared lengths | 0.037938974 (wall) | Certifies the 2x2 algebraic contradiction; does not numerically construct caps or establish the analytic range theorem. |
| part_c_b3_audit.py | Exact sparse polynomial arithmetic over Z,F7,F3 | 7 assertions:1 universal coefficient identity,2 discriminant+Cartier examples,1 Legendre coefficient,1 Legendre discriminant | 0.037317177 (wall) | Certifies arithmetic inputs only; cohomology, p-ranks and specialization are justified by the source theorems and proofs. |

## Diagnostic values

All 1209 normalized sampled Hessians were positive. Minimum sampled eigenvalue: 8.39697899191e-06. Maximum normalized symmetry residual: 1.81521464526e-14; maximum scaled finite-difference residual: 1.72401024196e-09. All 600 sampled monotonicity pairings were positive, with minimum 0.278718971118. No finite sample is used as a proof.

## Source-fetch and metadata utilities

`part_c_fetch_sources.py` made3 retrieval attempts: EGA_IV4 downloaded49,852,990 bytes in733.783871 s; HLP downloaded26,986,622 bytes in6.781591 s; Milne local fetch returned406 in4.799427 s (the primary web PDF was separately opened). `part_a2b_fetch_sources.py` made2 attempts: Ahlfors-Bers returned403 in11.651925 s (web PDF separately opened); Solynin downloaded4,227,450 bytes in31.946015 s. These are retrieval times, not mathematical tests; their original JSON outputs retain the SHA256 values and status.

`part_c_make_metadata.py`, `part_a2b_make_metadata.py`, and this final-audit program are record-generation utilities. They are not theorem verifiers and their generated ledger-row counts are not counted as independent mathematical checks.

### Historical metadata-utility runtime audit, 19 November 2026, 15:34 UTC

Existing source/output files and the retained project logs were inspected without rerunning either metadata generator or any source request. Neither generator measures elapsed time in its code. `part_a2b_make_metadata_output.json` and its matching text retain the completion timestamp `2026-11-19T11:51:52+00:00` and counts (four A2b rows, two A1 range rows, eight A2b events, three A1 range events), but no start time or duration. No saved wrapper-duration record for either generator was found in the inspected logs. File timestamps and output row counts are not substitutes for a measured runtime.

| Historical utility | Honest elapsed-time status | Existing evidence |
|---|---|---|
| `part_c_make_metadata.py` | **Not recorded in the retained files inspected.** No elapsed value supplied. | Script and generated PartC records; no saved command-duration or matching runtime output found. |
| `part_a2b_make_metadata.py` | **Not recorded in the retained files inspected.** A completion timestamp is available, not a duration. | Matching outputJSON/TXT, dated11:51:52UTC, with the exact row/event counts above. |
| `part_c_lieberman_ias_identity.py` | **Not recorded before the failed request terminated.** The saved `elapsed_seconds:null` is intentional. | Actual one-request HTTP403/exit1 record preserved in its matching outputJSON/TXT; no source saved or image created; no retry. |

The automatic inventory's earlier wording “see retained command/build log” should not imply that a measured elapsed value for these utilities was actually recovered. No request, mathematical check, or metadata mutation was rerun for this reconciliation. This is documentation maintenance, not movement of a mathematical or original-source gate.

The first C4 JSON-generation run reused the S3 variable `f` when serializing the C4 record. That output-only bug was fixed by retaining `c4_f`, and the mathematical certificate was rerun successfully. The attached current C4 JSON and the complete400-decomposition/64-alignment certificate are the corrected versions; no failed output is presented as a valid witness.

### A2b source-page audit utilities, 19 November 2026, 15:53 UTC

These are source renderers, not mathematical tests. `part_c_a2b_audit_source_pages.py` rendered six already-saved Solynin pages (printed9,21,23,28,32,33), with internal elapsed time0.5113126860014745s, starting15:46:37.519484UTC. `part_c_a2b_audit_admissibility_page.py` rendered printed22, with internal elapsed time0.11904288000368979s, starting15:52:14.764412UTC. Both made zero network requests and ran zero finite or numerical mathematical checks. Matching outputs and the seven image paths are retained. All seven pages were actually displayed and read; four initially truncated displays were reopened individually. The accompanying proof audit did not rerun any earlier diagnostic or finite certificate.

### New A6 scope counterexamples, 19 November 2026, 16:26 UTC

These are new finite certificates for newly identified scope branches, not reruns of old checks. `part_c_a6_scope_certificate.py` passed21 exact rational/integer assertions for two counterexamples: the nonsplit cubic's homogeneous normalization, singular points, branch signs and invariant tensor coefficient; and the Eisenstein quadratic's exact divisibility, nonzero discriminant and ramification-prime arithmetic. It started16:21:16.199169UTC and recorded0.0006688150024274364s internally. The geometric, valuation and log-cover proofs are in `part_a6_scope_supplement.tex`; the program does not replace them.

`part_c_a6_frobenius_certificate.py` passed20 assertions over F16, represented as F2[T]/(T^4+T+1). Its scope includes the3 possible irreducible factors of degree<=2,15 inverse identities,all6 cross-ratio values,all16 Frobenius images,primitive order15 and the cyclotomic-lift relation. It started16:25:30.115335UTC and recorded0.0002809529978549108s internally. The cross-ratio values are [2,3,9,14,15,8], distinct from a²=4 in polynomial-bit notation. The augmented étale-group equivalence is proved by the opened universal-homeomorphism theorem, not by the finite program. Both programs have matching full JSON/text outputs and make zero network requests.

### Distinct Pfluger public-catalogue route, 19 November2026,16:42UTC

`part_c_pfluger_distinct_public_route.py` ran three times, with one ordinary GET and no retry each: UPenn institutional serial record(HTTP200;5.775041263004823s), IITBombay print-journal catalogue(HTTP503;10.017750553000951s), and the actual UPenn-advertised HathiTrust record008320850(HTTP403challenge;5.847043253001175s). The challenged route stopped immediately. There were zero mathematical checks, PDF downloads or OCR runs. Matching outputJSONs preserve starts, URLs, status, byte counts and obtained bodies/links. The separate14web-search queries and4web opens have actual per-tool-call intervals in `part_c_pfluger_distinct_search1`–`search4.json` and `part_c_pfluger_distinct_open1.json`; complete scope and limits are in `notes/part_c_pfluger_distinct_public_audit.md`. No original mathematical source was recovered and no source status was promoted.

### Functor-scope original-sheet renderer, 19 November2026,16:49UTC

`part_c_functor_audit_source_page.py` rendered one already-saved original page(68/043, printedfolio42) for the renewed C.1(d) audit, which was actually displayed/read. Start16:46:04.899805UTC; internal elapsed0.48791543100378476s. Zero network requests and zero mathematical finite/numerical checks. Matching outputJSON preserves the source, one-basedPDFpage43, image path and embedded footer text. Original044 was viewed from its existing image, with no duplicate render or earlier certificate rerun.

### Deliverable-hygiene utilities,19November2026,17:13UTC

These are file inventory/provenance utilities, not mathematical verification or source retrieval. All made zero network requests and ran zero mathematical checks. Authored proofs, mathematical certificates and immutable checkpoints were not edited. Their measured runtimes do not represent the duration of the manual content review.

| Utility under `code/` | Actual scope/startUTC | Measured seconds |
|---|---|---:|
| `part_c_source_cache_hygiene.py` |Read-only inventory/hash:370JSONpayloads outside `sources/`;16:58:47.863248.|1.2151061129989102|
| `part_c_source_cache_plan.py` |Read-only exact selection proposal:5direct exclusions,11embedded files,2optional thumbnail files;17:02:25.458928.|0.008342838002135977|
| `part_c_normalize_source_payloads.py` |Parent-authorized11file/51field-block normalization, exact raw backups before writes, all3JSON/TXTpairs remain identical;17:06:37.134280.|0.022700369998347014|
| `part_c_remaining_web_bodies.py` |Read-only inventory of196actual MCPsource blocks in22files;17:10:21.439312.|0.24630621299729683|
| `part_c_remaining_web_plan.py` |Read-only second proposal:15files/50nonoverlapping ranges, including12partial prose spans preserving catalogue data;17:13:12.727210.|0.017585273999429774|
| `part_c_normalize_remaining_web.py` |Parent-authorized second plan:all15file/50range hashes verified, all external raw backups verified before writes, every unselected text segment/JSONfield retained;17:14:57.099346.|0.02573737399507081|

The first normalization's summary, exact per-file/per-field manifest and original-plan hash are retained. It moved only the selected raw source payloads into external byte-identical backups and preserved all historical timing fields and unselected data. The five direct caches and two optional thumbnail fields were not edited. See `notes/part_c_source_cache_hygiene_audit.md` for precise roles and limitations; no theorem/source-gate movement follows from this maintenance.

The second normalization has its own immutable manifest/output and separate external raw-cache directory. It preserves pure bibliographic/holdings/identifier metadata and all unselected portions of mixed catalogue records. The50selected ranges are actual retrieved third-party prose, not our mathematical outputs. Its15files changed from249,011 to236,293bytes. No earlier manifest, checkpoint, source access status or mathematical statement was altered.

### One new Lieberman institutional route,19November2026,17:30UTC

`part_c_lieberman_cambridge_http.py` made one ordinary public homepage GET with redirects disabled and no retry; start17:28:03.593414UTC, elapsed11.718183012002555s, HTTP503. It obtained no page inventory or mathematical content. Two separately recorded web-tool calls made2search queries(1.031s) and1homepage open(0.553s,502). `part_c_lieberman_cambridge_finalize.py` made zero requests and hashed the two external raw web records in0.0005918419992667623s, start17:29:26.862674UTC. All compact outputs and exact code-mode call transcript are retained. This bounded Cambridge/DPMMS–Scholl route ended without an advertised original-copy link; no mathematical checks, theorem/source-status changes, access workaround or claimed progress.

### Direct Lieberman zbMATH record-link attempt,19November2026,17:49UTC

Three separately executed web-tool calls made2discovery queries(1.081s), opened the actual Numdamreference page(0.735s), and followed its actual LiebermanZbllink38(0.582s). The direct record returned403and was not retried. No local HTTPrequest, API/alias probe, original-content read or mathematical check followed. `part_c_lieberman_zbmath_finalize.py` hashed3external raw web records with zero requests in0.0007754739999654703s, start17:49:23.647036UTC. Exact queries, URLs, locators, timings and source-cache hashes are retained in compact metadata; no source/theorem status changed. Full scope: `notes/part_c_lieberman_zbmath_audit.md`.

### Lieberman GoogleBooks original-volume route,19November2026,18:11UTC

Three separately executed web-tool calls made2queries(0.893s), opened the actual AJM90(1968)GoogleBooksrecord(0.823s), and followed one actual advertised inside-book abelianlink(0.877s). The last reached Google/sorryand stopped. `part_c_lieberman_books_page.py` made one ordinary GET to inspect the volume's form, with redirects disabled; HTTP302,8.254976579999493s, start18:08:44.375856UTC, no HTML/form obtained. `part_c_lieberman_books_finalize.py` made zero requests and hashed3external raw records in0.0007848410023143515s, start18:10:50.650006UTC. Original volume metadata was read, but its bound extent and required pp366–374were unverified; no original theorem, mathematical check, workaround, retry or source-status change. Exact compact provenance and full limitations: `notes/part_c_lieberman_books_audit.md`.
