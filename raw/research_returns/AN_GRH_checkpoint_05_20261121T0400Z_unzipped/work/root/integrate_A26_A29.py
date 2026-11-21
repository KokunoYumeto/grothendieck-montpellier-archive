from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib

R=Path('final');W=Path('work')
for s,d in [('row_audit/A26_RANK_ONE_AUGMENTATION.tex','rank_one_augmentation.tex'),('row_audit/RANK_ONE_AUGMENTATION_OBSTRUCTION.tex','rank_one_augmentation_obstruction.tex'),('row_audit/A28_RECOVERED_CANONICAL_CRITERION.tex','recovered_canonical_criterion.tex'),('gt_certificates/positive_rank_theta/A29_PRIME_POWER_CANONICAL.tex','prime_power_canonical.tex')]:
 shutil.copy2(W/s,R/'proof_sources'/d)

p=R/'reproduce/assemble_paper.py';s=p.read_text()
old="'lang_pairing_rank_bound.tex','effective_galois.tex'"
new="'lang_pairing_rank_bound.tex','rank_one_augmentation.tex','rank_one_augmentation_obstruction.tex','recovered_canonical_criterion.tex','prime_power_canonical.tex','effective_galois.tex'"
assert old in s;s=s.replace(old,new)
s=s.replace('numerical tests. The universal\npositive-rank', 'numerical tests. A parity improvement gives a separate rational cover test,\nand a rank-one curve defeats that size test over every extension. A\nprime-power canonical-class criterion supplies prescribed-point rational\nprimitive factors without size inequalities, and strictly extends the\nrecovered prime-level detector on an actual curve. Its residual canonical\nclasses and the universal\npositive-rank')
p.write_text(s)

p=R/'proof_sources/premises_section.tex';s=p.read_text()
s=s.replace('The return is \\textbf{INCOMPLETE as an exhaustive audit}; the\nrequested proof through Hooley is also not established.', 'The exhaustive audit remains in progress; the\nrequested proof through Hooley is also not established.')
s=s.replace('Findings A07--A25','Findings A07--A29')
s+='''
A26--A29 concern the same pointed finite etale coverings of cote~149,
scans~35--36. Their group-ring sums are character Euler factors of
unramified finite-order sheaves. Genus-two Riemann--Roch truncates their
reduction modulo the characteristic to a point-character sum; the
canonical class controls its inverse-character symmetry. A29 uses
the Picard functor, Lang isogeny and cyclic prime-power norm projector,
with the fibre-functor and arithmetic exact-sequence framework of
SGA~1, V, Theorem~4.1 and IX, Theorem~6.1. A28 is the explicitly
credited recovered successor A.26, not a new prime-degree theorem.
'''
p.write_text(s)

p=R/'proof_sources/open_section.tex';s=p.read_text()
anchor='The approaches actually tested were:'
addition=r'''A26 weakens the separate rational quotient criterion using even
augmentation. A27 nevertheless gives a rank-one curve over $\mathbf F_4$
where its numerical hypothesis fails for every extension and every
primitive-two prime. A28 recalls the recovered canonical-class criterion,
and A29 strictly improves its prime-level detection: a nonzero
$r$-primary component of $[K_C-2P]$ suffices if
$\operatorname{ord}_r(p)$ is even, with a cyclic $r^a$ cover and a
prime-to-$p$ rational top Prym. This is unconditional and needs no
prime-distribution theorem. The actual-curve strictness example in A29
shows why passage to prime powers matters even when all prime-level
canonical detectors fail. The residual points have canonical class
supported on the characteristic prime and odd primes of odd
multiplicative order, with the prime-two issue separate in odd
characteristic. In characteristic two this includes every Weierstrass
point and the purely two-primary non-Weierstrass examples of A09.
Constant extensions preserve that primary support. Other covers may
still work; no absence conclusion follows from this residual condition.

'''
assert anchor in s;s=s.replace(anchor,addition+anchor)
s=s.replace('and the independent cuspidal route.', 'the parity augmentation test; its all-extension rank-one obstruction;\ninverse-character canonical detection and its prime-power refinement;\nand the independent cuspidal route.')
s=s.replace('Their respective endpoints are recorded in A02--A20', 'Their respective endpoints are recorded in A02--A29')
s=s.replace('B.32 ask for prescribed-point rational class-number witnesses.', 'B.32 ask for prescribed-point rational class-number witnesses. A29\nnow settles the stated nonzero canonical-primary component cases,\nwhile their universal existence remains open.')
p.write_text(s)

