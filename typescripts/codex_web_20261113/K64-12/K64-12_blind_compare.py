"""Rebuild the blind collation from the crop readings, their alignment and the page files."""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def rows(name):
    with (ROOT/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def cell(s):
    return s.replace('|',r'\|').replace('\n',' ')

def main():
    blind = {(r['scan'],r['place']): r['what the crop shows'] for r in rows('K64-12_blind.tsv')}
    alignment = rows('K64-12_blind_alignment.tsv')
    assert len(blind) == len(alignment)
    entries, later, evidence = [], [], []
    for row in alignment:
        scan, place = row['scan'], row['place']
        reading = blind.pop((scan,place))
        lines = (ROOT/'pages'/f'K64-12_64_scan{scan}.tex').read_text().splitlines()
        ends = list(map(int,row['TeX lines'].split('-')))
        passage = '\n'.join(lines[ends[0]-1:ends[-1]])
        assert passage and row['first passage SHA256'] and reading
        assert hashlib.sha256(reading.encode('utf-8')).hexdigest() == row['blind reading SHA256'], (scan,place)
        if hashlib.sha256(passage.encode()).hexdigest() != row['audited passage SHA256']:
            later.append((scan,place))
        if row['settlement']:
            ref = f"pages/K64-12_64_scan{scan}.tex#L{ends[0]}"
            evidence.append([f"[{scan}, {place}]({ref})", row['TeX lines'], reading])
            entries.append([scan,place,row['TeX lines'],row['first file reading'],
                            row['contrast on blind reading'],row['settlement']])
    assert not blind
    note = ['# Blind comparison · K64-12','',
        f'{len(alignment)} crop readings were aligned to passages of the thirteen page files. '
        f'The two independent readings differed at {len(entries)} aligned places. '
        'One place can contain several letters or signs. The TSV preserves the full blind wording. '
        'The comparison uses a human alignment of the handwriting and TeX notation.',
        '', '| Scan | Place | TeX lines | First file | Blind reading | Settlement on the ink |',
        '|---|---|---|---|---|---|']
    note += ['| '+' | '.join(cell(x) for x in entry)+' |' for entry in entries]
    note += ['', '## Crop readings at the differing places', '',
        'The links open the final page files. The line numbers give each aligned passage, and the last column is read directly from the blind TSV.',
        '', '| Page and place | TeX lines | Blind TSV entry |', '|---|---|---|']
    note += ['| '+' | '.join(cell(x) for x in entry)+' |' for entry in evidence]
    note += ['', '## Source verification','',
        'SHA-256 is computed on the UTF-8 lines for each aligned passage, joined with line feeds. '
        'The alignment retains both its first-pass and its independently audited digest. Each independent crop entry is also checked against its recorded SHA-256. '
        'Coordinates refer to the page file, beginning at line 1.']
    if later:
        note += ['',f'{len(later)} aligned passages now include at least one post-freeze change. '
                 'The original blind judgments above are preserved. See the witness table for the exact changed marks.','']
        note += [f'- Scan {n}, {p}' for n,p in later]
    else:
        note += ['', 'All aligned passages match their independently audited digests.']
    (ROOT/'K64-12_blind_compare.md').write_text('\n'.join(note)+'\n')
    print(f'{len(alignment)} aligned, {len(entries)} blind differences, {len(later)} post-audit passage differences.')
if __name__=='__main__':
    main()
