# Pfluger1960: independent Tamil Digital Library catalogue audit

19 November2026,15:02–15:11UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; independent Part C agent. Parent retains the overall Pfluger source assessment.

## Outcome and exact limits

The original Tamil Digital Library catalogue is accessible and returns actual journal records. The six successfully read result pages contain60 catalogue entries,43 concerning the Journal of the Indian Mathematical Society or its supplements. All43 already occur in the parent's saved Internet Archive inventory. Every one has an explicit date in its advertised catalogue URL, and none identifies1960,1961, or a Golden Jubilee issue.

This is **not an exhaustive inventory of the17 advertised result pages**. Pages3 and13 returnedHTTP503, interrupting the chain of advertised links to pages4–12. One subsequent ordinary web-tool open of each failed as inaccessible; no successful reading of those pages is claimed. The Golden Jubilee query also returned503. The correctly stateful periodical-form attempt reached a303 redirect but its target returned503, so the1959–1962 filtered results were not obtained. These failures are not zero-result findings. The route has produced no new original mathematical pages; **Pfluger1960 remains NOT OPENED**.

## Discovery and actual public interface

The parent supplied https://tamildigitallibrary.in/index-search, independently opened as turn497349532view0. One ordinary local request returnedHTTP200 and saved273641bytes to sources/part_c_pfluger_tdl_index_search.html, SHA256bbfc62a34d168f5e4aae3929d45038e0062c342aba3fadb4ce05b5aaf570265b.

The original page's inline click handler, localHTML lines1899–1907, sends the entered title/author phrase to `https://tamildigitallibrary.in/search/<phrase>`. Its periodical form, beginning atline2127, publicly advertises a POST to `https://tamildigitallibrary.in/advance_search_Periodical_filter_data_form`. The actual form includes title, volume, author, source, edition, language, and beginning/ending publication-year fields. Its advertised JavaScript at https://tamildigitallibrary.in/assets/js/advance_search/advance_search.js was separately fetchedHTTP200; the script's category map identifies21 as Periodical. No category or private record identifier was guessed.

The longer query Journal of Indian Mathematical Society returned an explicit no-results page. This wording omits the second definite article found in the actual catalogue titles, so the response was not treated as evidence that the journal is absent. The shorter query Mathematical succeeds, including known journal volumes and unrelated mathematical books. Its first page advertises pagination through17 and supplies explicit next-page links. The inventory program follows only URLs actually returned by those links; it does not construct unseen article IDs or infer the contents of unread pages.

## Successfully read pages and candidate records

The cached first page and pages2,14,15,16,17 were read. The two failures were pages3 and13. The success pages are saved as sources/part_c_pfluger_tdl_mathematical.html and sources/part_c_pfluger_tdl_page_N.html. Complete parsed article titles and their original encoded/decoded URLs are in code/part_c_pfluger_tdl_inventory_output.json; hashes and status/timing for every page request are also preserved there.

Examples actually advertised by the catalogue include:

| TDL article ID | Journal issue stated in original catalogue URL |
|---|---|
|26852|Volume22(1958)|
|26544|Index to volumes1–20(1934–1956)|
|28834|Volume16,no.12(December1926)|
|28397|Volume10,nos.1–2(March–June1946)|
|28515|Supplement,VolumeXV; catalogue's additional wording saysVol.25,1924|
|28587|Supplement,VolumeXVII; catalogue's additional wording saysVol.27,1929|

Those inconsistent Roman/Arabic volume labels in the supplement URLs are retained, not corrected without reading the scan. None is relabelled as the1960 volume24. The source comparison program matches the43 actually read journal/supplement IDs against identifiers present in code/root_pfluger_public_ocr_inventory_output.json. That broader parent file contains154 distinct TDL IDs across its entries; this is not substituted for the parent's148-journal count. All43 matched and no new ID was found. This comparison does not say that the unread catalogue pages lack additional records.

## Periodical form: what did and did not execute

The first form submission used the exact advertised field names with category21, title Mathematical, and publication years1959–1962. It returnedHTTP200 after redirecting to `/book-search-new`, but the resulting HTML is a JavaScript-driven listing and did not itself contain searched records. The initial urllib opener did not preserve anonymous cookies across the redirect. Therefore that response was recorded as inconclusive, not as an empty filtered catalogue.

The listing's actual `Front_search_Book` function, localHTML lines5550–5795, advertises the read-only `book-list-data-ajax-new` endpoint and its complete request fields. A second program implements the ordinary form workflow with CookieJar, including the public form token and filter state; no account is used. Its actual execution made only the formPOST and automatic303 redirect. The redirected page returned503 before the intended AJAX request could run. Thus **the AJAX results request was present in the saved program but did not execute**. The output records this precisely as one explicit request operation plus one automatic redirect, with no results count.

