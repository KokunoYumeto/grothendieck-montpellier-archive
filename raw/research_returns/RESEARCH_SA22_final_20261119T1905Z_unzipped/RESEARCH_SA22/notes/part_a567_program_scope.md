# Program scope and runtime audit — A.5–A.7 and targeted supplements

Researcher: GPT-6 Astra (OpenAI), `part_a567`, this run, 19 November 2026. This ledger distinguishes actual executed assertions from descriptive values printed by a script. A program supplements the complete proofs in the TeX; a finite sample is never the proof for all characteristics or for a continuous analytic family.

## Main exact-check program: three preserved versions

### Initial version: `code/part_a567_checks_initial.py` and `.out`

The executed finite octahedron phase covers the 24 odd primes from 3 through 97: 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97. For primes congruent to 1 modulo 4 it works over F_p with a chosen square root of -1; otherwise it works over F_(p^2)=F_p[i]. For each prime it enumerates all 6*5*4=120 ordered images of a projective triple, hence 2,880 candidate projective transformations in total. It retains exactly those preserving the six-set, examines all pairs of its nonidentity involutions for Klein subgroups with that fixed-point union, computes the normalizer of the standard Klein subgroup, and examines all 15 complementary-pair harmonic tests per prime (360 such tests overall). All these assertions passed. It also evaluates the three exact exceptional-characteristic expressions 2, 5, and 5/4.

The next matrix phase failed: its initial choice r2=diag(1,-1) did not invert rho=ST, so r3=r2*rho was not an involution. This was a wrong selection of generators, not evidence for a false presentation. The failure is preserved. The characteristic-2 size in this version is a descriptive printed value, not an independently executed enumeration; the later dedicated characteristic-2 script supplies that certificate.

**Runtime:** no end-to-end runtime was retained for this failed version: the timer print was after the failed assertion. We do not invent a time or rerun this already completed exhaustive phase merely to obtain one.

### Second version: `code/part_a567_checks_second.py` and `.out`

The same 2,880 projective-triple candidates and 360 harmonic complementary-pair tests passed again. The reflection choice was corrected to r2=((0,1),(1,0)); all three involution square relations and the displayed SL2/GL2 product relations passed.

This version then failed on a structural SymPy equality between two mathematically identical polynomial matrices: `(A-I)*(A+I)==f*I` had not been simplified. The preserved failure was resolved by simplifying the difference to zero. No proposition used the failed unsimplified expression as a proof.

**Runtime:** likewise not retained because execution stopped before the final timer print. No retrospective runtime is claimed.

### Final version: `code/part_a567_checks.py` and `.out`

All assertions passed. The final program covers:

* The same 24 primes, 2,880 projective-triple candidates, all involution-pair candidates in each resulting stabilizer, and 360 complementary-pair harmonic tests. Stabilizer orders are 24 except for 120 at p=5; the numbers of Klein subgroups with that fixed-point union are 1 except for 5 at p=5; each normalizer has order24. Harmonic complementary pairs number3 except for15 at p=5.
* The three exact harmonic exceptional-characteristic expressions and all displayed integral reflection/product relations. Completeness of the abstract presentations is proved in the manuscript, not inferred from matrix multiplication.
* All 4^4=256 matrices modulo4, retaining the48 of determinant1. The explicitly listed four-element W is checked for closure (16 products), squares, and normality (48*4=192 conjugations). The eight-element mod2 kernel, the12 quotient cosets, the binary-dihedral relations, and all12 normal forms are checked.
* The universal-domain involution matrix and its matrix factorization by f=x^2+yz-1; every entry of its relation matrix vanishes at the specified residue point. Domain, exactness of the matrix factorization, generic rank and failure of invertibility are proved in the manuscript; their printed descriptions are not substitutes for those proofs.
* The25 candidate pairs (m,n) in [-2,2]^2 for norm m^2+mn+3n^2=1, yielding exactly (+-1,0). The manuscript's inequality restricts all units to this bounded set and proves the norm-Euclidean bound15/16, the F4 residue field and the three gluing classes. The field name, gluing count and Euclidean bound printed by the script are descriptions of that proof, not additional independent finite-field computations.
* The exact hexagonal Gram-matrix ratio3. The two H1 orders printed at the end are reported values from the separate cohomological proof, not computed cohomology by the script.

