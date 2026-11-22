"""Record actual root inspection of all eleven assigned final CP33 PNGs."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
out=w/'notes/qa33_root_actual_review.json';assert not out.exists()
observations={
 1:'Title, exact AI credit, incomplete abstract and contents rows are fully visible and legible; no clipping or overlap.',
 14:'Proof continuation, exact code path, status text, root-cover display and section heading fit the text block.',
 28:'Dense construction proof, direct sums, maps and precise citations are legible and contained.',
 55:'Contact-quartic prose, subheadings and dimension displays have clear spacing and no collision.',
 85:'The A.5 scope and exact-algorithm qualification are explicit; equation tags, displayed maps and proof text fit.',
 126:'Boxed rank formula, dagger tag, matrix, normalization sequence and proof remain legible without overlap.',
 175:'The actual remaining0.41342pt overflow paragraph was visually inspected; the integral inverse formula and surrounding text remain visibly contained with no clipping.',
 409:'New full-radical lemma and proposition, statuses, block matrices, FR1--FR6 displays and long group equality are clearly typeset and contained.',
 410:'New submodule/orbit corollary, FR7 equivalences, geometric component statement and scope paragraph fit with intact proof marks and no collision.',
 730:'Bibliographic entries, precise opened-source scopes and long publisher URL wrap within the text block; no clipping.',
 731:'Final bibliography continuation and page footer are clear, with normal margins.'}
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash=='029cc723c44c6d3feda3b23bf8803504c8f11309350b4adb57a1b670338d28d2'
r={'checkpoint':33,'status':'PASS: all eleven assigned actual images opened and visually inspected',
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256':pdfhash,'pages':sorted(observations),
 'observations':{str(p):v for p,v in observations.items()},
 'png_sha256':{str(p):hashlib.sha256((w/f'outputs/qa33/page_{p:03d}.png').read_bytes()).hexdigest() for p in observations},
 'scope':'Actual visual layout QA only; not an additional mathematical proof audit.',
 'truncated_image_calls':0}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'status':r['status'],'actual_utc':r['actual_utc'],'pages':r['pages'],'pdf_sha256':pdfhash},indent=2))
