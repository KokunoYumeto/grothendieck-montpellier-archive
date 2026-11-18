# Completeness statistics for package 33 (several cotes in one return).
# usage: python -I -B stats33.py <returns_dir> <mins_json> <out_json>
import re, sys, os, csv, json, glob, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wc_tex import count
from PIL import Image, ImageFilter, ImageChops

BS = chr(92)
ret, minsj, outj = sys.argv[1], sys.argv[2], sys.argv[3]
P = 'MPL_8_079-081+9+4+100'
unz = os.path.join(ret, P + '_unzipped')
scans = os.path.join(ret, P + '_check', 'package_unzipped', 'scans')
mins = json.load(open(minsj))
order = []
for cote, a, b in (('8', 79, 81), ('9', 1, 29), ('4', 1, 12), ('100', 1, 53)):
    for n in range(a, b + 1):
        f = os.path.join(unz, 'pages', '%s_%s_scan%03d.tex' % (P, cote, n))
        if os.path.exists(f):
            order.append((cote, n, f))
print('pages in run order:', len(order))
rows = list(csv.DictReader(open(os.path.join(unz, P + '_inventory.csv'), encoding='utf-8-sig')))
kind_of = {}
per = collections.Counter()
for r in rows:
    key = r['cote'] + '/%03d' % int(r['scan'])
    kind_of[key] = r['sheet_kind']
    per[key] += 1
words = {}; stroke = {}; texts = {}
for cote, n, f in order:
    key = cote + '/%03d' % n
    s = open(f, encoding='utf-8').read()
    texts[key] = s
    words[key] = count(s)[0]
    im = Image.open(os.path.join(scans, '%s_%s_scan%03d.jpg' % (P, cote, n))).convert('L')
    w0, h0 = im.size
    im = im.crop((int(w0 * 0.06), int(h0 * 0.05), int(w0 * 0.94), int(h0 * 0.95)))
    im.thumbnail((1100, 1100))
    d = ImageChops.subtract(im.filter(ImageFilter.GaussianBlur(12)), im)
    h = d.histogram()
    stroke[key] = sum(h[22:]) / sum(h)
keys = [c + '/%03d' % n for c, n, f in order]
W = sum(words.values())
print('words total %d, per page %.1f; first pass 151.5 min -> %.2f min per 100 words' % (W, W / len(keys), 151.5 / W * 100))
for cote in ('8', '9', '4', '100'):
    ks = [k for k in keys if k.startswith(cote + '/')]
    w = sum(words[k] for k in ks); m = sum(mins[k] for k in ks)
    kinds = collections.Counter(kind_of.get(k, '?') for k in ks)
    print('  cote %s: pages %d words %d (%.1f/page) minutes %.1f min/page %.2f min/100w %.2f; sheet kinds %s' % (cote, len(ks), w, w / len(ks), m, m / len(ks), m / w * 100, dict(kinds)))
# sheet kinds
byk = collections.defaultdict(list)
for k in keys:
    byk[kind_of.get(k, '?')].append(k)
for kd, ks in byk.items():
    print('  sheet kind %s: %d pages, words/page %.1f, min/page %.2f; pages %s' % (kd, len(ks), sum(words[k] for k in ks) / len(ks), sum(mins[k] for k in ks) / len(ks), ' '.join(ks[:40])))
