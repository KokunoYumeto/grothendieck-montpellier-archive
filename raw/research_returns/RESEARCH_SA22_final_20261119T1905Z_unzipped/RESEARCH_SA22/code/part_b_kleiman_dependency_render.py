from pathlib import Path
import fitz,time,json
start=time.monotonic();d=fitz.open('sources/kleiman1968.pdf');rows=[]
for page_index,printed in [(0,359),(17,376),(18,377),(19,378)]:
 page=d[page_index];path=Path('qa')/f'part_b_kleiman1968_audit_{printed}.png'
 page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(path)
 rows.append({'pdf_page':page_index+1,'expected_printed_page':printed,'image':str(path),'first_text':page.get_text()[:70]})
out={'kind':'Logged PyMuPDF source-render command; not a standalone historical program','pages':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Original field conventions p359; isogeny/divisor input p376; Theorem2A11 and Lemma2A12 pp377-378'}
Path('code/part_b_kleiman_dependency_render_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
