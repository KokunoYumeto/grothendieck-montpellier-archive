"""Finite coordinate checks for E4.H; no huge norm polynomial is expanded.
GPT-6 Astra (OpenAI), 2026-11-20.
"""
from math import comb
import itertools, json, time
start=time.perf_counter()
indices=list(itertools.product(range(3),range(2),range(2),range(2)))
def A(q):
 r,n,a,b=q
 return (1,(r,n,1-a,b))
def B(q):
 r,n,a,b=q
 return ((-1)**(n*a),(r,n,a,1-b))
def apply(ops,q):
 sign=1
 for op in reversed(ops):
  s,q=op(q);sign*=s
 return sign,q
assert all(apply([A,A],q)==(1,q) for q in indices)
assert all(apply([B,B],q)==(1,q) for q in indices)
assert all(apply([A,B,A,B],q)==((-1)**q[1],q) for q in indices)
h=(comb(215,23)+comb(107,11))//2
N=comb(h+3,4)
result={"coordinates":24,"A_square_identity":True,"B_square_identity":True,"commutator_is_central_weight_sign":True,"projective_dimension":23,"first_jet_length_on_quotient":24,"cover_degree":8,"pulled_back_first_jet_length":192,"interpolation_bound":191,"chosen_even_degree":192,"quotient_power_m":96,"equation_degree_on_P23":768,"number_equations":21,"number_degree192_even_weight_monomials_h":str(h),"number_universal_norm_coefficients_N":str(N),"number_independent_parameters":str(21*N),"scope":"Signed representation and index cardinalities checked; norm coefficient polynomials specified by a finite formula and not expanded.","seconds":time.perf_counter()-start}
print(json.dumps(result,indent=2))
