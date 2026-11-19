# Part B: continued primary-source retrieval, 19 November 2026

Researcher: GPT-6 Astra, OpenAI, ChatGPT Pro mode, agent `part_b_cycles`. This follow-up supplements the independent audit in `notes/secondary_source_retrieval_20261119.md`. It distinguishes actual theorem text from metadata, and mathematical proof from the prompt's demand for particular original articles.

## New original texts opened

| Work | Exact source and opened material | Consequence |
|---|---|---|
| Hartshorne1970, *Affine duality and cofiniteness* | Göttingen original scan of Inventiones9, https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0009/PPN356556735_0009.pdf; articlepp145–164 extracted to `sources/hartshorne1970.pdf`; §3pp149–151 visually opened as `qa/hartshorne1970_p149.png`–p151; webref `turn760234705search12`. | Historical source of the local-cohomology counterexample now directly verified. The original uses k[x,y][[u,v]]/(xu+yv); the manuscript supplies its own complete polynomial-ring variant and does not assume an unproved completion comparison. |
| Bhatt–Mathew2021, *The arc-topology* | Full authorv4 PDF https://arxiv.org/pdf/1807.04725, dated14December2020; `sources/bhatt_mathew_arc.pdf` and text; opened webref `turn760234705view1`. Theorem5.4,p38; Theorem6.4,p48; Cor6.10,Thm6.11,Rem6.12,p50; Rem6.13,pp50–51. Published metadata on Mathew's author page confirms Duke170(2021),1899–1988. | The completion-complement theorem now has its full modern intermediate proof opened and its formal-glueing deduction written. Remark6.12 explicitly restricts Fujiwara1995 to the noetherian case and attributes the generalization to Gabber. This is not opening the1994/1995 originals. |
| Kleiman1994, *The standard conjectures* | Original18-page chapter, https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische1994.Kleiman.Standard.Conjectures.pdf; `sources/kleiman1994.pdf`, full OCR text; webref `turn239821777view0`. Printedpp16–18 visually opened, especially Proposition4-3(2)(c),p16, and Proposition5-1,p17. | Confirms the abelian Lefschetz theorem and the precise homological-positivity hypothesis in the classical implication to D. Both exact citations now occur in B.1(b). Full OCR took191.549381555seconds; that is source-processing time, not a mathematical finite-check runtime. |

## Public DOI and repository metadata

Script `code/part_b_oa_discovery.py`, output `code/part_b_oa_discovery_output.json`, made six public requests: Crossref, OpenAlex and SemanticScholar for each of Gabber1994 DOI10.1007/BF02773001 and Fujiwara1995 DOI10.1215/S0012-7094-95-08002-8. Every request returned metadata successfully.

- Both OpenAlex records reported `is_oa=false`, `oa_status=closed`, `any_repository_has_fulltext=false`, and no best open location.
- Both SemanticScholar records had an empty open-PDF URL with statusCLOSED.
- Crossref lists only the known Springer and ProjectEuclid publisher URLs. A text-mining link is not treated as a grant of subscription access.
- Fujiwara's record also identifies the historical Euclid item `euclid.dmj/1077245853`. This supplied a legitimate new archive search target.

These metadata statements are evidence about the services' records, not a proof that no lawful copy exists anywhere.

## Public web archives

Script `code/part_b_public_archives.py`, output `code/part_b_public_archives_output.json`, checked InternetArchive's public Wayback availability API for:

1. `https://link.springer.com/content/pdf/10.1007/BF02773001.pdf` — no snapshot returned.
2. `http://projecteuclid.org/euclid.dmj/1077245853` — a public2020 landing snapshot was reported: `https://web.archive.org/web/20200812020402/https://www.projecteuclid.org/euclid.dmj/1077245853`.
3. `http://projecteuclid.org/download/pdf_1/euclid.dmj/1077245853` — no snapshot returned.
4. `https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8` — no snapshot returned.

The first opening of the advertised landing snapshot failed with HTTP503; this outcome is saved in `code/part_b_archived_landing_output.json` (web tool also failed, ref `turn104997922view0`). A later bounded retry succeeded, as recorded below. The earlier failure is preserved rather than overwritten.

## Whole-journal and institutional archive route

