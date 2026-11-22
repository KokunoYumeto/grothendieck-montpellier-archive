"""Current post-CP15 proved gates; candidates never silently advance a row."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
def proved(relative):
    p=w/relative
    return p.exists() and '\\status{Candidate' not in p.read_text()
thin=proved('agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex')
even=proved('agents/monodromy/supersingular_all_even_groups.tex') and proved('agents/monodromy/supersingular_even_image_sheaf.tex')
log=proved('agents/reduction_descent/B_p2_height_two_log_gate.tex')
residual=proved('agents/reduction_descent/B_p2_residual_trivial_gate.tex') and proved('agents/reduction_descent/B_p2_residual_c2_gate.tex')
positive=proved('agents/obstructions_crystals/A3_mixed_positive_index_bounds.tex')
generic=proved('agents/monodromy/generic_mixed_product_all_groups.tex')
dyadic=proved('agents/reduction_descent/B_p2_residual_c3_final.tex')
assert thin and even and log, 'Do not refresh proved gates before promotion.'
changes={
 'A.3':('OPEN generally; every elliptic product in characteristic two now has structural ranks in every degree',
 'cor:DE-A3-mixed-product-no-exception; thm:DE-A3-mixed-thin-all; thm:DE-A3-mixed-nonproduct-ranks; thm:DE-A3-ordinary-arbitrary-embedding; thm:DE-A3-all-ss-rectangles',
 'For every perfect characteristic-two field, all positivea,b,d and every ordinary/supersingular pair, the mixed product relative rank is9abd²−1−epsilon(ad), with no thin-system or modulus exception. The uniform residue proof establishes stable rank by the exact Frobenius-semilinear kernel-to-cokernel test and two independent evaluation isomorphisms. Every ordinary abelian surface and ampleM has rankchi(M)n²−1 for n>=3. Supersingular elliptic products have rank9abd²−1−epsilon(ad)−epsilon(bd). Mixed nonproduct classes with ordinary polarization indexa(M)=0 have ranks9chi(M)d²−1 odd and9chi(M)d²−2 even for L=M³. Explicit ambient restriction bounds persist. General nonproduct mixed classes witha(M)>0, other inseparable nonordinary types and arbitrary-X structural ranks remain open.'),
 'A.4':('OPEN generally; fixed supersingular product has full geometric and arithmetic groups in every degree',
 'thm:ss-product-all-full-groups; thm:ss-even-unit-Hasse-irreducible; thm:ss-even-full-group-if-unit-Hasse-irreducible; thm:ss-all-odd-full-groups; thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors',
 'For E:y²+y=x³, X=E² and L=O(3O)boxtimesO(3O), over any perfect characteristic-two base field, every oddd>=1 has geometric=arithmetic imageGL_(9d²−1)(F2). Every evend>=2 has the full stabilizer of its unique invariant covector, F2^(9d²−4) semidirectGL_(9d²−4)(F2), acting on rank9d²−3. The even first-image sheaf and its unique codimension-one invariant subspace are identified. Two odd boundary decompositions, together with the reduced intersection-Hasse divisor, prove irreducibility of the even unit-Hasse divisor for alld>=4; degree2 is the earlier exact case. All projective-space and ordinary principal-surface results persist. General-X structural monodromy and every-fixed-modulus mixed product monodromy remain open.'),
 'B.4':('OPEN generally; exact nu_min(3,2,2)=2 and3<=nu_min(2,1,2)<=7',
 'thm:B-RD42; prop:B-RD43; prop:B-RD44; thm:B-RD45'+('; prop:B-RD46; prop:B-RD47' if residual else '')+'; prop:B-RD30; prop:B-RD22',
 'At p3,e2,height2 the exact least manuscript index is2:27-torsion determines the prime-to-three character and the explicit9-torsion counterexample is sharp. At p2,e1,height2,8-torsion fails and256-torsion suffices, so3<=nu_min<=7. Every remaining level16 comparison is between two exact potentially supersingular elliptic BT groups, with joint good-reduction degree24,48,96,or192. At levels32,64,128 these lists shrink to48/96/192,96/192,and192.'+(' Trivial andC2 common residual inertia are excluded; onlyC3 remains at16.' if residual else ' The separate trivial/C2 residual exclusions are undergoing companion audits.')+' In particular16-torsion sufficiency remains undecided. Height one has least index0; general explicit bounds persist, but the general least-index formula remains open.')}
for row in rows:
    if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
    if row['item']=='A.3' and positive:
        row['where']+='; thm:DE-A3-positive-index-bounds'
        row['gate']=row['gate'].replace('General nonproduct mixed classes witha(M)>0, other inseparable nonordinary types and arbitrary-X structural ranks remain open.', 'For every positive ordinary index a=a(M), write D=chi(M). Odd-degree ranks lie between9Dd²-2^a and9Dd²-2, and even-degree ranks between9Dd²-2^(a+1) and9Dd²-2. Thus a=1 and oddd have exact rank9Dd²-2. Sharp ranks remain open for nonproduct classes witha>=2 in odd degree and everya>0 in even degree, other inseparable nonordinary types, and arbitraryX.')
    if row['item']=='A.4' and generic:
        row['status']='OPEN generally; all degrees solved for the fixed supersingular product and the generic ordinary/supersingular product'
        row['where']+='; thm:generic-mixed-product-all-groups-candidate'
        row['gate']=row['gate'].replace('General-X structural monodromy and every-fixed-modulus mixed product monodromy remain open.', 'For E ordinary with j transcendental over F2 and X=E times E_ss, every oddd has geometric=arithmetic GL_(9d²-1); every evend has the full two-covector stabilizer Hom(F2²,F2^(9d²-4)) semidirectGL_(9d²-4), acting in rank9d²-2. The generic-fibre image is normal in the total arithmetic family image, so two exact finite-field coefficient points prove the degree2 geometric generic result without reversed specialization. General-X structural monodromy and fixed algebraic ordinary-modulus mixed-product monodromy remain open.')
    if row['item']=='B.4' and dyadic:
        row['status']='OPEN generally; exact nu_min(3,2,2)=2 and nu_min(2,1,2)=3'
        row['where']='thm:B-RD48; prop:B-RD48; prop:B-RD43; thm:B-RD42; prop:B-RD30; prop:B-RD22'
        row['gate']='At p3,e2,height2 the exact least manuscript index is2:27-torsion determines the prime-to-three inertia character and the explicit9-torsion counterexample is sharp. At p2,e1,height2 the exact least index is3:16-torsion determines the prime-to-two character, while the explicit8-torsion ambiguity is sharp. Within the potentially supersingular elliptic subclass,8-torsion already suffices; the general height-two16 reduction and all residual1,C2,C3 branches are proved. The finalC3 proof uses the actual marked8-congruence models and exhaustiveness over arbitrary characteristic-zero fields, including exceptional j. Height one has least index0. General explicit bounds persist, but the least-index formula for other ramification indices and heights remains open.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text() if (w/'RESEARCH_SA15_paper.aux').exists() else ''
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 16 work: all supersingular-product groups and all mixed-product ranks\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint16_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP16 gates refreshed:',{'residual':residual,'positive_index':positive,'generic_mixed':generic,'dyadic_exact':dyadic},'; actual historical reviews untouched.')
