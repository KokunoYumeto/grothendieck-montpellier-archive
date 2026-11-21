"""Build finite characteristic-zero global per7 data, with named prolongation gates."""
from pathlib import Path
import sys,json,math,time
import numpy as np
from coordinate_koszul import slices,koszul,modular_rank
from weighted_koszul import blocks
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from build_det7_certificate import determinant_mod
HERE=Path(__file__).resolve().parent

def main():
 source=json.loads((HERE/'j7_target14.json').read_text())['records']
 bdata={tuple(r['subset']):r for r in json.loads((HERE/'j7_per_support_koszul.json').read_text())['records']}
 deps={}
 for label,sets in {
 'P-13':[[0,1,2,3,4,6,12],[0,1,2,3,6,7,8],[0,1,2,6,7,8,18],[0,1,2,6,7,18,20],[0,1,3,6,7,9,14]],
 'P-16':[[0,1,2,3,6,7,9],[0,1,2,3,6,7,18],[0,1,3,6,7,15,21]],
 'P-15':[[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]],
 'P-19':[[0,1,2,6,7,18,19]]}.items():
  for S in sets:deps[tuple(S)]=label
 results=[];start=time.time()
 for raw in source:
  if len(raw['support'])>=14:continue
  S=raw['subset'];support,mats=slices(S,1)
  rec={'subset':S,'support':support,'orbit_size':raw['orbit_size']}
  candidates=[c for c in raw['families']['per']['certificates'] if c['bound']>=14]
  if candidates:
   c=min(candidates,key=lambda c:13*c['pure_cost']+1);n=13*c['pure_cost']+1
   rows,cols=c['rows'][:n],c['cols'][:n];M=koszul(mats,c['p']);value=determinant_mod(M[np.ix_(rows,cols)]);assert value
   rec.update(type='A_koszul',p=c['p'],cost=c['pure_cost'],rows=rows,cols=cols,minor_order=n,determinant_mod_p=value,lower_bound=14)
  elif tuple(S) in bdata and any(c['bound']>=14 for c in bdata[tuple(S)]['certificates']):
   c=next(c for c in bdata[tuple(S)]['certificates'] if c['bound']>=14);bc=[];total=0
   for w,rows,cols,M in blocks(S,1,c['p']):
    r=modular_rank(M);n=r['rank_mod_p']
    if not n:continue
    value=determinant_mod(M[np.ix_(r['rows'],r['cols'])]);assert value
    bc.append({'weight':w,'rows':[rows[i] for i in r['rows']],'cols':[cols[i] for i in r['cols']],'size':n,'determinant_mod_p':value});total+=n
   assert total>13*c['cost']
   rec.update(type='B_koszul',p=c['p'],cost=c['cost'],rank_lower_bound=total,blocks=bc,lower_bound=14)
  else:rec.update(type='prolongation',finding=deps[tuple(S)],lower_bound=14)
  results.append(rec)
  if len(results)%100==0:print('records',len(results),'seconds',time.time()-start,flush=True)
 out={'n':4,'b':2,'j':7,'prime':1000003,'field_scope':'characteristic zero','all_coordinate_subsets':math.comb(36,7),'low_support_orbits':len(results),'low_support_subsets':sum(r['orbit_size'] for r in results),'records':results,'prolongation_dependencies':['P-13','P-15','P-16','P-19']}
 (HERE/'per7_global_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('DONE',len(results),'seconds',time.time()-start,'dependenciesstillseparate',flush=True)
if __name__=='__main__':main()
