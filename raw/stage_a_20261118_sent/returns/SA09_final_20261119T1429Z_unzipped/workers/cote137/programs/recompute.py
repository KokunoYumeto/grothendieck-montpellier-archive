"""Small exact arithmetic checks for cote 137; no verdict is inferred here.
General arguments and checked hypotheses are in proof_audit.md.
"""
from math import comb, factorial, gcd
from fractions import Fraction as Q
import json

def choose(n,r):
    if n >= 0: return comb(n,r) if r <= n else 0
    a=1
    for j in range(r): a=Q(a*(n-j),j+1)
    return int(a)

out={}
mu={1:2,3:1};nu={0:1,2:3}
out['DK_rank']=[{'n':n,'disk_sphere':sum(v*choose(n+1,i) for i,v in mu.items())+sum(v*choose(n,j) for j,v in nu.items()),'normalized':sum(choose(n,j)*(mu.get(j,0)+mu.get(j+1,0)+nu.get(j,0)) for j in range(n+1))} for n in range(8)]
assert all(r['disk_sphere']==r['normalized'] for r in out['DK_rank'])
out['Euler_at_minus_one']={'rank_polynomial_at_minus_one':sum(v*choose(0,i) for i,v in mu.items())+sum(v*choose(-1,j) for j,v in nu.items()),'Euler_homology':sum((-1)**j*v for j,v in nu.items())}
out['leading_term_degree3']={'mu3':1,'nu3':0,'actual_coefficient':str(Q(1,factorial(3))),'unscaled_claim':1}
out['missing_mu_i_rank_formula']={'object':'D_1(Z), differential identity','normalized_ranks':{0:1,1:1},'formula_without_mu_i_at_i1':0,'correct_formula_at_i1':1}
out['infinite_contractible_rank']=[{'n':n,'sum_binomial':sum(choose(n,j) for j in range(n+1)),'two_power':2**n} for n in range(11)]
out['nonuniform_fiber_ranks']=[{'prime':p,'nonzero_normalized_degree':i,'ranks_n0_to8':[choose(n,i) for n in range(9)]} for i,p in enumerate([2,3,5,7,11],1)]

# Integral chain maps D_i(n)->D_i(m): bottom = m/g, top = n/g.
out['disk_Hom_same_degree']=[]
for n,m in [(1,1),(2,3),(2,4),(6,10)]:
    g=gcd(n,m);bottom=m//g;top=n//g
    assert m*top==n*bottom
    out['disk_Hom_same_degree'].append({'source_d':n,'target_d':m,'bottom_basis':bottom,'top_basis':top,'obstruction_m_top_minus_n_bottom':m*top-n*bottom})
