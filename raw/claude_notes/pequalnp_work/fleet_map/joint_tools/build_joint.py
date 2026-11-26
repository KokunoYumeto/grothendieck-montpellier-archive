# -*- coding: utf-8 -*-
"""Build JOINT_GCT_LEMMA_SPACE.tsv from the site data, the repository clone, our returns and the hand rows/edges."""
import os, re, sys, glob, csv, json, io, zipfile, collections, datetime
sys.stdout.reconfigure(encoding='utf-8')
csv.field_size_limit(10 ** 9)
TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import hand_rows, edges as EDG  # noqa: E402
import ext_claims  # noqa: E402,F401  (24 Nov 2026: the two VP != VNP claims as external rows and edges)

JOINT = TOOLS  # intermediates (ours_runs.json, zip_envs.json) sit beside this script
PW = '<local>/pequalnp_work/'
DESK = PW + 'desk/'
SITE = DESK + 'site_20261123/'
OUT_TSV = PW + 'fleet_map/JOINT_GCT_LEMMA_SPACE.tsv'
DL = '<local>/Downloads/'
GH = 'https://github.com/brilliant-hq/pequalnp-proofs/tree/main/'
DATA = 'https://data.pequalnp.com/'
GCTMAP = 'data/map/program/gct.b583994396e7.json'
METAMAP = 'data/map/program/meta_complexity.9053e0ec7334.json'
LIBMAP = 'data/map/program/library.56839e2bf936.json'
CONTRIB = 'data/contributors.249cb61fb6e3.json'
PLAN = 'data/plan.c0dd4cd68cdb.json'
NEWS = 'data/news/index.1e6965f97935.json'
CODE = {'c': 'checked (Lean)', 'j': 'open (conjecture)', 'x': 'dead (retired)', 'r': 'refuted', 'w': 'in work'}


def ep(t):
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')


def d16(s):
    return (s or '')[:16].replace('T', ' ')


def cut(s, n):
    s = re.sub(r'\s+', ' ', s or '').strip()
    if len(s) <= n:
        return s
    k = s.rfind('. ', 0, n)
    if k < n * 0.5:
        k = s.rfind(' ', 0, n)
    return s[:k + 1].rstrip() + ' [...]'


def tsvsafe(s):
    return re.sub(r'[\t\r\n]+', ' ', str(s or '')).strip()


# ---------------------------------------------------------------- swarm side
def load_lemma(i):
    fs = glob.glob(SITE + 'data/lemma/%s.*.json' % i) or glob.glob(DESK + 'lemma_cache/%s.*.json' % i)
    f = fs[0]
    rel = ('site ' if 'site_2026' in f else 'cache ') + 'data/lemma/' + os.path.basename(f)
    return json.load(open(f, encoding='utf-8')), rel, os.path.basename(f).split('.')[1]


gmap = json.load(open(SITE + GCTMAP, encoding='utf-8'))
mmap = {n[0]: n for n in json.load(open(SITE + METAMAP, encoding='utf-8'))['nodes']}
lmap = {n[0]: n for n in json.load(open(SITE + LIBMAP, encoding='utf-8'))['nodes']}
feed = collections.defaultdict(list)
for f in glob.glob(SITE + 'data/feed/program/gct/page-*.json'):
    for e in json.load(open(f, encoding='utf-8'))['events']:
        feed[e['lemma_id']].append(e)
news = collections.defaultdict(list)
for a in json.load(open(SITE + NEWS, encoding='utf-8'))['articles']:
    for c in a.get('covers', []):
        news[c].append(a['id'] + ' (' + a['published_at'][:10] + ', ' + a['title'][:60] + ')')
outside = collections.defaultdict(list)
for c in json.load(open(SITE + CONTRIB, encoding='utf-8'))['contributors']:
    for l in c.get('lemmas', []):
        outside[l['id']].append(c['github'])
plan = json.load(open(SITE + PLAN, encoding='utf-8'))['programs']['gct']
role = {}
role[plan['target']['lemma_id']] = 'plan target (' + plan['target']['title'][:80] + ')'
for c in plan['chain']:
    role.setdefault(c['lemma_id'], 'plan chain')
role[plan['hard_link']['lemma_id']] = 'plan hard link'
clone = PW + 'pequalnp-proofs/'


