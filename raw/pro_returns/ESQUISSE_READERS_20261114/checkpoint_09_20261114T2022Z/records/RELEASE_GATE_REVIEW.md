# Independent review of the release gate

Reviewed by the translation/guide agent on 14 November 2026. The review read
`scripts/validate_release.py`, `scripts/release_bundle.py`, the generation and
PDF-audit functions they use, `scripts/write_readme.py`, and
`translated_pages/refresh_index.py`. It did not edit the root-owned validator or
packager and did not create scan or visual-review approvals. The findings below
were sent to the root agent and accepted for integration before release.

## Content and evidence checks

1. **Current prose review.** The earlier validator checked the presence of all
   58 English files and exact mathematics, while requiring only the existence of
   `records/INDEPENDENT_TEXT_REVIEW.tsv`. It did not require a recorded review of
   each current English or guide hash. A read-only, in-memory probe reduced
   English site003 to its scan/page/folio macros: its mathematics, scan marks and
   doubt counts still matched because the page contains no formulas or doubts.
   This demonstrated why those mechanical checks cannot certify the prose.
   Root accepted a current-hash review requirement for all 58 English pages and
   all 19 guide files, including the final collation preface. The few earlier
   review-hash gaps were identified explicitly for rereading.

2. **Variant class and location.** The earlier check compared the combined
   multiset of English `var` and `frapparatus` IDs with the French IDs. It did not
   verify the approved `english_variant_needed` class or the source-page key.
   In a read-only list probe, moving `V-FR-026-002` from the English wording
   class to the French-source class still passed that combined check, although
   the approved correction changes *hyperquadratic* to *hyperquadric*. Root
   accepted separate class checks and per-page ID alignment.

3. **Translation-index replay.** The earlier gate checked the paths' hashes but
   did not recompute the index's stored math, diagram, translator-note, variant
   and source-apparatus lists. It also used a set of keys without requiring
   exactly 58 unique rows or canonical per-key paths. Prose doubt counts were
   checked by the index writer but not replayed by the release validator;
   PDF-link validation compares each English PDF with its own source. Root
   accepted independent index-content and doubt-count replay, including the
   newly preserved dots.

4. **Guide structure and completion.** The earlier structural test accepted any
   18 files containing 18 subsection headings. Its negative-word test also
   accepted an empty existing collation-preface file; this was confirmed in
   memory without changing a file. Exact expected filenames, nonempty content
   and current review hashes provide the concrete structural and review checks.
   The actual commentary has 18 complete units; the collation preface remains
   explicitly provisional until all page pairs are checked.

5. **Cached PDF and probe evidence.** The earlier release validator trusted the
   visual-page lists in `FINAL_PDF_AUDIT.json` without binding that audit to its
   current `VISUAL_QA.tsv` and build-history inputs. The strict README already
   rereads the actual visual table, so the packaging path supplied that extra
   check. The reusable rendering-probe gate also accepted a passed result
   without comparing its source hash with the current template-generated
   probe. Root assigned dependency-freshness checks to the builder.

## Final index, README and reconciliation order

The existing sequence—first passing release gate, strict README generation,
reconciliation, and an identical second passing gate—avoids a timestamp cycle
because the gate report is deterministic and the README is written only once
between the two checks. Root accepted insertion of
`translated_pages/refresh_index.py` after the first passing gate and before the
strict README. This lets the index report completed final QA without making the
first gate depend on a status that itself requires a prior passing gate.

The translation index is outside the generator's `input_snapshot`, so this
status refresh does not change generated source or PDF hashes. Its final-status
branch now also requires the current generation-input snapshot to equal
`BUILD_INPUTS.json`; a previously passing gate for unchanged PDFs cannot label
newer, unregenerated inputs final. The second release check and reconciliation
must cover this final index. No README or index writes follow successful
packaging.

The inspected checkpoint manifests contain no `CHECKPOINT_RECONCILIATION` or
`FINAL_CONTENTS` output. Thus the existing checkpoint set has no recursive
live-hash requirement for those files. A checkpoint containing generated
reconciliation outputs needs an explicit archival destination for those older
outputs to avoid making a reconciliation hash itself.

## Owned correction and boundaries

The README snapshot reader tracked `retained_usages_fr.tex` instead of
`templates/retained_usages_fr.tex`. Its actual source reconstruction already
used the correct template through `make_document`, but the stability check
missed that template path. The snapshot path is now corrected.

Root separately added independent page-map URL/site-plus-one checks, exact
original-manifest coverage, and stronger checkpoint-member/hash accounting.
Those changes and the builder's dependency checks require final validation in
their implemented versions. This review record documents the inspected
predicates and accepted remedies; it does not itself certify the final release.
