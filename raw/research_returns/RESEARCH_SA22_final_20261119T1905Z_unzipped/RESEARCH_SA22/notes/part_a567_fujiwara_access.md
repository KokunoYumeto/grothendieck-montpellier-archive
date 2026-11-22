# Fujiwara1995 original-source access followup

Researcher: GPT-6 Astra, OpenAI, part_a567,19November2026. This file supplements `notes/part_b_source_followup_20261119.md` and `notes/secondary_source_retrieval_20261119.md`, both read before proceeding. Target: KazuhiroFujiwara, Theory of tubular neighborhood in étale topology, Duke80(1995),15--57, DOI10.1215/S0012-7094-95-08002-8, specifically Corollary6.6.4. The original remains UNOPENED until actual original mathematics is read. The different1997 rigid-geometry/Lefschetz article and the master's thesis are not substitutes. No already denied publisher file, private InternetArchive item, challenge or subscription-controlled endpoint was retried.

## New Tokyo catalogue investigation

- Opened official1995UTMS catalogue https://www.ms.u-tokyo.ac.jp/preprint/1995/ (`turn198762338view0`). Its displayed60-item numbering has no Fujiwara/tubular entry. The advertised main series page https://www.ms.u-tokyo.ac.jp/preprint/ (`turn457442262view0`) offers years1995--2018 only; no1992--1994online catalogue is advertised there.
- Opened CiNii's actual serial record https://ci.nii.ac.jp/ncid/AA11831096 (`turn463118368view0`). It identifies UTMS as starting93-1(January1993) and records print holdings for1993/1994. The advertised TokyoOPAC link returned403 (`turn173492633view0`), so it was not pursued. The predecessor anchor does not expose a usable predecessor record in the returned page.
- Public WaybackCDX prefix queries for `www.ms.u-tokyo.ac.jp/preprint/199*` and `.../preprint_e/199*` each returned five actual annual URLs1995--1999, with no earlier year. Complete metadata JSONs saved as `sources/part_a567_fujiwara_cdx_tokyo_preprint.json` and `_tokyo_preprint_e.json`. Individual request durations7.170267 and7.145219seconds; these are metadata access runtimes, not mathematical test times.
- Opened Tokyo's full master's-thesis catalogue, https://www.ms.u-tokyo.ac.jp/library/file/gakui/master2019(5).htm (`turn349443507view0`). Its exact Fujiwara record is M1988-24 at lines1512--1513 (`turn714144258view1`), on semiabelian schemes/1-motives and Shimura compactifications, with no linked electronic original. No tubular title appears (`turn714144258view2`). The exact1994doctoral subject was already distinguished by B.

## Other new public leads

- Exact-title searches restricted to Tokyo's repository, ordinary public catalogues and seminar bibliographies returned no actual original-file link. Search refs include `turn613785102search*`, `turn457442262search*`, `turn463118368search*`, `turn635142134search*`. This is a bounded negative search outcome, not a claim that no public copy exists.
- The SciSpace1995Duke listing advertised the target title but opening https://scispace.com/journals/duke-mathematical-journal-3hpqjgwd/1995 returned429 (`turn204547017view0`); stopped without workaround.
- The official Nagoya Japanese faculty page https://www.math.nagoya-u.ac.jp/ja/people/faculty-05.html opened (`turn204547017view1`). It uses the title variant *Theory of tubular neighbourhood in étale cohomology*, but gives the same Duke80(1995),15--57 citation and no paper link. Its linked PDF is a faculty introduction, not the43-page original; it was not relabelled as a paper. Title-variant searches yielded no further original.

## 14:25--14:33 UTC: public archives and a distinct author exposition

