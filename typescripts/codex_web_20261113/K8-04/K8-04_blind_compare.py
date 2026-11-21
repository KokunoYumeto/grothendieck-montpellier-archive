"""Compare the independently read passages with the first-reading register and the page files."""
from pathlib import Path
import argparse, csv, re
ROOT=Path(__file__).resolve().parent
BASE='K8-04'
def table(name):
    p=ROOT/(BASE+name)
    if not p.exists(): return []
    with p.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f,delimiter='\t'))
def unbrace(s,i):
    j=i+1
    depth=1
    while depth and j<len(s):
        depth += (s[j]=='{')-(s[j]=='}')
        j+=1
    return s[i+1:j-1],j
def plain(s):
    out=[]
    i=0
    wrapper=re.compile(r'\\(unsure|handwritten|inserted|deleted|margin|uline|uuline|mathrm|operatorname|text|mathbb|textsuperscript)\{')
    while i<len(s):
        m=wrapper.match(s,i)
        if m:
            v,i=unbrace(s,m.end()-1)
            if m[1]=='unsure': v=v.split('|')[0]
            out.append(plain(v))
        else:
            out.append(s[i]);i+=1
    s=''.join(out).replace('’',"'").replace(chr(92)+' ','')
    s=re.sub(r'\\(?:,|;|!|qquad|quad|left(?![a-zA-Z])|right(?![a-zA-Z]))','',s)
    s=re.sub(r'\\neq(?![a-zA-Z])',lambda _:r'\ne',s)
    return re.sub(r'[\s{}$&]','',s)
def quoted(s): return s.replace('|',r'\|').replace('\n',' ')
def run(num=None,write=False):
    blind=table('_blind.tsv')
    records={(r['scan'],r['place']):r for r in table('_collation.tsv')}
    output=['# Blind collation','',
     'Each independent entry was recorded before the corresponding keyed page was reopened. The register retains the original passage wherever the readings differed. Spaces, TeX grouping and editorial wrappers are ignored. The last column tests the settled passage against the current page file.','',
     '| Scan | Place | Independent reading | First reading | Resolution on the image | Settled text located |',
     '|---|---|---|---|---|---|']
    changed=unlocated=count=0
    for r in blind:
        n=r['scan'];p=r['place'];b=r['what the crop shows']
        if num is not None and int(n)!=num: continue
        page=(ROOT/'pages'/f'{BASE}_8_scan{int(n):03}.tex').read_text()
        rec=records.get((n,p))
        before=rec['first reading'] if rec else b
        after=rec['settled passage'] if rec else b
        ok=plain(after) in plain(page)
        differs=plain(b)!=plain(before)
        changed+=differs
        unlocated+=not ok
        if differs or not ok:
            output.append('| '+' | '.join(map(quoted,[n,p,b,before,rec['resolution'] if rec else 'Unmatched on current page','yes' if ok else 'no']))+' |')
            if num is not None: print(f'{p}\t{b}\t{before}\t{ok}')
        count+=1
    output.extend(['',f'{count} independent entries. {changed} differed in their reading. {unlocated} settled passages were not located in the current page files.'])
    if write: (ROOT/(BASE+'_blind_compare.md')).write_text('\n'.join(output)+'\n')
    return unlocated
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--scan',type=int)
    args=p.parse_args()
    raise SystemExit(1 if run(args.scan,args.scan is None) else 0)
