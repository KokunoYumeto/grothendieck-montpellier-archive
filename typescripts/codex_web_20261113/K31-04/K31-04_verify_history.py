"""Verify both sets of SHA-256 digests and the scope of every witness edit."""
from collections import Counter
import csv
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PAGES = [f'pages/K31-04_31_scan{n:03}.tex' for n in range(2, 18)]
FRAGMENT = 'K31-04_transcription.tex'
MARK = re.compile(r'\\(?:unsure|illegible)\{')
TEX = re.compile(r'\\(?:[A-Za-z]+|.)|[{}]', re.DOTALL)

def table(name):
    with (ROOT / name).open(encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file, delimiter='\t'))

def spans(text):
    for start in MARK.finditer(text):
        depth = 1
        for token in TEX.finditer(text, start.end()):
            if token.group() == '{':
                depth += 1
            elif token.group() == '}':
                depth -= 1
                if depth == 0:
                    yield start.start(), token.end()
                    break
        else:
            raise ValueError('Unclosed editorial mark')

def recorded_digests(phase):
    prefix = f'sha256 {phase} '
    lines = (ROOT / 'progress.log').read_text(encoding='utf-8').splitlines()
    pairs = [line[len(prefix):].split(' ', 1) for line in lines if line.startswith(prefix)]
    if len(pairs) != len(PAGES) + 1:
        raise ValueError(f'Unexpected number of {phase} hashes')
    return {name: digest for digest, name in pairs}

def verify():
    witnessed = table('K31-04_witness.tsv')
    changes = [r for r in table('K31-04_revisions.tsv') if r['phase'] == 'witness']
    final = {name: (ROOT / name).read_bytes().decode('utf-8') for name in PAGES}
    frozen = {}
    counts = Counter()
    for n, name in enumerate(PAGES, 2):
        source = final[name]
        for edit in reversed([e for e in changes if int(e['scan']) == n]):
            i = int(edit['offset'])
            if not source.startswith(edit['after'], i):
                raise ValueError(f'{name}, {i}: revision does not match')
            source = source[:i] + edit['before'] + source[i + len(edit['after']):]
        frozen[name] = source
        places = list(spans(source))
        rows = [r for r in witnessed if r['scan.locus'].startswith(f'{n:03}.')]
        labels = [r['scan.locus'] for r in rows]
        if labels != [f'{n:03}.{i:02}' for i in range(1, len(places) + 1)]:
            raise ValueError(f'{name}: ledger does not cover each frozen mark')
        reviewed = source
        for (i, j), row in reversed(list(zip(places, rows))):
            old, new, result = row['frozen_reading'], row['final_reading'], row['result']
            if source[i:j] != old:
                raise ValueError(f"{row['scan.locus']}: original reading differs")
            if result not in {'changed', 'alternative added', 'unchanged', 'not covered'}:
                raise ValueError(f"{row['scan.locus']}: unknown outcome")
            if (new == old) != (result in {'unchanged', 'not covered'}):
                raise ValueError(f"{row['scan.locus']}: incompatible outcome")
            if result == 'alternative added' and not new.startswith(old[:-1] + '|'):
                raise ValueError(f"{row['scan.locus']}: first candidate differs")
            reviewed = reviewed[:i] + new + reviewed[j:]
            counts[result] += 1
        if reviewed != final[name]:
            raise ValueError(f'{name}: difference outside frozen marks')
    if sum(counts.values()) != len(witnessed):
        raise ValueError('Witness ledger contains unexpected scan numbers')
    for phase, texts in [('frozen', frozen), ('witness', final)]:
        texts[FRAGMENT] = ''.join(texts[p] for p in PAGES)
        digests = {p: sha256(s.encode('utf-8')).hexdigest() for p, s in texts.items()}
        if digests != recorded_digests(phase):
            raise ValueError(f'{phase}: hash mismatch')
    if final[FRAGMENT].encode('utf-8') != (ROOT / FRAGMENT).read_bytes():
        raise ValueError('Assembled fragment differs from the page files')
    print('17/17 frozen and 17/17 final digests match. Every witness edit is confined to a frozen mark.')
    print(', '.join(f'{value} {key}' for key, value in sorted(counts.items())))

if __name__ == '__main__':
    verify()
