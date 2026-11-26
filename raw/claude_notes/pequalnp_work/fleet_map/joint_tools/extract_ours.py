"""Extract our GCT runs' findings: base id, title, statement (from the TeX), locator, check events (run + intake).
Writes scratchpad/joint/ours_runs.json. Reading only."""
import os, re, sys, glob, csv, json, collections
sys.stdout.reconfigure(encoding='utf-8')
csv.field_size_limit(10 ** 9)
RR = '<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/'
INT = '<local>/Documents/field_experts/intake_20261121/intakes/'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ours_runs.json')
EXCL = re.compile(r'supplied_sources|[\\/]sources[\\/]|_from_earlier|[\\/]literature[\\/]|snapshot|REFERENCE_COPY|[\\/]upload[\\/]')
BS = chr(92)

RUNS = [
    dict(run='GCT_KRON', dir=RR + 'GCT_KRON_checkpoint_07_20261121T0415Z_unzipped', main='GCT_KRON_work/GCT_KRON.tex',
         ce=['GCT_KRON_work/CHECK_EVENTS.tsv', 'GCT_KRON_work/ROOT_CHECK_EVENTS.tsv'], intake='GCT_KRON',
         base=r'^(O-?\d{3}|A-\d{3}|F-?\d{3}|M-?\d{3}|QA033)'),
    dict(run='GCT_PLETH', dir=RR + 'GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped', main='GCT_PLETH.tex',
         ce=['CHECK_EVENTS.tsv'], intake='GCT_PLETH', base=r'^(G-\d{3}|T-\d{3}|R-\d{3}|A-\d{3}|M-\d{3})(?![0-9])'),
    dict(run='GCT_OBS', dir=RR + 'GCT_OBS_checkpoint_05_20261122T0257Z_unzipped', main='GCT_OBS.tex',
         ce=['CHECK_EVENTS.tsv'], intake='GCT_OBS', base=r'^(S-\d{3}|QC-\d{2,3}|OBS-\d{3}|BR-\d{3}|FCA-\d{3})'),
    dict(run='GCT_OBS_cp15', dir='<local>/Documents/reports_20261122/overnight_intake/GCT_OBS_cp15/text',
         main='GCT_OBS.tex', ce=['CHECK_EVENTS.tsv'], intake='GCT_OBS',
         base=r'^(S-\d{3}|QC-\d{2,3}|OBS-\d{3}|BR-\d{3}|FCA-\d{3})'),
    dict(run='GCT_POS', dir=RR + 'GCT_POS_final_20261122T0219Z_unzipped', main='GCT_POS.tex', ce=['CHECK_EVENTS.tsv'],
         intake='GCT_POS', base=r'^(K-\d{3}|N-\d{3}|PNEW-\d{3}|PNEW-M\d+|R-NEW-?\d{3}|R-DIAG-\d{3})'),
    dict(run='GCT_GINEQ', dir=RR + 'GCT_GINEQ_final_20261120T2340Z_unzipped', main='GCT_GINEQ.tex', ce=['CHECK_EVENTS.tsv'],
         intake='GCT_GINEQ', base=r'^(F-\d{2})'),
    dict(run='GCT_NSRH', dir=RR + 'GCT_NSRH_checkpoint_09_20261121T0545Z_unzipped', main='GCT_NSRH.tex', ce=['CHECK_EVENTS.tsv'],
         intake='GCT_NSRH', base=r'^(F\d{2})(?![0-9])'),
    dict(run='ALPOGE_GCT', dir=RR + 'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped', main='ALPOGE_GCT.tex',
         ce=['CHECK_EVENTS.tsv'], intake='ALPOGE_GCT',
         base=r'^(P-F\d+|PLE-F\d+|PL-\d{2}|C-(?:GRH|SAT|COUNT|SIZE|PIT|SIGN|CHAIN-LOCAL)-\d{2}|B\d+\.\d+)(?![0-9])'),
    dict(run='CUE_GCT', dir=RR + 'CUE_GCT_checkpoint_08_20261121T0649Z_unzipped', main='deliverables/CUE_GCT.tex',
         ce=['deliverables/CHECK_EVENTS.tsv'], intake='CUE_GCT',
         base=r'^(I-\d{2}|P-\d{2}[ab]?|P-Z\d{2}|R-\d{2}|G-\d{2}|R-border-conditional|P-cubic-ordered-gate)(?![0-9])'),
    dict(run='BR_PENCIL', dir=RR + 'BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped', main='BR_PENCIL.tex',
         ce=['CHECK_EVENTS.tsv'], intake='BR_PENCIL', base=r'^(P-\d{2}|R-\d{2}|S-\d{2}|O-\d{2}|FL-\d{2})(?![0-9])'),
]

