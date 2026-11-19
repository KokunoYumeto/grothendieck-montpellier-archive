#!/usr/bin/env python3
"""Finite cellular certificate for the simultaneous-cone transition correction.
Constant one-point diagrams turn every cone block into a simplex. Quotient
its cells by all three specified transition families, or omit prefix maps.
This checks the exact finite counterexample and higher-chain cell counts.
"""
from itertools import combinations
from collections import Counter
from math import comb
from pathlib import Path
import time,json

def subsets(t, nonempty=False):
 for k in range(1 if nonempty else 0,len(t)+1):
  yield from combinations(t,k)

class UF:
 def __init__(self,items): self.p={x:x for x in items}
 def find(self,x):
  if self.p[x]!=x:self.p[x]=self.find(self.p[x])
  return self.p[x]
 def join(self,x,y):
  a,b=self.find(x),self.find(y)
  if a!=b:self.p[b]=a

def certificate(n,prefix=True):
 flags=list(subsets(tuple(range(n)),True))
 blocks=[(d,e) for e in flags for d in subsets(e[:-1])]
 selected={(d,e):d+(e[-1],) for d,e in blocks}
 cells=[(d,e,a) for d,e in blocks for a in subsets(selected[d,e],True)]
 uf=UF(cells);mapcount=0
 def impose(src,dst):
  nonlocal mapcount
  mapcount+=1
  for face in subsets(selected[src],True):
   assert set(face)<=set(selected[dst])
   uf.join((*src,face),(*dst,face))
 for d,e in blocks:
  for dp in subsets(e[:-1]):
   if set(d)<=set(dp):impose((d,e),(dp,e))
  f=selected[d,e]
  impose((d,e),(f[:-1],f))
  if prefix:
   for a in d:
    ep=tuple(x for x in e if x<=a)
    dp=tuple(x for x in d if x<a)
    impose((dp,ep),(d,e))
 reps={uf.find(c) for c in cells}
 count=Counter(len(c[2])-1 for c in reps)
 verts=[c for c in reps if len(c[2])==1]
 conn=UF(verts)
 for c in reps:
  if len(c[2])==2:
   d,e,face=c
   conn.join(uf.find((d,e,(face[0],))),uf.find((d,e,(face[1],))))
 components=len({conn.find(v) for v in verts})
 if prefix:
  assert [count[k] for k in range(n)]==[comb(n,k+1) for k in range(n)]
  assert components==(1 if n else 0)
 return {'vertices':n,'prefix_maps':prefix,'blocks':len(blocks),
         'raw_cells':len(cells),'transition_maps':mapcount,
         'quotient_cells_by_dimension':dict(sorted(count.items())),
         'connected_components':components}

def main():
 start=time.perf_counter()
 wrong=certificate(2,False);right=certificate(2,True)
 assert wrong['connected_components']==2 and wrong['quotient_cells_by_dimension']=={0:3,1:1}
 assert right['connected_components']==1 and right['quotient_cells_by_dimension']=={0:2,1:1}
 allchains=[certificate(n,True) for n in range(7)]
 result={'status':'PASS','omitting_prefix_maps':wrong,'all_three_families':right,
         'constant_chain_checks_0_to_6':allchains,
         'elapsed_seconds':round(time.perf_counter()-start,9)}
 text=json.dumps(result,indent=2)
 Path(__file__).with_suffix('.output.json').write_text(text+'\n')
 print(text)
if __name__=='__main__':main()
