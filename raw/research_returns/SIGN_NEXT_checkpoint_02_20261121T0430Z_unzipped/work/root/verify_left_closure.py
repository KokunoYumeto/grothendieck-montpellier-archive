"""Independent left-word closure from signed full exterior matrices.

The producer uses right multiplication on directly constructed Boolean
blocks.  This check constructs wedge and contraction on the full exterior
basis, extracts invariant blocks, and generates words by left multiplication.
It compares complete integral HNF lattices, not only ranks or indices.
SymPy HNF is shared infrastructure, not a second formal arithmetic kernel.
"""
from pathlib import Path
import json, math, time
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
INPUT=HERE.parent/'integral_fock'

def signed_exterior(n):
    dim=1<<(2*n)
    up={};down={}
    for mask in range(dim):
        for j in range(n):
            e=2*j;f=e+1;pair=(1<<e)|(1<<f)
            if mask&pair==0:
                inversions=(mask&((1<<e)-1)).bit_count()+(mask&((1<<f)-1)).bit_count()
                up[mask|pair,mask]=(-1)**inversions
            if mask&pair==pair:
                after_e=mask^(1<<e)
                inversions=(mask&((1<<e)-1)).bit_count()+(after_e&((1<<f)-1)).bit_count()
                down[mask^pair,mask]=(-1)**inversions
    L=S.SparseMatrix(dim,dim,up);D=S.SparseMatrix(dim,dim,down)
    assert D==L.T
    P=[S.SparseMatrix(dim,dim,{(a,a):1 for a in range(dim) if a.bit_count()==d}) for d in range(2*n+1)]
    return L,D,P

def blocks(G,n):
    ans=[]
    for v in range(n+1):
        singleton=sum(1<<(2*j) for j in range(v,n))
        idx=[singleton|sum(3<<(2*j) for j in range(v) if mask>>j&1) for mask in range(1<<v)]
        ans.append(G.extract(idx,idx))
    return ans

def left_action(gs):
    # For row-major coordinates, vec(G A)=(G tensor I)vec(A).
    entries={};offset=0
    for G in gs:
        d=G.rows
        for (r,c),value in G.todok().items():
            for col in range(d):entries[offset+r*d+col,offset+c*d+col]=value
        offset+=d*d
    return S.SparseMatrix(offset,offset,entries)

def check(n,kind,L,D,P):
    t0=time.monotonic()
    generators=[L,D]
    if 'pi' in kind:generators+=P
    if 'div' in kind:
        generators += [G**r/math.factorial(r) for r in range(2,n+1) for G in [L,D]]
    actions=[left_action(blocks(G,n)) for G in generators]
    B=S.Matrix([entry for v in range(n+1) for entry in S.eye(1<<v)])
    history=[]
    while True:
        C=hermite_normal_form(S.Matrix.hstack(B,*[a*B for a in actions]))
        history.append(C.cols)
        if C==B:break
        B=C
        assert len(history)<100
    original=json.loads((INPUT/f'order_basis_n{n}_{kind}.json').read_text())
    assert B==S.Matrix(original['basis_rows']),(n,kind)
    return {'n':n,'kind':kind,'full_integral_lattice_equal':True,
            'left_closure_ranks':history,'seconds':round(time.monotonic()-t0,3)}

results=[]
for n in range(1,5):
    L,D,P=signed_exterior(n)
    for kind in ['ordinary','ordinary_pi','divided','divided_pi']:
        row=check(n,kind,L,D,P)
        results.append(row)
        print(json.dumps(row),flush=True)
(HERE/'left_closure_verification.json').write_text(json.dumps(results,indent=2)+'\n')
