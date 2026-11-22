"""Refresh CP36 from explicitly promoted canonical inputs only."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current35.py')],cwd=w,check=True)
proved_inputs={
 'agents/obstructions_crystals/A4_primitive_type_1_3_full_group.tex':'f2830116b972b71469586796ad64820cf46f61829628d9680e70b7c3b680d07d',
 'agents/reduction_descent/B_full_Iwahori_selected_point.tex':'fa852188ae2896a81d4df4eb004dd1905e08a3f03df5d82e52b8a51b021e35b6'}
for rel,digest in proved_inputs.items():
 p=w/rel;assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
 assert '\\status{Candidate' not in p.read_text()
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']=='A.3':
  row['where']+='; lem:DE-odd-line-Frobenius-stable; lem:DE-primitive-one-three-Cartier; lem:DE-primitive-one-three-smooth-member; lem:DE-primitive-one-three-Euler'
  row['status']+='; globally generated primitive type(1,3) has sharp relative rank2'
  row['gate']=('ADDITIONAL PROVED PRIMITIVE SOURCE: on a fixed nonordinary abelian surface in characteristic2, an ample globally generated type(1,3) line has a nonempty smooth-member open, generic relative stable rank2 and generic curve p-rank f(A)+2, with genus4. The actual Euler determinant is the reduced Fermat cubic. Global generation is an explicit hypothesis and is not asserted for every type(1,3) polarization. General A.3 remains OPEN. Earlier proved cases and remaining gates: '+row['gate'])
 if row['item']=='A.4':
  row['where']+='; thm:DE-primitive-one-three-full-image; rem:DE-primitive-one-three-scope'
  row['status']+='; globally generated primitive type(1,3) full relative GL2 proved'
  row['gate']=('ADDITIONAL EXACT SOURCE IMAGE: for each fixed nonordinary surface and ample globally generated type(1,3) line in characteristic2, the actual rank2 relative Lang image is GL2(F2) and the nonzero cover is connected of degree3. Complete stability, Cartier nonvanishing, nodal smoothing and actual Kummer/Artin-Schreier restrictions prove the assertion. This is a separate source case; it does not remove fixed-principal degree17 or imply full image for arbitrary primitive(1,ell). General A.4 and the previously proved strongest exceptional-module bounds remain: '+row['gate'])
 if row['item']=='B.4':
  row['where']+='; lem:B-RD96-selected; lem:B-RD96-opposite; prop:B-RD96-conductor; lem:B-RD96-gap; thm:B-RD96-residual-wild'
  row['status']+='; entire first-wild residual-wild branch excluded at p5,e20'
  row['gate']=('CURRENT STRONGEST FIRST-WILD REFINEMENT: at p5,e20, B96 excludes the full Iwahori5^9 case, completing exclusion of every residual-wild actual125 comparison with different finite special characters in the normalized whole potentially supersingular height2 setting. The proof uses an actual selected quotient125 point supplied by M[125]/H, actual opposite25 point fields, an identified three-character compositum, exact Herbrand conversion and a coefficient-gap contradiction. No whole quotient125 comparison is assumed. The residual-irreducible sector remains, with necessary wild image orders5^r for5<=r<=8. The unrestricted least manuscript index remains in{2,3}; general B.4 is OPEN. Earlier residual-wild alternatives below are retained proof history, superseded by B96: '+row['gate'])
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
p=w/'RESEARCH_SA15_report.md';text=p.read_text();body=text[text.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 36 work: primitive sources and the remaining wild image\n'
if marker in body:body=body.split(marker)[0]
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+marker+'\n'+(w/'notes/checkpoint36_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\n\n| Item |')
assert all(next(r for r in rows if r['item']==item)['status'].startswith('OPEN') for item in ['A.3','A.4','B.3','B.4'])
print('CP36 primitive source and residual-wild exclusion refreshed; all four general open rows remain open.')
