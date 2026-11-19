# Requested-source coverage audit

Audit date: 2026-11-19. We distinguish an opened preview or bibliographic page
from an opened theorem. The user requests Happel and Lang at prompt lines
194–195 and 200–201. This note records the additional source search; the root
bibliography has not been modified.

This audit adds two explicitly qualified bibliography records in
`notes/extra_requested_references.bib`. There is no remaining proof dependency
on either unopened book passage.

## 1. Happel: metadata and preview opened; relevant theorem not opened

The book is Dieter Happel, *Triangulated Categories in the Representation
Theory of Finite Dimensional Algebras*, LMS Lecture Note Series 119,
Cambridge University Press, 1988, ISBN 9780521339223, book DOI
10.1017/CBO9780511629228. The relevant original locator is Chapter I,
Theorem 2.6, p. 16. We know that precise locator from the opened Bühler
Theorem 13.7, not from an inspection of p. 16 of the book.

### URLs actually attempted

| URL | Observed outcome |
| --- | --- |
| https://www.cambridge.org/core/books/triangulated-categories-in-the-representation-of-finite-dimensional-algebras/8B27A25C1ACEFD54EBD51306AFC3BADC | Official book metadata opened. |
| https://www.cambridge.org/core/books/abs/triangulated-categories-in-the-representation-of-finite-dimensional-algebras/triangulated-categories/AD4EA5E6215A0B586678B10B2D417F74 | Official Chapter I page opened: pp. 1–56; chapter DOI 10.1017/CBO9780511629228.002; access restriction displayed. |
| https://api.pageplace.de/preview/DT0400.9780511892271_A23680352/preview-9780511892271_A23680352.pdf | Lawful distributor preview opened and downloaded; 22 PDF pages, ending at printed p. 10, the start of §I.2. Theorem I.2.6 on p. 16 is absent. |
| https://assets.cambridge.org/97805213/39223/index/9780521339223_index.pdf | Publisher index opened and downloaded; printed pp. 207–208. It is not the theorem text. |
| https://www.math.uni-bielefeld.de/~sek/sem/studygroup/main.html | Institutional reading list opened. It names the book but supplies no full-book link. |
| https://books.google.com/books?hl=en&vid=ISBN0521339227 | Bibliographic/preview landing page opened. |
| https://books.google.com/books?id=rwGuMdtocAEC&printsec=frontcover | Followed the displayed preview link. Retrieval failed after a regional redirect; no theorem page was read. |
| https://books.google.com/books?id=rwGuMdtocAEC&pg=PA16 | Ordinary public preview navigation attempted; tool reported the URL inaccessible. No theorem text was read. |

**Disposition.** We mark the relevant book theorem **not opened**. The paper's
A2.6 proves the complexes statement and uses the opened Bühler Theorem 13.7
and Example 13.8 for the stable triangulation. The earlier source-log sentence
“Happel's book itself has not been opened” should now be read more precisely
as “Happel's relevant theorem has not been opened”; the preview has been read.

## 2. Lang: requested locator clarified; relevant section not opened

The edition examined is Serge Lang, *Algebra*, revised third edition,
Graduate Texts in Mathematics 211, Springer, 2002, ISBN 9780387953854,
DOI 10.1007/978-1-4613-0041-0. Its official contents, printed p. xii
(PDF page 12 of the front matter), place “Abelian Kummer theory” in
Chapter VI §8, beginning p. 293, and “The equation X^n−a=0” in §9,
beginning p. 297. Section 10 starts on p. 302; the contents alone do not
identify the exact end page of either preceding section. Thus the user's §9 is a
related binomial-equation section; it is not the section headed
“Abelian Kummer theory.” We do not infer theorem numbers from these titles.

### URLs actually attempted

| URL | Observed outcome |
| --- | --- |
| https://link.springer.com/book/10.1007/978-1-4613-0041-0 | Official book metadata and chapter list opened. |
| https://link.springer.com/chapter/10.1007/978-1-4613-0041-0_6 | Official Chapter VI page opened; pp. 261–332; subscription restriction displayed. |
| https://link.springer.com/content/pdf/bfm:978-1-4613-0041-0/1 | Public publisher front matter opened and downloaded; 15 PDF pages. Its contents verify the exact section titles and starting pages above. |
| https://page-one.springer.com/pdf/preview/10.1007/978-1-4613-0041-0_6 | Followed the publisher's public preview link; downloaded two pages, printed pp. 261–262. Neither §8 nor §9 is present. |
| https://books.google.com/books/about/Algebra.html?id=eOUlBQAAQBAJ | Bibliographic/preview landing page opened. |
| https://books.google.com/books?id=eOUlBQAAQBAJ&pg=PA297 | Ordinary public preview navigation attempted; tool reported the URL inaccessible. No §9 theorem text was read. |

