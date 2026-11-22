"""Exact bounded five-packet search on characteristic-two genus-two curves.

Curves: y^2+x*y=x^5+a*x^3+b*x, b!=0. All rational points are
enumerated over each specified finite field. General characteristic-two
Cantor arithmetic computes [5](P-infinity). No geometric exhaustion or
nodality conclusion is inferred from absence in a finite search.
"""
from pathlib import Path
import datetime, hashlib, json, time, traceback

START = time.perf_counter()
W = Path(__file__).resolve().parents[1]
OUT = W/'outputs/root_f1_five_packets.json'
assert not OUT.exists()

class Field:
    def __init__(self,n,mod):
        self.n,self.mod,self.q=n,mod,1<<n
        self.one=(1,)
        self.mul_checks=0
        self.invtab=[0]+[self.pow(x,self.q-2) for x in range(1,self.q)]
        assert all(self.mul(x,self.invtab[x])==1 for x in range(1,self.q))
        self.sq=[self.mul(x,x) for x in range(self.q)]
        self.as_roots={}
        for x in range(self.q):self.as_roots.setdefault(self.sq[x]^x,[]).append(x)
        assert all(len(v)==2 for v in self.as_roots.values())
    def mul(self,a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.mod
        return z
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def norm(self,a):
        a=list(a)
        while a and not a[-1]:a.pop()
        return tuple(a)
    def add(self,a,b):
        r=[0]*max(len(a),len(b))
        for i,x in enumerate(a):r[i]^=x
        for i,x in enumerate(b):r[i]^=x
        return self.norm(r)
    def pmul(self,a,b):
        if not a or not b:return ()
        r=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):r[i+j]^=self.mul(x,y)
        return self.norm(r)
    def scale(self,a,c):return self.norm([self.mul(x,c) for x in a])
    def divmod(self,a,b):
        assert b
        r=list(a);q=[0]*max(0,len(a)-len(b)+1);inv=self.invtab[b[-1]]
        while len(r)>=len(b):
            j=len(r)-len(b);c=self.mul(r[-1],inv);q[j]=c
            for i,x in enumerate(b):r[i+j]^=self.mul(c,x)
            while r and not r[-1]:r.pop()
        return self.norm(q),tuple(r)
    def rem(self,a,b):return self.divmod(a,b)[1]
    def exact(self,a,b):
        q,r=self.divmod(a,b);assert not r,(a,b,r)
        return q
    def monic(self,a):return self.scale(a,self.invtab[a[-1]])
    def xgcd(self,a,b):
        s0,s1,t0,t1=(1,),(),(),(1,)
        while b:
            q,r=self.divmod(a,b);a,b=b,r
            s0,s1=s1,self.add(s0,self.pmul(q,s1))
            t0,t1=t1,self.add(t0,self.pmul(q,t1))
        c=self.invtab[a[-1]]
        return self.scale(a,c),self.scale(s0,c),self.scale(t0,c)

class Jacobian:
    def __init__(self,F,a,b):
        self.F,self.a,self.b=F,a,b
        self.h=(0,1);self.f=(0,b,0,a,0,1);self.zero=((1,),())
        self.additions,self.reductions,self.validations=0,0,0
    def valid(self,D):
        u,v=D;F=self.F
        assert u and u[-1]==1 and len(u)<=3 and len(v)<len(u)
        assert not F.rem(F.add(F.add(F.pmul(v,v),F.pmul(self.h,v)),self.f),u),D
        self.validations+=1
        return D
    def neg(self,D):return self.valid((D[0],self.F.rem(self.F.add(D[1],self.h),D[0])))
    def add(self,A,B):
        F=self.F;u1,v1=A;u2,v2=B
        self.additions+=1
        d1,e1,e2=F.xgcd(u1,u2)
        d,c1,c2=F.xgcd(d1,F.add(F.add(v1,v2),self.h))
        s1,s2,s3=F.pmul(c1,e1),F.pmul(c1,e2),c2
        u=F.exact(F.pmul(u1,u2),F.pmul(d,d))
        num=F.add(F.add(F.pmul(F.pmul(s1,u1),v2),F.pmul(F.pmul(s2,u2),v1)),
                  F.pmul(s3,F.add(F.pmul(v1,v2),self.f)))
        v=F.rem(F.exact(num,d),u)
        while len(u)>3:
            un=F.monic(F.exact(F.add(F.add(self.f,F.pmul(self.h,v)),F.pmul(v,v)),u))
            v=F.rem(F.add(self.h,v),un);u=un;self.reductions+=1
        return self.valid((F.monic(u),v))
    def times(self,n,D):
        out=self.zero
        while n:
            if n&1:out=self.add(out,D)
            n>>=1
            if n:D=self.add(D,D)
        return out
    def points(self):
        F=self.F;out=[None,(0,0)]
        for x in range(1,F.q):
            rhs=F.pow(x,5)^F.mul(self.a,F.pow(x,3))^F.mul(self.b,x)
            zval=F.mul(rhs,F.invtab[F.sq[x]])
            out.extend((x,F.mul(x,z)) for z in F.as_roots.get(zval,[]))
        return out
    def divisor(self,P):return self.zero if P is None else self.valid(((P[0],1),F.norm((P[1],))))

try:
    records=[]
    for n,mod in [(2,0b111),(4,0b10011),(6,0b1000011),(8,0b100011011)]:
        F=Field(n,mod)
        for a,b in [(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]:
            J=Jacobian(F,a,b);pts=J.points();groups={};divisors=[]
            for P in pts:
                D=J.divisor(P);divisors.append(D)
                assert J.add(D,J.neg(D))==J.zero
                twice=J.add(D,D)
                five=J.add(J.add(twice,twice),D)
                assert five==J.times(5,D)
                groups.setdefault(five,[]).append(P)
            # Associativity is checked on actual point divisors independently of doubling.
            for i in range(min(24,len(divisors))):
                A=divisors[i];B=divisors[(3*i+1)%len(divisors)];C=divisors[(7*i+2)%len(divisors)]
                assert J.add(J.add(A,B),C)==J.add(A,J.add(B,C))
            multiple=[]
            for key,packet in groups.items():
                if len(packet)<3:continue
                base=J.divisor(packet[0]);dif=[J.add(J.divisor(P),J.neg(base)) for P in packet[1:]]
                assert all(J.times(5,D)==J.zero for D in dif)
                multiple.append({'points':packet,'common_five_divisor':key,'nonzero_differences':dif,
                                 'weil_pairing_automatically_one':F.q%5!=1})
            rec={'extension_degree':n,'modulus':mod,'field_size':F.q,'a':a,'b':b,
                 'rational_points':len(pts),'number_of_packets':len(groups),
                 'packet_size_census':{str(s):sum(len(p)==s for p in groups.values()) for s in sorted({len(p) for p in groups.values()})},
                 'packets_size_at_least_three':multiple,'arithmetic_additions':J.additions,
                 'reductions':J.reductions,'divisor_validations':J.validations}
            records.append(rec)
            print(json.dumps({k:v for k,v in rec.items() if k!='packets_size_at_least_three'}),flush=True)
    result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'runtime_seconds':time.perf_counter()-START,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'records':records,'scope':'Every rational point of the 24 specified curves/finite fields only. Coincident [5] divisors are explicit certificates. No absence claim over an algebraic closure and no incoming-isogeny existence result.'}
except BaseException as exc:
    result={'status':'FAILED','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'runtime_seconds':time.perf_counter()-START,'error':repr(exc),'traceback':traceback.format_exc(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    raise
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2),flush=True)
