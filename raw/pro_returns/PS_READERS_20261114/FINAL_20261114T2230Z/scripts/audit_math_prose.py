"""Read-only inventory of unwrapped alphabetic tokens in checked math spans.

Uses the reader builder's balanced TeX parsing helpers.  This is a review aid,
not an automatic prose classifier or a source mutation script.
"""
from pathlib import Path
import collections
import hashlib
import json
import re

from build_readers import command, group, skipspace, MATHENV, TEXTARG

ROOT = Path(__file__).resolve().parents[1]
SKIP = set(TEXTARG) | {
    'mathrm', 'mathit', 'mathbf', 'mathsf', 'mathtt', 'mathcal', 'mathbb',
    'mathfrak', 'mathnormal', 'operatorname', 'operatornamewithlimits',
    'textit', 'textbf', 'textsc', 'emph', 'label', 'ref', 'pageref', 'tag',
    'phantom', 'vphantom', 'hphantom', 'illegible', 'mspage', 'scanpage',
}
IGNORE_ARG = {'color', 'hspace', 'vspace', 'kern', 'mkern', 'rule'}
MATHENVS = set(MATHENV) | {'displaymath', 'math', 'eqnarray', 'eqnarray*',
                         'split', 'multline', 'multline*', 'gathered'}
TEXTENVS = {'tabular', 'tabular*', 'tikzpicture', 'minipage'}


def inventory(source):
    chunks = []

    def walk(s, base=0, in_math=False, context=()):
        i = 0
        math = in_math
        dollar = None
        stack = []
        while i < len(s):
            if s[i] == '%':
                end = s.find('\n', i)
                i = len(s) if end < 0 else end + 1
                continue
            if s[i] == '$':
                if dollar:
                    d = '$$' if dollar == '$$' and s.startswith('$$', i) else '$'
                    math, dollar = in_math, None
                else:
                    d = '$$' if s.startswith('$$', i) else '$'
                    math, dollar = True, d
                i += len(d)
                continue
            if s[i] == '\\':
                name, end = command(s, i)
                if name in {'[', '('}:
                    stack.append((math, dollar))
                    math, dollar = True, None
                    i = end
                    continue
                if name in {']', ')'}:
                    math, dollar = stack.pop() if stack else (in_math, None)
                    i = end
                    continue
                p = skipspace(s, end)
                if name in {'begin', 'end'} and p < len(s) and s[p] == '{':
                    env, q = group(s, p)
                    if env in MATHENVS or env in TEXTENVS:
                        if name == 'begin':
                            stack.append((math, dollar))
                            math, dollar = env in MATHENVS, None
                        else:
                            math, dollar = stack.pop() if stack else (in_math, None)
                    i = q
                    if name == 'begin':
                        i = skipspace(s, i)
                        if i < len(s) and s[i] == '[':
                            _, i = group(s, i, '[', ']')
                        if env in {'array', 'tabular', 'tabular*'}:
                            i = skipspace(s, i)
                            if i < len(s) and s[i] == '{':
                                _, i = group(s, i)
                    continue
                if name == 'tikz':
                    if p < len(s) and s[p] == '[':
                        _, p = group(s, p, '[', ']')
                        p = skipspace(s, p)
                    if p < len(s) and s[p] == '{':
                        a, q = group(s, p)
                        walk(a, base + p + 1, False, context + ('tikz',))
                        i = q
                    else:
                        i = end
                    continue
                if name in {'ar', 'arrow'} and p < len(s) and s[p] == '[':
                    opts, q = group(s, p, '[', ']')
                    # TikZ option names are not printed; quoted labels are math.
                    for m in re.finditer(r'"((?:\\.|[^"\\])*)"', opts, re.S):
                        walk(m[1], base + p + 1 + m.start(1), True,
                             context + ('arrow-label',))
                    i = q
                    continue
                if name in SKIP or name in IGNORE_ARG:
                    if p < len(s) and s[p] == '*':
                        p = skipspace(s, p + 1)
                    if p < len(s) and s[p] == '[':
                        _, p = group(s, p, '[', ']')
                        p = skipspace(s, p)
                    if p < len(s) and s[p] == '{':
                        _, i = group(s, p)
                    else:
                        i = end
                    continue
                if name in {'textcolor', 'colorbox', 'fcolorbox'}:
                    if p < len(s) and s[p] == '[':
                        _, p = group(s, p, '[', ']')
                        p = skipspace(s, p)
                    n = 2 if name == 'fcolorbox' else 1
                    for _ in range(n):
                        if p < len(s) and s[p] == '{':
                            _, p = group(s, p)
                            p = skipspace(s, p)
                    i = p
                    continue
                if name == 'ensuremath' and p < len(s) and s[p] == '{':
                    a, q = group(s, p)
                    walk(a, base + p + 1, True, context + (name,))
                    i = q
                    continue
                # Editorial wrappers retain the surrounding math state.  Their
                # optional provenance flags do not render as mathematical text.
                if name in {'inserted', 'over'} and p < len(s) and s[p] == '[':
                    _, p = group(s, p, '[', ']')
                    p = skipspace(s, p)
                if p < len(s) and s[p] == '{':
                    n = 2 if name in {'over', 'frac', 'dfrac', 'tfrac',
                                     'overset', 'underset', 'stackrel', 'binom'} else 1
                    for arg in range(n):
                        p = skipspace(s, p)
                        if p >= len(s) or s[p] != '{':
                            break
                        a, q = group(s, p)
                        walk(a, base + p + 1, math, context + (f'{name}:{arg+1}',))
                        p = q
                    i = p
                else:
                    i = end
                continue
            if s[i] == '{':
                a, q = group(s, i)
                walk(a, base + i + 1, math, context)
                i = q
                continue
            q = i + 1
            while q < len(s) and s[q] not in '%$\\{':
                q += 1
            raw = s[i:q]
            words = re.findall(r'[A-Za-z]+(?:-[A-Za-z]+)*', raw)
            if math and any(len(w) > 1 for w in words):
                chunks.append({'offset': base+i,
                               'line': source.count('\n', 0, base+i)+1,
                               'raw': raw, 'words': words,
                               'context': list(context)})
            i = q

    walk(source)
    return chunks


def main():
    records = []
    hashes = {}
    counts = collections.Counter()
    for p in sorted((ROOT/'checked_pages').glob('*.tex')):
        source = p.read_text()
        hashes[p.stem] = hashlib.sha256(p.read_bytes()).hexdigest()
        for row in inventory(source):
            row['source_key'] = p.stem
            counts.update(w for w in row['words'] if len(w) > 1)
            records.append(row)
    result = {
        'purpose': 'Read-only candidate inventory; actual rendered review is required.',
        'source_count': len(hashes), 'source_hashes': hashes,
        'method': 'Balanced command/group parsing with math delimiters, math environments, '
                  'transparent editorial wrappers and quoted TikZ arrow labels. Text/font/'
                  'operator arguments, comments, metadata and TikZ options are excluded.',
        'raw_math_word_counts': dict(counts.most_common()),
        'chunks': records,
    }
    output = ROOT/'records/MATH_PROSE_CONTEXT_AUDIT_CANDIDATES.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'path': str(output.relative_to(ROOT)), 'sources': len(hashes),
                      'chunks': len(records), 'unique_words': len(counts),
                      'word_counts': dict(counts.most_common())}, ensure_ascii=False))


if __name__ == '__main__':
    main()
