# Source handling and conventions

The separately attached PROMPT(20261119-011407).md governs this run. Its only differences from the zipped PROMPT.md concern checkpoints (45 minutes instead of one hour) and continuing after an execution outage. The separately supplied prompt is treated as the more recent explicit override. No scans and no second_pass files were supplied.

Line numbers mean 1-based physical lines of the exact attached transcription file; cote and scan identify the manuscript page. A scan marker governs following lines up to the next marker. Diplomatic uncertainty marks are preserved; mathematical arguments never silently replace an uncertain reading.

The source archives were unzipped with Python zipfile after checking each resolved member path stayed under its destination. Source texts are kept in sources/ outside the deliverable archive. All substantive code and outputs, source-reading outputs, searches, hand-authored audit data and verification results are retained in SA21_work. Generated indexes are navigation tools, not mathematical verdicts.

The run model is GPT-6 Astra Pro. The runtime does not expose an independently verifiable numerical effort setting, so check events identify effort as not exposed. Root and three parallel readers identify themselves separately. Content comparison is explicitly distinguished from proof checking in check-event outcomes.

The date of the run is 2026-11-19. UTC is used in progress and check logs as the prompt requests. Literature coverage is bounded by what the search service can retrieve on that date; absence of a matching result is never evidence of absolute nondevelopment.

Initial programs: the initial archive inventory used pathlib.Path, read_text, zipfile.ZipFile.infolist and json.dumps to read the two attached Markdown files and list members of three archives. The extraction command used ZipFile.extractall after member traversal validation, created the SA21_work directories and wrote run_metadata.json and progress.log. The second inspection used difflib.unified_diff for the two prompt variants, printed PREAMBLE.tex and enumerated NOTES_INDEX.tsv with csv.DictReader. These nonmathematical setup operations are documented here; all subsequent substantive programs are saved verbatim in code/ or the responsible reader's directory.
