"""Join the independent blind readings to the collation and check final anchors."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parent

def ledger(suffix):
    with (ROOT / f'K8-03_{suffix}.tsv').open(encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle, delimiter='\t'))
    keyed = {(r['scan'], r['place']): r for r in rows}
    if len(keyed) != len(rows):
        raise ValueError(f'duplicate scan and place in {suffix}')
    return keyed

def code(value):
    return chr(96) + value.replace('|', r'\|').replace('\n', ' ') + chr(96)

def table_row(cells):
    return '| ' + ' | '.join(cells) + ' |'

def main():
    blind = ledger('blind')
    collation = ledger('collation')
    if blind.keys() != collation.keys():
        raise ValueError('blind and collation keys disagree')
    differences = []
    witness = []
    failures = []
    for key, reading in blind.items():
        scan, place = key
        decision = collation[key]
        page = ROOT / 'pages' / f'K8-03_8_scan{int(scan):03}.tex'
        final = decision['final anchor']
        if not final or final not in page.read_text(encoding='utf-8'):
            failures.append(key)
        if decision['decision'] != 'same':
            differences.append(table_row([
                scan, place, code(reading['what the crop shows']),
                code(decision['first reading']), code(decision['page anchor']),
                decision['decision'], decision['basis']
            ]))
        if decision['page anchor'] != final:
            witness.append(table_row([scan, place, code(decision['page anchor']), code(final)]))
    total = len(blind)
    summary = (f'{total} blind crop readings. {len(differences)} differences from the first '
               f'reading in characters, placement or certainty. '
               f'{total-len(failures)} of {total} final anchors occur literally in their distributed page files.')
    sections = [
        '# Blind readings compared with the page files', '', summary, '',
        'The blind TSV preserves the independent readings. The collation records the first reading, '
        'the exact audit anchor before the freeze, the final anchor and the image-based decision. '
        'Short anchors can recur. The scan, named crop and position identify their intended occurrence. '
        'The comparison accepts equivalent descriptions of the same ink, including an isolated label '
        'read without its surrounding layout commands.', '',
        '## Differences at the blind audit', '',
        '| Scan | Crop and place | Independent blind reading | First reading | Reading after audit | Decision | How it was settled |',
        '|---|---|---|---|---|---|---|', *differences, '',
        '## Later witness changes at recorded blind anchors', '',
        '| Scan | Crop and place | Audit anchor | Final anchor |', '|---|---|---|---|', *witness, ''
    ]
    if failures:
        sections.extend(['## Unmatched final anchors', '', *[f'- Scan {n}, {place}' for n,place in failures], ''])
    (ROOT / 'K8-03_blind_compare.md').write_text('\n'.join(sections), encoding='utf-8')
    print(summary)
    return bool(failures)

if __name__ == '__main__':
    raise SystemExit(main())
