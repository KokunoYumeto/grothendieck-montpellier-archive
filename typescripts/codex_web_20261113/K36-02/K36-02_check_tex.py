"""Check the supplied fragments without invoking TeX. Run from any directory."""
from pathlib import Path
import argparse
import re
from collections import Counter

ROOT = Path(__file__).resolve().parent
FILES = [ROOT / 'pages' / f'K36-02_36_scan{i:03}.tex' for i in range(38, 53)]
ASSEMBLED = ROOT / 'K36-02_transcription.tex'
ALLOWED = set("""
Lambda Leftarrow Longleftarrow Rightarrow S Vert alpha arrow begin binom boxed bullet
cdot char check circledast cotefile deleted diagram doteq draw ell emptyset end enspace
fbox figure fill forall frac gamma geqslant handwritten hfill hspace illegible in
infty inserted leftarrow lim longleftarrow longmapsto longrightarrow makeatletter
makeatother mapsto margin mathbb mathbin mathcal mathop mathrel mathrm mathscr mid mspage mu
ne node nolimits operatorname otimes overset pi prod qquad quad rho scanpage
scriptscriptstyle shortmid sim simeq substack sum supset tag tagsleft@true tagsleft@false tau text
textsuperscript tikz times to uline underline underrightarrow underset unsure uuline
varinjlim varphi varprojlim vee wedge wr xi xleftarrow xrightarrow
""".split())
ENVS = {'aligned', 'tikzcd', 'tikzpicture'}
TOKEN = re.compile(r'\\(?:begin|end)\{[^}]*\}|\\[A-Za-z@]+|\\.|[{}$]')
def check(path, extra_names=(), extra_envs=()):
    source = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
    allowed = ALLOWED.union(extra_names)
    environments = ENVS.union(extra_envs)
    braces, envs, modes, errors = [], [], [], []
    for m in TOKEN.finditer(source):
        token = m[0]
        line = source.count('\n', 0, m.start()) + 1
        if token == '{':
            braces.append(line)
        elif token == '}':
            if braces: braces.pop()
            else: errors.append((line, 'unmatched }'))
        elif token.startswith(('\\begin{','\\end{')):
            env = token.split('{',1)[1][:-1]
            if env not in environments: errors.append((line,'unknown environment '+env))
            if token.startswith('\\begin'): envs.append((env,line))
            elif envs and envs[-1][0] == env: envs.pop()
            else: errors.append((line, 'mismatched '+token))
        elif token in ('$','\\[','\\]'):
            if token == '$':
                if modes and modes[-1][0] == '$': modes.pop()
                else: modes.append((token,line))
            elif token == '\\[': modes.append((token,line))
            elif modes and modes[-1][0] == '\\[': modes.pop()
            else: errors.append((line, 'unmatched display delimiter'))
        elif token.startswith('\\') and (token[1:].isalpha() or '@' in token):
            if token[1:] not in allowed: errors.append((line, 'unrecognized '+token))
    errors += [(0, str(v)) for v in [braces,envs,modes] if v]
    if errors: raise ValueError(f'{path.name}: {errors}')
    return Counter(re.findall(r'\\(unsure|illegible|deleted)\{',source))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--assemble',action='store_true')
    args = parser.parse_args()
    whole = b''.join(p.read_bytes() for p in FILES)
    if args.assemble: ASSEMBLED.write_bytes(whole)
    assert ASSEMBLED.read_bytes() == whole
    assert whole.startswith(b'\\cotefile{36}\n\\scanpage{38}') and whole.count(b'\\cotefile{') == 1
    counts = Counter()
    for n,p in enumerate(FILES,38):
        assert re.findall(r'\\scanpage\{(\d+)\}',p.read_text()) == [str(n)]
        counts += check(p)
    assert counts == check(ASSEMBLED)
    standalone = ROOT / 'K36-02_standalone.tex'
    assert standalone.read_text().splitlines() == [
        r'\input{PREAMBLE.tex}', r'\begin{document}',
        r'\input{K36-02_transcription}', r'\end{document}']
    check(standalone, {'input'}, {'document'})
    layout = ROOT / 'K36-02_margin_layout.tex'
    if layout.exists():
        names = {'input', 'linewidth', 'noindent', 'normalmarginpar', 'par',
                 'reversemarginpar', 'shortstack'}
        local_counts = check(layout, names, {'document','scope','minipage'})
        assert local_counts == check(FILES[49-38])
        stream = layout.read_text()
        assert re.findall(r'\\input\{pages/K36-02_36_scan(\d+)\}',stream) == [
            f'{n:03}' for n in range(38,53) if n != 49]
    print(f'{len(FILES)} pages and assembly pass; {dict(counts)}')
if __name__ == '__main__':
    main()
