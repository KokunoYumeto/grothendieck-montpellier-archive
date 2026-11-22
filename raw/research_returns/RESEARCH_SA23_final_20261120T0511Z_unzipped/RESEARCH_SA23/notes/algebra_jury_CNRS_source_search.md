# Bounded new thesis-jury / CNRS assessment route

Current-run documentary audit, 20 November 2026, approximately 03:56–04:02 UTC. This follows, and does not repeat, the earlier SUDOC/BCPR holding audit in `algebra_thesis1953_source_search.md`.

## Result and exact limitation

No original 1953 Grothendieck thesis, original jury report, or early CNRS assessment identifying the Hilbert trace/genus-zero proof was opened. No item-level archival description located in this branch names that proof, its omitted chapter, an enclosure, or the cote 1 leaves. The manuscript-date conclusion is unchanged. The branch does identify an independently public institutional thesis list, actual public archival series descriptions, and a misleading “Rapports” search hit which the primary catalogue expressly resolves as Bourbaki mathematical material.

## 1. Paris-Saclay / IMO historical Paris thesis list

Opened and downloaded the complete publicly rendered list “Thèses soutenues à Paris (1864–1971)” at:

<https://bibliotheque.imo.universite-paris-saclay.fr/bibliotheques-numeriques/theses/Paris/?critere=auteur>

This is a distinct digital-library route, with links for some listed theses to Numdam, Numaclay or SorbonNum, rather than a repeat of the known SUDOC record. The saved HTML has 110,874 bytes; the complete extracted text has 32,804 characters. A case-insensitive search of the full extraction found no `groth` occurrence, and the five `tensor` occurrences concern other entries. The linked-title inspection found no Grothendieck or relevant tensor-product thesis link. This establishes the result of this particular list inspection; it does not establish that no digital thesis exists elsewhere or that the list is exhaustive.

Source files: `sources/algebra_jury_imo_paris_theses.html/.txt`. Retrieval/hash log: `logs/algebra_jury_fetch54.json`.

## 2. Primary Sorbonne archival guide: the actual scope and access boundary

Opened in the web reader and downloaded:

<https://www.sorbonne-universite.fr/universite/archives>

The guide’s **“État des fonds – Archives nationales et autres établissements / Faculté des Sciences”** identifies **AJ/16/5120–5828, Faculté des sciences de Paris (1821–1959)**, and separately **20130097/1–118, Registres de scolarité (1901–1965)**. These are series locators, not opened Grothendieck files.

Under **“Ressources en ligne”**, the institution states that there is presently no detailed inventory or searchable nominal database for individual former-student files; the relevant boxes must be examined manually. The guide further explains that some Archives nationales instruments are not integrated into the online inventory system. I did not contact the institution, request an appointment, access an account, or represent the published series description as access to its original contents.

A search result for a scholarly study of all Paris juries from August 1944 to August 1961 gives the narrower report-series reference **AJ 16 5553–5567** for 1944–1959:

<https://sms.univ-tlse2.fr/servlet/com.univ.collaboratif.utils.LectureFichiergw?ID_FICHE=127805&ID_FICHIER=1317125398026&INLINE=FALSE>

That statement was returned in a searchable excerpt (printed p. 6). **Neither the complete study nor the underlying archival reports were opened in this branch.** It is retained as a source-qualified research lead, not as primary evidence about Grothendieck’s own report. Exact quoted-number searches did not locate a public scan or Grothendieck-specific item. The date/title of a thesis or an annual report-series range would in any case not by itself date the particular cote 1 proof.

The official Sorbonne page is saved as `sources/algebra_jury_sorbonne_archives.html/.txt`, with status, SHA-256 and timing in `logs/algebra_jury_fetch55.json`.

## 3. Actual linked primary catalogue: science dean’s cabinet

Followed the Sorbonne guide’s link **6 UPFS** to:

<https://calames.abes.fr/pub/ms/FileId-5518>

