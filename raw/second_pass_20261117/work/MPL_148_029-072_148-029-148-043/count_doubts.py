"""Count doubt marks (unsure, illegible) per corrected page, splitting lines that hold printed matter (texttt)."""
import io

OUT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
U = "\\unsure{"
I = "\\illegible{"
T = "\\texttt"

th = tp = 0
for n in range(29, 44):
    t = io.open(OUT + "MPL_148_029-072_148_scan%03d.tex" % n, encoding="utf-8").read()
    h = p = 0
    for line in t.splitlines():
        k = line.count(U) + line.count(I)
        if T in line:
            p += k
        else:
            h += k
    th += h
    tp += p
    print("scan %03d: handwriting %d, printed %d" % (n, h, p))
print("total handwriting %d, printed %d" % (th, tp))
