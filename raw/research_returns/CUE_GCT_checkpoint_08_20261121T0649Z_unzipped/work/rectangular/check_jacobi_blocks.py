"""Exact path/continuant coefficient model for endpoint Jacobi columns.

This is a finite diagnostic of the prospective uniform lower bound.
No rank at untested sizes is inferred from the output.
"""
import json
import sys
from pathlib import Path
import numpy as np

def rank(a,p):
    a=np.array(a,dtype=np.int64).copy()%p;r=0
    for c in range(a.shape[1]):
        ii=np.flatnonzero(a[r:,c])
        if not len(ii):continue
        i=r+int(ii[0]);a[[i,r]]=a[[r,i]];a[r]=a[r]*pow(int(a[r,c]),-1,p)%p
        if r+1<len(a):a[r+1:]=(a[r+1:]-a[r+1:,c,None]*a[r,None,:])%p
        r+=1
        if r==len(a):break
    return r

def main():
    m=int(sys.argv[1]);directory=Path(sys.argv[2]);p=1009
    old=directory/f'border_jacobi_mono_m{m}.json'
    if old.exists():
        data=json.loads(old.read_text());p=data['prime'];A=data['pencil_A'];alpha=[A[3*(m*i+i)] for i in range(m)];beta=[A[3*(m*i+i+1)+1] for i in range(m-1)];gamma=[A[3*(m*(i+1)+i)+2] for i in range(m-1)]
    else:
        alpha=[1]*m;beta=[1]*(m-1);gamma=[(17*i*i+29*i+7)%p or 1 for i in range(m-1)]
    intervals={}
    for a in range(m+1):
        intervals[a,a-1]=[1]
        if a<m:intervals[a,a]=[alpha[a]]
        for b in range(a+1,m):
            left=intervals[a,b-1];second=intervals[a,b-2];v=[0]*((b-a+1)//2+1)
            for k,c in enumerate(left):v[k]=(v[k]+alpha[b]*c)%p
            for k,c in enumerate(second):v[k+1]=(v[k+1]+beta[b-1]*gamma[b-1]*c)%p
            intervals[a,b]=v
    D=m+1;monos=[(a,b,D-a-b) for a in range(D,-1,-1) for b in range(D-a,-1,-1)];lookup={v:i for i,v in enumerate(monos)};C=np.zeros((len(monos),8*m+3),dtype=np.int64)
    def term(col,a,b,shift,scale=1):
        length=b-a+1
        for k,c in enumerate(intervals[a,b]):
            mon=(length-2*k+shift[0],k+shift[1],k+shift[2]);C[lookup[mon],col]=(C[lookup[mon],col]+scale*c)%p
    def product(v,a,b):
        r=1
        for i in range(a,b):r=r*v[i]%p
        return r
    B=[product(beta,0,i) for i in range(m)];G=[product(gamma,i,m-1) for i in range(m)];E=[product(gamma,0,i) for i in range(m)];F=[product(beta,i,m-1) for i in range(m)]
    units=[(1,0,0),(0,1,0),(0,0,1)]
    for k,e in enumerate(units):term(k,0,m-1,e)
    for i in range(m):
        for k,e in enumerate(units):
            term(3+3*i+k,i+1,m-1,(e[0]+1,e[1]+i,e[2]),B[i])
            term(3+3*i+k,0,i-1,(e[0],e[1],e[2]+m-i),G[i])
            term(3+3*m+3*i+k,i+1,m-1,(e[0]+1,e[1],e[2]+i),E[i])
            term(3+3*m+3*i+k,0,i-1,(e[0],e[1]+m-i,e[2]),F[i])
        if i>0:term(6*m+3+i,1,i-1,(2,0,m-i),2*G[i])
        if i<m-1:term(6*m+3+i,i+1,m-2,(1,i+1,1),2*B[i])
        if i>0:term(7*m+3+i,1,i-1,(2,m-i,0),2*F[i])
        if i<m-1:term(7*m+3+i,i+1,m-2,(1,1,i+1),2*E[i])
    checked=0
    if old.exists():
        J=np.fromfile(old.with_suffix('.u16'),dtype='<u2').reshape(data['rows'],data['columns'])
        for i,pt in enumerate(data['points']):
            ev=np.array([pow(pt[0],a,p)*pow(pt[1],b,p)*pow(pt[2],c,p)%p for a,b,c in monos],dtype=np.int64)
            assert np.all(ev@C%p==J[i]);checked+=C.shape[1]
    block=[]
    for r in range(m):
        rows=[i for i,(a,b,c) in enumerate(monos) if (b-c)%m==r]
        cols=[j for j in range(C.shape[1]) if np.any(C[rows,j])]
        block.append({'character':r,'rows':len(rows),'active_columns':len(cols),'rank':rank(C[rows,:],p)})
    out={'m':m,'prime':p,'rank':sum(b['rank'] for b in block),'target_8m_minus4':8*m-4,'entries_checked_against_DP':checked,'blocks':block}
    (directory/f'jacobi_blocks_m{m}.json').write_text(json.dumps(out,indent=2)+'\n');np.save(directory/f'jacobi_coefficients_m{m}.npy',C)
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
