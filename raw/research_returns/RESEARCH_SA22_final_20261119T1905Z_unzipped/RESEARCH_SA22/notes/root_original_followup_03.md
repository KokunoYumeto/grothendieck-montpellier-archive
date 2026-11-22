# Original-source follow-up after checkpoint03

19 November2026, root reviewer GPT-6 Astra (OpenAI, ChatGPT Pro mode).

## Joint Earle–Marden original: requirement closed

The user asked for Earle–Marden on plumbing coordinates, without specifying the published Contemporary Mathematics575 chapter. The earlier report had narrowed that requirement unnecessarily. The actual joint original manuscript **Holomorphic Plumbing Coordinates on Teichmüller and Compactified Moduli Space, Draft8/24/11** was recovered from the public archive of Marden's Minnesota papers directory:

https://web.archive.org/web/20131212124428id_/http://math.umn.edu/~am/papers/EMC.pdf

Local source: `sources/part_a567_marden_EMC.pdf` and its extracted text. A567 inspected the original printed p50 image and read §§4.1,4.5,4.8,6.1. Root independently read §§4.5 (p50),4.8.1–2 (p57),6.1.1 (p67), checked the complete proposition `A1-Earle-Marden-original`, and recomputed the coordinate identities. Physical PDF pagination has a leading blank, so printed p50 is PDF p51.

The directly checked operation is z=exp(2πiζ), w=exp(−2πiη), ζ−η=τ, hence zw=exp(2πiτ). The half-plane signs and circle phase on draft p50 are inconsistent with its own conventions; corrected signs and phase are explicitly derived. For Imτ>2h the exact bound is |t|<exp(−4πh); the printed exp(−4h) bound is weaker, not a false inequality. The sewn annulus has modulus Imτ−2h. The tensor is the first-order invariant, not a substitute for all coordinate jets.

The draft's global Theorem4.6.1 is not a premise. The distinct published2012 chapter remains unopened and is not identified with this draft. The local joint-source requirement in A1(c) is discharged by the actual original now opened.

## Koebe1907: original covering-radius passage opened

The official GDZ viewer advertises an IIIF manifest. Following that manifest led to the two original article PDFs:

- https://gdz.sub.uni-goettingen.de/download/pdf/PPN252457811_1907/LOG_0028.pdf — printed pp191–210, 21PDF pages including archive cover,1,814,016bytes, SHA256 `a8c4de684d59033f271d9291e2c9f2c4b47e8a89511f0825f4547131d28b41ef`.
- https://gdz.sub.uni-goettingen.de/download/pdf/PPN252457811_1907/LOG_0076.pdf — printed pp633–669, downloaded only, not represented as read.

The first article's second auxiliary theorem, pp203–205, gives a universal positive covering radius for normalized schlicht domains. Root read the OCR with the original images and visually inspected printed pp204–205. No numerical sharp quarter constant appears in this passage. The manuscript therefore cites it as the original qualitative theorem and uses its own full sharp proof plus the opened original Lavrentiev1934 pp173–174 for the bound4.

Programs and scope:

- `root_gdz_discovery.py`: official landing-page retrieval and advertised-link discovery,8.123929s.
- `root_gdz_manifest.py`: advertised manifest retrieval,9.12659s.
- `root_koebe_sources.py`: two public original-PDF requests,13.167846s; hashes and sizes retained.
- `root_koebe_ocr.py`: all20 mathematical pages,140dpi,4workers,500.513493s;20 renders and20 OCR calls, all exit0. OCR supports source reading and is not a mathematical certificate.

## Lehto–Virtanen and Pfluger

The Lehto–Virtanen book remains unopened in mathematical full text. Official Springer and ScienceOpen metadata identify electronic DOI **10.1007/978-3-642-65513-5**; the prior bibliography's final digit0 was an error in this run and has been corrected. The public OpenLibrary record advertises Read/PDF/plain-text links: Read leads to sign-in for borrowing, PDF and text return403. No borrowing or access control was bypassed. The SciSpace page labels the book open access, but its opened page exposes no original PDF; metadata labels are not counted as original inspection.

New search queries in both engines used the exact book title, authors, `filetype:pdf`, and the filename form `Lehto_Virtanen`. Results were catalogues, citations and a distinct Lehto1966 ICM lecture; none was confused with the joint book.

