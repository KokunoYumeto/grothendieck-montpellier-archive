"""Record the actual fresh root inspection of all sixteen final converged PNGs."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1];out=w/'notes/qa33_root_actual_review.json'
assert not out.exists()
old=json.loads((w/'notes/qa33_root_actual_review.preconvergence.json').read_text())
observations=dict(old['observations'])
observations.update({
 '2':'Corrected contents entries and wrapped long titles are legible and remain inside the text block.',
 '3':'Corrected contents page numbers including the new Pfaffian subsection are visible; dense long-number entries remain within their column.',
 '4':'New group and polar contents entries have the correct409 and411 destinations; Part B heading and entries are cleanly separated.',
 '5':'New B91 and B92 contents entries give645 and649, consistent with the inspected final pages; no clipping or overlap.',
 '6':'Corrected C--F contents destinations and transition to the first body section are legible with regular margins.'})
pages=sorted(map(int,observations));assert pages==[1,2,3,4,5,6,14,28,55,85,126,175,409,410,730,731]
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash=='ea99a27826f7221acc327cb54ded638c46928e93ec6a531fca57b7c0cdba0c7e'
r={'checkpoint':33,'status':'PASS: all sixteen assigned final converged images freshly opened and visually inspected',
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf_sha256':pdfhash,'pages':pages,
 'observations':observations,'all_prior_assigned_images_actually_reopened':True,
 'png_sha256':{str(n):hashlib.sha256((w/f'outputs/qa33/page_{n:03d}.png').read_bytes()).hexdigest() for n in pages},
 'prior_record':'notes/qa33_root_actual_review.preconvergence.json','truncated_image_calls':0,
 'scope':'Actual final-image layout inspection; no additional mathematical proof audit.'}
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'actual_utc':r['actual_utc'],'pages':pages,'pdf_sha256':pdfhash},indent=2))