**Disposition.** We mark the requested §9 **not opened**, and likewise do not
claim to have opened §8. No theorem is attributed to either section as if
we had read it. The paper's Kummer arguments use its explicit field-theoretic
proofs and the opened primary sources recorded by the B4 agent.

## 3. Integrated Dold–Puppe locator audit: passed

We re-opened the original article through its institutional mirror and checked
the PDF's printed folios against the references presently in `sections/A3.tex`
and `sections/A4.tex`:

| Use in paper | Exact original locator | PDF page, one-based | Result |
| --- | --- | --- | --- |
| A3.1 and A4.1: summands indexed by monotone surjections | §3.2, equation (3.3), printed p. 219 | 20 | Correct. |
| A3.1 and A4.1: normalization and denormalization are inverse equivalences | Theorem 3.6, printed p. 220; proof begins p. 222 | 21; proof 23 | Correct. |
| A4.1: projectivity comparison | Corollary 3.8, printed p. 220 | 21 | Correct. Finite generation and finite projectivity are derived in our text from the finite direct-sum formula. |
| A3.1: natural chain inclusion and projection | Equations (3.19)–(3.21), especially (3.20), printed p. 223 | 24 | Correct. Equation (3.20) is a direct-sum decomposition of chain complexes, so its projection and inclusion are chain maps. |

The direct-sum formula in our paper follows by counting the surjections with
a fixed target. The contraction `h_N = p s_{-1} j` in A3.1 is justified by
the chain splitting, not merely a degreewise module splitting. No correction
to the existing Dold–Puppe locators is required.

Primary bibliographic page:
https://www.numdam.org/item/AIF_1961__11__201_0/ .
Opened and retained institutional mirror:
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/doldpupp.pdf .
The retained PDF SHA-256 is
`e28828cf4776aecdad2edf844e141bc75c3a10987b94ee463d3fa7aa5f4c7a0c`.
The front cover accounts for the one-page offset in the PDF count.

## 4. Scope of the search and retained evidence

We searched the exact book titles and authors, the Happel theorem locator,
Lang's Chapter VI §9, and the Cambridge, Springer, Bielefeld, and Yale domains.
Representative exact searches were:

- `Happel Triangulated Categories in the Representation Theory of Finite Dimensional Algebras I.2.6 pdf`
- `"Dieter Happel" "Triangulated" pdf "16" frobenius`
- `"Happel" "Triangulated categories" filetype:pdf site:math.uni-bielefeld.de`
- `"Happel" "Triangulated categories" filetype:pdf site:cambridge.org "2.6"`
- `"Happel" "Triangulated categories" "pdf" site:assets.cambridge.org`
- `"Lang" "Algebra" "VI" "§9" Galois`
- `"Serge Lang" "Algebra" "pdf" site:link.springer.com/chapter/10.1007/978-1-4613-0041-0_6`
- `"Serge Lang" "Algebra" "297" site:math.yale.edu`

An initial broad Lang search mistakenly mentioned purely inseparable
extensions; the opened contents corrected that search direction. Search
results also surfaced unverified third-party full-book uploads; we did not
open or download them. We did not request subscription chapter PDFs, supply
credentials, alter access restrictions, or infer access from search snippets.
This is a source-coverage audit, not a proof of absence of every lawful copy.

`python code/requested_sources_audit.py` reproduces the four public PDF
downloads and the Dold–Puppe text-location scan. It produces
`logs/requested_sources_audit.json`; `logs/requested_sources_audit.stdout.txt`
retains its output. PDF files are named explicitly as previews or front matter
under `sources/`; their text extractions are under `logs/`. The status table
above also records unsuccessful web-tool requests that the download script
does not repeat.

For the root agent's chat citations, opened source references from this audit
include `turn542259189view0` (Happel chapter), `turn542259189view2` (Happel
preview), `turn785779096view4` (Lang contents), `turn946515211view2` (Lang
chapter preview), and `turn724310958view2`–`turn724310958view5` (Dold–Puppe
locators). Re-open the corresponding URL in the root turn before citing.
