# Targeted institutional manuscript-cote search for the Résumé

Search performed 20 November 2026 UTC by GPT-6 Astra Pro, agent `/root/geometry_dictionary`; reasoning-effort setting not exposed. This is a source-identification check, not a proof audit.

## Result and exact wording

The published source is identified: **CSG17**, Grothendieck's *Résumé de la théorie métrique des produits tensoriels topologiques*, original Boletim da Sociedade Matemática de São Paulo 8, pp. 1–79, catalogued as 1953; the verified original-pagination facsimile is the USP 1996 reprint, DOI **10.11606/resimeusp.v2i4.74836**. The article DOI, published-work catalogue identifier, and inspected scan leaves are exact bibliographic locators. They are not an unpublished-manuscript shelfmark.

**No separate unpublished Résumé manuscript cote was located in this targeted search. This does not establish that no manuscript exists. No additional unseen manuscript is used in the report's mathematics or historical crosswalk.**

Suggested report wording:

> The historical sources actually used are the published texts identified here by section, page, and scan. CSG17 is the published-work catalogue identifier for the Résumé; no additional unseen manuscript is used. A separate unpublished Résumé manuscript cote was not located in the institutional catalogues consulted. This is a search limitation, not a claim that no manuscript exists.

## Institutions and records checked

### Université de Montpellier

- Official public inventory: https://grothendieck.umontpellier.fr/archives-grothendieck/
- Institutional fonds description: https://grothendieck.umontpellier.fr/
- The HTML inventory was retrieved in full and stored as `work/geometry_sources/montpellier_archive_index.html`; extracted text is `montpellier_archive_index.txt`. The search service's simplified extraction omits many catalogue descriptions, so the actual HTML was also inspected.
- Exact-title fragments `Résumé de la théorie` and `théorie métrique` were absent from the retrieved public inventory text.
- A genuine nearby archival record is **Cote 1**, the functional-analysis dossier, catalogued as 149 pages of undated manuscript notes plus a 1953 letter. The catalogue supplies the viewer `../web/viewer.html?file=../1.pdf`, resolving to the institutional scan https://grothendieck.umontpellier.fr/1.pdf .
- **Cote 1 is not catalogued as the Résumé.** Its broad subject and date do not justify identifying it with that published text, or assigning its leaves to a theorem of the Résumé. No such identification has been made. A first-pass attempt to access its scan is recorded separately below.
- The inventory also contains later tensor-category files; those are not the metric tensor-product Résumé and have not been substituted for it.

### Bibliothèque nationale de France

- Direct catalogue reference found: https://archivesetmanuscrits.bnf.fr/ark:/12148/cc126317b . The search service received HTTP 403 on direct retrieval; the individual catalogue entries were therefore not read through that route.
- The BnF's own *Rapport d'activité 2023, entrées patrimoniales remarquables*, printed p. 7, PDF zero-based index 6 / one-based leaf 7, records the Grothendieck fonds as **NAF 29093**, acquisition **D. 23-21**: https://www.bnf.fr/sites/default/files/2024-06/rapport_2023_entrees_remarquables.pdf . This shelfmark is real, but it is a fonds identifier, not an identified Résumé manuscript.
- The BnF institutional discussion dates its newly received unpublished works to 1987–1999: https://www.bnf.fr/fr/les-mille-et-une-pages-de-grothendieck . The SMF's bibliography for the 2025 BnF lecture independently describes that date range and links the same catalogue ARK: https://smf.emath.fr/smf-dossiers-et-ressources/bibliographie-b-toen-bnf-2025?language=en . Neither source identifies the 1950s Résumé within this fonds. No inference that NAF 29093 is its manuscript cote is justified.

### Calames and the published-work catalogue

- Domain-targeted Calames searches for Grothendieck with Résumé/tensoriels did not identify a manuscript record for this title. Search results included other correspondence and category-theory archival records; those were not treated as substitutes.
- CSG's published-works page directly identifies the exact work as CSG17: https://csg.igrothendieck.org/published-works/ . The heading and its metadata were opened and read.
- Verified facsimile: https://revistas.usp.br/resenhasimeusp/en/article/download/74836/78406/100978 ; metadata page https://revistas.usp.br/resenhasimeusp/en/article/view/74836 . Its relevant exact scan leaves are already in the main archival crosswalk and `work/agent_geometry.md`.

## Search log

The following targeted queries were actually issued through the search service, followed by the direct opens and local inventory inspection described above:

1. `site.grothendieck.umontpellier.fr "Résumé" "tensoriels"`
2. `site.archivesetmanuscrits.bnf.fr Grothendieck "tensoriels"`
3. `site.calames.abes.fr Grothendieck "Résumé"`
4. `Grothendieck archives manuscrits Montpellier "Résumé de la théorie métrique" cote`
5. `site.grothendieck.umontpellier.fr "métrique"`
6. `site.grothendieck.umontpellier.fr "tensoriels"`
7. `site.archivesetmanuscrits.bnf.fr "Grothendieck" "Résumé"`
8. `site.calames.abes.fr "Grothendieck" "tensoriels"`
9. `site.archivesetmanuscrits.bnf.fr "Fonds Alexandre Grothendieck"`
10. `site.archivesetmanuscrits.bnf.fr "Grothendieck" "métrique"`
11. `"Résumé de la théorie métrique" "manuscrit"`
12. `site.grothendieck.umontpellier.fr "inventaire"`
13. `site.grothendieck.umontpellier.fr "Analyse fonctionnelle" "1"`
14. `"Grothendieck" "Résumé" "cote"`
15. `"Grothendieck" "NAF 29093"` (with a space between NAF and 29093 in the actual query)
16. `"Résumé de la théorie métrique" "archives"`

This is a targeted bibliography search, not an exhaustive folio-by-folio inventory of all surviving manuscripts or inaccessible correspondence. It supports the stated unlocated status only.

## Retrieval references for the parent

Opened primary records include Montpellier inventory `turn400005574view0` / `turn235823993view0`; CSG17 metadata `turn607755346view2`; BnF institutional description `turn607755346view3`; BnF acquisitions report and precise fonds entry `turn132225519view1` / `turn235823993view2`; SMF bibliography and catalogue link `turn141497995view0`. The parent should open the relevant URLs before citing these refs in its own final reply. Direct BnF catalogue retrieval returned 403 (`turn228283892view0`).

## Montpellier scan retrieval status

The institutional thumbnail `https://grothendieck.umontpellier.fr/1.png` was downloaded and visually inspected; it is an uninformative blank leaf, so it establishes no relationship to the Résumé. The linked 149-page PDF did not complete during the targeted check; the slow download was stopped at 2026-11-20 23:38:23 UTC and the incomplete file was marked `.pdf.partial`. No folio of that manuscript file was read, and no page-level identification of a Résumé manuscript is claimed. The public catalogue identification is independent of that incomplete retrieval.