avg = W / sum(stroke.values())
n = len(keys)
for name, ks in (('first third', keys[:n // 3]), ('middle third', keys[n // 3:2 * n // 3]), ('last third', keys[2 * n // 3:])):
    w = sum(words[k] for k in ks); st = sum(stroke[k] for k in ks); m = sum(mins[k] for k in ks)
    print('  %s %s..%s: pages %d words/page %.1f index %.2f min/page %.2f min/100w %.2f' % (name, ks[0], ks[-1], len(ks), w / len(ks), (w / st) / avg, m / len(ks), m / w * 100))
# text pages only (handwritten)
tk = [k for k in keys if kind_of.get(k) == 'text']
avg2 = sum(words[k] for k in tk) / sum(stroke[k] for k in tk)
m3 = len(tk)
for name, ks in (('text pages, first third', tk[:m3 // 3]), ('text pages, middle', tk[m3 // 3:2 * m3 // 3]), ('text pages, last third', tk[2 * m3 // 3:])):
    w = sum(words[k] for k in ks); st = sum(stroke[k] for k in ks)
    print('  %s %s..%s: pages %d words/page %.1f index %.2f' % (name, ks[0], ks[-1], len(ks), w / len(ks), (w / st) / avg2))
xs = [stroke[k] for k in keys]; ys = [words[k] for k in keys]
mx, my = statistics.mean(xs), statistics.mean(ys)
r = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
print('  correlation words~writing r = %.2f' % r)
low = sorted(keys, key=lambda k: (words[k] / stroke[k]) / avg)[:10]
print('  lowest index pages:', [(k, round((words[k] / stroke[k]) / avg, 2), words[k], kind_of.get(k)) for k in low])
# markers
bad = [k for k in keys if not re.match(r'\s*' + BS + BS + r'scanpage\{', texts[k])]
print('pages not starting with a scanpage marker:', bad)
print('first markers:', [texts[k].split('\n')[0][:40] for k in (keys[0], keys[3], keys[32], keys[44])])
main = open(os.path.join(unz, P + '_transcription.tex'), encoding='utf-8').read()
concat = ''.join(texts[k] for k in keys)
norm = lambda x: re.sub(r'\s+', ' ', x).strip()
print('main chars %d, concat chars %d, identical %s, identical up to white space %s' % (len(main), len(concat), main == concat, norm(main) == norm(concat)))
if norm(main) != norm(concat):
    extra = [l for l in main.splitlines() if l.strip() and l.strip() not in concat][:8]
    print('   lines of main not in pages:', [e[:80] for e in extra])
tails = {k: [l for l in texts[k].strip().splitlines() if l.strip()][-1][:60] for k in keys}
endm = [k for k in keys if re.search(BS + BS + r'(margin|mspage)\{', tails[k])]
print('pages ending with margin/mspage: %d of %d; others (first 10): %s' % (len(endm), len(keys), [(k, tails[k][:36]) for k in keys if k not in endm][:10]))
for pat in [r'\[\.\.\.\]', r'\[…\]', 'summar', 'omitted', 'not transcribed', 'TODO', 'remainder', 'continues', 'placeholder', 'crop']:
    c = len(re.findall(pat, main, flags=re.I))
    if c:
        print('  pattern %r: %d' % (pat, c))
un = len(re.findall(BS + BS + r'unsure\{', main)); il = len(re.findall(BS + BS + r'illegible', main))
print('unsure %d (with alternative %d), illegible %d, deleted %d, inserted %d, margin %d, tikzcd %d, tikzpicture %d, figure %d' % (
    un, len(re.findall(BS + BS + r'unsure\{[^{}]*\|', main)), il, len(re.findall(BS + BS + r'deleted\{', main)), len(re.findall(BS + BS + r'inserted\{', main)),
    len(re.findall(BS + BS + r'margin\{', main)), len(re.findall(r'begin\{tikzcd\}', main)), len(re.findall(r'begin\{tikzpicture\}', main)), len(re.findall(BS + BS + r'figure\{', main))))
print('marks per page %.1f, per 100 words %.2f' % ((un + il) / n, (un + il) / W * 100))
print('guillemets:', main.count('«'), ' double-quote pairs:', main.count('``'))
print('inventory rows %d; scans covered %d; rows per scan min %d max %d; pages without rows %s' % (len(rows), len(per), min(per.values()), max(per.values()), [k for k in keys if k not in per]))
json.dump({'words': words, 'stroke': stroke, 'kind': kind_of, 'keys': keys}, open(outj, 'w'))
