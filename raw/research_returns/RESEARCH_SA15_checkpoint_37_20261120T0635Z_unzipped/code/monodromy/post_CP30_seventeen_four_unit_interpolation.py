"""C0 norm17 interpolation for 1+2(g1+g2+g3+g4), exploratory only."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import combinations,permutations
import json,time,traceback,signal
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','attempts':[],'stages':[]}
def timeout(*unused):raise TimeoutError('Four-unit norm17 interpolation exceeded60seconds')
def stage(name,**kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw}
    out['stages'].append(row);print(json.dumps(row),flush=True)
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    modulus=0x10eb
    def mul(x,y):
        r=0
        while y:
            if y&1:r^=x
            y>>=1;x<<=1
            if x>>12:x^=modulus
        return r
    def power(x,n):
        r=1
        while n:
            if n&1:r=mul(r,x)
            x=mul(x,x);n>>=1
        return r
    AS={}
    for x in range(4096):AS.setdefault(mul(x,x)^x,x)
    autos=[]
    for s in range(1,4096):
        v=power(s,4);u=mul(v,v)
        if mul(u,u)!=s or power(s,5) not in AS:continue
        if mul(u,power(s,2))^mul(v,s)!=1:continue
        for beta in (AS[power(s,5)],AS[power(s,5)]^1):autos.append((s,u,v,beta))
    def comm(g,h):
        s,u,v,_=g;t,U,V,_=h
        return mul(u,mul(t,t))^mul(v,t)^mul(U,mul(s,s))^mul(V,s)
    quadruples=[row for row in combinations(autos,4) if all(comm(g,h)==1 for g,h in combinations(row,2))]
    assert quadruples
    cc=symbols('c');K=MonogenicFiniteExtension(Poly(cc**12+cc**7+cc**6+cc**5+cc**3+cc+1,cc,modulus=2))
    K.gcd=lambda x,y:K.one if x or y else K.zero;K.quo=K.exquo=lambda x,y:x/y
    powers=[K.generator**i for i in range(12)]
    convert=lambda n:sum((powers[i] for i in range(12) if n>>i&1),K.zero)
    encode=lambda v:sum(int(c)<<i for i,c in enumerate(reversed(v.rep.to_list())))
    R,X,p=ring('X,p',K);cv=R.ground_new
    stage('four_units_available',order_four_count=len(autos),quadruple_count=len(quadruples))
    selected=None
    for seed,gi in enumerate(quadruples[:20]):
        gs=[tuple(convert(v) for v in g) for g in gi]
        shifts=[g[0] for g in gs]
        ys=[p*p*g[1]+p*g[2]+cv(g[3]) for g in gs]
        derivs=[(p+cv(s))**4 for s in shifts]
        matrix=[[K.one,s*s,s**4]+[K.one if i==j else K.zero for j in range(3)] for i,s in enumerate(shifts[:3])]
        for j in range(3):
            pivot=next(i for i in range(j,3) if matrix[i][j]!=K.zero)
            matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
            v=1/matrix[j][j];matrix[j]=[x*v for x in matrix[j]]
            for i in range(3):
                if i!=j:
                    v=matrix[i][j];matrix[i]=[x+v*y for x,y in zip(matrix[i],matrix[j])]
        inverse=[row[3:] for row in matrix]
        def ell(ls,s):return sum((ls[i]*s**i for i in range(4)),R.zero)
        def coefficients(ls):
            F=[(ls[1]+ls[3]*s*s)*Y+ell(ls,s)*D for s,Y,D in zip(shifts,ys,derivs)]
            c1,c3,c5=[sum((F[j]*inverse[i][j] for j in range(3)),R.zero) for i in range(3)]
            values=[ell(ls,s)*Y+c1*s+c3*s**3+c5*s**5 for s,Y in zip(shifts,ys)]
            s,t=shifts[:2]
            c4=(values[1]*s*s+values[0]*t*t)/(s*s*t**4+s**4*t*t)
            c2=(values[0]+c4*s**4)/(s*s)
            return F,values,[c1,c2,c3,c4,c5]
        rows=[[],[],[]]
        for j in range(4):
            ls=[R.one if i==j else R.zero for i in range(4)]
            F,values,cs=coefficients(ls);c1,c2,c3,c4,c5=cs;s=shifts[3]
            rows[0].append(F[3]+c1+c3*s*s+c5*s**4)
            for i in (2,3):rows[i-1].append(values[i]+c2*shifts[i]**2+c4*shifts[i]**4)
        ls=[]
        for omitted in range(4):
            columns=[j for j in range(4) if j!=omitted]
            determinant=R.zero
            for perm in permutations(range(3)):
                determinant+=rows[0][columns[perm[0]]]*rows[1][columns[perm[1]]]*rows[2][columns[perm[2]]]
            ls.append(determinant)
        if not any(ls):out['attempts'].append({'seed':seed,'status':'ZERO_MAXIMAL_MINORS'});continue
        common=next(x for x in ls if x)
        for x in ls:
            if x:common=common.gcd(x)
        record={'seed':seed,'automorphisms_encoded':[list(g) for g in gi],'minor_degrees':[x.degree(p) for x in ls],'common_degree':common.degree(p)}
        out['attempts'].append(record)
        if common.degree(p)>0:continue
        F,values,cs=coefficients(ls);c1,c2,c3,c4,c5=cs
        linear=sum((ls[i]*X**i for i in range(4)),R.zero)
        polynomial=sum((cs[i]*X**(i+1) for i in range(5)),R.zero)
        for s,Y,D in zip(shifts,ys,derivs):
            assert not (linear.compose(X,cv(s))*Y+polynomial.compose(X,cv(s)))
            assert not ((ls[1]+ls[3]*s*s)*Y+linear.compose(X,cv(s))*D+c1+c3*s*s+c5*s**4)
        norm=polynomial**2+linear*polynomial+linear**2*((p+X)**5+p**5)
        prescribed=X
        for s in shifts:prescribed*=(X+cv(s))**2
        quotient,remainder=norm.div(prescribed)
        assert not remainder and quotient.degree(X)==2
        extract=lambda i:R.from_dict({(0,ep):v for (ex,ep),v in quotient.items() if ex==i})
        residual=[extract(i) for i in (2,1,0)]
        assert residual[0]==ls[3]**2
        serial=lambda f:[[list(m),encode(v)] for m,v in f.terms()]
        selected={**record,'coefficients':[serial(f) for f in ls+cs],'raw_rows':[[serial(f) for f in row] for row in rows],
                  'residual_coefficients':[serial(f) for f in residual],'residual_degrees':[f.degree(p) for f in residual],
                  'pole_squarefree_gcd_degree':ls[3].gcd(ls[3].diff(p)).degree(p),'pole_c5_gcd_degree':ls[3].gcd(c5).degree(p)}
        out['selected']=selected
        stage('selected_interpolation',seed=seed,residual_degrees=selected['residual_degrees'],pole_gcd=selected['pole_squarefree_gcd_degree'])
        break
    out.update({'status':'PASS_FOUR_UNIT_INTERPOLATION_ONLY' if selected else 'NO_RANK_CONSTANT_SEED_IN_RETAINED_RANGE','field_modulus_hex':hex(modulus),
                'scope':'All finite identities and attempted raw ranks are retained. A selected interpolation does not establish any residual-fibre bound or nodality.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP30_seventeen_four_unit_interpolation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('attempts','selected','stages')},indent=2))
