#!/usr/bin/env python3
"""Search for a counterexample to the fractional-flow-plus-integral-tree gate.

Random edge costs select integer graphs satisfying the six required cuts.
A second MILP tests the proposed integral packing.  Infeasibility status
alone is exploratory; a counterexample would need an exact certificate.
"""
import itertools
import json
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from sh_integer_network_search import model


def packing(n,edges,cap,limit):
    E=len(edges);nv=9*E;rows=[];lo=[];hi=[]
    demands=[(0,3,3),(1,2,3),(0,2,2),(1,3,2)]
    for k,(s,t,d) in enumerate(demands):
        for v in range(n):
            row=np.zeros(nv)
            for j,(a,b) in enumerate(edges):
                if v==a:row[2*E*k+2*j]=1;row[2*E*k+2*j+1]=-1
                if v==b:row[2*E*k+2*j]=-1;row[2*E*k+2*j+1]=1
            rhs=d if v==s else -d if v==t else 0
            rows.append(row);lo.append(rhs);hi.append(rhs)
    for j in range(E):
        row=np.zeros(nv)
        for k in range(4):row[2*E*k+2*j:2*E*k+2*j+2]=1
        row[8*E+j]=1;rows.append(row);lo.append(0);hi.append(cap[j])
    for termmask in range(1,8):
        for extra in range(1<<(n-4)):
            mask=termmask+(extra<<4);row=np.zeros(nv)
            for j,(a,b) in enumerate(edges):row[8*E+j]=int(((mask>>a)^(mask>>b))&1)
            rows.append(row);lo.append(1);hi.append(np.inf)
    rows=np.array(rows);lo=np.array(lo);hi=np.array(hi)
    upper=np.concatenate([np.full(8*E,3),np.ones(E)])
    result=milp(np.r_[np.zeros(8*E),np.ones(E)],integrality=np.r_[np.zeros(8*E),np.ones(E)],
                bounds=Bounds(0,upper),constraints=LinearConstraint(rows,lo,hi),
                options={'time_limit':limit,'mip_rel_gap':0.0})
    answer={'status':int(result.status),'message':str(result.message)}
    if result.x is not None:
        from fractions import Fraction
        x=np.array([float(Fraction(float(v)).limit_denominator(1000000)) for v in result.x])
        exact=[Fraction(float(v)).limit_denominator(1000000) for v in result.x]
        for row,l,h in zip(rows,lo,hi):
            val=sum(int(c)*v for c,v in zip(row,exact) if c)
            assert (not np.isfinite(l) or val>=int(l)) and (not np.isfinite(h) or val<=int(h))
        assert all(v.denominator==1 for v in exact[8*E:])
        answer['exact_rational_feasible']=True
        answer['tree_edges']=[list(edges[j]) for j in range(E) if x[8*E+j]]
        answer['commodity_flows']=[[[int(a),int(b),str(exact[2*E*k+2*j]),str(exact[2*E*k+2*j+1])]
                                     for j,(a,b) in enumerate(edges) if x[2*E*k+2*j] or x[2*E*k+2*j+1]] for k in range(4)]
    return answer


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());out=Path(sys.argv[2]);rng=np.random.default_rng(cfg['seed']);records=[]
    for k in cfg['internal_vertices']:
        n,edges,rows,rhs,labels=model(k)
        for trial in range(cfg['trials']):
            costs=rng.exponential(1,size=len(edges))+.05
            if cfg.get('critical_profile',False):
                allrows=list(rows);lower=list(rhs);upper=[np.inf]*len(rhs)
                # Zero-length external width-six edges allow terminal degree
                # six to be imposed when testing the critical profile.
                for v in range(4):
                    allrows.append(np.array([int(v in e) for e in edges],float));lower.append(6);upper.append(6)
                chosen=int(rng.integers(1<<k));mask=9+(chosen<<4)
                allrows.append(np.array([int(((mask>>a)^(mask>>b))&1) for a,b in edges],float));lower.append(5);upper.append(5)
                for extra in range(1<<k):
                    mask=5+(extra<<4)
                    allrows.append(np.array([int(((mask>>a)^(mask>>b))&1) for a,b in edges],float));lower.append(7);upper.append(np.inf)
                solve_rows=np.array(allrows);solve_lower=np.array(lower);solve_upper=np.array(upper)
            else:
                solve_rows=rows;solve_lower=rhs;solve_upper=np.full(len(rhs),np.inf)
            result=milp(costs,integrality=np.ones(len(edges)),bounds=Bounds(0,12),
                        constraints=LinearConstraint(solve_rows,solve_lower,solve_upper),
                        options={'time_limit':cfg['time_limit'],'mip_rel_gap':0.0})
            if result.x is None:continue
            cap=np.rint(result.x).astype(int);assert np.all(rows@cap>=rhs)
            active=[j for j,c in enumerate(cap) if c]
            es=[edges[j] for j in active];cs=cap[active]
            pack=packing(n,es,cs,cfg['time_limit'])
            record=dict(k=k,trial=trial,capacities=[[a,b,int(c)] for (a,b),c in zip(es,cs)],
                        objective=float(costs@cap),all_required_cuts_exact=True,packing=pack)
            if cfg.get('critical_profile',False):record['fixed_low_cut_internal_mask']=chosen
            records.append(record);print(json.dumps(record),flush=True)
            out.write_text(json.dumps(dict(config=cfg,runs=records,
                scope='Exploratory counterexample search; solver infeasibility alone is not a proof.'),indent=2))
            if pack['status']==2:
                print('CANDIDATE_COUNTEREXAMPLE_NEEDS_EXACT_CERTIFICATE',flush=True)
                return


if __name__=='__main__':main()
