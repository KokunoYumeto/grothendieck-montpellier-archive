"""Refresh checkpoint10 outcomes while preserving actual review history."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
 'A.3':(
  'OPEN: exact all-degree supersingular and transcendental mixed-product formulas proved',
  'thm:DE-A3-ss-product-rank; thm:DE-A3-mixed-generic; prop:effective-generic-rank; thm:all-X-explicit-positive-rank; thm:relative-ordinarity-fails-smooth',
  'Exact generic rank is effectively computable for every specified input and positivity has an explicit uniform degree bound. Ordinary elliptic products have full coherent relative rank. For the fixed supersingular E0×E0 in characteristic2 the rank is9d²−1 odd and9d²−3 even. For the fixed mixed Et×E0 overF2(t)^perf it is9d²−1 odd and9d²−2 even, also for every transcendental ordinaryj. No countable-open or changing-factor choice is used. A structural formula for arbitraryX remains open; the arbitrary algebraic mixed-factor refinement is not inferred from finite probes.'),
 'A.4':(
  'OPEN: eventual full geometric and arithmetic groups proved for every ordinary principally polarized surface in characteristic2',
  'thm:ordinary-ppav-eventual-full; thm:ordinary-ppav-Hasse-kernel; prop:ordinary-ppav-all-covectors; thm:ss-product-exact-covectors; thm:ss-uniform-GL8-block; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
  'All projective-space groups and exact effective matrix constructions for arbitrary input are proved. Every ordinary principally polarized abelian surface in characteristic2, embedded by3Theta, has eventual geometric GL_r for oddd and the full pointwise three-covector stabilizer for evend, r=9d²−1. The arithmetic even image is the full preimage of the actual Galois permutation group on the three nonzero Frobenius-kernel characters. A terminating polarized3-isogeny search gives multipliern and thresholdmax(n+1,reg(I_A)−1); auxiliary isogenies may require a finite field extension. Hasse irreducibility and common-kernel irreducibility hold in complete systems fromd2. On the fixed supersingular product the exact invariant quotient is0odd/1even and every degree contains an actual naturalGL8block. Its higher-degree full images and irreducibility remain open, as does the uniform structural classification for arbitraryX.'),
 'B.4':(
  'OPEN: p3,e2,h2 reduced to indices2,3,4 and two possible81-torsion inertia configurations',
  'thm:B-RD31; prop:B-RD32; prop:B-RD30; prop:B-RD29-p3-level-two; prop:B-RD28-wild-character; thm:B-RD17; prop:B-RD22',
  'Height1 has least index0. Sharper explicit finite upper bounds and wild lower bounds hold in all heights. Atp3,e2,h2 the exact least manuscript index is in{2,3,4}: an explicit9-torsion ambiguity gives the lower bound, and243-torsion determines the character. A27 comparison already excludes potentially-supersingular versus height-one-filtered pairs. Any81 failure must be two potentially supersingular groups with faithful inertia orders12 versus3 or6 and joint order36; existence of either comparison remains undecided. The exact least index in general and sharpness at27/81 remain open.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text() if (w/'RESEARCH_SA15_paper.aux').exists() else ''
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(text):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in text.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 10: supersingular structure, theta geometry, and sharper character comparisons\n'
if marker in body:body=body.split(marker)[0]
new=marker+'\n'+(w/'notes/checkpoint10_changes.md').read_text()
log=w/'notes/ROOT_SEARCH_LOG_10.md'
if log.exists():new+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
print('Checkpoint10 outcomes refreshed; actual historical reviews retained.')
