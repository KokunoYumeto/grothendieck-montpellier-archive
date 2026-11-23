"""HD-N23: an actual positive graph union on the Gaussian CM sixfold.

GPT-6 Astra Pro /root/imprimitive, 21 November 2026; inherited effort.
Fresh integer exterior and Gaussian determinant implementations.
No earlier certificate, group table or saved output is imported.
The local Ext result is proved in the accompanying text; only its
displayed Koszul maps and numerical consequences are checked here.
"""
from itertools import combinations, permutations, product
from pathlib import Path
from math import comb
from fractions import Fraction
import json
import sympy as sp


def add(a, b, scalar=1):
    out = dict(a)
    for mask, coeff in b.items():
        out[mask] = out.get(mask, 0) + scalar*coeff
        if out[mask] == 0:
            del out[mask]
    return out


def wedge(a, b):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            if x & y:
                continue
            inversions = sum((y & ((1 << j)-1)).bit_count()
                             for j in range(12) if x & (1 << j))
            z = x | y
            out[z] = out.get(z, 0) + (-1)**inversions*cx*cy
    return {m:c for m,c in out.items() if c}


def exterior_product(items):
    out = {0:1}
    for item in items:
        out = wedge(out, item)
    return out


def one(index, coefficient=1):
    return {1 << index:coefficient}


def gaussian_mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def gaussian_wedge(a, b):
    out = {}
    for x,cx in a.items():
        for y,cy in b.items():
            if x & y:
                continue
            sign = (-1)**sum((y & ((1 << j)-1)).bit_count()
                              for j in range(12) if x & (1 << j))
            c = gaussian_mul(cx,cy)
            old = out.get(x|y,(0,0))
            out[x|y] = (old[0]+sign*c[0],old[1]+sign*c[1])
    return {m:c for m,c in out.items() if c != (0,0)}


permutation_terms = []
for p in permutations(range(6)):
    sign = (-1)**sum(p[i] > p[j] for i in range(6) for j in range(i+1,6))
    permutation_terms.append((p,sign))


def gaussian_determinant(matrix):
    out = [0,0]
    for p,sign in permutation_terms:
        value = (sign,0)
        for i,j in enumerate(p):
            if matrix[i][j] == (0,0):
                value = (0,0)
                break
            value = gaussian_mul(value,matrix[i][j])
        out[0] += value[0];out[1] += value[1]
    return tuple(out)


# Physical elliptic order X1,Y1,X2,Y2,X3,Y3; two real forms each.
point_classes = [wedge(one(2*j),one(2*j+1)) for j in range(6)]
weights = [1,1,1,1,7,1]
theta = {}
for w,c in zip(weights,point_classes):
    theta = add(theta,c,w)
theta3 = exterior_product([theta]*3)
theta6 = exterior_product([theta]*6)
top = (1 << 12)-1
assert theta6 == {top:5040}

# Integral pure Weil volume T=-Im prod((x+i y)(u-i v)).
Kvolume = {0:(1,0)}
for j in range(3):
    z = {1 << (4*j):(1,0),1 << (4*j+1):(0,1)}
    barw = {1 << (4*j+2):(1,0),1 << (4*j+3):(0,-1)}
    Kvolume = gaussian_wedge(Kvolume,gaussian_wedge(z,barw))
T = {m:-c[1] for m,c in Kvolume.items() if c[1]}
assert T and all(abs(c)==1 for c in T.values())
assert not wedge(theta,T)
assert wedge(T,T) == {top:-32}

phase = [(1,0),(0,1),(-1,0),(0,-1)]
directions = []
graph_sum = {}
for amplitude,multiplicity in [(1,3),(3,9)]:
    for a,b in product(range(4),repeat=2):
        phases = [phase[a],phase[b],phase[(-a-b)%4]]
        slopes = [phases[0],phases[1],tuple(amplitude*z for z in phases[2])]
        factors=[];normal=[]
        for j,(real,imag) in enumerate(slopes):
            re = add(add(one(4*j+2),one(4*j),-real),one(4*j+1),imag)
            im = add(add(one(4*j+3),one(4*j),-imag),one(4*j+1),-real)
            factors.append(wedge(re,im))
            row=[(0,0)]*6
            row[2*j]=(-real,-imag);row[2*j+1]=(1,0)
            normal.append(row)
        cls=exterior_product(factors)
        graph_sum=add(graph_sum,cls,multiplicity)
        directions.append({'kind':'graph','amplitude':amplitude,
                           'phase_exponents':[a,b,(-a-b)%4],
                           'multiplicity':multiplicity,'normal':normal,'class':cls})

pair_classes=[add(point_classes[2*j+1],point_classes[2*j],weights[2*j])
              for j in range(3)]
pair_product=exterior_product(pair_classes)
assert graph_sum == add({m:192*c for m,c in pair_product.items()},T,120)

