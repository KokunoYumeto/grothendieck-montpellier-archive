from pathlib import Path
import urllib.request
import hashlib
import subprocess
import json
import time
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url = 'https://www.sbpcnet.org.br/site/publicacoes/outras-publicacoes/caderno_digital/caderno_7.pdf'
target = root / 'notes/category_nachbin_1956_caderno7.pdf'
started = time.monotonic()
try:
    with urllib.request.urlopen(url,timeout=60) as response:
        data = response.read()
        info = {'url':url,'final_url':response.url,'status':response.status,'content_type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'elapsed_seconds':round(time.monotonic()-started,3)}
    if not data.startswith(b'%PDF'):
        raise ValueError('Public URL did not return a PDF')
    target.write_bytes(data)
    info['saved'] = str(target)
    print(json.dumps(info),flush=True)
    for command in [['pdfinfo',str(target)],['pdftotext','-layout',str(target),str(root/'notes/category_nachbin_1956_caderno7.txt')]]:
        result = subprocess.run(command,capture_output=True,text=True,timeout=60)
        print('COMMAND',repr(command),'STATUS',result.returncode,'STDOUT',repr(result.stdout),'STDERR',repr(result.stderr),flush=True)
except Exception as exc:
    print(json.dumps({'url':url,'error':repr(exc),'elapsed_seconds':round(time.monotonic()-started,3)}),flush=True)
