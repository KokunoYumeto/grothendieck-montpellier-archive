"""Record only the ten final page images actually viewed by the root reviewer."""
from pathlib import Path
import datetime, hashlib, json
w = Path(__file__).resolve().parents[1]
expected = '7991e6ad5930965303d582621c16222edced953dee5f2d64193df27820815417'
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest() == expected
pages = [1,14,28,55,85,126,173,174,579,580]
record = {
    'status': 'PASS', 'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewer': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
    'pdf_sha256': expected, 'pages': pages,
    'observations': [
        'Individually opened every listed final PNG and visually inspected it, rather than relying on extracted text.',
        'Title, incomplete-work abstract, credits, first contents page and page numbering are clear.',
        'Earlier mathematical text, aligned displays, citations, theorem headings and status annotations fit cleanly.',
        'The exact residual 0.41342pt overflow was located by its printed phrase on final page174, separately rendered and actually viewed. It has no visible clipping or overlap. Page173 was also viewed.',
        'Both final bibliography pages have clear hanging entries, wrapped URLs, source-access notes and complete final entries.',
        'No missing glyph, clipping, overlapping equation/tag or other visible layout defect was observed.'
    ],
    'image_sha256': {str(n): hashlib.sha256((w/f'outputs/qa25/page_{n:03d}.png').read_bytes()).hexdigest() for n in pages},
    'scope': 'Actual final-image layout inspection only; not a new mathematical proof check.'
}
dest=w/'notes/qa25_root_actual_review.json'
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='image_sha256'},indent=2))
