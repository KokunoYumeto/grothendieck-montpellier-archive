#!/usr/bin/env python3
"""Borel extension enumeration with higher Koszul tests on the extension tensor."""
import argparse,json,time,math
from collections import Counter
from borel_quiver import ab_module,successors,extension_vectors
from probe_coupled_borel import wedge_ranks
from probe_extension_koszul import koszul
from check_koszul import ideals


def run(S,r=17):
 start=time.time();M=ab_module(S);a=len(S);b=len(M['support']);q=r-b
 states={tuple(() for _ in M['blocks'])};families=[];history=[];excluded=[]
 for level in range(1,q+1):
  nxt=set()
  for F in states:
   rigid,params=successors(M,F);nxt.update(rigid)
   families.extend((level,F,i,K) for i,K in params)
  states=set();counts=Counter()
  for F in nxt:
   E=M['U']+extension_vectors(M,F);rs=wedge_ranks(E,a,b)
   if rs['A']>(a-1)*r or rs['B']>(b-1)*r:counts['first_wedge']+=1;continue
   done=False
   for f,dim in ((2,b),(1,a)):
    for p in (2,3):
     if len(E)*dim<=r*(dim-p):continue
     t=koszul(E,M,f,0,p)
     if t['lower']>r:done=True;excluded.append({'level':level,'test':t});counts['higher_koszul']+=1;break
    if done:break
   if not done:states.add(F)
  history.append({'level':level,'generated':len(nxt),'remaining':len(states),'excluded':dict(counts),'families':len(families)})
  if not states:break
 out={'subset':S,'support_dim':b,'history':history,'rigid_survivors':len(states),'parameter_branches':len(families),'family_dimensions':dict(Counter(len(K) for lv,F,i,K in families)),
      'family_levels':dict(Counter(lv for lv,F,i,K in families)),'status':'EXCLUDED' if not states and not families else 'OPEN','higher_exclusions':excluded,'seconds':time.time()-start}
 print(json.dumps({k:v for k,v in out.items() if k!='higher_exclusions'}),flush=True)
 return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+');ap.add_argument('--output');args=ap.parse_args()
 cases=[args.subset] if args.subset else [S for S in ideals(10) if S<=tuple(sorted((q%6)*6+q//6 for q in S))]
 results=[]
 for S in cases:
  results.append(run(S))
  if args.output:open(args.output,'w').write(json.dumps(results,indent=2)+'\n')
