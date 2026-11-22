"""Maintain post-CP13 current gates; historical checkpoints/reviews are immutable."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':(
 'OPEN generally; structural ranks include ordinary surfaces, all product polarizations and mixed ordinary-index-zero classes',
 'thm:DE-A3-mixed-nonproduct-ranks; thm:DE-A3-ordinary-arbitrary-embedding; thm:DE-A3-all-ss-rectangles; thm:DE-A3-mixed-all-product-ranks; thm:DE-A3-separable-ranks; thm:all-X-explicit-positive-rank',
 'Every ordinary characteristic-two abelian surface and ample M has generic relative rank chi(M)n²−1 in |M^n| for n>=3, with explicit ambient bound. For L=M³ on E_ss² and product type(a,b), the rank is9abd²−1−epsilon(ad)−epsilon(bd) for all d>=1. On E_ord×E_ss it is9abd²−1−epsilon(ad) for d>=2, and for d1 if a is odd or b>=2. Any mixed surface with ordinary polarization index a(M)=0 now has ranks9chi(M)d²−1 for odd d and9chi(M)d²−2 for even d, with no parity restriction on chi(M) and no product hypothesis. All embeddings retain explicit regularity bounds. The mixed thin strip d1,a even,b1, general nonproduct mixed classes with a(M)>0, other inseparable nonordinary polarization types and arbitrary-X structural ranks remain open.'),
'A.4':(
 'OPEN: uniform mixed-contact norm witnesses proved; uniform tangent-triple bridges and general images remain unresolved',
 'prop:ss-uniform-graph-mixed-contact; cor:ss-degree3-hasse-irreducible; lem:ss-uniform-source-smoothness; thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors',
 'All previously proved projective-space groups, ordinary principal-surface eventual full groups, nonordinary principal-surface invariant quotients and supersingular-product groups in degrees1–3 remain. The degree-three relative Hasse divisor on the fixed supersingular product is geometrically irreducible and reduced. For every finite odd graph kernel and every nonzero difference, a globally smooth source on the Hasse cubic now has exactly one mixed self-tacnode in its norm image, unequal Cartier-kernel values, and otherwise only nodes; all unwanted pair/triple collisions are excluded uniformly, including the order-three flex case. The remaining uniform norm-family gate is construction of tangent-triple bridges. No higher-degree full-group conclusion is inferred; arbitrary-X structural monodromy remains open.'),
'B.4':(
 'OPEN generally; exact least index nu_min(3,2,2)=2 is proved',
 'thm:B-RD42; prop:B-RD41; prop:B-RD40; prop:B-RD29; prop:B-RD30; prop:B-RD22',
 'The full permitted height-two class at p=3,e=2 has exact least manuscript index2:27-torsion determines the prime-to-three character and the explicit9-torsion counterexample is sharp. The final antisymplectic C4 pair is normalized to M_b and a pi-twist M_b-prime; its reverse marked cocycle forces equal cubic good fields, contradicting necessary joint inertia18. Height one has least index0, and general explicit logarithmic upper and wild/tame lower bounds remain proved. The general least-index formula is unresolved. A remaining smallest-characteristic test is p=2,e=1,h=2:4-torsion fails by B22, and8-torsion sufficiency is undecided.')}
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
marker='\n## Checkpoint 14 work: the residual cyclic-four gate\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint14_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current post-CP13 gates updated; no historical review was changed.')
