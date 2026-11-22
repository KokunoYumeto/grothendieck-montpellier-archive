"""Refresh CP20 proved gates only, without altering actual historical reviews."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current19.py')],check=True,cwd=w)
def proved(relative):
    p=w/relative
    return p.exists() and '\\status{Candidate' not in p.read_text()
odd=proved('agents/monodromy/mixed_all_odd_norm_groups.tex')
even=proved('agents/monodromy/mixed_all_even_groups.tex')
b55=proved('agents/reduction_descent/B_tame_minimal_wild_layer.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.4' and odd:
        row['where']+='; thm:mixed-every-fixed-modulus-all-odd-candidate; lem:mixed-odd-common-graph-candidate'
        row['status']='OPEN generally; every odd balanced degree on every fixed mixed product is classified'
        row['gate']='All projective-space cases and the proved effective ordinary principal-surface results persist. For the proved supersingular product family in characteristic two, every odd d has both images GL_(9d²-1)(F2), and every even d has F2^(9d²-4) semidirect GL_(9d²-4), acting in rank 9d²-3. For every fixed ordinary/supersingular elliptic pair over any perfect characteristic-two field, every odd balanced degree d has geometric and arithmetic image GL_(9d²-1)(F2). The proof supplies independent S_(18d) node factors, an actual GL_(9d-1) normalization block and all type-heart shears. The anchored-loop graph proof works for every odd kernel; it is not extrapolated from finite tests. Every mixed strip of factor degrees (3,b), b>=3, also has exact images: GL_(3b-1) for odd b, and F2^(3b-2) semidirect GL_(3b-2) for even b. The geometric generic point of every nonordinary ppav-surface stratum has the exact groups in every degree; a finite prescribed set of degrees has a common nonempty open and actual finite-field examples, without a countable-intersection assertion. The unresolved gates are even balanced fixed mixed-product degrees d>=4, fixed nongeneric nonordinary nonproduct ppav surfaces, and the structural classification for arbitrary X.'
    if row['item']=='A.4' and even:
        row['where']+='; thm:mixed-every-fixed-modulus-all-even-candidate; cor:mixed-every-fixed-modulus-all-degrees-candidate'
        row['status']='OPEN generally; exact images in every balanced degree on every fixed mixed elliptic product'
        row['gate']=row['gate'].replace('The unresolved gates are even balanced fixed mixed-product degrees d>=4, fixed nongeneric nonordinary nonproduct ppav surfaces, and the structural classification for arbitrary X.','The even balanced fixed mixed-product degrees are also all closed: geometric and arithmetic image Hom(F2²,F2^(9d²-4)) semidirect GL_(9d²-4), the full pointwise stabilizer of the two invariant covectors, acting in rank 9d²-2. Their common kernel is irreducible and lies in every nonzero invariant subspace. Unequal odd-component lifted wreath groups supply actual blocks and all gluing translations; two opposite-twist grid decompositions force irreducibility through the finite Lang part of rank 9d²-3d, with no full-fibre identification across the rank drop. Thus every balanced degree on every fixed mixed product is classified. Fixed nongeneric nonordinary nonproduct ppav surfaces and the structural classification for arbitrary X remain open.')
    if row['item']=='B.4' and b55:
        row['where']+='; lem:B-RD55-valuations; prop:B-RD55-minimal-wild'
        row['gate']+=' In the irreducible-residual branch, the common second-level wild image has order p², p³ or p⁴; order p² cannot hide different special characters, without any CM hypothesis. At minimal order every primitive coordinate has valuation p-1 in the common division field, so one exact ramification coefficient identifies both wild matrix spaces with the same scalar F_(p²); the required Frobenius-semilinear orientation would make Frobenius scalar. Thus the remaining irreducible-residual wild orders are p³ and p⁴, namely 125 and 625 at p=5. Reducible residual cases and both larger wild orders remain unresolved.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text());aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 20 work: all balanced mixed-product degrees\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint20_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP20 proved gates refreshed:',{'all_odd_fixed_mixed':odd,'all_even_fixed_mixed':even,'minimal_wild_exclusion':b55})
