"""Check the diplomatic fragment structurally. Does not invoke a TeX engine."""
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parent
SCANS = [287, 288, 289, 290, 291, 292, 294, 295, 296, 297, 298, 299, 300, 301]
ARCHIVE = set("cotefile deleted diagram figure handwritten illegible inserted margin mspage scanpage uline unsure uuline".split())
LATEX = set("""S bar begin end check dim frac hspace ldots lim linewidth longleftarrow longrightarrow mathbf
mathbin mathpunct mathrm overbrace overset qquad quad resizebox text textsuperscript underline underbrace
widehat makeatletter makeatother""".split())
MATH = set("""Gamma Lambda Longleftrightarrow Omega Theta alpha amalg beta cap cdot checkmark circ delta div eta geq in
infty leq mathbb mathcal mathfrak mathscr mu ne neq not notin nu omega operatorname otimes partial pi pm prime
psi rho shortparallel sigma simeq subset substack tag tau times to underset varphi varprojlim vartheta xi xrightarrow""".split())
DRAW = {"arrow", "draw"}
INTERNAL = {"tagsleft@true", "tagsleft@false"}
ENVS = {"aligned", "tikzcd", "tikzpicture"}
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def check(path):
    text = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
    stack = []
    for m in re.finditer(r"\\(?:begin|end)\{[A-Za-z*]+\}|\\tagsleft@[a-z]+|\\[a-zA-Z]+|\\.|[{}$]", text):
        t = m[0]
        at = f"{path.name}:{1+text.count(chr(10),0,m.start())}"
        if t.startswith((r"\begin{",r"\end{")):
            which, env = t[1:-1].split("{")
            assert env in ENVS, (at,env)
            if which == "begin":
                stack.append(("environment",env))
            else:
                assert stack and stack.pop() == ("environment",env), (at,t,stack)
        elif t in ("{",r"\["):
            stack.append(t)
        elif t in ("}",r"\]"):
            assert stack and stack.pop() == ("{" if t == "}" else r"\["), (at,t,stack)
        elif t == "$":
            if stack and stack[-1] == "$":
                stack.pop()
            else:
                stack.append(t)
        elif len(t) > 1 and t[1].isalpha():
            assert t[1:] in ARCHIVE | LATEX | MATH | DRAW | INTERNAL, (at,t)
    assert not stack, (path,stack)

def verify():
    pages = [ROOT/"pages"/f"K57-18_57_scan{n}.tex" for n in SCANS]
    full = ROOT/"K57-18_transcription.tex"
    assert full.read_bytes() == b"".join(p.read_bytes() for p in pages), "page assembly"
    assert re.findall(rb"\\scanpage\{(\d+)\}",full.read_bytes()) == [str(n).encode() for n in SCANS]
    assert full.read_bytes().startswith(b"\\cotefile{57}\n\\scanpage{287}\n")
    assert full.read_text().count(r"\cotefile{")==1
    for p in [*pages,full]: check(p)
    print("PASS: 14 page files and their byte-for-byte assembly; braces, math delimiters, environments, control-sequence names, scan order.")
    return pages+[full]
if __name__ == "__main__":
    verify()

