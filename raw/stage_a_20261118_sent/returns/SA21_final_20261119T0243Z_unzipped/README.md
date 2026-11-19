# SA21: reading and reproducing the dossier

Start with **SA21_dossier.md**. The principal JSON/TSV tables are the final
consolidation. `parts/` contains the contributing readers' full records and
proof appendices; these preserve their local problem IDs. Use
`audit/problem_aliases.tsv` to translate those IDs to the master problem index.
Do not substitute an earlier per-cote serialization for a final `claims.json`.

## Evidence conventions

* `SA21-<n>` identifies a consolidated indexed Pro-note item.
* `C-SA21-<cote suffix>-<number>` identifies a claim record. Some suffixed `R`
  records are explicitly current-run refinements. Gaps in the IX number ranges
  were reserved between readers; they are not missing source pages or records.
* `MP-SA21-<three digits>` is the master problem ID. A problem may have been
  answered later on the pages, disproved, or left open. Its presence in this
  index does not assert present mathematical openness.
* `R-SA21-*` identifies a named independent proof/countermodel in an appendix,
  not an extra assertion attributed to Grothendieck.
* A BibTeX key identifies a checked bibliographic work. `note={verified}` means
  that its link or DOI was opened. The annotation and source-check ledger say
  whether a theorem, only metadata, or a limited excerpt was actually read.
  `unverified` references retain their access limitation.

The class-D literature label means that an exact publication was not located
within the logged search. It is independent of the claim's mathematical status.
Every claim's search assignment is in `SA21_search_map.tsv`. Search families
may be shared by related claims, but exact hypothesis comparisons and fates
remain individual. Some older IX batches retain a query-family description
rather than an exact transport string; this limitation is stated in their log.

All supplied text was read. VII scans2–9 and IX129 are absent from the attached
transcriptions. No ink was available, so mathematical reading alarms remain
undecided. Unresolved targets are kept in `SA21_unresolved_links.tsv` and the
separate other-project table, not counted as verified two-ended links.

## Inputs and layout

The original input archives and downloaded full publications are deliberately
not redistributed. Restore the supplied `SA21_notes.zip` and `SA21_texts.zip`
as sibling directories `sources/notes/` and `sources/texts/` beside the work
directory. The archive contents correspond to the original `SA21_work/`
directory; they may be extracted under that name for reproduction.

Source paths in the original reading programs preserve the session workspace
`/workspace/scratch/4017236f14bf`. When reproducing elsewhere, adjust that
input root explicitly. Do not alter the archived source hashes or claim
locators. Most root assembly programs derive their output root from `__file__`.

Two additional context archives were inspected for Stage5. Their exact names,
identities and hashes are in `audit/prior_context_manifest.json` and
`audit/prior_context_138_manifest.json`; `parts/project_links/source_manifest.json`
and `search_manifest.json` delimit the textual target search. Those recovered
inputs were neighboring context selections, not the original SA21 context.
The curated records suffice to understand the result without possessing them.

## Mathematical checks

The principal independent arguments are:

| Scope | Proofs | Executed finite/symbolic checks |
|---|---|---|
| I–II | `audit/root_proofs.md` | `code/root_checks.py`; `outputs/root_checks.json` |
| III–V | `parts/cotes_3_5/proof_checks.md` | Programs and outputs under that part's `code/` and `outputs/` |
| VI–VII | `parts/cotes_6_7/formalism_and_checks.md` | `check_finite_examples.py`; `finite_checks_output.json` |
| VIII–IX65 | `parts/cotes_8_9/proof_audits.md` | Programs and outputs in that part; see its execution log |
| IX66–104 | `parts/cotes_9_09_13/proof_checks.md` | `code/finite_checks.py`; `outputs/finite_checks.json` |
| IX105–140 | `parts/cotes_9_14_18/formalism_and_checks.md` | `check_ix_examples.py`; `finite_checks_output.json` |

These use Python and standard-library finite combinatorics unless a local
script explicitly states another dependency. The saved output is the output
of an actual execution, not illustrative expected output. Finite enumeration
is not used to establish infinite cases without an accompanying argument.
No Lean compiler verification is claimed.

## Assembly

The authoring programs serialize manually made decisions. They do not derive
source verdicts by keyword or heading matching. From a restored work folder,
the final root assembly order is:

```bash
python code/assemble.py
python code/build_search_map.py
python code/author_directions.py
python code/author_dossier.py
python code/validate_final.py
```

Run a mathematical check program only when its proof or input certificate
needs verification. The saved command logs give the original calls. Fetching
external primary sources depends on network availability; access failures
are preserved in the retrieval metadata. `PACKAGE_MANIFEST.json` records
hashes of the actual archived bytes and lists excluded research inputs.
Raw third-party search/page text is replaced in the ZIP by the executed
request or retained query description, URLs, tool identifiers, payload hash
and access-error metadata; the curated result assessments remain intact.
Outputs that merely echo the original attached transcriptions are likewise
represented by their execution-output hashes, byte/line counts and reproduction
instructions. This keeps the original inputs out of the ZIP while preserving
the full-reading audit. All mathematical computation outputs are retained in full.

`progress.log` records the root stages and final completion in UTC. Reader
progress logs record their own work. The earlier checkpoint ZIP is not nested
in this final ZIP. The final validation confirms coverage and consistency;
it is not presented as a machine verification of every mathematical proof.
