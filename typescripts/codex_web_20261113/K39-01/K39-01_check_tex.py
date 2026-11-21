"""Run with Python 3. Checks the supplied page fragments without invoking TeX."""
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SCANS = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
COMMANDS = set("""
cotefile scanpage mspage unsure illegible handwritten deleted inserted margin diagram figure uline uuline
Big Lambda Leftrightarrow Longleftarrow Longleftrightarrow Longrightarrow Theta Updownarrow
alpha approx arrow begin big bigl bigr cap cdot circ cos det dim dot downarrow end exists exp forall
frac geq hookrightarrow hspace in int ldots left leftarrow leq log longmapsto longrightarrow mapsto
mathbb mathbin mathcal mathfrak mathrel mathrm mathscr mu otimes overline overset partial pi qquad quad
right sim simeq sin subset substack sum supset text times to underbrace underline underset varepsilon varphi
widehat xi xrightarrow notin neq mathbf not mathop prod epsilon phi prime cdots
""".split())
ENVIRONMENTS = {"aligned", "cases", "tikzcd", "array", "tikzpicture"}
TOKENS = re.compile(r'\\(?:begin|end)\{[A-Za-z*]+\}|\\[A-Za-z]+|\\[^\n]|%[^\n]*|[{}$]')
SPECIALS = set(r"\{}[],$ ;:&%!_#".replace(" ", "")) | {" "}
def check(text, name):
    stack, math, env, counts = [], [], [], Counter()
    def error(token, message):
        line = text.count("\n", 0, token.start()) + 1
        raise ValueError(f"{name}:{line} {message}")
    for token in TOKENS.finditer(text):
        s = token.group()
        if s.startswith('%'):
            continue
        if s == '{':
            stack.append(token.start())
        elif s == '}':
            if not stack:
                error(token, "closing brace without opening brace")
            stack.pop()
        elif s == '$':
            if math and math[-1] == '$':
                math.pop()
            else:
                math.append('$')
        elif s == r'\[':
            if math:
                error(token, "opening display overlaps other math")
            math.append(s)
        elif s == r'\]':
            if not math or math.pop() != r'\[':
                error(token, "unpaired closing display")
        elif s.startswith((r'\begin{', r'\end{')):
            environment = s.split('{')[1][:-1]
            if environment not in ENVIRONMENTS:
                error(token, "unrecognized environment " + environment)
            if s.startswith(r'\begin'):
                env.append(environment)
            elif not env or env.pop() != environment:
                error(token, "environment mismatch")
        elif s[1:].isalpha():
            if s[1:] not in COMMANDS:
                error(token, "unknown control word " + s)
            counts[s[1:]] += 1
        elif s[1:] not in SPECIALS:
            error(token, "unknown control symbol " + s)
    if stack or math or env:
        raise ValueError(f"{name}: unclosed braces={len(stack)}, math={math}, environments={env}")
    return counts

if __name__ == "__main__":
    pages = sorted((ROOT / 'pages').glob('*.tex'))
    assert [int(p.stem[-3:]) for p in pages] == SCANS
    joined = b''.join(p.read_bytes() for p in pages)
    assert joined == (ROOT / 'K39-01_transcription.tex').read_bytes()
    total = Counter()
    for i, page in enumerate(pages):
        text = page.read_text()
        assert re.findall(r'\\scanpage\{(\d+)\}', text) == [str(SCANS[i])]
        assert text.count(r'\cotefile{39}') == int(i == 0)
        counts = check(text, page.name)
        total.update(counts)
        print(f"{SCANS[i]:03}  unsure {counts['unsure']:2}  illegible {counts['illegible']}  deleted {counts['deleted']:2}  OK")
    assert joined.startswith(b'\\cotefile{39}\n\\scanpage{3}\n')
    check(joined.decode(), "assembled fragment")
    print("16 pages and assembled fragment passed. The assembled bytes match the pages.")
    print("Totals", {k:total[k] for k in ('unsure','illegible','deleted','inserted','margin','diagram')})
