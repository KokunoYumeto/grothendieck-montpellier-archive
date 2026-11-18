r"""List the disagreements between two or three readings of the same scan pages, as a TSV, so that the scan check
looks only at those places (third pass of 17 Nov 2026: first pass, Claude second pass, GPT-6.2 Sol).

usage:
  python -I -B tools/reconcile_readings.py LABEL=DIR LABEL=DIR [LABEL=DIR] [--scans 44-58] [--out FILE.tsv]
                                           [--keep-tikz] [--context 5]

Each DIR holds one TeX file per scan page; a page is matched across readings by the number after "scan" in its file
name (MPL_148_029-072_148_scan044.tex, CTRL-148_148_scan044.tex, ...). A DIR may also be a single assembled file with
\\scanpage{N} markers. The first reading is the base: locators (line numbers) refer to its page files.

How the texts are compared:
- each page is cut into tokens: words, numbers, LaTeX commands, and single signs (^ _ ' ( ) = ...); braces, $, \\[ \\],
  spacing commands, comments, \\scanpage and \\cotefile are dropped, quotes are normalised (`` '' and the « » forms);
- \\unsure{a|b|...} contributes the tokens of its first reading, marked; the other readings are shown in the TSV but
  not compared;
- \\deleted{...} contributes its tokens with a leading "~", so a struck word read as live is a disagreement;
- \\illegible{n} is one token "<ill>"; \\inserted, \\margin, \\uline and the other text macros are transparent;
- \mathscr and \mathcal, \varepsilon and \epsilon count as the same (typeface variants the control verdicts
  do not count) unless --strict;
- tikzpicture drawings are left out (as in the control verdicts) unless --keep-tikz.

Output columns: scan, base_line, before, after (a few base tokens around the place), pattern (which readings agree,
e.g. "A=B≠C", "A≠B≠C"), marked (the labels whose reading at the place carries a doubt mark), and one column per
reading with its TeX source at the place. A summary per page goes to stderr.
"""
import argparse
import difflib
import pathlib
import re
import sys

DROP_CMDS = {r"\scanpage", r"\cotefile", r"\,", r"\;", r"\:", r"\!", r"\ ", r"\quad", r"\qquad", r"\hfill",
             r"\noindent", r"\par", r"\medskip", r"\smallskip", r"\bigskip", r"\newline", r"\\", r"\left", r"\right",
             r"\big", r"\Big", r"\bigl", r"\bigr", r"\Bigl", r"\Bigr", r"\displaystyle", r"\textstyle", r"\ldots",
             r"\dots", r"\cdots"}
TRANSPARENT = {r"\inserted", r"\margin", r"\uline", r"\uuline", r"\textit", r"\emph", r"\textbf", r"\text",
               r"\mathrm", r"\textup", r"\mbox", r"\hbox", r"\underline", r"\interline", r"\note", r"\marginnote"}
QUOTES = {"``": '"', "''": '"', "«": '"', "»": '"', "“": '"', "”": '"', "‘": "'", "’": "'"}
# typeface variants the control verdicts do not count (ℰ/𝓔, ε/ϵ); --strict keeps them apart
FOLD = {r"\mathscr": r"\mathcal", r"\varepsilon": r"\epsilon", r"\textup": ""}
STRICT = False
TOK = re.compile(r"\\[A-Za-z]+|\\.|``|''|[^\W_]+|\S", re.U)


def brace_end(s, i):
    """s[i] == '{'; index just after the matching '}' (or len(s))."""
    d = 0
    for k in range(i, len(s)):
        c = s[k]
        if c == "\\":
            continue
        if c == "{" and (k == 0 or s[k - 1] != "\\"):
            d += 1
        elif c == "}" and (k == 0 or s[k - 1] != "\\"):
            d -= 1
            if d == 0:
                return k + 1
    return len(s)


