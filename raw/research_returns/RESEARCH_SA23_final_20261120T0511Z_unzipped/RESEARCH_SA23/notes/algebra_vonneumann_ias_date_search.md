# Bounded von Neumann / IAS / Princeton correspondence route

Branch `/root/algebra_letters`, GPT-6 Astra Pro, inherited effort. Started at root's request shortly after 03:03 UTC, 20 November 2026. Objective: a publicly documented 1950–1958 Grothendieck correspondence item or separately described enclosure that identifies the Montpellier cote 1 Hilbert trace/genus-zero argument. **No such item has yet been identified.** No bibliography or mathematical section was changed for this branch.

## Princeton C1245: complete public finding-aid metadata read

The official collection index <https://findingaids.princeton.edu/pacscl/production> was opened and downloaded. Its exact link for the John Von Neumann Collection is:

<https://findingaids.princeton.edu/pacscl/production/C1245.xml>

That complete EAD was downloaded successfully and its collection description, scope, access statement and all container titles/dates read. It describes **29 letters to Gábor Szegő**, grouped as six letters in 1919–1920, nine in 1921–1928, and fourteen in 1933–1941. The other described substantive items are a MADDIDA lecture typescript (container date 1950; collection scope separately refers to a 1949 presentation), and a copy of a 1966 Princeton Alumni Weekly article. The two dates for the lecture are retained as the finding aid prints them, not silently harmonized. No Grothendieck correspondence or relevant enclosure is described in this bounded collection. **These are catalogue metadata; no original letters were read.**

Raw EAD: `sources/algebra_history_princeton_vonneumann_C1245.xml`, 16,167 bytes, SHA256 `19f442bbda8e99466edea81da22175e676b467c4f57a2750226ca6b2e24219a1`. Readable extraction: same basename `.txt`. Exact retrieval/extraction script `code/algebra_history_ias33.py`; outputs `logs/algebra_history_ias33.json/.txt`, 4.082241 seconds. The initial Princeton index and its exact link are preserved by `code/algebra_history_ias32.py`, matching logs, and `sources/algebra_history_princeton_collection_index.html`.

## Library of Congress MSS44180: access failure, not an inspected inventory

Search identified the official finding aid *John Von Neumann and Klára Dán Von Neumann Papers*, MSS44180:

<https://findingaids.loc.gov/repositories/19/resources/2207>

The web-reader open returned **HTTP 403**. Per the task's access instruction, this route was stopped; no alternative restricted endpoint or login was attempted. The search result describes broad correspondence holdings but is not a substitute for reading the complete finding aid. Thus this branch does **not** infer that the LOC papers lack a Grothendieck item. Exact search and failed open are in `notes/algebra_history_web57.json` and `web58.json`.

## IAS public holdings and exact limits

The official current collections page <https://www.ias.edu/library/archives/collections> was opened in the web reader. It advertises Director's Office Faculty and Members records, School of Mathematics records and several mathematicians' papers. The linked old Members and Faculty finding-aid URLs returned 404, and their corresponding public handle pages returned “No item found”; these are stale-link results, not an examined finding aid. Direct downloads of the IAS homepage and the Electronic Computer Project finding aid returned 403 and were not retried. Those failed responses and timings are preserved by `code/algebra_history_ias32.py`, `logs/algebra_history_ias32.json/.txt`. No access-controlled original was requested.

One independently indexed public IAS PDF **did open successfully in the web reader**:

<https://albert.ias.edu/server/api/core/bitstreams/4ec15dd0-10ee-44e8-93fa-c3816b1c801f/content>

This is a **42-page file concerning Lars Hörmander**, containing mixed dates. The target Grothendieck hit is in its last two physical PDF pages (41–42): a typed copy of an **A. Weil letter dated 31 October 1957**, beginning “Dear Marston”. The extracted text was read in context. It discusses appointments, Hirzebruch and Grothendieck's Riemann–Roch work, and asks why Grothendieck has not been invited to the Institute. It does **not** identify a Hilbert trace or genus-zero draft. This source cannot be used to infer that Grothendieck had no earlier contact with von Neumann or IAS mathematicians.

Scope flag: the original scan PDF was opened and its extracted relevant text read; it was **not** locally downloaded or fully visually collated. Screenshot requests for physical pages 41–42 returned only text placeholders through this web tool, so they are not counted as successful visual inspection. The other forty pages were searched as a finding aid, not read line by line. Raw open/find/screenshot outputs are in `notes/algebra_history_web61.json` through `web63.json`.

## Exact query and output record

Raw request-plus-response JSON is preserved in `notes/algebra_history_web56.json` through `web64.json`:

- Initial von Neumann/Grothendieck, LOC and Princeton correspondence queries.
- Stronger primary-domain queries locating LOC MSS44180, IAS collection descriptions and Princeton's actual public collection index.
- Actual source opens and stale-link responses for IAS Members/Faculty finding aids.
- Exact Princeton C1245 link identification from its downloaded official index.
- The public IAS PDF's Grothendieck, date and trace-word context checks.
- Targeted 1955/1958 IAS and Members-finding-aid queries, which produced no additional relevant correspondence item.

The physical date of the cote 1 argument remains unestablished by this route. This bounded result is not an assertion that no such correspondence survives elsewhere or that an unnamed enclosure is absent from unexamined files.