**Recorded runtime:** 0.236781 seconds, from the script's `time.monotonic()` timer started after imports. This is internal computation time, not process wall time including Python and SymPy startup. This already timed exhaustive program was not rerun for the present reporting audit.

## New finite characteristic-3 certificate

`code/part_a567_char3_inertia.py`, `.out`, and `_timed.out` enumerate all3^4=81 matrices over F3. The48 invertible matrices yield24 projective matrices and24 distinct permutations of all four points of P1(F3). It then explicitly evaluates all six anharmonic transforms at lambda=2=-1 and verifies that every value is2. This certifies the merged exceptional inertia S4 of order24; it does not replace the fixed-point-equation proof of the generic inertia statement.

The original output had no runtime. A single timing-only rerun at the parent's request passed with byte-for-byte identical output: **0.074782 seconds process wall time**, including interpreter startup. Original output preserved.

## New excluded-characteristic-2 certificate

`code/part_a567_char2_edge.py`, `.out`, and `_timed.out` implement F4=F2[a]/(a^2+a+1) exactly. All16 products of its four translations are checked. Each of its three nonidentity translations is checked to square to the identity and to fix exactly infinity among all five P1(F4) points. All four possible i are tested for i^2=1, with unique solution i=1. The standard displayed four maps are checked to have only two distinct values, and the six-set to have three points. The proof that no additional geometric fixed point appears after algebraic closure is the equation z+a=z forcing a=0.

The first output had no explicit timer. One timing-only rerun preserved it and reproduced it exactly: **0.049693 seconds process wall time**. This small new edge certificate is separate from the already timed odd-prime enumeration.

## Explicit collar certificate

`code/part_a567_collar_explicit.py`, `.out`, and `_timed.out` check the fixed example n=10000, epsilon=10^-14, with conformal collar cutoff heights1/100 and1/50. This is symbolic and rational arithmetic, not a sampled PDE solution. The exact scopes are:

* the separated-mode differential equation and its value/normal derivative at0;
* the quintic cutoff's two endpoint values and four vanishing endpoint derivatives, its factored first and second derivatives, and the exact extrema bounds obtained from the two critical points of the second derivative;
* two algebraic forms of the exact graph-curvature expression from the displayed connection;
* the rational collar-embedding estimates, cutoff derivative bounds, L(H)<=-1700, residual coefficient40600102300<2^100, and the supersolution sign;
* every fixed-parameter derivative/normal/curvature error inequality used in the text, especially 10*epsilon*n^3+epsilon^2*n^4=1/10+10^-12<1;
* the exact strict upper bound u<=-9991/2000000000000000 at the specified boundary point.

The continuous maximum-principle comparison, the collar theorem, and the area argument for positivity somewhere else are proved or precisely sourced in the manuscript; this script does not numerically approximate them.

The original output lacked an explicit timer. One timing-only rerun passed and exactly reproduced it: **2.734516 seconds process wall time**, including SymPy startup. Both outputs are kept. Parent and C researcher independently checked the full continuous proof; those are proof reviews, not additional numerical experiments.

## Independent exact plumbing review

`code/part_a567_plumbing_review.py`, `.out`, and `_timed.out` use only exact `Fraction` arithmetic for the parent's fixed numerical witness: R=3/2, A=420/569, B=3/4, c=289/4, t=9/11. Independent quotient-rule evaluation gives first derivative numerator0, second derivative271040/371353867, and cross-ratio323680/323761. These are exact evaluations at one completely specified parameter, not a parameter search. The global coordinate injectivity, retained images, and annulus overlap are proved separately in the review notes; the prose descriptions printed by the script report those arguments and do not themselves execute a topological check.

One timing-only rerun exactly reproduced the original output: **0.066977 seconds process wall time**. The parent's independent original witness program is outside this ledger; this row records only the child's independent arithmetic review.

