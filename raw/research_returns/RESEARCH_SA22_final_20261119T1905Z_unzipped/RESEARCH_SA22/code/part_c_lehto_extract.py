"""Extract the privately held original PDF for bibliographic/theorem inspection."""
import concurrent.futures
import datetime
import json
from pathlib import Path
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
READING=ROOT.parent/'source_reading'
pdf=READING/'lehto_virtanen1973_pdf_candidate.pdf'
txt=READING/'lehto_virtanen1973_pdf_candidate.txt'
commands=[['pdfinfo',str(pdf)],['pdftotext','-layout',str(pdf),str(txt)]]
def one(command):
    begin=time.perf_counter()
    done=subprocess.run(command,capture_output=True,text=True)
    return {'command':command,'returncode':done.returncode,'stdout':done.stdout,'stderr':done.stderr,'elapsed_seconds':time.perf_counter()-begin}
begin=time.perf_counter()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(one,commands))
result={'started_utc':started,'elapsed_seconds':time.perf_counter()-begin,'scope':'Two local original-source reading subprocesses, no mathematical certificate. Full text stays outside deliverable.','results':rows}
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_lehto_extract_output.json').write_text(text+'\n')
print(text)
