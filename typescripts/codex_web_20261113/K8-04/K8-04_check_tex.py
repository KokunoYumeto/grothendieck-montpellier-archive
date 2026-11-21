"""Check the diplomatic page syntax without running a TeX engine."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PAGES = sorted((ROOT / 'pages').glob('K8-04_8_scan*.tex'))
ASSEMBLED = ROOT / 'K8-04_transcription.tex'
# Standard LaTeX, AMS and tikz-cd controls used here. Archive macros are separate.
STANDARD = set("""Delta Longleftrightarrow Omega S Sigma alpha arrow begin beta bigcup bigl bigr binom
boxed cap cdot cdots circ cong delta dim ell end exists geq hfill hookrightarrow hphantom hspace in
infty joinrel lambda ldots left leq lhook longmapsto longrightarrow mathbb mathrel mathrm mu ne nu omega
operatorname otimes overset partial pi psi qquad quad relbar rho right rule sigma sim simeq subset sum
text textquotedblleft textquotedblright textsuperscript times to underset varphi varpi vee wedge xi
xrightarrow input""".split())
ARCHIVE = set("cotefile scanpage mspage handwritten deleted inserted margin uline uuline diagram figure unsure illegible".split())
TOKEN = re.compile(r'\\(?:begin|end)\{[A-Za-z*]+\}|\\[A-Za-z@]+|\\.|[{}$%]')

def check(path):
    stack = []
    for ln, line in enumerate(path.read_text().splitlines(), 1):
        for match in TOKEN.finditer(line):
            token = match[0]
            if token == '%':
                break
            if token.startswith(r'\begin{'):
                name = token[7:-1]
                assert name in {'center','tikzcd','aligned','document'}, (path.name, ln, name)
                stack.append(('environment ' + name, ln))
            elif token.startswith(r'\end{'):
                end(stack, 'environment ' + token[5:-1], path, ln)
            elif token in ('{', r'\['):
                stack.append((token, ln))
            elif token in ('}', r'\]'):
                end(stack, '{' if token == '}' else r'\[', path, ln)
            elif token == '$':
                if stack and stack[-1][0] == '$':
                    stack.pop()
                else:
                    stack.append(('$', ln))
            elif re.fullmatch(r'\\[A-Za-z@]+', token):
                assert token[1:] in STANDARD | ARCHIVE, (path.name, ln, token)
    assert not stack, (path.name, stack)

def end(stack, expected, path, ln):
    assert stack and stack[-1][0] == expected, (path.name, ln, expected, stack[-3:])
    stack.pop()

if __name__ == '__main__':
    assert len(PAGES) == 15
    for number, page in enumerate(PAGES, 35):
        check(page)
        assert re.findall(r'\\scanpage\{(\d+)\}', page.read_text()) == [str(number)]
    check(ASSEMBLED)
    wrapper = ROOT / 'K8-04_standalone.tex'
    check(wrapper)
    assert ASSEMBLED.read_bytes() == b''.join(p.read_bytes() for p in PAGES)
    assert ASSEMBLED.read_text().count(r'\cotefile{8}') == 1
    assert wrapper.read_text().splitlines() == [r'\input{PREAMBLE.tex}', r'\begin{document}', r'\input{K8-04_transcription}', r'\end{document}']
    print('PASS: 15 page fragments, assembled fragment and standalone wrapper. Braces, math delimiters, environment nesting, control names, scan order and byte-for-byte assembly.')
