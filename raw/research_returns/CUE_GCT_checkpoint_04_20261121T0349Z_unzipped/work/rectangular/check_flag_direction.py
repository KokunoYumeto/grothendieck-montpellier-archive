"""Exact tensor checks for G17 with a nontrivial Veronese and flag factor.
This builds the dual wedge vector in tensor words, not only its weight.
"""
from itertools import product,permutations
from math import factorial,comb
from pathlib import Path
import json
import sympy as sp


def run(m,n,s,nu):
    a=n-m;eta=tuple(x-nu[-1] for x in nu)
    theta=[(sp.Rational(nu[i],s)-(a if i==0 else 0))/m for i in range(4)]
    assert min(theta)>0 and sum(theta)==1
    first=[]
    for i in range(4):
        beta=[0]*4;beta[0]=a;beta[i]+=m
        coef=sp.sqrt(theta[i]*(1 if i==0 else comb(n,m)))
        first.append((tuple(beta),coef))
    aux={():sp.Integer(1)}
    for r in range(1,4):
      for repeat in range(eta[r-1]-eta[r]):
        step={}
        for old,c in aux.items():
          for perm in permutations(range(r)):
            inv=sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
            step[old+perm]=c*(-1)**inv/sp.sqrt(factorial(r))
        aux=step
    w={}
    for terms in product(first,repeat=s):
      bb=tuple(x[0] for x in terms);cc=sp.prod(x[1] for x in terms)
      for aa,coef in aux.items():w[(bb,aa)]=sp.simplify(cc*coef)
    def action(i,j):
        out={}
        def add(k,c):out[k]=out.get(k,0)+c
        for (bb,aa),coef in w.items():
          for h,beta in enumerate(bb):
            if beta[j]:
              b=list(beta);b[j]-=1;b[i]+=1;new=list(bb);new[h]=tuple(b)
              add((tuple(new),aa),beta[j]*coef)
          for h,value in enumerate(aa):
            if value==i:
              new=list(aa);new[h]=j;add((bb,tuple(new)),-coef)
        return {k:sp.simplify(v) for k,v in out.items() if v!=0}
    def inner(v):
        total=0
        for (bb,aa),coef in w.items():
          norm=sp.prod(sp.Rational(sp.prod(factorial(bi) for bi in beta),factorial(n)) for beta in bb)
          total+=sp.conjugate(coef)*v.get((bb,aa),0)*norm
        return sp.simplify(total)
    assert inner(w)==1
    columns=[action(i,j) for i in range(4) for j in range(4) if i!=j]
    for i in range(3):
      left=action(i,i);right=action(i+1,i+1)
      columns.append({k:sp.simplify(left.get(k,0)-right.get(k,0)) for k in set(left)|set(right)})
    assert all(inner(c)==0 for c in columns)
    keys=sorted(set(w).union(*(set(c) for c in columns)))
    mat=sp.Matrix([[c.get(key,0) for c in columns] for key in keys])
    r=mat.rank();rplus=mat.row_join(sp.Matrix([w.get(k,0) for k in keys])).rank()
    assert (r,rplus)==(15,16)
    return {'m':m,'n':n,'s':s,'nu':nu,'eta':eta,'theta':[str(t) for t in theta],
            'auxiliary_tensor_words':len(aux),'total_support':len(w),
            'norm_squared':1,'all15_moments_zero':True,'Lie_rank':r,'augmented_rank':rplus}

results=[]
for case in [(3,4,2,(4,2,1,1)),(4,5,2,(4,3,2,1))]:
    result=run(*case);results.append(result);print(json.dumps(result),flush=True)
Path(__file__).with_name('flag_direction_check.json').write_text(json.dumps({'all_passed':True,'results':results},indent=2)+'\n')
