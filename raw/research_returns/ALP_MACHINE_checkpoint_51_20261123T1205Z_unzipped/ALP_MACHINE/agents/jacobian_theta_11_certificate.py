#!/usr/bin/env python3
"""Exact finite arithmetic certificate used in AM-K013 (no asymptotic extrapolation)."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import sympy as sp
from jacobian_theta_direction_jets import jets

root=Path(__file__).resolve().parent
table_path=root/'jacobian_theta_direction_jets_mod11.json'
table=json.loads(table_path.read_text())
z=sp.Symbol('z')
phi=sum(z**i for i in range(7))
assert table['prime']==11 and table['max_order']>=122
rows=[]
for i,q in ((1,11),(2,121),(3,11)):
    R,h,S=jets(i,q+1,11)
    assert h[q+1]==R.zero
    assert all(h[n]==R.zero for n in range(1,q+2,2))
    logged=table['directions'][str(i)]
    assert str(q+1) not in logged['log_derivatives']
    expected=list(range(0,q,2))
    observed=list(map(int,logged['theta_derivatives']))
    assert observed==expected,(i,observed,expected)
    for n,coeff in logged['theta_derivatives'].items():
        f=sum(int(v)*z**j for j,v in enumerate(coeff))
        assert sp.degree(sp.gcd(f,phi,modulus=11))==0,(i,n)
    for n,c in enumerate(h):
        saved=tuple(int(v) for v in logged['log_derivatives'].get(str(n),['0']*6))
        assert c==saved,(i,n,c,saved)
    for n,c in enumerate(S):
        saved=tuple(int(v) for v in logged['theta_derivatives'].get(str(n),['0']*6))
        assert c==saved,(i,n,c,saved)
    rows.append({'direction':i,'q':q,'exceptional_log_derivative_order':q+1,
                 'exceptional_log_derivative_mod11':[0]*6,
                 'regenerated_all_coefficients_through':q+1,
                 'saved_nonzero_theta_orders_are_units_at_both_primes':expected,
                 'scope':'Finite exact check; the infinite bound requires AM-K013 stable-ring and Bell proofs.'})
result={'checked_utc':datetime.now(timezone.utc).isoformat(),
        'prime':11,'residue_algebra':'F11[Z]/Phi7(Z)',
        'Phi7_factorization_mod11':str(sp.factor(phi,modulus=11)),
        'claims':rows,
        'table_sha256':hashlib.sha256(table_path.read_bytes()).hexdigest(),
        'recurrence_sha256':hashlib.sha256((root/'jacobian_theta_direction_jets.py').read_bytes()).hexdigest(),
        'status':'PASS'}
(root/'jacobian_theta_11_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