- Two initial broad CDX forms with an interior wildcard, then explicit prefix combined with a trailing wildcard, returned empty arrays. Their wildcard semantics do **not** warrant a claim that all author archives were searched. Corrected prefix requests without that wildcard returned503 for Nagoya/Tokyo and timed out for Kyoto; no negative catalogue finding follows from those failures. The narrower ordinary CDX prefix `www.math.nagoya-u.ac.jp/~fujiwara/` returned32 captured URLs, all for the different mathematician Kazumasa Fujiwara; complete metadata is `sources/part_a567_author_prefix.json`. No desired paper appeared among those actual results. The response is preserved with request/hash/runtime in `sources/part_a567_fujiwara_new_access_1430.json`.
- The ordinary public catalogue request `https://libcats.org/g/Fujiwara` returned403 after7.164seconds. Stopped, with no file request or workaround. Exact-title ResearchGate/Academia/PostScript searches returned no linked target original (refs `turn961701674search*`).
- The broader public InternetArchive query for Duke title together with1995/year or80/volume/title returned four public table-of-contents items for volumes77--80, with no alternative full volume. Metadata saved as `sources/part_a567_fujiwara_ia_volume_search.json`; request6.314098seconds. This supplements, and partly overlaps, B's earlier annual-volume search; it does not alter the exact issue's already observed private-file restriction.
- Opened the official RIMS1073 table of contents (`turn298341261view0`), followed its actual article12 link, and recovered **Fujiwara's distinct1998 exposition**, *Rigid geometry and étale cohomology of schemes*,168--191: https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1073-12.pdf . Full original is `sources/part_a567_fujiwara1998_rims.pdf`,24pages,2768333bytes, SHA256ec5b44f12046bf40be8e21b5abf05b552c68af6f108b8a04b76b7233f2e0d1db. Retrieval14.851807seconds. Its CORE mirror returned403; the independently advertised official publisher copy opened normally. No denied endpoint was bypassed.

### Exact mathematical reading and deduction from the1998 exposition

Opened §2,175--179, definitions183 and references191 (`turn700884513view0`, `turn740528407view0`, `turn628460931view0`--`view3`); visually checked177--178. Work in the noetherian “good” class: (A,I) is a noetherian henselian pair, Â its I-adic completion, U=Spec(A)\V(I), Û=Spec(Â)\V(IÂ), and F a torsion abelian étale sheaf on U. Page176 identifies the rigid étale topoi of Sph(A) and its completion. Its proof is sketched using Elkik approximation/algebraization and rigidity of morphisms. Page177 gives the canonical cohomology comparison with rigid analytification in every degree; the global argument invokes Gabber's affine theorem. Page178 outlines the underlying deleted-tubular comparison through admissible blowups, proper base change and a stalk calculation.

**Checked deduction:** apply177 to A and Â. By176 their rigid targets are canonically equivalent, and the canonical comparison maps commute with completion. Thus H^q(U,F)→H^q(Û,F|Û) is an isomorphism for every q, equivalently the canonical derived-sections map is a quasi-isomorphism. This formal deduction is complete conditional on those stated comparison theorems; the1998 source supplies proof outlines, not all auxiliary proofs. Reference[Fu] at191 names the1995 Duke article but supplies no manuscript location. The exact1995 Corollary6.6.4 source-reading gate remains open.

## 14:33--14:37 UTC: further original-source routes

YMSC MathSciDoc's actual homepage search handler was inspected (`turn768490860view0`; ordinaryHTTP200,92185bytes,8.639seconds). Its observed GET query was used for title=tubular and author=KazuhiroFujiwara. The web tool could not render either search; ordinary requests returned200 with empty paper lists,46175/46252bytes in7.879335/7.820499seconds. Full catalogueHTML is retained under sources/part_a567_ymsc_{tubular,kazuhiro}.html; no content file was requested. Google Books/title searches produced no identified volume preview. The newly opened MathOverflow294834 page (`turn444332269view0`) supplies no original-file link for its bibliography[1]; it is not used as a proof input.

The new public IHES preprint searches are completely preserved in `code/part_a567_fujiwara_ihes.py` and `_output.json`. The Fujiwara query returned two Lafforgue works from2000/2002 in whose keywords he occurs; the tubular query returned zero records. Both ordinary requests returned200,25537/14990bytes,10.024461/9.995118seconds. No target1992 manuscript or1995 original was found; these are bounded catalogue outcomes.

## Advertised first-page preview investigation — 15:01–15:07 UTC

The saved publisher landing does contain a separate **First page** link, at `sources/fujiwara1995_archived_landing.html`, line343: `https://www.projecteuclid.org/first_page/euclid.dmj/1077245853`. This actual link is a distinct legitimate preview lead; the previously observed denial of the full article does not establish that no preview exists. The access attempt did not infer any unadvertised image or protected endpoint.

