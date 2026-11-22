"""Current proved gates after CP14; candidate files do not silently advance rows."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
thin_files=[w/'sections/A_mixed_six_three_seed.tex',w/'agents/obstructions_crystals/A3_mixed_axis_norms.tex']
thin=all(p.exists() and '\\status{Candidate' not in p.read_text() for p in thin_files)
a3_extra=(' The universal mixed(6,3) seed and corrected odd supersingular-axis norm transfer now also prove the degree-one thin-strip formula for a congruent2mod4,b1; only4|a remains in that strip.' if thin else ' The mixed degree-one strip a even,b1 remains a separate gate; a universal(6,3) seed and corrected odd-axis transfer are written and being audited.')
changes={
 'A.3':('OPEN generally; all ordinary embeddings, all supersingular products and mixed ordinary-index-zero classes have structural ranks',
 'thm:DE-A3-mixed-nonproduct-ranks; thm:DE-A3-ordinary-arbitrary-embedding; thm:DE-A3-all-ss-rectangles; thm:DE-A3-mixed-all-product-ranks'+('; lem:root-mixed-six-three-cartier; cor:DE-A3-mixed-thin-vone' if thin else ''),
 'Every ordinary characteristic-two abelian surface and ample M has generic relative rank chi(M)n²−1 for n>=3. For L=M³ on E_ss², product type(a,b), the rank is9abd²−1−epsilon(ad)−epsilon(bd) for everyd>=1. On E_ord×E_ss the rank is9abd²−1−epsilon(ad) for d>=2 and for d1 if a odd or b>=2. Every mixed surface with ordinary polarization index a(M)=0 has ranks9chi(M)d²−1 odd and9chi(M)d²−2 even, without a product hypothesis. Explicit ambient bounds persist.'+a3_extra+' General nonproduct mixed classes with a(M)>0, other inseparable nonordinary types and arbitrary-X structural ranks remain open.'),
 'A.4':('OPEN generally; fixed supersingular product has full geometric/arithmetic GL in every odd degree',
 'thm:ss-all-odd-full-groups; thm:ss-all-odd-Hasse; prop:ss-uniform-tangent-triple; prop:ss-uniform-graph-mixed-contact; thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors',
 'For E:y²+y=x³ in characteristic2, X=E² with L=O(3O)boxtimesO(3O), every oddd>=1 has geometric=arithmetic image GL_(9d²−1)(F2), over any perfect base field. For oddd>=3 the relative Hasse divisor is geometrically irreducible/reduced and has generic stable rank loss1. Uniform mixed contacts and tangent triples now exclude all unwanted collisions for every finite odd graph kernel; exact D² multiplicity and norm pullback degree d²>6 complete component allocation. The uniform even-degree image for this product remains open beyond degree2, despite its exact one-covector constraint and actualGL8 block. General-X structural monodromy remains open; all previous projective-space, ordinary principal-surface and invariant-quotient results persist.'),
 'B.4':('OPEN generally; exact nu_min(3,2,2)=2 and dyadic8-torsion insufficiency are proved',
 'thm:B-RD42; prop:B-RD43; prop:B-RD41; prop:B-RD29; prop:B-RD30; prop:B-RD22',
 'At p3,e2,height2 the exact least manuscript index is2:27-torsion determines the prime-to-three character and the explicit9-torsion counterexample is sharp. At p2, every3 not dividing e and h>=2 now has nu_min>=3: an explicit potentially supersingular elliptic quotient and a Tate group have isomorphic8-torsion but different special-inertia characters. In particular8-torsion fails already at e1,height2;16-torsion sufficiency remains undecided. Height one has least index0. General explicit upper/lower bounds persist, but the general least-index formula remains open.')}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
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
marker='\n## Checkpoint 15 work: all odd supersingular-product groups\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint15_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current post-CP14 gates updated; thin-strip promotion:',thin,'; historical reviews untouched.')
