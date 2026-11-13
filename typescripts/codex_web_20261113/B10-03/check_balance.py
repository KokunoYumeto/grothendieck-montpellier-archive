#!/usr/bin/env python3
"""Check the supplied fragments without invoking a TeX engine."""
from pathlib import Path
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parent
TOKEN = re.compile(r'\\begin\{([^{}]+)\}|\\end\{([^{}]+)\}|\\[\[\]()]|\\.|[{}$]')

def check(path):
    text = path.read_text()
    source = re.sub(r'(?<!\\)%[^\n]*', '', text)
    braces, envs, math = [], [], []
    counts = {'brace_pairs': 0, 'dollars': 0, 'display_pairs': 0, 'environment_pairs': 0}
    for m in TOKEN.finditer(source):
        token = m.group()
        line = source.count('\n', 0, m.start()) + 1
        if m.group(1):
            envs.append((m.group(1), line))
        elif m.group(2):
            assert envs and envs[-1][0] == m.group(2), (path.name, line, 'environment mismatch', envs)
            envs.pop(); counts['environment_pairs'] += 1
        elif token == '{':
            braces.append(line)
        elif token == '}':
            assert braces, (path.name, line, 'extra closing brace')
            braces.pop(); counts['brace_pairs'] += 1
        elif token == '$':
            counts['dollars'] += 1
            if math and math[-1][0] == '$': math.pop()
            else:
                assert not math, (path.name, line, 'dollar inside other math delimiter')
                math.append(('$', line))
        elif token in (r'\[', r'\('):
            assert not math, (path.name, line, 'nested math delimiters')
            math.append((token, line))
        elif token in (r'\]', r'\)'):
            expected = r'\[' if token == r'\]' else r'\('
            assert math and math[-1][0] == expected, (path.name, line, 'math delimiter mismatch')
            math.pop()
            if token == r'\]': counts['display_pairs'] += 1
    assert not braces and not envs and not math, (path.name, braces, envs, math)
    return counts

def main():
    pages = [ROOT/f'pages/B10-03_10_scan{n:03}.tex' for n in range(51,59)]
    fragment = ROOT/'B10-03_transcription.tex'
    files = pages + [fragment, ROOT/'B10-03_standalone.tex']
    report = ['Structural balance check: PASS', 'No compilation attempted.', '']
    for path in files:
        counts = check(path)
        report.append(path.relative_to(ROOT).as_posix()+': PASS; '+', '.join(f'{k}={v}' for k,v in counts.items()))
    assembled = fragment.read_text()
    assert assembled == ''.join(p.read_text() for p in pages), 'Fragment differs from ordered concatenation'
    assert assembled.startswith('\\cotefile{10}\n\\scanpage{51}'), 'Incorrect fragment opening'
    assert assembled.count(r'\cotefile{') == 1, 'Cote macro repeated'
    assert re.findall(r'\\scanpage\{(\d+)\}',assembled) == [str(n) for n in range(51,59)], 'Page order'
    assert not re.search(r'\\(?:includegraphics|newcommand|renewcommand|def)\b',assembled), 'Embedded image or new macro in fragment'
    assert not re.search(r'\\illegible\{[^0-9}]',assembled), 'Unexpected illegible estimate'
    rows = list(csv.DictReader((ROOT/'B10-03_inventory.csv').open()))
    assert set(r['scan'] for r in rows) == set(str(n) for n in range(51,59)), 'Inventory scan coverage'
    assert all(r['transcribed'] == 'yes' for r in rows), 'Unfinished inventory row'
    report += ['', 'Ordered concatenation, page coverage, one cote marker, and inventory coverage: PASS',
               f'Inventory rows: {len(rows)}; all transcribed=yes.',
               'Counts below use the assembled fragment only; nested marks count separately.']
    for name in ['unsure','illegible','deleted']:
        count = len(re.findall(r'\\'+name+r'\{',assembled))
        report.append(f'\\{name}: {count}')
    report.append('Estimated words in illegible spans: '+str(sum(map(int,re.findall(r'\\illegible\{(\d+)\}',assembled)))))
    report += ['Unfinished scans: none.', '', 'Page and assembled SHA-256:']
    for path in pages+[fragment]:
        report.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.relative_to(ROOT).as_posix())
    result='\n'.join(report)+'\n'
    (ROOT/'balance_check.txt').write_text(result)
    print(result)

if __name__ == '__main__':
    main()
