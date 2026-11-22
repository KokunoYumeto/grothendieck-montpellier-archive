"""Exact rational residual coordinates for the three-unit norm13 candidate."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,traceback,signal
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1];out={'status':'RUNNING'}
def timeout(*unused):raise TimeoutError('Coordinate construction exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    source=json.loads((agent/'outputs/post_CP28_thirteen_three_anticommuting_probe.json').read_text())
    mod=[1,1,0,1,0,1,1,1,0,0,0,0,1]
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(mod));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    def encode(c):return sum(int(v)<<i for i,v in enumerate(c.to_list()))
    def poly(rows):
        d=max((int(e[1]) for e,c in rows),default=-1);cs=[K(0)]*(d+1)
        for e,c in rows:assert e[0]==0;cs[e[1]]=val(c)
        return R(cs)
    class Fr:
        def __init__(self,n=0,d=1):
            if isinstance(n,Fr):self.n,self.d=n.n,n.d;return
            n=n if isinstance(n,type(p)) else R(n if isinstance(n,list) else [n])
            d=d if isinstance(d,type(p)) else R(d if isinstance(d,list) else [d])
            assert not d.is_zero()
            if n.is_zero():self.n,self.d=R.zero(),R.one();return
            g=n.gcd(d);n=n//g;d=d//g;c=1/d.coeffs()[-1]
            self.n,self.d=n*c,d*c
        def __add__(self,o):
            o=Fr(o);return Fr(self.n*o.d+o.n*self.d,self.d*o.d)
        __sub__=__add__;__radd__=__add__
        def __rsub__(self,o):return self+o
        def __mul__(self,o):
            o=Fr(o);return Fr(self.n*o.n,self.d*o.d)
        __rmul__=__mul__
        def __truediv__(self,o):
            o=Fr(o);return Fr(self.n*o.d,self.d*o.n)
        def __pow__(self,n):return Fr(self.n**n,self.d**n)
        def serial(self):return {'numerator':[encode(c) for c in self.n.coeffs()],'denominator':[encode(c) for c in self.d.coeffs()]}
    cs=[poly(x) for x in source['coefficients']];l0,l1,l2,c1,c2,c3,c4=map(Fr,cs)
    A,B,C=map(poly,source['residual_coefficients'])
    L=Fr(B,A);Kap=Fr(C,A);M=Fr(p)**2+L*Fr(p)+Kap
    d0=l0+l2*Kap;d1=l1+l2*L
    n1=c1+c2*L+c3*(L**2+Kap)+c4*L**3
    n0=c2*Kap+c3*L*Kap+c4*(L**2*Kap+Kap**2)
    determinant=d0**2+d0*d1*L+d1**2*Kap
    nu=(d1*n0+d0*n1)/determinant
    # The finite Mumford chart must have no pole away from l2=0.
    denominator_residual=nu.d
    while True:
        g=denominator_residual.gcd(cs[2])
        if g.degree()==0:break
        denominator_residual=denominator_residual//g
    assert denominator_residual.degree()==0
    out.update({'status':'PASS_RATIONAL_COORDINATES_ONLY','field_modulus':mod,'parameter_z':source['parameter_z'],
      'coordinates':{'L':L.serial(),'M':M.serial(),'nu':nu.serial()},
      'l2':[encode(c) for c in cs[2].coeffs()],
      'residual_middle':[encode(c) for c in B.coeffs()],
      'residual_constant':[encode(c) for c in C.coeffs()],
      'degrees':{name:[int(f.n.degree()),int(f.d.degree())] for name,f in [('L',L),('M',M),('nu',nu)]},
      'scope':'Exact rational coordinates and denominator support only. Fibre cardinalities have not been established.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_three_unit_coordinates.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in out if k not in ['coordinates','l2','residual_middle','residual_constant']},indent=2))
