#!/usr/bin/env python3
"""Lexical LaTeX balance checks only; does not invoke a TeX engine."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding='utf-8')
    braces, environments, math, errors = [], [], [], []
    counts = {'brace_pairs': 0, 'dollar_pairs': 0, 'display_pairs': 0, 'environment_pairs': 0}
    i = 0
    def line(pos):
        return source.count('\n', 0, pos) + 1
    def error(message, pos):
        errors.append(f'line {line(pos)}: {message}')
    while i < len(source):
        char = source[i]
        if char == '%':
            end = source.find('\n', i)
            i = len(source) if end < 0 else end + 1
            continue
        if char == '\\':
            if i + 1 >= len(source):
                error('terminal backslash', i)
                break
            nxt = source[i + 1]
            if nxt in '[]()':
                token = source[i:i+2]
                opening = {'\\[': '\\]', '\\(': '\\)'}
                if token in opening:
                    if math:
                        error('nested mathematical delimiter ' + token, i)
                    math.append((opening[token], i))
                elif not math or math[-1][0] != token:
                    error('unmatched mathematical delimiter ' + token, i)
                else:
                    math.pop()
                    if token == '\\]':
                        counts['display_pairs'] += 1
                i += 2
                continue
            if nxt.isalpha() or nxt == '@':
                match = re.match(r'\\([A-Za-z@]+)', source[i:])
                command = match.group(1)
                if command in ('begin', 'end'):
                    name = re.match(r'\s*\{([^{}]+)\}', source[i+len(match.group(0)):])
                    if not name:
                        error('missing environment name', i)
                    elif command == 'begin':
                        environments.append((name.group(1), i))
                    elif not environments or environments[-1][0] != name.group(1):
                        error('unmatched end of ' + name.group(1), i)
                    else:
                        environments.pop()
                        counts['environment_pairs'] += 1
                i += len(match.group(0))
                continue
            # Escaped braces, %, $, linebreak \\, and other control symbols.
            i += 2
            continue
        if char == '{':
            braces.append(i)
        elif char == '}':
            if not braces:
                error('unmatched closing brace', i)
            else:
                braces.pop()
                counts['brace_pairs'] += 1
        elif char == '$':
            token = '$$' if source[i:i+2] == '$$' else '$'
            if math and math[-1][0] == token:
                math.pop()
                counts['dollar_pairs'] += 1
            elif math:
                error('mixed/nested dollar delimiter', i)
            else:
                math.append((token, i))
            i += len(token)
            continue
        i += 1
    for pos in braces:
        error('unclosed brace', pos)
    for name, pos in environments:
        error('unclosed environment ' + name, pos)
    for delimiter, pos in math:
        error('unclosed math; expected ' + delimiter, pos)
    return counts, errors


def main():
    root = Path(__file__).resolve().parent
    targets = [Path(x) for x in sys.argv[1:]] or [
        *sorted((root / 'pages').glob('*.tex')),
        root / 'C123-02_transcription.tex',
        root / 'C123-02_standalone.tex',
    ]
    failed = False
    for path in targets:
        counts, errors = check(path)
        print(('FAIL' if errors else 'PASS') + ' ' + path.name + ': ' + ', '.join(f'{k}={v}' for k, v in counts.items()))
        for item in errors:
            print('  ' + item)
        failed |= bool(errors)
    print('No compilation attempted. This checks lexical delimiter/environment balance, not rendering.')
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
