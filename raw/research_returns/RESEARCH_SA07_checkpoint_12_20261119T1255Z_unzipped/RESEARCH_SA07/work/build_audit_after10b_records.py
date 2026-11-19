"""F3.29 primary-source, exact-certificate and scope records."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re

ROOT=Path('/workspace/scratch/f6dbb6638732')
DATE='2026-11-19'
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
LEDGER='work/audit_after10b_CHECK_EVENTS.tsv'
events=[]
def sha(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def event(s,t,o,who=WHO):events.append(dict(statement_id=s,date=DATE,who=who,type=t,outcome=o))

event('F.3.29','independent re-proof',
 'Proved q6 vanishing on the actual genus3 universal degree6 image with only one nonzero line constrained to be tangent. The complete180-dimensional balanced single-line space satisfies all mixed ES7 equations and the one additional scalar coefficient of R([D,delta_abc]) from MSS2026 Prop4.1. Its exact132-dimensional joint kernel has all105 contraction coordinates in the span of two actual J6 brackets. Equivariant extension and the post-constraint torus projector give the actual q6 conclusion. No CM decomposition, conjugate-line span or paired-orbit hypothesis is used.')
event('F.3.29','targeted proof check',
 'The primary R-vanishing theorem is imported explicitly from MSS2026v1 Prop4.1/4.2p11. Actual mapping classes extend by the identity to a stable-genus boundary surface, and R_G(i^tensor9 T)=i R_3(T) transfers vanishing injectively to genus3. The final proof uses no S equation, avoiding a raw-exterior-power versus primitive-quotient substitution. The associative centralizer Q[a], its primitive subspace Qa, and the full-logarithm rational conjugator removal prove the precise tangent condition on the one actual initial normalizer line.')
event('F.3.29','independent re-proof',
 'Root read the full proof, actual quotient maps and primary R formulas, and independently reran the core final certificate:exit0,internal33.973337743seconds. Root then read and approved the added exact b-run conjugator extraction, Dynkin test and R stabilization paragraph. Root approved integration after the independent elliptic rerun of that final revision.',
 WHO.replace('agent period_triangle','agent root'))
event('F.3.29','independent re-proof',
 'Elliptic independently read the final proof and primary MSS2026 Prop4.1/4.2, checked all five R contractions, the stabilization identity, invariant extension, projector and original-curve recognition map. Final revised program rerun:exit0,external42.928949937seconds,internal41.742954870seconds,start10:32:30.047760UTC. All180 paired-conjugator/Dynkin checks and all132x105 exact identities passed. Final source SHA2569b4d226893786c0edf7fc0ddd556d497ee7f9903971e940532becf2118367c4f.',
 WHO.replace('agent period_triangle','agent elliptic_splitting'))

code='output/RESEARCH_SA07/code/check_genus_three_single_line.py'
output='output/RESEARCH_SA07/code/check_genus_three_single_line.output.txt'
wall=re.search(r'ACTUAL_WALL_SECONDS ([0-9.]+)',(ROOT/output).read_text()).group(1)
record=dict(statement_id='F.3.29',code=code,output=output,code_sha256=sha(code),output_sha256=sha(output),
 actual_wall_seconds=wall,independent_root_core_wall_seconds='33.973337743',
 independent_elliptic_final_wall_seconds='42.928949937',independent_exit_codes=[0,0],
 input='Six symplectic generators; only D(a) tangent; complete15 balanced specialness blocks;20 mixed Johnson triples; scalar coefficient c of R([D,delta_abc]);105 contractions; two explicit sixfold Johnson brackets.')
event('F.3.29','computation or formal certificate',
 'All15 single-line specialness blocks have matching modular101 rank lower bounds and independent exact integer kernel lifts, proving total dimension180. Every basis vector has an explicitly reconstructed B with D(b)=[B,b]; the degree6 Dynkin identity certifies B is Lie. The7977x180 ES7-plus-one-R matrix has rank48:48 independent modular rows, exact rational row reduction,132 denominator-cleared independent kernels checked against every original integer row. All132x105 contraction identities hold over Z after clearing determinant-10752 against two literal J6 brackets. Largest kernel coefficient247830. Forty actual sevenfold Johnson brackets separately check implemented ES and R signs. Actual wall '+wall+'seconds; code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'.')
event('F.3.29','targeted proof check',
 'The original once-punctured genus3 curve now has cusp recognition for every prime and finite arithmetic base change without a Jacobian condition. The actual finite homology detector compares the same normalizer character with the first Magnus weight; weight1 is excluded by the single-line q6 theorem, and the actual boundary kernel gives the cyclotomic character on the full normalizer before applying Nakamura1994Th2.1.1. Separately, all-genus balanced single-line-to-paired tangency follows from cyclic-tensor reconstruction in constrained multiplicity1 and the certified three-handle basis in multiplicity>=2. An all-genus q6 theorem is not asserted.')
event('F.3.30','independent re-proof',
 'Constructed the exact invariant input reduction for every genus>=4: the Levi Sp(W) times Gm projector preserves actual U, tangency and q6; positive constrained multiplicity is reconstructed by T=-S8(b tensor[A,a])/m with explicit suffix-Lie and b-leading consistency equations. Dynkin images of15+90+90+20 decorated six-slot tensors span all positive parameters; five pure-complement special invariant tensors complete the input. All mixed equations remain coupled across ambient multiplicity blocks. Scalar dual contractions give explicit genus-polynomial rows, and the five-detector inclusion gives an exact map to ker q6. The mixed matrix and all-genus vanishing remain open.')
event('F.3.30','independent re-proof',
 'Root independently read LI.1-LI.6 and reopened original MSS2015 Prop7.2pp26-27. The actual invariant projector, positive-block at most six W slots, coupled mixed scalar rows, fixed matching-sign map and five-detector implication passed. Root approved production integration only at the completed reduction scope, with no all-genus q6 conclusion.',
 WHO.replace('agent period_triangle','agent root'))
event('F.3.30','independent re-proof',
 'Generation independently read LI.1-LI.6 and verified the actual Levi projector, cyclic identity S8 pi_b T=mT including periodic words, unique invariant conjugator,215-diagram span, five-dimensional pure-W component and five-detector output map. It checked that multiplicity projections need not preserve U and must remain coupled, and that scalar invariant-dual contractions avoid false output-basis independence in small complement genus. No all-genus vanishing was asserted.',
 WHO.replace('agent period_triangle','agent period_generation'))
event('F.3.30','targeted proof check',
 'The source matching coordinates and raw unsigned products differ by fixed row signs. The full-Sp projector is used only in the output implication, not to preserve tangency. The actual Levi projector is not represented as an individual Galois element. Formal support bounds and the finite input parametrization do not establish the remaining mixed-matrix rank or the full LM6A22 subgroup assertion.')
event('F.3.31','independent re-proof',
 'Completed at10:52:46UTC the actual witness map from every full-profinite nonperipheral procyclic subgroup with open normalizer to an integer s>=3 and a finite-matrix vector v with M(s)v=0 and LK(s)v!=0. Original NakamuraLemma2.1.4 gives an actual nonzero proper homology residue class in some finite cover; the same specified class is nonzero in torsion-free Z_l homology and Q_l. The characteristic l-component, finite-index powers, arithmetic normal core intersected with an actual genus3 cover, rational tangential cusp, and one-puncture filling preserve that proper class and the open normalizer. An actual G_L(6) class gives q!=0; the full-log correction gives tangency and the Levi projector preserves q. No primewise cyclotomic-character uniformity is required.')
event('F.3.31','independent re-proof',
 'Root independently reread original Nakamura1994Lemma2.1.4pp96-97 and the complete F3.23 normal-core proof, then checked FC1-FC7 including actual mod-l lift, genus raising, filling map, arithmetic degree6 lift, exponent1, full-log correction and explicit L. Root approved the full counterexample-to-matrix witness and finite Smith decision procedure before the actual10:55 review; the mixed inclusion remained uncomputed.',
 WHO.replace('agent period_triangle','agent root'))
event('F.3.31','independent re-proof',
 'Generation independently reread the original Nakamura1996pp115-117 images and verified both degree6 rank endpoints1, actual fibre surjection and finite-base invariance. Full FC1-FC7 audit passed for the original U0/Q: proper detector, characteristic l-component, arithmetic core/power pushforward, genus3-cover intersection, rational tangential descent, once-puncture filling, actual q-nonzero tangent vector and invariant projection. It checked alternating exterior-dual inputs, cyclic averaging on ES output, Q_l versus Q rank equivalence and the finite Smith normal form procedure. Audit saved in work/agent_full_profinite_composite_audit.md.',
 WHO.replace('agent period_triangle','agent period_generation'))
event('F.3.31','targeted proof check',
 'Explicit raw detector columns are(-104,-26,104,32,-32) and(-288,-72,288,192,-192). The integral matrix L=[[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]] has exactly their span as kernel. The fixed finite polynomial matrix uses alternating Lambda3 dual inputs and cyclic averages for ES coinvariants. Smith normal form over Q[s] gives generic polynomial identities and finitely many exceptional integer roots. This is a finitely decidable sufficient matrix certificate; its converse as a characterization of arithmetic subgroups is not asserted, and the quantified inclusion has not been verified.')

specs=[
 ('AuditNakamura1994','https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf',
  'ORIGINAL FULL-CLASS PROPER-HOMOLOGY DETECTOR REOPENED AND USED',
  'OriginalLemma2.1.4printedp96 and theorem proofp97: for every full class of finite groups and every nonperipheral z in the hyperbolic affine surface group, some prime l and open H containing z satisfy z notin[H,H]H^l<Z intersection H>. This detects the actual proper homology residue class, not merely open-curve homology. The actual filling map identifies that quotient with H1 of the compactification modl. Lemma2.1.2p95 supplies the peripheral centralizer input in the original lemma. Root and generation reread the full-class scope and source pages independently. The detector is applied before passing to any maximal pro-prime quotient of the original group.',
  'work/sources_audit_next/Nakamura1994.pdf','work/audit_after04_references.bib'),
 ('AuditMoritaSakasaiSuzuki2026v1','https://arxiv.org/pdf/2608.17673',
  'OPENED ORIGINAL V1; EXACT R FORMULA AND GEOMETRIC VANISHING USED',
  'Original28-page preprintv1,18August2026;399914-byte PDF downloaded from arXiv. Originalpp1-11 and21-25 read; p11 rendered and visually checked. Prop4.1p11 lists the five R contractions and eight S contractions; Prop4.2 states their quotient of the ES7 kernel on the [1]+[1^3] isotypical part. R vanishes on actual J7; stable-genus transfer is typed in F3.29. The source gives a sketch for Prop4.1, explicitly acknowledged. Final certificate uses only one R scalar and independently checks40 actual Johnson brackets. Th2.1p5,Th2.3p6 and Prop6.1p21 also read as source checks, but the explicit sigma3 formula is not required for F3.29. Root independently verified the table polynomials. Narrow arithmetic corrections: p22Prop6.3 displayed factors2g-1 should be2g+1 in f1(j1),f1(j2); p25 scalar term-3*(-3) should be-19*(-3). The final cancellation and stated trace ratio remain valid; these are not recorded as broad theorem refutations.',
  'work/sources_audit_next/FirstGaloisObstruction2026_arxiv2608_17673.pdf','work/audit_after10b_references.bib'),
 ('AuditMoritaSakasaiSuzuki2015v2','https://arxiv.org/pdf/1404.3351',
  'ORIGINAL INVARIANT-SPAN MAP REUSED; NORMALIZER AND FILLING SCOPE RECHECKED',
  'Prop2.1p8 gives the all-genus span of invariant tensor functionals by complete contractions; only surjectivity is used in genus3. Prop7.2p27 gives the five signed detector coordinates. Prop7.4 and Th7.5pp27-30 were reread: full Johnson normalizer conditions contain additional data beyond mixed ES7; formal j_g,1 membership alone is not geometric J membership. The final proof uses literal actual J6 brackets instead of assigning q6=0 to filling spiders.',
  'work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf','work/audit_after06_references.bib'),
 ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf',
  'ACTUAL UNIVERSAL QUOTIENT AND NONZERO FINITE-BASE CLASS REUSED',
  'Printedpp115-117, especially Lem4.5, finite-base invariance, degree6 rank table and actual GSp-equivariant sequences4.7.1/4.7.2. These give q6(J6)=0 and an actual sigma in G_L(6) with nonzero quotient for the same original genus3 curve. No formal tensor is declared an arithmetic Galois element; the weight projector is applied afterward inside the linear universal image.',
  'work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib')]
sources=[]
for key,url,status,detail,path,bib in specs:
 sources.append(dict(source_key=key,url=url,status=status,locator_and_access=detail,
  dependent_statement_ids='F.3.29; F.3.30; F.3.31',record_file=bib,date=DATE,who=WHO,local_path=path,sha256=sha(path)))
 event('SRC.'+key,'used and rechecked in this run',status+'. '+detail)

claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
before=Counter(row['status'] for row in claims)
ids={'I.B05.01','I.B05.02','II.MB15.02'}
addition=(' F3.29 proves the single-line q6 obstruction and complete once-punctured genus3 normalizer recognition without any Jacobian-simplicity or CM-pairing hypothesis. It also proves balanced single-line-to-paired tangency in every genus. An arbitrary rational detecting curve can have higher genus; the all-genus mixed-normalizer/contraction argument remains unproved, so the full A22 assertion is retained.')
for row in claims:
 if row['assertion_id'] not in ids:continue
 if ' F3.29 proves' not in row['remaining_obligation_or_scope']:row['remaining_obligation_or_scope']+=addition
 for key in ['proof_or_locator','canonical_dependencies']:
  if 'F.3.29' not in row[key]:row[key]+='; F.3.29'
  if 'F.3.30' not in row[key]:row[key]+='; F.3.30'
  if 'F.3.31' not in row[key]:row[key]+='; F.3.31'
 if ' F3.30 gives' not in row['remaining_obligation_or_scope']:
  row['remaining_obligation_or_scope']+=' F3.30 gives the exact Levi-invariant finite input and coupled scalar-polynomial matrix reduction; the mixed matrix and its all-genus contraction-image conclusion remain uncomputed.'
 if ' F3.31 gives' not in row['remaining_obligation_or_scope']:
  row['remaining_obligation_or_scope']+=' F3.31 gives the exact full-profinite counterexample-to-matrix witness, including the original proper-homology detector and residual-pronilpotent case, and a finite Smith decision procedure. The main remaining sufficient gate is the unverified all-integer-parameter kernel inclusion; no subgroup resolution is recorded.'
 row['check_event_statement_id']=row['assertion_id'];row['check_event_type']='targeted proof check';row['check_event_ledger']=LEDGER
 event(row['assertion_id'],'targeted proof check','Status '+row['status']+' retained.'+addition)
with (ROOT/'work/audit_claims.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
mdp=ROOT/'work/audit_claims.md';md=mdp.read_text();escape=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
 if row['assertion_id'] not in ids:continue
 line='| '+' | '.join(escape(row[key]) for key in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
 md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda _:line,md,flags=re.M);assert n==1
md=md.replace('Supplemental proofs F.3.1–F.3.28','Supplemental proofs F.3.1–F.3.29')
md=md.replace('Supplemental proofs F.3.1–F.3.29','Supplemental proofs F.3.1–F.3.30')
md=md.replace('Supplemental proofs F.3.1–F.3.30','Supplemental proofs F.3.1–F.3.31')
if '`audit_after10b_CHECK_EVENTS.tsv`' not in md:md=md.replace('`audit_after10_CHECK_EVENTS.tsv`.','`audit_after10_CHECK_EVENTS.tsv`, and `audit_after10b_CHECK_EVENTS.tsv`.')
mdp.write_text(md)
for path,rows,fields,delimiter in [(LEDGER,events,['statement_id','date','who','type','outcome'],'\t'),
 ('work/audit_after10b_source_checks.csv',sources,list(sources[0]),',')]:
 with (ROOT/path).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(rows)
(ROOT/'work/audit_after10b_computation_records.json').write_text(json.dumps([record],indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),
 status_counts=dict(Counter(row['status'] for row in claims)),addendum_event_count=len(events),source_record_count=len(sources),
 updated_claim_ids=sorted(ids),changed_statuses=[],canonical_new_result_ids=['F.3.29','F.3.30','F.3.31'],new_bibliography_keys=['AuditMoritaSakasaiSuzuki2026v1'])
assert before==Counter(row['status'] for row in claims)
(ROOT/'work/audit_after10b_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