def topics_swarm(n, i):
    s = set()
    if i.startswith('L-meta'):
        return 'meta: monotone circuits (outside GCT, target of our rows)'
    if i == 'L-lib-118':
        return 'level spaces (library fact used inline in L-gct-101)'
    rng = lambda a, b: a <= n <= b
    if rng(1, 10) or n in (15, 22, 28, 64, 68, 70, 72, 73, 74, 75, 76, 82) or rng(23, 34) or rng(38, 49) or rng(53, 60):
        s.add('border dc')
    if rng(12, 14) or rng(16, 21):
        s.add('border dc')
        s.add('Hessian rank (MR)')
    if n in (35, 36, 37, 44, 50, 51, 52, 55, 62, 69, 71, 77, 78, 79, 81, 85, 87, 112, 113, 115, 169, 205):
        s.add('border dc')
        s.add('zero-locus linear spaces')
    if n in (61, 63, 65, 66, 67):
        s.add('border dc')
        s.add('power-sum lemmas')
    if n in (122, 163):
        s.add('level spaces')
        s.add('power-sum lemmas')
    lv = {55, 77, 80, 83, 84, 86, 88, 89, 90, 91, 92, 93, 94, 98, 99, 100, 101, 102, 105, 106, 107, 108, 109, 110, 111, 114, 116,
          117, 118, 119, 120, 121, 123, 131, 133, 134, 135, 136, 142, 143, 150, 151, 152, 153, 156, 157, 158, 159, 160, 162, 165,
          166, 167, 168, 170, 171, 205}
    if n in lv or rng(175, 217):
        s.add('level spaces')
    if n in (95, 96, 97, 124, 125, 139, 140, 218):
        s.add('riffle rank')
    if n in (103, 104, 126, 127, 128, 129, 130, 132, 137, 138, 141, 144, 145, 146, 147, 148, 149, 154, 155, 161, 164, 172, 173, 174):
        s.add('sparse polynomials')
    if n in (6, 11):
        s.add('padding')
        s.add('obstructions')
    order = ['level spaces', 'border dc', 'zero-locus linear spaces', 'Hessian rank (MR)', 'power-sum lemmas', 'riffle rank', 'border rank',
             'positivity and GCT VI/VIII', 'Kronecker and plethysm', 'obstructions', 'padding', 'sparse polynomials']
    return '; '.join([t for t in order if t in s])


