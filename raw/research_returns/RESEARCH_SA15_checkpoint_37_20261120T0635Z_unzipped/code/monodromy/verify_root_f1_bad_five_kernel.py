"""Independent symbolic check of the parent's explicit f1 bad kernel."""
from pathlib import Path
import datetime,json,time
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start=time.perf_counter()
R,w,z=ring('w,z',GF(2))
relation=w**2+w+1
red=lambda f:f.div([relation])[1]
A=w*z**2+z+1
F=z**5+z**3+z
assert not red(A**2+z**2*A+F+(z+1)**5)
assert not red(w+A.compose(z,R.one))
assert red(w+A.compose(z,R.one)+1)==1
assert not red(w**2+w+1)
result={
    'status':'PASS',
    'actual_timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-start,
    'checks':['Norm(v+w z^2+z+1)=(z+1)^5 in F4(C)',
              'The function vanishes at z=1,v=w and its hyperelliptic conjugate is one',
              'The prescribed finite point satisfies the original curve equation'],
    'scope':'Polynomial identities only. The separate proof audit checks the unique pole5Q, exact divisor, order-five class and six bad Lagrangian quotients. No all-kernel or fixed-target existence conclusion.',
}
out=Path(__file__).resolve().parent.parent/'outputs/verify_root_f1_bad_five_kernel.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
