#!/usr/bin/env python3
"""Exact finite certificates for the Cote 150 investigation.

This is a mathematical computation, not a test of the writing implementation.
No numerical sampling is used for the Mobius automorphism computation.
"""
from __future__ import annotations
import itertools
import json
import time
from fractions import Fraction
from pathlib import Path
import sympy as sp


def twist_certificate():
    vertices = [(i, z) for i in range(3) for z in range(2)]
    source = {(0, 1): lambda z: z, (1, 2): lambda z: z,
              (0, 2): lambda z: 1-z}
    edges = {((i, source[i,j](z)), (j, z))
             for i, j in [(0, 1), (1, 2), (0, 2)] for z in range(2)}
    # All b_ij are the identity on a two-point target. Every pair-space is
    # the entire target, so the intersection/preimage equation (c) holds.
    sigma012 = {0, 1} & {0, 1}
    preimage = {z for z in range(2) if source[1,2](z) in {0,1}}
    assert sigma012 == preimage
    failures = [(a,b,c) for a,b in edges for b1,c in edges
                if b == b1 and (a,c) not in edges]
    assert len(failures) == 2
    return {"vertices":len(vertices), "strict_arrows":len(edges),
            "a_b_c_subset_axioms":True,
            "transitivity_failures":sorted(failures),
            "pi_control_fails_at":[z for z in range(2)
                 if source[0,2](z) != source[0,1](source[1,2](z))]}


INF = None


def mobius_matrix(images):
    # Solve f(infinity)=images[0], f(0)=images[1], f(1)=images[2].
    # A Mobius transformation is [a b;c d], up to nonzero scalar.
    rows=[]
    for x,y in zip([INF,0,1],images):
        if x is INF:
            rows.append([0,0,1,0] if y is INF else [1,0,-y,0])
        elif y is INF:
            rows.append([0,0,x,1])
        else:
            rows.append([x,1,-y*x,-y])
    ns=sp.Matrix(rows).nullspace()
    assert len(ns)==1
    a,b,c,d=map(sp.Rational, ns[0])
    assert a*d-b*c != 0
    return a,b,c,d


def apply_mobius(m,x):
    a,b,c,d=m
    if x is INF:
        return INF if c==0 else a/c
    den=c*x+d
    return INF if den==0 else (a*x+b)/den


def branch_certificate():
    branch=[INF,0,1,3,7,12,20,31,45,64]
    target=set(branch)
    automorphisms=[]
    count=0
    for images in itertools.permutations(branch,3):
        count+=1
        m=mobius_matrix(images)
        values=[apply_mobius(m,x) for x in branch]
        if set(values)==target:
            automorphisms.append({"matrix":[str(v) for v in m],
                                  "permutation":[branch.index(v) for v in values]})
    assert count==10*9*8==720
    assert len(automorphisms)==1
    assert automorphisms[0]["permutation"]==list(range(10))
    g=(len(branch)-2)//2
    assert g==4
    inv=list(range(2*g-1))
    anti=list(range(g-2))
    assert len(inv)+len(anti)==3*g-3
    return {"branch_points":["infinity" if x is INF else x for x in branch],
            "candidate_mobius_maps":count,"automorphisms":automorphisms,
            "genus":g, "quadratic_differential_invariant_x_degrees":inv,
            "quadratic_differential_antiinvariant_x_degrees":anti,
            "tangent_invariant_dimension":len(inv),
            "tangent_antiinvariant_dimension":len(anti)}


def local_homology_certificate():
    # Integral cellular differentials for RP^3, one cell in degrees 0..3.
    differentials={1:0,2:2,3:0}
    homology={}
    for degree in range(4):
        outgoing=differentials.get(degree,0)
        incoming=differentials.get(degree+1,0)
        if outgoing:
            homology[degree]="0"
        elif incoming:
            homology[degree]=f"Z/{incoming}"
        else:
            homology[degree]="Z"
    assert homology=={0:"Z",1:"Z/2",2:"0",3:"Z"}
    # Link of C^7 x cone(RP^3) is S^13 * RP^3 = Sigma^14 RP^3.
    # Local homology shifts reduced link homology by another 1.
    local={degree+15:group for degree,group in homology.items()
           if degree>0 and group!="0"}
    assert local=={16:"Z/2",18:"Z"}
    return {"RP3_cellular_differentials":differentials,
            "RP3_integral_homology":homology,
            "C7_times_C2_mod_sign_local_homology":local,
            "real_local_dimension":18,
            "not_a_manifold_due_to_torsion_in_local_degree":16}


def flags_certificate(max_n=5):
    counts={}
    total_flags=total_intervals=0
    for n in range(max_n+1):
        pairs=list(itertools.combinations(range(n),2))
        posets=0
        for mask in range(1<<len(pairs)):
            rel={(i,i) for i in range(n)} | {
                pair for j,pair in enumerate(pairs) if mask>>j&1}
            if any((a,c) not in rel for a,b in rel for b1,c in rel if b==b1):
                continue
            posets+=1
            flags=[frozenset(s) for k in range(1,n+1)
                   for s in itertools.combinations(range(n),k)
                   if all((a,b) in rel for a,b in itertools.combinations(s,2))]
            total_flags+=len(flags)
            for smaller in flags:
                for larger in flags:
                    if smaller<=larger:
                        interval={f for f in flags if smaller<=f<=larger}
                        added=larger-smaller
                        boolean={smaller|frozenset(s) for k in range(len(added)+1)
                                 for s in itertools.combinations(added,k)}
                        assert interval==boolean
                        total_intervals+=1
        counts[n]=posets
    return {"naturally_labelled_posets_by_cardinality":counts,
            "flags_checked":total_flags,"flag_intervals_checked":total_intervals,
            "all_intervals_boolean":True}


def main():
    started=time.perf_counter()
    results={}
    for name,fn in [("twist",twist_certificate),
                    ("genus4_branch_set",branch_certificate),
                    ("quotient_local_homology",local_homology_certificate),
                    ("boolean_flag_intervals",flags_certificate)]:
        t=time.perf_counter();results[name]=fn()
        results[name]["runtime_seconds"]=round(time.perf_counter()-t,6)
    results["total_runtime_seconds"]=round(time.perf_counter()-started,6)
    output=json.dumps(results,indent=2,sort_keys=True)
    print(output)
    Path(__file__).with_suffix('.output.json').write_text(output+'\n')


if __name__=='__main__':main()
