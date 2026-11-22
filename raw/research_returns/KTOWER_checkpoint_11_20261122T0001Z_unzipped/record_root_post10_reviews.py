"""Record actual whole readings, without substituting peer/source checks for root checks."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

B = Path(__file__).resolve().parent
D = B / 'evidence/root_post10_review'
D.mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
entries = [
 ('evidence/main_gate/order_five_greenberg_gate.tex',
  'KT-ORDER-FIVE-GREENBERG-UNIT-GATE',
  '5b1bb860c9233acdc85027fd1f9fdc81132122621f333c7eab226a57358828cf',
  ['Entire written proof read, including its specialized ambiguous-class sequence.',
   'The unique ramified prime is principal by the ideal norm of 1-zeta; all base units are norms of field elements by local reciprocity and Hasse norm.',
   'The maximal base-abelian subfield of the Hilbert p-class field is F_n H_0; inertia and total ramification give the coinvariant order.',
   'The ambiguous-class map, its Hilbert90 kernel, and surjectivity via the ideal permutation module prove the exact unit-norm quotient.',
   'The equivalences use the stated one-prime capitulation criterion; they do not evaluate the unit-norm index or prove base-class vanishing.']),
 ('evidence/main_gate/order_five_greenberg_abstract_model.tex',
  'KT-ORDER-FIVE-ABSTRACT-NORM-LIMIT',
  'b99339d3369f1e66a09a3fbb233361a4b9ad5a905bb6814df996b0747e5d8bb2',
  ['Entire written proof read.',
   'The binomial induction gives v_p((1-p)^(p^n)-1)=n+1 for odd p.',
   'Quotient norms and multiplication transfers are well-defined, compose, and satisfy both degree and group-norm identities.',
   'Transfers are injective, fixed groups have order p, and characteristic polynomial T+p gives lambda1,mu0.',
   'The commuting primitive order5 action exists because p is1 mod10; no arithmetic realization or Greenberg counterexample is asserted.']),
 ('evidence/lean_chain/hadamard_modularity_scope.tex',
  'KT-SATURATED-RANKIN-COHEN-SCOPE',
  '4b96075875ff1c3d07cc6b1bc2f146b390d8e6c78197bc02063bf189b761d6e2',
  ['Entire final written note read; earlier whole reading of predecessor88609e7c was supplemented by the explicit k1mod4 source qualification.',
   'Factorial denominators are p-units; numerator factors prove every asserted exact valuation and the zero interval after saturation.',
   'The equal-index indicator is correct on x+y nonzero; restriction to X+Y=1 and homogenization are injective in the stated degree.',
   'The r=p-3,p-2 coefficients force incompatible scalar values0,2.',
   'The proof rules out only this universal formal operator. Root did not replay the p31 control or freshly read all four primary papers; geometry peer source/replay scopes are distinguished.']),
 ('evidence/unitary_audit/dimension2_comparison/dimension_two_comparison.tex',
  'KT-GMA-MULTIGENERATOR-CONORMAL',
  'cda4a3fe08e922673a99889a9b0685f6487977188dd033941a5e964a6b6ac963',
  ['Entire final written note read, including both precise source corrections; predecessor94691d8 was also whole-read.',
   'Cyclic first factor and d-generated second factor give N onto conormal and B^d onto K; Hom exactness yields the displayed cardinality bound.',
   'No surjectivity at the final Hom term is claimed; the DVR finiteness argument and finite dual cardinality are correct.',
   'The conditional numerical criterion counts the adjacent divisible Selmer length d times.',
   'The original two L-value congruence factors supply one copy each. Root completed the primary Theorem10.2 proof through10.7 and its concluding sentence.',
   'The actual ordinary dimension is only known to be at least2; neither an upper bound2 nor applicability of a cited R=T theorem is proved.'])
]
records = []
for rel, fid, expected, checks in entries:
 p = B / rel
 assert sha(p) == expected, (rel, sha(p))
 shutil.copyfile(p, D / p.name)
 records.append({'finding_id':fid, 'proof_path':rel, 'proof_sha256':expected,
                 'outcome':'PASS', 'check_type':'targeted proof check: entire written proof',
                 'checks':checks})
peer_paths = [
 'evidence/lean_chain/order_five_greenberg_peer_review.json',
 'evidence/unitary_audit/quintic_review/greenberg_peer_review.json',
 'evidence/unitary_audit/quintic_review/greenberg_abstract_model_peer_review.json',
 'evidence/geometry_tower/rankin_cohen_review/review.json',
 'evidence/lean_chain/dimension_two_comparison_peer_review.json']
report = {
 'date_utc':now, 'who':'/root; run KTOWER', 'model':'GPT-6 Astra Pro',
 'effort':'setting not exposed', 'whole_readings':records,
 'root_primary_scopes':[
  {'source':'Ichimura2002, Acta Arith105.1,29-34',
   'pdf_sha256':sha(B/'evidence/main_gate/literature/quintic_greenberg/Ichimura_2002.pdf'),
   'scope':'Complete pages29-31, including Theorems1-2, Proposition1, Remark1, Lemmas1-2 and the displayed complete proofs of Lemma2, Theorem2 and Proposition1. Bounded-unit-index lemma and original Greenberg1976 theorem remain imported.'},
  {'source':'Gras arXiv2211.12279v3',
   'pdf_sha256':sha(B/'evidence/main_gate/literature/quintic_greenberg/Gras_2023_capitulation.pdf'),
   'scope':'Equation1.1 and its general setup only freshly read by root. Wider author/peer readings of pp2-5,23-25 are not attributed to root.'},
  {'source':'Berger-Klosin arXiv2611.19007v1',
   'pdf_sha256':sha(B/'evidence/unitary_audit/reducible_comparison/primary/berger_klosin_2026_arxiv.pdf'),
   'scope':'Assumption2.7; Lemma2.9, Remark2.10, Lemma2.11; entire Proposition2.12 proof; Lemma2.14, Proposition2.15 and Corollary2.16 proofs, pp6-9; entire Theorem7.8 proof p39; entire Theorem10.2 proof pp53-55, including inequalities10.5-10.7 and final conclusion. Other deep inputs remain imported.'}],
 'peer_reports':[{'path':rel, 'sha256':sha(B/rel)} for rel in peer_paths],
 'fresh_root_computation_replays':[],
 'movement':False,
 'boundary':'These results clarify hypotheses and conditional algebra; none eliminates the remaining order5 or order>=7 class obstruction, supplies the simultaneous unit, or proves Ihara positive-rank/route2.'}
(D/'review.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for r in records:
  w.writerow([r['finding_id'],now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed',
              'targeted proof check','PASS entire final written proof at SHA'+r['proof_sha256']+'; NONMOVEMENT; exact primary and peer scopes distinguished',
              'evidence/root_post10_review/review.json'])
 for fid in ['ICHIMURA-2002-ONE-PRIME-CAPITULATION','GRAS-2023-AMBIGUOUS-UNIT-EXACT-SEQUENCE','BK2026-CONORMAL-NUMERICAL-PROOFS']:
  w.writerow([fid,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed',
              'used and rechecked in this run','PASS exact primary scope recorded; imported inputs distinguished',
              'evidence/root_post10_review/review.json'])
print(json.dumps({'review_sha256':sha(D/'review.json'),'whole_proofs':len(records),'movement':False}))
