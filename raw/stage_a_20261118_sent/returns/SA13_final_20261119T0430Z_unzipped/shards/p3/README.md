# P3 review shard

This shard completes the assigned review of `MPL_36_002-052` and both supplied A36 Codex folders. It also provides the requested root Lie/Tate audit and the p3↔p4 consolidation proposal. The parent assembler owns final cross-package aliases and persistence.

## Scope and saved counts

- 93 indexed Pro entries: 76 kept, 14 merged locally and 3 corrected. Every entry has exactly one verdict row.
- 110 items, including the genuinely additional A36 objects.
- 101 claims, each mapped to a search group and a precise mathematical check event.
- 56 problems and 90 mathematical reading alarms. No transcription is edited.
- 43 bibliography entries, with exact access and theorem-inspection limits.
- 27 search groups, 159 links, all 34 earlier register rows and all 92 entry context paragraphs preserved separately as project leads.
- 272 check events: 119 mathematical claim checks, 110 explicitly non-proof source/summary background events, and 43 reference-access/background events.
- 11 ranked follow-up directions, each with item/claim/problem provenance.

`review.md` gives the mathematical reasoning and source comparisons. `research_evidence.md` gives the actual opened source locations and access limits. `root_lie_audit.md` supplies the extra K34:183–199 audit without allocating competing IDs. `cross_package_audit.md` and `cross_package_merge_map.tsv` propose four object-level item aliases and one problem alias while retaining all distinct claims and source rows.

## Reproduction

Python3 and SymPy suffice for the computations. From the workspace root:

```sh
python deliverable/shards/p3/code/computations.py
python deliverable/shards/p3/code/specialization_counterexample.py
python deliverable/shards/p3/code/rebuild_records.py
```

The retained computation outputs are in `outputs/computations.txt` and `outputs/specialization_counterexample.txt`. The table builder serializes human-written records; it does not infer a mathematical verdict from keywords. The reproduction pipeline also restores the polished reviewer prose and the separate background/reference events. Do not run only the raw table builder and assume it includes those final formatting and event steps.

`outputs/validation.json` and `outputs/validation.txt` record clean checks of local entry coverage, stable IDs, references, source scan/line ranges, search mappings and event coverage. Those checks establish structural consistency, not mathematical truth. The proof audits and explicit counterexamples are separately documented in the review and check table.
