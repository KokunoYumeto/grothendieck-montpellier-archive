# Bounded check of Nachbin's 1956 historical article

Date: 2026-11-20. Scope: seek an explicit contemporary identification of Grothendieck's Hilbert trace/genus-zero draft or a dated enclosure. This is a source-access report, not a finding about the unopened article's contents.

## Exact identity and inspected evidence

Jorge Mujica, *Os trabalhos de Leopoldo Nachbin (1922–1993)*, Unicamp research report RP25/94 (May1994), printedp13, item[27a], lists **“Aspectos do desenvolvimento recente da matemática no Brasil,” Ciência e Cultura8(1956),213–217; Sociedade Paranaense de Matemática, Anuário3(1956),28–41**. The report's cover and printedp13 were directly visually read from the public PDF, not merely accepted from search snippets. This is a bibliography of the article, not the article itself.

Public PDF: https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-1994-25.pdf . Local copy: `notes/category_nachbin_1956_bibliography1994.pdf`; inspected cover is physical1, printedp13 is the right half of physical9. Download, SHA256, rendering commands and outputs are preserved in `logs/category_nachbin_1956_metadata_fetch.txt` and `logs/category_nachbin_1956_bibliography_render.txt`. A web screenshot call returned only an ImageDisplayed marker without actual image content; no visual claim rests on that failed image delivery. The subsequent local rendering supplied the inspected image.

## Access and content bounds

| Source | Actual outcome | Evidentiary use |
|---|---|---|
| Official Ciência e Cultura archive page, https://revistacienciaecultura.org.br/?p=1860 | Opened; describes the1949–2017 digitization and links the national-library/SBPC archives | Establishes an official archive route, not the article's contents |
| National-library reader, https://memoria.bn.gov.br/docreader/DocReader.aspx?bib=003069&pagfis=1 | HTTP403 returned by web reader | Original journal pages **not opened** |
| Official link to https://bndigital.bn.gov.br/hemeroteca-digital/ | HTTP403 | No reading of original issue |
| Official link to https://sbpcacervodigital.org.br/handle/20.500.11832/2534 | Explicit Anubis Access Denied, code9e4edb5b6b850c41 | Stopped; no challenge bypass, endpoint probing or account attempted |
| Publisher's1996 *Ciência e sociedade* page, https://www.editora.ufpr.br/Categoria/ciencia-e-sociedade-17/p | Search-result metadata only | A possible later collection; not opened or treated as the1956 text |
| Cadernos SBPC7, *Fundação e primeiros movimentos1948–1958* (2004), https://www.sbpcnet.org.br/site/publicacoes/outras-publicacoes/caderno_digital/caderno_7.pdf | Web reader exceeded its content-size limit; ordinary public download succeeded, HTTP200 | Actual public PDF inspected as described below |

The82-page SBPC volume was opened locally. Its titlepage, table of contents and introduction were visually read (physical3,5,7; page labels5 and7 respectively for the latter two). The table lists the1956 material as an atomic-energy symposium report, followed by selected typed proceedings, rather than Nachbin's article. The introduction atp7 says the corresponding1956 journal extract concerns the25–27April1956 symposium. This volume therefore does not supply the requested article in its listed documentary contents.

All82pages were OCRed as a finding aid, with separate per-page statuses and hashes; no render/OCR failure occurred. The161,840-character combined OCR has no `nachbin`, `groth` or `fredholm` hit. Some reproduced handwritten records produce poor OCR, so this search is **not** an assertion that every name in the volume is absent. The direct contents-page identification, rather than keyword absence, is the reason this is not treated as a reproduction of the article.

Downloaded SBPC PDF:40,725,483bytes, SHA256 `a495bdb06ca8245109f8a4b6ea2c5c6ebbab646884944e07bc8d3593e93aa5f7`. Files: `notes/category_nachbin_1956_caderno7.pdf`, `notes/category_nachbin_1956_caderno7_full.txt`, and `notes/category_nachbin_1956_caderno7_ocr/`. Programs and logs use the same `category_nachbin_1956_` prefix. The original text extraction contains form-feed markers only; the later OCR is separately named.

## Exact search record

Complete returned records are preserved in `notes/category_nachbin_1956_web_records.json` and `notes/category_nachbin_1956_web_records2.json`. Queries, grouped in execution order, were:

1. `"Nachbin" "213-217" "1956"`; `"Ciência e Cultura" "1956" "8" pdf`; `"Anuário" "Sociedade Paranaense de Matemática" "1956" pdf`; `"Aspectos do desenvolvimento recente" Nachbin texto`.
2. `"Ciência e Cultura" acervo digital 1956`; `"Anuário da Sociedade Paranaense" Nachbin 1956 arquivo`.
3. `site:memoria.bn.gov.br "Nachbin" "1956"`; `site:memoria.bn.gov.br "Aspectos do" "matemática"`.
4. `"Leopoldo Nachbin" "Ciência e sociedade" pdf`; `"Nachbin" "213" "217" "Cultura"`; `"Aspectos do Desenvolvimento Recente da Matemática" "Grothendieck"`.
5. `site:sbpcnet.org.br "caderno_7.pdf" "Nachbin"`; `site:memoria.bn.gov.br "003069_1956"`; `"Aspectos do desenvolvimento recente da matemática no Brasil" filetype:pdf -site:academia.edu -site:scribd.com -site:researchgate.net -site:crephimat.com.br -site:rbhm.org.br`.
6. `"Aspectos do desenvolvimento recente da matemática no Brasil" "pdf"`; `"Ciência e Cultura" "1956" "Nachbin" "Grothendieck"`; `"Sociedade Paranaense" "1956" "28" "41" Nachbin`.
7. `"Nachbin" "Aspectos" "desenvolvimento" "1956" pdf`; `"003069" "1956" "Cultura"`; `"Anuário da Sociedade Paranaense de Matemática" "3" "1956"`.
8. `"Sociedade Paranaense de Matemática" "acervo" anuário`; `"Aspectos do desenvolvimento" "Nachbin" "1956" -site:academia.edu -site:scribd.com -site:researchgate.net -site:livrozilla.com -site:aprenderly.com -site:crephimat.com.br -site:rbhm.org.br`; `"Ciência e Cultura" "1956" "213" Nachbin -site:academia.edu`.

Groups2 and7 used the stronger search system; other groups used the routine system. Secondary theses, later histories and repository snippets were used only as finding aids, without inferring unpublished sheet dates from general career chronology. No paid copy was purchased and no individual or institution was contacted.

## Result and smallest remaining witness

The exact1956 article has **not been opened** in this bounded public-source route. No positive or negative assertion about its mention of Grothendieck, trace, genus zero or an enclosure is justified. Nor is a1955lecture date independently established by the present check. The identified publication remains a concrete source lead whose contents are unverified here.

Even opening the article would date the particular cote1 leaves only if it explicitly identifies that draft, a recognizable enclosure, or another dated record tied to the leaves. A general account of Grothendieck's Brazilian work, a course title or the subject of functional analysis would not supply that link. The smallest unresolved historical gate remains an explicit dated identification of the relevant manuscript leaves; the completed mathematical proof and publication-content comparison are unchanged.
