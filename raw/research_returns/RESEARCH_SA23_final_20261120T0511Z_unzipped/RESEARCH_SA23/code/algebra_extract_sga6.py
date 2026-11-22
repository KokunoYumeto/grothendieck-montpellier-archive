"""Extract and index the original SGA6 scan, without substituting a modern transcription."""
from pathlib import Path
import subprocess
import time

start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
pdf=root/'sources/algebra_SGA6.pdf'
txt=root/'sources/algebra_SGA6.txt'
command=['pdftotext','-layout',str(pdf),str(txt)]
result=subprocess.run(command,capture_output=True,text=True)
print('command',repr(command),'exit',result.returncode,flush=True)
print(result.stderr,flush=True)
result.check_returncode()
pages=txt.read_text().split('\f')
print('pages',len(pages)-1,'bytes',txt.stat().st_size,flush=True)
for needle in ['EXPOSÉ VII','EXPOSE VII','EXPOSÉ  VII','Proposition 1.7','1.7.','Koszul','Deligne']:
    hits=[i+1 for i,page in enumerate(pages) if needle.lower() in page.lower()]
    print(repr(needle),'physical pages',hits,flush=True)
print('Elapsed seconds',time.perf_counter()-start)
