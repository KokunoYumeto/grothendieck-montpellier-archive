"""Structural validation of the manually selected provenance records."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]

def validate(owner):
 p=ROOT/'SA23_work/parts'/owner
 def load(name):return json.loads((p/name).read_text())
 ps=load('problems.json');eds=load('editorial_tasks.json');audit=load('problem_origin_audit.json')
 cs=load('claims.json');its=load('items.json');dirs=load('directions.json');edirs=load('editorial_directions.json')
 ii={x['id'] for x in its};ci={x['id'] for x in cs};pi={x['id'] for x in ps};ei={x['id'] for x in eds}
 original={x['original_id'] for x in audit['decisions']}
 assert len(ps)+len(eds)==audit['total_input_count']
 assert pi|{x['original_id'] for x in eds}==original
 assert not pi&{x['original_id'] for x in eds}
 assert len(ei)==len(eds)
 quote_count=0
 for q in ps+eds:
  assert q['source_cues'] and q['origin'] and q['origin_reason']
  assert all(x['claim'] in ci for x in q['occurrences'])
  for x in q['source_cues']:
   lo,hi=x['physical_lines'];ls=(ROOT/x['source']).read_text().splitlines()
   assert 1<=lo<=hi<=len(ls)
   assert x['verbatim']=='\n'.join(ls[lo-1:hi]),q['id']+' altered quote'
   quote_count+=1
 for q in ps:
  assert q['record_type']=='authorial problem' and q['count_as_authorial_problem'] is True
  assert q['source_question_certainty'] and q['worth']
 for q in eds:
  assert q['record_type']=='editorial task' and q['count_as_authorial_problem'] is False
  assert q['original_id'].startswith('MP-') and q['id'].startswith('ED-')
  assert 'as_he_states' not in q and q['cue_or_reason']
 for path,digest in audit['source_hashes'].items():
  assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path+' changed source'
 for d in dirs+edirs:
  assert set(d['items'])<=ii and set(d['claims'])<=ci and set(d['problems'])<=pi
  assert set(d.get('editorial_tasks',[]))<=ei
 for d in dirs:assert d['items'] and d['claims'] and d['problems']
 for d in edirs:assert d['record_type']=='editorial follow-up outside Stage6'
 return {'original_tasks':len(original),'authorial_problems':len(ps),'editorial_tasks':len(eds),
         'ranked_directions':len(dirs),'editorial_directions':len(edirs),
         'literal_quote_checks':quote_count,
         'uncertain_source_questions':sum(q.get('source_question_certainty','').startswith('uncertain') for q in ps),
         'result':'PASS; exact audit partition, literal source quotes, source hashes and direction provenance verified'}

if __name__=='__main__':
 for o in ['bt','spaces']:print(o,json.dumps(validate(o)))
