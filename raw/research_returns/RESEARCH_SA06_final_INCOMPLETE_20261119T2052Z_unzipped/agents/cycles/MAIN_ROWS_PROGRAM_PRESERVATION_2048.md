# Preservation of the administrative 41-row comparison programs

Saved 2026-11-19T20:48:00.396751+00:00. Administrative preservation only, under the parent's express authorization during source freeze. No new mathematical calculation or proof claim.

## Original executions

Both complete Python here-document bodies were preserved from the executed tool arguments: `code/compare_main_rows_review15_exact.py` and `code/write_main_rows_receipt_original.py`, relative to this owner directory. Their actual stdout was preserved from the tool results, not reconstructed by substituting later output. The receipt-writing program is archived and was not rerun; its originally saved receipt remains byte-identical at SHA af26651a861e6efe21415db9e95f790b942852458083c23837e738ed8543148e.

The original comparison tool reported exit 0 and wall time 0.282543695 seconds (chunk afa8f5). The original receipt-writer tool reported exit 0 and wall time 0.188568427 seconds (chunk 3b5e30); its in-program save timestamp was 2026-11-19T20:45:29.711778+00:00. Neither original run instrumented precise UTC start/end times or an internal performance-counter runtime. Those missing measurements have not been invented or backdated.

## One scoped instrumented rerun

Executed `python agents/cycles/code/run_main_rows_preservation.py` from the research root. It ran the exact preserved comparison body once with its unchanged in-memory interception of root write operations and normalization saves. The outer runner captured complete stdout/stderr, the full historical/current TASKS arrays, and SHA-256 hashes for all 597 research-tree files observed in actual open events. Input fingerprints were taken immediately after the run under the source freeze; they are not falsely labeled as pre-run historical snapshots.

Start: 2026-11-19T20:47:14.509565+00:00. End: 2026-11-19T20:47:14.722844+00:00. Internal elapsed runtime: 0.21326796000357717 seconds. Exit: 0. Stderr: empty.

The new stdout is byte-identical to the preserved original stdout (5,533 bytes; SHA fb392f7573548534d615f9d167c34e612550db832c99dd9cb2bccc7a8cd245b3). The result remains all 41 statuses unchanged, 40 entire rows identical, and C.3 auxiliary append only. This scoped rerun supplies administrative timing evidence and is not mathematical movement.

## Retained artifacts

| Path relative to research root | Bytes | SHA-256 |
|---|---:|---|
| `agents/cycles/code/compare_main_rows_review15_exact.py` | 2234 | `4c2dc917d72e0fef7ef94fdc21833653799772922adccbb24a875a3683f15758` |
| `agents/cycles/code/write_main_rows_receipt_original.py` | 8326 | `edc1851667c871ce4e37cb400732d0d30ee0c27230b35ce6580c3a90075c5b6d` |
| `agents/cycles/code/run_main_rows_preservation.py` | 3379 | `26a7f469b06884113b2e191cdc3247d3c6e6546262e28469ec3fe4c0df6f7f28` |
| `agents/cycles/output/review15_main_rows_original.stdout.txt` | 5533 | `fb392f7573548534d615f9d167c34e612550db832c99dd9cb2bccc7a8cd245b3` |
| `agents/cycles/output/review15_main_rows_receipt_original.stdout.json` | 464 | `5e33aff5a6289815ad84e57642dda5a16ff263a70ff16ddc5800a34bee630c67` |
| `agents/cycles/output/review15_main_rows_rerun.stdout.txt` | 5533 | `fb392f7573548534d615f9d167c34e612550db832c99dd9cb2bccc7a8cd245b3` |
| `agents/cycles/output/review15_main_rows_rerun.stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `agents/cycles/output/review15_main_rows_rerun.inputs.json` | 105619 | `e994bdaafd7a81ae5caaeaa2881651d2d44d1b2ff06a3a6cf04d5eb5d2411182` |
| `agents/cycles/output/review15_main_rows_rerun.tasks.json` | 53314 | `e9599d361a4e28884db60c3f7e4949e2755313faf94a8d0809dc89ac6ea0ba0a` |
| `agents/cycles/output/review15_main_rows_rerun.run.json` | 1682 | `e183e2f393ee418da39b9e2d99c8f226c1160008c53dd04bbecaae7b481d1efc` |
| `agents/cycles/MAIN_ROWS_REVIEW15_COMPARISON_2045.md` | 6713 | `af26651a861e6efe21415db9e95f790b942852458083c23837e738ed8543148e` |

The machine-readable manifest is `agents/cycles/output/review15_main_rows_preservation_manifest.json`. No failed execution occurred in these two original administrative programs or the single timed rerun. The preserved receipt-writing program would rewrite its owned dated receipt if manually rerun; archival preservation does not authorize that replay during the freeze.
