"""Render CP30 additions and dynamically located overflow text for actual QA."""
from pathlib import Path
import json,re,hashlib,datetime
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
attempts=sorted((w/'outputs').glob('checkpoint30_integration_attempt*.json'))
assert attempts
integration=json.loads(attempts[-1].read_text());assert integration['build_exit_code']==0
titles=[]
for rel in integration['promoted_files']:
    titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
def key(s):return re.sub(r'[-\u2013\u2014]+','-',s.split('\\(')[0].strip())
pages={n for n in [1,14,28,55,85,126,len(d)-1,len(d)] if 1<=n<=len(d)}
matched=[]
for j,(level,title,start) in enumerate(toc):
    if any(key(title).startswith(key(t)) for t in titles):
        end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==len(titles),{'titles':titles,'matched':matched}
# The historical 0.41342pt paragraph moves as sections are added: locate its text.
phrase='asserted integral inverse formula'
overflow_pages=[i+1 for i,p in enumerate(d) if phrase in ' '.join(p.get_text().split())]
assert len(overflow_pages)==1,overflow_pages
pages.update(overflow_pages)
folder=w/'outputs/qa30';assert not folder.exists();folder.mkdir()
pending_path=w/'outputs/visual_qa30_pending.json';assert not pending_path.exists()
for n in sorted(pages):
    d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'rendered_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'pages_in_pdf':len(d),'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
        'pages_rendered':sorted(pages),'new_subsections':matched,
        'overflow_location_phrase':phrase,'exact_remaining_overflow_pages':overflow_pages,
        'manual_visual_review':'PENDING'}
pending_path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
