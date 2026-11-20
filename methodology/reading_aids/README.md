# Reading aids: what every second pass and implementation run reads first

These files go into the zip of every second pass and every implementation run on the Montpellier archive (from 20 Nov
2026), and they are refreshed here at every intake of returns. The runs are ChatGPT Pro (GPT-6 Astra, ChatGPT Pro mode);
the sheet is compiled by Claude (Claude Opus 5.5 at effort max) from the measurements below and from the patterns found by
Claude Fable 5.2 at effort max.

| file | what it is | how it is made |
|---|---|---|
| `COMMON_ERRORS_SHEET.md` | "Read this before working": the errors that recur in these papers, with measured rates; per-cote letter swaps; what is not ink (the paper's watermark, specks); typescripts; how a place is decided (the ink first, then his notation and the mathematics where the ink admits two readings; nothing normalised) | compiled from the files below; every run returns feedback on it |
| `HAND_LOGS.tsv` | his habits of hand, as each run logged them (a letter he writes like another, whether the habit holds elsewhere, whether it predicts errors) | collected from the `*_hand_log.md` of every return; the rows of the same cotes go into the zips of the waiting runs on those cotes |
| `SHEET_FEEDBACK.tsv` | the recurring issues each run reports against the sheet | collected from the `*_sheet_feedback.md` of every return |
| `FEATURE_RATES.tsv`, `LETTER_SWAPS.tsv`, `SYMBOL_SWAPS.tsv` | how often the first reading erred, by feature, letter and symbol, measured against the second passes token by token | measured on every returned second pass |
| `SP_CHANGE_PATTERNS.md`, `NOBODY_DOUBTED.tsv` | what the second passes changed, by class; the changes at places no reader had marked as doubtful | measured on every returned second pass |
| `FABLE_PATTERNS_2_20261120.md` | the error patterns Claude Fable 5.2 at effort max found in the measurements (N1-N17) | one analysis, 20 Nov 2026 |
| `IM_TEMPLATE_20261120.md` | the prompt of the implementation runs, which put the decided corrections into the pages | the template the implementation prompts are built from |

Each run's prompt, as sent, is kept with its return in `grothendieck-longue-marche/raw/pro_returns/`.
