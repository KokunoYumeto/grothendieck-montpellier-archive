"""Deterministic theta bounds: exploratory floating-point implementation.

Uses the proved one-sided grid/cell inequalities, but this file alone
does not certify rounding or input truncation.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"]="1"
import itertools, json
import numpy as np
from scipy.special import erf
import fermat_theta_explore as f

T=np.array([[-1,(-1+1j)/2,(1+1j)/2],[-1,(1-1j)/2,-(1+1j)/2],[0,0,-1-1j]])
W=np.diag([0,-1+1j,1+1j])

def product_coeffs(D):
    vals=np.zeros((D,D,D),dtype=complex)
    for r in itertools.product(range(D),repeat=3):
        u=np.array(r)/D;z=T@u
        if D==4:
            ex=.5j*np.pi*np.einsum('ni,ij,nj->n',f.k,f.TAU,f.k)+2j*np.pi*(f.k@z)
            val=(f.coeff[f.parity]*np.exp(ex)).sum()
            vals[r]=np.exp(2j*np.pi*(u@W@u))*val
        else:
            ex=1j*np.pi*np.einsum('ni,ij,nj->n',f.grid,f.TAU,f.grid)+2j*np.pi*(f.grid@z)
            vals[r]=np.exp(1j*np.pi*(u@W@u))*np.exp(ex).sum()
    coeff=np.fft.fftn(vals)/D**3
    a=np.arange(-10,11)
    S=[np.exp(-D*np.pi*(a+r/D)**2).sum() for r in range(D)]
    for r in itertools.product(range(D),repeat=3):coeff[r]/=np.prod([S[t] for t in r])
    return coeff

def normalized_basis(D,us):
    vals=[]
    for r in range(D):
        k=np.arange(-D*8+r,D*8+1,D)
        vals.append(np.exp(-np.pi/D*(k[:,None]+D*us.imag[None,:])**2
                           +2j*np.pi*k[:,None]*us.real[None,:]).sum(axis=0))
    return np.array(vals).T

def contract(coeff,b0,b1,b2):
    v=np.einsum('abc,ia->ibc',coeff,b0,optimize=True)
    v=np.einsum('ibc,jb->ijc',v,b1,optimize=True)
    return np.einsum('ijc,kc->ijk',v,b2,optimize=True)

def cell_grams(n):
    out=np.zeros((n*n,4),dtype=complex)
    kvals=np.arange(-12,13)
    for ix in range(n):
        x=(ix+.5)/n-.5
        for iy in range(n):
            yl=iy/n-.5;yh=(iy+1)/n-.5
            for k in kvals:
                for l in kvals:
                    d=k-l;q=k+l
                    dx=np.exp(2j*np.pi*d*x)*np.sinc(d/n)
                    dy=n/4*(erf(2*np.sqrt(np.pi)*(yh+q/4))-erf(2*np.sqrt(np.pi)*(yl+q/4)))
                    out[ix*n+iy,(k%2)*2+l%2]+=np.exp(-np.pi*d*d/4)*dx*dy
    return out

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("--n",type=int,default=12);args=p.parse_args()
    n=args.n
    c4=product_coeffs(4);c2=product_coeffs(2)
    points=np.array([x/n+1j*y/n for x in range(n) for y in range(n)])
    offsets=[1/37+1j/41,2/43+3j/47,3/53+5j/59]
    bases=[normalized_basis(4,(points+u+.5+.5j)%(1+0j)) for u in []]
    bases=[]
    for u in offsets:
        z=points+u
        z=(z.real+.5)%1-.5+1j*((z.imag+.5)%1-.5)
        bases.append(normalized_basis(4,z))
    ph=contract(c4,*bases)
    k_grid=float(np.log(abs(ph)).mean()-4*np.log(2))
    k_lower=k_grid-6*np.log(2)/n**2
    del ph
    G=cell_grams(n)
    D=np.zeros((4,4,4),dtype=complex)
    for r in itertools.product(range(2),repeat=3):
        for s in itertools.product(range(2),repeat=3):
            D[tuple(2*rj+sj for rj,sj in zip(r,s))]=c2[r]*c2[s].conjugate()/np.sqrt(2)
    meanq=contract(D,G,G,G)
    h_upper=float(np.log(meanq.real).mean()/2)
    i_lower=k_lower-2*h_upper+3.5*np.log(2)
    a_lower=i_lower/7-f.logT/18-10*np.log(2)/63
    result={"status":"floating-point exploration of rigorous inequalities; not certified",
            "n":n,"points":n**6,"K_grid":k_grid,"K_lower":k_lower,"H_upper":h_upper,
            "I_lower":i_lower,"A_lower":a_lower,"min_cell_mean":float(meanq.real.min()),
            "max_imag_cell_mean":float(abs(meanq.imag).max())}
    print(json.dumps(result,indent=2),flush=True)
    from pathlib import Path
    Path(__file__).with_name("fermat_theta_grid.json").write_text(json.dumps(result,indent=2))
