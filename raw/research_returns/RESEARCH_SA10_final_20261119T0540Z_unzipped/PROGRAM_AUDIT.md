# Complete saved-program audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.

Snapshot: **2026-11-19T05:38:55.754859+00:00**. **32 programs**, including this catalog generator; **10 mathematical certificate programs**. No inventoried program was rerun to produce this catalog.

Every count and duration below comes from an existing observed output, except the catalog generator's own current-run measurement. Historical outputs are not silently promoted to measurements of later edited files. A script runtime, a tool wall time, and an uninstrumented run are explicitly distinguished.

Machine-readable records: `PROGRAM_AUDIT.tsv`. Exact file inventory and SHA256s: `PROGRAM_AUDIT_FILES.tsv`. Requested-source matrix: `REQUESTED_SOURCE_STATUS.md` and `.tsv`. Paths are relative to the working deliverable directory; `../primary` and `../texmf` are external research/runtime inputs.

## Coverage and missing evidence

- Missing saved output: none.
- No printed script elapsed time: code/check_tex_runtime.lua; code/fetch_supplement_sources.py; code_C/build_C_sections.py; code_C/build_C_source_audit.py.
- Newly auto-discovered programs: none.
- `fetch_supplement_sources.py` failed with HTTP403 before its elapsed-time print; the saved traceback is an observed output, not a successful download.
- `check_tex_runtime.lua` is uninstrumented. `build_C_sections.py` is uninstrumented; its separately recovered tool wall time is labelled as such in the saved output.
- Preserve all four original code directories, the `stable_graph_data` JSONs, and the source/build logs. Final packaging additionally mirrors agent code under `code/programs/` and copies the source-fetch log into `code/`; these aliases are excluded from source discovery and inventory counts to avoid double counting. Each program's primary observed stdout/JSON is retained under the final code subtree; supplementary build logs and generated documents keep their recorded locations. Full fetched copyrighted sources and third-party TeX runtime packages remain excluded. This catalog does not relocate execution paths or assert that embedded working paths are portable.

## Mathematical certificates

### `code/check_A_finite.py`

Finite A1 gluing and Cech-arity counterexamples; A4 finite-meet colimits; R3/R6 support identities.

- **Inputs:** Embedded finite posets, sheaf maps, assignments and meet diagrams; no external input file.
- **Observed output:** `code/check_A_finite.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 9 distinct all-pair objects;14 nonidentity inclusions;32 successor assignments,0 extensions;7-index examples12→1 and19→2 points;three Cech-arity witnesses;9 failed strict-bound comparisons.
- **Timing:** observed printed timing — seconds=0.000640s.

### `code/stable_graph_meets.py`

Exhaustive stable-graph generation by inverse single-edge contractions; canonicalization and common-refinement tests.

- **Inputs:** Embedded (g,n) cases (0,3),(0,4),(0,5),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(3,0); genera, labelled legs, loops and multiple edges.
- **Observed output:** `code/stable_graph_meets.out`.
- **Generated artifacts:** code/stable_graph_data/g0_n3.json;code/stable_graph_data/g0_n4.json;code/stable_graph_data/g0_n5.json;code/stable_graph_data/g1_n1.json;code/stable_graph_data/g1_n2.json;code/stable_graph_data/g1_n3.json;code/stable_graph_data/g1_n4.json;code/stable_graph_data/g2_n0.json;code/stable_graph_data/g2_n1.json;code/stable_graph_data/g3_n0.json.
- **Observed scope/counts:** 10 cases;graph counts1,4,26,2,5,23,163,7,16,42;pair counts0,6,325,1,10,253,13203,21,120,861;meet failures only (1,4):21,(2,1):2,(3,0):25. Full graph/contraction/failure lists saved.
- **Timing:** observed printed timing — elapsed_seconds=1.847699604695663e-05s; elapsed_seconds=0.00013880499318474904s; elapsed_seconds=0.001682411995716393s; elapsed_seconds=3.1104995287023485e-05s; elapsed_seconds=0.0001572719993419014s; elapsed_seconds=0.013842715001374017s; elapsed_seconds=0.15386597600445384s; elapsed_seconds=0.00021443599689519033s; elapsed_seconds=0.000957172000198625s; elapsed_seconds=0.044610784003452864s.

### `code_B/check_B_finite.py`

Integral normalized C2 bar differential and tetrahedral sphere cocycle/coherence witnesses.

- **Inputs:** Embedded C2 and tetrahedral boundary;SymPy exact integer linear algebra.
- **Observed output:** `code_B/check_B_finite.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 8 associativity triples and2 inverses;bar differentials through degree4;H1(BC2;Z)=Z/2;tetrahedron4 vertices6 edges4 faces;rank(d2)=3;integral cocycle pairing−1.
- **Timing:** observed printed timing — elapsed_seconds=0.091153s.

