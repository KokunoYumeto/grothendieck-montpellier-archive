#!/usr/bin/env python3
"""Read saved programs and outputs; write a complete program/source audit.

This script never executes any inventoried program. It is reusable after
the final build, report and packaging scripts have been saved. Known
programs have reviewed scope/input/output annotations; new ones are
listed from their docstrings and saved stdout, with missing evidence
explicitly flagged. Runtime observations come only from saved outputs.
"""
from pathlib import Path
import ast
import csv
import datetime
import hashlib
import json
import re
import time

started = time.perf_counter()
W = Path(__file__).resolve().parents[1]
previous_output=W/"code_B56/build_program_audit.out"
if previous_output.exists():
    try:
        prior_stamp=json.loads(previous_output.read_text())["utc"]
        prior_stamp=re.sub(r"[^0-9]","",prior_stamp.split("+")[0])
    except (ValueError,KeyError):
        prior_stamp=datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S")
    prior_path=previous_output.with_name("build_program_audit_"+prior_stamp+".out")
    if not prior_path.exists():prior_path.write_bytes(previous_output.read_bytes())
DIRECTORIES = ["code", "code_B", "code_B56", "code_C"]
META = {}
def known(path, category, scope, inputs, artifacts, counts="", logs=(), notes=""):
    META[path] = dict(category=category, scope=scope, inputs=inputs,
                      artifacts=artifacts, counts=counts, logs=list(logs), notes=notes)

known("code/check_A_finite.py", "mathematical certificate",
      "Finite A1 gluing and Cech-arity counterexamples; A4 finite-meet colimits; R3/R6 support identities.",
      "Embedded finite posets, sheaf maps, assignments and meet diagrams; no external input file.", "",
      "9 distinct all-pair objects;14 nonidentity inclusions;32 successor assignments,0 extensions;7-index examples12→1 and19→2 points;three Cech-arity witnesses;9 failed strict-bound comparisons.")
known("code/stable_graph_meets.py", "mathematical certificate",
      "Exhaustive stable-graph generation by inverse single-edge contractions; canonicalization and common-refinement tests.",
      "Embedded (g,n) cases (0,3),(0,4),(0,5),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(3,0); genera, labelled legs, loops and multiple edges.",
      "code/stable_graph_data/g0_n3.json;code/stable_graph_data/g0_n4.json;code/stable_graph_data/g0_n5.json;code/stable_graph_data/g1_n1.json;code/stable_graph_data/g1_n2.json;code/stable_graph_data/g1_n3.json;code/stable_graph_data/g1_n4.json;code/stable_graph_data/g2_n0.json;code/stable_graph_data/g2_n1.json;code/stable_graph_data/g3_n0.json",
      "10 cases;graph counts1,4,26,2,5,23,163,7,16,42;pair counts0,6,325,1,10,253,13203,21,120,861;meet failures only (1,4):21,(2,1):2,(3,0):25. Full graph/contraction/failure lists saved.")
known("code/build_paper.py", "typesetting/build",
      "LuaLaTeX/BibTeX build, task-local TeX support/cache setup, build-history preservation and overflow/citation checks.",
      "RESEARCH_SA10_paper.tex and recursive inputs;RESEARCH_SA10_references.bib;existing aux;task-local texmf;system TeX fonts/maps.",
      "RESEARCH_SA10_paper.pdf;RESEARCH_SA10_paper.log;RESEARCH_SA10_paper.aux;RESEARCH_SA10_paper.bbl;pdftex.map;logs/build_*.out;logs/build_summary.json;logs/build_history/**",
      logs=["logs/build_summary.json"], notes="Build outputs are snapshots and may change with the final build. Preserve all existing history logs; this catalog does not run a build or authorize PDF delivery.")
known("code/check_tex_runtime.lua", "environment diagnostic",
      "Inspect task-local TeX cache directory permissions and compare lfs writable-file result with an actual temporary-file write.",
      "Task-local tex_cache directory and LuaFileSystem module.", "Temporary runtime_test.tmp is removed by the program.",
      "Observed isdir=true, writable-file predicate=nil, actual write=true.", notes="No script timing instrumentation. This is environment diagnosis, not a mathematical check.")
known("code/fetch_primary_A.py", "source retrieval",
      "Download/identify cote151, SGA4 tome1 and Schmitt notes; record bytes, SHA256 and per-file duration.",
      "URLs embedded in script: Montpellier151.pdf;CMLS SGA4 tome1.pdf;Bonn Schmitt Script.pdf.",
      "../primary/151.pdf;../primary/SGA4_tome1.pdf;../primary/Schmitt_ModCurves.pdf",
      "3 completed files:27695508,1512797,6518673 bytes;each SHA256 saved.", logs=["logs/fetch_primary_A.out"],
      notes="Original stdout is logs/fetch_primary_A.out; the package preflight also preserves it as code/fetch_primary_A.out. Identical copied logs are not counted as separate runs. Fetched full primary PDFs are research inputs excluded from the deliverable.")
