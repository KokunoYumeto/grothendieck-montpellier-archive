"""F3.28 exact partial-summand source/proof/certificate records."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/f6dbb6638732')
DATE='2026-11-19'
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
LEDGER='work/audit_after10_CHECK_EVENTS.tsv'
events=[]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest() if p else ''
def event(s,t,o,who=WHO):events.append(dict(statement_id=s,date=DATE,who=who,type=t,outcome=o))

event('F.3.28','independent re-proof',
      'Proved q6 vanishing for actual universal degree6 classes in genus3 tangent only to four specified basis lines spanning two symplectic pairs. Complementary handle values remain unrestricted. All mixed ES7 equations are retained. Two equivariant extensions turn q6 into an invariant tensor functional; MSS Prop2.1 gives its complete105-contraction expression. Exact contraction images of the entire partial-tangent trace kernel lie in those of two literal degree6 Johnson brackets, on which the actual quotient vanishes by Nakamura(4.7.1). No restriction morphism to an arithmetic smaller-curve quotient is asserted.')
event('F.3.28','targeted proof check',
      'The proof fixes a nonzero basis of the verified dimension1 Q6 before extending the invariant scalar-valued map. The geometric degree6 Johnson image is contained in the actual universal image and killed by its quotient, as in the original exact sequence. Symplectic complete reducibility then extends first to the whole special-derivation space and next to V tensor8. Unsigned contraction coordinates differ from MSS signed coordinates by invertible row signs. All computations are rational, so the nonzero determinant-10752 is invertible in Q_l at every prime, without any integral lifting assertion.')
event('F.3.28','independent re-proof',
      'Root read the full proof and final certificate, independently verified the invariant-extension route and original MSS Prop2.1p8, and reran the final program:exit0,6.337165875seconds. Exact31-dimensional partial space,16-dimensional trace kernel, determinant-10752, and all105 coordinate identities passed. Integration approved after the independent elliptic audit.',
      WHO.replace('agent period_triangle','agent root'))
event('F.3.28','independent re-proof',
      'Elliptic independently audited the proof and original MSS invariant-contraction locator, then reran the final certificate:exit0,8.859784069seconds. Exact dimensions, nonzero contraction minor and every105-coordinate geometric-image identity passed. This independent review was reported to period_triangle by root before integration.',
      WHO.replace('agent period_triangle','agent elliptic_splitting'))

code='output/RESEARCH_SA07/code/check_genus_three_two_pair_partial.py'
output='output/RESEARCH_SA07/code/check_genus_three_two_pair_partial.output.txt'
wall=re.search(r'ACTUAL_WALL_SECONDS ([0-9.]+)',(ROOT/output).read_text()).group(1)
record=dict(statement_id='F.3.28',code=code,output=output,code_sha256=sha(code),output_sha256=sha(output),
            actual_wall_seconds=wall,independent_root_wall_seconds='6.337165875',independent_elliptic_wall_seconds='8.859784069',
            independent_exit_codes=[0,0],input='Six ordered symplectic generators; tangency on a,b,c,d only; all15 balanced specialness blocks; all20 degree1 Johnson generators; all105 complete symplectic contractions; two specified sixfold Johnson brackets.')
event('F.3.28','computation or formal certificate',
      'Every balanced specialness block is constructed completely. Modular101 elimination gives rank lower bounds; independent integer kernel lifts are checked against each original integer specialness matrix, proving dimension31 over Q. The3920x31 ES7 matrix has rank15 by the same lower/upper-bound method, with16 exact independent integer kernel vectors. All105 contraction coordinates of each vector satisfy an explicit cleared-denominator identity against the two nested Johnson brackets cdf,cef,aef,def,bef,cde and bce,adf,adf,abd,bce,abc. Their minor [[-104,-288],[32,192]] has determinant-10752. NumPy integer bounds are asserted before potentially overflowing products. Actual wall '+wall+'seconds; code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'.')

specs=[
 ('AuditMoritaSakasaiSuzuki2015v2','https://arxiv.org/pdf/1404.3351',
  'REOPENED ORIGINAL V2; ALL-GENUS CONTRACTION SPAN VERIFIED',
  'Original v2,19July2015. Section2p7 defines dual signed chord contractions. Proposition2.1p8 explicitly states surjectivity for every genus and bijectivity only for g>=k; the proof invokes symplectic invariant theory. Thus all105 contractions span the invariant functionals on V tensor8 in genus3 despite the genus3 relations. Root and elliptic independently checked this exact original locator. Sections5.6p21 and7.5pp28-30 were also reread as work-only filling-kernel leads; they are not substituted for the geometric-image proof of F3.28.',
  'work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf','work/audit_after06_references.bib'),
 ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf',
  'ORIGINAL EXACT GEOMETRIC KERNEL VISUALLY RECHECKED',
  'Printedp117, equation4.7.1 is the exact GSp-equivariant geometric-to-universal quotient sequence; equation4.7.2 gives the fibre image. The final paragraph explicitly includes the topological Johnson image in the geometric image. Printedpp115-116 also freshly viewed: the degree6 rank sandwich has both endpoints1, and Lem4.5/finite-base invariance give the actual nonzero quotient. These identify J6 inside U6 and prove q6(J6)=0; they do not assign q6 to arbitrary Lie polynomials.',
  'work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib')]
sources=[]
for key,url,status,detail,path,bib in specs:
    sources.append(dict(source_key=key,url=url,status=status,locator_and_access=detail,dependent_statement_ids='F.3.28',
                        record_file=bib,date=DATE,who=WHO,local_path=path,sha256=sha(path)))
    event('SRC.'+key,'used and rechecked in this run',status+'. '+detail)

claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
before=Counter(r['status'] for r in claims)
ids={'I.B05.01','I.B05.02','II.MB15.02'}
addition=(' F3.28 proves q6 vanishing in genus3 for four actual basis-line tangencies spanning a proper symplectic four-dimensional summand, retaining the complementary handle and all mixed Johnson equations. Exact invariant contraction images lie in two actual geometric degree6 bracket images. It does not identify arbitrary detected CM lines with that paired summand, nor prove an all-genus proper-summand statement.')
for row in claims:
    if row['assertion_id'] in ids:
        if ' F3.28 proves' not in row['remaining_obligation_or_scope']:row['remaining_obligation_or_scope']+=addition
        for k in ['proof_or_locator','canonical_dependencies']:
            if 'F.3.28' not in row[k]:row[k]+='; F.3.28'
        row['check_event_statement_id']=row['assertion_id'];row['check_event_type']='targeted proof check';row['check_event_ledger']=LEDGER
        event(row['assertion_id'],'targeted proof check','Status '+row['status']+' retained.'+addition)
with (ROOT/'work/audit_claims.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
mdp=ROOT/'work/audit_claims.md';md=mdp.read_text();esc=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
    if row['assertion_id'] in ids:
        line='| '+' | '.join(esc(row[k]) for k in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
        md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda _:line,md,flags=re.M);assert n==1
md=md.replace('Supplemental proofs F.3.1–F.3.27','Supplemental proofs F.3.1–F.3.28')
if '`audit_after10_CHECK_EVENTS.tsv`' not in md:md=md.replace('`audit_after09_CHECK_EVENTS.tsv`.','`audit_after09_CHECK_EVENTS.tsv`, and `audit_after10_CHECK_EVENTS.tsv`.')
mdp.write_text(md)
for path,rows,fields,delimiter in [(LEDGER,events,['statement_id','date','who','type','outcome'],'\t'),
 ('work/audit_after10_source_checks.csv',sources,list(sources[0]),',')]:
    with (ROOT/path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(rows)
(ROOT/'work/audit_after10_computation_records.json').write_text(json.dumps([record],indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),status_counts=dict(Counter(r['status'] for r in claims)),
                addendum_event_count=len(events),source_record_count=len(sources),updated_claim_ids=sorted(ids),changed_statuses=[],
                root_combined_files_modified=False,canonical_new_result_ids=['F.3.28'],new_bibliography_keys=[])
assert before==Counter(r['status'] for r in claims)
(ROOT/'work/audit_after10_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
