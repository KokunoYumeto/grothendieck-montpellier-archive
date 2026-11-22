from pathlib import Path
import urllib.request,hashlib,json,time,subprocess
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url='https://iecl.univ-lorraine.fr/wp-content/uploads/2021/04/DELSARTE_archives_Bourbaki_cote_BKI.pdf';s=time.monotonic()
try:
    with urllib.request.urlopen(url,timeout=35) as response:
        data=response.read();final=response.url;typ=response.headers.get('Content-Type');status=response.status
    p=r/'sources/category_bourbaki_r230_bki_inventory.pdf';p.write_bytes(data)
    print(json.dumps({'url':url,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p),'seconds':time.monotonic()-s}),flush=True)
    if data.startswith(b'%PDF-'):
        for cmd in [['pdfinfo',str(p)],['pdftotext','-layout',str(p),str(r/'notes/category_bourbaki_r230_bki_inventory.txt')]]:
            p1=subprocess.run(cmd,capture_output=True,timeout=35)
            print(json.dumps({'command':cmd,'status':p1.returncode,'stdout':p1.stdout.decode(errors='replace'),'stderr':p1.stderr.decode(errors='replace')}),flush=True)
except Exception as e:print(json.dumps({'url':url,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-s}),flush=True)
