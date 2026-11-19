"""Read a downloaded public PDF locally; extracted source text stays outside deliverables."""
from pathlib import Path
import fitz,sys
p=Path(sys.argv[1]);doc=fitz.open(p)
text='\n'.join(page.get_text() for page in doc)
p.with_suffix('.txt').write_text(text)
print('PDF',p.name,'pages',len(doc),'text characters',len(text))
for num in map(int,sys.argv[2:]):
    dest=p.with_name(p.stem+f'_page{num}.png')
    doc[num].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(dest)
    print('Rendered',num,'to',dest)
