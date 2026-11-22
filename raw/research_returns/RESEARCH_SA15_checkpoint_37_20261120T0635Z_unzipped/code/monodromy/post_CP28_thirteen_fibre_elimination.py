"""Bounded exact affine-fibre elimination for the exceptional norm13 map.

Primitive polynomial remainder sequences identify a finite set of possible
first coordinates.  Each is then checked over its exact residue field.
This exploratory stage does not include the pole fibres.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','prs':[],'fibre_checks':[]}
def timeout(*unused):raise TimeoutError('Norm13 affine fibre elimination exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    data=json.loads((agent/'outputs/post_CP28_thirteen_three_unit_coordinates.json').read_text())
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(data['field_modulus']));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    enc=lambda c:sum(int(v)<<i for i,v in enumerate(c.to_list()))
    serial=lambda f:[enc(c) for c in f.coeffs()]
    dec=lambda rows:R([val(n) for n in rows])
    zero,one=R.zero(),R.one()
    l2=dec(data['l2']);exceptions={}
    def trim(a):
        a=list(a)
        while a and a[-1].is_zero():a.pop()
        return a
    def add_exception(f,reason):
        assert not f.is_zero()
        if f.degree()<=0:return
        unit,factors=f.factor();product=R([unit])
        for fac,n in factors:
            product*=fac**n;key=tuple(serial(fac))
            if key not in exceptions:exceptions[key]={'polynomial':fac,'reasons':[]}
            exceptions[key]['reasons'].append(reason)
        assert product==f
    def primitive(a,reason):
        a=trim(a);assert a
        g=next(x for x in a if not x.is_zero())
        for x in a:
            if not x.is_zero():g=g.gcd(x)
        add_exception(g,reason)
        return [x//g for x in a]
    def off_diagonal(coord):
        n,d=map(dec,[coord['numerator'],coord['denominator']]);nc,dc=n.coeffs(),d.coeffs()
        size=max(len(nc),len(dc));f=[d*(nc[i] if i<len(nc) else K(0))+n*(dc[i] if i<len(dc) else K(0)) for i in range(size)]
        f=trim(f);q=[zero]*(len(f)-1);q[-1]=f[-1]
        for i in range(len(f)-2,0,-1):q[i-1]=f[i]+p*q[i]
        assert f[0]+p*q[0]==zero
        return trim(q)
    equations=[off_diagonal(data['coordinates'][name]) for name in ['L','M','nu']]
    A=primitive(equations[0],'initial L content');B=primitive(equations[1],'initial M content')
    if len(A)<len(B):A,B=B,A
    step=0
    while len(B)>1:
        add_exception(B[-1],f'leading coefficient {step}')
        rem=list(A)
        while len(rem)>=len(B):
            top=rem[-1];shift=len(rem)-len(B);rem=[x*B[-1] for x in rem]
            for j,y in enumerate(B):rem[j+shift]+=top*y
            rem=trim(rem)
        assert rem,'Unexpected generic off-diagonal common component.'
        rem=primitive(rem,f'remainder content {step}')
        row={'step':step,'q_degrees':[len(A)-1,len(B)-1,len(rem)-1],
             'maximum_coefficient_degree':max(int(x.degree()) for x in rem),'seconds':time.perf_counter()-start}
        out['prs'].append(row);print(json.dumps(row),flush=True)
        A,B=B,rem;step+=1
    add_exception(B[0],'final constant')
    # Exact gcds after every possible exceptional first-coordinate specialization.
    for key,row in exceptions.items():
        mod=row['polynomial']
        if l2%mod==zero:continue
        def reduce(x):return x%mod
        def inverse(x):
            r0,r1=mod,reduce(x);s0,s1=zero,one
            assert not r1.is_zero()
            while not r1.is_zero():
                q,r=r0.divmod(r1);r0,r1=r1,r;s0,s1=s1,s0+q*s1
            assert r0.degree()==0
            return (s0*(1/r0.coeffs()[0]))%mod
        def qtrim(a):return trim([reduce(x) for x in a])
        def qrem(a,b):
            a=qtrim(a);b=qtrim(b);ib=inverse(b[-1])
            while len(a)>=len(b):
                c=reduce(a[-1]*ib);shift=len(a)-len(b)
                for j,v in enumerate(b):a[j+shift]=reduce(a[j+shift]+c*v)
                a=qtrim(a)
            return a
        def qgcd(a,b):
            a,b=qtrim(a),qtrim(b)
            while b:a,b=b,qrem(a,b)
            if not a:return []
            ii=inverse(a[-1]);return [reduce(x*ii) for x in a]
        g=qgcd(equations[0],equations[1]);g=qgcd(g,equations[2])
        # Remove diagonal/pole roots: they are excluded from the affine comparison.
        excluded=[[reduce(p),one],[R([c]) for c in l2.coeffs()]]
        for divisor in excluded:
            while len(g)>1:
                common=qgcd(g,divisor)
                if len(common)<=1:break
                quotient=[zero]*(len(g)-len(common)+1);rem=list(g);ii=inverse(common[-1])
                while len(rem)>=len(common):
                    shift=len(rem)-len(common);c=reduce(rem[-1]*ii);quotient[shift]=c
                    for j,v in enumerate(common):rem[j+shift]=reduce(rem[j+shift]+c*v)
                    rem=qtrim(rem)
                assert not rem;g=qtrim(quotient)
        result={'first_coordinate_factor':list(key),'degree':int(mod.degree()),'other_point_gcd_degree':len(g)-1,
                'gcd_coefficients':[serial(x) for x in g],'reasons':row['reasons']}
        out['fibre_checks'].append(result)
    out.update({'status':'PASS_AFFINE_FIBRE_ELIMINATION_ONLY','max_other_point_degree':max((x['other_point_gcd_degree'] for x in out['fibre_checks']),default=0),
                'exception_factor_count':len(exceptions),'exception_factors':[{'polynomial':list(k),'reasons':v['reasons']} for k,v in exceptions.items()],
                'scope':'Exact affine comparison of three rational coordinates. Pole fibres and the full geometric assembly remain outside this exploratory assertion.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_fibre_elimination.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],
                      'max_other_point_degree':out.get('max_other_point_degree'),'traceback':out.get('traceback')},indent=2))
