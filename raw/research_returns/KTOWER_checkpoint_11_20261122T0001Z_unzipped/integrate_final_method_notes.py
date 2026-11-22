"""Add the newly checked scope/gap notes; none changes a main-question state."""
from pathlib import Path
from datetime import datetime, timezone
import csv,hashlib,json,subprocess,sys
B=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
review=json.loads((B/'evidence/root_final_method_review/review.json').read_text())
for row in review['whole_readings']:assert sha(B/row['path'])==row['sha256']
p=B/'assemble_paper.py';s=p.read_text()
assert "'evidence/lean_chain/class_pairing_scope.tex'," not in s
s=s.replace("'evidence/main_gate/order_five_greenberg_abstract_model.tex',", "'evidence/main_gate/order_five_greenberg_abstract_model.tex',\n'evidence/lean_chain/class_pairing_scope.tex',")
s=s.replace("'evidence/unitary_audit/dimension2_comparison/dimension_two_comparison.tex',", "'evidence/unitary_audit/dimension2_comparison/dimension_two_comparison.tex',\n'evidence/unitary_audit/dimension2_comparison/adjacent_factor_attempt.tex',")
s=s.replace("'evidence/geometry_tower/rm_frobenius_avoidance.tex',", "'evidence/geometry_tower/rm_frobenius_avoidance.tex',\n'evidence/geometry_tower/route2_all_order_attempt/rm_theta_propagation_limit.tex',")
needle=" text=re.sub(r'\\\\texttt"
where=s.index(needle)
insert=""" if name=='evidence/lean_chain/class_pairing_scope.tex':
  text=text.replace(r'\\label{KT-QUINTIC-CLASS-PAIRING-SCOPE}', r'\\label{KT-QUINTIC-CLASS-PAIRING-SCOPE}'+'\\n'+r'\\noindent\\textbf{KT-QUINTIC-CLASS-PAIRING-SCOPE.}\\quad')
 if name=='evidence/unitary_audit/dimension2_comparison/adjacent_factor_attempt.tex':
  for heading,fid in [
   ('The two displayed adjacent ideals are the same ideal.','KT-ADJACENT-FACTOR-SCOPE'),
   ('A source normalization error and its ramification repair.','KT-BK2026-NORMALIZED-DEPTH-REPAIR'),
   ('A separate sign gap in the displayed algebraic argument.','KT-BK2026-LONG-ROOT-SIGN-SCOPE')]:
   text=text.replace(r'\\paragraph{'+heading+'}',r'\\paragraph{'+heading+'}'+r'\\textbf{'+fid+'.} ')
"""
s=s[:where]+insert+s[where:];p.write_text(s)
p=B/'sections/framework.tex';s=p.read_text()
rows=r'''KT-QUINTIC-CLASS-PAIRING-SCOPE &
Cartier duals of finite Tate sheaves, unramified Selmer local
conditions, and the reciprocity pairing. &
The (FW.1)--(FW.2) integral cohomology dictionary and
Morgan--Smith2024, \S\S5.1--5.2.
The even order-five character has an odd Cartier dual.
The published symmetric reciprocity identity supplies no
perfect alternating self-pairing of the remaining class.\\
KT-ADJACENT-FACTOR-SCOPE;
KT-BK2026-NORMALIZED-DEPTH-REPAIR;
KT-BK2026-LONG-ROOT-SIGN-SCOPE &
Integral conormal lengths under coefficient extension,
and the sign of a block-algebra anti-involution. &
EGA IV$_4$,16.1.2 supplies conormal terminology;
the precise arithmetic hypotheses are those audited in
Berger--Klosin2026, \S\S6,8--10.
The numerical scalar-extension repair is conditional on
the retained arithmetic inputs. The block-sign countermodel
identifies an algebraic proof gap without asserting an
arithmetic counterexample. No extra congruence length is obtained.\\
KT-RM-THETA-STABILIZER &
The principally polarized Jacobian, its actual Raynaud theta
translate, Rosati-fixed real multiplication, and radicial
maps of curves. &
AN\_GRH A35(T2F.3--4), A42(PE.14--15), A45--A52;
cote149 scans35--36 and the route-two substitute A33.
Only $\pm1$ in $\mathcal O_5$ preserve theta up to translation.
This prevents automatic propagation by real multiplication;
exceptional torsion incidences and the universal cover gate remain.\\
'''
s=s.replace('Ihara gate &',rows+'Ihara gate &');p.write_text(s)
with (B/'QUESTIONS.tsv').open(newline='') as f:
 reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;qs=list(reader)
