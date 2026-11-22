from pathlib import Path
import hashlib
import json
import re

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source = root / 'sources/mast_cnpq_inventory2025.pdf'
folder = root / 'notes/category_mast_inventory_ocr'
pages = [folder / f'page_{i:03d}.txt' for i in range(1, 190)]
metadata = [json.loads((folder / f'page_{i:03d}.json').read_text()) for i in range(1, 190)]
queries = ['groth', 'fredholm', 'nachbin', 'hilbert', r'6\.3\.003', r'CNPq.T.4.1.010', r'CNPq.TC.005']
findings = {}
for pattern in queries:
    matches = []
    for page, path in enumerate(pages, 1):
        for line_no, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(pattern, line, re.I):
                matches.append({'physical_pdf_page': page, 'ocr_line': line_no, 'text': line})
    findings[pattern] = matches
report = {
    'source': str(source),
    'source_bytes': source.stat().st_size,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'physical_pages_expected': 189,
    'ocr_text_pages_present': sum(p.is_file() for p in pages),
    'render_failures': [x['page'] for x in metadata if x['render_status']],
    'ocr_failures': [x['page'] for x in metadata if x['ocr_status']],
    'ocr_warning_pages': [x['page'] for x in metadata if x['ocr_stderr']],
    'queries': findings,
    'scope': 'All OCR searched as a finding aid only. Relevant inventory entries and index pages separately inspected as rendered images. Original archival documents not opened.',
}
print(json.dumps(report, ensure_ascii=False, indent=2))
(root / 'notes/category_mast_inventory_audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
