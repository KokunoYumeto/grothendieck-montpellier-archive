"""List every \\unsure{...} and \\illegible{...} in the corrected page files, with line numbers.
The S/G group-letter convention (\\unsure{\\mathfrak S...|\\mathcal G...}) is counted separately."""
import glob
import re

OUT = ("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/"
       "MPL_150_085-099+151_001-031/")
BS = "\\"
sg = 0
n = 0
for f in sorted(glob.glob(OUT + "*_151_scan0*.tex")):
    s = f[-7:-4]
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for m in re.finditer(r"\\(unsure|illegible)\{", line):
            j = m.end()
            d = 1
            while d and j < len(line):
                d += (line[j] == "{") - (line[j] == "}")
                j += 1
            tok = line[m.start():j]
            if tok.startswith(BS + "unsure{" + BS + "mathfrak S"):
                sg += 1
                continue
            n += 1
            print(s, i, tok)
print("non-convention doubt marks:", n, " S/G convention marks:", sg)
