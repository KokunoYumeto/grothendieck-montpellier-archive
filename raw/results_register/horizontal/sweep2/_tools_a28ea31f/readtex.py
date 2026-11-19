"""Print transcription pages compactly for study (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max).
python -I -B readtex.py <package> <cote> <first_scan> <last_scan> [keepdel]
Cancelled text (\\deleted) is dropped unless keepdel; \\unsure{a|b} -> a(?); figures dropped; margins inline.
"""
import re, sys, glob
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110")


def arg_end(s, i):
    """s[i] == '{'; return index after the matching '}'."""
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
    s = re.sub(r"(?m)^\s*%.*$", "", s)
    for env in ("tikzpicture", "tikzcd"):
        s = re.sub(r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}", "[diagram]" if env == "tikzpicture" else lambda m: m.group(0), s, flags=re.S)
    s = strip_cmd(s, "figure", lambda a: "[figure]")
    if not keepdel:
        s = strip_cmd(s, "deleted", lambda a: "")
    else:
        s = strip_cmd(s, "deleted", lambda a: "[del: " + a + "]")
    s = strip_cmd(s, "unsure", lambda a: a.split("|")[0] + "(?)")
    s = strip_cmd(s, "inserted", lambda a: a)
    s = strip_cmd(s, "margin", lambda a: " [margin: " + a + "] ")
    s = strip_cmd(s, "uline", lambda a: a)
    s = strip_cmd(s, "illegible", lambda a: "[illeg]")
    s = re.sub(r"\\illegible\b", "[illeg]", s)
    s = re.sub(r"\\(diagram|mspage)\b", "", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main():
    pkg, cote, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    keep = "keepdel" in sys.argv
    fs = glob.glob(str(T / "returns" / f"{pkg}*_unzipped" / "**" / "pages" / f"*_{cote}_scan*.tex"), recursive=True)
    seen = set()
    for f in sorted(fs, key=lambda x: int(re.search(r"scan(\d+)", x).group(1))):
        n = int(re.search(r"scan(\d+)", f).group(1))
        if not a <= n <= b or n in seen:
            continue
        seen.add(n)
        txt = open(f, encoding="utf-8").read()
        c = clean(txt, keep)
        if re.search(r"Tribu n|n\S{0,3} ?413|n\S{0,3} ?272|n\S{0,3} ?357", c[:400]):
            print(f"=== {cote}:{n} [reused typescript: " + " ".join(c.split()[:14]) + " ...]")
            continue
        if "--nodiag" in sys.argv:
            c = re.sub(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", "[diagram]", c, flags=re.S)
        print(f"=== {cote}:{n}")
        print(c)


if __name__ == "__main__":
    main()
