from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] in ('MT-S506', 'MT-S507') for r in rows)
with (root / 'section.tex').open('a') as f:
    f.write('\n' + (root / 's5_dirichlet_pole_cone.tex').read_text())
rows.extend([
    dict(id='MT-S506',
         statement='For every S5 Galois extension of Q, the rank-six Artin representation is induced from a nontrivial quartic F20 character and its L-function is entire. In 0<Re(s)<1 every possible irreducible Artin pole is supported on zeros of zeta_Q or of the quadratic Dirichlet factor. A_D alone therefore puts every possible pole on the critical line; explicit pole-order bounds also involve the entire rank-six factor.',
         input='neither for character identities, Hecke entireness and pole support; Alpoge A_D for critical-line location. No Calegari local hypothesis and no Masullo input needed.',
         status='proved here using classical all-prime Artin induction, Hecke analyticity and Brauer meromorphicity with exact locators. Pole absence and general zero location are not asserted.',
         where_the_proof_is='GRH_NIGHT.tex MT-S506; work/root/s5_dirichlet_pole_cone.tex; explicit complete S5 character table and seven induced identities; PY07 section2.1Properties1-2p3,section3.1pp4-5,Theorem3.3p5',
         where_it_lives='Q-S5-DIRICHLET-POLES; Q-ARTIN-POS; finite Artin motives and all-prime finite pushforward; strengthens the required analytic input for the S5 pole-location branch'),
    dict(id='MT-S507',
         statement='With the two four-dimensional S5 factors holomorphic at a point, all43 distinct induced-linear-character zero-order tests are equivalent to12 explicit inequalities. A rank-five pole of order v forces relative Dedekind order q>=4v and total order r>=5v, precise common zeros, and a zero of order>=v in the other rank-five factor. If the corresponding rank-four factor is nonzero, q>=6v and r>=8v. All bounds are sharp for this exact cone, with four verified formal witnesses.',
         input='neither for the cone and order bounds, plus pointwise rank-four holomorphy; Calegari Theorem1.1 supplies that premise in the stated local S5 family. Alpoge A_D confines possible poles to the line. Masullo M_H conditional plus MT-S505 excludes real poles in that family.',
         status='proved here with complete finite enumeration and exact integer decomposition certificate, author/root whole-proof readings and optimizer-free computational checks. Formal sharpness is not arithmetic realization; noncoincidence of the required zeros remains open.',
         where_the_proof_is='GRH_NIGHT.tex MT-S507; work/root/s5_dirichlet_pole_cone.tex; work/checks/s5_hecke_cone.py/.json and s5_cone_decomposition_verification.py/.json; Calegari13Theorem1.1p2/tablep4',
         where_it_lives='Q-ARTIN-POS; Q-S5-MONOMIAL-CONE; MT-S501/504/505; exact induced-rank-one positivity versus effectiveness of each irreducible Artin order divisor')
])
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([
            sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed',
            'GRH_NIGHT_20261121', kind, outcome])

event(root / 'events.tsv', 'MT-S506', 'targeted proof check',
      'Read the entire proof. Checked all seven character columns, virtual-character positivity and completeness, exact subgroup/twist conventions, primitive quartic F20 induction, T sign characters, all-prime analytic identities, meromorphic integer orders and A_D-only pole localization. No gap found; neither general zero location nor Artin holomorphy is inferred.')
event(root / 'events.tsv', 'MT-S507', 'targeted proof check',
      'Read the whole proof, all43 displayed decompositions, exhaustive subgroup/linear-character algorithm, exact certificate scope, inequalities, all four formal witnesses, common-zero inclusions and the Calegari/M_H separation. Checked the D8 tuple in its expressly stated cycle order. No gap found. The cone is exact only after the explicit c,d>=0 premise, and its sharp vectors are not claimed to be arithmetic divisors.')
for sid in ('MT-S506', 'MT-S507'):
    event(root / 'events.tsv', sid, 'computation or formal certificate',
          'Exact updated integer verifier re-executed by root:43 rows reconstructed from12 generators; both general witnesses attain relative4/total5 and both zero-rank-four branches attain relative6/total8. Exhaustive permutation/character enumeration was separately author-rerun without optimizer and was earlier root constructed/peer checked. This is an exact finite computation, not a proof-assistant certificate; the exploratory MILP is no premise.')
