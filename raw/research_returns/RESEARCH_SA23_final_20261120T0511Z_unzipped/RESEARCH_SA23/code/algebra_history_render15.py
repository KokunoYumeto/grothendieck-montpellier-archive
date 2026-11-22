"""Render cote1 physical pages1--24 for direct dating-evidence inspection."""
from pathlib import Path
import fitz,json,time,hashlib
root=Path(__file__).resolve().parents[1]
src=root/'sources/root_manuscript1_ranged.pdf'
t=time.perf_counter();sha=hashlib.sha256(src.read_bytes()).hexdigest()
doc=fitz.open(src)
dest=root/'sources/algebra_cote1_folios';dest.mkdir(exist_ok=True)
records=[]
for n in range(1,25):
 s=time.perf_counter();page=doc[n-1];pix=page.get_pixmap(matrix=fitz.Matrix(1900/page.rect.width,1900/page.rect.width),alpha=False)
 p=dest/f'page_{n:03d}.png';pix.save(p)
 records.append({'physical_pdf_page':n,'file':str(p.relative_to(root)),'width':pix.width,'height':pix.height,'elapsed_seconds':round(time.perf_counter()-s,6)})
out={'source':str(src.relative_to(root)),'source_bytes':src.stat().st_size,'sha256':sha,'page_count':len(doc),'renders':records,'elapsed_seconds':round(time.perf_counter()-t,6)}
(root/'logs/algebra_history_render15.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
