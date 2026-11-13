#!/usr/bin/env python3
"""Lexical balance checks only. This script does not compile LaTeX."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def escaped(text, pos):
    n = 0
    while pos > 0 and text[pos - 1] == '\\':
        n += 1
        pos -= 1
    return n % 2 == 1

def without_comments(text):
    lines = []
    for line in text.splitlines():
        for i, ch in enumerate(line):
            if ch == '%' and not escaped(line, i):
                line = line[:i]
                break
        lines.append(line)
    return '\n'.join(lines)

def check(path):
    text = without_comments(path.read_text(encoding='utf-8'))
    errors, braces, display, envs = [], [], [], []
    dollars = 0
    for i, ch in enumerate(text):
        if ch in '{}$' and not escaped(text, i):
            if ch == '{':
                braces.append(i)
            elif ch == '}':
                if braces:
                    braces.pop()
                else:
                    errors.append('unmatched closing brace')
            else:
                dollars += 1
    if braces:
        errors.append(f'{len(braces)} unclosed braces')
    if dollars % 2:
        errors.append('odd number of inline dollar delimiters')
    for m in re.finditer(r'\\([\[\]])', text):
        if escaped(text, m.start()):
            continue
        if m.group(1) == '[':
            if display:
                errors.append('nested display opener')
            display.append(m.start())
        elif display:
            display.pop()
        else:
            errors.append('unmatched display closer')
    if display:
        errors.append('unclosed display delimiter')
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', text):
        action, name = m.groups()
        if action == 'begin':
            envs.append(name)
        elif not envs or envs.pop() != name:
            errors.append(f'mismatched environment end: {name}')
    if envs:
        errors.append('unclosed environments: ' + ', '.join(envs))
    return errors

def main():
    paths = sorted((ROOT / 'pages').glob('*.tex')) + [
        ROOT / 'B10-08_transcription.tex',
        ROOT / 'B10-08_standalone.tex',
        ROOT / 'PREAMBLE.tex',
    ]
    failed = False
    for path in paths:
        errors = check(path)
        failed |= bool(errors)
        print(f'{path.relative_to(ROOT)}: ' + ('FAIL: ' + '; '.join(errors) if errors else 'PASS'))
    print('Checks: braces, display delimiters, inline dollar parity, nested environments. No compilation.')
    return int(failed)

if __name__ == '__main__':
    raise SystemExit(main())
