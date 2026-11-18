#!/usr/bin/env python3
"""Check transcription delimiters without compiling or changing any reading."""
from pathlib import Path
import json
import re


def check(path):
    text = path.read_text(encoding='utf-8')
    braces, displays, envs, errors = [], [], [], []
    dollar = None
    i, line = 0, 1
    while i < len(text):
        c = text[i]
        if c == '\n':
            line += 1
            i += 1
            continue
        if c == '%':
            end = text.find('\n', i)
            i = len(text) if end == -1 else end
            continue
        if c == '\\':
            m = re.match(r'\\(begin|end)\{([^{}]+)\}', text[i:])
            if m:
                kind, name = m.groups()
                if kind == 'begin':
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f'L{line}: unmatched end {name}; stack={envs}')
                else:
                    envs.pop()
                i += len(m.group())
                continue
            if i + 1 < len(text) and text[i + 1] == '[':
                if displays:
                    errors.append(f'L{line}: nested display opener')
                if dollar is not None:
                    errors.append(f'L{line}: display opened inside dollar math')
                displays.append(line)
                i += 2
                continue
            if i + 1 < len(text) and text[i + 1] == ']':
                if not displays:
                    errors.append(f'L{line}: unmatched display closer')
                else:
                    displays.pop()
                i += 2
                continue
            # A control symbol consumes exactly one following character. A control
            # word consumes letters only; braces following it remain significant.
            m = re.match(r'\\[A-Za-z]+', text[i:])
            i += len(m.group()) if m else 2
            continue
        if c == '{':
            braces.append(line)
        elif c == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'L{line}: unmatched closing brace')
        elif c == '$':
            if displays:
                errors.append(f'L{line}: dollar delimiter inside display math')
            dollar = line if dollar is None else None
        i += 1
    if braces:
        errors.append(f'unclosed braces opened at {braces}')
    if displays:
        errors.append(f'unclosed display(s) opened at {displays}')
    if dollar is not None:
        errors.append(f'unclosed dollar math opened at L{dollar}')
    if envs:
        errors.append(f'unclosed environments {envs}')
    return {'file': str(path), 'ok': not errors, 'errors': errors}


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    files = sorted((root / 'pages').glob('*.tex')) + [root / 'K34-08_transcription.tex', root / 'K34-08_standalone.tex']
    results = [check(p) for p in files]
    print(json.dumps({'compilation_attempted': False, 'ok': all(r['ok'] for r in results), 'results': results}, indent=2))
    raise SystemExit(0 if all(r['ok'] for r in results) else 1)
