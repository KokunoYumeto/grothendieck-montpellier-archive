from pathlib import Path
from datetime import datetime,timezone
import json,shutil,hashlib
R=Path('final');W=Path('work')
for s,d in [('effective_galois/A30_GENUS_THREE_POINTING_COUNTEREXAMPLE.tex','genus_three_pointing_counterexample.tex'),('row_audit/A31_A27_THETA_SEVEN.tex','a27_theta_seven.tex')]:
 shutil.copy2(W/s,R/'proof_sources'/d)
for s,d in [
 ('effective_galois/A29_independent_audit.md','evidence/A29_independent_audit.md'),
 ('effective_galois/A30_PROOF_AUDIT.md','evidence/A30_PROOF_AUDIT.md'),
 ('effective_galois/CHECK_EVENTS_A29_A30.tsv','evidence/check_events/CHECK_EVENTS_A29_A30_EFFECTIVE.tsv'),
 ('row_audit/A29_WHOLE_PROOF_REVIEW.md','evidence/A29_WHOLE_PROOF_REVIEW.md'),
 ('row_audit/CHECK_EVENTS_A28_A29.tsv','evidence/check_events/CHECK_EVENTS_A28_A29.tsv'),
 ('row_audit/CHECK_EVENTS_A31.tsv','evidence/check_events/CHECK_EVENTS_A31.tsv'),
 ('gt_certificates/positive_rank_theta/A28_WHOLE_SOURCE_REVIEW.md','evidence/A28_WHOLE_SOURCE_REVIEW.md'),
 ('gt_certificates/positive_rank_theta/A29_PROOF_AUDIT.md','evidence/A29_PROOF_AUDIT.md'),
 ('gt_certificates/positive_rank_theta/A30_WHOLE_PROOF_REVIEW.md','evidence/A30_WHOLE_PROOF_REVIEW.md'),
 ('gt_certificates/positive_rank_theta/A31_WHOLE_PROOF_REVIEW.md','evidence/A31_WHOLE_PROOF_REVIEW.md'),
 ('gt_certificates/positive_rank_theta/CHECK_EVENTS_POSITIVE_RANK.tsv','evidence/check_events/CHECK_EVENTS_POSITIVE_RANK.tsv')]:
 if (W/s).exists():shutil.copy2(W/s,R/d)
for sid,names,base in [('A30',['A30_GENUS_THREE_POINTING_COUNTEREXAMPLE.tex','check_A30_finite_arithmetic.py','A30_FINITE_ARITHMETIC.json'],'effective_galois'),('A31',['verify_A31_norm7.py','verify_A31_norm7.json'],'row_audit')]:
 D=R/'certificates'/sid;D.mkdir(exist_ok=True)
 for n in names:shutil.copy2(W/base/n,D/n)
for n in ['check_A31_symbolic.py','check_A31_symbolic.json']:shutil.copy2(W/'root'/n,R/'certificates/A31'/n)

p=R/'reproduce/assemble_paper.py';s=p.read_text();old="'prime_power_canonical.tex','effective_galois.tex'"
assert old in s;s=s.replace(old,"'prime_power_canonical.tex','genus_three_pointing_counterexample.tex','a27_theta_seven.tex','effective_galois.tex'")
s=s.replace('recovered prime-level detector on an actual curve. Its residual canonical', 'recovered prime-level detector on an actual curve. A genus-three example\nrefutes a proposed universal rule for detecting quotients. An exact\ndegree-seven geometric witness exists on the rank-one numerical-obstruction\ncurve even though its original rational points all miss the canonical detector.\nThe residual canonical')
p.write_text(s)
p=R/'proof_sources/premises_section.tex';s=p.read_text().replace('Findings A07--A29','Findings A07--A31')
s+='''
A30 tests the exact genus boundary of that character argument by a
ramified double map to a supersingular elliptic curve and local Euler
factors. Its proposed preliminary double cover is excluded from the
prime-to-characteristic fibre functor. A31 gives an exact principal
divisor, its Frobenius-twisted theta class, and the resulting tame cyclic
cover on the same curve as A27. The geometry remains within the
pointed-cover question of cote~149, scans~35--36.
''';p.write_text(s)
p=R/'proof_sources/open_section.tex';s=p.read_text()
anchor='The approaches actually tested were:'
add=r'''A30 refutes a proposed direct higher-genus extension of the
``every detecting quotient is good'' conclusion: a genus-three
rank-one curve has a detecting constant cyclic cubic quotient whose
relative class number is even. It does not exclude other good
quotients. The proposed unramified double-cover repair is unavailable
to the geometric prime-to-two fundamental group and does not preserve
the descending detector. A31 shows that the rank-one curve of A27
nevertheless has an exact signed-doubling theta witness of order seven.
All six of its original rational points permanently miss A29's
canonical detector, yet the geometric witness can be pointed after
a finite extension. Thus the sufficient tests have distinct limits;
their failure is not a nonexistence result.

'''
assert anchor in s;s=s.replace(anchor,add+anchor)
s=s.replace('Their respective endpoints are recorded in A02--A29','Their respective endpoints are recorded in A02--A31')
p.write_text(s)

