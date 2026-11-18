# Stroke measure that does not depend on how dark the pen is: share of pixels that are
# at least D gray levels darker than their blurred neighbourhood (borders cropped).
# usage: python -I -B ink2.py <returns_dir> <package> <stats_json>
import sys, os, glob, json, re, statistics
from PIL import Image, ImageFilter, ImageChops

ret, pkg, sj = sys.argv[1], sys.argv[2], sys.argv[3]
st = json.load(open(sj))
words = {int(k): v for k, v in st['words'].items()}
streams = st['streams']
scans_dir = os.path.join(ret, pkg + '_check', 'package_unzipped', 'scans')
pages = sorted(words)
ink = {}
for p in pages:
    f = glob.glob(os.path.join(scans_dir, '*scan%03d.jpg' % p))[0]
    im = Image.open(f).convert('L')
    w0, h0 = im.size
    im = im.crop((int(w0 * 0.06), int(h0 * 0.05), int(w0 * 0.94), int(h0 * 0.95)))
    im.thumbnail((1100, 1100))
    bl = im.filter(ImageFilter.GaussianBlur(12))
    d = ImageChops.subtract(bl, im)  # positive where the pixel is darker than its surroundings
    h = d.histogram()
    ink[p] = sum(h[22:]) / sum(h)
W = sum(words.values())
avg = W / sum(ink.values())


def part(ps):
    w = sum(words[p] for p in ps); i = sum(ink[p] for p in ps)
    return len(ps), w / len(ps), i / len(ps), w / i


n = len(pages)
print(pkg, 'words per unit of stroke, package: %.0f' % avg)
for name, ps in (('first third', pages[:n // 3]), ('middle third', pages[n // 3:2 * n // 3]), ('last third', pages[2 * n // 3:])):
    a = part(ps)
    print('  %s %03d-%03d: pages %d words/page %.1f stroke/page %.4f words/stroke %.0f index %.2f' % (name, ps[0], ps[-1], a[0], a[1], a[2], a[3], a[3] / avg))
if len(streams) > 1:
    f, m, l = [], [], []
    for a, b, k in streams:
        s = [p for p in pages if a <= p <= b]
        k = len(s)
        f += s[:k // 3]; m += s[k // 3:2 * k // 3]; l += s[2 * k // 3:]
    for name, ps in (('first third of each stream', f), ('middle of each stream', m), ('last third of each stream', l)):
        a = part(ps)
        print('  %s: pages %d words/page %.1f stroke/page %.4f words/stroke %.0f index %.2f' % (name, a[0], a[1], a[2], a[3], a[3] / avg))
xs = [ink[p] for p in pages]; ys = [words[p] for p in pages]
mx, my = statistics.mean(xs), statistics.mean(ys)
r = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
print('  correlation words~stroke r = %.2f' % r)
low = sorted(pages, key=lambda p: (words[p] / ink[p]) / avg)[:8]
print('  lowest index pages:', [(p, round((words[p] / ink[p]) / avg, 2), words[p]) for p in low])
st['stroke'] = ink
json.dump(st, open(sj, 'w'), indent=0)
