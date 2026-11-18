import difflib, re
BS = chr(92)
NL = chr(10)
A = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/returns/MPL_147_048-137_unzipped/pages/MPL_147_048-137_scan%03d.tex"
B = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_147_048-137/MPL_147_048-137_scan%03d.tex"
TOK = re.compile(BS + BS + "[A-Za-z]+|" + BS + BS + ".|[A-Za-z" + chr(0xC0) + "-" + chr(0x17F) + "]+|[0-9]+|[ " + NL + "]+|.", re.S)

def macros(s):
    out = []
    i = 0
    while True:
        cands = [k for k in (s.find(BS + "unsure{", i), s.find(BS + "illegible{", i)) if k >= 0]
        if not cands:
            break
        st = min(cands)
        j = s.find("{", st) + 1
        d = 1
        while d and j < len(s):
            if s[j] == "{":
                d += 1
            elif s[j] == "}":
                d -= 1
            j += 1
        out.append(s[st:j])
        i = st + 1
    return out

tot = 0
for n in range(48, 66):
    a = open(A % n, encoding="utf-8").read()
    b = open(B % n, encoding="utf-8").read()
    bad = [c for c in b if ord(c) < 32 and c != NL]
    bal = b.count("{") - b.count("}")
    dbl_a = a.count(BS + BS)
    dbl_b = b.count(BS + BS)
    ta, tb = TOK.findall(a), TOK.findall(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    ch = [(tag, "".join(ta[i1:i2]), "".join(tb[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
    u = macros(b)
    print("== scan%03d ctrl=%d brace_balance=%d dblbs %d->%d diffs=%d doubtmacros=%d" % (n, len(bad), bal, dbl_a, dbl_b, len(ch), len(u)))
    for c in ch:
        print("    DIFF", c)
    for x in u:
        print("    DOUBT", x)
    tot += len(u)
print("total doubt macros (incl. nested):", tot)