A fresh search located the InternetArchive journal collections. Public catalogue queries and record metadata were read, with outputs in `code/part_b_archive_volumes_output.json`, `code/part_b_archive_metadata_output.json`, and `code/part_b_archive_followup_output.json`.

- The IsraelJournal collection exists, but searches for year1994 and volume87 returned zero public items. The collection's public periodicals metadata lists institutional subscription providers; it does not provide an original article file.
- Duke1995 public results contain the four annual contents items. Volume80's contents explicitly link to the exact required issue, `https://archive.org/details/sim_duke-mathematical-journal_1995-10_80_1`.
- The exact issue's public metadata marks **access-restricted-item=true** and marks its PDF and OCR **private=true**. No private file was requested. This route therefore did not open Fujiwara.
- The AmericanJournal1968 public result is the volume90 index. Its advertised next issue likewise has restricted PDF/OCR metadata. The public index is not counted as reading Lieberman1968.

Search references include `turn787288422search2`/`search9` for the journal preservation catalogues; the actual holdings/restrictions above come from the saved public InternetArchive metadata responses, not an inference from those catalogue descriptions.

Additional exact-title, British/American-spelling,1992-preprint, DOI, author-page, HAL/EUDML/MPIM and whole-volume searches produced bibliographies or metadata, not original texts. The UniversityofTokyo public2024 Fujiwara60 conference site (`https://sites.google.com/view/fujiwara60`, ref `turn800321410view0`) contains a program and abstracts, not a historical-paper archive. No login, credential substitution, paywall bypass, anti-bot bypass, or restricted archive download was attempted.

## Final bounded repository and archive checks, 12:46–13:00 UTC

The six further public repository requests are fully saved in `code/part_b_repository_discovery_output.json`, generated by `code/part_b_repository_discovery.py`.

| Work | Service | Observed result | Request time (seconds) |
|---|---|---|---:|
| Gabber1994 | HAL DOI search | HTTP200, zero records | 4.963 |
| Fujiwara1995 | HAL DOI search | HTTP200, zero records | 5.179 |
| Gabber1994 | OpenAIRE DOI search | HTTP200, one record, CLOSED; no new full-text location | 27.385 |
| Fujiwara1995 | OpenAIRE DOI search | HTTP200, one record, OPEN at the already known historical Euclid landing URL; no new PDF location | 27.263 |
| Gabber1994 | Fatcat public DOI lookup | HTTP503, no record read | 10.277 |
| Fujiwara1995 | Fatcat public DOI lookup | HTTP503, no record read | 10.310 |

OpenAIRE's OPEN flag conflicts with OpenAlex/SemanticScholar. It is not discarded, but does not establish that the theorem text was accessible. In particular the following direct evidence is stronger than an access-label inference:

- Public Wayback CDX query for archived PDFs at `projecteuclid.org/*1077245853*` returned HTTP200 and the empty list, in6.222seconds (`code/part_b_wayback_followup_output.json`). This is only a statement about that query, not every possible archived URL.
- Retrying the advertised 2020 landing snapshot succeeded with HTTP200,60,164bytes in6.262seconds. A subsequent fetch saved the complete HTML in `sources/fujiwara1995_archived_landing.html` and readable text in the matching `.txt`; its elapsed time was9.235122544seconds (`code/part_b_archived_tags_output.json`). The page explicitly displays **“Full-text: Access denied (no subscription detected)”**. It gives the title, author, Duke80(1),15–57, DOI10.1215/S0012-7094-95-08002-8, and the already known publisher PDF URL. No archived original theorem was thereby read. The web-search tool itself still failed to render this snapshot (`turn807606659view1`); the saved ordinary HTTP response is the actual evidence.
- The current Euclid download response saved as `sources/fujiwara1995_alt.download` is an **Incapsula anti-bot HTML page**, not a PDF. This current failure and the archived subscription denial are different observations. No bypass was attempted.
- Gabber's current official Springer page was reopened (`https://link.springer.com/article/10.1007/BF02773001`, `turn546461080view0`). It expressly labels subscription content, offers purchase/institutional access, and states that a SharedIt link is unavailable. The official Hebrew University journal homepage (`https://math.huji.ac.il/~ijmath/`, `turn546461080view1`) advertises table-of-contents indices and directs online editions to Springer. The official volume87 contents (`https://math.huji.ac.il/~ijmath/index_pdf/87.pdf`, `turn750236603search28`) identify the article atp325 but are not its text.

