"""Refresh CP35 from explicitly promoted canonical inputs only."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current34.py')],cwd=w,check=True)
rows=json.loads((w/'notes/item_status.json').read_text())
proved_inputs={
 'agents/obstructions_crystals/A4_Lang_wedge_pole_theta_bound.tex':'4bc8feec42673f6863d2bd864fd7bce98d509011c6e64251cd421682f77d5a3c',
 'agents/obstructions_crystals/A4_compatible_residual_modules.tex':'fc1f3d437c6e4b5febf87495f1ad1924a2d4ef0474b97695bf7db1bfc0f05728',
 'agents/reduction_descent/B_both_large_tracefree_rows.tex':'59b1804c0bcb3f67338590e22bf013042b30abef1eee0f15c809198d759d760d',
 'agents/reduction_descent/B_remaining_tracefree_rows.tex':'f5e00599e196b898e13d8718e022d5616a00e78deac55155bc3be5707e58898e',
}
for rel,digest in proved_inputs.items():
 p=w/rel
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
 assert '\\status{Candidate' not in p.read_text()
for row in rows:
 if row['item']=='A.4':
  row['where']+='; lem:DE-Lang-wedge-pole-bound; lem:DE-theta-invariant-divisor-degree; thm:DE-Lang-theta-wedge-quotient-bound; cor:DE-Lang-wedge-cyclic-principal-bounds; lem:DE-source-residual-projection; thm:DE-compatible-residual-module-sum; cor:DE-prime-compatible-wedge-bound'
  row['status']+='; wedge and compatible cyclic modules strengthen the exceptional-dimension bound'
  row['gate']=('CURRENT STRONGEST UNCONDITIONAL DIMENSION REFINEMENT: for the fixed nonordinary principal surface in characteristic2 and every odd degree d, r=9d^2-1 and the canonical exceptional module satisfies dim(V/K_d)>=max(8,3d). The main Lang component therefore has degree at least2^r-2^(r-max(8,3d)). At an odd prime ell, put f=ord_ell(2); compatible actual intermediate residual modules give dim(K_ell)<=(ell+1)f floor((6ell-1)/f) and dim(V/K_ell)>=9ell^2-1-(ell+1)f floor((6ell-1)/f). At the first remaining degree17 this is dim(K_17)<=1728 and quotient dimension>=872 in rank2600, improving the previous quotient bound8. The wedge proof allows poles only on the remaining determinant divisor: if K is nonzero, its dimension k obeys k<=N-e_good-1 and quotient dimension>=e_good>=d2, where N=d1*d2 and e_good is the degree of the nonempty theta-invariant common full-radical wall. If e_good=N then K=0. Neither exhaustion of the determinant divisor nor vanishing of K has been proved in the remaining degrees. The full-image gate stays K_d=0, with the exceptional action and components still undetermined; no new full-image degree or general all-X effective bound follows. Earlier bounds and conditional reductions are retained as proof history: '+row['gate'])
 if row['item']=='B.4':
  row['where']+='; lem:B-RD94-group; lem:B-RD94-ordering; lem:B-RD94-common-high; prop:B-RD94-profiles; lem:B-RD94-terminal; thm:B-RD94-six-rows; lem:B-RD95-critical; prop:B-RD95-profiles; thm:B-RD95-tracefree'
  row['status']+='; residual-wild tracefree first layer excluded'
  row['gate']=('CURRENT STRONGEST FIRST-WILD REFINEMENT: at p5,e20, B94 excludes six of ten different-character both-large parameter pairs in layer shape(3,4), and B95 excludes the remaining four(7,15),(9,13),(9,17),(11,15) by the critical coefficient bound and the same actual terminal cyclotomic character. Together with the two crossing exclusions, any residual-wild actual125 different-character comparison must have the full Iwahori image of order5^9, with both congruence layers M2(F5). This full image is neither excluded nor realized. The residual-irreducible sector still requires wild order5^r,5<=r<=8. The unrestricted first-wild least manuscript index remains in{2,3}, and general B.4 remains OPEN. Earlier crossing and tracefree alternatives below are retained proof history superseded by B93-B95: '+row['gate'])
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
marker='\n## Checkpoint 35 work: theta degrees and compatible residual modules\n'
if marker in body:body=body.split(marker)[0]
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+marker+'\n'+(w/'notes/checkpoint35_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\n\n| Item |')
assert all(next(r for r in rows if r['item']==item)['status'].startswith('OPEN') for item in ['A.3','A.4','B.3','B.4'])
print('CP35 promoted wedge and compatible-module bounds refreshed; all four general open rows remain open.')
