from pathlib import Path
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
additions = {
    'notes/category_CHECK_EVENTS.tsv': "geo-H-history\t2026-11-20\tGPT-6 Astra, inherited effort, crystalline_categories\tbounded primary inventory dating-source check\tOCRed all189pages of MAST1998 CNPq inventory; visually checked exact IMPA report T.6.3.003 dated16Sep1955,78folios atp42, Nachbin photographic-index entries and record descriptions, broad correspondence holdings and inventory-scope qualifications. Originals unopened; no particular cote1 leaf identification. notes/category_mast_date_audit.md\n",
    'notes/category_source_search_log.md': "\n- Public MAST CNPq inventory route: publication year1998 visually confirmed, despite2025 URL. All189physical pages OCRed and searched; exact entry CNPq.T.6.3.003 atprintedp42 gives IMPA report16Sep1955,78folios. Nachbin positive hit belongs to photographs F0058/F0079; no trace draft identified. Relevant records/indexes visually checked. Original report unopened; Zenith registration limit respected with no query-endpoint probing. Complete bounded queries, opened-status table, source fingerprint and outputs retained in notes/category_mast_date_audit.md and notes/category_mast_web_records.json.\n",
    'notes/category_progress.md': "\n## Public MAST inventory audit completed\n\nAll189pages of the1998 CNPq inventory were OCRed, with relevant records/indexes directly viewed. It identifies an IMPA activity report16September1955,78folios (T.6.3.003,p42), but does not identify its author, topic, enclosures or any cote1 leaf. Nachbin occurs only in the located photographic-index hit, pointing to1952/1955installation photographs. Broad correspondence is not item indexed. Original report not opened; public Zenith registration requirement was not bypassed. Full bounded audit saved as notes/category_mast_date_audit.md. No mathematical or section/bibliography change. Actual sheet date remains unproved.\n",
}
for relative, addition in additions.items():
    path = root / relative
    old = path.read_text()
    marker = 'notes/category_mast_date_audit.md'
    if marker in old:
        print('ALREADY PRESENT', relative)
    else:
        path.write_text(old + addition)
        print('APPENDED', relative)
