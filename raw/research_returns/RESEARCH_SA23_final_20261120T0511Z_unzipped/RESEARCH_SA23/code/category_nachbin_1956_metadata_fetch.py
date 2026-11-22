from pathlib import Path
import urllib.request, hashlib, json, subprocess, time
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url = 'https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-1994-25.pdf'
target = root / 'notes/category_nachbin_1956_bibliography1994.pdf'
started = time.monotonic()
try:
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read()
        status = response.status
        final_url = response.url
    target.write_bytes(data)
    print(json.dumps({'url':url,'final_url':final_url,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'seconds':time.monotonic()-started,'saved':str(target)}),flush=True)
    commands = [
        ['pdfinfo',str(target)],
        ['pdftotext','-layout',str(target),str(target.with_suffix('.txt'))],
        ['pdftoppm','-f','1','-l','1','-singlefile','-scale-to','1800','-png',str(target),str(root/'notes/category_nachbin_1956_bibliography_page001')],
    ]
    for command in commands:
        result = subprocess.run(command,capture_output=True,timeout=40)
        print(json.dumps({'command':command,'returncode':result.returncode,'stdout':result.stdout.decode(errors='replace'),'stderr':result.stderr.decode(errors='replace')}),flush=True)
except Exception as error:
    print(json.dumps({'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}),flush=True)