swarm = []
ids = ['L-gct-%03d' % n[0] for n in gmap['nodes']] + ['L-lib-118'] + ['L-meta-%03d' % k for k in (583, 606, 608, 617, 632, 647, 655)]
gnode = {'L-gct-%03d' % n[0]: n for n in gmap['nodes']}
for i in ids:
    d, rel, ref = load_lemma(i)
    num = int(i.split('-')[-1])
    if i.startswith('L-gct'):
        node = gnode[i]
        mapfile = GCTMAP
    elif i.startswith('L-meta'):
        node = mmap[num]
        mapfile = METAMAP
    else:
        node = lmap[num]
        mapfile = LIBMAP
    code = node[1]
    status = CODE.get(code, code) + ' since ' + ep(node[4])
    if d.get('faithful'):
        status += '; faithfulness verdict: ' + d['faithful'].get('verdict', '') + ' (' + cut(d['faithful'].get('note', ''), 160) + ')'
    art = d.get('artifact') or {}
    lf = art.get('lean_file')
    links = []
    if lf:
        links.append(GH + lf)
        if not os.path.exists(clone + lf):
            links.append('(not in the local clone of 14:39; newer upstream)')
    if code == 'r' and d.get('counterexample', {}).get('artifact', {}).get('lean_file'):
        links.append(GH + d['counterexample']['artifact']['lean_file'])
    if d.get('artifact_url'):
        links.append(DATA + d['artifact_url'])
    if not links:
        links.append(DATA + 'data/lemma/%s.%s.json (no proof)' % (i, ref))
    if i == 'L-gct-215':
        links.append('local accepted copy: ' + DESK + 'L_gct_215_accepted.lean')
    pseat = d.get('seat') or next((e['seat'] for e in feed.get(i, []) if e['kind'] == 'lemma_proposed'), None)
    hist = ['proposed ' + d16(d.get('proposed_at')) + ' by ' + str(pseat)]
    ats = d.get('attempts') or []
    if ats:
        oc = collections.Counter(a.get('outcome') for a in ats)
        hist.append('attempts %d (%s)' % (len(ats), ', '.join('%s %d' % kv for kv in oc.items())))
    for a in ats:
        if a.get('outcome') == 'died' and a.get('why_died'):
            hist.append('died ' + d16(a.get('ended_at')) + ' (' + str(a.get('by')) + '): ' + cut(a['why_died'], 150))
    for e in sorted(feed.get(i, []), key=lambda e: e['seq']):
        if e['kind'] == 'lemma_checked':
            hist.append('checked ' + d16(e['at']) + (' on an outside runner' if e.get('runner_url') else ''))
        elif e['kind'] in ('lemma_retired', 'lemma_refuted'):
            hist.append(e['kind'].split('_')[1] + ' ' + d16(e['at']) + ': ' + cut(e['sentence'], 170))
    if d.get('retired') and not feed.get(i):
        r = d['retired']
        hist.append('retired ' + d16(r.get('at')) + ' by ' + str(r.get('by')) + ' -> ' + str(r.get('replaced_by')) + ': ' + cut(r.get('why', ''), 120))
    for c in d.get('corrections') or []:
        hist.append('correction ' + d16(c.get('at')) + ' (' + str(c.get('by')) + '): ' + cut(c.get('note', ''), 150))
    attr = ['proposer ' + str(pseat) + ('' if d.get('seat') else ' (from the feed)')]
    res = (d.get('result') or {}).get('contributor')
    if res:
        attr.append('result: ' + str(res.get('display_name') or res.get('id')) + ' (' + str(res.get('kind')) + ')')
    if d.get('contributor'):
        c = d['contributor']
        attr.append('outside author github ' + str(c.get('github')) + ' ' + str(c.get('pr_url', '')))
    elif outside.get(i):
        attr.append('outside author github ' + ', '.join(outside[i]))
    if len(node) > 7 and node[7]:
        attr.append('map credit ' + str(node[7]))
    if role.get(i):
        attr.append(role[i])
    if news.get(i):
        attr.append('news: ' + '; '.join(news[i]))
    notes = []
    if d.get('known'):
        notes.append('known: ' + str(d['known'].get('citation')))
    if d.get('barrier'):
        notes.append('barrier: ' + str(d['barrier']))
    src = ('statement, depends_on, used_by, attempts, seat: site %s; status: site %s; history: site data/feed/program/gct/page-*.json'
           '; attribution: site %s and %s; proof: repository %s' % (rel.replace('cache ', '').replace('site ', ''), mapfile,
                                                                     CONTRIB, PLAN if role.get(i) else 'lemma file', lf or '(none)'))
    if rel.startswith('cache'):
        src = src.replace('statement, depends_on', 'statement (local cache of the site file, ref = current map ref), depends_on')
    swarm.append(dict(id=i, side='swarm', statement=cut(d.get('plain_statement'), 700), status=status, proof_link=' ; '.join(links),
                      depends_on=','.join(d.get('depends_on') or []), used_by=','.join(d.get('used_by') or []),
                      topics=topics_swarm(num, i), cross_edges='', source=src, title=d.get('title', ''),
                      history=' | '.join(hist), attribution='; '.join(attr), notes='; '.join(notes),
                      formal_statement=re.sub(r'\s+', ' ', d.get('formal_statement') or '')))

# ---------------------------------------------------------------- our side: runs
RR = '<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/'
RUNDIR = {'GCT_KRON': RR + 'GCT_KRON_checkpoint_07_20261121T0415Z_unzipped', 'GCT_PLETH': RR + 'GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped',
          'GCT_OBS': RR + 'GCT_OBS_checkpoint_05_20261122T0257Z_unzipped',
          'GCT_OBS_cp15': '<local>/Documents/reports_20261122/overnight_intake/GCT_OBS_cp15/text',
          'GCT_POS': RR + 'GCT_POS_final_20261122T0219Z_unzipped', 'GCT_GINEQ': RR + 'GCT_GINEQ_final_20261120T2340Z_unzipped',
          'GCT_NSRH': RR + 'GCT_NSRH_checkpoint_09_20261121T0545Z_unzipped', 'ALPOGE_GCT': RR + 'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped',
          'CUE_GCT': RR + 'CUE_GCT_checkpoint_08_20261121T0649Z_unzipped', 'BR_PENCIL': RR + 'BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped'}
