"""Finite exact interpolation search for norm17 on three residual curve orbits.

No interpolation search result alone asserts nodality. All attempted seeds
and coefficient outputs are retained, including rejected rank-drop seeds.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,signal,time,traceback
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','models':[],'stages':[]}
def timeout(*unused):raise TimeoutError('Norm17 finite interpolation exceeded60seconds')
def stage(name,**kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw}
    out['stages'].append(row);print(json.dumps(row),flush=True)
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    modulus=0x10eb
    def mul(x,y):
        result=0
        while y:
            if y&1:result^=x
            y>>=1;x<<=1
            if x>>12:x^=modulus
        return result
    def power(x,n):
        result=1
        while n:
            if n&1:result=mul(result,x)
            x=mul(x,x);n>>=1
        return result
    parameters=[('zero',0)]
    parameters.append(('cubic',next(x for x in range(1,4096) if power(power(x,5),3)^power(x,5)^1==0)))
    parameters.append(('sextic',next(x for x in range(1,4096) if power(power(x,5),6)^power(power(x,5),5)^1==0)))
    AS={}
    for x in range(4096):AS.setdefault(mul(x,x)^x,x)
    cc=symbols('c')
    field=MonogenicFiniteExtension(Poly(cc**12+cc**7+cc**6+cc**5+cc**3+cc+1,cc,modulus=2))
    field.gcd=lambda x,y:field.one if x or y else field.zero
    field.quo=field.exquo=lambda x,y:x/y
    powers=[field.generator**i for i in range(12)]
    convert=lambda n:sum((powers[i] for i in range(12) if n>>i&1),field.zero)
    def encode(value):
        return sum(int(c)<<i for i,c in enumerate(reversed(value.rep.to_list())))
    for name,mu in parameters:
        autos=[]
        for shift in range(1,4096):
            v=power(shift,4)^mul(mu,power(shift,2));u=mul(v,v)^mul(mu,shift)
            if mul(u,u)!=shift:continue
            constant=power(shift,5)^mul(mu,power(shift,3))
            if constant not in AS:continue
            if mul(u,power(shift,2))^mul(v,shift)==1:
                for beta in (AS[constant],AS[constant]^1):autos.append((shift,u,v,beta))
        def comm(g,h):
            s,u,v,_=g;t,U,V,_=h
            return mul(u,mul(t,t))^mul(v,t)^mul(U,mul(s,s))^mul(V,s)
        pairs=[(g,h) for i,g in enumerate(autos) for h in autos[i+1:] if comm(g,h)==1]
        model={'name':name,'mu_encoded':mu,'mu_fifth_encoded':power(mu,5),'order_four_units':len(autos),'anticommuting_pairs':len(pairs),'attempts':[]}
        out['models'].append(model)
        assert pairs,model
        R,X,p=ring('X,p',field);cv=R.ground_new
        a,b=field.one,convert(mu)
        d1=p**4+p*p*b;d2=d1*d1+p*b
        selected=None
        for seed,(gi,hi) in enumerate(pairs[:20]):
            gs=[tuple(convert(v) for v in g) for g in (gi,hi)]
            shifts=[g[0] for g in gs]
            ys=[p*p*g[1]+p*g[2]+cv(g[3]) for g in gs]
            derivatives=[(p+cv(s))**4+(p+cv(s))**2*b for s in shifts]
            def ell(ls,s):return ls[0]+ls[1]*s+ls[2]*s*s
            def coefficients(ls):
                c1=ls[0]*d1;c2=ls[0]*d2+ls[1]*d1
                s=shifts[0]
                c3=(ls[1]*ys[0]+ell(ls,s)*derivatives[0]+c1)/(s*s)
                c4=(ell(ls,s)*ys[0]+c1*s+c2*s*s+c3*s**3)/(s**4)
                return [c1,c2,c3,c4]
            rows=[[],[]]
            t=shifts[1]
            for j in range(3):
                ls=[R.one if i==j else R.zero for i in range(3)]
                c1,c2,c3,c4=coefficients(ls)
                rows[0].append(ls[1]*ys[1]+ell(ls,t)*derivatives[1]+c1+c3*t*t)
                rows[1].append(ell(ls,t)*ys[1]+c1*t+c2*t*t+c3*t**3+c4*t**4)
            rr,ss=rows
            ls=[rr[1]*ss[2]+rr[2]*ss[1],rr[2]*ss[0]+rr[0]*ss[2],rr[0]*ss[1]+rr[1]*ss[0]]
            if not any(ls):
                model['attempts'].append({'seed':seed,'status':'ZERO_KERNEL_VECTOR'});continue
            common=next(f for f in ls if f)
            for f in ls:
                if f:common=common.gcd(f)
            attempt={'seed':seed,'automorphisms':[list(gi),list(hi)],'minor_degrees':[f.degree(p) for f in ls],'common_degree':common.degree(p)}
            model['attempts'].append(attempt)
            if common.degree(p)>0:continue
            bs=coefficients(ls);c1,c2,c3,c4=bs
            linear=ls[0]+ls[1]*X+ls[2]*X*X
            polynomial=c1*X+c2*X*X+c3*X**3+c4*X**4
            assert not ((linear*(d1*X+d2*X*X)+polynomial).div(X**3)[1])
            for s,Y,D in zip(shifts,ys,derivatives):
                assert not (linear.compose(X,cv(s))*Y+polynomial.compose(X,cv(s)))
                assert not (ls[1]*Y+linear.compose(X,cv(s))*D+c1+c3*s*s)
            fun=lambda x:x**5+x**3*b
            norm=polynomial**2+linear*polynomial+linear**2*(fun(p+X)+fun(p))
            prescribed=X**3
            for s in shifts:prescribed*=(X+cv(s))**2
            quotient,rem=norm.div(prescribed)
            assert not rem and quotient.degree(X)==2
            extract=lambda i:R.from_dict({(0,ep):v for (ex,ep),v in quotient.items() if ex==i})
            residual=[extract(i) for i in (2,1,0)]
            assert residual[0]==ls[2]**2
            serial=lambda f:[[list(m),encode(v)] for m,v in f.terms()]
            selected={'seed':seed,'automorphisms_encoded':[list(gi),list(hi)],'raw_rows':[[serial(f) for f in row] for row in rows],
                      'coefficients':[serial(f) for f in ls+bs],'residual_coefficients':[serial(f) for f in residual],
                      'common_degree':common.degree(p),'residual_degrees':[f.degree(p) for f in residual],
                      'l2_squarefree_gcd_degree':ls[2].gcd(ls[2].diff(p)).degree(p),'l2_c4_gcd_degree':ls[2].gcd(c4).degree(p)}
            model['selected']=selected
            break
        assert selected,model
        stage('model_interpolation',model=name,mu=mu,seed=selected['seed'],residual_degrees=selected['residual_degrees'],pole_gcd=selected['l2_squarefree_gcd_degree'])
    out.update({'status':'PASS_THREE_MODEL_INTERPOLATION_ONLY','field_modulus_hex':hex(modulus),'scope':'Exact norm17 interpolation for 3+2g+2h on three representative residual moduli. Raw rank, norm factorization and coefficient data only; all residual fibres and nodality still unproved.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_exceptional_interpolation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('models','stages')},indent=2))
