from pathlib import Path
import subprocess,concurrent.futures,json,time
R=Path(__file__).resolve().parents[1];T=time.perf_counter();pages=range(2,22);d=R/'qa/koebe_ocr';d.mkdir(exist_ok=True)
def run(p):
 t=time.perf_counter();base=d/f'p{p:02d}'
 a=subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','140','-png','-singlefile',str(R/'sources/koebe1907_first.pdf'),str(base)],capture_output=True,text=True)
 b=subprocess.run(['tesseract',str(base)+'.png',str(base),'-l','eng'],capture_output=True,text=True)
 return {'pdf_page':p,'printed_page':p+189,'render_exit':a.returncode,'ocr_exit':b.returncode,'seconds':time.perf_counter()-t}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(run,pages))
(R/'sources/koebe1907_first_ocr.txt').write_text('\n\n'.join(f'PDF_PAGE={p}, PRINTED_PAGE={p+189}\n'+(d/f'p{p:02d}.txt').read_text() for p in pages))
out={'pages':len(rows),'seconds':time.perf_counter()-T,'records':rows,'scope':'source-reading OCR only; original images must be visually verified'}
(R/'code/root_koebe_ocr_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'pages':len(rows),'seconds':out['seconds'],'errors':[x for x in rows if x['render_exit'] or x['ocr_exit']]}))
