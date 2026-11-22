# Public catalogue and toric-literature follow-up

## Missing originals: bounded new routes

The four discovery queries are retained in `code/root_initial_catalogue_queries_1545.json`. They produced public repository/catalogue entry points, not a missing original. The web opens and observed advertised forms are documented in `root_public_catalogues_open_web.json` and `root_public_catalogues_forms_web.json`.

The first Python form-fetch prototype failed at importing `requests`, before any network request. Its actual body and traceback are preserved as `root_public_catalogue_forms_failed01.py` and its output. No duration was measured for that failure. The working standard-library version made exactly three GET requests: MPIM's advanced form and NDLI's public home page were200; Google Books' normal1961-record request redirected to a429 challenge page and was stopped. Batch wall time was13.532168659 seconds. No challenge was bypassed.

Only observed form actions were used. MPIM's basic GET search for Fujiwara returned nine results, all nine actually read: modern Druţu–Mackay, two final reports, Pimenov, Gordeev, Gromadzki, Dranishnikov, Grunewald and Bell–Fujiwara2005 curve-graph material. None was the1992 preprint or1995 tubular-neighborhood article; no content PDF was fetched from those unrelated results. NDLI's live advertised `/search?key=Verheftung` endpoint returned404, not an empty search result. Batch time was12.189128438 seconds; individual MPIM12.187971946 seconds, NDLI8.259522739 seconds.

The Part A delayed Fatcat check made exactly two DOI lookups, Fujiwara and Lieberman, both503 upstream timeouts (11.899788230 and11.898996335 seconds; batch11.901000857 seconds). This supplied no records or files, and was stopped without retries. Part C's IISc audit separately records the public catalogue/repository failures; it is not an absence result. None of these attempts closes Pfluger1960, Lieberman1968 or Fujiwara1995.

## Unequal-toric and raw-descent literature scope

Three preliminary queries (`root_toric_literature_search.json`,0.463 seconds) were followed by two verifying queries (`root_toric_literature_verify.json`,0.957 seconds). They did not identify the exact global fiber theorem. Search headings and references are retained, without republishing long unrelated third-party extracts. The proof depends only on the previously opened capping, convex-variation and welding inputs. No priority is claimed.

A further three queries on hyperbolic capping/isotopy and conformal welding of pants are preserved in `root_toric_descent_search.json` with the measured tool time. They returned general welding and quantum/random-surface results, plus an asymptotic-Teichmüller reduction article, but no statement establishing the raw cap-size invariance under examination. Search results alone were not treated as opened proof sources.

## Audit status change

The new A6 audit identified a separate literal parenthesis in049(b): automatic cyclotomic action at a node requires checking branch interchange. This is recorded as a live proof gate pending the explicit corrected character and counterexample. It is separate from the previously proved graph-recovery and framed-logarithmic statements. The B3 complete37-row scope audit found no new mathematical gap; the phrase “finite R-modules” in Raynaud's theorem was clarified to “R-modules finite as sets”, matching the source's explicit convention.
