"""Integrate three fully checked bounded comparisons; no main gate or row closes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,difflib,subprocess,sys

B=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
specs=[
 ('evidence/main_gate/quintic_ramification_attempt/quintic_tame_configuration_limit.tex','67a94c9b', ['KT-QUINTIC-TAME-CONFIGURATION-LIMIT']),
 ('evidence/lean_chain/quintic_iwasawa_specialization_scope.tex','573cfda923eb6976dd0821bbf1e41e8b8f4cecf6b5cd4e2b352913b08805c32f',['KT-QUINTIC-IWASAWA-SPECIALIZATION-SCOPE']),
 ('evidence/unitary_audit/actual_polarization_repair/actual_image_polarization.tex','61e0320827db5f5e63e34b58d2c6200818521c0ac07f6f7c7eb2871921c6b25a',['KT-ACTUAL-IMAGE-SYMMETRIC-POLARIZATION','KT-ACTUAL-LONG-ROOT-SELMER-INJECTION','KT-ACTUAL-LOWER-LONG-FACTORIZATION'])
]
for rel,expected,_ in specs:
 assert sha(B/rel).startswith(expected),(rel,sha(B/rel))
reviews=['evidence/lean_chain/quintic_tame_configuration_peer_review.json','evidence/unitary_audit/iwasawa_peer_review/review.json','evidence/geometry_tower/actual_polarization_review/review.json','evidence/geometry_tower/actual_polarization_review/location_addendum.json']
for rel in reviews:assert (B/rel).is_file(),rel
D=B/'evidence/root_post11_review';D.mkdir(exist_ok=True)
root={'checked_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro','effort':'not exposed','outcome':'PASS','movement':False,'whole_readings':[], 'scope':'Whole mathematical predecessors actually read, followed by exact sole arithmetic-geometric location insertions; no foundational theory or Lean kernel replay is claimed.'}
details={
 specs[0][0]:'Whole511c2e5f predecessor read; exact arithmetic_geometric_location.diff read in full. Dummit–Kisilevsky publisher Introduction, Definitions2.1–2.4, Remark4.1 and nearby splitting explanation directly read. Milne foundations imported at exact peer-checked locators.',
 specs[1][0]:'Whole5df12bc2 predecessor proof read; exact quintic_iwasawa_location.diff read. Norm control, compact Nakayama, coefficient triviality and nontrivial Delta5 averaging, p-split finite-level descent, negative specialization sign and evaluation ideal checked. Marshall2004 printed1–3 read entirely, including Theorem1 hypotheses; no proof of that theorem imported.',
 specs[2][0]:'Whole1b92cb33 proof plus sole AP.12 comma/alignment repair read and verified; exact arithmetic_location.diff then read entirely. Direct pinned source and BC2011 Proposition2.4 scopes in actual_image_polarization_review.json. The actual image repair preserves the universal CH and adjacent rational gaps.'
}
for rel,_,ids in specs:
 root['whole_readings'].append({'path':rel,'sha256':sha(B/rel),'finding_ids':ids,'actual_scope':details[rel]})
root['peer_records']=[{'path':rel,'sha256':sha(B/rel)} for rel in reviews]
(D/'integration_review.json').write_text(json.dumps(root,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for row in root['whole_readings']:
  for fid in row['finding_ids']:
   w.writerow([fid,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS whole mathematical predecessor and sole location insertion; exact scope in review; NONMOVEMENT','evidence/root_post11_review/integration_review.json'])
 w.writerow(['MARSHALL-2004-INVERSE-LIMIT-SCOPE',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS entire printed1–3; inverse class-field convention and Theorem1 statement read; theorem assumes Vandiver, lambda1 and local-unit bound; no theorem proof imported','evidence/lean_chain/primary/iwasawa_scope/Marshall_2004.txt; evidence/root_post11_review/integration_review.json'])

p=B/'assemble_paper.py';s=p.read_text()
assert specs[0][0] not in s
s=s.replace("'evidence/main_gate/order_five_greenberg_abstract_model.tex',", "'evidence/main_gate/order_five_greenberg_abstract_model.tex',\n'"+specs[1][0]+"',\n'"+specs[0][0]+"',")
s=s.replace("'evidence/unitary_audit/dimension2_comparison/adjacent_factor_attempt.tex',", "'evidence/unitary_audit/dimension2_comparison/adjacent_factor_attempt.tex',\n'"+specs[2][0]+"',")
p.write_text(s)

p=B/'sections/framework.tex';s=p.read_text()
assert '$[-32],[-34],[-36],[-38]$' in s
s=s.replace('$[-32],[-34],[-36],[-38]$','$[-32],[-34],[-36],[-38],[-40]$')
rows=r'''KT-QUINTIC-TAME-CONFIGURATION-LIMIT &
An unramified $C_p$-torsor over $\operatorname{Spec}\mathcal O_F$,
with tame Frobenius-group descent over $\operatorname{Spec}\mathbf Z[1/p]$. &
The order-five class component of (FW.1)--(FW.2),
K17-VK-PT and SGA4, ExposeIX,3.2--3.3.
The exact local splitting and discriminants are compatible
with every primitive order-five label. No arithmetic case is excluded.\\
KT-QUINTIC-IWASAWA-SPECIALIZATION-SCOPE &
The actual integral norm limit of class groups and its
negative Tate-character specialization. &
(FW.1)--(FW.2), K17-VK-PT and the cyclotomic part of the
Teichmuller-tower gate. The cyclic presentation retains finite
submodules. The existing exponent bound for $p\mid e$ follows
automatically and does not bound $\lambda$ or evaluate capitulation.\\
KT-ACTUAL-IMAGE-SYMMETRIC-POLARIZATION;
KT-ACTUAL-LONG-ROOT-SELMER-INJECTION;
KT-ACTUAL-LOWER-LONG-FACTORIZATION &
An integral conjugate-dual pairing on the actual rank-three
etale sheaf and its matrix-image extension modules. &
The quadratic-twisted long-root strict group is killed by
the auxiliary unit. Its ideal becomes the square of the
adjacent ideal. The rational adjacent group in (FW.2),
dual to (FW.1), survives this comparison. No universal
Cayley--Hamilton kernel or original K-group obstruction is removed.\\
'''
s=s.replace('Ihara gate &',rows+'Ihara gate &');p.write_text(s)

p=B/'evidence/main_gate/ordinary_eisenstein_ideal_attempt.tex';old=p.read_text();assert 'cited in Attempt HI.' in old
new=old.replace('cited in Attempt HI.','cited in Attempt HS1.');p.write_text(new)
(D/'hs1_reference_editorial.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))

with (B/'QUESTIONS.tsv').open(newline='') as f:
 rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;questions=list(rd)
newids=[fid for _,_,ids in specs for fid in ids]
for q in questions:
 if q['id'] in {'KT-Q1B','KT-Q1C'}:
  ids=q['finding_ids'].split('; ')
  for fid in ['KT-ORDER-FIVE-PDIV-WEIGHT']+newids:
   if fid not in ids:ids.append(fid)
  q['finding_ids']='; '.join(ids)
  q['current_gate_or_scope']=q['current_gate_or_scope'].replace('All-weight arithmetic prime elimination Known','All-weight arithmetic prime elimination remains open. Known').replace('additional weight/local and source-sign gaps','additional weight/local and universal Cayley-Hamilton source-sign gaps')
  q['current_gate_or_scope']+=' The fixed symmetric source pairing and integral local projectors now repair the long-root injection for the actual finite-DVR matrix image; its lower long ideal equals the square of the adjacent ideal under the auxiliary2e unit. This leaves the adjacent rational strict group and universal Cayley-Hamilton kernel untouched. The actual cyclic Iwasawa presentation explains the p-divisible-weight exponent bound without any new lambda bound. Exact tame Frobenius-group splitting/discriminants remove no order-five character. These are NONMOVEMENT.'
with (B/'QUESTIONS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(questions)

with (B/'LEDGER.md').open('a') as f:
 f.write('\n\n## Actual-image repair and exact quintic control integrated — '+now+'\n\nThree complete bounded notes have whole root and independent peer PASS records. The source’s literal integral symmetric J and local spectral projectors repair the long-root sign and strict injection for its actual finite-DVR matrix image; the universal Cayley–Hamilton comparison remains separate. Under the auxiliary2e unit, the lower long ideal equals the square of the adjacent ideal. No adjacent rational class is killed.\n\nThe actual quintic norm limit has X/TX=A0, and the surviving character module is cyclic over Lambda. Strict weight specialization is exact with t_e=(1+p)^(-e)-1. The p-divisible-weight bound is automatic from I(0)=(p); no characteristic-ideal constant term or lambda bound is inferred. The tame C_p⋊C5 description computes exact splitting and discriminants and accommodates all primitive labels. All three notes are NONMOVEMENT.\n\nThe pre-integration consistency review found only minor references/listing defects: the framework now includes[-40], the stale HS1 label is corrected, Q1C begins with a complete sentence, and the existing p-divisible-weight finding is explicitly indexed. Source proof predecessors and precise insertion/typography lineage are retained. No Lean execution or new finite K job occurred.\n')
with (B/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n## Exact remaining comparison after the actual-image repair\n\nThe disputed sign inference is no longer needed for the actual matrix-image long-root module: the normalized source supplies its perfect symmetric pairing, and integral local projectors prove strictness. This yields a31=a21² under the corresponding auxiliary unit. It neither proves the same statement for an arbitrary universal Cayley–Hamilton quotient nor kills the adjacent rational Selmer module. The original all-weight and Ihara gates stay open.\n\nThe order-five Iwasawa module is now compared at the level of the actual compact module, including its finite submodules. Cyclicity and all p-divisible-weight exponent-one specializations follow from the already established base class bound and norm control. They impose no additional vanishing or lambda bound. The tame Frobenius-group cover description is compatible with every remaining order-five label; its exact discriminants provide no contradiction. These refinements preserve, rather than remove, the integral Tate-sheaf obstruction in FW.1–FW.2.\n')
subprocess.run([sys.executable,str(B/'merge_checks.py')],cwd=B,check=True)
subprocess.run([sys.executable,str(B/'assemble_paper.py')],cwd=B,check=True)
print(json.dumps({'integrated_utc':now,'tex_sha256':sha(B/'KTOWER.tex'),'root_review_sha256':sha(D/'integration_review.json'),'movement':False}))
