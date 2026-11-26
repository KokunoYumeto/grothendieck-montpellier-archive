"""List / extract theorem-like environments of TeX members inside zips (read in memory, nothing extracted to disk).
usage: python -I -B zip_envs.py count | dump OUTJSON"""
import zipfile, sys, re, collections, json
sys.stdout.reconfigure(encoding='utf-8')
DL = '<local>/Downloads/'
MEMBERS = [('GCT_FLIP_final.zip', 'workbench/papers/paper1.tex', 'GCT_FLIP', 'I'),
           ('GCT_FLIP_final.zip', 'workbench/papers/paper2.tex', 'GCT_FLIP', 'II'),
           ('GCT_SEPARATIONS_checkpoint_10.zip', 'workbench/papers/paper_i.tex', 'GCT_SEPARATIONS', 'I'),
           ('GCT_SEPARATIONS_checkpoint_10.zip', 'workbench/papers/paper_ii.tex', 'GCT_SEPARATIONS', 'II'),
           ('BORDER_RANK_checkpoint_14.zip', 'border_rank.tex', 'BORDER_RANK', 'P')]
BS = chr(92)
ENVS = 'theorem|proposition|lemma|corollary|conjecture|claim|finding|question|problem|definition'
ENV = re.compile(BS + BS + r'begin\{(' + ENVS + r')\*?\}')


def clean(s):
    s = re.sub(r'(?<!\\)%[^\n]*', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


mode = sys.argv[1]
out = []
for z, m, run, paper in MEMBERS:
    t = zipfile.ZipFile(DL + z).read(m).decode('utf-8', 'replace')
    c = collections.Counter()
    for x in ENV.finditer(t):
        env = x.group(1)
        c[env] += 1
        e = t.find(BS + 'end{' + env, x.end())
        if e < 0:
            continue
        body = t[x.end():e]
        opt = re.match(r'\s*\[([^\]]*)\]', body)
        lab = re.search(BS + BS + r'label\{([^}]*)\}', body)
        line = t.count('\n', 0, x.start()) + 1
        out.append(dict(run=run, paper=paper, zip=z, member=m, env=env, label=lab.group(1) if lab else '',
                        title=clean(opt.group(1)) if opt else '', line=line,
                        statement=clean(body[opt.end():] if opt else body)[:1500]))
    print(z, m, len(t), dict(c))
if mode == 'dump':
    json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('dumped', len(out))
