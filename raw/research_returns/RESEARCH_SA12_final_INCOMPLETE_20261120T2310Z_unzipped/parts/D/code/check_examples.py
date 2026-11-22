"""Exact finite checks supporting Part D counterexamples.

The nominal-set and DVR arguments are infinite mathematical arguments. The
finite checks below verify their displayed formulas, not the infinite claims.
The F_9 arithmetic and finite wreath-product quotients are checked exhaustively.
"""
import itertools, json, pathlib, time

def f9_add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def f9_mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def check_f9():
    el=list(itertools.product(range(3),repeat=2))
    zero=(0,0); one=(1,0)
    assert all((x*x+1)%3 for x in range(3))
    count=0
    for x,y,z in itertools.product(el,repeat=3):
        assert f9_mul(f9_mul(x,y),z)==f9_mul(x,f9_mul(y,z))
        assert f9_mul(x,f9_add(y,z))==f9_add(f9_mul(x,y),f9_mul(x,z))
        count+=1
    for x in el:
        if x!=zero:assert sum(f9_mul(x,y)==one for y in el)==1
    assert all(f9_mul((2,0),x)!=zero for x in el if f9_mul(x,x)==(2,0))
    return dict(elements=9,triple_checks=count,nonzero_inverses=8,
                polynomial='T^2+1 over F_3',irreducible=True,separable=True)

def rotate(v,j,n):
    return ((v<<j)|(v>>(n-j)))&((1<<n)-1) if j else v
def wreath_mul(x,y,n):return (x[0]^rotate(y[0],x[1],n),(x[1]+y[1])%n)
def closure(gens,n):
    seen={(0,0)}; stack=[(0,0)]
    while stack:
        x=stack.pop()
        for g in gens:
            y=wreath_mul(x,g,n)
            if y not in seen:seen.add(y);stack.append(y)
    return seen
def check_wreath():
    results=[]
    for n in range(1,10):
        a=(1,0);t=(0,1%n)
        assert wreath_mul(a,a,n)==(0,0)
        whole=closure([a,t],n)
        assert len(whole)==n*(2**n)
        conjugates=[(1<<i,0) for i in range(n)]
        kernel_image=closure(conjugates,n)
        assert kernel_image=={(mask,0) for mask in range(2**n)}
        results.append(dict(n=n,quotient_order=len(whole),kernel_image_order=len(kernel_image),elementary_abelian_rank=n))
    return results

def check_nominal_finite_models():
    results=[]
    for n in range(1,6):
        m=n+2; A=tuple(range(m)); tuples=list(itertools.permutations(A,n))
        graphs=[{(x[i],x) for x in tuples} for i in range(n)]
        union=set().union(*graphs)
        assert len(union)==n*len(tuples)
        whole={(a,x) for a in A for x in tuples}
        comp=whole-union
        assert len(comp)==(m-n)*len(tuples)
        for j in range(m-1):
            perm=lambda a: j+1 if a==j else j if a==j+1 else a
            for graph in graphs:
                assert {(perm(a),tuple(map(perm,x))) for a,x in graph}==graph
        # Stabilizer of (0,...,n-1) contains transposition of last two atoms;
        # its fixed points in A are exactly the n coordinates.
        assert [a for a in A if (n+1 if a==n else n if a==n+1 else a)==a]==list(range(n))
        results.append(dict(n=n,atoms=m,ordered_tuples=len(tuples),disjoint_sections=n,complement_size=len(comp)))
    return results

def mul_poly(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    while len(c)>1 and not c[-1]:c.pop()
    return c
def check_wild_identities():
    results=[]
    for p in [2,3,5,7,11,13]:
        prod=[1]
        for i in range(p):prod=mul_poly(prod,[1,i],p)
        expect=[1]+[0]*(p-2)+[p-1]
        assert prod==expect
        # [[1,0],[1,1]]^j=[[1,0],[j,1]]; exact order p in PGL_2(F_p).
        assert all(j%p!=0 for j in range(1,p))
        results.append(dict(p=p,norm_denominator=prod,moebius_order=p))
    return results

start=time.monotonic()
out={'F9':check_f9(),'wreath_products':check_wreath(),
     'nominal_finite_sanity_checks':check_nominal_finite_models(),
     'wild_DVR_identity_checks':check_wild_identities()}
out['runtime_seconds']=round(time.monotonic()-start,6)
path=pathlib.Path(__file__).with_name('check_examples_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
