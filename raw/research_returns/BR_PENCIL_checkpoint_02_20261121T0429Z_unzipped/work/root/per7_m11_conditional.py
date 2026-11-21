from pathlib import Path
import sys,json,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from det7_prolongation import data,prolong,rank
from build_det7_certificate import line_certificate,determinant_mod

def main():
 filters=json.loads(Path(__file__).with_name('per7_m11_line_filters.json').read_text());out=[]
 for old in filters:
  S=old['subset'];variables,T,blocks,image=data(S,1);U=[T[:,:,c] for c in range(11)];done=[];unresolved=[]
  for pair in old['remaining']:
   fixed=next((i for i in pair if blocks[i][2]==1),None)
   if fixed is None:unresolved.append(pair);continue
   variable=next(i for i in pair if i!=fixed)
   w,coords,d=blocks[fixed];params=coords[:-1] if w in image else coords;assert len(params)==1
   coord=list(params[0]);X=np.zeros(T.shape[:2],dtype=np.int64);X[tuple(coord)]=1;base=U+[X]
   resolved=False
   for F,dF in [('A',7),('B',11)]:
    M=prolong(base,F);rr,rows,cols=rank(M);needed=(dF-1)*13-rr+1
    if needed<1 or needed>dF:continue
    try:line=line_certificate(S,variables,T,blocks[variable],image,F,needed,extra_base_coordinates=[coord])
    except AssertionError:continue
    bc={'orientation':F,'minor_order':rr,'rows':rows,'cols':cols,'determinant_mod_p':determinant_mod(M[np.ix_(rows,cols)])};assert bc['determinant_mod_p']
    done.append({'pair':pair,'fixed_index':fixed,'variable_index':variable,'fixed_coordinate':coord,'base_rank_certificate':bc,'line_certificate':line})
    print(S,'pair',pair,'fixed',fixed,'variable_dim',blocks[variable][2],'factor',F,'base',rr,'min_inc',needed,'EXCLUDED',flush=True)
    resolved=True;break
   if not resolved:unresolved.append(pair)
  out.append({'subset':S,'conditioned_pair_checks':done,'unresolved':unresolved})
  print('CASE remaining',unresolved,flush=True)
 Path(__file__).with_name('per7_m11_conditional.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
