"""Write the English pages and check them against the French source (no model).

For each page with a parsed answer (GPT-6.1 Sol at reasoning effort max): drop anything the model put before the
first \\scanpage (the request's own header line), then compare with the source page:
- the \\scanpage and \\mspage commands, in order;
- the counts of the markup commands \\deleted, \\inserted, \\unsure, \\margin, \\illegible, \\uline, \\handwritten;
- every math span ($...$, \\[...\\], \\(...\\), equation-like environments), compared as a multiset after removing
  the text inside \\text{...}, \\mathrm{...}, \\textrm{...} and \\mbox{...} (which may hold translated words).
A page passing all three goes to <cote>/<source page name>; a page failing one is written too, with the failures
listed in CHECK.tsv, so a reader can look at it.
17 Nov 2026, Claude Opus 5.5 at effort high. usage: python -I -B finalize.py"""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
R = pathlib.Path(__file__).resolve().parent.parent
import os
W = R / os.environ.get("WORK", "_work")  # _work: first job (first-pass pages); _work2: second-pass pages
T = R.parent
BS = chr(92)
MARK = ["deleted", "inserted", "unsure", "margin", "illegible", "uline", "handwritten"]
MATH = re.compile(r"\$\$.*?\$\$|\$(?:\\.|[^$\\])+\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{(align\*?|equation\*?|gather\*?|eqnarray\*?|array)\}.*?\\end\{\1\}", re.S)
TXT = re.compile(r"\\(?:text|mathrm|textrm|mbox|textit|emph)\{[^{}]*\}")


def pages(t):
    return re.findall(r"\\(scanpage|mspage)\{([^}]*)\}", t)


def marks(t):
    return {m: len(re.findall(re.escape(BS + m) + r"\b", t)) for m in MARK}


def maths(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    return collections.Counter(re.sub(r"\s+", "", TXT.sub("", m.group(0))) for m in MATH.finditer(t))


rows = ["page\tcote\tsource\tscan/ms pages\tmarkup counts\tmath spans\tverdict"]
n = collections.Counter()
for line in (W / "files.tsv").read_text(encoding="utf-8").splitlines()[1:]:
    oid, cote, src = line.split("\t")[:3]
    out = W / "out" / f"{oid}.tex"
    if not out.exists():
        rows.append(f"{oid}\t{cote}\t{src}\t\t\t\tnot translated yet")
        n["missing"] += 1
        continue
    s = (T / src).read_text(encoding="utf-8")
    e = out.read_text(encoding="utf-8")
    first = s.lstrip().split("\n", 1)[0]
    if first.startswith(BS + "scanpage") and BS + "scanpage" in e:
        e = e[e.index(BS + "scanpage"):]
    p_ok = pages(s) == pages(e)
    ms, me = marks(s), marks(e)
    m_bad = [k for k in MARK if ms[k] != me[k]]
    xs, xe = maths(s), maths(e)
    x_bad = sum(((xs - xe) + (xe - xs)).values())
    ok = p_ok and not m_bad and not x_bad
    dst = R / cote / pathlib.Path(src).name
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(e.rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    rows.append(f"{oid}\t{cote}\t{src}\t{'ok' if p_ok else 'DIFFER'}\t{'ok' if not m_bad else ','.join(m_bad)}\t"
                f"{'ok' if not x_bad else str(x_bad) + ' differ'}\t{'OK' if ok else 'CHECK'}")
    n["OK" if ok else "CHECK"] += 1
(R / ("CHECK.tsv" if W.name == "_work" else "CHECK_SECOND_PASS.tsv")).write_text("\n".join(rows) + "\n", encoding="utf-8")
print(dict(n))
