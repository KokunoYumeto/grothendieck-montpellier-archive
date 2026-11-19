"""Open de Jong's author-hosted DVI and convert locally for exact theorem reading.
Original and extracted text stay in /tmp, outside the final dossier.
"""
import pathlib,subprocess,urllib.request,hashlib,sys
name=sys.argv[1]
url='https://www.math.columbia.edu/~dejong/papers/'+name+'.dvi'
target=pathlib.Path('/tmp/SA04_a_external');target.mkdir(exist_ok=True)
with urllib.request.urlopen(url,timeout=55) as r:data=r.read()
dvi=target/(name+'.dvi');pdf=target/(name+'.pdf');txt=target/(name+'.txt')
dvi.write_bytes(data)
subprocess.run(['dvipdfmx','-q','-o',str(pdf),str(dvi)],check=True)
subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True)
print('URL',url,'sha256',hashlib.sha256(data).hexdigest())
print('Extracted',txt,'bytes',txt.stat().st_size)
