"""Resolve a discrepancy between a universal resultant and a field probe."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1];out={'status':'RUNNING'}
try:
    data=json.loads((agent/'outputs/post_CP28_thirteen_parameter_probe.json').read_text())
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)([1,0,1,1]));R=fq_default_poly_ctx(K);L=R.gen();z=K.gen()
    a=z*z;delta=z+1;e=1/(delta*delta);j=a*L+delta**2;k=delta**4
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    H=a*a*L**6+(a*a+1)*L*L+(a+1);J=a*a*L**4+(a*a+1)
    b2=J*e**2+a*a*e**4*j*j;b1=1+H*e+a*a*e**4*k
    T=b1**3+j*j*b1*b2*b2+k*b2**3
    def binary_eval(h):
        n=int(h,16);v=K(0)
        for i in reversed(range(n.bit_length())):v=v*z+((n>>i)&1)
        return v
    def specialization(s):
        d=s['denominator_exponents_v_vplus1_G'];assert d[2]==0
        den=z**d[0]*(z+1)**d[1]
        return R([binary_eval(h)/den for h in s['numerator_L_coefficients_v_binary_hex']])
    As=specialization(data['A']);Ts=specialization(data['T'])
    out.update({'A_matches':bool(A==As),'T_matches':bool(T==Ts),'A':str(A),'T_direct':str(T),'T_serialized':str(Ts),
                'gcd_direct':str(A.gcd(T)),'gcd_serialized':str(As.gcd(Ts)),
                'resultant_value':str(binary_eval(data['stages'][1]['polynomial_hex']))})
    assert A==As and T==Ts
    out['status']='PASS_SPECIALIZATION_CROSSCHECK'
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_specialization_crosscheck.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
