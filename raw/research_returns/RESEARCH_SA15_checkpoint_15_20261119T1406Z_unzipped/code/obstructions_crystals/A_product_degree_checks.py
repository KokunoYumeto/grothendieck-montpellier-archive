"""Exact bound and finite-module checks for the product degree theorem."""
from pathlib import Path
import json
import time

started=time.perf_counter()

def ceil_div(a,b):
    return -((-a)//b)

rows=[]
for p in (2,3,5,7,11,13,17,19,23,29,31):
    D=p*p-p
    E=p+1
    assert 2*D>=E
    boundary=[]
    for i in range(p+1):
        m=ceil_div(p*(E+i),p+1)
        rel=p-m
        base=p*i-E
        boundary.append((rel,base))
        if i==0:
            assert (rel,base)==(0,-E)
        else:
            assert rel<0
        assert p*i-D-(p+1)<=-1
        assert p-ceil_div(p*(E+1+i),p+1)<0
    rows.append({"p":p,"negative_H1_threshold":D,
                 "negative_differential_threshold":E,
                 "product_saturation_bound":D,
                 "boundary_log_terms":boundary})
assert rows[0]["product_saturation_bound"]==2

# Finite cyclic p-primary modules: check all homomorphisms in a small exact
# range, retaining all conditions needed by the written Tor argument.
module_checks=0
for p in (2,3):
    for a in range(4):
        for b in range(4):
            M=p**a
            N=p**b
            for c in range(N):
                if (M*c)%N:
                    continue
                image={(c*x)%N for x in range(M)}
                injective=len(image)==M
                Mp={x for x in range(M) if (p*x)%M==0}
                Np={y for y in range(N) if (p*y)%N==0}
                torsion_surjective={(c*x)%N for x in Mp}==Np
                pM={(p*x)%M for x in range(M)}
                pN={(p*y)%N for y in range(N)}
                modp_injective=all(x in pM for x in range(M) if (c*x)%N in pN)
                if injective and torsion_surjective and modp_injective:
                    assert len(image)==N
                module_checks+=1

# The three separate shortcuts really fail; these are exact finite witnesses.
def finite_map(p,a,b,c):
    M,N=p**a,p**b
    image={(c*x)%N for x in range(M)}
    Mp={x for x in range(M) if p*x%M==0}
    Np={y for y in range(N) if p*y%N==0}
    pM={p*x%M for x in range(M)}
    pN={p*y%N for y in range(N)}
    return {"injective":len(image)==M,
            "modp_injective":all(x in pM for x in range(M) if c*x%N in pN),
            "p_torsion_surjective":{c*x%N for x in Mp}==Np,
            "cokernel_order":N//len(image)}

counterexamples={
    "reduction_W4_to_W2":finite_map(2,2,1,1),
    "inclusion_W2_to_W4_by2":finite_map(2,1,2,2),
    "zero_to_W2":finite_map(2,0,1,0),
}
assert counterexamples["reduction_W4_to_W2"]["modp_injective"]
assert not counterexamples["reduction_W4_to_W2"]["injective"]
assert counterexamples["inclusion_W2_to_W4_by2"]["p_torsion_surjective"]
assert counterexamples["inclusion_W2_to_W4_by2"]["cokernel_order"]==2
assert counterexamples["zero_to_W2"]["injective"]
assert counterexamples["zero_to_W2"]["modp_injective"]
assert not counterexamples["zero_to_W2"]["p_torsion_surjective"]

result={"status":"PASS","all_prime_bound_samples":rows,
        "finite_module_homomorphisms_checked":module_checks,
        "unsafe_shortcut_counterexamples":counterexamples,
        "characteristic_two_exact_ranges":{
            "integral_H2_injective":"all d>=1",
            "torsionfree_cokernel":"exactly d>=2",
            "torsion_isomorphism":"exactly d>=2"},
        "scope":"Computations check arithmetic and finite-module cautions; the geometric theorem is proved in A_product_degrees.tex.",
        "elapsed_seconds":time.perf_counter()-started}
out=Path(__file__).with_name("A_product_degree_checks_output.json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="all_prime_bound_samples"},indent=2))
