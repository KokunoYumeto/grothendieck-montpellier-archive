"""Refresh CP32 scope without promoting exploratory computations to main gates."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current31.py')],cwd=w,check=True)
rows=json.loads((w/'notes/item_status.json').read_text())
p=w/'agents/reduction_descent/B_p5_cyclotomic_break_three_example.tex'
b89=p.exists() and '\\status{Candidate' not in p.read_text()
def proved(rel):
 q=w/rel
 return q.exists() and '\\status{Candidate' not in q.read_text() and '\\textup{[Candidate' not in q.read_text()
b90=proved('agents/reduction_descent/B_p5_third_point_ramification.tex')
wallrel='agents/monodromy/ppav_all_odd_full_root_inertia.tex'
wall=proved(wallrel)
for row in rows:
 if row['item']=='B.4' and b89:
  row['where']+='; lem:B-RD89-base; rem:B-RD89-scope'
  row['gate']+=(' The explicit B89 base realizes the required cyclotomic break3 with e_K=20 and mu5, and gives full cyclic order25 at level125. Thus this cyclotomic necessary condition alone does not exclude the remaining full-image comparison. No height-two BT pair has been constructed, and the main gate is not reduced by this auxiliary realization.')
 if row['item']=='B.4' and b90:
  row['where']+='; lem:B-RD90-point-towers; prop:B-RD90-terminal; thm:B-RD90-tame-exclusion'
  row['status']+='; p5/e20 tame reducible residual branch excluded at actual125'
  row['gate']=('CURRENT REFINEMENT: B90 excludes the entire tame reducible residual branch at p5,e_K20 for different-special-character actual125-torsion comparisons. Actual third-point fields force a terminal filtration whose determinant coset average would be1896/5, impossible for an integral lower break. The earlier full5^8 necessary image is therefore eliminated in this branch. Irreducible-residual and nontrivial-residual-wild branches remain, and the unrestricted least manuscript index is still in{2,3}. The following earlier proved restrictions are retained as the proof history and continue to apply in their stated wider scopes: '+row['gate'])
 if row['item']=='A.4' and wall:
  labels=re.findall(r'\\label\{((?:lem|prop|thm|cor):[^}]+)\}',(w/wallrel).read_text())
  row['where']+='; '+'; '.join(labels)
  row['gate']=('CURRENT REFINEMENT: the canonical odd-principal-cube wall theorem proves nonemptiness of the Hasse wall inside the maximal common section/dual-rank open, using the exact Fermat nondivisibility theorem in one common theta coordinate system. Every fixed nonordinary principal surface in every odd|3dTheta| consequently has full hyperplane-radical divisorial inertia. The remaining gate on this structural route is global generation or an adequate irreducibility/connectivity theorem. This does not itself add a full exact-group degree; general A.4 and the previously stated first exact-image degree gaps remain open. The following earlier reductions are retained as proof history; their former local-nonemptiness condition is superseded by the new theorem: '+row['gate'])
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',(w/'RESEARCH_SA15_paper.aux').read_text()))
idmap={r['id']:r['label'] for r in root}
def location(value):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in value.split('; '))
def cell(value):return value.replace('|','\\|').replace('\n',' ')
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join(cell(v) for v in [r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
report=w/'RESEARCH_SA15_report.md'
old=report.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 32 work: the Hasse-divisor and actual wild-field gates\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint32_changes.md').read_text()
report.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP32 canonical scope:',{'B89_base_only':b89,'B90_tame_branch_excluded':b90,'odd_full_root_inertia':wall,'general_A4_open':True})
