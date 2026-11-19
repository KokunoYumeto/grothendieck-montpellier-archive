"""Validate the manually authored merge proposals and serialize comparison events."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WS=ROOT.parents[2]
OUT=WS/'work'/'outputs'
p=OUT/'cross_merge_proposals.json'
a=json.loads(p.read_text())
known={}
for part in ('cote62','cote64_early','cote64_late'):
 for item in json.loads((WS/'work'/'parts'/part/'items.json').read_text()):
  known[item['id']]=item
seen=set()
for proposal in a['recommended_merges']:
 ids=proposal['item_ids'];assert len(ids)==len(set(ids)) and proposal['keep_id'] in ids
 assert not seen.intersection(ids),'Overlapping proposed merge groups'
 seen.update(ids)
 assert set(proposal['source_entry_ids'])=={e for i in ids for e in known[i]['sources']}
for record in a['recommended_merges']+a['links_not_merges']:
 assert set(record['item_ids'])<=set(known)
 for loc in record['passages_read']:
  lines=(WS/loc['file']).read_text().splitlines()
  for start,end in loc['lines']: assert 1<=start<=end<=len(lines),(record,loc)
events=[]
for item_id in sorted({i for r in a['recommended_merges']+a['links_not_merges'] for i in r['item_ids']},key=lambda s:int(s.split('-')[-1])):
 related=[r for r in a['recommended_merges']+a['links_not_merges'] if item_id in r['item_ids']]
 decisions=[r.get('proposal_id',r.get('decision_id')) for r in related]
 outcomes=[r['rationale'] for r in related]
 events.append({'statement_id':item_id,'date':'2026-11-19',
  'who':a['reviewer'],'type':'used and rechecked in this run',
  'outcome':'Manual cross-package comparison of the item and cited actual manuscript passages. '+ ' | '.join(outcomes),
  'artifact':'work/outputs/cross_merge_proposals.json: '+', '.join(decisions),
  'scope':'Text and mathematical-identity comparison; no new proof certification or ink decision.'})
with (OUT/'cross_merge_check_events.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t');w.writeheader();w.writerows(events)
result={'date':'2026-11-19','recommended_merge_groups':len(a['recommended_merges']),
 'retired_item_ids':[i for r in a['recommended_merges'] for i in r['item_ids'] if i!=r['keep_id']],
 'link_only_comparisons':len(a['links_not_merges']),'comparison_events':len(events),
 'source_bounds_and_entry_unions':'passed','semantic_decisions':'Manually authored; not inferred by this validator.'}
(OUT/'cross_merge_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
