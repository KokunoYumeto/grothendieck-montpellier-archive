import re, sys
for n in sys.argv[2:]:
    t = open('statements/%03d.txt' % int(n), encoding='utf-8').read()
    h, _, b = t.partition('\n\n')
    s, _, p = b.partition('\begin{proof}')
    s = re.sub(r'\status\{[^}]*\}', lambda m: '[' + m.group(0)[8:-1] + ']', s)
    s = re.sub(r'\s+', ' ', s)[:int(sys.argv[1])]
    p = re.sub(r'\s+', ' ', p)[:int(sys.argv[1]) // 2]
    print(n, h.split('\n')[0][3:], '|', s, '|| PF:', p)
    print('==')
