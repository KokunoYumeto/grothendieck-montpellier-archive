"""Exact small-field consistency check; deliberately avoids symbolic derivatives."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
from gf16_exact_domain import MUL,INV,K16,F16
from sympy.polys.rings import ring

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
raw=json.loads((agent/'outputs/post_CP27_eleven_rational_quintic.json').read_text())
def mul(a,b):return MUL[a][b]
def power(a,n):
    x=1
    while n:
        if n&1:x=mul(x,a)
        a=mul(a,a);n>>=1
    return x
def bin_eval(p,v):
    x=0
    for i in range(p.bit_length()-1,-1,-1):x=mul(x,v)^((p>>i)&1)
    return x
def evaluate(item,v,L):
    q=0
    for co in reversed(item['numerator_L_coefficients_v_binary_hex']):q=mul(q,L)^bin_eval(int(co,16),v)
    a,b,c=item['denominator_exponents_v_vplus1_G']
    G=(1<<10)|(1<<7)|(1<<5)|(1<<3)|1
    den=mul(mul(power(v,a),power(v^1,b)),power(bin_eval(G,v),c))
    return mul(q,INV[den])
def trim(p):
    p=list(p)
    while p and not p[-1]:p.pop()
    return p
def gcd(p,q):
    p,q=trim(p),trim(q)
    while q:
        while p and len(p)>=len(q):
            shift=len(p)-len(q);fac=mul(p[-1],INV[q[-1]])
            for i,x in enumerate(q):p[shift+i]^=mul(fac,x)
            p=trim(p)
        p,q=q,p
    return [mul(x,INV[p[-1]]) for x in p] if p else []
v,L=10,10
A=evaluate(raw['A'],v,L)
cp=[evaluate(f,v,L) for f in raw['charpoly_P']]
cb=[evaluate(f,v,L) for f in raw['charpoly_B']]
assert A==0
assert cp==[mul(x,x) for x in cb]
dp=[cp[4],0,cp[2],0,1]
db=[cb[4],0,cb[2],0,1]
gp=gcd(list(reversed(cp)),dp)
gb=gcd(list(reversed(cb)),db)
assert len(gp)==1 and len(gb)==1
assert cp[2]==0 and cp[3]==0
assert cp[5]^mul(cp[1],cp[4])
R,T=ring('T',K16)
native_derivative=str((T*T).diff(T))
result={'status':'EXACT_CONSISTENCY_CHECK_COMPLETED','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,'parameter_v_L':[v,L],'A':A,
        'charpoly_P_descending':cp,'charpoly_B_descending':cb,
        'P_derivative_gcd_ascending':gp,'B_derivative_gcd_ascending':gb,
        'symbolic_T_squared_derivative':native_derivative,
        'prior_finite_discriminant_claim_valid_at_this_A_root':True,
        'scope':'The generic collision equations vanish here only because c3=c2=0; the separate exceptional condition is nonzero. Direct derivative gcds confirm both P and B values are distinct at this A-zero specialization. No geometric or uniform conclusion.'}
(agent/'outputs/post_CP27_eleven_f16_consistency.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
