"""Record the nine final CP26 PNGs actually opened and visually inspected by root."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
out=w/'notes/qa26_root_actual_review.json';assert not out.exists()
pages=[1,14,28,55,85,126,174,596,597]
sha=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert sha=='127c360164fa0a9bcf729f11b79b1fb41329c26020a0c4fde33f79c453dd46d6'
data={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
      'pdf_sha256':sha,'pages':pages,
      'inspection':'Each listed final page PNG was actually opened with the image viewer and visually inspected. The title/credit and contents, an earlier spread of mathematical proofs and displays, the exact residual-overflow paragraph on174, and the last two bibliography pages are legible with no clipping, overlap, missing glyph or citation-tag defect.',
      'log_check':'The actual final LuaLaTeX log was read: no box above2pt, sole0.41342pt paragraph on174; no undefined reference/citation or missing character.',
      'scope':'Actual rendered-image layout verification only, not a new mathematical proof check.',
      'image_sha256':{str(p):hashlib.sha256((w/f'outputs/qa26/page_{p:03d}.png').read_bytes()).hexdigest() for p in pages}}
out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
