import re, collections, glob, sys
BS = chr(92)
pat = re.compile(re.escape(BS) + r'([a-zA-Z]+)')
for pattern in sys.argv[1:]:
    c = collections.Counter()
    for f in sorted(glob.glob(pattern)):
        c.update(pat.findall(open(f, encoding='utf-8').read()))
    print(pattern)
    print(sorted(c.items(), key=lambda x: -x[1]))
