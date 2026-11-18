# List every open place (\unsure with alternatives, \illegible) in the corrected files, with line numbers.
import os
B = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
out = B + r"/second_pass/out/MPL_16+47+54+44"
def args(line, name):
    res = []; pat = "\\" + name + "{"; i = 0
    while True:
        j = line.find(pat, i)
        if j < 0: return res
        k = j + len(pat); d = 1; s = k
        while d and k < len(line):
            if line[k] == '{': d += 1
            elif line[k] == '}': d -= 1
            k += 1
        res.append(line[s:k-1]); i = k
def alt(a):
    d = 0
    for ch in a:
        if ch == '{': d += 1
        elif ch == '}': d -= 1
        elif ch == '|' and d == 0: return True
    return False
n_all = 0
for n in [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
    f = "MPL_16+47+54+44_16_scan%03d.tex" % n
    for i, line in enumerate(open(os.path.join(out, f), encoding='utf-8').read().split('\n'), 1):
        items = [a for a in args(line, 'unsure') if alt(a)] + ["\\illegible{%s}" % a for a in args(line, 'illegible')]
        for a in items:
            n_all += 1
            print("| %d | %d | `%s` |" % (n, i, a.replace('|', ' / ')))
print("TOTAL", n_all)
