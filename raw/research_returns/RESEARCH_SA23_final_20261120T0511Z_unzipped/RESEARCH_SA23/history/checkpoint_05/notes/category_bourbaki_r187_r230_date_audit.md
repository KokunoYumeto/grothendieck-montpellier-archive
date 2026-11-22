# Bourbaki rédactions 187 and 230: bounded original-source comparison

Checked 2026-11-20 by crystalline_categories. This is a documentary content and dating-witness inspection, not a new proof audit of the compact-operator theorems.

## Result

Rédaction 187 / NBR090 was retrieved from the public Internet Archive copy of an advertised Mathdoc scan and all seven physical PDF pages were visually read: a modern catalogue cover plus six typed text pages. Its subject is the elementary compact-operator Fredholm alternative and discreteness of nonzero eigenvalues. It contains no determinant construction, spectral trace formula, genus-zero argument, letter, enclosure statement, or identification with Montpellier cote 1. Its first typed page has pencil wording “Schwartz” and what reads as “sept53”. This is an observed annotation, not independently authenticated authorship or a contemporaneous date of inscription. No date for the Montpellier sheets follows.

Rédaction 230 is positively identified by the primary Delsarte inventory as “Rapport sur la théorie spectrale. Partie I B. Opérateurs compacts et produits tensoriels topologiques”, BKI 05-3 EVT. Its original scan has not yet been obtained. No conclusion about its proof content, author, or date is drawn.

## Retrieval and inspected identifiers

1. Actual archived Mathdoc home catalogue, HTTP200, was read from the URL returned by the public availability API: http://web.archive.org/web/20261019212122/http://sites.mathdoc.fr/archives-bourbaki/ . Saved as sources/category_bourbaki_archived_catalogue.html, 13,806 bytes, SHA256 9ea4b28a451906b00310ea9e93430181d6608012debf5193c6333a0ef235bbac. It advertises feuilleter.php?chap=2_REDAC_EVT and feuilleter.php?chap=2.
2. The actual EVT catalogue response redirected to http://web.archive.org/web/20260615041415/http://sites.mathdoc.fr/archives-bourbaki/feuilleter.php?chap=2_REDAC_EVT . HTTP200, 17,582 bytes, SHA256 98ed351979f76db8e832f91ab2304e6aa6a6fc904291357e6358c6527c44a9ea. Saved sources/category_bourbaki_evt_catalogue.html. Its R187_nbr_090 row advertises ./PDF/187_nbr_090.pdf, seven pages. Thus the file identifier was established from a real catalogue link, not inferred from the number179/NBR082.
3. Public availability API response saved notes/category_bourbaki_r187_available.json. Ordinary archived playback wrapper then its advertised iframe produced the PDF at http://web.archive.org/web/20260812025911if_/http://sites.mathdoc.fr/archives-bourbaki/PDF/187_nbr_090.pdf . HTTP200 application/pdf, 3,541,813 bytes, SHA256 26bfd9a18b90ac467a0a2a7fe69093dbdea3de2aa847ddf24d92d711b335b8ec. Saved sources/category_bourbaki_r187_1.pdf. PDF metadata is digitization metadata, not a manuscript date.
4. Actual all-rédactions catalogue http://web.archive.org/web/20250520161218/http://sites.mathdoc.fr/archives-bourbaki/feuilleter.php?chap=2 , HTTP200, 60,705 bytes, SHA256 3ad263a0f4136e68e909084c40f276a4686d0ee253fbc6660800404ca193e06a, saved sources/category_bourbaki_all_redactions_0.html. Its displayed sequence ends around200/201 and the nomenclature entry. It has no230 row or advertised230 PDF. This bounds this particular publicly archived catalogue, not the holdings of every archive or the existence of a230 scan.
5. The official Delsarte list was already downloaded from https://iecl.univ-lorraine.fr/wp-content/uploads/2021/04/DELSARTE_archives_numeros_de_redactions_bourbaki_2005.pdf . Its physical page10 entry187 was viewed during the previous route; physical page12 entry230 was now rendered and directly viewed at sources/category_bourbaki_delsarte_page012.png. The entry supplies title and BKI05-3EVT, no date or author.

