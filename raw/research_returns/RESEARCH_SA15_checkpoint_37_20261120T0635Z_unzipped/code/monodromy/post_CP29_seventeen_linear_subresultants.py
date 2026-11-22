"""Exact norm17 degree-one polynomial-combination certificates for affine fibres.

The subresultant recurrence is accompanied by explicit polynomial Bezout
coefficients.  Consequently its specialization implication is checked
directly, without invoking an unverified generic-specialization inference.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal,argparse
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
parser=argparse.ArgumentParser();parser.add_argument('--model',choices=['zero','cubic','sextic'],required=True);args=parser.parse_args()
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','model':args.model,'pairs':[]}
def timeout(*unused):raise TimeoutError('Linear-subresultant computation exceeded120seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(120)
try:
    package=json.loads((agent/'outputs/post_CP29_seventeen_exceptional_coordinates.json').read_text())
    assert package['status']=='PASS_COORDINATES_AND_POLES_ONLY'
    data=next(row.copy() for row in package['models'] if row['name']==args.model)
    data['field_modulus']=package['field_modulus']
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(data['field_modulus']));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    enc=lambda c:sum(int(v)<<i for i,v in enumerate(c.to_list()))
    serial=lambda f:[enc(c) for c in f.coeffs()];dec=lambda a:R([val(x) for x in a])
    zero,one=R.zero(),R.one();l2=dec(data['l2'])
    def trim(a):
        a=list(a)
        while a and a[-1].is_zero():a.pop()
        return a
    def qadd(a,b):return trim([(a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero) for i in range(max(len(a),len(b)))])
    def qscale(a,c):return trim([x*c for x in a])
    def qmul(a,b):
        if not a or not b:return []
        c=[zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return trim(c)
    def off_diagonal(coord):
        n,d=map(dec,[coord['numerator'],coord['denominator']]);nc,dc=n.coeffs(),d.coeffs()
        f=trim([d*(nc[i] if i<len(nc) else K(0))+n*(dc[i] if i<len(dc) else K(0)) for i in range(max(len(nc),len(dc)))])
        q=[zero]*(len(f)-1);q[-1]=f[-1]
        for i in range(len(f)-2,0,-1):q[i-1]=f[i]+p*q[i]
        assert f[0]+p*q[0]==zero
        return q
    equations={name:off_diagonal(data['coordinates'][name]) for name in ['L','M','nu']}
    def prem(a,b,ua,va,ub,vb):
        rem=list(a);u=list(ua);v=list(va);N=len(a)-len(b)+1;lc=b[-1]
        while len(rem)>=len(b):
            top=rem[-1];shift=len(rem)-len(b)
            rem=qadd(qscale(rem,lc),[zero]*shift+qscale(b,top))
            u=qadd(qscale(u,lc),[zero]*shift+qscale(ub,top))
            v=qadd(qscale(v,lc),[zero]*shift+qscale(vb,top));N-=1
        if N:
            c=lc**N;rem=qscale(rem,c);u=qscale(u,c);v=qscale(v,c)
        return rem,u,v
    def exactdivide(a,b):
        answer=[]
        for x in a:
            q,r=divmod(x,b);assert r.is_zero(),'Non-polynomial Bezout division.';answer.append(q)
        return trim(answer)
    common_contents=[]
    for names in [('L','M')]:
        original_a,original_b=equations[names[0]],equations[names[1]]
        f,g=list(original_a),list(original_b);uf,vf=[one],[];ug,vg=[],[one]
        if len(f)<len(g):f,g=g,f;uf,ug=ug,uf;vf,vg=vg,vf
        m=len(g)-1;delta=len(f)-len(g);lc=g[-1];c=lc**delta
        h,uh,vh=prem(f,g,uf,vf,ug,vg);steps=[]
        while len(h)>2:
            degree=len(h)-1;steps.append([len(g)-1,degree,max(int(x.degree()) for x in h)])
            f,g,uf,vf,ug,vg=g,h,ug,vg,uh,vh
            delta=m-degree;m=degree;divisor=lc*c**delta
            h,uh,vh=prem(f,g,uf,vf,ug,vg)
            h=exactdivide(h,divisor);uh=exactdivide(uh,divisor);vh=exactdivide(vh,divisor)
            lc=g[-1]
            if delta>1:
                c,rem=divmod(lc**delta,c**(delta-1));assert rem.is_zero()
            else:c=lc
        assert len(h)==2,'No degree-one subresultant encountered.'
        assert qadd(qmul(uh,original_a),qmul(vh,original_b))==h
        content=h[0].gcd(h[1]);common_contents.append(content)
        row={'pair':list(names),'steps':steps,'linear_coefficients':[serial(x) for x in h],
             'bezout_first':[serial(x) for x in uh],'bezout_second':[serial(x) for x in vh],
             'coefficient_gcd':serial(content),'coefficient_gcd_degree':int(content.degree()),
             'seconds':time.perf_counter()-start}
        out['pairs'].append(row);print(json.dumps({k:row[k] for k in ['pair','coefficient_gcd_degree','seconds']}),flush=True)
    common=common_contents[0];remaining=common
    while True:
        g=remaining.gcd(l2)
        if g.degree()==0:break
        remaining=remaining//g
    out.update({'status':'PASS_LINEAR_COMBINATION_CERTIFICATES','common_bad_polynomial':serial(common),
                'common_bad_degree':int(common.degree()),'nonpole_bad_polynomial':serial(remaining),
                'nonpole_bad_degree':int(remaining.degree()),
                'scope':'Exact polynomial-combination certificates. A nonpole triple fibre must lie in the displayed final common zero set; this script does not assume that set is empty.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/f'outputs/post_CP29_seventeen_linear_subresultants_{args.model}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],
                      'nonpole_bad_degree':out.get('nonpole_bad_degree'),'traceback':out.get('traceback')},indent=2))
