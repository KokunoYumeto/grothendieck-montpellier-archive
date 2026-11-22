"""Integrate root/peer whole-reviewed HOS17--19 and OL09--11."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
paths={'HOS17-19':'agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_involution_section.tex','OL09-11':'agents/imprimitive/orthogonal_lowlevels/orthogonal_nonextendible_section.tex'}
frozen={'HOS17-19':'f976dad03ec875a46b3c25e39da81bd7af7240d6ffc2f0029e9343c61b2a8d46','OL09-11':'5f7e898c37be40cb4a17cd8ccbfdce9fa48b90d3c3beb40d0637fed620ae5bd4'}
for k,p in paths.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k]
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a))
 return s.replace(a,b)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
ids=['Q2bv','Q2bw','Q2bx'];assert not set(ids)&{r['id'] for r in rows}
(R/'research/gates_before_hos_involution_orthogonal_nonextendible.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')
p=R/paths['HOS17-19'];p.write_text(change(p.read_text(),'This is a separate complete derivation, submitted for independent\nwhole-proof review.','This separate complete derivation has passed whole-proof reviews by\n/root and /root/imprimitive, with an independent exact supplement.'))
p=R/paths['OL09-11'];p.write_text(change(p.read_text(),'author supplement passed.  Independent review is pending.','author supplement passed. Whole-proof reviews by /root and\n/root/g34\\_eightfolds also pass, with a separate exact reconstruction.'))
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,extra in [('agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_sharp_section.tex',paths['HOS17-19']),('agents/imprimitive/orthogonal_lowlevels/orthogonal_support_section.tex',paths['OL09-11']),('agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_sharp_bibitems.tex','agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_involution_bibitems.tex')]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+r'\input{'+extra+'}')
anchor='cutoff $n<10^{30}$.'
s=change(s,anchor,anchor+r''' D-HOS-17--19 further shows that at least one genuine inertia
must preserve the factors and be nonscalar, and every projective
prime-order power in each nonscalar factor component must have odd
prime order at least five, with no natural eigenvalue $1$ or $-1$
for its odd-order lift. The projective factor orders of that inertia
are therefore coprime to six; its scalar part is unrestricted.
This necessary inertia condition does not assert existence.''')
anchor='This is a finite simple-factor parameter range, not an enumeration\nof tensor powers, scalar extensions or actual sources.'
s=change(s,anchor,anchor+r'''
D-OL-09--11 sharpens two ordinary-character subranges: for all $q\ge3$,
a remaining selfdual ordinary factor has $d\le21$, without an
extension-to-$O$ assumption. For all even $q$, every remaining ordinary
transitive factor has $d\le1134$, without a selfduality assumption.
The latter bound does not cover odd-field nonselfdual ordinary
characters or genuine spin characters; their previous bounds remain.''')
p.write_text(s)
hos='D-HOS-17--19 further restricts the residual nonselfdual Sp3 ranks4..283: at least one genuine inertia is factor-preserving and nonscalar, and EVERY projective prime-order power in EVERY nonscalar factor component has odd prime order>=5 and its odd-order lift has no natural +/-1 eigenvalue. Its projective factor orders are coprime6; scalar inertia part unrestricted. Symmetric-form fixed fraction1/39 yields support19a/78 for evenn and>19a/104 for oddn; opposite radicals plus LST Prop4.2.3 give the actual restriction bound. '
orthself='D-OL-09 gives all ordinaryq>=3,d>=22 full-compatible-normalizer support7a/64 without O-extension. For selfdual transitive cores the actual nontrivial multiplier budget forces e<=64, contradicting the degree floor. Remaining selfdual ordinaryq>=3 natural dimensiond<=21. '
ortheven='D-OL-10--11 gives every ordinary even-q transitive core natural dimensiond<=1134: non-O-extendible factorsd>=1136 have support11a/64 using all-rank weight bounds and LST restricted mu2 support567, forcinge<=96; extendible factors are real/selfdual and already excluded atd>=22. Odd-field nonselfdual ordinary and genuine spin cases retain their earlier bounds. '
for r in rows:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']+=' '+hos+orthself+ortheven
for id,question,gate in [(ids[0],'Can all actual inertias avoid the residual odd-prime/no-natural-eigenvalue condition in the remaining Sp3 range?',hos),(ids[1],'Can an ordinary selfdual orthogonal transitive factor overq>=3 have natural dimension>=22?',orthself),(ids[2],'Can an ordinary even-characteristic orthogonal transitive factor have natural dimension>=1136?',ortheven)]:
 rows.append(dict(zip(fields,[id,'Prompt target2; whole-reviewed HOS17--19 and OL09--11',question,'refuted',gate+'Whole root and separate peer proof/source checks PASS; finite arithmetic supplements do not replace the universal proofs.'])))
with q.open('w',newline='') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[('D-HOS-17--19','targeted proof check','Root whole frozen272-line proof, entire author checker and JSON, bibliography PASS. Exact Hermitian ranks/types, rank2 orbit1/39, LST subgroup restriction, both parity supports and quantified inertia gate checked. Author arithmetic3.717211556s; root does not claim rerun.',paths['HOS17-19']),('D-HOS-17--19 peer audit','targeted proof check','Root entire imprimitive report SHA1be0a857ee90ebfafd93d29cf6a08624e6db458de2b4be98507081343c2c6963 read. Whole proof/source/code PASS and independent Gauss-sum rank/type reconstruction0.347798531s:59076 symmetric forms,19683 Hermitian fixed forms. Root has not whole-read peer code.','agents/imprimitive/audit_symplectic_three_involution/PEER_AUDIT.md'),('LST2011 Proposition4.2.3 and Taylor classical forms','used and rechecked in this run','Root freshly read complete LST restriction setup and Prop4.2.3 proof printed1909-1912, all six steps. Root fresh full Taylor corrected text115-118 and138-141 including Hermitian norm/Witt/classification and full U/O orders. Exact subgroup natural threshold8, exponent8/3-N/2 and nontrivial ambient irreducible scope retained.','agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_involution_bibitems.tex'),('D-OL-09--11','targeted proof check','Root whole frozen355-line proof, full author checker and JSON PASS. Rank4 commutator avoids O-extension; arbitrary-field descent; even nonextendible support and exact source budgets. Author arithmetic0.057138158s. Root fresh LST p1907 support conventions and p1923 Remark4.3.7; complete Th4.3.6 proof earlier read. No independent re-proof of cited theorem claimed.',paths['OL09-11']),('D-OL-09--11 peer audit','targeted proof check','Root entire G34 report SHAe917b109b7901c1409e4bb23599a92964519f54891be3f2b4fce7b993daa1f4f read. Whole proof/source/author-code PASS; independent supplement0.083038458s on16418 alternating forms,2400 rank4 commutators and actual10-dimensional witnesses. Root has not whole-read peer code.','agents/g34_eightfolds/bireflection/ORTHOGONAL_NONEXTENDIBLE_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Inertia-class and ordinary orthogonal refinements\n\n'+now+' — Q2bv/Q2bw/Q2bx refuted; Q2i strictly reduced. '+hos+orthself+ortheven+'These changes occur after review09 and are not a formal hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Further actual curve-supplier restrictions\n\n'+hos+orthself+ortheven+'These restrict actual condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04), retaining original-field inclusion and rank-nine polarized Shapiro variation. They do not themselves supply cycles or use positivity to create one. Condition I (scan049/cote44 Th4), resultant/Cayley-Hamilton division (scans048-049), and scheme/lambda/K-theory/realization/weight/motive/L-function placements are the common framework. No new Markman, Severn or032 premise is introduced.\n')
out={'date_utc':now,'integrated':list(paths),'frozen_reviewed_sha256':frozen,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':dict.fromkeys(ids,'refuted'),'strictly_reduced_main_gates':['Q2i']}
(R/'research/hos_involution_orthogonal_nonextendible_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
