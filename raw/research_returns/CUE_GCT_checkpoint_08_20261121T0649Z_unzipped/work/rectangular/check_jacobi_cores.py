"""Finite core minors for a proposed continuant-insertion proof.

Only the listed rationally normalized core matrices are checked here.
The insertion argument must be proved separately before any uniform claim.
"""
import json
from pathlib import Path
import numpy as np

def core(r,j,seed=1,p=101,cuts_override=None,actual_K=False):
    m=r+j
    d=[(7*i*i+13*i+19+17*seed)%p or 1 for i in range(m-1)]
    cuts=[2,m-4]
    if abs(j-r)>=4:cuts.append(min(r,j)+1)
    if cuts_override is not None:cuts=list(cuts_override)
    for i in cuts:d[i]=0
    K=(3+11*seed)%p or 1
    if actual_K:
        numerator=denominator=1
        for e in range(min(r,j)):numerator=numerator*d[e]%p
        for e in range(max(r,j),m-1):denominator=denominator*d[e]%p
        K=numerator*pow(denominator,-1,p)%p
    P={}
    for a in range(m+1):
        P[a,a-1]=[1]
        if a<m:P[a,a]=[1]
        for b in range(a+1,m):
            x=P[a,b-1];y=P[a,b-2];v=[0]*((b-a+1)//2+1)
            for k,c in enumerate(x):v[k]=(v[k]+c)%p
            for k,c in enumerate(y):v[k+1]=(v[k+1]+d[b-1]*c)%p
            P[a,b]=v
    npart=(j+1)//2+1;nminus=(r+1)//2+1
    C=np.zeros((npart+nminus,8),dtype=np.int64)
    def term(col,a,b,tk=0,scale=1,negative=False):
        offset=npart if negative else 0
        for k,c in enumerate(P[a,b]):C[offset+k+tk,col]=(C[offset+k+tk,col]+scale*c)%p
    # Positive weight r, divided by y^r.
    term(0,r+1,m-1);term(1,r,m-1);term(2,r+2,m-1,1)
    term(3,0,j-1);term(4,0,j);term(5,0,j-2,1)
    term(6,r+1,m-2,1,2);term(7,1,j-1,0,2)
    # Negative weight r-m, divided by z^(m-r) and D_r.
    term(0,0,r-1,negative=True);term(1,0,r-2,1,d[r-1],True)
    term(2,0,r,0,pow(d[r],-1,p),True)
    term(3,j+1,m-1,0,K,True);term(4,j+2,m-1,1,K*d[j],True)
    term(5,j,m-1,0,K*pow(d[j-1],-1,p),True)
    term(6,1,r-1,0,2,True);term(7,j+1,m-2,1,2*K,True)
    a=C.copy();row=0;rs=list(range(len(a)));selected=[];det=1
    for col in range(8):
        ii=np.flatnonzero(a[row:,col])
        if not len(ii):continue
        i=row+int(ii[0]);a[[i,row]]=a[[row,i]];rs[i],rs[row]=rs[row],rs[i]
        pivot=int(a[row,col]);det=det*pivot%p;a[row]=a[row]*pow(pivot,-1,p)%p
        if row+1<len(a):a[row+1:]=(a[row+1:]-a[row+1:,col,None]*a[row,None,:])%p
        selected.append(rs[row]);row+=1
        if row==len(a):break
    return {'r':r,'j':j,'m':m,'prime':p,'seed':seed,'d':d,'K':K,'cuts':cuts,'rank':row,'selected_rows_in_order':selected,'selected_minor':det,'matrix':C.tolist()}

def main():
    all_results=[]
    for r in [5,6,7,8]:
        for gap in range(5):
            result=core(r,r+gap)
            all_results.append(result)
            print(r,gap,'rank',result['rank'],'minor',result['selected_minor'])
    Path('work/rectangular/border_ternary/jacobi_core_trials.json').write_text(json.dumps(all_results,indent=2)+'\n')

if __name__=='__main__':main()
