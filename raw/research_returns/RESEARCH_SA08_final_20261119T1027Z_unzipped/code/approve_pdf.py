"""Record explicit visual inspection after the rendered images were reviewed.

This command never performs or substitutes for visual inspection. The caller
must supply the exact reviewed page list and an inspection description.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, re

p = argparse.ArgumentParser()
p.add_argument('qa_record')
p.add_argument('--reviewed-pages', type=int, nargs='+', required=True)
p.add_argument('--inspection', required=True)
args = p.parse_args()
root = Path(__file__).resolve().parents[1]
qa_path = Path(args.qa_record)
qa = json.loads(qa_path.read_text())
if sorted(set(args.reviewed_pages)) != qa['rendered_pages']:
    raise SystemExit('The reviewed pages must match the rendered page list.')
pdf = root/'RESEARCH_SA08_paper.pdf'
if hashlib.sha256(pdf.read_bytes()).hexdigest() != qa['pdf_sha256']:
    raise SystemExit('The PDF changed after rendering.')
source_files = [root/'RESEARCH_SA08_paper.tex', root/'RESEARCH_SA08_references.bib']
for match in re.finditer(r'\\(?:input|InputIfFileExists)\{(sections/[^}]+)\}', source_files[0].read_text()):
    file = root/match.group(1)
    if not file.suffix:
        file = file.with_suffix('.tex')
    if file.exists():
        source_files.append(file)
qa['source_sha256'] = {
    str(file.relative_to(root)): hashlib.sha256(file.read_bytes()).hexdigest()
    for file in source_files
}
qa['visual_review'] = 'Passed explicit image inspection: ' + args.inspection
qa['visually_inspected_pages'] = sorted(set(args.reviewed_pages))
qa['reviewer'] = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; run /root'
qa['approval_utc'] = datetime.now(timezone.utc).isoformat()
qa_path.write_text(json.dumps(qa, indent=2) + '\n')
(root/'logs/PDF_QA_APPROVED.json').write_text(json.dumps(qa, indent=2) + '\n')
print(json.dumps({
    'approved_pdf_sha256': qa['pdf_sha256'],
    'pages': qa['pages'],
    'visually_inspected_pages': qa['rendered_page_count'],
    'source_files': len(source_files),
    'approval_utc': qa['approval_utc'],
}, indent=2))
