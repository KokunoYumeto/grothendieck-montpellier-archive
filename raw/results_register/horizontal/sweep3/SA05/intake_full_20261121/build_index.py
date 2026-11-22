# Builds the statement index for the full intake of RESEARCH_SA05 (21-22 Nov 2026), read-only on the return.
# For every id in ids.txt: the file and line of \label{id}, the environment, the statement text (to the end of
# the environment) and the length of the proof that follows. Output: index.tsv and statements/<n>.txt.
import os, re, sys, glob
RET = 'C:/Users/user/Documents/grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z_unzipped'
here = os.path.dirname(os.path.abspath(__file__))
ids = [l.strip() for l in open(os.path.join(here, 'ids.txt'), encoding='utf-8') if l.strip()]
files = sorted(glob.glob(RET + '/sections/*.tex')) + sorted(glob.glob(RET + '/part_*/*.tex')) + [RET + '/RESEARCH_SA05_paper.tex']
texts = {}
for f in files:
    try:
        texts[f] = open(f, encoding='utf-8', errors='replace').read()
    except Exception:
        pass
os.makedirs(os.path.join(here, 'statements'), exist_ok=True)
rows = []
for n, i in enumerate(ids, 1):
    key = '\\label{' + i + '}'
    hit = None
    for f in files:          # prefer sections/ (the paper) over part notes
        t = texts.get(f, '')
        k = t.find(key)
        if k >= 0:
            hit = (f, t, k); break
    if not hit:
        rows.append((n, i, '-', '-', '-', 0, 0)); continue
    f, t, k = hit
    b = t.rfind('\\begin{', 0, k)
    env = re.match(r'\\begin\{([^}]*)\}', t[b:]).group(1) if b >= 0 else '?'
    e = t.find('\\end{' + env + '}', k)
    stmt = t[b:e + len(env) + 6] if e >= 0 else t[b:k + 1500]
    p0 = t.find('\\begin{proof}', e)
    nxt = t.find('\\begin{', e + 1)
    proof = ''
    if p0 >= 0 and (p0 - e) < 400:
        p1 = t.find('\\end{proof}', p0)
        proof = t[p0:p1 + 11]
    line = t.count('\n', 0, k) + 1
    with open(os.path.join(here, 'statements', '%03d.txt' % n), 'w', encoding='utf-8') as g:
        g.write('ID %s\nFILE %s:%d\nENV %s\n\n%s\n\n%s\n' % (i, os.path.relpath(f, RET), line, env, stmt, proof))
    rows.append((n, i, os.path.relpath(f, RET), line, env, len(stmt), len(proof)))
with open(os.path.join(here, 'index.tsv'), 'w', encoding='utf-8', newline='\n') as g:
    g.write('n\tid\tfile\tline\tenv\tstmt_chars\tproof_chars\n')
    for r in rows:
        g.write('\t'.join(str(x) for x in r) + '\n')
miss = [r[1] for r in rows if r[2] == '-']
print('indexed', len(rows), 'missing', len(miss), miss[:10])
print('total stmt chars', sum(r[5] for r in rows), 'proof chars', sum(r[6] for r in rows))
