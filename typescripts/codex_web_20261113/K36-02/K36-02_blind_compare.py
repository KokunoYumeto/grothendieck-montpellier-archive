"""Compare recorded blind readings with first-pass excerpts and the current page files.

Run beside the supplied TSVs. Exact normalized matches are mechanical. The
independent ink judgments identify differences in wording, symbols and placement.
"""
from pathlib import Path
import csv
import re
import unicodedata

ROOT = Path(__file__).resolve().parent
PREFIX = 'K36-02_blind'
# Ordinals in each page's blind TSV, not foliation or TeX line numbers.
CONFLICTS = {
 38:{6},39:{2,5,7,12,15,17,18,19},40:{5,11},41:{8,9,13},
 42:{6,7,8,9,11},43:{4,8,9,10,11,12,13,14},44:{2,3,7,9,10},
 45:{3,5,6,7,10,11,13,14},46:{2,3,4,5,7,8,9,12,13,14},47:{2},
 48:{3,4,6,7,8,9,11,12,13,14,15,16,17},49:{6,7,11,16,19,20,22,23},
 50:{2,3,4,5,6,7,8,10,11,13,14},51:{5,6,7,8,14,15,16,17,18,20},
 52:{5,6,8,9,10,12,13,14,16}}
def read_tsv(filename):
    with (ROOT/filename).open(encoding='utf-8',newline='') as stream:
        return list(csv.DictReader(stream,delimiter='\t'))
def first_candidate(text):
    while True:
        pos=text.find(r'\unsure{')
        if pos<0: return text
        start=pos+len(r'\unsure{');depth=1;end=start
        while depth:
            depth+=(text[end]=='{')-(text[end]=='}');end+=1
        text=text[:pos]+text[start:end-1].split('|',1)[0]+text[end:]
def norm(s):
    s=unicodedata.normalize('NFC',first_candidate(s)).replace('’',"'")
    for word in ('handwritten','inserted','deleted','uline','uuline','boxed','mathrel','mathbin','mathop','nolimits','text','mathrm','operatorname','qquad','quad','enspace'):
        s=re.sub(r'\\'+word+r'(?![A-Za-z])','',s)
    for a,b in [(r'\longrightarrow',r'\to'),(r'\longleftarrow',r'\leftarrow'),(r'\mid','|'),(r'\,',''),(r'\!',''),(r'\ ','')]:
        s=s.replace(a,b)
    return re.sub(r'[\s{}$&]','',s)
def esc(value):
    return value.replace('|',r'\|').replace('\n',' ')
def main():
    blind=read_tsv(PREFIX+'.tsv');sources=read_tsv(PREFIX+'_sources.tsv')
    assert [(r['scan'],r['place']) for r in blind]==[(r['scan'],r['place']) for r in sources]
    rows=[];ordinal={};flagged=0
    for b,r in zip(blind,sources):
        n=int(b['scan']);ordinal[n]=ordinal.get(n,0)+1
        lo,*rest=map(int,r['source_lines'].split('-'));hi=rest[-1] if rest else lo
        lines=(ROOT/'pages'/f'K36-02_36_scan{n:03}.tex').read_text().splitlines()
        current=' '.join(lines[lo-1:hi]);initial=r['first_pass_extract'];reading=b['what_the_crop_shows']
        def match(text):
            return 'contained' if norm(reading) in norm(text) else 'see scope'
        conflict=ordinal[n] in CONFLICTS[n]
        if conflict: assert r['settlement']
        flagged+=conflict
        rows.append((n,ordinal[n],b['place'],lo,hi,reading,initial,current,match(initial),match(current),conflict,r['settlement']))
    with (ROOT/(PREFIX+'_compare.md')).open('w',encoding='utf-8') as out:
        print('# Blind readings compared with the page files\n',file=out)
        print(f'{len(rows)} independent entries. The crop comparison identified {flagged} differences of reading, coverage, or layout, including proposed alternatives that were rejected. The lines cited are local to each scan fragment.\n',file=out)
        print('The first table gives every difference settled during the independent second reading, before the witness was opened. The final witness decisions are recorded by locus in K36-02_doubts.md. The register below includes all entries and compares their original and final page-file contexts. “Contained” tests the first candidate as a normalized substring. “See scope” includes short sketches, diagrams and prose descriptions that have no single matching substring. Script alphabets, accents and alphabetic case remain distinct in the test.\n',file=out)
        print('| Scan / entry | Crop or location | Blind reading | Settlement on the ink |\n|---|---|---|---|',file=out)
        for n,i,k,lo,hi,b,orig,cur,x,y,conf,settle in rows:
            if conf:print(f'| {n}.{i:02} | {k} | `{esc(b)}` | {esc(settle)} |',file=out)
        print('\n## Register of all comparisons\n',file=out)
        for n,i,k,lo,hi,b,orig,cur,x,y,conf,settle in rows:
            if i==1: print(f'\n### Scan {n}\n',file=out)
            print(f'- **{i:02} · {k}** (L{lo}–{hi}). Blind `{b}`. First pass **{x}**. Current **{y}**.',file=out)
            if x!='contained' or y!='contained' or conf:
                print(f'  - First pass: `{orig}`.',file=out)
                if orig!=cur: print(f'  - Current: `{cur}`.',file=out)
                if settle: print('  - '+settle,file=out)
    print(f'{len(rows)} blind entries; {flagged} adjudicated differences.')
if __name__=='__main__':
    main()
