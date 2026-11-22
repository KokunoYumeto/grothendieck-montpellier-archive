"""Rigorous finite-rank/Arb certificate for NN-A017 adjacent CUE agreement.

The sine operator on an interval of length s is T T*, where T has Fourier
kernel exp(2*pi*i*x*xi), xi in[-1/2,1/2]. Replace this kernel by its degree-p
Taylor polynomial on the centered interval. A uniform Taylor remainder
gives a Hilbert-Schmidt error and then a trace-norm determinant error.
All matrix operations below use Arb real balls. No quadrature is used.
"""
from flint import arb, arb_mat, ctx
from pathlib import Path
import json, math

ctx.dps=160
p=100
pi=arb.pi()
rows=[]
gaps=[]
for s in range(1,7):
    ds=[arb(1)]
    for k in range(1,p+1): ds.append(ds[-1]*(2*pi*s)/k)
    determinant=arb(1)
    for parity in (0,1):
        inds=list(range(parity,p+1,2))
        n=len(inds)
        G=arb_mat(n,n)
        C=arb_mat(n,n)
        for a,k in enumerate(inds):
            for b,l in enumerate(inds):
                g=arb(1)/(2**(k+l)*(k+l+1))
                G[a,b]=g
                sign=1 if ((k-l)//2)%2==0 else -1
                C[a,b]=sign*ds[k]*ds[l]*g
        Q=s*(C*G)
        for a in range(n):
            for b in range(n): Q[a,b]=(1 if a==b else 0)-Q[a,b]
        determinant*=Q.det()
    h=pi*s/2
    rem=h.exp()*h**(p+1)/math.factorial(p+1)
    trace_error=s*rem*(2+rem)
    # Safe standard determinant-continuity majorant. The proof file also
    # derives it by finite-dimensional exterior estimates and trace limits.
    det_error=trace_error*(1+s+s*(1+rem)**2).exp()
    gap=determinant+arb(0,det_error.upper())
    assert gap>0 and gap<1
    gaps.append(gap)
    rows.append(dict(s=s,finite_rank_determinant=str(determinant),
                     trace_norm_error_bound=str(trace_error),
                     determinant_error_bound=str(det_error),gap_probability=str(gap)))

S5=sum((1 if k%2==0 else -1)*gaps[k] for k in range(5))
S6=S5-gaps[5]
lower=(1-2*S5).lower()
upper=(1-2*S6).upper()
assert lower>arb('0.66654660183721072003')
assert upper<arb('0.66654660183721072008')
out=dict(arithmetic='FLINT/Arb160 decimal digits',taylor_degree=p,
         determinant_data=rows,
         agreement_lower=str(lower),agreement_upper=str(upper),
         method='Odd/even alternating partial sums through5 and6; E(s) is decreasing to0.',
         scope='Limiting marked-CUE model, fixed exterior radius r<1; no arithmetic label-law claim.')
dest=Path(__file__).with_name('cue_agreement_certificate.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'agreement_lower':str(lower),'agreement_upper':str(upper),
                  'gap_probabilities':[str(x) for x in gaps]},indent=2))
