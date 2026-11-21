from pathlib import Path
import csv
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

root = Path('/workspace/scratch/74996cb138ef/work/archive')
path = root / 'ARCHIVE_QUESTIONS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
by_id = {row['question_id']: row for row in rows}

def update(qid, **kwargs):
    by_id[qid].update(kwargs)

update('A-Q069', status='proved', proof_id='A-019',
       result_or_exact_gate='EKM §8 Theorem8.4 p48, with full proof8.2-8.4 pp47-48 checked, cancels the hyperbolic summand in every characteristic because its polar form is nonsingular. The actual resulting isometry is recorded in FIELD_CANCELLATION.md.')
update('A-Q115', status='proved', proof_id='A-020',
       result_or_exact_gate='James Theorem11.5 p40 classifies simples by p-regular partitions. Jordan-Hoelder makes their classes a free Z-basis; for n=p exactly the partition(1^p) is excluded. Lemma10.2 p36 verifies the equal p-regular-class count.')
update('A-Q116', status='refuted', proof_id='A-023',
       source_kind='test of supplied study coefficient-ring question',
       result_or_exact_gate='A=Z_(2)[epsilon]/(2epsilon,epsilon^2) is local of characteristic0. The rank-one S2-character g maps to1+epsilon has determinant neither1 nor-1, while every combination of rho2 and rho1^2 has determinant +/-1. Thus the rho classes fail generation in degree2.')
update('A-Q117', status='proved', proof_id='A-022',
       assertion='Study formula w2(H(L))=c1(L) mod2',
       result_or_exact_gate='Proved for every scheme overZ[1/2] via the actual nonisotropic-line pullback, tautological-line identification, Bockstein identity and injectivity of etale cohomology. OriginalPDFp4 contains the c1 question. The full higher-rank formula is recorded separately.')
update('A-Q102', scan='23')
update('A-Q111', scan='26')

for row in rows:
    if row['cote'] == '133' and row['scan'] in {'4','20','21','22','23','26','27','29'}:
        p = int(row['scan'])
        row['scan_verification'] = f'Original Montpellier PDFp{p}/sitep{p-1} visually inspected at140dpi; allPDFpp19-29 andp4 are now checked. See PRIMARY_SCAN_FOLLOWUP.md.'

def append(qid, assertion, status, result, proof, scan, kind):
    assert qid not in by_id
    row = dict(zip(fields, [''] * len(fields)))
    row.update(question_id=qid, cote='133', scan=str(scan), source_kind=kind,
               source_file='SA17_STUDY_cote133_lambda.md', assertion=assertion,
               status=status, result_or_exact_gate=result, proof_id=proof,
               scan_verification=f'Original Montpellier PDFp{scan}/sitep{scan-1} visually inspected; study text read independently.')
    rows.append(row)
    by_id[qid] = row

append('A-Q120', 'The study leaves polynomiality for exact Z_p-lattices open', 'proved',
       'A021 supplies the explicit rationalization isomorphism, inverse Specht classes and induction compatibility. The proof works for every characteristic-zero DVR, complete or not, using uniformizer torsion and James all-field absolute splitting.',
       'A-021', 29, 'supplied study open question; resolved here')
append('A-Q121', 'Study general hyperbolic formula w_t(H(E))=sum(1+alpha t)^(r-j)c_j(E)t^(2j)', 'proved',
       'EKV Proposition5.5 pp183-184, fully read, proves the formula for regular schemes overZ[1/2] (regularity introduced in5.4 p182). Zibrowius WCS §1.4 eqs6-8 p8 reproduces it. Arbitrary ringed-topos target remains A-Q080.',
       'A-022', 4, 'supplied study addition')
append('A-Q122', 'Classify all coefficient rings for which the induction ring is polynomial on rho_i', 'gate',
       'Positive cases now include all characteristic-zero fields and DVRs, with the actual rationalization map proved. F_p gives the modular failure and A023 gives a characteristic-zero local failure. No complete necessary-and-sufficient classification of coefficient rings has been obtained.',
       'A-007; A-020; A-021; A-023', 29, 'original manuscript question repeated in supplied study')

