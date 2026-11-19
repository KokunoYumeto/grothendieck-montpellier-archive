"""Refresh current CP11 outcomes, preserving all actual historical reviews."""
from pathlib import Path
import json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':(
 'OPEN: exact all-degree formula proved for every odd-degree polarization on an abelian surface in characteristic2',
 'thm:DE-A3-separable-ranks; thm:DE-A3-ppav-ranks; prop:DE-A3-ppav-degree-one; thm:all-X-explicit-positive-rank; prop:effective-generic-rank; thm:relative-ordinarity-fails-smooth',
 'For every abelian surfaceA in characteristic2, ampleM with oddD=chi(M), and L=M³, the complete-system generic relative rank is9Dd²−1 odd and9Dd²−3+f_A even, f_A the2-rank. The coherent dimension is9Dd²−1, so generic bijectivity holds exactly for oddd or ordinaryA. The principal caseD1 settles every algebraic mixed-product factor. Ambient restriction is surjective for d>=max(1,reg(I_A)−1), and for everyd on cubic products. All-input exact computation and the all-X explicit positivity bound remain proved. Even-degree polarizations and arbitrary-X structural ranks remain open; no arbitrary embedding is assumed to be a third power.'),
'A.4':(
 'OPEN: every principal surface has an exact invariant quotient; full ordinary eventual groups and supersingular-product degrees1–3 proved',
 'thm:ordinary-ppav-eventual-full; thm:nonordinary-ppav-all-covectors; thm:ss-product-degree-two-full-group; thm:ss-product-degree-three-full-group; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
 'All projective-space groups and all-input exact matrix constructions remain proved. Every ordinary principal surface in characteristic2 has eventual oddGL_r and evenfull three-covector stabilizer, with explicit terminating isogeny/regularity threshold and full arithmeticGalois preimage. Every nonordinary principal surface has entire geometric/arithmetic covector dimension0odd,2^{f_A}even in complete systems, with the stated ambient regularity bound. The fixed supersingular product has full GL8, F2^32 semidirectGL32, GL80 in degrees1,2,3, and an actual naturalGL8block in every degree. Its uniform higher-degree full-image/irreducibility gate and arbitrary-X structural classification remain open.'),
'B.4':(
 'OPEN: p3,e2,h2 has only indices2 or3 remaining;81-torsion always suffices',
 'thm:B-RD34; lem:B-RD34-kernel; prop:B-RD33; thm:B-RD31; prop:B-RD32; prop:B-RD30; prop:B-RD29-p3-level-two; thm:B-RD17',
 'Height1 has least index0; explicit general upper/lower bounds remain. Atp3,e2,h2, explicit9-torsion ambiguity gives lower index2 and the audited supersingular logarithm estimate excludes every81-torsion failure, so nu_min is in{2,3}. Any27-torsion failure must compare two whole potentially supersingular groups with norm-one finite special inertia, different tame quotient orders, and joint faithful good-reduction image of order18 or36. Its special graph at each levelr is exactly kerF^r×kerF^r. Existence at27 and the general least character index remain open. This promotion followed the actual review06 and does not rewrite that historical review.')
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
marker='\n## Checkpoint 11: universal surface ranks and nonordinary invariant quotients\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint11_changes.md').read_text()
log=w/'notes/ROOT_SEARCH_LOG_11.md'
if log.exists():body+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('CP11 current outcomes refreshed; actual historical reviews retained.')
