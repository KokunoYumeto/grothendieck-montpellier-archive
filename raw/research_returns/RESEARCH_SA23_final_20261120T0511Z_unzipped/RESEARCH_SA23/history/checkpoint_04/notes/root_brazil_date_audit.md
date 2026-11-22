# Brazilian publication and archive route: cote 1 date

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run
SA23-20261120. Working record, 20 November 2026, before checkpoint 04.

## Question and present result

We seek a dated identification of the particular trace sheets, physical PDF
79–80, and genus-zero lemma, physical 111–112. A record that Grothendieck
taught functional analysis or submitted the Fredholm article in 1953 does
not by itself identify these leaves. This route has not supplied the
required witness.

## Sources and actual coverage

| Source | What was opened | Relevant finding and limit |
|---|---|---|
| MAST, current public publications catalogue, https://www.gov.br/mast/pt-br/centrais-de-conteudo/publicacoes | Official catalogue page and displayed cover links | It lists the Nachbin inventory (1997) and Gama inventory (1998). The cover images are not the inventory texts. |
| UNICAMP, collection BR SPCLEARQ CLN, https://arqhist.nuvem.cle.unicamp.br/index.php/leopoldo-nachbin-2 | Full public collection description | This particular collection has ten items and an accumulation range 1982–1989. It supplies no dated 1950s trace enclosure. We do not infer that all Nachbin papers have that range. |
| MAST, Zenith public home, http://zenith.mast.br/c_home.php | Public HTML downloaded, SHA256 84f894ca4ad6ad37f0b1df458408c7d6d67ae7fda74547b90393a86d4b93b953 | Lines 292–300 require registration before using search fields. We did not probe the search endpoints, register an account, or treat inaccessible contents as absent. |
| MAST, CNPq inventory, https://www.gov.br/mast/pt-br/imagens/publicacoes/2025/InventarioCNPq.pdf/@@display-file/file | Complete public PDF retrieved: 189 image-only pages, 15,612,559 bytes, SHA256 730425bf40a6c44057a4070832670f9169332d0976dd55d0408df038d43ef117 | The search index identifies CNPq.T.6.3.003, an IMPA activity report dated 16 September 1955, 78 folios, on printed inventory p.42. The independent visual/OCR audit is in progress; the report itself has not been opened. Empty native PDF extraction is not an absence finding. |
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

The discriminating next step is to inspect the public inventory's exact
entry and indexes, then seek an independently public copy or precise
description of a relevant original. We will not infer a date from a course
title, dossier adjacency, general subject period, or the mere existence of
an activity report. This is documentary search, not movement under the
user's formal-review rule.
