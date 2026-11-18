import re
BS = chr(92)
UN = BS + "unsure{"
B = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
CT = B + "second_pass/out/MPL_145/MPL_145_145_scan%03d.tex"
CX = B + "codex_web_20261113/returns_control/CTRL-145/out/pages/CTRL-145_145_scan%03d.tex"
def unsure_args(s):
    out = []; i = 0
    while True:
        j = s.find(UN, i)
        if j < 0: return out
        k = j + len(UN); d = 1
        while k < len(s) and d:
            if s[k] == "{": d += 1
            elif s[k] == "}": d -= 1
            k += 1
        out.append(s[j+len(UN):k-1]); i = k
def first_alt(a):
    d = 0
    for n, c in enumerate(a):
        if c == "{": d += 1
        elif c == "}": d -= 1
        elif c == "|" and d == 0: return a[:n]
    return a
CMD = re.compile(re.escape(BS) + "[A-Za-z]+")
def strip(s):
    s = re.sub("%.*", "", s)
    s = re.sub(re.escape(BS) + "(scanpage|mspage)" + re.escape("{") + "[^}]*" + re.escape("}"), " ", s)
    for a in unsure_args(s):
        s = s.replace(UN + a + "}", " " + first_alt(a) + " ", 1)
    return CMD.sub(" ", s)
def words(s):
    return re.findall("[0-9A-Za-zÀ-ÖØ-öø-ÿ']+", strip(s))
def norm(a):
    for x, y in (("mathscr", "mathcal"), ("widetilde", "tilde"), ("overline", "bar"), ("widehat", "hat"), (" ", "")):
        a = a.replace(x, y)
    return a
tw = tu = tct = tov = 0
print("scan words_CT unsure_codex unsure_CT codex_on_CT_doubt")
for n in range(20, 35):
    ct = open(CT % n, encoding="utf-8").read(); cx = open(CX % n, encoding="utf-8").read()
    w = len(words(ct)); ux = unsure_args(cx); uc = unsure_args(ct)
    alts = set()
    for a in uc:
        for p in a.split("|"): alts.add(norm(p))
    ov = sum(1 for a in ux if any(norm(p) in alts for p in a.split("|")))
    tw += w; tu += len(ux); tct += len(uc); tov += ov
    print("%03d %4d %3d %3d %3d" % (n, w, len(ux), len(uc), ov))
print("TOTAL words=%d codex_unsure=%d ct_unsure=%d overlap=%d" % (tw, tu, tct, tov))
