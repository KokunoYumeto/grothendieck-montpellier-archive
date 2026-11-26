# SA27 — Delivery guide

This archive contains the completed six-stage dossier for part 3 of *Autour de Pursuing stacks*, checked as of 19 November 2026. Its scope is the 578 entries of the supplied index for cotes 108, 112–118. Other cotes in TOPIC are covered as orientation records only.

## Main files

| File | Purpose |
|---|---|
| `SA27_dossier.md` | English overview, substantive findings, scope, counts and limitations |
| `SA27_entries.tsv` | Exactly one read verdict per indexed source entry |
| `SA27_items.json` | Consolidated items, source membership, exact text checks and reconstructions |
| `SA27_claims.json` | Authorial assertions, constructions and questions, with page status, literature fate and search IDs |
| `SA27_problems.json` | His questions, conjectures and unfinished steps, with precise modern comparisons |
| `SA27_readings.tsv` | Undecided scan-reading queue; no ink decision was made |
| `SA27_links.tsv` | All link records, with their different evidential statuses |
| `SA27_directions.md` | Fifteen ranked tasks for later research runs |
| `SA27_references.bib` | Consolidated references, each marked verified or unverified |
| `CHECK_EVENTS.tsv` | What was read, used, proved, computed or refuted, and by whom |
| `progress.log` | UTC work milestones and completion record |

## Supporting evidence

`work/p108/`, `work/p116/` and `work/p118/` retain the package readers' original records. They contain page-read logs, proofs, exact theorem matches, search ledgers, context-comparison subrows, programs and outputs. Their local item IDs can differ from the master IDs after a merger; `work/item_aliases.json`, `work/problem_aliases.json` and `work/reference_aliases.json` give the translations. The original package records are preserved intentionally, not treated as competing final editions. The master files at the archive root are authoritative for consolidation and counts.

`research/root_mathematical_checks.md` contains the independent checks and counterexamples. `research/shared_verifications.md` records the later public manuscript comparisons. `research/search_index.json` preserves the actual ledger rows, while `research/claim_search_links.tsv` gives the claim-to-search map. Search records may cover a tightly related family of claims; each claim states the exact hypothesis match or the remaining identification limit.

Modern claim refinements are in `research/modern_refinements.json`. Historical/editorial questions introduced by earlier notes are in `research/context_questions.json`, and modern audit questions are in `research/modern_questions.json`. Their stable IDs remain usable, but they are excluded from the authorial claim or problem totals. The original parent claim remains in the main register when its proposed stronger reading is refuted.

The three link categories are also available separately as `research/folder_links.tsv`, `research/published_links.tsv` and `research/project_links.tsv`. Private research returns are attributed, unverified leads. The available note-side occurrence has been read; an unavailable private endpoint is not reported as opened or proved. Public manuscript and published-work endpoints have exact opened locators where a result is used.

Line numbers refer to the supplied combined TeX file, one based, unless explicitly qualified. `work/page_map.json` resolves cote/scan boundaries. Mathematical reconstructions never alter the source text. The absence of second-pass and Codex files is a property of this supplied corpus, not an unfinished processing step.

## Reproduce the checks

Keep this `SA27/` directory next to a `source/` directory containing the original attachment's already-expanded `SA27_notes/` and `SA27_texts/` folders. Do not unpack nested archives: there were none. The source inventory contains hashes of the original inputs. The source files themselves are deliberately absent from this deliverable, as requested.

The scripts use Python 3. The exact nerve-homology program additionally uses SymPy. The saved JSON output is available without installing it. Network access is required only to rerun primary-source retrieval helpers, not to inspect the dossier or rerun the saved finite computations and structural checks.

From the directory containing `SA27/` and `source/`:

```bash
python3 SA27/code/validate_dossier.py
python3 SA27/code/finite_categories.py
python3 SA27/code/groupoid_pi0.py
python3 SA27/code/reused_sheet_arithmetic.py
python3 SA27/work/p108/finite_checks.py
python3 SA27/work/p116/computations.py
python3 SA27/work/p118/code/check_examples.py
```

The package build scripts serialize their explicitly authored reading decisions; they do not infer verdicts by keywords. Before rebuilding the p118 package from its scripts, run `python3 SA27/code/prepare_source_navigation.py` to regenerate the source-navigation input from the original attachment. That extracted full-source copy is omitted from the ZIP. `code/consolidate.py` applies the documented editorial mergers and reconstructs the master tables from the authored records. It should be followed by structural validation, then `code/finalize_editorial.py` if the count tables need rebuilding. All source decisions remain subject to scholarly review; successful validation checks identity, coverage, references and source immutability rather than mathematical truth.

The archive manifest in `outputs/archive_manifest.json` gives file sizes and hashes. Full copyrighted external PDFs, full-text research caches and raw web retrieval dumps are omitted; their opened URLs, locators and concise findings remain in the authored ledgers. The checkpoint history is included, but earlier ZIP files are not nested in this archive.
