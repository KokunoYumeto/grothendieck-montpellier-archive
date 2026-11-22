"""Retrieve the independently advertised 1964 NBS journal paper with a total timeout."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time
import fitz

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
source=root/'sources/root_schatten1964.pdf'
url='https://nvlpubs.nist.gov/nistpubs/jres/68B/jresv68Bn4p185_A1b.pdf'
command=['curl','--location','--fail','--silent','--show-error','--max-time','35','--output',str(source),url]
result=subprocess.run(command,capture_output=True,text=True,timeout=40)
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'url':url,'command':command,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
if result.returncode==0:
    data=source.read_bytes()
    record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    with fitz.open(source) as document:
        text='\n\f\n'.join(page.get_text() for page in document)
        (root/'sources/root_schatten1964.txt').write_text(text)
        record.update(pdf_pages=len(document),extracted_characters=len(text))
        images=[]
        for number in [1,9]:
            page=document[number-1]
            target=root/'sources'/f'root_schatten1964_p{number:03d}.png'
            page.get_pixmap(matrix=fitz.Matrix(1700/page.rect.width,1700/page.rect.width),alpha=False).save(target)
            images.append(str(target.relative_to(root)))
        record.update(rendered_physical_pages=[1,9],images=images,
            visual_inspection='Rendering is not reading; actual image displays are recorded separately.')
record['elapsed_seconds']=time.perf_counter()-started
(root/'logs/root_schatten_journal19.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
