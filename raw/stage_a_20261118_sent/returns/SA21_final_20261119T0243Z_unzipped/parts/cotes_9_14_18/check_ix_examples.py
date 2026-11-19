"""Finite certificates for IX scans105–140.

This is a transparent exhaustive Python calculation, not a proof-assistant
formalization.  Every hypothesis tested is named in the JSON output.  The
10-element reconstruction is expressly distinct from the literal transcription.
Run: python check_ix_examples.py > finite_checks_output.json
"""
import json
from itertools import combinations, product

def powerset(xs):
    xs=list(xs)
    for bits in range(1<<len(xs)):
        yield frozenset(x for i,x in enumerate(xs) if bits>>i&1)

def partial_order(E,rel):
    return (all(rel(x,x) for x in E)
      and all(not(rel(x,y) and rel(y,x)) or x==y for x,y in product(E,repeat=2))
      and all(not(rel(x,y) and rel(y,z)) or rel(x,z) for x,y,z in product(E,repeat=3)))

def equality_incidence_atelier(E,op,delta):
    """Exact primitive clauses for incidence=equality; no support axioms added."""
    inc=lambda x,y:x==y
    derived=lambda x,y:any(op(x,z) and inc(z,y) for z in E)
    receivers=lambda x,y:[z for z in E if inc(z,y) and op(x,z)]
    return {
      'incidence_is_partial_order':partial_order(E,inc),
      'open_refinement_is_partial_order':partial_order(E,op),
      'incidence_implies_derived_refinement':all(not inc(x,y) or derived(x,y) for x,y in product(E,repeat=2)),
      'derived_refinement_equals_open_refinement':all(derived(x,y)==op(x,y) for x,y in product(E,repeat=2)),
      'unique_receiver_for_each_derived_refinement':all(not derived(x,y) or len(receivers(x,y))==1 for x,y in product(E,repeat=2)),
      'receiver_for_every_face_under_refinement':all(not(op(x,y) and inc(z,x)) or len(receivers(z,y))==1 for x,y,z in product(E,repeat=3)),
      'disjointness_symmetric_irreflexive':all(delta(x,y)==delta(y,x) for x,y in product(E,repeat=2)) and all(not delta(x,x) for x in E),
      'open_refinement_heredity':all(not(op(x,y) and delta(y,z)) or delta(x,z) for x,y,z in product(E,repeat=3)),
      'distinct_common_faces_clause':all(not(inc(x,z) and inc(y,z) and x!=y) or delta(x,y) for x,y,z in product(E,repeat=3)),
    }

class FiniteOL:
    def __init__(self, elements, le, complement, zero, one):
        self.E=tuple(elements); self.le=le; self.C=complement
        self.zero=zero; self.one=one; self.J={}; self.M={}
        for x,y in product(self.E,repeat=2):
            ups=[z for z in self.E if le(x,z) and le(y,z)]
            los=[z for z in self.E if le(z,x) and le(z,y)]
            j=[z for z in ups if all(le(z,t) for t in ups)]
            m=[z for z in los if all(le(t,z) for t in los)]
            assert len(j)==len(m)==1,(x,y,j,m)
            self.J[x,y]=j[0]; self.M[x,y]=m[0]
        self.axioms={
            'bounded_partial_order':all(le(zero,x) and le(x,one) and le(x,x) for x in self.E)
              and all(not(le(x,y) and le(y,x)) or x==y for x,y in product(self.E,repeat=2))
              and all(not(le(x,y) and le(y,z)) or le(x,z) for x,y,z in product(self.E,repeat=3)),
            'binary_lattice_hence_complete_because_finite':True,
            'complement_involutive_order_reversing':all(complement(complement(x))==x for x in self.E)
              and all(not le(x,y) or le(complement(y),complement(x)) for x,y in product(self.E,repeat=2)),
            'complement_meet_zero_join_one':all(self.meet(x,complement(x))==zero and self.join(x,complement(x))==one for x in self.E)
        }
        assert all(self.axioms.values()),self.axioms
    def join(self,x,y): return self.J[x,y]
    def meet(self,x,y): return self.M[x,y]
    def orth(self,x,y): return self.le(x,self.C(y))
    def sup(self,xs):
        out=self.zero
        for x in xs: out=self.join(out,x)
        return out
    def generated(self,xs):
        s=set(xs)|{self.zero,self.one}
        while True:
            t=s|{self.C(x) for x in s}|{self.join(x,y) for x,y in product(s,repeat=2)}|{self.meet(x,y) for x,y in product(s,repeat=2)}
            if t==s: return s
            s=t
    def boolean(self,xs=None):
        s=self.E if xs is None else self.generated(xs)
        return all(self.meet(x,self.join(y,z))==self.join(self.meet(x,y),self.meet(x,z)) for x,y,z in product(s,repeat=3))
    def om_witness(self):
        return next(((x,y) for x,y in product(self.E,repeat=2) if self.le(x,y) and self.join(x,self.meet(y,self.C(x)))!=y),None)
    def repr(self,x): return str(x)

