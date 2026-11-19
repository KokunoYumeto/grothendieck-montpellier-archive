"""Print SA12 transcription pages compactly for study (sweep 3, lead of SA12: Claude Opus 5.5 at effort max).

python -I -B readtex_sa12.py <cote> <first_scan> <last_scan> [keepdel] [--nodiag] [--witness]

For each scan it prints the current reading: the page of the FINAL Pro package where one exists
(returns/<pkg>_unzipped, never a checkpoint folder), else the Codex-web transcription of the folder that holds the
scan (codex_web_20261113/returns/<folder>/out/<folder>_transcription.tex). The header line names the source and the
second witness when there is one. With --witness the Codex-web text is printed as well where both exist.
Cancelled text (\\deleted) is dropped unless keepdel; \\unsure{a|b} -> a(?); figures dropped; margins inline.
Reused typescripts with Bourbaki-type numbers (n° 280, 329, 339, 385, 391) are reduced to one line.
"""
import re, sys, glob
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
PRO = {"29": ["MPL_29_049-094", "MPL_29_095-140", "MPL_29_141-187"], "31": ["MPL_31_002-051"],
       "33": ["MPL_33_002-049", "MPL_33_050-097"]}
CODEX = ["A29-01", "C29-01", "C29-02", "C29-03", "C29-04", "C29-05", "C29-06", "C29-07", "K29-01", "K29-02", "K29-03",
         "K29-04", "K29-05", "K29-06", "K29-07", "K29-08", "K29-09", "K29-10", "K29-11", "K31-01", "K31-02", "K31-03",
         "B37-01", "B37-02", "B37-03", "B37-04", "B37-05", "C32-01", "H35-01", "H37-01"]


def arg_end(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] == "{" and (j == 0 or s[j - 1] != "\\"):
            d += 1
        elif s[j] == "}" and s[j - 1] != "\\":
            d -= 1
            if d == 0:
                return j + 1
    return len(s)


def strip_cmd(s, name, repl):
    out, i = [], 0
    pat = "\\" + name + "{"
    while True:
        k = s.find(pat, i)
        if k < 0:
            out.append(s[i:])
            break
        out.append(s[i:k])
        b = k + len(pat) - 1
        e = arg_end(s, b)
        out.append(repl(s[b + 1:e - 1]))
        i = e
    return "".join(out)


def clean(s, keepdel=False):
    s = re.sub(r"(?m)^%.*$", "", s)
    if not keepdel:
        s = strip_cmd(s, "deleted", lambda a: "")
    else:
        s = strip_cmd(s, "deleted", lambda a: "[del: " + a + "]")
    s = strip_cmd(s, "unsure", lambda a: a.split("|")[0] + "(?)")
    s = strip_cmd(s, "inserted", lambda a: a)
    s = strip_cmd(s, "handwritten", lambda a: a)
    s = strip_cmd(s, "uline", lambda a: a)
    s = strip_cmd(s, "uuline", lambda a: a)
    s = strip_cmd(s, "margin", lambda a: " [margin: " + a + "] ")
    s = strip_cmd(s, "figure", lambda a: "[figure]")
    s = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", "[figure]", s, flags=re.S)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def pro_pages(cote):
    out = {}
    for pkg in PRO.get(cote, []):
        for f in glob.glob(str(T / "returns" / f"{pkg}_unzipped" / "**" / "pages" / f"*_{cote}_scan*.tex"), recursive=True):
            n = int(re.search(r"scan(\d+)", f).group(1))
            out.setdefault(n, (pkg, f))
    return out


def codex_pages(cote):
    out = {}
    for fold in CODEX:
        if fold[1:3] != cote:
            continue
        p = T / "codex_web_20261113" / "returns" / fold / "out" / f"{fold}_transcription.tex"
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        parts = re.split(r"\\scanpage\{(\d+)\}", txt)
        for k in range(1, len(parts), 2):
            out.setdefault(int(parts[k]), (fold, parts[k + 1]))
    return out


def main():
    cote, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    keep = "keepdel" in sys.argv
    pro, cx = pro_pages(cote), codex_pages(cote)
    for n in range(a, b + 1):
        if n not in pro and n not in cx:
            continue
        if n in pro:
            src, txt = pro[n][0], open(pro[n][1], encoding="utf-8").read()
            wit = cx[n][0] if n in cx else ""
        else:
            src, txt = "codex " + cx[n][0], cx[n][1]
            wit = ""
        c = clean(txt, keep)
        if "--nodiag" in sys.argv:
            c = re.sub(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", "[diagram]", c, flags=re.S)
        head = f"=== {cote}:{n} [{src}" + (f"; second witness codex {wit}" if wit else "") + "]"
        if re.search(r"n\S{0,3} ?(280|329|339|385|391)\b", c[:500]):
            print(head + " [reused typescript: " + " ".join(c.split()[:16]) + " ...]")
            continue
        print(head)
        print(c)
        if "--witness" in sys.argv and wit:
            print(f"--- second witness codex {wit} ---")
            print(clean(cx[n][1], keep))


if __name__ == "__main__":
    main()
