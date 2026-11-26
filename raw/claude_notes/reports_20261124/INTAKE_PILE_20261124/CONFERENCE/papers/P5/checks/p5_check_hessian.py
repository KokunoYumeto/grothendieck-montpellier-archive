"""(h) P-F24's Hessian locus: the projective rank<=2 locus of the half Hessian of the chain cubic
is [e_1] and the three points [a e_{n-1} + b e_n], a=0 or a^2=3b^2 (paper P5, Prop. on the chain stabilizer).
a0805369bae2ebddc (Claude Opus 5.5 at effort high), 25 Nov 2026."""
import sympy as sp, itertools
res=[]
for n in (4,5,6):
    x=sp.symbols(f'x1:{n+1}')
    F=sum(x[i]**2*x[i+1] for i in range(n-1))+x[n-1]**3
    H=sp.Matrix(n,n,lambda i,j: sp.diff(F,x[i],x[j])/2)
    minors=set()
    for R in itertools.combinations(range(n),3):
        for Cc in itertools.combinations(range(n),3):
            mnr=sp.expand(H.extract(list(R),list(Cc)).det())
            if mnr!=0: minors.add(mnr)
    # affine charts x_k = 1 cover projective space
    pts=set()
    for k in range(n):
        sub={x[k]:1}
        eqs=[sp.expand(m.subs(sub)) for m in minors]
        eqs=[e for e in eqs if e!=0]
        unknowns=[v for v in x if v!=x[k]]
        sols=sp.solve(eqs, unknowns, dict=True)
        for s in sols:
            vec=[sp.nsimplify(s.get(v, v)) if v!=x[k] else 1 for v in x]
            assert all(not isinstance(c,sp.Symbol) for c in vec), ('positive-dimensional component', n, k, s)
            # normalize projectively
            first=next(c for c in vec if c!=0)
            pts.add(tuple(round(complex(sp.N(c/first)).real,9)+0.0 for c in vec))
    res.append((n,sorted(pts,key=str)))
for n,p in res: print(n,p)
ok=all(len(p)==4 for n,p in res)
line=f"(h) half-Hessian rank<=2 locus = [e_1] + 3 collinear points on <e_(n-1),e_n> for n=4,5,6: {ok}"
print(line); open('p5_checks_output.txt','a',encoding='utf-8').write(line+'\n')
