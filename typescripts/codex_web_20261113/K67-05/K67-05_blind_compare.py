"""Compare independent crop readings and their anchored TeX fragments."""
import csv
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ID='K67-05'
def norm(s):
    s=s.replace('’',"'").replace('~',' ').replace('$','').replace('\\,',' ').replace('\\quad',' ')
    s=s.replace('\\mid','|').replace('\\vert','|')
    for _ in range(2):
        s=re.sub(r'\\(?:unsure|deleted|inserted|uline|uuline|margin|mspage|text|mathrm|operatorname|mathord|ensuremath)\{([^{}]*)\}',r'\1',s)
    return re.sub(r'\s+','',s)
def rows(fn):
    with (ROOT/fn).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def show(s):
    return '<code>'+s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')+'</code>'
def compare():
    blind=rows(ID+'_blind.tsv')
    anchors={(r['scan'],r['place']):r for r in rows(ID+'_collation.tsv')}
    out=['# Blind comparison','','The crop readings preceded reopening each page. The first-pass and accepted fragments in the collation file retain the historical comparison after later witness decisions. Spaces and presentational markup are ignored.','','| Scan | Crop | Blind reading | First pass | Decision on the ink |','|---|---|---|---|---|']
    count=0
    for b in blind:
        a=anchors[b['scan'],b['place']]
        if norm(b['what the crop shows'])!=norm(a['first pass']):
            count+=1;out.append('| '+' | '.join([b['scan'],b['place'],show(b['what the crop shows']),show(a['first pass']),a['decision'].replace('|','／')])+' |')
        current=(ROOT/'pages'/f"{ID}_67_scan{int(b['scan']):03}.tex").read_text()
        if norm(a['current fragment']) not in norm(current) and a['current fragment'] not in current:
            raise ValueError(f"Cannot locate final anchor {b['scan']} {b['place']}: {a['current fragment']}")
    out[2]+=f' {len(blind)} crop readings compared. {count} differ from the first pass.'
    (ROOT/(ID+'_blind_compare.md')).write_text('\n'.join(out)+'\n')
    return count
if __name__=='__main__':print(compare())
