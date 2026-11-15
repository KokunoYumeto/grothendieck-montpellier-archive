#!/usr/bin/env python3
"""Lexical LaTeX balance check only; does not invoke a TeX engine."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding='utf-8')
    braces, environments, errors = [], [], []
    math = None
    counts = {'braces': 0, 'displays': 0, 'inline_pairs': 0, 'environments': 0}
    line, i = 1, 0
    while i < len(source):
        c = source[i]
        if c == '\n':
            line += 1
        if c == '%':
            j = source.find('\n', i)
            i = len(source) if j < 0 else j
            continue
        if c == '\\':
            m = re.match(r'\\(begin|end)\s*\{([^}]+)\}', source[i:])
            if m:
                action, name = m.groups()
                if action == 'begin':
                    environments.append((name, line))
                    counts['environments'] += 1
                elif not environments or environments[-1][0] != name:
                    errors.append(f'line {line}: unmatched end {{{name}}}')
                else:
                    environments.pop()
            command = re.match(r'\\(?:[A-Za-z@]+|.)', source[i:])
            token = command.group() if command else '\\'
            if token in (r'\[', r'\('):
                if math is not None:
                    errors.append(f'line {line}: nested math opening {token}')
                math = (token, line)
            elif token in (r'\]', r'\)'):
                expected = r'\[' if token == r'\]' else r'\('
                if math is None or math[0] != expected:
                    errors.append(f'line {line}: unmatched math closing {token}')
                else:
                    counts['displays' if token == r'\]' else 'inline_pairs'] += 1
                math = None
            i += len(token)
            continue
        if c == '{':
            braces.append(line)
            counts['braces'] += 1
        elif c == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'line {line}: unmatched closing brace')
        elif c == '$':
            if math is None:
                math = ('$', line)
            elif math[0] == '$':
                counts['inline_pairs'] += 1
                math = None
            else:
                errors.append(f'line {line}: dollar inside {math[0]} math')
        i += 1
    errors += [f'line {n}: unclosed brace' for n in braces]
    errors += [f'line {n}: unclosed environment {name}' for name, n in environments]
    if math is not None:
        errors.append(f'line {math[1]}: unclosed math {math[0]}')
    return errors, counts


root = Path(__file__).resolve().parent
files = sorted((root / 'pages').glob('*.tex')) + [
    root / 'J156-9-12_transcription.tex', root / 'J156-9-12_standalone.tex']
failed = False
for path in files:
    errors, counts = check(path)
    failed |= bool(errors)
    print(f'{path.relative_to(root)}: {"FAIL" if errors else "PASS"}; {counts}')
    for error in errors:
        print('  ' + error)
print('Lexical braces, display/inline math delimiters, and environment checks only.')
print('No LaTeX compilation attempted. Ordinary mathematical parentheses are not repaired.')
sys.exit(1 if failed else 0)
