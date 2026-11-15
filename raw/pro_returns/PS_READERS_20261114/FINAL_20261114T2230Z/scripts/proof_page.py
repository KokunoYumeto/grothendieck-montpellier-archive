"""Prepare a one-source-page diplomatic proof with the production preamble."""
from pathlib import Path
import argparse,json
from build_readers import normalize,repair_diagram_separators,repair_macro_layout,preserve_front_lineation,local_layout_repairs
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('key');args=a.parse_args();key=args.key
m=next(m for m in json.loads((P.parent/'inputs/text/records/PAGES_PS.json').read_text()) if m['key']==key)
s=(P/'checked_pages'/(key+'.tex')).read_text();fixes=[]
if not (P/'records/SOURCE_NORMALIZATION.json').exists():
    s=local_layout_repairs(preserve_front_lineation(repair_macro_layout(repair_diagram_separators(normalize(s,key,fixes),key,fixes),key,fixes),key,fixes),key,fixes)
url=f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{m['cote']}.pdf\\#page={m['pdf_page']}"
tex='\\def\\EditionMode{0}\n\\def\\EditionLabel{Isolated diplomatic proof}\n\\def\\EditionStatus{Local layout verification}\n'+(P/'scripts/reader_preamble.tex').read_text()
tex+='\n\\begin{document}\n\\pssource{'+key+'}{'+m['cote']+'/'+str(m['site'])+'}{'+url+'}\n'+s+'\n\\end{document}\n'
out=P/'qa/proofs';out.mkdir(parents=True,exist_ok=True);(out/(key+'.tex')).write_text(tex)
print(json.dumps({'source':str((out/(key+'.tex')).relative_to(P)),'mechanical_operations':len(fixes)}))
