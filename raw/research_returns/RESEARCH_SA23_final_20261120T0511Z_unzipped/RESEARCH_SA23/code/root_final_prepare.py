"""Verify the final stopped state and reuse only the unchanged, inspected PDF.

This does not stop research, rebuild a paper, render a page or create an
archive. Run it after the actual final formal review and registry merge.
"""
from pathlib import Path
import csv, datetime, hashlib, json, time, zipfile
import fitz

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviews=json.loads((root/'logs/formal_reviews.json').read_text())
assert reviews[-1]['review']==3
assert reviews[-1]['stopping_rule_fired']
assert reviews[-1]['consecutive_reviews_without_movement']==2
assert reviews[-1]['overall_state']=='INCOMPLETE'
audit=json.loads((root/'logs/registry_audit.json').read_text())
assert audit['numbered_labels']==audit['statement_rows']==120
for key in ['missing_rows','extra_rows','conflicting_rows','invalid_statuses',
            'labels_without_events','duplicate_labels','invalid_event_types']:
    assert not audit[key], (key,audit[key])
with (root/'notes/outcome_table.tsv').open() as handle:
    outcomes=list(csv.DictReader(handle,delimiter='\t'))
unsettled=[row for row in outcomes if 'unsettled' in row['state'].lower()]
assert len(unsettled)==1 and unsettled[0]['item'].startswith('Lead6')
with (root/'notes/manuscript_date_attempts.tsv').open() as handle:
    routes=list(csv.DictReader(handle,delimiter='\t'))
qa=json.loads((root/'logs/root_pdf_review_checkpoint06.json').read_text())
build=json.loads((root/'logs/build_diagnostics.json').read_text())
pdf=root/'RESEARCH_SA23_paper.pdf'
pdf_sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pdf_sha==qa['pdf_sha256']
assert qa['inspection_completed_utc']
seen=sorted(set(qa['root_pages_inspected']+qa['category_pages_inspected']))
assert seen==sorted(qa['pages_rendered']) and len(seen)==17
assert all(item['returncode']==0 for item in build['commands'])
assert not build['warnings']
assert build['overfull_count']==build['overfull_gt_2pt']==0
assert build['max_overfull_pt']<=2
with fitz.open(pdf) as document:
    assert len(document)==qa['pdf_pages']==91

# Check the complete current typesetting inputs against the inspected
# checkpoint, so an unchanged PDF cannot conceal an unbuilt source edit.
inputs=[root/'RESEARCH_SA23_paper.tex',root/'RESEARCH_SA23_references.bib']
inputs+=sorted((root/'sections').glob('*.tex'))
checkpoint=root.parent/'RESEARCH_SA23_checkpoint_06.zip'
unchanged=[]
with zipfile.ZipFile(checkpoint) as archive:
    for path in inputs:
        rel=path.relative_to(root).as_posix()
        old=archive.read(root.name+'/'+rel)
        current=path.read_bytes()
        assert current==old, 'Typesetting input changed since inspected checkpoint: '+rel
        unchanged.append({'path':rel,'sha256':hashlib.sha256(current).hexdigest(),'bytes':len(current)})
record={'created_utc':stamp,'overall_state':'INCOMPLETE',
        'stopping_review_utc':reviews[-1]['created_utc'],
        'research_stopped':True,'numbered_statements':audit['statement_rows'],
        'outcome_rows':len(outcomes),'unsettled_outcome_rows':unsettled,
        'check_events':audit['events'],'corrections':audit['corrections'],
        'documentary_routes':len(routes),'pdf_pages':91,'pdf_sha256':pdf_sha,
        'typesetting_inputs_identical_to_checkpoint06':unchanged,
        'visual_check_reused_from_utc':qa['inspection_completed_utc'],
        'pages_previously_directly_inspected':seen,
        'fresh_visual_inspection_claimed':False,
        'overfull_before':0,'overfull_after':0,'warnings':[],
        'elapsed_seconds':time.perf_counter()-started}
(root/'logs/root_final_prepare.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'verification/visual_QA.md').open('a') as handle:
    handle.write(f'\n\n## Final-delivery identity check — {stamp}\n\n'
      f'The final PDF SHA256 is `{pdf_sha}`, identical to checkpoint06. '
      f'All {len(unchanged)} current typesetting input files match that checkpoint byte for byte. '
      'We reuse the actual seventeen-page visual inspection completed at '
      f'{qa["inspection_completed_utc"]}; no new visual inspection is claimed. '
      'The unchanged build has zero warnings and zero overfull boxes '
      '(before/after 0/0; none exceeds 2 pt). '
      'The exact final-state and identity checks are in logs/root_final_prepare.json.\n')
print(json.dumps(record,indent=2))