OUT={'date':'2026-11-19','scope':'Finite exhaustive Python certificates; no theorem-prover certification; manuscript/reconstruction distinguished.'}

# All relations on labelled sets of size at most3. Γ is the graph subset,
# not an arbitrary span with duplicate edges.
count=0; failures=[]
for n,m in product(range(4),repeat=2):
    for bits in range(1<<(n*m)):
        count+=1
        edges={(i,j) for i in range(n) for j in range(m) if bits>>(i*m+j)&1}
        top=(1<<n)-1; top2=(1<<m)-1
        P=range(1<<n); Q=range(1<<m)
        u=lambda a: sum(1<<j for j in range(m) if any((i,j) in edges and a>>i&1 for i in range(n)))
        v=lambda b: sum(1<<i for i in range(n) if any((i,j) in edges and b>>j&1 for j in range(m)))
        disj=all(a&b or not(u(a)&u(b)) for a,b in product(P,repeat=2))
        meets=all(u(a&b)==u(a)&u(b) for a,b in product(P,repeat=2))
        diff=all(u(a&~b)==u(a)&~u(b) for a,b in product(P,repeat=2))
        diff_restricted=all(a&b!=b or u(a&~b)==u(a)&~u(b) for a,b in product(P,repeat=2))
        fp_inj=all(sum((i,j) in edges for i in range(n))<=1 for j in range(m))
        fp_surj=all(any((i,j) in edges for i in range(n)) for j in range(m))
        f_surj=all(any((i,j) in edges for j in range(m)) for i in range(n))
        f_inj=all(sum((i,j) in edges for j in range(m))<=1 for i in range(n))
        top_pres=u(top)==top2
        comp=all(u(top^a)==top2^u(a) for a in P)
        zero_reflect=all(u(a)!=0 or a==0 for a in P)
        v_zero_reflect=all(v(b)!=0 or b==0 for b in Q)
        faithful=all((a&b==0)==(u(a)&u(b)==0) for a,b in product(P,repeat=2))
        v_comp=all(v(top2^b)==top^v(b) for b in Q)
        tests={
          'A_disjoint_meet_difference_graph_equivalence':len({bool(disj),meets,diff,diff_restricted,fp_inj})==1,
          'Cor1_top_complement_bijection_equivalence':len({bool(disj and top_pres),meets and top_pres,comp,fp_inj and fp_surj})==1,
          'B_top_transpose_zero_reflection_graph_surjection':len({top_pres,v_zero_reflect,fp_surj})==1,
          'Cor2_faithful_disjointness':len({faithful,bool(disj and zero_reflect),fp_inj and f_surj})==1,
          'Cor3_surjective_inverse_image':len({comp and zero_reflect,faithful and top_pres,fp_inj and fp_surj and f_surj})==1,
          'direct_injection_characterization':bool(disj and v_comp)==(fp_inj and f_inj and f_surj),
          'orthogonality_conjugacy':all((u(a)&b==0)==(a&v(b)==0) for a,b in product(P,Q)),
        }
        if not all(tests.values()): failures.append({'n':n,'m':m,'edges':list(edges),'tests':tests})
