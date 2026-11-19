# Programs and outputs

`recompute.py` is the mathematical verification program. It uses Python and Sympy, writes `../outputs/computation_records.json`, and prints the exact calculations. The successful transcript is `../outputs/recompute.txt`. Run it from any working directory with output redirected to a new file if a fresh execution is wanted. It contains symbolic identities, a complete finite group, free-word reductions and explicitly bounded characteristic-p checks; the general proofs are in `../proof_notes.md`.

The `author_*.py` programs serialize manually authored decisions. They do not infer verdicts from headings, keywords, computations or retrieval output. Their output logs document the serialization. `polish_claims.py`, `finalize_metadata.py` and `review_c512.py` record explicit wording or scholarly revisions after the first serialization. The latter incorporates a team proof that was separately read and checked. They are an audit trail, not an automatic theorem classifier.

`author_support.py` uses exact search batches and raw provider output from the task’s external cache to preserve query and source metadata. Those external excerpts and whole third-party publications are intentionally not redistributed; the source URLs, locators, hashes, search requests and the reviewer’s own summaries are in the deliverable. This serialization program therefore needs that cache to be rerun. The mathematical verification program needs no such cache.

`read_sources.py` preserves line-numbered excerpts of the supplied source documents used in the review. Its source-reading outputs are included because those are user-provided materials. They are not substitutes for the actual reading recorded in the progress and check-event logs.

`validate.py` checks coverage, schemas, IDs, source-line bounds, reference mappings, refinement targets and output presence. It does not decide the truth of a claim. Its complete result is `../outputs/final_validation.txt`, with machine-readable counts in `../outputs/final_inventory.json`.
