#!/usr/bin/env python3
"""Exact orbitwise analysis of three Hurwitz pentagon evaluation pairs.

If every component has nilpotent second derived subgroup, the full pair does:
it embeds into their direct product. Unexamined components are recorded as such.
"""
import argparse, collections, json, pathlib, time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

def run(path,cap=216):
 path=pathlib.Path(path);st=time.monotonic();ps=np.load(path)['generators'];co=lambda a,b:a[b]
 x=[co(a,a) for a in ps]
 for a in (co(co(ps[0],ps[1]),ps[0]),co(co(ps[2],ps[1]),ps[2])):x.append(co(a,a))
 n=len(x[0]);rows=[];cache={};log=path.with_name(path.stem+'_components.jsonl')
 log.write_text('')
 for i,j in [(0,1),(2,3),(3,4)]:
  seen=set();orbits=[]
  for a in range(n):
   if a in seen:continue
   orb=[a];seen.add(a)
   for v in orb:
    for g in (x[i],x[j]):
     w=int(g[v])
     if w not in seen:seen.add(w);orb.append(w)
   orbits.append(orb)
  for oi,orb in enumerate(sorted(orbits,key=len)):
   row={'pair':[i+1,j+1],'component':oi,'degree':len(orb)}
   if len(orb)>cap:
    row['status']='OVER_CAP_NOT_ANALYZED'
   else:
    vi={v:k for k,v in enumerate(orb)}
    pp=tuple(tuple(vi[int(g[v])] for v in orb) for g in (x[i],x[j]));key=pp
    if key in cache:row.update(cache[key]);row['cache']=True
    else:
     group=PermutationGroup([Permutation(list(g)) for g in pp]);series=group.derived_series();orders=[int(g.order()) for g in series]
     row.update({'status':'EXACT','derived_orders':orders,'second_derived_nilpotent':bool(series[min(2,len(series)-1)].is_nilpotent)})
     if (i,j)==(0,1) and orders[0]%216==0:
      affine=[]
      for which in [0,1]:
       a=[]
       for u in range(3):
        for v in range(3):
         if which==0:b=((2*u+v)%3,(2*v)%3)
         else:b=((2*u+1)%3,(2*u+2*v)%3)
         a.append(b[0]*3+b[1])
       affine.append(a)
      joint=PermutationGroup([Permutation(list(g)+[len(g)+v for v in h]) for g,h in zip(pp,affine)])
      jo=int(joint.order());row['joint_with_marked_E0_order']=jo;row['has_marked_E0_quotient']=jo==orders[0]
     cache[key]={k:v for k,v in row.items() if k not in ['pair','component','degree']}
    if not row.get('second_derived_nilpotent',True):
     np.savez_compressed(path.with_name(path.stem+f'_pair{i+1}{j+1}_component{oi}.npz'),generators=np.array(pp))
   rows.append(row)
   with log.open('a') as f:f.write(json.dumps(row)+'\n')
   if row['status']=='EXACT' and not row.get('cache'):print(json.dumps(row),flush=True)
 out={'input':str(path),'degree':n,'component_cap':cap,'components':rows,'elapsed_seconds':time.monotonic()-st}
 path.with_name(path.stem+'_components.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'input':str(path),'component_count':len(rows),'unknown_count':sum(r['status']!='EXACT' for r in rows),'nonnilpotent_second_count':sum(r.get('second_derived_nilpotent')==False for r in rows),'elapsed_seconds':out['elapsed_seconds']}),flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('path');ap.add_argument('--cap',type=int,default=216);a=ap.parse_args();run(a.path,a.cap)