p=R/'reproduce/build_ledgers.py';s=p.read_text()
s=s.replace("'§3.3(3); §5(a), route2; A07–A23'", "'§3.3(3); §5(a), route2; A07–A29'")
s=s.replace("'A02,A03,A04,A06,A07,A08,A09,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23'", "'A02,A03,A04,A06,A07,A08,A09,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29'")
s=s.replace('Another separation argument could also suffice. A1 itself is proved by A05.', 'Alternatively use a prescribed-point rational primitive-factor witness: A29 supplies one whenever the canonical class has a nonzero r-primary part at an odd r with even ord_r(p). The residual primary-support cases still require a construction. A1 itself is proved by A05.')
s=s.replace('No theorem forces one of the unbounded-prime searches to succeed.', 'A27 likewise refutes universal forcing of the rank-one augmentation size test. A28 is the recovered prime canonical criterion; A29 strengthens it to nonzero primary components and proves actual-curve strictness. No theorem forces success for the residual classes or for one of the unbounded-prime geometric searches.')
anchor="question('Q-ARTIN',"
add="""question('Q-RANK-ONE-AUGMENTATION','AN_GRH; ANABELIAN_A1 B.2; ANABELIAN_SUCCESSOR A.10,A.35','A26; RA.1–RA.3','Does even rational point-count parity remove the older pair-count condition from a prescribed-point quotient test?','PROVED: if 2 is primitive modulo r and |J(FQ)/rJ(FQ)|>#C, some quotient works; if r divides#J and r>#C, every quotient works. Every rank-one genus-two curve has even point count over every extension.','A26','The existence of a prime satisfying the numerical hypothesis is separate; A27 refutes universal numerical success.','The odd group-algebra augmentation is1. Failure of every quotient would make every Fourier coefficient except augmentation zero and hence every coset coefficient1, contradicting an empty nonzero Abel coset. The conclusion is rational and need not survive arbitrary extensions.')
question('Q-RANK-ONE-AUGMENTATION-UNIVERSAL','AN_GRH','A27; RO.1–RO.13','Must the A26 numerical criterion succeed after some constant extension of every rank-one genus-two curve?','REFUTED: for y²+y=u*x³+x+u/x overF4, u²+u+1=0, the quotient size is strictly below the point count for every extension and every primitive2 prime.','A27,A26','Actual rational cover witnesses and geometric theta witnesses are not excluded.','Exact N4=6,N16=28 give (T²−T+4)(T²+2T+4). Coprime Frobenius blocks bound large rational torsion rank; a symbolic induction covers m>=10 and a complete independently verified table covers m1..9.')
question('Q-RECOVERED-CANONICAL-PRIME','ANABELIAN_SUCCESSOR final','A.26; AN_GRH A28','What does the already-proved prime canonical-class criterion require?','CITED AND WHOLE-READ: for odd r distinct from p, inversion in <p> and kappa_P outside rJ(k) give a constant P-split prime-degree rational witness.','A28','The fixed canonical class may be divisible by every prime in the rational Jacobian. Its order and primary support do not change after a constant extension.','This is credited to the recovered source, not claimed as a new prime-level theorem. No size inequality or analytic hypothesis is required.')
question('Q-CANONICAL-PRIME-POWER','AN_GRH; recovered ANABELIAN_SUCCESSOR A.26; ANABELIAN_A1 B.13–B.14','A29; PC.1–PC.14','Can higher cyclic powers remove the prime-level divisibility obstruction in canonical-class detection?','PROVED: a nonzero r-primary component of kappa_P=[K−2P], for odd r distinct from p with even ord_r(p), gives a constant P-split r^a-cover with prime-to-p rational top Prym and separates P.','A29,A28','Classes supported on p and odd primes of odd ord_r(p) remain outside this detector; the prime2 case in odd characteristic is separate. This limitation does not assert absence of other witnesses.','All faithful characters are p-units by genus-two Riemann–Roch and inversion as a p-power. Their product is the top-step Prym order; its vanishing rational p-primary group gives the free odd-deck pencil contradiction. On A09 after a finite13-division extension every prime canonical detector fails but A29 works, proving actual-curve strictness.')
"""
assert anchor in s;s=s.replace(anchor,add+anchor)
p.write_text(s)

p=R/'evidence/root_check_events.json';events=json.loads(p.read_text())
who='GPT-6 Astra Pro; effort not exposed; AN_GRH /root'
for sid,typ,out,ev in [
 ('A28','used and rechecked in this run','Read the complete recovered successor A.26 proof and its A.25 context, then the entire cited formulation and Weierstrass interpretation. Checked final attribution and removal of the undefined value b. This is source verification, not a new proof or originality claim. SHA256 2b33638f1ac4b8b854fc6ceecbd80eae14285e66aed2cdc359ce97ea4ef08801.','proof_sources/recovered_canonical_criterion.tex; recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex, A.26'),
 ('A1-B1-B2-B13-B14','used and rechecked in this run','Read the complete recovered B.1 and B.2 proofs and B.13–B.14 statements/proofs in the current check. Verified the odd-deck relative obstruction, exact effective-divisor Euler criterion and primitive packet in a cyclic prime-power tower. No same statement is promoted to a new independent re-proof.','recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex, B.1,B.2,B.13,B.14'),
 ('A29','targeted proof check','PASS after reading the entire six-step proof, source attribution, residual analysis and actual-curve strictness corollary. Checked detecting cyclic quotient, inversion at every prime power, connected pointed Lang pullback, exact RR polynomial and inverse symmetry, faithful p-units and top Prym integer, image(tau−1), and the separable pencil/free odd-deck contradiction. The appended strictness corollary is valid: the A09 canonical class has order13 and becomes13-divisible after a finite extension while retaining its nonzero primary component; other prime detectors also kill it. This does not exclude actual prime covers. SHA256 feb70cad020af94c8d471e4c97741eaf68e8d28a8381c09da164c38df46bb6b7.','proof_sources/prime_power_canonical.tex')]:
 events.append(dict(statement_id=sid,date='2026-11-21',who_model_effort_run=who,type=typ,outcome=out,evidence=ev))
