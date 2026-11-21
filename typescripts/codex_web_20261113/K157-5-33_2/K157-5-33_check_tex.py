"""Static structural checks for these manuscript pages. Run from any directory."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
KEY="K157-5-33"
ARCHIVAL=set("cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD=set("""Big Bigg Delta Longrightarrow Pi Rightarrow alpha approx ast begin beta cdot circ end exists
forall geq hphantom hspace in lambda left leftarrow leq lim limits longleftarrow longmapsto longrightarrow mapsto mathbb mathcal mathop mathord
csname endcsname cong mathrm mathscr mkern natural ne node nwarrow overline prime pi qquad quad relbar rho rule right scanpage scriptsize sharp sigma sim simeq
subset sup textcircled textsuperscript times to underbrace underline""".split())
PACKAGES=set("arrow bigcup boxed draw mathbb mathscr overset shortparallel tag text underset varinjlim varprojlim vphantom xrightarrow".split())
ENV=set("aligned gathered tikzcd tikzpicture".split())
TOKEN=re.compile(r"\\(?:begin|end)\{[^}]+\}|\\[A-Za-z]+|\\.|[{}$]")

def check(name,source):
    source=re.sub(r"(?<!\\)%[^\n]*","",source)
    assert all(m == "tagsleft@true" for m in re.findall(r"\\csname\s*(.*?)\\endcsname", source, re.S)), "Unknown constructed control word"
    errors=[]
    nesting=[]; env=[]; math=[]; used=set()
    def problem(m,message):
        line=source.count("\n",0,m.start())+1
        errors.append(f"{name}:{line}: {message}")
    for m in TOKEN.finditer(source):
        v=m.group()
        if v.startswith((r"\begin{",r"\end{")):
            value=v.split("{",1)[1][:-1]
            if value not in ENV:problem(m,"unrecognised environment "+value)
            if v.startswith(r"\begin"):
                env.append(value)
                if value=="tikzcd" and not source[m.end():].startswith(r"[ampersand replacement=\&"):
                    problem(m,"tikzcd lacks the explicit cell separator setting")
            elif not env or env.pop()!=value:problem(m,"mismatched environment "+value)
        elif v=="{":nesting.append(m.start())
        elif v=="}":
            if nesting:nesting.pop()
            else:problem(m,"stray closing brace")
        elif v=="$":
            if math and math[-1]=="$":math.pop()
            else:math.append("$")
        elif v in (r"\[",r"\("):math.append(v)
        elif v in (r"\]",r"\)"):
            expected={r"\]":r"\[",r"\)":r"\("}[v]
            if not math or math.pop()!=expected:problem(m,"math delimiter mismatch "+v)
        elif re.fullmatch(r"\\[A-Za-z]+",v):
            used.add(v[1:])
            if v[1:] not in ARCHIVAL|STANDARD|PACKAGES:problem(m,"unrecognised control word "+v)
    if nesting or math or env:errors.append(f"{name}: closure stack {len(nesting)} braces, {math}, {env}")
    return errors,used

def main():
    pages=sorted((ROOT/"pages").glob("*.tex"))
    nums=list(range(513,528))
    assert [int(p.stem[-3:]) for p in pages]==nums
    ms=[425,426,426,*range(427,439)]
    rows=[];errors=[];used=set()
    for n,manuscript,p in zip(nums,ms,pages):
        src=p.read_text()
        e,words=check(p.name,src);errors.extend(e);used|=words
        assert re.findall(r"\\scanpage\{(\d+)\}",src)==[str(n)]
        assert re.findall(r"\\mspage\{(\d+)\}",src)==[str(manuscript)]
        assert re.findall(r"^% archive sheet number: (\d+)$",src,re.M)==[str(n-1)]
        rows.append(f"| {n} | {manuscript} | {n-1} | {'passed' if not e else 'failed'} |")
    total=(ROOT/f"{KEY}_transcription.tex").read_text()
    assert total=="".join(p.read_text() for p in pages)
    assert total.startswith(r"\cotefile{157-5}"+"\n"+r"\scanpage{513}") and total.count(r"\cotefile")==1
    assert r"\documentclass" not in total
    assert (ROOT/f"{KEY}_standalone.tex").read_text().splitlines()==[
        r"\input{PREAMBLE.tex}",r"\begin{document}",r"\input{K157-5-33_transcription}",r"\end{document}"]
    assert all(re.search(r"\\(?:newcommand|renewcommand)\{\\"+m+r"\}",(ROOT/"PREAMBLE.tex").read_text()) or m in {"uline","uuline"} for m in ARCHIVAL)
    report=["# Static LaTeX verification","","| Scan | Manuscript | Archive folio | Delimiters and commands |","|---|---|---|---|",*rows,
        "\nBrace groups, inline dollar pairs, display and parenthesized math delimiters, named environments and the allowable control-word vocabulary were checked independently in each page. Scan and folio identifiers, the wrapper, and exact page concatenation were checked separately. The page files preserve incomplete manuscript parentheses as reading evidence. The six manuscript display labels use the scoped amsmath left-tag setting. No TeX engine was run.",
        "\nControl words encountered, excluding environment delimiters and single-character controls:\n",
        ", ".join(chr(96)+w+chr(96) for w in sorted(used))+"\n"]
    if errors:raise ValueError("\n".join(errors))
    (ROOT/f"{KEY}_syntax.md").write_text("\n".join(report))
    print(f"{len(pages)} pages passed, {len(used)} control words, exact concatenation and wrapper passed")

if __name__=="__main__":main()
