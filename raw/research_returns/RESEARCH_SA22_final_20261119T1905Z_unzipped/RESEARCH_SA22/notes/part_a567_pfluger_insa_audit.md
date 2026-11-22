# Pfluger1960: one bounded INSA institutional-repository route

Date:2026-11-19,17:25–17:30UTC. Researcher: GPT-6 Astra Pro, OpenAI, agent part_a567.

## Outcome

The new publicly advertised Indian National Science Academy institutional repository was actually opened and searched. Both exact queries **Pfluger** and **Verheftung** returned HTTP200 pages explicitly reporting **0 results**. No original target passage was obtained. Pfluger's1960 named-original gate remains **unread**; no mathematical status changed and this source search is not counted as progress movement.

Target identity is unchanged: Albert Pfluger, *Ueber die Konstruktion Riemannscher Flächen durch Verheftung*, Journal of the Indian Mathematical Society(N.S.)24(1960),401–412, issued1961 in the cited original bibliographies. INSA's own journals and its Indian Journal of History of Science are not substituted for that journal.

## Prior coverage and why this was distinct

Consulted the prior Pfluger offprint, Jubilee, TDL, IISc, public-archive and distinct-public-route notes, and the relevant root original-followup and public-catalogue notes. The IISc note explicitly left an INSA catalogue route unvisited; its saved manifest had search strings but no actual INSA URL. PartC confirmed that no advertised INSA catalogue/repository endpoint had been retained or requested.

The prior publisher subscription route, Internet Archive, Tamil Digital Library, IITBombay, IISc, Mathdoc, HathiTrust, ETH, NDLI central-search endpoint, and Eremenko collections were not retried. The new insa.ndl.gov.in repository is a distinct institution-specific public service discovered by an actual search, not a guessed replacement for the previously unsuccessful central NDLI search. No previously denied endpoint was requested.

## Discovery and exact locators

One system2 query was executed:

Indian National Science Academy library digital repository catalogue journals

It returned26 source blocks, including the actual official library https://insaindia.res.in/library/ (turn591746076search0) and actual institutional repository https://insa.ndl.gov.in/ (turn591746076search1). Other returned items were not opened merely to expand the search.

Both pages were opened:
- Library: turn293257147view0,132 extracted lines. Lines6–7 advertise an e-Granthalaya OPAC link; that separate holdings link was observed but not followed in this bounded repository task.
- Repository: turn293257147view1,90 extracted lines. Lines16–30 explicitly display all3 top-level communities: Biographical Memoirs563, Dept.ofChemistry0, and Indian Journal of History of Science1532. No community in this displayed list is JIMS. This catalogue fact alone was not treated as an exhaustive item-level absence result.

One ordinary GET of the actual repository homepage returned HTTP200,436131bytes, SHA25630ef73849bbcf1e1d656dd7dcdc744b87047caeb58edee9d3156dc07460102cd. Its actual public search form has action /search, input name query, and no method attribute, so the ordinary default is GET. The form and link metadata are preserved in code/part_a567_pfluger_insa_public_page_output.json. No JavaScript bundle, login form, unpublished API, internal asset or content file was requested.

The two ordinary form requests were therefore:
- https://insa.ndl.gov.in/search?query=Pfluger
- https://insa.ndl.gov.in/search?query=Verheftung

Each returned HTTP200 and the rendered result label0results, followed by an explicit no-results message. The full extracted search text was read from the first response; the second has the same text hash. The query URLs and different original HTML hashes are both preserved. This is a report of the repository's returned results for these two terms, not a claim to have inventoried every item, every spelling, every physical holding, or every other institution. The route stops here.

## Requests, actual timing and artifacts

There were2 web-tool calls:1query and2page opens. Tool-internal request/cache counts are unknown. There were separately3 explicit ordinary HTTP GETs:1homepage plus2form searches. No retries, item-file downloads, person contacts, account actions or mathematical computations occurred.

| Operation | Actual startUTC | Measured seconds |
|---|---|---:|
|Web discovery query|17:27:00|0.972|
|Two web opens in one call|17:27:12|0.753|
|Ordinary repository homepage GET+parse|17:27:55.480841|10.025533731000905|
|Pfluger form GET+parse|17:28:49.922517|10.761131628998555|
|Verheftung form GET+parse|17:28:49.923326|11.53256192200206|
|Two-search parallel batch|17:28:49.922227|11.534293568001885|
|Local web-output metadata summarization only|17:29:48.126350|0.00476940099906642|

The web intervals are Date.now measurements around the awaited tool calls, excluding the subsequent clock reads. Ordinary request/parse intervals are actual perf_counter measurements, not whole-audit durations. The final metadata-only interval excludes its final output serialization. No elapsed time is inferred for reading or discussion.

Saved source-access utilities and metadata:
- code/part_a567_pfluger_insa_public_page.py and _output.json.
- code/part_a567_pfluger_insa_search.py and _output.json.
- code/part_a567_pfluger_insa_web_metadata.py and _output.json.
- code/part_a567_pfluger_insa_discovery_web_metadata.json.
- code/part_a567_pfluger_insa_open_web_metadata.json.

Full web search/open bodies reside only in /workspace/scratch/9c53b536a97f/source_reading/recorded_web_search/part_a567_pfluger_insa_*_raw.json. Original repository/search HTML and extracted search text reside only in /workspace/scratch/9c53b536a97f/source_reading/pfluger_insa/. Deliverable metadata records exact cache paths, SHA256s, byte counts, commands, timings and source refs. No full-source body was written to authored notes or deliverable code records.

The original theorem/proof was not read. No TeX, bibliography, aggregate report, theorem or finite-certificate status was changed.

