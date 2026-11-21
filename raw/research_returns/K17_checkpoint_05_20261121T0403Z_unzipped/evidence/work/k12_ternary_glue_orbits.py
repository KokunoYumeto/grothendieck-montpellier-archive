from pathlib import Path
import json
# Reuse definitions without the exploratory exhaustive loop.
ns={}
exec(Path('work/k12_ternary_glue_explore.py').read_text().split('records=ast.literal_eval')[0],ns)
autos,SHIFT,SIGN=ns['autos'],ns['SHIFT'],ns['SIGN']
product,dot=ns['product'],ns['dot']
data=json.loads(Path('work/k12_ternary_glue_explore.json').read_text());out=[]
for rec in data['records']:
 B=[tuple(b)for b in rec['B']];G=autos(B);shifts=[tuple(dot(lam,b)%3 for b in B)for lam in product(range(3),repeat=3)]
 left={(tuple(s['state']),s['zero_count'],s['zero_weight'])for s in rec['survivors']};orbits=[]
 while left:
  state,z,zw=min(left);orbit=set()
  for A,perm,signs in G:
   signed=[None]*len(B)
   for j,m in enumerate(state):signed[perm[j]]=SIGN[m,signs[j]]
   for vals in shifts:orbit.add((tuple(SHIFT[m,t]for m,t in zip(signed,vals)),z,zw))
  assert orbit<=left
  left-=orbit;orbits.append({'state':state,'zero_count':z,'zero_weight':zw,'orbit_size':len(orbit)})
 print(rec['record'],len(orbits),orbits,flush=True)
 out.append({'record':rec['record'],'B':B,'orbits':orbits})
Path('work/k12_ternary_glue_orbits.json').write_text(json.dumps(out,indent=2)+'\n')
