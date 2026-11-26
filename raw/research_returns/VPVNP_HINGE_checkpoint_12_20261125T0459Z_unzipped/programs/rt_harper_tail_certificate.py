#!/usr/bin/env python3
"""All-level Harper tail-count relaxation with exact certificate checking.

Exploratory generator: no claim is made from optimizer status. Integer tail
indicator implications hold for actual profiles; relaxing them to[0,1] may
still admit a nonnegative rational Farkas contradiction. Standard certificate
reconstruction is reused, but all mathematical rows are constructed here.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import sys,json,time,math
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
from scipy.sparse import vstack,coo_matrix
import sh_radial_rank_certificate as exact

def system(D,growth_override=None,top_counts=None):
    assert 5<=D<=7
    d=D-1;M=1<<d;n=6*D
    order=[sum(1<<i for i in c) for r in range(d+1) for c in combinations(range(d),r)]
    growth={}
    for v in range(1,M+1):
        distances=[min((s^t).bit_count() for t in order[:v]) for s in range(M)]
        for r in range(1,d+1):growth[v,r]=sum(h<=r for h in distances)
    if growth_override is not None:
        assert growth_override['dimension']==D and growth_override['vertices']==M
        assert growth_override['exhaustive'] is True
        for v in range(1,M+1):
            for r in range(1,d+1):growth[v,r]=growth_override['growth'][str(r)][v]
    def x(k,v):return (k-1)*M+v-1
    rows=[]
    def row(label,c,b):rows.append((label,c,b))
    nv=n*M
    for j in range(nv):
        row(['upper',j],{j:1},1);row(['lower',j],{j:-1},0)
    for k in range(1,n+1):
        for v in range(1,M+1):
            if v<M:row(['count_order',k,v],{x(k,v+1):1,x(k,v):-1},0)
            if k<n:row(['level_order',k,v],{x(k+1,v):1,x(k,v):-1},0)
            for r in range(1,min(d,(k-1)//12)+1):
                row(['neighborhood',k,v,r,growth[v,r]],{x(k,v):1,x(k-12*r,growth[v,r]):-1},0)
    row(['moment'],{x(k,v):2*k-1 for k in range(1,n+1) for v in range(1,M+1)},(2809*D*D*M-1)//144)
    row(['mean'],{j:1 for j in range(nv)},(53*D*M-1)//12)
    required=(M*(1<<n)+2)//3
    row(['rank_average'],{x(k,v):Fraction(-(1<<(k-1)),1<<n) for k in range(1,n+1) for v in range(1,M+1)},Fraction(M-required,1<<n))
    for k,count in (top_counts or {}).items():
        k=int(k);assert 1<=k<=n and 0<=count<=M
        if count:row(['fixed_count_lower',k,count],{x(k,count):-1},-1)
        if count<M:row(['fixed_count_upper',k,count],{x(k,count+1):1},0)
    return {'dimension':D,'section_dimension':d,'vertices':M,'ceiling':n,'nv':nv,'rows':rows,'required_rank_sum':required,
            'expansion':[[v,r,growth[v,r]] for v in range(1,M+1) for r in range(1,d+1)]}

cfg=json.loads(Path(sys.argv[1]).read_text())
override=json.loads(Path(cfg['growth_file']).read_text()) if cfg.get('growth_file') else None
data=system(cfg['dimension'],override,cfg.get('top_counts'))
ri=[];ci=[];va=[]
for i,(_,c,_) in enumerate(data['rows']):
    for j,v in c.items():ri.append(i);ci.append(j);va.append(float(v))
A=coo_matrix((va,(ri,ci)),shape=(len(data['rows']),data['nv'])).tocsc()
b=np.array([float(row[2]) for row in data['rows']]);start=time.monotonic()
out={k:v for k,v in data.items() if k!='rows'}
out['config']=cfg;out['constraints']=len(data['rows'])
if cfg.get('mode','dual')=='dual':
    eq=vstack((A.T,coo_matrix(b.reshape(1,-1)))).tocsc()
    res=linprog(np.ones(A.shape[0]),A_eq=eq,b_eq=np.r_[np.zeros(data['nv']),-1],bounds=(0,None),method='highs',
                options={'time_limit':cfg.get('seconds',30),'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    if res.x is not None:
        try:
            cert=exact.bounded_rational_certificate(data,res.x)
            checked=exact.verify(data,cert)
            out.update(certificate=cert,verification=checked)
        except Exception as e:out['reconstruction_error']=repr(e)
else:
    res=milp(np.zeros(data['nv']),integrality=np.ones(data['nv']),bounds=Bounds(np.zeros(data['nv']),np.ones(data['nv'])),
             constraints=LinearConstraint(A,np.full(A.shape[0],-np.inf),b),options={'time_limit':cfg.get('seconds',30),'mip_rel_gap':0})
    if res.x is not None:
        values=np.rint(res.x).astype(int).tolist()
        bad=[label for label,c,rhs in data['rows'] if sum(c[j]*values[j] for j in c)>rhs]
        out['exact_rows_pass']=not bad;out['violations']=bad
        if not bad:out['tail_counts']=[sum(values[(k-1)*data['vertices']:k*data['vertices']]) for k in range(1,data['ceiling']+1)]
out.update(status=int(res.status),message=str(res.message),seconds=time.monotonic()-start,
           scope='Only an independently checked exact certificate proves exclusion. Feasible tail counts are not functions, networks, or tensors.')
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('certificate','expansion')}))
