"""Own canonical audit records after F.3.21, with no root combined-file edits."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/f6dbb6638732')
WHO = 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
DATE = '2026-11-19'
LEDGER = 'work/audit_after06_CHECK_EVENTS.tsv'
events = []


def event(statement, kind, outcome):
    events.append(dict(statement_id=statement, date=DATE, who=WHO, type=kind, outcome=outcome))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest() if path else ''


event('F.3.21', 'independent re-proof',
      'Proved actual cusp recognition for X5:Y^2=1-X^5 minus infinity for ell=5 or ell not congruent1 mod5, over every finite number-field extension. Absolute simplicity and the degree4 endomorphism field exclude every rational Galois line at these primes by Faltings and the exact local field degrees. A finite ell-quotient constructs an actual finite etale detecting cover; its maximal pro-ell group equals the chosen subgroup by the ell-group normal-closure argument. Intersecting its arithmetic subgroup with the normalizer yields an open arithmetic image and trivial geometric-kernel action on cover homology. The first Magnus character and proper-homology weights place the detected line in the actual boundary kernel. Making the finite boundary rational gives theta=chi exactly; comparison of lifts transfers it to the full normalizer. Nakamura1994 Theorem2.1.1 then gives actual inertia. Root independently re-proved the argument and reread original pp93-97; passed. Split primes and full profinite A22 remain unresolved.')
event('F.3.21', 'targeted proof check',
      'Checked the descent and normalizer maps explicitly: Pi_Y is the image of the actual finite-cover arithmetic subgroup because the previously divided-out geometric kernel is contained in it; N0=N intersect Pi_Y has finite index in N; p(N0) is open; N0 intersect P0 acts inner on P0^ab. The character theta is already trivial on N intersect P by comparison with the first nonzero rational Magnus term. The boundary line lies in the kernel before any field extension; over L1 all boundary points are rational, and every full-normalizer element has the same arithmetic image as an element of N1. No arithmetic section and no splitting of mixed homology are used.')
event('WORK.A22.G2.TANGENT', 'targeted proof check',
      'Constructed the exact special degree6 derivation D using z1,z2,c=[z1,z2], a1=[z2,c], a2=-[z1,c]. Its CM-torus character is chi^3, all four generator evaluations are inner, and D is not globally inner by free-Lie centralizers. The identity c=[z1,omega] makes its induced derivation on the closed-surface quotient L/(omega) zero. The actual moduli forgetful map and Takao2010 Theorem3.5 field-tower equality yield q6(Q_l[D] intersect gr6 Gamma_univ)=0. This does not assert membership of D in universal monodromy, a formula for the entire tangent subspace, or an arithmetic-normalizer subgroup. Work-only pending parent audit.')

code = 'output/RESEARCH_SA07/code/check_genus_two_tangent.py'
output = 'output/RESEARCH_SA07/code/check_genus_two_tangent.output.txt'
wall = re.search(r'ACTUAL_WALL_SECONDS: ([0-9.]+)', (ROOT / output).read_text()).group(1)
computation = dict(statement_id='WORK.A22.G2.TANGENT', code=code, output=output,
                   code_sha256=sha(code), output_sha256=sha(output), actual_wall_seconds=wall)
event('WORK.A22.G2.TANGENT', 'computation or formal certificate',
      'Exact integer associative-word certificate checks specialness, all four nonzero degree7 images, distinct conjugator multidegrees, character t^3, order5 and pair-exchange symmetries, and c=[z1,omega]. Actual wall seconds '+wall+'; code SHA256 '+sha(code)+'; output SHA256 '+sha(output)+'. The field-tower diagram is a written proof using an opened primary source, not a computational inference.')

specs = [
    ('AuditNakamura1994', 'https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf',
     'REOPENED, ORIGINAL EXACT SCOPE CHECKED',
     'Section2.1 pp93-97: full class, smooth noncomplete hyperbolic number-field curve, definition of cyclotomic normalizer onp94, Theorem2.1.1 p94, and actual finite-cover weight argument pp96-97 reread. Root independently reread the same original passage.',
     'F.3.21', 'work/sources_audit_next/Nakamura1994.pdf', 'work/audit_after04_references.bib',
     'used and rechecked in this run'),
    ('GenFaltings1983', "https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf",
     'EXACT PRIMARY LOCATORS REUSED AND HYPOTHESES RECHECKED',
     'Original Section5 Satz3 p360 semisimplicity and Satz4 p360 integral End. Finite number-field extensions retain the hypotheses. The local idempotent ranks on the rank-one E tensor Q_l module exclude rational lines at every nonsplit or ramified prime in F3.21.',
     'F.3.21', '', 'work/numberfield_references.bib', 'used and rechecked in this run'),
    ('AuditTakao2010RIMS1709', 'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1709.pdf',
     'OPENED, FULL ORIGINAL AUTHOR PREPRINT',
     'RIMS1709 November2010; cover and full25-page PDF obtained. Field-tower definitions pp4-5, Theorems3.4-3.6 p21 and Lemmas4.2-4.3 p22 read. Theorem3.5 expressly includes g>=2,r=0,n=1 and identifies the levels for r and r+1. This supplies the last-puncture equality used in the exact tangent-line quotient diagram. Final journal PDF not obtained; Cambridge publisher landing separately confirms JIMJ11(2012)161-188, DOI10.1017/S1474748010000241.',
     'WORK.A22.G2.TANGENT', 'work/sources_audit_next/Takao2010_RIMS1709.pdf', 'work/audit_after06_references.bib',
     'used and rechecked in this run'),
    ('AuditNakamuraTakaoUeno1994', 'https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0884-13.pdf',
     'REOPENED, PRECISE PUNCTURE SCOPE CHECKED',
     'Theorem2.4 printedp115 explicitly assumes n>=1; Section3 pp116-117 keeps that affine boundary. It was not used to fill the last puncture. The subsequent Takao2010 source supplies that exact additional map.',
     'WORK.A22.G2.TANGENT', '', 'work/audit_after05_references.bib', 'used and rechecked in this run'),
    ('AuditMoritaSakasaiSuzuki2015v2', 'https://arxiv.org/pdf/1404.3351',
     'OPENED, PRIMARY SOURCE LEAD; NO THEOREM IMPORTED',
     'Full39-page arXiv1404.3351v2(19July2015) opened and downloaded. Lemma3.2 and Proposition3.4 pp15-16, Section7 Table7/Proposition7.2/Theorem7.5 pp25-30 read. The normalized stable-range basis has a 2g-4 denominator. No specialization of that basis or stable normalizer calculation to genus2 is asserted; the current arithmetic quotient proof uses Takao instead.',
     'genus-two degree6 source route', 'work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf', 'work/audit_after06_references.bib',
     'carried as background without fault found'),
    ('AuditDavisPriesWickelgren2022v3', 'https://arxiv.org/pdf/1808.04917',
     'OPENED, PRIMARY SOURCE LEAD; NO FILTERED-ACTION CLAIM IMPORTED',
     'Full19-page arXiv1808.04917v3(14February2022) opened. Introduction pp1-3, Theorem1.1 p2, Corollary1.2 p3 read. The actual map Aut(pi) to Aut(gr pi) is determined by the action in degree1 because the graded Lie algebra is generated there. An element in the degree6 filtered automorphism kernel has trivial action on gr but may have a nonzero leading derivation V to L7, as in F3.20. Therefore this source does not supply that required filtered leading term. The explicit mod-p corollary retains its stated Vandiver premise.',
     'genus-two arithmetic action source route', '', 'work/audit_after06_references.bib',
     'carried as background without fault found')
]
sources = []
for key, url, status, detail, dependencies, local, bib, kind in specs:
    sources.append(dict(source_key=key, url=url, status=status, locator_and_access=detail,
                        dependent_statement_ids=dependencies, record_file=bib,
                        date=DATE, who=WHO, local_path=local, sha256=sha(local)))
    event('SRC.'+key, kind, status+'. '+detail)

claimpath = ROOT / 'work/audit_claims.csv'
claims = list(csv.DictReader(claimpath.open()))
before = Counter(row['status'] for row in claims)
ids = {'I.B05.01', 'I.B05.02', 'II.MB15.02'}
addition = (' F3.21 now proves actual normalizer recognition on the exhibited genus2 X5 target '
            'for ell=5 or ell not congruent1 mod5, through an actual detecting-cover boundary line. '
            'Split-prime genus2 and arbitrary-cover/full-profinite A22 remain unresolved.')
for row in claims:
    if row['assertion_id'] in ids:
        if 'F3.21 now proves' not in row['remaining_obligation_or_scope']:
            row['remaining_obligation_or_scope'] += addition
        for key in ['proof_or_locator', 'canonical_dependencies']:
            if 'F.3.21' not in row[key]:
                row[key] += '; F.3.21'
        row['check_event_statement_id'] = row['assertion_id']
        row['check_event_type'] = 'targeted proof check'
        row['check_event_ledger'] = LEDGER
        event(row['assertion_id'], 'targeted proof check',
              'Evidence and dependencies strengthened; '+row['status']+' status retained.'+addition)
with claimpath.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(claims[0]))
    writer.writeheader()
    writer.writerows(claims)

mdpath = ROOT / 'work/audit_claims.md'
md = mdpath.read_text()
escape = lambda text: str(text).replace('|', '&#124;').replace('\n', ' ')
for row in claims:
    if row['assertion_id'] in ids:
        line = '| '+' | '.join(escape(row[key]) for key in
                               ['assertion_id', 'status', 'claim', 'proof_or_locator', 'remaining_obligation_or_scope'])+' |'
        md, n = re.subn(r'^\| '+re.escape(row['assertion_id'])+r' \|.*$', lambda match: line, md, flags=re.M)
        assert n == 1
md = md.replace('Supplemental proofs F.3.1–F.3.20', 'Supplemental proofs F.3.1–F.3.21')
if '`audit_after06_CHECK_EVENTS.tsv`' not in md:
    md = md.replace('`audit_after05_CHECK_EVENTS.tsv`.', '`audit_after05_CHECK_EVENTS.tsv`, and `audit_after06_CHECK_EVENTS.tsv`.')
mdpath.write_text(md)

with (ROOT / LEDGER).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'], delimiter='\t')
    writer.writeheader()
    writer.writerows(events)
with (ROOT / 'work/audit_after06_source_checks.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(sources[0]))
    writer.writeheader()
    writer.writerows(sources)
(ROOT / 'work/audit_after06_computation_records.json').write_text(json.dumps([computation], indent=2)+'\n')
validation = dict(assertion_count=len(claims), source_entry_count=len({r['note_id'] for r in claims}),
                  status_counts=dict(Counter(r['status'] for r in claims)), addendum_event_count=len(events),
                  source_record_count=len(sources), updated_claim_ids=sorted(ids), changed_statuses=[],
                  root_combined_files_modified=False, canonical_new_result_ids=['F.3.21'],
                  work_only_result_ids=['WORK.A22.G2.TANGENT'])
assert Counter(r['status'] for r in claims) == before
(ROOT / 'work/audit_after06_validation.json').write_text(json.dumps(validation, indent=2)+'\n')
print(json.dumps(validation, indent=2))
