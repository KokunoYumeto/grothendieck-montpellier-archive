"""Check the transcription as source. Run with Python 3 from any directory."""
import argparse
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
FRAGMENT = ROOT / 'K31-04_transcription.tex'
PAGES = [ROOT / 'pages' / f'K31-04_31_scan{n:03}.tex' for n in range(2, 18)]
EDITORIAL = set('cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible'.split())
STANDARD = set('begin end bigl bigr left right ldots mathord mathrm quad qquad rm textcircled underline overbrace'.split())
MATH = set('Longleftrightarrow Longrightarrow Rightarrow alpha bigcup cap coprod dot emptyset geq in lambda leq longmapsto longrightarrow mathbb mathcal mu neq notin operatorname oplus otimes overset prime prod sim simeq subset substack supset tag text times to varinjlim xi xrightarrow'.split())
GRAPHICS = {'arrow', 'rotatebox'}
ENVIRONMENTS = {'aligned', 'tikzcd', 'cases'}
TOKEN = re.compile(r'%[^\n]*|\\(?:begin|end)\{[a-zA-Z*]+\}|\\[a-zA-Z]+|\\[\s\S]|[{}$]')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def check(page):
    src = page.read_text()
    stack = []
    def close(kind, match):
        if not stack or stack[-1][0] != kind:
            raise ValueError(f'{page.name}:{src.count(chr(10),0,match.start())+1}: unmatched {match.group()}; {stack[-2:]}')
        stack.pop()
    for m in TOKEN.finditer(src):
        t = m.group()
        if t.startswith('%'):
            continue
        if t.startswith((r'\begin{', r'\end{')):
            name = t[t.index('{') + 1:-1]
            if name not in ENVIRONMENTS:
                raise ValueError((page.name, name))
            if t.startswith(r'\begin'):
                stack.append((name,m.start()))
            else:
                close(name, m)
        elif t in ('{',r'\['):
            stack.append((t,m.start()))
        elif t in ('}',r'\]'):
            close('{' if t == '}' else r'\[', m)
        elif t == '$':
            if stack and stack[-1][0] == '$':
                close('$',m)
            else:
                stack.append(('$',m.start()))
        elif re.fullmatch(r'\\[a-zA-Z]+',t) and t[1:] not in EDITORIAL | STANDARD | MATH | GRAPHICS:
            raise ValueError(f'{page.name}: unknown command {t}')
    if stack:
        raise ValueError((page.name,'unclosed',stack))
    n=int(page.stem[-3:])
    if re.findall(r'\\scanpage\{(\d+)\}',src)!=[str(n)]:
        raise ValueError((page.name,'scan label'))
    if (n==2) != src.startswith(r'\cotefile{31}'):
        raise ValueError((page.name,'cote label'))
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--assemble',action='store_true')
    parser.add_argument('--verify-final',action='store_true')
    args=parser.parse_args()
    if list(sorted((ROOT/'pages').glob('*.tex'))) != PAGES:
        raise ValueError('Unexpected page list')
    for page in PAGES:check(page)
    content=b''.join(p.read_bytes() for p in PAGES)
    if args.assemble:FRAGMENT.write_bytes(content)
    if content!=FRAGMENT.read_bytes():raise ValueError('Fragment differs from the ordered pages')
    print('16/16 pages passed braces, display delimiters, dollar pairs, environments and control-word names. Concatenation exact.')
    if args.verify_final:
        records={}
        for line in (ROOT/'progress.log').read_text().splitlines():
            if line.startswith('sha256 witness '):
                _,_,value,file=line.split(' ',3);records[file]=value
        expected={p.relative_to(ROOT).as_posix():sha(p) for p in PAGES+[FRAGMENT]}
        if records!=expected:raise ValueError('Witness hashes differ')
        print('17/17 SHA-256 digests match the post-witness log.')
if __name__=='__main__':main()
