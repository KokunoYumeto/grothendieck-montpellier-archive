"""Compare dated blind entries to their own source lines; no imaging or OCR.
The JSON preserves the first and audited line(s) so later witness edits never
erase the original comparison. The script also rereads the delivered pages.
"""
from collections import Counter
from difflib import SequenceMatcher
from html import escape
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parent
TAG = 'K57-11'
def select(source, specification):
    lines = source.splitlines()
    result = []
    for block in specification.split(';'):
        first,*last = map(int,block.split(':'))
        result.extend(lines[first-1:(last[0] if last else first)])
    return '\n'.join(result)

WORDS = {'longrightarrow':'→','to':'→','leftarrow':'←','geq':'≥','leq':'≤',
         'simeq':'≃','ldots':'…','prime':'′','pi':'π','alpha':'α','mu':'μ',
         'xi':'ξ','zeta':'ζ','lambda':'λ','rho':'ρ','theta':'θ','times':'×',
         'sigma':'σ','Gamma':'Γ','Omega':'Ω','omega':'ω','tau':'τ'}
IGNORE = set('mathrm text textit qquad quad inserted deleted unsure handwritten uline uuline mspage'.split())
def projection(text):
    """Locate corresponding strokes despite brace/spacing and arrow-length differences."""
    chars=[]; positions=[]
    for m in re.finditer(r'\\[A-Za-z]+|\\.|.',text,re.S):
        a=m.group()
        if a.startswith('\\'):
            cmd=a[1:]
            if cmd in IGNORE or cmd in (',',' ',';','!'):continue
            a=WORDS.get(cmd,cmd)
        elif a.isspace() or a in '{}$':continue
        if a=="'":a='′'
        for c in a:
            chars.append(c);positions.append(m.start())
    return ''.join(chars),positions

def excerpt(scope, needle, anchor):
    target,_ = projection(needle)
    norm, offsets = projection(scope)
    found=norm.find(target)
    if anchor and anchor in scope:
        lo=scope.index(anchor)
        length=min(max(len(anchor),len(needle)+14),155)
        high=min(len(scope),lo+length)
    elif found>=0 and target:
        lo=offsets[found]; high=offsets[found+len(target)-1]+1
    else:
        match=SequenceMatcher(None,target,norm,autojunk=False).find_longest_match()
        if not offsets or match.size==0:return scope[:65],False
        start=max(0,match.b-match.a)
        end=min(len(norm)-1,start+max(len(target),match.size)-1)
        lo=offsets[start];high=offsets[end]+1
    # A small amount of literal context identifies corrections and cuts.
    return scope[max(0,lo-7):min(len(scope),high+9)].replace('\n',' ↵ '),found>=0

def cell(s):
    return '<code>'+escape(s).replace('|','&#124;').replace('\n',' ')+'</code>'
def main():
    d=json.loads((ROOT/f'{TAG}_collation.json').read_text())
    with (ROOT/f'{TAG}_blind.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    pages={}; entries=[]; seq=Counter()
    for row in rows:
        n=int(row['scan']);seq[n]+=1;key=f'{n}.{seq[n]}'
        if n not in pages:pages[n]=(ROOT/'pages'/f'{TAG}_57_scan{n:03d}.tex').read_text()
        v=d[key]; b=row['what the crop shows']; now=select(pages[n],v['lines'])
        first,hit1=excerpt(v['first'], b,v['first_anchor'])
        audit,hit2=excerpt(v['audited'],b,v['audit_anchor'])
        current,hit3=excerpt(now,b,v['audit_anchor'])
        disposition=v['finding'] or ('Same reading in the located passage.' if hit1 and hit2 else 'See the indexed line. The blind entry is selective or uses different TeX, graph order, state notation or punctuation.')
        entries.append((key,row,v,first,audit,current,disposition,hit1,hit2,hit3))
    assert len(d)==len(entries)
    output=['# Blind comparison','',f'{len(entries)} blind entries across {len(seq)} scans. The first table gives the readings that needed editorial adjudication, including cases where the difference was the state of a mark. The full register gives every comparison, including abbreviated descriptions of graph topology and typographical differences. Entries were recorded before reopening their page. First-pass and audited source lines are preserved in the companion JSON. The current source is read afresh when this script runs. Clip edges in the tables are excerpts of LaTeX source.','',
            '## Differences and decisions','','| Scan · entry / locus | Blind reading | First-pass excerpt | Image decision at audit |','|---|---|---|---|']
    for key,row,v,f,a,c,decision,*hits in entries:
        if v['finding']:output.append(f"| {key} · {row['place']} | {cell(row['what the crop shows'])} | {cell(f)} | {decision} |")
    output+=['','## Every blind entry','','The last three flags record a literal substring match after removing spacing and grouping and normalizing common equivalent commands. They are in the order first pass, second pass, delivered page. A dash means the quoted wording or encoding differs. The human comparison above also detects changes in layout, letter style and correction state.','',
             '| ID · TeX line(s) · locus | Blind reading | First pass | Audited | Delivered | Match |','|---|---|---|---|---|---|']
    for key,row,v,f,a,c,decision,*hits in entries:
        output.append(f"| {key} · {v['lines']} · {row['place']} | {cell(row['what the crop shows'])} | {cell(f)} | {cell(a)} | {cell(c)} | "+' '.join('✓' if h else '–' for h in hits)+' |')
    (ROOT/f'{TAG}_blind_compare.md').write_text('\n'.join(output)+'\n')
    print(f'{len(entries)} entries; {sum(bool(x[2]["finding"]) for x in entries)} explicit image adjudications')
if __name__=='__main__': main()
