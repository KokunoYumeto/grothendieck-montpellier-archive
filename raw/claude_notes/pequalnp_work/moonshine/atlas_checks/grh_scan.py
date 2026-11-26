"""Collect every entry and map where an L-function, a character sum, a Dirichlet/Hecke character, a theta series or
a class number enters, with the matched snippets. Output grh_hits.txt (compact) for reading."""
import json, re, sys, os
D = sys.argv[1]
E = json.load(open(os.path.join(D, 'entries.json'), encoding='utf-8'))
M = json.load(open(os.path.join(D, 'maps.json'), encoding='utf-8'))
PAT = re.compile(r"L\s*\(|L_\{?12|L_K|ζ_|zeta_|ζ\(|zeta\(|Dirichlet|Hecke|Gr(ö|o)ssen|Gauss sum|Jacobi[- ]sum|character sum|"
                 r"Kloosterman|Sali(é|e)|Epstein|class number|h\(\s*[−-]|Artin|GRH|Riemann hypothesis|\bRH\b|nebentypus|"
                 r"Alp(ö|o)ge|Mellin|Rankin|Sym\^?2|Sym²|Kim[–-]Shahidi|Gelbart|Langlands|root number|Chowla|Kronecker limit|"
                 r"Dedekind zeta|L-function|L-series|newform|CM character|cubic residue|quartic residue|residue symbol|"
                 r"χ\s*_?\{?[−-]?\d|chi_?\{?[−-]?\d|χ₋|χ₁|\(·/|\(\./|\(12/·\)|Legendre symbol", re.I)

def snippets(text, k=3, w=110):
    out = []
    for m in PAT.finditer(text):
        s = max(0, m.start() - w // 2)
        out.append(text[s:s + w].replace('\n', ' '))
        if len(out) >= k:
            break
    return out

lines = []
n_e = n_m = 0
for k, e in sorted(E.items(), key=lambda kv: (kv[0].split('-')[0], int(kv[0].split('-')[1]))):
    txt = e['title'] + ' ' + e['body']
    hits = PAT.findall(txt)
    if hits:
        n_e += 1
        loc = re.search(r'Locator[^:]*:\s*(.{0,160})', e['body'])
        lines.append('E %s (%d) %s | LOC %s' % (k, len(hits), e['title'][:110], loc.group(1).replace('\n', ' ') if loc else '?'))
        for s in snippets(txt, 2):
            lines.append('    ~ ' + s)
for mp in M:
    hits = PAT.findall(mp['text'])
    if len(hits) >= 2:
        n_m += 1
        lines.append('M %s (%d) %s' % (mp['mid'], len(hits), mp['text'][:240]))
open(os.path.join(D, 'grh_hits.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('entries with hits', n_e, 'maps with >=2 hits', n_m)
