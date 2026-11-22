#!/usr/bin/env python3
"""Assemble the 15 leaves and validate only the syntax used by this fragment."""
from pathlib import Path
import re,sys,hashlib
from tex_elements import escaped
root=Path(__file__).resolve().parent
scans=[*range(20,29),*range(30,36)]
pages=[root/'pages'/f'K58-03_58_scan{n:03}.tex' for n in scans]
# Independent names from the supplied preamble or LaTeX / amsmath / amssymb /
# mathrsfs / tikz-cd / tikz / ulem. Control symbols are scanned separately.
commands=set('''makebox cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible begin end text textrm mathrm mathsf mathit mathbb mathcal mathfrak mathscr operatorname mathbin mathrel mathop noindent hfill hspace vspace linewidth baselineskip textwidth columnwidth textsuperscript textsubscript textbf emph textcircled textnormal normalfont footnotesize small Large rule vphantom phantom strut left right Big Bigg big bigg underbrace overbrace underbracket overline underline widehat widetilde bar hat check tilde vec dot ddot prime vert Vert mid colon ldots cdots dots geq leq ge le leqslant geqslant neq ne in notin ni subset subseteq supset supseteq cap cup bigcup bigcap setminus emptyset varnothing forall exists neg lor land to gets mapsto longmapsto rightarrow longrightarrow hookrightarrow leadsto Rightarrow Leftarrow leftarrow Leftrightarrow Longrightarrow longleftarrow leftrightarrow cong simeq sim approx equiv times otimes oplus circ cdot ast star bullet wr pm minus dagger partial infty ell alpha beta gamma Gamma delta Delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda Lambda mu nu xi Xi pi Pi rho sigma Sigma tau upsilon phi varphi Phi chi psi omega Omega dim max min inf sup lim varinjlim injlim ker det Hom mathring mathbf frac dfrac tfrac sqrt overset underset substack limits nolimits tag multicolumn intertext textstyle displaystyle scriptstyle scriptscriptstyle quad qquad S P par linebreak newline nobreakspace textbackslash arrow ar tikz node draw path coordinate fill filldraw'''.split())
env_allowed={'samepage','aligned','tikzcd','tikzpicture','array','center','matrix','cases','gathered','smallmatrix','minipage','tabular','equation','equation*'}
def check(p):
    src=p.read_text();s='\n'.join(re.split(r'(?<!\\)%',l,1)[0] for l in src.splitlines())
    b=[];env=[];math=[];errors=[]
    for m in re.finditer(r'\\(?:begin|end)\{([^{}]+)\}|\\[a-zA-Z]+|\\.|[{}$]',s):
        tok=m[0]
        if m[1]:
            name=m[1]
            if name not in env_allowed:errors.append('unknown environment '+name)
            if tok.startswith(r'\begin'):env.append(name)
            elif not env or env.pop()!=name:errors.append('environment '+tok)
        elif tok=='{':b.append(m.start())
        elif tok=='}':
            if b:b.pop()
            else:errors.append('extra }')
        elif tok in (r'\[',r'\('):math.append(tok)
        elif tok in (r'\]',r'\)'):
            exp={r'\]':r'\[',r'\)':r'\('}[tok]
            if not math or math.pop()!=exp:errors.append('unpaired '+tok)
        elif tok=='$':
            if math and math[-1]=='$':math.pop()
            else:math.append('$')
        elif tok.startswith('\\') and tok[1:].isalpha() and tok[1:] not in commands: errors.append('unknown '+tok)
    if b or env or math:errors.append(f'open groups={len(b)}, env={env}, math={math}')
    return sorted(set(errors))
if __name__=='__main__':
    if '--assemble' in sys.argv:
        (root/'K58-03_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in pages))
        (root/'K58-03_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{K58-03_transcription}\n\\end{document}\n')
    targets=pages+[root/'K58-03_transcription.tex']
    failures=0
    for p in targets:
        issues=check(p);failures+=bool(issues)
        print(p.relative_to(root),'; '.join(issues) if issues else 'PASS',sep='\t')
    if targets[-1].read_bytes()!=b''.join(p.read_bytes() for p in pages):
        print('Assembly differs from the ordered leaves.'); failures+=1
    if failures:raise SystemExit(1)
