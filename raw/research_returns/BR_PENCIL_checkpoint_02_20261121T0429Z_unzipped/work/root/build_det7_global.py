"""Exact data for the25-ideal det7 reduction; prolongation dependencies separate."""
from pathlib import Path
import sys,json
import numpy as np
from coordinate_koszul import slices,koszul,modular_rank
from weighted_koszul import blocks
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from build_det7_certificate import determinant_mod
HERE=Path(__file__).resolve().parent

def transpose(S):return sorted((x%6)*6+x//6 for x in S)
def main():
 a=json.loads((HERE/'borel_7_12.json').read_text())['results'][0]['records']
 b={tuple(x['subset']):x for x in json.loads((HERE/'det7_support_koszul.json').read_text())}
 dependencies={}
 for label,reps in {
 'P-09':[[0,1,3,6,7,9,12],[0,1,3,6,7,12,13]],
 'P-12':[[0,1,2,3,6,7,8],[0,1,2,3,4,6,12]],
 'P-14':[[0,1,2,3,6,7,9],[0,1,2,3,6,7,18]],
 'P-15':[[0,1,3,6,7,9,18]]}.items():
  for S in reps:
   dependencies[tuple(S)]=label;dependencies[tuple(transpose(S))]=label
 records=[]
 for rec in a:
  S=rec['subset'];support,mats=slices(S,-1);m=len(support)
  out={'subset':S,'support':support}
  if m>=14:out.update(type='support',lower_bound=m)
  else:
   candidates=[c for c in rec['certificates'] if c['bound']>=14 and c['projection'] is None]
   if candidates:
    c=min(candidates,key=lambda c:13*c['pure_cost']+1);n=13*c['pure_cost']+1
    rows,cols=c['rows'][:n],c['cols'][:n];M=koszul(mats,c['p']);value=determinant_mod(M[np.ix_(rows,cols)])
    assert value
    out.update(type='A_koszul',p=c['p'],cost=c['pure_cost'],rows=rows,cols=cols,minor_order=n,determinant_mod_p=value,lower_bound=14)
   elif tuple(S) in b and any(c['bound']>=14 for c in b[tuple(S)]['certificates']):
    c=next(c for c in b[tuple(S)]['certificates'] if c['bound']>=14);bc=[];rank_sum=0
    for w,rows,cols,M in blocks(S,-1,c['p']):
     cert=modular_rank(M);r=cert['rank_mod_p']
     if not r:continue
     value=determinant_mod(M[np.ix_(cert['rows'],cert['cols'])]);assert value
     bc.append({'weight':w,'rows':[rows[i] for i in cert['rows']],'cols':[cols[i] for i in cert['cols']],'size':r,'determinant_mod_p':value})
     rank_sum+=r
    assert rank_sum>13*c['cost']
    out.update(type='B_koszul',p=c['p'],cost=c['cost'],rank_lower_bound=rank_sum,blocks=bc,lower_bound=14)
   else:
    label=dependencies[tuple(S)];out.update(type='prolongation',finding=label,lower_bound=14)
  records.append(out);print(S,out['type'],out.get('finding',''),flush=True)
 out={'n':4,'b':2,'j':7,'prime':1000003,'field_scope':'characteristic zero','target_minimum':14,'all_Borel_ideals':25,'records':records,'conditional_on_independent_prolongation_certificates':['P-09','P-12','P-14','P-15']}
 (HERE/'det7_global_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('Certificate assembled; prolongation dependencies must pass independently.')
if __name__=='__main__':main()