DEFAULT_TOPIC = {'GCT_KRON': 'obstructions', 'GCT_PLETH': 'Kronecker and plethysm', 'GCT_OBS': 'obstructions', 'GCT_POS': 'positivity and GCT VI/VIII',
                 'GCT_GINEQ': 'border rank', 'GCT_NSRH': 'positivity and GCT VI/VIII', 'ALPOGE_GCT': 'positivity and GCT VI/VIII',
                 'CUE_GCT': 'obstructions', 'BR_PENCIL': 'border rank', 'GCT_FLIP': 'positivity and GCT VI/VIII',
                 'GCT_SEPARATIONS': 'obstructions', 'BORDER_RANK': 'border rank'}
KW = [('level spaces', r'level space|perm\(J|J_n ?\+|subpermanent|doubly cent'),
      ('border dc', r'determinantal complexity|\\overline\{\\?(operatorname\{)?dc|border dc|determinantal (expression|representation|construction)|Mignon|Valiant|Grenet|matrix of (homogeneous )?linear forms|\bdc\('),
      ('riffle rank', r'riffle'),
      ('border rank', r'border rank|\\BR\b|\\BR_|CP border|tensor rank|Waring|secant|flattening|border apolarity|prolongation|ten-plane|seven-plane|residual minim|border substitution|substitution inequality'),
      ('positivity and GCT VI/VIII', r'PH1|PH2|PH3|SH\(a\)|GCT ?VI\b|GCT ?VIII|positivity (hypothes|index|conjecture)|saturation (index|hole|conjecture)|Ehrhart|nonstandard|quantum group|canonical basis|Kazhdan|\bRH\b|robust obstruction|\bflip\b'),
      ('Kronecker and plethysm', r'Kronecker coefficient|Kronecker series|Kronecker tensor|plethysm|Foulkes|Hermite reciprocity|outer degree|outer size|outer Schur|g\(\\lambda'),
      ('obstructions', r'obstruction|multiplicity space|occurrence|orbit closure|K_n\(|q_\\lambda|q\^\{?m|Det_n|\\Omega_n|ideal copy|separat'),
      ('padding', r'padd|\\ell\^\{?\\?,?n-|z\^\{?n-m|X_\{11\}\^'),
      ('sparse polynomials', r'sparse polynomial|hitting set|identity testing|\bPIT\b|Descartes|Wronskian|ROABP|isolat'),
      ('archive (lambda-rings, cotes)', r'\bcote|Burnside|lambda-ring|\\lambda-ring|G-set|Witt|Adams operation|Stiefel'),
      ('complexity (counting, GRH)', r'\\#SAT|#P-|SETH|\bGRH\b|counting transfer|parsimonious|\\#3SAT')]


def primary_topic(run, rid):
    p = rid.split(':', 1)[-1]
    if run == 'GCT_KRON':
        if re.match(r'A-0(0\d|1[0-6])$|A-029$', p):
            return 'archive (lambda-rings, cotes)'
        if p.startswith('F-'):
            return 'Kronecker and plethysm'
        return 'obstructions'
    if run == 'GCT_PLETH':
        return 'archive (lambda-rings, cotes)' if p.startswith('A-') else 'Kronecker and plethysm'
    if run == 'GCT_OBS':
        return 'border rank' if p.startswith('BR-') else 'obstructions'
    if run == 'GCT_POS':
        return 'Kronecker and plethysm' if p.startswith(('K-', 'R-NEW', 'R-DIAG')) else 'positivity and GCT VI/VIII'
    if run == 'ALPOGE_GCT':
        if p.startswith('PL-'):
            return 'archive (lambda-rings, cotes)'
        if p.startswith('C-'):
            return 'complexity (counting, GRH)'
        return 'positivity and GCT VI/VIII'
    if run == 'CUE_GCT':
        if p.startswith(('I-', 'P-')):
            return 'sparse polynomials'
        return 'obstructions'
    return DEFAULT_TOPIC.get(run, 'obstructions')


