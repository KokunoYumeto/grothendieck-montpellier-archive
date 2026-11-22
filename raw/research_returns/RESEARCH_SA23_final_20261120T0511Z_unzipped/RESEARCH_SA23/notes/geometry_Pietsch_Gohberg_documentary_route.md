# Bounded Pietsch and Gohberg–Krein documentary route

Date: 2026-11-20 UTC. Investigator: geometry_analysis. Requested by root after
the earlier primary-source and manuscript audits. This is documentary work,
not a new mathematical proof check and not a source for dating the handwritten
cote 1 folios.

## Outcome

No dated Grothendieck letter, identified unpublished Grothendieck proof, or
link to a particular cote 1 leaf was found in the inspected source discussions.
This bounded route does not close the manuscript-date gate. It does not support
an inference that no relevant letter exists elsewhere.

## Pietsch, original 2007 book

Opened the public complete PDF, verified its title/copyright page through the
PDF extraction and publisher metadata, and visually read printed pp. 404 and 417.
The relevant locations are §6.5.1.6–7 and §6.5.5.7. The first says that the
memoir II p.13 indicates Grothendieck's awareness of the Hilbert trace identity
by 1955. The second refers to memoir II pp. 18–19 for the two-thirds Banach
theorem and to Lidskii 1959 for Hilbert factorization. These are references to
published texts, not to an independently identified letter or manuscript.

Bibliographic entries for Grothendieck were read at printed pp. 693 and 759.
The full extract was searched for Lidski, Grothendieck, personal communication,
unpublished, and letter. Letter/Grothendieck co-occurrences were checked as
finding aids; they concern unrelated recollections, tensor products, and later
biography. The entire book was not visually read. Pietsch's historical
inferences are not substituted for the already inspected original publications.

Source: https://susanka.org/HSforQM/%5BPietsch%5D_History_of_Banach_Spaces_and_Linear_Operators.pdf
Publisher metadata: https://link.springer.com/book/10.1007/978-0-8176-4596-0

Local PDF: notes/geometry_Pietsch2007.pdf
SHA256: 75fa3e7d858d00ec02636282b1efac9dc04d5488c81a2ce2ba3735925b0a5ebb
876 PDF pages; printed 404 is zero-based PDF index 424, printed 417 is index 437.
Visual witnesses: notes/geometry_Pietsch2007_pages/pdfindex_424.png and
pdfindex_437.png. Retrieval and keyword-page logs are
logs/geometry_Pietsch2007_retrieval.json and
logs/geometry_Pietsch2007_hits.json.

## Gohberg–Krein, original Russian 1965 book

The public Russian institute library links the complete original DjVu. Its
title page was visually read and prints Nauka, Moscow 1965. In this scan the
one-based DjVu page numbers match the printed page numbers in the inspected
body pages.

Chapter III §8(3), Theorem 8.4 p. 131 attributes the trace theorem to Lidskii [6].
The footnote at the proof's start, p. 132, says that the simpler proof was worked
out jointly with the theorem's author. It identifies no Grothendieck letter or
proof. Chapter IV §1 p. 199 has a source note listing Hille–Tamarkin, Lidskii [5],
Kuroda and others. The corresponding bibliography p. 431 identifies [5] and [6]
as published 1959 articles. The prefatory acknowledgments p. 7 mention shared
unpublished results generally, with a list of Soviet colleagues, without the
sought Grothendieck identification.

The entire OCR layer was searched for Russian/Latin Grothendieck stems, Lidskii,
letter and unpublished stems. No Grothendieck stem matched. Alphabetical
bibliography pp. 427–428 was visually checked at the expected location: it
passes from Gohberg/Markus to Dunford without a Grothendieck entry. This supports
only the stated bounded search result, not an exhaustive negative about every
possible spelling or unexamined book edition.

Pages visually read: 1,7,131,132,199,427,428,431. Page 2 was rendered but not
counted as visually read. Text of neighboring pp. 198,200–201,430 was also read.
No mathematical-proof retest was performed.

Source landing page: https://eqworld.ipmnet.ru/ru/library/mathematics/operators.htm
Original file: https://eqworld.ipmnet.ru/ru/library/books/GohbergKrejn1965ru.djvu
Alternate official institute listing: https://mechmath.ipmnet.ru/lib/?s=operators
Local file: sources/geometry_GohbergKrein1965.djvu
SHA256: a29470b038fdc3a49e4c4a35d895ecd5b0ef08ffab8493b961634684ad9aadeb
4,277,656 bytes. DjVu text extraction has 448 pages plus trailing empty segment.
Images/text: notes/geometry_GohbergKrein1965_pages/page_NNN.png/.txt.
Retrieval/render/hit logs: logs/geometry_GohbergKrein1965_*.json.

## Access and reproducibility record

All seven web batches are saved as notes/geometry_docroute_search01.json
through search07.json. The AMS DOI page returned 403 through the web opener;
the institute DjVu links could not be rendered by that opener due to content
type, so the public linked file was retrieved directly, HTTP 200. No access
restriction was bypassed.

The environment initially had no DjVu decoder. The two publicly distributed
Debian 12 DjVuLibre packages were downloaded, hash-recorded, and extracted only
under /tmp/geometry_djvu_runtime. No system installation was performed.
code/geometry_djvu_runtime.py and logs/geometry_djvu_runtime.json record the
packages and successful extraction. First rendering at 125 dpi was too small
for the intended visual check; its source/log survive as *_attempt01. The
actual inspected images were rendered at 400 dpi, 1770 by 2748 pixels.
No final or checkpoint archive was created during this route.

## Scope retained

The earlier June 1957-dated printed textual occurrence, the 1955 memoir
statements, the 1956 reconstruction, and Lidskii's original Weyl attribution
are unchanged. The surviving documentary question is the date of the
particular handwritten leaves. These later historical accounts do not answer it.


The raw page-text keyword-hit caches were subsequently retained as
notes/geometry_Pietsch2007_hits_full.txt and
notes/geometry_GohbergKrein1965_hits_full.txt, excluded by the existing
retrievable-cache policy. The logs now retain page numbers, text lengths,
and hashes. Exact preservation hashes are in
logs/geometry_documentary_source_update.json. Root moved the unchanged
original DjVu into sources/; its move receipt is
logs/root_move_documentary_cache.json. These cache organization changes
add no historical conclusion.