assert len(rows) == len({row['question_id'] for row in rows})
assert all(row['status'] in {'proved','refuted','gate'} for row in rows)
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

stamp = datetime.now(ZoneInfo('Europe/Berlin')).isoformat(timespec='seconds')
who = 'GPT-6 Astra Pro; effort not exposed; run /root/archive_audit'
events = [
('A-REF-EKM8', 'targeted source check', 'Read complete EKM Lemma8.2 and Theorems8.3-8.4 pp47-48, including the F2 case; checked nonsingular-polar cancellation hypothesis and characteristic-free application to the hyperbolic stabilizer.'),
('A-019', 'targeted proof check', 'PASS complete application checked: dimension determines G, H(E) identifies with H(G) orthogonal H(F), nonsingular hyperbolic polar form permits cancellation, yielding the stated actual isometry.'),
('A-REF-JAMES8-12', 'targeted source check', 'Read James8.4 pp29-30 and8.6-8.11 pp30-31;10.2 p36;11.1-11.5 pp39-40;12.1-12.3 pp42-43. Verified integral basis/reduction, all-field absolute splitting, simple labels and unitriangularity. General modular-classification dependencies remain those explicitly cited by James.'),
('A-020', 'targeted proof check', 'PASS whole proof checked: exact K0 composition multiplicity map has inverse on simple classes; exactly(1^p) is excluded among p-regular partitions ofp, giving partition_number(p)-1.'),
('A-021', 'targeted proof check', 'PASS whole proof checked: torsion boundary via free O[G] presentation, independence by fibre product, horseshoe additivity, arbitrary lattice-presentation formula, zero on reductions, Specht-unitriangular generation, uniformizer filtration, commensurability, inverse Specht classes and induction compatibility. Extension to every characteristic-zero DVR uses the verified all-field theorem11.5.'),
('A-REF-EKV5', 'targeted source check', 'Visually read EKV5.5 pp183-184 and read5.1-5.4 pp179-182. Verified exact full hyperbolic formula and inherited regularity scope. Found the integral Picard-isomorphism sentence onp183 needs qualification; the independent line proof avoids it. Read Zibrowius WCS §1.4 eqs6-8 p8 and gamma Prop3.3 pp19-20.'),
('A-022', 'targeted proof check', 'PASS whole line-bundle proof checked: nonisotropic tautological line maps isomorphically to L, orthogonal complement has root alpha+x, determinant root alpha, Kummer/Bockstein c1=x^2+alpha*x, and injective etale pullback descends w2=c1. Full higher-rank formula recorded in the checked primary regular-scheme scope.'),
('A-023', 'targeted proof check', 'PASS whole counterexample checked: explicit ring product gives characteristic0, epsilon nonzero and local unit criterion; (1+epsilon)^2=1; determinant respects every admissible exact sequence via block triangular action; rho2 and rho1^2 determinants are1 and-1; character1+epsilon lies outside their determinant image.'),
('A-REF-ARCHIVE133-EXTRA', 'targeted source check', 'Actually viewed originalPDFp4,p20,p21,p22,p23,p26,p27,p29 at140dpi, in addition to previously checkedpp19,24,25,28. Confirmed c1 question, injection/map-power definitions, deleted coarse induction formula, quotient-partition factor, distinguished-functor and eventual-equivalence definitions, and original all-coefficient-ring question.'),
('A-ARCHIVE-ASSERTION-REGISTER', 'targeted proof check', 'Updated the122-row assertion ledger:80proved,24refuted,18gates. Split line and full hyperbolic formulas, recorded resolved Z_p/DVR question and precise remaining coefficient-ring classification. Page metadata updated only after actual image inspection; no synthetic per-row proof events were added.')
]
with (root / 'CHECK_EVENTS.tsv').open('a', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t')
    for ident, kind, outcome in events:
        writer.writerow([ident, stamp, who, kind, outcome])

print(dict(Counter(row['status'] for row in rows)))
print('rows', len(rows), 'events_added', len(events), 'date', stamp)
