"""Record the eight final PNGs actually opened by root; no mathematical test."""
from pathlib import Path
import json,datetime,hashlib
w=Path(__file__).resolve().parents[1]
pages=[1,14,24,28,39,55,70,173]
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'pages':pages,'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
        'observation':'All eight final PNG images were actually opened and inspected. Title/contents, early counterexamples and displays, initial monodromy material and the final residual-overflow page173 are legible, with no clipping, overlap or broken mathematical glyphs. The 0.41342pt line on173 remains within the stated2pt limit and was actually viewed.',
        'type':'Actual visual layout inspection, not mathematical verification.'}
p=w/'notes/qa22_root_actual_review.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
