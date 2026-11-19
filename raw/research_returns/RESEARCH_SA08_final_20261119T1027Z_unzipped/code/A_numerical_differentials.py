"""Exact induced degree lattices in ordinary relative numerical de Rham forms.

R=Num(Z^{n+1}), coordinates T,x_1,...,x_n, base Num(Z T).
F_w Omega^q is generated over Z by beta_a d beta_b1 ... d beta_bq,
with |a|+sum |b_i|<=w. Rational polynomial arithmetic, Hermite and Smith
normal forms compute the entire finite lattice quotient F_w/F_{w-1}.
This checks the specified finite range, not an infinite-range assertion.
"""
from pathlib import Path
from itertools import product, combinations
from functools import lru_cache
import json, time
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

started=time.monotonic()

def indices(d,w):
    return [a for a in product(range(w+1),repeat=d) if sum(a)<=w]

def calculate(n,q,maximum):
    variables=sp.symbols('T '+' '.join('x'+str(i) for i in range(1,n+1)))
    d=n+1
    wedge=list(combinations(range(1,d),q))
    @lru_cache(None)
    def beta(a):
        return sp.expand(sp.prod(sp.prod(variables[j]-i for i in range(a[j]))/sp.factorial(a[j]) for j in range(d)))
    @lru_cache(None)
    def gradient(a):
        return tuple(sp.diff(beta(a),x) for x in variables)
    previous=None
    result=[]
    for w in range(q,maximum+1):
        monomials=indices(d,w-q)
        ambient=[(m,I) for I in wedge for m in monomials]
        positions={key:i for i,key in enumerate(ambient)}
        all_indices=indices(d,w)
        positive=[b for b in all_indices if sum(b)>0]
        columns=[]
        generator_tuples=0
        def visit(a,bs,budget):
            nonlocal generator_tuples
            if len(bs)<q:
                for b in positive:
                    if sum(b)<=budget:
                        visit(a,bs+[b],budget-sum(b))
                return
            generator_tuples+=1
            col=[sp.S.Zero]*len(ambient)
            for I in wedge:
                determinant=sp.det(sp.Matrix([[gradient(b)[j] for j in I] for b in bs]))
                expression=sp.Poly(sp.expand(beta(a)*determinant),variables)
                for monomial,coefficient in expression.terms():
                    if coefficient:
                        col[positions[(monomial,I)]]=coefficient
            if any(col):columns.append(col)
        for a in all_indices:visit(a,[],w-sum(a))
        matrix=sp.Matrix.hstack(*(sp.Matrix(c) for c in columns))
        denominator=sp.ilcm(1,*(entry.q for entry in matrix))
        integral=(matrix*denominator).applyfunc(int)
        hnf=hermite_normal_form(integral)
        assert hnf.rows==hnf.cols==len(ambient)
        if previous:
            old_ambient,old_hnf,old_denominator=previous
            embedded=sp.zeros(len(ambient),len(old_ambient))
            for j,key in enumerate(old_ambient):embedded[positions[key],:]=old_hnf[j,:]
            inclusion=hnf.inv()*embedded*sp.Rational(denominator,old_denominator)
            assert all(entry.q==1 for entry in inclusion)
            snf=smith_normal_form(inclusion,domain=ZZ)
            diagonal=[abs(int(snf[i,i])) for i in range(min(snf.shape))]
        else:
            inclusion=sp.zeros(len(ambient),0)
            diagonal=[]
        rank=sum(v!=0 for v in diagonal)
        result.append({'relative_dimension':n,'form_degree':q,'weight':w,
          'generator_tuples':generator_tuples,'nonzero_generators':len(columns),
          'ambient_rank':len(ambient),'common_denominator':int(denominator),
          'free_rank':len(ambient)-rank,'torsion_invariants':[v for v in diagonal if v>1],
          'monomial_wedge_basis':[[list(a),list(I)] for a,I in ambient],
          'hnf_columns_after_denominator':[[int(hnf[i,j]) for i in range(hnf.rows)] for j in range(hnf.cols)],
          'previous_lattice_inclusion_columns':[[int(inclusion[i,j]) for i in range(inclusion.rows)] for j in range(inclusion.cols)]})
        previous=(ambient,hnf,denominator)
    return result

records=[]
for n,q,w in [(1,1,5),(2,1,4),(2,2,4)]:records.extend(calculate(n,q,w))
example=next(r for r in records if (r['relative_dimension'],r['form_degree'],r['weight'])==(1,1,2))
assert example['free_rank']==2 and example['torsion_invariants']==[2]
output={'status':'all exact assertions passed','cases':len(records),
 'generator_tuples':sum(r['generator_tuples'] for r in records),
 'nonzero_generators':sum(r['nonzero_generators'] for r in records),
 'seconds':time.monotonic()-started,'records':records}
path=Path(__file__).resolve().parents[1]/'logs/A_numerical_differentials.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='records'}))
for r in records:print(json.dumps({k:r[k] for k in ['relative_dimension','form_degree','weight','free_rank','torsion_invariants']}))
