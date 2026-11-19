import sys, re
# Convert a Work (K136-03) page file to the conventions of package MPL_136_328-376:
# plain & in tikz-cd, \mspage{N} for the archive sheet number, rules as \figure{tikzpicture},
# no \resizebox wrapper, \mathrm for {\rm ..}.
# usage: convert_work.py src.tex out.tex
BS = chr(92)
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
n0 = len(t)
log = []

def count_replace(t, a, b, label):
    c = t.count(a)
    if c:
        log.append((label, c))
    return t.replace(a, b)

t = count_replace(t, '[ampersand replacement=' + BS + '&]', '', 'ampersand option (alone)')
t = count_replace(t, 'ampersand replacement=' + BS + '&,', '', 'ampersand option')
t = count_replace(t, BS + '&', '&', 'escaped ampersand')

def arch(m):
    log.append(('archive number comment -> mspage', 1))
    return BS + 'mspage{' + m.group(1) + '}'
t = re.sub(r'%\s*archive sheet number:\s*(\d+)', arch, t)

def rule_fig(width):
    w = width.strip()
    m = re.match(r'([0-9.]+)cm$', w)
    if m:
        x = m.group(1)
    else:
        x = '8'
    return BS + 'figure{' + BS + 'begin{tikzpicture}' + BS + 'draw (0,0)--(' + x + ',0);' + BS + 'end{tikzpicture}}'

pats = [
    re.escape(BS + 'begin{center}' + BS + 'rule{') + r'([^}]*)\}\{[^}]*\}' + re.escape(BS + 'end{center}'),
    re.escape(BS + 'medskip' + BS + 'centerline{' + BS + 'rule{') + r'([^}]*)\}\{[^}]*\}\}',
    re.escape(BS + 'noindent' + BS + 'rule{') + r'([^}]*)\}\{[^}]*\}',
    re.escape(BS + 'rule{') + r'([^}]*)\}\{[^}]*\}',
]
for p in pats:
    def rep(m):
        log.append(('rule -> figure', 1))
        return rule_fig(m.group(1))
    t = re.sub(p, rep, t)

def unwrap(t, head):
    while True:
        i = t.find(head)
        if i < 0:
            return t
        j = i + len(head)
        assert t[j] == '{', 'unwrap: no brace after head'
        depth = 0
        k = j
        while True:
            ch = t[k]
            if ch == BS:
                k += 2
                continue
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        t = t[:i] + t[j + 1:k] + t[k + 1:]
        log.append(('resizebox unwrapped', 1))

t = unwrap(t, BS + 'resizebox{' + BS + 'linewidth}{!}')
t = count_replace(t, '{' + BS + 'rm perf}', BS + 'mathrm{perf}', 'rm -> mathrm')
open(out, 'w', encoding='utf-8', newline='\n').write(t)
rest = [l for l in t.splitlines() if l.lstrip().startswith('%')]
print(out, n0, '->', len(t), log, 'comment lines left:', len(rest))
for l in rest:
    print('   ', l[:150])
