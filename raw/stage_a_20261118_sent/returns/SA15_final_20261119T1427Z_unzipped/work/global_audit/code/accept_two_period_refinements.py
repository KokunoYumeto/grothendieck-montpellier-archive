"""Add the two newly read root refinement objects to the reviewed snapshot.

Only census files change. The prior384-row output is retained separately.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent
for filename in ['status_index.tsv','status_counts.json','status_input_snapshot.json','status_curated_map.json']:
    p=ROOT/filename;old=ROOT/(p.stem+'_384'+p.suffix)
    if p.exists() and not old.exists():old.write_bytes(p.read_bytes())
path=ROOT/'status_input_snapshot.json';snapshot=json.loads(path.read_text())
seen={r['legacy_claim_id'] for r in snapshot}
claims={c['id']:c for c in json.loads((WORK/'root_review/claims_c8.json').read_text())}
added=[]
for ident,parent in [('P78-C072','P78-C046'),('P78-C073','P78-C047')]:
    c=claims[ident]
    assert c['origin']=='present-run refinement' and c['parent']==parent
    assert c['refinement_provenance']=='Earlier-run period diagnostics retained; precise statement and proof scope recorded in this run.'
    assert c['status_on_pages']==f'present-run refinement; the parent literal assertion and its source status remain in {parent}'
    if ident in seen:continue
    snapshot.append({'legacy_claim_id':ident,'owner_file':'root_review/claims_c8.json','status_on_pages':c['status_on_pages'],
        'origin_present':True,'origin':c['origin'],'counterexample_origin':c.get('counterexample_origin'),
        'refinement_provenance':c['refinement_provenance'],'parent':parent,
        'his_statement':c['his_statement'],'statement':c['statement'],'owner_fate':c['fate']})
    added.append(ident)
assert len(snapshot)==386
path.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
(ROOT/'period_refinement_review.json').write_text(json.dumps({'added_after_full_object_read':added,'owner_registers_changed':False,'earlier_run_diagnostic_provenance_retained':True,'existing_census_decisions_changed':False},ensure_ascii=False,indent=2)+'\n')
print('Accepted two separately read period refinements; prior384-row census retained.')
