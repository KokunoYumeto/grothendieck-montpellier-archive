"""Exact pole-fibre algebra for the three-unit norm-thirteen candidate."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1];out={'status':'RUNNING'}
try:
    d=json.loads((agent/'outputs/post_CP28_thirteen_three_unit_coordinates.json').read_text())
    ip=json.loads((agent/'outputs/post_CP28_thirteen_three_anticommuting_probe.json').read_text())
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(d['field_modulus']));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    enc=lambda c:sum(int(v)<<i for i,v in enumerate(c.to_list()))
    dec=lambda a:R([val(v) for v in a]);serial=lambda f:[enc(c) for c in f.coeffs()]
    l2=dec(d['l2']);B=dec(d['residual_middle']);C=dec(d['residual_constant'])
    c4=R([K(0)])
    for e,c in ip['coefficients'][6]:c4+=p**e[1]*val(c)
    assert l2.degree()==8 and l2.gcd(l2.derivative()).degree()==0
    assert l2.gcd(B).degree()==0 and l2.gcd(c4).degree()==0
    assert (B+c4*c4)%l2==R.zero()
    def inverse(a):
        r0,r1=l2,a%l2;s0,s1=R.zero(),R.one()
        while not r1.is_zero():
            q,r=divmod(r0,r1);r0,r1=r1,r;s0,s1=s1,s0+q*s1
        assert r0.degree()==0
        return s0*(1/r0.coeffs()[0])%l2
    value=(p+C*inverse(B))%l2
    powers=[R.one()]
    for i in range(8):powers.append(powers[-1]*value%l2)
    n=8;mat=[[powers[j][i] for j in range(n)]+[powers[n][i]] for i in range(n)]
    pivots=[]
    for j in range(n):
        row=next((i for i in range(j,n) if mat[i][j]!=K(0)),None)
        assert row is not None,'Pole value fails to generate the eight-dimensional algebra.'
        mat[j],mat[row]=mat[row],mat[j];scale=1/mat[j][j]
        mat[j]=[v*scale for v in mat[j]]
        for i in range(n):
            if i!=j and mat[i][j]!=K(0):
                c=mat[i][j];mat[i]=[x+c*y for x,y in zip(mat[i],mat[j])]
        pivots.append(j)
    polynomial=R([mat[j][-1] for j in range(n)]+[K(1)])
    assert polynomial.gcd(polynomial.derivative()).degree()==0
    evaluated=R.zero()
    for c in reversed(polynomial.coeffs()):evaluated=(evaluated*value+R([c]))%l2
    assert evaluated.is_zero()
    out.update({'status':'PASS_POLE_FIBRE_ALGEBRA','l2':serial(l2),'pole_value':serial(value),
                'minimal_polynomial':serial(polynomial),'krylov_rank':8,'separable':True,
                'scope':'The eight distinct roots of l2 have pairwise distinct residual-point x coordinates. This is a pole-fibre algebra certificate; the complete nodality proof remains separate.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_pole_fibres.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
