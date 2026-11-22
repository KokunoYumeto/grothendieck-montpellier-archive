# Public source-route follow-up after checkpoint08

We inspected the already acquired historical JSTOR landing metadata for Lieberman1968 and made one delayed availability check for each of two public Fatcat DOI lookups. The timed script is `code/root_source_route_followup09.py`; its original output is retained alongside it. The run began2026-11-19T17:26:28.857017+00:00 and took12.642931041002157 seconds in total.

## Cached image evidence

The Lieberman landing JSON has SHA256 `b9ca879233daf4b0887c7abc43885846f2e719f74fdd2ff15abc30da62f3d618`. We decoded only the already embedded GIF bytes and read their dimensions. The sole non-placeholder GIF is97 by152 pixels and is explicitly labelled the *American Journal of Mathematics* cover. The apparent article-page image and all nine numbered page thumbnails are1 by1 pixel placeholders. They contain no readable mathematical text. We did not reinterpret the cover as an article preview or request the encoded private storage locations in the lazy-loading metadata.

## Delayed public metadata availability

| Work | Public DOI lookup | Result | Request seconds |
|---|---|---|---:|
| Fujiwara1995 | `https://api.fatcat.wiki/v0/release/lookup?doi=10.1215%2FS0012-7094-95-08002-8` | HTTP503, upstream connection timeout; no release record |12.640618183999322|
| Lieberman1968 | `https://api.fatcat.wiki/v0/release/lookup?doi=10.2307%2F2373533` | HTTP503, upstream connection timeout; no release record |12.638866581000912|

The two independent requests ran concurrently, with network wall time12.64203240799543 seconds. This was one delayed check after the earlier service failure, with no retry within this run and no file-content requests. These failures do not establish absence from the catalogue. No prescribed original-source gate changed status, and this follow-up is not substantive movement under the user's review rule.

## Separate Internet Archive Scholar route

Four indexed queries, split between the two search engines, used the Lieberman title, Fujiwara title and their two exact DOI suffixes with the `site:scholar.archive.org` restriction. Neither engine returned an indexed hit. An actual opening of `https://scholar.archive.org/` returned a rate-limit notice, reference `turn570345033view0`; no subsequent form, article, alternate endpoint or storage request was made. Empty indexed results are not an exhaustive repository inventory, and the unavailable homepage supplies no absence evidence.

The first two-query call took0.376seconds; the second two-query call together with the homepage open took0.974seconds. The exact executed bodies and compact result are `code/root_scholar_archive_route.js` and `code/root_scholar_archive_route_output.json`. Complete tool response bodies are retained only in the outside reading cache. No original text was obtained and no gate changed status.