- Opening the exact archived link from that landing failed in the web tool (`turn297529097view0`). The ordinary request in `code/part_a567_fujiwara_preview.py` returned HTTP404 in **10.359228540000913s**, recorded in `code/part_a567_fujiwara_preview_output.json`.
- A CDX query for that exact advertised original URL, successful status only, digest-collapsed and capped at20 records, returned HTTP200 with the empty array in **8.641206100997806s**. Exact request and output are preserved in `code/part_a567_fujiwara_preview_cdx_output.json`. This is a bounded no-capture result for this preview URL, not a general no-copy claim.
- The live advertised preview was inaccessible in the web tool (`turn400737486view0`). One ordinary request returned HTTP200 but only **1,159 bytes of Incapsula challenge HTML**, not the article page, in **7.235201277999295s**. The response and metadata are preserved at `sources/part_a567_fujiwara_live_preview.html` and `code/part_a567_fujiwara_live_preview_output.json`. No challenge was followed or bypassed, and this endpoint was not retried.

No original mathematical passage was read in this investigation. The exact1995 Corollary6.6.4 source gate remains open; the already read1998 original exposition is still distinguished. Earlier fresh search-only queries for title+thesis/preview and the1994 doctorate returned references/author metadata rather than a new original (`turn181441206search*`); they did not add a proof input. B independently confirmed the preview had been missed in the earlier landing inspection. No new mathematical program or mathematical status change occurred.


## Independent hypothesis and functoriality audit of the1998 exposition — 15:08UTC

Read the actual original images176,177,178 and183 again, alongside the extracted text. The earlier deduction is correct in its deliberately restricted **noetherian** scope. This recheck does not read1995 or change its gate.

| Input or operation | Exact1998 locator and checked scope |
| --- | --- |
| “Good”, type n | Appendix§1,p183: A is noetherian and I is arbitrary. No excellence, local-ring, principal-ideal, or initial completeness assumption is added in this case. We do not infer the arbitrary-ring modern theorem from the distinct type-v case. |
| Henselian input | §2,p175: the affine pair (S,D) is henselian along D; U=S minus D. This is a hypothesis on (A,I), not an assertion that A is already complete. |
| Completion | p176, Categorical equivalence: the natural morphism from the rigid étale topos of the completion to the henselian rigid étale topos is an equivalence. The completion is along the given ideal. For noetherian A, I is automatically finitely generated and its completion remains noetherian. |
| Cohomology input | p177, first Theorem: for X_U of finite type over U, the canonical global comparison holds in every degree for a torsion abelian étale sheaf. Taking X_U=U meets the finite-type condition by the identity morphism, even though U need not be proper over Spec(A). |
| Relative caveat | p178, last paragraph: constructibility and prime-to-residue-characteristic qualifications address comparison of relative direct images for a nonproper finite-type f. They are not extra hypotheses on the preceding global theorem applied here. |
| Proof completeness | p176 sketches full faithfulness and essential surjectivity through Elkik's results; pp177–178 supply a comparison statement and proof outline invoking Gabber and proper base change. The exposition does not reproduce every auxiliary proof. |

For precision, let E be the rigid étale topos of Sph(A), H that of its completion, and β:H→E the natural equivalence. Put Â=lim A/I^m, Û=Spec(Â) minus V(IÂ), and c:Û→U. The GAGA morphisms ε_A:E→U_et and ε_Â:H→Û_et satisfy ε_A∘β≅c∘ε_Â, because analytification and completion send each étale object by the same base-change construction. Hence the square on cohomology with top map induced by c, bottom map induced by β, and vertical canonical GAGA maps commutes. Both vertical maps are isomorphisms by p177; the bottom map is an isomorphism by p176. The top map therefore is an isomorphism in every degree. For a sheaf F placed in degree zero, this proves that the canonical map RΓ(U,F)→RΓ(Û,c*F) is a quasi-isomorphism.

This is a formal derivation from the opened1998 statements, with their published proof scope stated honestly. It neither supplies the unread text of1995 Corollary6.6.4 nor silently attributes the modern arbitrary-ring hypothesis to that1995 source. The full source file remains outside the distributable archive; the note records its URL, identity, hash and exact locators above.


## Concrete Tokyo predecessor and direct catalogue forms — 15:09–15:13UTC

No exact Fujiwara UTMS article number had been observed. In particular, **93-1 is the beginning of the series, not an identified preprint number for the target**. This uncertainty was confirmed with the parent before proceeding.

Following the actual relationship-map link in CiNii's UTMS record, then its actual MAPLIST frame, recovered a new concrete predecessor: **UTYO-MATH**, NCID **AA12191229**, ending at92,38(November1992). Its original catalogue record was opened at https://ci.nii.ac.jp/ncid/AA12191229 (`turn258066283view0`). This is a serial identification only; it gives neither the target article number nor a paper file. The map's actual frame/list HTML and exact requests are preserved in `sources/part_a567_utms_relation_{frame,list}.html` and `code/part_a567_utms_relation_{frame,list}_output.json`. Ordinary successful requests took8.377396447998763s and7.3720071030038525s. The web frame-list renderer failed (`turn614082659view0`), whereas the ordinary public request succeeded; no access restriction was bypassed.

