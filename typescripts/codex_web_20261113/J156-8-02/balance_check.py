#!/usr/bin/env python3
"""Lexical LaTeX delimiter check only; never invokes a TeX compiler."""
from pathlib import Path
import re
import sys


def check(path):
    text = path.read_text(encoding='utf-8')
    braces, displays, environments = [], [], []
    dollar = None
    counts = dict(braces=0, dollars=0, displays=0, environments=0)
    problems = []
    i, line = 0, 1
    while i < len(text):
        c = text[i]
        if c == '\n':
            line += 1
        elif c == '%':
            end = text.find('\n', i)
            i = len(text) if end == -1 else end
            continue
        elif c == '\\':
            if i + 1 == len(text):
                problems.append(f'line {line}: trailing backslash')
                break
            following = text[i + 1]
            if following in '[(':
                displays.append((following, line))
                i += 2
                continue
            if following in '])':
                expected = '[' if following == ']' else '('
                if not displays or displays[-1][0] != expected:
                    problems.append(f'line {line}: unmatched math close {following}')
                else:
                    displays.pop()
                    counts['displays'] += 1
                i += 2
                continue
            env = re.match(r'\\(begin|end)\{([^{}]+)\}', text[i:])
            if env:
                action, name = env.groups()
                counts['braces'] += 1
                if action == 'begin':
                    environments.append((name, line))
                elif not environments or environments[-1][0] != name:
                    problems.append(f'line {line}: mismatched end of {name}')
                else:
                    environments.pop()
                    counts['environments'] += 1
                i += len(env.group())
                continue
            # A control symbol escapes its next character; a control word does not.
            word = re.match(r'\\[A-Za-z@]+', text[i:])
            i += len(word.group()) if word else 2
            continue
        elif c == '{':
            braces.append(line)
        elif c == '}':
            if not braces:
                problems.append(f'line {line}: unmatched closing brace')
            else:
                braces.pop()
                counts['braces'] += 1
        elif c == '$':
            width = 2 if text[i:i+2] == '$$' else 1
            if dollar is None:
                dollar = (width, line)
            elif dollar[0] != width:
                problems.append(f'line {line}: mixed $ / $$ delimiters')
            else:
                dollar = None
                counts['dollars'] += 1
            i += width
            continue
        i += 1
    if braces:
        problems.append(f'unclosed braces from lines {braces}')
    if displays:
        problems.append(f'unclosed math delimiters {displays}')
    if environments:
        problems.append(f'unclosed environments {environments}')
    if dollar:
        problems.append(f'unclosed dollar math from line {dollar[1]}')
    return counts, problems


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    files = sorted((root / 'pages').glob('*.tex'))
    files += [root / 'J156-8-02_transcription.tex', root / 'J156-8-02_standalone.tex']
    errors = 0
    print('Lexical balance check: no compilation performed.')
    for path in files:
        counts, problems = check(path)
        print(f'{path.relative_to(root)}: {"FAIL" if problems else "PASS"}; {counts}')
        for problem in problems:
            print('  ' + problem)
        errors += len(problems)
    print(f'{len(files)} files checked; {errors} balance errors.')
    sys.exit(bool(errors))
