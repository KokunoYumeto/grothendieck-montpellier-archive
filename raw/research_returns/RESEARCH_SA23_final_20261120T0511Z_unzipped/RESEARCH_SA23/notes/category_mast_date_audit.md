# MAST CNPq inventory: bounded dating-source audit

Date: 2026-11-20. Agent: crystalline_categories. This is a source-inspection event for `geo-H-history`; it supplies no new theorem or manuscript date.

## Source and actual inspection

Museu de Astronomia e Ciências Afins, **Arquivo CNPq (Acervo MAST): Inventário Sumário**, Rio de Janeiro: MAST, **1998**. The copyright/cataloguing page (physical PDF page 3) explicitly gives 1998 and 185 pages. The public PDF has 189 physical pages. The URL directory and the downloaded filename contain 2025; those are not the book's publication year.

Primary public URL: https://www.gov.br/mast/pt-br/imagens/publicacoes/2025/InventarioCNPq.pdf/@@display-file/file

Opened status: **the inventory PDF was downloaded and directly inspected**. Its underlying archival documents and photographs were **not opened**. Local source: `sources/mast_cnpq_inventory2025.pdf`. The root's successful download is logged in `logs/root_brazil_sources02.json`; this agent's source fingerprint and search audit are in `notes/category_mast_inventory_audit.json`.

All 189 physical pages were rendered and OCRed with saved per-page commands, exit statuses, hashes, and text. The English OCR is a finding aid, not a diplomatic transcription. Full text: `notes/category_mast_inventory_full.txt`; per-page outputs: `notes/category_mast_inventory_ocr/`; program/log: `code/category_mast_inventory_ocr.py`, `logs/category_mast_inventory_ocr.txt`. Relevant pages were then viewed as images at a 1800-pixel longest dimension. Render programs and all outputs are retained under `category_mast_*`.

## Exact positive records

| Record | Exact catalogue locator | What the inventory identifies | What it does not establish |
|---|---|---|---|
| **CNPq.T.6.3.003** | Printed p42, physical PDF p75; directly viewed | An IMPA activity report, Rio de Janeiro, **16 September 1955**, one document, **78 folios** | No author, mathematical topic, enclosure list, manuscript-leaf identification, or link to a digital original is supplied. The date is the report's catalogue date, not a date for cote1. |
| CNPq.T.4.1.010 | Printed p25, physical p58; directly viewed | Conclusions and suggestions of the CNPq mathematics-sector commission concerning the country's principal mathematics centres; undated, one document, seven folios | The entry neither names Grothendieck nor identifies a trace/genus-zero manuscript. |
| CNPq.TC.005 | Printed p57, physical p90; directly viewed | Correspondence sent/received specifically by Álvaro Alberto da Motta e Silva, 2 January 1952–16 December 1954; 159 documents, 301 folios; described topics include grants and atomic energy | The catalogue does not itemize correspondents or enclosures. No original letter has been read. |
| CNPq-F0058 | Printed p65, physical p98; directly viewed | Four photographs of the installation of research-section directors, Rio de Janeiro, July 1955 | These are catalogue descriptions of photographs, not mathematical draft witnesses. |
| CNPq-F0079 | Printed p67, physical p100; directly viewed | Two photographs and one copy of the installation of IMPA members, Rio de Janeiro, **November? 1952**; the question mark is printed | These do not identify or date the crossed trace proof. |

The photographic index, printed p145 / physical p178, explicitly lists **Leopoldo Nachbin** with references F0058 and F0079. This positive hit was visually checked. It must not be confused with an absence of Nachbin from the inventory. The textual name index has no Nachbin entry in its M–N range (printed p127 / physical p160, viewed), but the separate photographic index does.

## Search scope and limits

Case-insensitive searches of the complete 189-page OCR for `groth`, `fredholm`, and `hilbert` returned no hits. `nachbin` returned the photographic-index entry above. The relevant G ranges of both the textual and photographic indexes were visually checked (printed pp125 and141 / physical pp158 and174), with no Grothendieck entry there. This is an exact report of this inventory search, **not a claim that relevant originals are absent**.

The source itself explains why an inventory keyword search is limited. Printed ppVIII–IX / physical pp11–12, both directly viewed, describe a summary inventory of technical/scientific material; administrative personnel/financial/property records and processes were excluded. Correspondence is partly grouped in substantial volumes rather than described item by item. Printed p57 lists, for example, 146 volumes of letters for 1951–1975 under TC.003. These are catalogue statements as of the 1998 publication, not verified descriptions of present-day access arrangements.

Three public web queries were run: `"CNPq.T.6.3.003"`; `"IMPA" "16 set. 1955" relatório`; `site:impa.br "relatório" "1955" Grothendieck`. The only relevant result was the same inventory entry (web reference `turn267381725search1`). A spurious Scribd result was not opened or used. Complete retrieval output is retained in `notes/category_mast_web_records.json`. No independently public image of the 78-folio report was located by these bounded queries.

The root separately inspected the ordinary Zenith home page and found its explicit registration requirement before search. This agent did **not** probe catalogue query endpoints, create an account, contact anyone, or attempt to retrieve restricted records. That access boundary leaves the original report unopened; it is not evidence against its possible relevance.

## Consequence for the actual question

The inventory gives a precise, potentially useful archival record identifier, but **no dated witness linking the particular cote1 trace/genus-zero leaves to 1952–1955 has been obtained**. Even an original report listing a Fredholm course or publication would date only that activity unless it expressly identifies the draft or a matching enclosure. The smallest remaining historical requirement is still a dated document or archival description identifying those particular sheets, or an unmistakably matching dated enclosure. This audit neither proves nor refutes the prompt's cautious suggestion that the manuscript may predate the later publication.

No section or master bibliography was modified for this route. A source entry, if later required in the paper, should use the year **1998**, with the public 2025 PDF path merely as the retrieval URL.
