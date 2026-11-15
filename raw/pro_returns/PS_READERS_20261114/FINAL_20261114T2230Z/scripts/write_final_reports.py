"""Write reader documentation from audited artifacts, without inventing QA."""
from pathlib import Path
import collections,csv,hashlib,json,re
P=Path(__file__).resolve().parents[1];R=P/'records'
STEMS=['PS_EN_diplomatic','PS_EN_corrected_apparatus','PS_EN_reading','PS_EN_master_annotated','PS_GUIDE']
def read(name):return list(csv.DictReader((R/name).open(),delimiter='\t'))
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x).replace('|',' / ').replace('\n',' ') for x in row)+' |' for row in rows])+'\n'
def load(name):return json.loads((R/name).read_text())
coverage=load('COVERAGE_AUDIT.json');review=read('REVIEW_COVERAGE.tsv');changes=read('CHANGES_EN.tsv');decisions=read('CHECK_DECISIONS.tsv');structure=load('FINAL_STRUCTURE_AUDIT.json');gate=load('FINAL_QA_GATE.json');guide=load('GUIDE_MANIFEST.json');checkpoint=load('CHECKPOINT_INVENTORY.json')
replay=load('CHANGE_REPLAY_AUDIT.json')
if gate.get('schema_version')!=2 or not gate.get('complete'):
    raise ValueError('Final reports require the complete provenance-aware final QA gate.')
for relative,expected in gate.get('validated_input_sha256',{}).items():
    path=(P/relative).resolve()
    if not path.is_relative_to(P) or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError('QA input changed after the final gate: '+relative)
for stem in STEMS:
    expected=gate['pdfs'][stem]['pdf_sha256']
    if hashlib.sha256((P/'readers'/(stem+'.pdf')).read_bytes()).hexdigest()!=expected:
        raise ValueError('PDF changed after the final gate: '+stem)
builds={stem:json.loads((P/structure['forms'][stem]['latest_build_record']).read_text()) for stem in STEMS}
visual={stem:gate['pdfs'][stem]['validated_visual_evidence'] for stem in STEMS}
labels={'PS_EN_diplomatic':'Diplomatic','PS_EN_corrected_apparatus':'Corrected with apparatus','PS_EN_reading':'Reading text','PS_EN_master_annotated':'Annotated master','PS_GUIDE':'Guide'}
group_order=['134-2','134-3','134-4','134-5','134-6','134-7','134-8','Brown (134-2)']
def grp(r):return 'Brown (134-2)' if r['key'].startswith('brown_') else r['cote']
counts=[]
for g in group_order:
    rows=[r for r in review if grp(r)==g]
    counts.append([g,len(rows),sum(int(r['unsure_before']) for r in rows),sum(int(r['illegible_before']) for r in rows),sum(int(r['unsure_after']) for r in rows),sum(int(r['illegible_after']) for r in rows)])
summary_rows=[]
for stem in STEMS:
    b=builds[stem];p=structure['pdfs'][stem];q=gate['pdfs'].get(stem,{})
    summary_rows.append([labels[stem],p['pages'],b['exit'],b['overfull_count'],b['widest_pt'],b['missing_character_lines'],p['archive_annotations'],p['distinct_source_pages']])
summary=table(['PDF','PDF pages','Engine exit','Overfull boxes','Widest, pt','Missing glyphs','Archive annotations','Distinct source pages'],summary_rows)
warning_rows=[]
for stem in STEMS:
    log=(P/builds[stem]['log']).read_text()
    warnings=re.findall(r'(?:LaTeX|Package [^\n]+) Warning:[^\n]*(?:\n\([^\n]*\)[^\n]*)*',log)
    warning_rows.append([labels[stem],len(re.findall(r'(?m)^! ',log)),len(warnings),len(re.findall(r'Underfull',log))])
summary+='\n'+table(['PDF','LaTeX errors','LaTeX/package warnings','Underfull boxes'],warning_rows)
summary+='\nWarning-family counts and their harmless interpretations are given in `TYPESETTING_REPORT.md`; the totals above are stated directly for each delivered PDF.\n'
visual_counts=[]
for stem in STEMS:
    q=gate['pdfs'][stem]
    visual_counts.append([labels[stem],len(q['selected_pages']),len(q['direct_current_pdf_viewed_pages']),len(q['inherited_exact_raster_review_pages']),len(q.get('master_body_equivalence',{}).get('reviewed_apparatus_pages_reused',[]))])
