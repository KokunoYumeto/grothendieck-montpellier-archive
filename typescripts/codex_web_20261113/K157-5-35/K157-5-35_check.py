"""Static checks for the diplomatic fragment. Invoke with Python 3; no TeX engine is used."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent
NAME = "K157-5-35"
HOUSE = set("cotefile scanpage mspage handwritten deleted inserted margin uline uuline "
            "diagram figure unsure illegible".split())
STANDARD = set("Longleftrightarrow Longrightarrow Vert alpha baselineskip begin beta big "
               "bigcup circ colon displaywidth end exists forall geq iff in infty joinrel "
               "ldots leq lfloor lhook lim longmapsto longrightarrow makebox mapsto "
               "mapstochar mathbin mathrm mid ne noindent overline pi qquad quad relbar "
               "rfloor rule setminus sim simeq smash subset tau textsuperscript to "
               "underbrace underline xi hookrightarrow".split())
PACKAGES = set("arrow mathbb mathcal mathfrak mathscr operatorname overset substack tag "
               "text underset varinjlim varnothing varprojlim".split())
ENVIRONMENTS = {"aligned", "tikzcd", "tikzpicture", "array"}
TOKEN = re.compile(r"\\[A-Za-z]+|\\.|\n|[{}$]")
MATH_ENVS = {"aligned", "array"}
PAGES = [ROOT / "pages" / f"{NAME}_157-5_scan{n}.tex" for n in range(543,558)]
WRAPPER = "\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{"+NAME+"_transcription}\n\\end{document}\n"

def inspect(path, n):
    raw = path.read_text(encoding="utf-8")
    assert re.findall(r"\\scanpage\{(\d+)\}", raw) == [str(n)], path
    assert raw.count("\\mspage{") == 1, path
    assert raw.splitlines().count(f"% archive sheet number: {n-1}") == 1, path
    source = re.sub(r"(?<!\\)%[^\n]*", "", raw)
    braces = []
    environments = []
    math = None
    for m in TOKEN.finditer(source):
        token = m[0]
        line = source.count("\n", 0, m.start()) + 1
        location = f"{path.name}:{line}"
        if token == "{":
            braces.append(line)
        elif token == "}":
            assert braces, f"Closing brace without an opening brace at {location}"
            braces.pop()
        elif token == "$":
            assert math in (None, "$"), f"Dollar inside display math at {location}"
            math = None if math else "$"
        elif token == "\\[":
            assert math is None, f"Nested math delimiter at {location}"
            math = "\\["
        elif token == "\\]":
            assert math == "\\[", f"Closing display without an opening at {location}"
            math = None
        elif token == "\n" and math:
            assert not re.match(r"[ \t]*\n", source[m.end():]), f"Paragraph in math at {location}"
        elif token.startswith("\\") and token[1:].isalpha():
            cmd = token[1:]
            assert cmd in HOUSE | STANDARD | PACKAGES, f"Unknown control word {token} at {location}"
            if cmd in ("begin", "end"):
                env_match = re.match(r"\{([a-zA-Z*]+)\}", source[m.end():])
                assert env_match and env_match[1] in ENVIRONMENTS, location
                env = env_match[1]
                if cmd == "begin":
                    assert env not in MATH_ENVS or math, f"Math environment outside math at {location}"
                    environments.append(env)
                else:
                    assert environments and environments.pop() == env, f"Environment mismatch at {location}"
    assert not braces and not environments and not math, (path, braces, environments, math)
    for diagram in re.findall(r"\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}", source, re.S):
        assert diagram.startswith("[ampersand replacement=\\&"), path
        assert not re.search(r"(?<!\\)&", diagram), f"Unescaped diagram cell separator in {path}"
    return raw

def main():
    assert sorted((ROOT / "pages").glob("*.tex")) == PAGES
    pieces = [inspect(p, n) for n,p in enumerate(PAGES,543)]
    assembled = (ROOT / f"{NAME}_transcription.tex").read_bytes()
    assert assembled == b"".join(p.read_bytes() for p in PAGES), "Assembly differs from page files"
    assert pieces[0].startswith("\\cotefile{157-5}\n\\scanpage{543}\n")
    assert sum(s.count("\\cotefile{") for s in pieces) == 1
    assert (ROOT / f"{NAME}_standalone.tex").read_text() == WRAPPER
    assert (ROOT / "PREAMBLE.tex").is_file()
    with (ROOT / f"{NAME}_inventory.csv").open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    assert all(r["transcribed"]=="yes" for r in records)
    for n,piece in enumerate(pieces,543):
        rows=[r for r in records if int(r["scan"])==n]
        assert [int(r["element"]) for r in rows]==list(range(1,len(rows)+1))
        for cmd,kind in (("deleted","deletion"),("inserted","insertion"),("diagram","diagram")):
            assert piece.count("\\"+cmd+"{")==sum(r["kind"]==kind for r in rows),(n,cmd)
        assert sum(m[0] == "\\[" for m in TOKEN.finditer(piece)) == sum(r["kind"]=="display" for r in rows),(n,"display")
        assert sum(r["kind"]=="margin note" for r in rows)==piece.count("\\margin{")+piece.count("\\rule["),(n,"margin")
    totals = {cmd:sum(s.count("\\"+cmd+"{") for s in pieces)
              for cmd in ("unsure","illegible","deleted","inserted","margin","diagram")}
    print(f"PASS · {len(pieces)} page files · matching assembly and wrapper · {len(records)} inventory rows")
    print(" · ".join(f"{k} {v}" for k,v in totals.items()))

if __name__ == "__main__":
    main()
