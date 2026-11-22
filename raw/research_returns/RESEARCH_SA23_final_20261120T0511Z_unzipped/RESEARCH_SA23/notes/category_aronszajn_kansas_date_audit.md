# Aronszajn and Kansas public archival descriptions: bounded dating audit

## Result and scope

Completed 2026-11-20, approximately 04:51–04:58 UTC. This route located a relevant primary archival holding, the **Personal Papers of Nachman Aronszajn, PP 236**, but did not identify a dated Grothendieck proof, enclosure, or the Montpellier cote 1 trace/genus-zero leaves. It also inspected the public catalogue of the related G. Baley Price papers. **Catalogue metadata was read; no original Aronszajn or Price letter or manuscript was opened.** The date of the particular Montpellier leaves remains unproved. The absence of a named item from coarse box descriptions does not establish its absence from the physical papers.

No contact, account creation, reading-room request, or access to restricted material was attempted. The paper and bibliography were not changed.

## 1. Aronszajn: the actual public holding

The official University of Kansas Kenneth Spencer Research Library collection page was opened and read:

<https://archives.lib.ku.edu/repositories/3/resources/11>

It identifies **PP 236**, five boxes/five linear feet, with collection dates **1951–1977**. Its five child descriptions were all opened and read. The correspondence child descriptions give the different range **1948–1976**, which is retained here rather than silently reconciled with the collection-level dates.

| Public record | Description and physical locator | Reading status |
|---|---|---|
| <https://archives.lib.ku.edu/repositories/3/archival_objects/40> | Correspondence A–J, 1948–1976, Box 1 | Complete public description read; originals not read |
| <https://archives.lib.ku.edu/repositories/3/archival_objects/41> | Correspondence K–M, 1948–1976, Box 2 | Complete public description read; originals not read |
| <https://archives.lib.ku.edu/repositories/3/archival_objects/42> | Correspondence N–Z, 1948–1976, Box 3 | Complete public description read; originals not read |
| <https://archives.lib.ku.edu/repositories/3/archival_objects/43> | Publications and index, Box 4 | Complete public description read; originals not read |
| <https://archives.lib.ku.edu/repositories/3/archival_objects/44> | Notes and documents, Box 5 | Complete public description read; originals not read |

The website's advertised public tree request was derived from its saved application JavaScript, not from a private interface. The response at <https://archives.lib.ku.edu/repositories/3/resources/11/tree/root> confirms five children, each with `child_count: 0` and `has_digital_instance: false`. Thus this public tree does not supply an item-level correspondent list or digitized letters. The collection page explains that the papers are stored at the KU Annex offsite, with advance arrangements needed for physical consultation. This is a limit on the material actually read, not a claim that no Grothendieck correspondence exists.

Saved tree: `sources/category_aronszajn_aronszajn_root.json`, SHA256 `a01c143f9e80b6206a837947fb5a3001dbe688cbf3a67f136d0aa1c6bad97b18`. All five child descriptions and the collection opening are preserved in `notes/category_aronszajn_kansas_web01.json` through `web10.json`, with the exact requests and responses. Native collection/notes HTML and retrieval logs are separately retained under `sources/category_aronszajn_*` and `logs/category_aronszajn_*`.

## 2. Public search behavior: not a certified absence result

The actual anonymous search forms were inspected before use. An ordinary native archive query for **Aronszajn** returned two catalogue results, the collection and its person authority record. The ordinary query for **Grothendieck** redirected to a reset search form without an explicit result count. Consequently, it is **not** recorded as a certified zero-result search. A collection-filter attempt likewise reset to the unfiltered collection listing; its five records do not constitute a Grothendieck search result.

The archive's advertised digital-library route led through the university library page to <https://digital.lib.ku.edu/islandora/root>. The public collection list and the first page of University Archives Records were opened. Anonymous POST submissions using the actual public search form for Grothendieck and Aronszajn each returned 404. That route was stopped. These failures do not prove an absence from KU's digital holdings. General search-engine results were also used for discovery, but irrelevant results and ignored domain filters are not treated as evidence of absence.

Exact native request/response/status records are in `logs/category_aronszajn_catalogue_queries.json` and `logs/category_aronszajn_public_searches.json`, with matching program sources and output logs. The initial `category_aronszajn_catalogue_fetch.py` failed at import (`bs4` unavailable) before fetching anything; that failed program and its output were preserved, and the subsequent stdlib-parser version is separately named.

## 3. Price: complete public title inventory and targeted descriptions

The related holding is **Personal papers of G. Baley Price**, PP 362 and PP 523:

