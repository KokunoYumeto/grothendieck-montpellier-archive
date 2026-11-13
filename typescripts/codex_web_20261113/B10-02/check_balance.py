#!/usr/bin/env python3
"""Static delimiter checks only. Does not invoke TeX or alter readings."""
from pathlib import Path
import csv
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parent

def without_comments(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)

def check(path):
    text = without_comments(path.read_text(encoding='utf-8'))
    errors, braces, math = [], [], None
    for m in re.finditer(r'\\(?:[A-Za-z]+|.)|[{}$]', text):
        token = m.group()
        line = text.count('\n', 0, m.start()) + 1
        if token == '{':
            braces.append(line)
        elif token == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'line {line}: unmatched closing brace')
        elif token == '$':
            if math is None:
                math = ('inline', line)
            elif math[0] == 'inline':
                math = None
            else:
                errors.append(f'line {line}: dollar inside display')
        elif token == r'\[':
            if math is not None:
                errors.append(f'line {line}: display opened inside {math[0]}')
            math = ('display', line)
        elif token == r'\]':
            if math is None or math[0] != 'display':
                errors.append(f'line {line}: unmatched display close')
            math = None
    errors.extend(f'line {line}: unclosed brace' for line in braces)
    if math:
        errors.append(f'line {math[1]}: unclosed {math[0]} math')
    envs = []
    for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}', text):
        action, env = m.groups()
        if action == 'begin':
            envs.append(env)
        elif not envs or envs.pop() != env:
            errors.append(f'environment mismatch at {m.group()}')
    errors.extend(f'unclosed environment {env}' for env in envs)
    for m in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}', text, re.S):
        if '[ampersand replacement=\\&]' not in m.group():
            errors.append('tikzcd lacks required ampersand replacement')
        if re.search(r'(?<!\\)&', m.group()):
            errors.append('unescaped ampersand in tikzcd')
    if path.name != 'B10-02_standalone.tex' and re.search(r'\\(?:newcommand|renewcommand|def|documentclass|includegraphics)\b', text):
        errors.append('unexpected definition, document class or included image')
    return errors

pages = [ROOT / 'pages' / f'B10-02_10_scan{n:03}.tex' for n in range(42, 51)]
files = pages + [ROOT / 'B10-02_transcription.tex', ROOT / 'B10-02_standalone.tex']
lines, failed = [], False
for path in files:
    errors = check(path)
    failed |= bool(errors)
    lines.append(f'{path.relative_to(ROOT)}: ' + ('FAIL: ' + '; '.join(errors) if errors else 'PASS'))
assembled = (ROOT / 'B10-02_transcription.tex').read_text()
expected = '\n'.join(p.read_text().rstrip() for p in pages) + '\n'
assert assembled == expected, 'assembly differs from ordered page files'
assert assembled.startswith('\\cotefile{10}\n\\scanpage{42}\n')
assert assembled.count('\\cotefile{') == 1
assert re.findall(r'\\scanpage\{(\d+)\}', assembled) == [str(n) for n in range(42, 51)]
rows = list(csv.DictReader((ROOT / 'B10-02_inventory.csv').open()))
assert all(r['transcribed'] == 'yes' for r in rows)
assert len({r['element'] for r in rows}) == len(rows)
assert {int(r['scan']) for r in rows} == set(range(42, 51))
lines += ['Ordered assembly: PASS', f'Inventory: PASS ({len(rows)} rows; all yes)', 'No compilation attempted.', 'Literal parentheses are not balanced by this checker: the source includes truncated and cancelled expressions.']
for name in ('unsure', 'illegible', 'deleted'):
    lines.append(f'\\{name} marks in assembled fragment: {assembled.count(chr(92) + name + chr(123))}')
report = '\n'.join(lines) + '\n'
(ROOT / 'B10-02_balance_check.txt').write_text(report)
print(report)
sys.exit(1 if failed else 0)
