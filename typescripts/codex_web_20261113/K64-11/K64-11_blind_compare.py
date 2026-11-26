"""Compare the independent crop readings with their aligned first readings and current TeX.
Run with Python 3 from any directory. Only the comparison report is written.
"""
import csv
import unicodedata
from pathlib import Path

root = Path(__file__).resolve().parent
def rows(name):
    with (root / ('K64-11_' + name + '.tsv')).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))
def key(row):
    return row['scan'], row['place']
def norm(value):
    return ' '.join(unicodedata.normalize('NFC', value).split())
def cell(value):
    return value.replace('|', r'\|').replace('\n',' ')
def main():
    blind = rows('blind')
    aligned = {key(row): row for row in rows('collation')}
    assert len(blind) == len(aligned) == len(set(map(key, blind)))
    assert set(map(key, blind)) == set(aligned)
    differences = []
    for reading in blind:
        scan, place = key(reading)
        record = aligned[(scan, place)]
        path = root / 'pages' / f'K64-11_64_scan{scan}.tex'
        anchor = record.get('post-witness TeX anchor') or record['audited TeX anchor']
        if anchor not in path.read_text(encoding='utf-8'):
            raise ValueError(f'{scan} {place}: TeX anchor missing in {path.name}: {anchor}')
        first = record['aligned first-pass reading']
        second = reading['what the crop shows']
        if norm(first) != norm(second):
            differences.append((scan, place, first, second, record['settlement']))
    content = ['# Comparison of the two independent readings', '',
               f'{len(blind)} crop readings from {len(set(r["scan"] for r in blind))} scans. '
               f'{len(differences)} differ from the aligned first reading. '
               'Every reading has an anchor in the page file. The first-pass wording in the collation table '
               'uses the same notation and description of pen position as the blind reading wherever they agree. '
               'The table below records the decisions made before the witness was opened.', '',
               '| Scan | Crop | First reading | Independent reading | Settlement on the ink |',
               '|---|---|---|---|---|']
    content.extend('| ' + ' | '.join(map(cell, line)) + ' |' for line in differences)
    (root/'K64-11_blind_compare.md').write_text('\n'.join(content)+'\n', encoding='utf-8')
    print(f'{len(blind)} anchors present, {len(differences)} differences recorded.')
if __name__ == '__main__':
    main()
