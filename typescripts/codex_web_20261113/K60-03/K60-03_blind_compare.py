"""Compare the crop-only observations with the initial and delivered page readings.

Run this file with Python 3 from any directory.  The collation ledger preserves
initial disagreements through the audit and the subsequent witness check.
The page test checks each target directly in the delivered TeX.
"""
from pathlib import Path
import csv
import re
import unicodedata

HERE = Path(__file__).resolve().parent
PREFIX = 'K60-03_'

def canon(s):
    """Retain glyphs, indices, primes, punctuation and editorial state."""
    s = unicodedata.normalize('NFC', s)
    # Keep the preferred reading of a doubt, respecting nested TeX braces.
    while r'\unsure{' in s:
        start = s.rindex(r'\unsure{')
        depth = 1
        stop = start + len(r'\unsure{')
        for j in range(stop, len(s)):
            if s[j] == '{':
                depth += 1
            elif s[j] == '}':
                depth -= 1
                if depth == 0:
                    break
        else:
            raise ValueError('unclosed doubt macro')
        s = s[:start] + s[stop:j].split('|', 1)[0] + s[j+1:]
    s = re.sub(r'\\(?:left|right|qquad|quad|displaystyle)(?![a-zA-Z])', '', s)
    s = re.sub(r'\\(?:,|;|!)', '', s)
    s = s.replace(r'\[','').replace(r'\]','').replace('$','').replace('&','')
    return ''.join(s.split())

def tsv(name):
    with (HERE / (PREFIX + name)).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def cell(s):
    return '\x60' + s.replace('|', r'\|').replace('\x60','ˋ') + '\x60'

def main():
    rows = tsv('blind.tsv')
    ledger = {(r['scan'],r['place']):r for r in tsv('collation.tsv')}
    lines = ['# Comparison of the blind readings', '',
             'The crop observations were entered before reopening each page. The initial column gives the corresponding preferred reading before the audit. The page test searches the delivered page for the recorded final reading, retaining editorial state, indices and punctuation.', '',
             '| Scan | Place | Crop reading | Initial page reading | Final reading | Settlement | Page test |',
             '|---|---|---|---|---|---|---|']
    misses = []
    agreements = 0
    for b in rows:
        n, p, blind = b['scan'], b['place'], b['what the crop shows']
        record = ledger.get((n,p))
        if record is None:
            misses.append(f'Scan {n}, {p} awaiting collation')
            continue
        first, final = record['initial'], record['final']
        page = (HERE/'pages'/f'{PREFIX}60_scan{int(n):03}.tex').read_text()
        matched = canon(final) in canon(page)
        if not matched:
            misses.append(f'Scan {n}, {p} final text not located')
        if canon(blind) == canon(first) and canon(blind) == canon(final) and matched:
            agreements += 1
            continue
        lines.append('| ' + ' | '.join([n,p,cell(blind),cell(first),cell(final),
                     record['settlement'], 'found' if matched else 'missing']) + ' |')
    lines.extend(['', f'{len(rows)} observations. {agreements} agree directly across all three readings.'])
    if misses:
        lines.extend(['','## Pending locations',''] + ['- '+m for m in misses])
    (HERE/(PREFIX+'blind_compare.md')).write_text('\n'.join(lines)+'\n')
    return len(misses)

if __name__ == '__main__':
    raise SystemExit(bool(main()))
