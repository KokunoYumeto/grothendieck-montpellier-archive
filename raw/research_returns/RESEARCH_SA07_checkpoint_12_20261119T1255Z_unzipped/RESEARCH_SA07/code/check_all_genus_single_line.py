#!/usr/bin/env python3
"""Exact all-genus single-line scalar certificate (F.3.32).

Recomputes the twelve Levi-invariant inputs, five detector contractions,
three necessary R rows, and four necessary cyclic ES rows.  It verifies a
literal polynomial row identity on all twelve columns.  No stored matrix,
pickle, finite-genus interpolation, or symbolic inverse is needed.

Conventions: T_D=sum(x tensor D(y)-y tensor D(x)); omega_W is oriented
x tensor y-y tensor x. Source detector signs are diag(+,-,+,-,-).
Only numpy and sympy are external dependencies.
"""
from itertools import combinations, permutations, product
from functools import lru_cache
from time import perf_counter
from math import lcm
import numpy as np
import sympy as sp

started=perf_counter();P=101;AA=-1;BB=-2;s=sp.Symbol('s')

def pairings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in pairings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

def diagrams(n,acount,bcount):
    positions=tuple(range(n))
    for apos in combinations(positions,acount):
        rem=tuple(i for i in positions if i not in apos)
        for bpos in combinations(rem,bcount):
            other=tuple(i for i in rem if i not in bpos)
            for pairs in pairings(other):
                key=[None]*n
                for i in apos:key[i]=AA
                for i in bpos:key[i]=BB
                for label,(i,j) in enumerate(pairs):key[i]=key[j]=label
                yield tuple(key)

@lru_cache(None)
def permute(key,order):
    inverse={old:new for new,old in enumerate(order)};sign=1
    for label in set(key):
        if label<0:continue
        first,second=[i for i,x in enumerate(key) if x==label]
        if inverse[first]>inverse[second]:sign=-sign
    labels={};result=[]
    for i in order:
        x=key[i]
        if x<0:result.append(x)
        else:
            if x not in labels:labels[x]=len(labels)
            result.append(labels[x])
    return tuple(result),sign

def add(a,b,scale=1):
    out=dict(a)
    for key,c in b.items():
        out[key]=out.get(key,0)+scale*c
        if not out[key]:del out[key]
    return out

@lru_cache(None)
def dynkin_orders(n):
    if n==1:return (((0,),1),)
    out=[]
    for tail,c in dynkin_orders(n-1):
        shifted=tuple(i+1 for i in tail)
        out.append(((0,)+shifted,c));out.append((shifted+(0,),-c))
    return tuple(out)

def apply_orders(poly,orders):
    result={}
    for key,c in poly.items():
        for order,d in orders:
            new,sign=permute(key,order)
            result[new]=result.get(new,0)+c*d*sign
    return {key:c for key,c in result.items() if c}

def cyclic(poly):
    n=len(next(iter(poly))) if poly else 8
    return apply_orders(poly,tuple((tuple(range(i,n))+tuple(range(i)),1) for i in range(n)))

def dynkin(poly,head=0):
    if not poly:return {}
    n=len(next(iter(poly)))
    orders=tuple((tuple(range(head))+tuple(i+head for i in order),c) for order,c in dynkin_orders(n-head))
    return apply_orders(poly,orders)

def mod_pivots(matrix):
    A=(np.asarray(matrix,dtype=np.int64)%P).astype(np.int16)
    nr,nc=A.shape;r=0;pivots=[]
    for j in range(nc):
        rows=np.flatnonzero(A[r:,j])
        if not len(rows):continue
        i=r+int(rows[0]);A[[r,i]]=A[[i,r]]
        A[r,j:]=A[r,j:]*pow(int(A[r,j]),-1,P)%P
        targets=np.flatnonzero(A[r+1:,j])+r+1
        if len(targets):
            block=A[targets,j:];block-=A[targets,j,None]*A[r,j:];block%=P;A[targets,j:]=block
        pivots.append(j);r+=1
        if r==nr:break
    return pivots

def matrix_columns(columns):
    keys=sorted(set().union(*(set(c) for c in columns)))
    return np.array([[c.get(key,0) for c in columns] for key in keys],dtype=np.int64).reshape((len(keys),len(columns))),keys

