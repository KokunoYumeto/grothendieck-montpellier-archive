#!/usr/bin/env python3
"""Static LaTeX delimiter checks only. This script never runs a TeX engine."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def uncomment(source):
    lines = []
    for line in source.splitlines():
        i = 0
        while i < len(line):
            if line[i] == '\\':
                i += 2
                continue
            if line[i] == '%':
                line = line[:i]
                break
            i += 1
        lines.append(line)
    return '\n'.join(lines)

def check(path):
    source = uncomment(path.read_text())
    braces = []
    envs = []
    display = []
    dollars = []
    errors = []
    counts = dict(groups=0, displays=0, inline_math=0, environments=0)
    token = re.compile(r'\\(?:begin|end)\{[^}]+\}|\\[\s\S]|[{}$]')
    for m in token.finditer(source):
        value = m[0]
        line = source[:m.start()].count('\n') + 1
        if value.startswith('\\begin{'):
            envs.append((value[7:-1],line)); counts['environments'] += 1
        elif value.startswith('\\end{'):
            name = value[5:-1]
            if not envs or envs[-1][0] != name:
                errors.append(f'l.{line}: unmatched end {name}')
            else:
                envs.pop()
        elif value == '{':
            braces.append(line); counts['groups'] += 1
        elif value == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'l.{line}: unmatched closing brace')
        elif value == r'\[':
            if display:
                errors.append(f'l.{line}: nested display opener')
            display.append(line); counts['displays'] += 1
        elif value == r'\]':
            if display:
                display.pop()
            else:
                errors.append(f'l.{line}: unmatched display closer')
        elif value == '$':
            if dollars:
                dollars.pop()
            else:
                dollars.append(line); counts['inline_math'] += 1
    if braces: errors.append('unclosed braces at '+str(braces))
    if envs: errors.append('unclosed environments '+str(envs))
    if display: errors.append('unclosed displays at '+str(display))
    if dollars: errors.append('unpaired dollar at '+str(dollars))
    return errors, counts

def main():
    pages = sorted((ROOT/'pages').glob('*.tex'))
    files = pages + [ROOT/'J156-8-05_transcription.tex', ROOT/'J156-8-05_standalone.tex']
    failures = 0
    print('Static balance check; no compilation performed.')
    for path in files:
        errors,counts = check(path)
        failures += bool(errors)
        print(f'{path.relative_to(ROOT)}: '+('FAIL' if errors else 'PASS')+' '+str(counts))
        for error in errors:
            print('  '+error)
    print(f'{len(files)} files checked; {failures} failures.')
    return bool(failures)

if __name__ == '__main__':
    sys.exit(main())
