# Bourbaki rédaction 230: complete Fredholm-section comparison

Checked 2026-11-20, 04:00 UTC, by crystalline_categories. This is direct primary-source reading and a comparison of the displayed proof architecture; it is not a new independent proof of all the source's theorems.

## Result and exact historical limit

The IECL/Delsarte original scan of rédaction 230 was obtained publicly and the entire Fredholm section, typed pp. 204–221 (physical PDF pp. 118–135), was visually read. It gives the general nuclear-tensor determinant construction, the zeros/eigenvalues correspondence including algebraic multiplicity, the general Banach-space square-summability bound, and a genus-at-most-one product theorem. Its precise distinction at **typed p. 219, Remarks 2 (physical p. 133)** is decisive: the Hermitian Hilbert case has a genus-zero product by the earlier spectral trace corollary, whereas the arbitrary Hilbert nuclear case is reported as a result announced by Grothendieck in his thesis. No proof of the latter statement is given in these remarks or the remaining pp. 220–221.

The relevant short wording is: “Grothendieck annonce dans sa thèse que cette dernière proposition est encore valable si u est quelconque”, followed by the completed-tensor and Hilbert-space hypotheses. This identifies an announcement in the thesis, not a particular unpublished manuscript, letter, or enclosure. It does not identify the Montpellier cote 1 sheets. No three-sector Phragmén–Lindelöf argument occurs in the inspected Fredholm section. The independently read Hilbert section, pp. 188–203, likewise does not supply that argument or the general spectral trace equality; see notes/geometry_r230_hilbert_date_audit.md for its full, separately owned inspection record.

The catalogue attributes this rédaction to Jean Dieudonné and dates it March 1956. Its own note explains that a **different copy at the ENS library** bears the handwriting Dieudonné mars 1956. The downloaded IECL copy is not that copy. The catalogue record has no advertised link to the ENS copy. No date or author inscription was observed on the downloaded title page, comments page, first text page, or final page. This source therefore supplies a precisely bounded contemporary attribution/announcement comparison, with catalogue-level dating; it supplies **no date for the particular Montpellier trace/genus-zero leaves**. A match of subject or the thesis reference does not close that remaining gate.

## Source identity, retrieval and opened scope

- Exact catalogue record: http://web.archive.org/web/20240917194937/https://archives-bourbaki.ahp-numerique.fr/items/show/664 . Saved sources/category_bourbaki_r230_item664_0.html, SHA256 41113871cda2b2db8893025739ff87a79b1b40606d1b9799e54d5e4f03a768ef. Identifier r230_iecl_bki05-3; IECL/Delsarte cote IECNR BKI05-3.1.
- Actual advertised PDF payload: http://web.archive.org/web/20260213200334if_/https://archives-bourbaki.ahp-numerique.fr/files/original/49e6e904fbc99a10207673c09e068fa7.pdf . Saved sources/category_bourbaki_r230_original_1.pdf; 156 physical pages; 29,100,237 bytes; SHA256 2ecd5627b5e9878a362a237fcadbac6ccdbb85e076551d7c4f6f37d31f19eba1.
- Exact independent Delsarte full-inventory printed p. 61 was visually read: sources/category_bourbaki_r230_bki_inventory_p61.png. It identifies rédaction 230, IECNR BKI05-3.1, IECN230, pagination 88–242 f.; this inventory entry itself gives no date or author.
- Category agent directly read original physical pp. 1–3, 118–135, and 156. Page 1 gives title/contents; physical 2 = typed 88 gives comments; physical 3 = typed 89 starts compact operators; physical 156 = typed 242 ends the kernel theorem. Physical pp. 118–135 have their expected typed numbers 204–221. No entire-PDF reading is claimed.
- Geometry agent separately read original physical pp. 102–117 = typed 188–203; its own note and events preserve that scope. Root independently read physical pp. 1–2; root owns its own check event.
- The comments at typed p. 88 state that most of the chapters come from Grothendieck's thesis, incorporating improvements and simplifications from Schwartz's 1954 seminar. They do not identify any cote 1 leaf.
- The original contents and section heading call Fredholm theory **Chapter III, §4**, whereas the catalogue prose calls it §5. Locators here follow the original.

The live AHP host was not revisited after its earlier challenge. All new archived catalogue/payload requests went only to web.archive.org, and the final retrieval scripts reject redirects outside that host. No login, credentials, contact, or reserved content was used. Full retrieval history, exact archive timestamps, wrapper/payload distinctions, and hashes are retained in notes/category_bourbaki_r187_r230_date_audit.md and the named logs below.

## Complete Fredholm architecture, read from page images

