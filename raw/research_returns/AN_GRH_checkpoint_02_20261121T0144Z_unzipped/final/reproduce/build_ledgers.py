"""Regenerate the question and merged check-event tables from retained evidence."""
from pathlib import Path
import csv, json
R=Path(__file__).resolve().parent.parent
D='2026-11-21'
WHO='GPT-6 Astra Pro; effort not exposed; AN_GRH /root'
EVENT_FIELDS=['statement_id','date','who_model_effort_run','type','outcome','evidence']
# These are the six categories specified in the supplied user prompt.
CHECK_EVENT_TYPES={
 'targeted proof check',
 'independent re-proof',
 'computation or formal certificate',
 'used and rechecked in this run',
 'carried as background without fault found',
 "refuted, with the refined statement's id",
}
# A different reader checking a whole written proof has not thereby rebuilt it
# independently. No alias below promotes proof reading to independent re-proof.
CHECK_EVENT_TYPE_ALIASES={
 'computational recheck':'computation or formal certificate',
 'exploratory arithmetic check':'computation or formal certificate',
 'finite exact computation':'computation or formal certificate',
 'independent finite exact computation':'computation or formal certificate',
 'independent verifier backend check':'computation or formal certificate',
 'independent full proof check':'targeted proof check',
 'targeted full proof check':'targeted proof check',
 'small-count deduction':'targeted proof check',
 'attempted extension check':'targeted proof check',
 'obstruction cross-check':'targeted proof check',
 'primary-source check':'used and rechecked in this run',
 'primary-source reduction check':'used and rechecked in this run',
 'primary-source scope check':'used and rechecked in this run',
 'targeted primary theorem check':'used and rechecked in this run',
 'source qualification':'used and rechecked in this run',
 'source recovery':'used and rechecked in this run',
 'remaining-gate audit':'used and rechecked in this run',
 # This is an author's account of a review response, not a second event
 # claiming that the author was the independent reader named in that response.
 'independent proof review response':'used and rechecked in this run',
}
def normalize_event(x,origin):
 raw=x.get('type','')
 label=raw.strip()
 canonical=label if label in CHECK_EVENT_TYPES else CHECK_EVENT_TYPE_ALIASES.get(label)
 if canonical is None:
  raise ValueError(f"Unmapped check-event type {raw!r} for {x.get('statement_id')!r} in {origin}; inspect its actual outcome before assigning a category")
 outcome=x.get('outcome','')
 if canonical!=raw:
  outcome=f'[Original recorded type: {raw!r}; normalized category only.] '+outcome
 return dict(statement_id=x.get('statement_id',''),date=x.get('date',D),
  who_model_effort_run=x.get('who_model_effort_run',x.get('who',WHO)),
  type=canonical,outcome=outcome,
  evidence=x.get('evidence',x.get('locator',origin)))
def read(name):
 with open(R/name,newline='',encoding='utf-8') as f:return list(csv.DictReader(f,delimiter='\t'))
