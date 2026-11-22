#!/usr/bin/env python3
"""Locate the Gabriel original in the publicly downloaded journal volume."""
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
began = datetime.now(timezone.utc).isoformat()
source = root/'sources/gabriel1932_volume33.pdf'
target = root/'sources/gabriel1932_volume33.txt'
p = subprocess.run(['pdftotext','-layout',str(source),str(target)], capture_output=True, text=True)
out = {'started_utc': began, 'exit_code': p.returncode, 'stderr': p.stderr}
if p.returncode == 0:
    pages = target.read_text(errors='replace').split('\f')
    hits=[]
    for i,page in enumerate(pages):
        if re.search(r'(rearrangement.*fourier|positive\s+fourier|r\.?\s*m\.?\s*gabriel)', page, re.I):
            if i < 110 or re.search(r'rearrangement.*fourier|positive\s+fourier',page,re.I):
                hits.append({'pdf_page_1based':i+1,'page_head':page[:1600]})
    out.update(text_pages=len(pages), hits=hits, saved=str(target.relative_to(root)))
out['runtime_seconds']=time.perf_counter()-start
Path(__file__).with_name('part_c_gabriel_locate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