summary+='\n'+table(['PDF','Selected pages','Current-PDF images opened directly','Prior observations inherited by exact raster equality','Reviewed apparatus body pages reused in master'],visual_counts)
summary+='\nCounts are distinct pages within each evidence class. Extra targeted openings can exceed the selected sample. An inherited observation is not counted as an opening of the current image. Master body comparison and inherited apparatus coverage are reported separately.\n'
master_reuse=gate['pdfs']['PS_EN_master_annotated']['master_body_equivalence']
master_reuse_description=(f"Every master body page, physical pages 2–{structure['pdfs']['PS_EN_master_annotated']['pages']}, was compared with the corresponding corrected-apparatus page at 144 dpi. All {len(master_reuse['body_pages_byte_identical']):,} pairs had identical geometry, decoded RGB bytes and lossless PNG bytes. This supports reuse of the {len(master_reuse['reviewed_apparatus_pages_reused'])} corresponding apparatus pages with validated visual review; it does not claim that every master body page was opened. The distinct master title/front page was opened directly from the final PDF. The complete proof is `{master_reuse['audit']}`.")
readme=f'''# Pursuing Stacks — complete checked English readers

Alexander Grothendieck, *Pursuing Stacks* (1983), with R. Brown's appendix translation. The primary witness is the supplied Université de Montpellier archive typescript, cotes 134-2–134-8. All 706 source pages (680 main-work pages and 26 Brown pages) have recorded inspection of both supplied image halves.

## Deliverables

`PS_READERS_EN.zip` contains five standalone LuaLaTeX sources and their PDFs: the diplomatic reader, corrected reader with apparatus, reading text, annotated master, and guide. `PS_READERS_RECORDS.zip` contains all 706 `checked_pages/` files, decision and concordance tables, variant and typesetting records, build and verification scripts, logs, review notes, proof images and final visual-QA evidence. Paths in the records are relative to that records package; `readers/` refers to the corresponding files in the English package.

### Extraction and duplicate-image aliases

Extract both packages into one working directory while preserving their folder structure. Each distinct image byte sequence is stored once. `records/FILE_ALIASES.tsv` identifies every omitted duplicate-image path, its retained identical image and the SHA-256 of those bytes. The complete set of logical proof paths is therefore recoverable without changing any image content or resolution.

Before running the record or proof-verification scripts, restore those duplicate paths from the extracted project directory:

```sh
python3 scripts/restore_file_aliases.py
```

The restoration script verifies the retained bytes against the alias manifest before recreating each duplicate path. Preserve the manifest with the records. All core sources, PDFs and records are physical archive members; the alias mechanism applies to duplicate images.

### Explicit supersession of intermediate PDFs

The final packages contain only the five published PDFs under `readers/`. `records/FINAL_OMISSIONS.tsv` explicitly supersedes {len(gate['final_omissions'])} intermediate PDFs, including cote builds, diagnostic excerpts, clean isolated proofs and complete predecessor PDFs. Each row gives the exact old path, byte count and SHA-256, the final-reader replacement and its SHA-256, and the reason. Workspace files and immutable checkpoints are preserved. Intermediate TeX, logs, actually-viewed PNGs, observations and provenance records remain in the delivery.

Before packaging, the full workspace gate verifies the retained old PDF bytes and geometry. In an extracted delivery those explicitly superseded PDFs are absent. After restoring image aliases, verify that delivery without rewriting its archived gate record by running:

```sh
python3 scripts/final_qa_gate.py --allow-omitted-historical-pdfs --check-only
```

This mode requires an exact omission row and validates the preserved original observation, old PNG hash, equivalence-audit hash and final replacement hash. It freshly renders the current page at the original image scale and at 144 dpi, requiring equality with the preserved old PNG and audited current signatures. An old PDF that is present is always verified normally. The verification scripts import PyMuPDF and Pillow; rerunning the complete ink screen additionally uses NumPy and SciPy.

For complete verification of the published ZIP pair, including restoration and the final publication gate, run:

```sh
python3 scripts/verify_final_archives.py PATH_EN.zip PATH_RECORDS.zip --restore --final-gate
```

Replace the two ZIP arguments with the paths to the English and records archives. Generic checkpoint manifest/restoration verification alone establishes those checkpoint properties; publication verification additionally requires `--final-gate`.

The master contains {len(changes):,} recorded maximal variants. The three reader sources have an identical annotated body and select its diplomatic or corrected branch through `EditionMode`. The master PDF renders the corrected branch with apparatus. A nested correction inside a wholly replaced or deleted passage is retained within that passage's one complete variant; it is not duplicated as an unrelated apparatus entry.

{master_reuse_description}

## Source review and uncertainty

There are {len(decisions):,} decision rows and {coverage['concordance_rows']:,} concordance rows. Every required difference, original doubt and note has its decision record. `CHANGE_REPLAY_AUDIT.json` independently reconstructs all 706 checked pages from the supplied drafts and recorded edits. `FINAL_STRUCTURE_AUDIT.json` verifies exact diplomatic reconstruction from the master, source order, scan metadata, apparatus correspondence and link targets.

The replay audit explicitly accounts for {len(replay['already_incorporated_explanatory_records'])} historical explanatory record already incorporated by exact edit rows. Its hashed adjudication is `records/REPLAY_RECORD_ADJUDICATIONS.json`; unexplained unmatched records, adjudication issues and replay exceptions all number zero.

'''+table(['Source group','Pages','Original unsure','Original illegible','Checked unsure','Checked illegible'],counts)+'''
The checked totals include newly recognized unreadable undertext and provenance doubts. A reduction in one class and an increase in another do not measure a percentage of readable text. The corrected running text omits canceled passages; their doubts remain in the diplomatic form and apparatus. Every doubt which remains in a form is linked to its source scan.

### Concordance outcomes

'''+table(['Outcome','Rows'],sorted(coverage['outcome_counts'].items()))+'''
### Decision labels

'''+table(['Recorded decision','Rows'],collections.Counter(r['decision'] for r in decisions).most_common())+f'''
## Editorial policy

Authorial wording and notation are retained, including consistent forms such as “standart,” “developped,” “it's” for “its,” and “A la.” Only individually justified isolated slips are corrected in the corrected branch. Mathematical defects and missing hypotheses are discussed in the relevant guide paragraph without alteration of the reader text. The supplied terminology standard governs editorial prose, with exact quotations and formulas protected; `EDITORIAL_STANDARDIZATION.tsv` records those editorial changes.

The guide has {len(guide['paragraphs'])} paragraphs, including every numbered section 1–140 and 16-prime in order, the front matter, complete letter to Quillen, related letters and notes, and Brown's appendix. Its references distinguish archive sites from internal typescript folios. It records changes of mind, dependencies and consequential differences from the arXiv witness.

## Compilation and verification

'''+summary+'''
Each `.tex` file is self-contained and compiles with LuaLaTeX from a standard TeX Live installation. Required packages include fontspec, unicode-math, amsmath, mathtools, tikz-cd, lua-ul, pdflscape, geometry, hyperref and bookmark; the fonts are Latin Modern Roman/Sans/Math. Compile a source twice with `lualatex -interaction=nonstopmode -halt-on-error FILENAME.tex`. No external image or TeX input is needed for a delivered reader.

`TYPESETTING_REPORT.md` gives the complete final log metrics, harmless warnings, logical/source link counts, annotation counts, all-page ink screening and every validated visual observation. It distinguishes direct openings from inherited exact-raster observations and separately documents master-body reuse. `APPARATUS_COUNTS.md` distinguishes variant inventory from apparatus entries actually printed in each form. No blanket scaling or raised overflow tolerance is used. The final gate is recorded in `records/FINAL_QA_GATE.json`.

## Rebuilding and records

To regenerate the reader sources, the extracted `edition/` and `inputs/` directories must be siblings under one working parent, with the supplied text files under `inputs/text/`: the build script resolves the inputs at `PROJECT.parent / 'inputs/text'`. Within that input directory it expects `records/PAGES_PS.json`. `scripts/build_readers.py` reads the canonical checked pages, explicit variants and that metadata; `scripts/build_guide.py` joins the reviewed guide fragments. From a fresh working parent containing the supplied archives, one concrete layout is:

```sh
mkdir -p edition inputs/text
unzip PS_READERS_EN.zip -d edition
unzip -o PS_READERS_RECORDS.zip -d edition
unzip PS_TEXT.zip -d inputs/text
python3 edition/scripts/restore_file_aliases.py
python3 edition/scripts/build_readers.py
python3 edition/scripts/build_guide.py
```

The original input archives are intentionally not duplicated in the final delivery. The standalone delivered `.tex` files compile independently of these inputs using the LuaLaTeX command above. `SOURCE_NORMALIZATION.json` records hashes for the completed mechanical integration; do not rerun historical review scripts over the final checked pages.

`CHECK_DECISIONS.tsv` includes exact before/after readings, reasons and source IDs. `ARXIV_CONCORDANCE.tsv` retains all original comparison columns plus outcomes and reasons; `BROWN_CONCORDANCE.tsv` provides the additional Brown comparison. `CHANGES_EN.tsv` has one row for every master variant and apparatus entry. Supplemental ownership tables, notes and historical proofs document the development of the edition and may retain explicitly obsolete working status.

## Checkpoint retention

Every available immutable checkpoint has been inventoried by archive SHA-256 and member path/size/CRC. `CHECKPOINT_ARCHIVES.tsv` identifies the archives; `CHECKPOINT_SUPERSESSION.tsv` lists every distinct earlier member version and either its identical final file or its specific replacement and reason. No earlier ZIP is nested in the final packages. Checkpoint number 61 was reserved across an interrupted save and is not asserted to be a verified saved archive; the recovery record describes that interruption. All work recoverable from the verified checkpoints and the conversation is retained or explicitly superseded.

Checkpoint 67 was valid locally at 591,029,848 bytes, but preparation of its save was rejected before upload because it exceeded the 512 MiB per-file limit. Its local ZIP remains immutable; it is not counted as durably saved.

Checkpoint 68 was durably uploaded using lossless duplicate-image packaging. ZIP CRC validation passed and all 817 aliases were restored exactly. Its verification nevertheless found a two-file manifest race: `scripts/write_final_reports.py` and `records/MATH_PROSE_PROOF_RENDER_MANIFEST.json` changed between manifest hashing and ZIP writing. All 5,851 logical files are accounted for; the discrepancy concerns two stale checksum rows and does not indicate lost content. The archive remains immutable, and its actual member versions are inventoried separately from those stale declarations in `records/CHECKPOINT_68_LOGICAL_MEMBER_AUDIT.json`. Subsequent full checkpoints capture stable member bytes before hashing and ZIP writing; their records explicitly supersede the affected entries. The retention manifest continues to enumerate every earlier version and its replacement.

## Credits and rights

AI-transcribed by Claude Opus 5.5 (Anthropic, effort high); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic).

The witness consulted and not reproduced is the LaTeX edition of Mateo Carmona with the collaboration of Ulrik Buchholtz (arXiv 2111.01000 v2, 2021), extended from the 2015 edition by “the scrivener,” CC0 1.0.

The translation in the appendix is R. Brown's, prepared with assistance from L. Breen and J-L. Loday, as his note says; the rights in it belong to its translator or his heirs.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.
'''
report='# Typesetting and verification report\n\n'+('All final verification gates passed.\n\n' if gate['complete'] else 'Verification remains in progress; unresolved gates are listed in records/FINAL_QA_GATE.json.\n\n')+summary
report+='\n## Log warnings\n\n'
for stem in STEMS:
    b=builds[stem];log=(P/b['log']).read_text();warnings=re.findall(r'(?:LaTeX|Package [^\n]+) Warning:[^\n]*(?:\n\([^\n]*\)[^\n]*)*',log)
    families=collections.Counter(re.sub(r'\b\d+\b','#',w.split('\n')[0]) for w in warnings)
    report+='### '+labels[stem]+'\n\n'+f"Build record: `{structure['forms'][stem]['latest_build_record']}`. Log: `{b['log']}`. Errors: 0; missing characters: {b['missing_character_lines']}; underfull boxes: {len(re.findall(r'Underfull',log))}.\n\n"
    report+=table(['Warning family','Occurrences'],families.most_common()) if families else 'No LaTeX/package warnings.\n'
