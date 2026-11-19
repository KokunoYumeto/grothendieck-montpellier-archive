"""Finite certificates and exact examples from cotes VIII/IX. No source text altered."""
from itertools import combinations,chain
from pathlib import Path
import json

def powerset(seq):
    seq=list(seq)
    return [frozenset(t) for k in range(len(seq)+1) for t in combinations(seq,k)]
def interval_mag(L,strict):
    le=lambda a,b:a==b or (a,b) in strict
    M=[('P',a) for a in L]+[('S',a,b) for a in L for b in L if (a,b) in strict]
    def faces(x): return {x} if x[0]=='P' else {x,('P',x[1]),('P',x[2])}
    def op(x,y):
        if y[0]=='P':return x==y
        if x[0]=='P':return (y[1],x[1]) in strict and (x[1],y[2]) in strict
        return le(y[1],x[1]) and le(x[2],y[2])
    def per(x,y):
        if x[0]=='P' and y[0]=='P':return (x[1],y[1]) in strict or (y[1],x[1]) in strict
        if x[0]=='S' and y[0]=='P':return per(y,x)
        if x[0]=='P':return le(x[1],y[1]) or le(y[2],x[1])
        return le(x[2],y[1]) or le(y[2],x[1])
    def perp(A):return frozenset(x for x in M if all(per(x,y) for y in A))
    def cl(A):return perp(perp(A))
    def label(x):return x[0]+'_'+''.join(map(str,x[1:]))
    return M,faces,op,per,perp,cl,label

out=[]
def emit(label,obj):out.append(label+'\n'+json.dumps(obj,ensure_ascii=False,indent=2))
M,faces,op,per,perp,cl,label=interval_mag(['a','b','c'],{('a','b'),('c','b')})
fmt=lambda A:sorted(label(x) for x in A)
Pa=('P','a');Pb=('P','b');Sab=('S','a','b')
emit('C-SA21-8-045 / 045R: exact V-poset computation',{
    'poset':'a<b, c<b, no other strict comparisons',
    'elements':fmt(M),'orthogonality':{label(x):fmt(perp({x})) for x in M},
    'cosupp_Pa':fmt(perp({Pa})),'supp_Pa':fmt(cl({Pa})),
    'cosupp_whole_Sab':fmt(perp(faces(Sab))),'supp_whole_Sab':fmt(cl(faces(Sab))),
    'shadow_Sab':fmt({('P','a'),('P','b'),Sab}),
    'printed_singleton_computation_correct':perp({Pa})=={Pb},
    'printed_whole_support_counterexample_correct':cl(faces(Sab))==set(M)
})
assert perp({Pa})=={Pb,Sab}
assert cl({Pa})=={Pa}
assert cl(faces(Sab))==set(M)
# Exhaustively verify relevant axioms in this five-element model.
ref=lambda x,y:any(op(x,z) for z in faces(y))
checks={}
checks['open_order_reflexive']=all(op(x,x) for x in M)
checks['open_order_antisymmetric']=all(x==y or not(op(x,y) and op(y,x)) for x in M for y in M)
checks['open_order_transitive']=all(not(op(x,y) and op(y,z)) or op(x,z) for x in M for y in M for z in M)
checks['unique_open_carrier']=all(sum(op(x,z) for z in faces(y))==1 for x in M for y in M if ref(x,y))
checks['face_lifting']=all(any(op(xp,yp) for yp in faces(y)) for x in M for y in M if op(x,y) for xp in faces(x))
checks['symmetric_irreflexive']=all(not per(x,x) for x in M) and all(per(x,y)==per(y,x) for x in M for y in M)
checks['orthogonality_hereditary']=all(not(per(x,y) and op(xp,x) and op(yp,y)) or per(xp,yp) for x in M for y in M for xp in M for yp in M)
checks['distinct_sibling_faces_disjoint']=all(x==y or per(x,y) for z in M for x in faces(z) for y in faces(z))
emit('All original magasin hypotheses for the V-poset',checks)
assert all(checks.values())

counts=[]
for n in range(1,7):
    vertices=frozenset(range(n));edges=[(i,i+1) for i in range(n-1)]
    figures=[(vertices,E) for E in powerset(edges)]
    counts.append({'vertices':n,'figures_with_exact_vertex_flag':len(figures),'formula':2**(n-1)})
emit('C-SA21-8-043: finite figure count',counts)

# Exact infinite family represented symbolically by a natural-number tail and atoms.
emit('C-SA21-8-026: exact infinite counterexamples',{
    'universe':'N disjoint union {ω,q}',
    'An':'{ω} union {k∈N:k≥n}, n≥0', 'intersection_all_An':'{ω}',
    'Ainfty':'{ω,q}', 'An_interior':'{n} for every n≥0',
    'example1_Ainfty_interior':'{ω,q}',
    'example1_partition':'all {n}, n≥0, together with {ω,q}',
    'example1_failure':'An meets block {ω,q} in {ω}, hence is not saturated; union of cells indexed below n omits ω',
    'example2_added_A':'{q}', 'example2_Ainfty_interior':'{ω}',
    'example2_partition':'all {n}, n≥0, {ω}, {q}',
    'example2_saturation':'every An is {ω} union all singleton {k} for k≥n; all sets are unions of blocks',
    'example2_failure':'Ainfty°={ω}⊂An, but q∈Ainfty∖An, so Ainfty is not below An',
    'proof':'An∖An+1={n} by the inequalities k≥n and k<n+1 for integers. A point in all tails must be ω. These formulas verify all n, rather than a finite-tail approximation.'
})

