"""Static checks only. Run with Python 3 from any directory."""
from pathlib import Path
from hashlib import sha256
import re
import sys

ROOT = Path(__file__).resolve().parent
SCANS = (17,18,19,20,21,22,23,25,26,27,29,30,31,32,34)
ALLOWED = set("""
Delta Gamma Omega Phi Psi Rightarrow S Theta alpha approx arrow bar begin beta big bigl bigr
boxed bullet cap check circ complement cotefile deleted delta diagram displaywidth draw ell end eta
exists fbox figure fill flat frac gamma geq handwritten illegible in infty inserted int lVert
lambda ldots left leq lfloor linewidth log longmapsto longrightarrow makebox mapsto margin mathbb
mathbin mathcal mathfrak mathrel mathrm mathscr mbox mspage mu nabla ne neq node noindent not nu
omega operatorname otimes overbrace overset par partial phi pi pm prime prod psi qquad quad rVert
rfloor rho right rotatebox rule scanpage sharp sigma sim simeq small subset sum tag tau text
textcircled tikz times to uline underbrace underline underset unsure uuline varepsilon varnothing
varphi vartheta vee vert vphantom widehat widetilde wr xi xrightarrow zeta delta
""".split())
ENVS = {'aligned','matrix','pmatrix','tikzcd','tikzpicture'}
STATE = {'unsure','illegible','deleted','inserted','margin','handwritten','mspage','scanpage','cotefile','diagram','figure','uuline','uline'}
TOKEN = re.compile(r'\\[A-Za-z@]+|\\.|[{}$]')
def check(src):
    errors=[]
    depth=0
    display=0
    dollar=False
    env=[]
    for line_no,line in enumerate(src.splitlines(),1):
        line=re.split(r'(?<!\\)%',line,1)[0]
        for m in TOKEN.finditer(line):
            t=m[0]
            err=None
            if t=='{': depth+=1
            elif t=='}':
                depth-=1
                if depth<0:err='unexpected closing brace'
            elif t=='$':dollar=not dollar
            elif t==r'\[':
                if display:err='nested display'
                display+=1
            elif t==r'\]':
                display-=1
                if display<0:err='unexpected end of display'
            elif t in (r'\begin',r'\end'):
                name=re.match(r'\{([^{}]+)\}',line[m.end():])
                if not name or name[1] not in ENVS:err='unknown or malformed environment'
                elif t==r'\begin':
                    env.append(name[1])
                    if name[1]=='tikzcd' and r'ampersand replacement=\&' not in line[m.end():]:err='tikzcd without localized ampersand'
                elif not env or env.pop()!=name[1]:err='mismatched environment'
            elif t.startswith('\\') and t[1:].isalpha():
                if t[1:] not in ALLOWED:err='unrecognized command '+t
                elif t[1:] in STATE and not line[m.end():].lstrip().startswith('{'):err='unbraced '+t
                elif t in (r'\diagram',r'\figure') and (dollar or display):err='block inside math'
            if err:errors.append(f'{line_no}: {err}')
    if depth or display or dollar or env:errors.append(f'end state braces={depth}, displays={display}, open dollar={dollar}, environments={env}')
    return errors
def main():
    full=b''
    problems=0
    for n in SCANS:
        f=ROOT/'pages'/f'K8-03_8_scan{n:03d}.tex'
        data=f.read_bytes();full+=data
        src=data.decode()
        issues=check(src)
        if src.count(r'\scanpage{'+str(n)+'}')!=1:issues.append('scan marker')
        problems+=len(issues)
        print(f'{n:03d} '+('; '.join(issues) if issues else 'PASS'))
    if full!=(ROOT/'K8-03_transcription.tex').read_bytes() or not full.startswith(b'\\cotefile{8}\n') or full.count(b'\\cotefile{8}')!=1:
        print('Assembly mismatch');problems+=1
    print('Assembly SHA-256',sha256(full).hexdigest())
    return bool(problems)
if __name__=='__main__':sys.exit(main())
