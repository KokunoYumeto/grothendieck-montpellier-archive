from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path('final');W=Path('work')
for s,d in [
 ('effective_galois/BUILD_A01_A31_AUDIT.md','evidence/BUILD_A01_A31_AUDIT.md'),
 ('effective_galois/CHECK_EVENTS_BUILD_A01_A31.tsv','evidence/check_events/CHECK_EVENTS_BUILD_A01_A31.tsv'),
 ('gt_certificates/positive_rank_theta/PDF_A26_A31_PAGES51_64_VISUAL_QA.md','evidence/PDF_A26_A31_PAGES51_64_VISUAL_QA.md'),
 ('gt_certificates/positive_rank_theta/CHECK_EVENTS_POSITIVE_RANK.tsv','evidence/check_events/CHECK_EVENTS_POSITIVE_RANK.tsv'),
 ('gt_certificates/positive_rank_theta/A32_WHOLE_PROOF_REVIEW.md','evidence/A32_WHOLE_PROOF_REVIEW.md'),
 ('row_audit/A32_ORDINARY_RATIONAL_WITNESS.tex','proof_sources/ordinary_rational_witness.tex'),
 ('row_audit/CHECK_EVENTS_A32.tsv','evidence/check_events/CHECK_EVENTS_A32.tsv'),
 ('row_audit/CHECK_EVENTS_A32_CITATION.tsv','evidence/check_events/CHECK_EVENTS_A32_CITATION.tsv'),
 ('row_audit/A32_MANIFEST.json','evidence/A32_MANIFEST.json'),
 ('row_audit/A32_REPRODUCTION_LOG.json','evidence/A32_REPRODUCTION_LOG.json')]:
 shutil.copy2(W/s,R/d)
D=R/'certificates/A32';D.mkdir(exist_ok=True)
for n in ['probe_A27_character13.py','probe_A27_theta13.py','probe_A27_character13.json','verify_A27_character13_linear.py','verify_A27_character13_linear.json','A32_ALL_POINT_IMAGES.json']:
 shutil.copy2(W/'row_audit'/n,D/n)
p=R/'evidence/root_check_events.json';ev=json.loads(p.read_text())
who='GPT-6 Astra Pro; effort not exposed; AN_GRH /root'
assert not any(x['statement_id']=='A32' and 'c14a25d7' in x['outcome'] for x in ev)
ev.extend([
 dict(statement_id='A32',date='2026-11-21',who_model_effort_run=who,type='targeted proof check',outcome='PASS after reading the complete four-step proof, all Mumford arithmetic justifications and final citation-only clarification. Checked the encoded quotient, group exponent and point counts, independent interpolation/norm-reduction logic including multiplicities and the branch point, the character polynomial, all twelve scalars, F8 trace/minimal polynomial, and the exact constant-extension rule. The cohomological map is the linear extension of q-power Frobenius; its character lines exclude hidden Jordan blocks. Full final source SHA256 c14a25d7eef5b20f2e81e4d6226809649d4b77922f6667603ac5db311e4ea32c.',evidence='proof_sources/ordinary_rational_witness.tex'),
 dict(statement_id='A32',date='2026-11-21',who_model_effort_run=who,type='computation or formal certificate',outcome='Read the complete independent binary-interpolation checker and reran it successfully before the final citation-only edit; outputs reproduced the quotient generator, all256 point images, character distribution and polynomial1+T4+T12. This checker is independent of the producer extended-GCD implementation, but the root rerun is not another independent implementation. No formal verification claim.',evidence='certificates/A32/verify_A27_character13_linear.py; certificates/A32/verify_A27_character13_linear.json'),
 dict(statement_id='KATZ-SGA7II-XXII-2.2.4-5',date='2026-11-21',who_model_effort_run=who,type='used and rechecked in this run',outcome='Opened the author-hosted primary scan and read both complete propositions and their proofs on pages407–409, including the Frobenius convention and the Artin–Schreier stable-part comparison. Used with recovered successor A.20 in A32.',evidence='https://web.math.princeton.edu/~nmk/old/congzeta.pdf; SGA7II, ExposeXXII, Propositions2.2.4–2.2.5'),
 dict(statement_id='DELIGNE-SGA4HALF-MODP-2.2B',date='2026-11-21',who_model_effort_run=who,type='used and rechecked in this run',outcome='Read the complete primary IAS-indexed Theorem2.2(b), Section2.1 hypotheses and formula2.4.1 after the full-volume PDF exceeded the web size limit. Checked finite reduced characteristic-two coefficient field, constructible lisse rank-one sheaf and finite Tor dimension in A32. This is a theorem-statement/hypothesis check, not a whole reading of Deligne’s theorem proof.',evidence='https://publications.ias.edu/sites/default/files/Number32.pdf; SGA4half Fonctions L modulo ell^n et modulo p, p116')
])
p.write_text(json.dumps(ev,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
entry='\n## Evidence staging at '+now+'\n\nThe canonical standalone source and88-page PDF match throughA31 (TeX447fed6f4d8c8b3479fe08d96eb10c8cf8c7ae21840de43c7f2822615484e287; PDFed7908c3570a783dce30ef1c7289d6d583cad36281cd7319004f5edbdc92ded7). All88pages and selected full pages passed visual review. A32 is fully checked, with two arithmetic implementations and exact Katz/Deligne source checks; its source and certificates are now staged in final, pending next paper assembly. It gives an ordinary12-dimensional new factor with odd rational order overF256, becoming even exactly at constant degrees divisible by7. A33 has a full draft and root whole-proof PASS except a requested scope wording correction in the normal-core sentence; row reading pending. A34 bounded rational Prym-exponent proof is in preparation. A concrete A27 degree19 probe overF64 has c1 of mod2 order7 and1+c1^7=2 modulo4, suggesting actual exponent2 after degree7 and strictness of A34; independent computation and complete proof still pending. A35 rank-one pure2-primary theta finite-field lemma is being written. These pending findings are not yet promoted in the canonical paper.\n'
for f in [R/'LEDGER.md',Path('AN_GRH_SESSION_STATE.md')]:
 with f.open('a') as out:out.write(entry)
print('A32 checked evidence staged; current canonical paper remains A01–A31.')
