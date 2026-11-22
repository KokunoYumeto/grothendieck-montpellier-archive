"""Static checks only. Run this file with Python from any directory."""
from pathlib import Path
import re
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
TAG = "K57-15"
PAGES = (242,243,244,245,246,248,249,250,251,252,253,254,255,256)
# Control words vetted against the supplied preamble, standard LaTeX, amsmath,
# amssymb, mathrsfs, TikZ/tikz-cd, ulem and their loaded dependencies.
ALLOWED = set("""
cotefile scanpage mspage handwritten deleted inserted margin diagram figure unsure
illegible uline uuline arrow begin end rotatebox text operatorname scriptsize
mathbb mathcal mathfrak mathscr mathrm big biggl bar widehat check overline
longrightarrow to leftarrow times otimes subset cap in notin ni ge geq le leq ne
simeq sim lim underset overset underleftarrow underrightarrow xrightarrow
alpha beta gamma delta eta theta lambda xi zeta nu omega varphi partial infty
wedge underline ldots quad hfill hspace vphantom S
""".split())
ENVS = {'center','aligned','tikzcd','tikzpicture','array'}
def assert_true(condition, why):
    if not condition:
        raise ValueError(why)

def clean_lines(s):
    return re.sub(r'(?<!\\)%[^\n]*','',s)

def check_source(name, data):
    s=clean_lines(data)
    stack=[]
    env=[]
    math=[]
    words=set()
    token=r'\\(?:begin|end)\{[^{}]+\}|\\[a-zA-Z]+|\\[\s\S]|[{}$]'
    for m in re.finditer(token,s):
        t=m.group(); loc=f'{name}, line {s.count(chr(10),0,m.start())+1}'
        if t.startswith(('\\begin{','\\end{')):
            e=t[t.index('{')+1:-1]
            assert_true(e in ENVS,(loc,t))
            if t.startswith('\\begin'):
                env.append(e)
            else:
                assert_true(env and env.pop()==e,(loc,t,'environment mismatch'))
        elif t=='{':
            stack.append(loc)
        elif t=='}':
            assert_true(stack,(loc,'unmatched closing brace'))
            stack.pop()
        elif t in (r'\(',r'\['):
            assert_true(not math,(loc,'nested explicit math delimiter',math))
            math.append(t)
        elif t in (r'\)',r'\]'):
            assert_true(math and math.pop()=={r'\)':r'\(',r'\]':r'\['}[t],(loc,t))
        elif t=='$':
            if math and math[-1]=='$':
                math.pop()
            else:
                assert_true(not math or (env and env[-1] in {'aligned','array'}),(loc,'crossing math delimiter',math))
                math.append('$')
        elif re.fullmatch(r'\\[A-Za-z]+',t):
            words.add(t[1:])
    assert_true(not (stack or env or math),(name,'unclosed',stack,env,math))
    assert_true(words<=ALLOWED,(name,'unrecognised control words',words-ALLOWED))
    for body in re.findall(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        assert_true(body.startswith(r'[ampersand replacement=\&'),(name,'tikzcd replacement'))
        assert_true(not re.search(r'(?<!\\)&',body),(name,'unescaped tikzcd alignment'))
    return words

def expected():
    return [ROOT/'pages'/f'{TAG}_57_scan{n}.tex' for n in PAGES]

def assemble():
    return b'\n'.join(p.read_bytes().rstrip(b'\n')+b'\n' for p in expected())

def verify_logged_hashes(sources):
    log = (ROOT / 'progress.log').read_text()
    assert_true('witness check done ' in log, 'Missing witness completion line')
    entries = re.findall(r'^witness sha256 ([0-9a-f]{64})  (.+)$', log, re.M)
    expected_paths = {p.relative_to(ROOT).as_posix() for p in sources}
    assert_true(len(entries) == len(sources), 'Unexpected number of witness hashes')
    assert_true({path for digest, path in entries} == expected_paths, 'Witness hash paths differ')
    for digest, path in entries:
        actual = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        assert_true(actual == digest, f'SHA-256 mismatch for {path}')
    print(f'All {len(entries)} page and assembled SHA-256 digests match the witness log.')

def main():
    pages=expected()
    assert_true(set((ROOT/'pages').glob('*.tex'))==set(pages),'page set')
    joined=ROOT/(TAG+'_transcription.tex')
    if '--assemble' in sys.argv:
        joined.write_bytes(assemble())
    assert_true(joined.read_bytes()==assemble(),'assembled byte order or content differs')
    sources=[*pages,joined]; words=set()
    for src in sources:
        words.update(check_source(src.name,src.read_text()))
    for n,p in zip(PAGES,pages):
        raw=p.read_text()
        assert_true(re.findall(r'\\scanpage\{(\d+)\}',raw)==[str(n)],(p.name,'page marker'))
        assert_true(f'% archive sheet number: {n-1}' in raw,(p.name,'archive number'))
    fragment=joined.read_text()
    assert_true(fragment.startswith('\\cotefile{57}\n\\scanpage{242}'),'cote or first page marker')
    assert_true(fragment.count('\\cotefile{')==1,'duplicated cote')
    wrapper=(ROOT/(TAG+'_standalone.tex')).read_text().split()
    assert_true(wrapper==[r'\input{PREAMBLE.tex}',r'\begin{document}',r'\input{K57-15_transcription}',r'\end{document}'],'standalone wrapper')
    print(f'{len(pages)} pages and the ordered fragment pass brace, math-delimiter, environment and control-word checks; {len(words)} distinct control words used. Standalone inputs and tikz-cd separators pass.')
    if '--verify-hashes' in sys.argv:
        verify_logged_hashes(sources)
    if '--hash' in sys.argv:
        for src in sources:
            print(hashlib.sha256(src.read_bytes()).hexdigest(),src.relative_to(ROOT).as_posix())
if __name__=='__main__':
    main()