def topics_ours(run, text, extra='', rid=''):
    s = [extra.split('; ')[0]] if extra else [primary_topic(run, rid)]
    if extra:
        s += [t for t in extra.split('; ')[1:] if t]
    for name, pat in KW:
        if name not in s and re.search(pat, text, re.I):
            s.append(name)
    return '; '.join(s)


def who_norm(w):
    w = w or ''
    if re.search(r'GPT-6 Astra', w) and 'Codex' not in w and '6.2' not in w:
        return 'GPT-6 Astra (ChatGPT Pro mode)'
    if re.search(r'Codex|GPT-6\.2', w):
        return 'GPT-6.2 Astra at reasoning effort ultra (Codex)'
    m = re.search(r'Claude Opus 5\.5 at effort (\w+)', w)
    if m:
        a = re.search(r'(agent|intake agent|main session) ([0-9a-f]{6,})', w)
        return 'Claude Opus 5.5 at effort ' + m.group(1) + (' (' + a.group(2)[:8] + ')' if a else '')
    return w[:60]


POSITIVE = re.compile(r'proof|re-?proof|review|reading|read|reconstruct|check', re.I)


def status_from(events, intake, conj=False):
    neg = [e for e in events if 'refuted' in e['type'].lower() or e['outcome'].strip().upper().startswith(('REFUTED', 'FAIL'))]
    proof = [e for e in events if POSITIVE.search(e['type']) and 'refuted' not in e['type'].lower()
             and 'used and rechecked' not in e['type'] and 'background' not in e['type']
             and not e['outcome'].strip().upper().startswith(('FAIL', 'REFUTED'))]
    comp = [e for e in events if 'comput' in e['type'].lower() or 'certificate' in e['type'].lower()]
    used = [e for e in events if 'used and rechecked' in e['type'] or 'background' in e['type']]
    parts = []
    if conj:
        parts.append('conjecture / open gate (as stated in the return)')
    if neg and not proof:
        parts.append('refuted (in-run: ' + cut(neg[-1]['outcome'], 120) + ')')
    elif neg:
        parts.append('proved after refinement (an earlier form refuted in-run: ' + cut(neg[0]['outcome'], 90) + ')')
    elif proof:
        whos = sorted(set(who_norm(e['who']) for e in proof))
        types = collections.Counter(e['type'] for e in proof)
        parts.append('proved and checked in-run by ' + ', '.join(whos) + ' (' + ', '.join('%s x%d' % kv for kv in types.most_common(3)) + ')')
    elif comp:
        parts.append('computed (in-run certificates, ' + ', '.join(sorted(set(who_norm(e['who']) for e in comp))) + ')')
    elif used:
        parts.append('proved (in-run: used and rechecked / carried)')
    elif not conj:
        parts.append('stated in the return; no check event found')
    if intake:
        pri = [e for e in intake if re.search(r'proof|re-?proof|read', e['type'], re.I)]
        iv = (pri or intake)[-1]
        parts.append('intake: ' + iv['type'] + ' by ' + who_norm(iv['who']) + ' (' + cut(iv['outcome'], 110) + ')')
    return '; '.join(parts)


runs = json.load(open(os.path.join(JOINT, 'ours_runs.json'), encoding='utf-8'))
# PLETH audits A-030..A-102 -> check events of the reviewed ids
pleth_reviews = collections.defaultdict(list)
keep = []
for r in runs:
    if r['run'] == 'GCT_PLETH' and r['id'].startswith('A-') and int(r['id'][2:]) >= 30:
        t = (r['defn'] or {}).get('title', '') + ' ' + (r['defn'] or {}).get('statement', '')[:200]
        m = re.findall(r'\b([GTR])-?0?(\d{2,3})\b', t)
        for g, k in m[:1]:
            pleth_reviews['%s-%03d' % (g, int(k))].append(dict(type='independent review (PLETH audit ' + r['id'] + ')', outcome='PASS (audit statement ' + r['id'] + ')', who='GPT-6 Astra Pro', src='GCT_PLETH.tex'))
        continue
    keep.append(r)
