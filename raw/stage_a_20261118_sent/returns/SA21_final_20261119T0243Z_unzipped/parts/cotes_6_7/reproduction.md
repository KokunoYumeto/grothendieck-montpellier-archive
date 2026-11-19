# Reproducing this part

All paths below are relative to `/workspace/scratch/4017236f14bf` unless stated otherwise. All writes by this reader are confined to `SA21_work/parts/cotes_6_7` (the additional IX assignment is separate).

## Programs actually run

1. `python SA21_work/parts/cotes_6_7/read_source.py <folder-id> ...` emitted every supplied VI/VII transcription with original line numbers. Short notes were read separately in the initial complete-reading pass. The script, `read_outputs/` and `read_log.tsv` retain the complete transcription emissions. Tool-display truncations were resolved by targeted `sed` reads of the omitted ranges. Verdicts were made by model reading, not by this script.
2. `python SA21_work/parts/cotes_6_7/check_finite_examples.py` wrote `finite_checks_output.json`. It was rerun after adding an explicit exhaustive check of the stronger VI complete join-prime formulation of At2 and deterministic subset ordering. The saved source is the final executed version; the output lists every condition and limitation.
3. `python SA21_work/parts/cotes_6_7/build_deliverables.py > SA21_work/parts/cotes_6_7/build_output.txt 2>&1` serializes hand-authored claim/problem/ancillary records into the requested files. It does not infer mathematical verdicts. Its source and imported manually authored records are included. Initial serialization before the ancillary table existed was rerun after that table was authored.
4. `python SA21_work/parts/cotes_6_7/validate_deliverables.py` writes `validation_output.json`; it validates schema, references and saved finite results only.

The shell was also used for read-only inventory and exact-passages: `ls -l SA21_work/parts/cotes_6_7`, `cat` of the authoritative prompt, saved scripts, read log and complete reading outputs; `rg -n` for scan markers, axiom labels and explicit page cross-references in `sources/texts/codex/J156-{6,7}-*_transcription.tex`; and `sed -n` to reread selected original line ranges. These are locator/read operations, not proof checking. The following cross-cote endpoint reads were made directly: IV `J156-4-07` lines75–160 and `J156-4-08` lines35–68; III `J156-3-01` lines288–321 (an earlier exploratory lines120–180 read did not contain the target and was not treated as the reference); V `J156-5-03` lines35–81; VIII `J156-8-01` lines225–266 and `J156-8-06` lines1–46. The III locator was resolved with `rg` on the scan9/tronçon markers rather than trusting a neighbouring reader's compressed-output line count.

## Literature tools and logs

`search_S67_01.json` through `search_S67_13.json` preserve exact search requests/results, date and source IDs. `open_O67_01.json` through `open_O67_15.json` preserve opened/found primary passages and access errors. `search_log.tsv` maps search families to the precise claim records. Searches used both exposed engines and site/domain-specific queries for the named databases; direct zbMATH attempts returned403, some EGA PDFs exceeded the fetch limit, original Raney/deJongh–Troelstra URLs failed, and Dacey's thesis was not obtained. Those failures are not interpreted as negative mathematical evidence.

The bibliography distinguishes verified primary text/metadata from originals not obtained. Ore1944 was read in a reproduction of the primary article after the AMS PDF failed; the host's generated summary and title were not used. The exact P4 example was checked in the published2023 article; the first arXiv submission date was checked separately, but its v1 PDF failed to fetch. All URL requests can be reproduced from the JSON logs without relying on source-ID availability in a later session.

## Manual reasoning

`formalism_and_checks.md` records independent arguments and clause-by-clause finite-model compliance. `check_events.tsv` states the actual kind of each check. The complete original reading notes, including an initial finite-type compactness suspicion later withdrawn, are retained in `reading_analysis.md`; the correction is explicit in the proof file, claims map and narrative.

No scan decision, external upload, library operation or checkpoint archive was performed by this child reader. The parent owns preservation and final packaging.