def write(name,rows,fields):
 with open(R/name,'w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
q=[]
def question(i,src,loc,ask,state,findings='',gate='',scope=''):
 q.append(dict(id=i,source=src,locator=loc,question=ask,state=state,finding_ids=findings,current_gate=gate,evidence_scope=scope))
question('Q-A1','Cote149; ANABELIAN_A1','scans33–38; A.1,A.2–A.5,A.14–A.19,A.30–A.33','Is the exact curve point-section map injective with the full arithmetic quotient?','PROVED unconditionally by the recovered cuspidal proof','A01,A05','','Whole proof reconstructed and checked; no originality or formal verification claimed.')
question('Q-HOOLEY','Prompt task1; intake; positive-rank follow-up','§3.3(3);§5(a),route2; A07–A11','Can the requested A1 proof be obtained from M through a theta-incidence bridge?','REQUESTED ROUTE NOT ESTABLISHED; A11 proves a sufficient prime-power bridge, but its universal finite-field positive-rank existence premise remains open','A02,A03,A04,A06,A07,A08,A09,A10,A11','For every positive-2-rank genus-two curve over a finite extension of F2, produce a geometric theta point of exact odd prime-power order n=ell^r with <2,-1>=(Z/nZ)^times, or supply an alternative geometric bridge controlling the needed proper-conductor factors. A1 itself is already proved by A05.','A06 refutes the unrestricted primitive-root prime-order premise on a rank-zero curve. A07 has transcendental moduli, so is not a finite-field counterexample. A08 has quantifiers: for every finite candidate list, some curve avoids that list. Hooley supplies neither exact-order theta incidence nor the unit-group condition at arbitrary higher prime powers.')
question('Q-GENERIC-POSITIVE-RANK','Ozman–Pries2019; Yang2021; AN_GRH','Theorems1.1(2),8.3; Yang Theorems1.1,3.5; A07','Does positive2-rank force odd prime-order theta incidence over every finitely generated characteristic-two field?','REFUTED: one geometric generic genus-two curve in each rank1 or2 stratum avoids every odd prime order; the generic ordinary case also avoids every nonzero odd order','A07','This does not decide exact-order incidence for curves over finite extensions of F2.','Finite-coefficient descent gives a finitely generated field with transcendental moduli; no finite-field specialization preserving an infinite collection of avoidance conditions is asserted. Original Nakajima text was not recovered.')
question('Q-FINITE-THETA-LIST','Ozman–Pries2019; Yang2021; ANABELIAN_SUCCESSOR A.16; AN_GRH','A08 and its ordinary strengthening','Can one finite candidate list of orders guarantee theta incidence for all finite-field genus-two curves of fixed positive2-rank?','REFUTED: for either rank1 or2 every finite list of odd primes is simultaneously avoided by some finite-field curve; for ordinary curves the list may contain arbitrary odd orders','A08','The finite field and curve depend on the list; no effective extension-degree bound or single finite-field curve avoiding all orders is supplied. The rank1 prime-power extension is not inferred.','Scheme-family spreading and finite closed incidence images prove forall finite list exists curve. Generic absence of all odd orders is used only for the ordinary strengthening.')
question('Q-RANK1-THETA13','Recovered ANABELIAN_A1 B.39/B.LIT7; AN_GRH','A09; identities PR.1–PR.3 and PR.10','Is there a concrete positive-rank instance of the sufficient theta bridge?','PROVED: the rank1 curve Y^2+X^2Y=X^5+X has an explicit exact-order13 theta class overF16; 2 generates the units modulo13, and the associated cyclic cover has zero2-rank new factor','A09,A11','','The complete principal-divisor certificate and separate verifier support the displayed example. Its four F2 points share a prime-to2 abelian Kummer class because #J(F2)=8, while the covering argument separates their full point-section classes. The direct Kummer model is distinguished from the retained Lang-cover model.')
question('Q-NONORDINARY-THETA3','AN_GRH','A10','Can a nonordinary genus-two curve in characteristic two have a nonzero order3 point on its Raynaud theta divisor?','REFUTED: no such point exists; every connected cyclic etale degree3 cover has ordinary new factor','A10','','Applies to ranks0 and1. The proof uses the effective theta characteristic and h0(2W)=h0(3W)=2. Ordinariness of the new factor does not make the whole cover ordinary over a nonordinary base.')
question('Q-PRIME-POWER-BRIDGE','AN_GRH; Poonen2005','A11; Poonen Theorem1.8','Does exact prime-power theta incidence with <2,-1>=units suffice, and does primary projection supply it?','PROVED sufficient bridge for n=ell^r: the primitive factor equals the relative Prym, has zero2-rank, and excludes a point-section collision. Universal finite-field incidence is UNRESOLVED','A11','Obtain exact odd prime-power order n with <2,-1>=(Z/nZ)^times, or control all additional proper-conductor factors by another argument. Poonen projection leaves an uncontrolled coprime factor m; multiplying by m need not preserve theta.','The criterion is a finite group computation and requires no non-Wieferich assumption. Theta symmetry supplies the two possible Frobenius orbits. Composite n with distinct prime factors has additional proper-conductor blocks, so primitive-zero alone is insufficient for the same deck-element argument.')
question('Q-ARTIN','Hooley1967; FanPollack2025','§7 concluding theorem; Theorem1.1','What primitive-root theorem follows from the two inputs?','PROVED conditional on M; not discharged by stipulated Dirichlet scope','A02','M remains a draft claim.','Exact Kummer Dedekind family identified.')
question('Q-ALP-A1','Prompt task1','Alpoge Main/Statements; A05','What does Alpoge alone give for A1?','A1 holds already without A; A supplies neither the missing Kummer family by the stated route nor the geometric bridge','A05,S02','','No logical-independence theorem is asserted.')
question('Q-M-SOURCE','Masullo supplied draft','§1.2; Th13.3.1.1,Th13.3.1.2,p522','Is there a completed numbered GRH theorem at the cited main locator?','SOURCE CLAIM CHECKED: intended Th13.3.1.2 has no statement','S01','All M consequences remain conditional on the claimed scope.','Page text and rendering inspected; not a whole-draft review.')
question('Q-ANALYTIC-SCOPE','Prompt input comparison','A Main/Statements; M§1.2','Which zeta families are discharged?','PROVED scope transfer: A for abelian Q-fields; M for arbitrary number fields','S02','','Primitive Dirichlet factorization and trivial Hecke specialization.')
question('Q-BACH','Bach1990; prompt/Fable7','Theorems2–3,pp372–373','What uniform prime-generator bound is supported by the cited theorem?','PROVED correction: strict3(log N)^2 for units under A','T01','','No counterexample to coefficient2 unit generation is claimed.')
question('Q-GT-SCOPE','LM7,LM8','E58/E65; C12,C49','What does a cyclotomic certificate certify?','PROVED subgroup and character test; broader GT inference refuted in stated scope','T02','','E58 profinite construction is carried background.')
question('Q-GT-FAMILIES','LM7,LM8','E1,E4; C33–C38','Can the identified infinite scalar towers be certified?','PROVED elementary2-bound for2^a3^b and5^b; exact12j andp^(k+1) scalar precision','T03,T04','','General identified moduli use T01.')
question('Q-GT-EXHAUSTIVE','GT_TOWER_CHECK','unrecovered180-row register','Were all original finite targets identified and checked?','INCOMPLETE source coverage','T06','Recover full register/paper and actual quotient maps.','All53identified arithmetic moduli verified.')
question('Q-CHEB','BachSorenson1996','Theorem5.1; §2 lastparagraph','What explicit finite Frobenius-prime bound follows?','PROVED conditional consequence under exact zeta hypotheses','G01,G02','General fields require M; abelian Q-fields fit A.','B(L)=(4logD+(5/2)n+5)^2, with finite exclusions via quadratic compositum.')
question('Q-ADIC','Prompt task4; MayleWang2024','Prop12; AN_GRH G03','Is there a complete finite trace test for full adic representations?','PROVED for semisimplifications under M','G03','Exact trace computation is needed to implement the finite test.','Integral coefficient DVR, rank and ramification hypotheses retained.')
question('Q-EXTENSION','Prompt task4','AN_GRH G04','Do Frobenius traces determine arbitrary extension classes?','REFUTED by explicit nontrivial unipotent cyclotomic-log extension','G04','','Semisimplifications are still determined.')
question('Q-OPEN-IMAGE','MayleWang2024; Lombardo2015','Theorems1–2; Corollary9.3,p2393','What numerical open-image and trace-separation constants follow?','PROVED cited Mayle–Wang consequences under M overQ; unconditional Lombardo adelic-index bound over general number fields','G-MW1,G-MW2,G-LOMBARDO','','Non-CM hypotheses retained; no general higher-dimensional bound.')
question('Q-LM8-FACTORS','LM8_PUSH; AN_GRH','A14,A32,A33; G06','Can the actual elliptic factors receive the stated explicit bound?','PROVED: descent toQ verified; underM ell>964log6+5760 gives full Q-image; overL index≤[L:Q]; unconditional adelic-index bound also given','G06','','F_(±6):y²=x³−3x±6; j=−216; bad support{2,3}. No full-image assertion overL.')
question('Q-LLS','LLS2015 corrected arXivv3','Theorem1.1; AN_GRH T07','Does the sharper general-subgroup estimate recover coefficient2?','PROVED sufficient criterion and coefficient2 for all integerN≥exp300 underA','T07','The remaining finite interval is not exhaustively checked.','Exact bound-expression examples are not generator counterexamples.')
question('Q-LM7-PREDICATES','LM7 full register','A16,A25','Can the two actual arithmetic prime predicates receive explicit exclusion bounds?','PROVED: G05.1 underA andG05.2 underM','G05','Original group-presentation proofs remain unavailable.','Arithmetic predicates reconstructed and proved independently.')
question('Q-COVERAGE','Sixsorted summaries; recovered archives','R01; source manifests','Is the complete1190-row audit possible from the available sources?','INCOMPLETE:800 full statements,591 available proof blocks','R01,T06','390 full statements and209 further LM7 proof blocks unavailable.','Every supplied flag and recovered row represented; no all-proof verification claim.')
question('Q-TRANSCRIPTION','Cote149','scans33–38','Which mathematical readings need a second pass against the handwriting?','CHECKED mathematical candidates; manuscript readings unverified','TN01–TN06','Original scan images required to decide transcription versus authorial lapse.','See TRANSCRIPTION_NOTES.tsv.')
# One record per actual programme-row audit question. Curated entries override general screens.
curated=read('ROW_ANALYTIC_LEDGER.tsv')
cm={(x['run'],x['row_id']):x for x in curated}
seen=set()
for x in read('ROW_FULL_REGISTER_AUDIT.tsv'):
 key=(x['run'],x['row_id']);seen.add(key);c=cm.get(key)
 if c:
  st=c['under_Alpoge_Dirichlet_GRH']+' | M: '+c['under_Masullo_all_field_Hecke_GRH'];gate=c['missing_theorem_or_data'];scope=c['evidence_scope'];fid=c['audit_id']
 else:
  st=x['direct_classification'];gate=x['missing_theorem_or_data'];scope=x['evidence_scope'];fid=x['direct_audit_id']
 question('AUDIT:'+key[0]+':'+key[1],key[0],x['proof_locator'] or x['register_source'],'Which analytic inputs, if any, occur in this recorded row? '+x['statement_original'],st,fid,gate,scope)
for x in curated:
 key=(x['run'],x['row_id'])
 if key in seen:continue
 seen.add(key)
 question('AUDIT:'+key[0]+':'+key[1],key[0],x['source_locator'],x['operation'],x['under_Alpoge_Dirichlet_GRH']+' | M: '+x['under_Masullo_all_field_Hecke_GRH'],x['audit_id'],x['missing_theorem_or_data'],x['evidence_scope'])
for x in read('ROW_UNIQUE_AUDIT.tsv'):
 key=(x['run'],x['row_id'])
 if key in seen:continue
 seen.add(key)
 question('AUDIT:'+key[0]+':'+key[1],key[0],x['file_and_line'],'Does the flagged statement evidence a GRH, effective Chebotarev, Artin primitive-root, or least-prime dependence? '+x['statement'],x['classification'],x['audit_id'],x['missing_statement_or_data'],x['evidence_scope'])
for x in read('ROW_EXCERPT_ONLY_AUDIT.tsv'):
 key=(x['run'],x['row_id'])
 if key in seen:continue
 seen.add(key)
 question('AUDIT:'+key[0]+':'+key[1],key[0],x['source_locator'] or x['available_in'],'Can the analytic dependence of this visible row be completely checked?',x['classification'],'',x['limit'],'Excerpt or identifier only.')
for x in read('GT_UNIT_CERTIFICATES.tsv'):
 n=x.get('N') or x.get('modulus')
 question('GT-UNIT:'+str(n),'GT_UNIT_CERTIFICATES.tsv','N='+str(n),'Do the supplied primes below strict2(log N)^2 generate U_N?','PROVED by complete unit-word certificate','T05','','Exact modular evaluation and rational logarithm interval checks.')
write('QUESTIONS.tsv',q,['id','source','locator','question','state','finding_ids','current_gate','evidence_scope'])
# Normalize the actual recorded check fragments without changing event meanings.
events=[]
for f in sorted((R/'evidence/check_events').glob('*.tsv')):
 for x in read(f.relative_to(R)):
  events.append(normalize_event(x,str(f.relative_to(R))))
if (R/'evidence/root_check_events.json').exists():
 events.extend(normalize_event(x,'evidence/root_check_events.json') for x in json.loads((R/'evidence/root_check_events.json').read_text()))
# Preserve independent events, removing only byte-identical normalized duplicates.
unique=[];keys=set()
for x in events:
 key=tuple(x[k] for k in EVENT_FIELDS)
 if key not in keys:keys.add(key);unique.append(x)
write('CHECK_EVENTS.tsv',unique,EVENT_FIELDS)
print('Questions:',len(q),'Check events:',len(unique))
