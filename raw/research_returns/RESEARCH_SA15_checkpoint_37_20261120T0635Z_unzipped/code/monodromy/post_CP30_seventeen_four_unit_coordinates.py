"""Residual coordinates and reduced pole algebra for the C0 four-unit norm17 model."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','models':[]}
def timeout(*unused):raise TimeoutError('Norm17 coordinate construction exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    source=json.loads((agent/'outputs/post_CP30_seventeen_four_unit_interpolation.json').read_text())
    assert source['status']=='PASS_FOUR_UNIT_INTERPOLATION_ONLY'
    modulus=[1,1,0,1,0,1,1,1,0,0,0,0,1]
    field=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(modulus));R=fq_default_poly_ctx(field);p=R.gen()
    val=lambda n:field([(n>>i)&1 for i in range(12)])
    enc=lambda x:sum(int(v)<<i for i,v in enumerate(x.to_list()))
    serial=lambda f:[enc(v) for v in f.coeffs()]
    def poly(rows):
        degree=max((int(e[1]) for e,c in rows),default=-1);cs=[field(0)]*(degree+1)
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
        def __add__(self,o):o=Fr(o);return Fr(self.n*o.d+o.n*self.d,self.d*o.d)
        __sub__=__add__;__radd__=__add__
        def __rsub__(self,o):return self+o
        def __mul__(self,o):o=Fr(o);return Fr(self.n*o.n,self.d*o.d)
        __rmul__=__mul__
        def __truediv__(self,o):o=Fr(o);return Fr(self.n*o.d,self.d*o.n)
        def __pow__(self,n):return Fr(self.n**n,self.d**n)
        def serial(self):return {'numerator':serial(self.n),'denominator':serial(self.d)}
    for model in [{'name':'zero_four_units','mu_encoded':0,'selected':source['selected']}]:
        data=model['selected'];cs=[poly(x) for x in data['coefficients']]
        l0,l1,l2,l3,c1,c2,c3,c4,c5=map(Fr,cs)
        A,B,C=map(poly,data['residual_coefficients'])
        L=Fr(B,A);Kap=Fr(C,A);M=Fr(p)**2+L*Fr(p)+Kap
        d0=l0+l2*Kap+l3*L*Kap;d1=l1+l2*L+l3*(L**2+Kap)
        n1=c1+c2*L+c3*(L**2+Kap)+c4*L**3+c5*(L**4+L**2*Kap+Kap**2)
        n0=c2*Kap+c3*L*Kap+c4*(L**2*Kap+Kap**2)+c5*L**3*Kap
        determinant=d0**2+d0*d1*L+d1**2*Kap
        nu=(d1*n0+d0*n1)/determinant
        den=nu.d
        while True:
            g=den.gcd(cs[3])
            if g.degree()==0:break
            den=den//g
        out['extra_ordinate_denominator']=serial(den)
        assert den.degree()==0,('Additional ordinate denominator',den.degree())
        pole_full=cs[3]
        pole=R.one()
        pole_factors=[]
        for factor,exponent in pole_full.factor()[1]:
            pole*=factor;pole_factors.append({'factor':serial(factor),'multiplicity':int(exponent)})
        n=pole.degree()
        assert pole.gcd(pole.derivative()).degree()==0
        assert pole.gcd(B).degree()==0 and pole.gcd(cs[8]).degree()==0
        assert (B+cs[8]*cs[8])%pole==R.zero()
        r0,r1=pole,B%pole;s0,s1=R.zero(),R.one()
        while not r1.is_zero():
            q,rem=divmod(r0,r1);r0,r1=r1,rem;s0,s1=s1,s0+q*s1
        assert r0.degree()==0
        inverse=s0*(1/r0.coeffs()[0])%pole
        value=(p+C*inverse)%pole
        powers=[R.one()]
        for i in range(n):powers.append(powers[-1]*value%pole)
        mat=[[powers[j][i] for j in range(n)]+[powers[n][i]] for i in range(n)]
        for j in range(n):
            pivot=next((i for i in range(j,n) if mat[i][j]!=field(0)),None)
            assert pivot is not None,(model['name'],'Pole x values collide')
            mat[j],mat[pivot]=mat[pivot],mat[j]
            scale=1/mat[j][j];mat[j]=[v*scale for v in mat[j]]
            for i in range(n):
                if i!=j and mat[i][j]!=field(0):
                    c=mat[i][j];mat[i]=[x+c*y for x,y in zip(mat[i],mat[j])]
        minimal=R([mat[j][-1] for j in range(n)]+[field(1)])
        assert minimal.gcd(minimal.derivative()).degree()==0
        evaluated=R.zero()
        for c in reversed(minimal.coeffs()):evaluated=(evaluated*value+R([c]))%pole
        assert evaluated.is_zero()
        row={'name':model['name'],'mu_encoded':model['mu_encoded'],'coordinates':{'L':L.serial(),'M':M.serial(),'nu':nu.serial()},
             'l2':serial(pole),'pole_full':serial(pole_full),'pole_factors':pole_factors,'residual_middle':serial(B),'residual_constant':serial(C),
             'degrees':{name:[int(f.n.degree()),int(f.d.degree())] for name,f in [('L',L),('M',M),('nu',nu)]},
             'pole_value':serial(value),'pole_minimal_polynomial':serial(minimal),'pole_krylov_rank':n,'pole_separable':True,'pole_squarefree_support_degree':n}
        out['models'].append(row)
        print(json.dumps({'model':row['name'],'degrees':row['degrees'],'pole_rank':n,'seconds':time.perf_counter()-start}),flush=True)
    out.update({'status':'PASS_FOUR_UNIT_COORDINATES_AND_POLES_ONLY','field_modulus':modulus,'scope':'Exact Mumford coordinates and distinct residual x values on the reduced pole support of the selected four-unit model. Nonpole fibre cardinalities and nodality remain unproved.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP30_seventeen_four_unit_coordinates.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='models'},indent=2))
