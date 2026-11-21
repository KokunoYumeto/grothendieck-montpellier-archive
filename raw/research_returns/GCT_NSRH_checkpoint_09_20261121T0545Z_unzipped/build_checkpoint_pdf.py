"""Two-pass paper build and reproducible render inputs for visual review."""
from pathlib import Path
import subprocess, os, hashlib, json
from PIL import Image, ImageDraw
import fitz

import argparse
ap=argparse.ArgumentParser();ap.add_argument("--number",type=int,required=True);args=ap.parse_args()
cp=f"{args.number:02d}"
r=Path(__file__).resolve().parent
env=dict(os.environ); env['TEXMF']='/usr/share/texlive/texmf-dist'
for number in (1,2):
    with (r/f'build_cp{cp}_final_{number}.txt').open('w') as log:
        subprocess.run(['pdflatex','-fmt='+str(r/'tex_check/pdflatex.fmt'),'-interaction=nonstopmode','-halt-on-error','GCT_NSRH.tex'],cwd=r,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
log=(r/f'build_cp{cp}_final_2.txt').read_text()
problems=[line for line in log.splitlines() if any(t in line for t in ['Overfull','undefined','Undefined','LaTeX Error']) or line.startswith('!')]
if problems:
    print('\n'.join(problems)); raise SystemExit('Resolve final build issues before visual review.')
pdf=r/'GCT_NSRH.pdf'; doc=fitz.open(pdf)
out=r/f'qa/cp{cp}';out.mkdir(parents=True,exist_ok=True)
subprocess.run(['pdftoppm','-png','-scale-to-x','280','-scale-to-y','-1',str(pdf),str(out/'page')],check=True)
pages=sorted(out.glob('page-*.png'))
assert len(pages)==len(doc)
contacts=[]
for start in range(0,len(pages),30):
    batch=pages[start:start+30]
    sheet=Image.new('RGB',(5*300,6*425),'#dce1e5'); draw=ImageDraw.Draw(sheet)
    for j,path in enumerate(batch):
        im=Image.open(path).convert('RGB');x=(j%5)*300+10;y=(j//5)*425+22
        sheet.paste(im,(x,y));draw.text((x,y-17),str(start+j+1),fill='black')
    dest=out/f'contact_{start//30+1}.png';sheet.save(dest);contacts.append(str(dest))
terms=['Closing the rank-one case','scalar-complex exclusion in every','Central polynomial coefficients','Universal tensor inversion','positive model for the containing','three-plus-three iteration','whole-output failure already','arithmetic-parameter classification','bounded audit of raw','nonflat case','single-center Lefschetz','actual duality and virtual inversion','central polynomial coefficients in Grothendieck','one-plus-three comparison in Grothendieck','relative quotient','variable-group quotient','finite-Frobenius','unbounded derived correspondence']
detail_pages={1,len(doc)}
for i,page in enumerate(doc):
    normalized=' '.join(page.get_text().split())
    if any(t in normalized for t in terms):detail_pages.add(i+1)
details=[]
for n in sorted(detail_pages):
    prefix=out/f'detail_{n}'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','115','-png',str(pdf),str(prefix)],check=True)
    details.append(str(prefix)+'.png')
meta={'pages':len(doc),'tex_sha256':hashlib.sha256((r/'GCT_NSRH.tex').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_bytes':pdf.stat().st_size,'contact_sheets':contacts,'detail_images':details,'build_problems':problems}
(out/'render_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
