# SA13: reading and reproducing the dossier

Start with `SA13_dossier.md`, then use the stable IDs in the JSON and TSV
registers. `SA13_directions.md` is the task list for subsequent work.
`SA13_aliases.tsv` resolves IDs consolidated across review folders.

The four Pro packages contain exactly 379 indexed note entries. The Codex
supplements create additional objects and claims, without creating Pro
verdict rows. Locators use one-based global source-file line numbers, together
with cote and scan. No manuscript scans or second-pass corrections were
supplied; the readings table contains alarms, not emendations.

## Evidence structure

The `shards` directories preserve the full authored reviews, proof notes,
source-reading logs, searched-fate logs, bibliography access qualifications,
original records and computation outputs. The global tables apply only the
explicit semantic merge maps and recorded mathematical corrections.

An entry in `CHECK_EVENTS.tsv` states what was actually done. In particular,
source comparison and reference access are not independent proofs. A
bibliography `note={verified}` records an actual URL/DOI opening; its access
annotation defines the narrower scope of that opening. Unidentified sources
and unopened candidates are labelled rather than assigned invented editions.

## Rebuilding the global tables

The saved global tables can be read without any dependencies. For rebuilding,
choose a working directory and extract this ZIP into its `deliverable/`
subdirectory. Extract the two original attachments separately into
`sources/notes/` and `sources/texts/`, so that `NOTES_INDEX.tsv` and `TOPIC.md`
are at those directory roots. The original attachments are intentionally not
duplicated in this archive.

Run from that working directory:

```sh
python3 deliverable/code/inventory.py
python3 deliverable/code/assemble.py
python3 deliverable/code/validate_assembly.py
python3 deliverable/code/build_final_directions.py
python3 deliverable/code/finalize_dossier.py
python3 deliverable/code/validate_final.py
```

`inventory.py` regenerates `work/pages.json` and the note-entry packets from
the supplied texts. `assemble.py` consumes the completed authored review
records. It does not create a verdict by parsing keywords. Full local table
rebuilds have ordered finishing steps: see p3's README, p2's
`code/final_quality_patches.py`, and p4's `code/finalize_validate.py`. Running
an early authoring script alone may omit later explicit corrections, so the
saved final records are the authoritative starting point.

## Computations

The arithmetic and symbolic certificates use Python 3, with SymPy where
imported. Their complete saved outputs accompany the programs. The main
entry points are:

| Scope | Program | Saved output |
|---|---|---|
| Derived operations, traces and local algebra | `code/p1_compute.py` | `outputs/p1_computations.json`, `outputs/p1_compute.txt` |
| Depth, model groups, weights and GIT signs | `code/root_codex_compute.py` | `outputs/root_codex_computations.json` |
| Ext, monodromy and reused EVT/operator calculations | `shards/p2/code/check_computations.py` | `shards/p2/outputs/` computation records |
| Independent weight audit | `shards/p2/code/check_weights.py` | `shards/p2/outputs/weights_computations.json` |
| Biextensions, Lie/Čech and A36 arithmetic | `shards/p3/code/computations.py` | `shards/p3/outputs/computations.txt` |
| Arbitrary-point specialization counterexample | `shards/p3/code/specialization_counterexample.py` | `shards/p3/outputs/specialization_counterexample.txt` |
| Pairings, formal functions and preparation | `shards/p4/code/computations.py` | `shards/p4/outputs/computations.txt` |
| Nearby-cycle degrees, Kummer maps and depth | `shards/p4/code/codex_computations.py` | `shards/p4/outputs/codex_computations.txt` |

Proof notes explain which calculations constitute exact finite
counterexamples and which merely check signs or small cases of a separately
proved symbolic assertion. Download/OCR scripts document the primary-source
retrievals. External PDFs, raw OCR and raw web bodies are not redistributed;
retrieval manifests, exact locators, access audits and paraphrased conclusions
are retained. Repeating online retrievals depends on the sources still being
available.

## Integrity

`outputs/validation.json` and `outputs/final_validation.json` record the final
structural checks. `ARCHIVE_MANIFEST.json` records each included file's size
and SHA-256. These checks concern coverage and reproducibility, not a blanket
certification of mathematical truth. The source hash inventory permits
comparison with the original attachments. All research-status statements
are dated 19 November 2026.
