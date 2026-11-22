"""Add the final page carrying the allowed 0.41342pt box to actual visual QA."""
from pathlib import Path
import fitz,json
w=Path(__file__).resolve().parents[1];d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
dest=w/'outputs/qa21/page_173.png';assert not dest.exists()
d[172].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(dest)
p=w/'outputs/visual_qa21_pending.json';r=json.loads(p.read_text());r['pages_rendered']=sorted(set(r['pages_rendered'])|{173});r['overflow_page_added']=173;p.write_text(json.dumps(r,indent=2)+'\n')
print('Rendered final page173 for direct inspection of the allowed0.41342pt box.')
