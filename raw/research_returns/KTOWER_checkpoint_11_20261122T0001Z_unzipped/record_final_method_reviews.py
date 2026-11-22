"""Bind actual root whole readings and the fresh 16-identity replay."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, shutil
B=Path(__file__).resolve().parent
D=B/'evidence/root_final_method_review';D.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
entries=[
 ('evidence/lean_chain/class_pairing_scope.tex',
  ['KT-QUINTIC-CLASS-PAIRING-SCOPE'],
  'b163e62064906a5b89197d04f9b805e8daf5c63eb1303b91fa7dea08bfc75f17',
  ['Entire written note read; final sole formatting correction checked.',
   'Reciprocity pairs the dual class group with the class group; Kummer Selmer has a unit kernel.',
   'The roots-of-unity hypothesis is on the whole extension ab, and the stated identity is symmetric.',
   'The even order5 character has odd Cartier dual; the suggested alternating perfect self-pairing is not supplied.',
   'The one-dimensional symmetric example is only linear algebra. No class-group vanishing is inferred.']),
 ('evidence/unitary_audit/dimension2_comparison/adjacent_factor_attempt.tex',
  ['KT-ADJACENT-FACTOR-SCOPE','KT-BK2026-NORMALIZED-DEPTH-REPAIR','KT-BK2026-LONG-ROOT-SIGN-SCOPE'],
  'f239a4d675ef6f7061cff625ecbe0abf663de28f272bd4357c3a48f0696c5a79',
  ['Entire predecessor proof and all final changes read, including the complete final sign countermodel and normalized-depth repair.',
   'Equal adjacent ideals do not square under addition. The DVR matrix order has the stated products and nonalternating square.',
   'The two integral L-value factors give only one copy of each Selmer bound; the numerical counterassignment is valid.',
   'The Tate substitution, transfer character, residual ratios, and two failures of the stated weight cone are correct.',
   'Cardinality under finite free scalar extension is a degree-th power; length scales by ramification.',
   'With N=rn, retained depth e(Edoubleprime/E)n contradicts a fixed extended annihilator for n>C; finite free cochains, kernels and sign projectors commute with scalar extension.',
   'The primitive-class and sign inputs are retained, not supplied by the normalization repair.',
   'The block anti-involution has centralizer square diag(-1,1,-1), is determinant preserving and reverses the long-root signs. It refutes the displayed algebraic inference, with no arithmetic realization asserted.']),
 ('evidence/geometry_tower/route2_all_order_attempt/rm_theta_propagation_limit.tex',
  ['KT-RM-THETA-STABILIZER'],
  '7d472074573e8f34af0dabb6359023b6592dc4860ba84141bceae61c2941f877',
  ['Entire written proof read.',
   'Push-pull and the injective polarization map give u squared equal to d, after distinguishing curve degree from isogeny degree.',
   'Genus2 Riemann-Hurwitz makes the separable degree1; the remaining degree is a2-power and the map is radicial.',
   'The equation in Q(sqrt5) gives u=plus/minus2^b. For b>0 the three actual theta2-torsion points contradict geometric-point injectivity.',
   'Symmetry of the actual Raynaud translate and principal polarization eliminate a nonzero translation for u=plus/minus1.',
   'An infinite intersection on the irreducible theta curve would force the excluded global preservation.',
   'The proof neither excludes exceptional torsion incidences nor settles simultaneous incidence for all primitive doubling orbits.'])]
out=[]
for rel,ids,expected,checks in entries:
 p=B/rel;assert sha(p)==expected,(rel,sha(p));shutil.copyfile(p,D/p.name)
 out.append({'path':rel,'sha256':expected,'finding_ids':ids,'whole_proof_verdict':'PASS','checks':checks})
replay=json.loads((D/'adjacent_factor_checks.json').read_text())
assert replay['passed'] and replay['check_count']==16
report={'date_utc':now,'who':'/root; run KTOWER','model':'GPT-6 Astra Pro','effort':'not exposed',
 'whole_readings':out,
 'primary_scope':[
  {'source':'Morgan-Smith2024 DOI10.1007/s40993-024-00545-2',
   'scope':'Official publisher text: reciprocity definitions, duality conventions, complete requested Sections5.1-5.2, Lemma5.4, Propositions5.5-5.6 and Proposition1.3 deduction; affiliation-only correction separately read. General machinery remains imported.'},
  {'source':'Berger-Klosin arXiv2611.19007v1',
   'scope':'Earlier root complete Section2 algebra and Theorem7.8/10.2 proofs retained. Newly whole-read Proposition6.7/Lemma6.8 and Theorem6.4 setup; entire displayed Eq9.3 context and subsequent coefficient-extension/primitive-class passage. Printed pages36 and50 freshly rendered and visually inspected. The authors/peer read the wider weight and ordinary source setup; those wider readings are not attributed to root.'},
  {'source':'Milne/Stacks abelian-variety and curve inputs to RT',
   'scope':'Standard cited inputs imported at the exact locators recorded by the author; no fresh whole source-proof read is claimed by root. The carried A35 actual theta/2-torsion and A42 odd-torsion facts are accepted prior-run inputs.'},
  {'source':'Fujima-Ichimura2025 Math.J.Ibaraki57,1-24',
   'scope':'Root read complete printed pages1-6 of the exact local primary text: the class prime must differ from the conductor for the polynomial criteria and be primitive modulo degree-prime squared for the relevant uniform propositions. No later proof audit. This does not cover class prime equal to conductor.'}],
 'fresh_replay':{'scope':'All16 exact identities in the wholly read copied script',
  'script_sha256':sha(D/'adjacent_factor_checks.py'),'report_sha256':sha(D/'adjacent_factor_checks.json'),
  'all_check_values_match_author':True,'byte_identity_not_claimed':'UTC differs by design'},
 'visual_source_checks':[{'path':str((D/f'BK2026_printed_{n}.png').relative_to(B)),
  'sha256':sha(D/f'BK2026_printed_{n}.png')} for n in [36,50]],
 'supersession':'The BK2026 Lemma6.8 block-case sign step is now a recorded source proof gap, not an established unconditional injection. Section2 algebra and the explicitly conditional D2 criterion remain valid. See the separate full prior-dependency audit.',
 'movement':False}
(D/'review.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for r in out:
  for fid in r['finding_ids']:
   w.writerow([fid,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check',
    'PASS entire written proof at SHA'+r['sha256']+'; exact source gap/conditional limits retained; NONMOVEMENT','evidence/root_final_method_review/review.json'])
 w.writerow(['BK2026-LEMMA6.8-BLOCK-SIGN-INFERENCE',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed',
  'refuted, with refined statement KT-BK2026-LONG-ROOT-SIGN-SCOPE',
  'GAP in stated algebraic inference, verified by exact countermodel and full displayed proof read; no arithmetic theorem counterexample','evidence/root_final_method_review/review.json'])
 w.writerow(['KT-BK2026-LONG-ROOT-SIGN-SCOPE',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','computation or formal certificate',
  'PASS fresh copied-script replay of all16 exact finite identities; whole script read','evidence/root_final_method_review/adjacent_factor_checks.json'])
 for fid in ['MORGAN-SMITH2024-CLASS-PAIRING-SCOPE','FUJIMA-ICHIMURA2025-CONDUCTOR-PRIME-SCOPE']:
  w.writerow([fid,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS exact limited primary scope recorded','evidence/root_final_method_review/review.json'])
 for fid in ['AN-GRH-A35-T2F3-4','AN-GRH-A42-PE14-15']:
  w.writerow([fid,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','carried as background without fault found','Accepted prior-run theta input to RT; no fresh derivation claimed','evidence/root_final_method_review/review.json'])
print(json.dumps({'root_review_sha256':sha(D/'review.json'),'whole_notes':len(out),'fresh_replay_checks':16,'movement':False}))
