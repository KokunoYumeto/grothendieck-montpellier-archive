# Hartshorne1968 and Ogus1973 original-source access audit

Agent `/root/tensor_and_finite`, 2026-11-19, pass begun18:23UTC and completed18:27:48UTC. This is an access audit only. Neither original theorem body was obtained; C.U001 and C.U002 are unchanged.

## Existing attempts read before searching

- `agents/lie_theory/notes_C_original_source_retry.md`, completed18:10:12UTC.
- `agents/singularities_duality/logs/C_original_source_pass_1750.md`.
- The PartC report and original-source bibliography notes.

Thus the JSTOR client challenges, private Internet Archive files, failed guessed publisher PDF paths, SciSpace/JSTOR redirection, author homepages, and OpenAlex/Crossref attempts were not treated as new leads. No private archive file, authenticated access, challenge bypass, or author contact was attempted.

## New concrete checks

### 1. Raw publisher pages have no article-PDF link

The ordinary public HTML for both article records was successfully retrieved and saved:

- Hartshorne: https://annals.math.princeton.edu/1968/88-3/p03 , HTTP200,75237bytes, `hartshorne_annals.html`.
- Ogus: https://annals.math.princeton.edu/1973/98-2/p05 , HTTP200,75726bytes, `ogus_annals.html`.

All href/content attributes containing PDF, download, fulltext, the DOI identifiers or JSTOR were inspected. The only relevant links are the DOI, the generic JSTOR journal link, and the generic `/pdf_information` page. There is no `citation_pdf_url` or article file link in the raw page. Machine-readable results are in `publisher_html_results.json`.

The browser also opened the records: `turn832727038view1` (Hartshorne, metadata only) and `turn832727038view0` (Ogus, abstract only). The public PDF-information page, https://annals.math.princeton.edu/pdf_information , opened as `turn541023906view0`; it contains generic reader instructions, not a separate old-article archive or article link.

### 2. Semantic Scholar public API explicitly has no open PDF

The public Graph API was queried by exact DOI, requesting title,year,url,openAccessPdf. Both calls returnedHTTP200 and the correct exact titles/years:

- https://api.semanticscholar.org/graph/v1/paper/DOI:10.2307/1970720?fields=title,year,url,openAccessPdf
  - paperId `71030bdcc40ba626f436ffb23093a0ddaacffc12`
  - openAccessPdf `{url:"",status:"CLOSED",license:null}`.
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.2307/1970785?fields=title,year,url,openAccessPdf
  - paperId `b67006fddaa169ade6dd6ba635629049fc82e241`
  - openAccessPdf `{url:"",status:"CLOSED",license:null}`.

The exact responses are saved in `semanticscholar_hartshorne.json`, `semanticscholar_ogus.json`, and `semantic_scholar_results.json`. Browser opens of the corresponding ordinary paper records were inaccessible (`turn911037365view0/1`), so no original text is attributed to those pages. The API result says only that this index offers no public PDF; it is not a proof that no public copy exists anywhere.

### 3. ResearchGate original records explicitly lack full text

The actual Ogus original record was located by the public author publication list and opened:

https://www.researchgate.net/publication/248667505_Local_Cohomological_Dimension_of_Algebraic_Varieties

Browser `turn214391608view0`, lines15–38: the record says no full text is available and offers an author request. Only the original abstract and later citation snippets are readable. No request was sent.

The actual Hartshorne original record was located on page2 of his public publication list and opened:

https://www.researchgate.net/publication/265429856_Cohomological_Dimension_of_Algebraic_Varieties

Browser `turn206988192view0`, lines14–34: again no full text is available and only an author request is offered. No request was sent. Later citation snippets on either record were not treated as original theorem statements.

### 4. Targeted public-repository search produced no original PDF

Both search engines were used. Queries included exact titles with PDF/full-text/download qualifiers; exact DOI identifiers; author+title+printed starting page+scan; `ogus73` and `hartshorne68`; and targeted institutional/course domains Berkeley, Columbia, Stanford, Chicago, Edinburgh, Harvard Library and DASH. Search refs include `turn716803954search0` onwards, `turn200802567search0/1`, `turn832727038search0` onwards, `turn867551698search0`, `turn955002615search0` onwards, `turn288472744search0` onwards, `turn541023906search18` onwards, `turn840576478search0` onwards, `turn560551477search0` onwards, and `turn911037365search0` onwards.

The results were the already known publisher records, bibliographies, the1967 Bowdoin catalogue entry, newer original research quoting the old papers, and unrelated Hartshorne books or papers. A Harvard Library institutional help page says most pre1997 dissertations require ProQuest or reproduction requests; the1972 Ogus thesis was not obtained, and even that would require concordance to the1973 article. No useful observed public scan URL remains untried from this pass.

## Exact remaining gate

Still not opened:

- Hartshorne, *Cohomological Dimension of Algebraic Varieties*, Annals88(1968),403–450: original Proposition4.3 and Theorem7.5 with all hypotheses and endpoint clauses.
- Ogus, *Local Cohomological Dimension of Algebraic Varieties*, Annals98(1973),327–365: originalSection3 comparison, index range, endpoint map and projective consequences.

The current verified mathematics and later-author/source comparisons are unaffected. These unsuccessful access checks do not close a historical source-verification row. The main paper, bibliography, results and checks were not edited during the checkpoint freeze.
