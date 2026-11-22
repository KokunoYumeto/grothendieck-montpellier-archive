"""Exact universal parameter certificate for the norm-seven candidate.

Both A(ell)!=0 and A(ell)=0 obstructions are included. The mathematical
proof explains why avoiding their radical gives a triple-free theta image.
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

    # If A(ell)=0, a triple requires two distinct common roots of the
    # quadratic B(Z) and cubic C(Z), hence B divides C.
    H=red(cg*cg*(cg*cg+A4*l*l+A2))
    exceptional=red(H*(H+A4*j)**2+k*A4**3)
    monic_A=A.mul_ground(r**4/(r**4+1))
    reduce_A=lambda f:red(f.div([monic_A])[1])
    columns=[reduce_A(exceptional*l**i) for i in range(3)]
    matrix=[[coeff_l(columns[jj],ii) for jj in range(3)] for ii in range(3)]
    from itertools import permutations
    det=R.zero
    for permutation in permutations(range(3)):
        term=R.one
        for ii in range(3):term=red(term*matrix[ii][permutation[ii]])
        det=red(det+term)
    exceptional_norm=red(det*red(det.compose(t,t+1)))
    assert exceptional_norm.degree(t)<=0
    result['exceptional_A_zero_remainder']=str(reduce_A(exceptional))
    result['exceptional_A_zero_resultant']=str(det)
    result['exceptional_A_zero_norm']=factored_ground(exceptional_norm)
    # Test the union of both necessary bad-r loci against the three r choices.
    numerator=(norm*exceptional_norm)[(0,0)].numer
    factor_rows=numerator.factor_list()[1]
    bad=numerator.ring.one
    for factor,multiplicity in factor_rows:bad*=factor
    zz=symbols('zeta');zbase=GF(2).frac_field(zz);zeta=zbase.gens[0]
    RR,rv=ring('rv',zbase)
    bad_in_r=RR.from_dict({e:zbase.convert(int(co)) for e,co in bad.items()})
    cubic_r=rv**3+(rv**2).mul_ground(1/zeta)+RR.ground_new(1/zeta)
    remainder_r=bad_in_r.div([cubic_r])[1]
    coefficient_numerators=[co.numer for co in remainder_r.values() if co]
    common=coefficient_numerators[0]
    for polynomial in coefficient_numerators[1:]:common=common.gcd(polynomial)
    result['combined_bad_r_radical_degree']=bad.degree()
    result['combined_all_three_bad_zeta_gcd']=str(common.factor_list())
    result['combined_bad_zeta_polynomial']=str(common)


    assert norm and exceptional_norm
    expected_factors=[
      r+1,r**3+r+1,r**6+r+1,r**6+r**3+1,
      r**6+r**4+r**3+r+1,r**9+r**4+r**2+r+1,
      r**12+r**9+r**8+r**7+r**6+r**4+1,
      r**15+r**12+r**11+r**9+r**7+r**6+r**3+r+1,
      r**39+r**36+r**35+r**33+r**31+r**29+r**27+r**25+r**23+r**21+r**19+r**18+r**17+r**14+r**12+r**8+r**7+r**6+r**3+r+1]
    expected=base.one
    for factor in expected_factors:expected*=factor
    assert expected.denom==expected.denom.ring.one and bad==expected.numer
    assert bad.degree()==97 and bad.gcd(bad.diff(r.numer)).degree()==0
    assert common==zeta.numer**3+zeta.numer**2+1
    assert red(cg*red(cg.compose(t,t+1)))==const((r**3+r+1)/r**2)
    for co in remainder_r.values():
        assert all(f.degree()==1 and f.get((0,),f.ring.domain.zero)==0 for f,m in co.denom.factor_list()[1])
    result['status']='PASS_UNIVERSAL_PARAMETER_CERTIFICATE'
    result['scope']='Universal identities and exact parameter exclusion, including A=0; the accompanying proof supplies the geometric interpretation.'
    result['displayed_bad_radical_verified']=True
    result['bad_radical_squarefree']=True
    result['all_three_bad_gcd_exact']=True
    result['cg_norm_verified']=True
    result['coefficient_denominators_only_zeta']=True
    result['bad_radical_coefficients']=[[e[0],int(co)] for e,co in sorted(bad.items(),reverse=True)]
    result['r_cubic_remainder_coefficients']={str(e[0]):{'numerator':str(co.numer),'denominator':str(co.denom)} for e,co in remainder_r.items()}

except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0);result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/independent_uniform_seven_parameters.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
