#!/usr/bin/env python3
"""Lexical balance check only; never invokes TeX or changes a reading."""
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent

def uncomment(source):
    lines = []
    for line in source.splitlines():
        for i, c in enumerate(line):
            if c == '%' and (len(line[:i]) - len(line[:i].rstrip('\\'))) % 2 == 0:
                line = line[:i]
                break
        lines.append(line)
    return '\n'.join(lines)

def check(path):
    s = uncomment(path.read_text())
    errors, braces, envs, math, scalable = [], [], [], [], []
    tokens = re.compile(r'\\(?:begin|end)\{[^{}]+\}|\\(?:left|right)(?![A-Za-z])|\\[A-Za-z]+|\\[^\n]|[{}$]')
    for match in tokens.finditer(s):
        t = match.group()
        line = s.count('\n', 0, match.start()) + 1
        if t == '{':
            braces.append(line)
        elif t == '}':
            if braces: braces.pop()
            else: errors.append(f'line {line}: excess closing group brace')
        elif t.startswith('\\begin{'):
            envs.append((t[7:-1], line))
        elif t.startswith('\\end{'):
            name = t[5:-1]
            if not envs or envs[-1][0] != name:
                errors.append(f'line {line}: unexpected end of {name}')
            else: envs.pop()
        elif t in ('\\[', '\\('):
            if math: errors.append(f'line {line}: nested explicit math delimiter {t}')
            math.append((t, line))
        elif t in ('\\]', '\\)'):
            expected = '\\[' if t == '\\]' else '\\('
            if not math or math[-1][0] != expected:
                errors.append(f'line {line}: unexpected math closer {t}')
            else: math.pop()
        elif t == '$':
            if math and math[-1][0] == '$': math.pop()
            elif math: errors.append(f'line {line}: dollar inside explicit math delimiters')
            else: math.append(('$', line))
        elif t == '\\left':
            scalable.append(line)
        elif t == '\\right':
            if scalable: scalable.pop()
            else: errors.append(f'line {line}: right without left')
    errors += [f'line {n}: unclosed group brace' for n in braces]
    errors += [f'line {n}: unclosed environment {e}' for e, n in envs]
    errors += [f'line {n}: unclosed math delimiter {m}' for m, n in math]
    errors += [f'line {n}: left without right' for n in scalable]
    return errors

paths = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else (
    sorted((BASE / 'pages').glob('*.tex')) +
    [BASE / 'J156-8-15_transcription.tex', BASE / 'J156-8-15_standalone.tex']
)
failed = False
for path in paths:
    errors = check(path)
    print(('FAIL' if errors else 'PASS') + ': ' + path.name)
    for error in errors: print('  ' + error)
    failed |= bool(errors)
print('Checks: grouping braces; display/inline math delimiters; environments; left/right pairs.')
print('Escaped source braces are printed delimiters, not TeX grouping braces.')
print('This is not compilation and does not certify rendering or mathematical correctness.')
sys.exit(1 if failed else 0)