known("code/fetch_supplement_sources.py", "source retrieval",
      "Attempt a local download and text extraction of Goresky–MacPherson Stratified Morse Theory.",
      "https://www.math.ias.edu/~goresky/pdf/SMT.pdf", "Intended ../primary/Goresky_MacPherson_SMT.pdf/.txt;not produced by the failed observed run.",
      "One attempted request;HTTP403 before timing output.", notes="Failure log is preserved. The full text was separately opened online; download failure is not an unopened-source claim. Timing instrumentation exists but was not reached.")
known("code/fetch_tex_support.py", "environment setup",
      "Fetch three CTAN LuaLaTeX support archives and extract task-local runtime files; generate lualibs entry point when needed.",
      "CTAN luaotfload.zip;lualibs.zip;lua-uni-algos.zip;local LuaTeX executable.",
      "../texmf/tex/luatex/luaotfload/*;../texmf/tex/luatex/lualibs/*;../texmf/tex/luatex/lua-uni-algos/*",
      "3 archives:1993888,282788,95510 bytes;103,35,11 extracted runtime files (149 total).",
      notes="Third-party runtime packages are not mathematical code authored in this run; retain the fetch program and observed log.")
known("code/integrate.py", "metadata integration",
      "Aggregate result CSVs, check events and bibliography fragments; reject duplicate result IDs or bibliography keys; normalize recorded event labels when configured.",
      "RESULTS_A.csv;RESULTS_B.csv;results_B56.csv;RESULTS_C.csv;RESULTS_C1_B.csv;CHECK_EVENTS_*.tsv;references_A.bib;B_references.bib;references_B56.bib;C_references.bib;references_C5_Hurewicz.bib;references_supplement.bib.",
      "RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv;RESEARCH_SA10_references.bib;CHECK_EVENT_NORMALIZATION.tsv when produced.")
known("code/make_checkpoint.py", "packaging",
      "Create a new numbered full-work checkpoint with SHA256 manifest, excluding supplied/fetched sources and earlier ZIPs; refuse overwrite or ≥500MB.",
      "CLI checkpoint number;current work tree;PDF_QA_APPROVED marker;library_helpers/*.py.",
      "CHECKPOINT_<NN>_FILES.tsv;../RESEARCH_SA10_checkpoint_<NN>.zip",
      logs=["code/make_checkpoint_*.out"], notes="Checkpoint ZIPs remain separate; never place earlier checkpoint ZIPs inside the final ZIP.")
known("code/make_final_package.py", "final packaging/preflight",
      "Verify the approved PDF hash,74 unique result rows and preserved checkpoint paths;prepare delivery-only code mirrors and helper records. Optional --build writes the final ZIP,hash manifest and CRC check while refusing overwrite or size≥500MB.",
      "qa/final_qa.json;RESEARCH_SA10_paper.pdf;RESEARCH_SA10_report.md;RESEARCH_SA10_results.csv;CHECKPOINT_*_FILES.tsv;authored work tree;../library_helpers/*.py.",
      "code/programs/{code_B,code_B56,code_C}/**;code/fetch_primary_A.out;support/library_helpers/*.py;DELIVERY_EXCLUSIONS.tsv;with --build only:DELIVERY_MANIFEST.tsv and ../RESEARCH_SA10_final.zip.",
      notes="The observed output currently records a default/preflight run only. It is not evidence that --build ran or that a final ZIP/CRC check has already succeeded. Delivery mirrors are excluded from program-source discovery because they duplicate the originals.")
known("code/verify_archive.py", "archive integrity audit",
      "Verify an existing ZIP's CRC, every current manifest hash, duplicate-name byte identity and absence of nested ZIPs;final-delivery manifests additionally forbid duplicate names.",
      "CLI archive pathname and --output pathname;embedded CHECKPOINT_<NN>_FILES.tsv or DELIVERY_MANIFEST.tsv.",
      "JSON integrity report at the supplied --output pathname;observed stdout.",
      notes="The observed saved run verifies checkpoint02:305 entries,302 manifest hashes,no mismatch or nested ZIP;two duplicated helper filenames have identical bytes. It is not an observed verification of the not-yet-built final archive.")
known("code/update_working_report.py", "historical report generation",
      "Assemble the working report and update the dated progress ledger from explicit item/lead states and agent summaries.",
      "Embedded19 item/lead states;agent_B_levels.md;agent_B56.md;PROGRESS_LEDGER.md.",
      "RESEARCH_SA10_report.md;PROGRESS_LEDGER.md", notes="Historical working-report generator. Its recorded run is not evidence that the current final report still has that wording.")
known("code/finalize_root_records.py", "metadata audit",
      "Record the root's late source/proof checks and annotate exact A-result dependencies.",
      "Embedded actual check descriptions;RESULTS_A.csv.", "CHECK_EVENTS_ROOT_FINAL.tsv;RESULTS_A.csv")
known("code/render_pdf_qa.py", "PDF rendering/QA preparation",
      "Render every PDF page with Poppler, create indexed contact sheets and locate theorem/citation keywords;record the exact PDF hash.",
      "RESEARCH_SA10_paper.pdf;Poppler pdftoppm;PyMuPDF;Pillow.",
      "qa/pages/page-*.png;qa/contact/contact-*.png;qa/render_manifest.json",
      notes="Observed current render has74 pages at110dpi and7 contact sheets. Rendering and keyword location do not themselves constitute visual approval; the output explicitly records visual_approval=false pending separate image inspection.")