## Timing record and nonmathematical scripts

The machine-readable timing record is `code/part_a567_timing_audit.json`. Every timing-only rerun returned exit code0 and `matches_original:true`; the original outputs were not overwritten. The only programs rerun in this timing audit were the four small scripts listed above, the fourth being the newly added characteristic-2 edge check. No exhaustive main version was rerun.

`part_a567_fetch_sources.py`, `part_a567_retrieval_metadata.py`, `part_a567_legacy_ids.py`, and `part_a567_audit_update.py` perform retrieval or ledger maintenance. They are not mathematical experiments, and their HTTP or file-writing times must not be interpreted as proof-verification runtimes. The original failed retrievals and both failed mathematical prototypes remain documented rather than silently discarded.


### Public-book source reading, 2026-11-19

`code/part_a567_read_public_birman.py` rendered and OCR-read14 original pages148--161, in36.648908seconds; `code/part_a567_read_public_birman.out` records the run. This is document-access processing, not a mathematical test or numerical verification. Book text and selected scan images remain outside the distributable project. Alling--Greenleaf's embedded OCR was extracted directly with djvutxt and original pages61,62,64,65,66 were visually checked; no mathematical program was run or rerun for that source comparison.

## Fujiwara source access and adversarial analytic audit,14:25--14:50UTC

`code/part_a567_fujiwara_ihes.py` made exactly two ordinary public metadata/catalogue GET requests, for Fujiwara and tubular in the IHES preprint collection. It requested no source content file. Total wall time 10.025774082998396 seconds; individual times 10.024460840999382, 9.99511767900185 seconds. Both returnedHTTP200; actual displayed results were two unrelated Lafforgue records and zero records respectively. Complete request/result text is preserved in `code/part_a567_fujiwara_ihes_output.json`. This is document discovery, not a mathematical test.

The direct official24-page Fujiwara1998 PDF download and the small author-prefix CDX query are recorded in `code/part_a567_fujiwara_new_access_1430.json`, including individual runtimes14.851806573999056 and16.17183668800135seconds. Local text extraction of those24pages and rendering printed177--178 used PyMuPDF; an ad-hoc command did not separately retain a runtime. These operations did not check a mathematical statement by computation. The exact1995 article remains unopened.

The subsequent independent A1/A2 range audit read the current proof files and Mondello source and re-derived the interface, convexity, face-recession, finite-boundary and equivariance arguments analytically. No mathematical program, numerical experiment or exhaustive enumeration was run. Full reasoning is `notes/part_a567_adversarial_range_audit.md`; it is an audit/expository refinement of existing results, not a new result or evidence of movement.


### Advertised Fujiwara preview requests, 15:01–15:07UTC

These are source-access operations, not finite mathematical tests. `code/part_a567_fujiwara_preview.py` made one ordinary archived First-page request (HTTP404;10.359228540000913s), preserving its output JSON. Two short inline Python procedures made one exact-URL CDX metadata request (HTTP200, empty array;8.641206100997806s) and one live advertised-preview request (HTTP200,1,159-byte challenge HTML;7.235201277999295s). Their exact requests, scope, outcomes and individual runtimes are saved as `code/part_a567_fujiwara_preview_cdx_output.json` and `code/part_a567_fujiwara_live_preview_output.json`. No challenge was bypassed; no original mathematics was read, no mathematical certificate was rerun, and no source status changed. The two web-tool opening failures and bounded search-only queries have no separately measured program runtime and are documented in the source note.


### Tokyo predecessor / CiNii direct catalogue operations,15:09–15:13UTC

Three short inline Python source-access procedures read the actual series relationship-map frame (8.377396447998763s), its actual list frame (7.3720071030038525s), and the original series page's search form (7.2460062760001165s). Exact URLs, links, scope and results are in `code/part_a567_utms_relation_frame_output.json`, `_relation_list_output.json`, and `_catalogue_form_output.json`. A fourth inline procedure batched2 independent searches using those observed forms: title+author returned0records in6.1083472879981855s; contents returned1record in6.211069315999339s, independently identified as Cox1974. Whole batch6.212781499998528s; metadata `code/part_a567_cinii_preprint_search_output.json`. These are catalogue reads, not mathematical programs or tests; no paper source gate or theorem status changed. The1998 hypothesis audit was a visual and deductive review, with no numerical computation.


