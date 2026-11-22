#!/usr/bin/env python3
"""Complete finite polygon-gluing certificate, including exceptional sweeps.
Ordinary gluing swaps the two chord names at a transition arc (154/039,
reflection convention). Exceptional stable endpoints preserve the original
vertex; exceptional unstable endpoints preserve the adjacent original edge,
recognized by the stable generization and its sweep partner.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter,deque
import json,time
ROOT=Path(__file__).resolve().parents[1]
def canon(s):
 a=next(v for v in s if v);return tuple(a*v for v in s)
class DSU:
 def __init__(self,n):self.p=list(range(n))
 def find(self,x):
  while self.p[x]!=x:self.p[x]=self.p[self.p[x]];x=self.p[x]
  return x
 def join(self,a,b):
  a=self.find(a);b=self.find(b)
  if a!=b:self.p[a]=b

def run(name):
 tic=time.perf_counter();inp=json.loads((ROOT/f'audit/counts_{name}_input.json').read_text());n=inp['n'];m=2*n;pairs=[tuple(x) for x in inp['pairs']];base={tuple(r[:3]):r[3] for r in inp['base_chirotope']}
 data=json.loads((ROOT/f'audit/counts_{name}_boundary_certificate.json').read_text());positions=[tuple(d['signs']) for d in data];lookup={s:i for i,s in enumerate(positions)}
 def chi0(a,b,c):
  if len({a,b,c})<3:return 0
  t=(a,b,c);return (-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))*base[tuple(sorted(t))]
 def q(s,a,b):return 0 if a==b else (1 if a<b else -1)*s[pairs.index(tuple(sorted((a,b))))]
 def sweep(s,i):return canon(tuple(-v if i in pair else v for pair,v in zip(pairs,s)))
 faces=[]
 for d,s in zip(data,positions):
  order=[tuple(x) for x in d['boundary_order']]
  arcs=[]
  for p,kind in d['ordinary_transitions']:
   if kind=='E':continue
   j=int(p);labels=(order[j],order[(j+1)%m]);arcs.append({'pos':p+0.5,'kind':kind,'labels':labels,'pair':tuple(sorted([labels[0][1],labels[1][1]]))})
  for e in d['exceptional_corridors']:
   a,b=e['start'],e['end'];length=(b-a)%m
   arcs.append({'pos':(a+length/2)%m,'kind':'E','line':e['line'],'start':a,'end':b})
  if d['nu']==0:
   for i in range(n):
    ratios={q(s,a,b)*chi0(a,b,i) for a,b in pairs if i not in (a,b)}
    if len(ratios)!=1:continue
    r=next(iter(ratios));ii=[j for j,t in enumerate(order) if t[1]==i];choices=[]
    for a,b in [ii,ii[::-1]]:
     j=(a+1)%m
     if order[j][0]*q(s,order[j][1],i)==-r:choices.append((a,b))
    assert len(choices)==1,(name,d,i,ratios,choices)
    a,b=choices[0];length=(b-a)%m;arcs.append({'pos':(a+length/2)%m,'kind':'E','line':i,'start':a,'end':b})
  arcs.sort(key=lambda a:a['pos'])
  assert all(arcs[i]['pos']!=arcs[i-1]['pos'] for i in range(len(arcs))),(name,d,arcs)
  faces.append(arcs)
 # Arc indices are the edges in the boundary cycle of each face.
 all_arcs=[(f,j) for f,a in enumerate(faces) for j in range(len(a))]
 edge_pair={};endpoint_map={}
 def pair_arc(a,b,perm):
  assert a!=b
  if a in edge_pair:assert edge_pair[a]==b
  if b in edge_pair:assert edge_pair[b]==a
  edge_pair[a]=b;edge_pair[b]=a
  for e in [0,1]:
   u=(*a,e);v=(*b,perm[e]);
   if u in endpoint_map:assert endpoint_map[u]==v
   if v in endpoint_map:assert endpoint_map[v]==u
   endpoint_map[u]=v;endpoint_map[v]=u
 for f,j in all_arcs:
  a=faces[f][j]
  if a['kind']!='S':continue
  s=list(positions[f]);s[pairs.index(a['pair'])]=0;g=lookup[canon(s)]
  cand=[k for k,b in enumerate(faces[g]) if b['kind']=='G' and set(b['labels'])==set(a['labels'])]
  assert len(cand)==1,(name,f,j,g,cand)
  k=cand[0];b=faces[g][k]
  # The chosen reflection exchanges the chord names, rather than continuing
  # a chord through to the same named chord (the discarded gluing).
  perm=[next(e for e in [0,1] if b['labels'][e][1]!=a['labels'][z][1]) for z in [0,1]]
  pair_arc((f,j),(g,k),perm)
 for f,j in all_arcs:
  a=faces[f][j]
  if a['kind']!='E' or data[f]['nu']!=0:continue
  i=a['line'];g=lookup[sweep(positions[f],i)];cand=[k for k,b in enumerate(faces[g]) if b['kind']=='E' and b['line']==i]
  assert len(cand)==1; k=cand[0]
  # Endpoint 0 lies next to the preceding arc; endpoint 1 next to following.
  def vertex(ff,jj,e):
   aa=faces[ff][(jj+(-1 if e==0 else 1))%len(faces[ff])]
   assert aa['kind']=='S',(name,ff,jj,e,aa)
   return aa['pair']
  perm=[next(e for e in [0,1] if vertex(f,j,z)==vertex(g,k,e)) for z in [0,1]]
  pair_arc((f,j),(g,k),perm)
 for f,j in all_arcs:
  a=faces[f][j]
  if a['kind']!='E' or data[f]['nu']!=1:continue
  i=a['line'];g=lookup[sweep(positions[f],i)];cand=[k for k,b in enumerate(faces[g]) if b['kind']=='E' and b['line']==i]
  assert len(cand)==1;k=cand[0]
  def stable_neighbor(ff,jj,e):
   z=(jj+(-1 if e==0 else 1))%len(faces[ff]);aa=faces[ff][z]
   assert aa['kind']=='G',(name,ff,jj,e,aa)
   return edge_pair[ff,z][0]
  perm=[]
  for z in [0,1]:
   st=stable_neighbor(f,j,z);wanted=lookup[sweep(positions[st],i)]
   cand=[e for e in [0,1] if stable_neighbor(g,k,e)==wanted]
   assert len(cand)==1,(name,f,j,z,g,k,st,wanted,cand)
   perm.append(cand[0])
  pair_arc((f,j),(g,k),perm)
 assert set(edge_pair)==set(all_arcs)
 # One polygon corner for every consecutive pair of arcs; identify endpoint
 # (f,j,1) with corner j and endpoint(f,j,0) with corner j-1.
 corners=[(f,j) for f,a in enumerate(faces) for j in range(len(a))];ci={c:i for i,c in enumerate(corners)};dsu=DSU(len(corners))
 def corner(v):
  f,j,e=v;return f,(j if e else (j-1)%len(faces[f]))
 for u,v in endpoint_map.items():dsu.join(ci[corner(u)],ci[corner(v)])
 orbits={}
 for c in corners:orbits.setdefault(dsu.find(ci[c]),[]).append(c)
 sizes=Counter(map(len,orbits.values()));assert set(sizes)=={4},(name,sizes)
 assert all(len({f for f,j in orbit})==4 for orbit in orbits.values())
 # The graph of face corners in a vertex orbit has degree two. Parallel
 # edges are retained; size four + connectivity gives a genuine four-cycle.
 link_edges={}
 for u,v in endpoint_map.items():
  if u>v:continue
  a,b=corner(u),corner(v);r=dsu.find(ci[a]);link_edges.setdefault(r,[]).append([a,b])
 for r,orb in orbits.items():
  deg=Counter(c for e in link_edges[r] for c in e)
  assert set(deg.values())=={2} and len(link_edges[r])==4
  assert len({tuple(sorted(e)) for e in link_edges[r]})==4
 # Connectivity and orientability are computed from the edge gluings.
 assigned={};parents={};components=0;orientable=True;obstruction=[];orientation_cycle=[]
 for start in range(len(faces)):
  if start in assigned:continue
  components+=1;assigned[start]=1;queue=deque([start])
  while queue:
   f=queue.popleft()
   for j in range(len(faces[f])):
    g,k=edge_pair[f,j];mapped=endpoint_map[f,j,0][2]
    # Same boundary direction reverses face orientations, opposite preserves.
    required=assigned[f]*(-1 if mapped==0 else 1)
    if g not in assigned:assigned[g]=required;parents[g]=(f,k);queue.append(g)
    elif assigned[g]!=required:
     orientable=False;obstruction.append([f,j,g,k])
     if not orientation_cycle:
      path_f=[];anc={f:0};u=f
      while u in parents:
       pp,ej=parents[u];path_f.append((u,ej));u=pp;anc[u]=len(path_f)
      path_g=[];v=g
      while v not in anc:
       pp,ej=parents[v];path_g.append((v,ej));v=pp
      walk=path_f[:anc[v]]+[edge_pair[a] for a in reversed(path_g)]+[(g,k)]
      product=1
      for ff,jj in walk:
       gg,kk=edge_pair[ff,jj];r=(-1 if endpoint_map[ff,jj,0][2]==0 else 1);product*=r
       orientation_cycle.append({'face':ff,'arc':jj,'next_face':gg,'next_arc':kk,'orientation_factor':r})
      assert product==-1
      assert all(orientation_cycle[i]['next_face']==orientation_cycle[(i+1)%len(orientation_cycle)]['face'] for i in range(len(orientation_cycle)))
 V=len(orbits);E=len(all_arcs)//2;F=len(faces)
 result={'case':name,'F':F,'E':E,'V':V,'chi':V-E+F,'components':components,'orientable':orientable,'crosscap_number_if_connected':2-(V-E+F),'vertex_link_sizes':dict(sizes),'all_closed_faces_embedded':True,'ordinary_edges':sum(a['kind']!='E' for arcs in faces for a in arcs)//2,'exceptional_edges':sum(a['kind']=='E' for arcs in faces for a in arcs)//2,'elapsed_seconds':time.perf_counter()-tic}
 full={'summary':result,'faces':faces,'edge_pairing':[[*a,*b,*[endpoint_map[*a,z][2] for z in [0,1]]] for a,b in edge_pair.items() if a<b],'vertex_orbits':list(orbits.values()),'orientation_conflicts':obstruction,'orientation_reversing_cycle':orientation_cycle}
 (ROOT/f'audit/counts_{name}_gluing_certificate.json').write_text(json.dumps(full,indent=2)+'\n');return result

def main():
 results=[]
 for f in sorted((ROOT/'audit').glob('counts_n*_boundary_certificate.json')):
  name=f.name[len('counts_'):-len('_boundary_certificate.json')]
  r=run(name);results.append(r);print(json.dumps(r),flush=True)
 (ROOT/'audit/counts_gluing_summary.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
