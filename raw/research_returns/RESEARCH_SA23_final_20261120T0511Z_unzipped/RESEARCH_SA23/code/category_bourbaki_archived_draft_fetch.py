from pathlib import Path
import urllib.request, hashlib, json, time, subprocess
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
metadata=json.loads((root/'notes/category_bourbaki_wayback_available.json').read_text())
url=metadata['archived_snapshots']['closest']['url']
started=time.monotonic()
try:
 with urllib.request.urlopen(url,timeout=35) as response:
  data=response.read()
  record={'url':url,'final_url':response.url,'status':response.status,'content_type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 target=root/'notes/category_bourbaki_nbr082_archived.download'
 target.write_bytes(data)
 record.update(saved=str(target),seconds=time.monotonic()-started,pdf_magic=data[:5]==b'%PDF-')
 print(json.dumps(record),flush=True)
 if data[:5]==b'%PDF-':
  pdf=target.with_suffix('.pdf');pdf.write_bytes(data)
  command=['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))]
  result=subprocess.run(command,capture_output=True,timeout=40)
  print(json.dumps({'command':command,'status':result.returncode,'stderr':result.stderr.decode(errors='replace')}),flush=True)
except Exception as error: print(json.dumps({'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}),flush=True)
text=(root/'notes/category_bourbaki_delsarte_list.txt').read_text()
for number,page in enumerate(text.split('\f'),1):
 if '179 ' in page:
  print(json.dumps({'delsarte_list_physical_page':number,'text':page}),flush=True)
  command=['pdftoppm','-f',str(number),'-l',str(number),'-singlefile','-scale-to','2200','-png',str(root/'notes/category_bourbaki_delsarte_list.pdf'),str(root/f'notes/category_bourbaki_delsarte_page{number:03d}')]
  result=subprocess.run(command,capture_output=True,timeout=40)
  print(json.dumps({'command':command,'status':result.returncode,'stderr':result.stderr.decode(errors='replace')}),flush=True)
