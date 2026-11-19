import glob, os, re
BS = chr(92)
root = r'C:/Users/user/Documents/grothendieck_archive_transcription_20261110/'
out = root + 'second_pass/out/MPL_136_328-376/'
pro = root + 'returns/MPL_136_328-376_checkpoint_02_unzipped/pages/'
work = root + 'codex_web_20261113/returns/K136-03/out/pages/'

def bal(t):
    t = t.replace(BS + '{', '').replace(BS + '}', '')
    d = 0
    m = 0
    for ch in t:
        if ch == '{':
            d += 1
        elif ch == '}':
            d -= 1
            m = min(m, d)
    return d, m

def envs(t):
    b = len(re.findall(re.escape(BS) + r'begin\{', t))
    e = len(re.findall(re.escape(BS) + r'end\{', t))
    return b, e

bad = 0
for f in sorted(glob.glob(out + '*.tex')):
    name = os.path.basename(f)
    s = int(re.search(r'scan(\d+)', name).group(1))
    src = pro + name if s <= 370 else work + 'K136-03_136_scan%d.tex' % s
    t = open(f, encoding='utf-8').read()
    u = open(src, encoding='utf-8').read()
    a, b = bal(t), bal(u)
    ea, eb = envs(t), envs(u)
    flag = ''
    if a[0] != 0 or a[1] < 0 or ea[0] != ea[1]:
        flag = '  <-- CHECK'
        bad += 1
    if a != b or ea != eb:
        flag += '  (differs from source: %s %s vs %s %s)' % (a, ea, b, eb)
    if flag:
        print(name, a, ea, flag)
print('files', len(glob.glob(out + '*.tex')), 'flagged', bad)
