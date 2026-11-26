"""Compare the independently entered crop probes with the transcription at two stages.

Run without arguments from the extracted folder. K64-08_collation.tsv carries
the first-pass comparison, source line numbers and the decisions on the crops.
"""
from pathlib import Path
import argparse, csv, re
ROOT=Path(__file__).resolve().parent
def tsv(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def norm(s, layers):
    s=s.replace(r'\widetilde',r'\tilde')
    s=re.sub(r'\\(?:long)?(mapsto|rightarrow|leftarrow)\b',r'\\\1',s)
    s=s.replace(r'\hookrightarrow',r'\hookto')
    s=re.sub(r'\\(?:hphantom|hspace)\{(?:[^{}]|\{[^{}]*\})*\}', '',s)
    s=re.sub(r'\\(?:qquad|quad|bigl|bigr|left|right|mathbin|mathrel|text|mathrm|operatorname)\b','',s)
    s=s.replace(r'\,','').replace(r'\;','').replace(r'\!','').replace(r'\ ','')
    s=s.replace('—','-').replace(r'\dfrac',r'\frac').replace(r'\tfrac',r'\frac')
    # A plain D cannot match a D inside a double-struck or script glyph.
    alphabets=('mathbb','mathcal','mathscr','mathfrak')
    def glyph(m):
        letter=m[2] or m[3]
        return chr(0xE100+128*alphabets.index(m[1])+ord(letter))
    s=re.sub(r'\\(mathbb|mathcal|mathscr|mathfrak)\s*(?:\{\s*([A-Za-z])\s*\}|([A-Za-z]))',glyph,s)
    s=re.sub(r'(?<!\\)&','',s)
    # Keep the preferred reading only; alternatives remain in the page file.
    while (a:=s.find(r'\unsure{'))>=0:
        end=level_end(s,a+7)
        body=s[a+8:end-1].split('|')[0];s=s[:a]+body+s[end:]
    if not layers:s=re.sub(r'\\(?:deleted|inserted|uline)\b','',s)
    s=re.sub(r'[\s{}$]','',s)
    return s
def level_end(s,opening):
    level=1
    for at in range(opening+1,len(s)):
        if s[at] in '{}' and (at==0 or s[at-1]!='\\'):
            level+=1 if s[at]=='{' else -1
            if level==0:return at+1
    raise ValueError('Unclosed editorial macro')
def local(s,x,line_key):
    if x.get(line_key):
        s=s.splitlines()[int(x[line_key])-1]
    start=x.get('region_start','');end=x.get('region_end','')
    if start and start in s:s=s[s.index(start):]
    if end and end in s:s=s[:s.index(end)]
    return s

def contains(s,probe):
    layers=any('\\'+k in probe for k in ('deleted','inserted','uline'))
    return norm(probe,layers) in norm(s,layers)
def row(x):return '| '+' | '.join(str(c).replace('|','\\|').replace('\n',' ') for c in x)+' |\n'
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pages',type=Path,default=ROOT/'pages')
    args=parser.parse_args()
    probes=tsv(ROOT/'K64-08_blind.tsv')
    base=tsv(ROOT/'K64-08_collation.tsv')
    assert [(p['scan'],p['place'],p['what_the_crop_shows']) for p in probes]==[(p['scan'],p['place'],p['what_the_crop_shows']) for p in base]
    changed=[]; still=0
    for x in base:
        s=(args.pages/f'K64-08_64_scan{x["scan"]}.tex').read_text()
        match=contains(local(s,x,'current_line'),x['what_the_crop_shows']);still+=not match
        if x['first_match']=='no' or not match or x['disposition']:
            changed.append((x,match))
    with (ROOT/'K64-08_blind_compare.md').open('w') as f:
        f.write('# K64-08 · Blind collation\n\n'+str(len(base))+' probes from the image reading. The comparison ignores spacing, layout commands and equivalent arrow lengths. Each probe is restricted to its numbered source line and, where needed, to a smaller part of that line. The line numbers at each stage are recorded in the collation TSV. It retains letter alphabets, left/right decoration, preferred doubt readings and explicitly recorded cancellations. A probe may match part of a longer word or formula. Such substring matches are not a verdict on the whole reading. The local evidence and decision columns distinguish visual differences from transcription conventions or a discontinuous excerpt. The last column compares the current page files.\n\n')
        f.write('| Scan | Place | Independent reading | First-page evidence | Decision on the crop | Current excerpt match |\n|---|---|---|---|---|---|\n')
        for x,match in changed:f.write(row([x['scan'],x['place'],'\x60'+x['what_the_crop_shows']+'\x60','\x60'+x['first_excerpt']+'\x60' if x['first_excerpt'] else 'matched the blind entry',x['disposition'] or 'Current preferred reading changed at witness check; see Witness check in the doubts file.','yes' if match else 'no']))
    print(len(base),'probes;',sum(x['first_match']=='no' for x in base),'unmatched first-pass excerpts;',still,'unmatched current excerpts.')
if __name__=='__main__':main()
