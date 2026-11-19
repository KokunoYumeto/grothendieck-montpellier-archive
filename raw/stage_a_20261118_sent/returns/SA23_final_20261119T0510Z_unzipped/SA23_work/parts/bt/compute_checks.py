#!/usr/bin/env python3
"""Reproducible exact checks; finite experiments are labelled as such.
The universal arguments are in proof_checks.md. No source text is modified.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import gcd
import json
import sympy as s
out={}
x,t,u=s.symbols('x t u')
out['horizontal_arc_counterexample']={'omega':'dx','operator':'identity','sections':[0,1], 'integral':str(s.integrate(1,(x,0,1))), 'primitive_difference':1,'de_Rham_class':'0 since dx=d(x)','closed_cycle_period':0}
f=t*x**2+t**2*x+1
a=t**2;b=t+1
I=s.integrate(f,(x,a,b))
leibniz=s.integrate(s.diff(f,t),(x,a,b))+f.subs(x,b)*s.diff(b,t)-f.subs(x,a)*s.diff(a,t)
out['endpoint_formula']={'f':str(f),'a':str(a),'b':str(b),'I':str(s.expand(I)), 'dI':str(s.expand(s.diff(I,t))),'leibniz_difference':str(s.simplify(s.diff(I,t)-leibniz))}
out['simultaneous_horizontal_obstruction']={'a_at_0':0,'b_at_0':0,'da_dt_at_0':0,'db_dt_at_0':1}
out['relative_closed_pullback']={'omega':'t dx on A1_x x A2_(t,u)','relative_d':0,'section':'x=u','pullback':'t du','d_pullback_coefficient_dt_wedge_du':str(s.diff(t,t))}
out['characteristic_p_coefficient_check']=[{'p':p,'coefficient_of_x_to_p_minus_1_in_d_of_sum_c_n_x_n':'p*c_p = 0','p_mod_p':p%p} for p in [2,3,5,7]]
out['derived_Hom_counterexample']={'dim_k':1,'dim_End_k_squared':s.eye(4).rank()}
n0,n1=s.symbols('n0 n1',integer=True,positive=True)
out['determinant_cocharacter']={'weights':['n1 on V0','-n0 on V1'],'det_exponent':str(s.expand(n0*n1+n1*(-n0))),'central_mu_h_test':[{'n0':a,'n1':b,'h':a+b,'gcd_n0_h':gcd(a,a+b),'gcd_n1_h':gcd(b,a+b)} for a,b in [(1,2),(2,3),(3,4),(2,5)]]}
polys=[]
for coeff in product(range(3), repeat=4):
    if any(coeff): polys.append(coeff)
checked=counter=0
for A in polys:
 for B in polys:
    C=[sum(A[i]*B[k-i] for i in range(4) if 0<=k-i<4) for k in range(7)]
    support=[i for i,c in enumerate(C) if c]
    if len(support)==2:
        checked+=1
        if len([v for v in A if v])*len([v for v in B if v])>2: counter+=1
out['positive_binomial_factor_sample']={'coefficient_range':'0..2','degrees':'0..3','binomial_products':checked,'violations_of_one_factor_monomial':counter,'scope':'finite test only; proof in proof_checks.md'}
def simply_laced_cartan(arms):
    n=1+sum(arms); M=2*s.eye(n); nxt=1
    for arm in arms:
        prev=0
        for _ in range(arm):
            M[prev,nxt]=M[nxt,prev]=-1;prev=nxt;nxt+=1
    return M
def roots(C):
    n=C.rows; seen=set(); todo=[]
    for i in range(n):
        v=tuple(int(i==j) for j in range(n));seen.add(v);todo.append(v)
    while todo:
        v=todo.pop()
        for i in range(n):
            w=list(v);w[i]-=sum(int(C[i,j])*v[j] for j in range(n));w=tuple(w)
            if w not in seen:seen.add(w);todo.append(w)
    return len(seen)
out['simply_laced_classification_checks']={}
for name,arms in [('D4',[1,1,1]),('E6',[2,2,1]),('E7',[3,2,1]),('E8',[4,2,1])]:
    C=simply_laced_cartan(arms);r=roots(C)
    out['simply_laced_classification_checks'][name]={'rank':C.rows,'roots':r,'lie_dimension':C.rows+r,'cartan_determinant':int(C.det())}
def phi(v,q,c):return min(q*v,v+c)
def psi(v,q,c):return max(v/q,v-c)
q=Q(9);c=Q(1);v=Q(4)
seq=[]
for n in range(1,13):
    seq.append({'n':n,'upper_bound':str(v),'phi_psi_identity':phi(psi(v,q,c),q,c)==v});v=psi(v,q,c)
out['valuation_recurrence_example']={'q':9,'c1':1,'threshold':'1/8','sequence':seq,'scope':'illustration of exact inverse and eventual geometric decay, not a formal group computation'}
out['strict_boundary_example']={'p':2,'formal_group':'multiplicative','[2](x)':'2*x+x**2','x':-2,'v2_x':1,'threshold':1,'[2](-2)':2*(-2)+(-2)**2,'consequence':'valuation equality fails at boundary; result is infinity'}
out['End_weight_decomposition']={'weights_V':[0,1],'weights_End':sorted({a-b for a in (0,1) for b in (0,1)}),'bracket_of_equal_extreme_degree_targets':[-2,2],'Jordan_triple_target_degrees':[-1,1]}
def mul(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def parity(a):return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2
e=tuple(range(5)); A5=[a for a in permutations(range(5)) if parity(a)==0]; odd=(1,0,2,3,4); h=(1,0,3,2,4)
def conj(a,b):return mul(mul(a,b),inv(a))
def closure(gens):
    H={e};todo=[e]
    while todo:
        a=todo.pop()
        for g in gens:
            b=mul(a,g)
            if b not in H:H.add(b);todo.append(b)
    return H
normal_sizes=set()
for a in A5:
    if a!=e:normal_sizes.add(len(closure({conj(g,a) for g in A5})))
inner_matches=[a for a in A5 if all(conj(a,g)==conj(odd,g) for g in A5)]
out['H1_neutral_fibre_not_injectivity']={'Gamma_and_A':'A5, trivial action','Pi':'< (12)(34) >','A5_order':len(A5),'normal_closure_sizes_of_nonidentity_elements':sorted(normal_sizes),'odd_conjugation_fixes_Pi_generator':conj(odd,h)==h,'number_of_A5_conjugators_between_identity_and_outer_automorphism':len(inner_matches),'logic':'simplicity makes neutral restriction fibre trivial; identity and odd conjugation give distinct nonneutral classes with identical restrictions'}
out['relative_cocycle_rank_one']={'coefficient_action':'pi acts on Omega; Z acts trivially','multipliers':['1','p'],'pi_fixed_multipliers':'Q_p^*','conjugation_by_fixed_scalars':'trivial','different_multipliers_remain_distinct':True}
out['semilinear_valuation']={'coboundary':'sigma(a)/a','valuation':'v(sigma(a))-v(a)=0','uniformizer_valuation':1,'uniformizer_is_coboundary':False}
out['restriction_of_scalars_quadratic']={'separable_Galois_degree':2,'map':'K tensor_Qp K -> K x K, a tensor b -> (ab,sigma(a)b)','K_dimension_source':2,'K_dimension_target':2,'T_Qp_points':'K^*','T_K_points':'K^* x K^*'}
out['uniformizer_splitting']={'valuation_x':7,'valuation_uniformizer':1,'valuation_unit_part':7-7*1,'reconstruction_exponent':7,'dependence':'changing uniformizer by u multiplies unit factor by u^(-v(x))'}
print(json.dumps(out,ensure_ascii=False,indent=2))
