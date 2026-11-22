"""Retained exact F8 probe of the remaining norm-thirteen A=0 sector.

This is not a geometric or uniform nodality certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time, traceback
sys.path.insert(0, '/tmp/research_sa15_flint')
from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

start=time.perf_counter(); agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING'}
try:
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)([1,0,1,1]))
    R=fq_default_poly_ctx(K); X=R.gen(); z=K.gen()
    a=z*z; delta=z+1; b=a+z+1; e=1/(delta*delta)
    A=R([a,a+1,0,a*a+1,0,0,0,a*a])
    vals=[K([n>>i&1 for i in range(3)]) for n in range(8)]
    encode=lambda t: next(n for n,v in enumerate(vals) if v==t)
    encpoly=lambda f: [encode(c) for c in f.coeffs()]
    factors=[{'coefficients':encpoly(f),'exponent':int(n)} for f,n in A.factor()[1]]
    rows=[]
    for L,n in A.roots():
        H=a*a*L**6+(a*a+1)*L**2+(a+1)
        J=a*a*L**4+(a*a+1)
        j=a*L+delta**2; k=delta**4
        b2=J*e**2+a*a*e**4*j*j
        b1=1+H*e+a*a*e**4*k
        T=b1**3+j*j*b1*b2*b2+k*b2**3
        C=X**3+j*X*X+k
        d1change=a*L**4+b*L*L
        Fchange=a*L**4+delta**2*L*L+delta*L
        assert Fchange**2==a*L
        slopechange=d1change+L*Fchange
        Zrows=[]
        for Z,_ in C.roots():
            Zrows.append({'Z':encode(Z),'B':encode(b2*Z*Z+b1*Z),'denominator_zero':bool(Z==delta)})
        rows.append({'L':encode(L),'multiplicity':int(n),'b2':encode(b2),'b1':encode(b1),
                     'T':encode(T),'slopechange':encode(slopechange),
                     'C_factorization':[{'coefficients':encpoly(f),'exponent':int(n)} for f,n in C.factor()[1]],
                     'Z_roots':Zrows})
    out.update({'status':'PASS_FINITE_FIELD_PROBE_ONLY','modulus_binary_coefficients':[1,0,1,1],
                'parameter_z':2,'A_factorization':factors,'rows':rows,
                'scope':'Only exact arithmetic over F8. Factors of higher degree and all ordinate/fibre implications remain to be proved.'})
except Exception:
    out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_exceptional_field_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
