"""Structural checks only. This script never invokes a TeX engine."""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parent

def escaped(s, i):
    n, i = 0, i - 1
    while i >= 0 and s[i] == '\\':
        n += 1; i -= 1
    return n % 2 == 1

def check(path):
    raw = path.read_text()
    lines = []
    for line in raw.splitlines(keepends=True):
        cut = next((i for i,c in enumerate(line) if c == '%' and not escaped(line,i)),len(line))
        lines.append(line[:cut] + ('\n' if cut < len(line) else ''))
    s = ''.join(lines)
    errors, braces, environments, displays = [], [], [], []
    dollars = []
    for i,c in enumerate(s):
        if escaped(s,i):
            continue
        line = s.count('\n',0,i) + 1
        if c == '{': braces.append(line)
        elif c == '}':
            if braces: braces.pop()
            else: errors.append(f'unmatched closing brace at line {line}')
        elif c == '$': dollars.append(line)
    if braces: errors.append(f'unclosed braces from lines {braces}')
    if len(dollars) % 2: errors.append(f'odd number of unescaped dollar delimiters: {len(dollars)}')
    for m in re.finditer(r'\\\[|\\\]|\\begin\{([^}]+)\}|\\end\{([^}]+)\}',s):
        if escaped(s,m.start()):
            continue
        line = s.count('\n',0,m.start()) + 1
        if m.group() == r'\[': displays.append(line)
        elif m.group() == r'\]':
            if displays: displays.pop()
            else: errors.append(f'unmatched display end at line {line}')
        elif m.group(1): environments.append((m.group(1),line))
        elif not environments: errors.append(f'unmatched end {m.group(2)} at line {line}')
        elif environments[-1][0] != m.group(2):
            errors.append(f'environment mismatch {environments[-1]} -> {m.group(2)} at {line}')
        else: environments.pop()
    if displays: errors.append(f'unclosed display delimiters at {displays}')
    if environments: errors.append(f'unclosed environments: {environments}')
    return dict(file=str(path.relative_to(ROOT)),ok=not errors,errors=errors,
                dollar_delimiters=len(dollars),display_pairs=len(re.findall(r'\\\[',s)),
                begin_environments=len(re.findall(r'\\begin\{',s)))

if __name__ == '__main__':
    pages = [ROOT/f'pages/K34-10_34_scan{n}.tex' for n in range(165,180)]
    results = [check(p) for p in pages]
    results.append(check(ROOT/'K34-10_transcription.tex'))
    assembled = (ROOT/'K34-10_transcription.tex').read_text()
    extra = {
        'literal_concatenation': assembled == ''.join(p.read_text() for p in pages),
        'one_cotefile_at_start': assembled.startswith('\\cotefile{34}\n') and assembled.count('\\cotefile{34}') == 1,
        'scan_order': [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',assembled)] == list(range(165,180)),
        'no_embedded_images': not re.search(r'\\(?:includegraphics|includepdf)',assembled),
        'tikzcd_ampersand_replacement': all('ampersand replacement=\\&' in x for x in re.findall(r'\\begin\{tikzcd\}\[([^]]*)\]',assembled)),
        'no_illegible_in_displays_or_drawings': all('\\illegible{' not in m.group() for m in re.finditer(r'\\\[[\s\S]*?\\\]|\\begin\{tikz(?:cd|picture)\}[\s\S]*?\\end\{tikz(?:cd|picture)\}',assembled)),
    }
    report = {'structural_balance_passed': all(r['ok'] for r in results),'results':results,'additional_checks':extra,
              'counts':{name:len(re.findall(r'\\'+name+r'\{',assembled)) for name in ('unsure','illegible','deleted')},
              'scope':'No compilation. Checks TeX braces, dollar parity, display delimiters, environment nesting, and the stated structural invariants. Does not normalize manuscript punctuation or establish semantic/typographic correctness.'}
    (ROOT/'K34-10_balance_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(0 if report['structural_balance_passed'] and all(extra.values()) else 1)