p.write_text(json.dumps(events,indent=2)+'\n')

p=R/'IMPLICATIONS.md';s=p.read_text()
anchor='The separate constant-twist route in recovered ANABELIAN_A1 B.28–B.29'
add='''A26 removes the pair-count inequality from a separate rational criterion when the point count is even, as it is for every rank-one genus-two curve: for primitive2 prime r, |J(FQ)/rJ(FQ)|>#C forces a prescribed-point quotient witness. A27 shows that this numerical improvement is still not universally forceable. Its explicit rank-one F4 curve has |J(F_(4^m))/rJ|<#C(F_(4^m)) for every m and every primitive2 prime. The proof covers all extension degrees, rather than extrapolating a search, and does not rule out the covers themselves.

**A29 strictly improves the prescribed-point canonical-class gate without any GRH assumption.** The prime criterion is the already-proved successor final A.26, cited and whole-read as A28. Put kappa_P=[K_C−2P]. It is now enough that kappa_P have a nonzero r-primary component for an odd r distinct from the characteristic p with even ord_r(p); it need not survive in J(k)/rJ(k). A detecting cyclic r^a quotient has all faithful character L-values prime to p. Their product is the rational order of the top-step Prym, which gives point separation by the free odd-deck argument. On the actual A09 curve, after rationalizing a13-division point of the canonical class at its order13 point, every prime-level canonical detector fails while A29 still supplies a13^a witness. This proves strictness of the criteria on a curve, without claiming failure of every actual prime cover.

The canonical residual is explicit: this detector does not treat classes supported on p and odd primes at which p has odd multiplicative order; prime2 in odd characteristic is separately outside its odd-deck hypothesis. In characteristic2 it includes Weierstrass points and points with purely2-primary canonical class. Constant extensions cannot alter the finite order or primary support of that fixed class. Other geometric or rational covers may still work. A29 is an additional route to the prescribed-point cover required in cote149 scans35–36, not a universal Hooley incidence theorem.

'''
assert anchor in s;s=s.replace(anchor,add+anchor)
s=s.replace('A06–A25 |','A06–A29 |')
row='| ANABELIAN_A1 B.28–B.29 |'
addrow='| ANABELIAN_SUCCESSOR A.26; ANABELIAN_A1 B.13–B.14 | A28–A29 | The prime canonical criterion is credited and rechecked. A29 replaces nondivisibility modulo r by a nonzero r-primary component using a prime-power top Prym; actual-curve strictness is proved. Residual canonical supports remain open for this construction. |\n| ANABELIAN_SUCCESSOR A.10,A.35; ANABELIAN_A1 B.2 | A26–A27 | Even augmentation removes an extra pair-count hypothesis, but the new sufficient size test still fails over every extension on an explicit rank-one curve. |\n'
assert row in s;s=s.replace(row,addrow+row)
p.write_text(s)

p=R/'README.md';s=p.read_text().replace('# AN_GRH final package','# AN_GRH working package')
anchor='- **GT certificates:**'
add='- **Prescribed-point rational refinement:** A26 gives an even-augmentation size test, and A27 refutes universal numerical success over constant extensions on a rank-one curve. A28 credits the recovered prime canonical-class criterion. A29 proves a strictly stronger prime-power detector in every characteristic: a nonzero suitable primary component of [K−2P] suffices, even when all prime-level canonical detectors vanish. The remaining primary-support cases are stated explicitly.\n'
assert anchor in s;s=s.replace(anchor,add+anchor)
p.write_text(s)

now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
entry='\n## Post-review movement at '+now+'\n\nA26–A29 are now integrated as complete checked sources, with A28 explicitly credited as the recovered successor A.26 rather than a new prime theorem. A29 strictly weakens a prescribed-point rational sufficient gate: nonzero primary canonical component replaces nondivisibility modulo the prime. The actual A09 curve after a finite13-division extension proves strictness on a curve. Its residual canonical supports remain stated, and the universal Hooley route is not claimed. The source has expanded beyond the74-page A25 build; a new hash-matched build is required before final delivery. A proposed genus-three extension of the canonical detector and a forbidden characteristic-two cover repair are under active audit. These are not yet included as proved findings.\n'
with (R/'LEDGER.md').open('a') as f:f.write(entry)
with Path('AN_GRH_SESSION_STATE.md').open('a') as f:f.write(entry)
print('Integrated A26-A29 source, questions, implications and exact proof-reading events; rebuild pending.')
