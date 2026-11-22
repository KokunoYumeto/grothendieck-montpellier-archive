"""Public-source retrieval and exhaustive text finding-aid for Fredholm1956.

This is not a proof of a negative historical claim. Every hit is retained
to guide manual reading of the full paper and verification on page images.
"""
from pathlib import Path
from time import perf_counter
import re, subprocess, urllib.request

start=perf_counter()
root=Path(__file__).resolve().parents[1]
pdf=root/'notes/geometry_Fredholm1956.pdf'
txt=root/'notes/geometry_Fredholm1956_full.txt'
url='https://www.numdam.org/article/BSMF_1956__84__319_0.pdf'
if not pdf.exists():
    with urllib.request.urlopen(url,timeout=120) as response: data=response.read()
    assert data.startswith(b'%PDF')
    pdf.write_bytes(data)
    print('downloaded',url,len(data),'bytes')
subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True)
pages=txt.read_text().split('\f')
print('PDF_pages',len(pages)-int(not pages[-1].strip()))
patterns=['Hilbert','genre','Weyl','Hadamard','factoris','produit infini',
          'valeurs propres','trace','sommab','ordre du déterminant',
          'identités','CHAPITRE']
for term in patterns:
    hits=[]
    rx=re.compile(term,re.I)
    for pageno,page in enumerate(pages,1):
        lines=page.splitlines()
        for i,line in enumerate(lines):
            if rx.search(line):
                hits.append((pageno,i+1,'\n'.join(lines[max(0,i-2):i+4])))
    print('\nTERM',term,'COUNT',len(hits))
    for pageno,line,context in hits:
        print('PDFPAGE',pageno,'LINE',line)
        print(context)
print('\nelapsed_seconds',round(perf_counter()-start,3))