assert not failures, failures[:1]
OUT['set_relation_classification']={'manuscript':'IX105–106 and IX133','sizes':'0≤|E|,|E′|≤3','relations_checked':count,'failed_instances':failures,'all_named_equivalences_checked':list(tests),'scope':'Exhaustion checks finite instances; the proof for arbitrary sets is separately given in formalism_and_checks.md.'}

# O6 as the complete ortholattice of closed subsets of the P4 orthoset.
V=frozenset(range(4)); edges={frozenset(e) for e in [(0,1),(1,2),(2,3)]}
polar=lambda a: frozenset(v for v in V if all(frozenset((v,w)) in edges for w in a))
closed=tuple(a for a in powerset(V) if polar(polar(a))==a)
O6=FiniteOL(closed,lambda x,y:x<=y,polar,frozenset(),V)
A=frozenset({1}); B=frozenset({2}); Btop=polar(B)
ol6=lambda x: sorted(x)
OUT['P4_comparability_counterexample']={
 'manuscript':'IX111 question about Σ from the comparability relation of a poset',
 'poset_strict_pairs':[[0,1],[2,1],[2,3]],
 'strict_order_irreflexive_transitive':all(x!=y for x,y in {(0,1),(2,1),(2,3)}) and all((a,d) in {(0,1),(2,1),(2,3)} for a,b in {(0,1),(2,1),(2,3)} for c,d in {(0,1),(2,1),(2,3)} if b==c),
 'comparability_edges_equal_P4':all((frozenset((x,y)) in edges)==((x,y) in {(0,1),(2,1),(2,3)} or (y,x) in {(0,1),(2,1),(2,3)}) for x,y in product(V,repeat=2)),
 'orthoclosed_sets':[ol6(x) for x in closed],
 'ortholattice_axioms':O6.axioms,
 'orthomodular_law_fails_for':[ol6(x) for x in O6.om_witness()],
 'conclusion':'The comparability-poset construction need not be orthomodular.'}

# B4 -> O6: complete join/meet preserving, orthogonality preserving, top
# preserving, with conjugate transpose, but not complement preserving.
u={0:frozenset(),1:A,2:B,3:V}
right=lambda y: sum(1<<i for i in range(2) if u[1<<i]<=y)
v=lambda y: 3^right(polar(y))
tests={
 'complete_join_preserving':all(u[x|y]==O6.join(u[x],u[y]) for x,y in product(range(4),repeat=2)) and u[0]==O6.zero,
 'complete_meet_preserving':all(u[x&y]==O6.meet(u[x],u[y]) for x,y in product(range(4),repeat=2)) and u[3]==O6.one,
 'orthogonality_preserving':all(x&y or O6.orth(u[x],u[y]) for x,y in product(range(4),repeat=2)),
 'top_preserving':u[3]==V,
 'transpose_is_join_preserving':v(O6.zero)==0 and all(v(O6.join(x,y))==v(x)|v(y) for x,y in product(O6.E,repeat=2)),
 'exact_orthogonality_conjugacy':all(O6.orth(u[x],y)==(x&v(y)==0) for x,y in product(range(4),O6.E)),
}
assert all(tests.values())
assert u[2]!=polar(u[1])
OUT['general_spatios_corollary_failure']={'manuscript':'IX107–108 proposed extension of IX105–106','source':'four-element Boolean powerset','target':'O6=P4 orthoclosed subsets','hypotheses':tests,'u_table':{str(k):ol6(z) for k,z in u.items()},'v_table':{str(ol6(y)):v(y) for y in closed},'failed_complement_equation':{'u(C{0})':ol6(u[2]),'C(u({0}))':ol6(polar(u[1]))},'conclusion':'Even all joins, all meets, orthogonality, top and existence of transpose do not imply preservation of complement for arbitrary complete ortholattices.'}