runs = keep
cp05 = {r['id']: r for r in runs if r['run'] == 'GCT_OBS'}
ours = []
for r in runs:
    run = r['run']
    if run == 'GCT_OBS':
        continue  # merged into cp15
    rid = r['id']
    events = r['events'] + pleth_reviews.get(rid, []) if run == 'GCT_PLETH' else r['events']
    intake = r['intake']
    base = RUNDIR[run]
    runname = 'GCT_OBS' if run == 'GCT_OBS_cp15' else run
    d = r['defn']
    other = ''
    if run == 'GCT_OBS_cp15' and rid in cp05:
        o = cp05[rid]
        events = events + [e for e in o['events'] if e not in events]
        if o['defn']:
            other = '; also in checkpoint 05: ' + (RUNDIR['GCT_OBS'] + '/' + o['defn']['file']).replace('/', '\\') + ':' + str(o['defn']['line'])
    if d:
        loc = (base + '/' + d['file']).replace('/', '\\') + ':' + str(d['line'])
        title = re.sub(r'^\\begin\{\w+\*?\}\s*[\[{]?', '', d['title']).replace(rid, '').strip(' .:,[]{}-')
        st = d['statement']
        st = re.sub(r'^[\s.:,}\]]+', '', st)
        stmt = cut(st, 900) if st else '(statement not separated from its heading; see the locator)'
        if len(st) > 900:
            stmt += ' (full: ' + loc + ')'
        conj = bool(re.search(r'conjecture|\bopen\b|candidate', d['title'], re.I))
    else:
        loc = (base + '/' + 'CHECK_EVENTS.tsv').replace('/', '\\') + ' (id only; no TeX definition found)'
        title = ''
        stmt = '(statement not located in the TeX; see the check events: ' + cut(' | '.join(e['outcome'] for e in events[:2]), 300) + ')'
        conj = False
    status = status_from(events, intake, conj)
    srcs = sorted(set(e['src'] for e in events))
    isrc = sorted(set(e['src'] for e in intake))
    src = 'statement: ' + loc + other + '; status: ' + (', '.join(srcs) if srcs else 'no check event') + (' in ' + base.replace('/', '\\') if srcs else '')
    if isrc:
        src += '; intake: ' + ', '.join('field_experts\\intake_20261121\\intakes\\' + s.replace('/', '\\') for s in isrc)
    ours.append(dict(id=runname + ':' + rid, side='ours', statement=stmt, status=status, proof_link=loc, depends_on='', used_by='',
                     topics=topics_ours(runname, title + ' ' + (d['statement'] if d else ''), rid=runname + ':' + rid), cross_edges='', source=src, title=title,
                     history='', attribution='GPT-6 Astra (ChatGPT Pro mode), run ' + runname + (' (checkpoint 15)' if run == 'GCT_OBS_cp15' else ''),
                     notes='', formal_statement=''))

# ---------------------------------------------------------------- our side: newest zips (FLIP final, SEPARATIONS cp10, BORDER_RANK cp14)
zenvs = json.load(open(os.path.join(JOINT, 'zip_envs.json'), encoding='utf-8'))
zev = {}
for z, m, run in [('GCT_FLIP_final.zip', 'CHECK_EVENTS.tsv', 'GCT_FLIP'), ('GCT_SEPARATIONS_checkpoint_10.zip', 'workbench/records/CHECK_EVENTS.tsv', 'GCT_SEPARATIONS'),
                  ('BORDER_RANK_checkpoint_14.zip', 'CHECK_EVENTS.tsv', 'BORDER_RANK')]:
    t = zipfile.ZipFile(DL + z).read(m).decode('utf-8', 'replace')
    rows_ = list(csv.reader(io.StringIO(t), delimiter='\t'))
    hdr = rows_[0]
    ti = [k for k, h in enumerate(hdr) if h.startswith('type')][0]
    oi = [k for k, h in enumerate(hdr) if h.startswith('outcome')][0]
    wi = [k for k, h in enumerate(hdr) if h.startswith('who')][0]
    ev = collections.defaultdict(list)
    for x in rows_[1:]:
        if x:
            ev[x[0]].append(dict(type=x[ti], outcome=x[oi][:220], who=x[wi], src=z + '!' + m))
    zev[run] = ev
