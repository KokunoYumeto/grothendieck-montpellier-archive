# Locate changed lines in the corrected files and check brace balance (block 16-001-16-018).
import os
B = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
src = B + r"/returns/MPL_16+47+54+44_unzipped/pages"; out = B + r"/second_pass/out/MPL_16+47+54+44"
def bal(t):
    t = t.replace('\\{', '').replace('\\}', '')
    return t.count('{') - t.count('}')
keys = [r"ss-jacent", r"une structure", r"gr.\ \uline", r"sont valables", r"déjà les", r"ou v.", r"cas particulier",
        r"dernière", r"sur-anneau", r"comme on a vu", r"équivaut", r"ascendante", r"de même", r"(\text{si }i\leq n-1)",
        r"\Lambda\in\mathcal E^{(2)}", r"cf. n\textsuperscript{o} 7", r"(6.\unsure{5|15})", r"n\textsuperscript{o} 1, et",
        r"ss-\deleted", r"(ii) Il existe", r"en $L$", r"la validité", r"primo", r"en $=$ temps", r"déjà pour $n$", r"(1.3)$}.",
        r"(\omega)", r"Restons|Reste", r"ni du fait", r"élts de base", r"devraient", r"obtenue", r"On convient", r"définissant",
        r"a déjà indiqué", r"intrinsèquement|", r"commut.", r"\mathrm{gr}", r"voudra|considère|suppose", r"donc|des",
        r"\uline{comme}|", r"on a|comme", r"(\text{si }i", r"(sur $\mathbb Z$ !)", r"Non}", r"\mspage", r"(w_iL^{n-i}-1)"]
for n in [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
    f = "MPL_16+47+54+44_16_scan%03d.tex" % n
    a = open(os.path.join(src, f), encoding='utf-8').read(); b = open(os.path.join(out, f), encoding='utf-8').read()
    print("scan", n, "balance first/out", bal(a), bal(b))
    for i, line in enumerate(b.split('\n'), 1):
        hits = [k for k in keys if k in line]
        if hits: print("  line", i, hits)
