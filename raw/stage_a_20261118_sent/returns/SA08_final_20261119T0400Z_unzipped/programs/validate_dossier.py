"""Check referential integrity and coverage of already-authored adjudications.
No checks here infer a mathematical verdict from headings or source keywords.
"""
from pathlib import Path
import collections,csv,json,re,hashlib
R=Path(__file__).resolve().parents[1];O=R/'outputs'
def j(n):return json.loads((O/n).read_text())
def t(p):return list(csv.DictReader(p.open(newline=''),delimiter='\t'))
entries=t(O/'SA08_entries.tsv');source=t(R/'sources/notes/NOTES_INDEX.tsv')
items=j('SA08_items.json');claims=j('SA08_claims.json');problems=j('SA08_problems.json')
events=t(O/'CHECK_EVENTS.tsv');aliases=t(O/'SA08_id_aliases.tsv')
errors=[];warnings=[]
def check(cond,msg):
 if not cond:errors.append(msg)
def ids(a):return [x['id'] for x in a]
I={x['id']:x for x in items};C={x['id']:x for x in claims};P={x['id']:x for x in problems}
for name,a in [('items',items),('claims',claims),('problems',problems)]:
 check(len(ids(a))==len(set(ids(a))),name+': duplicate IDs')
sourceids=[x['entry_id'] for x in source];entryids=[x['entry_id'] for x in entries]
check(len(entries)==437,'Expected437 verdict rows')
check(collections.Counter(sourceids)==collections.Counter(entryids),'Verdict IDs differ from NOTES_INDEX')
for e in entries:
 check(e['item_id'] in I,'Unknown primary item '+e['item_id'])
 if e['item_id'] in I:check(e['entry_id'] in I[e['item_id']]['sources'],'Primary item lacks source '+e['entry_id'])
 check(bool(e['reason'].strip()),'Empty verdict reason '+e['entry_id'])
 check(e['verdict'] in ['kept','corrected','withdrawn','rests on a misreading'] or e['verdict']=='merged into '+e['item_id'],'Invalid verdict '+str(e))
fields={
 'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
 'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
 'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for name,a in [('items',items),('claims',claims),('problems',problems)]:
 for x in a:
  check(set(fields[name])<=set(x),name+' missing field '+x['id'])
  for k in (['statement','check_reason'] if name=='items' else ['statement','fate','computation','present_status'] if name=='claims' else ['title','as_he_states','plausible_today','state_of_art','why_open','worth']):
   check(bool(x.get(k)),x['id']+' empty '+k)
for x in items:
 for s in x['sources']:check(s in sourceids,x['id']+' unknown entry '+s)
for c in claims:
 check(c['class'] in 'ABCDEF' and len(c['class'])==1,c['id']+' invalid class')
 check(c['confidence'] in ['high','medium','low'],c['id']+' invalid confidence category')
 for s in c['items']:check(s in I,c['id']+' unknown item '+s)
 check('2026' in c['present_status'],c['id']+' undated present status')
for p in problems:
 for z in p['occurrences']:
  if 'claim' in z:check(z['claim'] in C,p['id']+' unknown claim '+z['claim'])

bib=(O/'SA08_references.bib').read_text();bibkeys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
verified=re.findall(r'\bnote\s*=\s*\{(verified|unverified)\}',bib)
check(len(verified)==len(bibkeys),'Every bibliography record must have a verified/unverified note')
for a in [claims,problems]:
 for x in a:
  for r in x['refs']:check(r in bibkeys,x['id']+' missing bibliography key '+r)
searches=t(O/'SA08_claim_searches.tsv')
searched={x['claim_id'] for x in searches if x['search_record'].strip()}
check(set(C)<=searched,'Claims without a recorded fate search: '+str(sorted(set(C)-searched)))

# Source-locator bounds are an editorial consistency test, not a proof check.
files={str(f.relative_to(R/'sources/texts')):f.read_text().splitlines() for f in (R/'sources/texts').rglob('*_transcription.tex')}
def locs(x):
 a=x.get('lines',[])
 if isinstance(a,list):return a
 return []
locator_checks=0
for a in [items,claims]:
 for x in a:
  for z in locs(x):
   f=z.get('file','')
   if f.startswith('notes/'):continue
   if f and f not in files:errors.append(x['id']+' source file unavailable '+f);continue
   if f:
    line=str(z.get('lines',''))
    # Numeric spans at the start or after delimiters; descriptions remain prose.
    nums=[int(v) for v in re.findall(r'(?<![A-Za-z])\b\d+\b',line)]
    if nums:
     locator_checks+=1
     check(min(nums)>=1 and max(nums)<=len(files[f]),x['id']+' out-of-bounds lines '+f+':'+line)

checked={e.get('statement_id') for e in events}
for name,d in [('item',I),('claim',C),('reference',dict.fromkeys(bibkeys))]:
 check(set(d)<=checked,'Missing '+name+' check events: '+str(sorted(set(d)-checked)))
known=set(I)|set(C)|set(P)|bibkeys|{a['original_id'] for a in aliases}
unknown=sorted({e.get('statement_id','') for e in events}-known)
if unknown:warnings.append('Event IDs outside final canonical entities (inspect retained provenance): '+str(unknown))
for e in events:
 check(all(e.get(k,'').strip() for k in ['statement_id','date','who','type','outcome']),'Incomplete check event '+str(e))

valid=set(I)|set(C)|set(P);old={a['original_id'] for a in aliases}
prose=[]
for n in ['SA08_dossier.md','SA08_directions.md']:
 s=(O/n).read_text()
 cites=re.findall(r'@([A-Za-z][A-Za-z0-9_]*)',s)
 for r in cites:check(r in bibkeys,n+' noncanonical or absent citation '+r)
 refs=set(re.findall(r'\b(?:SA08-C\d+|MP-SA08-\d+|SA08-\d+)\b',s))
 for q in refs:check(q in valid or q in old,n+' dangling entity '+q)
 prose.append({'file':n,'words':len(s.split()),'citation_occurrences':len(cites),'entity_mentions':len(refs)})
directions=(O/'SA08_directions.md').read_text();sections=re.split(r'\n## \d+\. ',directions)[1:]
for i,s in enumerate(sections,1):
 lead=s.split('\n## ',1)[0]
 for pattern,typ in [(r'\bSA08-\d+','item'),(r'\bSA08-C\d+','claim'),(r'\bMP-SA08-\d+','problem')]:
  check(bool(re.search(pattern,lead)),f'Direction{i} lacks a {typ} ID')

report={'verdict':'PASS' if not errors else 'FAIL','errors':errors,'warnings':warnings,
 'counts':{'indexed_entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(t(O/'SA08_readings.tsv')),'links':len(t(O/'SA08_links.tsv')),'project_leads':len(t(O/'SA08_project_links.tsv')),'check_events':len(events),'references':len(bibkeys),'verified_references':verified.count('verified'),'unverified_references':verified.count('unverified'),'directions':len(sections),'numeric_source_locator_checks':locator_checks},'prose':prose,
 'scope':'Structural/editorial validation only. Mathematical judgments were authored from passage readings and checked source-specific arguments; finite tests do not certify all stated theorems.'}
(O/'SA08_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
