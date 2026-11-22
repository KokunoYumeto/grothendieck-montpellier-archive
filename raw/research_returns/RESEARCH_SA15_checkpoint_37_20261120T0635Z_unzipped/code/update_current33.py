"""Refresh only independently promoted CP33 scope; preserve every general open row."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current32.py')],cwd=w,check=True)
rows=json.loads((w/'notes/item_status.json').read_text())
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
group='sections/A_full_radical_image_structure.tex'
polar='agents/obstructions_crystals/A4_Lang_polar_irreducibility.tex'
orbit='agents/obstructions_crystals/A4_Lang_main_orbit.tex'
b91='agents/reduction_descent/B_residual_wild_high_quotient.tex'
b92='agents/reduction_descent/B_residual_wild_crossing.tex'
for row in rows:
 if row['item']=='A.4' and all(proved(p) for p in [group,polar,orbit]):
  labels=[]
  for rel in [group,polar,orbit]:
   labels.extend(re.findall(r'\\label\{((?:lem|prop|thm|cor):[^}]+)\}',(w/rel).read_text()))
  row['where']+='; '+'; '.join(labels)
  row['status']+='; all odd principal-cube reduced polars irreducible and their main orbit identified'
  row['gate']=('CURRENT REFINEMENT: for every fixed nonordinary principally polarized abelian surface in characteristic2 and every odd |3dTheta|, the actual reduced Lang polar is irreducible without a height-three base-locus assumption. Its unique maximal-dual-rank component is exactly the large orbit V minus K_d. The full geometric image is the complete block inverse image of H_d in GL(K_d), with all shears and the full GL(V/K_d), and dim(V/K_d)>=2. The remaining gate on this route is to exclude nonzero K_d, equivalently the exceptional nonzero Lang components entirely over lower dual-rank strata. No oddness of the large degree 2^r-2^dim(K_d) has been proved. This is not an exact determination of K_d or H_d and adds no full-image degree; the prior smallest exact-degree gaps and general all-X/effective-large-degree A.4 remain open. Earlier restrictions follow as retained proof history: '+row['gate'])
 if row['item']=='B.4' and proved(b91):
  row['where']+='; lem:B-RD91-first-break; prop:B-RD91-divisibility; prop:B-RD91-parameters; thm:B-RD91-large'
  row['status']+='; residual-wild high-quotient parameters and large layer shapes restricted'
  row['gate']=('CURRENT REFINEMENT: B91 proves that different-character residual-wild actual p^3 comparisons at e=p(p-1) require both original two-slope parameters divisible by p. At p5,e20, the two possible crossing pairs are(5,45) and(15,95). In the both-large branch, only congruence-layer dimensions(3,4) or(4,4), of wild orders5^8 or5^9, survive. These are necessary patterns, not examples. The irreducible residual branch is unchanged and the unrestricted least manuscript index remains in{2,3}. Earlier proved restrictions follow: '+row['gate'])
 if row['item']=='B.4' and proved(b92):
  labels=re.findall(r'\\label\{((?:lem|prop|thm|cor):[^}]+)\}',(w/b92).read_text())
  row['where']+='; '+'; '.join(labels)
  row['status']+='; crossing(15,95) excluded'
  row['gate']=('CURRENT REFINEMENT: the separately audited B92 actual-field comparison excludes crossing(15,95); only crossing(5,45) remains among the B91 crossing rows. No closure of that remaining row, the both-large shapes or the irreducible residual branch is claimed. Earlier proved restrictions follow: '+row['gate'])
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
p=w/'RESEARCH_SA15_report.md';text=p.read_text()
body=text[text.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 33 work: global Lang components and residual-wild quotients\n'
if marker in body:body=body.split(marker)[0]
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+marker+'\n'+(w/'notes/checkpoint33_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\n\n| Item |')
assert all(next(r for r in rows if r['item']==item)['status'].startswith('OPEN') for item in ['A.3','A.4','B.3','B.4'])
print('CP33 report refreshed from canonical proofs only:',{'Lang_polar':proved(polar),'main_orbit':proved(orbit),'group_structure':proved(group),'B91':proved(b91),'B92':proved(b92),'general_A4_open':True})
