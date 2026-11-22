# Montpellier: other indexed dossiers and the papers-lent list

Completed 2026-11-20, approximately 04:21 UTC, by crystalline_categories.

## Question and limits

This is a distinct check for a dated duplicate, enclosure or explicit archival cross-reference identifying the Hilbert spectral-trace/genus-zero proof in Montpellier cote 1. The already completed full cote 1 and A-C folder inspections were not repeated.

The complete **public catalogue** was reviewed. This must not be called inspection of the complete internal archival instrument or all holdings. The official site describes itself as the publicly consultable part; correspondence is partly withheld. Algebra_letters expressly confirmed that its earlier inventory work obtained the same public HTML and the CIRM methods presentation, not a fuller internal instrument or complete name index. The CIRM discussion of such an instrument does not constitute access to it. No withheld item, account or private endpoint was accessed.

## Public catalogue inspected

Official URL, freshly opened in the web reader:
https://grothendieck.umontpellier.fr/archives-grothendieck/

Raw current-run web response: `notes/category_montpellier_inventory_web01.json` (source reference `turn831821237view0`). The full saved official HTML previously retrieved in this run is `sources/algebra_history_montpellier_index.html`, SHA256 `2c0f1a5ceecb43a7956c670c568207fc46d495de7728600119bd278639e9300b`.

All **178 public item descriptions** were extracted, including their dates, source-line locators, advertised scan-viewer URLs and explanatory notes. Every item's title/description was read in three complete batches, not just keyword hits. Supplemental term matching covered functional analysis, Fredholm, Hilbert, nuclear spaces/operators, traces, determinants, genus, entire functions, compact operators, relevant names and early dates; matches were assessed in context.

The catalogue identifies functional analysis explicitly at cote 1. Cote **2**, HTML lines 1867 onward, concerns **Riemann-Roch**, with a bracketed 1957 attribution; its 44-page original was not opened because that description does not identify a relevant duplicate. Cotes **10/155** concern tensor categories, **98** Hilbert schemes, **60** geometric L-functions, and **153** analyseurs. None of these subject-name matches identifies an operator-trace dossier. Cote **57** mentions a 1956 supply-list verso in a Picard dossier; that is not a trace-manuscript reference. These originals were not broadly reread.

Cote **162-6** contains five unidentified pages; the catalogue explicitly says they were not assigned to an identifiable ensemble. That is a limit of the description, not evidence of a trace duplicate. This generic dossier was not opened under the instruction to follow directly relevant advertised scans.

One useful documentary lead was followed: **162-1**, a nine-page list of names and references for papers lent. Its advertised viewer is `../web/viewer.html?file=../162-1.pdf`, visible at HTML lines 4360 onward. A loan record could in principle identify an early manuscript independently of its position in a later folder.

## Original cote 162-1 opened and visually inspected

Advertised original URL:
https://grothendieck.umontpellier.fr/162-1.pdf

Retrieved with HTTP 200 at 2026-11-20T04:17:03Z. Local file: `sources/category_montpellier_162-1.pdf`, **3,706,992 bytes**, **10 PDF pages**, SHA256 `5ecb6efd0c0b7c19caefb83d3c146c24b099d26cac9f1fb829126e23f699e6f7`.

All ten PDF pages were directly viewed at readable resolution. Physical 1 is the modern cover; physical 2 is the original folder; physical 3-10 are eight pages of handwritten loan lists. Public PDF footer numbers 1-9 correspond to physical 2-10. The archival pencil numbers visible at the lower left also run 1-9 here; those remain a distinct numbering system.