report+='\nMargin-paragraph relocation warnings record the queueing used to prevent overlap. Numbered note calls remain at their source positions, and full note text is retained. Every selected page has validated visual-review coverage, either a direct opening from the final PDF or a preserved earlier observation carried by exact raster equality. All current ink candidates have their separate visual adjudications. Unicode-math/mathtools command-compatibility warnings do not report missing glyphs.\n'
report+='\n## Links, by PDF and source group\n\nLogical marks count each source macro once, including nested doubts which share their enclosing hyperlink. PDF annotations can be more numerous because one marked passage can wrap across lines. The audit compares every shipped logical mark with the source expectation and independently checks each source key/URL pair against the archive PDF-page metadata.\n\n'
mf=load('BUILD_MANIFEST.json')
linkrows=[]
for stem in STEMS:
    p=structure['pdfs'][stem]
    if stem=='PS_GUIDE':continue
    mode='diplomatic' if stem.endswith('diplomatic') else 'reading' if stem.endswith('reading') else 'corrected_apparatus'
    for g in group_order:
        mm=[m for m in mf if ('Brown (134-2)' if m['key'].startswith('brown_') else m['cote'])==g]
        totals={n:sum(m['expected_link_marks'][mode][n] for m in mm) for n in ['scanpage','unsure','illegible']}
        linkrows.append([labels[stem],g,totals['scanpage'],totals['unsure'],totals['illegible'],p['archive_annotations_by_cote'].get(g,0),p['distinct_pages_by_cote'].get(g,0)])
