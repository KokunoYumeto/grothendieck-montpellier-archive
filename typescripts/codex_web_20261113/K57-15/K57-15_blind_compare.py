"""Compare independent crop readings with the first saved text and today's page files."""
from pathlib import Path
import csv
import json
import re
import unicodedata
import zlib
import base64

ROOT = Path(__file__).resolve().parent
TAG = "K57-15"
def flatten(source):
    """Ignore source typography, not letter case, alphabet, or the count of stops."""
    wrappers = r'handwritten|inserted|deleted|uline|uuline|operatorname|text|textnormal|mspage|margin'
    source = re.sub(r'\\(?:longrightarrow|rightarrow)\b', r'\\to ', source)
    source = re.sub(r'\\illegible\{\d+\}', '〈unread〉', source)
    while True:
        last = source
        source = re.sub(r'\\unsure\{((?:[^{}]|\{[^{}]*\})*)\}',
                        lambda m: m[1].split('|')[0], source)
        source = re.sub(r'\\(?:'+wrappers+r')\{((?:[^{}]|\{[^{}]*\})*)\}', r'\1', source)
        if source == last:
            break
    for char, accent in [("'", "\u0301"), (chr(96), "\u0300")]:
        source = re.sub(re.escape(chr(92)+char)+r'\{?([A-Za-z])\}?',
                        lambda m: unicodedata.normalize("NFC", m[1]+accent), source)
    source = re.sub(r'\\(?:lvert|rvert)\b', '|', source)
    source = re.sub(r'\\(?:longrightarrow|rightarrow)\b', r'\\to', source)
    source = re.sub(r'\\leq\b', r'\\le', source)
    source = re.sub(r'\\geq\b', r'\\ge', source)
    source = re.sub(r'\\ldots\b', '...', source)
    return re.sub(r'\\[,\s]|\\\\|[\s\${}]', '', source)

def cell(s):
    return s.replace('|', r'\|').replace('\n', ' ').replace(chr(96), '′')

def main():
    audit = (ROOT / (TAG + '_audit.md')).read_text()
    data = re.search(r'<!-- baseline-v1\n([A-Za-z0-9+/=\n]+)\n-->', audit).group(1)
    ledger = json.loads(zlib.decompress(base64.b64decode(data)))
    with (ROOT / (TAG + '_blind.tsv')).open() as handle:
        blind = list(csv.DictReader(handle, delimiter='\t'))
    if len(ledger) != len(blind):
        raise ValueError('The baseline and blind file do not have the same number of entries.')
    result = []
    same = 0
    for row, (n, place, pos, raw, decision) in zip(blind, ledger):
        if (int(row['scan']), row['place']) != (n, place):
            raise ValueError((row['scan'], place))
        bounds = [int(v) for v in pos.split('-')]
        page = (ROOT / 'pages' / f'{TAG}_57_scan{n}.tex').read_text().splitlines()
        source = '\n'.join(page[bounds[0]-1:bounds[-1]])
        blind_text = row['what_the_crop_shows']
        key, first, now = map(flatten, (blind_text, raw, source))
        if key in first and key in now and not decision:
            same += 1
            continue
        fn = lambda item: 'substring present' if key in item else 'differs'
        result.append((n, place, pos, blind_text, fn(first), fn(now), decision))
    lines = ['# Independent readings compared with saved page files', '',
             f'{len(blind)} independently recorded crop readings. {same} have a local match in both page states without a separate editorial decision. The table gives the remaining {len(result)}. A listed row can be a difference in notation or attachment, even if the word itself agrees.', '',
             'The comparison uses the lines indicated in the audit, with the first candidate of each doubt. It preserves alphabet commands, case, literal dots and indices. The status columns report literal substring presence after these limited normalisations. The decision identifies the relevant glyph or word when a line contains similar objects at different positions. The baseline embedded in the audit preserves the original local lines, so rerunning this script on a witness-adjusted copy also compares its current text.', '',
             '| Scan | Hard place | Page-file line(s) | Blind reading | First saved text | Current page | Decision on the crop |', '|---:|---|---|---|---|---|---|']
    for n, place, pos, ink, before, after, disposition in result:
        lines.append('| '+' | '.join(map(cell, [str(n),place,pos,ink,before,after,disposition or 'Local difference requires review.']))+' |')
    (ROOT / (TAG + '_blind_compare.md')).write_text('\n'.join(lines)+'\n')
    print(f'{len(blind)} entries, {len(result)} reported.')

if __name__ == '__main__':
    main()

