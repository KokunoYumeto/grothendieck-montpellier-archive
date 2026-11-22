#!/usr/bin/env python3
"""Numerical exploration, not a proof, of continuous-branch pants radii.

Source: Firat (2021), equations (3.21), (3.35); Firat (2023), (4.1)-(4.3).
We use a continuous log-Gamma branch with v_i -> pi as lambda_i -> 0.
Lengths are L_i=2*pi*lambda_i. This program never certifies global injectivity.
"""
import itertools,json,time
import mpmath as mp
mp.mp.dps=40

def F(x): return mp.im(mp.loggamma((1+1j*x)/2))
def G(x): return mp.im(mp.loggamma(1+1j*x))
def log_radius(v,i):
    a=v[i];b=v[(i+1)%3];c=v[(i+2)%3]
    return (-mp.pi/2+2*G(a)-sum(F(a+s*b+t*c) for s in [-1,1] for t in [-1,1]))/a
def rs(v):return [mp.exp(log_radius(v,i)) for i in range(3)]
def jacobian_x(v):
    return mp.matrix([[mp.diff(lambda t:log_radius([t if k==j else v[k] for k in range(3)],i),v[j])/(2*v[j]) for j in range(3)] for i in range(3)])

if __name__=='__main__':
    start=time.monotonic()
    vals=[mp.mpf(x) for x in ['0.05','0.2','1','4','20']]
    rows=[];minimum=None;worst_asym=mp.mpf('0');negative=[]
    for v in itertools.product(vals,repeat=3):
        J=jacobian_x(v);asym=max(abs(J[i,j]-J[j,i]) for i in range(3) for j in range(3));worst_asym=max(worst_asym,asym)
        ev=mp.eigsy((J+J.T)/2,eigvals_only=True);e=ev[0]
        minimum=e if minimum is None else min(minimum,e)
        if e<=0:negative.append({'lambda':list(map(str,v)),'least_eigenvalue':str(e)})
        rows.append({'lambda':list(map(str,v)),'radii':list(map(str,rs(v))),'eigenvalues':list(map(str,ev))})
    special=[{'lambda1':str(x),'r0_two_cusps':str(mp.exp(log_radius([x,mp.mpf('0'),mp.mpf('0')],0)))} for x in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('1'),mp.mpf('10'),mp.mpf('100')]]
    print(json.dumps({'status':'exploratory; floating-point, no interval certification','precision_digits':mp.mp.dps,'sample_count':len(rows),'minimum_sample_eigenvalue':str(minimum),'max_asymmetry':str(worst_asym),'nonpositive_samples':negative,'two_cusp_samples':special,'rows':rows,'runtime_seconds':time.monotonic()-start},indent=2))
