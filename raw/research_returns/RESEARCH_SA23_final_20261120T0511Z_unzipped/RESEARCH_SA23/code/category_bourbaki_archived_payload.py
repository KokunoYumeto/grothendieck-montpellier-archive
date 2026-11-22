from pathlib import Path
from html.parser import HTMLParser
import urllib.request, hashlib, json, time, subprocess
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Playback(HTMLParser):
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='iframe' and attrs.get('id')=='playback': self.url=attrs['src']
parser=Playback(); parser.feed((root/'notes/category_bourbaki_nbr082_archived.download').read_text())
url=parser.url;started=time.monotonic()
try:
 with urllib.request.urlopen(url,timeout=35) as response:
  data=response.read()
  record={'url':url,'final_url':response.url,'status':response.status,'content_type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 target=root/'notes/category_bourbaki_nbr082_payload.download';target.write_bytes(data)
 record.update(saved=str(target),seconds=time.monotonic()-started,pdf_magic=data[:5]==b'%PDF-')
 print(json.dumps(record),flush=True)
 if data[:5]==b'%PDF-':
  pdf=root/'notes/category_bourbaki_nbr082.pdf';pdf.write_bytes(data)
  for command in [['pdfinfo',str(pdf)],['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],['pdftoppm','-f','1','-l','1','-singlefile','-scale-to','2200','-png',str(pdf),str(root/'notes/category_bourbaki_nbr082_page001')]]:
   result=subprocess.run(command,capture_output=True,timeout=40)
   print(json.dumps({'command':command,'status':result.returncode,'stdout':result.stdout.decode(errors='replace'),'stderr':result.stderr.decode(errors='replace')}),flush=True)
except Exception as error: print(json.dumps({'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}),flush=True)