# MO2 = horizontal sum of two four-element Boolean algebras.
E=('0','a','ac','b','bc','1'); comp={'0':'1','1':'0','a':'ac','ac':'a','b':'bc','bc':'b'}
MO2=FiniteOL(E,lambda x,y:x==y or x=='0' or y=='1',lambda x:comp[x],'0','1')
orth_families=[s for s in powerset(E) if all(x==y or MO2.orth(x,y) for x,y in product(s,repeat=2))]
assert MO2.om_witness() is None and not MO2.boolean()
assert all(MO2.boolean(s) for s in orth_families)
OUT['orthomodular_does_not_force_Boolean']={'manuscript':'IX109 corollary and IX111 question','model':'MO2: 0,1 and four atoms a,ac,b,bc; complement pairs (a,ac),(b,bc)','ortholattice_axioms':MO2.axioms,'orthomodular_all_comparable_pairs':True,'every_orthogonal_subfamily_generates_Boolean':True,'number_of_orthogonal_subsets_checked':len(orth_families),'arbitrary_family_quantifier':'Any indexed orthogonal family has at most two distinct nonzero entries; zero repetitions do not alter generated subalgebra. Thus the infinite-family version is covered too.','distributivity_failure':'a meet (b join bc)=a, while (a meet b) join (a meet bc)=0.'}

# Scan113 reconstruction: base Boolean algebra on blocks {i,i′},{j},{k},
# with an extra singleton {i} and its ordinary complement.
full=15
family=sorted({s for s in range(16) if bool(s&1)==bool(s&2)}|{1,14})
T10=FiniteOL(family,lambda x,y:x&y==x,lambda x:15^x,0,15)
literal=sorted({s for s in range(16) if ((s&1) and (s&2)) or ((not s&4) and (not s&2)) or s in (1,14)})
literal_complement_closed=all((15^x) in literal for x in literal)
assert len(family)==10 and T10.om_witness() is not None
OUT['scan113_reconstruction']={
 'label_bits':{'i':1,'i_prime':2,'j':4,'k':8},
 'analyst_reconstructed_set_family':family,
 'ortholattice_axioms':T10.axioms,
 'orthomodular_failure':{'b':1,'c':3,'c_meet_Cb':T10.meet(3,14),'b_join_that':T10.join(1,T10.meet(3,14))},
 'displayed_joins_recomputed':{'j_join_k':T10.join(4,8),'k_join_i':T10.join(8,1),'i_join_j':T10.join(1,4)},
 'literal_second_disjunct_j_i_prime_absent_family':literal,
 'literal_family_complement_closed':literal_complement_closed,
 'diagram_alarm':'The transcription includes an extra marked edge c<C, while C is the proposed complement of c; this cannot hold for nonzero c in an ortholattice.',
 'reconstruction_alarm':'Replace the second disjunct j,i′∉E by i,i′∉E and omit the marked c<C edge to obtain this valid model. No change to the transcription or decision about the ink is made.'}

# General Lemma3: omit decomposition a=a′∨a″ and the converse fails.
small=A; large=Btop
assert small<large and O6.meet(large,polar(small))==O6.zero
assert O6.boolean([small]) and not O6.boolean([small,large])
OUT['residual_lemma_missing_hypothesis']={
 'manuscript':'IX121–122 Lemma3 in its general-spatios formulation',
 'A0':[ol6(small)],'A1':[ol6(large)],
 'nonzero_finite_orthogonal_each':True,'pointwise_refinement_A0_ll_A1':small<=large,
 'residual_A1_doubleprime':ol6(O6.meet(large,polar(small))),
 'nonzero_residual_union':[ol6(small)],
 'residual_union_commensurable':True,'original_union_commensurable':False,
 'missing_decomposition':{'a':ol6(large),'a_prime_join_a_doubleprime':ol6(small)},
 'scope':'This refutes the standalone general criterion without Lemma2(ii)(a). If preceding γ² is retained as a standing hypothesis, that decomposition is available and the criterion is valid; no refutation of that strengthened reading.'}