known("code/finalize_qa.py", "publication QA record",
      "Seal the PDF verification record after matching the final PDF hash, successful build metrics and three independent visual-inspection records.",
      "RESEARCH_SA10_paper.pdf;qa/render_manifest.json;logs/build_summary.json;PDF_VISUAL_ROOT.md;PDF_VISUAL_B.md;PDF_VISUAL_C.md;logs/build_history/20261119T052014525518Z/build_pass2.out.",
      "qa/final_qa.json;PDF_QA_REPORT.md;logs/PDF_QA_APPROVED.txt",
      notes="Checks recorded image inspections rather than treating a successful render as visual approval. Before/after overflow counts and the exact PDF hash are retained in its artifacts.")
known("code/finalize_report.py", "final report assembly",
      "Assemble the outcome-first final report from the root conclusions, source/program catalogs, detailed proof/correction records and publication/register audits.",
      "REPORT_ROOT.md;REQUESTED_SOURCE_STATUS.md;PROGRAM_AUDIT.md;agent_B_levels.md;agent_B56.md;C_source_corrections.md;C5_Hurewicz_review.md;C5_audit_B.md;PDF_QA_REPORT.md;FINAL_register_audit_B56.md;RESEARCH_SA10_results.csv;CHECK_EVENTS.tsv.",
      "RESEARCH_SA10_report.md",
      notes="Observed character/section/result/event counts refer to the saved run. A later assembly may include a refreshed version of this catalog.")
known("code_B/check_B_finite.py", "mathematical certificate",
      "Integral normalized C2 bar differential and tetrahedral sphere cocycle/coherence witnesses.",
      "Embedded C2 and tetrahedral boundary;SymPy exact integer linear algebra.", "",
      "8 associativity triples and2 inverses;bar differentials through degree4;H1(BC2;Z)=Z/2;tetrahedron4 vertices6 edges4 faces;rank(d2)=3;integral cocycle pairing−1.")
known("code_B/download_sources.py", "source retrieval",
      "Fetch Treumann source/PDF, Quinn PDF and Higher Algebra; preserve failures; decompress Treumann TeX.",
      "Four URLs embedded in script;existing literature_B files.",
      "literature_B/treumann_source;literature_B/treumann.pdf;literature_B/treumann.tex;literature_B/quinn.pdf;intended literature_B/HA.pdf.",
      "Treumann source34221 bytes and PDF451815 bytes already present;Quinn1370605 bytes downloaded;HA local request403;Treumann TeX decompressed.",
      notes="Higher Algebra was independently opened online. Fetched complete copyrighted source files are excluded from the package.")
known("code_B/write_B_records.py", "metadata generation",
      "Write B1–B4 result rows and their recorded check events.",
      "Embedded statement/check descriptions.", "RESULTS_B.csv;CHECK_EVENTS_B.tsv",
      "Observed output15 statement rows,29 check-event rows;later independent additions may increase the current event file.")
known("code_B56/check_B56.py", "mathematical certificate",
      "Finite-set presentations, global relation countermodel, forest/orbit conditions, symmetric group nerve and hypercover nonimplications.",
      "Embedded finite sets/functions,C2 actions and exact rational simplex functions;no external data.", "",
      "14 corrected low-degree relations;56 finite maps;412 global countermodel instances;4 C2 cospans/8 squares;mod2 H1 dimension1;16 symmetric products;1528 cospans/6871 target pairs;126 monotone maps;30 rational amalgams.")
known("code_B56/check_matching_independence.py", "mathematical certificate",
      "GF2 cocycle matching-map ranks for the independently indispensable hypercover degrees.",
      "Embedded cocycle models K(F2,n),n1–4,simplex degree k0–7.", "",
      "32 comparisons;for each n exactly degree k=n+1 fails, image codimension1. Full row data in stdout.")
known("code_B56/check_stable_graphs_independent.py", "mathematical certificate",
      "Independent direct bounded-multigraph enumeration of the positive stable-graph cases, distinct from the root inverse-contraction algorithm.",
      "Embedded (g,n)=(1,1),(1,2),(1,3),(2,0);all bounded genera/legs/edge multiplicities.", "",
      "Candidate counts2,22,717,18;graph counts2,5,23,7;pair counts1,10,253,21;compatible pairs1,8,107,18;zero failures.")
known("code_B56/check_C5_boundary_group.py", "mathematical certificate",
      "Check a nontrivial finite quotient of the opened Mazur-boundary group presentation.",
      "Embedded presentation <x,y|y^5=x^7,y^4=x^2 y x^2>;fixed7-cycle;all5-cycles on7 points.", "",
      "504 five-cycles checked;14 solutions;chosen x,y generate A7 of order2520;both defining relations explicitly evaluated.",
      notes="Certifies the recorded group's nontriviality; does not replace the geometric verification of a handle presentation.")
known("code_B56/check_B6_translation.py", "mathematical certificate",
      "Check every coface/codegeneracy cycle-word substitution into the manuscript's delta,K,permutation generators.",
      "Embedded finite-set maps for every n1–12 and every allowed index i.", "",
      "90 coface words+78 codegeneracy words=168 checks;zero failures;last generators recovered literally.")
