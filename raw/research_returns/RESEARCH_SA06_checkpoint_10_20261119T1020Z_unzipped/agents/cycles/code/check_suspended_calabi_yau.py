"""Exact finite defining-data certificate for the all-dimensional C.3ai proof."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
eta,zeta,b=sp.symbols('eta zeta b')
pair_checks=[]
for degree in range(3,23):
    for multiplier in (eta,eta*zeta):
        expression=sp.expand((multiplier*b)**degree+b**degree)
        first=sp.rem(expression,eta**degree+1,eta)
        remainder=sp.rem(first,zeta**degree-1,zeta)
        assert sp.expand(remainder)==0
    determinant=sp.Matrix([[eta,eta*zeta],[1,1]]).det()
    assert sp.expand(determinant-eta*(1-zeta))==0
    pair_checks.append({'degree':degree,'both_pair_substitutions_zero':True,
                        'tangent_pair_determinant':str(determinant),
                        'nonzero_reason':'eta^degree=-1 and primitive zeta of degree>=3 imply eta!=0 and zeta!=1'})

cases=[]
for r in range(1,21):
    for N in range(r+2,2*r+2):
        d=2*r-N+2
        k=N-r-2
        e=d+2
        n=d+2*k
        assert d>=1 and k>=0
        assert r==d+k and N==n+2
        incidence_dimension=d+k
        incidence_codimension=d+n-incidence_dimension
        composite_codimension=2*incidence_codimension-n
        assert incidence_codimension==r and composite_codimension==d
        assert 2*(d+k)-n==d # transverse intersection dimension
        p,q=d+k-1,k-1
        assert p-q==d and p+q==n-2
        assert (q<0 if k==0 else p+q<n)
        cases.append({'r':r,'N':N,'d':d,'k':k,'fermat_degree':e,
                      'hypersurface_dimension':n,
                      'incidence_codimension':incidence_codimension,
                      'composite_codimension':composite_codimension,
                      'B_hodge_target':[p,q],
                      'vanishing_reason':'negative second Hodge index' if k==0 else 'off-diagonal projective-space cohomology below middle'})

record={'utc':datetime.now(timezone.utc).isoformat(),
        'sympy_version':sp.__version__,
        'all_checks_passed':True,
        'pair_checks':pair_checks,
        'range_cases':cases,
        'number_of_range_cases':len(cases),
        'scope':'Finite exact substitutions and degree bookkeeping. The written proof establishes the transverse integral correspondence identity, finite-data spread, Hodge contradiction and ordinary non-torsion for every dimension.',
        'runtime_seconds':time.perf_counter()-started}
text=json.dumps(record,indent=2)+'\n'
(base/'output/check_suspended_calabi_yau.json').write_text(text)
(base/'output/check_suspended_calabi_yau.out').write_text(text)
print(json.dumps({key:record[key] for key in ('utc','all_checks_passed','number_of_range_cases','runtime_seconds')},indent=2))
