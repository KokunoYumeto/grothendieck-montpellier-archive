"""Record the completed final checkpoint-12 log and visual inspections."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
build = json.loads((root / 'logs/build_20261119T202625Z.json').read_text())
render = json.loads((root / 'logs/pdf_qa_finish_12_render.json').read_text())
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert build['pdf_sha256'] == render['pdf_sha256'] == digest(root / 'RESEARCH_SA17_paper.pdf')
assert not build['warnings'] and not build['bibliography_warnings']
assert build['overfull_above_2pt'] == 0
assert render['pages_total'] == 300 and len(render['pages_rendered']) == 82
hashes = {}
def visit(path):
    if not path.suffix:
        path = path.with_suffix('.tex')
    key = str(path.relative_to(root))
    if key in hashes:
        return
    hashes[key] = digest(path)
    for name in re.findall(r'\\input\{([^}]+)\}', path.read_text()):
        visit(root / name)
visit(root / 'RESEARCH_SA17_paper.tex')
assert len(hashes) == 80
with (root / 'RESEARCH_SA17_results.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open(newline='') as f:
    events = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 271 and len(events) == 651
allowed = {'targeted proof check', 'independent re-proof', 'computation or formal certificate', 'used and rechecked in this run', 'carried as background without fault found', "refuted, with the refined statement's id"}
assert all(r['type'] in allowed for r in events)
assert sorted(r['id'] for r in rows if r['status'] == 'Open') == ['C:BO_general_gate', 'C:allrings_gate']
qa = dict(render)
qa.update({
    'inspected_utc': now,
    'visual_check': 'PASS: root directly viewed all21 contact sheets containing82 pages in small batches. All new odd-node comparison, relative-Swan, separably-closed, Greenberg and infinite-residue proofs, earlier MF and henselian additions, both residual overflow pages43 and57, a spread across all Parts, the remaining gates and the entire bibliography were inspected. No clipping, overlap or missing glyphs observed. Rendering alone was not treated as inspection.',
    'build_log': 'logs/build_20261119T202625Z_3.txt',
    'bibtex_log': 'logs/build_20261119T202625Z_1.txt',
    'full_logs_read_by_root': True,
    'overfull_above_2pt': 0,
    'overfull_pt': build['overfull_pt'],
    'max_overfull_pt': max(build['overfull_pt']),
    'warnings': [], 'bibtex_warnings': [],
    'compiled_source_hashes': hashes,
    'bibliography_sha256': digest(root / 'RESEARCH_SA17_references.bib'),
    'scope': 'Final verified build for checkpoint12; any later compiled-source or bibliography change invalidates this QA. No archive is created by this record.'
})
for name in ['pdf_qa_checkpoint_12.json', 'pdf_qa_passed.json']:
    (root / 'logs' / name).write_text(json.dumps(qa, indent=2) + '\n')
promoted = json.loads((root / 'logs/C_checkpoint12_second_promotion.json').read_text())['promotions']
repairs = {
    'timestamp': now,
    'scope': 'Production corrections only; no mathematical claims changed and no movement counted.',
    'corrections': [
        'Closed the missing displayed-math delimiter after (C.3.IR1).',
        'Moved the unchanged long Spec expression in the Greenberg proof to a display, removing its3.03589pt overflow.',
        'Moved the (C.3.IR5) tag outside the split environment.',
        'Recorded the Burke-Walker arXiv preprint as misc instead of an article with an empty journal.'
    ],
    'overfull_above_2pt_before': 1, 'overfull_above_2pt_after': 0,
    'sources': [{'source': r['source'], 'audited_sha256': r['audited_sha256'], 'compiled_source': r['compiled_source'], 'initial_compiled_sha256': r['compiled_sha256'], 'final_compiled_sha256': digest(root / r['compiled_source'])} for r in promoted],
    'failed_builds': ['logs/build_20261119T202249Z.json', 'logs/build_20261119T202544Z.json'],
    'final_build': 'logs/build_20261119T202625Z.json'
}
(root / 'logs/checkpoint_12_typesetting_repairs.json').write_text(json.dumps(repairs, indent=2) + '\n')
record = {'timestamp': now, 'scope': 'Completed final checkpoint12 QA; archive must wait for20:36:58UTC.', 'pages': 300, 'statements': 271, 'compiled_inputs': 80, 'check_events': 651, 'bibliography_entries': len(re.findall(r'^@', (root / 'RESEARCH_SA17_references.bib').read_text(), re.M)), 'final_build': 'logs/build_20261119T202625Z.json', 'final_build_seconds': build['seconds'], 'render_seconds': render['seconds'], 'pages_inspected': 82, 'contact_sheets_inspected': 21, 'pdf_sha256': qa['pdf_sha256']}
(root / 'logs/checkpoint_12_working_qa_summary.json').write_text(json.dumps(record, indent=2) + '\n')
report = root / 'RESEARCH_SA17_report.md'
s = report.read_text()
a = s.index('### Working verification for checkpoint 12')
b = s.index('### Historical checkpoint 11 verification', a)
s = s[:a] + '''### Current checkpoint 12 verification

The current PDF has300 pages, exactly271 numbered statements and271 catalog rows,80 compiled TeX inputs and651 allowed-type check events. The final four-pass build took27.223571 s. We read the complete final compiler and BibTeX logs. The final build has zero compiler or bibliography warnings, undefined references or missing glyphs. One new3.03589 pt prose overflow was removed by displaying the unchanged expression; the count above2 pt is now0. The two smaller unchanged overflows are1.40959 pt on page43 and0.93779 pt on page57. We also closed one missing display delimiter and moved one tag outside a split environment. Preprint bibliography records avoid invented journal metadata. These are production corrections only.

We directly viewed all21 contact sheets containing82 selected pages, including every new proof, the repaired display, both residual overflow pages, a spread across all Parts, the remaining-gate section and the entire bibliography. No clipping, overlap or missing glyphs was observed. Rendering took0.898960 s. The exact PDF, all80 compiled-source hashes and the bibliography hash are recorded in `logs/pdf_qa_checkpoint_12.json`; the post-audit typography changes are recorded in `logs/checkpoint_12_typesetting_repairs.json`. Later compiled-source changes invalidate this verification. No checkpoint was made outside its scheduled boundary.

''' + s[b:]
report.write_text(s)
with (root / 'notes/ROOT_STATUS.md').open('a') as f:
    f.write(f'''\n\n## Checkpoint12 preparation — {now}

Compiled-source and bibliography freeze remains active through the20:36:58UTC save. Final PDF300pages/271numbered and catalog statements/80compiled inputs/651check events/131bibliography entries. Build202625 took27.223571s; root has read the entire final compiler and BibTeX logs and directly inspected all82rendered pages on21sheets. Zero warnings and zero overflow>2pt; PDFSHA={qa['pdf_sha256']}. QA is logs/pdf_qa_checkpoint_12.json with all source/bibliography hashes. Three TeX production repairs and preprint bibliography types are recorded separately, without mathematical changes.

Ten additional audited statements are compiled: odd-node MCM comparison boundary, exact relative-Swan MF bridge, three separably-closed field/coefficient results, two Greenberg decision results and three infinite-residue henselian results. New C3 field/coefficient families strictly shrink the main gate; the C1 categorical boundaries and abstract Greenberg method are not counted separately. Only C.1/C.3 remain Open. Review05movementYES,streak0; nextreview21:06:58UTC. No stopping condition met.

Uncompiled drafts: perfection three-statement proof has full regular_coherent peer PASS; supported Picard two-statement proof has full flat_union peer PASS; nondiscrete-torsion C2 all-rank boundary and exact certificate are awaiting root audit. Root will read these actual files after QA. The supported Picard-to-Swan bridge and all-degree torsion/excision route remain unproved. Do not promote a draft before root audit or while this freeze remains.
''')
print(json.dumps(record, indent=2))