For Pfluger, broad exact-title and archive-volume searches newly revealed DOI **10.18311/JIMS/1960/16922** in a bibliography indexed by SciSpace. The DOI landing page and public Crossref metadata are being followed using `root_pfluger_discovery.py`. First invocation failed before any request because the system Python lacked `requests`; the script was repaired to use standard-library urllib, and the failed output is retained. No result from that failed invocation is claimed.

Follow-up completed approximately13:45UTC: DOI and Crossref requests both returned404. The current publisher is an ordinary React application. Its public HTML advertises `/assets/index-D8Y64Ztl.js`; that bundle advertises the public GET route `/api/public/article/16922` on `https://informatics-journals-api-he3ivhb46a-el.a.run.app`. Following that normal article-reading route with no credentials returned200 and the exact Pfluger title, authorship and pp401–412. Crucially, its access object is `{allowed:false, reason:SUBSCRIPTION_REQUIRED}` and `pdfUrl` is null. We stopped there: neither a full-text endpoint nor a hidden/private file was requested. The public metadata advertises the DOI despite its current resolver failure. The exact source gate is now a known subscription-restricted original article, not a missing title or an inferred citation.

The public Internet Archive journal search returned172 records. Because search fields omitted years, we inspected all172 public metadata records (168new requests,4cached;184.057536s), reading advertised filenames and access flags, with no errors. None contained the1960/1961 or volume24 sought. The four-record pilot took9.498099s; full catalogue request and two public landing probes took5.090510s. No journal PDF was downloaded from this negative inventory. The source lookup's four-request discovery batch took8.231415s, after the failed import had been repaired. The ordinary publisher-page/bundle requests and public metadata response have their own exact per-call timing records in `code/root_public_page_links_*_output.json`.

A separate Lehto catalogue search used three English/German title-and-author queries and inspected four metadata records in13.495938s. Two were unrelated surname matches and are not sources. The two actual book records, `quasiconformalma0000leht` and `quasikonformeabb0000leht`, both explicitly mark their PDFs and OCR as private. They were not downloaded. The German Springer book is likewise subscription content. Failed web opens of a possible SciSpace PDF and the publisher PDF are recorded as failures, not source readings.

## Rechecked main mathematical gate

Root reread the complete moving-seam energy, support/recession, convex image, weighted-deficit and cap-limit proofs and their use in `A1-graph-range`. The additional check-event rows specify exactly what was recalculated. No new unproved step was found in that review. This is rechecking existing proofs, not an additional closure of an open research row or a claim of independent formal verification.

## Further source and geometric-class closures before checkpoint04

The Part A reviewer recovered and actually read Nakamura1990 pp205,209–210,215 and Ihara–Nakamura1997 pp131–133,146,148 from the public GDZ original PDFs. The exact restrictions are incorporated into Part A: genus-zero reconstruction is not promoted to a full theorem inducing every group isomorphism, and the tangential choices, numbered nodes, smooth rational components and pro-l range of the1997 construction remain explicit. These two named-source requirements are closed.

The Part C reviewer recovered Gabriel1932 from the public journal volume and visually checked pp32–34 and38. Its opposite ordering for the first two arbitrary factors and symmetric restrictions on the remaining factors confirm the scope distinction already proved in Part C. This named-source requirement is closed. Full retrieval and reading records are in the reviewers' notes.

Root independently checked the three newly integrated fourfold statements `B1b-correspondence`, `B1b-blowup`, `B1b-fermat`. We read the complete proofs and Part B's independent audit, the actual Shioda–Katsura original pp98–103 (including original images98 and103), and Ancona's author-source PropositionA.9 and RemarkA.10. The result supplies explicit additional geometric members of the exact method domain, including characteristic2, and separates the finite F4 certificate from the all-characteristic argument. It does not turn the sufficient numerical-positivity assertion into a circular proof of D.

Additional public-source searches used both engines with Pfluger's exact German title, the1960/1961 volume24 and Golden Jubilee descriptions, and ETH author/archive terms. The Google Books original-volume catalogue at https://books.google.com/books/about/The_Journal_of_the_Indian_Mathematical_S.html?id=6k4_AQAAIAAJ explicitly gives snippet view only; physical holdings catalogues and later citing articles were not counted as original access. No full-text restriction was bypassed.

