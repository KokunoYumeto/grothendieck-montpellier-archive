# Lehto–Virtanen original-source follow-up

19 November 2026, 13:50–13:55 UTC. Independent reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode.

## Current outcome

The requested 1973 Lehto–Virtanen book remains **not opened in mathematical full text**. This is a named-source delivery gate, not a new mathematical gap in the already proved welding statements. No theorem from an unseen book has been made a premise. The additional checks below exhaust this bounded follow-up; negative catalogue results are not a claim that no public copy exists anywhere.

The earlier access findings remain in notes/root_original_followup_03.md and code/root_lehto_catalogue_output.json. In particular, the current English and German Internet Archive records mark their PDFs and OCR private. Those protected downloads were not retried.

## Public catalogue and author routes actually checked

1. The official HEAL-Link historical Springer complimentary-access list was opened at https://www.heal-link.gr/librarians_files/dcnts/Springer_eBooks_Complimentary%20Access.pdf (web turn998729578view2). Searching the exact electronic ISBN 9783642655135 produced no match (turn445910469view3). The similarly titled entry on printed p.1389 is the **different** 1983 Ławrynowicz–Krzyż book, ISBN9783540394648 (turn445910469view2). The catalogue's historical temporary-access announcement is not treated as present access authorization.

2. Google Books editions fEDvAAAAMAAJ, cI8_AQAAIAAJ and wjzvAAAAMAAJ were followed through ordinary edition links. The opened records provided snippet views or inaccessible redirects, not book mathematical pages. References: turn998729578view1, turn445910469view0–1. No preview restriction was circumvented.

3. Five public Wayback CDX catalogue requests tested the ordinary Springer PDF URL, its encoded-slash variant, the historical Springerlink ISBN path, and current publisher/CDN ISBN patterns. All five returned HTTP200 and empty JSON arrays. These were catalogue queries only; no unadvertised capture was invented or downloaded. Exact URLs, response hashes, and timings are saved in code/part_c_lehto_public_archives_output.json.

4. A public OpenLibrary result pointed to the older identifier quasiconformalma00leht, different from the already checked quasiconformalma0000leht. Its metadata endpoint returned is_dark=true and no file list. The check stopped at that public metadata response. No file was requested.

5. The Finnish Academy original publication list, https://www.acadsci.fi/mathematica/Vol10/vol10pp00V-0XI.pdf, was opened and downloaded. Its 1973 entry on printed p.IX (PDF p.5) identifies the second English edition, translated by K.W. Lucas, Grundlehren126, VIII+258 pages, ISBN3-540-06093-6. This is direct bibliographic evidence **only**, not mathematical access to the book. The list also distinguishes the German1965 book and the different short1966 congress lecture. Web reference turn533556228view0; local sources/part_c_lehto_author_publication_list.pdf, SHA256 8a0dde1a401fc10df8afe54714ea832329764b92b469928e0d57af0411cf1fd7, 7,412,414 bytes.

6. New searches used the exact title, both authors, the original print ISBN, Helsinki institutional terms, McMullen's Harvard site and Vuorinen/Turku terms. Results were catalogues, later citing papers, and course notes. A concrete new reading-list lead was Christopher Bishop's public Spring2025 MAT627 page, https://www.math.stonybrook.edu/~bishop/classes/math627.S25/ (turn984576677view0). Its advertised Lehto–Virtanen link23 was actually followed: it leads to the Springer print metadata page https://link.springer.com/book/9783642655159 (turn650185118view0), without mathematical preview pages. The page describes its book links as mostly publisher links. Its freely available Bishop notes and other authors' books were not misidentified as the requested original.

7. The Springer print record itself is open as metadata (turn755262743view0). It labels the reprint first edition and VIII,260 pages, whereas the Finnish Academy publication list labels the 1973 English original second edition and VIII+258 pages. No conclusion about an unseen book's exact mathematical pagination is drawn from this catalogue discrepancy. The manuscript's second-edition bibliography remains consistent with the contemporary author publication list.

The exact electronic DOI remains 10.1007/978-3-642-65513-5; the incorrect final digit0 from an earlier run was already corrected by root.

## Actual program scope and timing

