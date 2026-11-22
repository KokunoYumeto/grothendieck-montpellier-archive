# Cote 1: direct inspection for dating evidence

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root agent,
20 November 2026. This is a source inspection, not a claim of priority.

We retrieved the complete official PDF from
https://grothendieck.umontpellier.fr/1.pdf. The file has 150 physical PDF
pages and 84,267,714 bytes; SHA256
`38a9610e2a9227201f1bc162a28f2a2ac20951406bba7c9ccf507553f53e71e3`.
The cover calls the mathematical notes undated and separately mentions a
1953 letter. Its large 1953 dossier label does not date each sheet.

Root inspected all seven whole-dossier contact sheets as a finding aid,
then directly displayed physical pages 79–81 and every physical page
111–150 individually. Pages 111–113 and 142–143 were displayed at a width
of 1,800 pixels; the other pages in the final range at 1,400 pixels.
The renderings are in `sources/root_cote1_folios/`, with the commands,
source hash and measurements in `code/root_render_cote1.py` and its
matching JSON/text logs. The 35-page rendering batch took 11.905115798 s.

This inspection looked for letter headings, dates, signatures, dated
bibliographical references, and explicit links between sheets. It is not
a diplomatic transcription or a proof audit of every mathematical line.

## Numbering settled by content

| Physical PDF page | Public PDF footer | Archival pencil number | Content |
|---|---|---|---|
| 79 | 78 | 80 | Coefficient estimate and crossed-out Hilbert determinant product |
| 80 | 79 | 81 | Continuation of the crossed-out trace argument |
| 81 | 80 | 82 | Convex functions and supporting hyperplanes, not the trace continuation |
| 111 | 110 | 112 | Genus-zero majorization lemma and the linear exponential factor |
| 112 | 111 | 113 | Sector bound and product over the three cube-root rotations |
| 113 | 112 | 114 | Order of decreasing positive sequences |

Thus the prompt's 79–80 and 111–112 agree with physical PDF numbering.
No global shift of those references is appropriate. The original sheets
do contain the analytic steps reconstructed in H; the literal phase and
sector details require the corrections already proved in that section.

### Terminology correction and the early numbering discontinuity

Root subsequently displayed physical pages 2, 3 and 4 at 1,900-pixel
width. Their lower-left pencil numbers are 1, 2 and 5, while their
public PDF footers are 1, 2 and 3. The official institutional method
description explicitly identifies lower-left HB-pencil numbering as
the archivists' work. We therefore call those **archival pencil
numbers** and the added sequential typeset numbers **public PDF
footers**. Earlier notes calling the latter archive folios were
imprecise; the actual numerical correspondences above do not change.

The public site also says that correspondents' letters are not
disseminated without authorization. That general policy does not
identify what the skipped pencil numbers 3–4 contain. We neither
identify them with the catalogue's 1953 letter nor treat their
absence from the visible public sequence as a date for the maths.
The source is https://grothendieck.umontpellier.fr/, sections
Presentation and La numerisation de conservation; its retained
HTML and precise local line locators are in algebra's dating audit.

## Final forty pages: observed contents

| Physical PDF pages | Observed material |
|---|---|
| 111–112 | Genus-zero lemma; no date or external dated citation identified |
| 113–119 | Sequence order, zero-counting functions, summability and contour/logarithmic integral arguments |
| 120–122 | A holomorphic function on the Banach space of summable sequences and coefficient estimates |
| 123 | Blank except for page numbering |
| 124–126 | Exterior-power estimates, Cauchy–Schwarz and determinant inequalities |
| 127–140 | Schatten classes, eigenvalue/norm estimates, Hölder and multiplicative inequalities |
| 141 | Blank except for page numbering |
| 142–148 | Singular-value continuity, fractional powers and estimates for converging operators |
| 149–150 | Fredholm resolvent/minor coefficient estimates |

No explicit date, dated letter or dated reference was identified in this
range. Faint and cancelled marks prevent a claim that every possible
dating mark has been excluded. The result is **no dating witness found**,
not a proof that an unreadable mark cannot contain one. The names of
earlier mathematical authors provide no upper writing-date bound.

We also independently displayed geometry's enlarged physical page 26
(public PDF footer 25, archival pencil number 27). It contains the beginning of a typed
German letter to Paula beneath mathematical writing, but no legible date
was identified there. We do not identify this scrap with the catalogue's
1953 letter without further evidence.

## Related contemporary publication

Root independently displayed the original Lidskii article's printed
p. 487, physical p. 23 of the retrieved 1959 journal issue. Its closing
discussion attributes a genus-zero result to Weyl and points in a footnote
to reference 12, the 1955 Grothendieck memoir. The receipt date is
23 November 1958; it does not date a later added endnote. This is a
contemporary witness to the memoir's pointer, not a statement that
Grothendieck printed a proof or a date for the cote 1 sheets. Algebra's
source note and bibliography give the exact issue URL and source hash.
