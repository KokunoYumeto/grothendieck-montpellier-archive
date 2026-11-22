# Pfluger1960: bounded independent public journal/offprint route

Date: 19 November2026,16:34–16:38UTC. Researcher: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode, agent `part_c_algebra`.

## Outcome

The exact original remains **NOT OPENED**: Albert Pfluger, *Ueber die Konstruktion Riemannscher Flächen durch Verheftung*, Journal of the Indian Mathematical Society(N.S.)24(1960),401–412, issued1961. No mathematical theorem or named-source status changes. The parent's phrase “Konforme Verheftung” was confirmed in a message as shorthand; no bibliography correction is needed. This search never treats Huber's similarly titled papers or the1988 birthday volume as the requested original.

The distinct route was a curated institutional digital-journal registry → an actual HathiTrust catalogue link, together with an independent French mathematics-library serial registry and an IITBombay print-journal catalogue. The new returned author/offprint searches supplied no advertised target file. The bounded route is now stopped. These results do **not** prove that no public copy exists elsewhere.

## Prior coverage read before searching

I read `notes/part_a567_pfluger_offprint_audit.md`, `notes/part_b_pfluger_jubilee_catalogue_audit.md`, and the Pfluger portions of `notes/root_original_followup_03.md`, and inspected the saved publisher, YMSC, repository-metadata, ETH, and NDLI outputs. The publisher subscription refusal; IA182metadata/166OCR; TDL ordinary inventory, separate1959issue and date filters; IISc; NDLI; ETH finding aid; Eremenko indexes; and generic Jubilee title searches were not retried. The initial combined note display exceeded its output budget; the two audit notes were subsequently read separately in full and the root note was read through the targeted Pfluger passages. No reading is claimed from truncated portions alone.

## New public pages and exact access outcomes

1. University of Pennsylvania's Online Books Page, `https://onlinebooks.library.upenn.edu/webbin/serial?id=jinmathsoc`, was first returned by search and then obtained through one ordinary HTTP request. HTTP200;4134bytes;SHA256 `21ab74e03ecca0e591f29b1eda417b70e1025649fccfd80271d5afa83f7e5d74`. Its actual catalogue text advertises freely readable1909–1930volumes1–18, says later issues can be search-only, and gives the actual Hathi record below. It does not advertise a public1960article. Its IA1929supplement link was recognized as outside scope and not followed. The original journal's copyright/history statements are catalogue metadata, not a licence or an article reading.
2. The actual advertised link `https://catalog.hathitrust.org/Record/008320850` returned **HTTP403 with a managed challenge**,6069bytes. The request stopped there. No viewer, alternate API, challenged session, altered headers, mirror, page image or private asset was requested. The result does not identify the holdings inside that record; the UPenn description and this failed catalogue request have different evidentiary scopes.
3. Mathdoc/PCMath's actual institutional serial record, `https://cfp.mathdoc.fr/periodique/4527/`, opened as web text: `turn600635867view2`. Lines22–33 list only the existing publisher route and Iasi's1934–1948open-access collection. Lines38–180 list physical holdings, including1960volumes at several libraries, with binding/condition/shelf information. Those are print holdings, not digital-original availability. In particular Orsay's1960entry is in the **lacunes** column, so it is not recorded as a confirmed holding. Neither the already attempted publisher nor the out-of-period Iasi route was followed again.
4. The actual IITBombay archive URL, `https://www.library.iitb.ac.in/print-journals/journals-archive/`, was returned with an indexed “Print Journals Archive” listing identifying JIMS1960+24+. The web open timed out; one ordinary request returned **HTTP503**,98bytes, upstream connection failure. It was not retried. The indexed snippet is only print-holdings metadata; no catalogue body, offprint, scan or mathematical page was obtained through that request.

No original or substitute PDF was requested or downloaded in this audit. There were no contacts, accounts, purchases, private files or access-control workarounds.

## Search scope and saved outputs

Four search batches contain **14queries**. Their exact strings and complete returned results are in `code/part_c_pfluger_distinct_search1.json` through `search4.json`:

- Batch1(system1,4queries): target/HathiTrust; original journal1960/digital excluding earlier publisher/IA/TDL sites; the parent's shorthand title; page-range/reprint. Returned the IITBombay print list, Mathdoc serial record, later citations and the1988birthday volume.
- Batch2(system2,3queries): journal title at HathiTrust; title across selected institutional/offprint domains; Sonderdrucksammlung/offprints. Returned no results. This is a weak-engine result for those exact queries, not an exhaustive catalogue inventory.
- Batch3(system1,3queries): HathiTrust/journal; Pfluger/Sonderdrucksammlung; exact work with digitized/scan/download terms. Returned the useful UPenn registry and physical holdings, but no target original. Its same tool call also attempted the Hathi catalogue homepage, which was not accessible through the web tool. The later ordinary request used the actual UPenn-advertised record, not a guessed storage path.
- Batch4(system1,4queries): Helsinki offprint context; non-ETH Nachlass; original journal1960with digital/PDF terms and earlier sources excluded; exact author/page range with filetypePDF. Returned later citations, bibliographical history and the already known birthday volume; no new target file. These negative discovery results are not a claim to have inventoried those institutions.

The separate three-page web-open output is `code/part_c_pfluger_distinct_open1.json`. Useful ref IDs are `turn246232712search0`(UPenn), `turn842200559search0`(IITBombay indexed metadata), and `turn600635867view2`(actually opened Mathdoc text). Other returned refs are preserved in the raw JSONs. No mathematical claim relies on the secondary citation results.

## Exact request counts and measured runtimes

The audit used **5web-tool invocations**:4search batches containing14queries, plus one three-page-open invocation. There were4explicit web opens in all: the Hathi homepage plus UPenn/IITBombay/Mathdoc. Tool-internal network/cache counts are not known and are not inferred from this count.

| Saved call | StartUTC | Measured elapsed |
|---|---|---:|
| `part_c_pfluger_distinct_search1.json` |16:35:30.058|1.284s|
| `part_c_pfluger_distinct_search2.json` |16:35:39.629|0.375s|
| `part_c_pfluger_distinct_search3.json` |16:35:45.487|1.185s|
| `part_c_pfluger_distinct_open1.json` |16:35:51.252|5.657s|
| `part_c_pfluger_distinct_search4.json` |16:37:35.897|1.088s|

These are actual `Date.now()` intervals around the awaited tool calls, including any service caching; they are not estimates of remote crawler work or total research time.

The saved utility `code/part_c_pfluger_distinct_public_route.py` ran **three times**, making one ordinary public GET each, with zero retries:

| Output file suffix | StartUTC | HTTP | Measured request/processing elapsed |
|---|---|---:|---:|
| `upenn_output.json` |16:36:30.797204|200|5.775041263004823s|
| `iitb_output.json` |16:36:30.797999|503|10.017750553000951s|
| `hathi_record_output.json` |16:36:46.667627|403|5.847043253001175s|

Each full filename begins `code/part_c_pfluger_distinct_`; the output preserves exact URL, status, date, elapsed interval and obtained body/links. Only UPenn's ordinary HTML body was saved in `sources/`. No mathematical finite check, certificate, OCR or source-page rendering was run.

## Remaining gate

The requested1960original mathematical statement/proof has not been accessed. Its gate remains open independently of the already proved welding results and the opened Lehto–Virtanen and Huber–Kühnau originals. The bounded newly advertised institutional route is exhausted without an original-content link. Further work would need a genuinely new public copy or preview; repeating the stopped catalogues is not warranted by these results.