- Collection: <https://archives.lib.ku.edu/repositories/3/resources/3239>.
- Public organization: <https://archives.lib.ku.edu/repositories/3/resources/3239/collection_organization>.

The collection and organization pages were opened. Their actual public “load all records” mechanism advertised fourteen waypoints. All fourteen were retrieved through the same public endpoint and advertised URI lists used by the website. They contain **263 distinct catalogue records, including the collection record**. All 263 titles were actually read in four manageable displayed batches. The complete supplied metadata text was also searched for `Groth`, `Arons`, `Fredholm`, `genus`, `trace`, `tensor`, `Hilbert`, and `eigenvalue`, without a match. This is a statement about these supplied metadata fragments, not about the original papers or an unseen detailed index.

The particularly plausible catalogue descriptions were read in full as supplied, and four were additionally opened as individual record webpages:

| Record | Relevant public description | Actual scope |
|---|---|---|
| 127497, 127498 | Class, lecture, and research notebooks, Boxes 5 and 6 (PP 362 series) | Complete supplied waypoint text read; no notebooks read |
| 127500 | Education and teaching at named institutions including Kansas, Box 7 | Waypoint text and complete individual webpage read; no documents read |
| 127538 | Price's 1976 history of the mathematics department, 1866–1970 | Bibliographic catalogue entry read; book not read |
| 127639 | Correspondence concerning that department history, PP 523, Box 1, Folder 96 | Waypoint text and complete individual webpage read; no letters read |
| 127648, 127649 | Department history, Box 2, Folders 1–4; faculty/Ephraim Miller, Folder 5 | Complete supplied waypoint text read; originals not read |
| 127650, 127651 | Department history/faculty, PP 523, Box 2, Folders 6–8 and 9–14 | Waypoint text and complete individual webpages read; originals not read |

Individual URLs have the form `https://archives.lib.ku.edu/repositories/3/archival_objects/` followed by the record number. The four individually opened pages have no fuller correspondent description or target enclosure identification beyond the stated box/folder metadata. The machine keyword result was not substituted for reading these targeted descriptions.

The official department history page, <https://math.ku.edu/history-1866-1970>, was opened as a possible route to the 1976 book. Its advertised repository link, <https://kuscholarworks.ku.edu/handle/1808/29639>, failed in the web reader with a timeout. No book content was read, and no claim about its contents is made. The general career narrative was not used to assign a date to the proof.

Saved evidence:

- `sources/category_aronszajn_price_wp_00.json` through `_13.json` and corresponding native text files: all fourteen public waypoint payloads.
- `logs/category_price_public_inventory.json`: exact URLs, UTC retrieval times, SHA256 hashes and counts for the Aronszajn tree and all Price waypoint responses.
- `notes/category_price_inventory_titles.tsv`: all 263 unique URIs and titles actually read.
- `notes/category_price_inventory_contexts.json`: exact keyword scope, no-hit result, counts and fourteen source hashes.
- `notes/category_price_selected_record_contexts.txt`: full supplied text of the nine selected descriptions.
- `notes/category_aronszajn_kansas_web11.json`: complete individual-record openings for 127639, 127650, 127651 and 127500.
- `code/category_price_inventory_reading_aid.py` and `code/category_price_selected_record_contexts.py`, with their complete outputs in the correspondingly named `logs/*.txt` files.

## 4. Smallest remaining date requirement

This route establishes the existence and public description of potentially relevant physical holdings. It does not establish that they contain the trace proof, and it does not date that proof. A dated original letter or enclosure explicitly identifying the particular argument or leaves, a dated duplicate, or an equally precise primary archival cross-reference would still be required. A 1954–55 Kansas visit, a collection date range, or an undifferentiated correspondence box cannot supply that identification. No task-level gate changed.

## Addendum, 04:59 UTC: exact advertised Price book link

With the parent's instruction to follow this one concrete public link, ordinary retrieval of <https://kuscholarworks.ku.edu/handle/1808/29639> was attempted once. It returned **HTTP 404**, with no redirects. No book bytes, metadata page, or original-text passages were obtained. This supplements the earlier web-reader timeout; neither result is a finding about the book's contents. The route was stopped without alternate endpoint probing, accounts, or contact.

The initial local program `code/category_price_history_public_handle.py` failed to import the unavailable `requests` module **before making any network request**; its complete failure output is preserved. The separately named stdlib program `code/category_price_history_public_handle_v2.py` made the sole ordinary retrieval. Its timestamp, exact URL, empty redirect list and HTTP404 result are saved in `logs/category_price_history_public_handle_v2.json` and `.txt`. The history book remains **unopened**, and the task-level date gate is unchanged. No paper or bibliography edits were made.
