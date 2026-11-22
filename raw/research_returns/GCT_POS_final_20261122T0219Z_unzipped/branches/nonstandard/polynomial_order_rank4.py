"""Exact Q[D]-module closure of the full rank-four P-generated order.

Coordinates: coefficient of delta^(length(a)+length(b) mod 2) times
C_a tensor C_b (+ its flip when a<b).  The generator actions have
coefficients in Z[D].  Euclidean polynomial row insertion computes the
actual word module, not its saturation.  Used for a separately stated
bar-fixed globalization variant, not for the printed VIII prescription.
"""
from pathlib import Path
from collections import Counter
import itertools,json,time,sys,gzip
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/"dependencies"))
import e4lib as h
R,D=ring("D",QQ)
ZERO,ONE=R.zero,R.one


def axpy(x,y,c):
    if not c:return
    for j,a in y.items():
        b=x.get(j,ZERO)+c*a
        if b:x[j]=b
        else:x.pop(j,None)


def combination(x,a,y,b):
    z={j:c*a for j,c in x.items() if c*a}
    axpy(z,y,b)
    return z


class PolynomialModule:
    def __init__(self):
        self.rows={}
        self.expressions={}
        self.updates=0

    def contains(self,x):
        x=dict(x)
        while x:
            j=min(x)
            if j not in self.rows:return False
            q,r=divmod(x[j],self.rows[j][j])
            if r:return False
            axpy(x,self.rows[j],-q)
        return True

    def add(self,x,expr):
        x,e=dict(x),dict(expr)
        changed=False
        while x:
            j=min(x)
            if j not in self.rows:
                scale=QQ.one/x[j].LC
                self.rows[j]={k:p*scale for k,p in x.items()}
                self.expressions[j]={k:p*scale for k,p in e.items()}
                self.updates+=1
                return True
            b,f=self.rows[j],self.expressions[j]
            a,p=x[j],b[j]
            q,r=divmod(a,p)
            if not r:
                axpy(x,b,-q);axpy(e,f,-q)
                continue
            ss,tt,g=p.gcdex(a)
            assert ss*p+tt*a==g
            pp,aa=p.exquo(g),a.exquo(g)
            new=combination(b,ss,x,tt)
            newexpr=combination(f,ss,e,tt)
            side=combination(x,pp,b,-aa)
            sideexpr=combination(e,pp,f,-aa)
            assert new[j]==g and j not in side and g.is_monic
            self.rows[j],self.expressions[j]=new,newexpr
            self.updates+=1
            changed=True
            x,e=side,sideexpr
        return changed


keys=[(a,b) for a in h.G for b in h.G if a<=b]
index={k:j for j,k in enumerate(keys)}
parity={k:(h.length(k[0])+h.length(k[1]))%2 for k in keys}
CM={}
for a in h.G:
    for si,st in enumerate(h.S):
        vals=h.toCp(h.mulCp(h.Cp[a],st))
        out={}
        for b,p in vals.items():
            if b==a:
                assert p=={1:1,-1:1}
                out[b]=(-1,1)
            else:
                assert set(p)=={0}
                sign=(-1)**((h.length(b)-h.length(a)-1)%2)
                out[b]=(sign*p[0],0)
        CM[a,si]=out


def build_ops():
    operators=[]
    for si in range(3):
        op=[]
        for a,b in keys:
            srcpar=parity[a,b]
            ans={}
            def put(c,d,coef,power):
                if c>d:return
                p=srcpar+power-parity[c,d]
                assert p>=0 and p%2==0
                j=index[c,d]
                ans[j]=ans.get(j,ZERO)+coef*D**(p//2)
                if not ans[j]:del ans[j]
            for x,y in [(a,b)] if a==b else [(a,b),(b,a)]:
                put(x,y,1,2)
                for c,(u,e) in CM[x,si].items():put(c,y,u,e+1)
                for d,(v,f) in CM[y,si].items():put(x,d,v,f+1)
                for c,(u,e) in CM[x,si].items():
                    for d,(v,f) in CM[y,si].items():put(c,d,2*u*v,e+f)
            op.append(ans)
        operators.append(op)
    return operators


OPS=build_ops()


def step(x,si):
    z={}
    for j,p in x.items():axpy(z,OPS[si][j],p)
    return z


def serialize_poly(p):
    return {str(k[0]):str(c) for k,c in sorted(p.items())}


def serialize_vector(v):
    return {str(j):serialize_poly(p) for j,p in sorted(v.items())}


def main():
    start=time.time()
    one={index[h.e,h.e]:ONE}
    M=PolynomialModule()
    M.add(one,{0:ONE})
    words=[()];vectors=[one];head=0
    while head<len(words):
        for si in range(3):
            x=step(vectors[head],si)
            if M.contains(x):continue
            idx=len(words)
            words.append(words[head]+(si+1,));vectors.append(x)
            assert M.add(x,{idx:ONE})
            if len(words)%20==0:
                print(json.dumps({"accepted":len(words),"rank":len(M.rows),
                                  "updates":M.updates,"max_length":max(map(len,words)),
                                  "seconds":time.time()-start}),flush=True)
            if len(words)>=1000:raise RuntimeError("bounded exploratory stop: 1000 words")
        head+=1
    assert len(M.rows)==114
    # Exact bidirectional span and all-degree algebra closure verification.
    for j,b in M.rows.items():
        rebuilt={}
        for w,p in M.expressions[j].items():axpy(rebuilt,vectors[w],p)
        assert rebuilt==b
        assert min(b)==j and b[j].is_monic
    for x in vectors:
        assert M.contains(x)
        for si in range(3):assert M.contains(step(x,si))
    rows=[{"pivot":j,"vector":serialize_vector(M.rows[j]),
           "word_expression":serialize_vector(M.expressions[j])}
          for j in sorted(M.rows)]
    record={"status":"PASS","rank":114,"ambient_rank":300,
            "accepted_words":[list(w) for w in words],"accepted_count":len(words),
            "maximum_word_length":max(map(len,words)),"pivot_updates":M.updates,
            "pivot_degree_counts":dict(Counter(M.rows[j][j].degree() for j in M.rows)),
            "seconds":time.time()-start,
            "scope":"actual Q[D] word order, not integral Z[v±] order or saturation"}
    (HERE/"polynomial_order_rank4_verified.json").write_text(json.dumps(record,indent=2)+"\n")
    with gzip.open(HERE/"polynomial_order_rank4_rows.json.gz","wt") as f:
        json.dump({"coordinates":[[a,b] for a,b in keys],"rows":rows},f)
    print(json.dumps({k:v for k,v in record.items() if k!="accepted_words"},indent=2),flush=True)


if __name__=="__main__":main()
