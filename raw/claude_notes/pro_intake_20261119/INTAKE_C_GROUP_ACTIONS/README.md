# INTAKE_C_GROUP_ACTIONS: the Pro intake prompt for three Longue Marche runs (757 register rows)

Built 19 Nov 2026 by Claude Opus 5.5 at effort max (an agent of the main session), for GPT-6 Astra (ChatGPT Pro mode). Builder scripts: `pro_intake_20261119/_work/` (`select_20261119.py`, `build_20261119.py`, `write_prompts_20261119.py`, this README's `write_readmes_20261119.py`).

**To send:** drag in `PROMPT.md` and the four zips, with no text, in a new chat in Pro mode. Lint: `push_rule_pro_prompts.py --lint` passes. Privacy scan (e-mail addresses, keys and tokens, the user's names and account name) over every text member of every zip and over PROMPT.md: no hits.

## Files

| File | Bytes | Members | SHA-256 |
|---|---:|---:|---|
| `INTAKE_C_1_returns.zip` | 3,187,582 | 258 | `8f5dda1dd01d314a2802ed29e099a78f59c6a7a7a1cd7adcc446ab694f5d0474` |
| `INTAKE_C_2_evidence_code.zip` | 13,302 | 7 | `5e25900e554e6a17827d132f94b04d70a0e1427bff0965535ecd4b2cfa2d9181` |
| `INTAKE_C_3_earlier_intakes.zip` | 619,882 | 30 | `00a0cc9f3866f884f9e029dd9405342774b6165563e89805e3534b3d7f669215` |
| `INTAKE_C_4_prompts_as_sent.zip` | 54,611 | 5 | `9bc5fa134636af579346619022923a54543015943579fe92212c0683e12c06c0` |
| `PROMPT.md` | 17,823 |  | `573fda6e20782f195f3f5a705aa619449f4b8c742eb70ad012882549fcc7538f` |

## Rows per run

| Run | Return | Rows | Return files attached (MB) | Evidence files (MB) |
|---|---|---:|---:|---:|
| LM1_GROUP_SCHEMES_rerun_20261112 | return | 84 | 32 (0.6) | 1 (0.0) |
| LM4_FINITE_GROUP_ACTIONS | return | 272 | 6 (4.5) | 5 (0.0) |
| LM4_SUCCESSOR | cp40 | 401 | 219 (4.3) | 0 (0.0) |
| **all** | | **757** | | |

## Estimated length of the run

About 13 to 21 hours: 757 rows at 40 to 70 rows an hour, plus about two hours for the sections across the runs and the gap work. The rate is set from S6_09_PAPERS (GPT-6 Astra, ChatGPT Pro mode), which re-derived the proofs of 1,184 statements and typeset them in under 12 hours (its inputs were built on 16 Nov at 18:20 UTC, its final came on 17 Nov at 06:01 UTC), slowed down here for checking another run's proofs, rerunning computations with new code and searching the literature. A night run, or more than one; two Pro runs per account.

## What is attached and what is left out

- Zip 1, per run: the register, the report, the paper's TeX and its sections, the notes TeX and records, the check-event files and the bibliography. Left out: code, data, builds, PDFs, page renders and QA images, history copies, manifests, vendored TeX runtimes, nested checkpoint zips.
- Zip 2: only the code and data files that a register row names as its evidence.
- Zip 3: every document our intake ledger attributes to these runs (intakes, expert notes, referee reports, debate notes, main-session notes, prompt-item files), plus the reviews and checks the ledger does not scan (found for this build), the per-row coverage tables, the companion outline with its open items, the placement table of 3,929 Longue Marche statements, the check ledger and the mathematics to-do of 17 Nov.
- Zip 4: the prompts as sent, with their provenance.
- Privacy: home-folder paths in our notes are rewritten to `C:\Users\<user>\`; each zip's MANIFEST.tsv lists every member so changed. No other change.

## Not found or not attached

- LM4_SUCCESSOR: the run's hourly progress reviews are inside its `historical_data.tar` (1.9 GB), which is not attached; the final intake (zip 3) summarizes them. The 61 work files of the paper that checkpoint 40 does not hold are taken from checkpoint 36, the newest that holds them.
