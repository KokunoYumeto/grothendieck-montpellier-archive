"""Record the fourteen final CP34 images actually opened and visually inspected by root."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
out=w/'notes/qa34_root_actual_review.json';assert not out.exists()
observations={
 1:'Title, exact AI credit, explicit incomplete abstract, source limitation and initial contents entries are fully visible and legible.',
 2:'Contents continuation and wrapped two-line entry are readable; the widened subsection-number column clearly separates labels and titles.',
 3:'Dense contents including three-digit subsection labels have visible spacing, aligned page numbers and no clipping.',
 4:'New A.4 subsection titles and final destinations415,417,419 are consistent with the rendered additions; headings and wrapped Part B contents fit.',
 5:'Dense Part B contents entries, equation text and final page-number column are aligned and legible.',
 6:'B93 entry points to660; C-F contents and transition to the first body section at page6 have normal spacing and no overlap.',
 14:'Proof continuation, printed code path, status paragraphs, displayed maps and the new-section heading fit the text block.',
 28:'Dense complete-intersection proof, direct sums, finite-field construction and precise citations remain legible and contained.',
 55:'Contact-quartic argument, short subheadings and dimension displays have clear spacing without collisions.',
 85:'A.5 scope paragraph and the exact-algorithm qualification are explicit; displayed maps and equation tags fit with clear margins.',
 126:'Boxed all-degree rank formula, dagger tag, matrix and normalization exact sequence are intact and legible.',
 175:'The actual residual0.41342pt overflow paragraph with the integral inverse formula was inspected; no clipping or visible margin collision occurs.',
 742:'Bibliography entries, precise source-opening scope and the long DOI/URL text wrap within the page margins.',
 743:'Final bibliography continuation and footer are fully visible with normal spacing and margins.'}
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash=='7bb59e472c44e11f66ac8fc102e9e3b4afddb717529388335d0de3f2750ad5a5'
r={'checkpoint':34,'status':'PASS: all fourteen assigned final images actually opened and visually inspected',
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256':pdfhash,'pages':sorted(observations),'observations':{str(p):v for p,v in observations.items()},
 'png_sha256':{str(p):hashlib.sha256((w/f'outputs/qa34/page_{p:03d}.png').read_bytes()).hexdigest() for p in observations},
 'scope':'Actual layout QA only; no new mathematical proof audit. Every contents page, spread sample, residual overflow and final bibliography pages were freshly viewed.',
 'truncated_image_calls':0}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':r['status'],'actual_utc':r['actual_utc'],'pages':r['pages'],'pdf_sha256':pdfhash},indent=2))
