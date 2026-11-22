"""Refresh CP34 from explicitly promoted canonical inputs only."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current33.py')],cwd=w,check=True)
rows=json.loads((w/'notes/item_status.json').read_text())
slice_path='agents/obstructions_crystals/A4_Lang_deck_slice_bound.tex'
p=w/slice_path
assert p.exists() and '\\status{Candidate' not in p.read_text()
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
source='agents/obstructions_crystals/A4_general_odd_source_Cartier.tex'
intermediate='agents/monodromy/compatible_cyclic_intermediates.tex'
b93='agents/reduction_descent/B_residual_wild_last_crossing.tex'
for row in rows:
 if row['item']=='A.4':
  row['where']+='; lem:DE-Lang-block-slice-bound; prop:DE-Lang-deck-slice-quotient-eight'
  row['status']+='; exceptional module has quotient dimension at least eight'
  row['gate']=('CURRENT REFINEMENT: the actual central degree-one cubic slice and its common Fermat wall force K_d into the nontrivial odd-deck summands. Thus dim(V/K_d)>=8 and dim(K_d)<=r-8 for every fixed nonordinary principal surface and every odd |3dTheta|, where r=9d^2-1. The irreducible maximal-dual-rank main component has degree at least 2^r-2^(r-8). The full-image gate is still K_d=0; neither the action H_d on a possible nonzero K_d nor the exceptional lower-rank Lang components have been determined. No new full-image degree or general all-X effective bound follows. Earlier proved restrictions follow: '+row['gate'])
  if proved(source):
   row['where']+='; lem:DE-general-odd-source-twisted-blocks; prop:DE-general-odd-source-quotient-bound; cor:DE-general-source-principal-divisor-bound'
   row['gate']=('ADDITIONAL CONDITIONAL SOURCE REDUCTION: for any odd cubic pullback M=eta*(3Theta) of degree a, all nontrivial odd-twist Cartier multiplication and cross determinants have simultaneous common-wall witnesses. If that complete source system has full image, any further odd pullback has dim(V/K)>=9a-1 and K in its nontrivial outer-deck part. The full-source hypothesis remains explicit; this alone adds no unconditional full-image degree. '+row['gate'])
  if proved(intermediate):
   row['where']+='; lem:compatible-line-averaging; prop:compatible-intermediate-common-slice; thm:compatible-cyclic-intermediate-criterion; cor:compatible-cyclic-principal-prime-criterion'
   row['gate']=('COMPATIBLE INTERMEDIATE CRITERION: for one outgoing odd-prime deck group D=(Z/ell)^2, full images on its ell+1 particular type(1,ell) cubic intermediate systems, each of rank9ell-1, suffice for full image in rank9ell^2-1. The actual projectors are compared on one common smooth sharp cubic slice after extending their zero morphisms across connected intermediate opens. Their F2 identity sum e_H=1+e_D then kills K. These nonprincipal source full images are explicit unproved hypotheses; no new unconditional degree is claimed. '+row['gate'])
 if row['item']=='B.4' and proved(b93):
  row['where']+='; lem:B-RD93-cyclotomic; prop:B-RD93-second-field; lem:B-RD93-terminal-bound; thm:B-RD93-crossing'
  row['status']+='; all residual-wild crossing cases excluded'
  row['gate']=('CURRENT REFINEMENT: fully audited B93 excludes the last p5/e20 residual-wild crossing(5,45). The actual terminal determinant has conductor at most275496 from primitive125 point fields and at least391896 from the same cyclotomic subfield. Thus both crossing rows are now excluded. Only both-large residual-wild layer shapes(3,4),(4,4), of wild orders5^8,5^9, and the irreducible-residual sector remain in this first-wild actual125 gate. The unrestricted least manuscript index remains in{2,3}; no surviving comparison is realized here. Earlier statements about an open crossing are retained proof history superseded by B93: '+row['gate'])
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
marker='\n## Checkpoint 34 work: exceptional Lang modules and actual wild fields\n'
if marker in body:body=body.split(marker)[0]
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+marker+'\n'+(w/'notes/checkpoint34_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\n\n| Item |')
assert all(next(r for r in rows if r['item']==item)['status'].startswith('OPEN') for item in ['A.3','A.4','B.3','B.4'])
print('CP34 canonical deck-slice quotient bound refreshed; general A.4 remains open.')