### Gabber public reference metadata,15:14–15:17UTC

One inline Python procedure batched2 independent metadata-only requests: the full public Crossref record for10.1007/BF02773001 (4,190bytes,5.569238841002516s) and the publisher's actually advertised referenceRIS export (1,265bytes,8.392031429997587s). Whole batch8.394255646999227s. Exact request/provenance/status/hash records and raw responses are saved in `code/part_a567_gabber_reference_metadata_output.json`, `part_a567_gabber_crossref_references.json`, and `part_a567_gabber_publisher_ris_references.ris`. Scope: check all8references, specificallyBF02773001_CR4/ref4, for a Fujiwara preprint identifier. Both identify only title+preprint+1992. This was not an article-text download or a mathematical computation; no mathematical certificate was rerun.

The follow-up ordinary request to the actual GoogleScholar reference link returnedHTTP429 in13.089055586999166s; no results were read and no retry occurred. Metadata: `code/part_a567_gabber_fujiwara_scholar_output.json`. This is source-access timing only.


### Targeted1992 repository/catalogue metadata,15:20–15:25UTC

`code/part_a567_fujiwara1992_catalogues.py` ran2 independent public metadata queries: OpenAIRE title/author without DOI/year/OA restriction (HTTP200,26 total,25 records on page1,23.383468202002405s) and OpenAlex terms with explicit1990-1994 window (HTTP429,6.320761210001365s; no retry/results). Initial batch23.385180502002186s. An inline pagination request read the one remaining OpenAIRE record (HTTP200,17.033863463999296s). All26 records were inspected and a compact ledger saved; exactly one is the1995 Duke record, no separate1992 original. A subsequent ordinary WorldCat query from an observed public URL pattern returnedHTTP403 in5.801788866003335s; no retry/results. Exact URLs, output hashes and raw metadata are in the corresponding `code/part_a567_fujiwara1992_*` records. Search-tool batches have their exact queries/results register and two full raw result files, with no separately measured program runtime claimed. All operations were source metadata searches or inspection, not mathematical tests.


### Bounded Pfluger offprint route,15:28–15:37UTC

`code/part_a567_pfluger_kuehnau_retrieval.py` made one ordinary GET of the observed public GDZ PDF and rendered its first/final mathematical pages. HTTP200,906314bytes,12PDFpages; total retrieval/render runtime9.517221836002136seconds, exact metadata in `_output.json`. The original is by **Alfred Huber and Reiner Kühnau**,1994, not Pfluger–Kühnau and not the1960 target. Both selected pages were visually read. The five preserved query/result files in `notes/part_a567_pfluger_offprint_audit.md` contain10actual search queries; no independently measured search-tool runtime is claimed. No mathematical test or certificate was run; no denied endpoint was retried, and the Pfluger1960 source gate is unchanged.


### Historical-runtime existing-log audit,2026-11-19

Inspected existing outputs only for fetch_sources, retrieval_metadata, legacy_ids, audit_update, ocr_sources, and both failed main-check versions. Only the OCR block has a retained duration:41.446637seconds, code/part_a567_ocr_sources.out:3, excluding interpreter startup. The other six historical durations are genuinely unrecorded. Exact file sizes, log locators, measurement boundaries and preserved fetch-status text are in `notes/part_a567_historical_runtime_audit.md` and `checks/part_a567_historical_runtime_audit.csv`. No audited script was rerun and no duration was inferred. This is reporting maintenance, not mathematical progress.


### Single delayed Fatcat metadata batch,15:38UTC

