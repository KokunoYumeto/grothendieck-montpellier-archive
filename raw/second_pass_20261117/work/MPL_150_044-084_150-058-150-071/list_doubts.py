"""List every \\unsure{...} and \\illegible{...} in the corrected page files of this block."""
import re

OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_150_044-084"
PAT = re.compile(r"\\(unsure|illegible)\{")

for n in range(58, 72):
    with open(f"{OUT}/MPL_150_044-084_150_scan{n:03d}.tex", encoding="utf-8") as f:
        t = f.read()
    for m in PAT.finditer(t):
        i, d = m.end(), 1
        while d and i < len(t):
            d += {"{": 1, "}": -1}.get(t[i], 0)
            i += 1
        line = t.count("\n", 0, m.start()) + 1
        print(f"{n:03d} l{line}: {t[m.start():i][:100]}")
