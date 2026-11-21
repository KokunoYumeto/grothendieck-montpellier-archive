"""Collate the independent site readings against the first and delivered transcripts."""
import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PFX = 'K34-13'
WRAPPERS = re.compile(
    r'\\(unsure|uline|uuline|deleted|inserted|margin|mspage|tag\*|text|operatorname|'
    r'displaystyle|mathrm|underline|mathrel|overset)\{'
)
EQUIVALENTS = (
    (r'\overline K', r'\bar K'), (r'\overline V', r'\bar V'),
    (r'\xrightarrow{\sim}', '≃'), (r'\bigl', ''), (r'\bigr', ''),
    (r'\longrightarrow', '→'), (r'\longleftarrow', '←'),
    (r'\rightarrow', '→'), (r'\leftarrow', '←'), (r'\to', '→'),
    (r'\geq', '≥'), (r'\leq', '≤'), (r'\neq', '≠'), (r'\ne ', '≠'),
    (r'\ell', 'ℓ'), (r'\pi', 'π'), (r'\infty', '∞'),
    (r'\widehat', '^'), (r'\widetilde', '~'), (r'\simeq', '≃'),
    (r'\mid', '|'), (r'\mapsto', '↦'), (r'\cap', '∩'), (r'\otimes', '⊗'),
    (r'\subset', '⊂'), (r'\prod', '∏'), (r'\(', ''), (r'\)', ''),
    (r'\[', ''), (r'\]', ''), (r'\,', ''), (r'\!', ''), (r'\;', ''),
    (r'\ ', ' '), ('’', "'"), ('–', '-'), (chr(96) * 2, '“'), ("''", '”'),
)

def read(suffix):
    with (ROOT / f'{PFX}_{suffix}.tsv').open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def argument(s, start):
    """Return the contents and end offset of a balanced TeX argument."""
    level = 1
    for i in range(start + 1, len(s)):
        if s[i - 1] != '\\':
            level += (s[i] == '{') - (s[i] == '}')
        if not level:
            return s[start + 1:i], i + 1
    raise ValueError('Unbalanced argument at ' + str(start))

def plain(s):
    s = re.sub(r'(?m)^%[^\n]*', '', s)
    while m := WRAPPERS.search(s):
        arg, end = argument(s, m.end() - 1)
        value = arg.split('|')[0] if m[1] == 'unsure' else arg
        s = s[:m.start()] + value + s[end:]
    for before, after in EQUIVALENTS:
        s = s.replace(before, after)
    return re.sub(r'[\s{}]', '', unicodedata.normalize('NFC', s))

def versions(s):
    """With and without cancellations, since some blind entries quote just the live line."""
    live = s
    while m := re.search(r'\\deleted\{', live):
        _, end = argument(live, m.end() - 1)
        live = live[:m.start()] + live[end:]
    return plain(s), plain(live)

def contains(reading, texts):
    return all(any(plain(part) in text for text in texts) for part in reading.split(' ⟐ '))

def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def first_copy(delivered, edits):
    """Recover the first page file by applying the sparse, reversible revision records."""
    if not edits or digest(delivered) != edits[0]['delivered SHA-256']:
        raise ValueError('Wrong delivered page for the stored revision record')
    text = delivered
    for edit in sorted(edits, key=lambda z: int(z['delivered start']), reverse=True):
        start, end = int(edit['delivered start']), int(edit['delivered end'])
        if text[start:end] != json.loads(edit['delivered text (JSON)']):
            raise ValueError(f'Revision context differs at character {start}')
        text = text[:start] + json.loads(edit['first text (JSON)']) + text[end:]
    if digest(text) != edits[0]['first SHA-256']:
        raise ValueError('The reconstructed first page failed its hash check')
    return text

def table_row(values):
    return '| ' + ' | '.join(str(v).replace('|', r'\|').replace('\n', ' ') for v in values) + ' |'

def run():
    readings = read('blind')
    alignment = {(r['scan'], r['place']): r for r in read('blind_alignment')}
    revisions = defaultdict(list)
    for r in read('blind_revision'):
        revisions[r['scan']].append(r)
    assert {(r['scan'], r['place']) for r in readings} == set(alignment)
    versions_by_scan = {}
    for scan, changes in revisions.items():
        delivered = (ROOT / 'pages' / f'{PFX}_34_scan{int(scan):03d}.tex').read_text(encoding='utf-8')
        versions_by_scan[scan] = versions(first_copy(delivered, changes)), versions(delivered)
    assert len(versions_by_scan) == 15
    differences = []
    unresolved = []
    for r in readings:
        sc, place, observed = r['scan'], r['place'], r['what the crop shows']
        first, final = versions_by_scan[sc]
        a = alignment[sc, place]
        if not contains(a['final excerpt'], final):
            unresolved.append(f'Scan {sc}, {place}: final excerpt')
        if a['kind'] == 'agreement' and not (contains(observed, first) and contains(observed, final)):
            unresolved.append(f'Scan {sc}, {place}: first/final literal agreement')
        if a['kind'] == 'difference':
            differences.append((sc, place, observed, a['first page file'], a['ink decision'],
                                a['subsequent witness result'] or '—'))
    lines = [
        '# Independent readings and their resolution', '',
        f'{len(readings)} passages were entered from the images before the corresponding page files '
        f'were reopened. The table gives the {len(differences)} differences, including differences '
        'in the extent of a cancellation and readings where the ink removed an earlier alternative. '
        'The last column records later witness decisions that affect the same comparison.', '',
        'The companion script reconstructs all 15 first page files from the delivered text and the sparse '
        'revision table. It verifies both sets of hashes, searches quotations among the live and cancelled '
        'readings, and tests each final excerpt. The alignment table records the manual decisions about '
        'handwriting. A ⟐ separates quoted parts of one passage. Equivalent TeX spacing, typography '
        'and array layout do not constitute variant readings.', '',
        table_row(('Scan', 'Place', 'Independent reading', 'First page file', 'Decision on the ink', 'Later witness result')),
        '|---|---|---|---|---|---|',
        *(table_row(r) for r in differences), '',
        f'All 15 first versions reconstructed and verified. {len(readings)} sites compared. '
        f'{len(differences)} differences. {len(unresolved)} unlocated or inconsistent excerpts.',
    ]
    if unresolved:
        lines.extend(['', *('- ' + x for x in unresolved)])
    (ROOT / f'{PFX}_blind_compare.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return unresolved

if __name__ == '__main__':
    raise SystemExit(bool(run()))
