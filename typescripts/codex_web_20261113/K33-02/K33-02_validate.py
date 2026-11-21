"""Check the diplomatic TeX sources without invoking a typesetter. Run with Python 3."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
ALLOWED = set("""
cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible
Downarrow Gamma Phi S alpha arrow bar begin beta big bigl bigr binom cap cdot diagdown diagup
displaystyle ell end frac gamma geq hfill hookrightarrow in lambda ldots left leq longrightarrow
mathbb mathbin mathcal mathrel mathrm mid mu neq nu omega otimes overset partial pm psi
qquad quad rho right sim simeq sqrt sum text textcircled textsuperscript tilde to underline
varepsilon varphi vert wr xi xrightarrow
""".split())
ENVS = {"aligned", "tikzcd"}
LEX = re.compile(r"\\(?:begin|end)\{[A-Za-z*]+\}|\\[A-Za-z]+|\\.|%[^\n]*|[{}$]")

def check(path):
    text = path.read_text(encoding="utf-8")
    groups, environments, mode, issues = [], [], None, []
    for token in LEX.finditer(text):
        s = token.group()
        line = text.count("\n", 0, token.start()) + 1
        def issue(message):
            issues.append(f"{path.name}:{line}: {message}")
        if s.startswith("%"):
            continue
        if s == "{":
            groups.append(line)
        elif s == "}":
            if groups:
                groups.pop()
            else:
                issue("unexpected closing brace")
        elif s.startswith((r"\begin{", r"\end{")):
            env = s[s.index("{") + 1:-1]
            if env not in ENVS:
                issue("unknown environment " + env)
            if s.startswith(r"\begin"):
                environments.append(env)
            elif not environments or environments.pop() != env:
                issue("unmatched end of " + env)
        elif s == "$":
            if mode == "display":
                issue("inline delimiter nested in display")
            else:
                mode = None if mode == "inline" else "inline"
        elif s == r"\[":
            if mode is not None:
                issue("nested display delimiter")
            mode = "display"
        elif s == r"\]":
            if mode != "display":
                issue("unexpected end of display")
            mode = None
        elif re.fullmatch(r"\\[A-Za-z]+", s) and s[1:] not in ALLOWED:
            issue("unknown command " + s)
    if groups or environments or mode:
        issues.append(f"{path.name}: unfinished groups at {groups}, environments {environments}, math mode {mode}")
    return issues

def main():
    pages = [ROOT/"pages"/f"K33-02_33_scan{i:03}.tex" for i in range(18,34)]
    whole = ROOT/"K33-02_transcription.tex"
    errors = []
    for n, path in enumerate(pages,18):
        errors.extend(check(path))
        page = path.read_text()
        prefix = (r"\cotefile{33}"+"\n" if n == 18 else "")+rf"\scanpage{{{n}}}"+"\n"
        if not page.startswith(prefix) or page.count(r"\scanpage{") != 1:
            errors.append(f"{path.name}: scan identification")
    if whole.read_bytes() != b"".join(p.read_bytes() for p in pages):
        errors.append("assembled fragment differs from page concatenation")
    if whole.read_text().count(r"\cotefile{33}") != 1:
        errors.append("cote identification")
    print("\n".join(errors) if errors else "PASS: 16 pages, 1 exact concatenation; braces, displays, inline math, environments, command names and scan identifiers.")
    return int(bool(errors))

if __name__ == "__main__":
    sys.exit(main())
