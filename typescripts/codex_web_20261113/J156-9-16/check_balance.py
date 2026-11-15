#!/usr/bin/env python3
"""Structural checks only: this script never invokes a TeX compiler."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def check(path):
    source = path.read_text()
    braces = []
    environments = []
    math = None
    at = 0
    while at < len(source):
        char = source[at]
        line = source.count('\n', 0, at) + 1
        if char == '%':
            end = source.find('\n', at)
            at = len(source) if end < 0 else end
            continue
        if char == '\\':
            match = re.match(r'\\([A-Za-z]+|.)', source[at:])
            if match is None:
                raise ValueError(f'{path.name}:{line}: incomplete control sequence')
            command = match[1]
            at += len(match[0])
            if command in ('begin', 'end'):
                argument = re.match(r'\s*\{([^{}]+)\}', source[at:])
                if argument is None:
                    raise ValueError(f'{path.name}:{line}: missing environment name')
                name = argument[1]
                if command == 'begin':
                    environments.append((name, line))
                elif not environments or environments.pop()[0] != name:
                    raise ValueError(f'{path.name}:{line}: unmatched end {name}')
                at += len(argument[0])
            elif command in ('[', '('):
                if math is not None:
                    raise ValueError(f'{path.name}:{line}: nested math delimiter')
                math = (command, line)
            elif command in (']', ')'):
                wanted = '[' if command == ']' else '('
                if math is None or math[0] != wanted:
                    raise ValueError(f'{path.name}:{line}: unmatched math delimiter')
                math = None
            # Escaped braces, dollars and percent signs are control symbols,
            # not grouping, math, or comment delimiters.
            continue
        if char == '{':
            braces.append(line)
        elif char == '}':
            if not braces:
                raise ValueError(f'{path.name}:{line}: unmatched closing brace')
            braces.pop()
        elif char == '$':
            if math is None:
                math = ('$', line)
            elif math[0] == '$':
                math = None
            else:
                raise ValueError(f'{path.name}:{line}: dollar inside other math delimiter')
        at += 1
    if braces or environments or math:
        raise ValueError(f'{path.name}: unclosed braces={braces}, environments={environments}, math={math}')
    return path.name

if __name__ == '__main__':
    files = sorted((ROOT/'pages').glob('J156-9-16_156-9_scan*.tex'))
    files += [ROOT/'J156-9-16_transcription.tex', ROOT/'J156-9-16_standalone.tex']
    try:
        for path in files:
            print('PASS', check(path))
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
    print('PASS: braces, display/inline math delimiters, and environments; no compilation attempted.')