def split_top(s, sep="|"):
    out, d, cur = [], 0, []
    for k, c in enumerate(s):
        if c == "{" and (k == 0 or s[k - 1] != "\\"):
            d += 1
        elif c == "}" and (k == 0 or s[k - 1] != "\\"):
            d -= 1
        if c == sep and d == 0 and (k == 0 or s[k - 1] != "\\"):
            out.append("".join(cur))
            cur = []
        else:
            cur.append(c)
    out.append("".join(cur))
    return out


def clean(text, keep_tikz=False):
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    if not keep_tikz:
        text = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
                      lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return text


def tokens(text, offset=0, marked=False, struck=False, span=None, keep_tikz=False):
    """list of (norm, start, end, marked); start/end index the source (the enclosing macro for marked tokens)."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        m = TOK.match(text, i)
        if not m:
            i += 1
            continue
        t = m.group(0)
        j = m.end()
        a, b = (span if span else (offset + m.start(), offset + j))
        if t in (r"\unsure", r"\deleted", r"\illegible", r"\scanpage", r"\cotefile") or t in TRANSPARENT:
            k = j
            while k < n and text[k] in " \t":
                k += 1
            if k < n and text[k] == "{":
                e = brace_end(text, k)
                inner = text[k + 1:e - 1]
                if t == r"\unsure":
                    first = split_top(inner)[0]
                    sp = span if span else (offset + m.start(), offset + e)
                    out += tokens(first, offset + k + 1, True, struck, sp)
                elif t == r"\deleted":
                    out += tokens(inner, offset + k + 1, marked, True, span)
                elif t == r"\illegible":
                    out.append(("~<ill>" if struck else "<ill>", a if span else offset + m.start(),
                                b if span else offset + e, marked))
                elif t in (r"\scanpage", r"\cotefile"):
                    pass
                else:
                    out += tokens(inner, offset + k + 1, marked, struck, span)
                i = e
                continue
        i = j
        if t in DROP_CMDS or t in ("{", "}", "$", r"\[", r"\]", r"\(", r"\)", "&", "~"):
            continue
        if t in (r"\begin", r"\end"):
            k = j
            if k < n and text[k] == "{":
                e = brace_end(text, k)
                env = text[k + 1:e - 1]
                i = e
                if env in ("center", "flushleft", "flushright", "quote", "itemize", "enumerate"):
                    continue
                t = t + "{" + env + "}"
        t = QUOTES.get(t, t)
        if not STRICT and t in FOLD:
            t = FOLD[t]
            if not t:
                continue
        out.append((("~" if struck else "") + t, a, b, marked))
    return out


def read_pages(path, keep_tikz):
    p = pathlib.Path(path)
    pages = {}
    if p.is_dir():
        for f in sorted(p.glob("*.tex")):
            m = re.search(r"scan(\d{3})", f.name)
            if m:
                pages[int(m.group(1))] = f.read_text(encoding="utf-8")
    else:
        t = p.read_text(encoding="utf-8")
        parts = re.split(r"(\\scanpage\{(\d+)\})", t)
        for k in range(1, len(parts) - 2, 3):
            pages[int(parts[k + 1])] = parts[k] + parts[k + 2]
    return {n: clean(t, keep_tikz) for n, t in pages.items()}


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def mapper(ops):
    """functions mapping a base index to the other reading's index (start and end of a region)."""
    def start(i):
        for tag, i1, i2, j1, j2 in ops:
            if i1 <= i < i2 or (i1 == i2 == i):
                return j1 + (i - i1) if tag == "equal" else j1
        return ops[-1][4] if ops else 0

    def end(i):
        for tag, i1, i2, j1, j2 in ops:
            if i1 < i <= i2:
                return j1 + (i - i1) if tag == "equal" else j2
        return ops[0][3] if ops else 0
    return start, end


def regions(base, others):
    """merged base intervals [a, b) where some other reading differs."""
    iv = []
    for ops in others:
        for tag, i1, i2, j1, j2 in ops:
            if tag != "equal":
                iv.append([i1, i2])
    iv.sort()
    merged = []
    for a, b in iv:
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    return merged