Fresh primary-source searches were also made for `"Gabber" "Affine analog" pdf`, `"Fujiwara" "tubular" "1992" preprint`, each exact DOI, the exact Fujiwara title with PDF, and the Israel87(1994) page325 citation. Returned useful primary records were the official journal contents, author profile, NDL bibliographic record, and the already opened Stacks/HHW papers; no new original copy appeared. Reference groups: `turn433147575search0`–`search11` and `turn750236603search0`–`search33`. Search hits were not treated as reading the cited full texts.

The six repository request times above sum to85.377seconds. That is a sum of recorded individual request durations, not wall-clock research time or mathematical proof time. The numerical/formal mathematical certificate remains `code/part_b_finite_checks.py`, whose independent saved runtime is0.11084066100011114seconds. Its exact scope and126/114 monomial,5chart and symbolic-family counts remain in `notes/part_b_audit_addendum.md`.

## Exact title and hypotheses audit

The source required for completion-complement rigidity is Fujiwara's **1995 _Theory of tubular neighborhood in étale topology_**, Duke80(1),15–57. It is not his1997 _Rigid geometry, Lefschetz–Verdier trace formula and Deligne's conjecture_, Inventiones127,489–533. Bhatt–Mathew Remark6.12 explicitly reports the1995 original's **noetherian** hypothesis and attributes the generalization to Gabber.

Our affine theorem permits an arbitrary commutative ring and arbitrary ideal, with the henselian-pair condition including containment in the Jacobson radical; no restriction on torsion primes is present. The completion-complement theorem permits arbitrary rings but requires the ideal finitely generated. Those full modern hypotheses are verified in the opened Stacks and HHW/Bhatt–Mathew texts. We do **not** claim to have verified Gabber1994's exact original hypotheses from a bibliographic abstract or the zbMATH summary carried by OpenAIRE. The manuscript states this source distinction explicitly.

## Precise remaining gate

The mathematical affine rigidity theorem is available through the fully opened Stacks proof, and completion-complement rigidity through the opened HHW and Bhatt–Mathew proofs. Their applications and the necessary hypotheses are written in the manuscript.

The task's distinct demand to inspect and derive the result **directly from Gabber1994 §5Corollary1 and Fujiwara1995 Corollary6.6.4 remains unresolved**. Both original bibliography entries continue to say **original full text not opened**. Lieberman1968 likewise remains marked not opened; every actual use of the abelian Lefschetz theorem instead cites the opened Kleiman1968/1994 originals. A supplied lawful copy or newly located public institutional copy would close these reading requirements; no unavailable statement has been promoted to a direct original-source verification.


## Required SGA collections fetched and opened, 13:06–13:14 UTC

The literal source-fetch audit located full scholarly archive copies of SGA4,4½,5 and6. This is additional source-delivery work; the earlier mathematical proofs did not rely on a mistaken identification of Toen's later `sga6.pdf` with the original book.

| Required collection | Saved complete available file | Actual bounded reading and locators |
|---|---|---|
| SGA4, tomes1–3 | `sources/sga4_complete_reedition.pdf`,874pages, Orgogozo version71766d9 dated30July2024; https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf; webref `turn315778431view0` | Previously opened XII,XIV,XVI,XVIII; now additionally VI Proposition9.0 and its entire proof, reeditionpp464–466. This is the local-coherence/enough-points result. |
| SGA4½ | `sources/sga4half_original.pdf`,316-page original scan; https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf | Introduction and contents; Theoremes de finitude, Theorem1.1 and Corollary1.5, originalpp233–234, visually read. Original base is regular noetherian of dimension0 or1, narrower than the ILO theorem used. |
| SGA5 | `sources/sga5_original.pdf`,496-page original scan; https://library.slmath.org/nonmsri/sga/sga5/SGA5.pdf | Introduction and contents; IIIp73; Theorem4.4p102; Lefschetz–Verdier Corollaries4.7–4.8p109, visually read. These give the original finite-coefficient proper-compatibility/trace statements; the manuscript uses Varshavsky for its current Q_l formulation. Illusie's one-page III erratum correctingp98 andp124 also opened from his author page, webref `turn394378884view1`. |
| SGA6 | `sources/sga6_original.pdf`,702-page original scan; https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf | Introduction and contents; IIITheorem1.1/Lemma1.1.1pp222–223; relative pseudo-coherencep229; Conjecture2.1/Theorem2.2pp236–237; Scholium2.6p241. The book proves the noetherian-base/projective finiteness cases and explicitly leaves the general proper case conjectural; later Kiehl/Lipman–Neeman is a substantive additional input. |