# An 18-element ortholattice: double the complementary rank-two elements
# {1,3}, {2,4} of the Boolean16 into two-element chains. This is an analyst
# construction to test IX123; all lattice operations are independently inferred
# from the full order, not supplied so as to force the desired equations.
special={5,10}
E18=tuple((s,k) for s in range(16) for k in (range(2) if s in special else range(1)))
le18=lambda x,y:(x[0]!=y[0] and x[0]&y[0]==x[0]) or (x[0]==y[0] and x[1]<=y[1])
c18=lambda x:(15^x[0],1-x[1] if x[0] in special else 0)
T18=FiniteOL(E18,le18,c18,(0,0),(15,0))
g=(1,0); gp=(2,0); f=(3,0); fp=(4,0); e=(7,0)
A0={g,gp}; A1={f}; A2={f,fp}
pointwise=lambda X,Y:all(any(T18.le(x,y) for y in Y) for x in X)
commref=lambda X,Y:pointwise(X,Y) and T18.boolean(X|Y)
tests={
 'each_figure_nonzero_pairwise_orthogonal':all(all(x!=T18.zero for x in X) and all(x==y or T18.orth(x,y) for x,y in product(X,repeat=2)) for X in (A0,A1,A2)),
 'each_figure_commensurable':all(T18.boolean(X) for X in (A0,A1,A2)),
 'A0_comm_refines_A1':commref(A0,A1),
 'A1_comm_refines_A2':commref(A1,A2),
 'A0_pointwise_refines_A2':pointwise(A0,A2),
 'A0_does_not_comm_refine_A2':not commref(A0,A2),
 'author_triple_g_gp_fp_is_orthogonal':all(x==y or T18.orth(x,y) for x,y in product((g,gp,fp),repeat=2)),
 'g_gp_and_f_fp_separately_commensurable':T18.boolean([g,gp]) and T18.boolean([f,fp]),
 'every_two_of_g_gp_fp_commensurable':all(T18.boolean([x,y]) for x,y in combinations((g,gp,fp),2)),
 'g_gp_fp_not_jointly_commensurable':not T18.boolean([g,gp,fp])}
assert all(tests.values())
OUT['commensurable_refinement_not_transitive']={
 'manuscript':'IX123 construction and doubt; also IX121 pairwise versus joint commensurability',
 'model_description':'Boolean powerset of four labels; duplicate subset bitmasks5 and10 as chains (s,0)<(s,1), complement swaps complementary duplicated chains in reverse order.',
 'elements':[list(x) for x in E18],
 'full_order_pairs':[[list(x),list(y)] for x,y in product(E18,repeat=2) if le18(x,y)],
 'complement':{str(x):list(c18(x)) for x in E18},
 'ortholattice_axioms':T18.axioms,
 'figures':[[list(x) for x in sorted(X)] for X in (A0,A1,A2)],
 'all_required_hypotheses_and_failure':tests,
 'generated_cardinalities':[len(T18.generated(X)) for X in (A0|A1,A1|A2,A0|A2)],
 'scope':'Refutes transitivity on commensurable discrete spatial figures in a complete ortholattice. It confirms the author’s triple obstruction, but does not claim a counterexample using only one-stratum figures at every step.'}

# Deleted quotient-topology characterization: final topology versus single
# comparability lifting. This is a general finite-poset check, not an atelier
# realization satisfying the preceding subdivision assumptions.
P=tuple(range(4)); Q=tuple(range(3)); pairs={(0,1),(2,3)}; phi={0:0,1:1,2:1,3:2}
leP=lambda x,y:x==y or (x,y) in pairs
leQ=lambda x,y:x<=y
lower=lambda U,E,le:all(not(y in U and le(x,y)) or x in U for x,y in product(E,repeat=2))
quotient=all(lower(U,Q,leQ)==lower({x for x in P if phi[x] in U},P,leP) for U in powerset(Q))
one_step=all(not leQ(x,y) or any(phi[a]==x and phi[b]==y and leP(a,b) for a,b in product(P,repeat=2)) for x,y in product(Q,repeat=2))
assert quotient and not one_step
OUT['deleted_quotient_topology_equivalence']={'manuscript':'IX139–140 canceled block','source_poset':'disjoint union of chains0<1 and2<3','target_poset':'chain0<1<2','map':phi,'monotone_surjective':set(phi.values())==set(Q) and all(not leP(x,y) or leQ(phi[x],phi[y]) for x,y in product(P,repeat=2)),'all_eight_target_subsets_tested_for_final_Alexandrov_topology':quotient,'single_comparable_pair_lifting_for_0_le_2':any(phi[a]==0 and phi[b]==2 and leP(a,b) for a,b in product(P,repeat=2)),'scope':'Only the general poset/topology equivalence is refuted. No complete atelier realization of this map is asserted, and the passage is canceled in the manuscript.'}

