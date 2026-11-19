"""Read-only research OCR of an original primary source; copyrighted OCR stays in work/."""
from pathlib import Path
import fitz, subprocess
from concurrent.futures import ThreadPoolExecutor
root=Path(__file__).resolve().parents[2]
source=root/'work/p2_primary/sga7_original.pdf'
out=root/'work/root_primary/sga7_first'
out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(source)
jobs=[]
for n in range(0,45):
    image=out/f'pdf_{n+1:03}.png'
    if not image.exists():doc[n].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(image)
    jobs.append((n,image))
def run(job):
    n,image=job
    dest=image.with_suffix('.txt')
    if not dest.exists():
        r=subprocess.run(['tesseract',str(image),'stdout','-l','eng'],capture_output=True,text=True,check=True)
        dest.write_text(r.stdout)
    return n,dest.read_text()
with ThreadPoolExecutor(max_workers=5) as ex:
    results=sorted(ex.map(run,jobs))
(out/'combined.txt').write_text('\n\n'.join(f'PDF PAGE {n+1}\n{t}' for n,t in results))
print(f'OCR completed for {len(results)} pages; research files excluded from deliverable ZIP.')
