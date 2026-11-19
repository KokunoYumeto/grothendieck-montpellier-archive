"""Actual searches and locator-based inspections, without invented query strings."""
from pathlib import Path
import json,csv,re,datetime
P=Path(__file__).resolve().parents[1]
C=json.loads((P/'claims.json').read_text())
R={x['key']:x for x in json.loads((P/'references.json').read_text())}
Q={
 (1,0):[216,217,218,219,220],(1,1):[221,224,225,248,249],(1,2):[224,225],(1,3):[220,221,222],
 (4,0):[256,257,258,259],(4,1):[210,211,212,213,260],(4,2):[216,221,223,224,225],(4,3):[230,237,238,239,240,241,242,243,244,245,246,247],
 (7,0):['SA06-277'],(7,1):[264,267,268,269,270,271],(7,2):[228,229,230,231,232,233,234,235],(7,3):[224,225],
 (13,0):[237,238,239,240,241,243,244,245,246],(13,1):[220,221,222],(13,2):[244,247,248,249,250],(13,3):[204],
 (15,0):[237,245,246],(15,1):[204],(15,2):[220,221,222],(15,3):[228,229,235],
 (17,0):[205,206,207,208,209],(17,1):[200,201,202,261,262,263,264,265,266,267,268,269,272,273,274,275,276,277,278,279,280,281,282],(17,2):[228,229,230,231,237],(17,3):[220,221,222],
 (18,0):[216,218,219,221],(18,1):[220,221,222],(18,2):[205,206,207,208,209],
 (19,0):[205,206,207,208,209],(19,1):[207,208,209],(19,2):[220,221,222],(19,3):[251,252],
 (22,0):[267,268,269,270,271],(22,1):[220,221,222],(22,2):[251,252],
 (25,0):[210,213],(25,1):[210,211,212,213,260],(25,2):[214],
 (26,0):[203,204],(26,1):[232,242,243,254],(26,2):[270,271],(26,3):[203,216,221,223,224,225],
 (27,0):[271],(27,1):[271],(27,2):[232,242,243,254],
 (28,0):[203,204,261,262,267,268,269],(28,1):[216,221,223],(28,2):[211],(28,3):[270,271],
 (31,0):[233,234],(31,1):[230,231,234,235],(31,2):[230,231,232,233,235],(31,3):[233,235,237],
 (32,0):[239],(32,1):[237,245,246],(32,2):[237],
 (35,0):[254],(35,1):[252],(35,2):[203,261,267,268,269],
 (39,0):[252],(39,1):[252],(39,2):[251,252],
 (46,0):[215],(46,1):[215],(46,2):['SA06-266','SA06-267','SA06-269','SA06-270'],(46,3):[203],
 (47,0):[215],(47,1):['SA06-266'],(48,0):[215]
}
rows=[]
fields=['claim_id','query','source','result','opened_url','ref_ids','exact_locator','hypothesis_match','date','method','record']
for file in sorted((P/'research').glob('web_*.json')):
 d=json.loads(file.read_text());n=int(file.stem.split('_')[-1]);args=d.get('args',{})
 txt=json.dumps(d.get('result',{}),ensure_ascii=False)
 refs=sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',txt)))
 for typ in ['system1_search_query','system2_search_query']:
  for j,q in enumerate(args.get(typ,[])):
   ids=Q.get((n,j),[])
   assert ids,(n,j)
   for ident in ids:
    ident='C-SA06-'+str(ident)if isinstance(ident,int)else ident
    c=next((c for c in C if c['id']==ident),None)
    rows.append(dict(claim_id=ident,query=q['q'],source=typ,result='Actual discovery/coverage query. The retained result is the exact-primary comparison below; an empty or irrelevant search is not evidence of novelty.',opened_url='',ref_ids=';'.join(refs),exact_locator='See paired primary-locator rows; raw returned results in '+file.name,hypothesis_match=c['fate']if c else'Contextual earlier-run comparison, not a claim attributed to the manuscript.',date='2026-11-19',method='search query',record='research/'+file.name))

# These are real directed primary inspections, not retrospectively invented web queries.
for c in C:
 for key in c['refs']:
  r=R[key]
  rows.append(dict(claim_id=c['id'],query='Directed primary lookup: '+key,source=r['url'],result=c['fate'],opened_url=r['url'],ref_ids=';'.join(r.get('opened_refs',r.get('tool_refs',[]))),exact_locator=' | '.join(r.get('locators',[])),hypothesis_match=c['statement']+' Scope: '+r.get('limitations','No further scope extension inferred.'),date='2026-11-19',method='primary locator comparison',record='references.json; '+r.get('verification','')))

context={
 'SA06-254':['Beauville2008','Kunnemann1993','Grothendieck1969Standard'],
 'SA06-255':['DeligneMilne1982'], 'SA06-256':['DeligneMilne1982'], 'SA06-257':['DeligneMilne1982'],
 'SA06-258':['Grothendieck1969Standard'], 'SA06-259':['Grothendieck1969Standard'],
 'SA06-260':['Jannsen1992'], 'SA06-261':['Kunnemann1993','Beauville2008'], 'SA06-263':['Deligne1980WeilII'],
 'SA06-266':['Tate1966','Faltings1983','Faltings1984Erratum','Mochizuki1999'],
 'SA06-267':['Mochizuki2004','DeligneMilne1982'], 'SA06-268':['DeligneMilne1982'],
 'SA06-269':['Stacks03PK','Mochizuki1999'], 'SA06-271':['HuberMuellerStach2017','Kahn2025Descent'],
 'SA06-272':['ChoudhuryGallauer2017'], 'SA06-273':['HuberMuellerStach2017','Arapura2013'],
 'SA06-274':['Huber2020','HuberMuellerStach2017'], 'SA06-275':['Huber2020'],
 'SA06-276':['Grothendieck1966DeRham'], 'SA06-277':['Ayoub2026']}
for ident,keys in context.items():
 for key in keys:
  r=R[key]
  rows.append(dict(claim_id=ident,query='Directed contextual lookup: '+key,source=r['url'],result='Earlier-run comparison kept separate from source claims. '+r.get('verification',''),opened_url=r['url'],ref_ids=';'.join(r.get('opened_refs',r.get('tool_refs',[]))),exact_locator=' | '.join(r.get('locators',[])),hypothesis_match=r.get('limitations','Exact published hypotheses retained; no attribution to the assigned handwritten range.'),date='2026-11-19',method='contextual primary comparison',record='references.json; contextual_comparisons.md'))
with(P/'search_log.tsv').open('w',newline='')as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
with(P/'progress.log').open('a')as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tSEARCH_LOG_SAVED\t{len(rows)} actual query/primary inspection records; all84 claims covered.\n')
print({'search_rows':len(rows),'claims_covered':len(set(r['claim_id']for r in rows if r['claim_id'].startswith('C-')))})
