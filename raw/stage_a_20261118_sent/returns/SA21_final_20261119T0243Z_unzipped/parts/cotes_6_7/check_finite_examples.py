"""Reproducible finite checks for SA21 cotes 156-6/7, 2026-11-19.

These certificates verify the stated finite models, not arbitrary manuscript
theorems. Sets are finite, so the quantifiers tested below are exhaustive.
Author: GPT-6 Astra Pro, run /root/cotes_156_6_7.
"""
from itertools import combinations, product
import json
from pathlib import Path

OUT = Path(__file__).parent

def powerset(s):
    s = tuple(sorted(s, key=repr))
    return [frozenset(c) for n in range(len(s)+1) for c in combinations(s,n)]

def display(s):
    return sorted(s)

report = {"date":"2026-11-19", "scope":"exhaustive finite model certificates; no claim of formal proof-assistant verification"}

# VII scan14-15: the claimed simplex criterion.
# Nonempty faces of a square, ordered by inclusion of vertex sets.
V = frozenset(range(4))
faces = [frozenset([v]) for v in V]
faces += [frozenset([0,1]),frozenset([1,2]),frozenset([2,3]),frozenset([3,0]),V]
common_lower_pair_meets = True
for a,b in product(faces,repeat=2):
    lowers = [c for c in faces if c<=a and c<=b]
    if lowers:
        common_lower_pair_meets &= any(all(c<=m for c in lowers) for m in lowers)
preds = {tuple(sorted(f)): [g for g in faces if g<f and not any(g<h<f for h in faces)] for f in faces}
every_nonminimal_two_predecessors = all(len(preds[tuple(sorted(f))])>=2 for f in faces if len(f)>1)
assert common_lower_pair_meets and every_nonminimal_two_predecessors
assert all(f<=V for f in faces)
assert len(faces)==9 and 2**len(V)-1==15
report["square_simplex_counterexample"] = {
    "manuscript":"J156-7-01, scans14-15, lines139-143",
    "finite":True,"greatest_element":display(V),
    "every_pair_with_common_lower_bound_has_infimum":common_lower_pair_meets,
    "every_nonminimal_face_has_at_least_two_immediate_predecessors":every_nonminimal_two_predecessors,
    "nonempty_face_count":len(faces),"nonempty_subsets_of_minimal_elements":2**len(V)-1,
    "conclusion":"The written criterion does not characterize simplices; square face poset is not Boolean."
}

# VII scans94-100: local support-complement formula, including the L1 rescue.
# Graph A'--A--B--B'; edges mean orthogonality of distinct loci.
M = frozenset(["A'","A","B","B'"])
edges = {frozenset(e) for e in [("A'","A"),("A","B"),("B","B'")]}
orth = lambda a,b: frozenset([a,b]) in edges and a!=b
clique = lambda a: all(orth(x,y) for x,y in combinations(a,2))
figures = [s for s in powerset(M) if clique(s)]
le = lambda a,b: a<=b
ref = le
strata = lambda f: [frozenset([x]) for x in f]
compatible = lambda a,b: clique(a|b)
disjoint = lambda a,b: compatible(a,b) and not(a&b)
perp = lambda a: frozenset(x for x in M if all(orth(x,y) for y in a))
closure = lambda a: perp(perp(a))
strong_interior = lambda x: frozenset([x])  # each stratum is a singleton locus; boundary is empty
axioms = {}

# At1: every bounded family has its set union, including the empty family.
axioms["At1_nonempty_and_bounded_arbitrary_joins"] = bool(figures) and all(
    (not any(all(f<=b for f in family) for b in figures))
    or frozenset().union(*family) in figures
    for family in powerset(figures))
# Strictly join-irreducible nonzero figures are exactly singletons.
strict_irreducibles = []
for f in figures:
    if not f: continue
    proper = [g for g in figures if g<f]
    if not any(frozenset().union(*fam)==f for fam in powerset(proper)):
        strict_irreducibles.append(f)
axioms["At2_strict_irreducibles_and_decomposition"] = set(strict_irreducibles)==set(strata(M)) and all(
    frozenset().union(*strata(f))==f for f in figures)
# VI scan12 uses the STRONG complete join-prime formulation. Verify that
# formulation separately, including the empty family, for every bounded
# family, rather than relying on ordinary complete join-irreducibility.
complete_join_primes = []
for x in figures:
    if not x: continue
    valid = True
    for family in powerset(figures):
        if not any(all(f<=b for f in family) for b in figures):
            continue
        join = frozenset().union(*family)
        if x<=join and not any(x<=f for f in family):
            valid = False
    if valid:
        complete_join_primes.append(x)
