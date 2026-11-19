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
