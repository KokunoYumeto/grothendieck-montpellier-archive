"""Second round for block MPL_151_032-075_151-032-151-046: settle five first-pass doubts where the ink reading
and Michel Hua's transcription (batch-02/03) agree. Edits the corrected files in second_pass/out in place;
each old string must occur exactly once."""
import os, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
OUT = os.path.join(BASE, 'second_pass', 'out', 'MPL_151_032-075')

R = {
 32: [("\\unsure{ces} types", "ces types")],
 39: [("\\deleted{\\unsure{est}}", "\\deleted{est}")],
 42: [("\\unsure{d'une} gerbe", "d'une gerbe"), ("\\deleted{\\unsure{iso.}}", "\\deleted{iso.}")],
 45: [("\\deleted{\\unsure{parties}}", "\\deleted{parties}")],
}

for n, reps in R.items():
    p = os.path.join(OUT, 'MPL_151_032-075_151_scan%03d.tex' % n)
    with open(p, encoding='utf-8', newline='') as f:
        t = f.read()
    for old, new in reps:
        c = t.count(old)
        if c != 1:
            print('ABORT scan %d: %r occurs %d times' % (n, old, c)); sys.exit(1)
        t = t.replace(old, new)
    with open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(t)
    print(n, len(reps), 'done')