RUNCFG = None


def norm_base(run, raw):
    """Return list of base ids covered by a check-event statement_id."""
    out = []
    for part in re.split(r'\s*[;,/]\s*|\s+and\s+', raw.strip()):
        part = part.strip()
        if not part:
            continue
        if re.match(r'^(GCT_|ALPOGE|CUE_|BR_PENCIL|INTAKE)', part):
            continue
        m = re.match(r'^([A-Z]+(?:-[A-Z]+)?-?)(\d+)([a-z]?)(?:--|\u2013)([A-Z]+-?)?(\d+)$', part)
        if m:
            pre, a, _, _, b = m.groups()
            w = len(a)
            for k in range(int(a), int(b) + 1):
                out.append(pre + str(k).zfill(w))
            continue
        out.append(part)
    res = []
    for p in out:
        mm = re.match(RUNCFG['base'], p)
        if mm:
            b = mm.group(1)
            if run == 'GCT_KRON':
                b = re.sub(r'^([OAFM])-?(\d{3})$', r'\1-\2', b)
            if run == 'GCT_POS':
                b = re.sub(r'^R-NEW-?(\d{3})$', r'R-NEW-\1', b)
            res.append(b)
    return res


ENVS = 'finding|theorem|proposition|lemma|corollary|conjecture|claim|definition|question|problem|remark|example'
ENVOPEN = BS + BS + r'begin\{(?:' + ENVS + r')\*?\}'
STOP = re.compile(BS + BS + r'begin\{proof\}|' + BS + BS + r'paragraph\*?\{Proof|' + BS + BS + r'textit\{Proof|' + BS + BS
                  + r'emph\{Proof|^Proof[.:]|' + BS + BS + r'section\*?\{|' + BS + BS + r'subsection\*?\{|' + BS + BS
                  + r'subsubsection\*?\{', re.M)


