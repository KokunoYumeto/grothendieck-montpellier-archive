from pathlib import Path
import csv
import hashlib
import json

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
note = root / 'notes/category_bourbaki_congress_date_audit.md'
if note.exists():
    raise SystemExit('Audit already exists; do not duplicate events.')
records = {
    '802': ('c3966f934393b5d3eec3ee6afdd5b919111b462d210ff711db5350cf2e77de2c', 205112518),
    '805': ('cbae58a01e48190a70f5fac1f5ae6b133512cfa1cb886494429be4a83bf94318', 60289920),
}
for number, (digest, size) in records.items():
    p = root / f'sources/category_bourbaki_congress_{number}_pdf0_1.pdf'
    actual = hashlib.file_digest(p.open('rb'), 'sha256').hexdigest()
    assert p.stat().st_size == size and actual == digest
    print(json.dumps({'record': number, 'bytes': size, 'sha256': actual, 'verified': True}))
note.write_text('''# Bourbaki congress minutes 802 and 805: bounded manuscript-date audit

Inspection completed 2026-11-20 at about 04:08 UTC by crystalline_categories.
The question is whether an original dated record identifies the Montpellier cote 1 Hilbert trace/genus-zero sheets or a dated enclosure of those sheets. A date for rédaction 230 alone does not answer that question.

## Actual link chain and access scope

The opened archived R230 catalogue, `sources/category_bourbaki_r230_item664_0.html`, line 321, explicitly advertises congress records 802, 803, 804 and 805. This audit owns 802 and 805; geometry_analysis owns 803 and 804. Requests used only independently public archived pages and their advertised archived PDF payloads. The retained fetch code checks that every request and redirect remains on `web.archive.org`. No further request was made to the challenged live AHP portal.

### Record 802: La Tribu 38

Opened catalogue URL:
http://web.archive.org/web/20240226171921/http://archives-bourbaki.ahp-numerique.fr/items/show/802

Local catalogue: `sources/category_bourbaki_congress_802_0.html`, 34,107 bytes, SHA256 `82aaf4c622f25fc6a870abe490319d6ec3f49e63420010703d8178976cf03df9`.

Opened original PDF URL:
http://web.archive.org/web/20240411124957if_/http://archives-bourbaki.ahp-numerique.fr/files/original/1e592cdae6a5954a107f7f19240b860e.pdf

Local PDF: `sources/category_bourbaki_congress_802_pdf0_1.pdf`, 36 physical pages, 205,112,518 bytes, SHA256 `c3966f934393b5d3eec3ee6afdd5b919111b462d210ff711db5350cf2e77de2c`.

Catalogue identifier `t038_ahp_pct_003`, Fonds Pierre Cartier. The catalogue describes one six-page main fascicle and six independent mathematical fascicles totalling 29 pages, with a modern cover giving 36 PDF pages. It explicitly says the detailed fascicles concern the listed subjects except spectral theory. Those remaining 29 pages were not visually inspected in this audit.

### Record 805: La Tribu 41

Opened catalogue URL:
http://web.archive.org/web/20221007022704/http://archives-bourbaki.ahp-numerique.fr/items/show/805

Local catalogue: `sources/category_bourbaki_congress_805_0.html`, 32,426 bytes, SHA256 `7f08b1c31a26781caabbd4ef91c516304e000af0f5be0467106275b73f5e566b`.

Opened original PDF URL:
http://web.archive.org/web/20240418092949if_/https://archives-bourbaki.ahp-numerique.fr/files/original/a3b77dce36dfea03a432144444110e47.pdf

Local PDF: `sources/category_bourbaki_congress_805_pdf0_1.pdf`, 28 physical pages, 60,289,920 bytes, SHA256 `cbae58a01e48190a70f5fac1f5ae6b133512cfa1cb886494429be4a83bf94318`.

Catalogue identifier `t041_ahp_pct_006`, Fonds Pierre Cartier. The catalogue describes one six-page main fascicle followed by 21 pages of other fascicles, with the modern cover giving 28 PDF pages. Its subject description excludes a detailed spectral-theory fascicle. Those remaining 21 pages were not visually inspected in this audit.

The PDFs' 2021 creation metadata concern digitization, not the dates of the original records. Their dated original title text, described below, is separate evidence.

## Direct page-image inspection

Each main fascicle was read from the rendered original page images, not inferred from OCR. For each record, physical page 1 is the modern catalogue cover, and physical pages 2-7 are original typed pages 1-6. Images are retained under `sources/category_bourbaki_congress_802_pages/` and `sources/category_bourbaki_congress_805_pages/`, named `page_001.png` through `page_007.png`.

### La Tribu 38, original congress 11-17 March 1956

| Physical / typed page | Content relevant to the bounded inquiry |
|---|---|
| 1 / modern cover | La Tribu 38, PCT 003, March 1956; this is catalogue apparatus. |
| 2 / 1 | Original heading names the Amboise congress and explicitly dates it 11-17 March 1956. Its contents identify a portion of part Ib of the spectral-theory report as rédaction 230. |
| 3 / 2 | Anecdotes and editorial discussion about extensive topological-vector-space material being introduced as spectral theory. No trace/genus-zero proof or dated enclosure is identified. |
| 4 / 3 | State of algebra, topology and integration chapters. No particular Hilbert-trace manuscript is identified. |
| 5 / 4 | General programme and assignments to Borel, Bruhat, Cartan, Cartier, Chevalley, Dieudonné and Dixmier. No matching enclosure or Montpellier reference. |
| 6 / 5 | Grothendieck's listed work concerns semisimple material, Cartan-Oka and bundles; Schwartz's concerns differential equations and analytic functions. No trace-draft assignment. |
| 7 / 6 | Future programme includes the spectral-theory report. No specific Hilbert trace/genus-zero leaves or enclosure are identified. |

This is direct dated original evidence that R230 was among the congress's discussed documents. It does not date the Montpellier sheets.

### La Tribu 41, original congress 17-24 March 1957

| Physical / typed page | Content relevant to the bounded inquiry |
|---|---|
| 1 / modern cover | La Tribu 41, PCT 006, March 1957; catalogue apparatus. |
| 2 / 1 | Original heading explicitly dates the Amboise congress 17-24 March 1957. The contents again name the spectral-theory report, no. 230. Spectral-sequence anecdotes concern a different subject. |
| 3 / 2 | Editorial corrections and the beginning of a general book plan. No trace-draft identification. |
| 4 / 3 | Plans for categories, homological algebra, topological categories and varieties. Nuclear spaces and the kernel theorem occur in that programme, without identifying the Montpellier trace sheets. |
| 5 / 4 | Discussion of reorganizing the vector-space/algebra volumes; waiting to discuss Grothendieck's rédaction occurs in the varieties/category programme. The context does not identify it as a trace manuscript. |
| 6 / 5 | Detailed assignments. Grothendieck's is the varieties text; Godement has a rapid kernel-theorem proof; Schwartz has elliptic equations. No trace/genus-zero draft or enclosure. |
| 7 / 6 | Programme for the next congress at Die, 23 June-7 July: integration, commutative algebra, bundles, varieties, harmonic analysis and other reports. No matching trace manuscript. |

## Result and exact remaining bound

The original dated minutes corroborate circulation/discussion of R230 in March 1956 and again March 1957. Neither fully read main fascicle identifies the Montpellier cote 1 trace/genus-zero sheets, their distinctive three-sector proof, or a dated letter/enclosure containing them. This is a bounded negative finding for the main minutes, not a claim that every appendix or all Bourbaki correspondence has been read. The catalogue's explicit exclusion of a detailed spectral-theory fascicle explains why the main minutes were the targeted scope.

The remaining manuscript-date gate is still an explicit dated source tied to those particular leaves, or a securely established original date on the leaves themselves. R230's date and subject do not transfer to them.

## Reproducibility and retained outputs

- `code/category_bourbaki_congress_fetch.py` and `logs/category_bourbaki_congress_fetch.txt`: actual advertised link chain, archived wrappers, payload retrieval, hashes, PDF metadata and native-text attempt.
- `code/category_bourbaki_congress_render.py` and `logs/category_bourbaki_congress_802_render.txt`, `logs/category_bourbaki_congress_805_render.txt`: first seven pages rendered; OCR retained only as a finding aid.
- `notes/category_bourbaki_congress_802_main_full.txt`, `notes/category_bourbaki_congress_805_main_full.txt`, and per-page text/JSON records under corresponding notes directories.
- `code/category_bourbaki_congress_metadata.py` and `logs/category_bourbaki_congress_metadata.txt`: this authored audit and repeat hash checks.

No new mathematical assertion or independent re-proof is claimed by these source-reading events.
''', encoding='utf-8')
events = root / 'notes/category_CHECK_EVENTS.tsv'
with events.open('a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    for number, date in [('802', '11-17 March 1956'), ('805', '17-24 March 1957')]:
        w.writerow(['geo-H-history', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', f'Opened advertised archived congress record {number} and original PDF; visually read modern cover plus all six original main-minute pages. Original heading dates congress {date} and contents explicitly list R230. No Montpellier cote 1 trace/genus-zero draft or dated enclosure identified in those pages. Remaining mathematical appendices not read. notes/category_bourbaki_congress_date_audit.md'])
for name in ['category_progress.md', 'category_source_search_log.md']:
    with (root / 'notes' / name).open('a', encoding='utf-8') as f:
        f.write('\n\n## 2026-11-20 04:08 UTC: original congress 802/805 main minutes completed\n\nOpened the actual catalogue links advertised by R230, retrieved both original PDFs, and visually read each cover plus complete six-page main fascicle. Original dates establish R230 congress context in March 1956 and March 1957. No identification of Montpellier cote 1 trace/genus-zero leaves or dated enclosure; actual sheet-date gate unchanged. The other mathematical appendices were not read. Exact URLs, hashes, page findings and limits: `notes/category_bourbaki_congress_date_audit.md`. Source caches remain under sources/.\n')
print(json.dumps({'note': str(note), 'events_added': 2, 'main_pages_read': {'802': 6, '805': 6}}))
