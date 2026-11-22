#!/usr/bin/env python3
"""Finite first-variation probe, not a uniform nonproduct proof.

Pull the proved sharp mixed (6,3) seed back by ordinary Verschiebung.
Reuse explicitly the retained one-factor Cartier formulas, with no execution
of that older probe's top-level search or alteration of its output.
"""
from pathlib import Path
from time import perf_counter
import ast, itertools, json, random

started=perf_counter()
source=Path(__file__).with_name('A3_mixed_product_probe.py')
tree=ast.parse(source.read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],
                        type_ignores=[]),str(source),'exec'))

def padd(*terms):
    ans=set()
    for a in terms:ans.symmetric_difference_update(a)
    return ans

def pmul(a,b):
    return padd(*(multiply(x,y,True) for x in a for y in b))

def ppow(a,n):
    ans={(0,0)}
    for _ in range(n):ans=pmul(ans,a)
    return ans

# For E/F2, trace=-1 and V=-1-F. These rational functions give V.
u={(1,0),(-1,0)}
v={(0,1),(-2,1),(0,0),(-1,0),(-2,0)}
assert not padd(pmul(v,v),pmul(u,v),ppow(u,3),{(0,0)})
seed=[({(0,0),(1,0)},(0,0)),
      ({(0,0),(1,0),(1,1),(3,0)},(1,0)),
      ({(1,0),(3,0)},(0,1))]
lifted=[]
for coeff,z in seed:
    pull=padd(*(pmul(ppow(u,i),ppow(v,j)) for i,j in coeff))
    pull=pmul({(3,0)},pull)
    assert all(i>=0 for i,j in pull)
    lifted.extend((t,z) for t in pull)

first,second=basis(12),basis(3)
pairs=list(itertools.product(first,second))
indices={v:i for i,v in enumerate(pairs)}
section=sum(1<<indices[v] for v in lifted)
b=len(pairs)
m1=[[cartier(multiply(c,u,True),True) for u in first] for c in first]
m2=[[cartier(multiply(c,u,False),False) for u in second] for c in second]
coefficients=[]
for c,d in itertools.product(range(12),range(3)):
    coefficients.append([
      sum(1<<indices[(u,v)] for u in m1[c][i] for v in m2[d][j])
      for i,j in itertools.product(range(12),range(3))])

def matrix(s):
    columns=[0]*b
    for h in range(b):
        if s>>h&1:columns=[x^y for x,y in zip(columns,coefficients[h])]
    return columns

def transpose(cols,n):
    return [sum(((cols[j]>>i)&1)<<j for j in range(n)) for i in range(n)]

def nullspace(rows,n):
    rows=rows[:];pivots=[];r=0
    for j in range(n):
        ix=next((i for i in range(r,len(rows)) if rows[i]>>j&1),None)
        if ix is None:continue
        rows[r],rows[ix]=rows[ix],rows[r]
        for i in range(len(rows)):
            if i!=r and rows[i]>>j&1:rows[i]^=rows[r]
        pivots.append(j);r+=1
    ans=[]
    for j in range(n):
        if j in pivots:continue
        v=1<<j
        for i,k in enumerate(pivots):
            if rows[i]>>j&1:v|=1<<k
        ans.append(v)
    return ans

def coordinate_solver(vectors):
    piv={}
    for i,v in enumerate(vectors):
        coord=1<<i
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j][0];coord^=piv[j][1]
            else:piv[j]=(v,coord);break
        assert v
    def solve(v):
        ans=0
        while v:
            j=v.bit_length()-1
            assert j in piv,('not in span',v)
            v^=piv[j][0];ans^=piv[j][1]
        return ans
    return solve

def toral(s):
    ans=0
    for j,((i,h),z) in enumerate(pairs):
        if not(s>>j&1):continue
        if (i+h)%2:ans^=1<<j
        if h:ans^=1<<indices[((i+2,0),z)]
    return ans

C=matrix(section);F=transpose(C,b)
assert apply(C,section)==apply(C,toral(section))==0
stable,sequence=stable_rank(C)
I=nullspace([section,toral(section)],b)
coords=coordinate_solver(I)
FI=[coords(apply(F,x)) for x in I]
kernel=nullspace(transpose(FI,len(I)),len(I))
left=nullspace(FI,len(I))
full_kernel=[apply(I,x) for x in kernel]
variation=[]
for j in range(b):
    Ft=transpose(coefficients[j],b)
    columns=[]
    for k in full_kernel:
        z=coords(apply(Ft,k))
        columns.append(sum(((lam&z).bit_count()%2)<<i for i,lam in enumerate(left)))
    variation.append(columns)

out={'scope':'Finite single-curve etale-double-cover first-variation probe only',
     'curve':'y^2+xy=x^3+1 over F2',
     'isogeny_functions':{'u':sorted(u),'v':sorted(v)},
     'seed':'1+z+x(1+z+w)+xy*z+x^3(z+w)',
     'lifted_section_bits':section,'lifted_section_terms':lifted,
     'rank_sequence_C':sequence,'stable_rank_C':stable,
     'rank_C':rank(C),'I_dimension':len(I),'rank_F_on_I':rank(FI),
     'kernel_dimension_FI':len(kernel),'cokernel_dimension_FI':len(left),
     'variation_matrices_by_section_basis':variation}
if len(kernel)==len(left)==2:
    def determinant(cols):
        return ((cols[0]&1)*((cols[1]>>1)&1))^(((cols[0]>>1)&1)*(cols[1]&1))
    nonzero=[]
    for i in range(b):
        if determinant(variation[i]):nonzero.append([i,i])
        for j in range(i+1,b):
            z=[x^y for x,y in zip(variation[i],variation[j])]
            if determinant(z)^determinant(variation[i])^determinant(variation[j]):
                nonzero.append([i,j])
    out['quadratic_determinant_nonzero_monomials']=nonzero
    out['first_variation_determinant_identically_zero']=not nonzero
out['elapsed_seconds']=perf_counter()-started
out['status']='COMPLETED_FINITE_PROBE'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in
 ('variation_matrices_by_section_basis','lifted_section_terms')},indent=2))
