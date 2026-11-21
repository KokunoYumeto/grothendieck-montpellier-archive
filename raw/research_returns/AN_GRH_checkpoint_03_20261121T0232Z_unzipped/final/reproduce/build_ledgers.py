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
 'independent verifier rerun':'computation or formal certificate',
 'independent full proof check':'targeted proof check',
 'independent whole-proof recheck':'targeted proof check',
 'independent whole-proof review':'targeted proof check',
 'targeted full proof check':'targeted proof check',
 'source mapping and whole-proof check':'targeted proof check',
 'full new-proof check':'targeted proof check',
 'multiple-cover bypass audit':'targeted proof check',
 'recovered abelian norm criterion check':'targeted proof check',
 'primary projection proof check':'targeted proof check',
 'full arithmetic deduction check':'targeted proof check',
 'small-count deduction':'targeted proof check',
 'attempted extension check':'targeted proof check',
 'obstruction cross-check':'targeted proof check',
 'primary-source check':'used and rechecked in this run',
 'primary-source reduction check':'used and rechecked in this run',
 'primary-source scope check':'used and rechecked in this run',
 'primary theorem check':'used and rechecked in this run',
 'primary formula check':'used and rechecked in this run',
 'primary analytic theorem scope check':'used and rechecked in this run',
 'arithmetic wording correction':'used and rechecked in this run',
 'targeted primary theorem check':'used and rechecked in this run',
 'source qualification':'used and rechecked in this run',
 'source recovery':'used and rechecked in this run',
 'remaining-gate audit':'used and rechecked in this run',
 # This is an author's account of a review response, not a second event
 # claiming that the author was the independent reader named in that response.
 'independent proof review response':'used and rechecked in this run',
 'independent review reported':'used and rechecked in this run',
 'independent arithmetic review reported':'used and rechecked in this run',
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
question('Q-HOOLEY','Prompt task1; intake; positive-rank follow-up','§3.3(3); §5(a), route2; A07–A20','Can the requested A1 proof be obtained from M through a theta-incidence bridge?','REQUESTED ROUTE NOT ESTABLISHED; the sufficient geometric criterion now permits arbitrary odd conductor on every genus-two base, but universal finite-field positive-rank incidence remains unproved','A02,A03,A04,A06,A07,A08,A09,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20','For every positive-2-rank genus-two finite-field curve, produce a nontrivial odd cyclic cover whose primitive factor has geometric 2-rank zero. Equivalently in the genus-two character description, obtain a cyclic odd-order class whose theta multiples meet every doubling orbit of primitive characters. A single theta point of exact order n with <2,-1> equal to the full unit group suffices; n need not be a prime power. Another separation argument could also suffice. A1 itself is proved by A05.','A06 refutes the unrestricted rank-zero primitive-root premise. A07 has transcendental moduli and is not a finite-field counterexample; A08 has finite-list quantifiers. A12–A14 give a Lang test, an ordinary example and its fixed-prime limitation. A16 verifies a composite example. A17 supplies arithmetic candidate orders under M; A18 removes the geometric elliptic-quotient exception. A19 makes each fixed prime support an exact finite search, while A20 disproves the single-prime 3-power strategy on one rank-one curve. No theorem forces one of the unbounded-prime searches to succeed.')
question('Q-GENERIC-POSITIVE-RANK','Ozman–Pries2019; Yang2021; AN_GRH','Theorems1.1(2),8.3; Yang Theorems1.1,3.5; A07','Does positive2-rank force odd prime-order theta incidence over every finitely generated characteristic-two field?','REFUTED: one geometric generic genus-two curve in each rank1 or2 stratum avoids every odd prime order; the generic ordinary case also avoids every nonzero odd order','A07','This does not decide exact-order incidence for curves over finite extensions of F2.','Finite-coefficient descent gives a finitely generated field with transcendental moduli; no finite-field specialization preserving an infinite collection of avoidance conditions is asserted. Original Nakajima text was not recovered.')
question('Q-FINITE-THETA-LIST','Ozman–Pries2019; Yang2021; ANABELIAN_SUCCESSOR A.16; AN_GRH','A08 and its ordinary strengthening','Can one finite candidate list of orders guarantee theta incidence for all finite-field genus-two curves of fixed positive2-rank?','REFUTED: for either rank1 or2 every finite list of odd primes is simultaneously avoided by some finite-field curve; for ordinary curves the list may contain arbitrary odd orders','A08','The finite field and curve depend on the list; no effective extension-degree bound or single finite-field curve avoiding all orders is supplied. The rank1 prime-power extension is not inferred.','Scheme-family spreading and finite closed incidence images prove forall finite list exists curve. Generic absence of all odd orders is used only for the ordinary strengthening.')
question('Q-RANK1-THETA13','Recovered ANABELIAN_A1 B.39/B.LIT7; AN_GRH','A09; identities PR.1–PR.3 and PR.10','Is there a concrete positive-rank instance of the sufficient theta bridge?','PROVED: the rank1 curve Y^2+X^2Y=X^5+X has an explicit exact-order13 theta class overF16; 2 generates the units modulo13, and the associated cyclic cover has zero2-rank new factor','A09,A11','','The complete principal-divisor certificate and separate verifier support the displayed example. Its four F2 points share a prime-to2 abelian Kummer class because #J(F2)=8, while the covering argument separates their full point-section classes. The direct Kummer model is distinguished from the retained Lang-cover model.')
question('Q-NONORDINARY-THETA3','AN_GRH','A10','Can a nonordinary genus-two curve in characteristic two have a nonzero order3 point on its Raynaud theta divisor?','REFUTED: no such point exists; every connected cyclic etale degree3 cover has ordinary new factor','A10','','Applies to ranks0 and1. The proof uses the effective theta characteristic and h0(2W)=h0(3W)=2. Ordinariness of the new factor does not make the whole cover ordinary over a nonordinary base.')
question('Q-PRIME-POWER-BRIDGE','AN_GRH; Poonen2005','A11; Poonen Theorem1.8; later A18','Does exact prime-power theta incidence with <2,-1>=units suffice, and does primary projection supply it?','PROVED sufficient bridge for n=ell^r on every genus-two base: the primitive factor equals the relative Prym, has zero 2-rank, and excludes a point-section collision. It is a special case of the later arbitrary-odd geometric criterion A18.','A11,A18','Universal incidence remains unresolved. Poonen projection leaves an uncontrolled coprime factor m; multiplying by m need not preserve theta. Composite order is now allowed by A18, but its unit-group or primitive-orbit coverage condition is not supplied by that projection theorem.','Theta symmetry supplies the two possible Frobenius orbits; no non-Wieferich assumption is needed. Additional proper-conductor blocks obstruct only the original single-deck-element argument, not A18 with geometric primitive rank zero. No necessity of prime-power order is claimed.')
question('Q-LANG-THETA-TEST','AN_GRH; Poonen2005; finite-field Weil bound','A12; LW.1–LW.9','Is there an explicit curve-dependent test for theta incidence in a pure prime-power subgroup?','PROVED unconditionally: for a=[J(F_Q):H], the Lang pullback has genus a+1 and #Y(F_Q)=a times #Theta(F_Q) intersect H. In particular Q+1-2(a+1)sqrt(Q)>a guarantees a nonzero theta point in H.','A12,A11','For H=J(F_Q)[ell^r], actual success of the numerical test and <2,-1>=(Z/ell^r Z)^times are still required. This is a sufficient test, not a necessary condition for theta incidence.','The pullback is geometrically connected even when a has a characteristic-primary part. A nonzero point in H has exact order ell^s for some 1<=s<=r, and the unit-group condition descends to that order. All counting input is unconditional finite-field purity, not number-field GRH.')
question('Q-ORDINARY-THETA4159','AN_GRH; exact arithmetic certificates','A13; LW.10–LW.17','Does the explicit Lang test yield a verified ordinary genus-two example?','PROVED: the ordinary F2 curve y^2+y=x+x^(-1)+(x-1)^(-1) has at least four theta points over F128 of exact order 4159, and <2,-1> is the full unit group modulo 4159. A11 gives a separating cyclic cover of that prime degree.','A12,A13,A11','','The exact count #J(F128)=16636=4*4159 gives subgroup index a=4 and the lower bound N_H>=4. The order of 2 is 2079, so 2 alone is not a primitive root; adjoining -1 supplies the full group. A separate resultant calculation checks the Jacobian order. No universal incidence conclusion is inferred.')
question('Q-FIXED-PRIME-LANG-BARRIER','AN_GRH','A14; LW.18–LW.24; later A19','Can enlarging the constant field at one fixed odd prime force the sufficient Lang test to succeed?','REFUTED for that numerical strategy: at fixed ell, the ell-primary subgroup has order at most C_ell*m^4 over F_(q^m), and the sufficient inequality fails for every r once m reaches the explicit computable threshold.','A14,A19','Varying ell requires information about large pure prime-power divisors of det(1-Phi^m), together with the unit-group condition. An Artin-prime density theorem alone does not provide that information. A19 separately gives a finite exact decision at each fixed prime support.','This is eventual failure of the sufficient Lang inequality, not absence of theta torsion or failure of computability. It uses the determinant valuation after Phi^d=1 modulo ell and the unconditional Weil lower bound. A19 bounds all primary exponents by a different geometric argument.')
question('Q-COMPOSITE-PRIMITIVE-BRIDGE','ANABELIAN_SUCCESSOR final A.14 / AC.11; AN_GRH','A15; CB.1–CB.5; later A18','What does the original composite projector argument prove when only rational primitive 2-primary torsion is excluded?','PROVED for every odd n>1 on a rank-one genus-two base, or one known to have no separable double cover of a genus-one curve: a pointed cover with P_n(L)[2^infinity]=0 suffices. With geometric primitive rank zero, A18 removes that base restriction and works in every genus at least two.','A15,A18','The rational-only statement keeps its geometric qualification unless the extra nonordinarity condition of A18 is known. Universal finite-field existence of the needed cover or theta-orbit coverage remains unproved.','The projector produces a function of degree 2^omega(n); the Castelnuovo–Severi reduction forces an elliptic double quotient. Rank one excludes it by Deuring–Shafarevich. A18 instead computes its positive primitive rank. Proper-conductor factors may remain ordinary, as in A16. Theta points in unrelated cyclic groups do not establish coverage in one primitive block.')
question('Q-COMPOSITE-THETA15','AN_GRH; explicit finite-field certificates','A16; CE.1–CE.5','Can a rank-one base have a theta class of exact order 15 and a separating composite-degree cover whose proper-conductor factors remain ordinary?','PROVED displayed example: the F8 curve has a theta class of exact order 15; its cyclic cover of degree 15 has genus 16 and 2-rank 7. The primitive conductor-15 factor has rank zero, while conductor-3 and conductor-5 factors are ordinary of dimensions 2 and 4. A15 supplies point separation.','A15,A16','','The norm identity and exact-order exclusions support this concrete example; the producer and independent symbolic verifier are retained. The whole new factor has positive 2-rank 6. No claim is made that the curve lacks a prime-power witness or that the finite search classifies curves. The smaller degree-5 comparison is a separate proved example, without a minimality claim.')
question('Q-ARTIN-COMPOSITE-CANDIDATES','Lenstra1977; AN_GRH','A17; AF.1–AF.5; Lenstra Theorem3.1; later A18–A19','Does M supply an infinite arithmetic family of composite conductors eligible for the genus-two theta bridge?','PROVED conditional on M: primes q=5 modulo 8 with ord_q(2)=q-1 have natural density Artin_constant/2 among primes. For each such q, <2,-1>=(Z/3qZ)^times. A18 makes this an eligible family on every genus-two base.','A17,A18,A19','For a given finite-field curve, still obtain a theta point of exact order q or 3q for one of these primes, or the more general primitive-orbit coverage. A16 supplies q=5 on one curve. Poonen projection does not force its remaining cofactor to be a prime in this family. A19 makes each fixed support {3,q} finite, without bounding the successful prime q.','The sufficient analytic family is Dedekind GRH for Q(zeta_n,2^(1/n)) with squarefree n, contained in M and not discharged by the stipulated Dirichlet scope. Lenstra supplies the infinite-limit step; finite Chebotarev inclusion-exclusion alone would not establish the density. Arithmetic density does not prove geometric incidence.')
question('Q-GEOMETRIC-PRIMITIVE-BRIDGE','AN_GRH; Poonen gonality and Deuring–Shafarevich inputs','A18; GP.1–GP.9','Does a geometric primitive rank-zero cover suffice without excluding elliptic double quotients?','PROVED in characteristic two for every genus at least two and every nontrivial odd cyclic etale conductor: geometric 2-rank zero of the primitive factor implies the finite-field point-section separation conclusion. No prime-power or non-bielliptic hypothesis is needed.','A18,A15','Existence of such a cover on every positive-rank curve is not established. The exact theta-orbit characterization still uses genus-two one-dimensional character spaces. A rational torsion-zero condition over just one field is weaker and retains the stated qualification.','A proposed collision forces an actual pullback from an etale elliptic isogeny. Deuring–Shafarevich at every intermediate conductor and Mobius inversion force f(P_n)=r*phi(n)>0. For genus two r=1 and the whole new factor is ordinary; consequently rational torsion zero plus known nonordinarity also excludes a collision.')
question('Q-FINITE-SUPPORT-THETA','AN_GRH; Boxall-type argument proved in full','A19; FS.1–FS.10','Can all exponents be decided exactly when the odd prime support of a genus-two theta point is fixed?','PROVED unconditionally: if Phi^d is identity on J[ell] for every ell in finite S, every geometric S-primary theta point is rational over F_(Q^d). Their orders divide the S-part of #J(F_(Q^d)), so one terminating finite-field search covers all exponents.','A19','The prime support still ranges over an unbounded set; the result does not prove that a search succeeds for every curve or give a practical running time. It does not supply the unavailable original Boxall chapter statement.','An explicit choice is d=lcm over ell in S of |GL4(F_ell)|. A nonfixed primary component would create an ell-cycle under translation inside both theta and a nontrivial translate, contradicting their at-most-two-point intersection. Exact orders and doubling-orbit coverage can then be tested. For fixed q, all orders supported on {3,q} are covered at once.')
question('Q-RANK1-NO-THREE-POWER','AN_GRH; exact A20 certificates','A20; TP.1–TP.4','Does allowing arbitrary powers of 3 always supply a positive-rank theta witness?','REFUTED: on the rank-one A09 curve Y^2+X^2Y=X^5+X, the entire geometric 3-primary theta intersection is {0}, despite its exact-order13 theta witness.','A20,A19,A10,A09','This excludes one fixed-prime strategy on a specific positive-rank curve. It does not refute the existence of a witness at another odd prime or composite support, and it does not obstruct A1 on this curve.','Cayley–Hamilton gives Phi^20=1 on J[3]; #J(F_(2^20))=1099812538656 has 3-adic valuation 4, so its rational 3-primary subgroup equals J[3]. A19 captures every geometric 3-primary theta point in that field; A10 excludes its nonzero order-three points. The determinant and independent resultant certificates verify the finite arithmetic.')
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
