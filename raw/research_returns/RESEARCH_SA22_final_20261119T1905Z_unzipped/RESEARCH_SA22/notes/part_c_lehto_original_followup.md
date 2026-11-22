# Lehto–Virtanen original-source follow-up

19 November 2026, 13:50–14:15 UTC. Independent reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode.

## Current outcome

The requested 1973 Lehto–Virtanen book is now **OPENED in original mathematical full text**. A distinct ordinary public catalogue route, detailed below, supplied the correct second English edition. The title/copyright pages and printed81,83,85,88,92–95,100 were visually read. The exact relevant statements and their proofs were read from the original. The source-delivery gate is closed; the earlier negative searches below remain a chronological audit, not the present outcome.

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

## Effect on coverage at13:55UTC, superseded by the14:15 opening below

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

## Successful public catalogue route and rejected candidate,14:06–14:15UTC

The Part A reviewer found the ordinary public catalogue https://libcats.org/ and its advertised author-search route. The actual public searches https://libcats.org/g/Lehto and https://libcats.org/g/Virtanen both returned HTTP200. Their saved HTML advertises https://libcats.org/book/1088544 and https://libcats.org/book/548781. Both actual book pages were requested normally and returned HTTP200. The first identifies the second-edition Lehto–Virtanen DjVu; the second has the Lehto title but an inconsistent description of a numerical-computing textbook. No source status was assigned from those labels.

The actual advertised link https://libcats.org/dl/1088544/c81b4b returned HTTP200 after its ordinary redirect. It supplied3,275,089bytes, valid DjVu format, MD5 ddcb1f3e119fd1cf14221aa6fd7c9aed, SHA256 57b56b94eed9079e0ec2b9b6bde244a11fd82bac5238b1d110022cdea6e7b86a. The file is stored outside the deliverable at /workspace/scratch/9c53b536a97f/source_reading/lehto_virtanen1973.djvu. Decoding with the Part A reviewer's already obtained DjVuLibre binaries found264 pages and extracted524,474bytes of embedded OCR.

The second advertised link https://libcats.org/dl/548781/1d4ee0 also returned HTTP200, providing a6,885,445byte PDF with SHA256 9e1e221f624785f4a5c52e2993b6913b5caaadc7a6f36f226fdca0be7bda2d90 and MD5 3452e3f519da2716aedbf31c4e37dd1e. Its actual399-page contents identify Dianne P. O'Leary's Scientific Computing with Case Studies, SIAM2009. It is a miscatalogued, unrelated book and is rejected as evidence for Lehto–Virtanen. Its file and extracted text also remain outside the deliverable. Matching a catalogue title, filename or hash was not treated as sufficient verification.

The correct DjVu title page explicitly reads Second Edition; it identifies O. Lehto and K. I. Virtanen, the English title Quasiconformal Mappings in the Plane, translation by K. W. Lucas, and Springer-Verlag1973. The copyright page names the1965 German original and gives the English print ISBNs0-387-06093-6 and3-540-06093-6. Printed text pages are offset by six in this scan. The title and copyright pages, and printed81,83,85,88,92,93,94,95,100 were rendered and visually read. The source pages, OCR and full scan are all excluded from the delivered project.

The public web search independently indexed https://libcats.org/g/A.%20Planes (turn351039302search1, opened as turn811956341view0), which also lists the target work. The web tool could not open the exact author/detail routes (turn120100003view0–1 and turn561902310view0–2), while ordinary HTTP succeeded. These failures are not represented as web-tool readings of the book. The mathematical evidence is the actually decoded and visually inspected original scan. No authentication, private endpoint, challenge workaround, protected Internet Archive file, or blocked English mirror was used. File downloads were coordinated to remain within the site's stated two-simultaneous-file limit.

## Exact mathematical passages and deductions checked

