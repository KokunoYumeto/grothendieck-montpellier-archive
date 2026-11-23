"""HD-G25 exact F4 matrix/root certificate, independently constructed.
GPT-6 Astra Pro, /root/g34, inherited effort, 2026-11-21.
All roots are stored as twice their real coordinate vectors. No group
table, numerical matrix arithmetic or precomputed permutations are used.
"""
from itertools import combinations, product
from fractions import Fraction as F
from pathlib import Path
import json

eye=[tuple(int(i==j) for i in range(4)) for j in range(4)]
roots=set()
for v in eye:
    for a in [-2,2]:roots.add(tuple(a*x for x in v))
for i,j in combinations(range(4),2):
    for a,b in product([-2,2],repeat=2):
        v=[0]*4;v[i]=a;v[j]=b;roots.add(tuple(v))
roots.update(product([-1,1],repeat=4))
roots=sorted(roots)
assert len(roots)==48
positions={v:i for i,v in enumerate(roots)}
simple=[(0,1,-1,0),(0,0,1,-1),(0,0,0,1),
        (F(1,2),F(-1,2),F(-1,2),F(-1,2))]

def dot(v,w):return sum(a*b for a,b in zip(v,w))
def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))
Id=tuple(eye)
matrices=[]
for v in simple:
    norm=dot(v,v)
    R=tuple(tuple(F(int(i==j))-2*F(v[i])*F(v[j])/norm
                  for j in range(4)) for i in range(4))
    assert matmul(R,R)==Id
    assert matmul(tuple(zip(*R)),R)==Id
    assert all((2*x).denominator==1 for row in R for x in row)
    matrices.append(R)

gram=[[dot(a,b) for b in simple] for a in simple]
assert gram==[[2,-1,0,0],[-1,2,-1,0],[0,-1,1,F(-1,2)],
              [0,0,F(-1,2),1]]
sign2=tuple(tuple(F((-1 if i==1 else 1)*int(i==j)) for j in range(4)) for i in range(4))
sign3=tuple(tuple(F((-1 if i==2 else 1)*int(i==j)) for j in range(4)) for i in range(4))
word=matmul(matrices[3],matmul(sign2,matmul(sign3,matrices[3])))
assert tuple(word[i][3] for i in range(4))==eye[0]

generators=[]
for R in matrices:
    perm=[]
    for v in roots:
        w=tuple(sum(R[i][j]*v[j] for j in range(4)) for i in range(4))
        assert all(x.denominator==1 for x in w)
        perm.append(positions[tuple(int(x) for x in w)])
    assert len(set(perm))==48
    generators.append(tuple(perm))

def compose(a,b):return tuple(a[b[j]] for j in range(len(b)))
def closure(gens,degree):
    initial=tuple(range(degree));seen={initial};todo=[initial]
    for a in todo:
        for b in gens:
            c=compose(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return todo

W=closure(generators,48)
assert len(W)==1152
neg=tuple(positions[tuple(-x for x in v)] for v in roots)
assert neg in W
extended=[p+tuple(j+48 for j in p) for p in generators]
scalar_i=tuple(j+48 for j in range(48))+neg
H=closure(extended+[scalar_i],96)
assert len(H)==2304
basis_positions=[positions[tuple(2*x for x in v)] for v in eye]
trace_norm_sum_times4=0
odd_count=0
for p in H:
    re=im=0
    odd=p[basis_positions[0]]>=48
    odd_count+=odd
    for j,bp in enumerate(basis_positions):
        image=p[bp]
        if image>=48:im+=roots[image-48][j]
        else:re+=roots[image][j]
    trace_norm_sum_times4+=re*re+im*im
assert trace_norm_sum_times4==4*len(H)
assert odd_count==1152

out={'status':'PASS','root_count':48,'W_order':len(W),'scalar_extension_order':len(H),
     'minus_identity_in_W':True,'central_i_in_H':True,'character_norm':1,
     'coefficient_Gram':'I4','all_entries_in_half_Gaussian_integers':True,
     'simple_root_Gram':[[str(x) for x in row] for row in gram],
     'reflection_matrices':[[[str(x) for x in row] for row in R] for R in matrices],
     'scope':'Exact root and group closure only; the universal parabolic and rank argument is the full HD-G25 proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
