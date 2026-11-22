"""Record the actual root visual inspection of nine final CP32 page PNGs."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
out=w/'notes/qa32_root_actual_review.json';assert not out.exists()
observations={
 1:'Title, exact AI credit, incomplete abstract and contents rows are legible and fit; no clipping or overlap.',
 14:'The root-cover lemma, statement statuses, displays and long code path fit with a clean proof continuation.',
 28:'Cohomology sums, maps, precise citations and the end-of-proof mark are legible and contained.',
 55:'Dense contact-quartic prose, bold subheadings and dimension displays fit with regular spacing and no collision.',
 85:'The A.5 scope paragraph, exact-algorithm heading, proposition and equation43 are clear; displayed maps fit.',
 126:'The boxed rank formula, tagged display, matrix, normalization sequence and proof text fit without overlap.',
 175:'The actual residual0.41342pt overflow location was opened: integral inverse formula and adjacent text remain visibly contained, with no clipping or collision.',
 713:'Bibliographic entries and long publisher URL wrap within the text block; all visible lines and page footer fit.',
 714:'The final reference continuation is clear with regular margins and an intact final page number.'}
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash=='406ade402449604644a2b030e0cc8a05508a0eb52ec119cddc8108009a6c562a'
r={'checkpoint':32,'status':'PASS: all nine assigned images actually opened and visually inspected',
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256':pdfhash,'pages':sorted(observations),
 'observations':{str(p):v for p,v in observations.items()},
 'png_sha256':{str(p):hashlib.sha256((w/f'outputs/qa32/page_{p:03d}.png').read_bytes()).hexdigest() for p in observations},
 'scope':'Actual visual layout QA only; no mathematical proof verification is claimed by this record.',
 'truncated_image_calls':0}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':r['status'],'actual_utc':r['actual_utc'],'pages':r['pages'],'pdf_sha256':pdfhash},indent=2))
