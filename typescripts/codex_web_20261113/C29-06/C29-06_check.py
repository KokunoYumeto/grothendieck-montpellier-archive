#!/usr/bin/env python3
"""Check delimiter/environment balance without running a TeX engine."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent


def check(path):
    s = path.read_text()
    braces = []
    envs = []
    math = None
    counts = {'braces': 0, 'inline_math': 0, 'display_math': 0, 'environments': 0}
    errors = []
    i = 0
    while i < len(s):
        c = s[i]
        line = s.count('\n', 0, i) + 1
        if c == '%':
            j = s.find('\n', i)
            i = len(s) if j < 0 else j + 1
            continue
        if c == '\\':
            m = re.match(r'\\(begin|end)\{([^{}]+)\}', s[i:])
            if m:
                action, name = m.groups()
                if action == 'begin':
                    envs.append((name, line)); counts['environments'] += 1
                elif not envs or envs[-1][0] != name:
                    errors.append(f'line {line}: unmatched end {name}')
                else:
                    envs.pop()
                i += len(m[0]); continue
            token = s[i:i+2]
            if token in (r'\[', r'\('):
                if math is not None:
                    errors.append(f'line {line}: nested math opener {token}')
                math = (token, line)
                counts['display_math' if token == r'\[' else 'inline_math'] += 1
                i += 2; continue
            if token in (r'\]', r'\)'):
                wanted = r'\[' if token == r'\]' else r'\('
                if math is None or math[0] != wanted:
                    errors.append(f'line {line}: unmatched math closer {token}')
                math = None; i += 2; continue
            if i+1 < len(s) and not s[i+1].isalpha():
                i += 2; continue  # escaped brace, percent, dollar, &, or line break
            m = re.match(r'\\[A-Za-z]+', s[i:])
            i += len(m[0]) if m else 1
            continue
        if c == '{':
            braces.append(line); counts['braces'] += 1
        elif c == '}':
            if braces: braces.pop()
            else: errors.append(f'line {line}: unmatched closing brace')
        elif c == '$':
            if math is None:
                math = ('$', line); counts['inline_math'] += 1
            elif math[0] == '$':
                math = None
            else:
                errors.append(f'line {line}: dollar inside {math[0]} math')
        i += 1
    if braces: errors.append(f'unclosed braces opened on lines {braces}')
    if envs: errors.append(f'unclosed environments {envs}')
    if math: errors.append(f'unclosed math {math}')
    return counts, errors


def main():
    paths = sorted((ROOT/'pages').glob('C29-06_29_scan*.tex'))
    paths += [ROOT/'C29-06_transcription.tex', ROOT/'C29-06_standalone.tex']
    failed = False
    for path in paths:
        counts, errors = check(path)
        print(f'{path.relative_to(ROOT)}: {"FAIL" if errors else "PASS"}; {counts}')
        for error in errors: print('  '+error)
        failed |= bool(errors)
    print('No compilation attempted. This is a delimiter/environment check, not a TeX rendering test.')
    return int(failed)


if __name__ == '__main__':
    sys.exit(main())
