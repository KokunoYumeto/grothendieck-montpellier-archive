"""Exact certificate for C-RD5, and the ordinary F3 curve used in notes."""
from fractions import Fraction
import json,time,pathlib
start=time.perf_counter()
# In Q[eps]/eps^2, (a,b) means a+b eps.
def mul(x,y):return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
def inv(x):return (1/x[0],-x[1]/(x[0]*x[0]))
a=(Fraction(1),Fraction(0)); b=(Fraction(1),Fraction(1))
denom=(4*mul(mul(a,a),a)[0]+27*mul(b,b)[0],4*mul(mul(a,a),a)[1]+27*mul(b,b)[1])
j=mul((Fraction(6912),Fraction(0)),inv(denom))
assert denom==(31,54)
assert j==(Fraction(6912,31),Fraction(-373248,961))
delta=tuple(-16*x for x in denom)
assert delta==(-496,-864)
assert int(delta[0])%5!=0
ordinary_points=[(x,y) for x in range(3) for y in range(3) if (y*y-x*x*x-x*x-1)%3==0]
assert len(ordinary_points)+1==6
out={'input':{'base':'Z_5[eps]/eps^2','family':'y^2=x^3+x+1+eps'},'discriminant':list(map(str,delta)),'j_invariant':list(map(str,j)),'j_derivative_nonzero':j[1]!=0,'good_special_discriminant_mod5':int(delta[0])%5,'ordinary_F3_test':{'equation':'y^2=x^3+x^2+1','affine_points':ordinary_points,'projective_count':len(ordinary_points)+1,'trace':-2,'trace_mod3':1},'elapsed_seconds':time.perf_counter()-start}
print(json.dumps(out,indent=2))
pathlib.Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