def exact_kernel(matrix):
    rows=mod_pivots(matrix.T)
    if rows:R,pivots=sp.Matrix(matrix[rows,:].tolist()).rref()
    else:R,pivots=sp.zeros(0,matrix.shape[1]),()
    assert len(pivots)==len(rows)
    result=[]
    for free in range(matrix.shape[1]):
        if free in pivots:continue
        denominator=lcm(*[int(sp.denom(R[i,free])) for i in range(len(pivots))])
        v=[0]*matrix.shape[1];v[free]=int(denominator)
        for i,j in enumerate(pivots):v[j]=int(-denominator*R[i,free])
        assert all(sum(int(matrix[i,j])*v[j] for j in range(len(v)))==0 for i in range(matrix.shape[0]))
        result.append(v)
    return result,len(rows)

def linear_combination(columns,coefficients):
    out={}
    for poly,c in zip(columns,coefficients):
        if c:out=add(out,poly,c)
    return out

inputs=[];labels=[]
for m in range(1,5):
    keys=list(diagrams(6,m-1,m-1));index={key:i for i,key in enumerate(keys)}
    allA=[dynkin({key:1}) for key in keys]
    dyn=np.array([[col.get(key,0) for col in allA] for key in keys],dtype=np.int64)
    assert int(abs(dyn).max())**2*dyn.shape[1] < 2**63
    assert np.array_equal(dyn@dyn,6*dyn)
    rank=int(np.trace(dyn))//6
    selected=mod_pivots(dyn);assert len(selected)==rank
    As=[allA[j] for j in selected]
    tensors=[];equations=[]
    for A in As:
        comm={}
        for key,c in A.items():
            comm=add(comm,{(BB,)+key+(AA,):c,(BB,AA)+key:-c})
        T={key:-c for key,c in cyclic(comm).items()}
        lie=add(dynkin(T,1),T,-7)
        consistency=add({key:c for key,c in T.items() if key[0]==BB},comm,m)
        equations.append({(0,)+key:c for key,c in lie.items()}|{(1,)+key:c for key,c in consistency.items()})
        tensors.append(T)
    E,rows=matrix_columns(equations)
    kernel,erank=exact_kernel(E)
    for j,coeff in enumerate(kernel):
        T=linear_combination(tensors,coeff)
        assert T and dynkin(T,1)=={key:7*c for key,c in T.items()}
        assert cyclic(T)=={key:8*c for key,c in T.items()}
        inputs.append(T);labels.append(('positive',m,j))
    print('POSITIVE_BLOCK',m,'RAW_DIAGRAMS',len(keys),'LIE_PARAMETER_DIM',rank,
          'CONSTRAINT_MATRIX',E.shape,'RANK',erank,'INPUT_DIM',len(kernel),flush=True)

keys=list(diagrams(8,0,0))
allC=[cyclic({key:1}) for key in keys]
C=np.array([[col.get(key,0) for col in allC] for key in keys],dtype=np.int64)
assert int(abs(C).max())**2*C.shape[1] < 2**63
assert np.array_equal(C@C,8*C)
selected=mod_pivots(C);assert len(selected)==int(np.trace(C))//8
Ts=[allC[j] for j in selected]
E,rows=matrix_columns([add(dynkin(T,1),T,-7) for T in Ts])
kernel,rank=exact_kernel(E)
assert len(kernel)==5
for j,coeff in enumerate(kernel):
    T=linear_combination(Ts,coeff)
    assert T and dynkin(T,1)=={key:7*c for key,c in T.items()}
    assert cyclic(T)=={key:8*c for key,c in T.items()}
    inputs.append(T);labels.append(('pure',0,j))
print('PURE_W_BLOCK','CYCLIC_DIM',len(Ts),'CONSTRAINT_MATRIX',E.shape,'RANK',rank,'INPUT_DIM',len(kernel))
print('TOTAL_FORMAL_INPUT_DIM',len(inputs))

def pair(x,y):
    return (1 if x%2==0 else -1) if x//2==y//2 and x!=y else 0

