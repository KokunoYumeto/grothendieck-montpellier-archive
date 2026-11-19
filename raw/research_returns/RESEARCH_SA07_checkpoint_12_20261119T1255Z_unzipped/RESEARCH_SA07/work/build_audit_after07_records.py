"""Canonical F.3.22 records; preserve historical ledgers and root combined files."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/f6dbb6638732')
DATE = '2026-11-19'
WHO = 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
LEDGER = 'work/audit_after07_CHECK_EVENTS.tsv'
events = []

def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest() if path else ''

def event(statement, kind, outcome, who=WHO):
    events.append(dict(statement_id=statement, date=DATE, who=who, type=kind, outcome=outcome))

event('F.3.22', 'independent re-proof',
      'Proved actual cusp recognition on X5:y^2=1-x^5 minus infinity for every prime and every finite number-field extension. F3.21 supplies the nonsplit primes. At split primes, four actual G_Q-conjugate normalizer subgroups supply simultaneous tangency constraints for one actual arithmetic element. The four Hodge-Tate exponent sets prove exact CM-character independence; the closed actual arithmetic image admits a denominator-cleared character projection. The complete special degree6 tangent space is one-dimensional and its spanning derivation vanishes after filling the puncture. The actual moduli forgetful map and Takao Theorem3.5 identify the relevant universal arithmetic quotient, producing the contradiction. The exact finite-cover boundary argument then transfers the cyclotomic character to the full normalizer and Nakamura1994 Theorem2.1.1 gives actual inertia. The arbitrary-cover and full profinite LM6 A22 assertion remains OPEN.')
event('F.3.22', 'targeted proof check',
      'Checked the arithmetic normal core: gamma_1 is the identity; one finite Galois field L has G_L inside G_Q(zeta5) and all four conjugate arithmetic images. Each restricted normalizer still surjects onto this SAME G_L. The action of gamma_b sends V_a to V_(a b^-1). Four independent lifts of the SAME sigma act with exponent1 by their nonzero degree-one terms; they give four simultaneous inner-tangency equations. No Galois section is assumed.')
event('F.3.22', 'targeted proof check',
      'Checked the filtered boundary representative and nonprimitive conjugators. Remove a degree2 multiple of omega using the full logarithm of the boundary word, then the free-Lie centralizer forces the degree3 through degree5 terms to vanish. The unique special degree6 representative is GSp-equivariant. In each normalizer conjugacy equation, remove the scalar degree1 term using a rational power of the full logarithm of the actual subgroup generator; the original arithmetic element remains actual. The compact image is a closed Z_l-module; Baire separates finitely many infinite-image character ratios, and clearing the spectral-polynomial denominators keeps the projected element in that actual image.')
event('F.3.22', 'targeted proof check',
      'Checked the exact map needed for the surface quotient. Filling the puncture kills the actual boundary word with initial term omega; degree-one generation gives a canonical SURJECTION L(V)/(omega) to the graded proper pro-ell fundamental group. No injectivity theorem is required or asserted. Since C=[z1,omega], every value of the spanning derivation lies in the ideal (omega). The actual forgetful moduli morphism commutes with the arithmetic field quotient maps. Takao Theorem3.5 identifies both field levels, so q6 kills precisely the intersection of the tangent line with the universal image, which contains the actual projected element.')
event('F.3.22', 'independent re-proof',
      'Parent independently read the complete proof, rechecked original Nakamura pp115-117 and Takao Theorem3.5, inspected and reran the full coefficient certificate, and approved the canonical-surjection clarification. Complete proof/source/code audit PASSED. This records the explicit audit message; the parent also maintains its own independent ledger.',
      'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent root')
event('F.3.22', 'independent re-proof',
      'Independent Steps3-5 audit PASSED: actual conjugate normalizer lifts and common normal core; full-log boundary correction and GSp-equivariant uniqueness; same sigma across four lifts; nonprimitive rational conjugator removal; compact actual Z_l image, Baire separation and denominator-cleared projection. Original Nakamura printed pp115-117 were visually reread, including finite-base-change invariance, Lemma4.5 surjectivity, degree6 nonzero table and (4.7.1)-(4.7.2).',
      'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_generation')
event('F.3.22', 'independent re-proof',
      'Independent Steps2-5 audit PASSED, as reported explicitly by the parent: Hodge-Tate/conjugation calculation and common-element simultaneous tangency constraints checked; original primary pages reopened. This is the documented independent-review outcome, with no additional unreported checks attributed.',
      'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent elliptic_splitting')

code = 'output/RESEARCH_SA07/code/check_genus_two_tangent_space.py'
output = 'output/RESEARCH_SA07/code/check_genus_two_tangent_space.output.txt'
wall = re.search(r'ACTUAL_WALL_SECONDS: ([0-9.]+)', (ROOT/output).read_text()).group(1)
computations = [dict(statement_id='F.3.22', code=code, output=output,
                     code_sha256=sha(code), output_sha256=sha(output), actual_wall_seconds=wall,
                     independent_root_wall_seconds='0.305329', independent_root_exit_code=0,
                     input='Four-letter free Lie algebra, degree6 balanced CM weight, five specialness blocks; selected minors modulo101 and exact integer kernel.')]
event('F.3.22', 'computation or formal certificate',
      'Complete exact certificate: balanced degree6 free-Lie dimensions3,30,30,3; five specialness matrix shapes(8,6),(140,66),(312,120),(140,66),(8,6); rational ranks6,66,119,66,6. Explicit nonzero selected minors modulo101 have determinants100,1,99,100,100. Exact integer middle kernel supplies the matching upper bound and spans the displayed derivation; C=[z1,omega] verifies vanishing on the proper quotient. All minor row/column indices and the exact kernel are in the output. Actual wall seconds '+wall+'; code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'. Parent independent run exited0 in0.305329 seconds. Arithmetic projection and universal-quotient maps are proved in the text, not inferred from this calculation.')
event('F.3.21', 'used and rechecked in this run',
      'The exact finite-cover boundary line and full-normalizer character-transfer proof is reused in F3.22, with all actual subgroup maps retained. The previous split-prime residual scope for this one curve is now closed by F3.22. Its all-prime conclusion does not change the full profinite A22 gate.')

specs = [
 ('AuditNakamura1996','https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0304/LOG_0019.pdf',
  'REOPENED ORIGINAL; THREE INDEPENDENT SCOPE CHECKS',
  'Printed pp115-117: Corollary4.2, degree6 table4.3, Lemma4.5 surjectivity and finite-base-change invariance, Corollary4.6, equations(4.7.1)-(4.7.2). These give the nonzero actual arithmetic quotient of character chi^3. No End(J)=Z premise is imported from the separate centralizer conclusion of TheoremB. Root and period_generation independently reopened the original page images.',
  'work/sources_audit_next/Nakamura1996_Coupling_original.pdf','work/audit_after05_references.bib'),
 ('AuditTakao2010RIMS1709','https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1709.pdf',
  'OPENED ORIGINAL AUTHOR PREPRINT; EXACT LAST-PUNCTURE SCOPE',
  'Field-tower definitions printed pp4-5; Theorem3.5 p21 gives Q_(g,r)(m)=Q_(g,r+1)(m) for g>=2,n>=1, including g2,r0. Theorem3.6 and Lemmas4.2-4.3 pp21-22 support the exact tower maps. F3.22 writes the actual moduli forgetful square and uses both levels6 and7. Final journal full PDF remains not obtained; publisher metadata only: JIMJ11(2012)161-188, DOI10.1017/S1474748010000241.',
  'work/sources_audit_next/Takao2010_RIMS1709.pdf','work/audit_after06_references.bib'),
 ('Tate1967','https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf',
  'OPENED ORIGINAL; EXACT GOOD-REDUCTION HYPOTHESES RECHECKED',
  'Section4.1 Theorem3 and Corollary2, already used in B1.4, supply the Hodge-Tate decomposition for the good-reduction p-divisible group. F3.22 exhibits the smooth charts y^2=1-x^5 and v^2=s^6-s away from2,5. Split primes satisfy ell congruent1 mod5, hence exclude both bad primes. At the four embeddings the Lie characters have exponent-one sets{1,2},{2,4},{4,3},{3,1}; their equations and polarization give every finite monomial relation explicitly.',
  'work/sources_audit_next/Tate1967_full.pdf','work/triangle_comparison_references.bib'),
 ('GenFaltings1983',"https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf",
  'OPENED ORIGINAL LOCATORS REUSED; FINITE-EXTENSION SCOPE CHECKED',
  'Section5 Satz3 printedp360 semisimplicity, Satz4 p360 endomorphisms, and Korollar1 p361 Hom. F3.18-19 establish the actual absolutely simple CM surface and its full endomorphism field. At split primes E tensor Q_l=Q_l^4, so the rank-one idempotents identify all rational Galois lines after every finite extension. Root independently reopened these exact original locators.',
  '', 'work/numberfield_references.bib'),
 ('AuditNakamura1994','https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf',
  'REOPENED ORIGINAL; ACTUAL NORMALIZER AND INERTIA SCOPE',
  'Section2.1 printed pp93-97, especially normalizer definition and Theorem2.1.1 p94. The full class of finite ell-groups satisfies the source assumptions. F3.21 supplies the exact detected boundary character and its transfer to the full normalizer; F3.22 invokes the original theorem only after that equality is proved.',
  'work/sources_audit_next/Nakamura1994.pdf','work/audit_after04_references.bib')
]
sources=[]
for key,url,status,detail,local,bib in specs:
    sources.append(dict(source_key=key,url=url,status=status,locator_and_access=detail,
                        dependent_statement_ids='F.3.22',record_file=bib,date=DATE,who=WHO,
                        local_path=local,sha256=sha(local)))
    event('SRC.'+key,'used and rechecked in this run',status+'. '+detail)

claimpath=ROOT/'work/audit_claims.csv'
claims=list(csv.DictReader(claimpath.open()))
before=Counter(r['status'] for r in claims)
ids={'I.B05.01','I.B05.02','II.MB15.02'}
old=(' F3.21 now proves actual normalizer recognition on the exhibited genus2 X5 target '
     'for ell=5 or ell not congruent1 mod5, through an actual detecting-cover boundary line. '
     'Split-prime genus2 and arbitrary-cover/full-profinite A22 remain unresolved.')
new=(' F3.21-F3.22 now prove actual normalizer recognition on the exhibited genus2 X5 target '
     'for EVERY prime and every finite number-field extension. The exact actual morphism '
     'Y20 to U5 therefore excludes the specified CM-surface homology image of an open-normalizer '
     'procyclic subgroup. Arbitrary-cover CM factors and full profinite A22 remain unresolved.')
for row in claims:
    if row['assertion_id'] in ids:
        row['remaining_obligation_or_scope']=row['remaining_obligation_or_scope'].replace(old,'')
        if 'F3.21-F3.22 now prove' not in row['remaining_obligation_or_scope']:
            row['remaining_obligation_or_scope']+=new
        for key in ['proof_or_locator','canonical_dependencies']:
            if 'F.3.22' not in row[key]: row[key]+='; F.3.22'
        row['check_event_statement_id']=row['assertion_id']
        row['check_event_type']='targeted proof check'
        row['check_event_ledger']=LEDGER
        event(row['assertion_id'],'targeted proof check',
              'Evidence and dependencies strengthened; '+row['status']+' status retained.'+new)
with claimpath.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(claims[0]));w.writeheader();w.writerows(claims)
mdpath=ROOT/'work/audit_claims.md'
md=mdpath.read_text()
escape=lambda x:str(x).replace('|','&#124;').replace('\n',' ')
for row in claims:
    if row['assertion_id'] in ids:
        line='| '+' | '.join(escape(row[k]) for k in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |'
        md,n=re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$',lambda m:line,md,flags=re.M)
        assert n==1
md=md.replace('Supplemental proofs F.3.1–F.3.21','Supplemental proofs F.3.1–F.3.22')
if '`audit_after07_CHECK_EVENTS.tsv`' not in md:
    md=md.replace('`audit_after06_CHECK_EVENTS.tsv`.','`audit_after06_CHECK_EVENTS.tsv`, and `audit_after07_CHECK_EVENTS.tsv`.')
mdpath.write_text(md)

with (ROOT/LEDGER).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
with (ROOT/'work/audit_after07_source_checks.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(sources[0]));w.writeheader();w.writerows(sources)
(ROOT/'work/audit_after07_computation_records.json').write_text(json.dumps(computations,indent=2)+'\n')
validation=dict(assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),
                status_counts=dict(Counter(r['status'] for r in claims)),addendum_event_count=len(events),
                source_record_count=len(sources),updated_claim_ids=sorted(ids),changed_statuses=[],
                root_combined_files_modified=False,canonical_new_result_ids=['F.3.22'],
                superseded_scope='F.3.21 split-prime residual gate for X5; full LM6 A22 unchanged',
                included_F_result_count=len(re.findall(r'\\begin\{result\}\{F\.3\.',(ROOT/'output/RESEARCH_SA07/sections/F_audit.tex').read_text())))
assert Counter(r['status'] for r in claims)==before
(ROOT/'work/audit_after07_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
