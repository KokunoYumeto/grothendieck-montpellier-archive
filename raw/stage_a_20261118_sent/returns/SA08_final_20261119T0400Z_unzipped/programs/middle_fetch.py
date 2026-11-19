"""Fetch middle-agent primary sources and preserve source/byte audit."""
from pathlib import Path
import urllib.request,json,hashlib,datetime,subprocess
root=Path(__file__).resolve().parents[1]
dest=root/'work/middle/references';dest.mkdir(exist_ok=True)
sources={'dejong1998.dvi':'https://www.math.columbia.edu/~dejong/papers/TATE.dvi','dejong1999err.dvi':'https://www.math.columbia.edu/~dejong/papers/ErratumTate.dvi','bmt2016.pdf':'https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf'}
for name,url in sources.items():
 try:
  with urllib.request.urlopen(url,timeout=40) as r:b=r.read()
  (dest/name).write_bytes(b)
  result={'source':url,'file':str(dest/name),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'status':'downloaded'}
  if name.endswith('.dvi'):
   proc=subprocess.run(['dvipdf',name,name[:-4]+'.pdf'],cwd=dest,capture_output=True,text=True)
   result['conversion_returncode']=proc.returncode;result['conversion_output']=proc.stdout+proc.stderr
  pdf=dest/(name[:-4]+'.pdf')
  if pdf.exists():subprocess.run(['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],check=True)
 except Exception as e:result={'source':url,'status':'failed','error':str(e)}
 result['date']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 print(json.dumps(result,ensure_ascii=False))