# The twelve missing coordinate-plane normal sets have one full pair.
coordinate_count=0
for normals in combinations(range(6),3):
    if all(sum(k//2==j for k in normals)==1 for j in range(3)):
        continue
    multiplier=192
    for k in normals:
        multiplier*=weights[k]
    normal=[]
    for k in normals:
        row=[(0,0)]*6;row[k]=(1,0);normal.append(row)
    cls=exterior_product(point_classes[k] for k in normals)
    directions.append({'kind':'coordinate','normal_indices':list(normals),
                       'multiplicity':multiplier,'normal':normal,'class':cls})
    coordinate_count+=multiplier

cycle={}
for d in directions:
    cycle=add(cycle,d['class'],d['multiplicity'])
assert cycle == add({m:32*c for m,c in theta3.items()},T,120)
assert len(directions)==44
N=sum(d['multiplicity'] for d in directions)
assert N==9408 and coordinate_count==9216

# Independently obtain every pair-intersection degree from the actual
# six-by-six Gaussian quotient matrix, and compare with exterior Gysin.
q=0;proper_direction_pairs=0
for i,left in enumerate(directions):
    assert not wedge(left['class'],left['class'])
    for right in directions[i+1:]:
        det=gaussian_determinant(left['normal']+right['normal'])
        degree=det[0]**2+det[1]**2
        expected=wedge(left['class'],right['class'])
        assert expected == ({top:degree} if degree else {})
        q+=left['multiplicity']*right['multiplicity']*degree
        proper_direction_pairs+=int(degree!=0)
assert q==2350080
assert wedge(cycle,cycle)=={top:2*q}
assert Fraction(q,5040)==Fraction(3264,7)

# The explicit greedy 101-torsion selection leaves a positive number
# of choices at every step; no random choice is used in this assertion.
ell=101
available_lower=ell**12-(N-1)*ell**10-q*ell**6
assert available_lower>0
coordinate_multiplicities=sorted({d['multiplicity'] for d in directions if d['kind']=='coordinate'})
assert coordinate_multiplicities==[192,1344]
assert all(v%ell for v in coordinate_multiplicities)
assert set.union(*(set(d['normal_indices']) for d in directions if d['kind']=='coordinate'))==set(range(6))

# Actual maximal-ideal Koszul resolution used in the local Ext proof.
x,y,z=sp.symbols('x y z')
d0=sp.Matrix([[x,y,z]])
d1=sp.Matrix([[-y,-z,0],[x,0,-z],[0,x,y]])
d2=sp.Matrix([[z],[-y],[x]])
assert d0*d1==sp.zeros(1,3)
assert d1*d2==sp.zeros(3,1)

ext2_lower=9*q-9*N-20
trace_target=sum(comb(6,p)*comb(6,p+2) for p in range(5))
assert ext2_lower==21066028 and trace_target==495
kernel_lower=ext2_lower-trace_target
assert kernel_lower==21065533

first=next(d for d in directions if d['kind']=='graph' and
           d['amplitude']==1 and d['phase_exponents']==[0,0,0])
second=next(d for d in directions if d['kind']=='graph' and
            d['amplitude']==1 and d['phase_exponents']==[1,1,2])
det=gaussian_determinant(first['normal']+second['normal'])
intersection=det[0]**2+det[1]**2
assert intersection==16 and first['multiplicity']==second['multiplicity']==3
group_bound=intersection*first['multiplicity']*second['multiplicity']
assert group_bound==144 and q//group_bound==16320
uniform_kernel=9*(q//group_bound-N)-20-trace_target
assert uniform_kernel==61693

out={
 'statement':'HD-N23','status':'PASS',
 'polarization_weights':weights,'ordinary_hermitian_determinant':-7,
 'theta_top_degree':5040,'integral_Weil_square':-32,
 'cycle_character':{'theta_cubed':32,'integral_Weil_T':120},
 'graph_directions':32,'coordinate_directions':12,'total_components':N,
 'coordinate_components':coordinate_count,
 'coordinate_direction_multiplicities':coordinate_multiplicities,
 'proper_direction_pairs':proper_direction_pairs,
 'actual_quotient_determinant_checks':comb(len(directions),2),
 'nodes':q,'ideal_top_theta_coefficient':str(Fraction(q,5040)),
 'End_Euler_characteristic':2*q-wedge(cycle,cycle)[top],
 'torsion_prime':ell,'greedy_available_lower':available_lower,
 'local_Koszul_maps_checked':True,
 'Ext2_lower':ext2_lower,'trace_target_dimension':trace_target,
 'trace_kernel_lower':kernel_lower,
 'two_graph_intersection_order':intersection,
 'uniform_translation_stabilizer_bound':group_bound,
 'uniform_invariant_trace_kernel_lower':uniform_kernel,
 'scope':'Exact cycle/Gysin/actual isogeny-degree, integer and Koszul-composition checks. Local Ext identification, natural gluing, spectral-sequence survival and coherent point-action conclusions are proved separately in the full text.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