The initially advertised IAS/Stein PDF endpoints returned six403 responses; no access parameters were altered. The independent advertised SLMath archive and Orgogozo edition then returned four valid PDFs. Both manifests are preserved: `code/part_b_fetch_required_sga_output.json` and `code/part_b_fetch_required_sga_mirrors_output.json`. Complete source URLs, sizes, page counts, SHA256s and individual times are included. Whole successful batch wall time93.05661828400116seconds. Original archive/source landing pages opened as `turn904141903view0` (DeligneIAS), `turn904141903view1` (Stein), `turn201054793view0` and `turn897438494view0`–`view1` (SLMath). Web PDF parsing was limited by large file size; ordinary public downloads and local page rendering succeeded.

The full volumes were fetched, but only the passages listed above are represented as read or checked. The primary-source bibliography now includes separate SGA4Complete/SGA4Half/SGA5/SGA6 entries; no claim of having verified every theorem in thousands of pages is made.


## Lieberman1968 and the exact Raynaud thesis: new metadata routes

At the literal named-source audit, the independently checked Paris-Saclay institutional catalogue identifies Raynaud's thesis as **Faisceaux amples sur les schemas en groupes et les espaces homogenes**, Paris1968; its published form is SpringerLNM119(1970). The exact catalogue entry is at https://bibliotheque.imo.universite-paris-saclay.fr/bibliotheques-numeriques/theses/Paris/ (independent refs `turn660614806view1`, `turn178881246view1`; independently reopened here as `turn595050097view2`). The official book record is https://link.springer.com/book/10.1007/BFb0059504 (`turn513261720search4`). This is neither the opened Picard1970 article nor LNM169 *Anneaux locaux henseliens*. C's detailed primary identity/frontmatter audit is `notes/part_c_required_originals.md`.

A new bounded eight-request public metadata batch (`code/part_b_fetch_named_metadata.py` and matching output) checked OpenAlex, HAL, OpenAIRE and InternetArchive for each of Lieberman DOI10.2307/2373533 and Raynaud DOI10.1007/BFb0059504. Whole-batch elapsed time33.071762045998184seconds. Both OpenAlex entries report CLOSED/no repository full text; both HAL queries return zero. Both OpenAIRE requests timed out (27.678458291 and26.719467634seconds), so no access conclusion is inferred from them. The exact-title InternetArchive query found zero Lieberman article records and one Raynaud book record.

The Raynaud record is https://archive.org/details/faisceauxampless0000rayn. Its public metadata was read in6.912482088999241seconds and saved as `code/part_b_raynaud_archive_output.json`: access-restricted-item=true, PDF/EPUB/OCR files private=true. The public-looking LCP files are explicitly encrypted lending files, not unrestricted originals. No content file was requested and no decryption/borrowing attempt was made. Its catalogue gives the author as Michele; that metadata error is not used to override the primary publisher's Michel. OpenAlex also advertises a CERN catalogue record, https://cds.cern.ch/record/1690769, which the web tool could not open (`turn883495219view0`); this does not establish an accessible source file.

Additional new bounded routes were the Gottingen digitization catalogue for AmericanJournal1968/Lieberman, institutional-domain exact-title searches, and the advertised SLMath alternate-book list (`turn195956159view0`). They returned references/catalogues, not either required original. A commercial preview and unrelated later Raynaud Bourbaki talk are not substituted for the thesis. The remaining source gates are maintained explicitly.


The exact advertised CERN catalogue URL was then requested by the saved standalone utility `code/part_b_cern_record.py`. HTTP200 returned7,513bytes in9.607086445seconds, but visual/text inspection identifies an **Anubis automated-access challenge**, not the catalogue record. This is saved as `sources/raynaud_cern_catalogue.html` and `code/part_b_cern_record_output.json`; no challenge code was executed, no proof-of-work was performed and no bypass or guessed file URL was attempted. The semantic failure is retained alongside the successful HTTP status. The eight-request batch and this follow-up do not close the original-text reading requirement.