sep_stat = {}
t = zipfile.ZipFile(DL + 'GCT_SEPARATIONS_checkpoint_10.zip').read('workbench/records/STATEMENTS.tsv').decode('utf-8', 'replace')
for x in list(csv.DictReader(io.StringIO(t), delimiter='\t')):
    sep_stat[x['statement_id']] = x
xwalk = {}
for z, m, run in [('GCT_SEPARATIONS_checkpoint_10.zip', 'workbench/records/CROSSWALK.tsv', 'GCT_SEPARATIONS'), ('GCT_FLIP_final.zip', 'CROSSWALK.tsv', 'GCT_FLIP')]:
    t = zipfile.ZipFile(DL + z).read(m).decode('utf-8', 'replace')
    for x in csv.DictReader(io.StringIO(t), delimiter='\t'):
        if x.get('earlier_ids'):
            xwalk[(run, x['paper_statement'])] = x['earlier_ids']
codex_int = {'prop:general-padding-nonnormal': 'targeted proof check by GPT-6.2 Astra at reasoning effort ultra (Codex intake of GCT_FLIP cp01, 22 Nov): finite birational map and proper subalgebra checked',
             'thm:relaxed-torus-hardness': 'targeted proof check and computation (52 instances) by GPT-6.2 Astra at reasoning effort ultra (Codex intake, 22 Nov)',
             'thm:finite-nonic': 'targeted proof check and computation (156-graph replay; minors 84 and 46 mod 101) by GPT-6.2 Astra at reasoning effort ultra (Codex intake of GCT_SEPARATIONS cp01, 22 Nov)',
             'thm:43': 'Codex intake of BORDER_RANK cp01 (22 Nov, GPT-6.2 Astra at reasoning effort ultra): 59 lower ideals / 31 orbits regenerated; 25 prolongation cases not checked',
             'thm:44': 'Codex intake of BORDER_RANK cp01: permanent upper witnesses mu10 <= 18, mu11 <= 19, mu12 <= 20 verified over Z; the lower bound 18 for the determinant carried'}
for e in zenvs:
    run = e['run']
    lab = e['label'] or ('line%d' % e['line'])
    rid = (e['paper'] + '.' + lab) if run != 'BORDER_RANK' else lab
    loc = DL.replace('/', '\\') + e['zip'] + '!' + e['member'] + ':' + str(e['line'])
    st = e['statement']
    stmt = cut(st, 900) + (' (full: ' + loc + ')' if len(st) > 900 else '')
    evs = zev[run].get(lab, []) if e['label'] else []
    if run == 'GCT_SEPARATIONS' and rid in sep_stat:
        s = sep_stat[rid]
        status = 'proved; ' + s['check_status'] + ' (in-run, GPT-6 Astra (ChatGPT Pro mode)); independent scope: ' + cut(s['independent_scope'], 120)
    elif evs:
        status = status_from(evs, [], e['env'] == 'conjecture')
    elif e['env'] == 'definition':
        status = 'definition'
    else:
        status = 'stated in the paper; in-run checks indexed in ' + ('CHECK_EVENTS.tsv (BRR ids via CROSSWALK.tsv)' if run == 'BORDER_RANK' else 'CHECK_EVENTS.tsv')
    if e['label'] in codex_int:
        status += '; ' + codex_int[e['label']]
    dep = xwalk.get((run, rid), '') or xwalk.get((run, e['label']), '')
    ours.append(dict(id=run + ':' + rid, side='ours', statement=stmt, status=status, proof_link=loc,
                     depends_on=('consolidates earlier ids: ' + dep) if dep else '', used_by='',
                     topics=topics_ours(run, e['title'] + ' ' + st, rid=run + ':' + rid), cross_edges='', source='statement: ' + loc + '; status: '
                     + (e['zip'] + '!workbench/records/STATEMENTS.tsv' if run == 'GCT_SEPARATIONS' else e['zip'] + '!CHECK_EVENTS.tsv')
                     + ('; Codex intake: field_experts\\intake_20261121\\intakes\\' + {'GCT_FLIP': 'GCT_FLIP', 'GCT_SEPARATIONS': 'GCT_SEPARATIONS', 'BORDER_RANK': 'BORDER_RANK'}[run] if e['label'] in codex_int else ''),
                     title=(e['env'] + (': ' + e['title'] if e['title'] else '')), history='',
                     attribution='GPT-6 Astra (ChatGPT Pro mode), run ' + run + ' (' + e['zip'] + ')', notes='', formal_statement=''))

