import csv,pathlib,re
base=pathlib.Path(__file__).resolve().parent.parent; w=base/'work'; out=base/'deliverable'
fields=['statement_id','date','who','type','outcome','how','model','effort','run']
rows=[]
alias={'ROOT-KM-2D':'P-F1','ROOT-POSITIVE-RATIONAL-SELECTOR':'P-F2'}
for p in sorted(w.glob('*checks.tsv')):
 for row in csv.DictReader(p.open(),delimiter='\t'):
  r={k:row.get(k,'') for k in fields}
  old=r['statement_id'];r['statement_id']=alias.get(old,old)
  if old!=r['statement_id']:r['how']+=' Original check identifier: '+old+'.'
  if not r['model']:r['model']='GPT-6 Astra Pro'
  if not r['effort']:r['effort']='inherited/not exposed by runtime'
  if not r['run']:
   ma=re.search(r'/root(?:/[A-Za-z0-9_]+)?',r['who']);r['run']=ma.group() if ma else 'See who field'
  rows.append(r)
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)
qfields=['id','source_and_locator','question','state','finding_ids_or_counterexample','current_gate']; qs=[]
for p in sorted(w.glob('*questions.tsv')):
 for row in csv.DictReader(p.open(),delimiter='\t'):
  state=row.get('state',''); q={k:row.get(k,'') for k in qfields}
  q['source_and_locator']=row.get('source_and_locator',row.get('source_locator',''))
  if not q['finding_ids_or_counterexample']:q['finding_ids_or_counterexample']='; '.join(dict.fromkeys(re.findall(r'(?:P-F\d+|P-K\d+|PLE-F\d+|PL-\d+|B[3457]\.\d+|C-[A-Z]+-\d+)',state)))
  if not q['current_gate'] and re.search(r'gate|open|not settled|unresolved',state,re.I):q['current_gate']=state
  qs.append(q)
with (out/'QUESTIONS.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=qfields,delimiter='\t');wr.writeheader();wr.writerows(qs)
print({'check_events':len(rows),'questions':len(qs)})
