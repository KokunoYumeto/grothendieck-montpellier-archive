from pathlib import Path
import subprocess
import hashlib
import json
import re
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source = root / 'sources/mast_nachbin_inventory1997.pdf'
print(json.dumps({'source':str(source),'bytes':source.stat().st_size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}))
info_cmd = ['pdfinfo', str(source)]
info = subprocess.run(info_cmd,capture_output=True,text=True,timeout=60)
print('COMMAND',repr(info_cmd),'STATUS',info.returncode,'STDERR',repr(info.stderr),'STDOUT\n'+info.stdout,flush=True)
(root / 'notes/category_nachbin_inventory_pdfinfo.txt').write_text(info.stdout)
target = root / 'notes/category_nachbin_inventory_extracted.txt'
command = ['pdftotext','-layout',str(source),str(target)]
result = subprocess.run(command,capture_output=True,text=True,timeout=60)
print('COMMAND',repr(command),'STATUS',result.returncode,'STDERR',repr(result.stderr),'STDOUT',repr(result.stdout),flush=True)
if result.returncode == 0:
    contents = target.read_text()
    print('TEXT CHARACTERS',len(contents),flush=True)
    pages = contents.split('\f')
    for i, page in enumerate(pages,1):
        if re.search(r'groth|fredholm|hilbert|195[2345]|schwartz|dieudonn',page,re.I):
            print('=== EXTRACTED PHYSICAL PAGE',i,'===\n'+page,flush=True)