axioms["At2_strong_complete_join_primality_VI_scan12"] = set(complete_join_primes)==set(strata(M))
axioms["At3_pairwise_stratum_compatibility"] = all(
    not all(compatible(x,y) for x in strata(f) for y in strata(g)) or compatible(f,g)
    for f,g in product(figures,repeat=2))
axioms["At4_refinement_stratumwise"] = all(
    ref(f,g)==all(any(ref(x,y) for y in strata(g)) for x in strata(f))
    for f,g in product(figures,repeat=2))
axioms["At5_least_receiving_stratum"] = all(
    not ref(x,f) or any(ref(x,y) and all(y<=z for z in strata(f) if ref(x,z)) for y in strata(f))
    for x in strata(M) for f in figures)
axioms["At6_compatible_refinement_is_subfigure"] = all(
    not(compatible(x,y) and ref(x,y)) or le(x,y)
    for x,y in product(strata(M),repeat=2))
# Immediate refinement on singleton strata is equality; no nonempty proper
# sub-stratum exists. Equality is transitive.
interior_ref = lambda x,y: x==y
axioms["At7_transitivity_of_immediate_refinement"] = all(
    not(interior_ref(x,y) and interior_ref(y,z)) or interior_ref(x,z)
    for x,y,z in product(M,repeat=3))
axioms["L1_nonempty_interior_locus"] = all(any(interior_ref(y,x) for y in M) for x in M)
axioms["L2_orthogonality_detected_by_loci"] = all(
    disjoint(f,g)==all(orth(x,y) for x in f for y in g)
    for f,g in product(figures,repeat=2))
axioms["L3_distinct_compatible_strata_have_orthogonal_interior_loci"] = all(
    not(x!=y and compatible(frozenset([x]),frozenset([y]))) or orth(x,y)
    for x,y in product(M,repeat=2))
axioms["CLspac_criterion_on_strata"] = all(
    compatible(frozenset([x]),frozenset([y])) ==
    all(orth(u,v) for u in (frozenset([x])-frozenset([y])) for v in (frozenset([y])-frozenset([x])))
    for x,y in product(M,repeat=2))
axioms["D0_refinement_preserves_orthogonality"] = all(
    not(disjoint(f,g) and fp<=f and gp<=g) or disjoint(fp,gp)
    for f,g,fp,gp in product(figures,repeat=4))
# AtD in its restriction form, for compatible ambient figures.
axioms["D_restriction_disjointness"] = all(
    not(compatible(f,g) and fp<=f and gp<=g)
    or disjoint(fp,gp)==disjoint(fp&(f&g),gp&(f&g))
    for f,g,fp,gp in product(figures,repeat=4))
# AtC's sufficiency: exclusive refined pieces disjoint implies compatibility.
axioms["Cspac_exclusive_parts_criterion"] = all(
    not all(disjoint(fp,gp) for fp in figures for gp in figures
            if fp<=f and gp<=g and not(fp&(f&g)) and not(gp&(f&g)))
    or compatible(f,g)
    for f,g in product(figures,repeat=2))
# AtSupp (old At13) is automatic for an elementary singleton: F is empty or X.
axioms["AtSupp_witness_inside_ambient_stratum"] = all(
    not(f<=frozenset([x]) and any(disjoint(g,f) and not disjoint(g,frozenset([x])) for g in figures))
    or any(y==x and disjoint(frozenset([y]),f) for y in M)
    for x in M for f in figures)
assert all(axioms.values()), axioms
F0=frozenset(["A","B"])
A=F0
B=frozenset(["B"])
support_A=closure(A)
support_B=closure(B)
left=closure(A-B)
right=support_A & perp(support_B)
assert left==frozenset(["A"]) and right==frozenset(["A","B'"])
report["path_graph_local_support_counterexample"] = {
    "manuscript":"J156-7-12 scans94,97-100; L1 explicit J156-7-02 scan20 lines96-98",
    "model":"Figures are all cliques of A'--A--B--B'; both orders are inclusion; M=L consists of singleton figures.",
    "figures":[display(f) for f in figures],"all_axioms_exhaustively_checked":axioms,
    "L1_scope":"No strictness is inserted: a locus is an interior refinement of itself, since it has no proper nonempty sub-stratum.",
    "compatible_ambient_figure":display(F0),
    "closed_singletons_A_B":[display(closure(frozenset([x]))) for x in ["A","B"]],
    "support_A_union_B":display(support_A),
    "left_S_A_minus_B":display(left),"right_S_A_intersection_cosupp_S_B":display(right),
    "conclusion":"The relative complement formula remains false with At1-7, L1-3, Cspac, D, and AtSupp.",
    "limitation":"The model does not satisfy optional AtSupp1 absorption: closure({A'}) contains B. No refutation is claimed when that additional hypothesis is imposed."
}

