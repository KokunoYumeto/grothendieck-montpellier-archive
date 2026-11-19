"""Fetch original primary PDFs used in the additional A36 search."""
from pathlib import Path
from urllib.request import urlopen,Request
import subprocess
R=Path(__file__).resolve().parents[4]
D=R/'work/p3_primary';D.mkdir(exist_ok=True)
urls={
 'koblitz1975':'https://www.numdam.org/item/CM_1975__31_2_119_0.pdf',
 'deligne1969lefschetz':'https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf',
}
for name,url in urls.items():
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
        if not data.startswith(b'%PDF'):raise ValueError('Response is not PDF')
        p=D/(name+'.pdf');p.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(p),str(D/(name+'.txt'))],check=True)
        print(name,url,len(data),'bytes; downloaded and extracted')
    except Exception as e: print(name,type(e).__name__,str(e))
subprocess.run(['pdftoppm','-f','24','-singlefile','-scale-to','1600','-png',str(D/'koblitz1975.pdf'),str(D/'koblitz141')],check=True)
