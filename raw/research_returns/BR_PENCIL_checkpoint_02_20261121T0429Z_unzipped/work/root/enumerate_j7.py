"""Memory-bounded exhaustive orbit enumeration at j=7, target residual rank14."""
from coordinate_koszul import *
from itertools import combinations
from pathlib import Path
from collections import Counter
import json,time,math

j=7;target=14;total=math.comb(36,j)
choose=[[math.comb(x,k) for x in range(36)] for k in range(1,j+1)]
def colex(s):return sum(choose[k][x] for k,x in enumerate(s))
seen=bytearray(total);maps=group_maps();records=[];start=time.time()
for subset in combinations(range(36),j):
    if seen[colex(subset)]:continue
    orbit={tuple(sorted(mp[i] for i in subset)) for mp in maps}
    for s in orbit:seen[colex(s)]=1
    support,mats=slices(subset,-1)
    rec={'subset':list(subset),'orbit_size':len(orbit),'support':support,'families':{}}
    for fam,sg in [('det',-1),('per',1)]:
        lower=max(j,len(support),13) # proved propagation from m5=11
        certs=[]
        if lower<target:
            _,mm=slices(subset,sg)
            for p in [1,2,3]:
                mat=koszul(mm,p);c=modular_rank(mat)
                cost=math.comb(6,p)
                c.update({'p':p,'shape':list(mat.shape),'pure_cost':cost,'bound':(c['rank_mod_p']+cost-1)//cost})
                lower=max(lower,c['bound']);certs.append(c)
                if lower>=target:break
        rec['families'][fam]={'lower_bound':lower,'certificates':certs}
    records.append(rec)
    if len(records)%1000==0:
        print('orbits',len(records),'seconds',round(time.time()-start,1),flush=True)
assert sum(seen)==total
out={'j':j,'target':target,'number_of_subsets':total,'number_of_orbits':len(records),'orbit_sum':sum(x['orbit_size'] for x in records),'seconds':time.time()-start,'records':records}
assert out['orbit_sum']==total
for fam in ['det','per']:
    out[fam+'_unresolved']=[r['subset'] for r in records if r['families'][fam]['lower_bound']<target]
Path('work/root/j7_target14.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
