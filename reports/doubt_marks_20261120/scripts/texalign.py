"""Shared helpers for the doubt-mark report (20 Nov 2026, main session, Claude Opus 5.5 at effort max).

A page's LaTeX becomes a list of word tokens. Each doubt mark of our readings (\\unsure{a|b}, \\unsure{a},
\\illegible{n}) is written out with its first reading, between two sentinels, so that a mark glued to its neighbours
(d'\\unsure{opérateurs}, $(\\unsure{v}),f_1$) stays inside the word it belongs to. Every token that overlaps a mark is
tagged with it. Hua's marks (\\uncertain{x}, \\ill) are tagged the same way. Two token lists are aligned with difflib,
and each mark of the first text is looked up in the second between the nearest words the two texts share (the
anchors). A mark's alternatives are compared as whole covering words, with the alternative written in."""
import difflib
import re
import unicodedata

OURS = ("unsure", "illegible")
HUAS = ("uncertain", "ill")
DROP = {"scanpage", "cotefile", "page", "note", "label", "drawing", "folder", "batch", "pages", "foldertitle",
        "dating", "watermark", "keywords", "supplied", "pagerange", "footnote", "grothDrawingFile", "includegraphics",
        "vspace", "hspace", "input", "documentclass", "usepackage", "newcommand", "renewcommand", "setlength"}
WRAP = {"mspage", "textit", "emph", "text", "mathrm", "mathit", "textbf", "mathbf", "handwritten", "inserted", "margin", "uline",
        "underline", "hand", "over", "xout", "uuline", "textsf", "mbox", "hbox", "textup", "textsc", "add", "struck",
        "marginal", "diagram", "figure", "deleted", "sout", "textsuperscript", "textsubscript", "operatorname", "mathsf",
        "mathcal", "mathscr", "mathfrak", "mathbb", "boldsymbol", "bm", "overline", "underbrace", "overbrace", "small",
        "footnotesize", "large", "Large", "centering", "ensuremath", "fbox", "boxed", "framebox", "makebox", "raisebox",
        "color", "textcolor", "uwave", "dashuline", "dotuline", "circled", "encircle", "tikz", "noindent", "par",
        "medskip", "smallskip", "bigskip", "newline", "linebreak", "quad", "qquad", "left", "right", "big", "Big",
        "bigg", "Bigg", "displaystyle", "textstyle", "scriptstyle", "nolimits", "limits"}
ENVSKIP = re.compile(r"\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}", re.S)
CMT = re.compile(r"(?<!\\)%.*")
PUNCT = ".,;:!?«»\"“”‘’'`()[]<>"
S0, S1 = "\x01", "\x03"  # start and end of a mark's written-out reading
ILL = "⟨illeg⟩"


def strip_comments(t):
    return "\n".join(CMT.sub("", line) for line in t.splitlines())


def close_brace(t, i):
    """t[i] == '{': index just after its matching '}', or len(t)."""
    d = 0
    k = i
    while k < len(t):
        ch = t[k]
        if ch == "\\":
            k += 2
            continue
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
            if d == 0:
                return k + 1
        k += 1
    return len(t)


def split_top(s, sep="|"):
    out, d, cur, k = [], 0, [], 0
    while k < len(s):
        ch = s[k]
        if ch == "\\" and k + 1 < len(s):
            cur.append(s[k:k + 2])
            k += 2
            continue
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
        if ch == sep and d == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
        k += 1
    out.append("".join(cur))
    return out


def alternatives(arg):
    """The readings of \\unsure{arg}. A '|' that leaves an empty side (g=|f|) is an absolute value, not a choice."""
    parts = split_top(arg or "")
    if len(parts) > 1 and any(not p.strip() for p in parts):
        return [arg or ""]
    return parts


def norm_word(w):
    w = unicodedata.normalize("NFC", w).replace("’", "'").replace("‘", "'")
    return w.strip(PUNCT)


def loose(w):
    w = unicodedata.normalize("NFD", w.lower())
    return "".join(ch for ch in w if unicodedata.category(ch) != "Mn" and ch not in PUNCT + "'-")


