"""Compare independent crop readings with the first pass and the current pages."""
import csv
import json
import re
from pathlib import Path
from importlib import import_module

check = import_module('K64-10_check')
out = Path(__file__).resolve().parent
def first_choice(s):
    depth=0
    for i,x in enumerate(s):
        if x=='|' and depth==0:return s[:i]
        if x=='{':depth+=1
        if x=='}':depth-=1
    return s
def visible(s):
    # Keep accents, case, signs, subscripts and mathematical alphabets.
    rx=r'\\(unsure|inserted|deleted|uline|uuline|handwritten|text|underline|phantom|vphantom)\s*\{'
    while (m:=re.search(rx,s)):
        inside,end=check.arg(s,m.end());name=m[1]
        if name=='unsure':inside=first_choice(inside)
        if name in ('phantom','vphantom'):inside=''
        s=s[:m.start()]+inside+s[end:]
    s=re.sub(r'\\(?:underline|qquad|quad|left|right|Bigg|big)\b','',s)
    s=s.replace(r'\\','').replace('’',"'").replace(r'\,','').replace(r'\ ','').replace(r'\&','')
    return re.sub(r'[\s{}&$]','',s)
def relevant(lines,rng):
    a,_,b=rng.partition('-')
    return '\n'.join(lines[int(a)-1:int(b or a)])
def missing(reading,source):
    source=visible(source)
    return [p.strip() for p in reading.split('⟐') if visible(p.strip()) not in source]
def render():
    h=json.loads((out/'K64-10_blind_locations.json').read_text())
    with (out/'K64-10_blind.tsv').open() as f:observations=list(csv.DictReader(f,delimiter='\t'))
    report=['# Blind readings compared','',
            'The TSV contains the readings entered from the images before reopening each page. The comparison uses the same local line ranges in the saved first-pass excerpts and in the delivered page files. Each side of ⟐ is a separately checked feature. The search disregards TeX grouping, layout and spacing. It retains accents, case, numeric indices, signs and alphabet commands. The report also records changes in cancellation, stroke placement or attachment. Settlements below refer to the independent audit. Subsequent witness readings are in the doubts file.','']
    differences=[]
    mechanical=[]
    for row in observations:
        n=row['scan']; place=row['place']; words=row['what the crop shows']
        rec=h[n][place]
        final=relevant(check.page(int(n)).read_text().splitlines(),rec['lines'])
        before=missing(words,rec['initial'])
        after=missing(words,final)
        if before or rec.get('state'):differences.append((n,place,words,rec,before))
        mechanical.append([n,place,','.join(before) or 'match',','.join(after) or 'match'])
    report += [f'{len(observations)} local comparisons. {len(differences)} differed from the first pass.','',
               '| Scan | Locus | Independently read | First-pass difference | Settlement on the crop |','|---|---|---|---|---|']
    def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
    for n,place,words,r,before in differences:
        b=r.get('before') or ', '.join(before) or r['state']
        report.append('| '+' | '.join(map(cell,[n,place,words,b,r['resolution']]))+' |')
    report += ['','## Comparison with the delivered page files','',
               'A fragment can still differ after review when the original reading was retained, the independent form was kept as a second choice, or the witness subsequently settled a marked form. The companion JSON contains the exact pre-audit excerpts and line windows.','',
               '| Scan | Locus | Blind fragments absent from first preferred reading | Blind fragments absent from delivered preferred reading |','|---|---|---|---|']
    report.extend('| '+' | '.join(map(cell,r))+' |' for r in mechanical)
    (out/'K64-10_blind_compare.md').write_text('\n'.join(report)+'\n')
    print(f'{len(observations)} comparisons, {len(differences)} differences')
if __name__=='__main__':render()