## Complete visual reading of187

| PDF page | Typed page | Directly observed content |
|---|---|---|
|1|catalogue cover|Rédaction187, NBR090, seven pages/seven sheets; cover title abbreviates the actual typed title.|
|2|1, unnumbered|Actual title Théorie élémentaire des applications linéaires complètement continues; compactness definition; ideal property; locally convex Hausdorff setting; Theorem1 on compact perturbation of a closed embedding; beginning of proof. Upper-left pencil Schwartz/sept53; top-right identifiers187/NBR090.|
|3|2|Completion of Theorem1 proof; Theorem2 on a weak quotient map satisfying compact convex lifting condition(K), with compact perturbation having closed image of finite codimension; dual proof begins.|
|4|3|Completion of Theorem2; Fréchet corollary; specialize to I+v; finite-dimensional kernel and finite-codimensional closed image; stabilization lemma for successive subspaces and nonzero scalars bounded away from zero.|
|5|4|Proof of stabilization lemma, first normed case and then reduction by a continuous seminorm.|
|6|5|Completion of lemma; Bochner–Weil remark; Proposition1 and Proposition2 comparing kernel dimension and image codimension of I+v.|
|7|6|Equality corollary; Proposition3, finitely many eigenvalues outside any disk about zero; proof by stabilization lemma; closing instruction that the universal editor should combine propositions1–3 and earlier corollary into Theorem3.|

All these page images were opened individually, including margins. The first-page pencil annotation was also read in enlarged rendering sources/category_bourbaki_r187_pages/page_02_margin.png. This is not a claim that every faint character or the initial preceding Schwartz was palaeographically authenticated. No mathematical proof is reclassified merely because the source was read.

## Search and access bounds

Two search engines were used for exact combinations of Bourbaki,230, spectral-report title, compact operators, topological tensor products, and BKI05-3. The official Delsarte inventory was the only positive exact230 identification. Unrelated public Bourbaki seminar exposé230 was not confused with rédaction230. Search output is retained in notes/category_bourbaki_adjacent_web_records.json.

The live AHP archive had previously returned a bot challenge. No further requests to that host were made and the challenge was not executed. The independent archived Mathdoc catalogue and explicitly advertised archived scan were read publicly. No registration, credentials, withheld material, or contacts were used.

## Programs and retained outputs

