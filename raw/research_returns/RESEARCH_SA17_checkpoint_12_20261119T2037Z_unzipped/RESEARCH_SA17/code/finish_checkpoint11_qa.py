"""Record root's completed log/image inspections; this does not inspect images."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, time

start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
build=json.loads((root/'logs/build_20261119T193945Z.json').read_text())
render=json.loads((root/'logs/pdf_qa_finish_11_render.json').read_text())
assert build['pdf_sha256']==render['pdf_sha256']
assert not build['warnings'] and build['overfull_above_2pt']==0
hashes={}
def visit(path):
    if not path.suffix:path=path.with_suffix('.tex')
    key=str(path.relative_to(root))
    if key in hashes:return
    hashes[key]=hashlib.sha256(path.read_bytes()).hexdigest()
    for name in re.findall(r'\\input\{([^}]+)\}',path.read_text()):visit(root/name)
visit(root/'RESEARCH_SA17_paper.tex')
assert len(hashes)==71
compiler=(root/'logs/build_20261119T193945Z_3.txt').read_text()
bib=(root/'logs/build_20261119T193945Z_1.txt').read_text()
assert 'Warning:' not in compiler and 'Warning' not in bib
qa=dict(render)
qa.update({'inspected_utc':now,'visual_check':'PASS: root directly inspected all18 contact sheets containing72 selected pages. The selection covers every new section, the repaired alignment, both residual overflow pages43 and57, a spread across PartsA-D, the exact remaining gates and the entire bibliography. No clipping, overlap or missing glyphs observed. Rendering itself is not the inspection.', 'build_log':'logs/build_20261119T193945Z_3.txt','bibtex_log':'logs/build_20261119T193945Z_1.txt','full_logs_read_by_root':True,'overfull_above_2pt':0,'max_overfull_pt':max(build['overfull_pt']),'overfull_pt':build['overfull_pt'],'warnings':[],'bibtex_warnings':[],'compiled_source_hashes':hashes,'bibliography_sha256':hashlib.sha256((root/'RESEARCH_SA17_references.bib').read_bytes()).hexdigest()})
for name in ['pdf_qa_checkpoint_11.json','pdf_qa_passed.json']:
    (root/'logs'/name).write_text(json.dumps(qa,indent=2)+'\n')
record={'timestamp':now,'scope':'typesetting/editorial repairs only','initial_fatal':'Extra alignment tab in C.1.MT7: changed split to aligned, preserving all four equations','bookmark_warnings_before':6,'bookmark_warnings_after':0,'bookmark_repair':'Two subsection optional plain-text C1 headings, without changing mathematical content','overfull_above_2pt_before':0,'overfull_above_2pt_after':0,'build_warning_guard':'Expanded build_paper.py to reject all Warning lines as well as undefined references and missing glyphs','WG_reference_repair':'Two attempted Lemma-to-Theorem environment-name substitutions, one matched in the actual draft; the other reference was absent','post_audit_source_hashes':{key:hashes[key] for key in ['sections/C_finish_shallow_mixed_three_torsion.tex','sections/C_finish_C1_henselizations.tex','sections/C_finish_C1_coherent_products.tex','sections/C_finish_global_function_WG.tex']}}
(root/'logs/checkpoint_11_typesetting_repairs.json').write_text(json.dumps(record,indent=2)+'\n')
report=root/'RESEARCH_SA17_report.md'
text=report.read_text().replace('### Current checkpoint 10 verification','### Historical checkpoint 10 verification')
needle='## Typesetting verification\n\n'
assert needle in text
text=text.replace(needle,needle+'''### Current checkpoint 11 verification

The current PDF has270 pages, exactly252 numbered statements and252 catalog rows, and71 compiled TeX inputs. The final four-pass LuaLaTeX/BibTeX build took24.118218 s. Root read the entire final compiler and bibliography logs. No LaTeX or bibliography warnings, undefined references or missing glyphs remain. There were no boxes above2 pt in either successful build; the two unchanged smaller boxes are1.40959 pt on page43 and0.93779 pt on page57. One invalid split alignment was changed to an aligned display. Six math-in-bookmark warnings from two new headings were removed with plain-text bookmark headings. The build guard now also rejects all compiler Warning lines. These are production repairs, not mathematical movement.

Root directly inspected all18 contact sheets containing72 selected pages, including every new section, the repaired display, both residual overflow pages, a spread across all Parts, the exact remaining gates and the entire bibliography. No clipping, overlap or missing glyphs was observed. Rendering took0.761930 s. `logs/pdf_qa_checkpoint_11.json` records the exact PDF hash, all71 compiled-source hashes and the bibliography hash. The successful and failed build logs, repair record and rendered sheets are retained.

''',1)
report.write_text(text)
with (root/'CHECK_EVENTS.tsv').open(newline='') as f:events=list(csv.DictReader(f,delimiter='\t'))
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(row['type'] in allowed for row in events)
status=f'''\n\n## Checkpoint11 preparation — {now}

Compiled-source freeze is active until checkpoint11 is saved at its19:51:58UTC boundary. The current verified PDF has270pages,252numbered/catalog rows,71compiled TeX inputs and{len(events)}check events. Final build193945 took24.118218s; root read the complete final compiler/BibTeX logs and directly inspected72pages on18contact sheets. Zero warnings and zero overflow above2pt; PDFSHA256={qa['pdf_sha256']}. Full hash record is logs/pdf_qa_checkpoint_11.json. All newly included statements have root and independent actual-proof audits. Minor post-audit changes are recorded in logs/checkpoint_11_typesetting_repairs.json.

Promoted families: the exact regular-coherent/valuation C1 criterion and coherent modular-locus sufficiency; C1-residue and coherent-local henselizations, higher-rank valuation families outside flat Noetherian local unions, and full-square-class products for C3; all explicit global function-field arithmetic including inseparable towers, CSA splitting/index/division factors, arbitrary finite-algebra radicals, all hermitian isometry cases, and complete WG algorithms over their finite-dimensional coefficient algebras and stated affine/valuation henselizations. C1 noncoherent positive example and mixed shallow three-torsion bound are not counted as fresh main-gate movement. Failed first-pi and pi-cubed probes are recorded with exact scope and timings.

Only C.1 and C.3 remain open. No stopping condition met. Review05 is due20:06:58UTC; previous no-movement streak0. Active new research remains uncompiled: the ramified node xy=pi³u,2=v*pi² and singularity-category transfer; mixed shallow cubic classes; henselian valued fields beyond the global function-field family. Next checkpoint12 due20:36:58UTC after checkpoint11save. Do not recreate checkpoint10.
'''
with (root/'notes/ROOT_STATUS.md').open('a') as f:f.write(status)
with (root/'PROGRESS_LEDGER.md').open('a') as f:f.write(f'''\n\n### Working update before checkpoint11 — {now}

This is not the scheduled hourly review. The regular-coherent/valuation criterion and coherent modular-locus theorem are now promoted. The new effective C1/coherent-local henselization families and global function-field division/hermitian arithmetic, coefficient-algebra and henselization WG theorems all have complete written proofs and independent audits. They remove whole families from the remaining C1/C3 gates. The noncoherent positive example was already covered by filtered colimits, the mixed shallow three-torsion bound proves no vanishing, and the failed detector programs count as no movement. Only C.1 and C.3 remain Open. The verified270-page/252-statement paper is ready for the19:51:58UTC checkpoint boundary; research continues. Formal review05 remains due20:06:58UTC, with the previous no-movement streak0.
''')
summary={'timestamp':now,'scope':'completed root log and visual QA record; not mathematical progress','pages':270,'statements':252,'compiled_inputs':len(hashes),'check_events':len(events),'pdf_sha256':qa['pdf_sha256'],'seconds':time.perf_counter()-start}
(root/'logs/checkpoint_11_qa_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
