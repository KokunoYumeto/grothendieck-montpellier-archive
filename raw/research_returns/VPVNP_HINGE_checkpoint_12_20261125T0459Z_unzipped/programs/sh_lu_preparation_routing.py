"""Exact rational routing certificate for the explicit LU preparation graph.

An LP searches for uniform all-pairs routing on paths of length at most4.
Only the independently checkable rational paths in the output are a proof.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

ROOT = Path(__file__).resolve().parents[1]
cp = ROOT / (sys.argv[1] if len(sys.argv)>1 else 'inputs/sh_lu_preparation_routing.json')
cfg = json.loads(cp.read_text())
gp = ROOT / cfg['graph_input']
raw = json.loads(gp.read_text())
if cfg.get('graph_format') == 'lc_search':
    raw_edges = raw['best_edges_one_based']
else:
    raw_edges = raw['systematic_css']['source_graph_edges_one_based']
edges = [tuple(sorted(e)) for e in raw_edges]
n = cfg['vertices']; nv = range(1,n+1)
eid = {e:i for i,e in enumerate(edges)}
adj = {v:[] for v in nv}
for a,b in edges:adj[a].append(b);adj[b].append(a)
pairs = [(u,v) for u in nv for v in nv if u<v]
pid = {p:i for i,p in enumerate(pairs)}
paths=[]; pp=[]; masks=[]
for u in nv:
    def visit(path):
        v=path[-1]
        if len(path)>1 and u<v:
            paths.append(path[:]);pp.append(pid[(u,v)])
            masks.append([eid[tuple(sorted(e))] for e in zip(path,path[1:])])
        if len(path)-1==cfg['max_path_length']:return
        for w in adj[v]:
            if w not in path:visit(path+[w])
    visit([u])
K=len(paths)
er=[];ec=[];ev=[];ur=[];uc=[];uv=[]
for j,(pair,used) in enumerate(zip(pp,masks)):
    er.append(pair);ec.append(j);ev.append(1)
    for e in used:ur.append(e);uc.append(j);uv.append(1)
for i in range(len(pairs)):er.append(i);ec.append(K);ev.append(-1)
Aeq=coo_matrix((ev,(er,ec)),shape=(len(pairs),K+1)).tocsr()
Aub=coo_matrix((uv,(ur,uc)),shape=(len(edges),K+1)).tocsr()
c=np.zeros(K+1);c[-1]=-1
r=linprog(c,A_ub=Aub,b_ub=np.ones(len(edges)),A_eq=Aeq,b_eq=np.zeros(len(pairs)),
          bounds=(0,None),method='highs',options={'time_limit':cfg['time_limit_seconds']})
out={'status':'SEARCH ONLY','input_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
     'graph_input':cfg['graph_input'],'graph_format':cfg.get('graph_format','systematic_css'),
     'graph_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),
     'vertices':n,'edges':edges,'path_count':K,'lp_status':int(r.status),'lp_message':r.message}
if r.x is not None:
    out['floating_uniform_demand']=float(r.x[-1])
    target=Fraction(2,n)
    D=cfg['rounding_denominator']
    bypair=[[]for _ in pairs]
    for j,x in enumerate(r.x[:K]):
        z=math.floor(max(0,float(x))*(1-cfg['uniform_shrink'])*D)
        if z:bypair[pp[j]].append((j,Fraction(z,D)))
    totals=[sum((x for _,x in row),Fraction())for row in bypair]
    if min(totals)>=target:
        cert=[];loads=[Fraction()for _ in edges];demands=[Fraction()for _ in pairs]
        for i,row in enumerate(bypair):
            for j,x in row:
                x=x*target/totals[i]
                cert.append({'path':paths[j],'weight':[x.numerator,x.denominator]})
                demands[i]+=x
                for e in masks[j]:loads[e]+=x
        assert all(x==target for x in demands)
        assert all(x<=1 for x in loads)
        out.update(status='PASS exact rational uniform routing',uniform_demand=[target.numerator,target.denominator],
                   certificate=cert,edge_loads=[[x.numerator,x.denominator]for x in loads],
                   exact_verified_pairs=len(pairs),exact_verified_edges=len(edges))
dest=ROOT/cfg['output'];tmp=dest.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(dest)
print(json.dumps({k:v for k,v in out.items()if k not in('certificate','edge_loads','edges')},indent=2))
