"""OCR physical pages1--72 of the existing public manuscript as a date finding aid.

OCR is not treated as a transcription or a proof of a missing date. The
retained page text and search contexts identify candidates for image reading.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import hashlib, json, os, re, subprocess, time
import fitz

root=Path(__file__).resolve().parents[1]
source=root/'sources/root_manuscript1_ranged.pdf'
folder=root/'notes/geometry_cote1_date_ocr'
folder.mkdir(exist_ok=True)
start=time.perf_counter()

def extract(number):
    with fitz.open(source) as doc:
        page=doc[number-1]
        matrix=fitz.Matrix(1500/page.rect.width,1500/page.rect.width)
        data=page.get_pixmap(matrix=matrix,alpha=False).tobytes('png')
    run=subprocess.run(['tesseract','stdin','stdout','-l','eng'],
                       input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                       env=dict(os.environ,OMP_THREAD_LIMIT='1'),timeout=60,check=True)
    content=run.stdout.decode('utf-8',errors='replace')
    (folder/f'page_{number:03d}.txt').write_text(content)
    return number,content

if __name__=='__main__':
    print('OCR physical pages1--72;8 processes;1 Tesseract thread each',flush=True)
    with ProcessPoolExecutor(max_workers=8) as executor:
        pages=list(executor.map(extract,range(1,73)))
    pattern=re.compile(r'195[0-9]|19[3456]\d|cher|lettre|amiti|novembre|decembre|janvier|fevrier|mars|avril|juillet|octobre|septembre|ao[uû]t',re.I)
    hits=[]
    for number,content in pages:
        lines=content.splitlines()
        for k,line in enumerate(lines):
            if pattern.search(line):
                hits.append(dict(pdf_page=number,line=k+1,context='\n'.join(lines[max(0,k-1):k+2])))
    report=dict(source=str(source.relative_to(root)),
                sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                pages=72,workers=8,width=1500,hits=hits,
                elapsed_seconds=time.perf_counter()-start,
                caveat='Handwriting OCR is only a finding aid; negative hits do not establish absence.')
    target=root/'logs/geometry_cote1_date_search.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
