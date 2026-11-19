#!/usr/bin/env python3
"""Download only already identified primary sources for local reading.

cache_sources is a transient reading cache, excluded from the deliverable ZIP.
The accompanying authored reference metadata records the inspected loci.
"""
import sys, urllib.request, subprocess
from pathlib import Path
O=Path(__file__).resolve().parent/'cache_sources';O.mkdir(exist_ok=True)
S={
'groth1969':('https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1968.Grothendieck.StandardConjs.pdf','Grothendieck1969_StandardConjectures'),
'icm1958':('https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf','ICM1958'),
'icm1970':('https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf','ICM1970_1'),
'sga6':('https://wstein.org/sga/sga/pdf/sga6.pdf','SGA6'),
'sga6iut':('https://www.iut-theory.org/divers/SGA6.pdf','SGA6_iut')}
for k in sys.argv[1:]:
    url,stem=S[k];p=O/(stem+'.pdf')
    if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=90).read())
    print(k,p.stat().st_size,'bytes',flush=True)
    subprocess.run(['pdftotext','-layout',str(p),str(O/(stem+'.txt'))],check=True)
    print(k,'text extracted',flush=True)