After checkpoint03, bibliography metadata warnings were corrected without changing source status: publishers for Kleiman1968, Deligne-Milne, Voisin2010 and Raynaud1966; SGA5 editor Illusie with Grothendieck direction in the note. The distinct `BRaynaudThesis1970` entry is explicitly partial-only. The exact attached-input correction table now has21rows, including prompt233's thesis identity and publication-year refinement.


## New collection and thesis routes after the A6 audit

The public RIMS preprint catalogue was inspected directly for1991–1995, following advertised annual links from https://www.kurims.kyoto-u.ac.jp/preprint/preprint_y1992.html. All five annual pages opened; searches within each found neither FUJIWARA nor TUBULAR. URLs are the same advertised stem with years1991,1992,1993,1994,1995, not guessed content-file paths. Exact opening refs: `turn869383634view0` and `turn998517943view1`–`view4`; find refs `turn753724292view0`–`view1` and `turn163082626view0`–`view7`. This is a negative result for these five catalogues, not a claim that no preprint ever existed.

Fujiwara's official Nagoya profile (`turn869383634view1`) confirms his Tokyo doctorate in October1994. A new NationalDietLibrary thesis search resolves that thesis to the *different* work on rigid geometry, Lefschetz–Verdier and Deligne's conjecture: https://ndlsearch.ndl.go.jp/en/books/R100000039-I3115841, opened `turn998517943view0`. Its metadata says access is through restricted digitized transmission to registered eligible users. No thesis content was requested; its subject is not substituted for the required1995 tubular-neighbourhood paper. The earlier1997-versus1995 title distinction is thus corroborated by an additional primary record.

These were web-tool catalogue/metadata readings, not standalone executed source-fetch programs. Search/read elapsed times were not recorded as research runtimes; no retrospective estimates are supplied. Search groups include `turn385628497search*`, `turn869383634search*` and `turn753724292search*`; unrelated nonmathematical and citation-only results were not used as theorem evidence.

## Public IHES historical archive: new bounded Gabber route

The public archives landing page https://archives.ihes.fr/ opened as `turn339334598view0`. Its advertised historical preprint collection https://omeka.ihes.fr/collections/show/59 opened as `turn546429686view0`; the actual public search form https://archives.ihes.fr/items/search opened as `turn546429686view1`. The form advertises its GET search action and collection controls. The collection describes the institute's historical preprints through2002; it is an appropriate new public route for the1994 Gabber paper, not a guessed private file path.

The saved utility `code/part_b_ihes_archive_search.py` first read the actual form and then made two ordinary searches restricted to collection59. Three requests took27.34997928499797seconds total; the individual durations are5.83024454,10.878306365 and10.641266258seconds in `code/part_b_ihes_archive_search_output.json`. All returned HTTP200 and their HTML/text were retained.

- The Gabber query returned four records: BBD *Faisceaux pervers* (M_83_62); Deligne's1981 purity exposition after Gabber (M_81_08); Lafforgue's2002 grassmannian paper (M_02_31); and Gromov's1999 topological-invariants paper (M_99_80). None is the1994 affine analogue paper. No unrelated PDF was downloaded as a substitute.
- The Affine query returned one unrelated1976 Ruelle physics preprint.

The same saved utility, with `--global-search`, reused the advertised form and queried the public exact-match search across Item and File records for **Affine analog** and **changement de base**. Both returned HTTP200 and **zero results**. The two requests took12.019484579002892seconds total, individually6.60557 and5.412469059seconds; the complete responses are preserved in `code/part_b_ihes_archive_global_output.json`. Web-tool rendering of two query URLs failed (`turn638029585view0`, `turn638029585view1`), whereas the ordinary public HTTP responses were successfully read. Those outcomes are recorded separately.

This bounded catalogue search produced no original Gabber theorem text. Gabber1994, Fujiwara1995, Lieberman1968 and the mathematical text of RaynaudLNM119 remain the four named-original reading requirements. The corresponding mathematical statements already derived from opened sources retain their status. No access challenge, private file, subscription restriction or robot check was bypassed.

## Further public thesis catalogue and DOI-free repository searches, 13:47–13:50 UTC

