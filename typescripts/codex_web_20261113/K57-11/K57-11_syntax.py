"""Static checks only. Run with Python 3 from any directory."""
from pathlib import Path
import collections
import re

ROOT = Path(__file__).resolve().parent
SCANS = [*range(89, 98), *range(99, 105)]
COMMANDS = set("""Gamma Leftarrow Longleftarrow Omega Rightarrow alpha arrow backslash begin boxed
centerline cotefile deleted diagram dim downarrow end exists fbox figure forall frac geq geqq
handwritten hookrightarrow illegible in infty inserted lambda ldots left leftarrow leq linewidth
longrightarrow mapsto margin mathbb mathcal mathfrak mathrm mathscr medskip mid mspage mu neq
nwarrow omega operatorname oplus otimes overline overset par phantom pi pm prime prod qquad
quad rho right rule scanpage sigma sim simeq sqrt subset substack sum swarrow tau text
textsuperscript theta times to uline underbrace underline underset unsure uuline vee widetilde
xi xleftarrow xrightarrow zeta""".split())
ENVIRONMENTS = {'aligned', 'array', 'center', 'tikzcd', 'tikzpicture'}
TOKEN = re.compile(r'\\(?:begin|end)\{[^{}]*\}|\\[A-Za-z]+|\\.|[{}$]')
def check(source, filename):
    source = re.sub(r'(?<!\\)%[^\n]*', '', source)
    stacks = {k: [] for k in ('group', 'environment', 'display', 'inline', 'dollar')}
    def pair(key, opening, value, pos):
        stack = stacks[key]
        if opening:
            stack.append((value, pos))
        elif not stack or stack.pop()[0] != value:
            raise ValueError(f'{filename} at offset {pos}: unpaired {value}')
    for token in TOKEN.finditer(source):
        t = token.group()
        pos = token.start()
        if t.startswith((r'\begin{',r'\end{')):
            env = t[t.index('{')+1:-1]
            assert env in ENVIRONMENTS, (filename, env)
            pair('environment', t.startswith(r'\begin'), env, pos)
        elif t in '{}': pair('group', t == '{', '{}', pos)
        elif t in (r'\[',r'\]'): pair('display', t == r'\[', 'display', pos)
        elif t in (r'\(',r'\)'): pair('inline', t == r'\(', 'inline', pos)
        elif t == '$': pair('dollar', not stacks['dollar'], '$', pos)
        elif re.fullmatch(r'\\[A-Za-z]+',t):
            assert t[1:] in COMMANDS, (filename,t)
    assert not any(stacks.values()), (filename, stacks)
    assert source.count(r'\left') - source.count(r'\leftarrow') == source.count(r'\right'), filename
    for d in re.finditer(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}', source, re.S):
        assert r'ampersand replacement=\&' in d[1] and not re.search(r'(?<!\\)&', d[1]), filename
def main():
    pages = sorted((ROOT/'pages').glob('*.tex'))
    assert [int(p.stem[-3:]) for p in pages] == SCANS
    for n,p in zip(SCANS,pages):
        s=p.read_text()
        assert re.findall(r'\\scanpage\{(\d+)\}', s)==[str(n)]
        check(s,p.name)
    together=b''.join(p.read_bytes() for p in pages)
    assert together==(ROOT/'K57-11_transcription.tex').read_bytes()
    assert together.startswith(b'\\cotefile{57}\n\\scanpage{89}\n') and together.count(b'\\cotefile')==1
    count=collections.Counter(re.findall(rb'\\(unsure|illegible|deleted)\{',together))
    print(f'{len(pages)} pages passed, exact concatenation, balanced delimiters and environments, command names checked; '+', '.join(f'{k.decode()} {v}' for k,v in sorted(count.items())))
if __name__=='__main__': main()
