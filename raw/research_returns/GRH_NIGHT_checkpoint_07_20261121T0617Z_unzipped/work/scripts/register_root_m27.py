from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] == 'MT-M27' for r in rows)
with (root / 'section.tex').open('a') as f:
    f.write('\n' + (root / 'full_adelic_strip_trace.tex').read_text())
rows.append(dict(
    id='MT-M27',
    statement='The full adelic Masullo wide-strip Hilbert quotient has exact all-character zero-jet kernel and trace-class convolution for every compactly supported smooth idelic test. The absolute all-character/all-zero trace and trace norms are uniform on bounded test sets. The corrected smooth quotient embeds with proper dense image. Centered trace positivity is equivalent to Hecke GRH over the fixed field.',
    input='neither for wide strips containing [0,1] in their interior; classical Meyer Lemma5.6 uniform nuclear extension, MT-M24/M26, actual Masullo definitions; Masullo (conditional) for positivity, not for trace class',
    status='proved here by explicit bounded ambient-pair map, nuclear transfer, orthogonal quotient section and uniform trace-norm tails; narrow all-character strips remain a separate gate',
    where_the_proof_is='GRH_NIGHT.tex MT-M27; work/root/full_adelic_strip_trace.tex; Meyer math/0311468v3 Lemma5.6 pp41–42 and §2.1; Masullo9.2.2.31p416/10.1.1.1p434/10.4.1.3p456',
    where_it_lives='Q-MAS-INFINITE-BASIS and Q-MAS-STRIP-TRACE; actual full adelic Hilbert trace at cote1/SA23 geo-H-lidskii and geo-H-genus'))
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed', 'GRH_NIGHT_20261121', kind, outcome])

event(root / 'events.tsv', 'MT-M27', 'targeted proof check', 'Read entire proof and final positivity/scope deductions. Checked finite-level Fourier approximation, both closed kernels, proper dense image, actual two-polar-term splitting, bounded map B killing H_+, wide-strip diagonal inclusion, rank-one nuclear transfer to Hilbert spaces, identity on dense E before descent, isometric quotient section, finite invariant-block trace-norm inequality, relative compactness of bounded test sets, uniform character and height tails, and centering twist. No gap found. Fresh complete MeyerLemma5.6 proof read; its upstream kernel lemmas remain cited classical inputs.')
event(base / 'work/checks/source_events.tsv', 'MEYER05-ID', 'used and rechecked in this run', 'Fresh root complete read of Lemma5.5 and Lemma5.6, author pp41–42, including its cutoff/Poisson reduction and both nuclear extensions. Exact codomain S(C_K)_>< restricted to U_S-invariants verified. Upstream local Lemma4.3 is a classical prerequisite, not newly fully audited.')
event(base / 'work/checks/root_peer_reviews.tsv', 'AG-SHIMURA-RAM', 'targeted proof check', 'Read entire proposition and proof. Checked generic-fibre transversality versus the ramified nonunit line, unit homothety of the Tate lattice and exact multiplier order Z_p+p^n O_Kp, conductor ideal p^(2n), ramified Hodge valuation and period slope as cited, disk bound, and explicit binomial estimate v_p(u^((p−1)p^j)−1)>=j+1/2. Preserved local-unit restrictions, not all finite Frobenius values. No gap found. Primary AI proof read by author; this is a complete new-proof review, not a new whole-source audit.')

sources = json.loads((root / 'sources.json').read_text())
for source in sources:
    if source['id'] == 'MEYER05-ID':
        source['locator'] += '; Lemma5.5 and Lemma5.6 pp41–42; §2.1 formula(5) pp6–7'
        source['inspection'] += ' Root and complexity subsequently read the complete Lemma5.6 proof and exact nuclear-extension scope for MT-M27; the upstream local kernel results retain classical credit.'
(root / 'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t'); fields = reader.fieldnames; questions = list(reader)
for question in questions:
    if question['id'] == 'Q-MAS-INFINITE-BASIS':
        question['state'] = question['state'].replace('global varying-character uniformity remains separate.', 'MT-M27 closes full adelic varying-character trace class on every wide strip containing [0,1] in its interior, using an explicit comparison with Meyer’s uniform nuclear extension. Narrow centered all-character strips remain separate.')
    if question['id'] == 'Q-MAS-STRIP-TRACE':
        question['state'] += ' MT-M27 closes the all-character passage on wide strips containing [0,1], with exact smooth/Hilbert kernels and uniform absolute trace tails. Under M, the remaining all-character gate is restricted to centered widths at most1/2.'
questions.append(dict(id='Q-MAS-NARROW-ALL-CHARACTERS', source_and_locator='MT-M26/27; Masullo10.4.1.3p456', question='Under M, is the actual all-character centered strip quotient trace class for every positive width, including widths at most1/2?', state='current gate: each fixed sector is proved by MT-M26; full adelic wide strips by MT-M27. Need a uniform transfer or reconstruction on narrow strips, since the wide-strip diagonal inclusion into MeyerLemma5.6 source is unavailable.'))
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t'); writer.writeheader(); writer.writerows(questions)
with (root / 'implications.md').open('a') as f:
    f.write('\n## Full adelic trace on the specified wide-strip quotient\n\nMT-M27 closes the all-character trace-class gate for the actual Masullo Hilbert quotient whenever its strip contains [0,1] in its interior. The proof gives an explicit bounded map from Meyer’s ambient pair to that Hilbert quotient and proves the uniform absolute spectral tails. It includes infinitely many archimedean characters at each finite level. The corrected smooth quotient has its exact all-jet kernel and proper dense image. Full narrow-strip trace class under M_H remains the smaller completion gate; positivity of the centered trace is still equivalent to the relevant GRH.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — full adelic wide-strip trace closed\n\nMT-M27 moves Q-MAS-STRIP-TRACE from fixed-character estimates to a trace-class operator on the actual full adelic Hilbert quotient, with all-character uniform absolute sums. It has complete author and root readings and a fresh primary Lemma5.6 proof check. The unresolved completion branch is now restricted to narrow centered strips under M_H. AG-SHIMURA-RAM also has a complete root proof reading.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added='MT-M27')))
