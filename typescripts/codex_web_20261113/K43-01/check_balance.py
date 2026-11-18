#!/usr/bin/env python3
"""Static delimiter/environment checks only; never invokes a TeX engine."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
SCANS = list(range(1, 14)) + [15, 16]


def escaped(s, i):
    n = 0
    while i > 0 and s[i - 1] == '\\':
        i -= 1
        n += 1
    return bool(n % 2)


def uncomment(s):
    lines = []
    for line in s.splitlines():
        stop = next((i for i, c in enumerate(line) if c == '%' and not escaped(line, i)), len(line))
        lines.append(line[:stop])
    return '\n'.join(lines)


def check(path):
    s = uncomment(path.read_text())
    errors = []
    braces = 0
    for i, c in enumerate(s):
        if c in '{}' and not escaped(s, i):
            braces += 1 if c == '{' else -1
            if braces < 0:
                errors.append('unmatched closing brace at offset ' + str(i))
    if braces:
        errors.append('brace balance ' + str(braces))
    dollars = sum(c == '$' and not escaped(s, i) for i, c in enumerate(s))
    if dollars % 2:
        errors.append('odd number of unescaped dollar delimiters')
    math_stack = []
    math_pairs = {'[': ']', '(': ')'}
    display_pairs = 0
    for m in re.finditer(r'\\([\[\]()])', s):
        if escaped(s, m.start()):
            continue
        c = m[1]
        if c in math_pairs:
            math_stack.append(c)
            display_pairs += c == '['
        elif not math_stack or math_pairs[math_stack.pop()] != c:
            errors.append('mismatched explicit math delimiter at offset ' + str(m.start()))
    if math_stack:
        errors.append('unclosed explicit math delimiter(s)')
    env_stack = []
    envs = 0
    for m in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}', s):
        if m[1] == 'begin':
            env_stack.append(m[2])
            envs += 1
        elif not env_stack or env_stack.pop() != m[2]:
            errors.append('mismatched environment ' + m[2])
    if env_stack:
        errors.append('unclosed environment(s): ' + ', '.join(env_stack))
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?', s):
        if 'ampersand replacement=\\&' not in (m[1] or ''):
            errors.append('tikzcd lacks ampersand replacement')
    return dict(file=str(path.relative_to(ROOT)), passed=not errors, brace_balance=braces,
                dollar_pairs=dollars // 2, display_pairs=display_pairs,
                environments=envs, errors=errors)


def main():
    pages = [ROOT / 'pages' / ('K43-01_43_scan%03d.tex' % n) for n in SCANS]
    assembled = ROOT / 'K43-01_transcription.tex'
    wrapper = ROOT / 'K43-01_standalone.tex'
    result = [check(p) for p in pages + [assembled, wrapper]]
    text = assembled.read_text()
    extra = []
    if not text.startswith('\\cotefile{43}\n\\scanpage{1}'):
        extra.append('assembled beginning is wrong')
    if text.count('\\cotefile{43}') != 1:
        extra.append('cotefile does not occur exactly once')
    if [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}', text)] != SCANS:
        extra.append('scan order differs from the requested list')
    expected = '\n'.join(p.read_text().rstrip() + '\n' for p in pages)
    if text != expected:
        extra.append('assembled fragment is not the exact ordered page concatenation')
    counts = {name: len(re.findall(r'\\' + name + r'\{', text))
              for name in ('unsure', 'illegible', 'deleted')}
    report = dict(passed=all(x['passed'] for x in result) and not extra,
                  compiled=False, checks=result, assembly_errors=extra, marks=counts,
                  scope='Static braces, unescaped dollar pairs, explicit math delimiters, environments, diagram options and assembly checks. No typesetting/layout validation.')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
