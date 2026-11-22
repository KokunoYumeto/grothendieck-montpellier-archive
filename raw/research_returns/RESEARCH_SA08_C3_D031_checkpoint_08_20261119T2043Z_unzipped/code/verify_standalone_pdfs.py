#!/usr/bin/env python3
"""Rebuild and render every retained standalone QA PDF with final source."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, os, re, subprocess, time
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
out = root.parent/'qa_standalone_committed'
out.mkdir(exist_ok=True)
env = os.environ.copy()
texroot = root.parent/'texdeps/unpacked/usr/share/texlive/texmf-dist'
if texroot.exists():
    env['LUAINPUTS'] = str(texroot)+'//:'
    env['TEXINPUTS'] = str(texroot/'tex')+'//:'
start = time.monotonic()
wrappers = sorted(root.glob('*_QA.tex'))

def verify(wrapper):
    t = time.monotonic()
    stem = wrapper.stem
    stdout = root/'logs'/f'{stem}_rebuild_stdout.log'
    commands = [['lualatex','--interaction=nonstopmode','--halt-on-error',
                 '--output-directory=logs',wrapper.name]]
    if '\\bibliography{' in wrapper.read_text():
        commands.append(['bibtex', 'logs/'+stem])
    commands.extend([commands[0], commands[0]])
    with stdout.open('w') as f:
        for cmd in commands:
            subprocess.run(cmd,cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
    log = (root/'logs'/f'{stem}.log').read_text()
    pdf = root/'logs'/f'{stem}.pdf'
    sub = out/stem
    sub.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-png','-scale-to','900',str(pdf),str(sub/'page')],
                   stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,check=True)
    pages = sorted(sub.glob('page-*.png'))
    return {'file':str(pdf.relative_to(root)), 'pages':len(pages),
            'overfull_widths_pt':[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt',log)],
            'undefined':len(re.findall('undefined',log)),
            'latex_warnings':len(re.findall('LaTeX Warning',log)),
            'seconds':time.monotonic()-t,
            'images':[str(x) for x in pages]}

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(verify,wrappers))
samples=[]
for item in results:
    for index in sorted({0,len(item['images'])-1}):
        samples.append((Path(item['file']).stem,index+1,Path(item['images'][index])))
cols,w,h=4,360,530
sheet=Image.new('RGB',(cols*w,((len(samples)+cols-1)//cols)*h),'#d7d7d7')
draw=ImageDraw.Draw(sheet)
for i,(stem,n,path) in enumerate(samples):
    im=Image.open(path).convert('RGB');im.thumbnail((w-12,h-45))
    x=(i%cols)*w+(w-im.width)//2;y=(i//cols)*h+38
    sheet.paste(im,(x,y))
    draw.text(((i%cols)*w+8,(i//cols)*h+5),stem.replace('A_integral_','').replace('_QA',''),fill='black')
    draw.text(((i%cols)*w+8,(i//cols)*h+20),f'Page {n}',fill='black')
sheet.save(out/'contact.png')
data={'pdf_count':len(results),'pages':sum(x['pages'] for x in results),
      'runtime_seconds':time.monotonic()-start,'results':results,
      'visual_inspection':'Pending explicit image review.'}
(root/'logs/standalone_pdf_verification.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='results'}))
for r in results:
    print(json.dumps({k:v for k,v in r.items() if k!='images'}))
