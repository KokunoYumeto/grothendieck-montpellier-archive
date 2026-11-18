# ctrl_counts.py: word counts of the corrected text, doubt marks of the Codex return, and their overlap with hard places.
import re
B = chr(92)
OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
CTX = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/codex_web_20261113/returns_control/CTRL-148_SOL62/out/pages/"
UNS = B + "unsure{"

def braced(s, j):
    depth, k = 1, j
    while depth:
        if s[k] == "{":
            depth += 1
        elif s[k] == "}":
            depth -= 1
        k += 1
    return s[j:k - 1], k

def first_alt(s):
    out, i = [], 0
    while i < len(s):
        if s.startswith(UNS, i):
            inner, k = braced(s, i + len(UNS))
            d, cut = 0, len(inner)
            for m, ch in enumerate(inner):
                if ch == "{":
                    d += 1
                elif ch == "}":
                    d -= 1
                elif ch == "|" and d == 0:
                    cut = m
                    break
            out.append(first_alt(inner[:cut]))
            i = k
        else:
            out.append(s[i])
            i += 1
    return "".join(out)

def words(t):
    t = re.sub(re.escape(B + "begin{tikzpicture}") + ".*?" + re.escape(B + "end{tikzpicture}"), " ", t, flags=re.S)
    t = re.sub(re.escape("[ampersand replacement=" + B + "&") + r"[^\]]*\]", " ", t)
    t = re.sub(re.escape(B + "arrow[") + r"([^\]]*)\]", lambda m: " ".join(re.findall('"([^"]*)"', m.group(1))), t)
    t = first_alt(t)
    t = re.sub(re.escape(B) + r"(scanpage|mspage|cotefile)\{[^}]*\}", " ", t)
    t = re.sub(r"%[^\n]*", " ", t)
    t = re.sub(re.escape(B) + r"[A-Za-z]+\*?", " ", t)
    toks = re.findall(r"[0-9A-Za-zÀ-ÿœŒ']+", t)
    return [x for x in toks if re.search(r"[0-9A-Za-zÀ-ÿ]", x)]

def unsure_tokens(t):
    res, i = [], 0
    while True:
        i = t.find(UNS, i)
        if i < 0:
            return res
        inner, k = braced(t, i + len(UNS))
        res.append(inner)
        i = i + len(UNS)

tw = tu = ti = to = 0
for n in range(44, 59):
    corr = open(OUT + "MPL_148_029-072_148_scan%03d.tex" % n, encoding="utf-8").read()
    cdx = open(CTX + "CTRL-148_148_scan%03d.tex" % n, encoding="utf-8").read()
    w = len(words(corr))
    cu = unsure_tokens(cdx)
    ill = cdx.count(B + "illegible{")
    hard_words, hard_syms = set(), []
    for u in unsure_tokens(corr):
        hard_words |= set(x.lower() for x in re.findall(r"[A-Za-zÀ-ÿ]{3,}", u))
        hard_syms.append(re.sub(r"\s", "", u))
    ov = 0
    for u in cu:
        ws = set(x.lower() for x in re.findall(r"[A-Za-zÀ-ÿ]{3,}", u))
        sym = re.sub(r"\s", "", u)
        if (ws and ws & hard_words) or (not ws and any(sym[:5] and sym[:5] in h for h in hard_syms)):
            ov += 1
    tw += w; tu += len(cu); ti += ill; to += ov
    print("%03d words=%d codex_unsure=%d illegible=%d overlap=%d corrected_unsure=%d" % (n, w, len(cu), ill, ov, len(unsure_tokens(corr))))
print("TOTAL words=%d codex_unsure=%d illegible=%d overlap=%d marks_per100=%.1f" % (tw, tu, ti, to, 100.0 * (tu + ti) / tw))
