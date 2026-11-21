"""Deterministic exact elimination certificate for the three boundary jets."""
import json
from pathlib import Path
import numpy as np

def certificate(a,p):
    a=a.copy()%p;nr,nc=a.shape;names=list(range(nr));r=0;rows=[];cols=[];det=1
    for c in range(nc):
        ii=np.flatnonzero(a[r:,c])
        if not len(ii):continue
        i=r+int(ii[0]);a[[i,r]]=a[[r,i]];names[i],names[r]=names[r],names[i]
        v=int(a[r,c]);det=det*v%p;a[r]=a[r]*pow(v,-1,p)%p
        if r+1<nr:a[r+1:]=(a[r+1:]-a[r+1:,c,None]*a[r,None,:])%p
        rows.append(names[r]);cols.append(c);r+=1
        if r==nr:break
    return {'shape':[nr,nc],'rank':r,'ordered_selected_rows':rows,'selected_columns':cols,
            'selected_minor_mod101':det,'remaining_rows_zero':bool(not np.any(a[r:]))}

def main():
    directory=Path('work/rectangular/border_ternary');d=np.load(directory/'jacobi_boundary_repair_m17.npz');Cs=[d['C0'],d['C1'],d['C2']];R,C=Cs[0].shape;results=[]
    for s in range(3):
        T=np.zeros(((s+1)*R,(s+1)*C),dtype=np.int64)
        for i in range(s+1):
            for j in range(i+1):T[i*R:(i+1)*R,j*C:(j+1)*C]=Cs[i-j]
        r=certificate(T,101);r['jet_order']=s;results.append(r)
        print(s,r['shape'],r['rank'],r['selected_minor_mod101'],r['remaining_rows_zero'])
    (directory/'boundary_toeplitz_certificates.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
