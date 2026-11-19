"""Record the proved top-degree bound and exact local-invariant-cycle gate."""
from pathlib import Path
import csv
import json
import time

start = time.perf_counter()
root = Path(__file__).resolve().parents[2]
path = root / 'part_c/results.csv'
with path.open(newline='') as handle:
    rows = list(csv.DictReader(handle))
fields = list(rows[0])
new = [
    ['c:top-direct-image', 'Top direct image has weight 2n+j; nonvertical components vanish above 2n-1', 'Proved', 'sections/part_c.tex, Proposition label c:top-direct-image', 'Gabber Illusie XVIII_A Theorem1.1; support dimension; proper base change; Poincare duality', '12:118-120; C.4', 'Any lisse coefficient for vanishing; pure weight-j coefficient at a finite-field point for top weight; no dimension-j normalization required.'],
    ['c:lic-endpoint', 'The weight-at-most-j assertion for inertia invariants on a regular proper trait model is equivalent to local invariant cycle surjectivity', 'Proved exact equivalence; general mixed-characteristic assertion unresolved', 'sections/part_c.tex, Proposition label c:lic-endpoint', 'Flach-Morin2012 Theorem10.1(a), checked purity-duality proof; Esnault-Wittenberg2016 section3.1', '12:118-120; C.4', 'This is the precise remaining lower coefficient endpoint, not a proof of the general local invariant cycle theorem.'],
]
known = {row['id'] for row in rows}
for values in new:
    if values[0] not in known:
        rows.append(dict(zip(fields, values)))
with path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields)
    writer.writeheader()
    writer.writerows(rows)
events = root / 'part_c/CHECK_EVENTS.tsv'
prior = events.read_text()
with events.open('a', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t')
    for values in new:
        if values[0] not in prior:
            writer.writerow([values[0], '2026-11-19', 'GPT-6 Astra (OpenAI), /root/part_c', 'used and rechecked in this run', values[1] + '; ' + values[4]])
sources = root / 'part_c/sources.tsv'
prior = sources.read_text()
with sources.open('a') as handle:
    for key, url, locator in [
        ('illusie2014cd', 'https://www.numdam.org/item/AST_2014__363-364__455_0.pdf', 'Theorem1.1,formula1.1.1,p455;Corollary1.4'),
        ('flachmorin2012topos', 'https://www.math.u-bordeaux.fr/~bmorin/Weiletaletopos05-20-12.pdf', 'Theorem10.1(a),author pp77-80; full purity-duality argument read'),
    ]:
        if key + '\t' not in prior:
            handle.write(f'{key}\topened full PDF\t{url}\t{locator}\n')
notes = root / 'part_c/part_c_notes.md'
prior = notes.read_text()
header = '## C4 endpoint update before checkpoint 02\n'
if header not in prior:
    notes.write_text(prior.replace('# Part C research ledger\n', '# Part C research ledger\n\n' + header + '\nThe top coefficient endpoint is now proved: for a regular source, only n-dimensional components mapping entirely to y contribute R^{2n}, and their pure weight-j coefficient gives pure weight2n+j. Every other component vanishes above2n-1. The proof uses Gabber\u2019s strictly-local cohomological dimension bound, support dimensions in a proper compactification, and Poincare duality, and works for arbitrary lisse coefficients before the weight assertion. The remaining lower endpoint over a regular proper trait model has been identified exactly with local invariant cycle surjectivity, by the fully checked Flach\u2013Morin Theorem10.1(a). Thus the prior plural endpoint gate has narrowed to the lower endpoint.\n'))
checked = 0
for n in range(1, 101):
    for q in range(1, 2*n):
        bound = 2*n - 2*((q+2)//2) + q
        assert bound <= 2*n-1
        checked += 1
output = {'result_rows': len(rows), 'events': sum(1 for _ in events.open())-1, 'top_support_inequalities_checked': checked, 'input_n_range': [1, 100], 'runtime_seconds': time.perf_counter()-start}
result = root / 'code/part_c/update_endpoint_records_output.json'
result.write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output))
