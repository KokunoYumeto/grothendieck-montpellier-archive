#!/usr/bin/env python3
"""Exploratory B/C coordinate substitution with exact modular Koszul ranks.

For determinant Borel ideals the residual tensor has a Borel stabilizer.
On the variable dual, invariant coordinate subspaces are upper filters.
This script first tests all such one-factor restrictions of each size.
No negative outcome is an exact border-rank upper bound.
"""
from pathlib import Path
from itertools import combinations
import argparse,json,math,time
import numpy as np
from det10_koszul_probe import weighted_blocks
from det7_prolongation import data,rank

def upper_filters(variables,k):
    for chosen in combinations(variables,k):
        D=set(chosen)
        if all(w in D for v in D for w in variables
               if w//4>=v//4 and w%4>=v%4):
            yield tuple(variables.index(v) for v in chosen)

class Calculation:
    def __init__(self,S):
        self.S=S;self.variables,self.T,_,_=data(S,-1)
        self.m=len(self.variables);self.blocks={}
    def prepare(self,p):
        if p not in self.blocks:
            self.blocks[p]=[(np.array(r)%self.m,np.array(c)%self.m,M)
                            for w,r,c,M in weighted_blocks(self.S,'A',p)]
    def bound(self,B,C,target=99):
        M=self.T[:,B,:][:,:,C]
        best=max(sum(np.any(M,axis=(1,2))),sum(np.any(M,axis=(0,2))),sum(np.any(M,axis=(0,1))))
        results=[]
        for p in [4,3,2,1]:
            self.prepare(p);value=0
            for rr,cc,N in self.blocks[p]:
                rows=np.flatnonzero(np.isin(rr,B));cols=np.flatnonzero(np.isin(cc,C))
                if len(rows) and len(cols):value+=rank(N[np.ix_(rows,cols)])[0]
            cost=math.comb(len(self.S)-1,p);b=(value+cost-1)//cost
            results.append({'p':p,'rank':value,'cost':cost,'bound':b});best=max(best,b)
            if best>=target:break
        return int(best),results

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--support',type=int,default=11);args=pa.parse_args()
    here=Path(__file__).resolve().parent;records=json.loads((here/f'det10_borel_support{args.support}.json').read_text())
    out=[];start=time.time()
    for rec in records:
        if rec['excluded']:continue
        S=rec['subset'];calc=Calculation(S);m=calc.m;allB=tuple(range(m));results=[]
        for k in range(m-1,max(3,m-7),-1):
            filters=list(upper_filters(calc.variables,k));minimum=99;tests=[]
            for B in filters:
                b,rs=calc.bound(B,allB,target=18-(m-k));minimum=min(minimum,b)
                tests.append({'retained_B_variables':[calc.variables[i] for i in B],'residual_lower':b,'koszul':rs})
                if minimum+m-k<18:break
            complete=len(tests)==len(filters)
            result={'k':k,'number_of_filters':len(filters),'tested':len(tests),'complete':complete,'minimum_tested':minimum,'substitution_bound':minimum+m-k if complete else None,'tests':tests}
            results.append(result)
            print(S,'k',k,'filters',len(filters),'tested',len(tests),'complete',complete,'minimum',minimum,'plus deleted',minimum+m-k,'seconds',round(time.time()-start,2),flush=True)
        out.append({'subset':S,'support':m,'results':results})
        (here/f'det10_variable_substitution_m{args.support}.json').write_text(json.dumps({'status':'EXPLORATION','records':out,'seconds':time.time()-start},indent=2)+'\n')

if __name__=='__main__':main()
