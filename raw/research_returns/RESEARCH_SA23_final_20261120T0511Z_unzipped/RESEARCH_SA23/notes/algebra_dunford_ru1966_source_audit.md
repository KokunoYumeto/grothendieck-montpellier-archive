# Dunford--Schwartz II: bounded audit of the original Russian translation

Recorded in the current run on 20 November 2026. Retrieval began 04:53:54 UTC; the selected original images were individually displayed and read by 04:58:20 UTC. The exact machine timestamps and hashes are in the accompanying logs/manifest.

## Result and scope

The inspected 1966 Russian edition supplies **no dated identification of a Grothendieck Hilbert trace/genus-zero proof, letter, enclosure, or the particular cote 1 sheets**. Its Fredholm historical subsection and the Grothendieck/Lidskii bibliography entries give ordinary publication references. The particular-sheet date gate is unchanged.

This is a successful new original-edition reading, unlike the earlier unsuccessful English-copy search. It is **not** a reading of the English 1963 body. The Russian editor expressly says that some inaccuracies were corrected and historical notes were added (printed p. 6). Therefore no statement here is silently transferred to the English edition.

## Provenance and access

The actual opened EqWorld operator-theory library page, https://eqworld.ipmnet.ru/ru/library/mathematics/operators.htm (web reference `turn748259498view0`), advertises the file as link 16:

https://eqworld.ipmnet.ru/ru/library/books/DanfordShvarc_t2_1966ru.djvu

The web reader returned an unsupported DjVu content-type error (400), not an access denial. An ordinary direct request to that advertised public link returned HTTP 200. No denied host was retried, and no account or access override was used. The downloaded original scan is `sources/algebra_dunford_ru1966.djvu`, 18,240,028 bytes, SHA256 `176dbdf4d51440456a1b8c7048d7db3a68b0a518a5b50b37d72533872ea52229`.

Physical p. 2 reproduces the English title page for *Linear Operators, Part II: Spectral Theory. Self Adjoint Operators in Hilbert Space*, Nelson Dunford and Jacob T. Schwartz, with assistance from W. G. Bade and R. G. Bartle, Interscience, 1963. Physical p. 3 is the Russian title/imprint: Mir, Moscow, 1966; translation by M. G. Gasymov, V. Ya. Lin and B. S. Mityagin, edited by A. G. Kostyuchenko. These are title-page facts within the Russian volume, not evidence of inspecting the separate English edition. The colophon (physical p. 1064) records submission to production on 22 February 1966 and authorization for printing on 30 August 1966. Those dates concern this edition only.

## Exact original-page reading

Every page in this table was individually displayed as an original image, not inferred from OCR. Body, bibliography, index and contents page numbers agree with the physical image numbers at the checked locations.

| Original pages | Scope actually read and result |
|---|---|
| Physical 1--3 | Cover and English/Russian title pages; edition identification above. |
| Printed 5--6 | Entire Russian editor's preface. General chapter survey, including Hilbert--Schmidt/Carleman material and a new Gohberg--Krein book; p. 6 says historical notes were added. No dated supplied Grothendieck proof or manuscript. |
| Printed 7--8 | Entire translated authors' preface, ending July 1963. Acknowledgments concern corrections, preparation and support; no Grothendieck trace manuscript identification. |
| Printed 328--330 | Chapter XI, section 11, notes and addenda; the complete subsection on Fredholm theory and eigenvalue localization, ending before the subsection on singular integrals. Carleman, Hille--Tamarkin and Smithies are cited for Hilbert--Schmidt theory; eigenvalue estimates and Schatten/von Neumann classes lead to Krein, Gohberg--Krein and Brodskii--Livshits on completeness, dissipative operators and subdiagonalization. No dated Grothendieck communication, manuscript, or distinctive supplied genus-zero proof is identified. |
| Printed 753, 755 | Both name-index body hits for Lidskii, in Chapter XIII's notes on ordinary differential operators. Lidskii [1] is included among differential-equation spectral references, with no trace manuscript or correspondence statement. |
| Printed 970--971 | Complete Grothendieck bibliography entry (items 1--7). It lists publications, including Memoir 16 and the Fredholm paper, with no manuscript/letter description. The actual scan prints the French Fredholm reference as volume 84 (1958), pp. 319--384, and the Russian translation as 2:5 (1958), pp. 51--103. These literal bibliographic data are retained here without silently correcting them; the already-opened French original establishes 1956 elsewhere in the project. This edition's date typo cannot date cote 1. |
| Printed 993--994 | Complete Lidskii bibliography entry, two items: the 1954 differential-equation solutions note and the 1958 completeness-of-root-subspaces paper. No received Grothendieck proof is mentioned. This entry is not the already-read 1959 trace note. |
| Printed 1045, 1047 | Name index: Grothendieck points only to the bibliography beginning at 970; Lidskii points to 753, 755, 993. All those target entries were checked as above. Index coverage is not an exhaustive absence proof. |
| Printed 1061--1062 | Contents locating Hilbert--Schmidt operators (XI.6, p. 168), compact-operator classes and generalized Carleman inequalities (XI.9, p. 251), subdiagonalization (XI.10, p. 281), notes (XI.11, p. 309), bibliography and name index. |
| Physical 1064 | Colophon and printing dates, as above. |

Physical p. 4 was rendered and its native text extracted, but was not visually read. The rest of the book was not read page by page. Full native-text searches were used solely as finding aids; exact patterns, contexts and original image hashes are in `notes/algebra_dunford_ru1966_manifest.json`. No claim of exhaustive visual reading is made.

## Reproducibility and page-index correction

`code/algebra_dunford_ru_fetch76.py` downloaded the file, extracted native text and rendered front matter. `code/algebra_dunford_ru_render77.py` verified 1064 physical pages and rendered the selected targets. All render/extract return codes in the saved logs are zero.

Whole-file `djvutxt` skips the initial cover text segment. Consequently the initial search-hit ordinals in fetch76 are **text-segment ordinals, not physical page numbers**. The original images were always correctly selected with explicit `ddjvu -page=n`. Script77 regenerated every selected page's text with explicit `djvutxt -page=n`; its log records this correction. This audit uses visually verified printed page numbers. The full-text manifest also labels search ordinals explicitly and does not convert them by an assumed global offset.

Records: `notes/algebra_history_web180.json`, `notes/algebra_history_web183.json`; `logs/algebra_dunford_ru_fetch76.json`, `logs/algebra_dunford_ru_render77.json`, `logs/algebra_dunford_ru_record78.json`; images and corrected per-page text now in `sources/algebra_dunford_ru1966_pages/`.

No paper section or bibliography entry was changed for this bounded negative source result.

## Source-cache relocation

After the original page reading, the raw images and extracted per-page text were moved unchanged from `notes/algebra_dunford_ru1966_pages/` to `sources/algebra_dunford_ru1966_pages/`, following the project source-cache policy. The executed retrieval/render programs and their original logs retain their historical paths. `logs/algebra_dunford_cache_correct79.json` records every old/new path, byte count and SHA256; no file bytes changed during the move.
