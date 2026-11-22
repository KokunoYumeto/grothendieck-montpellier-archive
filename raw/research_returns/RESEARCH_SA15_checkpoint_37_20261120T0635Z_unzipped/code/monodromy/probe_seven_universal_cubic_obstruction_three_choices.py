"""Universal necessary conditions for three distinct residual Z-values.

Cleared polynomial arithmetic, no field inversions of cg or leading terms.
This program does not handle A(ell)=0 and does not infer nodality.
"""
from pathlib import Path
import datetime,json,signal,time,traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start=time.perf_counter();root=Path(__file__).resolve().parent.parent
def timeout(*unused):raise TimeoutError('Universal cubic obstruction exceeded 60 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
result={'status':'RUNNING'}
try:
    rr=symbols('r');base=GF(2).frac_field(rr);r=base.gens[0]
    R,l,t=ring('l,t',base)
    const=R.ground_new;D=const(r*r);z=const((r*r+1)/r**3);a=z*z;b=a+z+1
    gt=t*t+t+D;red=lambda f:f.div([gt])[1]
    cg=red(z*D+t);ft=red(a*t**5+b*t**3)
    q0=red(ft+t*t*(z+1)+(t*t+1)*cg*cg+t*cg).mul_ground(1/r**4)
    A4=a*D;A2=A4*(D+1)+1;A1=a*D*D
    A=A4*l**3+A2*l+A1
    j=red(a*D*D*l+D*D*q0);k=red(D*D*cg**4)
    P2=red(cg**4*(cg*cg+A4*l*l+A2)**2+A4*A4*j*j+l*A*A4*cg**4)
    P1=red(A4*A4*k+cg**6*A*(l*cg*cg+A1))
    def lc_l(f):
        deg=f.degree(l)
        return R.from_dict({(0,et):co for (el,et),co in f.items() if el==deg})
    lead=lc_l(P2);rem=P1;steps=[]
    while rem and rem.degree(l)>=P2.degree(l):
        deg=rem.degree(l)-P2.degree(l)
        rem=red(lead*rem+lc_l(rem)*l**deg*P2);steps.append(rem.degree(l))
    def coeff_l(f,i):return R.from_dict({(0,et):co for (el,et),co in f.items() if el==i})
    c2,c1,c0=[coeff_l(P2,i) for i in (2,1,0)]
    r1,r0=coeff_l(rem,1),coeff_l(rem,0)
    obstruction=red(c2*r0*r0+c1*r0*r1+c0*r1*r1)
    # Norm to F2(r), useful for identifying every specialization excluded by it.
    conjugate=red(obstruction.compose(t,t+1))
    norm=red(obstruction*conjugate)
    assert norm.degree(t)<=0
    def factored_ground(f):
        if not f:return '0'
        q=f[(0,0)]
        return {'numerator':str(q.numer.factor_list()),'denominator':str(q.denom.factor_list())}
    result={'status':'COMPLETED_UNIVERSAL_NECESSARY_CONDITIONS',
      'q0':str(q0),'A':str(A),'P1':str(P1),'P2':str(P2),
      'pseudo_remainder':str(rem),'pseudo_steps':steps,
      'obstruction':str(obstruction),'obstruction_norm':factored_ground(norm),
      'scope':'Necessary conditions for three distinct Z values on A(ell)!=0; exceptional A=0 and any resultant zeros still require separate proof.'}

    # For a fixed zeta, all three admissible r satisfy zeta*r^3+r^2+1.
    # Test whether that entire cubic can divide the squarefree obstruction norm.
    numerator=norm[(0,0)].numer
    factor_rows=numerator.factor_list()[1]
    bad=numerator.ring.one
    for factor,multiplicity in factor_rows:
        bad*=factor
    zz=symbols('zeta');zbase=GF(2).frac_field(zz);zeta=zbase.gens[0]
    RR,rv=ring('rv',zbase)
    bad_in_r=RR.from_dict({e:zbase.convert(int(co)) for e,co in bad.items()})
    cubic_r=rv**3+(rv**2).mul_ground(1/zeta)+RR.ground_new(1/zeta)
    remainder_r=bad_in_r.div([cubic_r])[1]
    coefficient_numerators=[co.numer for co in remainder_r.values() if co]
    common=coefficient_numerators[0]
    for polynomial in coefficient_numerators[1:]:common=common.gcd(polynomial)
    result['bad_r_radical_degree']=bad.degree()
    result['all_three_bad_zeta_gcd']=str(common.factor_list())
    result['bad_cubic_remainder']=str(remainder_r)

except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0);result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/probe_seven_universal_cubic_obstruction_three_choices.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