def rational_rank(matrix):
    a=[[Q(v) for v in row] for row in matrix]
    if not a:return 0
    r=0
    for c in range(len(a[0])):
        piv=next((u for u in range(r,len(a)) if a[u][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
        for u in range(len(a)):
            if u!=r:
                q=a[u][c];a[u]=[x-q*y for x,y in zip(a[u],a[r])]
        r+=1
    return r
out['disk_Hom_degree_table']=[]
for i in range(1,4):
 for j in range(1,5):
    unknowns=sorted({i,i-1}&{j,j-1});equations=[]
    for d in range(0,max(i,j)+2):
        if d not in {i,i-1} or d-1 not in {j,j-1}:continue
        equations.append([(3 if (d==j and v==d) else 0)-(2 if (d==i and v==d-1) else 0) for v in unknowns])
    out['disk_Hom_degree_table'].append({'i':i,'j':j,'chain_equation_matrix':equations,'rank':len(unknowns)-rational_rank(equations)})
out['torsion_counts_not_invariants']=[{'differential':n,'free_H_rank':0,'torsion_factor_count':1,'H_cyclic_order':n,'simplicial_ranks_n0_to4':[choose(t+1,1) for t in range(5)]} for n in (2,3)]

# Gamma^2 K(Z,1): in degree 2, use gamma2(a), ab, gamma2(b).
# Degeneracies span the first and last terms; d1(ab)=2 gamma2(e).
pd_basis=[(2,0),(1,1),(0,2)]
faces=[[int(a==0),factorial(2)//(factorial(a)*factorial(b)),int(b==0)] for a,b in pd_basis]
d2=[v[0]-v[1]+v[2] for v in faces];torsion=abs(d2[1])
assert d2[0]==d2[2]==0 and torsion==2
out['Gamma2_KZ1']={'degree2_basis':['gamma2(a)','a*b','gamma2(b)'],'face_coefficients_by_basis':faces,'alternating_d2':d2,'degenerate_basis_indices':[0,2],'normalized_d2_matrix':[[d2[1]]],'normalized_d1_matrix':[[0]],'Smith_d2':[[torsion]],'H1':f'Z/{torsion}','H2':'0','N_higher':'0: every weight-2 monomial uses at most two bar coordinates'}

out['AW_interval']={'f_vertex0':0,'f_vertex1':1,'edge_cochain':1,'f_cup_e_edge':0*1,'e_cup_f_edge':1*1,'strict_commutativity':False}
out['truncation_disk']={'cochain':'Z in n --id--> Z in n+1','original_Hn':0,'brutal_Hn':1,'good_Hn':0}
out['Fp_scalar_weights']=[{'p':p,'all_lambda_lambda_p_equal':all((a**p-a)%p==0 for a in range(p)),'laws_differ_over_Fp_T':'T^p-T is a nonzero polynomial'} for p in (2,3,5,7)]
out['PD_iteration']=[{'p':p,'q':q,'coefficient':factorial(p*q)//(factorial(p)*factorial(q)**p)} for p,q in [(2,2),(2,3),(3,2),(3,3)]]
out['IntZ_leading_product']=[{'m':m,'n':n,'coefficient':comb(m+n,m),'from_leading_coefficients':str(Q(factorial(m+n),factorial(m)*factorial(n)))} for m,n in [(1,1),(2,3),(3,3)]]
out['constant_substitution']={'b(t)':'t(t-1)/2','c(t)':'t(t-1)/2+t','same_top_symbol':True,'b(1)':0,'c(1)':1}
def b2(t):return Q(t*(t-1),2)
cocycle=[{'a':a,'b':b,'coboundary':str(b2(a+b)-b2(a)-b2(b)),'a_times_b':a*b} for a,b in [(-2,3),(-1,-1),(0,7),(1,1),(2,3),(5,7)]]
assert all(Q(x['coboundary'])==x['a_times_b'] for x in cocycle)
out['PS119_quadratic_splitting']={'sample_identity':cocycle,'generic_P':'A*t^2+B*t+C','constant_equation':'C=0','ab_coefficient_equation':'2*A=1','forced_quadratic_coefficient':str(Q(1,2)),'integral_polynomial_solution':False,'degree_argument':'highest-degree coboundary forces degree<=2 over Q; additive remainder is linear'}
out['binomial_counterexamples']={'Burnside_C2':{'relation':'t^2=2t','binom_t_2':'t/2','integral_in_basis_1_t':False},'free_PD_Zx':{'x_square':'2 gamma2(x)','binom_x_2':'gamma2(x)-x/2','integral_in_gamma_basis':False},'unit_PD_on_Z':{'required':'2 gamma2(1)=1','integral_solution':False}}
out['false_density']={'field':'Q','function':'h(x,y)=x if y=0, else 0','homogeneous':True,'h_1_0':1,'h_0_1':0,'h_1_1':0,'additive':False}
out['same_index_pairing']={'object':'C^(n+1)','Hom_Cn_to_object':'Z','Hom_object_to_Cn':'0','perfect':False,'corrected_target':'C^(n+1) in second Hom; composition lands in Z d_n'}
print(json.dumps(out,indent=2,ensure_ascii=False))
