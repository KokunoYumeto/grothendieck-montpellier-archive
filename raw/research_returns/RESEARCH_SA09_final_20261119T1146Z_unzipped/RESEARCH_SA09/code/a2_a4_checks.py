#!/usr/bin/env python3
"""Finite certificates and scope-limited checks for A.2 and A.4.

The proofs in sections/A2_A4.tex establish the infinite assertions.
This program exhausts the finite counterexample data, and checks the
binomial formulas on the indicated finite ranges; it does not claim that
finite sampling proves an assertion for every degree.
"""
from itertools import product
from math import comb
from time import perf_counter
import json

t0 = perf_counter()
out = {}

# A2.1: all chain retractions D_0 -> F_2[0].  The degree-one component
# is necessarily zero, and the degree-zero component is a scalar a.
# The chain-map condition is a*id = 0.  A retraction would require a=1.
chain_maps = [a for a in range(2) if a == 0]
retractions = [a for a in chain_maps if a == 1]
assert chain_maps == [0] and retractions == []
out["A2.1"] = {"base_ring":"F_2", "candidate_scalars":2,
               "chain_maps_D0_to_S0":chain_maps, "retractions":retractions}

# A2.3: the category B consists of finite free Z/4-modules.  The
# representable-kernel condition evaluated at its rank-one generator
# would require a group with exactly two elements.  A free object has
# cardinality 4**r; only r=0 can have fewer than four elements.
kernel2 = [x for x in range(4) if (2*x) % 4 == 0]
assert kernel2 == [0, 2]
out["A2.3"] = {"base_ring":"Z", "target_scalar_ring":"Z/4",
               "elements_exhausted":4,"kernel_of_2":kernel2,
               "kernel_cardinality":len(kernel2),
               "free_rank_zero_cardinality":1,
               "free_positive_rank_min_cardinality":4}

# A2.5: Grothendieck's two printed closure axioms are weaker than
# Quillen exactness.  Pull back Z/16 -> Z/4 along multiplication by 2.
pullback=[(x,y) for x in range(16) for y in range(4) if x%4==(2*y)%4]
assert len(pullback)==16
def order_pair(p):
    for n in range(1,17):
        if (n*p[0])%16==0 and (n*p[1])%4==0:
            return n
    raise AssertionError
orders={n:sum(order_pair(p)==n for p in pullback) for n in [1,2,4,8,16]}
projection_kernel=[p for p in pullback if p[1]==0]
assert len(projection_kernel)==4 and len({p[1] for p in pullback})==4
assert max(order_pair(p) for p in pullback)==8
# The basic extension has cyclic middle of order16, a split extension
# with the same ends has exponent4.  The pullback has exponent8.
out["A2.5"]={"candidate_pairs":64,"pullback_pairs":pullback,
               "order_distribution":orders,"kernel":projection_kernel,
               "quotient_cardinality":4,"middle_exponent":8,
               "basic_extension_middle_exponent":16,
               "split_extension_middle_exponent":4}

# A4.5: F_2[e]/(e^2), elements a+b*e encoded by a+2*b.
def add(x, y):
    return x ^ y
def mul(x, y):
    a,b,c,d = x&1, x>>1, y&1, y>>1
    return (a*c) | (2*((a*d+b*c)&1))
table = [[mul(x,y) for y in range(4)] for x in range(4)]
epsilon_image = sorted({mul(2,x) for x in range(4)})
epsilon_kernel = [x for x in range(4) if mul(2,x)==0]
ring_axioms = all(mul(mul(x,y),z)==mul(x,mul(y,z)) and
                  mul(x,add(y,z))==add(mul(x,y),mul(x,z))
                  for x,y,z in product(range(4), repeat=3))
assert ring_axioms and epsilon_image == epsilon_kernel == [0,2]
assert mul(2,2) == 0 and all(mul(1,x)==x for x in range(4))
out["A4.5"] = {"ring":"F_2[e]/(e^2)","ring_axiom_triples":64,
               "multiplication_table":table,"image_times_e":epsilon_image,
               "kernel_times_e":epsilon_kernel,
               "tensor_with_F2_differential":0,
               "conclusion":"The periodic free resolution has Tor_i=F_2 for every i>=0; the assertion for every i follows from the proved repeating map."}

# A4.4: the normalization of the locally finite sum of all disks D_i
# has rank 1 in degree zero and rank 2 thereafter.
rows=[]
for n in range(17):
    via_normalization = sum(comb(n,i)*(1 if i==0 else 2) for i in range(n+1))
    via_disks = sum(comb(n+1,j) for j in range(1,n+2))
    assert via_normalization == via_disks == 2**(n+1)-1
    rows.append([n,via_normalization])
out["A4.4"]={"checked_degrees":[0,16],"rank_values":rows,
              "scope":"finite verification of closed formulas; general proof uses binomial theorem"}

# A4.6: one disk D_j has a copy of the base ring in degrees j and j+1.
disk_checks=[]
for j in range(8):
    for i in range(10):
        # Manuscript mu_{j+1}=1; mu_i+mu_{i+1}.
        corrected=int(i==j+1)+int(i+1==j+1)
        actual=int(i==j)+int(i==j+1)
        assert corrected==actual
    disk_checks.append(j)
out["A4.6"]={"disk_bottom_degrees":disk_checks,"tested_chain_degrees":[0,9],
             "corrected_formula":"rank N_i=mu_i+mu_{i+1}+beta_i+beta_{i+1}+nu_i"}
out["runtime_seconds"] = perf_counter()-t0
print(json.dumps(out,indent=2))
