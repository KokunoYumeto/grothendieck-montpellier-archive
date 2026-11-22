"""Record actual completed public-inventory inspections, not dates for manuscripts."""
from pathlib import Path
import csv, datetime, hashlib, json, time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
record_path = root / 'logs/root_brazil_inventory_record.json'
if record_path.exists():
    raise SystemExit('Completed inspection already recorded; refusing a duplicate event.')

path = root / 'notes/root_brazil_date_audit.md'
text = path.read_text()
text = text.replace('Working record, 20 November 2026, before checkpoint 04.',
                    'Working record, 20 November 2026; updated after checkpoint 04.')
text = text.replace('It lists the Nachbin inventory (1997) and Gama inventory (1998). The cover images are not the inventory texts.',
                    'It links the Nachbin and Gama inventories. The Gama URL directory says 1998, but the original copyright/cataloguing page gives 1988. The cover images alone were not treated as the inventory texts; the complete public PDFs were subsequently retrieved and inspected.')
text = text.replace('The search index identifies CNPq.T.6.3.003, an IMPA activity report dated 16 September 1955, 78 folios, on printed inventory p.42. The independent visual/OCR audit is in progress; the report itself has not been opened. Empty native PDF extraction is not an absence finding.',
                    'The complete 189-page OCR and relevant original page images were subsequently checked by the category agent. Printed p.42, physical p.75, identifies CNPq.T.6.3.003, an IMPA activity report dated 16 September 1955, 78 folios. The original inventory was published in 1998, despite the 2025 URL directory. The report itself has not been opened; the catalogue does not identify a trace draft or enclosure. Exact coverage and limitations: notes/category_mast_date_audit.md.')
old = '''The discriminating next step is to inspect the public inventory's exact
entry and indexes, then seek an independently public copy or precise
description of a relevant original. We will not infer a date from a course
title, dossier adjacency, general subject period, or the mere existence of
an activity report. This is documentary search, not movement under the
user's formal-review rule.
'''
new = '''## Completed Gama inspection after checkpoint 04

We retrieved the complete public PDF of *Arquivo Lélio Gama: inventário
sumário*, Rio de Janeiro: MAST, **1988**. The directory of the public URL
contains 1998, but physical PDF p.3 explicitly prints copyright 1988 and
catalogues the work as MAST, 1988, 76 pages. The digital file has 74 physical
pages. We directly viewed p.3, p.40, p.62 and p.63 after rendering at width
1600 pixels. The earlier attempted display of p.3 was truncated by the
tool/context boundary and was not counted; the subsequent successful
display is the actual inspection recorded here.

Public URL:
https://www.gov.br/mast/pt-br/imagens/publicacoes/1998/inventarios_lelio_gama.pdf/@@display-file/file

Local source: sources/mast_gama_inventory1998.pdf, 9,259,564 bytes,
SHA256 71933f098a7a56f5bee8a9b6a0bddafaab48aeed7f99677b49abfc54a79bbb65.

All 74 pages were OCRed as a finding aid, using six workers at 150 dpi in
13.4998819760076 seconds. The exact pattern was
Groth|Fredholm|Nachbin|Hilbert|tensor|Summa|IMPA; hit pages were 4, 40, 63
and 70. There was no Groth/Fredholm/Hilbert/tensor hit in that OCR. This is
not an exhaustive absence claim about the archive or about faint text.

Physical p.40, printed p.39, identifies **LG.D 10/138**: 53 documents on
Gama's activities at IMPA and the Brazilian Mathematical Society, with
the broad date range **26 August 1933 to 3 November 1980**, 140 folios,
including a speech and other material. No individual correspondence or
enclosure description is given. Physical pp.62–63, printed pp.63–64,
were visually checked through the relevant alphabetical index range;
the IMPA entry points back to LG.D 10/138. No Grothendieck entry appears
in this inspected G/H range. We have not opened any original document
within that archival group. The inventory does not date the target sheets.

## Completed Nachbin inspection by the category agent

The same public download batch retrieved *Arquivo Leopoldo Nachbin:
inventário sumário*, MAST, **1997** (58 physical PDF pages; catalogued as
62 pages). The agent OCRed the complete digital source and directly read
all textual-inventory pages, the relevant name indexes, and the Hilbert
entry's target. Its exact positive records and limits are in
notes/category_nachbin_date_audit.md. The correspondence groups begin in
1960; the undated five-folio Horváth recollection LN.T.3.013 has no stated
Grothendieck or trace topic. No underlying letter, recollection, or
photograph was opened. These descriptions do not establish an absence
of earlier correspondence from other holdings.

## Remaining discriminating step

The public summary inventories are now inspected within the exact scopes
above and in the two category audits. The original IMPA report or a
separate dated draft/enclosure identification is still required. We will
not infer a date from a course title, dossier adjacency, general subject
period, or the mere existence of an activity report. This documentary
work has not changed an open row or reduced its gate under the user's
formal-review rule.

Additional reproducible programs and outputs are root_brazil_sources03,
fetch_public_sources (batch root_brazil_sources04), ocr_public_pdf
(tag root_mast_gama), render_source_pages (tag root_mast_gama), and this
root_brazil_inventory_record program. Per-page OCR is in
sources/root_mast_gama_ocr; selected images retain their physical page
numbers in sources/root_mast_gama_pNNN.png.
'''
assert old in text
path.write_text(text.replace(old, new))

event = {
    'statement_id': 'geo-H-history', 'date': '2026-11-20',
    'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, run SA23-20261120/root',
    'type': 'used and rechecked in this run',
    'outcome': 'Opened the complete public Gama inventory and directly viewed physical pages 3,40,62,63 after full 74-page OCR. Original publication is 1988, not the 1998 URL directory. LG.D 10/138 is a broad 53-document IMPA/SBM group dated 1933-1980, with no item-level trace/enclosure identification. Original archival documents remain unopened; the manuscript-date gate is unchanged.',
    'where': 'notes/root_brazil_date_audit.md;logs/ocr_public_pdf_root_mast_gama.json;logs/render_source_pages_root_mast_gama.json',
}
with (root / 'notes/root_CHECK_EVENTS.tsv').open('a', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=list(event), delimiter='\t')
    writer.writerow(event)
with (root / 'notes/root_source_log.md').open('a') as handle:
    handle.write('\n\n## Brazilian public inventories: completed bounded inspection\n\n')
    handle.write('We directly read the Gama inventory copyright/cataloguing page and exact IMPA group and index pages (physical 3,40,62,63), after complete 74-page OCR. The source was published in 1988. LG.D 10/138 describes 53 documents across 1933–1980 without an individual trace enclosure. The category agent separately completed the CNPq and Nachbin inventory audits. Neither an original IMPA report nor a dated identification of the particular cote 1 sheets was obtained. Exact positive records, hashes, search scopes and unopened-original qualifications are retained in notes/root_brazil_date_audit.md and the category inventory audits. No source access limit or catalogue search is counted as formal-review movement.\n')

record = {
    'created_utc': now,
    'gama_source_sha256': hashlib.sha256((root / 'sources/mast_gama_inventory1998.pdf').read_bytes()).hexdigest(),
    'actually_viewed_physical_pages': [3,40,62,63],
    'observed_publication_year': 1988,
    'new_events': 1,
    'manuscript_date_established': False,
    'formal_review_movement': False,
    'elapsed_seconds': time.perf_counter() - started,
}
record_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
