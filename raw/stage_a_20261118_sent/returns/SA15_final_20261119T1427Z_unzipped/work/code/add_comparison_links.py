"""Serialize manually reviewed relations that must not become identity merges."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1]
items={};probs={};claims={}
for folder,pref in [('cotes5_6','P56'),('cotes6_7','P67'),('root_review','P78')]:
 for k,dest in [('items',items),('problems',probs),('claims',claims)]:
  paths=[W/folder/(k+'.json')] if pref!='P78' else [W/folder/(k+'_c7.json'),W/folder/(k+'_c8.json')]
  for p in paths:
   for x in json.loads(p.read_text()):dest[x['id']]=x
rows=[
 ('cote6:007 line1551','cote7:071–072 lines201–211',
  'Categorical crystal/stratification comparison and its flat-coherent weakening are related to, but distinct from, the later comparison of ambient site cohomology.',
  ['P56-I106','P78-I010'],['P56-P021','P78-P003']),
 ('cote6:018–019 lines1743–1751','cote7:015–017 lines1077–1133',
  'Successive failures of the ordinary non-PD programme. Field-level unit coefficients and a proposed derived category of quasi-coherent crystals differ from the later W(k)-valued inverse-limit comparison with a lift.',
  ['P56-I133','P56-I134'],['P56-P028','P67-P018']),
 ('cote6:019–020 lines1759–1767','cote7:051–052 lines1763–1784',
  'Curvature/integrability, the complete Leray spectral sequence, and construction/descent of the global derived Gauss–Manin connection are separate proof obligations; Katz–Oda Theorems1 and3 address different parts.',
  ['P56-I135'],['P56-P029','P56-P030','P67-P031']),
 ('cote5:037 lines1007–1032','cote7:024,026 lines1269–1274,1309–1316',
  'Ordinary local/formal Poincaré examples and the alleged cusp Betti discrepancy share an Euler-homotopy test, but have different hypotheses and conclusions.',
  ['P56-I053','P56-I054'],['P56-P014','P67-P021'])
]
out=[]
def values(x,key):
 if isinstance(x,dict):
  yield from x.get(key,[])
  for k,v in x.items():
   if k!=key:yield from values(v,key)
 elif isinstance(x,list):
  for v in x:yield from values(v,key)
for a,b,what,its,ps in rows:
 assert all(x in items for x in its)
 assert all(x in probs for x in ps)
 its=list(its)
 for pid in ps:
  its+=list(values(probs[pid],'items'))
  for cid in values(probs[pid],'claims'):its+=claims[cid]['items']
 src=sorted({s for i in set(its) for s in items[i]['sources']})
 out.append({'kind':'folder','from':a,'to':b,'what':what,
  'evidence':'Both exact transcription passages were independently reread in the global merge audit; see work/global_audit/merge_audit.tsv. Distinct problem IDs: '+', '.join(ps)+'.',
  'note_ids':';'.join(src)})
with (W/'global_audit/comparison_links.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(out)
print(json.dumps({'checked_distinction_links':len(out)}))
