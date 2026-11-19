"""Download the opened primary B.1--B.3 sources and extract readable text.
This records the transfer route used in the preliminary source checks too.
No source is needed as an oracle for the finite computational certificates.
"""
from pathlib import Path
import urllib.request, gzip, subprocess, time, json

root=Path(__file__).resolve().parents[1]
sources=root/'sources'
items=[
 ('Schneps1994.pdf','https://webusers.imj-prg.fr/~leila.schneps/Fschneps.pdf'),
 ('Jones2018.source.gz','https://arxiv.org/e-print/1805.09764'),
 ('Jones2018.pdf','https://arxiv.org/pdf/1805.09764'),
 ('Wendl2015.pdf','https://www2.mathematik.hu-berlin.de/~wendl/pub/jhol_bookv33_2.pdf'),
 ('LandoZvonkin2004.pdf','https://www-users.cse.umn.edu/~reiner/Classes/Math8680Fall2014Papers/LandoZvonkin.pdf'),
]
results=[]
for name,url in items:
    begin=time.perf_counter(); p=sources/name
    try:
        if not p.exists():
            with urllib.request.urlopen(url,timeout=45) as response:
                data=response.read(); p.write_bytes(data)
        if name.endswith('.pdf'):
            subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
        if name.endswith('.gz'):
            (sources/'Jones2018.tex').write_bytes(gzip.decompress(p.read_bytes()))
        result={'file':name,'url':url,'bytes':p.stat().st_size,'status':'success',
                'seconds':round(time.perf_counter()-begin,3)}
    except Exception as exc:
        result={'file':name,'url':url,'status':'failed','error':str(exc),
                'seconds':round(time.perf_counter()-begin,3)}
    results.append(result)
    print(json.dumps(result),flush=True)
(root/'logs/B_fetch_sources.json').write_text(json.dumps(results,indent=2)+'\n')
