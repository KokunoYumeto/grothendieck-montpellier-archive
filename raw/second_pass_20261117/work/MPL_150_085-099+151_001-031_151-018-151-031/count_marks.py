"""Count doubt marks in the first pass and in the corrected files of this block."""
BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
P = "MPL_150_085-099+151_001-031_151_scan"
SRC = BASE + "returns/MPL_150_085-099+151_001-031_unzipped/pages/"
OUT = BASE + "second_pass/out/MPL_150_085-099+151_001-031/"
U = "\\unsure{"
IL = "\\illegible{"
tot = [0, 0, 0, 0, 0, 0]
for s in [18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31]:
    a = open(SRC + P + "%03d.tex" % s, encoding="utf-8").read()
    b = open(OUT + P + "%03d.tex" % s, encoding="utf-8").read()
    sg = b.count(U + "\\mathfrak S")
    zx = b.count(U + "\\zeta") + b.count(U + "\\xi")
    bal = b.count("{") - b.count("}")
    print(s, "first pass:", a.count(U), "unsure", a.count(IL), "illegible",
          "| corrected:", b.count(U), "unsure", b.count(IL), "illegible",
          "| of which group letter", sg, "zeta/xi", zx, "| brace balance", bal)
    tot[0] += a.count(U); tot[1] += a.count(IL); tot[2] += b.count(U)
    tot[3] += b.count(IL); tot[4] += sg; tot[5] += zx
print("totals: first-pass unsure %d illegible %d | corrected unsure %d illegible %d | group %d zeta/xi %d" % tuple(tot))
