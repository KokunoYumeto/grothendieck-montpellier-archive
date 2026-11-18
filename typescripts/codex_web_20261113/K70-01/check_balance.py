#!/usr/bin/env python3
"""Structural checks only; this script does not invoke a TeX engine."""
from pathlib import Path
import collections
import json
import re


def without_comments(text):
    return re.sub(r"(?<!\\)(?:\\\\)*%[^\n]*", lambda m: m.group(0).split('%')[0], text)


def check(text):
    text = without_comments(text)
    braces, displays, environments, errors = [], [], [], []
    dollars = 0
    counts = collections.Counter()
    i = 0
    while i < len(text):
        ch = text[i]
        line = text.count('\n', 0, i) + 1
        if ch == '\\':
            env = re.match(r'\\(begin|end)\{([^}]+)\}', text[i:])
            if env:
                action, name = env.groups()
                if action == 'begin':
                    environments.append((name, line))
                    counts['environments'] += 1
                elif not environments or environments[-1][0] != name:
                    errors.append(f'L{line}: mismatched end {name}')
                else:
                    environments.pop()
            word = re.match(r'\\[A-Za-z]+', text[i:])
            if word:
                i += len(word.group())
                continue
            if i + 1 < len(text):
                escaped = text[i + 1]
                if escaped == '[':
                    displays.append(line)
                    counts['displays'] += 1
                elif escaped == ']':
                    if displays:
                        displays.pop()
                    else:
                        errors.append(f'L{line}: unmatched display close')
                i += 2
                continue
        elif ch == '{':
            braces.append(line)
            counts['brace_pairs'] += 1
        elif ch == '}':
            if braces:
                braces.pop()
            else:
                errors.append(f'L{line}: unmatched closing brace')
        elif ch == '$':
            dollars += 1
        i += 1
    errors.extend(f'L{n}: unclosed brace' for n in braces)
    errors.extend(f'L{n}: unclosed display' for n in displays)
    errors.extend(f'L{n}: unclosed environment {name}' for name, n in environments)
    if dollars % 2:
        errors.append(f'odd number of unescaped dollar delimiters: {dollars}')
    counts['dollar_pairs'] = dollars // 2
    return {'passed': not errors, **dict(counts), 'errors': errors}


if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    paths = sorted((root / 'pages').glob('*.tex'))
    paths += [root / 'K70-01_transcription.tex', root / 'K70-01_standalone.tex']
    results = {str(p.relative_to(root)): check(p.read_text()) for p in paths if p.exists()}
    print(json.dumps(results, ensure_ascii=False, indent=2))
    raise SystemExit(0 if all(r['passed'] for r in results.values()) else 1)