Chapter II Theorem6.2 on p.81 proves the quasisymmetric ratio bound for boundary values of a normalized quasiconformal self-map of the upper half-plane. Theorem6.3, stated on p.83 and proved through p.85, proves the converse: the increasing boundary function with a uniform two-sided ratio bound has a quasiconformal extension. Its explicit extension averages the boundary function over the two adjacent intervals; positivity of the four derivatives gives the Jacobian sign, and inequalities(6.16)–(6.19) bound the dilatation. Section7.1 p.88 records the exact equivalence. Thus passage between circle and line coordinates yields precisely the extension input of A3-welding.

Section7.5 on p.92 states the Sewing theorem: a quasisymmetric real boundary transition is realized by conformal maps of the upper and lower half-planes onto disjoint Jordan domains with the prescribed boundary relation. Its proof on pp.92–95 first solves the problem for analytic approximations. Nested circular segments and Schwarz reflection extend the finite-interval solution; uniform quasiconformal bounds and three-point normalization then give a nondegenerate limit. The glued maps W_n in(7.11), p.95, converge to a global quasiconformal W, while the limiting half-plane maps remain conformal. The construction therefore produces the required Jordan seam. Footnote25 on p.92 credits Lehto–Virtanen and Pfluger, and explains that this construction precedes their general prescribed-dilatation theorem. It does not require treating the still-unopened Pfluger paper as a premise.

Theorem8.5 on p.100 characterizes a Jordan seam as a quasiconformal curve exactly when the transition between its two normalized conformal parametrizations is quasisymmetric. The forward implication uses quasiconformal extension of a complementary map; the converse extends the transition, glues the maps across the line, and uses removability of that analytic line. This matches the seam regularity asserted in A3-welding. The source's sewing theorem is an existence statement. The manuscript proves its precise uniqueness assertion separately by conformal removability. Neither result asserts arbitrary-homeomorphism welding or rectifiability of every seam. The book comparison in sections/part_a3.tex states this exact scope.

The book's bibliography lists the Pfluger Verheftung article as J. Indian Math. Soc.24,401–412(1961); this agrees with the1960 golden-jubilee volume's publication-year distinction and does not close the original Pfluger access gate.

## Complete new program scope and timing

All outputs are saved under the matching code/part_c..._output.json and .txt names. These programs perform source retrieval, identity checking and document reading; they are not additional mathematical or numerical verification.

| Program | Actual scope/count | Runtime | Result |
|---|---|---:|---|
| part_c_lehto_libcats_catalog.py | 2 advertised public author-search requests |14.491566170s|BothHTTP200; actual target detail links read|
| part_c_lehto_libcats_book.py | 2 actual advertised public book-detail requests |11.695717279s|BothHTTP200; actual download links read|
| part_c_lehto_libcats_fetch.py | 1 advertised DjVu download, ordinary redirect |22.029461595s|Correct original scan, subsequently verified|
| part_c_lehto_libcats_pdf_fetch.py | 1 separately advertised PDF download, ordinary redirect |35.811126398s|Unrelated O'Leary book; rejected|
| part_c_lehto_extract.py | pdfinfo and pdftotext, 2 local reading subprocesses |7.251142322s|399-page unrelated PDF identified|
| part_c_lehto_djvu_read.py | Page count, OCR extraction and front-page conversion, 3 local subprocesses |4.006492592s|264-page original decoded; title and contents match|
| part_c_lehto_pages.py | 20-page local conversion and11 rendered page images |13.888866521s|Title/copyright and9 mathematical pages visually inspected|

The public catalogue run began2026-11-19T14:06:39.235898+00:00. The DjVu reading run began14:12:32.558372 and the exact-page rendering run14:13:23.498612. Every retrieval has its exact URL, status, individual timing and hash in the saved JSON. The earlier13:59 public-page request was7.494104414s and remains a separate unsuccessful route.

## Current integration and gate

ALehtoVirtanen1973 in sources/part_a_classics.bib is now marked OPENED with edition and exact mathematical locators. A comparison paragraph immediately after the proof of A3-welding cites these original passages. checks/part_c_lehto_events.tsv preserves the earlier negative event and appends the rejected-candidate and successful-reading events. The source-delivery gate for this named book is closed. No other source's access status is promoted by association.