known("code_B56/sync_B56_mirrors.py", "typesetting/source mirroring",
      "Normalize B56 section levels and mirror the directly maintained authoritative TeX into secondary TeX/Markdown.",
      "B56.tex;Pandoc.", "B56.tex;agent_B56.tex;agent_B56_proofs.md",
      "Two parallel B5/B6 sections;TeX mirror byte-identical;observed Markdown42518 bytes.")
known("code_B56/finalize_B56_records.py", "metadata generation",
      "Update the B56 integration note,13 result rows and final scope/source/audit check events.",
      "agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv;embedded exact audit descriptions.",
      "agent_B56.md;results_B56.csv;CHECK_EVENTS_B56.tsv",
      "Two retained runs:13 result rows in both;check events54 then56;new event IDs retained in the output.")
known("code_B56/audit_final_register.py", "read-only integration audit",
      "Recursively inspect actual manuscript inputs;match numbered statement headings to the requested five CSVs and exact-ID check events;verify citation keys/access labels.",
      "RESEARCH_SA10_paper.tex and recursive TeX inputs;five result CSVs;source/aggregate CHECK_EVENTS;RESEARCH_SA10_references.bib.",
      "FINAL_register_audit_B56.md;FINAL_register_audit_B56.json",
      notes="Does not execute mathematical tests or reopen every source. Records SHA256 snapshots; counts in stdout identify the audited version.")
known("code_C/check_cote150.py", "mathematical certificate",
      "Projection-control twist counterexample;Boolean flag intervals;exact genus4 branch-set automorphisms;quotient local homology.",
      "Embedded6-point twist;all naturally labelled posets through5 elements;ten rational/infinite branch points;SymPy and Fraction exact arithmetic.", "",
      "6 twist vertices/6 strict arrows/2 transitivity failures;poset counts1,1,2,7,40,357;4135 flags/10603 intervals;720 Mobius candidates,only identity;genus4 tangent invariant/anti-invariant dimensions7/2;local torsion Z/2 in degree16.")
known("code_C/check_cone_transitions.py", "mathematical certificate",
      "Cellular quotient certificate for the missing selected-prefix transitions and the corrected simultaneous-cone construction.",
      "Embedded constant one-point chain diagrams with0–6 vertices;union-find of cells under transition families.", "",
      "Two-vertex old diagram:2 components,3 vertices,1 edge;corrected:1 component,2 vertices,1 edge. All7 chain sizes0–6 checked;at6 vertices364 blocks,2366 raw cells,2276 transitions,quotient cell counts6,15,20,15,6,1.")
known("code_C/build_C_sections.py", "typesetting/metadata generation",
      "Convert the C-agent's complete source into the paper contribution and result rows while retaining separately audited TeX inputs.",
      "agent_C.md;Pandoc;embedded statement/locator/dependency mappings.",
      "C_paper_source.md;C_sections.tex;RESULTS_C.csv",
      "Latest recovered stdout:27 statements;95724 TeX bytes;remaining non-ASCII character ö. Earlier generation:93716 bytes.",
      notes="No script timing instrumentation. Recovered tool wall times are0.476677675s for the latest generation and0.441562165s for the earlier one; original outputs preserved without rerunning.")
known("code_C/build_C_source_audit.py", "inherited-source metadata audit",
      "Record the exact inherited cote150 statement IDs actually checked, their supplied file/line locators and current proof dispositions;append corresponding check events.",
      "../sources/RESEARCH_SA10_study/study/readings/150_*_CHECK_EVENTS.tsv;150_*_CORRECTIONS.tsv;CHECK_EVENTS_C.tsv;embedded actual audit descriptions.",
      "C_inherited_audit.tsv;C_source_corrections.md;CHECK_EVENTS_C.tsv",
      "56 inherited source-ID records;98 total C check-event rows.",
      notes="Metadata-only program;does not modify TeX or perform a new mathematical computation. Script runtime not instrumented.")
known("code_B56/build_program_audit.py", "read-only program/source catalog",
      "Inventory all saved programs in four code directories;read their observed outputs;catalog requested-source opening evidence without executing inventoried programs.",
      "code/**;code_B/**;code_B56/**;code_C/**;logs;reference/status notes;current TeX citations.",
      "PROGRAM_AUDIT.md;PROGRAM_AUDIT.tsv;PROGRAM_AUDIT_FILES.tsv;REQUESTED_SOURCE_STATUS.md;REQUESTED_SOURCE_STATUS.tsv",
      notes="The current run's measured interval covers inventory/source analysis and ends immediately before final report serialization. No inventoried program is rerun.")

def files_for(pattern):
    return sorted(p for p in W.glob(pattern) if p.is_file())
def relative(path):
    return str(path.relative_to(W))
def docstring(path):
    text=path.read_text(errors="replace")
    if path.suffix==".py":
        try:
            return ast.get_docstring(ast.parse(text)) or "No module docstring; see saved program."
        except SyntaxError:
            pass
    return " ".join(text.splitlines()[:3])