event(base / 'work/checks/source_events.tsv', 'PY07', 'used and rechecked in this run',
      'Root freshly read primary author PDF section2.1Properties1-2p3,section3.1pp4-5 and Theorem3.3p5 for all-prime multiplication/induction, finite-order Hecke entireness and Brauer meromorphicity. These classical results are cited, not independently re-proved. No unrelated permutation-example formula or historical status discussion is used.')

sources = json.loads((root / 'sources.json').read_text())
for s in sources:
    if s['id'] == 'PY07':
        s['locator'] += '; MT-S506/507 also use section2.1Properties1-2p3 and section3.1pp4-5'
        s['web_refs'].append('turn357864581view0')
        s['inspection'] += ' Root additionally read the exact all-prime induction/multiplication and Hecke analyticity statements for MT-S506/507.'
    if s['id'] == 'CALEGARI13':
        s['locator'] += '; MT-S506/507 character labels: section2tablep4; pointwise holomorphy premise: Theorem1.1p2'
(root / 'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields, qs = rd.fieldnames, list(rd)
for q in qs:
    if q['id'] == 'Q-ARTIN-POS':
        q['state'] += ' MT-S506 proves A_D-only critical-line pole support for every S5/Q extension. In the Calegari rank-four-holomorphic family, MT-S507 reduces the remaining rank-five poles to explicit simultaneous-zero sets with relative Dedekind order>=4 times the pole order (>=6 in the nonzero corresponding rank-four branch) and total order>=5 (respectively>=8). Relative order<=3 closes Artin holomorphy at the point. All43 monomial tests are exhausted; their formal sharp witnesses show the missing noncoincidence/order input is additional.'
qs.extend([
    dict(id='Q-S5-DIRICHLET-POLES', source_and_locator='MT-S501/505; PY07section2.1Properties1-2p3,section3.1pp4-5,Theorem3.3p5; S5 character table',
         question='Does localizing possible S5 Artin poles in the critical strip require Hecke GRH over all fields?',
         state='proved MT-S506: A_D suffices for every S5/Q extension, without the Calegari local hypotheses. All possible poles are supported on zeta_Q and the quadratic Dirichlet zero sets; X is entire by explicit quartic induction. Absence of poles is a separate gate.'),
    dict(id='Q-S5-MONOMIAL-CONE', source_and_locator='MT-ART07; MT-S501/504/505; exact S5 subgroup-character certificate',
         question='What do all induced one-dimensional Hecke positivity tests imply about the remaining rank-five S5 poles once the rank-four factors are holomorphic?',
         state='proved exact reduction MT-S507:43 distinct tests reduce to12 inequalities, force q>=4v/r>=5v and stated common zeros, with stronger q>=6v/r>=8v when the corresponding rank-four factor is nonzero. Four formal witnesses prove these cone constants optimal. Remaining gate: rule out the explicit nonreal simultaneous-zero configurations or their order thresholds; the formal witnesses are not realized arithmetic examples.')
])
with path.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(qs)
with (root / 'implications.md').open('a') as f:
    f.write('\n## The S5 pole gate now has exact support and order thresholds\n\nMT-S506 uses only A_D for critical-line pole location in every S5/Q extension, via explicit induced characters and all-prime Artin identities. MT-S507 adds the known rank-four holomorphy in the Calegari family and exhausts all43 induced-linear Hecke tests. A remaining rank-five pole requires explicit common zeros and relative Dedekind order at least4 times its order; when the corresponding rank-four value is nonzero, the penalty rises to6. The total Dedekind penalties are5 and8. Relative order at most3 therefore closes the pointwise holomorphy gate. M_H viaMT-S505 removes the real-axis case in this family. Exact formal witnesses delimit what these positivity tests can prove; they are not arithmetic counterexamples.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — exact S5 pole-support and monomial cone\n\nMT-S506/507 passed complete root proof readings after the author pass. The updated exact verifier checked43 decompositions and four witnesses. The remaining Calegari-family Artin gate is strictly narrowed to the explicit simultaneous-zero/order configurations; general Artin holomorphy is unchanged.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added=['MT-S506', 'MT-S507'])))
