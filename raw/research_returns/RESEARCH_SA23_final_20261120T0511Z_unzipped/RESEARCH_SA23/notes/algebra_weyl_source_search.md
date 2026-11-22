# Weyl archival route: exact scope and outcome

Research branch `/root/algebra_letters`, GPT-6 Astra Pro, inherited effort, 20 November 2026. This is a primary catalogue investigation for a dated contemporary reference to the specific Montpellier cote 1 Hilbert trace/genus-zero argument. No such reference has been identified in the sources below.

## Separate 1995 inventory: bibliographic metadata only

The primary IAS finding aid points to ETH's bulk Weyl papers and to DOI **10.3929/ethz-a-000310478**. DataCite's public metadata was retrieved at <https://api.datacite.org/dois/10.3929/ethz-a-000310478>, describing *Hermann Weyl (1885–1955): Verzeichnis der Manuskripte und Korrespondenzen*, ETH Zürich, **1995**, 18 pages, series *Handschriften und Autographen der ETH-Bibliothek* 8. The record calls the publication open access, but provides no content URL. Its media endpoint returned no file link. The public Handle API returns the same Research Collection handle already unsuccessfully opened by the category agent. A single request to ETH's currently documented public OAI Identify endpoint returned HTTP 429 and was not retried. Thus **the 1995 inventory PDF was not read in this branch**.

Scripts and full outputs: `code/algebra_history_weyl21.py`, `weyl22.py`, corresponding JSON/TXT logs; public metadata in `sources/algebra_history_weyl_datacite.json`, `algebra_history_weyl_handle_metadata.txt`, `algebra_history_weyl_datacite_media.txt`. Web queries/source opens are preserved in `notes/algebra_history_web48.json` through `web55.json`.

## Distinct modern ETH catalogue: actually retrieved

ETH's current archive page, <https://library.ethz.ch/sammlungen-und-archive/archivieren/hochschularchiv-der-eth-zuerich.html>, explicitly directs researchers to the public virtual reading room at <https://vls.hsa.ethz.ch/client/> and to e-manuscripta. The virtual reading room's ordinary public search JavaScript was retrieved, and its anonymous metadata search schema used. No account, archive order, access request, protected download or message was submitted.

The exact `Grothendieck` query returned **seven** records, all modern course catalogues (2009–2020), without a correspondence hit. An exact-phrase `Hermann Weyl` query returned **592** records, of which the first 20 were read as a finding aid. The documented call number **Hs 91** resolved to the following public record:

<https://vls.hsa.ethz.ch/client/#/de/archiv/einheit/13c9773a2cb24d548cae7ef1158ef0df>

Its title is **Weyl, Hermann (1885–1955): Briefe**. Both the record metadata and the complete displayed child-list were retrieved. The child-list contains **447 entries**, exactly matching the fonds' `childCount`. All 447 call numbers, titles and public record links are extracted into `notes/algebra_weyl_catalogue_children.tsv`. The complete returned title list was searched for `groth`, `schwartz`, `dieud`, `choquet`, `schauder`, `lids`, `koethe`, `köthe`, `schatten`, `carleman`, `smithies`, `trace`, `spur`, `determin`, `eigenwert`, `fredholm`: all returned zero. This is a complete returned **title-list search**, not an assertion that every letter's content or every possible enclosure has been read.

The fonds' own method note explains that its item/dossier records were retroconverted in **2016–2018** from older library cards and a typescript finding aid, generally without rechecking the physical originals. This source limitation reinforces the distinction between the catalogue result and a claim about all surviving correspondence.

Exact public metadata URLs are saved in `logs/algebra_history_weyl27.json`; raw files:

- `sources/algebra_history_eth_hs91_record.json`, SHA256 `1e3c5a454636e75bbccbc256b6ac296962ba386cdc3e221104686429a0f45a3c`.
- `sources/algebra_history_eth_hs91_children.json`, SHA256 `f9bef57c6c18e8920ea3894c68c6b9388746b4a39f2162f0f4999ce6d738d0bd`.

Retrieval and extraction scripts: `code/algebra_history_weyl23.py` through `weyl28.py`; matching logs retain all requests, responses, hashes, exact timings and the extraction checks. The initial public search-client resource URL was resolved literally from the returned HTML and returned JavaScript successfully; no hidden or private API was used.

## Hs 91a mathematical-material branch

The first Weyl search page also supplied the separate public Hs 91a fonds:

<https://vls.hsa.ethz.ch/client/#/de/archiv/einheit/4511846b9bd34adba98356cda7a42e59>

Title: **Weyl, Hermann (1885–1955): Materialien zum Werk**. Its ten top-level subdivisions were retrieved, and three relevant displayed child lists were read in full at the catalogue level:

| Subdivision | Returned title entries | Exact coverage |
|---|---:|---|
| Diverse Manuskripte aus den Jahren 1909–1955 | 16 | Hs 91a:1–15, including the separately catalogued 4a; no identified Grothendieck or Hilbert trace/genus-zero manuscript title |
| Literaturauszüge, Notizen, Zeichnungen | 11 | Hs 91a:74–84; includes three generically titled note folders, so the titles cannot exclude an unindexed relevant note |
| Fremdmanuskripte | 2 | Hs 91a:88–89, both Rabi nuclear-physics manuscripts catalogued ca. 1927/1927 |

The other seven Hs 91a subdivisions were **not** individually opened. No complete original-file inspection or complete fonds exclusion is claimed. Scripts `code/algebra_history_weyl29.py`, `weyl30.py` and matching logs preserve these exact primary metadata responses.

The three generically titled folders Hs 91a:79, :83, :84 were then retrieved in one ordinary public `GetEntities` metadata request. The returned compact records provide no `contains` description or primary-data/manifest link and no children. They therefore remain content-unidentified; no conclusion about an unindexed proof or enclosure inside them follows. Exact request, response, hash and timing: `code/algebra_history_weyl31.py`, `logs/algebra_history_weyl31.json/.txt`, `sources/algebra_history_eth_weyl_note_records.json`. This compact response was not described as a complete original-file inspection.

## Other Swiss public search

The actual public e-manuscripta query <https://www.e-manuscripta.ch/search/quick?query=Grothendieck> returned no results. Its response is preserved in `sources/algebra_history_emanuscripta_grothendieck.html`; retrieval and hash in `logs/algebra_history_weyl23.json`. This is an exact-query result, not a claim that no relevant physical correspondence exists.

## Consequence for Lead 6

No documentary date for the actual cote 1 proof is supplied by this branch. The result is a bounded negative for the identified public catalogue routes, with the original Weyl letters and generically described note folders unexamined. It does not create a new condition for the already established 1959 witness to the 1955 memoir's announcement. It also does not infer historical priority, authorship of a proof, or an identity for Montpellier's catalogue letter from thematic resemblance or catalogue adjacency.