def clean(s):
    s = re.sub(r'(?<!\\)%[^\n]*', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\(?:emph|textit|textbf|mathrm|operatorname|texttt)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:small|allowbreak)\b(\{\})?', '', s)
    s = re.sub(r'\\fid\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\end\{(?:' + ENVS + r')\*?\}', ' ', s)
    s = re.sub(r'\\begin\{(?:enumerate|itemize)\}(\[[^\]]*\])?|\\end\{(?:enumerate|itemize)\}', ' ', s)
    s = re.sub(r'\\item\b', ' -', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def heading_end(txt, i):
    depth = 0
    j = i
    while j < len(txt) and j < i + 800:
        c = txt[j]
        if c == '{' and txt[j - 1] != BS:
            depth += 1
        elif c == '}' and txt[j - 1] != BS:
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    k = txt.find('\n', i)
    return k if k > 0 else i + 1


def find_def(files_text, bid, mainrel):
    e = re.escape(bid)
    nb = r'(?![0-9A-Za-z])'
    pats = [
        (1, re.compile(ENVOPEN + r'\s*(?:\[[^\]\n]*?(?<![A-Za-z0-9-])' + e + nb + r'[^\]\n]*\]|\{' + e + r'\}\{[^}\n]*\}|\[' + BS + BS + r'fid\{' + e + r'\}[^\]\n]*\])'), 'env'),
        (2, re.compile(BS + BS + r'(?:section|subsection|subsubsection)\*?(\{)\s*(?:Finding |Statement |Theorem |Proposition )?' + e + nb), 'head'),
        (3, re.compile(BS + BS + r'paragraph\*?(\{)\s*(?:Finding |Statement )?' + e + nb + r'(?!--)'), 'head'),
        (4, re.compile(r'Statement~?\s+' + BS + BS + r'textbf\{' + e + r'\}|' + BS + BS + r'textbf\{(?:Statement |Finding )?' + e + r'\.?\}'), 'bold'),
        (5, re.compile(r'(?m)^#+\s*(?:Finding |Statement )?' + e + nb + r'|\*\*(?:Finding |Statement )?' + e + nb), 'md'),
    ]
    best = None
    for rank, pat, kind in pats:
        for rel, txt in files_text.items():
            if (kind == 'md') != rel.endswith('.md'):
                continue
            m = pat.search(txt)
            if not m:
                continue
            key = (rank, 0 if rel == mainrel else 1)
            if best is None or key < best[0]:
                best = (key, rel, m, kind)
        if best:
            break
    if not best:
        return None
    _, rel, m, kind = best
    txt = files_text[rel]
    s = m.start()
    line = txt.count('\n', 0, s) + 1
    if kind == 'head':
        he = heading_end(txt, m.start(1))
        title = txt[m.start(1) + 1:he - 1]
        start = he
    else:
        eol = txt.find('\n', m.end())
        title = txt[s:eol if eol > 0 else m.end() + 200]
        start = m.end()
    m2 = STOP.search(txt, start)
    stop = m2.start() if m2 else len(txt)
    if kind == 'md':
        m3 = re.compile(r'(?m)^#+ ').search(txt, start)
        stop = min(stop, m3.start() if m3 else len(txt))
    body = txt[start:min(stop, start + 2500)]
    return dict(file=rel, line=line, title=clean(title)[:300], statement=clean(body), kind=kind)


rows = []
for cfg in RUNS:
    RUNCFG = cfg
    run = cfg['run']
    d = cfg['dir']
    ev = collections.defaultdict(list)
    for c in cfg['ce']:
        p = os.path.join(d, c)
        if not os.path.exists(p):
            continue
        R = list(csv.reader(open(p, encoding='utf-8', errors='replace'), delimiter='\t'))
        hdr = [h.strip() for h in R[0]]
        ti = [i for i, h in enumerate(hdr) if h.startswith('type')][0]
        oi = [i for i, h in enumerate(hdr) if h.startswith('outcome')][0]
        wi = [i for i, h in enumerate(hdr) if h.startswith('who')]
        mi = [i for i, h in enumerate(hdr) if h == 'model']
        for x in R[1:]:
            if not x:
                continue
            for b in norm_base(run, x[0]):
                who = (x[wi[0]] if wi and len(x) > wi[0] else '') + ((' ' + x[mi[0]]) if mi and len(x) > mi[0] else '')
                ev[b].append(dict(type=x[ti].strip() if len(x) > ti else '', outcome=(x[oi] if len(x) > oi else '')[:220],
                                  who=who[:160], src=os.path.basename(c)))
    iev = collections.defaultdict(list)
    for p in glob.glob(INT + cfg['intake'] + '/*CHECK_EVENTS.tsv'):
        R = list(csv.reader(open(p, encoding='utf-8', errors='replace'), delimiter='\t'))
        if not R:
            continue
        hdr = [h.strip() for h in R[0]]
        try:
            ti = [i for i, h in enumerate(hdr) if 'type' in h][0]
            oi = [i for i, h in enumerate(hdr) if h.startswith('outcome')][0]
            wi = [i for i, h in enumerate(hdr) if h.startswith('who')][0]
        except IndexError:
            continue
        for x in R[1:]:
            if not x:
                continue
            for b in norm_base(run, x[0]):
                iev[b].append(dict(type=x[ti] if len(x) > ti else '', outcome=(x[oi] if len(x) > oi else '')[:220],
                                   who=(x[wi] if len(x) > wi else '')[:120], src=os.path.relpath(p, INT).replace(BS, '/')))
    files = (glob.glob(d + '/**/*.tex', recursive=True) + glob.glob(d + '/work/**/*.md', recursive=True)
             + glob.glob(d + '/branches/**/*.md', recursive=True))
    ft = {}
    for f in files:
        rel = os.path.relpath(f, d).replace(BS, '/')
        if EXCL.search('/' + rel):
            continue
        try:
            ft[rel] = open(f, encoding='utf-8', errors='replace').read()
        except Exception:
            pass
    ids = list(dict.fromkeys(list(ev.keys()) + list(iev.keys())))
    main = ft.get(cfg['main'], '')
    for m in re.finditer(r'(?:' + BS + BS + r'begin\{(?:finding|theorem|proposition|lemma|corollary)\*?\}\s*(?:\[|\{)(?:' + BS + BS
                         + r'fid\{)?|' + BS + BS + r'(?:sub)*section\*?\{\s*(?:Finding )?|' + BS + BS
                         + r'paragraph\*?\{\s*(?:Finding |Statement ))([A-Z][A-Za-z]*-?[A-Z]*-?\d+[a-z]?)', main):
        for b in norm_base(run, m.group(1)):
            if b not in ids:
                ids.append(b)
    nf = 0
    for b in ids:
        dd = find_def(ft, b, cfg['main'])
        if dd is None:
            nf += 1
        rows.append(dict(run=run, id=b, defn=dd, events=ev.get(b, []), intake=iev.get(b, [])))
    print(run, 'ids', len(ids), 'no def', nf, 'files', len(ft))
json.dump(rows, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('rows', len(rows))
