# Section 7: factor each f of E^opp(3) into quantum integers [n]_{q^m}; realize by Weil restrictions of P^{n-1};
# compare graded dimensions (unimodal?) with traces (= f).
import os,sys,json,itertools
from collections import Counter
import sympy as sp
here=os.path.dirname(os.path.abspath(__file__))
v,q,t=sp.symbols('v q t')
R=json.load(open(os.path.join(here,sys.argv[1] if len(sys.argv)>1 else 'e3_constants.json')))
def cyclo_index(poly):
    P=sp.Poly(poly,q)
    for k in range(1,60):
        if sp.Poly(sp.cyclotomic_poly(k,q),q)==P: return k
    return None
def qint_cyc(n,m):  # cyclotomic multiset of (q^{mn}-1)/(q^m-1)
    return Counter(k for k in sp.divisors(n*m) if m%k!=0)
def covers(target):
    """all multisets of (n,m) whose cyclotomic multisets sum to target (Counter)"""
    ks=sorted(target); maxk=max(ks) if ks else 0
    cands=[(n,m) for m in range(1,maxk+1) for n in range(2,maxk+1) if n*m<=4*maxk and all(target.get(k,0)>=c for k,c in qint_cyc(n,m).items())]
    sols=[]
    def rec(rem,start,chosen):
        if sum(rem.values())==0: sols.append(tuple(chosen)); return
        for i in range(start,len(cands)):
            n,m=cands[i]; cc=qint_cyc(n,m)
            if all(rem.get(k,0)>=c for k,c in cc.items()):
                r2=rem.copy(); r2.subtract(cc); rec(+r2,i,chosen+[(n,m)])
    rec(+target,0,[]); return sols
def dims_of(cover):
    D=sp.Integer(1)
    for n,m in cover: D*=sum(t**j for j in range(n))**m
    return sp.Poly(sp.expand(D),t).all_coeffs()
def unimodal(seq):
    k=seq.index(max(seq)); return all(seq[i]<=seq[i+1] for i in range(k)) and all(seq[i]>=seq[i+1] for i in range(k,len(seq)-1))
rows=[]
for r in R:
    f=sp.sympify(r['f'])
    P=sp.Poly(sp.expand(f*v**200),v); exps=[m[0]-200 for m in P.monoms()]
    lo=min(exps)
    Pq=sp.expand(sp.cancel(f*v**(-lo))).subs(v,sp.sqrt(q))   # polynomial in q (all exponents even)
    Pq=sp.Poly(sp.expand(Pq),q)
    content,fl=sp.factor_list(Pq.as_expr())
    cyc=Counter(); noncyc=sp.Integer(1); ok=True
    for g,e in fl:
        k=cyclo_index(g)
        if k is None: noncyc*=g**e
        elif k==1: ok=False  # (q-1) factor would be a torus factor, should not occur in f
        else: cyc[k]+=e
    sols=covers(cyc) if sum(cyc.values())>0 else [()]
    ncpoly=sp.Poly(sp.expand(noncyc),q).all_coeffs()
    res={'b':r['b'],'bp':r['bp'],'bpp':r['bpp'],'a':r['a'],'f_unimodal':r['unimodal'],'content':int(content),
         'cyclotomic':dict(cyc),'noncyclotomic_part':str(sp.factor(noncyc)),'n_quantum_factorizations':len(sols)}
    best=None
    for s in sols:
        d=dims_of(s); dd=sp.Poly(sp.expand(sp.Poly(d[::-1],t).as_expr()*sp.Poly(ncpoly[::-1],t).as_expr()),t).all_coeffs()
        dd=[int(content)*int(x) for x in dd]
        u=unimodal(dd) and dd==dd[::-1] and all(x>=0 for x in dd)
        if best is None or (u and not best[1]): best=(s,u,dd)
    res['realization']=[list(x) for x in best[0]]; res['dims_unimodal']=best[1]; res['dims']=best[2]
    res['all_factorizations']=[[list(x) for x in s] for s in sols]
    res['noncyc_nonneg']=all(c>=0 for c in ncpoly)
    rows.append(res)
json.dump(rows,open(os.path.join(here,'quantum_realize.json'),'w'),indent=0)
tot=len(rows)
print('constants:',tot)
print('pure quantum-integer products (no non-cyclotomic part):',sum(1 for x in rows if x['noncyclotomic_part']=='1'))
print('realization with symmetric unimodal dims:',sum(1 for x in rows if x['dims_unimodal']))
print('unique quantum factorization (canonical):',sum(1 for x in rows if x['n_quantum_factorizations']==1),
      ' several:',sum(1 for x in rows if x['n_quantum_factorizations']>1))
fails=[x for x in rows if not x['f_unimodal']]
print('the',len(fails),'non-unimodal f:')
for x in fails: print(' ',x['b'],x['bp'],x['bpp'],'content',x['content'],'cyc',x['cyclotomic'],'noncyc',x['noncyclotomic_part'],'factorizations',x['all_factorizations'],'dims',x['dims'],'unimodal dims',x['dims_unimodal'])
bad=[x for x in rows if not x['dims_unimodal']]
print('constants with no unimodal realization:',len(bad))
for x in bad[:10]: print(' ',x['b'],x['bp'],x['bpp'],x['cyclotomic'],x['noncyclotomic_part'],x['dims'])
from collections import Counter as Ct
print('non-cyclotomic parts occurring:',Ct(x['noncyclotomic_part'] for x in rows).most_common(12))