| Typed pages | Physical pages | Displayed result or argument |
|---|---|---|
|204|118|§4 begins with the finite-dimensional characteristic determinant, adjugate, coefficient recurrences, and trace/derivative identity.|
|205–207|119–121|The normalized determinant defines symmetric multilinear coefficients; Propositions 1–4 identify them and prove recurrences and the multilinear adjugate construction.|
|208|122|Higher Fredholm minors and their trace/derivative and multiplication identities, Proposition 5.|
|209–210|123–124|Proposition 6 relates the first nonzero minor to kernel dimension; proof by alternating determinants and independent vectors. The infinite-dimensional Banach case begins at the end of p. 210.|
|211|125|Distinguishes the completed projective tensor product from its associated nuclear operators because injectivity is not assumed; extends the algebraic formulas.|
|212–213|126–127|Hadamard's matrix bound; Lemma 2 gives the general coefficient constant m^(m/2)/m!; Lemma 3 bounds adjugates. Completion gives entire determinant and adjugate series and the inverse identity.|
|214|128|Theorem 1 (Fredholm): determinant zeros give the operator spectrum and the minors give geometric multiplicity. A following remark compares tensor-algebra and operator spectra.|
|215–216|129–130|Lemma 4 proves continuity into entire functions with compact convergence. Proposition 7 gives determinant multiplicativity. Proposition 8 identifies zero order with algebraic eigenvalue multiplicity, by finite primary-space splitting and finite-rank approximation.|
|216–217|130–131|Lemma 5 is a mixed finite-rank coefficient estimate. Lemma 6 gives arbitrarily small quadratic exponential growth. Proposition 9 begins the general Banach square-sum bound for eigenvalues.|
|218|132|Completes Proposition 9 through a finite-dimensional Hilbert norm and continuity of zeros. Proposition 10 states genus 1 (understood as at most 1) and starts the Weierstrass factorization argument.|
|219, upper part|133|Uses a Hadamard lower bound on circles and the quadratic minimal-type estimate to eliminate the quadratic exponential factor. This is the proof of the general genus-at-most-one statement, not a three-sector genus-zero proof.|
|219, Remarks 1–2|133|Relates the linear exponential coefficient to the trace. Distinguishes the general Banach square-sum bound, the Hilbert absolute eigenvalue sum, and the Hermitian Hilbert genus-zero product; the arbitrary Hilbert genus-zero assertion is specifically attributed to an announcement in Grothendieck's thesis.|
|219–220, Remark 3|133–134|Integral representations yield the classical Fredholm determinant coefficient formulas.|
|220–221, Remark 4|134–135|Logarithmic derivative and Plemelj coefficient formulas, followed by trace-removing regularization for Hilbert–Schmidt operators and a Smithies reference. No additional proof of the arbitrary trace-class Hilbert genus-zero statement is supplied.|
|221, Remark 5|135|Extension of the Fredholm framework to separated locally convex spaces using Banach disks and equicontinuous dual disks. End of §4.|

The proof-content conclusion is bounded to the explicitly read sections. It is not a claim that none of the source's ingredients could be combined with additional arguments to prove the trace theorem. Our already established modern reconstruction from Grothendieck's 1956 published ingredients is a separate result with its own proof/audit record. Nor does this source establish whether Dieudonné had or had not seen a particular unpublished proof: it simply states the thesis-announcement attribution above.

## Reproducibility and retained outputs

- code/category_bourbaki_r230_fredholm_render.py and logs/category_bourbaki_r230_fredholm_render.txt: all 18 original-page renderings, exact command/status/stderr, hashes, and OCR outputs.
- sources/category_bourbaki_r230_pages/page_118.png through page_135.png: individually opened original page images. The crucial Remarks 2 image is page_133.png.
- notes/category_bourbaki_r230_fredholm_pages/page_118.txt through page_135.txt and corresponding JSON command records; combined notes/category_bourbaki_r230_fredholm_full.txt. English-only OCR is poor because the original violet typescript is faint; OCR was not relied on for the decisive wording or theorem scopes.
- Front/end page images are sources/category_bourbaki_r230_pages/page_001.png, page_002.png, page_003.png, and page_156.png; front-render program/log retained.
- Earlier archived-catalogue, inventory, and original-fetch programs/logs are enumerated in notes/category_bourbaki_r187_r230_date_audit.md.

At 04:00 UTC the concrete next source route consists only of the actual congress links advertised by item 664: records 802 (March 1956), 803 (June–July 1956), 804 (October 1956), and 805 (March 1957). Their contents have not yet been inspected by this agent. That prospective route is not counted as a completed source check here.