# Bare IX134 atelier morphisms can have a non-orthoclosed kernel.
source=tuple(range(4)); target=(1,2,3); bottom=-1
delta=lambda x,y:frozenset((x,y)) in edges
p=lambda x:bottom if x==0 else x
inc_ext=lambda x,y:x==bottom or y==bottom or x==y
open_ext=lambda x,y:x==bottom or x==y
delta_ext=lambda x,y:x==bottom or y==bottom or delta(x,y)
source_primitive=equality_incidence_atelier(source,lambda x,y:x==y,delta)
target_primitive=equality_incidence_atelier(target,lambda x,y:x==y,delta)
bare_axioms={**source_primitive,
 'target_has_same_bare_axioms_by_induced_subgraph':all(target_primitive.values()),
 'morphism_preserves_incidence_with_bidirectional_zero':all(x!=y or inc_ext(p(x),p(y)) for x,y in product(source,repeat=2)),
 'morphism_preserves_open_refinement_with_bottom_zero':all(x!=y or open_ext(p(x),p(y)) for x,y in product(source,repeat=2)),
 'morphism_preserves_disjointness_with_universally_orthogonal_zero':all(not delta(x,y) or delta_ext(p(x),p(y)) for x,y in product(source,repeat=2))}
assert all(bare_axioms.values()) and polar(polar({0}))!=frozenset({0})
OUT['bare_morphism_kernel_not_closed']={'manuscript':'IX134–135 provisional morphism and kernel; earlier primitive axioms IX41','source':'P4, both typed primitive orders equality, disjointness P4 edges','target':'induced graph on vertices1,2,3 with both primitive orders equality','map':{str(x):p(x) for x in source},'zero_symbol':bottom,'all_named_hypotheses':bare_axioms,'target_primitive_axioms':target_primitive,'kernel':[0],'kernel_orthoclosure':ol6(polar(polar({0}))),'scope':'Counterexample to automatic orthoclosedness for the bare provisional definition. The extra support-admissibility axioms are not imposed; the manuscript itself anticipates extra conditions.'}

# Faithful external realization does not impose Boolean commensurability on
# the INTERNAL virtual support lattice.  VIII68 lists exactly(i)–(iv).
points={('private',x) for x in source}|{('pair',x,y) for x,y in combinations(source,2) if not delta(x,y)}
S={x:frozenset(t for t in points if (t[0]=='private' and t[1]==x) or (t[0]=='pair' and x in t[1:])) for x in source}
faithful_tests={
 'VIII68_i_refinement_monotonicity':all(x!=y or S[x]<=S[y] for x,y in product(source,repeat=2)),
 'VIII68_ii_orthogonality_implies_disjoint_open_supports':all(not delta(x,y) or not(S[x]&S[y]) for x,y in product(source,repeat=2)),
 'VIII68_iii_each_open_support_nonempty':all(S[x] for x in source),
 'VIII68_iv_closed_support_union_of_face_open_supports':all(S[x]==frozenset().union(*(S[y] for y in source if y==x)) for x in source),
 'VIII71_faithfulness_exact_equivalence':all(delta(x,y)==(not(S[x]&S[y])) for x,y in product(source,repeat=2)),
 'normalization_coverage':frozenset().union(*S.values())==points,
 'normalization_point_separation':all(p==q or any((p in S[x])!=(q in S[x]) for x in source) for p,q in product(points,repeat=2)),
 'middle_edge_is_a_figure_lower_compatible_subset':delta(1,2),
 'virtual_open_supports_are_closed_singletons':polar(polar({1}))==A and polar(polar({2}))==B,
 'their_virtual_subortholattice_is_not_Boolean':not O6.boolean([A,B])}