A fresh inspection of the actual CiNii Books form on the UTMS page recorded GET `/books/search` with `title`, `author`, `count`, and the separate GET `/books/contents` with `contents`, `count`. Its full observed form and request record are in `code/part_a567_utms_catalogue_form_output.json` (HTTP200,51,119bytes,7.2460062760001165s). The two direct catalogue queries then returned:

- `title=tubular&author=Fujiwara&count=20`: HTTP200, explicitly0records;6.1083472879981855s.
- `contents=tubular neighborhood&count=20`: HTTP200, exactly1record;6.211069315999339s. That record, https://ci.nii.ac.jp/ncid/BA55321572, was actually opened (`turn439373772view0`) and identifies **David Archibald Cox's1974 Princeton dissertation**, not Fujiwara's paper. No unrelated thesis file was fetched.

The independent queries were batched in6.212781499998528s. Full request/result metadata and HTML are in `code/part_a567_cinii_preprint_search_output.json` and `sources/part_a567_cinii_{title_author,contents}.html`. Targeted searches using the newly identified predecessor name and the exact tubular title returned no article identifier or original-file link (`turn752944782search*`, `turn258066283search*`); these search outcomes are bounded, not a universal nonexistence claim. Earlier preprint/offprint/title queries (`turn838006231search*`) and a Duke-site/preview search (`turn216727265search*`) likewise supplied no new original. The author profile supplies a journal DOI, not a preprint number.

The1995 original gate remains unread. No1992/1993 version has been identified. A same-work original preprint with a verified relationship and complete relevant theorem/hypotheses would suffice; no full-article proof-reading condition has been imposed.


## Gabber[4] exact preprint provenance — 15:14–15:17UTC

The newly opened original Gabber preview, printedp326, explicitly refers to Fujiwara[4]. The actual bibliography entry is visible in the saved public publisher HTML: `sources/part_b_gabber_preview_landing.html`, line1174, `id=ref-CR4`; and the historical landing, line238, `id=CR4`. I independently opened the current public publisher page at https://link.springer.com/article/10.1007/BF02773001 (`turn301768299view0`, line90; find `turn301768299view1`). Its reference[4] is:

> K. Fujiwara, Theory of tubular neighborhoods in étale topology, preprint,1992.

This verifies an actual contemporary citation to a1992 preprint under the plural-title variant. It supplies **no institution, series, preprint number, file URL or other identifier**. Neither UTYO-MATH membership nor any92-number follows from it. The1992 version's relationship to the1995 work is a bibliographic lead; full identity and relevant statement still require the actual text if a copy is located.

The earlier B-side Crossref discovery output retained only selected access metadata, so a full public Crossref-record request was justified. Two independent ordinary metadata requests were batched, without requesting gated article text:

- https://api.crossref.org/works/10.1007/BF02773001 returned4,190bytes, HTTP200, in5.569238841002516s. Reference key `BF02773001_CR4` contains only the same unstructured1992 citation. Full raw record: `code/part_a567_gabber_crossref_references.json`; SHA25614bb3066958efd6d95603e617166f72d49443dd66fc68423d4e828a4eb21bedb.
- The **actual advertised** Download references link from current publisherHTML line1177, https://citation-needed.springer.com/v2/references/10.1007/BF02773001?format=refman&flavour=references, returned1,265bytes ofRIS, HTTP200, in8.392031429997587s. Its `ID=ref4` contains the same citation and no further identifier. Full response: `code/part_a567_gabber_publisher_ris_references.ris`; SHA2568582029d2f2b9380b3995e73e03b900ac340bebfbd7db344f8edecbd1e87a1a4.

Whole batch8.394255646999227s, exact requests/provenance/results in `code/part_a567_gabber_reference_metadata_output.json`. Publisher metadata were read; originalp335 was not falsely marked opened. No Fujiwara original mathematics was read and no source gate or mathematical status changed.

The historical publisher entry also advertises a GoogleScholar reference-query link for this exact1992 citation. The web opening failed (`turn350512275view0`); one ordinary public request returnedHTTP429 after13.089055586999166s. It was not retried and no results were read. Exact request/scope/error: `code/part_a567_gabber_fujiwara_scholar_output.json`. No full-text or protected endpoint was requested.


