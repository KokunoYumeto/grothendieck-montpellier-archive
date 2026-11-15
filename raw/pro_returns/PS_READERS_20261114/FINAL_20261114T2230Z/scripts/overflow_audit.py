"""Retain every logged overflow, including superseded and failed builds."""
from pathlib import Path
import csv,re,json
P=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted((P/'logs').glob('*.log')):
    s=p.read_text(errors='replace');key='';ordinal=0
    for line in s.splitlines():
        if 'PS-SOURCE:' in line:key=line.split('PS-SOURCE:',1)[1].strip()
        m=re.search(r'Overfull \\([hv])box \(([\d.]+)pt too (wide|high)\)(.*)',line)
        if m:
            ordinal+=1
            rows.append({'log':str(p.relative_to(P)),'overflow_number':ordinal,'page_key':key,'box':m[1],'excess_pt':m[2],'location':m[4].strip(),'requires_visual_review':'yes'})
recovered=P/'records/RECOVERED_BUILD_RESULTS.json'
if recovered.exists():
    for n,build in enumerate(json.loads(recovered.read_text()),1):
        for i,item in enumerate(build['overflows'],1):
            rows.append({'log':f'records/RECOVERED_BUILD_RESULTS.json:entry{n}:{build["form"]}','overflow_number':i,'page_key':item['key'],'box':'h','excess_pt':str(item['pt']),'location':'Pre-reset measured result preserved in conversation; final proof required.','requires_visual_review':'yes'})
with (P/'records/OVERFLOW_HISTORY.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ['log'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'logged_overflows':len(rows),'source_pages':len({r['page_key'] for r in rows if r['page_key']}),'unlocated':sum(not r['page_key'] for r in rows)}))
