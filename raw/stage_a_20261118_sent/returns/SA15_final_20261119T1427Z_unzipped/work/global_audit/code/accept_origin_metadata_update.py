"""Accept the70 owner-origin additions read in full during the census.

This only updates this audit's reviewed input snapshot. It edits no owner file
and changes no classification. Unexpected source transitions still fail.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parent
path=ROOT/'status_input_snapshot.json'
before=json.loads(path.read_text());byid={r['legacy_claim_id']:r for r in before}
current={c['id']:c for filename in ['claims_c7.json','claims_c8.json'] for c in json.loads((WORK/'root_review'/filename).read_text())}
changes=[]
for n in range(1,71):
    ident=f'P78-C{n:03d}';old=byid[ident];new=current[ident]
    assert new.get('origin')=='manuscript' and new['status_on_pages']==old['status_on_pages']
    if old['origin_present']:
        assert old['origin']=='manuscript'
        continue
    assert old['origin'] is None
    changes.append({'legacy_claim_id':ident,'old_origin_present':False,'old_origin':None,'new_origin':'manuscript',
        'status_unchanged':True,'census_unchanged':True,'review':'Full status and new origin fields read; root classifies the source assertion/reused text as manuscript origin.'})
    old['origin_present']=True;old['origin']='manuscript'
if changes:
    initial=ROOT/'status_input_snapshot_before_root_origin_update.json'
    if not initial.exists():initial.write_text(path.read_text())
    path.write_text(json.dumps(before,ensure_ascii=False,indent=2)+'\n')
    history=ROOT/'origin_metadata_review.json'
    earlier=json.loads(history.read_text()) if history.exists() else []
    history.write_text(json.dumps(earlier+changes,ensure_ascii=False,indent=2)+'\n')
print(f'Accepted {len(changes)} reviewed origin additions; no census decision changed.')
