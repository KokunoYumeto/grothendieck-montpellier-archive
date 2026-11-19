# Print a scan range of a cleaned text, without the [?alternatives] and with tikz lines dropped (agent a6d42bf6, horizontal sweep 3)
# usage: python -I -B show.py <clean.txt> <first scan> <last scan> [cap chars]
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(sys.argv[1], encoding='utf-8').read()
a, b = int(sys.argv[2]), int(sys.argv[3]); cap = int(sys.argv[4]) if len(sys.argv) > 4 else 40000
parts = re.split(r'=== scan (\d+) ===', t); out = []
for i in range(1, len(parts) - 1, 2):
    n = int(parts[i])
    if a <= n <= b:
        s = parts[i + 1]
        s = '\n'.join(l for l in s.split('\n') if not re.search(r'execute at end|\\draw|\\node|\\path|tikz|controls \+|\\fill', l))
        s = re.sub(r'\[\?[^\]]{0,30}\]', '', s)
        out.append(f'[{n}] ' + s.strip())
print('\n'.join(out)[:cap])