| Program | Scope | Count | Runtime | Outcome |
|---|---|---:|---:|---|
| code/part_c_lehto_public_archives.py | Public catalogue/bibliographic retrieval only | 7 ordinary HTTP requests: 5 CDX, 1 public metadata, 1 publication-list PDF | 12.661742126 s | All HTTP200; five empty capture lists, one dark metadata record, one 7-page bibliographic PDF |

The run began 2026-11-19T13:53:49.006674+00:00. Every request has a separate timing and hash in the JSON output; exact stdout is in the matching .txt file. The program never requested a full Lehto–Virtanen book PDF or a private file. Web search/open/click operations are separately identified above and are not counted as numerical verification.

## Effect on coverage

ALehtoVirtanen1973 remains NOT OPENED. The existing original Beurling–Ahlfors and Bishop proofs and the manuscript's direct arguments are unchanged. This follow-up does not close the literal instruction to fetch the named Lehto–Virtanen source.

## Additional public-copy check, 13:58–14:00UTC

Root clarified that a publicly accessible third-party scan may be read for this authorized research, while access controls must remain intact and whole copyrighted books must not be redistributed. No ordinary public direct Lehto copy had been found and excluded solely for its host. Nevertheless, searches were broadened without publisher/institutional restrictions and included PDF, DjVu, the exact title, both authors, and ordinary public reading collections.

The resulting booktracker listing identifies a258-page Lehto–Virtanen DjVu in a large book inventory (turn427829009search24–25); it does not itself expose the mathematical pages or an individual direct book link in the retrieved result. A separate public directory at https://ebooks.karbust.me/Mathematics/ was actually opened (turn772902828view0). It contains200 advertised PDF entries; the only Lehto entry is the different1987 Univalent Functions and Teichmüller Spaces, and no Virtanen entry exists (turn873444553view1–2). The public parent directory has only Mathematics and Technology. The old Nikita Danilov link index was also opened; no Virtanen entry was found (turn772902828view1, turn873444553view3). The independent Part A reviewer likewise reported no Lehto entry there and owns the separate Birman link follow-up.

SciSpace's ordinary public book page was opened through the web tool (turn329840990view0). Its Get PDF text has no exposed book hyperlink, while separate PDF links belong to other cited articles. To check the public HTML itself, code/part_c_lehto_public_page.py made exactly one ordinary request. It returned HTTP202 with a zero-byte body in7.494104414s, started2026-11-19T13:59:29.018756+00:00. No service API, private endpoint, challenge workaround or PDF request followed. Complete output is saved in the matching JSON and TXT files. This did not retrieve an original page.

No mathematical-text access has been gained by these additional routes. The NOT OPENED status remains accurate as of14:00UTC.

## Distinct translation and ISBN route, after14:00UTC

At root's request, new searches used the Russian author spellings Лехто/Виртанен, both Квазиконформные отображения and Квазиконформные отображения плоскости, translation and download terms, and possible Japanese/Chinese edition terms. Both search engines were used because the routine engine's Russian coverage was poor. The Russian Academy biography (https://new.ras.ru/academy-new/staff/inostrannyy-chlen-ran/lekhto-olli/, turn981107295search0) uses a translated Russian book title, but supplies no Russian publisher, translator, or edition. It is not evidence that a Russian translation was published. The later Russian research papers found continue to cite the1973 English or1965 German work. The Japanese Kyoto Sangyo catalogue (turn480230789search2) explicitly identifies the1973 English translation by K.W. Lucas, not a Japanese translation. No alternate-language mathematical text was found; no claim is made that none exists.

Additional queries for ISBN9783540060932,0387060936 and3540060936 led to the public booktracker inventory https://booktracker.org/viewtopic.php?t=9503. This page was actually opened (turn722966617view0). Its listing includes a Lehto–Virtanen PDF filename, but exposes no individual direct book download or mathematical pages. It is an inventory of1000 different books, not a reading of the requested book. No bulk transfer, torrent transfer, registration or other account operation was performed. This metadata lead does not close the source requirement.

These follow-up web searches and opens ran without additional local retrieval scripts. The public sources listed above were inspected only for identity/access, and no mathematical theorem in the manuscript relies on them.