`code/part_a567_fatcat_delayed_check.py` issued exactly2ordinary public DOI metadata requests: one delayed Fujiwara availability check of the previously503 URL, and the first recorded Lieberman lookup. BothHTTP503,91-byte upstream timeout bodies; no release/file records, no content requests, no retries. Individual durations11.899788230002741and11.898996335003176seconds; parallel batch11.901000856996689seconds. Exact UTCstarts/URLs/status/bodyhashes are in `code/part_a567_fatcat_delayed_check_output.json`. The route stopped. This is metadata/service reporting, not a mathematical test or new source reading.


### Global A1 definition-risk audit and unequal-toric repair,2026-11-19

No mathematical program was run. The proof identified the distinction between normalized toric angles and equal paired lengths, constructed an exact radius(1,1)/(2,1/2) cut-object counterexample, and derived the full imbalance-fiber theorem analytically. Root and PartB independently reviewed it. `code/part_a567_a1_scope_scan_read.py` only rendered four already downloaded manuscript pages79-82; its recorded wall duration is0.7716450989973964seconds. All four images were visually read. Exact source lines, proof scope and corrected all-seams converse: `notes/part_a567_a1_global_domain_audit.md`. No finite certificate was rerun.


### Raw-toric isotopy descent refutation,2026-11-19

No new mathematical program or finite test was run. The normalized cap third jet and four-point plumbing cubic coefficient were derived analytically by Laurent matching and independently re-derived by PartB; root checked the full proof. The counterexample's radius choice is exact, and its phase is exp(i/N), where N is the least positive integer for which the specified analytic crossratio difference is nonzero. Existence follows from the identity theorem and an explicit nonzero cubic coefficient. N was **not numerically evaluated**, and the construction is not a claimed finite certificate. Exact proof: `sections/part_a567_toric_descent.tex`; convention/source-line audit: `notes/part_a567_a1_convention_completeness.md`.


### IAS public-search form access, 2026-11-19
One ordinary public request to the observed https://albert.ias.edu/search link; HTTP403 after6.7515461790026166seconds, start2026-11-19T16:33:18.232690Z. Output code/part_a567_fujiwara_ias_search_metadata.json. No results or source file read; stopped without retry. Other contemporaneous web-tool queries/catalogue readings have saved query/result JSON and UTC bounds, but no separate HTTP runtime; no duration is inferred. No mathematical program was run.


### Intrinsic tame category: source-page utility only

No mathematical program or finite certificate was run. The proof is a formal Galois-category/valuative argument, independently checked by PartC. `code/part_a567_intrinsic_hoshi_source_read.py` made one ordinary official RIMS1558 PDF request (HTTP200,413694bytes,67pages), then rendered exactly three PDF pages,56/61/65. Retrieval 9.100027041997237s; total retrieval/render 9.333157077999203s. Exact start, URL, hash and image paths are in its `_output.json`. All three images were actually visually read. This scope clarification is not counted as progress movement or an existing gate closure.


### Bounded Lieberman public paper-collection audit,16:48–16:51UTC

No standalone retrieval script or mathematical program was run. Eight saved web-orchestration records cover5 search queries in2 batches,2 direct opens,4 actual advertised-link clicks and5 text finds. Their exact JavaScript-measured block durations are0.533,0.664,1.116,0.754,1.973,1.030,1.209and1.282seconds; these are not individual HTTP timings and some include a trailing clock read. No whole-audit duration is inferred. Full scope, actual URLs, source refs, query strings and output-file mapping are in notes/part_a567_lieberman_public_collections_audit.md. The advertised15147-line bibliography catalogue has no author/title-fragment match; no original article was requested or read. Named-original gate unchanged; no mathematics or finite checks rerun.


### Lieberman web-record normalization only,16:55UTC

code/part_a567_normalize_lieberman_web_records.py performed no network operations or mathematical checks. It read8 existing web records, preserved their exact115180bytes in /workspace/scratch/9c53b536a97f/source_reading/recorded_web_search/, verified hashes, and replaced deliverable records with27850bytes of execution/source metadata. Full path/hash/byte/source-count manifest: code/part_a567_lieberman_web_normalization_manifest.json. Original search/click/open/find times and outcomes are unchanged. The first parser attempt stopped before all writes on a multiline result heading; exact failed script/output retained as *_failed01.py/json,0.03589149400067981s. The corrected single successful utility execution took0.07138120599847753s. These subprocess timings include interpreter startup and all utility operations and manifest writes; they exclude the wrapper's final output-record serialization. No source or mathematical gate changed.