assert all(faithful_tests.values())
OUT['faithful_external_does_not_imply_commensurability']={'manuscript':'IX124 question; exact external-support definition VIII68–71','atelier':'Same P4 bare atelier, incidence=equality, open-refinement=equality; all figures are cliques.','all_primitive_atelier_hypotheses':{k:v for k,v in bare_axioms.items() if not k.startswith('morphism') and not k.startswith('target')},'external_point_set':[list(p) for p in sorted(points)],'external_supports':{str(x):[list(p) for p in sorted(S[x])] for x in source},'all_external_support_hypotheses_and_failure':faithful_tests,'figure':[1,2],'virtual_generated_subortholattice':[ol6(x) for x in O6.generated([A,B])],'conclusion':'Normalized faithful external support does not imply supp1; hence it does not imply γ³.','scope':'No full-faithfulness hypothesis from VIII86–87 is imposed or claimed. Axiom versions and both typed primitive orders are fixed explicitly.'}

# VIII55–56 full figure pullback and IX132 elementary-or-zero assertion.
base=frozenset('abc'); subset=frozenset('ab')
F=(frozenset('a'),frozenset('b'),base)
opens=lambda fig:{s:s-frozenset().union(*(t for t in fig if t<s)) for s in fig}
original_open=opens(F)
pull=tuple(s&subset for s in F if original_open[s]&subset)
pull_open=opens(pull)
valid=lambda fig:all(opens(fig).values()) and all(not(opens(fig)[s]&opens(fig)[t]) for s,t in combinations(fig,2))
assert valid(F) and valid(pull) and any(all(t<=s for t in F) for s in F)
assert pull and not any(all(t<=s for t in pull) for s in pull)
OUT['elementary_figure_pullback_not_elementary']={'manuscript':'IX132 with VIII55 formula(1) and VIII56 retained lower faces','E':sorted(base),'E_prime':sorted(subset),'set_map':'inclusion E_prime into E','original_closed_strata':[sorted(s) for s in F],'original_open_strata':[sorted(original_open[s]) for s in F],'original_admissible_and_elementary':True,'corrected_figure_pullback':[sorted(s) for s in pull],'pullback_admissible':valid(pull),'pullback_nonempty':True,'pullback_has_greatest_stratum':False,'scope':'Same full-figure pullback displayed in IX132 and explicitly defined in VIII55–56. A different partial map on elementary generators that sends a killed top open stratum to zero is a possible reconstruction, not this figure pullback.'}

# Conditional check: commensurability by itself cannot give the final local
# subdivision-detection implication.  The name Atmag supp² on scan138 must be
# checked against scan119's gamma²; the certificate does not decide that ink.
W=frozenset(('g','f','h'))
d3=lambda x,y:{x,y}=={'g','h'}
o3=lambda x,y:x==y or (x,y)==('g','f')
p3=lambda S:frozenset(x for x in W if all(d3(x,y) for y in S))
closed3=tuple(S for S in powerset(W) if p3(p3(S))==S)
L3=FiniteOL(closed3,lambda x,y:x<=y,p3,frozenset(),W)
assert L3.boolean()
Sg=p3(p3({'g'})); Sf=p3(p3({'f'}))
tests3={**equality_incidence_atelier(W,o3,d3),
 'virtual_support_lattice_Boolean_hence_every_commensurability_gamma_n':L3.boolean(),
 'G_refines_F':o3('g','f'),
 'condition_iii_no_Z_refines_F_disjoint_G':not any(o3(z,'f') and d3(z,'g') for z in W),
 'condition_ii_equal_supports_fails':Sg!=Sf,
}
assert all(tests3.values())
OUT['commensurability_alone_not_local_subdivision_detection']={'manuscript':'IX138–139 (iii)⇒(ii), conditional identification of Atmag supp² with scan119 gamma²','source_atelier':'g,f,h; incidence equality; open-refinement g<f; only disjoint pair g,h','all_named_hypotheses':tests3,'virtual_supports':[sorted(x) for x in closed3],'G':['g'],'F':['f'],'supp_G':sorted(Sg),'supp_F':sorted(Sf),'scope':'This refutes derivability from bare At1–4 plus arbitrary commensurability axioms. It is NOT an unconditional refutation of the manuscript if Atmag supp² denotes a stronger local support-density condition. Spatiality/refinement reflection is absent in the model.'}

print(json.dumps(OUT,ensure_ascii=False,indent=2))
