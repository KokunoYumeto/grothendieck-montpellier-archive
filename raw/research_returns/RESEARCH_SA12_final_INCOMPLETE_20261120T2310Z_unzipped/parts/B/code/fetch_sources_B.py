#!/usr/bin/env python3
"""Reproducible source fetches, PDF extraction and SHA-256 provenance for Part B.

Existing local sources are reused.  Network failure is recorded, not hidden.
This script performs no mathematical calculations.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import time
import urllib.request

base=Path(__file__).resolve().parents[1]
sources=base/"sources"
sources.mkdir(exist_ok=True)
items=[
 ("Marrama2026.pdf","https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.836.pdf"),
 ("Raynaud1970.pdf","https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf"),
 ("MoretBailly1985.pdf","https://perso.univ-rennes1.fr/laurent.moret-bailly/articles/PurCourbesWeb.pdf"),
 ("Kleiman2005.pdf","https://arxiv.org/pdf/math/0504020"),
 ("ChatzistamatiouRulling2011.pdf","https://arxiv.org/pdf/0911.3599"),
 ("ChatzistamatiouRullingErratum.pdf","https://www2.math.uni-wuppertal.de/~ruelling/erratum-corcohadd.pdf"),
 ("Lipman1978.pdf","https://www.math.purdue.edu/~jlipman/papers-older/%5B1978%5D%20Desingularization%20of%20two-dimensional%20schemes.pdf"),
 ("Stacks_0G4F.html","https://stacks.math.columbia.edu/tag/0G4F"),
 ("Stacks_0FD4.html","https://stacks.math.columbia.edu/tag/0FD4"),
 ("Stacks_0A3P.html","https://stacks.math.columbia.edu/tag/0A3P"),
 ("Stacks_0A4T.html","https://stacks.math.columbia.edu/tag/0A4T"),
 ("Stacks_0FD6.html","https://stacks.math.columbia.edu/tag/0FD6"),
 ("Stacks_0EC0.html","https://stacks.math.columbia.edu/tag/0EC0"),
 ("Stacks_03RP.html","https://stacks.math.columbia.edu/tag/03RP"),
 ("Stacks_0BFH.html","https://stacks.math.columbia.edu/tag/0BFH"),
 ("Schroer2024.pdf","https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/AlbaneseOpenSpaces_07.2023.pdf"),
 ("deJong1997.pdf","https://www.numdam.org/item/10.5802/aif.1575.pdf"),
 ("MilneAG2022.pdf","https://www.jmilne.org/math/Books/iAG2022.pdf"),
 ("Stacks_0BXT.html","https://stacks.math.columbia.edu/tag/0BXT"),
 ("Stacks_0CCJ.html","https://stacks.math.columbia.edu/tag/0CCJ"),
 ("Stacks_02KH.html","https://stacks.math.columbia.edu/tag/02KH"),
 ("Stacks_0EBJ.html","https://stacks.math.columbia.edu/tag/0EBJ"),
 ("Stacks_0BCY.html","https://stacks.math.columbia.edu/tag/0BCY"),
 ("Stacks_0BD2.html","https://stacks.math.columbia.edu/tag/0BD2"),
 ("CotnerZavyalov2024.pdf","https://arxiv.org/pdf/2204.06121"),
 ("CotnerZavyalov2024_source.tar","https://arxiv.org/src/2204.06121"),
 ("AchterCasalainaMartinVial2025.pdf","https://www.math.colostate.edu/~achter/math/alb.pdf"),
 ("Kollar2025.pdf","https://arxiv.org/pdf/2502.13800"),
 ("Geisser2020_corrected.pdf","https://www2.rikkyo.ac.jp/web/geisser/picard_corrected.pdf"),
 ("RavindraSrinivas_GrothendieckLefschetz.pdf","https://arxiv.org/pdf/math/0511134"),
 ("BoissiereGabberSerman2019.pdf","https://arxiv.org/pdf/1104.1861"),
 ("Stacks_01ZM.html","https://stacks.math.columbia.edu/tag/01ZM"),
 ("Stacks_038O.html","https://stacks.math.columbia.edu/tag/038O"),
 ("Stacks_038P.html","https://stacks.math.columbia.edu/tag/038P"),
 ("Stacks_05Y8.html","https://stacks.math.columbia.edu/tag/05Y8"),
 ("Lipman1969.pdf","https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf"),
 ("Stacks_06DI.html","https://stacks.math.columbia.edu/tag/06DI"),
 ("Stacks_06LN.html","https://stacks.math.columbia.edu/tag/06LN"),
 ("Stacks_02KE.html","https://stacks.math.columbia.edu/tag/02KE"),
 ("Stacks_03DW.html","https://stacks.math.columbia.edu/tag/03DW"),
 ("Stacks_045M.html","https://stacks.math.columbia.edu/tag/045M"),
 ("Stacks_0339.html","https://stacks.math.columbia.edu/tag/0339"),
 ("Stacks_031S.html","https://stacks.math.columbia.edu/tag/031S"),
 ("MilneEC2021.pdf","https://jmilne.org/math/Books/EC2.pdf"),
 ("CossartPiltant2019_draft.pdf","https://lmv.math.cnrs.fr/wp-content/uploads/2014/12/pdf_characmix.pdf"),
 ("CossartPiltant2019.pdf","https://arxiv.org/pdf/1412.0868"),
 ("Tanaka2015.pdf","https://arxiv.org/pdf/1502.01381"),
 ("Kelly2018.pdf","https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf"),
]

def fetch(item):
    name,url=item
    path=sources/name
    start=time.perf_counter()
    record={"name":name,"url":url,"accessed_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())}
    try:
        record["reused_existing_file"]=path.exists()
        if not path.exists():
            request=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 academic source verification"})
            with urllib.request.urlopen(request,timeout=45) as response:
                data=response.read()
            path.write_bytes(data)
        data=path.read_bytes()
        record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if path.suffix==".pdf":
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            proc=subprocess.run(["pdftotext","-layout",str(path),str(path.with_suffix(".txt"))],capture_output=True,text=True)
            record["pdftotext_returncode"]=proc.returncode
            record["pdftotext_stderr"]=proc.stderr
        record["status"]="saved"
    except Exception as error:
        record["status"]="failed"
        record["error"]=repr(error)
    record["elapsed_seconds"]=time.perf_counter()-start
    return record

started=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(fetch,items))
out={"sources":records,"elapsed_seconds":time.perf_counter()-started}
destination=base/"code"/"output"
destination.mkdir(exist_ok=True)
text=json.dumps(out,indent=2)+"\n"
stamp=time.strftime("%Y%m%dT%H%M%SZ",time.gmtime())
(destination/("fetch_sources_B_"+stamp+".json")).write_text(text)
print(text,end="")
