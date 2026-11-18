import re
base = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
to = tn = 0
for n in range(20, 39):
    f = base + "second_pass/out/MPL_145/MPL_145_145_scan%03d.tex" % n
    g = base + "returns/MPL_145_unzipped/pages/MPL_145_145_scan%03d.tex" % n
    s = open(f, encoding="utf-8").read()
    o = open(g, encoding="utf-8").read()
    bal = s.count("{") - s.count("}")
    disp = s.count(r"\[") - s.count(r"\]")
    un, uo = s.count(r"\unsure{"), o.count(r"\unsure{")
    to += uo; tn += un
    print("scan%03d brace=%d display=%d unsure old=%d new=%d" % (n, bal, disp, uo, un))
print("total unsure old=%d new=%d" % (to, tn))