@lru_cache(maxsize=300000)
def scalar_diagram(key,caps):
    n=len(key);assert sorted(x for cap in caps for x in cap)==list(range(n))
    edge_labels=sorted({x for x in key if x>=0})
    edges={label:tuple(i for i,x in enumerate(key) if x==label) for label in edge_labels}
    adjacency=[[] for _ in range(n)]
    for i,j in caps:
        adjacency[i].append(j);adjacency[j].append(i)
    for i,j in edges.values():
        adjacency[i].append(j);adjacency[j].append(i)
    seen=set();assigned={};loops=0
    for vertex in range(n):
        if vertex in seen:continue
        component=set();todo=[vertex]
        while todo:
            x=todo.pop()
            if x in component:continue
            component.add(x);todo.extend(adjacency[x])
        seen|=component
        omega={key[i] for i in component if key[i]>=0}
        constants=[-key[i]-1 for i in component if key[i]<0]
        if not omega:continue
        if not constants:loops+=1;handle=1
        else:
            assert len(constants)==2
            if any(x//2==0 for x in constants):return 0,0
            if constants[0]//2!=constants[1]//2:return 0,0
            handle=constants[0]//2
        for label in omega:assigned[label]=handle
    coefficient=0
    for bits in product((0,1),repeat=len(edge_labels)):
        values=[-x-1 if x<0 else None for x in key];sign=1
        for label,bit in zip(edge_labels,bits):
            i,j=edges[label];h=assigned[label]
            values[i]=2*h+bit;values[j]=2*h+1-bit
            if bit:sign=-sign
        for i,j in caps:
            sign*=pair(values[i],values[j])
            if not sign:break
        coefficient+=sign
    return coefficient,loops

def canonical_caps(caps):
    sign=1;out=[]
    for i,j in caps:
        if i>j:i,j=j,i;sign=-sign
        out.append((i,j))
    return tuple(sorted(out)),sign

def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))

def bracket_plans():
    # T_delta is minus the alternating tensor for our delta convention.
    for perm in permutations(range(3)):
        E=tuple(8+i for i in perm);wedge_sign=-parity(perm)
        for j in (1,2):
            output=(E[0],)+tuple(x for k in (1,2) for x in (tuple(range(1,8)) if k==j else (E[k],)))
            yield output,(0,E[j]),wedge_sign
        for j in range(1,8):
            output=(0,)+tuple(x for k in range(1,8) for x in (E[1:] if k==j else (k,)))
            yield output,(E[0],j),-wedge_sign

rterms=[(-2,((0,1),(2,4),(3,6),(5,7))),
        (2,((0,1),(2,5),(3,6),(4,7))),
        (2,((0,1),(2,5),(3,7),(4,6))),
        (2,((0,1),(2,6),(3,5),(4,7))),
        (1,((0,2),(1,5),(3,6),(4,7)))]

def plans_R():
    plans={}
    for output,glue,sign in bracket_plans():
        for coefficient,pairs in rterms:
            caps,orientation=canonical_caps((glue,)+tuple((output[i],output[j]) for i,j in pairs)+((output[8],11),))
            plans[caps]=plans.get(caps,0)+sign*coefficient*orientation
    return {caps:c for caps,c in plans.items() if c}

def plans_ES(chord):
    plans={}
    for output,glue,sign in bracket_plans():
        tail=output[2:]
        for rotation in range(7):
            word=tail[rotation:]+tail[:rotation]
            caps,orientation=canonical_caps((glue,(output[0],output[1]))+
               tuple((word[i],word[j]) for i,j in chord)+((word[6],11),))
            plans[caps]=plans.get(caps,0)+sign*orientation
    return {caps:c for caps,c in plans.items() if c}

def evaluate(poly,constants,plans):
    coefficients=[0]*5
    for key,c in poly.items():
        extended=key+constants
        for caps,d in plans.items():
            value,loops=scalar_diagram(extended,caps)
            coefficients[loops]+=c*d*value
    return sum(c*s**i for i,c in enumerate(coefficients))


assert len(inputs)==12
assert [sum(label[0]=='positive' and label[1]==m for label in labels) for m in range(1,5)]==[3,3,1,0]
chords=list(pairings(tuple(range(8))))
detector=[chords[i] for i in (0,1,2,7,13)]
K=sp.Matrix([[evaluate(T,(),{chord:1}) for T in inputs] for chord in detector])
pure=[i for i,label in enumerate(labels) if label[0]=='pure']
pure_det=sp.factor(K[:,pure].det())
expected_pure_det=3538944*s**5*(s-2)*(s-1)**4*(s+1)**3*(2*s-1)*(2*s+1)**5*(2*s+3)
assert sp.expand(pure_det-expected_pure_det)==0
print('PURE_RAW_DETECTOR_DETERMINANT',pure_det,flush=True)
print('SOURCE_FROM_RAW_SIGNS',[1,-1,1,-1,-1],flush=True)
J=sp.Matrix([[-104,-288],[-26,-72],[104,288],[32,192],[-32,-192]])
L=sp.Matrix([[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]])
assert L*J==sp.zeros(3,2) and L.rank()==3 and J.rank()==2
LK=L*K
R=plans_R()
tests=[('abx',(-1,-2,-3,-4)),('axy',(-1,-3,-4,-2)),('xyu',(-3,-4,-5,-6))]
rows=[];names=[]
for name,constants in tests:
    rows.append([sp.factor(evaluate(T,constants,R)) for T in inputs])
    names.append('R_'+name)