vertices=['a','b','c','d','e'];present={'a','c','e'};edges=[('a','b'),('b','c'),('c','d')]
degrees={v:sum(v in e for e in edges) for v in vertices}
types={v:('isolated' if degrees[v]==0 else ('proper boundary' if v in present else 'improper boundary') if degrees[v]==1 else ('redundant' if v in present else 'lacunary')) for v in vertices}
emit('C-SA21-8-051: five vertex types',{'degrees':degrees,'types':types,'final_degree_one_boundary':[v for v in vertices if degrees[v]==1]})

# Finite counterexample to extension of an arbitrary monotone elementary-value map.
emit('C-SA21-8-030: compatibility is needed',{
 'source':'two-element discrete maquette; its whole two-element set is a figure',
 'target':'two-element discrete incidence/open orders with empty orthogonality relation; figures are ∅ and the two singletons',
 'map':'send the two source elementary elements to the two distinct target singleton figures',
 'monotone':True,'source_finite':True,'target_unconditional_figure_atlas':True,
 'failure':'The image join does not exist: the two target elements are incompatible. Thus arbitrary monotonicity alone cannot define a join-preserving extension.'
})

def polar(E,R,A):return frozenset(x for x in E if all((x,y) in R for y in A))
def closure(E,R,A):return polar(E,R,polar(E,R,A))
E=frozenset('ab');Ep=frozenset('uv');R=frozenset();Rp=frozenset({('u','v'),('v','u')})
alpha={'a':frozenset('u'),'b':frozenset('v')}
im=lambda A:frozenset().union(*(alpha[a] for a in A))
A=frozenset('a')
left=closure(Ep,Rp,im(closure(E,R,A)))
right=closure(Ep,Rp,im(A))
preserves=all((xp,yp) in Rp for x,y in R for xp in alpha[x] for yp in alpha[y])
emit('C-SA21-9-030: independent exact counterexample to closure formula (*)',{
 'source':sorted(E),'source_orthogonality':sorted(R),
 'target':sorted(Ep),'target_orthogonality':sorted(Rp),
 'map':{x:sorted(v) for x,v in alpha.items()},'preserves_disjointness':preserves,
 'A':sorted(A),'source_closure_A':sorted(closure(E,R,A)),
 'alpha_star_source_closure_A':sorted(left),'closure_alpha_A':sorted(right),
 'formula_holds':left==right,
 'scope':'Own counterexample; unlike the author’s injection example, this refutes (*) itself.'})
assert preserves and left!=right

E=frozenset('a');Ep=frozenset('uv');R=frozenset();Rp=frozenset({('u','v'),('v','u')})
alpha={'a':frozenset('u')};B=frozenset('a')
left=closure(Ep,Rp,im(polar(E,R,B)))
right=polar(Ep,Rp,im(B))
emit('C-SA21-9-030: author’s nonsurjective-injection complement counterexample',{
 'source':['a'],'target':['u','v'],'map':'a↦u','B':['a'],
 'alpha_star_complement_B':sorted(left),'complement_alpha_B':sorted(right),
 'formula_holds':left==right,'closure_formula_star_in_this_model':'holds because both closure operators are identities'})
assert left!=right

# Exact separation of the strong and weakened face-disjointness axioms.
E=frozenset('abcde');edges=[('a','b'),('c','b'),('a','d'),('c','e')]
R=frozenset(edges+[(b,a) for a,b in edges])
face=lambda x,y:x==y or (x,y) in {('a','b'),('c','b')}
op=lambda x,y:x==y
dep=lambda y:frozenset(closure(E,R,{x}) for x in E if face(x,y))
checks={'weak_comparable_faces_disjoint':all((x,y) in R for x in E for y in E if x!=y and face(x,y)),
        'strong_common_faces_disjoint':all(x==y or (x,y) in R for z in E for x in E for y in E if face(x,z) and face(y,z)),
        'deployment_injective':len({dep(x) for x in E})==len(E),
        'open_order_is_identity':all(op(x,y)==(x==y) for x in E for y in E),
        'unique_open_carrier':all(sum(op(x,z) for z in E if face(z,y))==1 for x in E for y in E if face(x,y)),
        'face_lifting':all(any(op(xp,yp) for yp in E if face(yp,y)) for x in E for y in E if op(x,y) for xp in E if face(xp,x))}
emit('C-SA21-8-018 and 9-024: weak face-disjointness is genuinely weaker',{
 'incidence':'a<b,c<b; d,e otherwise isolated','open_refinement':'identity',
 'orthogonality_edges':edges,'checks':checks,
 'deployments':{x:sorted([sorted(s) for s in dep(x)]) for x in sorted(E)},
 'failure':'a,c are distinct faces of b but not orthogonal; deployment injectivity does not repair the weakened axiom.'})
assert checks['weak_comparable_faces_disjoint'] and checks['deployment_injective'] and not checks['strong_common_faces_disjoint']

counts=[]
for n in range(1,4):
    vertices=list(range(n+1));strict={(a,b) for a in vertices for b in vertices if a<b}
    M,faces,op,per,perp,cl,label=interval_mag(vertices,strict)
    closed={cl(s) for s in powerset(M)}
    atoms=[frozenset({('P',a)}) for a in vertices]+[frozenset({('S',a,a+1)}) for a in vertices[:-1]]
    supports={cl(set().union(*s)) for s in powerset(atoms)}
    counts.append({'consecutive_intervals':n,'strata_in_fixed_full_figure':2*n+1,'all_supports_in_total_chain_model':len(closed),'supports_generated_by_subsets_of_figure':len(supports),'expected':2**(2*n+1)})
    assert len(closed)==len(supports)==2**(2*n+1)
emit('C-SA21-9-012: finite Boolean count on chains, n=1,2,3 (not a general proof)',counts)

text='\n\n'.join(out)+'\n'
(Path(__file__).parent/'computations_output.txt').write_text(text)
print(text)
