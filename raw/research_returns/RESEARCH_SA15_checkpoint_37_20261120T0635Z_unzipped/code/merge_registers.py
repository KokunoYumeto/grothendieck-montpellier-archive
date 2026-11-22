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
 for m in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|question|definition|example)\}(.*?)\\end\{\1\}',t,re.S):
  block=m[2]; lm=re.search(r'\\label\{([^}]+)\}',block)
  if not lm:continue
  lab=lm[1]
  if lab in labels:continue
  labels.add(lab); status='Proved under stated hypotheses'
  if m[1]=='question':status='Open'
  if m[1]=='definition':status='Definition: conventions only'
  sm=re.search(r'\\status\{([^}]+)\}',block)
  if sm:status=sm[1]
  if 'audit requested' in block or 'audit pending' in block:status='Candidate proof; independent audit pending'
  cleaned=re.sub(r'\\label\{[^}]+\}','',block)
  cleaned=re.sub(r'\\status\{[^}]+\}','',cleaned)
  cleaned=' '.join(cleaned.split())
  pages='4:8--12'
  if f.stem=='A_foundations':pages='4:2--9'
  elif f.stem in ['A_coherent_counterexample','A_surface_counterexample','A_integral_counterexample','A_injectivity_counterexample','A_injectivity_degrees','A_product_degrees']:pages='4:4--6;4:8'
  elif f.stem=='A_lifting':pages='4:10--11'
  elif f.stem=='B':pages='9:10--14;100:48--53'
  elif f.stem=='C':
   pages='100:3--17'
   if 'descent' in lab or lab in ('prop:C-RD1','prop:C-RD2'):pages='100:23--25'
   if any(x in lab for x in ['C-RD7','C-RD8','C-RD9','C-RD10']):pages='100:17'
  elif f.stem=='F':
   match=re.search(r'(?:DE-quote-([DE])(\d+)|DE-R(\d+))',lab)
   if match and match[1]:
    item=match[1]+'.'+match[2]
    pages={'D.1':'8:81','D.2':'8:78--81','E.1':'5:39--41','E.2':'6:6--7','E.3':'7:16--17','E.4':'7:70--72','E.5':'7:24','E.6':'7:42--43','E.7':'8:48--50','E.8':'9:22','E.9':'9:24--29','E.10':'7:17--19','E.11':'6:14'}[item]
   elif match:pages={'7':'9:16--18','8':'9:5--8','9':'6:22--27','10':'7:16--17'}[match[3]]
   else:pages='Manuscript wording and source-access record'
  elif f.stem=='D':
   heads=re.findall(r'\\subsection\{([DE]\.\d+)\.',t[:m.start()])
   item=heads[-1] if heads else 'D.1'
   pages={'D.1':'8:81','D.2':'8:78--81','E.1':'5:39--41','E.2':'6:6--7','E.3':'7:16--17','E.4':'7:70--72','E.5':'7:24','E.6':'7:42--43','E.7':'8:48--50','E.8':'9:22','E.9':'9:24--29','E.10':'7:17--19','E.11':'6:14'}[item]
  proof=t[m.end():]
  stop=re.search(r'\\(?:begin\{(?:theorem|proposition|lemma|corollary|question)\}|subsection)',proof)
  if stop:proof=proof[:stop.start()]
  refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',block+proof)
  cites=re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',block+proof)
  depends=sorted(set(refs+[key.strip() for group in cites for key in group.split(',')]))
  rows.append(dict(id=lab,statement=cleaned,status=status,where_proved=f'{f.relative_to(w)}; {m[1].title()} {nums.get(lab,"pending")}',depends_on='; '.join(depends) or 'Self-contained proof in the indicated section',manuscript_pages_settled=pages,notes='Exact hypotheses in statement; independent/targeted/computational audit distinctions are recorded in CHECK_EVENTS.tsv.'))
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
for f in sorted((w/'agents/monodromy').glob('CHECK_EVENTS_post_CP*.tsv')):
 for r in csv.DictReader(f.open(),delimiter='\t'):
  typ='artifact verification' if 'actual-rendered-pages' in r['status'] else 'targeted proof check'
  events.append(dict(statement_id=r['event_id'],date=r['utc'],
    who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root/monodromy; inherited effort',
    type=typ,outcome=r['status']+'; '+r['notes']))
with (w/'CHECK_EVENTS.tsv').open('w') as f:
 wr=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');wr.writeheader();wr.writerows(events)
print(len(rows),'numbered statements;',len(events),'check events')
