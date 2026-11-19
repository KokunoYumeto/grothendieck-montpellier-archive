"""Index already audited TeX spans; does not read images or check mathematics."""
from pathlib import Path
import re

OUT=Path(__file__).resolve().parent
TASK=OUT.parent.name
TOKEN=re.compile(r'\\(?:[A-Za-z]+|.)|%[^\n]*|[{}$]',re.S)
MARKER='\n# Complete formula and state register\n'

def math_spans(s):
    mode=None; start=0
    for m in TOKEN.finditer(s):
        t=m.group()
        if t.startswith('%'):
            continue
        if t==r'\[' and mode is None:
            mode='display';start=m.start()
        elif t==r'\]' and mode=='display':
            yield start,m.end(),mode
            mode=None
        elif t=='$':
            if mode is None:
                mode='inline';start=m.start()
            elif mode=='inline':
                yield start,m.end(),mode
                mode=None

def state_spans(s):
    pat=re.compile(r'\\(diagram|figure|margin|deleted|inserted|handwritten)\s*\{')
    for m in pat.finditer(s):
        depth=1;end=m.end()
        for t in TOKEN.finditer(s,m.end()):
            if t.group()=='{':depth+=1
            elif t.group()=='}':depth-=1
            if depth==0:
                end=t.end();break
        if depth:
            raise ValueError('Unbalanced state macro')
        yield m.start(),end,m.group(1)

header='''
# Complete formula and state register

The page sections above record the actual image readings, observations and changes. For completeness, this exact-text register lists every standalone inline/display math span and every marked diagram, drawing, margin, insertion and deletion block in the audited page files. The contents of diagrams include their unwrapped math labels. Nested states are indexed as well as their enclosing block. These are locators for the documentary comparisons already made; generating this register adds no mathematical verification. Line numbers locate the TeX deliverable, not inferred manuscript lines. The i/j and alphabet observations remain in the individual page audits.

'''
chunks=[header]
counts={}
for p in sorted((OUT/'pages').glob('*.tex')):
    s=p.read_text();scan=re.search(r'scan(\d+)',p.name).group(1)
    spans=sorted([*math_spans(s),*state_spans(s)],key=lambda x:(x[0],x[1]))
    chunks.append(f'## Scan {scan}: exact locators\n\n```tex\n')
    for a,b,kind in spans:
        line=s.count('\n',0,a)+1
        chunks.append(f'% {kind}; TeX line {line}\n{s[a:b]}\n\n')
    chunks.append('```\n\n')
    counts[scan]=len(spans)
p=OUT/f'{TASK}_audit.md'
core=p.read_text().split(MARKER)[0]
p.write_text(core.rstrip()+'\n'+''.join(chunks))
print('Audit locators:',counts,'total',sum(counts.values()))
