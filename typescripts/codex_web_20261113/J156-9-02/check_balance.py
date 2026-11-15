#!/usr/bin/env python3
"""Lexical checks only. Does not invoke TeX or expand macros."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def uncomment(text):
    return '\n'.join(re.split(r'(?<!\\)%', line, maxsplit=1)[0]
                     for line in text.splitlines())

def check(path):
    text = uncomment(path.read_text())
    braces, envs, errors = [], [], []
    dollars = False
    display = False
    i = 0
    while i < len(text):
        ch = text[i]
        line = text.count('\n', 0, i) + 1
        if ch == '\\':
            env = re.match(r'\\(begin|end)\{([^}]+)\}', text[i:])
            if env:
                action, name = env.groups()
                if action == 'begin':
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f'line {line}: mismatched end {{{name}}}')
                else:
                    envs.pop()
                i += len(env[0]); continue
            if i+1 < len(text):
                nxt = text[i+1]
                if nxt == '[':
                    if display or dollars:
                        errors.append(f'line {line}: nested display opener')
                    display = True
                elif nxt == ']':
                    if not display:
                        errors.append(f'line {line}: display close without open')
                    display = False
                if not nxt.isalpha():
                    i += 2; continue
            i += 1; continue
        if ch == '{': braces.append(line)
        elif ch == '}':
            if braces: braces.pop()
            else: errors.append(f'line {line}: unmatched closing brace')
        elif ch == '$':
            if display: errors.append(f'line {line}: dollar inside display')
            dollars = not dollars
        i += 1
    if braces: errors.append(f'unclosed braces from lines {braces}')
    if envs: errors.append(f'unclosed environments {envs}')
    if dollars: errors.append('unclosed dollar math')
    if display: errors.append('unclosed display math')
    return errors

if __name__ == '__main__':
    paths = sorted((ROOT/'pages').glob('*.tex'))
    paths += [ROOT/'J156-9-02_transcription.tex', ROOT/'J156-9-02_standalone.tex']
    failures = 0
    for path in paths:
        errors = check(path)
        print(('FAIL' if errors else 'PASS') + ' ' + str(path.relative_to(ROOT)))
        for error in errors: print('  ' + error)
        failures += bool(errors)
    print(f'{len(paths)} files checked; {failures} failed.')
    print('Checks: braces, display delimiters, paired dollars, nested environments.')
    print('No TeX engine invoked; no compilation or macro expansion performed.')
    sys.exit(bool(failures))
