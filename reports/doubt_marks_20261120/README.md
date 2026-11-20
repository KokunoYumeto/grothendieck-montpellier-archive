# The doubt marks of the Montpellier archive transcription (working report, 20 Nov 2026)

[DOUBT_MARKS_REPORT_20261120.md](DOUBT_MARKS_REPORT_20261120.md) is the report; the `.html` file beside it is the same
report as a styled page. It counts the doubt marks (`\unsure{...}`, `\illegible{n}`) still open in our transcription of
the archive, sorts them by kind and by where they sit, and measures what each second-pass design did with them. It is a
working report: we rebuild it as returns come in, and the method is still being developed.

## Provenance

- **Written by** Claude (Claude Opus 5.5 at effort max), from the files, by the scripts in [`scripts/`](scripts/). Every
  number is computed; none is typed by hand.
- **Inputs:**
  - the returns of the second passes and of the doubt-marks-only run DM01 (GPT-6 Astra, ChatGPT Pro mode), each with the
    prompt as sent: [grothendieck-longue-marche `raw/pro_returns/`](https://github.com/KokunoYumeto/grothendieck-longue-marche/tree/main/raw/pro_returns)
    (the SP and DM folders);
  - the first readings and the text of record of each page (the best reading of each page);
  - Michel Hua's transcription ([Commutator-IO/grothendieck-project](https://github.com/Commutator-IO/grothendieck-project)),
    used only as a second witness, compared position by position; his text is not reproduced here.
- **Method:** [`scripts/texalign.py`](scripts/texalign.py) lines up the first reading, a pass's final text and Hua's page
  word by word, and classifies each doubt mark. It was checked against DM01's own recorded decisions (section 2 of the
  report). The paths in the scripts start at `<project root>`, our working folder.
- **The overall method** of the transcription: [METHODOLOGY.md](../../METHODOLOGY.md).