report+=table(['Form','Source group','Scan marks','Unsure marks','Illegible marks','PDF archive annotations','Distinct source pages'],linkrows)
report+='\n## Ink boundaries\n\nEvery final PDF page was raster-screened at 144 dpi and its drawing/text bounding boxes checked for objects outside the sheet. Candidate components were then inspected as enlarged crops. The body is 18 mm from the left, 45 mm from the right, 18 mm from the top and 22 mm from the bottom; the 28 mm marginal-note column begins 7 mm beyond the body, and page numbers/headers occupy their declared regions. A 0.5 pt raster quantization tolerance is recorded. Only the permitted overhang of one letter remains; punctuation overhangs and layout collisions were repaired locally.\n\n'
for stem in STEMS:
    ink=load('INK_AUDIT_'+stem+'.json')
    report+='### '+labels[stem]+'\n\n'+f"Pages screened: {ink['pages_screened']}; objects outside the sheet: {len(ink['objects_outside_sheet'])}; candidate pages: {len(ink['candidate_pages'])}.\n\n"
    if ink['candidate_pages']:report+=table(['PDF page','Adjudication','Observation'],[[r['page'],r['adjudication'],r.get('observation','')] for r in ink['candidate_pages']])
report+='\n## Visual-review coverage and provenance\n\nThe three readers each include a forty-page sample evenly spread over the complete PDF. Every source page identified by the retained TeX overflow history was additionally selected in each reader, including all its continuation pages; every landscape page was also selected. The full guide is covered, including every previously overflowing heading and bottom-ink location. Selection and rendering alone are never counted as visual inspection.\n\n'
apparatus_qa=gate['pdfs']['PS_EN_corrected_apparatus']
report+=(f"The separate historical raster audit identified **{apparatus_qa['historical_bottom_overflow_sheets_mapped']} bottom-overflow PDF sheets**. Each was mapped by source key and continuation offset to the final corrected-apparatus PDF, producing {len(apparatus_qa['historical_bottom_overflow_target_pages'])} distinct final target pages. Every target has validated visual-review coverage. These historical sheets are additional to the source-page overflow records and are not described as current defects. The complete mapping is `records/QA_SELECTION_PS_EN_corrected_apparatus.json`.\n\n")
report+='A direct review means an image rendered from the exact current PDF was opened and observed. An inherited review uses the method “raster identity with an actually opened image”: an original observation remains attached to its old PDF and retained PNG, and an audit proves equality with the current page at 144 dpi and at the original 1.4 rendering scale. The gate validates the current and old PDF/image hashes, the immutable original evidence snapshot and entry, the equivalence-audit hash, geometry, pixel signatures, and normalized historical provenance. When an original record did not store a PNG byte hash, that absence remains explicit; its retained PNG must instead be bound to the exact old PDF raster. Any changed raster page requires a fresh direct current-image opening.\n\n'
report+='The full pre-packaging gate runs with every old PDF present and verifies its bytes. Final delivery explicitly supersedes those intermediate PDFs, so extracted verification uses `--allow-omitted-historical-pdfs --check-only` after image-alias restoration. That mode accepts an absent predecessor only through its exact `FINAL_OMISSIONS.tsv` row, validates all preserved PNG/original-record/audit hashes, and freshly renders the current page at both required scales. It does not claim to reread an absent old PDF or to reopen the inherited image visually. Any old PDF actually present still receives normal hash and geometry checks.\n\n'
report+='### Annotated-master body reuse\n\n'+master_reuse_description+f" Audit SHA-256: `{master_reuse['audit_sha256']}`. The comparison itself claims zero image openings.\n\n"
for stem in STEMS:
    sha=gate['pdfs'][stem]['pdf_sha256']
    # Prefer direct current-image evidence when both methods cover one page.
    by_page={}
    for row in visual[stem]:
        if row['page'] not in by_page or row['review_basis'].startswith('direct opening'):
            by_page[row['page']]=row
    rows=[by_page[page] for page in sorted(by_page)]
    details=[]
    for row in rows:
        inherited=row['review_basis']=='raster identity with an actually opened image'
        observation=row.get('prior_actual_image_observation',row['observation']) if inherited else row['observation']
        provenance=row['evidence_file']
        if inherited:
            prior=row['provenance']
            provenance+=(f"; original {prior['preserved_original_evidence_file']} entry {prior['source_entry_index']}; old PDF SHA-256 {prior['old_pdf_sha256']}; audit {prior['equivalence_audit']}")
        details.append([row['page'],row.get('key',''),row['review_basis'],observation,row.get('image',''),provenance])
    report+='### '+labels[stem]+'\n\n'+f'PDF SHA-256: `{sha}`.\n\n'+table(['PDF page','Source key / scope','Review basis','Observation','Rendered image','Evidence and provenance'],details)