### `code_B56/check_B56.py`

Finite-set presentations, global relation countermodel, forest/orbit conditions, symmetric group nerve and hypercover nonimplications.

- **Inputs:** Embedded finite sets/functions,C2 actions and exact rational simplex functions;no external data.
- **Observed output:** `code_B56/check_B56.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 14 corrected low-degree relations;56 finite maps;412 global countermodel instances;4 C2 cospans/8 squares;mod2 H1 dimension1;16 symmetric products;1528 cospans/6871 target pairs;126 monotone maps;30 rational amalgams.
- **Timing:** observed printed timing — runtime_seconds=0.044837s.

### `code_B56/check_B6_translation.py`

Check every coface/codegeneracy cycle-word substitution into the manuscript's delta,K,permutation generators.

- **Inputs:** Embedded finite-set maps for every n1–12 and every allowed index i.
- **Observed output:** `code_B56/check_B6_translation.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 90 coface words+78 codegeneracy words=168 checks;zero failures;last generators recovered literally.
- **Timing:** observed printed timing — seconds=0.000609891s.

### `code_B56/check_C5_boundary_group.py`

Check a nontrivial finite quotient of the opened Mazur-boundary group presentation.

- **Inputs:** Embedded presentation <x,y|y^5=x^7,y^4=x^2 y x^2>;fixed7-cycle;all5-cycles on7 points.
- **Observed output:** `code_B56/check_C5_boundary_group.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 504 five-cycles checked;14 solutions;chosen x,y generate A7 of order2520;both defining relations explicitly evaluated.
- **Timing:** observed printed timing — seconds=0.006783651s.
- **Qualification:** Certifies the recorded group's nontriviality; does not replace the geometric verification of a handle presentation.

### `code_B56/check_matching_independence.py`

GF2 cocycle matching-map ranks for the independently indispensable hypercover degrees.

- **Inputs:** Embedded cocycle models K(F2,n),n1–4,simplex degree k0–7.
- **Observed output:** `code_B56/check_matching_independence.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 32 comparisons;for each n exactly degree k=n+1 fails, image codimension1. Full row data in stdout.
- **Timing:** observed printed timing — runtime_seconds=0.016021s.

### `code_B56/check_stable_graphs_independent.py`

Independent direct bounded-multigraph enumeration of the positive stable-graph cases, distinct from the root inverse-contraction algorithm.

- **Inputs:** Embedded (g,n)=(1,1),(1,2),(1,3),(2,0);all bounded genera/legs/edge multiplicities.
- **Observed output:** `code_B56/check_stable_graphs_independent.out`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** Candidate counts2,22,717,18;graph counts2,5,23,7;pair counts1,10,253,21;compatible pairs1,8,107,18;zero failures.
- **Timing:** observed printed timing — runtime_seconds=4.4e-05s; runtime_seconds=0.000146s; runtime_seconds=0.00284s; runtime_seconds=0.000157s.

### `code_C/check_cone_transitions.py`