The CSG Istituto Grothendieck scientific-biography page was opened at https://csg.igrothendieck.org/scientific-biography/ (`turn841622216view0`). Its thesis catalogue at lines85–109 provides actual source links for several other theses, but the MichelRaynaud1968/LNM119 entry atline93 has **no linked original**. The advertised Jouanolou link was followed and is only that separate authorized thesis-transcription project (`turn988829369view0`), not a collection with a Raynaud scan. The same institution's complete public articles/books catalogue, https://csg.igrothendieck.org/articles-and-books/ (`turn988829369view1`), was opened; searches for Faisceauxamples, Lieberman, Affineanalog and Fujiwara each returned no matching text (`turn461918376view0`–`view3`). No unadvertised file path was guessed.

Fresh exact-title searches restricted to HAL/theses and Gallica produced the already checked Paris-Saclay catalogue, citation-only records and unrelated works, not a new original. One search-engine batch returned “Found no tool response”; that is recorded as a tool failure, not evidence of absent records. The subsequent functioning engine batch is `turn577320598search0`–`search34`. Search summaries were not treated as opened theorem text.

To remove a limitation of the earlier DOI searches, the saved utility `code/part_b_hal_title_search.py` queried HAL by **title without any DOI condition**, allowing older preprints or the1968 thesis to be found even if they lack journal identifiers. All four queries returned HTTP200 and zero records: “Affine analog”, “Theory of tubular neighborhood”, “Numerical and homological equivalence”, and “Faisceaux amples”. The exact requests and full JSON responses are saved in `code/part_b_hal_title_search_output.json`. Whole-batch wall time10.61962721600139seconds; individual times10.585650686,10.568037985,10.262979602 and10.529325546seconds in the same order. No content file was requested. This closes that specific repository-query gap, while leaving all four original-text reading requirements unresolved.

The catalogue/search-tool readings have no separately recorded mathematical-research runtime. The repository utility's measured time is an HTTP metadata-search runtime only. Program inventory now includes this additional saved utility; no mathematical certificate was rerun.

## Ordinary public copies and the2020 Raynaud access lead, 14:00–14:03 UTC

The parent clarified that reading an ordinary publicly accessible third-party copy for this authorized research does not require a separately established publisher-authorization chain. No known public original in this branch had been excluded solely on that basis. Logins, subscription controls, anti-bot challenges and private/encrypted archive files remain distinct access restrictions and were not bypassed. New searches for ordinary copies, including the public DOKUMEN catalogue, returned references to Raynaud rather than the thesis text (`turn408408750search0`); no original was marked opened from those references. A567 independently checked the advertised Fizmatclub book index and its archive, so that denied endpoint was not redundantly retried here.

SciSpace's Raynaud page was opened, https://scispace.com/papers/faisceaux-amples-sur-les-schemas-en-groupes-et-les-espaces-264rmfdzrc (`turn712283074view0`). Its actual “PDF” link is **a publisher product flyer**, `https://www.springer.com/productFlyer_978-3-540-04908-1.pdf?SGWID=0-0-1297-173799810-0`, which now redirects to the generic Springer brand page (`turn601890340view0`). It is not an original book file. This advertised link was followed without any modified access parameter.

A genuinely new historical lead was the Greek HEAL-Link library consortium's2020 temporary-access catalogue: https://www.heal-link.gr/librarians_files/dcnts/Springer_eBooks_Complimentary%20Access.pdf . The full catalogue opened as `turn959467716view0`; its first page states temporary access through30July2020, and PDFpage805 (printed806) lists the exact Raynaud1970 title and eISBN9783540362494 (`turn712283074view1`). This is evidence of the listed programme, not proof of current unrestricted access or of any archived original.

Prompted by that lead, `code/part_b_raynaud_public_snapshots.py` made three new public Wayback CDX catalogue queries for publisher locations containing the exact DOI or ISBN. All returned HTTP200 and the empty JSON list: `link.springer.com/*BFb0059504*`, `link.springer.com/*978-3-540-36249-4*`, and `springerlink.com/content/978-3-540-36249-4*`, filtered for successful PDF captures. No original-content endpoint was requested. The full requests/responses are in `code/part_b_raynaud_public_snapshots_output.json`; wall time6.496664332000364seconds and individual times6.464643513,6.242542902 and6.272260716seconds. These particular public snapshot searches are negative; no claim is made about every possible archive URL.

All four named-original reading requirements remain unchanged at this point. The separate A6 counterexample and its finite chart certificate were completed during the same interval; their mathematical verification is recorded separately from these source-search utilities.