# ---------------------------------------------------------------- hand rows
for h in hand_rows.R:
    ours.append(dict(id=h['id'], side=h.get('side', 'ours'), statement=h['statement'], status=h['status'], proof_link=h['proof_link'],
                     depends_on=h['depends_on'], used_by=h['used_by'], topics=h['topics'], cross_edges='', source=h['source'],
                     title=h['title'], history='', attribution=h.get('attribution', ''), notes=h['notes'],
                     formal_statement=h.get('formal_statement', '')))

# ---------------------------------------------------------------- edges
allrows = swarm + ours
byid = {r['id']: r for r in allrows}
missing = []
nedge = collections.Counter()
for s, typ, o, cand, note in EDG.E:
    for x in (s, o):
        if x not in byid:
            missing.append(x)
    if s not in byid or o not in byid:
        continue
    tag = ('candidate ' if cand else '') + typ
    nedge[tag] += 1
    txt_s = tag + ':' + o + (' [' + note + ']' if note else '') + (' [work needed: ' + cand + ']' if cand else '')
    txt_o = '<-' + tag + ':' + s + (' [' + note + ']' if note else '') + (' [work needed: ' + cand + ']' if cand else '')
    byid[s]['cross_edges'] = (byid[s]['cross_edges'] + ' ; ' if byid[s]['cross_edges'] else '') + txt_s
    byid[o]['cross_edges'] = (byid[o]['cross_edges'] + ' ; ' if byid[o]['cross_edges'] else '') + txt_o
# swarm notes for internal relations worth a reader's attention
extra_notes = {'L-gct-182': 'excluded in general by the checked L-gct-216 (doubly centred 4 x 4 level spaces have dim <= 3)',
               'L-gct-181': 'excluded mathematically by the checked L-gct-215 (dim <= 7 at 4 x 5); the row is still labelled conjecture',
               'L-gct-006': "paddedPerm pads with x00 outside the m^2 permanent variables (padIndex avoids (0,0)): our GCT_OBS S-004 'independent padding' (support cap m^2+1), not GCT_KRON's internal padding",
               'L-gct-011': "paddedPerm convention as in L-gct-006 note; c <= 2 follows from L-gct-074 plus the converse of L-gct-006 (PNP-SURVEY rows)",
               'L-gct-149': "'Kronecker' here is the substitution x_j -> X^(2^j), not a Kronecker coefficient",
               'L-gct-087': 'independently replayed by Codex (PNP-CODEX:L087-replay)',
               'L-gct-126': 'a one-line ring proof is already in the repository (lean/PEqualNP/Outside/L_gct_126.lean, present in the local clone) while the map lists the row open',
               'L-gct-218': 'with L-gct-097 it negates Rossman Conjecture C.2 (riffle rank of I_n (x) I_n is Omega~(n^2)), so the riffle line has no complexity payoff left (relayed from fleet_map/gct.md 1.7)'}
for k, v in extra_notes.items():
    byid[k]['notes'] = (byid[k]['notes'] + '; ' if byid[k]['notes'] else '') + v
print('missing edge endpoints:', sorted(set(missing)))
print('edges by type:', dict(nedge), 'total', sum(nedge.values()))
COLS = ['id', 'side', 'statement', 'status', 'proof_link', 'depends_on', 'used_by', 'topics', 'cross_edges', 'source', 'title',
        'formal_statement', 'history', 'attribution', 'notes']
with open(OUT_TSV, 'w', encoding='utf-8', newline='') as f:
    f.write('\t'.join(COLS) + '\n')
    for r in allrows:
        f.write('\t'.join(tsvsafe(r.get(c, '')) for c in COLS) + '\n')
json.dump(dict(edges=dict(nedge), n_swarm=len(swarm), n_ours=len(ours)), open(os.path.join(JOINT, 'build_stats.json'), 'w'))
print('rows: swarm', len(swarm), 'ours', len(ours), 'total', len(allrows))
tc = collections.Counter()
for r in allrows:
    for t in [x.strip() for x in r['topics'].split(';') if x.strip()]:
        tc[(r['side'], t)] += 1
for k, v in sorted(tc.items()):
    print(k, v)
