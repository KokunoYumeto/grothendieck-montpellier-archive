"""Exploratory theta integration only: no certified logarithmic quadrature.

Period matrix: Guardia2001 Proposition5 + exact Landen specialization.
Frobenius normalization: deJong2020 Theorem4.1, absolute value at a two-torsion point.
This script reports numerical evidence, not a proof of the height gate.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import json
from pathlib import Path
import itertools
import numpy as np
from scipy.stats import qmc

TAU=np.array([[.5+1j,-.5,-.5-.5j],[-.5,.5+1j,.5+.5j],[-.5-.5j,.5+.5j,1+1j]])
X,Y=TAU.real,TAU.imag
grid=np.array(list(itertools.product(range(-7,8),repeat=3)),dtype=float)
chars=list(itertools.product(range(2),repeat=6))
even=[c for c in chars if sum(c[j]*c[j+3] for j in range(3))%2==0]
thetanulls={}
for ch in even:
    p=np.array(ch[:3])/2
    q=np.array(ch[3:])/2
    v=grid+p
    thetanulls[ch]=np.exp(1j*np.pi*np.einsum('ni,ij,nj->n',v,TAU,v)+2j*np.pi*(v@q)).sum()
logT=sum(np.log(abs(t)) for t in thetanulls.values())

ki=np.array(list(itertools.product(range(-12,13),repeat=3)),dtype=int)
quad=np.einsum('ni,ij,nj->n',ki,Y,ki)
ki=ki[quad<=100]
k=ki.astype(float)
parity=(ki[:,0]%2)*4+(ki[:,1]%2)*2+(ki[:,2]%2)
e0=np.exp(.5j*np.pi*np.einsum('ni,ij,nj->n',k,TAU,k))
constraints=[]
for weights in [np.ones(len(k))]+[k[:,i]*k[:,j] for i in range(3) for j in range(i,3)]:
    constraints.append(np.array([(weights*e0)[parity==p].sum() for p in range(8)]))
mat=np.array(constraints)
u,s,vh=np.linalg.svd(mat)
coeff=vh[-1].conj()
phi_half=np.dot(coeff[parity],e0*((-1.)**ki[:,0]))
h_abs=np.prod([abs(v) for ch,v in thetanulls.items() if ch[0]==1])
coeff*=h_abs/abs(phi_half)
residual=float(np.max(abs(mat@coeff)))

ni=np.array(list(itertools.product(range(-8,9),repeat=3)),dtype=int)
quad=np.einsum('ni,ij,nj->n',ni,Y,ni)
ni=ni[quad<=40]
n=ni.astype(float)
phase_phi=.5*np.pi*np.einsum('ni,ij,nj->n',k,X,k)
phase_theta=np.pi*np.einsum('ni,ij,nj->n',n,X,n)

def integrand(points):
    xx=points[:,:3]-.5
    yy=points[:,3:]-.5
    re=xx+yy@X
    result=[]
    for start in range(0,len(points),128):
        re_b=re[start:start+128]
        yb=yy[start:start+128]
        v=k[:,None,:]+2*yb[None,:,:]
        decay=-.5*np.pi*np.einsum('nbi,ij,nbj->nb',v,Y,v)
        phase=phase_phi[:,None]+2*np.pi*(k@re_b.T)
        ph=(coeff[parity,None]*np.exp(decay+1j*phase)).sum(axis=0)
        v=n[:,None,:]+yb[None,:,:]
        decay=-np.pi*np.einsum('nbi,ij,nbj->nb',v,Y,v)
        phase=phase_theta[:,None]+2*np.pi*(n@re_b.T)
        th=np.exp(decay+1j*phase).sum(axis=0)
        result.extend((np.log(abs(ph))-2*np.log(abs(th))).tolist())
    return np.array(result)

if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--power",type=int,default=12)
    parser.add_argument("--replicates",type=int,default=4)
    args=parser.parse_args()
    rows=[]
    for seed in range(args.replicates):
        values=integrand(qmc.Sobol(6,scramble=True,seed=seed).random_base2(args.power))
        I=float(values.mean())
        A=I/7-logT/18-10*np.log(2)/63
        rows.append({"seed":seed,"points":len(values),"I_mean":I,"A_estimate":float(A),
                     "sample_min":float(values.min()),"sample_max":float(values.max())})
        print(json.dumps(rows[-1]),flush=True)
    output={"status":"exploratory, not certified","tau_real":X.tolist(),"tau_imag":Y.tolist(),
            "Y_eigenvalues":np.linalg.eigvalsh(Y).tolist(),"log_abs_T":float(logT),
            "gamma00_constraint_residual":residual,"singular_values":s.tolist(),
            "phi_modes":len(k),"theta_modes":len(n),"rows":rows}
    path=Path(__file__).with_name("fermat_theta_explore.json")
    path.write_text(json.dumps(output,indent=2))
    print("Wrote",path,flush=True)
