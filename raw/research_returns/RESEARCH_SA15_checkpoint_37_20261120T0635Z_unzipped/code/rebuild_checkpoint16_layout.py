"""Retain both visible overflow examples and repair their exact source layouts."""
from pathlib import Path
import shutil,subprocess,sys,json,datetime
import fitz
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/checkpoint16_overflow_evidence';assert not dest.exists()
dest.mkdir()
doc=fitz.open(w/'RESEARCH_SA15_paper.pdf')
for page in [180,319]:
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(dest/f'page_{page}.png')
doc.close()
for rel in ['agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex',
            'agents/reduction_descent/B_p2_height_two_mixed_gate.tex',
            'RESEARCH_SA15_paper.log','outputs/build_summary.json']:
    shutil.copy2(w/rel,dest/Path(rel).name)
p=w/'agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex'
t=p.read_text()
old='\\begin{pmatrix}t&u\\\\v&t\\end{pmatrix},\n\\quad\n\\begin{split}'
new='\\begin{pmatrix}t&u\\\\v&t\\end{pmatrix},\n\\]\nwhere\n\\[\n\\begin{split}'
assert t.count(old)==1
p.write_text(t.replace(old,new))
p=w/'agents/reduction_descent/B_p2_height_two_mixed_gate.tex'
t=p.read_text();old='The parent reran the complete exact certificate in'
assert t.count(old)==1
p.write_text(t.replace(old,'The root rerun took'))
for name in ['consolidate.py','number_statements.py','merge_registers.py','build_paper.py','merge_registers.py','update_current16.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['build_summary.json','build_console.txt']:
    target=w/'outputs'/('checkpoint16_final_'+name)
    assert not target.exists()
    shutil.copy2(w/'outputs'/name,target)
print(json.dumps({'status':'REBUILT','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
