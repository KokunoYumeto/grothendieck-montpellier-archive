from pathlib import Path
from urllib.request import Request,urlopen
from html.parser import HTMLParser
import hashlib
import subprocess

ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
sources=[
 ('Kothe_A201','https://kalliope-verbund.info/de/ead?ead.id=DE-611-HS-3165596'),
 ('Kothe_findingaid','https://www.sub.uni-goettingen.de/fileadmin/media/texte/spezialsammlungen/Nachl%C3%A4sse/Koethe.pdf'),
]
for name,url in sources:
    print('REQUEST',url,flush=True)
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
            data=response.read()
            print('STATUS',response.status,'FINAL',response.url,'BYTES',len(data),'SHA256',hashlib.sha256(data).hexdigest(),flush=True)
        suffix='pdf' if data.startswith(b'%PDF') else 'html'
        path=ROOT/f'notes/category_date_{name}.{suffix}';path.write_bytes(data)
        if suffix=='pdf':
            p=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
            print('EXTRACT',p.returncode,p.stderr.strip(),flush=True)
            pages=path.with_suffix('.txt').read_text().split('\f')
            for number,page in enumerate(pages,1):
                if 'Grothendieck' in page:
                    print('GROTHENDIECK_PAGE_PHYSICAL',number,flush=True)
                    print(page,flush=True)
                    target=ROOT/f'notes/category_date_Kothe_findingaid_physical_{number:03d}'
                    r=subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-scale-to','1600','-singlefile','-png',str(path),str(target)],capture_output=True,text=True)
                    print('RENDER',r.returncode,r.stderr.strip(),flush=True)
    except Exception as exc:
        print('FAILED',type(exc).__name__,str(exc),flush=True)
