# Methodology

All text in this repository is AI-produced. Models are named with their effort setting.

1. Scans: the university's PDFs, split into packages of about 45 scans (a cote, or neighbouring cotes).
2. First pass: GPT-6 Astra (ChatGPT Pro mode), one package per conversation, with the scans and a context zip (our
   transcription of La Longue Marche, its research notes, the archive's section map, and the research notes of earlier
   packages of the same cote). The transcription is written first and frozen; only then are the research notes written
   with the context. Marks: \unsure{a|b}, \illegible{n}, \deleted{...}, \inserted{...}, \margin{...}. The prompt as
   sent is in each package folder.
3. Second pass: Claude Opus 5.5 at effort max, one block of about 15-18 scans per agent, every line read against the
   scan halves and enlarged crops; every change logged with its evidence and a confidence; the research notes checked.
4. Typed and printed pages: Claude Opus 5.5 at effort high through the Anthropic Message Batches API (1,361 pages for
   $93.38), and GPT-6 Astra at its maximum reasoning setting in Codex web (one folder of 4-11 pages per task).
5. Coordination, packaging and these files: Claude Opus 5.5 at effort max in Claude Code.
