# Independent original-source retrieval audit

Researcher: GPT-6 Astra, OpenAI, ChatGPT Pro mode, `part_c_algebra` agent.
Date: 2026-11-19. Gabber/Fujiwara retrieval was time-boxed from 12:17:15 UTC to approximately 12:26 UTC.

## Status and use

| Work | Original theorem text opened? | What was actually opened | Consequence |
|---|---|---|---|
| Earle–Marden, *Holomorphic plumbing coordinates* (2012), Contemp. Math. 575, 41–52, DOI 10.1090/conm/575/11411 | No | Institutional publication metadata; volume contents; author listing; a separate conference abstract | No statement is certified from the unavailable chapter. Use the independently opened Kra, Hubbard–Koch, Hinich and Wolpert originals for claims they actually prove. |
| Marden, *Geometric complex coordinates for Teichmüller space* (1987), 341–354, DOI 10.1142/9789812798411_0016 | No | Volume metadata; later precise locators in Hinich | Theorem p.345 and corollary p.346 are secondary locators only, not direct verification of the 1987 source. |
| Gabber, *Affine analog of the proper base change theorem* (1994), Israel J. Math. 87, 325–335, DOI 10.1007/BF02773001 | No | Official publisher abstract, bibliography and subscription notice; institutional journal contents | Section 5, Corollary 1 remains checked through the opened modern source. The independently opened full Stacks proof supplies the mathematical result used. |
| Fujiwara, *Theory of tubular neighborhood in étale topology* (1995), Duke Math. J. 80(1), 15–57, DOI 10.1215/S0012-7094-95-08002-8 | No | Official institutional author metadata; NDL/CiNii bibliographic records and official download locator | Corollary 6.6.4 remains attributed through the opened Haine–Holzschuh–Wolf paper and ILO. Their full proofs or checked deductions are distinct from direct inspection of Fujiwara. |

An unavailable original is a source-access limitation, not a mathematical gap when the manuscript supplies a complete independent proof or an explicitly identified, fully opened later proof. No access-control workaround, credential substitution, paywall bypass or anti-bot bypass was attempted.

## Earle–Marden 2012: exact approaches

1. Official AMS chapter URL, `https://www.ams.org/books/conm/575/11411/conm575-11411.pdf`, was requested; the tool could not retrieve it (ref `turn136726761view2`). The root researcher independently observed HTTP 403. No theorem text was returned.
2. Bonn Hausdorff Research Institute's original program publication list was opened: `https://www.mathematics.uni-bonn.de/him/programs/past/tp_2010_05` (ref `turn697793923view0`; search verification `turn982347237search0`). Entry 2010b30 gives authors, title, volume and DOI; its preprint column is a dash. It exposes no preprint download.
3. Public library contents PDFs were found at `https://digitale-objekte.hbz-nrw.de/storage2/2018/06/15/file_323/7916464.pdf` and `https://toc.library.ethz.ch/objects/pdf/e01_978-0-8218-5340-5_01.pdf`. They show this chapter starting p.41 and the next chapter p.53 (refs `turn982347237search8`, `turn263093959search5`). These are contents only.
4. Google Books volume `pvKdD74g6UEC` metadata and contents were opened (`turn668306202view0`). A direct p.41 preview was inaccessible (`turn136726761view1`). The advertised preview link redirected and failed (`turn225165164view2`); a further advertised common-term link reached Google's sorry/CAPTCHA endpoint (`turn225165164view3`). Retrieval from that service stopped at the challenge. The Google Books API metadata request had also failed before that challenge (`turn668306202view1`).
5. ResearchGate and Academia public search results exposed author/publication metadata or the volume contents, not an opened copy of the chapter. Exact-title, DOI, author, download and institutional-domain queries in both search engines found no accessible original.
6. Marden's official Minnesota profile was opened: `https://cse.umn.edu/math/albert-marden` (`turn274609710view0`). Its website link leads to `https://www-users.cse.umn.edu/~am/` (`turn832412060view0`). The advertised **Papers** link, `https://www-users.cse.umn.edu/~am/papers/`, was opened and lists no available files (`turn440654416view0`). Cornell author/archive searches produced metadata, not this chapter.
7. A separate, original Earle conference abstract, *Plumbing paired punctures in Kleinian groups*, was opened in `https://fsw01.bcc.cuny.edu/zhe.wang/A.pdf` (`turn136726761view0`; zero-based PDF p.4; search text `turn274609710search6`). It describes continuing joint work with Marden and Kleinian plumbing groups. It contains neither the required chapter's theorem nor its proof and is not counted as opening the chapter.

### Bibliographic distinction

Marden's 2016 *Hyperbolic Manifolds* bibliography was opened at `https://www.cambridge.org/core/books/abs/hyperbolic-manifolds/bibliography/E5911F5BC5EF7AAA62EB93674D4FD825` (`turn696445006view0`; targeted locator `turn898873699view1`, lines 784–787). It separately lists:

- *Holomorphic plumbing coordinates*, published in the 2012 edited volume;
- *Holomorphic plumbing coordinates on Teichmueller and compactified moduli space*, “to appear”;
- *Disjointness of parabolic canonical regions*, “to appear”.

The first entry there has inconsistent volume/page metadata (573, 67–97). The volume contents and DOI metadata support **575, 41–52**. Do not silently identify the short published article with the longer “to appear” work or borrow theorem locators between them.

## Marden 1987: exact approaches

