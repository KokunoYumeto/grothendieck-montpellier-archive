from pathlib import Path
import json
import re
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
folder = root / 'notes/category_nachbin_inventory_ocr'
records = [json.loads((folder / f'page_{i:03d}.json').read_text()) for i in range(1,59)]
searches = {}
for query in ['groth','fredholm','hilbert']:
    searches[query] = []
    for i in range(1,59):
        for line_no,line in enumerate((folder / f'page_{i:03d}.txt').read_text().splitlines(),1):
            if re.search(query,line,re.I):
                searches[query].append({'physical_pdf_page':i,'ocr_line':line_no,'text':line})
report = {'physical_pages':58,'ocr_pages':len(records),'render_failures':[x['page'] for x in records if x['render_status']],'ocr_failures':[x['page'] for x in records if x['ocr_status']],'ocr_warning_pages':[x['page'] for x in records if x['ocr_stderr']],'queries':searches,'scope':'OCR findings only; visually checked exact relevant catalogue pages separately; originals not opened.'}
(root / 'notes/category_nachbin_inventory_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
additions = {
    'notes/category_CHECK_EVENTS.tsv': "geo-H-history\t2026-11-20\tGPT-6 Astra, inherited effort, crystalline_categories\tbounded primary Nachbin inventory dating-source check\tOCRed all58physical pages of MAST1997 inventory; directly viewed complete textual-record cataloguepp33–37, indexpp57–58, Hilbert targetp46 and technical scopep27. Correspondence groups dated1960onward; Hilbert hit is1961 representation paper. No Grothendieck/Fredholm entry or dated cote1 enclosure identified; originals unopened. notes/category_nachbin_date_audit.md\n",
    'notes/category_source_search_log.md': "\n- Public Nachbin inventory route: official1997 PDF downloaded by root and locally opened; separate web-reader timeout recorded honestly. All58physical pages OCRed; textual-inventorypp33–37 and relevant index/target pages visually checked. No Grothendieck/Fredholm hit; Hilbert entry LN.I.048 is a1961 representation paper. Listed correspondence starts1960. Exact queries, retained output and source limits are in notes/category_nachbin_date_audit.md and notes/category_nachbin_web_records.json. No original archival documents opened and no Zenith query attempted.\n",
    'notes/category_progress.md': "\n## Public Nachbin inventory audit completed\n\nAll58physical pages of the1997 official inventory were OCRed; complete textual-record cataloguepp33–37 and relevant index pages were directly viewed. No Grothendieck correspondence or trace-draft enclosure is identified. Dated correspondence groups begin1960; the Hilbert-index hit is a1961 unitary-representation paper. Original records remain unopened, so this is a bounded catalogue finding rather than an assertion of archival absence. Audit: notes/category_nachbin_date_audit.md. No section or bibliography change; actual manuscript sheet date remains unproved.\n",
}
for relative, addition in additions.items():
    path = root / relative
    old = path.read_text()
    if 'notes/category_nachbin_date_audit.md' in old:
        print('ALREADY PRESENT', relative)
    else:
        path.write_text(old+addition)
        print('APPENDED',relative)