p=R/'reproduce/build_ledgers.py';s=p.read_text()
anchor="question('Q-ARTIN',"
add="""question('Q-CANONICAL-HIGHER-GENUS','AN_GRH','A30; DC.1–DC.13','Does every odd detecting quotient in the genus-two canonical argument remain a rational witness in genus three?','REFUTED: D/F4:z²+z=(t²+t)^(-3) has a constant P-split detecting cubic quotient with even relative class number.','A30','The example does not exclude other good quotients or powers for that pointed genus-three curve. The preliminary geometric double cover is outside the pro-odd quotient.','A translated Lang3-isogeny of E:y²+y=x³ supplies the quotient. Branch degrees1,1,1,3 yield the relative numerator (1−T)(1−T³) modulo2; each faithful reduced character polynomial is quadratic and vanishes at1. The detecting canonical class is nonzero in that quotient.')
question('Q-A27-DIRECT-THETA-WITNESS','AN_GRH','A31; TS.1–TS.11; A27','Does the rank-one curve defeating the numerical tests actually have a geometric witness?','PROVED: exact order7 theta incidence after the explicit F4 Frobenius twist gives a primitive-rank-zero degree7 cover and a pointed witness after finite extension.','A31,A27,A11','This is a concrete curve, not a universal finite-field incidence theorem. Its six original rational points all remain outside A29 despite this geometric witness.','The isomorphic model Y²+X²Y=X5+X4+uX3+u²X2+uX+u has Norm((X+u)Y+X)=(X+1)^7 and divF=7(R−W). Exact dX/X² identifies the theta bundle; <2,−1>=U7. Two distinct arithmetic implementations check the norm and coordinate identities.')
"""
assert anchor in s;s=s.replace(anchor,add+anchor)
s=s.replace("'§3.3(3); §5(a), route2; A07–A29'","'§3.3(3); §5(a), route2; A07–A31'")
s=s.replace('A27 likewise refutes universal forcing of the rank-one augmentation size test.', 'A27 likewise refutes universal forcing of the rank-one augmentation size test, while A31 supplies an exact7 geometric witness on that same curve.')
s=s.replace('A29 strengthens it to nonzero primary components and proves actual-curve strictness.', 'A29 strengthens it to nonzero primary components and proves actual-curve strictness. A30 refutes the proposed every-quotient higher-genus extension.')
p.write_text(s)