The web reader timed out, but one ordinary anonymous local retrieval succeeded. I read the complete 5,047-character text of the catalogue page. It describes **Cabinet du doyen de la Faculté des Sciences de l’Université de Paris, 1929–1966**, two boxes / 0.22 linear metres; the fonds concerns solicitations and informational submissions. The listed subdivisions concern events, ceremonies, university/institutional/international relations, operation of the faculty, a memorial plaque and historical studies. The description does not name Grothendieck, a doctoral assessment, the trace/genus-zero proof, or an enclosure. It records consultation by appointment and that the fonds was inventoried in 2025. **The underlying archival papers were not opened.** No contact was made.

Saved primary catalogue: `sources/algebra_jury_calames_science_dean.html/.txt`.

## 4. False-positive “Rapports” lead resolved by the primary catalogue

The Persée Laurent Schwartz authority page, <https://www.persee.fr/authority/416864>, exposed a Calames item **HC 12/8, [088] Rapports (1947 à 1951), 136 feuillets**. Before reading its hierarchy this title could be mistaken for evaluations. The legitimate public Calames full-text search for the exact shelfmark returned its parent **HC 12/8–HC 16/2, Groupes et algèbres de Lie**. I then followed the actual Persée-supplied record URL:

<https://calames.abes.fr/pub/ms/Calames-2025061317113412349>

The complete primary catalogue page was retrieved and read. Its hierarchy is **Fonds Henri Cartan → Bourbaki → Groupes et algèbres de Lie → Rapports**. Its content description names real/complex analytic varieties, differentiable varieties (including February 1947 notes), a Schwartz report connected with the June 1948 congress, prolonged varieties, and Schwartz’s Lie-algebra formulas of June 1951. It does **not** describe a thesis-jury or CNRS assessment. This classification is grounded in the actual catalogue, not inferred solely from the generic title or the fact that Schwartz is indexed.

The original 136 archival folios were not opened. The catalogue’s reproduction/consultation conditions were respected; no request was sent. The item is excluded from the sought assessment route on the strength of its stated subject, without asserting that all related Cartan files lack relevant material.

Saved files: `sources/algebra_jury_persee_schwartz.html/.txt`, `algebra_jury_calames_HC12_8.xml`, and `algebra_jury_calames_cartan_reports.html/.txt`.

## 5. CNRS and other search bounds

Targeted public searches for Grothendieck with CNRS, early evaluation, archival dossier and the relevant year range produced no specific early assessment locator. Results concerning a CNRS agents-born-1921 series, unrelated social-science fonds, Montpellier degree records, and Paris Faculty of Letters records were not treated as Grothendieck evidence. Broad biographical claims about his CNRS years were excluded as incapable of identifying this proof. Previously inspected Dieudonné correspondence/EGA inventory sections, general Schwartz correspondence descriptions, and the SUDOC holding were not represented as new opened originals.

This is a bounded failure to locate the necessary public witness, not proof that the assessment never existed. The concrete outstanding documentary step would be a publicly supplied original report or a sufficiently specific item description, followed by a content comparison with the particular trace/genus-zero argument. No unreviewed archive request or contact is proposed as completed work.

## Reproducibility and access flags

- Raw query/open/click responses: `notes/algebra_history_web115.json` through `126.json`, each with a recorded UTC retrieval timestamp.
- Exact independent retrieval scripts: `code/algebra_jury_fetch54.py` and `code/algebra_jury_fetch55.py`.
- Their complete outputs, statuses, byte counts, hashes and elapsed times: corresponding `logs/algebra_jury_fetch54.json/.txt` and `algebra_jury_fetch55.json/.txt`.
- Script 55 initially stopped before network access because `bs4` was unavailable; it was changed to Python’s standard-library `HTMLParser` and then run successfully. The initial error is retained separately in `logs/algebra_jury_fetch55_initial_failure.txt`.
- A fresh allowed-type documentary event, **“used and rechecked in this run”**, is appended under existing statement ID `geo-H-history`; no new mathematical result, numbered statement or bibliography entry is added.

**Opened:** the public thesis list, Sorbonne institutional guide, Persée metadata page, exact Calames search response, and the two specified primary catalogue descriptions. **Not opened:** original 1953 thesis, original jury/CNRS assessments, original Cartan report folios, original dean’s cabinet papers, and the complete scholarly jury study. No date gate was closed.
