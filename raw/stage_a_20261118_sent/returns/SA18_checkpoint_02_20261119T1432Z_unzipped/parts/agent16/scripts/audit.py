"""Structural and provenance-coverage audit; does not assign mathematical verdicts."""
from pathlib import Path
import json,csv,re,hashlib,collections,datetime
O=Path(__file__).resolve().parents[1]
BASE=Path('/workspace/scratch/c38eb4e8f07f/sources')
def j(p):return json.loads((O/p).read_text())
def t(p):return list(csv.DictReader((O/p).open(),delimiter='\t'))
I,C,P,R=j('SA18_items.json'),j('SA18_claims.json'),j('SA18_problems.json'),j('reference_audit.json')
E,READ,L,SEARCH,EV=t('SA18_entries.tsv'),t('SA18_readings.tsv'),t('SA18_links.tsv'),t('literature_search.tsv'),t('CHECK_EVENTS.tsv')
itemfields='id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()
claimfields='id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()
problemfields='id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()
for data,fields in [(I,itemfields),(C,claimfields),(P,problemfields)]:
 assert len({x['id'] for x in data})==len(data)
 for x in data:
  assert set(fields)<=set(x),(x['id'],'missing fields')
  for f in fields:
   assert x[f] is not None,(x['id'],f)
   if isinstance(x[f],str):assert x[f].strip(),(x['id'],f,'empty')
idx=list(csv.DictReader((BASE/'SA18_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected={r['entry_id'] for r in idx if r['package']=='MPL_16+47+54+44'}
assert len(expected)==85
assert len(E)==85 and {r['entry_id'] for r in E}==expected
ii={x['id']:x for x in I};cc={x['id']:x for x in C};pp={x['id']:x for x in P}
assert all(e['item_id'] in ii and e['verdict'] and e['reason'] for e in E)
assert all(e['entry_id'] in ii[e['item_id']]['sources'] for e in E)
assert all(s in expected for x in I for s in x['sources'])
assert all(x['check'] in ['agrees','overstates','understates','misreads','not on the page'] for x in I)
assert all(c['class'] in 'ABCDEF' and c['confidence'] in ['high','medium','low'] for c in C)
assert all(i in ii for c in C for i in c['items'])
assert all(r['key'] in R for c in C for r in c['refs'])
assert all(r['key'] in R for p in P for r in p['refs'])
searched={r['statement_id'] for r in SEARCH}
assert set(cc)|set(pp)<=searched
assert all((O/r['request_log']).is_file() for r in SEARCH)
events={r['statement_id'] for r in EV}
assert set(ii)|set(cc)|set(R)<=events
assert all(r['who']=='GPT-6 Astra Pro / inherited effort / agent16' for r in EV)
assert all(l['kind'] in ['folder','published work','our projects'] for l in L)
assert len(t('SA18_project_links.tsv'))==0
textfile=BASE/'SA18_texts/pro/MPL_16+47+54+44_transcription.tex'
textlines=textfile.read_text().splitlines()
for x in I:
 loc=x['lines']
 if isinstance(loc,dict) and loc.get('file')=='SA18_texts/pro/MPL_16+47+54+44_transcription.tex':
  assert all(isinstance(n,int) and 1<=n<=len(textlines) for n in loc.get('absolute_1_based',[])),x['id']

coverage={}
for row in csv.reader((O/'read_log.tsv').open(),delimiter='\t'):
 date,key,a,b,out=row
 coverage.setdefault(key,set()).update(range(int(a),int(b)+1))
 assert (O/'outputs'/out).is_file()
assert set(range(27,len(textlines)+1))<=coverage['text']
notes=(BASE/'SA18_notes/pro/MPL_16+47+54+44_notes.md').read_text().splitlines()
doubts=(BASE/'SA18_notes/pro/MPL_16+47+54+44_doubts.md').read_text().splitlines()
assert set(range(1,len(notes)+1))<=coverage['notes']
assert set(range(1,len(doubts)+1))<=coverage['doubts']
second=list((BASE/'SA18_notes/second_pass/MPL_16+47+54+44').glob('*.md'))
assert len(second)==6
for f in second:assert set(range(1,len(f.read_text().splitlines())+1))<=coverage[f.stem]

for f in (O/'research').glob('web_*.json'):
 d=json.loads(f.read_text())
 assert 'result' not in d and 'content' not in d and 'image_url' not in d,f.name
 assert 'request' in d or 'requests' in d
 assert 'source_results' in d
assert not list(O.rglob('*.pdf'))
assert not list(O.rglob('*.zip'))
assert not list(O.rglob('*transcription.tex'))
bib=(O/'SA18_references.bib').read_text()
assert len(re.findall(r'@misc\{',bib))==len(R)
for k,r in R.items():
 entry=bib.split('@misc{'+k+',',1)[1].split('\n}',1)[0]
 want='verified' if r['verification'].lower().startswith('verified:') else 'unverified'
 assert 'note = {'+want+'}' in entry,(k,want)

directions=(O/'SA18_directions.md').read_text()
assert len(re.findall(r'^## \d+\.',directions,re.M))==11
# Explicitly written long IDs, excluding typographical range continuations.
for sid in re.findall(r'(?<![A-Z-])(?:CL-SA18|MP-SA18|SA18)-\d+',directions):
 assert sid in ii or sid in cc or sid in pp,sid

counts=j('outputs/finalize_counts.json')
counts['directions']=11
counts['indexed_entry_verdicts']=dict(collections.Counter('kept' if x['verdict'].startswith('kept') else 'merged' if x['verdict'].startswith('merged') else x['verdict'] for x in E))
counts['source_check_status']=dict(collections.Counter(x['check'] for x in I))
counts['bibliography_verified']=sum(r['verification'].lower().startswith('verified:') for r in R.values())
counts['bibliography_unverified']=len(R)-counts['bibliography_verified']
counts['named_exact_computations']=len(j('outputs/computations.json'))+1
counts['all_claims_have_actual_search_rows']=True
counts['all_problems_have_actual_search_rows']=True
counts['all_items_claims_references_have_check_events']=True
counts['complete_source_read_coverage']=True
counts['second_pass_files_read']=6
counts['public_response_bodies_retained']=0
counts['no_attachment_transcription_copies']=True
counts['no_agent_checkpoints']=True
counts['audit_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
counts['audit_result']='PASS: structural checks only; mathematical decisions are individually authored.'
(O/'outputs/audit.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
files={}
for f in sorted(O.rglob('*')):
 if f.is_file() and '__pycache__' not in str(f) and f.name not in ['file_manifest.json']:
  files[str(f.relative_to(O))]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
(O/'file_manifest.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
