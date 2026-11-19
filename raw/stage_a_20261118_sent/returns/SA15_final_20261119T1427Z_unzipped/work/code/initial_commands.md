# Commands executed before audit helpers were installed

1. Read `upload/PROMPT(20261119-130151).md` with `cat`; output is the complete user brief.
2. Python `zipfile.ZipFile.infolist()` printed the attachment inventory (23 files); no recursive unzipping.
3. Python validated all ZIP destinations were below `sources/`, then `extractall('sources')` once. Printed TOPIC, NOTES_INDEX and PREAMBLE.
4. Read NOTES_INDEX again because the first combined output was truncated by unrelated tool metadata. The complete second output had exactly 80 indexed entries in one package.
5. Python printed note-heading counts and the first 45 lines of each Pro transcription, detecting the level-two versus level-three heading discrepancy.

These were source inspection operations, not mathematical proof checks. The equivalent extraction/inventory logic is recorded in `bootstrap.py`, which does not re-extract the sources.
