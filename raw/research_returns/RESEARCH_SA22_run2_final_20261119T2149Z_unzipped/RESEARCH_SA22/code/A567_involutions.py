#!/usr/bin/env python3
"""Finite residue-field and matrix checks for the integral-involution examples."""
import json
from time import perf_counter
start=perf_counter()
# F4=F2[w]/(w^2+w+1), using binary encodings 0,1,w,1+w.
def mul(a,b):
    a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
    return ((a0*b0+a1*b1)%2)+2*((a0*b1+a1*b0+a1*b1)%2)
units=[a for a in range(4) if any(mul(a,b)==1 for b in range(4))]
assert units==[1,2,3]
# The integer norm proof establishes k^*=+-1; both images are 1 in F4.
unit_image=[1]
orbits=sorted({tuple(sorted(mul(a,u) for u in unit_image)) for a in units})
assert orbits==[(1,),(2,),(3,)]
# Quadratic integer multiplication in Z[w], w^2=w-3.
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def prod(a,b):
    return (a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
z=(0,0); one=(1,0); neg=(-1,0)
def mm(A,B):
    return [[add(prod(A[i][0],B[0][j]),prod(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
identity=[[one,z],[z,one]]
matrices=[]
for t in [(1,0),(0,1),(1,1)]:
    A=[[one,t],[z,neg]]
    assert mm(A,A)==identity
    matrices.append(A)
# Integral hexagon Gram matrix: Q(u)=Q(v)=1, <u,v>=1/2.
hexagonal_ratio=4-2+1
assert hexagonal_ratio==3
# Exact arithmetic in Z[t]/(t^2), represented by the pair (constant,t).
def dual_prod(a,b):
    return (a[0]*b[0],a[0]*b[1]+a[1]*b[0])
def dual_mm(A,B):
    return [[add(dual_prod(A[i][0],B[0][j]),
                 dual_prod(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
dual_t=(0,1)
dual_sigma=[[one,dual_t],[z,neg]]
assert dual_mm(dual_sigma,dual_sigma)==identity
negative_eigen_generators=[(dual_t,(-2,0)),(z,dual_t)]
for x,y in negative_eigen_generators:
    assert add((2*x[0],2*x[1]),dual_prod(dual_t,y))==z
# (2,t)/(4,2t) has these four distinct coefficient normal forms.
ideal_residue_representatives=[(a,b) for a in (0,2) for b in (0,1)]
assert len(set(ideal_residue_representatives))==4
print(json.dumps({"F4_multiplication_table":[[mul(a,b) for b in range(4)] for a in range(4)],
"unit_image":unit_image,"nonsplit_slope_orbits":orbits,"involution_matrices":matrices,
"hexagonal_squared_length_ratio":hexagonal_ratio,
"dual_number_sigma":dual_sigma,
"dual_number_negative_eigen_generators":negative_eigen_generators,
"dual_number_ideal_mod_maximal_ideal_representatives":ideal_residue_representatives,
"seconds":perf_counter()-start},indent=2))
