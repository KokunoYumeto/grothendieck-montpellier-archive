# Pfluger: bounded IISc public institutional-catalogue route

19 November 2026, approximately15:37–15:40UTC. Researcher: GPT-6 Astra Pro, subagent `part_c_algebra`.

## Outcome and scope

**No original Pfluger text or relevant holding record was recovered.** The IISc institutional route was attempted and stopped after the actual advertised public catalogue returned502 and the independently advertised research repository returned403. A catalogue search could not be submitted, so this is **not a zero-result search and not evidence that IISc lacks the volume**. The original-source requirement remains open. No mathematical status changed.

Before starting, I searched the saved notes and the root/B Pfluger retrieval records for NDLI, the National Digital Library of India, INSA, IISc, and their actual institutional domains. The only IISc mentions found in the relevant earlier catalogue outputs concerned an unrelated1971biochemistry jubilee volume. There was no previous institutional catalogue attempt for this mathematical source. The detailed completed IA Jubilee audit and the TDL audit were read to avoid repeating their holdings searches.

## Search discovery and actual public links

Three web-search batches used eight queries, all retained in `code/part_c_pfluger_iisc_web_manifest.json`. The first batch checked the precise society/Jubilee title and potential IISc/INSA indexing. The second located IISc's official library site and its description of public catalogue access. The final two-query batch sought the actual IISc catalogue link after the main site was unavailable. No institutional search result was treated as an original mathematical text.

The official IISc library homepage is `https://library.iisc.ac.in/`. The web opening timed out (`turn793753024view0`); one ordinary GET separately returned502. The two actually indexed official library pages `https://library.iisc.ac.in/index.php/faq` and `https://library.iisc.ac.in/index.php/node/6254` likewise failed in the web tool with timeout and502 respectively (`turn264245988view0` and `turn264245988view1`). No search form or holding result was read from these failed responses.

An independently indexed, publicly readable institutional resource directory opened at `https://libraryidp.iisc.ac.in/` (`turn763433441view0`). I read only its public directory and extracted the actual anchors in its “Important Links” section. The page also describes authenticated subscription access, but **none of its publisher authentication links or login flows was followed**. Its public catalogue anchor was not a guessed hostname or path:

`http://saraslibrary.iisc.ac.in:8280/opac/`

The exact ordinary GET to that advertised URL returned502. No different port, account, legacy terminal login, internal service, or unadvertised catalogue endpoint was tried. This exhausted the bounded catalogue attempt.

The same directory advertises `http://eprints.iisc.ac.in/` as the research-publications repository. Clicking that actual link in the web tool reached `https://eprints.iisc.ac.in/` and returned403 (`turn860809031view0`). It was stopped immediately, without an ordinary-HTTP retry, altered headers, a guessed article path, or an alternative repository API. Its restriction is not represented as a zero-hit result.

The directory's NDLI link and the search results for INSA were observed as possible future routes, but **no NDLI or INSA catalogue request was made in this bounded IISc task**. The requested1960/1961mathematical volume was not conflated with IISc's own jubilee lectures, alumni publications, or the1971biochemistry volume.

## Saved evidence and measured operations

One utility, `code/part_c_pfluger_iisc_public_page.py`, was actually invoked three times. It only reads a specified previously observed public URL and records its advertised forms/links; it submits no form. Each invocation has a separate full outputJSON/TXT. The canonical `part_c_pfluger_iisc_public_page_output.json` is a manifest of these actual runs, not a newly executed request or an invented combined runtime.

| Invocation | Start UTC | Request outcome | Measured elapsed |
|---|---|---|---:|
| `home` |15:38:35.064865 |One GET to official library homepage;502 |8.164364077s |
| `directory` |15:39:27.857982 |One GET to public institutional directory;200,33,222bytes |9.050398982s |
| `catalogue` |15:39:53.863235 |One GET to its actual advertised public OPAC;502 |10.546002719s |

The directory HTML is saved as `sources/part_c_pfluger_iisc_directory.html`, SHA256 `11a9b67b702ecff7bac86d9b56acd2262cf2c65ce79679e5c03249720807b0c5`, with extracted text and the complete actual links in its output record. Failed invocations saved status/error metadata and did not create fictitious source pages.

There were **three locally timed GET operations**, **eight web-search queries in three batches**, and **five web open/click operations**. Web-operation runtimes were not separately measured and are not inferred from the local timings. No source-content PDF, offprint, journal volume, or account-protected item was requested in this route. This is a bounded source-discovery audit, not a finite mathematical check or a gate closure.