def to_plain(s, drop_env=False):
    """LaTeX -> plain text with spaces between words; the sentinels pass through. drop_env: leave out drawings
    (tikzpicture, tikzcd), for counting reading changes without redrawn figures."""
    if drop_env:
        s = ENVSKIP.sub(" ", s)
    buf = []  # 20 Nov: diagrams are kept (their doubt marks count too)
    k = 0
    while k < len(s):
        ch = s[k]
        if ch == "\\":
            m = re.match(r"\\([A-Za-z@]+)\*?", s[k:])
            if m:
                name = m.group(1)
                j = k + m.end()
                if name in ("begin", "end"):
                    if j < len(s) and s[j] == "{":
                        j = close_brace(s, j)
                    buf.append(" ")
                    k = j
                    continue
                if name in DROP:
                    while j < len(s) and s[j] in " \t":
                        j += 1
                    while j < len(s) and s[j] in "[{":
                        if s[j] == "{":
                            j = close_brace(s, j)
                        else:
                            e = s.find("]", j)
                            j = e + 1 if e > 0 else j + 1
                    buf.append(" ")
                    k = j
                    continue
                if name in WRAP:
                    k = j
                    if name in ("color", "textcolor") and j < len(s) and s[j] == "{":
                        k = close_brace(s, j)
                    continue
                buf.append(" \\" + name + " ")
                k = j
                continue
            nxt = s[k + 1:k + 2]
            buf.append(nxt if nxt in "{}$%&#_|" else " ")
            k += 2
            continue
        if ch in "{}$~":
            k += 1
            continue
        buf.append(ch)
        k += 1
    return "".join(buf)


def words_of(plain):
    """plain text -> list of (key, start, end) by whitespace; keys without sentinels, normalized."""
    out = []
    for m in re.finditer(r"\S+", plain):
        key = norm_word(SENT.sub("", m.group()))
        out.append((key, m.start(), m.end()))
    return out


SENT = re.compile("[\U000F0000-\U0010FFFF]")


def find_marks(t, names):
    """Top-level marks in t: list of dict(s, e, name, arg); marks nested in a mark are counted on their parent."""
    pat = re.compile(r"\\(" + "|".join(names) + r")(?![A-Za-z])")
    res = []
    for m in pat.finditer(t):
        s = m.start()
        if res and s < res[-1]["e"]:
            res[-1]["nested"] += 1
            continue
        j = m.end()
        arg = None
        e = j
        if j < len(t) and t[j] == "{":
            e = close_brace(t, j)
            arg = t[j + 1:e - 1]
        res.append(dict(s=s, e=e, name=m.group(1), arg=arg, nested=0))
    return res


def context_flags(t, s):
    flags = {}
    for name in ("deleted", "margin", "inserted"):
        inside = False
        for m in re.finditer(r"\\" + name + r"\{", t[:s]):
            if close_brace(t, m.end() - 1) > s:
                inside = True
                break
        flags[name] = inside
    st = math_state(t[:s])
    flags["math"] = st["math"]
    flags["diagram"] = st["diagram"]
    return flags


# 20 Nov 2026: a delimiter counts only after an even run of backslashes, so the line break with spacing \\[2pt] (1,025
# times on 582 pages of the text of record) no longer opens a display, and $$ ... $$ is a display of its own.
_EVEN = r"(?<!\\)(?:\\\\)*"
MATH_ENVS = "equation|align|gather|multline|eqnarray|array|cases|tikzcd|displaymath"
DELIM = re.compile(_EVEN + r"(\$\$|\$|\\\[|\\\]|\\\(|\\\)|\\begin\{(?:" + MATH_ENVS + r"|tikzpicture)\*?\}|\\end\{(?:"
                   + MATH_ENVS + r"|tikzpicture)\*?\})")


