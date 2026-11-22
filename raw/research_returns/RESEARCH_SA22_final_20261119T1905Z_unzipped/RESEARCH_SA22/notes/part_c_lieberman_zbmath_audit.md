# Lieberman1968: direct zbMATH record-link assessment

19 November2026,17:47–17:49UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; agent `part_c_algebra`.

## Outcome

The actually advertised direct zbMATH target link returned **403Forbidden**, and the route stopped immediately. The record's full-text links could not be read. No original mathematical text or new public reprint URL was obtained. Lieberman1968 remains **NOT OPENED**; this is a bounded failed source lookup, not research movement or a mathematical-status change.

## Prior-record check

Before querying, retained `notes/` and `code/` were searched for `zbmath.org`, `eudml.org`, `0159.50501` and `3257059`. The relevant prior Lieberman output was `code/part_b_lieberman_archival_queries1_output.json`: it contains MaRDI's bibliographic identifiers, including zbMATHOpen documentID0159.50501 and DE3257059, but no retained opening of the direct target record. Other zbMATH URLs in the repository-discovery output concerned different identifiers,645163 and850799. The earlier general source notes mention EuDMLdiscovery searches but record no direct EuDMLtarget copy. Thus no prior direct-target record inspection was found in the retained notes/metadata searched; this is not a claim about unrecorded activity.

## Exact new route

1. One search batch submitted two queries: `"0159.50501"` with the zbmath.org domain filter, and the exact article title with the eudml.org filter. The returned results included MaRDIidentifiers and citing references; no actual EuDMLrecord for this target appeared. Because returned results included other domains, this result is not described as an exhaustive search of EuDML's catalogue.
2. The search-discovered Numdam record was opened at `https://www.numdam.org/item/ASENS_1995_4_28_3_317_0/`, the metadata/reference page for Friedlander's1995paper *Filtrations on algebraic cycles and homology* (webref `turn776334025view0`). **Line121** contains the exact Lieberman title, AJM90(1968),366–374, and an advertised **Zbl link38**. This is the citation record used to obtain an actual public target link, not a replacement mathematical source.
3. Clicking that link requested `https://zbmath.org/?q=an%3A0159.50501` and returned403Forbidden (webref `turn468466701view0`). No local HTTP fallback, retry, numeric-ID alias, alternative API, changed header, protected file, login or challenge operation followed. Neither the record contents nor any outgoing full-text link was read.

Known JSTOR, Internet Archive, SciSpace, thesis, MUSE, IHES, Ranicki, Cambridge and Fatcat routes were not retried. The discovery result's already known publisher/SciSpace hits were not opened. No original article was inferred from a title, review identifier, abstract or later citation.

## Counts, timings and compact provenance

| Actual operation | StartUTC | Measured elapsed | Scope/result |
|---|---|---:|---|
| Search-tool batch |17:48:03.468|1.081s|Two discovery queries; metadata/reference results.|
| Numdam reference-page open |17:48:16.440|0.735s|One page read, exact line121/link38 identified.|
| Advertised zbMATH link click |17:48:20.126|0.582s|One403denial; stopped.|
| `part_c_lieberman_zbmath_finalize.py` |17:49:23.647036|0.0007754739999654703s|Hashed three external raw web records; zero requests.|

There were exactly three web-tool calls, two search queries, one open, one click, zero ordinary local HTTPrequests and zero mathematical checks. `code/part_c_lieberman_zbmath_web.js` records the independently executed code-mode blocks and was not rerun as a batch. The compact metadata output is `code/part_c_lieberman_zbmath_web_output.json`, SHA256 `e138d9775cde31e42a5827475fca998bfe7ffe51dade9543dec2028eb427b8c4`.

All source bodies are retained only outside the project under `source_reading/lieberman_zbmath/`; the compact output preserves requests, starts, measured elapsed times, source titles, exact URLs, referenceIDs, error semantics, byte counts and hashes. Raw record identities are:

| Raw cache basename | Bytes | SHA256 |
|---|---:|---|
| `part_c_lieberman_zbmath_discovery.json` |16262|`09d87389595c1271d693c039edda78aa7e3962385d15edef07773c96f89b2520`|
| `part_c_lieberman_zbmath_reference_links.json` |7411|`8414be4295bdcc56c2500c6da5a2ae2257108be513a767ef97196739680bdc4f`|
| `part_c_lieberman_zbmath_record.json` |537|`4b6f81fe8a2ccbc4705e03077ecc8f78cdd429ff1bb318749c8a350fb679bf01`|

The denied direct record remains uninspected. There is no basis here to claim that zbMATH has no full-text link, only that its links could not be checked through this bounded route. No TeX, aggregate, prior archive or mathematical/source-status record was changed.
