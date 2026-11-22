"""Record completed root log and image inspections of the working build."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
build=json.loads((root/'logs/build_20261119T200126Z.json').read_text())
render=json.loads((root/'logs/pdf_qa_finish_12_render.json').read_text())
assert build['pdf_sha256']==render['pdf_sha256']
assert not build['warnings'] and not build['bibliography_warnings']
assert build['overfull_above_2pt']==0
assert render['pages_total']==283 and len(render['pages_rendered'])==72
hashes={}
def visit(path):
    if not path.suffix:path=path.with_suffix('.tex')
    key=str(path.relative_to(root))
    if key in hashes:return
    hashes[key]=hashlib.sha256(path.read_bytes()).hexdigest()
    for name in re.findall(r'\\input\{([^}]+)\}',path.read_text()):visit(root/name)
visit(root/'RESEARCH_SA17_paper.tex')
assert len(hashes)==75
qa=dict(render)
qa.update({'inspected_utc':now,'visual_check':'PASS: root directly viewed all18 contact sheets containing72 pages. All new MF and henselian sections, both residual overflow pages43 and57, a spread across all Parts, the remaining gates and the entire bibliography were inspected. No clipping, overlap or missing glyphs observed. Rendering alone was not treated as inspection.','build_log':'logs/build_20261119T200126Z_3.txt','bibtex_log':'logs/build_20261119T200126Z_1.txt','full_logs_read_by_root':True,'overfull_above_2pt':0,'overfull_pt':build['overfull_pt'],'max_overfull_pt':max(build['overfull_pt']),'warnings':[],'bibtex_warnings':[],'compiled_source_hashes':hashes,'bibliography_sha256':hashlib.sha256((root/'RESEARCH_SA17_references.bib').read_bytes()).hexdigest(),'scope':'Verified working build for checkpoint12; any later source changes require renewed build and QA. No archive created by this record.'})
for name in ['pdf_qa_checkpoint_12.json','pdf_qa_passed.json']:
    (root/'logs'/name).write_text(json.dumps(qa,indent=2)+'\n')
with (root/'CHECK_EVENTS.tsv').open(newline='') as f:events=list(csv.DictReader(f,delimiter='\t'))
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(r['type'] in allowed for r in events)
record={'timestamp':now,'scope':'Production correction only, not mathematical movement','bibliography_warnings_before':1,'bibliography_warnings_after':0,'correction':'The Nowak primary arXiv preprint was changed from article to misc to avoid inventing journal metadata. The build guard now checks every BibTeX warning as well as final compiler warnings.','overfull_above_2pt_before':0,'overfull_above_2pt_after':0,'final_build':'logs/build_20261119T200126Z.json','final_build_seconds':build['seconds'],'render_seconds':render['seconds'],'pages':283,'statements':261,'compiled_inputs':75,'check_events':len(events)}
(root/'logs/checkpoint_12_working_qa_summary.json').write_text(json.dumps(record,indent=2)+'\n')
report=root/'RESEARCH_SA17_report.md';s=report.read_text()
marker='## Typesetting verification\n\n'
heading='### Working verification for checkpoint 12'
assert heading not in s
s=s.replace('### Current checkpoint 11 verification','### Historical checkpoint 11 verification')
s=s.replace(marker,marker+f'''{heading}

The current working PDF has283 pages, exactly261 numbered statements and261 catalog rows,75 compiled TeX inputs and{len(events)} allowed-type check events. The final four-pass build took25.728453 s. Root read the complete final compiler and BibTeX logs. One bibliography warning in the preceding build was corrected by recording the opened Nowak arXiv preprint as a miscellaneous source, with no invented journal. The build guard now rejects bibliography warnings as well as compiler warnings. The final build has zero warnings, undefined references or missing glyphs; no overfull box exceeds2 pt. The two unchanged smaller overflows are1.40959 pt on page43 and0.93779 pt on page57.

Root directly viewed all18 contact sheets containing72 selected pages, including every newly added proof, both overflow pages, a spread across all Parts, the remaining-gate section and the entire bibliography. No clipping, overlap or missing glyphs was observed. Rendering took0.854033 s. The exact PDF,75 source hashes and bibliography hash are recorded in `logs/pdf_qa_checkpoint_12.json`. This working verification is valid only for those hashes; later source changes require a fresh build and inspection. No checkpoint was made outside its scheduled boundary.

''',1)
report.write_text(s)
with (root/'notes/ROOT_STATUS.md').open('a') as f:f.write(f'''\n\n## Verified working build — {now}

Nine audited statements were promoted: the2 MF-Swan/cancellation statements and7 henselian projective/arithmetic/coefficient statements. Current PDF283pages,261numbered/catalog rows,75compiled inputs,{len(events)}check events,126bibliography entries. Final build200126 took25.728453s; full compiler/BibTeX logs and all72rendered pages on18sheets have been read/viewed. PDFSHA={qa['pdf_sha256']}. QA is logs/pdf_qa_checkpoint_12.json. One empty-journal warning was fixed by changing the arXiv preprint record to misc; no mathematical source changes. Source freeze is not imposed yet; changes invalidate this working QA. Formal review05 due20:06:58UTC, checkpoint12due20:36:58UTC. No archive created early and no stopping condition met.
''')
print(json.dumps(record))
