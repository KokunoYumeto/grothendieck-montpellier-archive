"""Retain the actual two initial overflow pages and their source before repair."""
from pathlib import Path
import fitz,json,shutil,datetime
w=Path(__file__).resolve().parents[1]
o=w/'outputs/checkpoint18_overflow_evidence';o.mkdir(exist_ok=False)
d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
for p in [243,245]:d[p-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(o/f'page_{p:03d}.png')
for rel in ['RESEARCH_SA15_paper.log','outputs/build_summary.json','agents/monodromy/mixed_degree_two_uniform_full_groups.tex']:
    shutil.copy2(w/rel,o/rel.replace('/','__'))
(o/'record.json').write_text(json.dumps({'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':[243,245],'scope':'Original pages with 40.82396pt status-line overflow and 7.21278pt exact-sequence overflow.'},indent=2)+'\n')
