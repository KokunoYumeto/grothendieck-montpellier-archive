"""Refresh promoted CP18 gates without altering actual historical reviews."""
from pathlib import Path
import subprocess, sys, json, re
w = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(w/'code/update_current17.py')], check=True, cwd=w)
def proved(relative):
    p = w/relative
    return p.exists() and '\\status{Candidate' not in p.read_text()
boundary = proved('agents/reduction_descent/B_tame_norm_square_boundary.tex')
orbits = proved('agents/reduction_descent/B_tame_primitive_norm_orbits.tex')
degree_two = proved('agents/monodromy/mixed_degree_two_uniform_full_groups.tex')
bundles = proved('agents/obstructions_crystals/A3_mixed_positive_index_bundles.tex')
radicals = proved('agents/obstructions_crystals/A3_mixed_positive_index_trace_radicals.tex')
rows = json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item'] == 'A.3' and bundles:
        row['where'] += '; lem:DE-A3-positive-two-bundles; lem:DE-A3-positive-determinant-curve; lem:DE-A3-positive-torsor-boundary'
        row['gate'] += ' The two toral rank2 bundles differ by the unique nontrivial geometric2-torsion Picard lineP, which is acyclic. A general sharp source yields a rank2 quotient with a line cokernel on a Cartier determinant curveD of genusb+1; the line has degreeb=g-1, including nonreducedD. The contraction boundary of an actual etale trace lift is the ordinary torsor class. These exact bundle statements do not prove the missing residue pairing nonzero.'
    if row['item'] == 'A.3' and radicals:
        row['where'] += '; lem:DE-A3-positive-trace-radical; lem:DE-A3-positive-matrix-ruling'
        row['gate'] += ' The descended variation also kills the two toral trace directions R=span(s,es), so its exact domain is W/R. Its determinant vanishes identically exactly when its matrix space has a common kernel line or a common image line. Neither exclusion is established uniformly.'
    if row['item'] == 'A.4' and degree_two:
        row['status'] = 'OPEN generally; all nonordinary ppav generic moduli in every degree, and every fixed mixed product in degrees one and two'
        row['where'] += '; thm:mixed-every-fixed-modulus-degree-two-candidate; lem:mixed-degree-two-common-grid-candidate'
        row['gate'] = row['gate'].replace('The remaining fixed mixed-product group gate starts at degree2; higher-degree uniform groups and arbitrary-X structural classification remain open.', 'The degree-one result is now supplemented by the uniform degree-two theorem below; arbitrary-X structural classification remains open.')
        row['gate'] += ' For every fixed ordinary modulus in degree2, the geometric and arithmetic group is Hom(F2²,F2^32) semidirect GL32(F2), the full pointwise stabilizer of the two invariant covectors. Their common32-dimensional kernel is irreducible and lies in every nonzero invariant subspace. The labelled-intersection sum-zero wreath group supplies all nodal gluing translations, and two opposite-Picard-twist decompositions of one K6,6 elliptic grid force irreducibility through its finite Lang part of rank30. No full-fibre specialization across the34-to30 rank drop is used. The remaining fixed mixed-product degree gate begins at3.'
    if row['item'] == 'B.4' and boundary:
        row['where'] += '; lem:B-RD50-boundary; prop:B-RD50-square; cor:B-RD50-remaining'
        row['gate'] += ' The closed coefficientwise logarithm bound excludes all square common finite determinants, including joint degree p+1. Every remaining p² comparison has nonsquare finite determinant; a simultaneous finite twist normalizes its value to primitive order p-1. Its normalized joint tame degree is then (p²-1)/d for d an odd divisor of p+1. No analytic convergence at the logarithm boundary or source-to-quotient Hasse thickness is assumed.'
        if orbits:
            row['where'] += '; lem:B-RD51-orbits; cor:B-RD51-p5'
            row['gate'] += ' The exact primitive-norm fibre has q/2 Frobenius orbits, where q=(p+1)/d, so q>=4 is necessary for unequal characters. At p5 only joint degree24 remains, with two unordered patterns up to common quadratic twist: individual degrees24/8, or opposite quadratic twists of an order24 type. These are necessary character restrictions, not constructions of a remaining congruent pair; the least index still lies in{1,2}.'
(w/'notes/item_status.json').write_text(json.dumps(rows, indent=2)+'\n')
root = json.loads((w/'notes/root_results.json').read_text())
aux = (w/'RESEARCH_SA15_paper.aux').read_text()
nums = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
idmap = {r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table = '| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table += '\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p = w/'RESEARCH_SA15_report.md'
old = p.read_text()
body = old[old.index('# RESEARCH_SA15 research report'):]
marker = '\n## Checkpoint 18 work: the remaining tame characters and fixed mixed-product monodromy\n'
if marker in body:
    body = body.split(marker)[0]
notes = w/'notes/checkpoint18_changes.md'
if notes.exists():
    body += marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP18 proved gates refreshed:', {'closed_logarithm_square_exclusion':boundary,'primitive_norm_character_list':orbits,'every_fixed_mixed_degree_two':degree_two,'positive_index_bundles':bundles,'trace_radicals':radicals})