def _delim_step(st, tok):
    """Update a math state with one delimiter token (as DELIM's group 1 gives it)."""
    if tok == "$$":
        st["dd"] ^= 1
    elif tok == "$":
        st["d"] ^= 1
    elif tok == "\\[":
        st["disp"] += 1
    elif tok == "\\]":
        st["disp"] -= 1
    elif tok == "\\(":
        st["par"] += 1
    elif tok == "\\)":
        st["par"] -= 1
    else:
        name = re.match(r"\\(begin|end)\{([A-Za-z]+)", tok)
        step = 1 if name.group(1) == "begin" else -1
        if name.group(2) in ("tikzcd", "tikzpicture"):
            st["diag"] += step
        if name.group(2) != "tikzpicture":
            st["env"] += step


def _flags_of(st):
    return {"math": bool(st["d"] or st["dd"] or st["disp"] > 0 or st["par"] > 0 or st["env"] > 0), "diagram": st["diag"] > 0}


def math_state(pre):
    """Is the end of `pre` inside mathematics, inside a drawing?"""
    st = dict(d=0, dd=0, disp=0, par=0, env=0, diag=0)
    for m in DELIM.finditer(pre):
        _delim_step(st, m.group(1))
    return _flags_of(st)


def zone_words(t, names=OURS):
    """Words of a page by zone and by struck-out text, counted the way tokenize counts them: each doubt mark written out
    with its first reading. -> Counter of (zone, struck) -> [words, letters]; zone is 'diagram' (tikzcd, tikzpicture),
    'math' or 'prose'; struck is True inside \\deleted{...}. A delimiter itself is not a word."""
    t = strip_comments(t)
    pieces, pos = [], 0
    for m in find_marks(t, names):
        pieces.append(t[pos:m["s"]])
        if m["name"] in ("illegible", "ill"):
            inner = ILL
        else:
            arg = NESTED_ILL.sub(ILL, NESTED_UNS.sub("{", m["arg"] or "")) if m["nested"] else (m["arg"] or "")
            inner = (alternatives(arg) if m["name"] == "unsure" else [arg])[0]
        pieces.append(inner)
        pos = m["e"]
    pieces.append(t[pos:])
    t2 = "".join(pieces)
    events = [(m.start(1), m.end(1), "delim", m.group(1)) for m in DELIM.finditer(t2)]
    for m in re.finditer(_EVEN + r"(\\deleted\{)", t2):
        events.append((m.start(1), m.end(1), "del_open", close_brace(t2, m.end(1) - 1)))
    events.sort()
    out = {}
    st = dict(d=0, dd=0, disp=0, par=0, env=0, diag=0)
    del_ends = []  # end positions (just past the closing brace) of the open \deleted groups
    last = 0

    def emit(a, b):
        if b <= a:
            return
        f = _flags_of(st)
        zone = "diagram" if f["diagram"] else "math" if f["math"] else "prose"
        for key, _, _ in words_of(to_plain(t2[a:b])):
            if key:
                c = out.setdefault((zone, bool(del_ends)), [0, 0])
                c[0] += 1
                c[1] += len(key)

    for s, e, kind, val in events:
        if s < last:
            continue
        while del_ends and min(del_ends) <= s:  # a \deleted group closes before this event
            end = min(del_ends)
            emit(last, end - 1)
            del_ends.remove(end)
            last = max(last, end)
        emit(last, s)
        if kind == "delim":
            _delim_step(st, val)
        else:
            del_ends.append(val)
        last = e
    while del_ends:
        end = min(del_ends)
        emit(last, end - 1)
        del_ends.remove(end)
        last = max(last, end)
    emit(last, len(t2))
    return out


