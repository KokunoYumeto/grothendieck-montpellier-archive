# Claim-status census methodology

**Scope and purpose.** This is a census normalization of386 current raw claim records from four package owners: P56(151), P67(80), P894(82), and the combined root P78 package(73). P78 includes its12 c7 records,58 original c8 records and3 present-run refinements, P78-C071–C073. C071 is also retained in a supplementary transport file; its two byte-equivalent record objects are counted once by their shared legacy ID, and non-identical copies would stop the audit. This is not a new mathematical verdict, a proof audit, or a semantic deduplication of different claims across packages. No owner register was modified. The preceding384-record census is retained in files with the `_384` suffix.

Every complete `status_on_pages` and `origin` field was read. Where a status combined assertions or was ambiguous, the full claim statement and owner’s fate were read to distinguish its components. The original status, original origin, presence/absence of the origin field, and any separate `counterexample_origin` are preserved in `status_index.tsv`. The input snapshot and SHA256 hashes make the census reproducible. The script uses manually selected claim IDs and individual reasons, not keyword rules; a later change to status or origin stops the script for a new reading.

## Normalization decisions

An explicit documentary status takes precedence over a modern judgment when the two can be separated. Thus P894-C006 remains **open on the pages**, with its modern refutation in a separate column. P894-C022 and C038 remain **corrected or withdrawn by himself**, while their confirmed falsity is recorded separately. P67-C046 remains **stated without proof**: the failed ordinary-cusp example is not the same as falsity of the general singular de Rham assertion.

Where the owner supplies only “false as stated” or a literal-formula failure, that permitted bucket is retained, but the documentary component explicitly says that historical proof/retraction status was not separately supplied. A contemporary counterexample is never evidence that Grothendieck withdrew the claim. Likewise, deleting a hypothesis or an initial arrow does not mean withdrawing the whole surviving assertion.

**Mixed or conditional page status** retains substantive mixtures: a proved/sketched subclaim alongside an open broader classification; conflicting cancellation witnesses; a running-text question alongside a report that an absent section proves it; or a programme conditional on admitted but unproved inputs. Standard named premises of an expressly completed deduction do not make every proof a “conditional programme.” For calculation claims explicitly described as computed on the pages, **proved there** means documentary completion of that calculation, not independent certification. Reused proof fragments remain **proof sketched** unless the owner expressly gives another level.

The fixed vocabulary has no “earlier-run-only record” bucket. Accordingly,9 P56 records explicitly described as not manuscript assertions are in **insufficient text** *for a historical page-status assignment*: C024, C045, C057, C062, C063, C080, C093, C095, C104. This does not mean an archival gap or doubt about those earlier ideas. The other3 records in that bucket—P78-C034, C052, C064—lack a sufficiently identified assertion or proof status. These two meanings are separated explicitly in the rows and count metadata.

## Refinement provenance

There are16 separate **present-run refinement** records:

- P56-C147–C151. C148, C149 and C151 refine diagnostics already present in the earlier run; their original provenance is retained, and no new-discovery claim is made.
- P67-C076–C080, whose origin fields expressly identify present-run refinements.
- P894-C077, C078 and C082, confirmed by their owner and now expressly labelled in the owner register. The motivating manuscript phrases remain in the original-status column; the raw-versus-finite inertia clarification, stronger trace-integrality statement and P1 boundary test are not attributed to Grothendieck.
- P78-C071, the separately supplied restricted filtration-length descent refinement, with its actual origin field and parent P78-C035 preserved by the owner file.
- P78-C072 and C073, respectively the K× eigenperiod ambiguity with a separate A-lattice requirement, and the corrected open-inertia quantifier. Both full objects were read after their addition. Their actual origin fields say present-run refinement, while `refinement_provenance` explicitly attributes the diagnostics to the earlier notes. Those fields and their parent IDs P78-C046/C047 are preserved separately; no new-discovery or additional-manuscript-assertion claim is made.

P894-C023 remains manuscript-origin: its question and ambiguous negative report are historical, while its independently constructed counterexample has a separate present-run origin. During this audit root added `origin=manuscript` to P78-C001–C070, first the58 original c8 records and then the12 c7 records. Both sets of additions were read in full and accepted without changing any bucket. Their reused-text qualifications remain in the original statuses. The final census therefore preserves the explicit owner origins for all P78 records; the earlier absence and accepted updates are documented in the saved input/review history.

## Census totals

| Census bucket | Raw records |
|---|---:|
| Proved there | 18 |
| Proof sketched | 105 |
| Stated without proof | 84 |
| Corrected or withdrawn by himself | 24 |
| False as stated | 21 |
| Open on the pages | 85 |
| Mixed or conditional page status | 21 |
| Insufficient text | 12 |
| Present-run refinement | 16 |
| **Total** | **386** |

The21 “false as stated” rows are the normalized records carrying that sole validity description. They are not a census of every false proposition mentioned anywhere in the dossier: modern refutations attached to historical open questions, retractions or examples are retained in their separate column.

Prepared19November2026 by GPT-6 Astra Pro; effort not exposed; SA15-20261119/global-status-audit. The mathematical judgments remain those of the owner registers.
