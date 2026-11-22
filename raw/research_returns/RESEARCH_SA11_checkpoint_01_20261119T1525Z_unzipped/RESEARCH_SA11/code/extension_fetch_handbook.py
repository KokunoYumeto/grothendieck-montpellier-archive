"""Preserve the already-opened Felsner--Goodman author chapter.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
"""
from pathlib import Path
import urllib.request, subprocess, time, hashlib, json
root=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
url='https://www.csun.edu/~ctoth/Handbook/chap5.pdf'
start=time.monotonic()
data=urllib.request.urlopen(url,timeout=45).read()
path=root/'sources/extension_FelsnerGoodman2017.pdf'
path.write_bytes(data)
subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],
               check=True,capture_output=True)
result=dict(url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
            runtime_s=time.monotonic()-start)
(root/'audit/extension_fetch_handbook_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
