"""Exact finite certificates for IX scans 66--104; no external packages.
All structures and maps are enumerated. Infinite conclusions are proved in
proof_checks.md, not inferred from enumeration. Run: python code/finite_checks.py
"""
from pathlib import Path
from itertools import product, combinations
import json, datetime
ROOT=Path(__file__).resolve().parents[1]
def powerset(xs):
    xs=list(xs)
    return [frozenset(xs[i] for i in range(len(xs)) if m>>i&1) for m in range(1<<len(xs))]
def orthoset(E,pairs):
    E=frozenset(E); pairs=set(pairs)
    assert all((b,a) in pairs for a,b in pairs)
    assert all(all((a,b) in pairs for b in E) for a in E if (a,a) in pairs)
    def perp(A): return frozenset(x for x in E if all((x,a) in pairs for a in A))
    def cl(A): return perp(perp(A))
    S=[A for A in powerset(E) if cl(A)==A]
    return E,perp,cl,S
def norm(x):
    if isinstance(x,(set,frozenset)): return sorted((norm(y) for y in x),key=str)
    if isinstance(x,tuple): return [norm(y) for y in x]
    if isinstance(x,list): return [norm(y) for y in x]
    if isinstance(x,dict): return {str(k):norm(v) for k,v in x.items()}
    return x
out={}
E,p,c,S=orthoset(['p','q'],[])
F,pf,cf,T=orthoset(['a','b'],[('a','b'),('b','a')])
alpha={'p':frozenset('a'),'q':frozenset('b')}
bar=lambda A:frozenset().union(*(alpha[x] for x in A))
f=lambda A:cf(bar(A))
g=lambda B:E if B else frozenset()
assert all(f(c(A|B))==cf(f(A)|f(B)) for A in S for B in S)
assert f(c(frozenset()))==cf(frozenset())
assert all((f(A)<=pf(B))==(A<=p(g(B))) for A in S for B in T)
gamma={y:frozenset(x for x in E if alpha[x]<=pf({y})) for y in F}
assert all(G not in S for G in gamma.values())
out['early_lemma2_omits_generator_condition']={'source_closed':S,'target_closed':T,'alpha':alpha,'join_map':{str(norm(A)):f(A) for A in S},'adjoint':{str(norm(B)):g(B) for B in T},'gamma_not_closed':gamma,'generator_failure':{'x':'p','f_cl_x':f(c({'p'})),'cl_alpha_x':cf(alpha['p'])}}
E,p,c,S=orthoset([0,1,2],[(0,1),(1,0)])
F,pf,cf,T=orthoset(['a'],[])
alpha={0:frozenset(),1:frozenset(),2:frozenset('a')}
bar=lambda A:frozenset().union(*(alpha[x] for x in A))
f=lambda A:cf(bar(A))
assert f(c({0,1})) != cf(f(c({0}))|f(c({1})))
out['early_lemma1_not_join_preserving']={'source_closed':S,'alpha':alpha,'join_of_0_1':c({0,1}),'f_join':f(c({0,1})),'join_images':cf(f(c({0}))|f(c({1})))}
# MO(4): the six-element complete ortholattice with four atoms.
L=tuple(range(6)); atoms=tuple(range(1,5)); BOT=0; TOP=5
def le(a,b): return a==0 or b==5 or a==b
def join(a,b):
    if a==0:return b
    if b==0:return a
    return a if a==b else 5
def meet(a,b):
    if a==5:return b
    if b==5:return a
    return a if a==b else 0
comp={0:5,5:0,1:2,2:1,3:4,4:3}
assert all(comp[comp[a]]==a and meet(a,comp[a])==0 and join(a,comp[a])==5 for a in L)
assert all(not le(a,b) or le(comp[b],comp[a]) for a in L for b in L)
maps=[]
for vals in product(L,repeat=5):
    m=(0,)+vals
    if all(m[join(a,b)]==join(m[a],m[b]) for a in L for b in L):maps.append(m)
def maple(f,g):return all(le(a,b) for a,b in zip(f,g))
zero=(0,)*6; top=(0,5,5,5,5,5)
ats=[f for f in maps if f!=zero and not any(g!=f and g!=zero and maple(g,f) for g in maps)]
coats=[f for f in maps if f!=top and not any(g!=f and g!=top and maple(f,g) for g in maps)]
assert len(maps)==234
assert len(ats)==40 and len(coats)==16
out['hom_has_no_orthocomplement']={'L_elements':L,'atoms':atoms,'complement':comp,'all_join_maps_count':len(maps),'atoms_count':len(ats),'coatoms_count':len(coats),'atoms':ats,'coatoms':coats,'reason':'Any order-reversing bijection must biject atoms with coatoms; 40 != 16.'}
# OR product and the separately orthoclosed relations.
E,p,c,S=orthoset(range(4),[(0,1),(1,0),(2,3),(3,2)])
P=tuple(product(range(4),repeat=2))
PR={(u,v) for u in P for v in P if v[0] in p({u[0]}) or v[1] in p({u[1]})}
_,pp,cp,SP=orthoset(P,PR)
R=frozenset([(0,0),(1,1),(2,2)])
rows={x:frozenset(y for xx,y in R if xx==x) for x in E}
cols={y:frozenset(x for x,yy in R if yy==y) for y in E}
assert all(v in S for v in list(rows.values())+list(cols.values()))
assert cp(R)==frozenset(P) and R!=cp(R)
separate=[R0 for R0 in powerset(P) if all(frozenset(y for x,y in R0 if x==a) in S for a in E) and all(frozenset(x for x,y in R0 if y==b) in S for b in E)]
assert set(SP)<=set(separate)
out['product_closed_vs_closed_fibers']={'factor_closed':S,'R':R,'rows':rows,'columns':cols,'R_perp':pp(R),'R_closure':cp(R),'product_closed_count':len(SP),'closed_fiber_count':len(separate)}
# A join map that cannot have the proposed span factorization; obstruction
# over every possible intermediate ortholattice is symbolic in proof_checks.md.
alpha=(0,0,1,1,1,1)
assert alpha in maps and alpha[5]==1 and alpha!=zero
out['span_obstruction_map']={'map':alpha,'joins_checked':36,'top_image':alpha[5],'reason':'Every nontrivial complete ortholattice homomorphism from MO(4) is injective, hence its orthogonal adjoint takes top to top.'}
# For trivial factors, complement/orthogonality is pointwise on generators,
# not all subsets. The crossed singleton assignments are disjoint at each point.
f={'p':frozenset('a'),'q':frozenset('b')};g={'p':frozenset('b'),'q':frozenset('a')}
assert all(f[x].isdisjoint(g[x]) for x in f)
assert not (f['p']|f['q']).isdisjoint(g['p']|g['q'])
out['pointwise_on_atoms_not_all_subsets']={'f':f,'g':g,'f_on_full':f['p']|f['q'],'g_on_full':g['p']|g['q']}
out['metadata']={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'program':'code/finite_checks.py','all_assertions_passed':True}
(ROOT/'outputs/finite_checks.json').write_text(json.dumps(norm(out),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':list(out),'join_maps':len(maps),'atoms':len(ats),'coatoms':len(coats),'product_closed':len(SP),'fiber_closed':len(separate),'all_assertions_passed':True},indent=2))