1. The official World Scientific PDF URL `https://www.worldscientific.com/doi/pdf/10.1142/9789812798411_0016` returned HTTP 403 (`turn136726761view3`).
2. The Google Books 1987 volume was located as `S40GCwAAQBAJ`, title *Mathematical Aspects of String Theory*. Indexed contents put Marden's chapter at 341 and the following Wolpert chapter at 355 (`turn192912457search19`). No full chapter was opened; the existing Google challenge was not circumvented.
3. Exact title, DOI, author and institutional-site searches returned bibliographies, contents, or later papers rather than an original chapter copy.
4. Hinich's *Plumbing coordinates on Teichmüller space: A counterexample* explicitly points to Marden's theorem p.345 and corollary p.346. A CiteSeer mirror search exposes this passage (`turn274609710search5`), but opening that mirror returned 403 (`turn696445006view1`). The root has independently opened Hinich's full arXiv original. These locators remain second-hand with respect to Marden.

## Gabber 1994: exact approaches

1. `https://link.springer.com/content/pdf/10.1007/BF02773001.pdf` resolved to the publisher article/abstract rather than a PDF (`turn462551639view0`). The article page was independently opened again at `https://link.springer.com/article/10.1007/BF02773001` (`turn274609710view2`). Lines 31–60 contain the abstract and an explicit subscription/pay-purchase notice. No PDF theorem text was accessible.
2. The original publisher bibliography and metadata were visible, including the 1992 Fujiwara preprint reference. These do not verify Gabber's Section 5, Corollary 1.
3. The Hebrew University journal contents `https://math.huji.ac.il/~ijmath/index_pdf/87.pdf` were found (`turn539842336search9`); they confirm the bibliographic page range only.
4. The seminar page `https://mahalex.net/teaching/seminars/gabber/index.html` was opened (`turn697793923view1`); it lists a lecture on the paper but no paper download.
5. IHES author-directory requests `https://www.ihes.fr/~gabber/` and `https://www.ihes.fr/~/gabber/` were inaccessible (`turn225165164view0/1`). Indexed IHES papers contain citations to the 1994 work, not a located copy of it.
6. Searches of exact title, DOI, “affine analogue”, author, Corollary 1, PDF and institutional sites in both engines produced references, later proofs, or abstract metadata. A ResearchGate author listing supplied metadata only.

## Fujiwara 1995: exact approaches

1. The NDL/CiNii bibliographic records expose only the official Euclid download: `https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8` (`turn539842336search3`, `turn192912457search0/2`). The download request was inaccessible (`turn462551639view1`).
2. The normal Project Euclid article URL ending `/10.1215/S0012-7094-95-08002-8.full` was inaccessible (`turn462551639view2`). The B researcher separately saved non-PDF results, which are not original-source PDFs.
3. The Nagoya University official faculty listing was opened at `https://www.math.nagoya-u.ac.jp/en/people/faculty-01.html` (`turn982347237view0`, lines 77–88). It lists Fujiwara's paper but no full-text link. The institutional researcher profiles at `https://profs.provost.nagoya-u.ac.jp/html/100000275_en.html` and the corresponding Japanese publication page likewise give metadata only (`turn192912457search1/3`, `turn374217657search5`).
4. Reopening `https://cir.nii.ac.jp/crid/1363107369908715904` produced a robot-verification page (`turn274609710view1`). No bypass was attempted.
5. Exact-title, DOI, singular/plural “neighborhood(s)”, 1992-preprint, 1995, Corollary 6.6.4 and institutional-site searches found no legal original full text. Later references were not relabelled as the original.

## Independent collar audit

Recorded separately in `checks/part_a2_collar_secondary_events.tsv`. Both rows use the required `statement_id,date,who,type,outcome` schema. The audit checked the outward curvature sign, the moving-boundary Neumann condition, the high-frequency residual, its O(sqrt(n)) L2 norm, the even-double correction, the positive-gradient term in the Bochner identity, and the order of limits (fix large n, then take small epsilon). It found no proof gap. The weak H2 solve on the closed double can, if desired, be justified explicitly by smooth source approximation before passing the Bochner bound to the limit.

## Lieberman1968: short independent retrieval, 12:56–12:58 UTC

Target: David I. Lieberman, *Numerical and Homological Equivalence of Algebraic Cycles on Hodge Manifolds*, American Journal of Mathematics 90(2) (1968), 366–374, DOI10.2307/2373533. The bounded task was stopped after approximately two minutes when root reassigned this reviewer to the full coverage audit. No mathematical original was opened.

- Official `https://www.jstor.org/stable/2373533` opened only a scripts/GoogleTagManager shell (`turn861915358view0`). No theorem text was returned.
- Public SciSpace page `https://scispace.com/papers/numerical-and-homological-equivalence-of-algebraic-cycles-on-56ceyax5sw` supplied metadata and partial introductory OCR (`turn861915358view1`). Its advertised PDF link16 leads back to the same JSTOR endpoint (`turn945339389view0`); it is not a separate accessible original copy.
- Official issue contents `https://www.jstor.org/stable/i316409` were found (`turn151990364search0`). Exact title, DOI, institutional-host and complete-volume searches returned bibliographies and citations, not an opened article.
- Grothendieck's 1969 note at `https://matematicas.unex.es/~navarro/res/articles/Hodge%27s%20Conjecture%20is%20False.pdf` (`turn397784008search6`) cites a different Lieberman source, the Princeton1966 thesis *Algebraic cycles on nonsingular complex projective varieties*. That thesis was not retrieved and is not relabelled as the target article.
- Kleiman1968's already opened original exposition at `https://agrothendieck.github.io/divers/kleimanweil.pdf` (`turn397784008search9`) supplies the theorem actually used in B1. This closes the mathematical premise, not the requested original Lieberman fetch.

B independently obtained the required Kleiman1994 original from Mainz during this task; its source record and theorem checks belong to B. No further Lieberman search was undertaken in this bounded interval, and no access-control or authentication workaround was attempted.