## Actual scripts, request scope, and runtimes

All programs below actually ran and have matching _output.json and _output.txt files. They are source-retrieval or metadata-comparison programs, not mathematical certificate tests.

| Program in code/ | Actual scope | Runtime |
|---|---|---:|
|part_c_pfluger_tdl_forms.py|1 ordinary catalogue-pageGET; parsed public forms and script links|9.425723308s|
|part_c_pfluger_tdl_search.py|2GETs: actual journal-title search and advertised advanced-searchJS|8.953959248s|
|part_c_pfluger_tdl_filters.py|2public searchGETs plus1periodical formPOST; one search503; form's redirectedHTML inconclusive|46.497532967s|
|part_c_pfluger_tdl_inventory.py|7actual paginationGETs;5successful,2HTTP503; cached first page reused|69.999104874s|
|part_c_pfluger_tdl_form_session.py|1explicit formPOST plus1observed303redirectGET; target503; AJAX not executed|12.076119009s|
|part_c_pfluger_tdl_compare.py|0network requests;43read journal IDs compared to parent's saved inventory|0.004830234s|

The total is14 explicit urllib request operations, with automatic redirects reported separately rather than hidden in an invented wire-request total. Exact starts, individual durations, status codes, fields and response hashes are in each program output. The stateful form's303 is explicitly instrumented. The earlier form's redirect was not separately instrumented; its changed finalURL is recorded. Web-tool opens of the source page and the two failed pagination URLs have no locally measured runtime. The failed follow-up refs are turn569150419view0 and turn569150419view1.

No mathematical source or bibliography status was promoted. No journalPDF was fetched in this audit, because no new candidate for the target volume was identified. The parent received the positive catalogue findings and the exact incomplete-coverage limits.
# Final TDL scope as of 15:33 UTC

The delayed checks are complete. **The original Pfluger source gate remains open.** The ordinary `Mathematical` search was eventually read through all17 advertised pages:170 records, including133 journal/supplement records identified by their Mathematical Society titles; all133 IDs occur in the parent's previous InternetArchive inventory. The separate ordinary `Jubilee` search was read through all6 pages:53 records, with no mathematical-journal title match. These are exact per-query counts, not a claim that the whole TDL catalogue has been exhausted.

The successful advanced periodical form is materially distinct. With title `Mathematical` and publication years1959–1962, its normal anonymous session and the actual advertised read-only AJAX returned `count="1"`, `Showing 1 to 1 of 1 entries`, and no pagination. That result is **TDL26669, labelled volume23(1959)**, absent both from the parent's previous IA inventory and from the ordinary170-result search. This discrepancy itself rules out treating the ordinary search as an exhaustive inventory of every matching holding. The form result and its exact fields are retained verbatim. Its single returned record is a new holding, not the required1960 article.

## Actual bound-volume inspection

The returned actual record URL was opened normally:

`https://tamildigitallibrary.in/Articles/%E0%AE%87%E0%AE%A4%E0%AE%B4%E0%AF%8D-26669-The%20journal%20of%20the%20Mathematical%20Society-Vol.%2023%20%281959%29`

The exact URL is also preserved in `code/part_c_pfluger_tdl_1959_record_output.json` and the form-result HTML. The page explicitly embeds an `object` of type `application/pdf` with this public data URL:

`https://tamildigitallibrary.in/assets/docs/uploads/primary_files/periodicals/TVA_PRL_0026664/ACL-CPL_00586_The_journal_of_the_Indian_Mathematical_society_Vol_23_1959.pdf`

Following that actual public reader link returned200 and a187-page original PDF,4,726,442bytes, SHA256 `af10cf82063ebb3587d8a6510d1ea34280f1d1231635137d8af1c4f7082ce379`. The full volume is retained outside the deliverable at `source_reading/part_c_tdl_jims_1959.pdf`; it is not redistributed in the project. Embedded text is absent from the pages inspected; the reported3631-character extraction consists essentially of the extraction program's page separators and is **not** usable full-book OCR.

I actually viewed the title (PDF1), imprint (PDF2), complete contents (PDF3), first article (PDF4), printedp2 (PDF5), and final printedpp181 and184 (PDF184 and187). The title identifies *The Journal of the Indian Mathematical Society*, new series, Vol.XXIII,1959, edited by R.P.Bambah and P.L.Bhatnagar. The complete one-page contents has14 author entries representing13 distinct articles; it contains no Pfluger entry. The file has three front pages followed by printedpp1–184. The first article is R.C.Buck's *Convergence theorems for finitely additive integrals*. The last is Sahib Ram Mandan's *Uni- and demi-orthocentric simplexes*, listed fromp169 and ending onp184. No appended later-volume title or contents is present in these front/end pages; the complete contents and matching first/last pagination identify the bound volume inspected. The final bibliography actually cites a1960 paper, so the exclusion of the target is based on the actual contents and pagination, **not merely the catalogue's1959 year**. The required Pfluger article, volume24pp401–412, is not supplied by this opened volume.

