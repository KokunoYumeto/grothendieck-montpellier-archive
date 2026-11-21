"""Integrate the complete characteristic-three odd-orthogonal endpoint."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
path='agents/imprimitive/orthogonal_lowlevels/orthogonal_three_odd_section.tex'
peer='agents/g34_eightfolds/bireflection/ORTHOGONAL_THREE_ODD_PEER_AUDIT.md'
frozen='7d0e8c1e9e9023e0840b306642696c942020cc870c2460f5265a1a9feb947e5b'
assert hashlib.sha256((R/path).read_bytes()).hexdigest()==frozen
assert hashlib.sha256((R/peer).read_bytes()).hexdigest()=='71abb690e78fdd573ab047df35446bfe295716b1a90ce25aa2808e162f5d2fd4'
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
s=(R/path).read_text();s=change(s,'proof and exact supplement pass the author check; independent\nwhole-proof review is pending.',
 'proof and exact supplement pass the author check; complete\nproof reviews by /root and /root/g34\\_eightfolds have also passed,\nwith a separate exact peer supplement.');(R/path).write_text(s)
gate=('D-OL14--15 closes the q3 odd-natural ordinary nonselfdual case atd>=1135, allowing arbitrary mixed such ranks, scalar extensions and factor permutations. '
      'Every inner element except an actual negative reflection has support>delta*a; arbitrary-order classification handles higher2-power roots directly by restricted natural support. '
      'Negative reflections have support>=beta*a, beta=4997/30000. Two active bad tensor factors already have support>1/4. '
      'The exact source budget forces exactly12bad inertias, each scalar times one negative-reflection factor. Actual generation would make <=12negative reflections generate the perfect naturalOmega factor, '
      'but their nonzero common perpendicular has a nontrivial scalar sign action, contradiction. '
      'Consequently EVERY remaining transitive ordinary odd-dimensional orthogonal factor over any odd field has d<=1133; selfdual factors retain d<=21. '
      'The earlier q3 fixed-fraction quarter estimate remains refuted, but no longer leaves this large ordinary source endpoint open. '
      'Odd-field even-natural ordinary and genuine spin cases retain their earlier bounds; no finite-source enumeration or existence claim. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert 'Q2cb' not in {r['id'] for r in rows}
(R/'research/gate_before_orthogonal_three_odd.json').write_text(json.dumps(next(r for r in rows if r['id']=='Q2i'),indent=2)+'\n')
for r in rows:
 if r['id']=='Q2i':
  s=r['finding_ids_or_current_gate']
  s=change(s,'The q3 rank-one fixed-fraction29525/88574>1/3 refutes that shortcut only; q3 odd-natural, odd-field even-natural and genuine spin cases retain earlier gates. ',gate)
  r['finding_ids_or_current_gate']=s
rows.append(dict(zip(fields,['Q2cb','Prompt target2; all-order orthogonal support and actual inertia generation',
 'Can q3 ordinary nonselfdual odd-natural factorsd>=1135 escape through the rank-one signed-radical boundary?',
 'refuted',gate+'Whole author/root/G34 proofs and author code/output PASS; independent natural-matrix supplement retained.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=R/'HODGE_DIVISION.tex';s=p.read_text();a=r'\input{agents/imprimitive/orthogonal_lowlevels/orthogonal_odd_nonselfdual_section.tex}'
s=change(s,a,a+'\n'+r'\input{'+path+'}')
s=change(s,'''explicitly false. The ordinary odd-$q$ even-natural case, this $q=3$
boundary, and genuine spin characters retain their previous bounds.''',r'''explicitly false. D-OL-14--15 nevertheless closes the large ordinary
$q=3$ odd-natural endpoint by a different argument. Only actual negative
reflections can have projective support below the stronger constant;
higher roots are covered by the full restricted-support character bound.
The exact budget leaves twelve bad inertias, each active on one factor.
Their generation would make at most twelve negative reflections generate
the perfect natural orthogonal factor. Their common nonzero perpendicular
instead carries a nontrivial scalar sign character, a contradiction.
Thus all ordinary odd-natural transitive cores over every odd field
satisfy $d\le1133$. Odd-field even-natural ordinary characters and
genuine spin characters retain their earlier bounds.''')
p.write_text(s)
events=[('D-OL14--15 root whole-proof and author-code review','targeted proof check',
 'Root complete frozen proof7d0e8c1e, every author checker line, full correct orthogonal_three_odd_checked.json and both THREE_ODD notes read. All-order classification, exact two-involution convolution, complete scalar-inner normalizers, actual12-generator/perfectness contradiction and scope PASS. Final author0.003415117s22:21:39UTC read, not rerun; initial0.004013822s22:20:11UTC retained separately by author.',path),
 ('Taylor11.46--11.48 characteristic-three perfectness','used and rechecked in this run',
 'Root freshly read complete local published-text passages Theorems11.46,11.47,11.48, printed161--162: Siegel generation, full perfectness proof includingF3 commutator, simplicity and exact small exceptions. Large odd dimensions lie inside scope. No fresh visual page inspection claimed. Earlier KTV, LST, GLT and LiXia source interfaces retained.', 'agents/imprimitive/orthogonal_lowlevels/cache/TaylorClassicalGroups.txt'),
 ('D-OL14--15 peer audit','targeted proof check',
 'Root entire G34 report71abb690 read. Full frozen proof, author code/output and source interfaces PASS. Separate252norm distributions,17D order8 root,15D twelve-reflection common3-space and exact budgets PASS0.007994914s22:25:19UTC first run. Fresh Taylor/LiXia and exact LST application review recorded; root has not whole-read peer code.',peer),
 ('D-OL14--15 integration','targeted proof check',
 'Only review status changed. Q2cb refuted, Q2i strictly reduced to d<=1133 for ordinary odd-natural transitive factors over every odd field. Earlier falseq3quarter estimate retained, no spin or even-natural claim. No TeX compilation.', 'scripts/integrate_orthogonal_three_odd.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Closing the large ordinary odd-natural q3 endpoint\n\n'+now+' — Q2cb refuted and Q2i strictly reduced. '+gate+'No formal review or off-schedule checkpoint.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Actual monodromy generation removes the q3 endpoint\n\n'+gate+'The proof uses the actual generating inertia tuple of a finite local system, not only a numerical profile; it restricts condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04). The common scheme/representation-lambda-ring/SGA-weight-one/motivic frame remains as stated. No new cycles or Markman, Severn or032 premise.\n')
out={'date_utc':now,'finding':'D-OL14--15','reviewed_sha256':frozen,'canonical_sha256':hashlib.sha256((R/path).read_bytes()).hexdigest(),
     'new_row':'Q2cb','strictly_reduced_main_gate':'Q2i','all_odd_field_ordinary_odd_natural_cutoff':1133}
(R/'research/orthogonal_three_odd_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
