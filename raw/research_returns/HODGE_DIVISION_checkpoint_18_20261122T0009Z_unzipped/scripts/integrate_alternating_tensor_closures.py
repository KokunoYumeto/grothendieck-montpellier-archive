"""Integrate three complete alternating tensor-source obstructions."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,io,subprocess,sys
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
items={
 'HD-AST07--09':('research/alternating_standard_two_factor_section.tex','32b5cc512a130b41b5d6f3d8e0d4f2d5fa02e3714ce9d6ba6d6b89d5a4163108','agents/g34_eightfolds/bireflection/STANDARD_TWO_FACTOR_PEER_AUDIT.md','f1ed2a926733321399b7bab457f376f1e8a0b7124e368bc574b06b2b128332c3'),
 'HD-AST10--12':('agents/imprimitive/standard_all_tensors/standard_all_tensors_section.tex','571d9d5475dbd1aadb7a68d85d39346f0bea7db6fd04d220ef881ad4e3a5a2a3','agents/g34_eightfolds/bireflection/STANDARD_ALL_TENSORS_PEER_AUDIT.md','9e6fe6bbcdf06156579d9ada3018f674c0079f770641b49abdecb1bf245599b8'),
 'D-ATT07--09':('agents/g34_eightfolds/bireflection/alternating_two_tail_all_tensors_section.tex','2e9afd9be79f01ee143291b73619837be11182569bccc0234bfb66d45c73372b','agents/imprimitive/audit_alternating_two_tail_all_tensors/PEER_AUDIT.md','955bf07e27c543418217938427135e18cf106fba416f0b379583a2b3d80a1607')}
for proof,sha,report,rsha in items.values():
 assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==sha
 assert hashlib.sha256((R/report).read_bytes()).hexdigest()==rsha
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
pending={};canonical={}
for key,(p,sha,report,rsha) in items.items():
 before=s=(R/p).read_text()
 if key=='HD-AST07--09':
  s=change(s,'The complete author whole-proof reading has passed; an independent\nwhole-proof review remains pending.',
   'The complete root author reading, the contributor verification, and\nthe separate /root/g34\\_eightfolds whole-proof/code audit have passed.\nDistinct exact supplements and the formatting-only repair are retained.')
 elif key=='HD-AST10--12':
  s=change(s,'No\nindependent review is asserted in this initial frozen version.',
   'The complete root reading and /root/g34\\_eightfolds whole-proof\naudit have passed. Shared weighted-cycle authorship is explicit;\nthe separate exact implementations are not labelled independent\ndiscoveries of that common lemma.')
 else:
  s=change(s,'Independent review is\npending.',
   'The complete root and /root/imprimitive whole-proof/code\nreadings have passed, with a distinct matrix supplement and\nexplicit disclosure of the shared preceding framework.')
 assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',s,re.S)
 pending[p]=s;canonical[key]=hashlib.sha256(s.encode()).hexdigest()
# Preserve a runnable frozen author triple before its status-only promotion.
frozen_dir=R/'research/frozen_alternating_two_tail_all_tensors';assert not frozen_dir.exists();frozen_dir.mkdir()
tail_dir=R/'agents/g34_eightfolds/bireflection'
for name in ('alternating_two_tail_all_tensors_section.tex','check_alternating_two_tail_all_tensors.py','alternating_two_tail_all_tensors_checked.json'):
 (frozen_dir/name).write_bytes((tail_dir/name).read_bytes())
checker='agents/g34_eightfolds/bireflection/check_alternating_two_tail_all_tensors.py';code=(R/checker).read_text()
code=change(code,"assert proof_hash=='"+items['D-ATT07--09'][1]+"'",
 'assert proof_hash in '+repr({items['D-ATT07--09'][1],canonical['D-ATT07--09']}))
pending[checker]=code
standard2=('HD-AST07--09 excludes the transitive exactly-two-standard-factor core forALLn>=15 overEVERYoriginal imaginaryquadraticfield, withoutscalar-conductormarks. '
 'The new universal estimate isnu(Ux tensorUy)>=((n-3)(indx+indy)+n)/2 for nonidentitytensor permutations, using squared-multiplicity Cauchy plus bothreal-target cycle counts. '
 'Four swaps exceedthebudget; the actual2n-letter quotient then givesD>=2e+a+5>2e+6. '
 'The n100t2 Gaussian profile provesstrictness againstpriornecessarygates. ')
standardall=('HD-AST10--12 excludes ALLtransitive standard tensorcounts t>=3,n>=15 for everyNON-EISENSTEINoriginalK. '
 'Two scalar phasesoutside mu6 force exactlytwo fulltensorcycles. Selectingthelargest-indexpair at eachfactor-fixingmark preserves thefulln/2constant; weightedcycles retain theexactrotationerrorR_t=sum a^gcd(t,j)<=2a^(t-2). '
 'The actualnt-letter quotient givesN+H>=2n-2 andD-2e>=a^(t-2)((5t-6)n+2)/t>6. '
 'Togetherwiththetwo-factor andprior single-factor results, everytransitive standardcore isexcluded in themainnonEisensteinproblem. The n100t3 Gaussianprofilepassedpriorfinite/shapegates; noactualsourceexistenceisasserted. ')
tailall=('D-ATT07--09 excludes ALLt>=3 forbothordinarytwo-box-tail labels overNON-EISENSTEINoriginalK, retainingfullnormalizersandactualfieldcontainment. '
 'Atfactor-fixingmarks thecommonindexestimate preservesfullB=n/4; bothfullcyclesusetheexactshort-orbitdefect andallowidentitycycleproductswithscalarfixedvectors. '
 'The actualnt-quotientRH bound makesD-2e>3n*a^(t-1)/2>6. TogetherwithATT06andtheprior single-factor proofs, alltransitive tensorcounts for(n-2,2)and(n-2,1,1)areexcluded. '
 'The n100t3Gaussianprofilesproveindependentstrictness fromstandardcores. Supersedingtheearlierfinite standard/two-tailranges, everyremainingordinaryalternatinglonglabel in themainnonEisensteingate has,aftertranspose,tail k>=3 andstillobeysALT07/ALT08exactandfield-sensitive inequalities. Otherlabels,nontransitiveconfigurationsandnonalternatingcoresremain. ')
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);newids={'Q2ch','Q2ci','Q2ck'};assert not newids&{r['id'] for r in rows}
main=next(r for r in rows if r['id']=='Q2i');old=dict(main);main['finding_ids_or_current_gate']+=' '+standard2+standardall+tailall
for rid,source,question,finding in [
 ('Q2ch','Prompt target2; standard two-factor source in arbitrarydegree','Can two transitive standard alternating factors supply the actual rank-nine source for anyn>=15 and any originalfield?',standard2),
 ('Q2ci','Prompt target2; allstandard tensorcounts overnonEisensteinfields','Can a transitive ordinary standard core witht>=3,n>=15 supply the actual nonEisenstein rank-nine source?',standardall),
 ('Q2ck','Prompt target2; alltwo-box-tail tensorcounts','Can either ordinarytwo-box-tailcore witht>=3,n>=15 supply the actual nonEisenstein rank-nine source?',tailall)]:
 rows.append(dict(zip(fields,[rid,source,question,'refuted',finding+'Whole root and peer readings PASS; finite supplements and shared derivation provenance distinguished.'])))
out=io.StringIO();w=csv.DictWriter(out,fields,delimiter='\t');w.writeheader();w.writerows(rows);pending['QUESTIONS.tsv']=out.getvalue()
s=(R/'HODGE_DIVISION.tex').read_text();anchor=r'\input{agents/g34_eightfolds/bireflection/alternating_two_factor_section.tex}'
s=change(s,anchor,anchor+'\n'+'\n'.join(r'\input{'+items[k][0]+'}' for k in ('D-ATT07--09','HD-AST07--09','HD-AST10--12')))
s=change(s,'contradiction. Larger unexcluded tensor counts remain.',r'''contradiction. D-ATT-07--09 removes every larger transitive
tensor count for these same two labels over non-Eisenstein fields.
Its exact weighted-cycle error includes all short word orbits, and
the factor-fixing index bound keeps its full constant term.
HD-AST-07--09 independently excludes the standard two-factor case
in every degree $n\ge15$, over all original fields, using a new
uniform tensor index estimate and the actual degree-$2n$ quotient.
HD-AST-10--12 then excludes every larger standard tensor count
over non-Eisenstein fields by pair selection and the same exact
cycle error. These all-count results supersede the finite cutoffs
for the three labels. Every remaining ordinary long label in the
main non-Eisenstein problem has at least three boxes off its long
row or column and satisfies the exact ALT07/ALT08 shape bounds.''')
pending['HODGE_DIVISION.tex']=s
for p,s in pending.items():(R/p).write_text(s)
(R/'research/gate_before_alternating_tensor_closures.json').write_text(json.dumps(old,indent=2)+'\n')
# This is a root execution of the status-hash-compatible checker, not an
# alteration or relabelling of the retained frozen author execution.
run=subprocess.run([sys.executable,str(R/checker)],cwd=R,check=True,capture_output=True,text=True)
rerun=json.loads((tail_dir/'alternating_two_tail_all_tensors_checked.json').read_text())
events=[('HD-AST07--09 complete root derivation','targeted proof check',
 'Root whole initial proof and exact final formatting delta read; every checker line and full initial/final outputs read. Contributor supplied Cauchy estimate; all real-target margins/source proof byroot. Final frozen32b5cc51 PASS. AST2.7font escape caught bycontributor andcorrected totext even; no mathfailure. Complete D-AST01--03 reread.','research/alternating_standard_two_factor_section.tex'),
 ('HD-AST07--09 root exact grid supplement','computation or formal certificate',
 'Root actual firstPASS7.0059244s22:48:38UTC; final-hashPASS6.773588782s22:50:10UTC.160926partitionpairs7886278spectralentries23417one-target22820minus-targetchecks4000weighted-swaps. Initialoutputretained; nofailedassertion.','research/standard_two_factor_checked.json'),
 ('HD-AST07--09 contributor and independent peer','targeted proof check',
 'Root entire contributor f5b88436 and separate G34peerf1ed2a92 read. Contributor verification distinguished fromindependentorigin. G34completeproof/code/interfacePASS; own13.119050608s22:55:22UTC convolution160926pairs,60actualrationalmatrices616quotientactions. Root has notwhole-read peercode.',items['HD-AST07--09'][2]),
 ('D-ATT07--09 root and peer complete reading','targeted proof check',
 'Root all333prooflines, everyauthorcheckerline andfull32caseoutput, andentirepeer955bf07e read. Exactrotationerror, fullBconstant, actualntquotient andallfieldinclusionchecksPASS. Author0.872104665s22:52:01UTC; peer distinct15actualmatrix supplement0.906830721s22:57:37UTC. Sharedprecedingframeworkdisclosed; rootnotwhole-readpeercode.',items['D-ATT07--09'][2]),
 ('HD-AST10--12 root and peer complete reading','targeted proof check',
 'Root whole326lineproofread includingseparate105--202read aftercombined-outputtruncation; everycheckerline,full60caseoutput andfailedattemptrecordread; entirepeer9e6fe6bb read. Fullpairconstant, exactweightedcycleerror, scalarplacement andactualquotientPASS. Author1.550464386s22:56:07UTC; prior expand/cancel assertion failure andformfeedrepair retained. Peer0.206236488s22:59:32UTC directtrace/Fourier and900standardtensor cases. Sharedweighted-lemmaauthorship explicit; rootnotwhole-readpeercode.',items['HD-AST10--12'][2]),
 ('D-ATT07--09 promoted-hash root rerun','computation or formal certificate',
 'Root preservedrunnablefrozenproof/checker/outputtriple, allowedonlyfrozenandstatus-promotedhashes, andactuallyreranallunchangedmathchecks. PASS '+str(rerun['completed_utc'])+' '+str(rerun['runtime_seconds'])+'s. The new execution is attributedtoroot, notoriginalauthor.',checker),
 ('Alternating tensor closures integrated','targeted proof check',
 'All theorem/displays unchanged bystatuspromotion; Q2ch,Q2ci,Q2ckrefuted andQ2istrictlysmaller. EveryremainingnonEisensteinordinarylongtail hask>=3. No offschedulecheckpoint, review, cycleorcompilationclaim.','scripts/integrate_alternating_tensor_closures.py')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,t,o,e in events:w.writerow([sid,datetime.now(timezone.utc).isoformat(),'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',t,o,e])
with (R/'LEDGER.md').open('a') as f:f.write('\n## All-count standard and two-tail alternating exclusions\n\n'+now+' — Q2ch,Q2ci,Q2ck refuted; Q2i strictly reduced afterreview10. '+standard2+standardall+tailall+'No formalreview or checkpoint inthisintegration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Three infinite alternating supplier families removed\n\n'+standard2+standardall+tailall+'These are actual finite-cover/local-system obstructions to dominating condition-A suppliers (cote16scan050;SIGN_NEXT SN-C03/C04), stated through rational representation lambda-rings, tensor K-theory and finite quotient morphisms. They supply no condition-I cycle and change no Markman, Severn or032 premise. The common schemes-over-Z, EGA/SGA/FGA, projector and motivic/L-function frame remains.\n')
result={'date_utc':now,'reviewed_files_reports':items,'canonical_sha256':canonical,'new_rows':sorted(newids),'strictly_reduced_main_gate':'Q2i','tail_checker_frozen_archive':str(frozen_dir.relative_to(R)),'root_status_hash_rerun':{k:rerun[k] for k in ('status','completed_utc','runtime_seconds','proof_sha256','script_sha256')}}
(R/'research/alternating_tensor_closures_integration.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
