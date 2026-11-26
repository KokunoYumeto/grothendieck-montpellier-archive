#!/usr/bin/env python3
"""Exploratory integer-capacity four-terminal geometric network search.

Alternates an exact-capacity MILP at fixed candidate positions with a
continuous convex length minimization for the selected capacities.
Only displayed feasible networks are certified; search failure is not
a lower bound on arbitrary layouts or numbers of internal vertices.
"""
from pathlib import Path
import itertools
import json
import sys
import time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint, minimize


def model(k):
    n=4+k;edges=list(itertools.combinations(range(n),2));rows=[];rhs=[];labels=[]
    requirements=[(1,6),(2,6),(4,6),(8,6),(3,12),(9,5)]
    for mask,need in requirements:
        for extra in range(1<<k):
            full=mask+(extra<<4)
            rows.append([int(((full>>a)^(full>>b))&1) for a,b in edges])
            rhs.append(need);labels.append([mask,extra])
    return n,edges,np.array(rows,dtype=float),np.array(rhs,dtype=float),labels


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());out=Path(sys.argv[2])
    fixed=np.array([[1.,0.],[0.,1.],[-1.,0.],[0.,-1.]])
    rng=np.random.default_rng(cfg['seed']);records=[];best=float('inf')
    for k in cfg['internal_vertices']:
        n,edges,rows,rhs,labels=model(k);ei=np.array(edges)
        for trial in range(cfg['restarts']):
            pos=rng.normal(size=(k,2));pos*=rng.uniform(.1,.8,size=(k,1))/np.linalg.norm(pos,axis=1)[:,None]
            if trial==0 and k>=2:
                h=(1-1/np.sqrt(3))/2
                pos[0]=[h,-h];pos[1]=[-h,h]
            previous=None
            for iteration in range(cfg['alternations']):
                allpos=np.vstack([fixed,pos]);lengths=np.linalg.norm(allpos[ei[:,0]]-allpos[ei[:,1]],axis=1)
                solved=milp(lengths,integrality=np.ones(len(edges)),bounds=Bounds(0,12),
                            constraints=LinearConstraint(rows,rhs,np.inf),
                            options={'time_limit':cfg['milp_time_limit'],'mip_rel_gap':0.0})
                if solved.x is None:
                    records.append(dict(k=k,trial=trial,iteration=iteration,milp_status=int(solved.status),message=str(solved.message)))
                    break
                cap=np.rint(solved.x).astype(int)
                assert np.all(rows@cap>=rhs)
                def fg(x):
                    pp=np.vstack([fixed,x.reshape(k,2)]);dif=pp[ei[:,0]]-pp[ei[:,1]]
                    ll=np.sqrt(np.sum(dif*dif,axis=1)+1e-20);value=float(cap@ll)
                    grad=np.zeros_like(pp);g=(cap/ll)[:,None]*dif
                    np.add.at(grad,ei[:,0],g);np.add.at(grad,ei[:,1],-g)
                    return value,grad[4:].ravel()
                moved=minimize(fg,pos.ravel(),jac=True,method='L-BFGS-B',bounds=[(-1,1)]*(2*k),
                               options={'maxiter':1000,'ftol':1e-13,'gtol':1e-9,'maxls':40})
                pos=moved.x.reshape(k,2)
                # Euclidean projection onto the terminal diamond.  The
                # minimizer normally already lies there; this preserves feasibility.
                for i in range(k):
                    a=np.abs(pos[i])
                    if a.sum()>1:
                        if abs(a[0]-a[1])>=1:a=np.array([1.,0.]) if a[0]>a[1] else np.array([0.,1.])
                        else:a-=(a.sum()-1)/2
                        pos[i]=np.sign(pos[i])*a
                allpos=np.vstack([fixed,pos]);lengths=np.linalg.norm(allpos[ei[:,0]]-allpos[ei[:,1]],axis=1)
                value=float(cap@lengths)
                record=dict(k=k,trial=trial,iteration=iteration,cost=value,milp_status=int(solved.status),
                            capacities=[[int(a),int(b),int(c)] for (a,b),c in zip(edges,cap) if c],
                            positions=allpos.tolist(),all_required_cuts_verified=True,
                            cut_minima={str(mask):int(min((rows@cap)[i] for i,lab in enumerate(labels) if lab[0]==mask)) for mask in[1,2,4,8,3,9]})
                records.append(record);print(json.dumps(record),flush=True)
                if value<best:
                    best=value
                    out.write_text(json.dumps(dict(config=cfg,best=record,runs=records,
                        scope='Feasible finite layouts only; no arbitrary-network lower bound.'),indent=2))
                if previous is not None and np.array_equal(cap,previous):break
                previous=cap
    out.write_text(json.dumps(dict(config=cfg,best_cost=best,runs=records,
        scope='Exploratory alternating optimization; no arbitrary-network lower bound.'),indent=2))


if __name__=='__main__':main()
