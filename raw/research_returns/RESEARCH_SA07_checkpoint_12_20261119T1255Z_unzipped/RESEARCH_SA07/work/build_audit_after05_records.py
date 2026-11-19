"""Canonical records for root-approved F.3.18--20; no root combined file edits."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re
ROOT=Path('/workspace/scratch/f6dbb6638732')
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
DATE='2026-11-19'
LEDGER='work/audit_after05_CHECK_EVENTS.tsv'
PROOF='targeted proof check';REPROOF='independent re-proof';USE='used and rechecked in this run';BACKGROUND='carried as background without fault found';CERT='computation or formal certificate'
events=[]
def event(sid,kind,outcome):events.append(dict(statement_id=sid,date=DATE,who=WHO,type=kind,outcome=outcome))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest() if p else ''

event('F.3.18',REPROOF,'Proved rank-one Galois homology forces an actual simple CM quotient. A rational simple-factor projection is cleared to a genuine surjective abelian-variety map. Faltings supplies a rank-one idempotent in D tensor Q_l; its exact rank m times the sum of s_lambda*d*delta_lambda*[E_lambda:Q_l] equals1, forcing m=d=1 and a degree-one completion. The rank-one E-module complex structure excludes real embeddings; Rosati positivity makes the fixed field totally real, proving E is CM. The actual Prym projector is n*id-f^*f_*; composed with the quotient and Abel-Jacobi it detects the line. Root independently checked all rank, Rosati and morphism steps and passed. Dimension1 and punctured-fibre containment are not asserted for arbitrary covers.')
event('F.3.19',REPROOF,'Constructed C20 to C4 by fifth powers and the degree800 cover to E0, branched only overO. The degree40 map (X,Y)=((x/z)^4,(y/z)^10) lands on the genus2 curve Y^2=1-X^5. Its Jacobian contains Q(zeta5), and absolute simplicity follows by ruling out every elliptic product algebra: in M2(D) for imaginary quadraticD, the commuting degree8 field would equal a noncommutative algebra, impossible by explicit matrix units. Norm-pullback gives q_*q^*=[40], f_*q^*=0 and integral Tate injection into the connected Prym for every prime. The inverse fibre of infinity is exactly z=0 and is removed. Root independently checked all steps and passed. No arithmetic-normalizer lift is supplied.')
event('F.3.20',REPROOF,'Proved all-prime normalizer recognition for every once-punctured elliptic curve over every number field. Actual finite-cover homology forces first Magnus degree1 or2. Faltings excludes non-CM and nonsplit-CM rank-one cases; in split CM the character ratio remains infinite on every open subgroup. The nonzero N6 degree6 quotient of character chi^3 is projected within the actual closed arithmetic image; the two complete middle-weight special-derivation matrices have determinant-8. The nonprimitive lower inner conjugator is removed in rational completion and degrees3-6 are cancelled before the degree7 contradiction. Degree2 gives the actual cyclotomic exponent, so Nakamura1994 supplies actual inertia. Root independently read the proof and original sources and passed, then independently ran the coefficient certificate successfully. Arbitrary higher-genus/full-profinite A22 is not inferred.')
event('F.3.20',PROOF,'Checked the actual-element step rather than only its rational shadow. M is the compact image of H intersect G_K(6) in the finite-free degree6 lattice, so it is a closed Z_l-module invariant under conjugation by an actual tau inH. The spectral projection to chi^3 has Q_l coefficients; multiplying by l^r clears them, hence the nonzero projected vector belongs toM. The definition ofM lifts it to an actual sigma inH intersect G_K(6). Root reviewed this chain and passed. Both determinant-8 obstructions are used only over Q_l, including l=2; no integral division by8 or chosen arithmetic section is asserted.')

computations=[]
for sid,name,desc,rootwall in [
 ('F.3.19','check_CM_surface_Prym','Exact C20 morphism equations;40/25 finite deck scalings; primitive Phi5 action; unique real quadratic subfield; explicit noncommuting matrix units; genus171 and degrees800/40.','0.535934'),
 ('F.3.20','check_elliptic_degree_six','Independent associative-word construction; full middle special space has dimension2; both displayed derivations preserve omega; both exact5x5 obstruction matrices have determinant-8.','0.656353')]:
 code='output/RESEARCH_SA07/code/'+name+'.py';output='output/RESEARCH_SA07/code/'+name+'.output.txt'
 wall=re.search(r'ACTUAL_WALL_SECONDS: ([0-9.]+)',(ROOT/output).read_text()).group(1)
 row=dict(statement_id=sid,code=code,output=output,code_sha256=sha(code),output_sha256=sha(output),actual_wall_seconds=wall,root_independent_wall_seconds=rootwall)
 computations.append(row)
 event(sid,CERT,desc+' Actual wall time '+wall+' seconds; source SHA256 '+row['code_sha256']+'; output SHA256 '+row['output_sha256']+'. Root independently inspected and ran the same program through its timing registry, exit0, wall '+rootwall+' seconds. The written arithmetic and geometric proofs retain their stated scope.')

specs=[
 ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf','OPENED, ORIGINAL IMAGES CHECKED','Official GDZ article PDF obtained through its IIIF manifest,2315978bytes. Printedp100 TheoremB, p101 unrestricted rational-prime scope, pp115-117 Cor4.2/table4.3, Lemma4.5/Cor4.6, and exact(4.7.1)-(4.7.2) visually read. These give the nonzero degree6 arithmetic quotient of characterchi^3 without End(J)=Z or an odd-prime premise. The centralizer-finiteness addition onp100 retains End(J)=Z. Root independently inspected original101,115-117.','F.3.20','work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib',USE),
 ('GenFaltings1983',"https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf",'REOPENED, ORIGINAL EXACT LOCATORS CHECKED','Complete original PDF reopened. Section5 Satz3,p360 is semisimplicity; Satz4,p360 is integralEnd; Korollar1,p361 isHom; Korollar2,p361 gives isogeny equivalences. Source numbering explicitly corrected from a shorthand agent message. Root separately reopened original Sätze3-4 and Kor1.','F.3.18; F.3.20','','work/numberfield_references.bib',USE),
 ('AuditNakamura1995','https://www.ms.u-tokyo.ac.jp/journal/pdf/jms020107.pdf','RECHECKED, ORIGINAL ADDITIONAL SCOPE','Introductionpp199-200 and referenceN6p230 identify the higher-genus source and its advertised centralizer application. Equations(4.3)-(4.4),p214, were rechecked for the canonical boundary-fixing representative and graded comparison in degrees at least3. Their use inF3.20 supplies an actual representative in filtration6. No odd-prime restriction from the different Lemma4.10 is imported into this step. Root independently rereadp214.','F.3.20','work/sources_audit_next/Nakamura1995.pdf','work/audit_after04_references.bib',USE),
 ('AuditNakamuraTakaoUeno1994','https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0884-13.pdf','OPENED, PRIMARY SOURCE LEAD ONLY','Complete twelve-page original lecture report opened. Introductionpp112-113 and Theorem2.4/discussionpp115-116 read. No independent theorem imported: the subsequently obtained original1996 article supplies the exact source used inF3.20.','N6 source route','','work/audit_after05_references.bib',BACKGROUND)
]
sources=[]
for key,url,status,loc,deps,path,bib,kind in specs:
 sources.append(dict(source_key=key,url=url,status=status,locator_and_access=loc,dependent_statement_ids=deps,record_file=bib,date=DATE,who=WHO,local_path=path,sha256=sha(path)))
 event('SRC.'+key,kind,status+'. '+loc+' Dependencies: '+deps+'.')

claimpath=ROOT/'work/audit_claims.csv';claims=list(csv.DictReader(claimpath.open()));before=Counter(r['status'] for r in claims)
ids={'I.B05.01','I.B05.02','II.MB15.02'}
addition=' F3.18 now proves the exact rank-one-to-CM quotient with actual Prym maps; F3.19 exhibits an absolutely simple CM surface in an actual cover; F3.20 proves pro-prime recognition for every punctured elliptic target. The arbitrary-cover higher-dimensional CM and full profinite A22 requirements remain OPEN.'
for row in claims:
 if row['assertion_id'] in ids:
  if 'F3.18 now proves' not in row['remaining_obligation_or_scope']:row['remaining_obligation_or_scope']+=addition
  for key in ['proof_or_locator','canonical_dependencies']:
   for sid in ['F.3.18','F.3.19','F.3.20']:
    if sid not in row[key]:row[key]+='; '+sid
  row['check_event_statement_id']=row['assertion_id'];row['check_event_type']=PROOF;row['check_event_ledger']=LEDGER
  event(row['assertion_id'],PROOF,'Evidence/dependencies strengthened; '+row['status']+' status retained.'+addition)
with claimpath.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
mdpath=ROOT/'work/audit_claims.md';md=mdpath.read_text();esc=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
 if row['assertion_id'] in ids:
  line='| '+' | '.join(esc(row[k]) for k in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
  md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda m:line,md,flags=re.M);assert n==1
md=md.replace('Supplemental proofs F.3.1–F.3.17','Supplemental proofs F.3.1–F.3.20')
if '`audit_after05_CHECK_EVENTS.tsv`' not in md:md=md.replace('`audit_after04_CHECK_EVENTS.tsv`.','`audit_after04_CHECK_EVENTS.tsv`, and `audit_after05_CHECK_EVENTS.tsv`.')
mdpath.write_text(md)
with (ROOT/LEDGER).open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
with (ROOT/'work/audit_after05_source_checks.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(sources[0]));w.writeheader();w.writerows(sources)
(ROOT/'work/audit_after05_computation_records.json').write_text(json.dumps(computations,indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len(set(r['note_id'] for r in claims)),status_counts=dict(Counter(r['status'] for r in claims)),addendum_event_count=len(events),source_record_count=len(sources),updated_claim_ids=sorted(ids),changed_statuses=[],root_combined_files_modified=False,canonical_new_result_ids=['F.3.18','F.3.19','F.3.20'])
assert Counter(r['status'] for r in claims)==before
(ROOT/'work/audit_after05_validation.json').write_text(json.dumps(validation,indent=2)+'\n');print(json.dumps(validation,indent=2))
