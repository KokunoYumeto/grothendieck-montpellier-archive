"""Refresh the current table using only the five audited CP37 canonical inputs."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current36.py')],cwd=w,check=True)
for rel,digest in json.loads((w/'notes/checkpoint37_promoted_hashes.json').read_text()).items():
 assert hashlib.sha256((w/rel).read_bytes()).hexdigest()==digest
 assert '\\status{Candidate' not in (w/rel).read_text()
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']=='A.4':
  row['where']+='; lem:prime-five-exceptional-composition; prop:prime-five-empty-common-wall; lem:DE-five-evaluation-kernel; prop:DE-five-evaluation-fibre-dichotomy; lem:root-elliptic-double-cover-lines; lem:root-double-cover-branch-module; thm:root-primitive-prime-permutation-counterexamples; cor:root-primitive-permutation-Lang-components'
  row['status']+='; actual primitive counterexamples to unrestricted full image and Lang connectedness'
  row['gate']=('ACTUAL PRIMITIVE LIMITATION: on E:y^2+y=x^3 over F2bar, A=E x E and L_m=O(mV+H+Gamma), all m>=1 give ample globally generated type(1,2m+1) lines with elliptic fibre degree2. For n=2m+1 in{5,7,11,13,17}, generic smooth curves have genus n+1 and p-rank n-1; their actual relative Lang representation is the canonical branch-permutation module F2^B/F2*1 with |B|=n. Hence the actual image lies in S_n, strictly smaller than GL_(n-1)(F2), and the nonzero cover has at least(n-1)/2 components. Exact S_n is not asserted. These non-very-ample primitive systems are not powers of a fixed embedding, so they do not refute or close general large-degree A.4. '
   'TYPE(1,5) GEOMETRY: the actual theta image lies on Q=sum y_i sigma_i^2; the evaluation-kernel map has positive-dimensional generic fibres exactly when an elliptic curve has L-degree2, and then factors through that elliptic quotient. Abstract prime5 ratios with c1,c2 nonzero and c1^5=c2^5 have no common maximal-rank Euler wall despite birational radicals; this checkpoint does not yet identify the actual coefficient ratio of the displayed geometric example. Generic rank and birationality therefore do not by themselves prove connectedness. The fixed-principal degree17 gate remains K_17=0, with dim K_17<=1728 and quotient dimension>=872 in rank2600. Earlier proved reductions and source cases: '+row['gate'])
 if row['item']=='B.4':
  row['where']+='; lem:B-RD99-points; lem:B-RD99-cyclotomic; thm:B-RD99-irreducible; lem:B-RD100-arc; thm:B-RD100-ambiguity; cor:B-RD100-threshold; thm:B-RD100-exact'
  row['status']='OPEN generally; exact nu_min(p,2p(p-1),2)=3 for every p>=5 and nu_min(5,20,2)=2; valuation-one irreducible-residual branch recovered; prior exact tame/small-prime cases retained'
  old=row['gate'].replace('other wild absolute indices,','wild absolute indices outside the newly closed e=2p(p-1) family,')
  row['gate']=('NEW EXACT SECOND-WILD FAMILY: for every p>=5, nu_min(p,2p(p-1),2)=3 in the full height-two monodromy-condition setting. An actual integral Lubin-Tate arc, exact tame descent and compatible Kummer-cocycle lift construct whole-versus-filtered groups with isomorphic actual p^3 truncations and different prime-to-p special characters. Actual p^4 determines all such characters, by B76 dimension/determinant/mixed exclusions and the actual-target B64 quotient recurrence. In particular nu_min(5,40,2)=3. The lower examples are actual Barsotti-Tate groups over explicitly defined complete DVR fields, not merely coefficient profiles. '
   'SHARP EXISTENTIAL MIXED THRESHOLD AT VALUATION ONE: for p>=5 and e=t p(p-1) with p not dividing t, an actual p^3 mixed comparison with different special characters exists if and only if e>p^2. The construction actually works whenever p(p-1) divides e and e>p^2; no least-index formula for every such e is claimed. '
   'ALL VALUATION-ONE IRREDUCIBLE RESIDUAL COMPARISONS: at every e=t p(p-1), p not dividing t, an actual p^3 isomorphism between whole potentially supersingular height-two groups with irreducible residual inertia determines the requested special characters. Exact point-field ramification, both cyclotomic tower cases and the selected actual critical coefficients are all treated. Reducible branches and mixed groups at arbitrary e remain separate. Earlier exact cases and remaining general gate: '+old)
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
marker='\n## Checkpoint 37 work: actual primitive counterexamples and wild ramification\n'
if marker in body:body=body.split(marker)[0]
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+marker+'\n'+(w/'notes/checkpoint37_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\n\n| Item |')
assert all(next(r for r in rows if r['item']==item)['status'].startswith('OPEN') for item in ['A.3','A.4','B.3','B.4'])
print('CP37 five audited inputs refreshed; general A.3/A.4/B.3/B.4 remain open. No future review executed.')