p=R/'evidence/root_check_events.json';ev=json.loads(p.read_text());who='GPT-6 Astra Pro; effort not exposed; AN_GRH /root'
for sid,fn,out in [
 ('A30','genus_three_pointing_counterexample.tex','PASS after the complete four-step proof and double-cover repair audit, plus the final scope-only correction. Checked the elliptic group by tangent intersection, translated Lang fibres, coprime-degree connected pullback, norm detector, every local mod2 Euler factor, both individual quadratic character reductions, and the forbidden pro-odd degree2 repair. The counterexample concerns the every-detecting-quotient rule, not nonexistence of all other good covers.'),
 ('A31','a27_theta_seven.tex','PASS after the complete written proof and all-six-points scope addition. Root derived the norm/isomorphism and read the independent written treatment. Checked the affine smoothness, exact pole/zero divisor, nontrivial exact7 class, exact differential and its divisor, explicit F4 Frobenius twist, signed-unit condition and A11 normalization. The order28 rational Jacobian places every original canonical class outside A29; this does not prevent the geometric7 witness.')]:
 sha=hashlib.sha256((R/'proof_sources'/fn).read_bytes()).hexdigest()
 ev.append(dict(statement_id=sid,date='2026-11-21',who_model_effort_run=who,type='targeted proof check',outcome=out+' SHA256 '+sha+'.',evidence='proof_sources/'+fn))
ev.append(dict(statement_id='A31',date='2026-11-21',who_model_effort_run=who,type='computation or formal certificate',outcome='Authored and executed a separate symbolic checker in SymPy over the formal F2 coefficient u modulo u²+u+1. PASS for the full norm, cleared-denominator coordinate identity, cancellation of y, point values and derivative. This imports no row-checker code. Also read and reran the encoded-F4 standalone checker: PASS. The written geometric proof, not these polynomial tests alone, proves the cover statement.',evidence='certificates/A31/check_A31_symbolic.py; certificates/A31/check_A31_symbolic.json; certificates/A31/verify_A31_norm7.py'))
p.write_text(json.dumps(ev,indent=2)+'\n')

p=R/'IMPLICATIONS.md';s=p.read_text()
anchor='The separate constant-twist route in recovered ANABELIAN_A1 B.28–B.29'
add='''A30 closes the proposed direct higher-genus symmetry repair negatively. On a genus-three rank-one curve overF4, a detecting cubic quotient has even relative class number; its reduced character polynomial has a genuine quadratic term. This refutes the rule that every detecting quotient works. It does not exclude other covers. The tempting unramified2-cover that moves one genus-two branch point to a non-Weierstrass point is also unavailable in the pro-odd fundamental group, and descended odd characters kill the relevant lifted difference.

A31 supplies an exact geometric witness on the very curve used in A27. After an explicit change of coordinates, F=(X+u)Y+X has norm (X+1)^7 and divisor7(R−W). The exact differential dX/X² identifies B on the Frobenius twist, and <2,−1>=U7 supplies the rank-zero new factor. Thus this curve's numerical failures do not hide an absence of actual covers. Moreover #J(F4)=28 shows that all six original rational points remain outside A29's canonical detector after every constant extension, yet the geometric7 cover can be pointed at any of them after a finite extension. This is an exact residual-case example, not a universal incidence claim.

'''
assert anchor in s;s=s.replace(anchor,add+anchor).replace('A06–A29 |','A06–A31 |')
p.write_text(s)
p=R/'README.md';s=p.read_text();anchor='- **GT certificates:**'
add='- **Distinct limits of the cover tests:** A30 refutes the direct every-detecting-quotient rule in genus three and checks why an unramified2-cover does not repair the pro-odd argument. A31 gives an exact geometric degree7 witness on A27, although its six original rational points all miss A29 and the stated size tests fail over every extension.\n'
assert anchor in s;s=s.replace(anchor,add+anchor);p.write_text(s)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
entry='\n## Checked follow-up at '+now+'\n\nA30 and A31 are integrated after complete proof readings. A30 refutes the direct every-detecting-quotient genus-three repair and records why the proposed preliminary2-cover is outside the pro-odd group. A31 closes the concrete actual-witness question for A27: its exact7 theta point gives a geometric primitive-rank-zero cover despite all numerical failures, and its six original points remain outside A29. Two distinct finite arithmetic implementations check the norm/coordinate identities. These facts keep sufficient-test failure distinct from nonexistence. Source freeze/build throughA31 follows; the74-pageA25 PDF is currently an older retained snapshot.\n'
for p in [R/'LEDGER.md',Path('AN_GRH_SESSION_STATE.md')]:
 with p.open('a') as f:f.write(entry)
print('Integrated A30-A31 and evidence. Canonical standalone rebuild is required.')
