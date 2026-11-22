"""Render every newly integrated CP24 subsection for actual image inspection."""
from pathlib import Path
import json,re,hashlib,datetime
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
attempts=sorted((w/'outputs').glob('checkpoint24_integration_attempt*.json'))
integration=json.loads(attempts[-1].read_text());assert integration['build_exit_code']==0
titles=[]
for rel in integration['promoted_files']:
 titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
def key(s):return s.split('\\(')[0].strip()
pages={1,14,28,55,85,126,173,len(d)-1,len(d)};matched=[]
for j,(level,title,start) in enumerate(toc):
 if any(title.startswith(key(t)) for t in titles):
  end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
  pages.update(range(start,min(end+1,len(d)+1)))
  matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==len(titles),{'titles':titles,'matched':matched}
folder=w/'outputs/qa24';assert not folder.exists();folder.mkdir()
for n in sorted(pages):d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'rendered_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pages_in_pdf':len(d),'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
 'pages_rendered':sorted(pages),'new_subsections':matched,'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa24_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