report+='\nOriginal observations, including any defects described on superseded PDFs, remain in their source records and immutable historical snapshots. They are not relabeled as current-PDF openings or counted as unresolved current defects. `FINAL_QA_GATE.json` lists the superseded evidence separately; current coverage is accepted only through a validated direct opening or the explicit raster-equality chain above.\n'
report+='\n## Exact change replay\n\n'+f"All {replay['equal_pages']} of {replay['pages']} source pages reconstruct identically, with complete source coverage. The audit exposes {len(replay['already_incorporated_explanatory_records'])} historical explanatory record already incorporated by exact edit rows; its full row objects and canonical row hashes are bound in `{replay['adjudication_file']}` (SHA-256 `{replay['adjudication_sha256']}`). There are {len(replay['unmatched_records'])} unexplained unmatched records, {len(replay['adjudication_issues'])} adjudication issues and {len(replay['exceptions'])} replay exceptions. Any such unresolved condition fails the final gate.\n"
history=read('OVERFLOW_HISTORY.tsv');report+='\n## Historical repairs and supersession\n\n'+f"The retained overflow history contains {len(history)} measured events, with a largest recorded excess of {max((float(r['excess_pt']) for r in history),default=0):.5f}pt. These include failed and superseded builds; they are not final defects. Every event remains in `records/OVERFLOW_HISTORY.tsv`; local repairs, source lines and their reasons are in `records/TYPESETTING_FIXES.tsv`. The final boxes are all at most 2 pt.\n\n"
report+='There is no blanket rescaling. The specifically recorded whole-diagram reduction is 82% on 134-6/106; smaller scale values attached to decorative marks are not reductions of text or mathematical diagrams. Long displays are locally broken, and diagram gaps are adjusted at their source. Long marginal notes are ruled, labeled blocks at their call; short notes use the margin queue.\n\n'
report+=f"The checkpoint inventory covers {checkpoint['archives']} verified archives, {checkpoint['unique_paths']} paths and {checkpoint['unique_member_versions']} distinct member versions. Every inventoried logical path has a retained counterpart or an explicit replacement; duplicate-image paths are recoverable through the alias manifest. The complete file-by-file disposition, including every superseded passage-bearing version, is `records/CHECKPOINT_SUPERSESSION.tsv`. Earlier partial reader, guide, record and report versions are superseded by the named final counterparts; historical diagnostics are retained with runtime-location redactions documented separately. No earlier checkpoint was overwritten or deleted.\n"
report+='\n## Extraction, image aliases and checkpoint save status\n\nExtract the English and records packages into the same working directory, preserving their folders. The packages store each distinct image byte sequence once. `records/FILE_ALIASES.tsv` maps every omitted duplicate-image path to a retained image with identical bytes and its SHA-256. Before running record or proof verification, run `python3 scripts/restore_file_aliases.py` from the extracted project directory. The script checks the retained bytes against the manifest before recreating the duplicate paths. This restores every logical proof path at its original content and resolution. Core sources, PDFs and records remain physical archive members.\n\nCheckpoint 67 was validated locally (591,029,848 bytes), but its save preparation was rejected before any upload because the file exceeded 512 MiB. The local ZIP is preserved and is not represented as durably saved. Checkpoint 68 was durably uploaded; its ZIP CRC passed and all 817 aliases were restored exactly. Two physical members nevertheless disagreed with the manifest because they changed between hashing and ZIP writing: `scripts/write_final_reports.py` and `records/MATH_PROSE_PROOF_RENDER_MANIFEST.json`. The immutable archive and its actual member versions remain inventoried, and subsequent full checkpoints capture stable bytes before hashing and packaging and explicitly supersede those race-affected entries. The complete older-version and explicit-replacement retention manifests remain in force.\n'
report+='\nCheckpoint 68 has no detected content loss: all 5,851 logical files are accounted for through 5,034 physical members and 817 verified aliases. Its two stale checksum declarations and the actual archived byte hashes are distinguished in `records/CHECKPOINT_68_LOGICAL_MEMBER_AUDIT.json`; the restoration audit is `records/CHECKPOINT_68_RESTORATION_AUDIT.json`. `CHECKPOINT_ALIAS_MEMBERS.tsv` records each checkpoint alias separately, and `CHECKPOINT_MANIFEST_VERIFICATION.json` distinguishes documented historical metadata discrepancies from unexplained failures.\n'
report+='\n## Intermediate-PDF supersession\n\n'+f"Only the five published PDFs are included in final delivery. `records/FINAL_OMISSIONS.tsv` maps {len(gate['final_omissions'])} exact intermediate-PDF versions to their final-reader replacements, with both SHA-256 values and individual reasons. This includes clean viewed local proofs as well as obsolete cote/probe builds and predecessor PDFs used during raster verification. Their non-PDF sources, logs, PNG observations and provenance remain available, and all original workspace/checkpoint files remain unchanged. `CHECKPOINT_SUPERSESSION.tsv` classifies the omitted paths as explicitly superseded for final delivery, rather than retained PDFs. `records/FINAL_OMISSIONS_AUDIT.json` records source scope and associated evidence.\n"
report+='\n## Final archive verification\n\nVerify the complete published pair with `python3 scripts/verify_final_archives.py PATH_EN.zip PATH_RECORDS.zip --restore --final-gate`. The verifier must restore the exact declared alias set and run the final publication gate. Within an already extracted project, use `python3 scripts/final_qa_gate.py --allow-omitted-historical-pdfs --check-only`; this checks the explicit intermediate-PDF supersessions without rewriting the archived gate record. A generic checkpoint manifest/restoration check without `--final-gate` certifies only the checkpoint manifest and restoration properties, not final publication.\n'
(P/'README.md').write_text(readme);(P/'TYPESETTING_REPORT.md').write_text(report)
print(json.dumps({'readme_bytes':len(readme.encode()),'report_bytes':len(report.encode()),'complete_gate':gate['complete']}))