def count_excerpt(text):
    lines=[]
    for line in text.splitlines():
        if re.search(r"(?i)(assembled|recorded|updated|statement|check.event|count|passed|failure|overfull|undefined|missing|runtime|elapsed|sha256|bytes)",line):
            if len(line)>1200: line=line[:1200]+" [line continues in output]"
            lines.append(line.strip())
    return " | ".join(lines[:16]) or text.strip()[:1800]
def runtime_evidence(text):
    # The printed numeric values are retained as strings, without inference
    # from file mtimes, durations of earlier calls, or current execution.
    pat=r'(?i)(?<![A-Za-z_])(?:"?((?:total_)?(?:runtime_seconds|elapsed_seconds|elapsed|runtime|seconds))"?)\s*[:=]?\s*([0-9]+(?:\.[0-9]*)?(?:[eE][+-]?\d+)?)'
    return [{"label":m.group(1),"seconds":m.group(2)} for m in re.finditer(pat,text)]

def is_delivery_mirror(path):
    parts=path.relative_to(W).parts
    return len(parts)>=2 and parts[:2]==("code","programs")
programs=sorted(p for directory in DIRECTORIES for p in (W/directory).rglob("*")
                if p.is_file() and p.suffix in {".py",".lua",".sh",".js",".mjs",".ipynb"}
                and "__pycache__" not in p.parts and not is_delivery_mirror(p))
records=[]
new_programs=[]
observed_paths=set()
for path in programs:
    name=relative(path)
    meta=META.get(name)
    if meta is None:
        new_programs.append(name)
        meta=dict(category="additional saved program",scope=docstring(path),
                  inputs="See saved program; not inferred from a successful run.",
                  artifacts="See program and observed output.",counts="",logs=[],
                  notes="Auto-discovered after the reviewed catalog annotations; exact observed stdout is linked. No runtime or count is guessed.")
    logs=set()
    for suffix in [".out",".output.json",".log",".stdout.txt"]:
        candidate=path.with_suffix(suffix)
        if candidate.exists():logs.add(candidate)
    logs.update(p for p in path.parent.glob(path.stem+"_*.out") if p.is_file())
    for pattern in meta["logs"]:
        logs.update(files_for(pattern))
    unique_logs=[];seen_log_hashes=set()
    for p in sorted(logs):
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest not in seen_log_hashes:
            seen_log_hashes.add(digest);unique_logs.append((p,p.read_text(errors="replace")))
    text="\n".join(s for p,s in unique_logs)
    times=[dict(output=relative(p),**observation) for p,s in unique_logs for observation in runtime_evidence(s)]
    tool_times=re.findall(r"(?i)tool[ _-]*wall(?:[ _-]*time|[ _-]*seconds)?[^\n0-9]*([0-9]+(?:\.[0-9]+)?)",text)
    instrumented=bool(re.search(r"perf_counter|time\.time\(|process_time|os\.clock",path.read_text(errors="replace")))
    if times:
        time_status="observed printed timing"
    elif instrumented:
        time_status="instrumented, but no elapsed time in the observed output"
    else:
        time_status="not instrumented"
    counts=meta["counts"] or count_excerpt(text)
    row=dict(program=name,category=meta["category"],scope=meta["scope"],
             input_filenames=meta["inputs"],output_filenames=meta["artifacts"],
             observed_output_filenames=";".join(relative(p) for p in sorted(logs)),
             observed_counts=counts,runtime_status=time_status,
             observed_runtime_seconds=json.dumps(times,ensure_ascii=False),
             observed_tool_wall_seconds=json.dumps(tool_times),
             output_status="observed output saved" if logs else "NO SAVED OBSERVED OUTPUT FOUND",
             program_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),notes=meta["notes"])
    records.append(row)
    observed_paths.update(logs)

