# Lieberman1968: bounded original-volume public-preview route

19 November2026,18:07–18:11UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; agent `part_c_algebra`.

## Outcome

An actually indexed GoogleBooks record for **American Journal of Mathematics, Volume90(1968)** was opened. It supplies original-volume catalogue metadata, **not a readable Lieberman theorem statement**. The record does not reveal its bound extent or issue split, so inclusion of the required pp366–374 in this particular digitized item is itself unverified. Its advertised inside-book link encountered an access challenge and the route stopped. Lieberman1968 remains **NOT OPENED**; there is no mathematical or source-status movement.

## Prior scope checked

The existing Lieberman follow-up, PartB source/variant notes, A567paper-collection audit, and root MUSE/original-follow-up notes were searched before this attempt. Earlier GoogleBooks examples concerned Earle–Marden, Pfluger or unrelated books; no direct AJM90GoogleBooks item inspection was found in the retained target records searched. Broad prior whole-volume searches were acknowledged, but were not treated as an inspection of this newly exposed item.

## Actual catalogue and stopping point

The two-query discovery batch used `site:books.google.com "American Journal of Mathematics" "90" "1968"` and `site:books.google.com "Numerical and Homological Equivalence" "Lieberman"`. It exposed the actual public record:

`https://books.google.com/books/about/American_Journal_of_Mathematics.html?id=Q5k0AAAAIAAJ`

The record was opened as `turn140774001view0`, from search result `turn865599972search0`. Lines17–19identify volume90, Johns Hopkins University Press and1968. Lines54–58give the University of California copy and digitization on31May2007. Lines24–34show three early contents entries and state that fourteen other sections are not shown. None is the requested Lieberman article. The common-terms index and other-edition links are not original page readings.

The page exposed a `From inside the book` input area. One ordinary GET attempted to inspect its actual form action/fields, with automatic redirects disabled and no custom access headers. That request returned302; it did not supply the HTMLform. The local program retained the302status but not its Locationheader, so no destination is inferred from that request.

The already opened page separately advertised an ordinary inside-book word link, **abelian**, link15. This actual link—not a constructed API or page URL—was followed once:

`https://books.google.com/books?cad=4&id=Q5k0AAAAIAAJ&q=abelian&source=gbs_word_cloud_r`

The web tool reported a redirect to `https://www.google.com/sorry/index` and a non-retryable access error (`turn207803310view0`). The attempt stopped immediately. No modified query, page parameter, alternate edition, numericpage guess, preview API, account, purchase, challenge operation or retry followed. No inside-book results or page image was read. In particular, no claim is made that the record offers full view, limited preview or sufficient original snippets for the theorem.

## Exact counts and timings

| Actual operation | StartUTC | Measured elapsed | Result |
|---|---|---:|---|
| Search-tool batch,2queries |18:07:51.570|0.893s|Original-volume catalogue result.|
| GoogleBooksvolume-page open |18:07:56.267|0.823s|Metadata/contents/index only.|
| `part_c_lieberman_books_page.py`,1ordinary GET |18:08:44.375856|8.254976579999493s|302; redirects disabled; no form obtained.|
| Advertised inside-book link15 |18:09:39.692|0.877s|Google/sorryaccess challenge; stopped.|
| `part_c_lieberman_books_finalize.py`,0requests |18:10:50.650006|0.0007848410023143515s|Hashed3external raw web records and finalized compact metadata.|

The web scope is exactly three tool calls: two discovery queries, one page open and one advertised link click. The local scope is one ordinary HTTPrequest and zero mathematical checks. No previously exhausted article/thesis/institutional route was retried. The saved `.js` file is a transcript of the three independently executed tool calls, not a claim that they were rerun as a batch.

## Preserved compact provenance

`code/part_c_lieberman_books_web_output.json` has SHA256 `6e4dfbdabc581be66c98b42216b752142586a9c5d2a12ff466cb5aacf9f1f5b5`. It preserves exact requests, starts, measured runtimes, volume identity, actual links, source refs and access outcomes. The opaque challenge query is omitted from its compact URL list; the complete raw error remains preserved in the external cache, and was not followed.

Raw web records are outside the project under `source_reading/lieberman_books/`:

| Basename | Bytes | SHA256 |
|---|---:|---|
| `part_c_lieberman_books_discovery.json` |2867|`6f2edf7f571b5da949c34ecdf72d8c3ff7e3601effacd4f450a7d7005b7e3fe5`|
| `part_c_lieberman_books_volume.json` |4745|`e3f3367531ba962947801fda6a1f1bffa5ccb61ff15f0b63094ffb2d9944563c`|
| `part_c_lieberman_books_advertised_search.json` |902|`731c7f2bcfc65709433367f3824cdbfef4a0310ce264bef3780fa092fe78d992`|

Matching Python scripts and measured outputs are retained. The HTTP302request saved no HTMLcache and is not described as a successful form inspection. No TeX, aggregate, previous archive, theorem or source-status record was changed.