Cellular quotient certificate for the missing selected-prefix transitions and the corrected simultaneous-cone construction.

- **Inputs:** Embedded constant one-point chain diagrams with0–6 vertices;union-find of cells under transition families.
- **Observed output:** `code_C/check_cone_transitions.output.json`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** Two-vertex old diagram:2 components,3 vertices,1 edge;corrected:1 component,2 vertices,1 edge. All7 chain sizes0–6 checked;at6 vertices364 blocks,2366 raw cells,2276 transitions,quotient cell counts6,15,20,15,6,1.
- **Timing:** observed printed timing — elapsed_seconds=0.024328412s.

### `code_C/check_cote150.py`

Projection-control twist counterexample;Boolean flag intervals;exact genus4 branch-set automorphisms;quotient local homology.

- **Inputs:** Embedded6-point twist;all naturally labelled posets through5 elements;ten rational/infinite branch points;SymPy and Fraction exact arithmetic.
- **Observed output:** `code_C/check_cote150.output.json`.
- **Generated artifacts:** stdout only; no separate artifact.
- **Observed scope/counts:** 6 twist vertices/6 strict arrows/2 transitivity failures;poset counts1,1,2,7,40,357;4135 flags/10603 intervals;720 Mobius candidates,only identity;genus4 tangent invariant/anti-invariant dimensions7/2;local torsion Z/2 in degree16.
- **Timing:** observed printed timing — runtime_seconds=0.129894s; runtime_seconds=0.724255s; runtime_seconds=3.3e-05s; total_runtime_seconds=0.854292s; runtime_seconds=4e-05s.

## Retrieval, typesetting, metadata, packaging and audit programs

### `code/build_paper.py`

LuaLaTeX/BibTeX build, task-local TeX support/cache setup, build-history preservation and overflow/citation checks.

