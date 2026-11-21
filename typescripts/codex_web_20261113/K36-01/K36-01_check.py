"""Check the diplomatic fragments without running TeX. Run from any directory."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
COTE=ROOT/'K36-01_transcription.tex'
COMMANDS=set("""
Gamma Rightarrow Vert alpha arrow ast atop bar begin begingroup bigl bigr boxed cdot
cotefile csname deleted diagram dim draw ell end endcsname endgroup figure geq
handwritten hfill hline hrule illegible in infty inserted ldots left limits linewidth
longmapsto longrightarrow mapsto margin mathbb mathbin mathcal mathfrak mathop mathrel
mathrm mathsf mspage ne node nu omega operatorname otimes overbrace overset partial
phi qquad quad resizebox rho right rightleftarrows rule scanpage shortmid shortstack sigma
sim simeq smallskip smash subset substack tag text tikz times uline underbrace underline
underset unsure uuline varinjlim varphi wedge xi xleftarrow xrightarrow zeta
""".split())
# The only constructed name invokes the amsmath switch for left-hand equation tags.
DYNAMIC_NAMES={'tagsleft@true'}
ENVS={'array','aligned','tikzcd','tikzpicture','gathered'}
LEX=re.compile(r'\\(?:[A-Za-z]+|.)|[{}$]')
def inspect_file(p):
    raw=p.read_text()
    s='\n'.join(re.split(r'(?<!\\)%',line,1)[0] for line in raw.splitlines())
    braces=[];env=[];displays=[];dollars=[];cmds=set();groups=[]
    dynamic=re.findall(r'\\csname\s*([^\\]*?)\\endcsname',s)
    if set(dynamic)-DYNAMIC_NAMES or len(dynamic)!=s.count(r'\csname') or len(dynamic)!=s.count(r'\endcsname'):
        raise ValueError(f'{p.name}: unknown or incomplete constructed command')

    for m in LEX.finditer(s):
        t=m.group();line=s.count('\n',0,m.start())+1
        def fail(what):raise ValueError(f'{p.name}:{line}: {what}')
        if t==r'\begingroup':groups.append(line)
        if t==r'\endgroup':
            if not groups:fail('unexpected endgroup')
            groups.pop()
        if t=='{':braces.append(line)
        if t=='}':
            if not braces:fail('unexpected }')
            braces.pop()
        if t in (r'\begin',r'\end'):
            a=re.match(r'\{([A-Za-z*]+)\}',s[m.end():])
            if not a or a[1] not in ENVS:fail('unknown environment')
            if t==r'\begin':env.append(a[1])
            elif not env or env.pop()!=a[1]:fail('mismatched environment')
        if t==r'\[':
            if displays:fail('nested display')
            displays.append(line)
        if t==r'\]':
            if not displays:fail('unexpected end of display')
            displays.pop()
        if t=='$':
            if dollars and dollars[-1]==len(braces):dollars.pop()
            else:dollars.append(len(braces))
        if len(t)>1 and t.startswith('\\') and t[1:].isalpha():cmds.add(t[1:])
    if groups:raise ValueError(f"{p.name}: unclosed group")
    if braces or env or displays or dollars:raise ValueError(f'{p.name}: open {braces,env,displays,dollars}')
    unknown=cmds-COMMANDS
    if unknown:raise ValueError(f'{p.name}: undefined names: {sorted(unknown)}')
    return 'braces, display delimiters, inline math, environments and command names pass'
def main():
    pp=sorted((ROOT/'pages').glob('*.tex'))
    expected=[3,4,5,6,7,8,28,29,30,31,32,33,34,35,36,37]
    assert [int(p.stem[-3:]) for p in pp]==expected
    assert COTE.read_text()=='\n'.join(p.read_text().rstrip()+'\n' for p in pp)
    assert COTE.read_text().count(r'\cotefile{36}')==1
    for p in [*pp,COTE]:print(p.name,inspect_file(p))
if __name__=='__main__':main()
