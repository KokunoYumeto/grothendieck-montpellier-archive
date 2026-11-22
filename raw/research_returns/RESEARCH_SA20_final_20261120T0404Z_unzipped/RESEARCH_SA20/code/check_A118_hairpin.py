#!/usr/bin/env python3
"""Exact rational polygon and all-link certificate for A.118."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter, defaultdict
import json,time

start=time.perf_counter(); checks=Counter(); e=F(1,4)
polygon=[(-2,2),(1,2),(1,2+e),(-1,2+e),(-1,2+2*e),(2,2+2*e),(2,-2),(-2,-2)]
polygon=[tuple(map(F,p)) for p in polygon]
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on(a,b,c):return cross(a,b,c)==0 and all(min(a[i],b[i])<=c[i]<=max(a[i],b[i]) for i in (0,1))
def meet(a,b,c,d):
 u,v,w,z=cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
 return (u*v<0 and w*z<0) or any((on(a,b,c),on(a,b,d),on(c,d,a),on(c,d,b)))
for i,j in combinations(range(8),2):
 if (i-j)%8 in (1,7):continue
 assert not meet(polygon[i],polygon[(i+1)%8],polygon[j],polygon[(j+1)%8])
 checks['nonadjacent_polygon_edge_pairs']+=1

xs=list(map(F,[-2,-1,0,1,2]));ys=list(map(F,[-2,0,2]))+[2+e,2+2*e]
tri=[]; cells=[]
for i in range(4):
 for j in range(4):
  if j<2 or (j==2 and i==3) or (j==3 and i>=1):
   a,b,c,d=(xs[i],ys[j]),(xs[i+1],ys[j]),(xs[i+1],ys[j+1]),(xs[i],ys[j+1])
   tri.extend([(a,b,c),(a,c,d)]);cells.append((i,j))
edges=Counter();vertices=set();links=defaultdict(list)
for t in tri:
 assert cross(*t)>0;checks['positive_triangle_areas']+=1
 vertices.update(t)
 for a,b in combinations(t,2):edges[tuple(sorted((a,b)))]+=1
 for v in t:links[v].append(tuple(x for x in t if x!=v))
assert set(edges.values())<={1,2}
checks['edge_incidence_counts']=len(edges)
boundary=[edge for edge,n in edges.items() if n==1]
def connected(ad):
 seen=set();stack=[next(iter(ad))]
 while stack:
  x=stack.pop()
  if x in seen:continue
  seen.add(x);stack.extend(ad[x]-seen)
 return len(seen)==len(ad)
badj=defaultdict(set)
for a,b in boundary:badj[a].add(b);badj[b].add(a)
assert all(len(n)==2 for n in badj.values()) and connected(badj)
checks['boundary_cycle']=1
for v,le in links.items():
 adj=defaultdict(set)
 for a,b in le:adj[a].add(b);adj[b].add(a)
 assert connected(adj)
 degrees=Counter(map(len,adj.values()))
 if v in badj:assert degrees[1]==2 and sum(degrees.values())==degrees[1]+degrees[2]
 else:assert set(degrees)=={2}
 checks['vertex_links']+=1
assert len(vertices)-len(edges)+len(tri)==1
assert (F(0),F(0)) in vertices and (F(0),F(0)) not in badj
checks['Euler_and_interior_vertex']=2
for a,b in boundary:
 assert any(on(polygon[i],polygon[(i+1)%8],a) and on(polygon[i],polygon[(i+1)%8],b) for i in range(8))
 checks['boundary_polygon_agreement']+=1
result=dict(statement='A.118',passed=True,parameter=str(e),rectangular_cells=len(cells),
            f_vector=[len(vertices),len(edges),len(tri)],boundary_edges=len(boundary),
            checks=dict(checks),total_checks=sum(checks.values()),seconds=time.perf_counter()-start)
print(json.dumps(result,indent=2))
