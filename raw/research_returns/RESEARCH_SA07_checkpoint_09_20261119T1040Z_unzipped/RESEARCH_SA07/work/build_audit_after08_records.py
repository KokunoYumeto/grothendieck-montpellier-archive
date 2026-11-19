"""F.3.23 and the audited-in-progress genus3 source/certificate addendum."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re
ROOT=Path('/workspace/scratch/f6dbb6638732')
DATE='2026-11-19'
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
G3_ID='F.3.24'
LEDGER='work/audit_after08_CHECK_EVENTS.tsv'
events=[]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest() if p else ''
def event(s,t,o,who=WHO):events.append(dict(statement_id=s,date=DATE,who=who,type=t,outcome=o))
event('F.3.23','independent re-proof',
 'Constructed the actual arithmetic-normal-core detecting cover. Topological finite generation gives finitely many arithmetic conjugates of the finite-index geometric subgroup H. Their intersection S is open and normal in the full arithmetic group. An actual rational-point section yields the covering subgroup S semidirect G_Q and a rational point above the chosen basepoint. Inclusion sends [u^(ell^r)] to ell^r[u], preserving the nonzero rational homology and its proper image. Intersecting the normalizer with the arithmetic covering subgroup preserves an open arithmetic image. All finite G_Q-orbit lines admit lifts of one common G_L after an exact finite normal-core intersection.')
event('F.3.23','targeted proof check',
 'The tangential descent gives a Q-rational cusp and a once-punctured Q-model. With D_O=I_O semidirect s_O(G_Q) and Pi_Y=S semidirect s_O(G_Q), the chosen cusp decomposition group is exactly (S intersect I_O) semidirect s_O(G_Q), so its residue arithmetic quotient is G_Q and its residue field is Q. The actual map Y to its smooth compactification minus this one cusp preserves proper homology, nontrivial pro-ell subgroup image and open arithmetic normalizer. The same once-punctured Q-curve now carries all G_Q-conjugate detected lines. No assertion that those lines span the entire CM module is made.')
event('F.3.23','independent re-proof',
 'Root independently checked and approved both the rational-open-point construction and the tangential strengthening, including the exact decomposition intersection, residue field, actual filling map, proper homology and normalizer images. F3.23 integration explicitly authorized.',
 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent root')
event(G3_ID,'independent re-proof',
 'The integrated proof establishes the exact genus3 universal-quotient target q6(T intersect U6)=0 for the complete full-diagonal-torus chi^3 space tangent to all six symplectic basis lines. New three-handle specialness block gives the complete six-dimensional tangent space. ES7 brackets with all20 degree1 geometric derivations cut it to the differences T2-T1 and T3-T1. Handle permutations exchange these Ti, so every Sp-invariant functional vanishes there. Complete reducibility extends the invariant quotient from the universal submodule. No arbitrary-cover CM-character or spanning assertion is substituted. Root final proof/source audit PASSED and independent certificate rerun exited0 in2.468692seconds; integration explicitly approved.')
event(G3_ID,'targeted proof check',
 'Typed the completed geometric map through Zariski closure at each finite nilpotent level. Polynomial continuity places actual profinite geometric monodromy in the Q_l Zariski closure of the discrete image. Hain original Th3.4p605, Lem4.5/Cor4.8/Th4.10pp610-611, Remark4.11p613 and Section14.4p643 give the strict weight-compatible punctured action and its degree1-generated graded image. Enomoto-Satoh Th3.5/Prop3.6p640 identify this image with rational Johnson. The tangential arithmetic action normalizes the actual geometric algebraic image; removing the full-log boundary twist stays inside it. Leading commutators therefore lie in its strict degree7 Johnson image. No density of discrete filtration kernels is asserted.')
event(G3_ID,'independent re-proof',
 'Generation agent independently read the exact original Hain passages and checked the completed geometric bridge, strictness, boundary correction and leading commutator equation. Audit PASSED with the explicit Th4.10/Remark4.11 references added. The genus3-to-genus9 stabilization and cyclic-coinvariant projection left inverse also passed.',
 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_generation')
code='output/RESEARCH_SA07/code/check_genus_three_normalizer_trace.py'
output='output/RESEARCH_SA07/code/check_genus_three_normalizer_trace.output.txt'
wall=re.search(r'ACTUAL_WALL_SECONDS: ([0-9.]+)',(ROOT/output).read_text()).group(1)
computation=dict(statement_id=G3_ID,code=code,output=output,code_sha256=sha(code),output_sha256=sha(output),actual_wall_seconds=wall,
 independent_root_wall_seconds='2.468692',independent_root_exit_code=0,input='Six ordered symplectic generators; balanced degree6 conjugators; new1260x360 specialness block;20 degree1 wedge derivations; K12 contraction and cyclic words; exact integer kernel and minors modulo101.')
event(G3_ID,'computation or formal certificate',
 'New complete certificate passed. Three-handle block1260x360 has rational rank359: nonzero359-minor modulo101 and an explicit exact integer kernel. Together with the already certified lower-support blocks this gives tangent dimension6. The ES7 bracket matrix has2208 nonzero rows and6 columns; an explicit4x4 integer minor has determinant1, and exact equality of its last three full columns gives kernel span(T2-T1,T3-T1). A concrete substitution killing omega detects nonzero P12 on the proper genus3 quotient, so the additional normalizer equation is substantive. Actual wall seconds '+wall+'; code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'. Arithmetic image and q6 maps are proved in the work text and are not program inferences.')

specs=[
 ('AuditHain1997Torelli','https://nsalter.science.nd.edu/teaching/torelli/hain.pdf','OPENED FINAL JOURNAL ARTICLE; AMS DIRECT URL FAILED',
  'Full55-page final JAMS article obtained from an academic mirror. Relative-completion universal property pp603-604; Th3.4p605; Lem4.5, Cor4.8, Th4.10pp610-611; Remark4.11p613; Sections14.3-14.4pp641-643 read. The strict boundary-fixed punctured action onp643 identifies the graded image. Genus>=3, central Malcev kernel and action-versus-lower-central filtration are retained through the exact image map.',
  'work/sources_audit_next/Hain1997_Torelli_original.pdf','work/audit_after08_references.bib','used and rechecked in this run'),
 ('AuditEnomotoSatoh2014','https://msp.org/agt/2014/14-2/agt-v14-n2-p01-s.pdf','OPENED FINAL PUBLISHER PDF',
  'Full43-page final article obtained. Theorem3.4p638, Theorem3.5 and Proposition3.6p640, exact contraction/cyclic diagram in Section7.1p656 read. Its stated genus>=k+2 scope is retained; for k7 the work proof uses an actual boundary-fixed genus3-to-genus9 surface inclusion and a cyclic-tensor projection left inverse to obtain vanishing in genus3.',
  'work/sources_audit_next/EnomotoSatoh2014_original.pdf','work/audit_after08_references.bib','used and rechecked in this run'),
 ('AuditMoritaSakasaiSuzuki2015v2','https://arxiv.org/pdf/1404.3351','REOPENED EXACT CONTRACTION AND NORMALIZER MAPS',
  'Original v2,19July2015. Section2p7 defines the signed chord contractions; Prop7.2pp26-27 and Th7.5pp28-30 describe the invariant coordinates and geometric normalizer; Section8pp34-35 gives the exact K12-to-cyclic ES formula. Theorem4.2p18, citing Labute, was also read as a background source lead. No genus2 substitution into the normalized stable basis is made. The genus3 trace certificate computes its own exact matrices.',
  'work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf','work/audit_after06_references.bib','used and rechecked in this run'),
 ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf','OPENED ORIGINAL QUOTIENT MAP REUSED',
  'Printedpp115-117: degree6 nonzero quotient, Lemma4.5, Corollary4.6, equations4.7.1-4.7.2 and similitude-cubed equivariance. The work genus3 argument uses the same actual universal quotient on its universal-image submodule; arbitrary Lie vectors are not assigned arithmetic q6 values.',
  'work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib','used and rechecked in this run'),
 ('AuditLabute1967','https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0004/LOG_0015.pdf','OPENED ORIGINAL ARTICLE; BACKGROUND ONLY',
  'Official GDZ article manifest supplied the1805726-byte original. Visually read printedpp143-145: Theorem3, Proposition1, primitive-relator definition, Theorem4 and Demushkin example. No theorem is imported. F3.22 uses its own canonical surjection from the surface-relation quotient and does not depend on a stronger graded-isomorphism assertion.',
  'work/sources_audit_next/Labute1967_original.pdf','work/audit_after08_references.bib','carried as background without fault found'),
 ('AuditLabute1970Gate','https://www.sciencedirect.com/science/article/pii/0021869370901304','EXACT ORIGINAL ATTEMPTED; NOT OBTAINED',
  'Publisher original URL returned403 through the web tool. Metadata only checked: J.Algebra14(1970)16-23, DOI10.1016/0021-8693(70)90130-4. No original theorem or page claimed read. Later MSS Theorem4.2p18 and DPW references are explicit substitutes only; no theorem imported and no manuscript dependency.',
  '','work/audit_after08_references.bib','carried as background without fault found'),
 ('AuditLabute2015Author','https://www.math.mcgill.ca/labute/papers/RTF1-rel.pdf','OPENED COMPLETE AUTHOR PREPRINT; BACKGROUND ONLY',
  'Complete two-page author preprint dated8March2015 opened. Theorem1p1 and Theorems3-4p2 read as source leads. Weighted-filtration hypotheses retained; no weighted-to-ordinary filtration identification or manuscript theorem imported.',
  '','work/audit_after08_references.bib','carried as background without fault found')
]
sources=[]
for key,url,status,detail,local,bib,kind in specs:
    dep=G3_ID if not key.startswith('AuditLabute') else 'surface-source provenance; no theorem dependency'
    sources.append(dict(source_key=key,url=url,status=status,locator_and_access=detail,dependent_statement_ids=dep,
                        record_file=bib,date=DATE,who=WHO,local_path=local,sha256=sha(local)))
    event('SRC.'+key,kind,status+'. '+detail)

claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
before=Counter(r['status'] for r in claims)
ids={'I.B05.01','I.B05.02','II.MB15.02'}
addition=(' F3.23 constructs an actual arithmetic-normal-core detector with a rational cusp, '
          'then an actual once-punctured Q-model preserving the nonzero proper homology and open normalizer. '
          'The full arithmetic orbit need not yet be identified with an entire CM symplectic basis; '
          'the universal quotient on that actual remaining constraint space is still required.')
for row in claims:
    if row['assertion_id'] in ids:
        if 'F3.23 constructs' not in row['remaining_obligation_or_scope']:row['remaining_obligation_or_scope']+=addition
        for k in ['proof_or_locator','canonical_dependencies']:
            if 'F.3.23' not in row[k]:row[k]+='; F.3.23'
            if 'F.3.24' not in row[k]:row[k]+='; F.3.24'
        row['check_event_statement_id']=row['assertion_id'];row['check_event_type']='targeted proof check';row['check_event_ledger']=LEDGER
        event(row['assertion_id'],'targeted proof check','Added the exact normal-core and rational-cusp maps; '+row['status']+' status retained.'+addition)
with (ROOT/'work/audit_claims.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
mdp=ROOT/'work/audit_claims.md';md=mdp.read_text();esc=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
    if row['assertion_id'] in ids:
        line='| '+' | '.join(esc(row[k]) for k in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
        md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda m:line,md,flags=re.M);assert n==1
md=md.replace('Supplemental proofs F.3.1–F.3.23','Supplemental proofs F.3.1–F.3.24')
if '`audit_after08_CHECK_EVENTS.tsv`' not in md:md=md.replace('`audit_after07_CHECK_EVENTS.tsv`.','`audit_after07_CHECK_EVENTS.tsv`, and `audit_after08_CHECK_EVENTS.tsv`.')
mdp.write_text(md)
for path,rows,fields,delimiter in [(LEDGER,events,['statement_id','date','who','type','outcome'],'\t'),
 ('work/audit_after08_source_checks.csv',sources,list(sources[0]),',')]:
    with (ROOT/path).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter);w.writeheader();w.writerows(rows)
(ROOT/'work/audit_after08_computation_records.json').write_text(json.dumps([computation],indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),status_counts=dict(Counter(r['status'] for r in claims)),
                addendum_event_count=len(events),source_record_count=len(sources),updated_claim_ids=sorted(ids),changed_statuses=[],
                root_combined_files_modified=False,canonical_new_result_ids=['F.3.23','F.3.24'],work_result_ids=[])
assert Counter(r['status'] for r in claims)==before
(ROOT/'work/audit_after08_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
