"""Refresh current CP13 status without changing historical review records."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':(
 'OPEN: exact ranks for every ordinary surface embedding and every supersingular product polarization',
 'thm:DE-A3-ordinary-arbitrary-embedding; thm:DE-A3-all-ss-rectangles; thm:DE-A3-separable-ranks; thm:DE-A3-ppav-ranks; thm:all-X-explicit-positive-rank',
 'Every ordinary characteristic-two abelian surface and ample M has generic relative rank chi(M)n²−1 in |M^n| for all n>=3, with explicit ambient bound max(3,reg(I_A)−1). On E²:y²+y=x³, every product M of type(a,b), L=M³, has exact rank9abd²−1−epsilon(ad)−epsilon(bd) in all positive degrees, with epsilon the evenness indicator. The previous valuation restriction is removed by a uniform two-point kernel-sheaf calculation. The odd-polarization formula for all abelian surfaces remains. Arbitrary-X structural ranks and remaining nonproduct inseparable nonordinary polarization types are open.'),
'A.4':(
 'OPEN: degree-three supersingular Hasse divisor now irreducible/reduced; uniform higher-degree image remains unresolved',
 'cor:ss-degree3-hasse-irreducible; lem:ss-uniform-source-smoothness; prop:ss-level3-three-witness-reduction; thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors',
 'All previously proved projective-space groups, ordinary principal-surface eventual full groups, nonordinary principal-surface invariant quotients and supersingular-product groups in degrees1–3 remain. The degree-three relative Hasse divisor on the fixed supersingular product is now geometrically irreducible and reduced. Uniform globally smooth mixed-contact sources also exist for every translation with both coordinates nonzero, by an explicit Artin-Schreier slice and discriminant-degree proof. The remaining uniform gate is exclusion of further norm collisions and construction of uniform tangent-triple bridges. No higher-degree full-group conclusion is inferred; the arbitrary-X structural classification remains open.'),
'B.4':(
 'OPEN: p=3,e=2,h=2 residual27 test narrowed to C3, or C4 with joint inertia18',
 'prop:B-RD38; prop:B-RD37; prop:B-RD36; prop:B-RD35; thm:B-RD34; thm:B-RD31',
 'The least index remains2 or3 and81-torsion always suffices. Every remaining27 comparison is realized by elliptic curves over the ramification-two Witt DVR, with minimal discriminant valuations0..23 and different tame classes. Scalar residual representations are now excluded already at9-torsion by the corrected direct/reverse Hesse equations and unit obstructions. After a common quadratic twist the residual image is C3 or C4. In the C4 case v(j)=6 and6 divides v(Delta), so only individual special-inertia orders3,6 and joint18 remain. Every joint36 possibility has residual C3. Existence of either residual27 comparison and the general least-index formula remain open.')}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text() if (w/'RESEARCH_SA15_paper.aux').exists() else ''
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(t):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 13: uniform rectangular ranks and residual character restrictions\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint13_changes.md').read_text()
log=w/'notes/ROOT_SEARCH_LOG_13.md'
if log.exists():body+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('CP13 current outcomes refreshed; historical reviews unchanged.')
