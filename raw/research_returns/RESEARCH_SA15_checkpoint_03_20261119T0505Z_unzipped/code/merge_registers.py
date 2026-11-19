from pathlib import Path
import re,json,csv
w=Path(__file__).resolve().parents[1]
root_events=w/'notes/root_check_events.tsv'
if not root_events.exists():root_events.write_text((w/'CHECK_EVENTS.tsv').read_text())
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
rows=json.loads((w/'notes/root_results.json').read_text()); labels={r['label'] for r in rows}
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
for f in (w/'sections').glob('*.tex'):
 t=f.read_text()
 for m in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|question)\}(.*?)\\end\{\1\}',t,re.S):
  block=m[2]; lm=re.search(r'\\label\{([^}]+)\}',block)
  if not lm:continue
  lab=lm[1]
  if lab in labels:continue
  labels.add(lab); status='Proved under stated hypotheses'
  if m[1]=='question':status='Open'
  if m[1]=='remark':status='Verified observation'
  if 'audit requested' in block or 'audit pending' in block:status='Candidate proof; independent audit pending'
  cleaned=re.sub(r'\\label\{[^}]+\}','',block)
  cleaned=re.sub(r'\\status\{[^}]+\}','',cleaned)
  cleaned=' '.join(cleaned.split())
  rows.append(dict(id=lab,statement=cleaned,status=status,where_proved=f'{f.relative_to(w)}; {m[1].title()} {nums.get(lab,"pending")}',depends_on='See proof and citations',manuscript_pages_settled='See item mapping in report',notes='Proof incorporated; targeted audit state in CHECK_EVENTS.tsv.'))
for r in rows:
 if 'label' in r:r['where_proved']+='; numbered '+nums.get(r['label'],'pending')
with (w/'RESEARCH_SA15_results.csv').open('w') as f:
 wr=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');wr.writeheader();wr.writerows(rows)
events=list(csv.DictReader(root_events.open(),delimiter='\t'))
for folder in ['monodromy','reduction_descent','obstructions_crystals']:
 f=w/'agents'/folder/'CHECK_EVENTS.tsv'
 for r in csv.DictReader(f.open(),delimiter='\t'):
  if folder=='monodromy':
   typ={'proof':'targeted proof check','source-proof-check':'used and rechecked in this run','computation':'computation or formal certificate'}.get(r['type'],r['type'])
   events.append(dict(statement_id=r['statement_id'],date=r['date'],who=r['who'],type=typ,outcome=r['outcome']))
  elif folder=='reduction_descent':events.append(dict(statement_id=r['id'],date=r['timestamp_utc'],who='GPT-6 Astra (OpenAI); /root/reduction_descent; inherited effort',type='computation or formal certificate' if 'COMPUTED' in r['status'] else 'targeted proof check',outcome='; '.join((r.get(k,'') or '') for k in ['status','claim','check','artifact'])))
  else:events.append(dict(statement_id=r['item'],date=r['utc'],who='GPT-6 Astra (OpenAI); /root/obstructions_crystals; inherited effort',type='computation or formal certificate' if 'comput' in r['kind'] else 'targeted proof check',outcome='; '.join((r.get(k,'') or '') for k in ['input','method','result','artifact'])))
with (w/'CHECK_EVENTS.tsv').open('w') as f:
 wr=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');wr.writeheader();wr.writerows(events)
print(len(rows),'numbered statements;',len(events),'check events')
