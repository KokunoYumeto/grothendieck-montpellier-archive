#!/usr/bin/env python3
"""Independent numerical checks of the pants radius formula.

These are diagnostics, not a proof of positivity or injectivity.  The proof is
the moving-seam identity in sections/part_a2b_secondary.tex.  The formula uses
continuous log Gamma, not the principal logarithm of a Gamma quotient.
"""
from pathlib import Path
import json, math, time
import numpy as np
from scipy.special import loggamma, digamma

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
SEED = 22021119
rng = np.random.default_rng(SEED)

def f(t):
    return float(loggamma(0.5 + 0.5j*t).imag)

def fp(t):
    return 0.5*float(digamma(0.5 + 0.5j*t).real)

def radii_and_hessian(lam):
    values = np.empty(3)
    H = np.empty((3,3))
    for i in range(3):
        js = [j for j in range(3) if j != i]
        x,y,z = lam[i],lam[js[0]],lam[js[1]]
        terms = [(x+a*y+b*z,a,b) for a in (-1,1) for b in (-1,1)]
        G = float(loggamma(1+1j*x).imag)
        Gp = float(digamma(1+1j*x).real)
        values[i] = (-math.pi/2 + 2*G - sum(f(t) for t,a,b in terms))/x
        H[i,i] = (2*Gp-sum(fp(t) for t,a,b in terms)-values[i])/(2*x*x)
        H[i,js[0]] = -sum(a*fp(t) for t,a,b in terms)/(2*x*y)
        H[i,js[1]] = -sum(b*fp(t) for t,a,b in terms)/(2*x*z)
    return values,H

samples = [10**rng.uniform(-3,2,3) for _ in range(1200)]
samples += [np.array(v,dtype=float) for v in
            [(1,1,1),(10,10,10),(100,100,100),(2,1,1),
             (2.000001,1,1),(1.999999,1,1),(100,1,.001),
             (.001,100,1),(1,.001,100)]]
worst = None
max_symmetry = 0.0
positive = 0
finite_difference_max = 0.0
for lam in samples:
    val,H = radii_and_hessian(lam)
    scale = np.sqrt(np.maximum(np.diag(H),np.finfo(float).tiny))
    normalized = H/np.outer(scale,scale)
    eig = np.linalg.eigvalsh((normalized+normalized.T)/2)
    max_symmetry = max(max_symmetry,float(np.max(np.abs(normalized-normalized.T))))
    if eig[0] > 0:
        positive += 1
    rec = {'lambda':lam.tolist(),'log_radii':val.tolist(),
           'normalized_eigenvalues':eig.tolist()}
    if worst is None or eig[0] < worst['normalized_eigenvalues'][0]:
        worst = rec

# Independently check analytic derivatives away from extremely ill-conditioned
# scales.  Differentiate with respect to s=lambda^2.
for _ in range(30):
    lam = 10**rng.uniform(-.6,.6,3)
    val,H = radii_and_hessian(lam)
    s = lam*lam
    numerical = np.empty((3,3))
    for j in range(3):
        step = 2e-5*s[j]
        plus=s.copy(); minus=s.copy()
        plus[j]+=step; minus[j]-=step
        numerical[:,j]=(radii_and_hessian(np.sqrt(plus))[0]-
                        radii_and_hessian(np.sqrt(minus))[0])/(2*step)
    finite_difference_max=max(finite_difference_max,
        float(np.max(np.abs(numerical-H)/(1+np.abs(H)))))

pair_min = math.inf
for _ in range(600):
    a,b = 10**rng.uniform(-2,1.5,(2,3))
    fa = radii_and_hessian(a)[0]
    fb = radii_and_hessian(b)[0]
    pairing = float(np.dot(a*a-b*b,fa-fb))
    pair_min = min(pair_min,pairing)
    assert pairing > 0, (a,b,fa,fb,pairing)

output = {
    'purpose':'Numerical diagnostic only; analytic proof is the energy identity.',
    'seed':SEED,
    'formula_source':'Firat 2023 body eqs 3maprad/v_func; continuous loggamma branch',
    'floating_type':'IEEE 754 float64; scipy.special.loggamma/digamma',
    'sample_count':len(samples),'positive_normalized_hessian_count':positive,
    'worst_normalized_hessian_sample':worst,
    'max_normalized_symmetry_residual':max_symmetry,
    'max_scaled_finite_difference_residual':finite_difference_max,
    'random_strict_monotonicity_pairs':600,
    'minimum_monotonicity_pairing':pair_min,
    'runtime_seconds':time.perf_counter()-START,
}
dest=ROOT/'code'/'part_a2b_checks_output.json'
dest.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
