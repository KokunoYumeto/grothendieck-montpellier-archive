# Keyword in context over transcriptions, with the scan number (agent a6d42bf6, horizontal sweep 3)
# usage: python -I -B kwic.py <regex> <width> <tex> [<tex> ...]
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
pat, w = sys.argv[1], int(sys.argv[2])
for p in sys.argv[3:]:
    t = open(p, encoding='utf-8', errors='replace').read()
    for m in re.finditer(pat, t, re.I):
        sc = re.findall(r'scanpage\{0*(\d+)\}', t[:m.start()])
        s = t[max(0, m.start() - w):m.end() + w]
        s = re.sub(r'\\(deleted|unsure|inserted|uline|textit|emph)\{', '{', s)
        s = re.sub(r'\\rotatebox\{90\}\{\\reflectbox\{\{EXTRA STRONG\}\}\}', '', s)
        s = re.sub(r'\s+', ' ', s)
        print(p.replace('\\', '/').split('/')[-1][:34], 'scan', sc[-1] if sc else '?', '|', s, '\n')
