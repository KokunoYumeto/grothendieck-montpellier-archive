#!/usr/bin/env python3
"""Structural coverage/integrity checks; no generated mathematical judgments."""
import json,csv,re,collections,hashlib
from pathlib import Path
W=Path('/workspace/scratch/26604d0a9a98/work/cotes6_7');ROOT=W.parents[1]
def rows(f):
 with (W/f).open() as x:return list(csv.DictReader(x,delimiter='\t'))
items=json.loads((W/'items.json').read_text());claims=json.loads((W/'claims.json').read_text());problems=json.loads((W/'problems.json').read_text());refs=json.loads((W/'reference_evidence.json').read_text());entries=rows('supplementary_entries.tsv');checks=rows('check_events.tsv');mapping=rows('search_by_claim.tsv')
errors=[]
def test(cond,msg):
 if not cond:errors.append(msg)
required={'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
 test(len({r['id'] for r in data})==len(data),name+' duplicate id')
 for r in data:
  test(all(k in r for k in required[name]),name+' missing required field '+r['id'])
  test(all(r[k] is not None and r[k]!='' for k in required[name]),name+' empty required field '+r['id'])
pkg='MPL_6_038-067+7_001-060';expected={f'{pkg}##{i}' for i in range(1,256)}
test({e['entry_id'] for e in entries}==expected,'supplementary coverage not1..255')
test(len(entries)==255,'supplementary duplicate row')
test(collections.Counter(s for i in items for s in i['sources'])==collections.Counter(expected),'note sources not assigned exactly once')
ii={i['id'] for i in items};cc={c['id'] for c in claims};rr={r['key'] for r in refs}
for c in claims:
 test(set(c['items'])<=ii,'bad claim item '+c['id'])
 test(set(c['refs'])<=rr,'missing claim bibliography '+c['id'])
 test(c['class'] in 'ABCDEF','bad fate class '+c['id'])
 test(bool(c['search_history']),'unsearched claim '+c['id'])
 test(c['origin'] in ['manuscript claim','present-run refinement; not an additional assertion by Grothendieck'],'missing origin '+c['id'])
for p in problems:
 test(set(p['refs'])<=rr,'missing problem bibliography '+p['id'])
 for o in p['occurrences']:test(set(o['claims'])<=cc,'bad problem claim '+p['id'])
for l in rows('links.tsv'):test(set(l['note_ids'].split(';'))<=expected,'unknown link note')
for e in entries:test(e['item_id'] in ii,'bad entry item')
test({m['claim_id'] for m in mapping}==cc,'claim search mapping incomplete')
test(all(m['query_ids'] for m in mapping),'claim without actual query ids')
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
for e in checks:
 test(e['statement_id'] in ii|cc|rr,'unknown check id '+e['statement_id'])
 test(e['type'] in allowed,'bad check type '+e['type'])
 if e['type'].startswith('refuted'):
  ids=re.findall(r'P67-C\d{3}',e['outcome']);test(bool(ids) and all(s in cc for s in ids),'missing refined claim id')
test(all(r['fields'].get('note')=='verified' and r['evidence'] for r in refs),'unverified reference marked verified')
supp=json.loads((W/'supplementary_root_claims.json').read_text())
test(len(supp)==1 and supp[0]['id']=='P78-C071','root supplement id/count')
for s in supp:
 test(all(k in s for k in required['claims']),'root supplement fields')
 test(set(s['refs'])<=rr,'root supplement reference missing')
 test(s['origin']=='present-run refinement' and s['parent']=='P78-C035','root supplement attribution')
test(sum(c['origin']=='manuscript claim' for c in claims)==75,'manuscript claim count differs')
test(sum(c['origin'].startswith('present-run') for c in claims)==5,'refinement count differs')
source=ROOT/'sources/SA15_texts/pro'/f'{pkg}_transcription.tex';lines=source.read_text().splitlines();log=rows('source_read_log.tsv');covered=set()
for r in log:
 if r['file']==f'SA15_texts/pro/{pkg}_transcription.tex':covered.update(range(int(r['line_start']),int(r['line_end'])+1))
test(set(range(2,len(lines)+1))<=covered,'transcription page-span log gap')
summary={'ok':not errors,'errors':errors,'counts':{'items':len(items),'manuscript_claims':75,'present_run_refinements':5,'problems':len(problems),'supplemental_entries':len(entries),'readings':len(rows('readings.tsv')),'links':len(rows('links.tsv')),'references':len(refs),'query_rows':len(rows('query_log.tsv')),'check_events':len(checks)},'verdicts':dict(collections.Counter(e['verdict'] for e in entries)),'manuscript_classes':dict(collections.Counter(c['class'] for c in claims if c['origin']=='manuscript claim')),'input_transcription_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'narrative_words':len((W/'narrative.md').read_text().split())}
(W/'outputs/validation.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));raise SystemExit(bool(errors))
