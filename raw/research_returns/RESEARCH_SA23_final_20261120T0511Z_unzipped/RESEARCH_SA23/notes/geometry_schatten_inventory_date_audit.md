# Robert Schatten: bounded Hunter College / CUNY inventory check

Completed 2026-11-20T04:55:37.101197+00:00. Existing statements: `geo-H-history`, `SA23-49`.
This is a documentary source-use check, not a mathematical proof.

## Result and exact scope

No opened public catalogue description names a Robert Schatten personal
collection, a Grothendieck correspondence file, or a dated enclosure
identifying the particular cote 1 trace/genus-zero proof. The official
Hunter academic-department page does identify a general **Mathematics &
Statistics Department, 1908–1954, 1971** collection, described as annual
reports, by-laws, correspondence and selected personnel files. It gives
no item-level Schatten or Grothendieck identification, and that entry has
no linked detailed finding aid on the opened page. Its underlying records
were not inspected.

The complete **19-entry Faculty Papers/Collections section** of Hunter's
public finding-aid page was read, including all collection descriptions.
No Schatten entry appears there. The complete returned HTML texts of that
page, the academic-department page and the CUNY archives guide were also
searched for `schatten` and `grothendieck`: each returned zero. These are
bounded checks of public pages, not an inventory of unprocessed holdings
or proof that a relevant collection cannot exist.

## Official pages actually opened and preserved

1. **Hunter finding aids**:
   <https://library.hunter.cuny.edu/archives/finding-aids>.
   Its introductory scope distinguishes processed collections with finding
   aids. The entire Faculty Papers/Collections section was read from both
   the web return and the preserved text. The 19 named collections are
   Haft, Hill, Hyslop, Hahn, Luetz, Lewis, Cone, Cox, Landers, Gold, Farrell,
   Fuller, Ferguson, Morgan, Brenner, Pomeroy, Kennedy, Roberts and Schor.
   Landers's description concerns professional/faculty-organization
   records, not a named Schatten mathematical archive. Other unrelated
   underlying folders were not opened.
2. **Hunter academic departments**:
   <https://library.hunter.cuny.edu/archives/collection-categories/academic-departments>.
   The complete returned department listing was read, including the
   Mathematics & Statistics entry and its exact date range/scope above.
   This is a distinct public category page; its contents were not silently
   treated as identical to the main finding-aid page.
3. **CUNY archives guide**:
   <https://guides.cuny.edu/archives/>.
   The Hunter and Graduate Center scope paragraphs and their actual
   advertised finding-aid links were read. The Graduate Center describes
   institutional records and a small number of donated manuscript
   collections; it identifies no Schatten manuscript in those paragraphs.
   This is a guide to repositories, not a complete item-level inventory.

Each of these three ordinary public HTML preservation requests returned
HTTP200. Exact URLs, final URLs, byte counts, SHA256 values and the
case-insensitive name-search counts are in
`logs/geometry_schatten_catalogue_fetch.json`. Raw HTML and extracted
finding-aid text are under `sources/geometry_schatten_*`; the actually read
faculty section is also retained as
`sources/geometry_schatten_hunter_faculty_section.txt`.

## Advertised portals that could not be opened

The CUNY guide links the Hunter and Graduate Center searchable archives at
<https://archives.library.hunter.cuny.edu/> and
<https://archives.library.gc.cuny.edu/>. Each first web-reader opening
reported **Failed to fetch restricted URL**. These routes were stopped:
no local request, alternate endpoint, account, form submission or access
workaround was attempted. No search result or absence claim is attributed
to either unopened portal.

## Search and duplication boundaries

Nine actual search-engine queries are preserved in
`notes/geometry_schatten_inventory_web01.json` through `web04.json`, along
with all actual opens, clicks and finds. They cover the exact name with
Hunter/archive/papers, CUNY correspondence, and the two official archive
domains. Returned references to memorial prizes and unrelated people
named Schatten were not treated as correspondence. An IAS catalogue hit
was not followed because that source family and its access limits were
already recorded by the team. The Kansas/Aronszajn branch belongs to the
category agent and was not duplicated here.

Before searching, local source/date notes were checked. Algebra's earlier
Schatten1960 book-preview route and root's modern biography / NBS route
are separate actual approaches; their publications were not reread here.
The bank-safe recollection supplied only the reason to look for a public
collection. It supplies no current repository or identification of these
particular leaves, and was not used as a manuscript-date witness.

## Reproducibility and remaining next step

`code/geometry_schatten_catalogue_fetch.py` made the three independent HTML
requests in parallel, taking 9.334941880006227 seconds. The initial
dependency-based invocation failed before any HTTP request because the
`requests` module was unavailable; its source/output are retained as
`geometry_schatten_catalogue_fetch_attempt01.py` and the matching log. The
successful revision used only standard-library urllib and HTMLParser.
No request was retried after a denial.

`notes/geometry_schatten_inventory_query_manifest.json` links all actual
query records and the successful preservation log. This recording program
adds only documentary events and route-table rows; it does not modify the
paper or bibliography. The date gate remains unchanged. A public
item-level accession record or original dated communication identifying
the actual proof or its enclosure would be needed to advance it. Generic
departmental dates and the absence of a name from a public faculty list
cannot supply that identification.

Source-cache relocation: the raw faculty-section excerpt was moved unchanged from its initial `notes/` path into `sources/`; exact old/new path and hash are preserved in `logs/geometry_schatten_excerpt_relocate.json`. The actual executed retrieval program and its initial output remain unchanged as historical records.
