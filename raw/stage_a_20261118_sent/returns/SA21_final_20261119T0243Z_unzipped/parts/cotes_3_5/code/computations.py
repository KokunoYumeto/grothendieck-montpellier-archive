"""Finite independent certificates, not extraction or automated manuscript verdicts.
All structures and claims were selected after full reading. Exhaustive finite checks
certify only the explicitly printed models; no infinite theorem is inferred from them.
"""
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]/'outputs'
def powerset(xs):
 xs=list(xs)
 return [frozenset(c) for n in range(len(xs)+1) for c in combinations(xs,n)]
def canon(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,(set,frozenset)):return sorted((canon(y) for y in x),key=repr)
 if isinstance(x,dict):return {str(k):canon(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [canon(y) for y in x]
 return x
def comp_graph(xs,rel):
 unseen=set(xs); comps=[]
 while unseen:
  a=unseen.pop();seen={a};todo=[a]
  while todo:
   a=todo.pop(); nxt={b for b in unseen if rel(a,b) or rel(b,a)};unseen-=nxt;seen|=nxt;todo+=list(nxt)
  comps.append(seen)
 return comps
def relation_ok(xs,le):
 return all(le(x,x) for x in xs) and all(not(le(x,y) and le(y,x)) or x==y for x,y in product(xs,repeat=2)) and all(not(le(x,y) and le(y,z)) or le(x,z) for x,y,z in product(xs,repeat=3))
def poset_join(xs,le,sub):
 upp=[z for z in xs if all(le(s,z) for s in sub)]
 least=[z for z in upp if all(le(z,w) for w in upp)]
 return least[0] if len(least)==1 else None
def irreds(xs,le):
 return [x for x in xs if all(poset_join(xs,le,A)!=x or x in A for A in powerset(xs))]
results={}
# Initial graph data alone do not make moderated complementation injective.
V=set('abc');R=lambda x,y:x==y or 'c' in (x,y)
C=lambda T:{x for x in V if x not in T and all(R(x,t) for t in T)}
results['complement_noninjective']={'vertices':V,'reflexive_symmetric':all(R(x,x) for x in V) and all(R(x,y)==R(y,x) for x,y in product(V,repeat=2)),'C_a':C({'a'}),'C_b':C({'b'}),'same':C({'a'})==C({'b'})}
# Boolean polynomial identity over F_2, including every input.
results['boolean_ring']=[{'x':x,'y':y,'join':int(bool(x or y)),'polynomial_mod2':(x+y-x*y)%2} for x,y in product([0,1],repeat=2)]
assert all(r['join']==r['polynomial_mod2'] for r in results['boolean_ring'])
# One interval generates only itself and its complement as Boolean atoms.
regions=frozenset(['left','left_endpoint','interior','right_endpoint','right'])
I=frozenset(['left_endpoint','interior','right_endpoint'])
results['one_interval_boolean_atoms']={'ambient_cells':regions,'generated_algebra':[frozenset(),I,regions-I,regions],'atoms':[I,regions-I],'boundary_adapted_atom_count':5,'generated_atom_count':2}
results['gap_counts']=[{'removed_points':n,'gap_representatives':[Fraction(2*k-1,2) for k in range(n+1)],'gap_count':len([k for k in range(n+1)])} for n in range(11)]
results['rational_gap_witness']={'points':[str(Fraction(1,n)) for n in range(1,8)],'deleted_gap': [str(Fraction(1,5)+Fraction(1,100)),str(Fraction(1,4)-Fraction(1,100))], 'contains_no_sequence_point': all(not Fraction(21,100)<Fraction(1,n)<Fraction(24,100) for n in range(1,6)), 'tail_below_gap': str(Fraction(1,6))+' < 21/100'}
results['pair_cut_middle_on_rationals']={'a':0,'b':1,'c':2,'selected_components':['(1,+infinity)','(-infinity,1)','(0,2)'],'first_pair_disjoint':True,'other_intersection_witnesses':['3/2','1/2'],'proof_kind':'symbolic endpoint calculation; witnesses exact rational numbers'}
results['complement_component_counts']=[{'pieces':n,'left_gap':l,'right_gap':r,'count':n-1+l+r} for n in range(1,11) for l,r in product([0,1],repeat=2)]
# M3: C1, C2 and C3 hold, but lower-irreducibles does not preserve joins.
M=['0','a','b','c','1'];le=lambda x,y:x==y or x=='0' or y=='1';irr=irreds(M,le)
results['diamond_M3']={'is_poset':relation_ok(M,le),'all_joins_exist':all(poset_join(M,le,A) is not None for A in powerset(M)),'irreducibles':irr,'C2':all(poset_join(M,le,[p for p in irr if le(p,x)])==x for x in M),'C3':all(any(all(le(x,z) for x in A) for z in M) for A in powerset(M)),'join_a_b':poset_join(M,le,['a','b']),'irreducibles_below_join':{p for p in irr if le(p,'1')},'union_below_a_b':{'a','b'}}
assert irr==['a','b','c'] and results['diamond_M3']['C2']
nonsep=[frozenset(),frozenset('ab')]
results['nonseparating_family']={'M':['a','b'],'family':nonsep,'least_A_a':['a','b'],'least_A_b':['a','b'],'point_map_injective':False,'condition_a':all(frozenset().union(*fam) in nonsep for A in nonsep for fam in powerset([B for B in nonsep if B<=A])),'condition_b':all(any(x in A and all(A<=B for B in nonsep if x in B) for A in nonsep) for x in 'ab'),'condition_c':frozenset() in nonsep}
# Compatible-lower-ideal models from graphs. Orthogonality means compatible and
# no common lower element, exactly as in IV scans57,66.
def graph_model(n,edge_pairs):
 V=[f'v{i}' for i in range(n)];E=[f'e{i}' for i in range(len(edge_pairs))];M=V+E
 edge={E[k]:{V[i],V[j]} for k,(i,j) in enumerate(edge_pairs)}
 le=lambda x,y:x==y or (y in edge and x in edge[y])
 compat=lambda x,y:any(le(x,z) and le(y,z) for z in M)
 orth=lambda x,y:compat(x,y) and not any(le(z,x) and le(z,y) for z in M)
 F=[A for A in powerset(M) if all(y in A for x in A for y in M if le(y,x)) and all(compat(x,y) for x,y in product(A,repeat=2))]
 perp=lambda A:frozenset(y for y in M if all(orth(x,y) for x in A))
 cl=lambda A:perp(perp(A))
 closed=[A for A in powerset(M) if cl(A)==A]
 join=lambda A,B:cl(A|B)
 witnesses=[]
 for A,B,C in product(closed,repeat=3):
  lhs=A&join(B,C);rhs=join(A&B,A&C)
  if lhs!=rhs:witnesses.append({'A':A,'B':B,'C':C,'lhs':lhs,'rhs':rhs});break
 # C1: all subfamilies bounded by a figure have a union in F.
 c1=all(frozenset().union(*fam) in F for bound in F for fam in powerset([a for a in F if a<=bound]))
 prin={x:frozenset(y for y in M if le(y,x)) for x in M}
 irrF=irreds(F,lambda a,b:a<=b)
 c2=set(irrF)==set(prin.values()) and all(frozenset().union(*(p for p in irrF if p<=a))==a for a in F)
 c3=all(not all(compat(x,y) for x in a for y in b) or a|b in F for a,b in product(F,repeat=2))
 return {'M':M,'edges':edge,'is_poset':relation_ok(M,le),'compat_reflexive_symmetric':all(compat(x,x) for x in M) and all(compat(x,y)==compat(y,x) for x,y in product(M,repeat=2)),'compat_hereditary':all(not(compat(x,y) and le(a,x) and le(b,y)) or compat(a,b) for x,y,a,b in product(M,repeat=4)),'figure_count':len(F),'figures':F,'C1':c1,'C2':c2,'C3':c3,'components_M':comp_graph(M,le),'C4':len(comp_graph(M,le))==1,'orthogonal_pairs':[(x,y) for x,y in combinations(M,2) if orth(x,y)],'closed_supports':closed,'support_count':len(closed),'distributivity_failure':witnesses,'identity_subdivision_C5_C6_C7':'manual tautological check, not an executed formal certificate: subdivisions are identities; restriction and extension are the same figures; gluing is union when admitted','dimension':[0]*n+[1]*len(E)}
results['cyclic_support_lattice']=graph_model(5,[(0,1),(1,2),(2,3),(3,4),(4,0)])
results['hua_seven_element_model']=graph_model(4,[(0,1),(1,2),(2,3)])
assert results['cyclic_support_lattice']['support_count']==12
assert results['hua_seven_element_model']['support_count']==6
assert all(results[k][p] for k in ['cyclic_support_lattice','hua_seven_element_model'] for p in ['is_poset','compat_reflexive_symmetric','compat_hereditary','C1','C2','C3','C4'])
results['chain_same_support']={'poset':'0<1','figures':[[],['0'],['0','1']],'cosupp_nonempty':['empty figure only'],'same_support_of_proper_subfigure':True}
# All admissible figures over a finite set, by least-containing members and nonempty residuals.
def support(F):return frozenset().union(*F)
def residual(F,A):return A-frozenset().union(*(B for B in F if B<A))
def admissible(F):
 S=support(F)
 return all(residual(F,A) for A in F) and all(any(x in A and all(A<=B for B in F if x in B) for A in F) for x in S)
def subfigure(F,G):return F<=G and all(A in F for B in F for A in G if A<=B)
def preord(F):
 S=support(F)
 return {(x,y) for x,y in product(S,repeat=2) if all(x in A for A in F if y in A)}
def refines(F,G):return support(F)<=support(G) and preord(F)<=preord(G)
S=frozenset('ab');Figs=[F for F in powerset([A for A in powerset(S) if A]) if admissible(F)]
Elem=[F for F in Figs if F and any(all(A<=B for A in F) for B in F)]
results['set_figures_two_points']={'all_figures':Figs,'figure_count':len(Figs),'elementary_figures':Elem,'elementary_count':len(Elem),'components':comp_graph(Elem,subfigure)}
assert len(Elem)==5 and len(results['set_figures_two_points']['components'])==3
bad=frozenset([frozenset('a'),frozenset('b'),S])
results['boxtimes_counterexample']={'family':bad,'admissible':admissible(bad),'residual_top':residual(bad,S)}
old=frozenset([S]);new=frozenset([frozenset('a'),S]);
results['common_closed_stratum_counterexample']={'F':old,'Fprime':new,'G':[],'admissible_old':admissible(old),'admissible_new':admissible(new),'refines':refines(new,old),'same_support':support(new)==support(old),'retains_closed_stratum':S in new,'old_residual':residual(old,S),'new_residual':residual(new,S),'target_map_injective':False}
assert all(results['common_closed_stratum_counterexample'][x] for x in ['admissible_old','admissible_new','refines','same_support','retains_closed_stratum'])
# Three-point counterexample from V49, using the prose closure rather than the ambiguous drawing.
S=frozenset('uab');T=frozenset('ua');U=S-T
tau={(x,x) for x in S}|{('u','a'),('a','u'),('u','b'),('a','b')}
sigma={(x,x) for x in T}
star={(x,x) for x in S}|{('u','b'),('a','b')}
other={(x,x) for x in S}|{('a','b')}
def closed_sets(S,R):return [A for A in powerset(S) if all(x in A for x,y in R if y in A)]
ct=closed_sets(S,tau);cs=closed_sets(T,sigma);cstar=closed_sets(S,star);co=closed_sets(S,other)
trace=lambda C,T:{A&T for A in C}
checks={'finer':set(ct)<=set(co),'trace_T':trace(co,T)==set(cs),'trace_U':trace(co,U)==trace(ct,U),'finality':all((A in ct)==(A in co and A&T in trace(ct,T)) for A in powerset(S))}
close=lambda R,A:frozenset(x for x,y in R if y in A)
results['author_three_point_extension']={'S':S,'T':T,'tau_closed':ct,'sigma_closed':cs,'least_extension_closed':cstar,'other_closed':co,'weak_tests':checks,'least_cl_b':close(star,{'b'}),'other_cl_b':close(other,{'b'}),'different':cstar!=co}
assert all(checks.values()) and cstar!=co
# Closure formula checked on all eight subsets, independently of closed-set presentation.
results['least_extension_closure_formula']=[{'X':A,'actual':close(star,A),'formula':close(tau,A&U)|close(sigma,A&T)} for A in powerset(S)]
assert all(r['actual']==r['formula'] for r in results['least_extension_closure_formula'])
dest=OUT/'computations.json'; dest.write_text(json.dumps(canon(results),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'certificate':'all assertions passed','models':list(results),'output':str(dest),'cyclic_support_count':12,'hua_support_count':6,'two_point_elementary_components':3},indent=2))
