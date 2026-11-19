# SA07 part 3 collaboration protocol

Read user PROMPT fully. Complete substantive research, not an automatically classified catalogue. The root is integrating three independent package readers and Codex folder review.

Only edit your assigned agents/<name>/ directory. Source files in work/ are immutable. Use exact physical line numbers of provided .tex files (1-based), plus cote and scan; cite filenames when a single scan has multiple versions. A second-pass changed reading is current, but do not modify source files. No scans were supplied.

Read every indexed ### entry in your package and the transcription passages it concerns. Read the complete transcription to find statements or open steps missed by notes. Headings and scripts may help navigate, never decide verdicts. Notes can contain earlier-run inventions; label them as such. For out-of-topic cotes bundled with a package, judge every indexed entry, but clearly segregate external-context material instead of silently presenting it as motives.

Write incremental JSON arrays/JSONL of items, claims, problems and TSV verdicts, readings, links, check events. At completion use exact field names in user prompt. All source entries must receive individual reasons derived from reading. Merge genuine duplicates; do not group unrelated entries under a generic theme. Claim id use CL-SA07-NNN (your assigned range); items SA07-N; problems MP-SA07-NN. Root may renumber at integration.

Every mathematical claim needs a searched fate. Search primary literature, using web tools, including named repositories/secondary discovery indexes in prompt as appropriate; a search is not proof of absence. Check exact hypotheses and record searches, returned sources, opened URLs and exact theorem/page locators in literature_search.tsv and refs.json. Each reference: key,title,authors,date,first_circulation,publication,url,verified,locator,result_used. Open all references marked verified. Retain raw web query/open results under evidence/ and record queries, even if no relevant result.

For each checked/used statement (item, claim, reference) record CHECK_EVENTS.tsv with statement_id,date,who,type,outcome. Who: GPT-6 Astra Pro; effort not exposed; SA07-part3/<agent>. Use actual event types: targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id. Text comparison is used and rechecked, not independent proof. Merely quoted mathematical results may be carried as background. Do not claim a mathematical proof by reading an abstract.

Redo every actual computation underlying your claims with explicit derivation, code if computable, and output. No meaningless finite checks as proof of general theorems. Save every program and output you execute (navigation utilities can be collected in commands.log; research code must be preserved as files with outputs). Summarize unexecutable symbolic derivations in computations.md.

Stage 5: links need both endpoints checked. If the other endpoint is not supplied, label external lead unverified; do not assert verified equivalence. Own cross-references and other-project leads should remain separate. Source note ids mandatory for project links.

Stage 6: directions brief, ranked, cite item/claim/problem ids; develop none. Save package_summary.md with main findings, exact caveats, coverage counts and recommended cross-package merges. Root handles checkpoints and final delivery. Do not save your own separate Library deliverable or checkpoint. Communicate substantive progress to root periodically, and continue until all allocated work done. There is no requested time limit.
