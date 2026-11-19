"""Structural and provenance validation; this program makes no mathematical verdicts."""
from pathlib import Path
import json,csv,re,collections,hashlib,bisect
R=Path(__file__).resolve().parents[1];W=R.parents[2]
def js(name):return json.loads((R/name).read_text())
def tsv(name):return list(csv.DictReader((R/name).open(),delimiter='\t'))
I=js('items.json');C=js('claims.json');P=js('problems.json');B=js('reference_details.json');E=tsv('entries.tsv');S=tsv('search_log.tsv');K=tsv('CHECK_EVENTS.tsv');A=tsv('readings.tsv');L=tsv('links.tsv')
source=json.loads((W/'SA14_work/research/entries_source.json').read_text())
expected={k for k in source if k.startswith('MPL_60_002-035#') or k.startswith('MPL_60_036-070#')}
assert len(expected)==139
assert len(E)==139 and {e['entry_id'] for e in E}==expected
assert len({e['entry_id'] for e in E})==len(E)
assert len(I)==93 and len(C)==167 and len(P)==16 and len(A)==53 and len(L)==24
item_ids={i['id'] for i in I};claim_ids={c['id'] for c in C};problem_ids={p['id'] for p in P};ref_ids={b['key'] for b in B}
assert len(item_ids)==len(I) and len(claim_ids)==len(C) and len(problem_ids)==len(P) and len(ref_ids)==len(B)
assert claim_ids=={f'C-SA14-{n}' for n in range(401,568)}
assert problem_ids=={f'MP-SA14-{n}' for n in range(401,417)}
all_sources=[s for i in I for s in i['sources']]
assert len(all_sources)==139 and set(all_sources)==expected and len(set(all_sources))==139
mapping={s:i['id'] for i in I for s in i['sources']}
assert all(e['item_id']==mapping[e['entry_id']] for e in E)
verdicts={'kept','merged','corrected','withdrawn','rests on a misreading'}
assert all(e['verdict'] in verdicts and e['reason'].strip() for e in E)
kinds={'conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other'}
checks={'agrees','overstates','understates','misreads','not on the page'}
item_fields={'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'}
claim_fields={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'}
problem_fields={'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
assert all(item_fields<=set(i) and i['kind'] in kinds and i['check'] in checks for i in I)
statuses={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
assert all(claim_fields<=set(c) and set(c['items'])<=item_ids and c['class'] in 'ABCDEF' and c['status_on_pages'] in statuses for c in C)
assert all(problem_fields<=set(p) for p in P)
assert all(set(c['refs'])<=ref_ids and c['confidence'] in {'high','medium','low'} for c in C)
assert all(set(p['refs'])<=ref_ids for p in P)
search={s['search_id']:s for s in S}
for c in C:
 assert c['search_events'] and set(c['search_events'])<=set(search)
 for sid in c['search_events']:assert c['id'] in search[sid]['claim_ids'].split(';')
for sid,s in search.items():
 assert set(s['claim_ids'].split(';'))<=claim_ids
 for cid in s['claim_ids'].split(';'):assert sid in next(c['search_events'] for c in C if c['id']==cid)
event_ids={e['statement_id'] for e in K}
assert item_ids|claim_ids|problem_ids|ref_ids<=event_ids
assert all('effort not exposed' in e['who'] for e in K)
assert all(c['id'] in {e['statement_id'] for e in K if e['type'].startswith('refuted')} for c in C if c['status_on_pages']=='false as stated')
allowed_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(e['type'] in allowed_types for e in K)
files={p.name:p for p in (W/'sources/SA14_texts/pro').glob('MPL_60*tex')}
scan_maps={};lengths={}
for name,path in files.items():
 lines=path.read_text().splitlines();lengths[name]=len(lines)
 scan_maps[name]=[(n,int(m.group(1))) for n,line in enumerate(lines,1) if (m:=re.match(r'\\scanpage\{(\d+)\}',line))]
for rec in I+C:
 for loc in rec['lines']:
  if ':' not in loc:continue
  name,numbers=loc.split(':',1)
  if name not in files:continue
  for part in numbers.split(','):
   nums=list(map(int,re.findall(r'\d+',part)))
   if not nums:continue
   lo=nums[0];hi=nums[1] if len(nums)>1 else lo
   assert 1<=lo<=hi<=lengths[name],(rec['id'],loc)
   scan=scan_maps[name][bisect.bisect_right(scan_maps[name],(lo,999))-1][1]
   assert scan in rec['scans'],(rec['id'],loc,scan,rec['scans'])
for link in L:
 assert link['kind'] in {'folder','published work','our projects'}
 assert link['status']=='both endpoints read'
 assert set(link['note_ids'].split(';'))<=expected
readlog=tsv('read_log.tsv');coverage={}
for row in readlog:
 coverage.setdefault(row['file'],set()).update(range(int(row['from_line']),int(row['to_line'])+1))
for prefix,folder,suffix in [('MPL_60_002-035','SA14_texts/pro','_transcription.tex'),('MPL_60_036-070','SA14_texts/pro','_transcription.tex'),('MPL_60_002-035','SA14_notes/pro','_notes.md'),('MPL_60_036-070','SA14_notes/pro','_notes.md'),('MPL_60_002-035','SA14_notes/pro','_doubts.md'),('MPL_60_036-070','SA14_notes/pro','_doubts.md')]:
 name=f'sources/{folder}/{prefix}{suffix}';n=len((W/name).read_text().splitlines())
 assert set(range(1,n+1))<=coverage[name],(name,'missing logged ranges')
out=(R/'outputs/calculations.txt').read_text()
assert 'ALL ASSERTIONS PASSED.' in out
for n in range(1,26):assert f'CALC-{n:02d}' in out
for c in C:
 for calc in re.findall(r'CALC-\d+',c['computation']):assert calc in out,(c['id'],calc)
required=['entries.tsv','items.json','claims.json','problems.json','readings.tsv','links.tsv','directions.md','references.bib','CHECK_EVENTS.tsv','search_log.tsv','read_log.tsv','synthesis.md','proof_notes.md','literature_notes.md','primary_read_log.tsv','project_leads.tsv','progress.log']
assert all((R/f).is_file() and (R/f).stat().st_size>0 for f in required)
assert not list(R.rglob('*.pdf')),'Whole external PDFs must remain outside deliverables.'
print('PASS:139 exact source IDs; individual verdict/item bijection;93 items;167 claims;16 problems.')
print('PASS: all required schemas, enums, item references, bibliographic keys and claim-search mappings.')
print('PASS: all claims/items/problems/references have truthful event records; events=',len(K))
print('PASS: all physical claim/item line ranges exist and their starts match declared scans.')
print('PASS: read-log ranges cover every physical line of both notes, both doubts and both transcriptions.')
print('PASS:25 computation sections and final success marker; no external PDF in the part archive.')
print('COUNTS verdicts',dict(collections.Counter(e['verdict'] for e in E)))
print('COUNTS classes',dict(collections.Counter(c['class'] for c in C)))
print('COUNTS statuses',dict(collections.Counter(c['status_on_pages'] for c in C)))
print('COUNTS bibliography',dict(collections.Counter(b['note'] for b in B)))
print('COUNTS readings',len(A),'links',len(L),'project groups',len(tsv('project_leads.tsv')),'search groups',len(S))
print('SHA256 calculations.py',hashlib.sha256((R/'scripts/calculations.py').read_bytes()).hexdigest())
print('SHA256 calculations.txt',hashlib.sha256((R/'outputs/calculations.txt').read_bytes()).hexdigest())
print('Structural validation does not substitute for the separately documented reading, proofs and source matches.')
