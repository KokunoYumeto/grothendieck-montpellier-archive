"""Exact CM/Q and all-genus source/proof addendum; parent combined files untouched."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/f6dbb6638732')
DATE = '2026-11-19'
WHO = 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
LEDGER = 'work/audit_after09_CHECK_EVENTS.tsv'
included26 = '{F.3.26}' in (ROOT/'output/RESEARCH_SA07/sections/F_audit.tex').read_text()
included27 = '{F.3.27}' in (ROOT/'output/RESEARCH_SA07/sections/F_audit.tex').read_text()
events = []

def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest() if path else ''

def event(statement, kind, outcome, who=WHO):
    events.append(dict(statement_id=statement, date=DATE, who=who, type=kind, outcome=outcome))

event('F.3.25', 'independent re-proof',
      'Proved the actual CM/Q endomorphism action using G/H embedding labels, the semilinear identity sigma S=S n_sigma, and the exact right-stabilizer proof via an induced-type F-linear Hodge projector. Normality of the left stabilizer and the index sandwich force E/Q Galois, actual action onto Aut(E), and exact kernel G_E. The Tate formula rho(sigma)V_phi=V_(phi composed with a_sigma inverse) supplies the full actual orbit, and Rosati identifies the nondegenerate conjugate pairs.')
event('F.3.25', 'targeted proof check',
      'The Hodge projector gives an analytic torus endomorphism after clearing its integral-lattice denominators. Chow algebraizes its graph. The original Milne1986 Cor20.4(b),pp146-147, applies after finite-type spreading over Qbar and descends the actual endomorphism from C to Qbar. Thus the contradiction uses exactly the stated absolute simplicity; no unproved base-extension equality is substituted.')
event('F.3.25', 'independent re-proof',
      'Root read and approved the complete general CM field proof and genus3 application, including nonsplit local-factor rank exclusion, actual common arithmetic element and six simultaneous conjugate normalizers, rational inner corrections and post-constraint torus projection. Root independently viewed Milne originalpp146-147 and its graph descent. Integration explicitly approved.',
      WHO.replace('agent period_triangle', 'agent root'))
event('F.3.25', 'independent re-proof',
      'Generation independently audited the complete general CM/Q lemma: right stabilizer, semilinear orientation sigma S=S n_sigma, normal left kernel, exact index sandwich and Tate eigenline formula all passed. The explicit Qbar-to-C rigidity/base-change descent sentence was requested and inserted. This review covers the CM lemma, not a claimed separate audit of the genus3 application.',
      WHO.replace('agent period_triangle', 'agent period_generation'))
event('F.3.25', 'targeted proof check',
      'At any candidate degree1 normalizer line, F3.18 and absolute simplicity give the full degree6 CM endomorphism field. The rank-one E_l module and Faltings idempotent formula exclude a line at every nonsplit prime, including ramified primes. At a split prime six actual G_Q conjugations give all paired lines. One common G_L(6) element with nonzero q6 supplies all tangencies. The later full diagonal-torus projector preserves the established constraint space and U6, requires no arithmetic lift, and F3.24 kills its q6. The exact finite-cover boundary sequence and full-normalizer character transfer then invoke Nakamura1994Th2.1.1. Scope: the entire genus3 Jacobian is absolutely simple; proper CM factors in arbitrary detecting covers retain their exact unresolved map.')
if included27:
    event('F.3.27','independent re-proof',
          'Extended the actual curve theorem to everyg>=3 using the whole absolutely simple Jacobian. Rank-one Galois projector plus F3.18 gives the full CM field of degree2g; F3.25 gives its actual Q-model endomorphism action and2g paired orbit lines. Equal local factor degrees exclude nonsplit primes. Actual conjugate normalizers on one original curve surject onto a common G_L, and one actual degree6 element has nonzero q6. The rational full-log conjugator corrections give all2g tangencies, contradicted by F3.26. The original-curve first Magnus weight and the actual finite-cover boundary kernel transfer the exact cyclotomic character to the full normalizer and invoke Nakamura1994Th2.1.1.')
    event('F.3.27','independent re-proof',
          'Root read the complete final text and approved all prime/local idempotent arguments, original-curve first Magnus comparison,2g actual conjugation maps, common arithmetic lift, and the exact QCM.4-5 references to the included F3.25 correction. Root freshly viewed Nakamura originalpp115-117 and verified the degree6 quotient has dimension1 and is nonzero for every hyperbolic(g,n),n>=1, with finite-base fibre surjection. No additional mathematical computation was needed; F3.26 supplies the reused finite universal calculation.',
          WHO.replace('agent period_triangle','agent root'))

specs = [
 ('AuditMilne1986AV', 'https://www.jmilne.org/math/articles/1986b.pdf',
  'OPENED ORIGINAL CHAPTER; EXACT PAGES VISUALLY READ',
  'Complete48-page original chapter,3833583bytes. Printedpp146-147: Prop20.3 and Cor20.4(a)-(b) with its graph-descent proof visually read. Regular-extension hypothesis used after finite-type spreading over Qbar. The non-www URL initially returned406 locally; www with ordinary user-agent succeeded. Root independently viewed both original pages.',
  'work/sources_audit_next/Milne1986_Abelian_Varieties_original.pdf', 'work/audit_after09_references.bib', 'used and rechecked in this run', 'F.3.25'),
 ('AuditGoodman2026', 'https://link.springer.com/article/10.1007/s40993-026-00722-5',
  'OPENED FINAL PUBLISHER ARTICLE HTML; LITERATURE COMPARISON',
  'Lemma2.5 and proof, plus reference17, read in the final publisher article published23March2026. It assumes the CM field E/Q already Galois and states the reflex-field endomorphism formula. The source points to Shimura1998Prop28p62/Prop30p65. This is a consulted comparison; F3.25 supplies its own general Q-model proof and makes no novelty claim. PMC mirror was blocked by browser-check page; publisher article succeeded.',
  '', 'work/audit_after09_references.bib', 'carried as background without fault found', 'F.3.25 source comparison'),
 ('AuditShimura1998Gate', 'https://link.springer.com/article/10.1007/s40993-026-00722-5',
  'EXACT ORIGINAL LEAD IDENTIFIED; BOOK PASSAGE NOT OBTAINED',
  'Bibliographic metadata and exactProp30p65/Prop28p62 locators identified in Goodman2026Lemma2.5/reference17. The original book passage was not obtained or read. No original theorem statement imported; the direct proof of F3.25 is independent of this bibliographic gate.',
  '', 'work/audit_after09_references.bib', 'carried as background without fault found', 'literature provenance; no theorem dependency'),
 ('GenMilneCM2020', 'https://www.jmilne.org/math/CourseNotes/CM.pdf',
  'REOPENED AUTHOR NOTES FROM LOCAL SOURCE; BACKGROUND',
  'Version0.10,14July2020. Proposition2.4p22 on actual Riemann-pair maps and Proposition3.13p30 on primitive CM types/simple abelian varieties read from the previously obtained complete author notes. The F-linear projector in F3.25 is written explicitly rather than importing a stronger categorical statement.',
  'work/sources_generation/milne_cm2020.pdf', 'work/numberfield_references.bib', 'carried as background without fault found', 'F.3.25 background'),
 ('GenFaltings1983', "https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf",
  'OPENED ORIGINAL SOURCE REUSED WITH EXACT LOCATORS',
  'Original Section5,Satz3p360 semisimplicity and Satz4p360 endomorphism equality, as previously visually checked, used through F3.18. After all geometric endomorphisms are defined these identify any rational Galois-line projector with an idempotent in the full geometric endomorphism algebra tensored with Q_l. The local factor rank is computed explicitly in F3.25.',
  '', 'work/generation_references.bib', 'used and rechecked in this run', 'F.3.25'),
 ('AuditNakamura1996', 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf',
  'OPENED ORIGINAL UNIVERSAL QUOTIENT MAP REUSED',
  'Originalpp115-117, degree6 table,Lem4.5,Cor4.6,(4.7.1)-(4.7.2): actual finite-base-invariant arithmetic image, nonzero degree6 quotient, and multiplier-cubed action. All six tangency conditions in F3.25 use one actual element of the common finite-base arithmetic kernel before the later purely linear torus projection.',
  'work/sources_audit_next/Nakamura1996_Coupling_original.pdf', 'work/audit_after05_references.bib', 'used and rechecked in this run', 'F.3.25'),
]
if included26:
    specs += [
      ('AuditHain1997Torelli', 'https://nsalter.science.nd.edu/teaching/torelli/hain.pdf',
       'REOPENED EXACT ALL-GENUS SCOPE IN ORIGINAL ARTICLE',
       'Th3.4p605 explicitly holds for everyg>=3; Th4.10p611 excludes onlyg=2 and identifies weight with lower central series; Remark4.11p613 and Section14.4p643 give the strict boundary-fixed action. The F3.24 exact finite-level geometric-normalizer bridge therefore applies in everyg>=3. No discrete-filtration-kernel density assertion used.',
       'work/sources_audit_next/Hain1997_Torelli_original.pdf', 'work/audit_after08_references.bib', 'used and rechecked in this run', 'F.3.26'),
      ('AuditEnomotoSatoh2014', 'https://msp.org/agt/2014/14-2/agt-v14-n2-p01-s.pdf',
       'REOPENED EXACT STABLE-RANGE TRACE MAP',
       'Th3.5/Prop3.6p640 and Section7.1p656 used with their genus>=k+2 premise. For k7 and3<=g<9 the actual surface inclusion into genus9 and cyclic projection left inverse transfer the stated vanishing; g>=9 is already in range. All cyclic maps and outside-handle terms are computed explicitly in F3.26.',
       'work/sources_audit_next/EnomotoSatoh2014_original.pdf', 'work/audit_after08_references.bib', 'used and rechecked in this run', 'F.3.26')]
if included27:
    specs.append(
      ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf',
       'ORIGINAL ALL-HYPERBOLIC SCOPE FRESHLY VERIFIED',
       'Printedpp115-117, local image filespage18-page20: original Lem4.5,Cor4.6,rank table,(4.7.1)-(4.7.2) explicitly give the actual GSp-equivariant universal quotient for every hyperbolic(g,n),n>=1, with nonzero dimension1 degree6 chi^3 quotient and finite-base fibre surjection. Root and generation each independently reopened and read the exact original images before F3.27 integration. The additional endomorphism-ring hypothesis of TheoremB is not substituted for these universal quotient maps.',
       'work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib','used and rechecked in this run','F.3.26; F.3.27'))
sources=[]
for key,url,status,detail,path,bib,kind,dependencies in specs:
    sources.append(dict(source_key=key,url=url,status=status,locator_and_access=detail,
                        dependent_statement_ids=dependencies,record_file=bib,date=DATE,
                        who=WHO,local_path=path,sha256=sha(path)))
    event('SRC.'+key,kind,status+'. '+detail)

computations=[]
if included26:
    code='output/RESEARCH_SA07/code/check_genus_four_tangent_block.py'
    output='output/RESEARCH_SA07/code/check_genus_four_tangent_block.output.txt'
    witness='output/RESEARCH_SA07/code/check_genus_four_tangent_block.witness.json'
    wall=re.search(r'ACTUAL_WALL_SECONDS ([0-9.]+)',(ROOT/output).read_text()).group(1)
    computations.append(dict(statement_id='F.3.26',code=code,output=output,witness=witness,
                             code_sha256=sha(code),output_sha256=sha(output),witness_sha256=sha(witness),
                             actual_wall_seconds=wall,independent_root_wall_seconds='1.597119087',
                             independent_root_exit_code=0,registry_runtime_seconds='1.348439',registry_exit_code=0,
                             registry_output='code/run_records/check_genus_four_tangent_block.out',
                             input='Balanced specialness block n=(1,1,1,1),eight generators,5040 Lyndon coefficient rows,960 conjugator columns; exact formal-z kernels and S4 orbit sums.'))
    event('F.3.26','computation or formal certificate',
          'Full four-handle block5040x960 has rational rank958: an ordered958-minor has determinant1 modulo101; two explicit exact integer kernel vectors have independence minor-1. Each formal-z kernel generator has exact zero S4 orbit sum. NumPy int16 elimination is exact: all products are at most10000 in absolute value, within range. Actual wall seconds '+wall+'; root independent exit0 wall1.597119087seconds. Code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'; witness SHA256 '+sha(witness)+'. No arithmetic map is inferred from the program.')
    event('F.3.26','independent re-proof',
          'Complete balanced tangent space has support at most four handles and basis P_pairs,T_repeated-triples,Q_quadruples. The exact ES restriction to a three-handle symplectic span has outside contribution cyc(p delta A_i+p delta B_i), zero because each term is a degree7 Lie polynomial. The genus3 trace kernel kills every pair coefficient and forces zero total triple coefficient. Handle permutations kill triple differences and the exact S4 orbit sums kill all quadruple invariant functionals. Complete reducibility extends q6 from the actual universal submodule; the post-constraint torus projector proves the full unbalanced tangency statement for everyg>=3. Proper symplectic CM-summand q6 compatibility remains a separate exact map requirement.')
    event('F.3.26','independent re-proof',
          'Root read the whole all-genus proof and checked all projection contraction signs, support completion, coefficient restrictions, S4 averages and invariant extension/projector. Root read the full finite code and independently reran it,exit0,1.597119087seconds, with the same witness SHA256. The direct inner-bracket cancellation proof was included on approval.',
          WHO.replace('agent period_triangle','agent root'))
    event('F.3.26','independent re-proof',
          'Generation independently reopened Hain3.4(allg>=3),4.10(g!=2),4.11 and Nakamura originalpp115-117, then passed the finite-level arithmetic normalization, universal quotient domain, AG.8 signs and outside-letter removal, and invariant extension. Supplied a separate proof of S4 averaging: each fixed output component sums S3 permutations of a multilinear degree3 Lie word, with cancellation by exchanging the arguments of its inner bracket. This independent proof is now included.',
          WHO.replace('agent period_triangle','agent period_generation'))

claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
before=Counter(row['status'] for row in claims)
changed={'I.B05.01','I.B05.02','II.MB15.02'}
addition=(' F3.25 proves that an absolutely simple CM variety over Q has a Galois full endomorphism field and the actual G_Q orbit of one split eigenline is the whole paired basis. It also gives all-prime cusp recognition for once-punctured genus3 Q-curves with a whole absolutely simple Jacobian. A proper geometric CM factor in an arbitrary detecting-cover Jacobian is not substituted for that whole module.')
if included26:
    addition+=(' F3.26 proves full-basis-tangency q6 vanishing in every genus>=3 by exact support<=4 matrices and the three-handle trace projection. The equality relating q6 to restriction onto a proper symplectic CM summand remains unproved.')
if included27:
    addition+=(' F3.27 applies these exact maps to once-punctured Q-curves with a whole absolutely simple Jacobian of any genus>=3, at every prime and after every finite arithmetic base change. General detecting-cover Jacobians may be reducible, so this does not close the original subgroup gate.')
for row in claims:
    if row['assertion_id'] in changed:
        if ' F3.25 proves' in row['remaining_obligation_or_scope']:
            row['remaining_obligation_or_scope']=row['remaining_obligation_or_scope'].split(' F3.25 proves')[0]
        row['remaining_obligation_or_scope']+=addition
        for key in ['proof_or_locator','canonical_dependencies']:
            if 'F.3.25' not in row[key]:row[key]+='; F.3.25'
            if included26 and 'F.3.26' not in row[key]:row[key]+='; F.3.26'
            if included27 and 'F.3.27' not in row[key]:row[key]+='; F.3.27'
        row['check_event_statement_id']=row['assertion_id']
        row['check_event_type']='targeted proof check'
        row['check_event_ledger']=LEDGER
        event(row['assertion_id'],'targeted proof check','Status '+row['status']+' retained.'+addition)
with (ROOT/'work/audit_claims.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(claims[0]));writer.writeheader();writer.writerows(claims)
mdpath=ROOT/'work/audit_claims.md';md=mdpath.read_text()
escape=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
    if row['assertion_id'] in changed:
        line='| '+' | '.join(escape(row[key]) for key in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
        md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda _:line,md,flags=re.M);assert n==1
md=re.sub('Supplemental proofs F.3.1–F.3.[0-9]+','Supplemental proofs F.3.1–F.3.'+('27' if included27 else '26' if included26 else '25'),md)
if '`audit_after09_CHECK_EVENTS.tsv`' not in md:
    md=md.replace('`audit_after08_CHECK_EVENTS.tsv`.','`audit_after08_CHECK_EVENTS.tsv`, and `audit_after09_CHECK_EVENTS.tsv`.')
mdpath.write_text(md)
for path,rows,fields,delimiter in [
    (LEDGER,events,['statement_id','date','who','type','outcome'],'\t'),
    ('work/audit_after09_source_checks.csv',sources,list(sources[0]),',')]:
    with (ROOT/path).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);writer.writeheader();writer.writerows(rows)
(ROOT/'work/audit_after09_computation_records.json').write_text(json.dumps(computations,indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),
                status_counts=dict(Counter(r['status'] for r in claims)),addendum_event_count=len(events),
                source_record_count=len(sources),updated_claim_ids=sorted(changed),changed_statuses=[],
                root_combined_files_modified=False,canonical_new_result_ids=['F.3.25']+(['F.3.26'] if included26 else [])+(['F.3.27'] if included27 else []))
assert before==Counter(row['status'] for row in claims)
(ROOT/'work/audit_after09_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
