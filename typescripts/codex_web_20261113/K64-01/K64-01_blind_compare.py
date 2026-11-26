"""Compare the blind TSV with its places in the distributed page files. Run with Python 3."""
from pathlib import Path
import csv, re, difflib, json
BASE=Path(__file__).resolve().parent
TAG="K64-01"
# One line or line range in the individual page file per blind observation, in TSV order.
PLACE={
2:'3 5 3 5 5 5 5 5 6',
3:'1 2 4 4 4 4 4 4 4 4 4 4 6 6 6 8 10 12 12 14 17 19 17 20 20 20 20 20 20 20 23 24 25 27',
4:'2 2 2 2 2 6 8 8 8 10 10 10 13 16 17 20 20 20 20 24 24 26 26 26 26 26 27',
5:'1 2 2 2 2 2 2 2 2 2 2 2 2 4 6 8 8 11 12 12 16 16 17',
6:'2 4 10 12 12 12 12 14 16 16 16 16 16 16 16 16 16 18 16 16 20 20 20 22 20 20 20 20 20 20 26 24 24 27',
7:'1 8 8 8 8 10 2 2 4 6 14 14 18 20 20 20 22 22 22 24 24 24 31-33 37-38 34-36 34-41 43',
8:'2 6 6 10-11 14 15 15 17-18 21 22 22 22 22 22 22 22 23',
9:'1 2 4-7 9 9 11 12 17 17 17 19 19 21 24-26 28 28 33-35 29 29 29 29,31 37',
10:'2 4 6 6 6 6 8 10 10 10 12 12 12 12 12 20 22 16,18 27',
11:'1,39 4-5 6 9 13-15 18 20,22,24 26 28 30 32 36 38',
12:'4 8 10 10 10 10 14 16 17 19 21 23 24',
13:'1,38 2,4 6,8 11-17 19 19 19 19 19 19 22-23 26 26 28-35 26',
14:'3-7 9 9 9 9 9 9 9 9 9 9 9 11-17 19'}
RENDER={
 r"\longrightarrow":"→",r"\to":"→",r"\hookrightarrow":"↪",r"\longmapsto":"↦",r"\mapsto":"↦",
 r"\xrightarrow{\sim}":"→≃",r"\simeq":"≃",r"\sim":"∼",r"\approx":"≈",r"\times":"×",r"\ne":"≠",r"\in":"∈",
 r"\setminus":"∖",r"\wedge":"∧",r"\subset":"⊂",r"\pm":"±",r"\implies":"⇒",r"\cap":"∩",r"\amalg":"⊔",
 r"\omega":"ω",r"\Gamma":"Γ",r"\varpi":"ϖ",r"\rho":"ρ",r"\tau":"τ",r"\ast":"*",r"\circledast":"⊛",r"\circ":"∘",r"\bigl":"",r"\bigr":"",
 r"\Longleftrightarrow":"⇔",r"\longleftrightarrow":"↔",r"\Longrightarrow":"⇒",r"\#":"#",
 r"\{":"｛",r"\}":"｝",r"\quad":" ",r"\qquad":" ",r"\,":" ",r"\&":" ",r"\text{---}":"—"}
def rendered(s):
    s=s.replace('’',"'").replace('′',"'").replace('″',"''").replace('²','^2').replace('₂','_2').replace('³','^3').replace('₃','_3').replace('⁺','^+').replace('⁻¹','^-1')
    for a in sorted(RENDER,key=len,reverse=True):
        s=re.sub(re.escape(a)+(r'(?![A-Za-z])' if a[-1].isalpha() else ''),lambda m:RENDER[a],s)
    s=re.sub(r'\\(?:mathfrak|mathcal|mathscr|mathbb|mathrm|underline|uline|text|deleted|inserted|unsure|illegible|margin|mspage|tag\*?)\s*','',s)
    s=s.replace(chr(96)*2,'“').replace("''",'”').replace('\\hfill',' ').replace('\\','').replace('$','').replace('&',' ')
    return re.sub(r'\s+',' ',s.replace('{','').replace('}','').replace('｛','{').replace('｝','}')).strip()

def sections(lines,ref):
    result=[]
    for chunk in ref.split(','):
        a,*b=map(int,chunk.split('-')); end=b[0] if b else a
        assert 1<=a<=end<=len(lines), (ref,len(lines))
        result.extend(lines[a-1:end])
    return ' '.join(result)

def match(blind,raw,focus=None):
    target=rendered(raw); key=rendered(blind)
    pivot=target.find(focus) if focus else -1
    exact=target.find(key) if key else -1
    if exact!=-1 and pivot==-1:pivot=exact
    if pivot==-1:pivot=difflib.SequenceMatcher(None,key,target,autojunk=False).find_longest_match().b
    lo=max(0,pivot-24); hi=min(len(target),pivot+max(30,min(len(key)+14,210)))
    return ('…' if lo else '')+target[lo:hi]+('…' if hi<len(target) else ''), exact!=-1

