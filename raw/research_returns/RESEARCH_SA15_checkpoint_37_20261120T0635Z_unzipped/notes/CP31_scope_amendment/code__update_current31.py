"""Refresh CP31 canonical gates and distinguish auxiliary dual-rank results."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current30.py')],cwd=w,check=True)
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
b85=proved('agents/reduction_descent/B_first_wild_diagonal_projection.tex')
b86=proved('agents/reduction_descent/B_first_wild_cyclotomic_quotient.tex')
b87=proved('agents/reduction_descent/B_p5_tame_full_first_layer.tex')
dual=proved('agents/monodromy/ppav_twisted_Cartier_Moore.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']=='B.4':
  if b85:
   row['where']+='; lem:B-RD85-diagonal; cor:B-RD85-tame'
   row['status']+='; residual-tame first-wild order at leastp^6 forp=1mod4'
   row['gate']+=(' B85 proves both diagonal-coordinate projections of the first wild layer nonzero, using actual degree-p point fields when one vanishes and incompatible exact coordinate breaks. Forp=1mod4 tame projectors separate off-diagonal and diagonal weights, giving dimW1>=3 and dimW2>=3, so the residual-tame ambiguity requires wild order at leastp^6. This is a necessary condition on actual torsion representations, not a realization.')
  if b86:
   row['where']+='; lem:B-RD86-cyclotomic; prop:B-RD86-traceless; cor:B-RD86-tame'
   row['status']+='; residual-tame first-wild order at leastp^7 forp=1mod4'
   row['gate']+=(' B86 excludes the remaining orderp^6 traceless-layer branch. If W1=W2=sl2, the actual determinant forces mu_(p^2) intoK and the next cyclotomic quotient has lower break(p^2-1)^2 after the tame good base change. Its inclusion in an actual degree-p^2 point field contradicts the exact norm-quotient average and coordinate displacement bound. Consequently the residual-tame sector forp=1mod4 requires wild order at leastp^7; atp5 only5^7 or5^8 remain. Zero terminal trace is not confused with trivial full determinant. The other residual sectors and unrestricted least index remain open.')
  if b87:
   row['where']+='; lem:B-RD87-coefficient; lem:B-RD87-fields; prop:B-RD87-three; cor:B-RD87-full'
   row['status']+='; atp5 the residual-tame sector requires the full5^8 congruence kernel'
   row['gate']+=(' B87 excludes every three-dimensional first wild layer in thep5,e20 residual-tame sector. The two actual degree25 point fields share one diagonal cyclic quotient. Its break is a positive multiple24, whereas the two off-diagonal quotient breaks are6 and18mod24. The fixed-coefficient cancellation lemma and four actual coordinate rows force successive incompatible larger quotient breaks6,72,24,66. Hence W1=W2=M2(F5), and the wild image is the full principal congruence kernel of order5^8. The base does not contain mu25. This remaining image is neither excluded nor realized; the overall least manuscript index still lies in{2,3}.')
 if row['item']=='A.4' and dual:
  row['where']+='; thm:DE-Moore-singular-parameters; prop:ppav-Cartier-cross-Moore-identification; thm:ppav-non-two-torsion-cross-Cartier; cor:fixed-ppav-all-odd-maximal-dual-Cartier'
  row['gate']+=(' A separate structural auxiliary result now identifies every cubic twisted Cartier cross block with the actual characteristic-two Moore matrix, whose identically singular parameters are exactly81 projective three-spaces. Symmetry-normalized theta translations identify the parameter with the squared cubic-theta embedding at a fixed geometric2-torsion shift. The embedding excludes singularity for every twist not killed by2. Outgoing odd-isogeny character decomposition therefore gives maximal dual alternating rank9d^2-1 for every fixed nonordinary principal surface in every odd|3dTheta|. This is distinct from the previously proved generic curve p-rank. The incidence, local inertia and global generation steps connecting this dual rank to new full monodromy cases remain open; no additional exact-group degree is claimed solely from this result.')
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',(w/'RESEARCH_SA15_paper.aux').read_text()))
idmap={r['id']:r['label'] for r in root}
def location(value):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in value.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text()
body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 31 work: first wild images and the theta coefficient route\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint31_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP31 canonical proofs:',{'B85':b85,'B86':b86,'B87':b87,'all_odd_dual_rank_auxiliary':dual})
