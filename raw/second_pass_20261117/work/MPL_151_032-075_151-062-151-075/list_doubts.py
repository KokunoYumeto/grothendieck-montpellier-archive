"""List the \\unsure and \\illegible marks left in the corrected pages of this block, with line numbers."""
import glob
import os
import re

OUT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_151_032-075"
files = sorted(glob.glob(os.path.join(OUT, "MPL_151_032-075_151_scan06[2-9].tex"))
               + glob.glob(os.path.join(OUT, "MPL_151_032-075_151_scan07[0-5].tex")))
pat = re.compile(r"\\(unsure|illegible)\{")
total = 0
for f in files:
    lines = open(f, encoding="utf-8").read().split("\n")
    found = []
    for i, line in enumerate(lines, 1):
        for m in pat.finditer(line):
            j, depth = m.end(), 1
            while depth and j < len(line):
                depth += {"{": 1, "}": -1}.get(line[j], 0)
                j += 1
            found.append(f"L{i}:{line[m.start():j]}")
    total += len(found)
    print(os.path.basename(f)[-7:-4], len(found), " ; ".join(found))
print("TOTAL", total)
