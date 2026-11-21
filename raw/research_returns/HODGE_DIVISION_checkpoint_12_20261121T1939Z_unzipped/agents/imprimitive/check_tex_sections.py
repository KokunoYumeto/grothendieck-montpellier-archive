#!/usr/bin/env python3
"""Check structural TeX syntax; this is explicitly not a TeX compilation.

The workspace lacks a usable LaTeX format and the attempted Tectonic bundle
download returned HTTP403. This small lexer certifies only matched braces,
environments and math delimiters, and records the exact checked file hashes.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
FILES = ['imprimitive_section.tex', 'semiregular_section.tex',
         'monomial_sixfold_section.tex', 'imprimitive_bibitems.tex',
         'e8_tuple_section.tex', 'e8_period_section.tex',
         'e8_period_bibitems.tex', 'e8_transfer_diagrams.tex',
         'nielsen_rank_algorithm.tex', 'nielsen_rank_bibitems.tex']

def check(name):
    text = (ROOT/name).read_text()
    i = 0
    braces = []
    envs = []
    math = None
    displays = 0
    errors = []
    line = 1
    while i < len(text):
        c = text[i]
        if c == '\n':
            line += 1
            i += 1
            continue
        if c == '%':
            j = text.find('\n', i)
            i = len(text) if j < 0 else j
            continue
        if c == '\\':
            match = re.match(r'\\(begin|end)\{([^}]+)\}', text[i:])
            if match:
                op, env = match.groups()
                if op == 'begin':
                    envs.append((env, line))
                elif not envs or envs[-1][0] != env:
                    errors.append(f'line {line}: unmatched end {env}')
                else:
                    envs.pop()
                i += len(match.group())
                continue
            if i+1 < len(text) and text[i+1] in '()[]':
                d = text[i+1]
                if d in '([':
                    if math is not None:
                        errors.append(f'line {line}: nested math delimiter')
                    math = {'(': ')', '[': ']'}[d]
                    displays += d == '['
                elif math != d:
                    errors.append(f'line {line}: unmatched math delimiter')
                else:
                    math = None
                i += 2
                continue
            match = re.match(r'\\(?:[A-Za-z]+\*?|.)', text[i:], re.S)
            i += len(match.group()) if match else 1
            continue
        if c == '{':
            braces.append(line)
        elif c == '}':
            if not braces:
                errors.append(f'line {line}: unmatched closing brace')
            else:
                braces.pop()
        elif c == '$':
            if math is None:
                math = '$'
            elif math == '$':
                math = None
            else:
                errors.append(f'line {line}: dollar in delimited math')
        i += 1
    if braces:
        errors.append(f'unclosed braces from lines {braces}')
    if envs:
        errors.append(f'unclosed environments {envs}')
    if math is not None:
        errors.append('unclosed math delimiter')
    return {'file': name, 'sha256': hashlib.sha256(text.encode()).hexdigest(),
            'balanced_environments_braces_math': not errors,
            'display_count': displays, 'errors': errors,
            'compiled_or_rendered': False}

if __name__ == '__main__':
    result = [check(name) for name in FILES]
    (ROOT/'tex_syntax_check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if not all(x['balanced_environments_braces_math'] for x in result):
        raise SystemExit(1)
