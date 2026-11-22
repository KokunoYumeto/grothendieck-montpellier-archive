"""Record only final page images actually opened and inspected by root."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
dest=w/'notes/qa24_root_actual_review.json';assert not dest.exists()
pages=[1,14,28,55,85,126,173,558,559]
pdf=w/'RESEARCH_SA15_paper.pdf'
sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert sha=='e7bcec75173711319c9c12a0b3be355c9782fc8329207cfa9c6f1253ad6aa649'
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'pdf_sha256':sha,'pages':pages,
 'actual_observations':'Each of the nine final PNGs was individually emitted and visually inspected in three calls. The title, explicit incomplete abstract and contents are legible. Earlier proof pages and equation numbers fit the page. The persistent0.41342pt paragraph onp173 has no clipping. Both bibliography pages have readable entries and URLs without overlap or missing glyphs. No layout defect was observed.',
 'image_sha256':{str(n):hashlib.sha256((w/f'outputs/qa24/page_{n:03d}.png').read_bytes()).hexdigest() for n in pages}}
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
