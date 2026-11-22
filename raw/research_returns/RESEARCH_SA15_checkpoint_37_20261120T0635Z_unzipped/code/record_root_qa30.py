"""Record the actual nine individual final CP30 root page inspections."""
from pathlib import Path
import datetime, hashlib, json
w=Path(__file__).resolve().parents[1]
p=w/'notes/qa30_root_actual_review.json'
assert not p.exists()
pages=[1,14,28,55,85,126,174,671,672]
record={
 'status':'PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'pages':pages,
 'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
 'actual_method':'All nine individual PNGs were opened one at a time with view_image and visually inspected. The earlier truncated page 055 call was not credited; page 055 was reopened and actually inspected after resumption.',
 'observations':{
  '1':'Title, credit, incomplete abstract and first contents page fit; links and page numbers are visible.',
  '14':'Cyclic-cover formulas and lemma opening are legible; bottom display and page break fit.',
  '28':'Integral cohomology theorem and proof, arrows and citations fit the text block.',
  '55':'Dense contact-curve proof, subheadings and final inequalities fit without overlap or clipping.',
  '85':'Section heading, conditional algorithm scope, rank formula and semilinear arrows are clear and within the margins.',
  '126':'Normalization sequence, Cartier rank formulas, citations and the next corollary fit without overlap.',
  '174':'The actual 0.41342pt overfull paragraph is fully legible and unclipped; surrounding text and displays fit.',
  '671':'Bibliography source-scope annotations and wrapped URLs are legible; the page ends cleanly.',
  '672':'Final bibliography entries and continuation from the preceding page fit with no missing glyphs or overlapping lines.'},
 'scope':'Layout QA only; this record asserts no additional mathematical audit or mathematical rerun.'}
assert record['pdf_sha256']=='dcf4fdae25ae05e1b6c55ff69f60b0a54f0a3dafbc402d2e33e0a37717b977bd'
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
