"""Refresh only promoted CP21 gates; historical actual reviews stay immutable."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current20.py')],check=True,cwd=w)
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.3':
        row['where']+='; prop:DE-A3-positive-cup-trace-zero-candidate; cor:DE-A3-positive-tracezero-matrix-line-candidate'
        row['gate']+=' For the remaining mixed positive-index sharpness problem, the actual cup-ratio matrix is now proved trace zero. Its coherent variation is the transpose of the coefficient-square of the Cartier-dual derivative. An acyclic alternating rank-two bundle factors the relevant pairing, making the cohomological graph isotropic. Thus failure of invertibility of every first-order variation means the variation image is zero or one rank-one nilpotent line; it is enough to prove image dimension at least two at a suitable sharp source. That image lower bound remains unproved.'
        row['gate']=row['gate'].replace('Neither exclusion is established uniformly.','The stronger trace-zero reduction stated below now makes the two possible rulings coincide in one nilpotent line.').replace('This identifies the remaining variation map but does not prove its determinant nonzero or exclude either rank-one matrix ruling.','This identifies the remaining variation map; the further trace-zero argument below narrows its possible singular image to one nilpotent line.')
    if row['item']=='A.4':
        row['where']+='; cor:nonordinary-ppav-uniform-root-inertia-candidate; cor:root-nonordinary-Lang-rank-four-excluded-candidate'
        row['gate']+=' On every nonordinary principal surface in characteristic two, degree-one geometric monodromy now contains the full order-2^7 root subgroup fixing a seven-dimensional hyperplane pointwise. For a nonproduct such surface, the actual Cartier tensor is stable: its rank-four scheme is precisely the smooth Frobenius-twisted 3Theta surface, and its Pfaffian cubic has no other reduced singular points. Consequently rank-four nonzero Lang incidence cannot dominate, while the rank-eight part is an irreducible affine-line torsor over an open Fermat cone. Only rank-six compatibility can supply an additional dominating component. Excluding that component, and full global monodromy, remain open.'
    if row['item']=='B.4':
        row['where']+='; prop:B-RD56-cubic-wild; thm:B-RD57'
        row['gate']=row['gate'].replace('Thus the remaining irreducible-residual wild orders are p³ and p⁴, namely 125 and 625 at p=5. Reducible residual cases and both larger wild orders remain unresolved.','')
        row['gate']+=' The complete cubic-wild exhaustion also excludes order p³, including the projective-order-two split anti-Cartan cases. Hence every remaining irreducible-residual different-character pair must have the full wild image M2(Fp), of order p⁴. Both p=5 candidate type patterns require order625. Reducible-residual cases and the full-p⁴ branch remain open in this frozen checkpoint paper. The later B58 restriction is retained as separately audited candidate material and is not integrated into this checkpoint theorem register.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text());aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 21 work: actual Coble geometry, root inertia and wild-layer exhaustion\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint21_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP21 promoted gates refreshed.')
