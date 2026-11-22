"""Refresh only promoted CP17 gates; retain the actual historical review ledger."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current16.py')],check=True,cwd=w)
def proved(relative):
    p=w/relative
    return p.exists() and '\\status{Candidate' not in p.read_text()
ppav=proved('agents/monodromy/generic_nonordinary_ppav_groups.tex')
variation=proved('agents/obstructions_crystals/A3_mixed_positive_index_variation.tex')
tame=proved('agents/reduction_descent/B_tame_minimal_height_two.tex')
fixed=proved('agents/monodromy/mixed_degree_one_uniform_full_groups.tex')
assert ppav and variation and tame
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.3':
        row['where']+='; lem:DE-A3-positive-index-image-candidate; lem:DE-A3-positive-index-double-corank-candidate'
        row['gate']+=' The positive-index toral lattice I=ann(s,es) has rank b-2 and degree-b Frobenius determinant. At an etale double pullback of a sharp positive-index source, the restricted first and stable ranks equal b-4. The exact remaining sufficient deformation test is nonvanishing of a 2-by-2 first-variation determinant on the trace quotient of sections. No general nonvanishing theorem is claimed; the full coherent first rank need not equal b-4.'
    elif row['item']=='A.4':
        row['status']='OPEN generally; all nonordinary ppav geometric generic moduli solved in every degree'
        row['where']+='; thm:generic-nonordinary-ppav-groups-candidate; cor:generic-nonordinary-ppav-finite-degrees-candidate'
        row['gate']+=' For every degree at a geometric generic point of the p-rank-one ppav-surface stratum, and of each p-rank-zero component, the odd image is GL_(9d²-1)(F2) and the even image is the full stabilizer of f+1 invariant covectors: Hom(F2^(f+1),F2^(9d²-4)) semidirect GL_(9d²-4), on rank 9d²-3+f. Perfect-field arithmetic images agree. Each finite prescribed set of degrees has a nonempty open and actual finite-field examples; no single finite-field point in a countable intersection is inferred.'
        if fixed:
            row['status']='OPEN generally; all nonordinary ppav generic moduli in every degree, and every fixed mixed product in degree one'
            row['where']+='; thm:mixed-every-fixed-modulus-degree-one-candidate'
            row['gate']+=' For every ordinary elliptic E and supersingular elliptic Eprime over every perfect characteristic-two field, the (3,3) system on E times Eprime has rank8 and geometric=arithmetic GL8(F2), including every algebraic ordinary modulus. The proof uses the uniform smooth Frobenius Gram map to bound the exceptional Lang incidence and seven independent Artin-Schreier inertia directions, followed by elementary-matrix generation. The remaining fixed mixed-product group gate starts at degree2; higher-degree uniform groups and arbitrary-X structural classification remain open.'
    elif row['item']=='B.4':
        row['status']='OPEN generally; exact minimal dyadic/triadic height-two indices, and 1<=nu_min(p,p-1,2)<=2 for p>=5'
        row['where']+='; thm:B-RD49; prop:B-RD49-mixed; lem:B-RD49-point'
        row['gate']+=' For every p>=5 at e=p-1 and height2, 1<=nu_min<=2: p³-torsion suffices. Every possible p² ambiguity must compare two whole potentially supersingular groups, with equal finite determinant characters and joint faithful tame degree m dividing p²-1 but m>p. The mixed formal/height-one-filtered case is excluded by a rational p²-point valuation contradiction. No existence or exact least index within this interval is asserted.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 17 work: generic nonordinary surfaces and uniform mixed degree one\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint17_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP17 proved gates refreshed:',{'generic_nonordinary_ppav':ppav,'positive_index_variation':variation,'tame_height_two':tame,'all_fixed_mixed_degree1':fixed})
