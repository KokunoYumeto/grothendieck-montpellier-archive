from pathlib import Path
import urllib.request,subprocess,hashlib,json
p=Path(__file__).resolve().parent
records=[]
for name,url in [('ErtlKellerQin2025','https://arxiv.org/pdf/2012.01337'),('Yuan2021HodgePublished','https://par.nsf.gov/servlets/purl/10327977')]:
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        data=urllib.request.urlopen(req,timeout=30).read();(p/(name+'.pdf')).write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(p/(name+'.pdf')),str(p/(name+'.txt'))],check=True)
        records.append({'name':name,'url':url,'status':'downloaded','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    except Exception as e: records.append({'name':name,'url':url,'status':'failed','error':str(e)})
(p/'surface_reduction_fetch_output.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
