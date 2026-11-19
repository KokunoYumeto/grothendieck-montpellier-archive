"""Exact page bookkeeping and PDF rendering for narrow supplemental checks."""
from pathlib import Path
import json,subprocess
P=Path(__file__).parent/'primary'
specs={
 'EsquisseFr':['5. Je voudrais','IsomT (X, Y )','6. Un des'],
 'sga4_II':['Corollaire 2.4.'],
 'sga4_IV':['4.2.1. —','4.2.2. —']}
out=[]
for stem,needles in specs.items():
    raw=(P/(stem+'.txt')).read_text();pages=raw.split('\f')
    for needle in needles:
        hits=[]
        for i,page in enumerate(pages,1):
            if needle in page:
                before='\f'.join(pages[:i-1])
                pos=raw.index(needle, len(before))
                hits.append({'pdf_page_1based':i,'pdf_page_0based':i-1,'text_line':raw[:pos].count('\n')+1,'header':page.strip().splitlines()[0]})
        out.append({'document':stem,'needle':needle,'hits':hits})
        if stem!='EsquisseFr' or needle=='IsomT (X, Y )':
            for hit in hits:
                n=hit['pdf_page_1based'];dest=P/f'{stem}_p{n}'
                r=subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','115','-png','-singlefile',str(P/(stem+'.pdf')),str(dest)],capture_output=True,text=True)
                hit['render']=str(dest)+'.png';hit['render_returncode']=r.returncode
(P/'passage_locations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