| Physical page / public footer | Direct observation relevant to this inquiry |
|---|---|
| 1 / no footer | Modern catalogue cover supplies a bracketed lower-date attribution from EGA/SGA references, not an original date. |
| 2 / 1 | Original folder, headed Papiers prêtés. No early proof identifier or original date observed. |
| 3 / 2 | Loan list on IHES Bures letterhead. One clear entry reads “Résumé PTT Grenoble”. Other entries include EGA, Riemann-Roch, differential calculus and Atiyah material. |
| 4 / 3 | Names/document lists including Raynaud, Illusie and Deligne; principally algebraic and homological references. |
| 5 / 4 | Further loans and references, including SGA 7, Quillen, Hartshorne and EGA material. |
| 6 / 5 | Further crossed and uncrossed references to algebraic-geometry papers and correspondence. |
| 7 / 6 | More names/document lists; no Hilbert spectral-trace proof or matching enclosure identified. |
| 8 / 7 | An entry under Thomas names Lindenstrauss and Pelczynski papers and a Lindenstrauss survey: functional-analysis references are indeed present. |
| 9 / 8 | The bottom entry under a name read as Nakai gives “Produits tens. top. (Groth)”. It does not state a date, format, sheet identifier or trace-proof connection. |
| 10 / 9 | Final names/references, including a dated Serre article. A cited publication year is not a date for a loan or for the target proof. |

The quoted functional-analysis references are abbreviated. They are not silently identified with a particular surviving copy or manuscript. Some heavily crossed-out entries cannot be completely deciphered. Thus the justified finding is that **no matching dated duplicate/enclosure or trace-proof identifier was found in the inspected legible material**, not that every canceled word has been transcribed or that no such paper could ever have been lent.

## Result

The complete public description set identifies no second functional-analysis/Fredholm/trace dossier beyond cote 1. The adjacent cote 2 suggestion is resolved at catalogue level as Riemann-Roch. The directly relevant documentary list 162-1 contains recognizable functional-analysis references, but no identified link to the particular genus-zero proof or its date.

The original date of the Montpellier trace/genus-zero sheets remains unproved. This bounded route does not establish absence of an unindexed or unpublished duplicate elsewhere in the fonds. No chronology is transferred from a neighbouring dossier, a publication year, the catalogue's lower-date estimate for the loan list, or a general subject match.

## Preserved programs, outputs and correction

- `code/category_montpellier_inventory_extract.py`: first extraction attempt; it failed because bs4 was unavailable. The program and exact error are retained in `logs/category_montpellier_inventory_extract_error.txt`.
- `code/category_montpellier_inventory_extract_v2.py`, `logs/category_montpellier_inventory_extract_v2.txt`, `notes/category_montpellier_inventory_entries.tsv`, `notes/category_montpellier_inventory_extract.json`: standard-library extraction of all 178 entries.
- `code/category_montpellier_inventory_filter_v3.py` and corresponding log/JSON: corrects a search-only false hit. V2 accidentally included source-line numbers in matching and therefore reported 1954 for cote 9; v3 searches only the actual dates, descriptions and notes. The inventory rows themselves were correct and unchanged.
- `notes/category_montpellier_inventory_titles_1.txt` through `_3.txt`: complete three-batch description reading aid.
- `code/category_montpellier_inventory_additional_terms.py`, corresponding log and JSON: additional full-description/context searches.
- `notes/category_montpellier_inventory_web02.json`: one exact-name official-domain inventory search. It returned institutional overview articles, not a fuller instrument; no unsupported claim of absence is inferred.
- `code/category_montpellier_loanlist_fetch.py`, `logs/category_montpellier_loanlist_fetch.txt`: advertised PDF retrieval, UTC timestamp, hash, status and PDF metadata.
- `code/category_montpellier_loanlist_render.py`, `logs/category_montpellier_loanlist_render.txt`: complete ten-page rendering and finding-aid OCR; per-page command/hash records and OCR under `notes/category_montpellier_162-1_pages/`.
- All reproducible page images remain under `sources/category_montpellier_162-1_pages/`, `page_001.png` through `page_010.png`; raw source payloads remain under sources/.

These are bounded primary-source reading checks, not new mathematical proof checks.

## Later separate check of cote 162-6

After the catalogue audit above, root independently opened the advertised cote 162-6 scan and visually inspected all six physical pages (modern cover plus five original pages). The separate record is `notes/root_montpellier162_6_date_audit.md`. Root reports gamma factors and Hodge indices, real Weil-group/cohomological material, norm characters, L-factor twists and idele diagrams, with no identification of the target proof, a date or an enclosure. The earlier statement that this category audit did not open 162-6 remains a chronological and attribution distinction; it is superseded as a statement of the team's current source coverage by root's completed check. This paragraph does not claim an additional independent reading by crystalline_categories.
