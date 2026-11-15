"""Prepare private diplomatic proofs from reviewed page sources."""
import importlib.util,json,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ps_builder',P/'scripts/build_readers.py')
b=importlib.util.module_from_spec(spec);sys.modules['ps_builder']=b;spec.loader.exec_module(b)
out=P/'qa/isolated_134_5_6';out.mkdir(exist_ok=True)
for page in sys.argv[1:]:
 key=f'ps_134-6_{int(page):03d}'
 raw=(P/'checked_pages'/f'{key}.tex').read_text();fixes=[]
 body=b.local_layout_repairs(b.preserve_front_lineation(b.repair_macro_layout(b.repair_diagram_separators(b.normalize(raw,key,fixes),key,fixes),key,fixes),key,fixes),key,fixes)
 top='\\def\\EditionMode{0}\n\\def\\EditionLabel{Diplomatic page proof}\n\\def\\EditionStatus{Local layout verification}\n'
 link=f'\\pssource{{{key}}}{{134-6/{int(page)}}}{{https://grothendieck.umontpellier.fr/web/viewer.html?file=../134-6.pdf\\#page={int(page)+1}}}\n'
 tex=top+(P/'scripts/reader_preamble.tex').read_text()+'\n\\begin{document}\n'+link+body+'\n\\end{document}\n'
 (out/f'page{int(page)}_diplomatic.tex').write_text(tex)
print('Prepared private proofs:',', '.join(sys.argv[1:]))