chords6=list(pairings(tuple(range(6))))
selected=[('abx',(-1,-2,-3,-4),1),('abx',(-1,-2,-3,-4),2),
          ('axy',(-1,-3,-4,-2),1),('xyu',(-3,-4,-5,-6),1)]
for name,constants,index in selected:
    plans=plans_ES(chords6[index])
    rows.append([sp.factor(evaluate(T,constants,plans)) for T in inputs])
    names.append('ES1_'+name+'_'+str(index))
M=sp.Matrix(rows)
assert M.shape==(7,12) and K.shape==(5,12)
print('INPUT_LABELS',labels,flush=True)
print('FIVE_RAW_DETECTOR_MATRIX',K.tolist(),flush=True)
print('SELECTED_ROW_NAMES',names,flush=True)
print('SELECTED_SCALAR_MATRIX',M.tolist(),flush=True)

d0=9*(2*s+3)*(4*s**2+6*s-1)
N0=sp.Matrix([[-2*s*(2*s + 3)*(128*s**4 + 528*s**3 + 776*s**2 + 465*s + 101), -4*s*(2*s + 3)*(16*s**4 - 48*s**3 - 305*s**2 - 402*s - 152), 2*s*(s - 1)*(2*s + 3)*(128*s**3 + 464*s**2 + 550*s + 199), -3*s*(576*s**4 + 2720*s**3 + 4684*s**2 + 3546*s + 1029), -6*s*(s + 2)*(4*s + 3)*(4*s + 5)*(8*s + 7), 3*s*(2*s + 1)*(2*s + 3)*(80*s**2 + 240*s + 187), 24*s*(s - 1)*(2*s + 3)*(4*s**2 + 6*s - 1)], [2*s*(2*s + 1)**2*(2*s + 3)*(8*s**2 + 25*s + 20), 2*s*(2*s + 1)*(2*s + 3)*(4*s**3 - 14*s**2 - 70*s - 61), -4*s*(s - 1)*(2*s + 1)*(2*s + 3)*(8*s**2 + 25*s + 20), 3*s*(2*s + 3)*(72*s**3 + 232*s**2 + 224*s + 69), 6*s*(s + 2)*(2*s + 1)*(2*s + 3)*(8*s + 7), -3*s*(2*s + 3)*(40*s**3 + 140*s**2 + 146*s + 37), -6*s*(s - 1)*(2*s + 3)*(4*s**2 + 6*s - 1)], [-6*s*(2*s + 3)*(16*s**3 + 66*s**2 + 80*s + 27), -6*s*(2*s + 3)*(4*s**3 - 12*s**2 - 82*s - 81), 6*s*(s - 1)*(2*s + 3)*(16*s**2 + 60*s + 53), -18*s*(s + 2)*(36*s**2 + 102*s + 67), -36*s*(s + 2)**2*(8*s + 7), 18*s*(s + 2)*(2*s + 3)*(10*s + 13), 0]])

assert N0.shape==(3,7)
defect=(N0*M-d0*LK).applyfunc(sp.expand)
assert defect==sp.zeros(3,12)
print('CERTIFICATE_DENOMINATOR',sp.factor(d0),flush=True)
print('CERTIFICATE_NUMERATOR',N0.tolist(),flush=True)
print('EXACT_POLYNOMIAL_DEFECT',defect.tolist(),flush=True)
t=sp.Symbol('t')
assert sp.expand(d0.subs(s,t+3)-9*(9+2*t)*(53+30*t+4*t*t))==0
assert all(c>0 for c in sp.Poly(d0.subs(s,t+3),t).all_coeffs())
assert all(c>0 for c in sp.Poly(expected_pure_det.subs(s,t+3),t).all_coeffs())
print('DENOMINATORS_NONZERO_FOR_ALL_INTEGER_s_GE_3: positive coefficients after s=3+t.',flush=True)
print('EXACT_UNIVERSAL_KERNEL_INCLUSION_PASSED: ker M(s) is contained in ker L K(s) for every integer s>=3.',flush=True)
print('SCOPE: finite algebraic certificate; actual source and arithmetic morphisms are proved in F.3.30--32.',flush=True)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'),flush=True)
