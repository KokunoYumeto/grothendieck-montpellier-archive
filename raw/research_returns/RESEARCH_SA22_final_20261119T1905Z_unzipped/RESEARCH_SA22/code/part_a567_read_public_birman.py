from pathlib import Path
import os, subprocess, time, concurrent.futures, json
import fitz
base=Path('/workspace/scratch/9c53b536a97f')
private=base/'source_reading'
start=time.perf_counter()
env=os.environ.copy()
env['LD_LIBRARY_PATH']='/tmp/part_a567_djvu/unpack/usr/lib/x86_64-linux-gnu'
env['OMP_THREAD_LIMIT']='1'
source=private/'part_a567_birman1974_public'
pdf=private/'part_a567_birman1974_pp148_161.pdf'
r=subprocess.run(['/tmp/part_a567_djvu/unpack/usr/bin/ddjvu','-format=pdf','-page=148-161',str(source),str(pdf)],capture_output=True,text=True,env=env,check=True)
d=fitz.open(pdf)
paths=[]
for i in range(len(d)):
    q=private/f'part_a567_birman1974_p{i+148}.png'
    d[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(q)
    paths.append(q)
def ocr(q):
    z=subprocess.run(['tesseract',str(q),'stdout','--psm','3'],capture_output=True,text=True,env=env,check=True)
    return q.stem,z.stdout
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    texts=list(pool.map(ocr,paths))
out=private/'part_a567_birman1974_pp148_161_ocr.txt'
out.write_text('\n\n'.join('--- '+n+' ---\n'+s for n,s in texts))
report={'kind':'document-access OCR, not mathematical testing','pages':len(d),'printed_pages':'148-161','elapsed_seconds':round(time.perf_counter()-start,6),'private_output':str(out),'full_book_distributed':False}
(base/'RESEARCH_SA22/code/part_a567_read_public_birman.out').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
