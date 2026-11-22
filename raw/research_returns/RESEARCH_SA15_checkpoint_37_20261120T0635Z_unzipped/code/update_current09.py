"""Refresh checkpoint09 outcomes without rewriting actual review history."""
from pathlib import Path
import datetime,json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':('OPEN: exact supersingular-product parity formula added',
 'thm:DE-A3-ss-product-rank; cor:DE-A3-ss-product-defect; prop:effective-generic-rank; thm:product-exact-fixed-covectors; thm:all-X-explicit-positive-rank; thm:relative-ordinarity-fails-smooth',
 'Exact generic rank is effectively computable for every specified input; positivity has a uniform explicit degree bound. Ordinary elliptic products have full coherent relative rank. For E:y²+y=x³ over F2 and its Segre cubic product, the generic relative stable rank is 9d²-1 for odd d and 9d²-3 for even d, proved for every positive d. Thus persistent parity defects occur even with smooth ambient Picard scheme and torsion-free crystalline cohomology. A structural formula for arbitrary X remains open.'),
'A.4':('OPEN: every ordinary elliptic pair now has eventual full groups with a terminating explicit threshold',
 'thm:ordinary-products-eventual-full; thm:ordinary-products-Hasse-irreducible; cor:ordinary-products-irreducible-kernel; thm:ss-product-degree-one-full-group; thm:product-char2-all-full-groups; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
 'All projective-space groups and complete effective matrix constructions for arbitrary input are proved. In characteristic2, every ordinary elliptic pair with cubic product polarization has, for every d>=d1, geometric and arithmetic groups GL_(9d²-1)(F2) for odd d and the full pointwise three-covector stabilizer for even d. The threshold d1=max(m1,m2)+1 is obtained by a terminating 3-isogeny search for a degree-one GL8 pair. Hasse irreducibility and irreducibility of the common covector kernel hold uniformly for d>=2. The fixed ordinary F2 product remains settled in every degree. The fixed supersingular product has degree-one group GL8 despite a double Hasse component. The remaining main gate is uniform structural image and irreducibility classification for arbitrary X; the threshold is algorithmically explicit, not a closed uniform bound.'),
'B.4':('OPEN: stronger wild bounds and explicit 9-torsion character ambiguity at p3,e2 proved',
 'prop:B-RD29-p3-level-two; prop:B-RD28-wild-character; thm:B-RD17; prop:B-RD18; cor:B-RD18; prop:B-RD22; prop:B-RD5',
 'Height1 has least index0, and explicit finite upper/lower bounds hold in every height. For p3,e=2u,h>=2 the wild full-torsion constructions give lower bound Nw=1+min(v3u,floor((floor(log3u)+1)/2),floor((floor(log3u)+v3u+1)/4)). Independently, an explicit elliptic curve B and Tate curve T_23328 over Q3(zeta3) have B[9] isomorphic to T[9] but different prime-to-3 inertia characters; hence the least manuscript index is at least2 for every e congruent2 mod4 and h>=2. The earlier p2,e1,h>=2 M[4] obstruction remains. The exact least index in general, including sufficiency of index2 at p3,e2,h2, remains open.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
 if row['item']=='A.1':
  row['status']='REFUTED (a),(b),(c), with exact counterexample degree ranges; corrected (d) PROVED under its stated identification'
  if 'The transpose' not in row['gate']:row['gate']+=' The transpose is always Gysin on the correctly typed torsion groups; its cup-product expression uses the stated torsion identification and the factor d.'
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
marker='\n## Checkpoint 09: all ordinary elliptic pairs, supersingular parity, and a level-nine ambiguity\n'
if marker in body:body=body.split(marker)[0]
new=marker+'\n'+(w/'notes/checkpoint09_changes.md').read_text()
log=w/'notes/ROOT_SEARCH_LOG_09.md'
if log.exists():new+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
print('Checkpoint09 current outcomes refreshed; all actual historical reviews retained.')