- **Inputs:** RESEARCH_SA10_paper.tex and recursive inputs;RESEARCH_SA10_references.bib;existing aux;task-local texmf;system TeX fonts/maps.
- **Observed output:** `code/build_paper.out;logs/build_summary.json`.
- **Generated artifacts:** RESEARCH_SA10_paper.pdf;RESEARCH_SA10_paper.log;RESEARCH_SA10_paper.aux;RESEARCH_SA10_paper.bbl;pdftex.map;logs/build_*.out;logs/build_summary.json;logs/build_history/**.
- **Observed scope/counts:** Overfull boxes: [1.4243, 0.20518] | Overfull boxes exceeding 2pt: 0 | Runtime: 23.495529 seconds | "overfull_pt": [ | "overfull_exceeding_2pt": 0, | "runtime_seconds": 23.495528904997627, | "missing_characters": 0, | "undefined_citations": 0
- **Timing:** observed printed timing — Runtime=23.495529s; runtime_seconds=23.495528904997627s.
- **Qualification:** Build outputs are snapshots and may change with the final build. Preserve all existing history logs; this catalog does not run a build or authorize PDF delivery.

### `code/check_tex_runtime.lua`

Inspect task-local TeX cache directory permissions and compare lfs writable-file result with an actual temporary-file write.

- **Inputs:** Task-local tex_cache directory and LuaFileSystem module.
- **Observed output:** `code/check_tex_runtime.out`.
- **Generated artifacts:** Temporary runtime_test.tmp is removed by the program..
- **Observed scope/counts:** Observed isdir=true, writable-file predicate=nil, actual write=true.
- **Timing:** not instrumented.
- **Qualification:** No script timing instrumentation. This is environment diagnosis, not a mathematical check.

### `code/fetch_primary_A.py`

Download/identify cote151, SGA4 tome1 and Schmitt notes; record bytes, SHA256 and per-file duration.

- **Inputs:** URLs embedded in script: Montpellier151.pdf;CMLS SGA4 tome1.pdf;Bonn Schmitt Script.pdf.
- **Observed output:** `code/fetch_primary_A.out;logs/fetch_primary_A.out`.
- **Generated artifacts:** ../primary/151.pdf;../primary/SGA4_tome1.pdf;../primary/Schmitt_ModCurves.pdf.
- **Observed scope/counts:** 3 completed files:27695508,1512797,6518673 bytes;each SHA256 saved.
- **Timing:** observed printed timing — seconds=632.8592769669995s; seconds=23.43754161099787s; seconds=6.256165902996145s.
- **Qualification:** Original stdout is logs/fetch_primary_A.out; the package preflight also preserves it as code/fetch_primary_A.out. Identical copied logs are not counted as separate runs. Fetched full primary PDFs are research inputs excluded from the deliverable.

### `code/fetch_supplement_sources.py`

Attempt a local download and text extraction of Goresky–MacPherson Stratified Morse Theory.

- **Inputs:** https://www.math.ias.edu/~goresky/pdf/SMT.pdf
- **Observed output:** `code/fetch_supplement_sources.out`.
- **Generated artifacts:** Intended ../primary/Goresky_MacPherson_SMT.pdf/.txt;not produced by the failed observed run..
- **Observed scope/counts:** One attempted request;HTTP403 before timing output.
- **Timing:** instrumented, but no elapsed time in the observed output.
- **Qualification:** Failure log is preserved. The full text was separately opened online; download failure is not an unopened-source claim. Timing instrumentation exists but was not reached.

### `code/fetch_tex_support.py`

Fetch three CTAN LuaLaTeX support archives and extract task-local runtime files; generate lualibs entry point when needed.

- **Inputs:** CTAN luaotfload.zip;lualibs.zip;lua-uni-algos.zip;local LuaTeX executable.
- **Observed output:** `code/fetch_tex_support.out`.
- **Generated artifacts:** ../texmf/tex/luatex/luaotfload/*;../texmf/tex/luatex/lualibs/*;../texmf/tex/luatex/lua-uni-algos/*.
- **Observed scope/counts:** 3 archives:1993888,282788,95510 bytes;103,35,11 extracted runtime files (149 total).
- **Timing:** observed printed timing — Runtime=23.239087s.
- **Qualification:** Third-party runtime packages are not mathematical code authored in this run; retain the fetch program and observed log.

### `code/finalize_qa.py`

Seal the PDF verification record after matching the final PDF hash, successful build metrics and three independent visual-inspection records.

- **Inputs:** RESEARCH_SA10_paper.pdf;qa/render_manifest.json;logs/build_summary.json;PDF_VISUAL_ROOT.md;PDF_VISUAL_B.md;PDF_VISUAL_C.md;logs/build_history/20261119T052014525518Z/build_pass2.out.
- **Observed output:** `code/finalize_qa.out`.
- **Generated artifacts:** qa/final_qa.json;PDF_QA_REPORT.md;logs/PDF_QA_APPROVED.txt.
- **Observed scope/counts:** Runtime 0.004582853 seconds.
- **Timing:** observed printed timing — Runtime=0.004582853s.
- **Qualification:** Checks recorded image inspections rather than treating a successful render as visual approval. Before/after overflow counts and the exact PDF hash are retained in its artifacts.

### `code/finalize_report.py`

Assemble the outcome-first final report from the root conclusions, source/program catalogs, detailed proof/correction records and publication/register audits.

- **Inputs:** REPORT_ROOT.md;REQUESTED_SOURCE_STATUS.md;PROGRAM_AUDIT.md;agent_B_levels.md;agent_B56.md;C_source_corrections.md;C5_Hurewicz_review.md;C5_audit_B.md;PDF_QA_REPORT.md;FINAL_register_audit_B56.md;RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv.
- **Observed output:** `code/finalize_report.out`.
- **Generated artifacts:** RESEARCH_SA10_report.md.
- **Observed scope/counts:** Assembled final report: 10 sections/source records; 129858 characters; 74 results; 302 events. | Runtime 0.006510858 seconds.
- **Timing:** observed printed timing — Runtime=0.006510858s.
- **Qualification:** Observed character/section/result/event counts refer to the saved run. A later assembly may include a refreshed version of this catalog.

### `code/finalize_root_records.py`

Record the root's late source/proof checks and annotate exact A-result dependencies.

- **Inputs:** Embedded actual check descriptions;RESULTS_A.csv.
- **Observed output:** `code/finalize_root_records.out`.
- **Generated artifacts:** CHECK_EVENTS_ROOT_FINAL.tsv;RESULTS_A.csv.
- **Observed scope/counts:** Recorded 72 actual root check events; annotated 15 A result dependencies. | Runtime 0.001156276 seconds. | Recorded 73 actual root check events; annotated 15 A result dependencies. | Runtime 0.001005915 seconds.
- **Timing:** observed printed timing — Runtime=0.001156276s; Runtime=0.001005915s.

### `code/integrate.py`

Aggregate result CSVs, check events and bibliography fragments; reject duplicate result IDs or bibliography keys; normalize recorded event labels when configured.

- **Inputs:** RESULTS_A.csv;RESULTS_B.csv;results_B56.csv;RESULTS_C.csv;RESULTS_C1_B.csv;CHECK_EVENTS_*.tsv;references_A.bib;B_references.bib;references_B56.bib;C_references.bib;references_C5_Hurewicz.bib;references_supplement.bib.
- **Observed output:** `code/integrate.out`.
- **Generated artifacts:** RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv;RESEARCH_SA10_references.bib;CHECK_EVENT_NORMALIZATION.tsv when produced..
- **Observed scope/counts:** Assembled 74 result rows, 302 check events, 40 bibliography records. | Runtime: 0.007535 seconds
- **Timing:** observed printed timing — Runtime=0.007535s.

### `code/make_checkpoint.py`

Create a new numbered full-work checkpoint with SHA256 manifest, excluding supplied/fetched sources and earlier ZIPs; refuse overwrite or ≥500MB.

- **Inputs:** CLI checkpoint number;current work tree;PDF_QA_APPROVED marker;library_helpers/*.py.
- **Observed output:** `code/make_checkpoint_01.out;code/make_checkpoint_02.out`.
- **Generated artifacts:** CHECKPOINT_<NN>_FILES.tsv;../RESEARCH_SA10_checkpoint_<NN>.zip.
- **Observed scope/counts:** 89 working files; 296541 compressed bytes; runtime 0.192699 seconds | 303 working files; 25554624 compressed bytes; runtime 1.211560 seconds
- **Timing:** observed printed timing — runtime=0.192699s; runtime=1.211560s.
- **Qualification:** Checkpoint ZIPs remain separate; never place earlier checkpoint ZIPs inside the final ZIP.

### `code/make_final_package.py`

Verify the approved PDF hash,74 unique result rows and preserved checkpoint paths;prepare delivery-only code mirrors and helper records. Optional --build writes the final ZIP,hash manifest and CRC check while refusing overwrite or size≥500MB.

- **Inputs:** qa/final_qa.json;RESEARCH_SA10_paper.pdf;RESEARCH_SA10_report.md;RESEARCH_SA10_results.csv;CHECKPOINT_*_FILES.tsv;authored work tree;../library_helpers/*.py.
- **Observed output:** `code/make_final_package.out`.
- **Generated artifacts:** code/programs/{code_B,code_B56,code_C}/**;code/fetch_primary_A.out;support/library_helpers/*.py;DELIVERY_EXCLUSIONS.tsv;with --build only:DELIVERY_MANIFEST.tsv and ../RESEARCH_SA10_final.zip..
- **Observed scope/counts:** Preflight PASS: 299 selected current files; 74 results; QA digest matches; no missing checkpoint-manifest path. | Excluded 264 research-input/runtime files. No supplied attachment or previous ZIP is selected. | Preparation runtime 0.054080653 seconds.
- **Timing:** observed printed timing — runtime=0.054080653s.
- **Qualification:** The observed output currently records a default/preflight run only. It is not evidence that --build ran or that a final ZIP/CRC check has already succeeded. Delivery mirrors are excluded from program-source discovery because they duplicate the originals.

### `code/render_pdf_qa.py`

Render every PDF page with Poppler, create indexed contact sheets and locate theorem/citation keywords;record the exact PDF hash.

- **Inputs:** RESEARCH_SA10_paper.pdf;Poppler pdftoppm;PyMuPDF;Pillow.
- **Observed output:** `code/render_pdf_qa.out`.
- **Generated artifacts:** qa/pages/page-*.png;qa/contact/contact-*.png;qa/render_manifest.json.
- **Observed scope/counts:** "sha256": "1786ba59ec32382ec60392f23bd95ef926d14872f851478dbeb0771e12a79301", | "runtime_seconds": 23.081229158997303, | "note": "Rendering and text location only. Human-style image inspection must be recorded separately."
- **Timing:** observed printed timing — runtime_seconds=23.081229158997303s.
- **Qualification:** Observed current render has74 pages at110dpi and7 contact sheets. Rendering and keyword location do not themselves constitute visual approval; the output explicitly records visual_approval=false pending separate image inspection.

### `code/update_working_report.py`

Assemble the working report and update the dated progress ledger from explicit item/lead states and agent summaries.

- **Inputs:** Embedded19 item/lead states;agent_B_levels.md;agent_B56.md;PROGRESS_LEDGER.md.
- **Observed output:** `code/update_working_report.out`.
- **Generated artifacts:** RESEARCH_SA10_report.md;PROGRESS_LEDGER.md.
- **Observed scope/counts:** Updated 19 item/lead states. Runtime 0.001724 seconds.
- **Timing:** observed printed timing — Runtime=0.001724s.
- **Qualification:** Historical working-report generator. Its recorded run is not evidence that the current final report still has that wording.

### `code/verify_archive.py`

Verify an existing ZIP's CRC, every current manifest hash, duplicate-name byte identity and absence of nested ZIPs;final-delivery manifests additionally forbid duplicate names.

- **Inputs:** CLI archive pathname and --output pathname;embedded CHECKPOINT_<NN>_FILES.tsv or DELIVERY_MANIFEST.tsv.
- **Observed output:** `code/verify_archive.out`.
- **Generated artifacts:** JSON integrity report at the supplied --output pathname;observed stdout..
- **Observed scope/counts:** "bytes": 25554624, | "duplicate_bytes_identical": { | "runtime_seconds": 0.29703593300655484
- **Timing:** observed printed timing — runtime_seconds=0.29703593300655484s.
- **Qualification:** The observed saved run verifies checkpoint02:305 entries,302 manifest hashes,no mismatch or nested ZIP;two duplicated helper filenames have identical bytes. It is not an observed verification of the not-yet-built final archive.

### `code_B/download_sources.py`

Fetch Treumann source/PDF, Quinn PDF and Higher Algebra; preserve failures; decompress Treumann TeX.

- **Inputs:** Four URLs embedded in script;existing literature_B files.
- **Observed output:** `code_B/download_sources.out`.
- **Generated artifacts:** literature_B/treumann_source;literature_B/treumann.pdf;literature_B/treumann.tex;literature_B/quinn.pdf;intended literature_B/HA.pdf..
- **Observed scope/counts:** Treumann source34221 bytes and PDF451815 bytes already present;Quinn1370605 bytes downloaded;HA local request403;Treumann TeX decompressed.
- **Timing:** observed printed timing — elapsed_seconds=11.378s.
- **Qualification:** Higher Algebra was independently opened online. Fetched complete copyrighted source files are excluded from the package.

### `code_B/write_B_records.py`

Write B1–B4 result rows and their recorded check events.

- **Inputs:** Embedded statement/check descriptions.
- **Observed output:** `code_B/write_B_records.out`.
- **Generated artifacts:** RESULTS_B.csv;CHECK_EVENTS_B.tsv.
- **Observed scope/counts:** Observed output15 statement rows,29 check-event rows;later independent additions may increase the current event file.
- **Timing:** observed printed timing — elapsed_seconds=0.000767s.

### `code_B56/audit_final_register.py`

Recursively inspect actual manuscript inputs;match numbered statement headings to the requested five CSVs and exact-ID check events;verify citation keys/access labels.

- **Inputs:** RESEARCH_SA10_paper.tex and recursive TeX inputs;five result CSVs;source/aggregate CHECK_EVENTS;RESEARCH_SA10_references.bib.
- **Observed output:** `code_B56/audit_final_register.out;code_B56/audit_final_register_052044.out;code_B56/audit_final_register_053221.out;code_B56/audit_final_register_053641.out`.
- **Generated artifacts:** FINAL_register_audit_B56.md;FINAL_register_audit_B56.json.
- **Observed scope/counts:** "scope": "Actual recursive TeX inputs; only numbered statement headings, not equation tags or older drafts.", | "missing_includes": [], | "numbered_statements": 74, | "register_counts": { | "missing_result_rows": [], | "duplicate_statement_headings": {}, | "missing_exact_source_check_events": [], | "missing_exact_aggregate_check_events": [], | "inherited_C_ids_missing_exact_aggregate_event": [], | "missing_bibliography_keys": [], | "cited_bibliography_keys_missing_access_status": [], | "scope": "Actual recursive TeX inputs; only numbered statement headings, not equation tags or older drafts.", | "missing_includes": [], | "numbered_statements": 74, | "register_counts": { | "missing_result_rows": [],
- **Timing:** observed printed timing — seconds=0.012551097s; seconds=0.010835391s; seconds=0.017263091s; seconds=0.01214952s.
- **Qualification:** Does not execute mathematical tests or reopen every source. Records SHA256 snapshots; counts in stdout identify the audited version.

### `code_B56/build_program_audit.py`

Inventory all saved programs in four code directories;read their observed outputs;catalog requested-source opening evidence without executing inventoried programs.

- **Inputs:** code/**;code_B/**;code_B56/**;code_C/**;logs;reference/status notes;current TeX citations.
- **Observed output:** `code_B56/build_program_audit.out`.
- **Generated artifacts:** PROGRAM_AUDIT.md;PROGRAM_AUDIT.tsv;PROGRAM_AUDIT_FILES.tsv;REQUESTED_SOURCE_STATUS.md;REQUESTED_SOURCE_STATUS.tsv.
- **Observed scope/counts:** 32 programs cataloged;10 requested works;no inventoried program rerun.
- **Timing:** observed printed timing;before final report serialization — runtime_seconds=0.018680949s.
- **Qualification:** The current run's measured interval covers inventory/source analysis and ends immediately before final report serialization. No inventoried program is rerun.

### `code_B56/finalize_B56_records.py`

Update the B56 integration note,13 result rows and final scope/source/audit check events.

- **Inputs:** agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv;embedded exact audit descriptions.
- **Observed output:** `code_B56/finalize_B56_records.out`.
- **Generated artifacts:** agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv.
- **Observed scope/counts:** Two retained runs:13 result rows in both;check events54 then56;new event IDs retained in the output.
- **Timing:** observed printed timing — seconds=0.001580352s; seconds=0.001191058s.

### `code_B56/sync_B56_mirrors.py`

Normalize B56 section levels and mirror the directly maintained authoritative TeX into secondary TeX/Markdown.

- **Inputs:** B56.tex;Pandoc.
- **Observed output:** `code_B56/sync_B56_mirrors.out`.
- **Generated artifacts:** B56.tex;agent_B56.tex;agent_B56_proofs.md.
- **Observed scope/counts:** Two parallel B5/B6 sections;TeX mirror byte-identical;observed Markdown42518 bytes.
- **Timing:** observed printed timing — seconds=0.176059078s.

### `code_C/build_C_sections.py`

Convert the C-agent's complete source into the paper contribution and result rows while retaining separately audited TeX inputs.

- **Inputs:** agent_C.md;Pandoc;embedded statement/locator/dependency mappings.
- **Observed output:** `code_C/build_C_sections.out`.
- **Generated artifacts:** C_paper_source.md;C_sections.tex;RESULTS_C.csv.
- **Observed scope/counts:** Latest recovered stdout:27 statements;95724 TeX bytes;remaining non-ASCII character ö. Earlier generation:93716 bytes.
- **Timing:** not instrumented.
- **Tool wall time, not script runtime:** 0.476677675, 0.441562165s.
- **Qualification:** No script timing instrumentation. Recovered tool wall times are0.476677675s for the latest generation and0.441562165s for the earlier one; original outputs preserved without rerunning.

### `code_C/build_C_source_audit.py`

Record the exact inherited cote150 statement IDs actually checked, their supplied file/line locators and current proof dispositions;append corresponding check events.

- **Inputs:** ../sources/RESEARCH_SA10_study/study/readings/150_*_CHECK_EVENTS.tsv;150_*_CORRECTIONS.tsv;CHECK_EVENTS_C.tsv;embedded actual audit descriptions.
- **Observed output:** `code_C/build_C_source_audit.out`.
- **Generated artifacts:** C_inherited_audit.tsv;C_source_corrections.md;CHECK_EVENTS_C.tsv.
- **Observed scope/counts:** 56 inherited source-ID records;98 total C check-event rows.
- **Timing:** not instrumented.
- **Qualification:** Metadata-only program;does not modify TeX or perform a new mathematical computation. Script runtime not instrumented.

## Stable-graph case-by-case recorded measurements

These rows are parsed from the saved outputs, not recomputed.

| Program | (g,n) | Graphs | Pairs | Compatible | Failures | Recorded seconds |
|---|---|---:|---:|---:|---:|---:|
| code/stable_graph_meets.out | (0,3) | 1 | 0 | 0 | 0 | 1.847699604695663e-05 |
| code/stable_graph_meets.out | (0,4) | 4 | 6 | 3 | 0 | 0.00013880499318474904 |
| code/stable_graph_meets.out | (0,5) | 26 | 325 | 70 | 0 | 0.001682411995716393 |
| code/stable_graph_meets.out | (1,1) | 2 | 1 | 1 | 0 | 3.1104995287023485e-05 |
| code/stable_graph_meets.out | (1,2) | 5 | 10 | 8 | 0 | 0.0001572719993419014 |
| code/stable_graph_meets.out | (1,3) | 23 | 253 | 107 | 0 | 0.013842715001374017 |
| code/stable_graph_meets.out | (1,4) | 163 | 13203 | 2050 | 21 | 0.15386597600445384 |
| code/stable_graph_meets.out | (2,0) | 7 | 21 | 18 | 0 | 0.00021443599689519033 |
| code/stable_graph_meets.out | (2,1) | 16 | 120 | 90 | 2 | 0.000957172000198625 |
| code/stable_graph_meets.out | (3,0) | 42 | 861 | 603 | 25 | 0.044610784003452864 |
| code_B56/check_stable_graphs_independent.out | (1,1) | 2 | 1 | 1 | 0 | 4.4e-05 |
| code_B56/check_stable_graphs_independent.out | (1,2) | 5 | 10 | 8 | 0 | 0.000146 |
| code_B56/check_stable_graphs_independent.out | (1,3) | 23 | 253 | 107 | 0 | 0.00284 |
| code_B56/check_stable_graphs_independent.out | (2,0) | 7 | 21 | 18 | 0 | 0.000157 |