- code/category_bourbaki_archived_catalogue.py and logs/category_bourbaki_archived_catalogue.txt.
- code/category_bourbaki_evt_catalogue_fetch.py and matching log.
- code/category_bourbaki_adjacent_fetch.py and matching log: two independent advertised catalogue/PDF fetches, API responses, wrapper and payload hashes.
- code/category_bourbaki_r187_render.py and matching log: pdfinfo, native text extraction, seven page renderings and OCR.
- code/category_bourbaki_r187_margin.py and matching log: enlarged original annotation and Delsartep12.
- sources/category_bourbaki_r187_pages/page_01.png through page_07.png; notes/category_bourbaki_r187_pages/*.txt; notes/category_bourbaki_r187_full.txt.

Tesseract could not load its French language file and fell back to English; stderr is preserved. OCR is a finding aid only and all content findings above use direct images. Source PDFs and page images reside under sources/ so reproducible caches are excluded consistently by the checkpoint policy. Author-created notes and all programs/logs are retained.


## 03:53UTC continuation — exact230 original obtained; content inspection in progress

This paragraph supersedes the original-unopened state above for rédaction230. The earlier bounds describe the first retrieval stage, not a current claim of unavailability.

The official full Delsarte BKI inventory was opened via its advertised IECL link: https://iecl.univ-lorraine.fr/wp-content/uploads/2021/04/DELSARTE_archives_Bourbaki_cote_BKI.pdf . The web reader returned403, but a single ordinary anonymous urllib download succeeded HTTP200 with no challenge or authentication. Saved sources/category_bourbaki_r230_bki_inventory.pdf,409,377bytes,SHA25648576997942931cae6bad76a891931477cd5f89da9a391742e252bebf00eeb60. Its printedp61 (directly viewed at sources/category_bourbaki_r230_bki_inventory_p61.png) supplies IECNR BKI05-3.1, IECN230, pagination88–242f. It gives no author or date for this entry. The official repository page was opened at https://iecl.univ-lorraine.fr/l-iecl/bibliotheque/archives-delsarte-bourbaki/ ; it describes on-site appointment consultation and publicly advertises inventory PDFs and the two digitized portals. Nobody was contacted.

A separately public Internet Archive snapshot of the AHP homepage was obtained from the archive.org availabilityAPI. No request was made to the blocked live AHP host. Actual cached homepage at http://web.archive.org/web/20261029104253/https://archives-bourbaki.ahp-numerique.fr/ says the public corpus was extended after2023 to1954–1973, and advertises /redactions. That archived page advertises subject links; its Théories spectrales link returned the catalogue snapshot20250209112923, saved sources/category_bourbaki_r230_subject_spectral.html. It positively lists item664 and the exact PDF r230_iecl_bki05-3.pdf. All links were followed on web.archive.org; the final scripts reject any redirect outside that host.

The detailed original catalogue record was read at http://web.archive.org/web/20240917194937/https://archives-bourbaki.ahp-numerique.fr/items/show/664 . It attributes the report to Jean Dieudonné, gives1956-03, and explains the date evidence: **a different copy at the ENS library bears the handwritten wording Dieudonné mars1956 on its first page**. That ENS copy has not been opened. The downloaded copy is identified as the IECL/Delsarte copy, IECNR BKI05-3.1, digitizedJune2019. The catalogue's date is therefore explicitly reported evidence about a different copy, not a date mark directly observed in this scan.

The actual advertised archived PDF was obtained HTTP200 at http://web.archive.org/web/20260213200334if_/https://archives-bourbaki.ahp-numerique.fr/files/original/49e6e904fbc99a10207673c09e068fa7.pdf . Saved sources/category_bourbaki_r230_original_1.pdf,29,100,237bytes,SHA2562ecd5627b5e9878a362a237fcadbac6ccdbb85e076551d7c4f6f37d31f19eba1. It has156physicalpages, is image-only, and has2019digitization metadata. Directly viewed so far: physical1 (original title and contents) and physical2 (typedp88 Commentaires). The comments say most of the chapters derive from Grothendieck's thesis with improvements and simplifications from Schwartz's1954seminar. This refers broadly to published/thesis material; it does not identify Montpellier cote1 or its trace leaves.

The actual contents locate ChapterIII§3 on compact operators in a Hilbert space atpp188–203, and §4 on Fredholm theory for nuclear operators atpp204–221. The catalogue description calls the latter §5; the original contents say§4. Its substantive pages have not yet been inspected at this checkpoint. Physicalp2=typed88, so the intended ranges are physical102–117 and118–135, subject to checking actual intervening numbering.

New retained programs/logs: category_bourbaki_r230_archived_portal, category_bourbaki_r230_redactions_fetch, category_bourbaki_r230_subjects_fetch, category_bourbaki_r230_bki_inventory, category_bourbaki_r230_inventory_render, category_bourbaki_r230_original_fetch, category_bourbaki_r230_front_render. Their corresponding code/ and logs/ files preserve exact URLs, redirects, status, hashes, commands and outputs. All rawPDF/PNG/HTML caches are under sources/. New search/open responses are notes/category_bourbaki_r230_web_records.json. No bibliography or core-section change was made during the checkpoint freeze.