## Targeted1992 plural-title catalogue/repository search — 15:20–15:25UTC

The exact1992 citation was pursued separately from the1995 journal record. No UTYO-MATH issue number was inferred. Exact queries, pooled-result reference IDs, result classifications and caveats are preserved in `code/part_a567_fujiwara1992_query_register.json`; two complete search-tool result objects are saved as `part_a567_fujiwara1992_system1_queries.json` and `part_a567_fujiwara1992_targeted_queries.json`.

System2 returned broad unrelated material rather than even the now-known publisher citation, so its coverage was inadequate. System1 verification found later references to the1995 paper (including plural-title references), Cox's different1974/1975 work, the already known1998 author exposition and2024 talks, but no separately identified1992 original. These are limited search outcomes, not proof that the preprint has no public copy. Two exploratory literal `site:repository`/`site:catalogue` forms do not identify verified domains and are not treated as catalogue searches or negative coverage evidence. No denied CORE/Scholar/Euclid endpoint was revisited.

### Concrete repository metadata query, including pagination

The official OpenAIRE query documentation was opened (`turn615353085view0`), confirming its title-keyword, author, date and pagination parameters. `code/part_a567_fujiwara1992_catalogues.py` queried `title=tubular&author=Fujiwara` without DOI, year or OA restriction, so a separately catalogued earlier preprint would not be excluded by a journal identifier. It returned **26 records**. Page1 contained25 and was inspected completely; the actual reported total justified one page2 request for the remaining record. The concise complete inspection ledger is `code/part_a567_fujiwara1992_openaire_all26_summary.json`.

**Exactly one of those26 records concerns the target mathematics.** Its date is1995-10-01 and its DOI is10.1215/S0012-7094-95-08002-8. Its child instances from Crossref, zbMATH and Euclid all identify the1995 journal article. Its OPEN label points only to the already known Euclid landing; “Unknown Repository” labels in merged instances do not supply an additional paper URL. The other25 records concern different Fujiwaras and unrelated engineering, biology or medicine. Thus this complete26-record result contains no separately identified1992 preprint and no new original-text location. No unrelated paper files or denied endpoints were fetched.

The initial OpenAIRE request returned602,011bytes in23.383468202002405s. Page2 returned8,852bytes in17.033863463999296s. Full raw responses, exact URLs, hashes, total counts and timings are saved in `code/part_a567_fujiwara1992_openaire_raw.json`, `_openaire_page2_raw.json`, `_catalogues_output.json`, and `_openaire_page2_output.json`.

An independent OpenAlex query used the exact explicit1990-01-01 through1994-12-31 date window and the terms `Fujiwara tubular neighborhoods etale topology`, capped at25records. It returnedHTTP429 in6.320761210001365s and was not retried. **No OpenAlex result was read**, so no zero-result claim follows. The initial two-request batch took23.385180502002186s.

### Actual WorldCat catalogue attempt

The public WorldCat home page opened (`turn286918635view0`) but its search interface requires JavaScript in that representation. The exact public GET `/search?q=` pattern was independently observed in the WorldCat link already present in CiNii's UTMS HTML. One ordinary query, `Fujiwara "tubular neighborhoods" 1992`, returnedHTTP403 in5.801788866003335s; it was not retried. No search results were read, and this is **not** a zero-result catalogue finding. Exact query, provenance, status and duration: `code/part_a567_fujiwara1992_worldcat_output.json`.

The1992 citation remains a provenance lead rather than a located original. The exact1995 Corollary6.6.4 source gate remains open. No theorem status changed and no mathematical certificate was rerun.


## One delayed Fatcat availability check,15:38UTC

At root's explicit request, the exact previously503 public DOI lookup was requested once more after the earlier long interval: `https://api.fatcat.wiki/v0/release/lookup?doi=10.1215%2FS0012-7094-95-08002-8`. The original URL/status is recorded in `code/part_b_repository_discovery_output.json`, Fujiwara/Fatcat entry. Existing source notes and scripts showed no earlier Lieberman Fatcat query, so one lookup for DOI10.2307/2373533 was included in the same bounded batch. This was an availability check, not a repeated author/title search.

Both requests returned **HTTP503** with the identical91-byte message `upstream connect error or disconnect/reset before headers. reset reason: connection timeout`. No release, file, access-status, or URL record was returned or inspected. No source content was requested, no retry occurred, and the route stopped. Failure is not a zero-result record search and establishes nothing about whether Fatcat holds either article.

