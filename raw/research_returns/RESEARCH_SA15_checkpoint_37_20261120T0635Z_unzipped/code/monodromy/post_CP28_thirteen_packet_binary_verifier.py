"""Independent binary-field verification of one retained four-point packet.

No FLINT, symbolic-algebra library, field root search, or resultant is used.
The input is the literal coordinate data of the first retained packet.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,traceback
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING'}
try:
    data=json.loads((agent/'outputs/post_CP28_thirteen_exceptional_ordinate_probe.json').read_text())
    packet=data['packets'][0]
    modulus=sum(1<<i for i in [24,16,15,14,13,10,9,7,5,3,0])
    def parse(s):
        if s=='0':return 0
        out=0
        for term in s.split(' + '):
            e=0 if term=='1' else 1 if term=='c' else int(term[2:])
            out ^= 1<<e
        return out
    def mul(a,b):
        c=0
        while b:
            if b&1:c^=a
            b>>=1;a<<=1
            if a>>24:a^=modulus
        return c
    def power(a,n):
        r=1
        while n:
            if n&1:r=mul(r,a)
            a=mul(a,a);n>>=1
        return r
    def inv(a):
        assert a
        b=power(a,(1<<24)-2);assert mul(a,b)==1
        return b
    def trim(a):
        a=list(a)
        while a and not a[-1]:a.pop()
        return a
    def add(a,b):return trim([(a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
    def pmul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]^=mul(x,y)
        return trim(c)
    def scale(a,c):return trim([mul(x,c) for x in a])
    def remainder(a,b):
        a=trim(a);bi=inv(b[-1])
        while len(a)>=len(b):
            c=mul(a[-1],bi);offset=len(a)-len(b)
            for i,x in enumerate(b):a[i+offset]^=mul(c,x)
            a=trim(a)
        return a
    def fpow(a,n):
        c=[1]
        while n:
            if n&1:c=pmul(c,a)
            a=pmul(a,a);n>>=1
        return c
    z=parse(data['z']);beta=parse(data['beta']);a=mul(z,z);delta=z^1;b=a^z^1
    assert power(z,3)^power(z,2)^1==0
    assert power(beta,2)^beta==delta
    L,M,nu,v0=[parse(packet[k]) for k in ['L','M','nu','constant']]
    u=[M,L,1];v=[v0,nu]
    curve=[0,0,0,b,0,a]
    assert not remainder(add(add(pmul(v,v),v),curve),u)
    checks=[];seen=set()
    for row in packet['points']:
        p,y,Z=[parse(row[k]) for k in ['p','y','Z']]
        assert (p,y) not in seen;seen.add((p,y))
        assert mul(y,y)^y==mul(a,power(p,5))^mul(b,power(p,3))
        d1=mul(a,power(p,4))^mul(b,power(p,2));d2=mul(d1,d1)^mul(b,p)
        G=mul(z,power(p,2))^mul(delta,p)^beta;F=G^d1
        assert Z==delta^F^d2 and Z
        A1=mul(delta,d1);A2=mul(Z,d1)^mul(delta,d2)
        A3=mul(Z,F^delta)^mul(delta,delta)
        # Expand the norm in X=x+p independently by literal field arithmetic.
        linear=[delta,Z];polynomial=[0,A1,A2,A3]
        shifted_curve=add(scale(fpow([p,1],5),a),scale(fpow([p,1],3),b))
        shifted_curve=add(shifted_curve,[mul(a,power(p,5))^mul(b,power(p,3))])
        norm=add(add(pmul(polynomial,polynomial),pmul(linear,polynomial)),pmul(pmul(linear,linear),shifted_curve))
        Rb=mul(A3,A3)^mul(mul(a,p),mul(Z,Z))
        Rc=mul(delta,mul(Z,Z))^mul(a,mul(delta,delta))
        rhs=pmul([0,0,0,1],pmul([1,0,1],[Rc,Rb,mul(a,mul(Z,Z))]))
        assert norm==rhs
        # The same residual divisor is contained in f_P=0, now in global x.
        Xp=[p,1]
        polynomial_global=add(add(scale(Xp,A1),scale(fpow(Xp,2),A2)),scale(fpow(Xp,3),A3))
        linear_global=add(scale(Xp,Z),[delta])
        f_on_residual=add(pmul(linear_global,add(v,[y])),polynomial_global)
        assert not remainder(f_on_residual,u)
        assert len(remainder(u,linear_global))==1 and remainder(u,linear_global)[0]
        checks.append({'p_binary_hex':hex(p),'y_binary_hex':hex(y),'Z_binary_hex':hex(Z),'norm_factorization':True,'same_full_residual_divisor':True})
    assert len(seen)==4 and L
    out.update({'status':'PASS_EXACT_FOUR_POINT_PACKET','modulus_binary_hex':hex(modulus),
                'z_binary_hex':hex(z),'beta_binary_hex':hex(beta),
                'residual_divisor_binary_hex':{'L':hex(L),'M':hex(M),'slope':hex(nu),'constant':hex(v0)},
                'points':checks,'scope':'One exact four-point packet for psi=3+2g at mu^5=1. This refutes nodality for that selected isogeny; it does not exclude other norm-thirteen isogenies.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_packet_binary_verifier.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