# Source matrix: exactly the ten mathematical works named in the user prompt.
# These entries summarize already recorded openings; no new opening is claimed.
SOURCES=[
 dict(source="Ayala–Francis–Tanaka, Local structures on stratified spaces",keys="AFT;AFTLocal;C_AFT",
      url="https://arxiv.org/abs/1409.0501",version="arXiv v6;Adv.Math.307(2017)903–1028",
      locator="Cor.1.2.10;Lemmas6.1.4,6.1.7;Th6.1.9;Cor.7.3.7;Th7.3.8;Props7.3.10,8.2.3,8.2.5",
      evidence="references_A.bib;B_references.bib;C_source_manifest.tsv;notes/root_source_searches.md",
      tex="Opened: literature_C/AFT/AFT1-2016.tex;source archive fetched by C agent",
      use="Unzipping, conically smooth local models, cone/collar and exit comparisons",
      limitation="Root web source-fetch attempt failed; C-agent TeX retrieval succeeded. Earlier85-page author version also opened; cited numbering uses v6. Root additionally opened AFT1-2016.tex lines5533–5565 for Proposition8.2.5 on regular neighborhoods of closed constructible embeddings;both8.2.3 and8.2.5 checked."),
 dict(source="Treumann, Exit paths and constructible stacks",keys="Treumann2009",
      url="https://arxiv.org/pdf/0708.0659",version="arXiv v1;Compos.Math.145(2009)1504–1532",
      locator="Definition3.1;Theorems7.13,7.14",
      evidence="B_references.bib;code_B/download_sources.out;literature_B/treumann.tex",
      tex="Opened and saved as literature_B/treumann.tex",use="Constructible groupoid stacks and exit-path2-functors",
      limitation="ArXiv identifier and DOI verified on the primary abstract page; no failed download used as an opening."),
 dict(source="Lurie, Higher Algebra, Appendix A",keys="LurieHA",
      url="https://www.math.ias.edu/~lurie/papers/HA.pdf",version="18September2017",
      locator="TheoremsA.4.19,A.7.1,A.9.3;Cor.A.9.4;RemarkA.9.7;Prop.A.9.16;A.8.4,A.8.11,A.8.14;finite induction pp1463–1465",
      evidence="B_references.bib;code_B/download_sources.out;CHECK_EVENTS_B.tsv",
      tex="No LaTeX source opening recorded",use="Constructible sheaves, exit categories, truncation and recollement induction",
      limitation="Full PDF actually opened online. Local direct download returned403; local-file failure does not negate the online opening."),
 dict(source="Barwick–Glasman–Haine, Exodromy",keys="BGHExodromy",
      url="https://arxiv.org/abs/1807.03281",version="arXiv v7,23August2020;opened PDF datedAugust2020",
      locator="Definition2.1.8;Lemma2.7.3;Theorem2.7.4;Definition4.2.1;Example4.2.3",
      evidence="B_references.bib;CHECK_EVENTS_B.tsv",
      tex="No LaTeX source opening recorded",use="Shapes, stratified homotopy and exodromy framework",
      limitation="Full primary paper opened through https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/barwick-glasman-haine.pdf;version verified on arXiv."),
 dict(source="Haine, On the homotopy theory of stratified spaces",keys="B56Haine2023",
      url="https://arxiv.org/pdf/1811.01119",version="v6;paper dated27March2023",
      locator="Definition1.1.1p7;Definition1.1.4 and Theorem1.1.7p8;Theorem3.2.4p27;Comparison3.4.2p30",
      evidence="references_B56.bib;B5_scope_audit.md;CHECK_EVENTS_B56.tsv;C1_collage_B.tex",
      tex="No LaTeX source opening recorded;full PDF downloaded/text extracted",
      use="Theorem1.1.7 identifies flag decollages with conservative infinity-categories after C1.B2",
      limitation="Not a premise of B5;does not replace the separate geometric Exit comparison. Independently opened by B1–B4 agent."),
 dict(source="Woolf, The fundamental category of a stratified space",keys="Woolf2009",
      url="https://arxiv.org/pdf/0811.2580",version="arXiv v3,including2013 correction;J.Homotopy Relat.Struct.4(2009)359–387",
      locator="Lemma3.5;Theorem4.3,p15 ofv3",
      evidence="B_references.bib;CHECK_EVENTS_B.tsv",
      tex="No LaTeX source opening recorded",use="Opened comparison/background for endpoint fibrations and constructible sheaf classification",
      limitation="Introduction's obsolete Theorem4.6 reference is not used;body numbering is4.3. Paper citation status is reported separately below."),
 dict(source="Quinn, Homotopically stratified sets",keys="Quinn1988",
      url="https://webhomes.maths.ed.ac.uk/~v1ranick/papers/quinn5.pdf",version="JAMS1(1988)441–499",
      locator="Definition2.1pp451–452;Lemma2.4 and corollarypp454–455;Definition3.1 and Proposition3.2p469",
      evidence="B_references.bib;code_B/download_sources.out;literature_B/quinn.txt",
      tex="No LaTeX source opening recorded;full scanned PDF downloaded/text extracted",
      use="Tame holinks, mapping-cylinder comparison, stratified-fibration and normal-germ results",
      limitation="Quinn's cylinder topology is distinguished from ordinary quotient topology;additional fibration hypotheses are stated."),
 dict(source="Mather, Notes on topological stability",keys="C_Mather",
      url="https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf",version="July1970 notes;the requested2012 publication is not substituted silently",
      locator="Section7,p15,control equations",
      evidence="C_references.bib;C_source_manifest.tsv;literature_C/Mather.pdf/.txt",
      tex="No LaTeX source opening recorded;primary notes PDF opened",
      use="Projection/radius control and comparison with Thom–Mather data",
      limitation="Opening claim is for the1970 notes at the cited locator, not a separately opened2012 typesetting."),
 dict(source="Goresky–MacPherson, Stratified Morse Theory",keys="GoreskyMacPherson1988",
      url="https://www.math.ias.edu/~goresky/pdf/SMT.pdf",version="Springer1988",
      locator="PartI Section1.4pp40–41;Section1.5pp41–42;Section1.6pp42–43",
      evidence="references_supplement.bib;notes/supplement_source_audit.md;code/fetch_supplement_sources.out",
      tex="No LaTeX source opening recorded;full author-hosted PDF opened online",
      use="Normal slices/links,conical local triviality,first isotopy lemma and stratified maps",
      limitation="Local download403;full text was actually read through web retrieval. Source warns normal-slice maps need not be topologically constant along a stratum."),
 dict(source="SGA4, Expose IV section9",keys="SGA4",
      url="https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/tomes/tome1.pdf",version="Tome1,LNM269(1972);opened revised2015 primary PDF",
      locator="ExposeIV Sections9.3–9.6,especially9.5.1–9.5.7 and Theorem9.5.4;PDFpp240–246",
      evidence="references_A.bib;logs/fetch_primary_A.out;notes/root_source_searches.md",
      tex="No LaTeX source opening recorded;full primary PDF fetched",
      use="Closed–open recollement and the gluing comparison",
      limitation="Search result/English transcription was a locator only;the primary text was opened and used.")
]

