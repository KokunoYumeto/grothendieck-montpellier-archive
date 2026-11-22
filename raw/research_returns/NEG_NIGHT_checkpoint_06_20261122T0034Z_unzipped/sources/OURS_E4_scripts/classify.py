import sympy as sp
v=sp.symbols('v')
t=v-1/v
def classify(c):
    """c: sympy rational function in v. Returns dict with a, sign, f, laurent, bar, nonneg, unimodal."""
    c=sp.cancel(sp.together(c))
    if c==0: return None
    a=0; g=c
    while True:
        val=sp.limit(g,v,1) if sp.denom(g).subs(v,1)==0 else g.subs(v,1)
        if val!=0: break
        g=sp.cancel(g/t); a+=1
    sign=1 if val>0 else -1
    f=sp.cancel(sign*g)
    num,den=sp.fraction(sp.together(f))
    # Laurent test: den must be a monomial c*v^k
    dp=sp.Poly(den,v)
    laurent=len(dp.terms())==1
    res={'a':a,'sign':sign,'f':f,'laurent':laurent}
    if laurent:
        (k,),dc=dp.terms()[0]
        npoly=sp.Poly(sp.expand(num/dc),v)
        coeffs={m[0]-k:co for m,co in npoly.terms()}
        exps=sorted(coeffs)
        bar=all(coeffs.get(-e,0)==coeffs[e] for e in exps)
        nonneg=all(co>=0 for co in coeffs.values())
        # unimodal on the support lattice (step 2 if all exponents have one parity)
        step=2 if len({e%2 for e in exps})==1 else 1
        lo,hi=exps[0],exps[-1]
        seq=[coeffs.get(e,0) for e in range(lo,hi+1,step)]
        m=seq.index(max(seq))
        unimodal=all(seq[i]<=seq[i+1] for i in range(m)) and all(seq[i]>=seq[i+1] for i in range(m,len(seq)-1))
        res.update(bar=bar,nonneg=nonneg,unimodal=unimodal,coeffs=[seq[i] for i in range(len(seq))],lo=lo,step=step)
    return res