def esc(x):return x.replace('|',r'\|').replace('\n',' ')
def run():
    with (BASE/f"{TAG}_blind.tsv").open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    recovery_fresh=[r for r in rows if r["place"].startswith("Recovery / ")]
    rows=[r for r in rows if r not in recovery_fresh]
    directory=json.loads((BASE/f"{TAG}_reading_key.json").read_text(encoding='utf-8'))
    out=['# Blind readings against the page files','',
         'The blind column gives the observation saved before the page file was opened on the second pass. The line numbers refer to that TeX file. The program extracts the cited line each time it runs, removes editorial wrappers for comparison and renders some common signs. Vertical bars within an excerpt separate reading candidates. Literal means the blind excerpt occurs in its designated line after these substitutions. A string that matches the corrected page can still have differed on the blind pass. Some observations describe the graphic form of a cancellation, figure or insertion. The settlement column records the second-pass decision before the witness was consulted. Page excerpts are from the current files. Later decisions at the frozen marks, including the title on scan 2, are identified in the Witness check table of the doubts file. The TeX preserves placement, typeface and cancellation.','']
    differences=[]
    total=0;literal=0;diffs=0
    for scan,ref in PLACE.items():
        data=[r for r in rows if int(r['scan'])==scan]
        refs=ref.split();assert len(refs)==len(data),(scan,len(refs),len(data))
        lines=(BASE/'pages'/f'{TAG}_64_scan{scan:03}.tex').read_text(encoding='utf-8').splitlines()
        out.extend([f'## Scan {scan}','','| Place · TeX line | Blind reading | Page excerpt | Comparison and settlement |','|---|---|---|---|'])
        for i,(r,where) in enumerate(zip(data,refs),1):
            k=f'{scan}.{i}'; item=directory.get(k,{})
            reading=r['what the crop shows']; extract,agrees=match(reading,sections(lines,where),item.get('focus'))
            literal+=int(agrees);total+=1;diffs+=int(bool(item.get('difference')))
            settlement=item.get('decision') or ('The observed reading occurs in this passage.' if agrees else 'The observation identifies the same objects or words in abbreviated or graphic form. See the stroke comparison for this sheet.')
            if item.get('difference'):
                differences.append((str(scan),r['place']+' · '+where,reading,settlement))
            status='Different reading. ' if item.get('difference') else ('Literal. ' if agrees else 'Graphic or partial correspondence. ')
            out.append('| '+' | '.join(esc(v) for v in [r['place']+' · '+where,reading,extract,status+settlement])+' |')
        out.append('')
    assert total==len(rows);out[2:2]=[f'{total} observations. {diffs} places have substantive differences recorded below. {literal} blind strings occur literally after conversion.','']
    index=['## Where the blind reading differed','',
           '| Scan | Place and TeX line | Blind reading | Decision on the scan |',
           '|---|---|---|---|']
    index.extend('| '+' | '.join(esc(value) for value in entry)+' |' for entry in differences)
    index.extend(['','## All blind observations',''])
    first_page=out.index('## Scan 2')
    out[first_page:first_page]=index
    out[0]='# Blind readings against the delivered pages'
    out.insert(2,'The original reader’s observations, recorded decisions and their present-day excerpts occupy the first tables. The newly acquired source-first readings and direct-ink settlements follow them.')
    out.extend(['','## Independent recovery reading','','Each observation was saved in a source-only file before opening the returned TeX. All observations are reproduced verbatim in the TSV. The extracts below are calculated from the delivered page. Each final column describes the direct inspection of that sheet.','','| Sheet and lines | Source-only reading | Delivered excerpt | Resolution |','|---|---|---|---|'])
    with (BASE/'recovery'/'blind-settlements.tsv').open(encoding='utf8',newline='') as handle:
        conclusions=dict(list(csv.reader(handle,delimiter=chr(9)))[1:])
    for r in recovery_fresh:
        n=r['scan'];ref=r['place'].split('TeX ')[1]
        lines=(BASE/'pages'/f'{TAG}_64_scan{int(n):03}.tex').read_text(encoding='utf8').splitlines()
        sample=sections(lines,ref)
        excerpt=sample if len(sample)<=400 else sample[:217]+' … '+sample[-170:]
        fields=[n+' · '+ref,r['what the crop shows'],excerpt,conclusions[n]]
        out.append('| '+' | '.join(esc(x) for x in fields)+' |')
    out.extend(['',str(len(recovery_fresh))+' independently recorded continuous passages; exact differences in recovery/prewitness-revisions.tsv and recovery/witness-changes.tsv.'])
    (BASE/f'{TAG}_blind_compare.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(f'{total} mapped; {literal} literal; {diffs} reading differences.')
if __name__=='__main__':run()
