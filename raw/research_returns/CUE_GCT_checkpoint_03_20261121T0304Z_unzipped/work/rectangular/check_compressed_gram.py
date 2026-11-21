"""Small exact tests of the compressed coefficient Gram formula.
The tensor columns and the kernel coefficients are built separately.
"""
from itertools import product
from math import factorial
from pathlib import Path
import json
import sympy as sp


def compositions(total,length):
    if length==1:yield(total,);return
    for j in range(total+1):
        for tail in compositions(total-j,length-1):yield(j,)+tail


def run_case(label,f,d,expected):
    n=2;N=2;D=n*d
    x,y=sp.symbols('x y');Z=sp.symbols('z00 z01 z10 z11');W=sp.symbols('w00 w01 w10 w11')
    g=sp.Poly(sp.expand(f.subs({x:Z[0]*x+Z[2]*y,y:Z[1]*x+Z[3]*y},simultaneous=True)),x,y)
    gg={beta:g.coeff_monomial(x**beta[0]*y**beta[1]) for beta in compositions(n,N)}
    kernel0=factorial(n)*sum(factorial(b[0])*factorial(b[1])*v*v.xreplace(dict(zip(Z,W))) for b,v in gg.items())
    kernel=sp.Poly(sp.expand(kernel0**d),*(Z+W))
    alphas=list(compositions(D,4));index={a:i for i,a in enumerate(alphas)};M=len(alphas)
    gram=sp.zeros(M,M)
    for exponent,co in kernel.terms():gram[index[exponent[:4]],index[exponent[4:]]]=co
    tensor=[]
    for word in product(range(N),repeat=D):
        value=1
        for block in range(d):
            sub=word[block*n:(block+1)*n]
            beta=(sub.count(0),sub.count(1))
            value*=factorial(beta[0])*factorial(beta[1])*gg[beta]
        value=sp.Poly(sp.expand(value),*Z)
        row=[0]*M
        for exponent,co in value.terms():row[index[exponent]]=co
        tensor.append(row)
    C=sp.Matrix(tensor)
    assert C.T*C==gram
    ranks={}
    for mu in compositions(D,2):
        selected=[j for j,a in enumerate(alphas) if (a[0]+a[1],a[2]+a[3])==mu]
        ranks[mu]=gram.extract(selected,selected).rank()
    mult={}
    for q in range(D//2+1):
        lam=(D-q,q)
        mult[lam]=ranks.get(lam,0)-ranks.get((lam[0]+1,lam[1]-1),0)
    assert mult==expected,(label,mult,expected)
    return {'label':label,'n':n,'d':d,'tensor_rows':2**D,'coefficient_columns':M,
            'all_gram_entries_checked':M*M,'weight_ranks':{str(k):v for k,v in ranks.items()},
            'multiplicities':{str(k):v for k,v in mult.items()}}

x,y=sp.symbols('x y')
results=[
 run_case('pure_quadratic_degree1',x*x,1,{(2,0):1,(1,1):0}),
 run_case('pure_quadratic_degree2',x*x,2,{(4,0):1,(3,1):0,(2,2):0}),
 run_case('nonsingular_quadratic_degree2',x*x+x*y+y*y,2,{(4,0):1,(3,1):0,(2,2):1}),
]
p=Path(__file__).with_name('compressed_gram_check.json')
p.write_text(json.dumps({'all_passed':True,'results':results},indent=2)+'\n')
print(json.dumps({'all_passed':True,'cases':len(results),'gram_entries_checked':sum(x['all_gram_entries_checked'] for x in results)}))
