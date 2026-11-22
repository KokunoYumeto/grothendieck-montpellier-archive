from pathlib import Path
import urllib.request,datetime,time,hashlib,json
import fitz
base=Path('/workspace/scratch/9c53b536a97f')
private=base/'source_reading';project=base/'RESEARCH_SA22'
url='https://www.ias.edu/sites/default/files/library/pdfs/hs/cos.pdf'
t=time.perf_counter();started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with urllib.request.urlopen(url,timeout=45) as f:
 data=f.read();status=f.status
source=private/'ias1980_community_of_scholars.pdf';source.write_bytes(data)
doc=fitz.open(source)
path=private/'part_c_ias1980_p248.png'
doc[265].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(path)
text_path=private/'part_c_ias1980_p248.txt';text_path.write_text(doc[265].get_text())
report={'started_utc':started,'elapsed_seconds':time.perf_counter()-t,'scope':'One ordinary original IAS-directory download, one exact-page render/text read; bibliographic identity only, not mathematical testing. Full volume outside deliverable.','url':url,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pages':len(doc),'printed_page':248,'pdf_page':266,'image':str(path),'text':str(text_path)}
payload=json.dumps(report,indent=2);(project/'code/part_c_lieberman_ias_identity_output.json').write_text(payload+'\n');(project/'code/part_c_lieberman_ias_identity_output.txt').write_text(payload+'\n');print(payload)