# VI scan51: naive inverse images of closed strata need not remain admissible.
base=frozenset(["a","b","c"])
figure=[frozenset(["a"]),frozenset(["b"]),base]
domain=frozenset(["a","b"])
open_stratum=lambda s,f:s-frozenset().union(*(t for t in f if t<s))
admissible=lambda f: all(open_stratum(s,f) for s in f) and all(
    not any(p in s for s in f) or any(p in s and all(s<=t for t in f if p in t) for s in f)
    for p in frozenset().union(*f))
pullback=list(set(s&domain for s in figure if s&domain))
assert admissible(figure) and not admissible(pullback)
report["naive_figure_pullback_counterexample"]={
    "manuscript":"J156-6-07 scan51 lines51-56",
    "original_figure":[display(s) for s in figure],"original_admissible":True,
    "map":"inclusion {a,b} -> {a,b,c}","naive_nonempty_closed_preimages":[display(s) for s in pullback],
    "empty_open_strata":[display(s) for s in pullback if not open_stratum(s,pullback)],
    "conclusion":"Discarding only empty closed preimages does not produce a figure; discard empty open strata as an analyst's corrected construction."
}

# VI scan43: a lower family need not satisfy At3.
three=frozenset([0,1,2]); lower_family=[f for f in powerset(three) if len(f)<=2]
f=frozenset([0,1]);g=frozenset([1,2])
assert all(frozenset([x,y]) in lower_family for x in f for y in g)
assert f|g not in lower_family
report["lower_subfamily_At3_failure"]={
    "manuscript":"J156-6-05 scan38 corrected J156-6-06 scan43",
    "family":"all subsets of {0,1,2} of cardinality at most 2",
    "lower_and_nonempty":True,"F":display(f),"G":display(g),
    "all_cross_stratum_pairs_have_join":True,"F_G_have_no_upper_bound":True,
    "conclusion":"Sousat2 is essential; the manuscript itself adds it."
}

# VI scan50-51, corrected VII scan35: At8/L1 and equality of the two orders.
chain=[0,1]
minimal=[0]
interior=lambda x,y:x<=y and not any(x<=z<y for z in chain)
assert not any(interior(x,1) for x in minimal)
report["trivial_order_At8_counterexample"]={
    "manuscript":"J156-6-07 scans50-51 corrected J156-7-04 scan35 line100",
    "strata_poset":"0<1; both orders equal",
    "each_element_is_minimal_or_covers_a_minimal":True,
    "upper_stratum_has_interior_locus":False,
    "corrected_statement":"If both orders on M coincide, At8/L1 holds iff M is discrete."
}

# A finite grid illustrates the exact orthogonality closure calculation in VII83-84.
# In a dense total order, the corresponding open rectangles give the same
# analytic witness; this finite calculation is not offered as an atelier model.
grid=frozenset(product(range(5),repeat=2))
parallel=lambda p,q:(p[0]<q[0] and p[1]<q[1]) or (q[0]<p[0] and q[1]<p[1])
grid_perp=lambda s:frozenset(p for p in grid if all(parallel(p,q) for q in s))
grid_cl=lambda s:grid_perp(grid_perp(s))
z1=(1,3);z2=(3,1);z3=(2,2)
assert grid_cl({z1})==frozenset([z1]) and grid_cl({z2})==frozenset([z2])
join=grid_cl({z1,z2})
assert z3 in join
report["two_strand_grid_computation"]={
    "manuscript":"J156-7-10 scans82-84",
    "scope":"finite relation calculation, not verification of the geometric atelier or dense-order realization hypotheses",
    "z1":z1,"z2":z2,"z3":z3,"singleton_closures_are_singletons":True,
    "join":sorted(join),"z3_in_join":True,
    "distributivity_witness":"supp({z3}) meet (supp({z1}) join supp({z2})) contains z3; each separate meet is empty.",
    "important":"The manuscript marginally states the natural endpoint realization fails Supp1 (orthogonality iff disjoint supports)."
}

text=json.dumps(report,indent=2,ensure_ascii=False)
(OUT/'finite_checks_output.json').write_text(text+'\n')
print(text)
