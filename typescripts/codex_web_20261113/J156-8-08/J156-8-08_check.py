#!/usr/bin/env python3
"""Non-compiling structural checks for the returned transcription package."""
from pathlib import Path
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parent


def without_comments(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)


def check_tex(path):
    s = without_comments(path.read_text())
    braces, environments, displays, dollars, lefts = [], [], [], [], []
    token = re.compile(r'\\(?:begin|end)\{[^{}]+\}|\\\[|\\\]|\\left\b|\\right\b|\\[A-Za-z]+|\\.|[{}$]', re.S)
    for m in token.finditer(s):
        t = m.group()
        line = s.count('\n', 0, m.start()) + 1
        if t == '{': braces.append(line)
        elif t == '}':
            assert braces, f'{path.name}:{line}: extra closing brace'
            braces.pop()
        elif t.startswith('\\begin{'): environments.append((t[7:-1], line))
        elif t.startswith('\\end{'):
            assert environments and environments[-1][0] == t[5:-1], f'{path.name}:{line}: environment mismatch {t}'
            environments.pop()
        elif t == r'\[': displays.append(line)
        elif t == r'\]':
            assert displays, f'{path.name}:{line}: extra display close'
            displays.pop()
        elif t == '$':
            if dollars: dollars.pop()
            else: dollars.append(line)
        elif t == r'\left': lefts.append(line)
        elif t == r'\right':
            assert lefts, f'{path.name}:{line}: extra right delimiter'
            lefts.pop()
    assert not (braces or environments or displays or dollars or lefts), (path.name,braces,environments,displays,dollars,lefts)
    print(f'PASS {path.name}: braces, display delimiters, dollar pairs, environments, left/right delimiters')


pages = sorted((ROOT / 'pages').glob('J156-8-08_156-8_scan*.tex'))
assert len(pages) == 8
for scan, page in zip(range(58,66), pages):
    source = page.read_text()
    assert page.name.endswith(f'scan{scan:03}.tex')
    assert source.startswith(f'\\scanpage{{{scan}}}\n\\mspage{{{scan-9}}}\n')
    assert f'% archive sheet number: {scan}' in source
    assert not re.search(r'\\(?:newcommand|renewcommand|def|includegraphics|handwritten)\b', source)
    check_tex(page)

fragment = ROOT / 'J156-8-08_transcription.tex'
text = fragment.read_text()
assert text == '\\cotefile{156-8}\n' + ''.join(p.read_text() for p in pages)
assert text.count('\\cotefile{') == 1
assert '\\documentclass' not in text
check_tex(fragment)
check_tex(ROOT / 'J156-8-08_standalone.tex')

with (ROOT / 'J156-8-08_inventory.csv').open(newline='') as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
    inventory = list(reader)
assert {r['scan'] for r in inventory} == {str(n) for n in range(58,66)}
assert all(r['transcribed']=='yes' and r['cote']=='156-8' for r in inventory)
assert len({r['element'] for r in inventory}) == len(inventory)

counts = Counter(re.findall(r'\\(unsure|illegible|deleted|inserted|diagram|figure|margin)\{', without_comments(text)))
for key in ('unsure','illegible','deleted','inserted','diagram','figure','margin'):
    print(f'{key}: {counts[key]}')
print(f'Inventory: {len(inventory)} rows, all transcribed=yes; scans 58–65 present.')
print('Assembled fragment equals the eight page files in order, prefixed by exactly one cotefile marker.')
print('No LaTeX compilation was attempted. These checks establish structural balance, not typeset layout or reading accuracy.')