seen=set();cited=set()
def cites_in(path):
    if path in seen or not path.exists():return
    seen.add(path);s=path.read_text()
    for m in re.finditer(r"\\(?:[A-Za-z]*cite[A-Za-z]*|nocite)\*?(?:\[[^\]]*\])*\{([^}]+)\}",s):
        cited.update(k.strip() for k in m.group(1).split(","))
    for m in re.finditer(r"\\(?:input|include)\{([^}]+)\}",s):
        p=path.parent/m.group(1)
        cites_in(p if p.suffix else p.with_suffix(".tex"))
cites_in(W/"RESEARCH_SA10_paper.tex")
for row in SOURCES:
    row["opened_status"]="OPENED full primary text, as recorded in this run"
    row["cited_in_current_paper"]="yes" if any(k in cited for k in row["keys"].split(";")) else "no;opened contextual source with exact locator in this matrix/bibliography"

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
own=next(row for row in records if row["program"]=="code_B56/build_program_audit.py")
own_out=W/"code_B56/build_program_audit.out"
own["observed_output_filenames"]=relative(own_out)
own["output_status"]="observed output saved"
elapsed=round(time.perf_counter()-started,9)
own["runtime_status"]="observed printed timing;before final report serialization"
own["observed_runtime_seconds"]=json.dumps([dict(label="runtime_seconds",seconds=str(elapsed))])
own["observed_counts"]=f"{len(records)} programs cataloged;{len(SOURCES)} requested works;no inventoried program rerun."
summary=dict(utc=now,program_count=len(records),mathematical_program_count=sum(r["category"]=="mathematical certificate" for r in records),
             requested_source_count=len(SOURCES),auto_discovered_new_programs=new_programs,
             missing_saved_output=[r["program"] for r in records if r["output_status"].startswith("NO")],
             no_script_elapsed_output=[r["program"] for r in records if r["runtime_status"] in {"not instrumented","instrumented, but no elapsed time in the observed output"}],
             runtime_seconds=elapsed,timing_scope="inventory/source analysis,before final report serialization")
own_out.write_text(json.dumps(summary,indent=2)+"\n")
observed_paths.add(own_out)

def write_tsv(path,rows):
    with path.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter="\t")
        writer.writeheader();writer.writerows(rows)
write_tsv(W/"PROGRAM_AUDIT.tsv",records)
write_tsv(W/"REQUESTED_SOURCE_STATUS.tsv",SOURCES)

