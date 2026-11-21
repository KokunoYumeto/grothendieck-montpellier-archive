"""Validate the diplomatic source without invoking a TeX engine. Run with Python 3."""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BATCH = 'K157-5-34'
TOKEN = re.compile(r'\\(?:[A-Za-z@]+|.)|[{}$%]')
ARCHIVE = 'cotefile scanpage mspage unsure illegible handwritten deleted inserted margin diagram figure'
STANDARD = """
begin end begingroup endgroup makeatletter makeatother hspace mathcal mathop mathord mathrel
mathrm lim limits left middle right bigl bigr overline underline underbrace textsuperscript
textquotedblleft textquotedblright alpha beta lambda tau sigma rho pi phi varphi natural sharp
forall exists in subset ne geq leq circ wedge cap pm prime mapsto mapstochar longmapsto
to longrightarrow leftarrow nearrow Longrightarrow Rightarrow relbar Vert sim quad qquad
backslash mid varnothing
"""
PACKAGES = """
operatorname text boxed overset underset varinjlim varprojlim xrightarrow tag tagsleft@true
arrow uline uuline
"""
WORDS = set((ARCHIVE + ' ' + STANDARD + ' ' + PACKAGES).split())
SYMBOLS = set(" &,[\\]{};!")
ENVS = {'tikzcd', 'aligned'}
SCANS = range(528, 543)

def require(test, detail):
    if not test:
        raise ValueError(detail)

def check_source(src, scan):
    label = f'scan {scan}'
    scopes, environments, math = [], [], []
    skip_to = 0
    count = Counter()
    for match in TOKEN.finditer(src):
        if match.start() < skip_to:
            continue
        token = match[0]
        if token == '%':
            newline = src.find('\n', match.end())
            skip_to = len(src) if newline < 0 else newline + 1
            continue
        if token == '{':
            scopes.append('{')
        elif token == '}':
            require(scopes and scopes.pop() == '{', (label, 'closing brace', match.start()))
        elif token == '$':
            if math and math[-1] == '$':
                math.pop()
            else:
                math.append('$')
        elif token == r'\[':
            require(not math, (label, 'nested display', match.start()))
            math.append('display')
        elif token == r'\]':
            require(math and math.pop() == 'display', (label, 'display closure', match.start()))
        else:
            cmd = token[1:]
            require(cmd in WORDS or cmd in SYMBOLS, (label, 'undefined command', token))
            count[cmd] += 1
            if cmd == 'begingroup':
                scopes.append('group')
            elif cmd == 'endgroup':
                require(scopes and scopes.pop() == 'group', (label, 'unmatched group'))
            if cmd in ('begin', 'end'):
                env = re.match(r'\{([a-zA-Z*]+)\}', src[match.end():])
                require(env and env[1] in ENVS, (label, 'unknown environment', match.start()))
                if cmd == 'begin':
                    environments.append(env[1])
                    require(env[1] != 'aligned' or math == ['display'], (label, 'aligned outside display'))
                else:
                    require(environments and environments.pop() == env[1], (label, 'environment closure', env[1]))
    require(not (scopes or environments or math), (label, 'unclosed structures', scopes, environments, math))
    require(not re.search(r'@[A-Za-z0-9_]+\{', src), (label, 'unrendered editorial key'))
    require(count['scanpage'] == count['mspage'] == 1, (label, 'page markers'))
    require(r'\scanpage{'+str(scan)+'}' in src and r'\mspage{'+str(scan-89)+'}' in src, (label, 'numbers'))
    require('% archive sheet number: '+str(scan-1)+'\n' in src, (label, 'archive sheet'))
    require(count['cotefile'] == int(scan == 528), (label, 'cote marker'))
    diagrams = re.findall(r'\\diagram\{\s*\\begin\{tikzcd\}\[ampersand replacement=\\&\](.*?)\\end\{tikzcd\}', src, re.S)
    require(len(diagrams) == count['diagram'], (label, 'unwrapped or unconfigured diagram'))
    require(all(not re.search(r'(?<!\\)&', d) for d in diagrams), (label, 'literal diagram tab'))
    require(count['tag'] == count['tagsleft@true'], (label, 'tag placement'))
    return count

def main():
    paths = [ROOT/'pages'/f'{BATCH}_157-5_scan{n}.tex' for n in SCANS]
    require(set((ROOT/'pages').glob('*.tex')) == set(paths), 'Page set')
    total = Counter()
    for n, path in zip(SCANS, paths):
        total.update(check_source(path.read_text(encoding='utf-8'), n))
    assembled = (ROOT/f'{BATCH}_transcription.tex').read_bytes()
    require(assembled == b''.join(p.read_bytes() for p in paths), 'Assembly differs from page files')
    require(assembled.startswith(b'\\cotefile{157-5}\n\\scanpage{528}'), 'Opening markers')
    wrapper = '\n'.join([r'\input{PREAMBLE.tex}',r'\begin{document}',r'\input{K157-5-34_transcription}',r'\end{document}',''])
    require((ROOT/f'{BATCH}_standalone.tex').read_text() == wrapper, 'Standalone wrapper')
    with (ROOT/f'{BATCH}_inventory.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    require(rows and {int(r['scan']) for r in rows} == set(SCANS), 'Inventory pages')
    require(all(r['transcribed']=='yes' for r in rows), 'Unfinished inventory row')
    state = {'deletion':'deleted', 'insertion':'inserted', 'margin note':'margin', 'diagram':'diagram'}
    for kind, cmd in state.items():
        require(sum(r['kind']==kind for r in rows) == total[cmd], ('Inventory total',kind))
    print(f'{len(paths)} pages passed; {len(rows)} inventory rows, all yes; {total["diagram"]} diagrams; {total["tag"]} left-hand labels.')
    print('Marks: '+', '.join(f'{x}={total[x]}' for x in ('unsure','illegible','deleted','inserted','margin'))+'.')
    print('Balanced braces, groups, inline/display math and environments. Command list, page markers and bytewise assembly passed.')

if __name__ == '__main__':
    main()