def tokenize(t, names=OURS, drop_env=False):
    """-> (tokens, marks). tokens: list of (key, frozenset of mark indices). Each mark gets kind, alts (the covering
    words' keys with each alternative written in), span (token range), flags and its source text."""
    t = strip_comments(t)
    marks = find_marks(t, names)
    pieces, pos = [], 0
    for i, m in enumerate(marks):
        pieces.append(t[pos:m["s"]])
        if m["name"] in ("illegible", "ill"):
            m["raw_alts"] = None
            m["kind"] = "illegible"
            inner = ILL
        else:
            arg = NESTED_ILL.sub(ILL, NESTED_UNS.sub("{", m["arg"] or "")) if m["nested"] else (m["arg"] or "")
            m["raw_alts"] = alternatives(arg) if m["name"] == "unsure" else [arg]
            m["kind"] = ("choice" if len(m["raw_alts"]) > 1 else "single") if m["name"] == "unsure" else "uncertain"
            inner = m["raw_alts"][0]
        pieces += [chr(0xF0000 + i), inner, chr(0x100000 + i)]  # this mark's own sentinels
        m["flags"] = context_flags(t, m["s"])
        m["text"] = t[m["s"]:m["e"]][:300]
        pos = m["e"]
    pieces.append(t[pos:])
    plain = to_plain("".join(pieces), drop_env)
    starts, ends = {}, {}
    for q, ch in enumerate(plain):
        o = ord(ch)
        if 0xF0000 <= o < 0x100000:
            starts[o - 0xF0000] = q
        elif o >= 0x100000:
            ends[o - 0x100000] = q
    words = words_of(plain)
    toks = []
    live = [(i, starts[i], ends[i]) for i in range(len(marks)) if i in starts and i in ends]
    carry, carry_a = set(), None  # marks of a word that is only punctuation, e.g. "(" glued to \unsure{...}
    for key, a, b in words:
        ms = set(i for i, s, e in live if s < b and e >= a)
        if not key:
            if ms:
                carry |= ms
                carry_a = a if carry_a is None else carry_a
            continue
        if carry:
            ms |= carry
            a = carry_a
            carry, carry_a = set(), None
        toks.append((key, frozenset(ms) if ms else None, a, b))
    if carry:  # punctuation-only marks at the very end
        if toks:
            k0, m0, a0, b0 = toks[-1]
            toks[-1] = (k0, frozenset((m0 or set()) | carry), a0, b0)
        else:
            toks.append(("⟨empty⟩", frozenset(carry), carry_a, len(plain)))
    for i in range(len(marks)):  # a mark whose reading is empty still needs a token
        if i in starts and i in ends and not any(tk[1] and i in tk[1] for tk in toks):
            pos_i = starts[i]
            q = next((q for q, tk in enumerate(toks) if tk[2] >= pos_i), len(toks))
            toks.insert(q, ("⟨empty⟩", frozenset({i}), pos_i, ends[i] + 1))
    for i, m in enumerate(marks):
        if i not in starts or i not in ends:
            m.update(span=(0, 0), alts=[], lost=True, lost_in=enclosing(t, m["s"]))
            continue
        cov = [q for q, tk in enumerate(toks) if tk[1] and i in tk[1]]
        if not cov:
            m.update(span=(0, 0), alts=[], lost=True, lost_in="(no words)")
            continue
        q0, q1 = cov[0], cov[-1] + 1
        region_a, region_b = toks[q0][2], toks[q1 - 1][3]
        alts = []
        for raw in (m["raw_alts"] if m["raw_alts"] is not None else [ILL]):
            alt_plain = plain[region_a:starts[i]] + to_plain(raw) + plain[ends[i] + 1:region_b]
            alts.append([w for w, _, _ in words_of(alt_plain) if w])
        m.update(span=(q0, q1), alts=alts, lost=False, lost_in="")
    return [(k, ms) for k, ms, _, _ in toks], marks


NESTED_UNS = re.compile(r"\\unsure(?=\{)")
NESTED_ILL = re.compile(r"\\illegible\{[^{}]*\}")


def enclosing(t, s):
    """The innermost command or environment around position s whose content the tokenizer drops."""
    best = ""
    for m in re.finditer(r"\\begin\{(tikzpicture|tikzcd)\}", t[:s]):
        e = t.find("\\end{" + m.group(1) + "}", m.end())
        if e < 0 or e > s:
            best = m.group(1)
    for m in re.finditer(r"\\([A-Za-z]+)\s*\{", t[:s]):
        if m.group(1) in DROP and close_brace(t, m.end() - 1) > s:
            best = m.group(1)
    return best or "(other)"


def align(a_toks, b_toks):
    sm = difflib.SequenceMatcher(None, [k for k, _ in a_toks], [k for k, _ in b_toks], autojunk=False)
    amap = {}
    ops = sm.get_opcodes()
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            for d in range(i2 - i1):
                amap[i1 + d] = j1 + d
    return amap, ops, sm.ratio()


