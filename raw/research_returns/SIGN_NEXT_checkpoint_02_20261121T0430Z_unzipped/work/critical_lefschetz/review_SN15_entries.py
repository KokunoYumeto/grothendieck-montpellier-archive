#!/usr/bin/env python3
"""Independent signed full-exterior check of both SN-15 compressed formulas.
No word closure and no invocation of the author's matrix-construction code.
"""
from pathlib import Path
from math import comb, factorial
import json

def add(to, mask, coefficient):
    if coefficient:
        to[mask] = to.get(mask, 0) + coefficient
        if not to[mask]: del to[mask]

def wedge(left, right):
    if left & right: return None, 0
    sign = (-1)**sum((right & ((1 << i)-1)).bit_count()
                    for i in range(left.bit_length()) if left & (1 << i))
    return left | right, sign

def interior(mask, i):
    if not mask & (1 << i): return None, 0
    return mask ^ (1 << i), (-1)**((mask & ((1 << i)-1)).bit_count())

def L(vector, n):
    ans={}
    for m,z in vector.items():
        for i in range(n):
            t,s=wedge((1 << (2*i)) | (1 << (2*i+1)), m)
            if s: add(ans,t,z*s)
    return ans

def D(vector, n):
    ans={}
    for m,z in vector.items():
        for i in range(n):
            t,s=interior(m,2*i)
            if s:
                q,r=interior(t,2*i+1)
                if r: add(ans,q,z*s*r)
    return ans

def block(source,n):
    active=[i for i in range(n) if ((source >> (2*i)) & 3) in (0,3)]
    fixed=source
    for i in active: fixed &= ~(3 << (2*i))
    S={i for i in active if ((source >> (2*i)) & 3)==3}
    out=[]
    for bits in range(1 << len(active)):
        T={active[j] for j in range(len(active)) if bits & (1 << j)}
        target=fixed
        for i in T: target |= 3 << (2*i)
        out.append((target,len(T),len(S & T)))
    return len(active),len(S),out

def expected(v,k,l,t,a,c,b,n,projectors):
    s=l-c
    if not 0 <= s <= t or k != s+a:return 0
    return factorial(a)*factorial(c)*comb(t,s)*(int(b==n-v+2*l) if projectors else (v-2*s)**b)

results=[]
for n in range(5):
    checked=0
    H={}
    for src in range(1 << (2*n)):
        h=D(L({src:1},n),n)
        for m,z in L(D({src:1},n),n).items():add(h,m,-z)
        assert h==({src:n-src.bit_count()} if n!=src.bit_count() else {})
        H[src]=h.get(src,0)
    for src in range(1 << (2*n)):
        v,l,targets=block(src,n)
        dp={src:1}
        for c in range(n+1):
            for b in range(2*n+1):
                hp={m:z*H[m]**b for m,z in dp.items() if z*H[m]**b}
                lp=hp
                ldp=dp if b==src.bit_count() else {}
                for a in range(n+1):
                    for target,k,t in targets:
                        assert lp.get(target,0)==expected(v,k,l,t,a,c,b,n,False),(n,src,target,a,c,b,'ordinary')
                        assert ldp.get(target,0)==expected(v,k,l,t,a,c,b,n,True),(n,src,target,a,c,b,'projectors')
                        checked+=2
                    assert all(m in {x[0] for x in targets} for m in lp)
                    assert all(m in {x[0] for x in targets} for m in ldp)
                    lp=L(lp,n);ldp=L(ldp,n)
            dp=D(dp,n)
    row_count=sum(sum(min(k,l)-max(0,k+l-v)+1 for k in range(v+1) for l in range(v+1)) for v in range(n+1))
    assert row_count==comb(n+4,4)
    results.append({'n':n,'signed_exterior_basis_vectors':1 << (2*n),'entry_equalities':checked,'compressed_rows':row_count,'status':'PASS'})
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps({'method':'direct signed exterior wedge/contraction, all full-basis entries in each preserved Boolean block','results':results,'total_entry_equalities':sum(x['entry_equalities'] for x in results)},indent=2)+'\n')
print(out.read_text())
