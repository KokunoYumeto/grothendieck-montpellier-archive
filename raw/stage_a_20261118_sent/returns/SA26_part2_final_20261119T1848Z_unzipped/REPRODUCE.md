# SA26: reading and reproducing this dossier

Start with `SA26_dossier.md`. The numbered tables are the canonical consolidated
records; the `parts/` directories retain the detailed arguments and the original
contributions used in assembly. The 63 entry verdicts were authored after reading
the notes and their transcription passages. The scripts serialize and validate
those judgments; they do not infer judgments from headings or keywords.

## Files and scope

The ten requested deliverable groups are at the archive root. Additional useful
tables are `SA26_refinements.json`, `SA26_self_flags.tsv`,
`SA26_literature_search.tsv`, `SA26_verified_textual_links.tsv`,
`SA26_context_links.tsv`, and the three project/provenance annexes.

The source attachments are intentionally absent. The input manifest records all
six source files and their hashes. To rerun input-dependent assembly, extract this
archive into a directory named `deliverable/` and place the original unpacked
attachment directories under the sibling `sources/` directory:

- `sources/SA26_notes/NOTES_INDEX.tsv` and its `pro/` files;
- `sources/SA26_texts/TOPIC.md`, `PREAMBLE.tex`, and its `pro/` transcription.

The public editions and third-party papers are not bundled. The bibliography gives
opened URLs and exact consulted locators. Retrieval logs preserve exact retained
requests, returned source identifiers, titles and access failures; full copied
web excerpts have been removed from the distributed audit. The first homotopy
search capture lacked query parameters; its limitation and a genuinely rerun
replacement query are explicitly recorded.

## Reproduce the mathematical computations

These programs use only Python's standard library and print their complete results:

```bash
python parts/cote106/code/algebra_checks.py
python parts/cote107_objects/code/finite_checks.py
python parts/cote107_homotopy/code/check_telescope.py
```

Their original outputs are in the corresponding `parts/.../audit/` directories.
Independent executions during assembly are preserved as `audit/recheck_106_algebra.out`,
`audit/recheck_107_objects.json` and `audit/recheck_107_telescope.json`.
The results match. These are exact symbolic or finite calculations. They do not
certify the infinite arguments; those are written out in the three proof audits.

## Reproduce structural assembly

With the source layout above, run from the extracted `deliverable/` directory:

```bash
python code/build_self_flag_crosswalk.py
python code/assemble_dossier.py
python code/validate_final.py
```

Assembly preserves the manually authored data, normalizes the phrase “open on the
pages”, canonicalizes the duplicate `GrothDerXVIII` reference as `DerXVIII`, combines
independently consulted bibliography annotations, normalizes refutation event types,
qualifies actual proof/program paths, maps contextual “other runs” to the required
`our projects` link kind, and produces counts and cross-reference checks. Its time-stamped root review rows
will naturally carry the rerun timestamp. All original contribution records remain
available to inspect. The final validator checks the dossier's structure and the
agreement of reproduced outputs; it is not a formal proof checker.

The earlier generators under `parts/` and `code/build_root_*` are retained as the
programs used to write the contributions. They are not prerequisites for reading
or verifying the final tables. Running them can overwrite later editorial refinements.
Some original child validators expected the raw web-response shape used during
their run. The distributed logs now retain metadata only; `code/validate_final.py`
is the validator for that final audit format.
`code/polish_dossier.py` records an early typography pass and is not intended to be
rerun on the final text; `code/final_editorial_fixes.py` records the bounded final
corrections. The Brown download/inspection helper retains its original workspace
path and needs network access and PDF utilities if reused elsewhere.

## Interpreting verification

`note={verified}` means the linked work or record was opened. Each annotation says
whether mathematical text, edition metadata, or only a lead was inspected. A
verified URL is not a blanket certification of the whole work. Four unverified
bibliography records remain explicitly labelled leads.

`CHECK_EVENTS.tsv` distinguishes textual checking, proof review, independent
re-proof, finite computation, refutation and background use. Corrected statements
referenced by refutations are defined either as claim IDs or in
`SA26_refinements.json`. Model effort was not exposed and is not invented.

The 26 self-flags, R1–R11 subnotes and H01–H13 subnotes have explicit coverage.
Every private-context link preserves its note IDs and cited provenance while
stating that the private target proof was unavailable. Such rows are not adopted
as verified two-endpoint mathematical results. No scan image was available; the
38 reading alarms remain undecided and the transcription is unchanged.

## Integrity

`FILES.sha256` lists the archive's file hashes, excluding itself. No input archive,
earlier checkpoint, generated ZIP or downloaded full paper is nested in the
deliverable. `progress.log` records UTC stage times. `audit/` retains structural
validation outputs and the corrected administrative failures as well as successes.
