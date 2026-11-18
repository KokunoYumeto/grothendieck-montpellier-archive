import sys, os, re, glob, csv, json, datetime, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wc_lib import count_words
from PIL import Image
import numpy as np

BS = chr(92)
ROOT = r'C:/Users/user/Documents/grothendieck_archive_transcription_20261110/returns'
pkg = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'all'
ret = f'{ROOT}/{pkg}_unzipped'
chk = f'{ROOT}/{pkg}_check'
TS = re.compile(r'(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) UTC')


def t(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


lines = open(f'{ret}/progress.log', encoding='utf-8').read().splitlines()
start = t(TS.search(lines[0]).group(1))
done = []      # (cote, scan, time, reader)
audited = []
frozen = None
alltimes = []
for ln in lines:
    m = TS.search(ln)
    if m:
        alltimes.append(t(m.group(1)))
    d = re.match(r'(\d+) scan (\d+) done (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) UTC(?: reader=(\w+))?', ln)
    if d:
        done.append((d.group(1), int(d.group(2)), t(d.group(3)), d.group(4)))
    a = re.match(r'(\d+) scan (\d+) audited (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) UTC(?: reader=(\w+))?', ln)
    if a:
        audited.append((a.group(1), int(a.group(2)), t(a.group(3)), a.group(4)))
    if ln.startswith('transcription frozen'):
        frozen = t(TS.search(ln).group(1))
end = max(alltimes)

# page files in package order
pagefiles = sorted(glob.glob(f'{ret}/pages/*.tex'))
order = []
comb = open(glob.glob(f'{ret}/*_transcription.tex')[0], encoding='utf-8').read()
pos = []
for f in pagefiles:
    m = re.search(r'_(\d+)_scan(\d+)\.tex$', f)
    order.append((m.group(1), int(m.group(2)), f))
# order by position in the combined transcription
def keypos(o):
    txt = open(o[2], encoding='utf-8').read().strip()
    i = comb.find(txt[:200])
    return i if i >= 0 else 10**9
order.sort(key=keypos)
idx = {(c, s): i for i, (c, s, f) in enumerate(order)}
words = {}
marks = {}
for c, s, f in order:
    tx = open(f, encoding='utf-8').read()
    words[(c, s)] = count_words(tx)[0]
    marks[(c, s)] = (len(re.findall(re.escape(BS) + 'unsure', tx)), len(re.findall(re.escape(BS) + 'illegible', tx)),
                     len(re.findall(re.escape(BS) + 'deleted', tx)))

# streams
streams = {}
if any(d[3] for d in done):
    for d in done:
        streams.setdefault(d[3], []).append(d)
else:
    chains = []
    for d in done:
        i = idx.get((d[0], d[1]))
        for ch in chains:
            if idx.get((ch[-1][0], ch[-1][1])) == i - 1:
                ch.append(d)
                break
        else:
            chains.append([d])
    for k, ch in enumerate(chains):
        streams[f's{k+1}'] = ch
pagegap = {}
pagestream = {}
print('== TIMING', pkg)
print('start', start, 'done lines', len(done), 'last done', max(d[2] for d in done), 'frozen', frozen, 'end', end)
print('clock transcription min %.1f' % ((max(d[2] for d in done) - start).total_seconds() / 60),
      '| per page %.2f' % ((max(d[2] for d in done) - start).total_seconds() / 60 / len(done)),
      '| to freeze min %.1f' % ((frozen - max(d[2] for d in done)).total_seconds() / 60),
      '| notes min %.1f' % ((end - frozen).total_seconds() / 60), '| whole run min %.1f' % ((end - start).total_seconds() / 60))
if audited:
    print('audited lines', len(audited), 'distinct pages', len(set((a[0], a[1]) for a in audited)), 'first', min(a[2] for a in audited), 'last', max(a[2] for a in audited))
tot_min = 0
tot_w = 0
for name, ch in streams.items():
    prev = start
    mins = 0
    w = 0
    for j, d in enumerate(ch):
        g = (d[2] - prev).total_seconds() / 60
        pagegap[(d[0], d[1])] = g
        pagestream[(d[0], d[1])] = (name, j + 1, len(ch))
        prev = d[2]
        w += words.get((d[0], d[1]), 0)
    mins = (ch[-1][2] - start).total_seconds() / 60
    tot_min += mins
    tot_w += w
    print(f'stream {name}: {len(ch)} pages {ch[0][0]}:{ch[0][1]:03d}..{ch[-1][0]}:{ch[-1][1]:03d} first done {ch[0][2].time()} last {ch[-1][2].time()} min {mins:.1f} per page {mins/len(ch):.2f} per100w {100*mins/max(w,1):.2f} words {w}')
print('within-stream total min %.1f per page %.2f per 100 words %.2f; words total %d; words/page %.1f' % (tot_min, tot_min / len(done), 100 * tot_min / tot_w, tot_w, tot_w / len(done)))

if mode in ('all', 'complete'):
    print('== COMPLETENESS')
    cat = ''.join(open(f, encoding='utf-8').read() for c, s, f in order)
    def norm(x):
        return re.sub(r'\s+', '', x)
    print('pages', len(order), 'combined chars', len(comb), 'concat chars', len(cat), 'equal modulo whitespace', norm(cat) == norm(comb))
    nsp = sum(1 for c, s, f in order if re.search(re.escape(BS) + r'scanpage\{0*%d\}' % s, open(f, encoding='utf-8').read()))
    nms = sum(1 for c, s, f in order if BS + 'mspage' in open(f, encoding='utf-8').read())
    print('pages with their scanpage marker', nsp, '| with mspage', nms, '| cotefile markers in combined', re.findall(re.escape(BS) + r'cotefile\{[^}]*\}', comb))
    rows = list(csv.DictReader(open(glob.glob(f'{ret}/*_inventory.csv')[0], encoding='utf-8-sig')))
    per = {}
    kinds = {}
    for r in rows:
        per[(r['cote'].strip(), int(re.sub(r'\D', '', r['scan']) or 0))] = per.get((r['cote'].strip(), int(re.sub(r'\D', '', r['scan']) or 0)), 0) + 1
        kinds[r['kind'].strip()] = kinds.get(r['kind'].strip(), 0) + 1
    print('inventory rows', len(rows), 'not yes', sum(1 for r in rows if r['transcribed'].strip().lower() != 'yes'), 'scans covered', len(per), 'rows/scan min', min(per.values()), 'max', max(per.values()))
    print('kinds', kinds)
    if 'sheet_kind' in rows[0]:
        sk = {}
        seen = set()
        for r in rows:
            k = (r['cote'], r['scan'])
            if k not in seen:
                seen.add(k)
                sk[r['sheet_kind']] = sk.get(r['sheet_kind'], 0) + 1
        print('sheet kinds (per scan)', sk)
    missing = [k for k in idx if k not in per]
    print('scans without inventory rows', missing)
    for pat, lab in [(r'\[\.\.\.\]|\[…\]', '[...]'), (r'crop-candidate', 'crop-candidate'), (re.escape(BS) + r'diagram', 'diagram'), (re.escape(BS) + r'figure', 'figure'),
                     (r'tikzcd\}', 'tikzcd tags'), (r'tikzpicture\}', 'tikzpicture tags'), (re.escape(BS) + r'unsure', 'unsure'), (re.escape(BS) + r'unsure\{[^{}]*\|', 'unsure with alt (simple)'),
                     (re.escape(BS) + r'illegible', 'illegible'), (re.escape(BS) + r'deleted', 'deleted'), (re.escape(BS) + r'inserted', 'inserted'), (re.escape(BS) + r'margin', 'margin'),
                     (r'«', 'guillemets'), (r'``', 'backtick quotes'), (r'(?i)\b(omitted|summar|not transcribed|description)', 'omitted/summar words')]:
        print(lab, len(re.findall(pat, comb)), end='; ')
    print()
    W = sum(words.values())
    print('words', W, 'unsure per page %.1f per 100 words %.2f' % (len(re.findall(re.escape(BS) + 'unsure', comb)) / len(order), 100 * len(re.findall(re.escape(BS) + 'unsure', comb)) / W))

if mode in ('all', 'ink'):
    print('== INK')
    ink = {}
    for c, s, f in order:
        p = f'{chk}/scans_unzipped/{pkg}_{c}_scan{s:03d}.jpg'
        im = Image.open(p).convert('L')
        im.thumbnail((1000, 1000))
        a = np.asarray(im)
        ink[(c, s)] = float((a < 110).mean())
    json.dump({f'{c}_{s:03d}': v for (c, s), v in ink.items()}, open(f'{chk}/ink_measured.json', 'w'), indent=0)
    keys = [(c, s) for c, s, f in order]
    tw = sum(words[k] for k in keys)
    ti = sum(ink[k] for k in keys)
    avg = tw / ti
    def part(label, ks):
        w = sum(words[k] for k in ks)
        i = sum(ink[k] for k in ks)
        print(f'{label}: pages {len(ks)} words/page {w/len(ks):.1f} ink/page {i/len(ks):.4f} words/ink {w/i:.0f} index {w/i/avg:.2f}')
    n = len(keys)
    part('first third (package order)', keys[:n // 3])
    part('middle third', keys[n // 3: 2 * n // 3])
    part('last third', keys[2 * n // 3:])
    runorder = [(d[0], d[1]) for d in sorted(done, key=lambda d: d[2])]
    part('first third (run order)', runorder[:n // 3])
    part('middle third (run order)', runorder[n // 3: 2 * n // 3])
    part('last third (run order)', runorder[2 * n // 3:])
    f3, m3, l3 = [], [], []
    for name, ch in streams.items():
        k = [(d[0], d[1]) for d in ch]
        a = len(k) // 3
        f3 += k[:a]
        m3 += k[a:len(k) - a]
        l3 += k[len(k) - a:]
    part('first third of each stream', f3)
    part('middle of each stream', m3)
    part('last third of each stream', l3)
    x = [ink[k] for k in keys]
    y = [words[k] for k in keys]
    print('avg words per unit ink %.0f; r(words, ink) = %.2f' % (avg, statistics.correlation(x, y)))
    low = sorted(keys, key=lambda k: words[k] / ink[k] / avg if ink[k] > 0 else 9)[:8]
    print('lowest index pages:', ', '.join(f'{c}:{s:03d} idx {words[(c,s)]/ink[(c,s)]/avg:.2f} w {words[(c,s)]}' for c, s in low))

if mode in ('all', 'pages'):
    print('== PAGES (cote:scan stream pos/len min words unsure illegible deleted)')
    for name, ch in streams.items():
        out = []
        for d in ch:
            k = (d[0], d[1])
            out.append(f'{k[0]}:{k[1]:03d} {pagegap[k]:.2f}m {words.get(k,0)}w u{marks.get(k,(0,0,0))[0]} d{marks.get(k,(0,0,0))[2]}')
        print(name, '|', ' ; '.join(out))
