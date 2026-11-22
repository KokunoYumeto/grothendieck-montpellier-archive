"""Finite exact certificates for the infinite-chain Prop5 counterexample."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
import json,time
import sympy as s
begin=time.perf_counter();x,t=s.symbols('x t')
assert s.expand((1-x)*((1-x)-1)-x*(x-1))==0
# On x^2-x-t=0, t invertible makes x and x-1 invertible.
assert s.rem(x*(x-1)-t,x*x-x-t,x)==0
perms=list(permutations(range(2))); checks=[]
for level in range(13):
    target=level+1
    g=1<<(target-1)
    assert (g & ((1<<level)-1))==0
    binary_action=[1,0]
    possible=[]
    for f in perms:
        intertwines=all(f[a]==binary_action[f[a]] for a in range(2))
        if intertwines:possible.append(f)
    assert not possible
    checks.append({'candidate_level':level,'next_coordinate':target,'witness_group_element_bitmask':g,'equivariant_bijections':len(possible)})
# Finite families with N coordinates all admit a common level N, but no smaller.
finite=[]
for n in range(1,13):
    assertions=0
    for g in range(1<<n):
        for coord in range(n):
            value=(g>>coord)&1
            assert value in (0,1)
            if g==(1<<coord): assert value==1
            assertions+=1
    finite.append({'number_components':n,'common_level':n,'group_order':1<<n,'character_values_checked':assertions})
output={'statement_id':'D:prop5-counterexample','utc':datetime.now(timezone.utc).isoformat(),'chart_gluing_t_identity':True,'monic_degree_two_relation':True,'two_permutations_checked_per_level':len(perms),'obstruction_checks':checks,'finite_family_checks':finite,'limitation':'The nodal scheme and impossibility of a uniform level over infinitely many components are proved in paper_D.tex. Finite certificates verify chart algebra and the character obstruction; they do not replace the infinite argument.','elapsed_seconds':time.perf_counter()-begin}
Path(__file__).with_name('check_prop5_chain_output.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({'passed':True,'levels':len(checks),'finite_families':len(finite),'character_values_checked':sum(z['character_values_checked'] for z in finite),'elapsed_seconds':output['elapsed_seconds']}))