for q in qs:
 if q['id'] in ['KT-Q1B','KT-Q1C']:
  q['finding_ids']+='; KT-QUINTIC-CLASS-PAIRING-SCOPE; KT-ADJACENT-FACTOR-SCOPE; KT-BK2026-NORMALIZED-DEPTH-REPAIR; KT-BK2026-LONG-ROOT-SIGN-SCOPE'
  q['current_gate_or_scope']+=' The class reciprocity pairing gives no alternating self-duality of the even order-five component. The proposed ordinary comparison has additional weight/local and source-sign gaps; no unconditional existing K certificate depends on the disputed sign step.'
 if q['id']=='KT-Q7':
  q['finding_ids']+='; KT-RM-THETA-STABILIZER'
  q['current_gate_or_scope']+=' Only plus/minus1 in Rosati-fixed O5 can preserve the actual ordinary theta curve up to translation; this blocks automatic RM propagation but does not exclude exceptional torsion incidences or settle the all-orbit condition. NONMOVEMENT.'
with (B/'QUESTIONS.tsv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(qs)
with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Final bounded method checks and source correction — '+now+'\n\n')
 f.write('Whole root checks pass for the class-pairing scope, the adjacent-factor/normalization/sign note, and the RM theta-preservation limitation. Independent peer checks are complete for the first two notes; the separately requested RM peer check is pending at this entry time. Root freshly replayed all16 finite algebra checks and directly viewed the source PDF pages36 and50. Exact readings and limits are in evidence/root_final_method_review/review.json.\n\n')
 f.write('A source proof gap is now recorded: BK2026 Lemma6.8 does not deduce a common positive polarization sign from an involution on its M2-times-field case. This is an algebraic inference counterexample, not an arithmetic theorem counterexample. The previous manifest phrase calling Theorem6.4 a published injection is superseded; its sign-bearing injection remains an explicit unverified hypothesis in the conditional comparison. The Section2 conormal proof, independent Urban sign argument, quintic comparisons and completed finite K certificates are unaffected by the audited dependency search. The Eq9.3 cardinality error has a conditional normalized-depth repair.\n\n')
 f.write('None of these closes an old-open row or makes an original main arithmetic gate strictly smaller. They are NONMOVEMENT for the scheduled review. The universal route2 incidence question, remaining Ihara question and all-weight Vandiver remain open.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## Pairing, source-sign, and theta-propagation limits\n\n')
 f.write('The possible order-p quintic class is not excluded by Morgan–Smith reciprocity: its Cartier dual has opposite parity, and the cited roots-of-unity construction is symmetric. The conditional GMA route gains no extra adjacent factor. A precisely scoped block-sign gap in the cited preprint is recorded and its prior-use audit retained; no completed arithmetic result depends unconditionally on that step. The numerical coefficient-extension error is repaired with ramification-normalized depth, retaining the separate arithmetic and sign inputs.\n\n')
 f.write('For route2, the Rosati-fixed O5 action preserves the actual ordinary genus-two Raynaud theta curve up to translation only for plus/minus1. Thus real multiplication alone cannot propagate a seed through all required torsion incidences. This does not rule out exceptional points or construct a curve avoiding every odd cover. The Grothendieck/SGA/EGA and prior-row dictionary states these exact limitations without promoting them to new K-group, Ihara, or section conclusions.\n')
subprocess.run([sys.executable,str(B/'merge_checks.py')],cwd=B,check=True)
subprocess.run([sys.executable,str(B/'assemble_paper.py')],cwd=B,check=True)
print(json.dumps({'integrated_utc':now,'movement':False,'tex_sha256':sha(B/'KTOWER.tex')}))