def segment(amap, a_len, b_len, a0, a1):
    left = next((i for i in range(a0 - 1, -1, -1) if i in amap), None)
    right = next((i for i in range(a1, a_len) if i in amap), None)
    b0 = amap[left] + 1 if left is not None else 0
    b1 = amap[right] if right is not None else b_len
    c0 = left + 1 if left is not None else 0
    c1 = right if right is not None else a_len
    return (c0, c1), (b0, max(b0, b1))


def classify(mark, a_toks, b_toks, amap, b_marks, slack=12):
    """What text b has at the place of a's mark -> (outcome, b's reading there, detail)."""
    if mark.get("lost"):
        return "not aligned (mark inside a dropped command)", "", ""
    a0, a1 = mark["span"]
    (c0, c1), (b0, b1) = segment(amap, len(a_toks), len(b_toks), a0, a1)
    seg = b_toks[b0:b1]
    keys = [k for k, _ in seg]
    reading = " ".join(keys)
    width = a1 - a0
    if (c1 - c0) - width > slack or len(seg) - width > slack:
        return "not aligned (large rewrite here)", reading[:200], ""
    pre = [k for k, _ in a_toks[c0:a0]]
    post = [k for k, _ in a_toks[a1:c1]]
    kinds = sorted({b_marks[j]["kind"] for _, ms in seg if ms for j in ms}) if b_marks is not None else []
    alts = mark["alts"]
    if mark["kind"] == "illegible":
        if not seg:
            return "nothing there", "", ""
        if "illegible" in kinds:
            return "still illegible", reading[:200], ""
        if kinds:
            return "narrowed to a doubtful reading", reading[:200], ",".join(kinds)
        return "read", reading[:200], ""
    if kinds:
        same = any(keys == pre + a + post or keys == a for a in alts)
        return ("still doubtful, same reading" if same else "still doubtful, reading changed"), reading[:200], ",".join(kinds)
    for k, a in enumerate(alts):
        if keys == pre + a + post or keys == a:
            return ("first reading confirmed" if k == 0 else "another listed alternative chosen"), reading[:200], str(k)
    for k, a in enumerate(alts):
        n = len(a)
        if n and any(keys[q:q + n] == a for q in range(len(keys) - n + 1)):
            return ("first reading confirmed (neighbours changed)" if k == 0 else
                    "another listed alternative chosen (neighbours changed)"), reading[:200], str(k)
    if not seg:
        return "nothing there", "", ""
    lo = [loose(k) for k in keys if loose(k)]
    for k, a in enumerate(alts):
        if lo == [loose(x) for x in pre + a + post if loose(x)] or lo == [loose(x) for x in a if loose(x)]:
            return "same up to accents, case or punctuation", reading[:200], str(k)
    return "a reading not among the alternatives", reading[:200], ""


def unmarked_changes(a_toks, b_toks, ops):
    """Changed blocks of a with no doubt mark on either side: (blocks, words, blocks that differ only in accents,
    case or punctuation)."""
    blocks = words = trivial = 0
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            continue
        if any(ms for _, ms in a_toks[i1:i2]) or any(ms for _, ms in b_toks[j1:j2]):
            continue
        blocks += 1
        words += max(i2 - i1, j2 - j1)
        if [loose(k) for k, _ in a_toks[i1:i2] if loose(k)] == [loose(k) for k, _ in b_toks[j1:j2] if loose(k)]:
            trivial += 1
    return blocks, words, trivial


def new_marks(a_toks, b_toks, b_marks, ops):
    """b's marks that sit where a had no mark."""
    new, old = set(), set()
    for tag, i1, i2, j1, j2 in ops:
        if tag == "equal":
            for d in range(i2 - i1):
                ms = b_toks[j1 + d][1]
                if ms:
                    (old if a_toks[i1 + d][1] else new).update(ms)
            continue
        a_has = any(ms for _, ms in a_toks[i1:i2])
        for _, ms in b_toks[j1:j2]:
            if ms:
                (old if a_has else new).update(ms)
    return [b_marks[m]["kind"] for m in sorted(new - old)]
