"""Render selected primary PDF pages and OCR them; preserve both for checking."""
from pathlib import Path
import subprocess,sys
from concurrent.futures import ThreadPoolExecutor
root=Path(__file__).resolve().parents[1]
pdf=Path(sys.argv[1]); label=sys.argv[2]
pages=[int(x) for x in sys.argv[3:]]
out=root/'research'/'primary_pages'/label
out.mkdir(parents=True,exist_ok=True)
def run(p):
    stem=out/f'page_{p:03d}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','130','-singlefile','-png',str(pdf),str(stem)],check=True,capture_output=True)
    r=subprocess.run(['tesseract',str(stem)+'.png','stdout','-l','eng'],check=True,capture_output=True,text=True)
    stem.with_suffix('.txt').write_text(r.stdout)
    return f'PAGE {p}\n'+r.stdout
with ThreadPoolExecutor(max_workers=3) as ex:
    for text in ex.map(run,pages):print(text)