def snippet(text, toks, a, b, ctx_tok=None):
    if a < b:
        s, e = min(t[1] for t in toks[a:b]), max(t[2] for t in toks[a:b])
        return text[s:e].replace("\n", " ").replace("\t", " ").strip()
    return ""


def compare(readings, scans=None, context=5):
    """readings: list of (label, {scan: text}). Yields dict rows."""
    labels = [l for l, _ in readings]
    base_label, base_pages = readings[0]
    for n in sorted(base_pages):
        if scans and n not in scans:
            continue
        texts = [pages.get(n) for _, pages in readings]
        if any(t is None for t in texts):
            yield dict(scan=n, base_line="", before="", after="", pattern="page missing in " + ",".join(
                l for l, t in zip(labels, texts) if t is None), marked="", readings=[""] * len(labels))
            continue
        toks = [tokens(t) for t in texts]
        norms = [[x[0] for x in tk] for tk in toks]
        ops = [difflib.SequenceMatcher(None, norms[0], nk, autojunk=False).get_opcodes() for nk in norms[1:]]
        maps = [mapper(o) for o in ops]
        for a, b in regions(norms[0], ops):
            spans = [(a, b)] + [(ms(a), me(b) if b > a else ms(a)) for ms, me in maps]
            seqs = [tuple(norms[k][s:e]) for k, (s, e) in enumerate(spans)]
            if len(set(seqs)) == 1:
                continue
            letters = "ABC"
            groups = {}
            for k, sq in enumerate(seqs):
                groups.setdefault(sq, []).append(letters[k])
            pattern = "≠".join("=".join(g) for g in groups.values())
            marked = ",".join(labels[k] for k, (s, e) in enumerate(spans) if any(x[3] for x in toks[k][s:e]))
            pos = toks[0][a][1] if a < len(toks[0]) else (toks[0][-1][2] if toks[0] else 0)
            yield dict(scan=n, base_line=line_of(texts[0], pos),
                       before=" ".join(norms[0][max(0, a - context):a]), after=" ".join(norms[0][b:b + context]),
                       pattern=pattern, marked=marked,
                       readings=[snippet(texts[k], toks[k], s, e) or "(nothing)" for k, (s, e) in enumerate(spans)])


def parse_scans(s):
    out = set()
    for part in s.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("readings", nargs="+", help="LABEL=DIR (2 or 3)")
    ap.add_argument("--scans")
    ap.add_argument("--out")
    ap.add_argument("--keep-tikz", action="store_true")
    ap.add_argument("--context", type=int, default=5)
    ap.add_argument("--strict", action="store_true", help=r"do not fold \mathscr/\mathcal and \varepsilon/\epsilon")
    a = ap.parse_args()
    global STRICT
    STRICT = a.strict
    if not 2 <= len(a.readings) <= 3:
        raise SystemExit("give two or three readings")
    rd = []
    for r in a.readings:
        label, _, path = r.partition("=")
        rd.append((label, read_pages(path, a.keep_tikz)))
    scans = parse_scans(a.scans) if a.scans else None
    labels = [l for l, _ in rd]
    head = ["scan", "base_line", "before", "after", "pattern", "marked"] + [f"reading_{l}" for l in labels]
    out = open(a.out, "w", encoding="utf-8", newline="\n") if a.out else sys.stdout
    if not a.out:
        sys.stdout.reconfigure(encoding="utf-8")
    out.write("# readings: " + ", ".join(f"{'ABC'[k]}={l}" for k, l in enumerate(labels)) + "\n")
    out.write("\t".join(head) + "\n")
    per = {}
    for row in compare(rd, scans, a.context):
        per[row["scan"]] = per.get(row["scan"], 0) + 1
        out.write("\t".join(str(x) for x in [row["scan"], row["base_line"], row["before"], row["after"],
                                             row["pattern"], row["marked"]] + row["readings"]) + "\n")
    if a.out:
        out.close()
    sys.stderr.write("disagreements per scan: " + ", ".join(f"{n:03d}:{c}" for n, c in sorted(per.items()))
                     + f"; total {sum(per.values())}\n")


if __name__ == "__main__":
    main()
