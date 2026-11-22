"""Refresh CP30 gates from canonical audited proofs; retain all open scopes."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current29.py')],cwd=w,check=True)
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
b82=proved('agents/reduction_descent/B_first_wild_reducible_terminal.tex')
b83=proved('agents/reduction_descent/B_first_wild_swapped_quotients.tex')
b84=proved('agents/reduction_descent/B_tame_residual_one_prime_recovery.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']!='B.4':continue
 if b82:
  row['where']+='; lem:B-RD82-Newton; lem:B-RD82-terminal; prop:B-RD82-recovery; thm:B-RD82'
  row['status']+='; first-wild nontrivial residual wild branch requires order at leastp⁵'
  row['gate']+=(' B82 further shrinks the first-wild actualp³ gate: when residual wild inertia '
   'is nontrivial, any different-character comparison requires wild orderp^r,5<=r<=9. '
   'The denominator, terminal matrices on all outside-line vectors and two opposite '
   'break inequalities exclude order at mostp⁴; if both normalized slope parameters '
   'are divisible byp, the determinant and common high line recover the character. '
   'This replaces the earlier unqualified residual-wild open branch. Residual-tame '
   'exchanged high lines, larger wild images and the full least index in{2,3} remain open.')
 if b83:
  row['where']+='; lem:B-RD83-tame; lem:B-RD83-quotients; prop:B-RD83-Lie; cor:B-RD83'
  row['status']+='; forp=1mod4 every residual type requires first-wild order at leastp⁵'
  row['gate']+=(' B83 completes the small-image exclusion for primesp=1mod4: two actual '
   'opposite high-line quotients detect both off-diagonal directions in the same W1. '
   'The nonsquare tame weight separates them; actual commutators then give '
   'dimW1>=2 and dimW2>=3. Combined with B81/B82, any different-character actualp³ '
   'comparison at e=p(p-1),p=1mod4 has wild order at leastp⁵, regardless of residual type. '
   'Atp5/e20 this means at least3125. No larger image is excluded or constructed. '
   'Forp=3mod4 coincident order-two tame weights remain an explicit exception. '
   'The unrestricted first-wild least manuscript index is still in{2,3}.')
 if b84:
  row['where']+='; prop:B-RD84-tame; cor:B-RD84-first-wild'
  row['status']+='; residual-tame first-wild parameters bothp²-divisible; p5 tame pattern only{25,75}'
  row['gate']+=(' B84 further proves an arbitrary-e actualp² recovery theorem when the first-level '
   'modules are L-rational and either normalized low parameter b_i is prime to p. '
   'The common single-point field has degreep² and contains every first-level translation; '
   'opposite high/low break comparisons recover the high line and b_i, with no restriction '
   'on the full division field. Consequently the first-wild residual-tame ambiguity must '
   'have exchanged high lines and B_i=p²k_i,1<=k_i<=p-2, at every wild image size. '
   'Atp5/e20 only the parameter pair{25,75} and type pairA/B up to common quadratic '
   'twist remain in that sector. The exploratory pairs{35,75} and{55,75} are excluded. '
   'No surviving pair is constructed, other residual sectors remain, and the full '
   'least manuscript index remains in{2,3}.')
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
marker='\n## Checkpoint 30 work: quotient images and twisted Cartier blocks\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint30_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP30 proved gates:',{'residual_wild_order_bound':b82,'all_residual_p1mod4_order_bound':b83,'one_prime_tame_recovery':b84})
