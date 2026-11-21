"""Exact finite Enriquez distribution tests for the new affine216 detector.

This is a necessary finite word-image test, not a lift to an actual GT element.
SymPy permutations use right multiplication; matrix actions are inverted when
embedded, so products agree with the left-matrix convention of D23.P10.
"""
from pathlib import Path
import json, sys, time
from sympy.combinatorics import Permutation, PermutationGroup

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'agents/pentagon/cubic_detector_216.json').read_text())
I = (1,0,0,0,1,0,0,0,1)
X, Y = tuple(data['x']), tuple(data['y'])

def mm(a,b):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%3
                 for i in range(3) for j in range(3))
def mp(a,n):
    r=I
    while n:
        if n&1:r=mm(r,a)
        a=mm(a,a);n//=2
    return r
def ap(a):
    p=[3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)
       +(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)]
    return Permutation(p)**-1
def disjoint(ps):
    r=[];off=0
    for p in ps:
        r.extend(off+p(i) for i in range(p.size));off+=p.size
    return Permutation(r)
p = Permutation([1,2,0,3])**-1
t = Permutation([1,2,3,0])**-1
c = Permutation(list(range(1,12))+[0])
cx = Permutation(list(range(12)))
gx, gy = disjoint([ap(X),p]), disjoint([ap(Y),t])
ax, ay = disjoint([ap(X),p,cx]), disjoint([ap(Y),t,c])
d=ax.size

def induced(N, a, b):
    x=list(range(N*d));y=list(range(N*d))
    for j in range(N):
        for v in range(d):
            x[j*d+v]=((j+1)%N)*d+(a(v) if j==N-1 else v)
            y[j*d+v]=j*d+(b(v) if j==0 else v)
    x,y=Permutation(x),Permutation(y)
    # Exact Schreier-generator checks on the zero block.
    assert all((x**N)(i)==a(i) for i in range(d))
    for j in range(1,N):
        z=x**j*y*x**(-j)
        assert all(z(i)==i for i in range(d))
    return x,y

allrows=[]
for N in ([int(sys.argv[1])] if len(sys.argv)>1 else [2,3,4,6]):
    start=time.monotonic();ix,iy=induced(N,ax,ay)
    G=PermutationGroup([disjoint([ix,gx]),disjoint([iy,gy])])
    print('N',N,'building derived generators',flush=True)
    der=G.derived_subgroup()
    selected=list(range(d))+list(range(N*d,N*d+13))
    indexing={v:i for i,v in enumerate(selected)}
    gens=[]
    for g in der.generators:
        assert all(g(v) in indexing for v in selected)
        gens.append(Permutation([indexing[g(v)] for v in selected]))
    J=PermutationGroup(gens)
    order=int(J.order());rows=[]
    print('N',N,'projected derived order',order,flush=True)
    for row in data['six_actual_gentle_residues']:
        rho,e=row['rho'],row['a3'];F=tuple(row['f_matrix'])
        for nu in [0,1]:
            fs=t**(2*nu)*p**rho
            base=disjoint([ap(F),fs]);passing=[]
            for k in range(12):
                expect=disjoint([ap(mm(mp(Y,k),F)),t**k*fs,c**k,base])
                if J.contains(expect):passing.append(k)
            rows.append({'rho':rho,'a3':e,'nu4':nu,'passing_c_mod12':passing})
    out={'N':N,'test':'delta_N(f)=y^c f in affine216 and S4, c_N modulo12',
         'projected_Fprime_order':order,'projected_generators':[g.array_form for g in gens],
         'rows':rows,'elapsed_seconds':time.monotonic()-start,
         'scope':'ordinary common-word images; no gentle or GT lifting asserted'}
    (ROOT/f'records/distribution_216_N{N}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='projected_generators'}),flush=True)
    allrows.append(out)
