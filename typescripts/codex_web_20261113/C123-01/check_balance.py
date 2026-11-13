#!/usr/bin/env python3
"""Check only LaTeX delimiter structure; never compile or amend readings."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def escaped(s, i):
    j = i - 1
    while j >= 0 and s[j] == '\\':
        j -= 1
    return (i - j - 1) % 2 == 1

def without_comments(s):
    lines = []
    for line in s.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char == '%' and not escaped(line, i):
                line = line[:i] + '\n'
                break
        lines.append(line)
    return ''.join(lines)

def check(path):
    s = without_comments(path.read_text())
    braces, environments, math, errors = [], [], None, []
    for i, char in enumerate(s):
        if char in '{}' and not escaped(s, i):
            if char == '{':
                braces.append(i)
            elif braces:
                braces.pop()
            else:
                errors.append(f'unmatched closing brace at {i}')
    if braces:
        errors.append(f'{len(braces)} unclosed braces')
    token_pattern = r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\[|\\\]|\$'
    for match in re.finditer(token_pattern, s):
        if escaped(s, match.start()):
            continue
        token = match.group()
        if match.group(1):
            environments.append(match.group(1))
        elif match.group(2):
            env = match.group(2)
            if not environments or environments.pop() != env:
                errors.append(f'environment mismatch: {env}')
        elif token == r'\[':
            if math is not None:
                errors.append('display opened inside math')
            math = 'display'
        elif token == r'\]':
            if math != 'display':
                errors.append('display close without display open')
            math = None
        elif token == '$':
            if math == 'display':
                errors.append('dollar inside display')
            else:
                math = None if math == 'inline' else 'inline'
    if environments:
        errors.append('unclosed environments: ' + ', '.join(environments))
    if math:
        errors.append('unclosed ' + math + ' math')
    return errors

paths = sorted((ROOT / 'pages').glob('*.tex')) + [ROOT / 'C123-01_transcription.tex', ROOT / 'C123-01_standalone.tex']
failed = False
for path in paths:
    errors = check(path)
    failed |= bool(errors)
    print(f'{path.relative_to(ROOT)}: ' + ('FAIL: ' + '; '.join(errors) if errors else 'PASS — braces, display delimiters, dollars, environments'))
print('No LaTeX compilation was attempted. Mathematical correctness and source punctuation are not tested.')
sys.exit(1 if failed else 0)
