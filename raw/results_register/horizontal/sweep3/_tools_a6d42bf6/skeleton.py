# Axiom/definition skeleton of a cleaned transcription (agent a6d42bf6, horizontal sweep 3)
# usage: python -I -B skeleton.py <clean.txt> [width] [cap]
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
p = sys.argv[1]; w = int(sys.argv[2]) if len(sys.argv) > 2 else 200; cap = int(sys.argv[3]) if len(sys.argv) > 3 else 9000
t = open(p, encoding='utf-8').read()
KEY = re.compile(r'(Axiome|Déf|Def\b|Définition|Théorème|Theorem|Proposition|Prop\b|Lemme|Corollaire|Cor\b|Scholie|Sorite|Question|Probl|Conjecture|Remarque|Digression|Mag ?\d|Mag\s?[0-9]|At ?\d|At\s?[A-Z]|Cont ?\d|Fig ?\d|maquette|magasin|atelier|ombre|multistrat|lieu|Récapitulation|je présume|J.ai envie|à vérifier|faux|Faux|innovation|\d{1,2}\.? ?(juin|juillet))', re.I)
out = []; n = 0; scan = '?'
for line in t.split('\n'):
    m = re.match(r'=== scan (\d+) ===', line)
    if m: scan = m.group(1); continue
    if KEY.search(line[:60]) or re.search(r'(Mag|At|Cont|C)\s?\d', line[:12]):
        s = re.sub(r'\s+', ' ', line).strip()
        s = re.sub(r'\[\?[^\]]{0,40}\]', '', s)
        out.append(f'[{scan}] ' + s[:w]); n += len(out[-1])
        if n > cap: out.append('... (cap)'); break
print('\n'.join(out))
