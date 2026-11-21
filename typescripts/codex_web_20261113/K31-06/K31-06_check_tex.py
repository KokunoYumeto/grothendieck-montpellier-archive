"""Static checks of the returned LaTeX, without running a TeX engine."""
import csv
from pathlib import Path
from hashlib import sha256
import re
import sys

ROOT = Path(__file__).resolve().parent
PAGES = [33, 35, 36, 37, 38, 39, 42, 43, 44, 45, 47, 48, 49, 50, 51]
CUSTOM = set(re.findall(r'\\(?:newcommand|renewcommand)\{\\([A-Za-z]+)\}', (ROOT/'PREAMBLE.tex').read_text()))
# Standard LaTeX and the named AMS, tikz-cd, and ulem interfaces used on these pages.
STANDARD = set("""
Downarrow Gamma Leftrightarrow Longrightarrow Rightarrow alpha bar begin beta bigcap
bigoplus cap cdot chi complement ell end exists forall gamma geq in infty lambda
ldots lim longleftarrow longrightarrow mathbb mathcal mathfrak mathrm mathscr ne ni
notin operatorname otimes overline partial pi pm qquad quad sigma sim simeq subset
substack sum supset tau text textstyle textsuperscript theta times to underbrace
underline underset varphi vphantom widehat widetilde wp wr xi xrightarrow zeta
arrow uline uuline hat prime ast mapsto cdots equiv mathrm left right ge le
""".split())
ENVIRONMENTS = {'center','tikzcd','aligned'}
TOKEN = re.compile(r'\\[A-Za-z]+|\\.|[{}$%]|[^\\{}$%]+')
ENCLOSED = {'unsure','illegible','inserted','deleted','margin','handwritten','mspage','scanpage','cotefile','diagram','figure','uline','uuline'}

def check(path):
    source = path.read_text()
    stack, env, dollars, display = [], [], [], None
    commands, errors = set(), []
    for number, line in enumerate(source.splitlines(),1):
        for match in TOKEN.finditer(line):
            t = match.group()
            if t == '%':
                break
            if t == '{':
                stack.append(number)
            elif t == '}':
                if not stack:
                    errors.append(f'{number}: excess closing brace')
                else:
                    stack.pop()
            elif t == '$':
                # AMS text and \text equivalents can introduce inline math inside a display.
                if dollars and dollars[-1][0] == len(stack):
                    dollars.pop()
                else:
                    dollars.append((len(stack),number))
            elif t == r'\[':
                if display is not None:
                    errors.append(f'{number}: nested display')
                display = number
            elif t == r'\]':
                if display is None:
                    errors.append(f'{number}: unmatched display end')
                display = None
            elif t.startswith('\\') and t[1:].isalpha():
                cmd=t[1:];commands.add(cmd)
                rest=line[match.end():]
                if cmd not in STANDARD | CUSTOM:
                    errors.append(f'{number}: unrecognised control word {t}')
                if cmd in ENCLOSED and not re.match(r'\s*\{',rest):
                    errors.append(f'{number}: missing braced argument to {t}')
                if cmd in ('begin','end'):
                    m = re.match(r'\{([^{}]+)\}',rest)
                    if not m or m[1] not in ENVIRONMENTS:
                        errors.append(f'{number}: unknown environment after {t}')
                    elif cmd == 'begin':
                        env.append((m[1],number))
                    elif not env or env[-1][0] != m[1]:
                        errors.append(f'{number}: mismatched end {m[1]}')
                    else:
                        env.pop()
    if stack or env or dollars or display is not None:
        errors.append(f'open braces {stack}, environments {env}, inline dollars {dollars}, display {display}')
    for m in re.finditer(r'\\begin\{tikzcd\}(.+?)\\end\{tikzcd\}',source,re.S):
        if 'ampersand replacement=\\&' not in m[1] or re.search(r'(?<!\\)&',m[1]):
            errors.append('tikzcd cell separator or replacement option')
    return commands, errors

def check_witness_history(paths, book):
    """Reconstruct the freeze using only the returned pages and witness table."""
    history = (ROOT / "progress.log").read_text(encoding="utf-8")
    if "witness check done " not in history:
        return
    expected = {"frozen": {}, "witness": {}}
    for stage, digest, filename in re.findall(
        r"^(frozen|witness) sha256 ([0-9a-f]{64})  (.+)$", history, re.MULTILINE
    ):
        expected[stage][filename] = digest
    names = {p.relative_to(ROOT).as_posix() for p in [*paths, book]}
    assert set(expected["frozen"]) == names == set(expected["witness"])
    records = {}
    with (ROOT / "K31-06_witness.tsv").open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            records.setdefault(int(row["page"]), []).append(row)
    assert set(records) == set(PAGES)
    recovered = []
    for path in paths:
        n = int(path.stem[-3:])
        source_bytes = path.read_bytes()
        final = source_bytes.decode("utf-8")
        name = path.relative_to(ROOT).as_posix()
        assert sha256(source_bytes).hexdigest() == expected["witness"][name], name
        pieces = []
        frozen_end = 0
        final_end = 0
        for row in records[n]:
            before = row["frozen"]
            after = row["final"]
            offset = int(row["offset_in_frozen_characters"])
            assert before.startswith((r"\unsure{", r"\illegible{")), row["site"]
            assert frozen_end <= offset, row["site"]
            pos = final_end + offset - frozen_end
            assert final[pos:pos + len(after)] == after, row["site"]
            pieces.extend((final[final_end:pos], before))
            frozen_end = offset + len(before)
            final_end = pos + len(after)
        pieces.append(final[final_end:])
        original = "".join(pieces).encode("utf-8")
        assert sha256(original).hexdigest() == expected["frozen"][name], name
        recovered.append(original)
    assert sha256(book.read_bytes()).hexdigest() == expected["witness"][book.name]
    assert sha256(b"".join(recovered)).hexdigest() == expected["frozen"][book.name]
    sites = sum(len(rows) for rows in records.values())
    print(f"{sites} marked sites verified. All {len(names)} frozen and "
          f"{len(names)} post-witness hashes match.")



def main():
    paths=[ROOT/'pages'/f'K31-06_31_scan{n:03}.tex' for n in PAGES]
    assert set(paths) == set((ROOT/'pages').glob('*.tex'))
    book=ROOT/'K31-06_transcription.tex'
    assert book.read_bytes() == b''.join(p.read_bytes() for p in paths), 'assembly mismatch'
    assert book.read_text().startswith('\\cotefile{31}\n\\scanpage{33}\n')
    assert book.read_text().count('\\cotefile{31}') == 1
    assert (ROOT/'K31-06_standalone.tex').read_text().splitlines() == [
        r'\input{PREAMBLE.tex}',r'\begin{document}',r'\input{K31-06_transcription}',r'\end{document}']
    failed=False
    all_commands=set()
    for n,p in zip(PAGES,paths):
        assert re.findall(r'\\scanpage\{(\d+)\}',p.read_text()) == [str(n)]
        commands, errors=check(p)
        all_commands.update(commands)
        print(p.name, 'FAIL ' + ' | '.join(errors) if errors else 'PASS')
        failed |= bool(errors)
    print(f'{len(paths)} page files; {len(all_commands)} distinct recognised control words; assembly verified.')
    if failed:
        sys.exit(1)
    check_witness_history(paths, book)

if __name__=='__main__':
    main()