The public record advertised30 related records. Seven have Mathematical Society titles, dated1918–1950 or old-series1920s/1931 in their labels; all seven IDs are in the parent's already examined IA inventory. They are retained in `code/part_c_pfluger_tdl_catalogue_findings_output.json`. No unadvertised neighboring record IDs or content filenames were guessed or requested.

## Later requests and measured processing

All later requests used ordinary public metadata, the documented anonymous form/session flow, or the PDF explicitly embedded in the opened reader. There was no login, challenge, access-control response, hidden content request, or altered download restriction. The final successful page6 request occurred after its earlier temporary503 and was logged separately rather than overwriting that failure.

| Actual program | Actual scope | Recorded elapsed time |
|---|---|---:|
| `part_c_pfluger_tdl_inventory_delayed.py` |11 metadata GETs;10 succeeded, one page6 temporary503; combines six earlier cached pages |117.121053684s |
| `part_c_pfluger_tdl_compare_delayed.py` |No network; compares123 actually read journal IDs |0.010750347s |
| `part_c_pfluger_tdl_final_public_queries.py`, Jubilee phase |One new public query GET,200 |21.156959784s |
| Same wrapper, reused advertised-form phase |Two explicit POST operations, both200; first has one logged303 redirect GET; returns the single1959 record |31.078547201s |
| `part_c_pfluger_tdl_jubilee_inventory.py` |Five further advertised pagination GETs, all200; six pages/53 records in total |44.813292657s |
| `part_c_pfluger_tdl_1959_record.py` |One actual public record GET,200; extracts its advertised links |22.715578608s |
| `part_c_pfluger_tdl_1959_pdf.py` |One actually embedded PDF GET,200; extracts text and renders12 selected pages |11.740142727s |
| `part_c_pfluger_tdl_catalogue_findings.py` |No network; parses exact counts and30 related records |0.012531202s |
| `part_c_pfluger_tdl_last_page.py` |One delayed page6 GET,200; completes17-page ordinary search and compares133 journal IDs |16.704724133s |

The wrapper's two separately timed phases are not falsely labelled a single measured outer runtime. Matching outputJSON/TXT files preserve timestamps, statuses, URLs, sizes, hashes and counts. This later segment made22 explicit urllib request operations, plus the one separately logged automatic303 redirect; combined with the earlier14 explicit operations, the TDL route has36 explicit operations. Earlier automatically followed redirects retain their original stated limitations. These are source-access/metadata utilities, not finite mathematical proof checks. No source status or theorem status is promoted by the additional1959 holding.

# Delayed public-catalogue recovery, 15:23–15:26 UTC

After the earlier temporary503 responses and a substantial backoff, a single bounded retry of the two actually advertised missing pagination links succeeded. The program `code/part_c_pfluger_tdl_inventory_delayed.py` began at `2026-11-19T15:23:54.775123Z`, made11 ordinary metadata GETs with at most two concurrent requests, and ran117.121053684seconds. It followed only pagination anchors actually returned by successfully read pages. Ten requests returned200; the newly encountered page6 returned503 and was not retried in that run. No authentication/permission response was encountered and no book file was requested.

Together with the six previously read pages, this gives **16 of the17 advertised Mathematical-search pages**, containing160 distinct article records. Of these,123 are Journal of the Indian Mathematical Society entries or supplements. None has a1960/1961 or Golden/Jubilee indication in the displayed title/decoded catalogue URL. Three entries lack a year in that URL; their IDs are26348,26357 and28479, and their absence of a year is not silently converted into a pre1960 date.

`code/part_c_pfluger_tdl_compare_delayed.py` actually ran at15:26:01.763077UTC for0.010750347seconds, with zero network requests. It compared all123 journal IDs against the parent's saved InternetArchive metadata inventory. **All123 are already present; zero new journal IDs were found.** This is stronger coverage of the originally partial catalogue route, but not an exhaustive absence theorem: page6 is still unread, the query is specifically Mathematical, and differently titled records could exist. Exact requests, timings, hashes, all160 records and the three undated rows are preserved in the two matching outputJSON/TXT pairs. The mathematical and original-source statuses remain unchanged.

