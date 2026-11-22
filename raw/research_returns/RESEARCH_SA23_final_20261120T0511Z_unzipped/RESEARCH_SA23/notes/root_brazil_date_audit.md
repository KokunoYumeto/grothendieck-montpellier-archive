# Brazilian publication and archive route: cote 1 date

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run
SA23-20261120. Working record, 20 November 2026; updated after checkpoint 04.

## Question and present result

We seek a dated identification of the particular trace sheets, physical PDF
79–80, and genus-zero lemma, physical 111–112. A record that Grothendieck
taught functional analysis or submitted the Fredholm article in 1953 does
not by itself identify these leaves. This route has not supplied the
required witness.

## Sources and actual coverage

| Source | What was opened | Relevant finding and limit |
|---|---|---|
| MAST, current public publications catalogue, https://www.gov.br/mast/pt-br/centrais-de-conteudo/publicacoes | Official catalogue page and displayed cover links | It links the Nachbin and Gama inventories. The Gama URL directory says 1998, but the original copyright/cataloguing page gives 1988. The cover images alone were not treated as the inventory texts; the complete public PDFs were subsequently retrieved and inspected. |
| UNICAMP, collection BR SPCLEARQ CLN, https://arqhist.nuvem.cle.unicamp.br/index.php/leopoldo-nachbin-2 | Full public collection description | This particular collection has ten items and an accumulation range 1982–1989. It supplies no dated 1950s trace enclosure. We do not infer that all Nachbin papers have that range. |
| MAST, Zenith public home, http://zenith.mast.br/c_home.php | Public HTML downloaded, SHA256 84f894ca4ad6ad37f0b1df458408c7d6d67ae7fda74547b90393a86d4b93b953 | Lines 292–300 require registration before using search fields. We did not probe the search endpoints, register an account, or treat inaccessible contents as absent. |
| MAST, CNPq inventory, https://www.gov.br/mast/pt-br/imagens/publicacoes/2025/InventarioCNPq.pdf/@@display-file/file | Complete public PDF retrieved: 189 image-only pages, 15,612,559 bytes, SHA256 730425bf40a6c44057a4070832670f9169332d0976dd55d0408df038d43ef117 | The complete 189-page OCR and relevant original page images were subsequently checked by the category agent. Printed p.42, physical p.75, identifies CNPq.T.6.3.003, an IMPA activity report dated 16 September 1955, 78 folios. The original inventory was published in 1998, despite the 2025 URL directory. The report itself has not been opened; the catalogue does not identify a trace draft or enclosure. Exact coverage and limitations: notes/category_mast_date_audit.md. |
| Alberto de Azevedo, “Grothendieck no Brasil,” Matemática Universitária 44 (2009), pp.39–42, https://rmu.sbm.org.br/wp-content/uploads/sites/27/2018/03/n44_Artigo04.pdf | Complete four-page publisher PDF retrieved and text read, SHA256 74d020acdc7a9a3febef26e47b5e29441aa21c55ad96b67c5468af619996c03c | Contains original interviews from 2008–2009 and a retrospective account of the Brazilian publications and courses. It identifies no particular trace/genus-zero leaves. Its general period account is not used as a date proof. |
| Raphael Alcaires de Carvalho, UFRJ doctoral thesis (2021), “O ensino e a pesquisa em matemática no Rio de Janeiro em meados do século XX” | Public web extraction opened; relevant printed pp.141–145 searched/read. Local download returned HTTP 406 and is not claimed successful. | Table 23, printed p.141, reports a 1953 São Paulo seminar on compact Hilbert-space operators and a July 1953 Fredholm course, citing IMPA archives. Printed p.145 describes a Nachbin letter of 6 December 1954. This is a finding aid for originals, not an opened original report or letter; neither description identifies our sheets. |

We also opened the 2017 Robert article as a secondary route-finding aid and
the CSG published/unpublished-work catalogues. They supplied no dated
identification of the manuscript. Our mathematical conclusions continue to
rest on the original sources already checked and the complete proofs in
the paper, not on a secondary historical summary.

## Failures retained

The old public Gama-inventory URL
https://www.mast.br/inventarios/inventarios_lelio_gama.pdf returned HTTP 503.
The current MAST news page returned HTTP 401 in the web tool; we did not
retry that access-restricted page. A distinct public inventory endpoint
succeeded. The web tool rejected the 15.6 MB inventory as too large, so its
ordinary public download was used. The Zenith home was accessible by its
advertised HTTP URL, but its stated registration condition ends that
search route. No credentials or user account were used.

The first local fetch script stopped because the optional requests package
was absent. We replaced that dependency with standard-library urllib;
the failure and subsequent results are retained in the logs.

## Reproducible record and next step

Search/open outputs: notes/root_history_web03.json through
notes/root_history_web14.json. Fetch code and measured outputs:
code/root_brazil_sources01.py and code/root_brazil_sources02.py, with
matching logs. Original source caches are under sources/ and are listed
by hash in checkpoint exclusions.

## Completed Gama inspection after checkpoint 04

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
