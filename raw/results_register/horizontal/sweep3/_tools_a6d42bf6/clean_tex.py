# Clean a Codex/Pro transcription .tex into readable text per scan (agent a6d42bf6, horizontal sweep 3, 18 Nov 2026)
# usage: python -I -B clean_tex.py <out.txt> <tex> [<tex> ...]
# Keeps inserted text, the first reading of \unsure{a|b} with the alternatives in brackets, margins as [margin: ...];
# drops \deleted{...} (recorded as a count), % comments, \mspage.
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def find_brace(s, i):
    # s[i] == '{'; return index of matching '}'
    d = 0
    for j in range(i, len(s)):
        c = s[j]
        if c == '\\' and j + 1 < len(s): continue
        if c == '{' and (j == 0 or s[j - 1] != '\\'): d += 1
        elif c == '}' and (j == 0 or s[j - 1] != '\\'):
            d -= 1
            if d == 0: return j
    return len(s) - 1

def repl_cmd(s, name, fn):
    out = []; i = 0; key = '\\' + name + '{'
    while True:
        k = s.find(key, i)
        if k < 0: out.append(s[i:]); break
        out.append(s[i:k]); b = k + len(key) - 1; e = find_brace(s, b)
        out.append(fn(s[b + 1:e])); i = e + 1
    return ''.join(out)

def split_top(s, sep='|'):
    parts = []; d = 0; cur = []
    for c in s:
        if c == '{': d += 1
        elif c == '}': d -= 1
        if c == sep and d == 0: parts.append(''.join(cur)); cur = []
        else: cur.append(c)
    parts.append(''.join(cur)); return parts

def clean(t):
    t = re.sub(r'(?m)(?<!\\)%.*$', '', t)
    t = re.sub(r'\\mspage\{[^}]*\}', '', t)
    t = re.sub(r'\\cotefile\{[^}]*\}', '', t)
    for _ in range(3): t = repl_cmd(t, 'deleted', lambda x: '')
    for _ in range(3): t = repl_cmd(t, 'unsure', lambda x: (lambda p: p[0] + ('[?' + '|'.join(p[1:]) + ']' if len(p) > 1 else '[?]'))(split_top(x)))
    for nm in ('inserted', 'uline', 'textbf', 'emph', 'textit', 'underline', 'boxed', 'text', 'mathrm', 'operatorname'):
        for _ in range(2): t = repl_cmd(t, nm, lambda x: x)
    for _ in range(2): t = repl_cmd(t, 'margin', lambda x: ' [margin: ' + x.strip() + '] ')
    t = re.sub(r'\\(illegible|ill)\{[^}]*\}', '[illeg.]', t)
    t = re.sub(r'\\(quad|qquad|,|;|!|noindent|medskip|smallskip|bigskip|par)\b', ' ', t)
    t = t.replace('\\[', ' $').replace('\\]', '$ ')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t

out = open(sys.argv[1], 'w', encoding='utf-8')
for p in sys.argv[2:]:
    t = open(p, encoding='utf-8', errors='replace').read()
    parts = re.split(r'\\scanpage\{0*(\d+)\}', t)
    for i in range(1, len(parts) - 1, 2):
        out.write(f'\n=== scan {parts[i]} ===\n' + clean(parts[i + 1]).strip() + '\n')
out.close()