inventory=set(p for d in DIRECTORIES for p in (W/d).rglob("*") if p.is_file() and "__pycache__" not in p.parts and not is_delivery_mirror(p))
inventory.update(observed_paths)
# These auxiliary observed build/source logs must accompany the code audit.
inventory.update(p for p in (W/"logs").rglob("*") if p.is_file())
file_rows=[dict(path=relative(p),kind="program" if p in programs else "observed output/data/log",
                bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(inventory)]
write_tsv(W/"PROGRAM_AUDIT_FILES.tsv",file_rows)

def escape(text):return str(text).replace("|",r"\|").replace("\n"," ")
md=["# Complete saved-program audit", "",
    "AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.", "",
    f"Snapshot: **{now}**. **{len(records)} programs**, including this catalog generator; **10 mathematical certificate programs**. No inventoried program was rerun to produce this catalog.", "",
    "Every count and duration below comes from an existing observed output, except the catalog generator's own current-run measurement. Historical outputs are not silently promoted to measurements of later edited files. A script runtime, a tool wall time, and an uninstrumented run are explicitly distinguished.", "",
    "Machine-readable records: `PROGRAM_AUDIT.tsv`. Exact file inventory and SHA256s: `PROGRAM_AUDIT_FILES.tsv`. Requested-source matrix: `REQUESTED_SOURCE_STATUS.md` and `.tsv`. Paths are relative to the working deliverable directory; `../primary` and `../texmf` are external research/runtime inputs.", "",
    "## Coverage and missing evidence", "",
    "- Missing saved output: "+("; ".join(summary["missing_saved_output"]) or "none")+".",
    "- No printed script elapsed time: "+("; ".join(summary["no_script_elapsed_output"]) or "none")+".",
    "- Newly auto-discovered programs: "+("; ".join(new_programs) or "none")+".",
    "- `fetch_supplement_sources.py` failed with HTTP403 before its elapsed-time print; the saved traceback is an observed output, not a successful download.",
    "- `check_tex_runtime.lua` is uninstrumented. `build_C_sections.py` is uninstrumented; its separately recovered tool wall time is labelled as such in the saved output.",
    "- Preserve all four original code directories, the `stable_graph_data` JSONs, and the source/build logs. Final packaging additionally mirrors agent code under `code/programs/` and copies the source-fetch log into `code/`; these aliases are excluded from source discovery and inventory counts to avoid double counting. Each program's primary observed stdout/JSON is retained under the final code subtree; supplementary build logs and generated documents keep their recorded locations. Full fetched copyrighted sources and third-party TeX runtime packages remain excluded. This catalog does not relocate execution paths or assert that embedded working paths are portable.", ""]
for category,title in [(True,"Mathematical certificates"),(False,"Retrieval, typesetting, metadata, packaging and audit programs")]:
    md += ["## "+title,""]
    for row in records:
        if (row["category"]=="mathematical certificate")!=category:continue
        md += ["### `"+row["program"]+"`","",
               row["scope"],"",
               "- **Inputs:** "+row["input_filenames"],
               "- **Observed output:** `"+(row["observed_output_filenames"] or "MISSING")+"`.",
               "- **Generated artifacts:** "+(row["output_filenames"] or "stdout only; no separate artifact")+".",
               "- **Observed scope/counts:** "+(row["observed_counts"] or "No count emitted in the available output.")]
        times=json.loads(row["observed_runtime_seconds"])
        timing="; ".join(t["label"]+"="+t["seconds"]+"s" for t in times)
        md += ["- **Timing:** "+row["runtime_status"]+(" — "+timing if timing else "")+"."]
        if json.loads(row["observed_tool_wall_seconds"]):
            md += ["- **Tool wall time, not script runtime:** "+", ".join(json.loads(row["observed_tool_wall_seconds"]))+"s."]
        if row["notes"]:md += ["- **Qualification:** "+row["notes"]]
        md.append("")

md += ["## Stable-graph case-by-case recorded measurements", "",
       "These rows are parsed from the saved outputs, not recomputed.", "",
       "| Program | (g,n) | Graphs | Pairs | Compatible | Failures | Recorded seconds |",
       "|---|---|---:|---:|---:|---:|---:|"]
for name in ["code/stable_graph_meets.out","code_B56/check_stable_graphs_independent.out"]:
    for line in (W/name).read_text().splitlines():
        item=json.loads(line)
        md.append("| "+name+" | ("+str(item["g"])+","+str(item["n"])+") | "+str(item.get("graph_count",item.get("graphs")))+" | "+str(item.get("pairs_tested",item.get("pairs")))+" | "+str(item.get("pairs_with_common_refinement",item.get("compatible_pairs")))+" | "+str(item.get("failure_count",item.get("failures")))+" | "+str(item.get("elapsed_seconds",item.get("runtime_seconds")))+" |")
(W/"PROGRAM_AUDIT.md").write_text("\n".join(md)+"\n")

sm=["# Requested-literature opening-status matrix", "",
    "AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/hypercovers_finite_sets. No priority claimed.", "",
    f"Snapshot: {now}. This matrix covers all ten mathematical works named in the user's Sources list. It consolidates actual openings recorded in the bibliography, source-status files and logs. It does not treat a search result, a failed download or an abstract as a full-text opening, and it does not claim that the catalog generator reopened these sources.", "",
    "All ten requested works have a recorded full primary-text opening. Local download failures for Higher Algebra and Stratified Morse Theory coexist with successful online full-text openings. LaTeX-source availability is stated separately and is not inferred from the existence of a PDF.", "",
    "| Requested work | Status/version | Exact locators | Use and current paper citation |",
    "|---|---|---|---|"]
for row in SOURCES:
    sm.append("| "+escape(row["source"])+" | OPENED;"+escape(row["version"])+" | "+escape(row["locator"])+" | "+escape(row["use"])+";citation:"+escape(row["cited_in_current_paper"])+" |")
sm += ["", "## Individual evidence and retrieval qualifications", ""]
for row in SOURCES:
    sm += ["### "+row["source"],"", "Primary URL: <"+row["url"]+">. Bibliography keys: `"+row["keys"]+"`.","",
           "- Opening evidence: `"+row["evidence"]+"`.",
           "- LaTeX-source status: "+row["tex"]+".",
           "- Qualification: "+row["limitation"],""]
sm += ["## Additional source-status caveat", "",
       "Mazur's original1961 Annals paper, DOI10.2307/1970288, is **not opened in full**. It is not one of the ten requested works. The C5 proof uses the actually opened Zeeman1964p347 construction/nontrivial-boundary statement, Milnor's h-cobordism theorem, Ferry's strong-regularity theorem, and Rolfsen's explicitly limited auxiliary group presentation. See `C5_Hurewicz_review.md` and `references_C5_Hurewicz.bib`. A reproduced abstract and inaccessible JSTOR PDF are not called a primary full-text opening.", "",
       "Original cote147,150,151 scan readings and their remaining ink ambiguities are recorded separately in `C_source_manifest.tsv`, `notes/root_source_searches.md`, and `ink_B56/INK_REVIEW.md`; the present matrix does not upgrade transcription readings to independent ink readings."]
(W/"REQUESTED_SOURCE_STATUS.md").write_text("\n".join(sm)+"\n")
print(json.dumps(summary,indent=2))
