"""Record the nine final CP27 page images actually opened by root."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
out=w/'notes/qa27_root_actual_review.json';assert not out.exists()
pages=[1,14,28,55,85,126,174,622,623]
sha=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert sha=='0f2d8000fdbbfccba5646287b67468df826b441ff3b312ce88e89e8975de38cc'
data={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
      'pdf_sha256':sha,'pages':pages,
      'inspection':'Every listed final PNG was individually opened with the image viewer and visually inspected. The title, explicit incomplete abstract, credit, contents, earlier proof and formula pages, the exact 0.41342pt paragraph on174, and the final two bibliography pages are legible, with no clipping, overlap, missing glyph or citation/tag defect observed.',
      'log_check':'The relevant actual final LuaLaTeX log entries were read: no box above2pt, sole0.41342pt paragraph on174; no undefined reference/citation or missing character. Two earlier bibliography compilation failures and their actual inputs/logs are retained.',
      'scope':'Actual rendered-image layout verification only, not a new mathematical proof check.',
      'image_sha256':{str(p):hashlib.sha256((w/f'outputs/qa27/page_{p:03d}.png').read_bytes()).hexdigest() for p in pages}}
out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
