"""Refresh current CP12 outcomes, preserving all actual historical reviews."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':(
 'OPEN: every ordinary surface polarization and several inseparable supersingular product types now have exact all-degree ranks',
 'thm:DE-A3-ordinary-all-ranks; thm:ss-rectangular-all-degrees; thm:DE-A3-separable-ranks; thm:DE-A3-ppav-ranks; thm:all-X-explicit-positive-rank; prop:effective-generic-rank',
 'For every ordinary abelian surface in characteristic two and every ample M, L=M³ has generic relative rank 9 chi(M)d²−1 in every complete system. For all surfaces with odd chi(M), the earlier parity formula remains. On the fixed supersingular product, a product M of type (a,b) with exactly one even factor of 2-adic valuation one has rank 9abd²−2 in odd degree and 9abd²−3 in even degree; if both a,b are even, the rank is always 9abd²−3. The relative dimension is 9 chi(M)d²−1. All statements retain their explicit ambient regularity bounds and third-power embedding. Remaining even nonordinary polarization types and arbitrary-X structural ranks are open.'),
'A.4':(
 'OPEN: every principal surface has an exact invariant quotient; full ordinary eventual groups and supersingular-product degrees 1–3 proved',
 'thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors; thm:ss-product-degree-two-full-group; thm:ss-product-degree-three-full-group; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
 'All previous projective-space groups, ordinary principal-surface eventual groups, nonordinary principal-surface invariant quotients, and supersingular-product full groups in degrees 1–3 remain proved. The paper now includes complete local Cartier criteria at self-tacnodes and triple points and one global mixed self-tacnode witness certified on all projective charts. The two tangent-triple witness proofs and the global degree-three collision reduction are retained separately as unintegrated candidates at the paper freeze. No uniform higher-degree full-image theorem is inferred from them. The arbitrary-X structural classification remains open.'),
'B.4':(
 'OPEN: p=3, e=2, h=2 has only indices 2 or 3 remaining; 81-torsion always suffices',
 'prop:B-RD36; prop:B-RD35; thm:B-RD34; lem:B-RD34-kernel; prop:B-RD33; thm:B-RD31; prop:B-RD32; thm:B-RD17',
 'Height one has least index zero; explicit general upper and lower bounds remain. At p=3, e=2, h=2, the least index is 2 or 3 and 81-torsion suffices. Every remaining level-27 comparison is realized by two elliptic curves. The exact residual question asks for two triples (a2,a4,a6) over W(k)[pi]/(pi²−3), with 0≤v(Delta)≤23, 3v(c4)>v(Delta), isomorphic 27-torsion and discriminant valuations in different classes: 0 mod 4, 2 mod 4, or odd. The tame quotient order is 4/gcd(4,v(Delta)). Joint faithful inertia has order 18 or 36. This six-coefficient criterion has not been decided; existence at level 27 and the general least index remain open.'),
'E.2':(
 'REFUTED in the unrestricted scope; PROVED for coherent coefficients over a locally Noetherian base',
 'thm:DE-E2-counterexample; cor:DE-E2-Noetherian-counterexample; thm:DE-E2-coherent-Noetherian; lem:DE-E2-completed-Cech',
 'For flat locally finitely presented X/S with S locally Noetherian, ordinary coherent stratified modules are equivalent to quasi-coherent infinitesimal crystals with coherent value on X, on the small or big site and arbitrary classical tests. Values on Noetherian tests are coherent and on arbitrary tests finitely presented. No coefficient flatness or characteristic restriction is required. The proof uses universally exact completed Cech descent and H0 of a derived crystal, without asserting derived discreteness. The broader arbitrary-module and non-Noetherian assertions remain refuted by the retained counterexamples.')
}
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
p=w/'RESEARCH_SA15_report.md'; old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 12: coherent crystals and inseparable surface polarizations\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint12_changes.md').read_text()
log=w/'notes/ROOT_SEARCH_LOG_12.md'
if log.exists():body+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('CP12 current outcomes refreshed; actual historical reviews retained.')
