"""Record actual root image inspections performed in the conversation."""
from pathlib import Path
import datetime, hashlib, json
w=Path(__file__).resolve().parents[1]
p=w/'notes/qa29_root_actual_review.json'
assert not p.exists()
pages=[1,14,28,55,85,126,174,659,660]
record={
 'status':'PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'pages':pages,
 'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
 'actual_method':'All nine individual PNGs were opened one at a time with view_image and visually inspected. An earlier batched call was truncated and is not credited as image inspection.',
 'observations':{
  '1':'Title, authorship, incomplete abstract and first contents page fit; links and page numbers are visible.',
  '14':'Cyclic-cover formulas and the lemma opening are legible; the bottom display and page break fit without clipping.',
  '28':'Integral cohomology theorem and proof, arrows and citations fit the text block.',
  '55':'Dense contact-curve proof and final inequalities fit; no overlap or clipped text.',
  '85':'Section heading, algorithm scope warning, rank formula and semilinear arrows are legible.',
  '126':'Normalization sequence, rank formulas and next corollary fit without overlap.',
  '174':'The actual 0.41342pt overfull paragraph is fully legible and unclipped; displays and surrounding text fit.',
  '659':'Bibliography entries, source-scope annotations and wrapped URLs are legible without clipping.',
  '660':'Final bibliography entries and continuation from preceding page fit; no lost glyph or overlapping line.'},
 'scope':'Layout QA only. No additional mathematical proof audit or rerun is asserted by this record.'}
assert record['pdf_sha256']=='2eb1a849c9dad5158bd079f059464d3733b5322522d859f781d0ab80321cfcf9'
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
