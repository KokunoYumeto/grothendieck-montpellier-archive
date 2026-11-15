#!/usr/bin/env python3
"""Lexical LaTeX balance checks only; this script does not compile TeX.

Escaped braces/dollars and comments do not count as delimiters. Literal
parentheses/brackets in the manuscript may intentionally remain unmatched.
"""
from pathlib import Path
import re
import sys

TOKEN = re.compile(
    r'%[^\n]*|\\begin\{([^{}]+)\}|\\end\{([^{}]+)\}'
    r'|\\\[|\\\]|\\\(|\\\)|\\[A-Za-z]+|\\.|[{}$]', re.S
)

def check(path):
    source = path.read_text(encoding='utf-8')
    braces, envs, math = [], [], []
    counts = dict(braces=0, displays=0, dollars=0, environments=0)
    errors = []
    for token in TOKEN.finditer(source):
        value = token.group(0)
        line = source.count('\n', 0, token.start()) + 1
        if value.startswith('%'):
            continue
        if token.group(1):
            envs.append((token.group(1), line))
            counts['environments'] += 1
        elif token.group(2):
            if not envs or envs[-1][0] != token.group(2):
                errors.append(f'line {line}: mismatched environment {value}')
            else:
                envs.pop()
        elif value == '{':
            braces.append(line)
            counts['braces'] += 1
        elif value == '}':
            if not braces:
                errors.append(f'line {line}: unmatched closing brace')
            else:
                braces.pop()
        elif value in (r'\[', r'\('):
            math.append((value, line))
            if value == r'\[':
                counts['displays'] += 1
        elif value in (r'\]', r'\)'):
            expected = {r'\]': r'\[', r'\)': r'\('}[value]
            if not math or math[-1][0] != expected:
                errors.append(f'line {line}: mismatched math delimiter {value}')
            else:
                math.pop()
        elif value == '$':
            counts['dollars'] += 1
            if math and math[-1][0] == '$':
                math.pop()
            else:
                math.append(('$', line))
    if braces:
        errors.append(f'unclosed braces opened at lines {braces}')
    if envs:
        errors.append(f'unclosed environments {envs}')
    if math:
        errors.append(f'unclosed math delimiters {math}')
    details = ', '.join(f'{k}={v}' for k, v in counts.items())
    return errors, f'{path.name}: {"FAIL" if errors else "PASS"} ({details})'

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    paths = sorted((root / 'pages').glob('*.tex'))
    paths += [root / 'J156-8-16_transcription.tex',
              root / 'J156-8-16_standalone.tex']
    failures = []
    for path in paths:
        errors, result = check(path)
        print(result)
        failures.extend(f'{path.name}: {e}' for e in errors)
    for failure in failures:
        print(failure)
    print('No compilation attempted. This is a delimiter/environment check, not a TeX rendering test.')
    sys.exit(bool(failures))
