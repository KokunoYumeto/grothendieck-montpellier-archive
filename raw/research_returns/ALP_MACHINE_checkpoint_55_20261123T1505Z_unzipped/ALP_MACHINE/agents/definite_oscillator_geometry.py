from pathlib import Path
import json
from sympy import symbols, rem, expand
z,t=symbols("z t")
phi=sum(z**i for i in range(7))
a=z+z**6
q=z+z**2+z**4-z**3-z**5-z**6
poly=t**3+t**2-2*t-1
out={
 "a_minpoly_remainder": str(rem(poly.subs(t,a),phi,z)),
 "quadratic_subfield_remainder": str(rem(q*q+7,phi,z)),
 "inverse_type_on_representatives": [1 if pow(j,-1,7) in (1,2,3) else -1 for j in (1,2,3)],
 "sign_brackets": {str(x): int(poly.subs(t,x)) for x in (-2,-1,0,1,2)},
 "canonical_weight_gaps": [{"m":m,"r":m-2,"oscillator_min":m*(m-2),"canonical":(m-2)*(m-1),"gap":m-2} for m in range(3,13)]
}
assert out["a_minpoly_remainder"]=="0"
assert out["quadratic_subfield_remainder"]=="0"
assert out["inverse_type_on_representatives"]==[1,-1,-1]
assert all(row["oscillator_min"]-row["canonical"]==row["gap"]>0 for row in out["canonical_weight_gaps"])
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