Exact preserved program: `code/part_a567_fatcat_delayed_check.py`; complete output: `code/part_a567_fatcat_delayed_check_output.json`. Fujiwara started2026-11-19T15:38:02.984500+00:00 and ran11.899788230002741seconds. Lieberman started2026-11-19T15:38:02.985523+00:00 and ran11.898996335003176seconds. Parallel batch11.901000856996689seconds. Both response-body SHA256 values are `2f85832e31ca57711e6107af6b142363351ae516adb71c69afc643fac26be7f6`. The exact request headers match the ordinary earlier metadata program; no authentication or access-control workaround was used.

**Fujiwara1995 and Lieberman1968 source gates remain unchanged.** This records service availability and documentary scope, not mathematical progress.


## Distinct IAS provenance and MPIM catalogue route — 16:32–16:34 UTC

The earlier access record and B/C source-retrieval notes were read before this bounded investigation. Exact search queries and complete returned result objects are preserved in `code/part_a567_fujiwara_distinct_search_1633.json`, `part_a567_fujiwara_ias_discovery_1634.json`, `part_a567_fujiwara_ias_provenance_1635.json`, `part_a567_fujiwara_ias_queries_1637.json`, and `part_a567_fujiwara_contemporary_ias_refs.json`. These filename suffixes are descriptive labels; the embedded UTC start/end values are authoritative. Per-HTTP timings are not supplied by the web search tool and are not inferred from its elapsed batch time.

A genuinely new institutional lead was found and read: the IAS original annual report for1991–1992, https://albert.ias.edu/bitstream/handle/20.500.12111/6023/reportforacademi1992inst.pdf (`turn184750752view0`, exact find `turn455411488view2`). Printedp42 identifies **Kazuhiro Fujiwara**, arithmetic algebraic geometry, University of Tokyo, among School of Mathematics members and visitors; printedp75 records his February24 seminar on arithmetic compactifications of modular varieties. Thus this is the correct mathematician, not Koji Fujiwara, the agricultural researcher of the same romanized name, or the Princeton economist Thomas Fujiwara. The report's searchable text has no tubular occurrence (`turn455411488view3`), and the read entries give no original preprint number, title or offprint location. Membership is not evidence that the target preprint was issued by IAS.

The actual IAS repository home https://albert.ias.edu/ (`turn184750752view1`) advertises an Advanced Search link to https://albert.ias.edu/search, which was followed (`turn455411488view1`; rendered interface `turn966714452view0`). The web representation exposes only a loading state and no completed result list. One ordinary request for that exact advertised public search page, to inspect its public form, returned **HTTP403** in **6.7515461790026166seconds**, beginning2026-11-19T16:33:18.232690Z. Exact output is `code/part_a567_fujiwara_ias_search_metadata.json`; the originally inline request was subsequently preserved, without rerunning, as `code/part_a567_fujiwara_ias_search.py`. The route stopped there: no retry, alternate headers, inferred REST endpoint, login, challenge bypass, or private file was requested. Consequently no negative repository-search result is claimed. Two-engine targeted site searches found the annual reports and unrelated Voevodsky publication catalogues, with no target original or preprint identifier; search coverage is limited.

A second distinct bounded catalogue check followed the actual1992 link on MPIM's public year index https://archive.mpim-bonn.mpg.de/view/year/ (`turn455411488view0`) to https://archive.mpim-bonn.mpg.de/view/year/1992.html (`turn966714452view1`). The complete displayed102-item catalogue was inspected. It contains neither a Fujiwara author entry nor the tubular-neighborhood title. This establishes only absence from that specific102-item1992 MPIM list, not from all MPIM holdings or all possible versions. No unrelated preprint was downloaded.

Finally, two targeted contemporary-provenance searches (`Fujiwara tubular preprint Princeton` and `Fujiwara tubular1992 Berkovich`, exact quoted queries retained in the JSON register) supplied later1995 journal references, the already opened1998 exposition, and unrelated names. They supplied no contemporary series number or actual earlier manuscript. No blocked Euclid, WorldCat, CiNii OPAC, Scholar, CORE, private InternetArchive, OpenAlex or Fatcat endpoint was retried.

**Outcome:** the distinct IAS route is blocked before results, and the bounded MPIM1992 catalogue is negative. No actual1992 original or relevant1995 theorem statement was obtained. The1995 original-source reading gate remains open; no mathematics, theorem status, bibliography source-reading status or program certificate changed. These are bounded route outcomes, not proof that no public copy exists.