The broader Internet Archive title query increased the catalogue from172 to182 records. The10 additional public metadata records were checked in17.503207s; the one ambiguously dated volumeXVIII was then read in its openly advertised OCR and proved to be the1931 seventh-conference report, not volume24 of1960. No Pfluger original was found. The three-request broader-search/ETH-finding-aid batch took8.806878s; the ETH finding aid returned429 and was not retried. A new Iasi journal collection covers1934–1948 only; its catalogue request failed403. Eremenko's advertised public books-and-papers collection and the open `Pdf/` and `Pdf/Complex/` directory indexes contain no advertised Pfluger or Lehto–Virtanen original.

The A6 task-to-answer audit reread the actual049(c) image and its input wording. It verified that the initial anabelian assumption is part of the sheet, and explicitly restricted specialization to the proved equal-characteristic-zero trait. Its new counterexample `A6-special-fibre-counterexample` retains the same generic open and cover data while changing the special fibre from one to two irreducible components. Root read the full proof and finite local-chart certificate, checked all comparison maps and hypotheses, and verified the parameter-system wording refinement. This is a refutation of a stronger chosen-fibre reconstruction claim, not an invented unresolved gate in the original definition request.

## Checkpoint04 build and page audit, 19 November2026

The build13 wrapper failed before running TeX because `/usr/bin/time` was unavailable; its actual failed-command output remains in `logs/build_13.out`. We used `code/root_timed_build.py` for build14: both LuaLaTeX passes and BibTeX completed, exit0, recorded elapsed238.440812106s. The final120-page PDF has zero overfull boxes, undefined references/citations or missing-character diagnostics. We rendered and visually inspected pages1,4,17,23,30,53,54,56,70,104,106,110,120; render elapsed4.721145637s. The exact QA record is `logs/typesetting_checkpoint_04.json`. This scheduled checkpoint was delayed by the failed wrapper and completion of the required build/page checks; no extra checkpoint was made.

## Original-text closures after checkpoint04

Alling–Greenleaf1971, Birman1974 and Lehto–Virtanen1973 are now directly read. Root independently opened original images Allingpp61,64,65; Birmanpp151–152; Lehtopp92,95,100 and checked the exact comparisons in sections/part_a7.tex,part_a6.tex,part_a3.tex. The five-row real-lattice crosswalk, configuration-space convention, and sewing/transition normalization agree with the cited passages. Agent notes contain the wider actual reading scopes and fetch hashes. The three live source rows are closed. Root also re-read the complete cap-image and graph-range proofs, checking moving-seam signs, positive Hessian, recession/minimization and the equivariant phase-torus retract; this is a recheck, not movement.

Further Pfluger searches after checkpoint04 used both web engines for the exact title, Verheftung/Pfluger/401–412 variants, Golden Jubilee variants, original journal volume and public catalogue terms. The official Indian Mathematical Society home page was opened; its digitization announcement concerns The Mathematics Student, a different journal, and does not supply the required article. The Bielefeld DML journal registry was opened and its JIMS link followed: it leads to GoogleBooks editions marked snippet view. CiNii AA00699860 was opened; it confirms a separately described unnumbered Golden Jubilee1907–1958 volume issued1961, but provides physical holdings, not mathematical pages. The Calcutta Mathematical Society Golden Jubilee1958–1959 volume is a different publication and was not substituted. Search refs turn419489119*,turn841790702*,turn246060173*,turn232942087*,turn398031481*,turn793948950*; opened/find refs turn915194732view0–2,turn206854569view0–2,turn793948950view0. No runtime is invented for web-tool catalogue reads.

A new five-request public repository-metadata batch (`root_pfluger_repository_metadata.py`) completed in27.299035476s. OpenAlex identifies the exact workW2773398315, marked closed with no repository full text and only the already checked publisher landing page. SemanticScholar DOI lookup returned the exact1960 record but an empty original-PDF URL. HAL exact-title returned0; OpenAIRE returned total0 (the actual saved response was read). The broader InternetArchive creator query returned168records; all titles were inspected, with three1957 Riemann-surface-book records and unrelated authors/physiology, but no1960 welding article. These are metadata results, not mathematical readings.

## Public journal OCR and finding-aid audit, 14:27–14:40UTC

The indexed ETH finding aid, *Albert Pfluger1907–1993*, Handschriften250 (1998), DOI10.3929/ethz-a-001980311, was actually opened as web-readable text at the public indexed bitstream URL. Its §1.2, pp6–7, lists late publications and research notes, rather than a digital copy of the1960 article. Its p26 lists Helfer's1962/63 thesis on differentiable welding as a physical archival item. Neither catalogue passage was confused with the mathematical original. An ordinary download of that same advertised bitstream returned429 in6.993536072s; no workaround was used. A subsequent attempted extraction command encountered a nonexistent PDF and produced no reading. The saved HTTP result and the web-text reading have different scopes.

