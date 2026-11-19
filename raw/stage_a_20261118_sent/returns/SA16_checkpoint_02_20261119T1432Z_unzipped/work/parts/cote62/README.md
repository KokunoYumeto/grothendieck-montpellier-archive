# Cote 62 component: reproducibility and scope

Run: **SA16-2026-11-19-cote62**. Model: **GPT-6 Astra Pro**. Reasoning effort: **inherited/unspecified**. Audit date: **2026-11-19**.

## Deliverable manifest

| File | Content |
|---|---|
| `items.json` | 97 consolidated items, covering every one of the 103 original Pro entries |
| `entries.tsv` | Exactly one verdict for each original entry: 90 kept, 7 corrected, 6 merged |
| `claims.json` | 79 manually assessed claim families, each with source locators, searched fate and reference keys |
| `problems.json` | 31 mathematical or editorial problems, distinguished by kind |
| `readings.tsv` | 83 proposed reading alarms; all remain undecided without manuscript images |
| `links.tsv` | 34 links checked at both available endpoints, plus 101 explicitly unverified external-context leads |
| `references.bib`, `reference_registry.json` | 50 records: 49 verified to the stated scope, 1 inaccessible archival lead |
| `search_log.tsv` | 36 search or retrieval batches, exact requests, evidence summaries and claim/problem coverage |
| `check_events.tsv` | 351 checks, distinguishing passage comparison, mathematical proof work, computation and refutation |
| `proof_checks.md` | Reconstructed proofs and counterexamples P1–P7; not diplomatic source text |
| `dossier_notes.md` | Substantive findings, source distinctions and limits |
| `directions.md` | Nine ranked next tasks; no new Stage 6 research project was developed |
| `code/`, `outputs/` | All local programs and their retained output, including exact symbolic and numerical checks |

The current structural validation reports no missing entry, broken item/claim/reference/search ID, duplicate ID or reading scan mismatch. This validation checks structure, not mathematical truth. All verdicts and search-fate summaries were authored after reading the passages; the builder scripts serialize those decisions.

## Reproduction

Run the programs from the workspace root containing `sources/` and `work/`. Python requires `sympy` and `mpmath` for `check_math.py`. The builders use the standard library. The source-reading program and numbered outputs preserve the supplied transcription context. Physical line locators are one-based in the exact named transcription file.

Rebuild in this order:

```text
code/build_items.py
code/build_claims.py
code/build_problems.py
code/build_readings.py
code/build_references.py
code/build_links.py
code/build_search_log.py
code/build_check_events.py
code/check_math.py
code/validate_registers.py
```

The saved mathematical run uses 60-digit numerical precision with explicit nonspecial inputs; exact algebraic rows are distinguished from numerical rows in both output formats. It does not execute any external Lean certificate. The relative normalizer proof uses fppf descent plus exact matrix identities, not a test of geometric points alone.

Searches cannot be faithfully reproduced from an offline package: the exact requests, opened URLs and retrieval dates are retained. Original third-party retrieval bodies and the full EGA PDF/text are outside this component in `external_cache/cote62/`. The full PDF hash and exact EGA locators are retained in `outputs/fetch_ega.json` and `outputs/ega_passage.txt`. `code/prepare_web_metadata.py` moves raw tool responses outside deliverables and retains request/source metadata; it does not alter mathematical assessments.

## Limits that must survive the global merge

No manuscript images were supplied. A false literal transcription is not thereby an established authorial error. The 30 `false as stated` families include defective subsidiary formulas, not 30 wholly false developments. Every refined statement is separately identified.

The normalizer over bases with 6 invertible is settled in P2; its bad-characteristic extension is only a proposed next task. The exceptional trisection fibres retain nilpotent structure and an arithmetic stabilizer twist. The exact archival identity of rédaction numbers 272 and 276 is unverified. The minimum-parameter and scratch-module questions lack sufficient quantifiers; no current open-problem claim follows from that limitation.

This component does not assert new cross-project conclusions from unavailable LM, Dérivateurs, S6 or WG records. Their note-side leads are retained separately. Cross-cote links are the root merger’s responsibility.

The subsequent Katz/Hodge review requested by the parent is complete in `supplement_katz/` and does not change this cote 62 coverage boundary. It contains an independent proof review, 15 exact search batches, 15 additional review/source events, seven scoped bibliographic records (including the three newly verified Bertrand1978, Waldschmidt2004 and Spence2018 references), and an exact symbolic check program with output. Its core finding is that the zero-locus and phase arguments pass; a general-matrix sign in the checking proof was repaired; no verified solution of the exact Katz algebraicity converse was located. Its counts are additional to the core manifest above.
