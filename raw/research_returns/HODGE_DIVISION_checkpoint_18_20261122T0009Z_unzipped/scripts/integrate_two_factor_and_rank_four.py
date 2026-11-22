"""Integrate independently reviewed ATT04--06 and E840 restrictions."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,io
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
items={
 'D-ATT04--06':('agents/g34_eightfolds/bireflection/alternating_two_factor_section.tex','b7a5a8d6e9c887fb0e3cdb4964bd2cda6a927d38d8d314b2c821cb3f4c78bcbf','agents/imprimitive/audit_alternating_two_factor/PEER_AUDIT.md','211304c4d4e4e0fe2bf83f20245c1db94feab826d34cf72448078b16eae43830'),
 'SF-E840':('agents/sixfolds/rm_rank_four_principal_image_section.tex','5c341f9dd9bfeb465e8d94712984f3741e50f922189c7216bf3faa4120380257','agents/g34_eightfolds/bireflection/RANK_FOUR_PRINCIPAL_IMAGE_PEER_AUDIT.md','e8b35f850b5ddfa94815aa8b7cfdaea8ebaadf52fa3ea306ef3f1fd35e9a1b1d')}
for proof,sha,report,rsha in items.values():
 assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==sha
 assert hashlib.sha256((R/report).read_bytes()).hexdigest()==rsha
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
pending={}
p=items['D-ATT04--06'][0];before=s=(R/p).read_text()
s=change(s,'Independent whole-proof review is pending.','The root and independent /root/imprimitive whole-proof, source and\ncode readings have passed, with distinct exact supplements.')
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S);pending[p]=s
p=items['SF-E840'][0];before=s=(R/p).read_text()
s=change(s,'Status: complete new author derivation; independent review pending.',
 'Status: complete new author derivation; whole root and independent\n/root/g34\_eightfolds proof, source and code audits passed.')
s=change(s,'proof. Independent review is pending. Rank-at-most-three pencils,',
 'proof. The complete independent review has passed. Rank-at-most-three pencils,')
assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S);pending[p]=s
att=('D-ATT04--06 excludes both ordinary two-box-tail labels forALLn>=15 when the actual inducing image is transitive on exactlyt2 factors, over every non-Eisenstein originalK. '
 'A common single-factor index bound and exact weighted-swap eigenspaces force precisely two factor swaps, both scalar-marked outside mu6. '
 'The actual connected2n-letter quotient gives indexsum>=2n-2; the moving-rank sum exceeds2e+6 by at leasta/2-6. '
 'The n100t2 Gaussian profiles survive previous finite and shape gates but are now excluded. Larger tensor counts are not treated by this theorem. ')
artin=('SF-E840 refines the regular-quadratic-CI residual locus: every rank-four leading pencil image J must equal ellV for a unique line, equivalently the intrinsic common-linear-factor space K(J) has dimension1. '
 'The regularity/basepoint lemma givesdim(VL)>=5 wheneverdimL>=2; equality in the all-size filtered square-matrix bound forces a common linear factor. '
 'The actual companion matrix is noninvertible by the independent mixed-Jacobian-socle argument, so this condition applies to everyrank4direction in everymultiplicity and allhigherperturbations. '
 'The explicit nonsquare Q=(x²+yw,y²,z²,w²), p=(1,1,0,0,1,1),q=(1,-1,0,0,-1,1) has all36scalarcrossminors and all36five-minorszero, mixedwedge64xyzw, genericpencilrank4, butK(J)=0atplus endpoint. '
 'It lies outside commuting-triple and formal-square families, proving strictness beyondE836--839. Rank<=3pencils andprincipalrank4images remain necessary residual cases, not established deformations. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not {'Q2cf','Q5an'}&{r['id'] for r in rows}
backup={r['id']:dict(r) for r in rows if r['id'] in ('Q2i','Q5i')}
for r in rows:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']=change(r['finding_ids_or_current_gate'],'Longer unexcluded tensor cases remain. ',att+'Longer unexcluded tensor cases remain. ')
 if r['id']=='Q5i':r['finding_ids_or_current_gate']+=' '+artin
rows.extend([dict(zip(fields,['Q2cf','Prompt target2; all-degree transitive two-factor two-tail cores','Can either two-box-tail core with exactly two transitive factors supply a non-Eisenstein rank-nine source at anyn>=15?','refuted',att+'Complete root and independent imprimitive audits PASS.'])),dict(zip(fields,['Q5an','Prompt target5; rank-four Artin companion equality','Can a regular quadratic common-CI point defect with a nonprincipal rank-four leading pencil image admit the required weak balanced semiregularity?','refuted',artin+'Complete root and independent G34 audits PASS; explicit actual coherent extension family retained.']))])
out=io.StringIO();w=csv.DictWriter(out,fields,delimiter='\t');w.writeheader();w.writerows(rows);pending['QUESTIONS.tsv']=out.getvalue()
s=(R/'HODGE_DIVISION.tex').read_text()
for anchor,new in [(r'\input{agents/g34_eightfolds/bireflection/alternating_two_tail_section.tex}',items['D-ATT04--06'][0]),(r'\input{agents/sixfolds/rm_rank_five_jet_obstruction_section.tex}',items['SF-E840'][0])]:s=change(s,anchor,anchor+'\n'+r'\input{'+new+'}')
s=change(s,'separate strict reduction. Larger unexcluded tensor ranges remain.',r'''separate strict reduction. D-ATT-04--06 further excludes both
two-box labels for every $n\ge15$ with exactly two transitive factors,
over every non-Eisenstein original field. Exactly two marked factor
swaps and an actual degree-$2n$ quotient give a Riemann--Hurwitz
contradiction. Larger unexcluded tensor counts remain.''')
anchor='small algebraic boundary example. No residual-locus existence follows.'
s=change(s,anchor,anchor+r'''
SF-E840 determines the relevant equality constraint: every rank-four
pencil image must be $\ell V$ for a unique linear factor. The
regular-quadratic multiplication lemma and the exact filtered matrix
equalities prove this for every multiplicity. An explicit nonsquare
intersection has rank-four pencils and all preceding scalar and
rank-five tests zero, yet no common linear factor. Thus the new
condition strictly narrows the remaining quadratic locus.''')
pending['HODGE_DIVISION.tex']=s
for p,s in pending.items():(R/p).write_text(s)
(R/'research/gates_before_two_factor_and_rank_four.json').write_text(json.dumps(backup,indent=2)+'\n')
events=[('D-ATT04--06 root full certificate and peer','targeted proof check','Root complete frozen proofb7a5a8d6, every author checker line and entire output read; entire peer211304c4 read. Universal index/weighted-swap/actual quotient proof PASS. Author11224partitions4412weightedtypes239620multiplicity504actualindex1972arithmetic checks1.783030233s22:37:00UTC. Peer own2.194461129s22:40:28 includes112weighted cases576actualS4pairs and independent character moments; initial floating symbolic constant repaired before final exact run, no author repair. Root has not whole-read peer code.',items['D-ATT04--06'][2]),
 ('SF-E840 root canonical and peer','targeted proof check','Root complete initial draft, all359canonical TeX lines, every author checker line and full output read; entire peer e8b35f85 and conversion metadata read. All18displays unchanged; root does not claim whole-read conversion diffs. Universal equality/basepoint/actual companion and strict witness PASS. Peer independent Groebner/Jacobian supplement0.210295113s22:42:09; rational auxiliary-minor output repair retained, mathematical rank assertions unchanged. Root has not whole-read peer code.',items['SF-E840'][2]),
 ('D-ATT04--06 SF-E840 canonical integration','targeted proof check','Status-only promotions with all displayed mathematics unchanged. Q2cf andQ5an refuted;Q2i andQ5i strictly smaller. Unreviewed standard/all-t and orthogonal proofs remain excluded. No compilation or residual-source existence claim.','scripts/integrate_two_factor_and_rank_four.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## All-degree two-factor and principal-image restrictions\n\n'+now+' — Q2cf andQ5an refuted; both continuing main gates strictly reduced after review10. '+att+artin+'No formal review or checkpoint in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Actual quotients and filtered equality restrict suppliers\n\n'+att+artin+'These constrain condition-A suppliers and actual semiregular K-theory classes (cote16scan050;SIGN_NEXT SN-C03/C04;DEG_L S-14), while conditionI/cote44Th4 divides classes already supplied. Actual finite quotient morphisms and filtered coherent modules remain in the common schemes-over-Z, EGA/SGA/FGA, lambda-ring, projector and motivic/L-function frame. No new Markman, Severn or032 premise is used.\n')
result={'date_utc':now,'reviewed_files_and_reports':items,'canonical_sha256':{k:hashlib.sha256((R/v[0]).read_bytes()).hexdigest() for k,v in items.items()},'new_rows':['Q2cf','Q5an'],'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/two_factor_and_rank_four_integration.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
