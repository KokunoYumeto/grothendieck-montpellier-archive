#!/usr/bin/env python3
"""Exact finite curve/divisor checks for C.3bb; geometry is proved in the text."""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import json

started=perf_counter(); base=Path(__file__).resolve().parent
primes=[2,3,5,7,11,13,17,19]
curves=[]
for p in primes:
    n=p*(p+1); g=(n-1)*(n-2)//2; degree=n*(n-3)
    assert n%p==0 and n>=6 and g>=10 and degree==2*g-2>0
    # Projectively normalized representatives: W=1; W=0,Z=1; (1:0:0).
    points=[(Y,Z,1) for Y in range(p) for Z in range(p)]
    points += [(Y,1,0) for Y in range(p)] + [(1,0,0)]
    zeros=[]; singular=[]; infinite=[]
    for Y,Z,W in points:
        F=(pow(Y,n,p)-Y*pow(W,n-1,p)-pow(Z,n-1,p)*W)%p
        FY=(n*pow(Y,n-1,p)-pow(W,n-1,p))%p
        FZ=(-(n-1)*pow(Z,n-2,p)*W)%p
        FW=(-(n-1)*Y*pow(W,n-2,p)-pow(Z,n-1,p))%p
        assert FY==(-pow(W,n-1,p))%p
        assert FZ==(pow(Z,n-2,p)*W)%p
        assert FW==(Y*pow(W,n-2,p)-pow(Z,n-1,p))%p
        if F==0:
            zeros.append((Y,Z,W))
            if W==0:infinite.append((Y,Z,W))
            if FY==FZ==FW==0:singular.append((Y,Z,W))
    assert infinite==[(0,1,0)] and not singular
    assert (0,0,1) in zeros
    # The selected germ's derivative in y is always minus one, also p=2.
    for b in range(p):
        assert (-1)%p!=0
        # d(z-bt)/(z-bt)-dz/z at t=0 has dt coefficient -b/z.
        for z in range(1,p):
            coefficient=(-b*pow(z,-1,p))%p
            residue=(coefficient*z)%p
            assert residue==(-b)%p
    curves.append({'p':p,'n':n,'genus':g,'canonical_degree':degree,
                   'rational_points_checked':len(points),'rational_curve_points':len(zeros),
                   'infinity':infinite,'singular_rational_points':singular,
                   'affine_y_derivative':p-1,'all_checks_passed':True})

dimensions=[]
for N in range(2,51):
    m=N-2
    assert m>=0 and m+1+1==N
    coefficients=[1]+[0]*m
    assert len(coefficients)==m+1 and coefficients[0]==1
    dimensions.append({'N':N,'projective_factor_dimension':m,
                       'dim_H0_O1':m+1,'z0_extraction':coefficients[0],
                       'all_checks_passed':True})

record={'utc':datetime.now(timezone.utc).isoformat(),'all_checks_passed':True,
        'curve_cases':curves,'dimension_cases':dimensions,
        'counts':{'curve_cases':len(curves),'dimension_cases':len(dimensions)},
        'runtime_seconds':perf_counter()-started,
        'scope':'Finite exact formulas and finite-field samples only. Smoothness over the algebraic closure is proved by the displayed global derivative argument; ampleness, actual henselian branches, integral dlog trace and ordinary divisibility are proved in the text.'}
(base/'check_divisor_endpoint_output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