### One bounded INSA repository route for Pfluger,17:27–17:30UTC

No mathematical program or finite check ran. part_a567_pfluger_insa_public_page.py made one ordinary GET to the actually discovered repository homepage and parsed advertised forms/links in10.025533731000905s. part_a567_pfluger_insa_search.py made two independent ordinary GETs through that observed form for Pfluger and Verheftung; bothHTTP200 with0results, individual10.761131628998555and11.53256192200206s, parallel batch11.534293568001885s. No retry or item file request. Two web calls covered one discovery query and two opens, measured0.972and0.753s. The metadata-only utility part_a567_pfluger_insa_web_metadata.py summarized already cached outputs in0.00476940099906642s, excluding final output serialization, with zero network operations. Full source bodies remain outside the project; compact metadata, exact hashes/paths, bounded scope and source refs are in code and notes/part_a567_pfluger_insa_audit.md. Named-original and mathematical statuses unchanged; no progress movement.


### Sole failed IA OCR item: local disposition only,17:37UTC

part_a567_pfluger_failed_ocr_assessment.py read only the selected failed item's compact fields from the existing inventory, preserving its provenance hash and row locators. It made zero network requests and ran0.011198207997949794s, excluding final output serialization. The explicit catalogue title identifies volumeVI no3 June1914, so no new GET or retry-log investigation was warranted for the1960 volume24 target. Prior failed-request duration12.101609681001719s remains a historical measurement, not a new request. Initial inline triage has no separately measured Python duration. Full frontmatter was not printed/copied; no mathematical check, source closure or progress movement.


### Bounded Pfluger article-registry route,17:47–17:50UTC

Six web queries in3batches and3opens in2batches were executed, with actual tool-call intervals0.317,1.098,1.117,0.803and0.617s. No ordinary HTTP retrieval script or original-content file request ran. Official zbMATH403 and EuDML timeout were not retried. The exact indexed Zbl identifier remains a bibliographic lead, not an opened registry record or original theorem. Full bodies are outside the project; compact commands/refs/URLs/outcomes/timings/hashes are in code/part_a567_pfluger_article_registry_*_metadata.json. The metadata-only utility part_a567_pfluger_article_registry_metadata.py ran0.004282533998775762s with zero network calls, excluding final output serialization. No mathematics, finite certificate, TeX, aggregate or source status changed.


### Bounded TIFR metadata/interface route,18:14–18:16UTC

One3-query web batch and one open of the actual official SIRC page took0.992and0.824s respectively. No ordinaryHTTP request, form submission, original-content retrieval or mathematical computation occurred. The batch exposed no target-original record; no TIFR holdings absence is inferred. Full source bodies remain outside the deliverable. The local metadata-only utility part_a567_pfluger_tifr_metadata.py took0.0016092070000013337s for cached reads/parsing/compact writes, excluding final output serialization; matching output preserves raw/compact SHA256s, bytes and paths. Complete bounded scope: notes/part_a567_pfluger_tifr_audit.md. Source status unchanged; not progress movement.


### Final three-target Zenodo/Figshare batch,18:21–18:23UTC

One system1 call executed exactly3targeted title/DOI queries with explicit Zenodo/Figshare restrictions; elapsed0.860s. HAL was omitted because all3targets already have recorded negative title/DOI searches. The batch returned an explicit empty-search response and was followed by zero opens, ordinaryHTTP calls or content requests. Three source-event rows refer to this same single batch, not3batches. Full raw output is outside the project. The local utility part_a567_openrepo_batch_metadata.py performed cached read/hash/metadata assembly only in0.00010812099935719743s, excluding final serialization; no network or mathematics. Exact commands, hashes, timings and bounded outcome are in code/part_a567_remaining_originals_openrepo_batch_metadata.json and notes/part_a567_remaining_originals_openrepo_audit.md. All3original gates unchanged; not progress movement.