The larger journal OCR search (`root_pfluger_public_ocr_inventory.py`) attempted166 explicitly advertised public OCR files in469.041786806s:165 downloaded, one HTTP500 (a catalogue-labelled1914 issue), and no title/author match. Inspection then exposed an important limitation:148 frontmatter records contain heavily misrecognized Tamil characters for the mostly English originals. Therefore zero matches are **not** reliable absence evidence for those scans. The offline quality audit records that limitation, each identifier and its diagnostic character counts; runtime0.056221181s. The remaining17 retrieved records have predominantly Latin frontmatter and identify older issues. No original Pfluger text was located or marked opened.

The initial OCR script also excluded10 already checked metadata records because their filenames used the earlier `pfluger_delta_` prefix. The quality audit records this bookkeeping omission rather than representing all182 catalogue records as OCR-searched. Their actual metadata concerns1918,1931,1949,1980 and1985 conference/journal material; the undated volumeXVIII was already read as the1931 conference. Six further records advertise no public OCR. No restricted file was requested.

Further exact-title, author, page-range, German spelling, filename and Golden Jubilee queries in both search engines returned bibliographies, physical holdings and unrelated surname matches. In particular, references to the1988 Pfluger birthday volume do not mean that it reprints the1960 paper. The YMSC catalogue was queried through the actual form action and field IDs exposed by its homepage; its results and runtime are separately saved. No metadata or failed request is promoted to a mathematical source reading.

## Raynaud original chapter preview recovered before checkpoint05

The publicly advertised Springer chapter list in the Akalin LNM gist led to the actual subscription landing for chapterIII, DOI10.1007/BFb0059509, pp37–55. Its advertised public preview returned the two original pages37–38, not the whole chapter. The root visually read both page images on19Nov2026 around14:55UTC. The PDF is102730bytes, SHA2567d08cf7d84c585d63359e57f38cdcdbfc5a582e3eee410e3b28631a595c3882c. Fetch, text extraction and first-page rendering took7.393654237s; exact provenance is in code/root_raynaud_advertised_preview_output.json.

Original LemmaIII1.1 and its complete proof, DefinitionIII1.2, and PropositionIII1.4 with its complete proof are visible. LemmaIII1.5 starts but its proof continues beyond the preview. The lemma is directly relevant to the cohomological-flatness/base-change input to B3 subject17, subject to checking the exact conditionW atII1.3 and the finite-presentation representing module. The local algebra cited atII2.9 can be re-proved directly. PropositionIII1.4 has additional earlier dependencies that are not declared checked here. Thus this is actual original mathematical reading and a smaller remaining source gate, but the live requirement remains open until the precise deduction is written and its hypotheses verified.

The preceding retrieval script tested17 exact chapter-PDF URLs against the public capture catalogue (all empty exact-URL results) and fetched two ordinary publisher pages (both subscription HTML), in48.942440765s. These outcomes do not establish exhaustive absence of archived copies. The gist retrieval took12.973843046s; only its Raynaud entry and19 chapter/front/back links were inspected, not the thousands of unrelated entries.


### Visual resolution of undated public journal covers

The148 Tamil-OCR records have no catalogue date fields, but145 contain an explicit year in their advertised PDF filenames. Those filenames range1911–1958. Root fetched and visually read the remaining three undated covers and the1958 cover, four successful public requests in15.021509744s. They are respectively December1930 volumeXVIII no12, April1926 volumeXVI no8, August1929 volumeXVIII no4, and new-series volumeXXII1958. Exact identifiers, hashes and image readings are in code/root_pfluger_unknown_issue_covers_output.json. This resolves the unknown filename dates; it is not an assertion that every internal page was read or that the poor OCR proves article absence.


### Lieberman indexed issue/XML lead after review2

Root opened the actual JSTOR issue record i316409 in the web index, which advertises an XML link for2373533. Following that advertised link reached the same article landing without mathematical text. Its named download likewise yielded no original text. A separate ordinary request to the issue returned200 but only3038-byte Client Challenge HTML in11.237733227s; no challenge script or protected asset was requested. The MaRDI full-work link was checked and is only the known DOI. This distinct indexed-XML lead did not change the source gate. Exact queries/refs and distinctions are in code/root_lieberman_postreview_web_record.json.
