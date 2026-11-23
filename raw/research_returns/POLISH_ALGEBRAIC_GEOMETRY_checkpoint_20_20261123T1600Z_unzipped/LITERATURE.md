# Consolidated dated literature searches

An early failed opening or pending gate is historical; later dated entries state whether it closed. Search failure does not prove novelty.

## Record: workbench/records/ROOT_LITERATURE.md

# Literature search log

Dates and times use Europe/Berlin unless marked UTC. Entries distinguish a
search result from a source opened and checked. Failed searches are not evidence
that a result is new.

## 2026-11-23: initial source access and purity

1. Opened the requested GitHub `mathematics-workbenches/blob/main/FORMAT.md` and
   raw-content URL. The search tool returned DisabledError for both. A direct
   retrieval is being attempted. Format-1 compliance is pending.
2. Opened `https://hexagonmath.org/2611.00789`; the bare versionless address was
   not accessible. A search found the versioned page `2611.00789v1` and PDF.
3. Searched “Moret-Bailly purity finite flat torsors regular scheme
   characteristic p Picard”. Found Andrea Marrama, *On the restriction of
   finite torsors*, C. R. Math. 364 (2026), 431–435,
   DOI `10.5802/crmath.836`, and Česnavičius–Scholze, *Purity for flat
   cohomology*, §7.1. Both require exact statement inspection before use.
4. Searched first-higher-direct-image vanishing for a normal source and regular
   target. Results point to work on rational singularities and birational
   invariance; no novelty conclusion is drawn from these initial searches.


## 2026-11-23 — Paper 1, further exact comparisons

- Query: `"birational" "normal" "regular" "first higher direct image"`
  and `"R^1 f_*" "normal" "regular" vanishing`, primary-source search.
  Result: Ishii–Yoshida, *On vanishing of higher direct images of the structure
  sheaf*, arXiv:2410.15282v3, 19 April 2025, opened in full. Corollary 1.4,
  p.3, proves the vanishing of the first direct image for a proper birational
  map with normal source and regular target in every characteristic. Theorem
  1.3, pp.2–3, permits locally quasi-unmixed S3 targets pseudo-rational in
  codimension two. Thus the proposed L6c theorem is KNOWN, even in a stronger
  characteristic scope. The paper now cites it and does not repeat its proof.
  URL https://arxiv.org/pdf/2410.15282 ; SHA-256
  `29f5bebc90ece8bbef00bc7d45c79dfd1a1d29c52648a451b795aa5f918c0272`;
  186,962 bytes; pages used1–5. The independently developed characteristic-p
  proof remains an own-work checking record, not a novelty claim.
- Query: `"Arithmetic duality for two-dimensional local rings with perfect
  residue field" Suzuki 2024`. Publisher confirms Journal of Pure and Applied
  Algebra228(2024),107465, DOI10.1016/j.jpaa.2023.107465. Opened author/arXivv4
  PDF: Proposition6.1.2(1),(3),p51; Proposition8.1.4,pp64–65;
  Proposition8.2.1(1),(3),p65; Proposition8.2.3,p66. Checked all assumptions
  at the opening of section8,p62 for A=W(Fbar2)[[t]]. These are the exact
  injectivity, strictness and differential-filtration inputs for the wild
  symbol argument. The separate 2024 Algebraic Geometry paper on class field
  theory and Picard–Brauer duality is a different work, not this citation.
- Queries: `"Picard" "persistent" "Dedekind" 2`, `"class groups" "infinite
  algebraic extensions" "2"`, and class-group-realization variants. No exact
  arithmetic counterexample located yet. This is not a proof of novelty.
  Opened Guralnick–Jaffe–Raskind–Wiegand, arXiv:alg-geom/9410031,
  Example4.7,pp17–18: its large Picard quotient is in characteristic p and
  p-primary, so it does not provide an invertible-coefficient counterexample.
  Eakin–Heinzer and polynomial-Dedekind constructions are leads for further
  primary comparison, not yet claimed to settle the question.
- Queried Hexagon with Picard/cohomological terms and ECCC with Dedekind terms.
  No exact matching theorem returned. Hexagon returned other Picard-group work
  on quotient stacks, which does not address the arithmetic tower. Earlier
  broad negative searches are recorded as negative searches only.
- Opened Stacks Tag07QS, Proposition15.53.3(4): a Dedekind domain whose
  fraction field has characteristic zero is excellent. Opened Tag0BUA,
  Lemma58.13.5: the wild inertia subgroup is pro-p with prime-to-p tame
  quotient, without a perfect-residue-field hypothesis. Tag history comparison
  remains to be added for final filing.

## 2026-11-23 01:59 UTC — Paper 1, finite-torsor invariance

Queries combining birational, normal, smooth, Picard, and Nori led to
Lingguang Li and Hao Wang, *The Birational Invariance of Fundamental Group
Schemes*, arXiv:2604.23997v2, 9 June 2026. Opened the primary PDF and read
Corollary 4.6, p.7, with its proof and references. It asserts invariance
of the Nori fundamental group scheme for a birational morphism of normal
proper varieties over a perfect field when the target is smooth. This
contains the finite commutative torsor assertion used for B.1. Over an
algebraically closed field our regular target is smooth. Cartier duality
and finite-subgroup detection therefore give the desired Picard-tau
assertion as a KNOWN CONSEQUENCE. The paper now states that attribution;
it retains only the explicit deduction in Picard language, a form not
stated in the source, using Moret-Bailly purity as detailed by Marrama.
The source is a preprint, not asserted to be journal-published.
URL: https://arxiv.org/pdf/2604.23997 .
Forward references include Hogadi–Mehta2011, Adroja–Amrutiya2025,
and Sun–Zhang2025. Their broader scope is not inferred without inspection.


## 2026-11-23 — Paper1 additional primary comparisons and source closure

- Followed class-group-realization searches to Claborn, *Every abelian group
  is a class group*, Pacific J.Math.18(1966),219–222, Theorem7,p222, and read
  the construction. It realizes every abelian group by a Dedekind domain;
  its polynomial/localization construction does not assert a fraction field
  algebraic over Q with two-cohomological dimension one. The theorem alone
  does not give the simultaneous arithmetic conclusion studied here.
  Primary: https://msp.org/pjm/1966/18-2/pjm-v18-n2-p04-p.pdf .
- Followed citations to Heitmann1974, DOI10.1215/S0012-7094-74-04162-3,
  Eakin–Heinzer1973, and recent prescribed-residue-field constructions.
  Heitmann's primary full text is still being retrieved; no secondary account
  of his theorem is treated as a verified source. Heinzer–Olberding2020,
  Theorem5.2, concerns an almost-Dedekind construction and does not by itself
  supply the present noetherian arithmetic/cohomological combination.
- Opened Martinelli–Naranjo–Pirola, *Connectedness Bertini theorem via
  numerical equivalence*, Advances in Geometry17(2017),31–38, Theorem1.1,p31.
  Its connectedness assertion for every linear section of the stated
  dimension applies uniformly to every normalized finite cover. Together
  with tame Kummer charts it closes the fixed-curve input. The source is
  published, not merely its older arXiv preprint.
- SGA4 X primary re-edition was fetched from Orgogozo's normalesup mirror
  after his CNRS page returned502/503. Read Theorem2.2, originalp46,
  Corollary4.2, originalp56, and Corollary4.4, originalp57. In dimension one
  the strict-local input follows directly from Theorem2.2. The proof no
  longer needs an unlocated general Gabber citation. Stacks Tag0DV9,
  Lemma59.67.3, was also opened in full and gives the exact arbitrary-coefficient
  field criterion used in the new text.
- Searched the current OpenAI mathematics overview at
  https://raw.githubusercontent.com/openai/math/main/overview.tex ; snapshot
  SHA-256 39de58f1bf2185eb11d444a58aec4c7c7530419f3127deb9261fa46e044a4135.
  No exact Dedekind/persistent Picard, Murre or local metabelian result was
  found. The Milne and CM-Hodge entries were passed to the cycle/gerbe
  literature comparison; no unexamined AI claim is a proof input.
- Opened Hexagon2609.00105v1, *Graded absolute integral closures and Picard
  groups*, contributed by Akhil Mathew, provenance ChatGPT6Pro,26September2026.
  Theorem1.1,p1, concerns faithfully flat extensions with seminormal reduction
  and trivialization of polynomial line bundles. This is neighboring Picard
  work, not the claimed simultaneous arithmetic tower/cohomology example.
  Primary PDF: https://hexagonmath.org/pdf/2609.00105v1 . Its theorem is not
  used as an input here. Negative search results do not establish priority.


## 2026-11-23 — Paper1 closer tower precedent and exact boundary credit

S. A. Popescu, *Infinite algebraic extensions of Dedekind structures*, Math. Reports24(74)(2022),505–512, official https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/3/14.pdf, was opened by root and read in full by worker4. Section5 pp511–512 starts from Q(i) over Z[1/2] and makes every old odd prime eventually unramified inert in a quadratic tower; its integral closure is Dedekind. This is a known occurrence of the eventual-inertness/noetherian mechanism, now credited in Paper1. The source makes no claim about Picard/class-group preservation, Brauer groups, or cohomological dimension, and its construction does not control dyadic primes. It therefore does not establish the combined persistent Pic/2 theorem. Its references to Hasse1925 and Schilling1950 are further leads, not automatically checked sources. The precise simultaneous class-preserving and local-degree assertion remains the main literature comparison.

Root independently opened Drinfeld's arXiv1007.4004v7 LemmaC.2 p19 and Esnault–Kindler's primary author text Proposition6.2 pp8–9, together with their29September2016 one-page erratum. The projective finite-generation input is a known consequence of their complete-intersection curve theorem. The closed-boundary formulation and prescribed-neighborhood/finite-inertia deductions are presented with those inputs credited, without priority claims. The already corrected omission stays in author-correction records.

Claborn1966 Theorem7 p222 is now cited for general class-group realization, with the exact scope separated from algebraic-Q fraction field and cohomological constraints. Hexagon2609.00105v1, contributed by Akhil Mathew and produced by ChatGPT6Pro, Theorem1.1 p1, is cited as a neighboring polynomial-ring Picard/base-change theorem; it is not used as a proof dependency. The full primary PDF was opened and bytes were successfully retrieved on this retry. All URL/hash/page metadata are in paper_1/SOURCES.tsv and CONTEXT_SOURCE_RETRIEVAL.json; no external source is redistributed.

## 2026-11-23 03:20 UTC — source-correction checks

Root opened Popescu2022 section4,pp510–511 and checked the selected/full
valuation-family inference against the multiquadratic counterexample. The
main selected-family criterion and section5 construction are not refuted.
Exact-title and author-name searches with erratum/correction returned no
correction; this is a limited search, not proof of nonexistence. Full own
argument and scope are in workbench/records/ROOT_CORRECTIONS.md.

Root reopened Stacks0BTP,02W8,0AP9 and0APK. The0BTP proof's fpqc claim
cites02W8, whose statement/proof is only fppf. The valid replacement is
0AP9 plus Gabber0APK. This is a citation defect, not a false theorem.
Addresses and SHA256 values are in ROOT_CORRECTION_SOURCE_RETRIEVAL.json.

Chai's author PDF still returns403 for direct web and byte retrieval. Targeted
searches retrieved the indexed primary text of Theorem2.4 onp6 and its
complete final tangent-space argument and Remarks onp7 from the official
www2.math.upenn.edu author URLs. This verifies the target wording in indexed
primary text, not a downloaded or visually inspected PDF. The geometric
ordinary-Igusa proof is undergoing a full current check; no full source
opening is fabricated. Katz1981 was downloaded from Princeton and its
Theorem2.1,pp148–149 and constructionpp150–152 are being checked.

## 2026-11-23 03:35 UTC — ordinary Igusa corrections fully checked

Opened the exact official indexed primary text of Chai, Theorem 2.4(iii), pp6–7 and its final tangent argument, after direct author downloads returned403. Opened the full statements of Mumford–Fogarty GIT Theorem6.14 and Proposition6.15 in the primary-book indexed text. No unavailable PDF hash or visual opening is claimed. Downloaded and read Katz pp148–152 (all five pages viewed), Partsch pp102–104,106 (102–104 viewed), and Chai–Oort §3.9 pp35 (viewed). The attached EGAII4.5.13 and FGAVI Remark3.4 were read directly. Complete targeted proof now closes ordinary all-Artinian Pic-tau flatness and the explicit first-order Albanese-fibration obstruction. Full proof, source access and hashes, three original finite reruns and a different-method computation: workbench/records/igusa_corrections/. The supersingular extension and hull/algebraization are not certified by this event.

Exact-title/author searches for Partsch corrections and Chai Igusa Pic-tau flatness corrections returned the original articles, author note and later citations, but no correction. The Cambridge author listing showed only the original Partsch article. This limited search does not establish absence of a correction or priority.

## 2026-11-23 03:48 UTC — K-theory dictionary bridge

Opened Grayson, Weight filtrations in algebraic K-theory, author version13November1992, pp9 and12, https://www.graysonfamily.org/dan/Papers/seattle.pdf. Page12 states and explains K0(R)=Z direct-sum Pic(R) for every Dedekind domain through rank and determinant. This supports only the programme dictionary translation of the persistent Pic/2 example, not a new result or a higher-K claim. Hash and retrieval data: paper_1/DICTIONARY_SOURCE.json.
# Searches and source audit, 2026-11-23, 04:00--04:18 UTC

## Smooth tangent-line obstruction and finite flat torsors

Queries, in both general and primary-source-restricted searches:
"smooth ample" curve "line subbundle" tangent surface;
"foliation" "O(-D)" "ample" surface;
"tangent" "ample curve" "positive characteristic";
site:arxiv.org regular foliation smooth surface ample invariant curve positive characteristic;
site:hexagonmath.org foliation surface ample curve;
site:eccc.weizmann.ac.il algebraic surface foliation tangent;
Liedtke algebraic surfaces positive characteristic 2013 corrigendum abelian surfaces table.

Opened C. Liedtke's author PDF, arXiv:0912.4291v4, Theorems 4.4-4.5 p.21,
section 7 pp.26-30, and the warning furnished by Proposition 8.5 p.33:
negative Euler characteristic alone does not imply ruledness in positive
characteristic. The complete application in ROOT_SMOOTH_TORSOR_CHECK.md
instead first proves K.D=0 and uses pluricanonical divisors. PDF SHA-256
17309a48dad424540f3f25e1e0cb35e898c3e7f79d7f5bb8aab20ec32f6c1776.
The institutional publication page confirms chapter pp.229-292 (2013),
DOI 10.1007/978-1-4614-6482-2_11:
https://portal.fis.tum.de/en/publications/algebraic-surfaces-in-positive-characteristic/ .
The exact author-version table corrections are outside the paper.

The searches located the current primary preprint by Fassarella, Mendson,
dos Santos and Touzet, Foliations with small singular set in arbitrary
characteristic, arXiv:2607.18571v2. Downloaded and read introduction pp.1-5,
the regular rational/del Pezzo statements, and Theorem 2.8 with proof, p.13.
URL https://arxiv.org/pdf/2607.18571 ; SHA-256
60d19ea3e35ffde9578ae81602e4dbf4e3c9d92de87e96827382f9a9f9d5164a.
Its Camacho-Sad equality is an equality in the ground field, not an
integer vanishing in positive characteristic. Its rational-surface
classification does not itself cover the higher-genus ruled exclusion
needed here. No exact prior version of the particular tangent-line
statement was identified in these searches. This is not a priority claim.
ECCC returned unrelated arithmetic-circuit or Chow-form items, not an
applicable theorem.

Hexagon's landing page and primary PDF were opened:
https://hexagonmath.org/2611.00204v1 and
https://hexagonmath.org/pdf/2611.00204v1 .
The PDF title is Counterexamples in positive characteristics, by ChatGPT
and Claude in collaboration with Rahul Ajit and Seungsu Lee. It is a
preliminary draft last revised 5 November 2026; the landing page was posted
8 November. Theorem A, printed p.2, concerns globally +-regular rational
surfaces with anticanonical divisor nef but neither big nor semiample.
The introduction, exact theorem, and authors' scope notice pp.1-3 were
opened. The theorem is contextual, not used as an input; its full proof
was not certified. Direct local retrieval returned HTTP 403, so no raw-PDF
SHA-256 is asserted from that failed retrieval. The successful web opening
is recorded distinctly from a downloaded source.

## Other open gates searched in this interval

Queries: tame fundamental group normal proper compactification topologically
finitely generated nonprojective; Kerz Schmidt tame fundamental group finite
generation proper compactification arbitrary boundary; normal proper variety
complement codimension two fundamental group finitely generated positive
characteristic; "divisor-tame" "finitely generated"; "normal compactification"
"finitely generated" fundamental group; "proper" "codimension" "fundamental
group" "finite generation" nonprojective.

Pop's author manuscript, https://www2.math.upenn.edu/~pop/Research/files-Res/2018-12-24_IOM.pdf,
was located in search results, with a valuation-tame finite-generation
statement. Its all-valuation tameness is stronger than tameness at the
specified compactification divisors in the open question; it is not
adopted as a solution. It was not downloaded or fully checked in this
interval. A 2024 MSP paper on invariance of the tame fundamental group was
also located, but not opened or used. These search leads do not close
the unrestricted boundary gate.

Opened the primary Compositio article Lefschetz theorems in flat cohomology
and applications:
https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64 .
Theorems 1.1.1 and 1.1.6, Remark 1.1.2, and Theorem 3.4.4 require the
strongly-ample condition. The remark explicitly distinguishes it from
ampleness alone. These statements do not automatically settle the source
questions for arbitrary smooth very ample sections or arbitrary Picard
point kernels. This is a primary HTML opening; raw PDF bytes and SHA-256
were not obtained here.

# 2026-11-23 04:18–04:35 UTC: recent primary context and successful retrievals

This entry supplements the earlier failed request recorded below. A subsequent request with an ordinary browser User-Agent successfully retrieved the three Hexagon PDFs. The initial 403 remains part of the access history; it is not the final access status. The external PDFs and extracted text remain scratch-only and are excluded from every returned package.

Searches used primary-source discovery, with the following exact query families: `site:hexagonmath.org henselian descent representability`; `site:hexagonmath.org "formal" "smooth" lifting`; `site:github.com/openai/math "henselian" OR "cotangent" OR "representability"`; `site:hexagonmath.org "Cohen" "algebra"`; `site:hexagonmath.org "formal smoothness"`; `site:hexagonmath.org "fpqc" "representability"`; `site:github.com/openai/math "Cohen" "lifting"`. Time-sensitive primary discovery used a one-year recency filter. These found contextual works, not a matching representability or nonlocal lifting theorem. A failed opening of an OpenAI Gersten PDF is not counted as a source reading or as evidence of its theorem.

| Opened primary work | Exact scope read and use | Local source-byte SHA-256 |
|---|---|---|
| ChatGPT and Claude, in collaboration with Rahul Ajit and Seungsu Lee, *Counterexamples in positive characteristics*, preliminary draft, 5 November 2026, <https://hexagonmath.org/2611.00204v1> and <https://hexagonmath.org/2611.00204v1/pdf> | Introduction pp.1–3, exact Theorem A p.2, and the preliminary/AI-production disclosure. Theorem A concerns globally plus-regular rational surfaces with nef, non-big, non-semiample anticanonical divisor in every positive characteristic. Paper2 cites this as a distinct recent positivity counterexample, not an input or a proof verified here. | `2a22308bb63bd22404e2c92573a26275dba820b6523791264a3e120bbecf0ec8` (662331 bytes) |
| Niels Feld, *Gersten injectivity and Morel’s purity conjecture*, <https://hexagonmath.org/2611.00017v1>, PDF <https://hexagonmath.org/pdf/2611.00017v1> | Introduction pp.1–3, exact Theorem B p.2, and the indicated later theorem/remark context. It compares injectivity after dense-open restriction for A1-localized K-theory sheaves with Gersten injectivity on henselian local rings. Paper3 uses the local-testing comparison as context only; it uses none of the K-theory claims as proof input. The complete proof was not certified. | `72c8d45705cfcf6f1d57e1aa5570f6bdb239ab3f251044bec71b6a043c25e750` (479870 bytes) |
| Niels Feld, *Universal test rings for rational Gersten injectivity*, <https://hexagonmath.org/2610.00619v2>, PDF <https://hexagonmath.org/pdf/2610.00619v2> | Introduction pp.1–4, Theorem1.1 p.2, Corollary1.3 p.3, and Corollary4.3 p.12 with its opening proof. The complete DVR/Cohen-subring comparison is contextual to Paper4's classical local structure background; it supplies no nonlocal deformation input. The complete K-theory proof was not certified. | `e15dada75777cdce38c29fe9ce2c8a03022432d7bbd2ee99d6be6ea395970e49` (591830 bytes) |

The two Feld landing pages and PDFs explicitly disclose AI assistance; this is recorded as their authors' disclosure. Paper3 and Paper4 distinguish these contextual statements from their own hypotheses and from every result used in a proof.

## Formal-scheme input for the new strict pro-modular reconstruction

The root opened and checked Alonso Tarrío, Jeremías López and Pérez Rodríguez, *Local structure theorems for smooth maps of formal schemes*, author v3, 22 April 2008, <https://arxiv.org/pdf/math/0605115>, Proposition6.5, author pp.32–33. Both pages were visually inspected, and the exact formal étaleness criterion was read with its hypotheses. Published identity: J. Pure Appl. Algebra213 (2009),1373–1398, DOI <https://doi.org/10.1016/j.jpaa.2008.12.006>. Downloaded-source SHA-256 `5fb9bcd7fd5ff4ba2fa450797ba279d2bff1f444751f3fb74d32d62731b817d1`,356255bytes. The compatible noetherian formal-scheme construction was separately checked in the attached French EGA I10.6.3–10.6.4 LaTeX. Murre1965 Proposition1 printedp249 and Appendix case(d) printedpp259–260 were reread in full relevant context; their precise completion-descent and quasi-finite gluing roles are explained in ROOT_PRO7_FRESH_COMPARISON.md.

## Fresh arithmetic primary recheck

The root reopened Stacks07QW Proposition15.53.3(4),03SA Lemma59.73.2(3),03R8 Proposition59.67.4 and its primewise proof, and03Q7 Theorem59.53.1. These exactly support excellence, constructible approximation, the primewise Brauer criterion and strict-local higher-direct-image stalks in the new independent reconstruction. These accesses were indexed-only, so no source-byte hashes are asserted. ROOT_ARITHMETIC_FRESH_COMPARISON.md records the complete mathematical comparison and the worker's frozen proof hash.


# 2026-11-23 04:41–04:52 UTC: boundary and Picard searches, with fresh primary rechecks

Boundary queries: `normal proper variety nonprojective divisorial tame fundamental group finite generation exceptional divisors`; `fundamental group complement codimension two proper normal variety finite generation positive characteristic`; `site:stacks.math.columbia.edu tame fundamental group proper finite generation normal`; `site:math.upenn.edu Pop tame fundamental groups finitely generated normal proper`; `site:arxiv.org fundamental group proper nonprojective tame finite generation`. The first two used a one-year recency filter. Search leads included Esnault–Srinivas–Bost, *Simply connected varieties in characteristic p>0*, Compositio 152 (2016),255–287, DOI10.1112/S0010437X15007654, whose abstract assumes a normal PROJECTIVE compactification with boundary of codimension at least two; the MSP paper *Tame fundamental groups of pure pairs and Abhyankar’s lemma* (Algebra & Number Theory17 (2023)), whose attempted PDF opening returned no readable content; Pop’s author manuscript already identified above, whose indexed valuation-tame scope is stronger than the boundary-divisor scope here; and Achinger–Hübner–Lara–Stix, *Tame fundamental groups of rigid spaces*, arXiv2608.12601 (August2026), whose abstract addresses rigid spaces. These are leads and scope comparisons from indexed results, not full new source readings or proofs. No boundary question was closed by these queries.

Surface queries: `"Kodaira vanishing" "very ample" "surface" Raynaud`; `"Kodaira" "globally generated" "Raynaud" surface`; `"Raynaud" "ninth" surface vanishing`; `Bernasconi Valloni "Brauer" "Kodaira" 2026`; `"very ample" "Kodaira" "root" surface Bhatt`; `"very ample" "Raynaud" "cover" surface Kodaira`; `"very ample" "Kodaira" "surface" "562"`. These recovered the previously located Bernasconi–Valloni comparison and the Raynaud/Zheng literature, not an exact prior numerical example. Root reopened the primary HTML at <https://arxiv.org/html/2605.28278v1>, read its introduction and Propositions3.13–3.14 with their proofs, and retrieved <https://arxiv.org/pdf/2605.28278v1>. SHA-256 `331419431f35c6c01f3daa55cd37f8a6ae394df45f67aa9e5d4f00f42a473290`,451747bytes. Exact author pages16–17 prove global generation of A^p and point separation under additional hypotheses; the specified family has p>2. The line bundle causing nonvanishing is A, so these statements do not assert the very ample nonvanishing bundle in Paper2. This confirms, rather than replaces, the earlier worker comparison in FINAL_CITATION_AUDIT.md. No priority conclusion is inferred from failed exact-number searches.

Picard queries: `Grothendieck Lefschetz Picard group smooth ample divisor dimension four positive characteristic SGA 2`; `Picard schemes weak Lefschetz very ample divisor positive characteristic isomorphism dimension four`; `"Picard" "Lefschetz" "counterexample" "positive characteristic"`; `"restriction" "Picard" "injective" "ample divisor" characteristic`; `"Lefschetz" "Picard" "Mukai" torsion` (the last with recency365). Primary journal HTML of Cotner–Zavyalov was reopened at <https://www.cambridge.org/core/journals/compositio-mathematica/article/lefschetz-theorems-in-flat-cohomology-and-applications/8556201EDB51D7F2F76F5950A800CD64>. Root read Corollary3.4.5, Examples3.3.6 and3.4.6, their proofs, and footnotes4and6. Corollary3.4.5 explicitly needs Hodge2-equivalence and negative coherent H1,H2 vanishing; its citation of SGA2XII3.6 is under those hypotheses. Example3.4.6(ii) additionally assumes an isomorphism on global1-forms, and footnote6 says the authors do not know whether such examples exist. These conditions cannot be omitted to close A1 or A2. The logical feasibility of that extra differential condition is being examined separately; no published false theorem is alleged here.

The Cotner–Zavyalov author PDF was then retrieved successfully from <https://bogdanzavyalov.com/refs/papers/Lefschetz.pdf>:403913bytes, SHA-256 `c29c1d5d5257d0d2ff271fed90f406d48d7daee0213e9829be498cf34fae8b7d`. Read author pp.12–13 (Example3.3.6 and proof),17 (Theorem3.4.4/Corollary3.4.5),18 (Example3.4.6, proof and footnote6), compared with the published primary HTML. These are author-page locators, not an invented journal-page correspondence.

At04:54–04:55UTC, searches `"Cotner" "Zavyalov" "3.4.6" correction`, `"Lefschetz theorems in flat cohomology" erratum`, and `"alpha_p" "differentials" "Lefschetz" injective` returned the primary article and unrelated errata, but no located correction of this premise. This bounded search does not establish that the incompatibility was never noticed. An institutional-repository copy of the published PDF was located at <https://pure.mpg.de/pubman/item/item_3606755_2/component/file_3623558/Cotner-Zavyalov_Lefschetz%20theorems%20in%20flat%20cohomology%20and%20applications_2024.pdf>, but its local retrieval returned HTTP403. No source bytes or page check is claimed for that failed retrieval. Primary journal HTML and the successfully retrieved author PDF are the source evidence.

# 2026-11-23 04:56–04:58 UTC: nilpotent Picard kernels and the exact formal reduction

Queries: `Picard nilpotent thickening kernel connected unipotent`; `Picard scheme nonreduced reduction kernel connected unipotent group`; `Picard group infinitesimal thickening kernel etale p group`. Root opened Lipman, *The Picard group of a scheme over an Artin ring*, author-hosted PDF <https://www.math.purdue.edu/~jlipman/papers-older/%5B1976%5D%20Picard%20group%20of%20a%20scheme%20over%20an%20Artin%20ring.pdf>, and read Proposition2.5 and its proof (printedpp30–32, physical16–18), the surrounding connected-component arguments, and Corollary2.11 (printedp33,physical19), together with the setup in section1. Downloaded1424358bytes, SHA-256 `4dc2a4a1fe7132c47f7645df84368cbeaae6985c2f05e1c55e1d7aa3adb825bb`. The general nilpotent restriction has unipotent kernel and cokernel; this statement cannot be strengthened silently to a connected kernel for arbitrary composite thickenings. The connectedness argument explicitly applies to an individual square-zero step, and a subgroup arising in a composite need not be connected. This blocks a proposed shortcut from finite unipotence to triviality.

Also opened Geisser’s *The affine part of the Picard scheme (corrected)*, <https://www2.rikkyo.ac.jp/web/geisser/picard_corrected.pdf>, pp1–2and5–6 (Theorem3, Proposition4, Lemma9 and the relevant proof), and the published2021 corrigendum <https://www.cambridge.org/core/journals/compositio-mathematica/article/corrigendum-the-affine-part-of-the-picard-scheme/61F122F6C3D353DD6D0EBC38A5C133CA>. Downloaded corrected-author PDF95498bytes, SHA-256 `ba3d9b907b2c144df59f151f73af3028de264d89e9b528627ef799200117fa38`. Its universal-homeomorphism theorem permits finite unipotent groups in the kernel and cites Gabber’s realization result. Its schemes are reduced, so this is not presented as an example of a nilpotent thickening or a solution of A2. The known corrigendum, Compositio157(2021),2338–2340, DOI10.1112/S0010437X21007612, is explicitly distinguished from a new correction.

The root separately reopened the existing French SGA2 bytes (SHA-256 `27390cd8e8d7b3fffe25c6f5950218b090e336d1bece03fed36abd6808b60718`) at <https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2original.pdf>, XII3.4–3.6 on retypesetpp113–115 (physical121–123, original margin151–154), and XII4.9(b)/4.10 onpp120–121. These give the exact algebraization/vanishing requirements used in ROOT_PICARD_FINITE_REDUCTION_CHECK.md. That whole targeted check certifies the inherited finite multiplicative obstruction and fourfold reduction, while leaving the gate mathematically unchanged.

## 23November2026,05:00–05:10UTC — boundary definition and exact new comparison

Follow-up of the recorded recent boundary queries opened the full Achinger–Hübner–Lara–Stix author PDF, *Tame fundamental groups of rigid spaces*,12August2026, <https://www.math.uni-frankfurt.de/~stix/research/preprints/ACHINGER-HUEBNER-LARA-STIX-tamepi1-20260812.pdf>. Root read printed/PDFpp12,13,23 in full: Definitions2.2.1–2.2.2, Proposition2.2.3, and Theorem2.6.1 with proof. The algebraic theorem applies to every connected finite-type scheme over an algebraically closed field, with tameness at all specified valuations. It does not identify that quotient with the quotient imposing tameness only at the divisors of the original compactification. The explicit new comparison example is proved in Paper1§4.1; it makes no priority claim and closes no general boundary question. PDF1257985bytes; SHA256a8bfd3c3faa1d7cf789bb31b14abf46e037583254ca816c5f24cee8e7b340904. The initial root web URL open failed, and direct HTTPS retrieval succeeded. Stacks0BMB and0BUM were opened and their exact statements/proofs checked for purity and the proper homotopy sequence.

The worker's detailed remaining boundary searches and seven failed routes are in `paper_1/ROOT_BOUNDARY_CONTINUATION.md`; its full source receipts, exact versions/pages/URLs/SHA256s, are in `paper_1/FRESH_BOUNDARY_SOURCE_RECEIPTS.md`. They cover CRST2018, BCRGST arXivv1, Suzuki2023v4, and Lara–Srinivas–Stix2023 author version. These are known special cases and scope comparisons, not closures of the unrestricted nonprojective boundary problem.

# 23 November 2026,05:00–05:18 UTC — further local ramification and Picard searches

Exact query families used in this interval:

- `"fundamental groups" "punctured spectra" finite generation 2026`
- `"normal" "local" "surface" "fundamental group" finitely generated`
- `"Swan conductor" "punctured" "surface" bound`
- `Kato rank one ramification surfaces clean blowups bound Swan conductor zeros`
- `Artin Schreier covers surfaces resolution genus bounded conductor`
- `local surfaces Betti numbers rank one sheaves Swan conductor bound complete local`
- `Kato Oi Artin Schreier surfaces ramification r_x exceptional genus resolution`
- `"cyclic covers" "local" "surfaces" "Swan"`
- `"complete local" "Betti" "Teyssier"`
- `Grothendieck Lefschetz Picard smooth ample divisor positive characteristic p torsion injectivity dimension four`
- `"Lefschetz" "Picard" "injective" "mu_p"`
- `"Picard" "ample divisor" "p-torsion"`
- `Albanese smooth ample hyperplane section purely inseparable isogeny positive characteristic Picard injectivity`
- `"Picard" "hyperplane" "kernel" "p-group"`
- `"Lefschetz" "Albanese" "inseparable"`

The time-sensitive fundamental-group discovery queries used a one-year recency filter. Search results led to the primary Oi I/III papers, finite-type ramification/Betti results, Bădescu1982, and the Kleiman author treatment. Primary sources, exact pages read, byte hashes, hypotheses, and failed deductions are recorded in `ROOT_RESEARCH_CONTINUATION_03.md`. The two Oi PDFs and Bădescu PDF were successfully retrieved; the existing Kleiman source bytes were reused and rehashed. Search snippets and secondary discussion were discovery leads only.

Oi's order-p local formulas and proper-surface Euler formula do not alone bound the complete-local degree-one cohomology in the requested family. Bădescu's characteristic-zero or lifting/vanishing hypotheses do not settle the arbitrary positive-characteristic Picard question. Kleiman's finite unipotent kernel does not imply triviality in characteristic p. All these routes were checked against the attached research record, which already contains the relevant cleaning and multisection obstructions. No mathematical gate is marked closed or strictly smaller by this entry.

The differential exclusion of Cotner–Zavyalov Example3.4.6(ii), discussed earlier above, was already proved in the attached A-CZ346ii. The current proof is an explicit corollary and a fresh source/proof recheck. Records now state that provenance; no claim of a newly discovered correction is made.

## 2026-11-23 — retained root research searches, before review03

The following six query strings were used in the preceding continuation; no exact per-query timestamp is retained, so none is invented: `Kato Class field theory D modules ramification higher dimensional schemes1994pdf`; `local fundamental group surface tame generators cyclic cover Swan conductor genus resolution Kato`; `"Picard" "geometrically normal" "scheme" "arbitrary" base algebraic space`; `Kazuya Kato "D-modules" "1994" "pdf"`; `"Picard" "algebraic space" "non-projective" "Raynaud"`; `"abelian algebraic space" "scheme" Raynaud`. The Kato DOI10.2307/2375001 was a bibliographic lead, not a full source reading. The Raynaud–Deligne abelian-space scheme theorem, referred to as Faltings–Chai Theorem1.9 p3, remained a lead requiring the primary text; secondary notes https://www.math.columbia.edu/~gyujinoh/abschZ.pdf were not adopted as a proof of a Picard-schematicity conclusion. No open gate was closed by those searches.

The root separately opened and read Stacks Tag01XX, https://stacks.math.columbia.edu/tag/01XX, during the surface duality correction. The exact relative projective-space perfect pairing uses the dual of the symmetric power, not the symmetric power of the dual in arbitrary characteristic. The current-paper display was corrected and its unchanged numerical theorem rechecked. The source theorem had the correct formula; this is not a correction attributed to an external author. Search-service receipt:turn787710225view0.

## 2026-11-23 06:00–06:02UTC — further Picard routes

Stronger-engine queries: `"Picard" "geometrically normal" "algebraic space" scheme Raynaud`; `"Picard" "geometrically integral" "non-projective" representable scheme`. Results returned the official Brochard overview https://imag.umontpellier.fr/~brochard/recherche/overview.pdf, along with secondary Kleiman and Faltings–Chai discussions. The overview is a lead for a properness result assuming that Pic0 is open, separated and finite type with proper fibres; it has not yet been read by root and is not treated as closing schematicity. The exact arbitrary-base normal/integral scopes were delegated for a primary-source continuation. Search receipt:turn196554195search6; other snippets were not proof inputs.

Stronger-engine queries: `Picard group restriction smooth ample divisor characteristic p injective p torsion Lefschetz kernel`; `Grothendieck Lefschetz Picard smooth ample divisor positive characteristic dimension three injectivity`; `Lefschetz Picard scheme smooth divisor p torsion kernel nonnormal mu p torsor`. Routine-engine queries: `"Picard" "Lefschetz" "Cartier" "torsion"`; `"smooth ample" "Picard" "injective" "positive characteristic"`; `"Lefschetz" "Picard" "purely inseparable"`. Results returned Bhatt–de Jong's local Picard paper (official Numdam PDF https://www.numdam.org/item/10.24033/asens.2228.pdf), Cotner–Zavyalov's already compared flat-cohomology Lefschetz paper, and primary author-book/disjoint-divisor leads. Generic/general hyperplane statements and strongly ample hypotheses were not substituted for the arbitrary specified smooth very ample pair. Root then read all three inherited Cartier-leading, closed-form and target-Frobenius proofs directly. This is an active research search, not a newly proved vanishing or a priority claim. Search receipts:turn364936169search7,turn361079796search35–39,turn361079796search0.

## 2026-11-23 06:05UTC — independent H reconstruction and new literature comparison

H_FIXED_BASE_FRESH_REPROOF.md contains the isolated worker's exact primary access sequence and query strings, including incidental unused snippets. Root read all467lines and checked every assertion; its source-specific dependencies are only official Stacks pages. FRESH_P_H_DATED_LITERATURE_SEARCH.md is consolidated in full below, with26 exact queries and bounded negative comparison against Murre, Hall, published Hall–Rydh, Stacks, Hexagon and ECCC. The exact24 post-freeze primary byte receipts across the two P manifests are preserved separately; no copied external paper is returned. The comparison does not identify an earlier exact polynomial-base H conclusion, and makes no priority claim.

## 2026-11-23 06:11–06:25UTC — exact Lefschetz and torsor continuation

Queries: `smooth ample divisor Picard restriction p torsion kernel characteristic p counterexample`; `Lefschetz Picard schemes ample divisor etale kernel positive characteristic Albanese inseparable`; `Lefschetz theorem fundamental group scheme smooth ample divisor counterexample mu_p`; stronger-engine `"The Lefschetz type theorem for fundamental group schemes" 2026` with recency300 and `"On ample divisors" "165" Picard`; `Enriques surface non normal canonical covering divisorial singular locus conductrix ample`; `Enriques characteristic 2 canonical bundle trivial restriction smooth ample curve`; `Cartier invariant differential ample zero divisor mu p torsor surface`.

Root opened and read the exact primary Bhatt–de Jong, Bogomolov–Pirutka–Silberstein and Li–Tian sources at the locators and scope recorded in ROOT_RESEARCH_CONTINUATION_04.md. Exact source URLs, byte hashes and fetch times are in ROOT_RESEARCH04_SOURCE_RECEIPTS.json. Li–Tian v3,Theorem1.1p2 and Propositions4.10/4.13pp10–11 retain stronger positivity or W2-lifting; they do not close the arbitrary specified-divisor question. Bhatt–de Jong Section2 was read in full and retains the finite p-primary ambiguity. The BPS general-linear-section statement is not an arbitrary-divisor theorem. Badescu1982 was recognized as the source already checked in the preceding continuation; it was not counted as new evidence. Enriques results in the search output were leads only, not adopted primary theorem inputs. No correction or priority claim is made.


## 2026-11-23, approximately06:32–06:45UTC — abelian-torsor schematicity comparison

Root searches actually issued: system2 queries `"abelian" "torsor" "pushout" "scheme" Raynaud`; `"torsors" "schemes" "homomorphism" "Raynaud" Picard`; `"Achter" "Casalaina-Martin" "1.7.2" Picard`; `"schematic" "torsors" "abelian" pushout`. Stronger-engine queries: `"abelian schemes" "pushout" "torsor" "scheme"`; `"torsors" "representable" "abelian" "homomorphism" "Raynaud"`. Quotient-source searches: `site:stacks.math.columbia.edu quotient flat locally finite presentation equivalence relation algebraic space free action`; `site:stacks.math.columbia.edu free action flat locally finite presentation quotient algebraic space`.

Opened primary source Achter–Casalaina-Martin, https://www.math.colostate.edu/~achter/math/prym1224.pdf, standing conventions p3 and §§1.7.1–1.7.2 pp12–13. First paragraph of1.7.2 already states full-Picard schematicity. The adjacent torsor-as-component descent claim has an explicit real counterexample, separately recorded only in CORRECTIONS_FOR_AUTHORS.md. Opened primary EMS page https://ems.press/journals/rsmup/articles/6577399 for Rémi Lodh, Torsors under abelian schemes via Picard schemes, RSMUP147(2022),79–89, DOI10.4171/RSMUP/91. Its abstract assumes a principally polarized abelian scheme and projective torsor over a noetherian base. Full text was behind a subscription response and was not read. A Cesnavicius PDF lead returned403; it was not adopted as a new proof input. Nonprimary generated/mirrored mathematical pages were not relied on.

Root read the exact primary portions listed in ROOT_E4_TRANSFER_COMPARISON.md, including BLR6.6Theorem2c,d; Raynaud Cor3.8 and its application, p5-15, and Theorem4.2/proof pp5-16–18; attached EGAII6.5.5–6.6.4; Poonen–Rains §§3.1–3.2 pp1311–12; Laurent–Schroer Definition4.2 and Cor4.6 pp13–15; Alexeev Theorem3.0.3 p664. Root opened Stacks06PH and03XX in full. The free smooth quotient is supported exactly by06PH; no discrete-group quotient theorem was substituted.

The transfer theorem is a proved consequence of classical inputs and is not given a novelty claim. The full-Picard conclusion has the located prior statement. These results close the higher-dimensional abelian-torsor construction expressly left open in the inherited E4 attempt lines81–93. They do not settle the arbitrary-family normal/integral questions. The finer source receipts and35-query independent worker search are in papers_2_3/E4_LITERATURE_SEARCH.md and E4_PRIMARY_SOURCE_RECEIPTS.json.

### 2026-11-23T07:10:28.280197+00:00 — original full-Picard archival question

Opened the official Montpellier cote57 PDF by HTTP byte ranges and visually read physical page315. Both page numbers on the scan identify archive sheet314. The last paragraph asks whether the Picard functor is representable for a proper flat family with geometrically normal, or merely integral, fibres. Paper2 cites sheet314 and gives PDF page315 as a secondary locator. The general question remains open; the new abelian-torsor result is one positive subcase. Exact ranges and SHA256 values: root_current/GROTH57_SHEET314_SOURCE_RECEIPT.json. No scan copy is returned.


## 2026-11-23 07:17UTC — recent local-group and Picard literature sweep

Primary-oriented web queries (system1, recency365) were: `"local fundamental group" "finite generation" 2026`; `"Picard" "geometrically integral" "scheme" 2026`; and `"Picard" "ample divisor" "p-torsion" restriction`. Results returned already compared Suzuki, Cotner–Zavyalov and projective Picard sources, and Braun's klt characteristic-zero scope; none changed a current gate. A secondary index advertised Li–Tian, *Base Change Of Local Fundamental Group Schemes*, arXiv2611.15643, submitted11November2026. Opening the official https://arxiv.org/abs/2611.15643 failed with DisabledError. The primary text has not been read and no assertion from it is adopted. Its advertised local Nori group scheme of a proper variety is not automatically the punctured-spectrum etale fundamental group studied here. This is an unverified lead only, not a literature conclusion or research movement.


## 2026-11-23 about07:25–07:36UTC — local-cover curve-degeneration search

The six exact queries, opened author pages, successful and failed retrievals, primary-source scopes and the unchanged F13.6 gate are recorded in ROOT_RESEARCH_CONTINUATION_05.md. Root read Cutkosky–Srinivasan's rational-tree prime-to-p presentation and the specified Achinger–Lara–Youcis specialization/tame-covering passages. Neither supplies the local logarithmic extension comparison needed for the proposed bounded-genus route. Download hashes and inspected pages are in root_current/F13_CURVE_SOURCE_RECEIPTS.json. No movement is claimed.


## 23 November 2026, 12:13 UTC

Positive-genus refinement: bounded primary searches on purely inseparable ruled surfaces, rational double points and very-ample Picard torsion found no exact matching application. Tziolas, Topics in group schemes and surfaces in positive characteristic, Annali Ferrara70(2024),891–954, DOI10.1007/s11565-024-00514-8, Proposition4.10 supplies related Frobenius/genus context only; not a proof input and not a priority conclusion.

## 2026-11-23: equality-cover Euler formula and characteristic-two rational normalization

Primary mathematical inputs: Mumford1969§1StepsI–VII pp326–330, Ekedahl1988Lemma0.1.5 p103, Stacks023T,05B2,0BEM,0AYQ and45.7.8/0FH0; foundational RR exact statement02UO. Full applied source/read metadata are in the two continuation SOURCE_RECEIPTS files and root comparisons. GeneralGRR is invoked as foundational, not claimed reproved from the proofless Stacks statement.

Root searched: Picard very ample torsion characteristic2 surface inseparable; inseparable ruled torsion Picard surfaces; Hexagon Picard torsion inseparable surfaces; ECCC Picard torsion algebraic surfaces; arXiv Picard inseparable ruled surface; very ample torsion restriction Picard surfaces positive characteristic. Related Lang1984weighted complete-intersection torsion-freeness was opened at printed197; it requires a weighted-complete-intersection hypothesis absent here and is not a proof input. PDF metadata: tmp/a2_positive_genus_continuation/Lang_root_receipt.json (source bytes excluded). Six separate worker queries and their bounded outcomes are preserved in its receipts. No exact characteristic-two refinement located and no priority claim.

Further root queries: torsor filtration deformed group scheme Euler characteristic; arXiv torsor degree filtration characteristic; Hexagon torsor Euler characteristic Picard surface; ECCC torsor Euler characteristic. Search results suggested the known alpha_L,a-torsor flag in Enriques Surfaces I; third-party snippets are not proof evidence, and exact primary comparison is a remaining literature task. No exact G_s character-twisted statement was inferred from that lead. Unrelated Hexagon topology/symplectic and ECCC complexity results are not applied. The filtration uses classical equivariant descent; its novelty is not claimed.

## 23 November 2026, 13:11–13:17 UTC — canonical-cover continuation and exact filtration comparison

The preceding Enriques-book lead is now checked against the official author draft: François Cossec, Igor Dolgachev and Christian Liedtke, Enriques Surfaces I, 19 April 2024, printed pp.37–40, especially equations(0.2.15)–(0.2.17), https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf. The local additive coaction and affine coordinate changes give a degree filtration for alpha_(L,a)-torsors. The paper's group instead has u^p=0 and coproduct u⊗1+1⊗u+s u⊗u; its additional character yields the twist P. This is contextual comparison with a standard construction, not a claim of priority for a filtration method. The April2024 author draft is distinguished from the published2025 second edition. Raw download returned403; the web extraction was read and hashed. Screenshot calls returned markers without image data, so no visual source-reading claim is made. Exact cache identity and limits are in ROOT_A2_CANONICAL_SOURCE_RECEIPTS.json.

Root's stronger-engine queries were `"Picard" "very ample" "torsion" "characteristic" surface restriction`; `"torsion line bundle" "restriction" "ample curve"`; `"Picard" "restriction" "genus" "characteristic two"`; and `site:hexagonmath.org Picard torsion surface restriction`. The next routine-engine queries were `site:arxiv.org "Picard" "restriction" "torsion" surface ample`; `site:eccc.weizmann.ac.il Picard ample surface`; and `"uniruled surfaces of general type" Liedtke pdf`. No exact smallest-equality nonexistence statement was located in this bounded search. Search-result dates were not substituted for publication dates.

An Open Maths course page, https://openmaths.org/courses/AG-LCL/picard-groups-and-grothendieck-lefschetz.html, explicitly credits GPT-6.1 Sol. Root read its complete Section2.1 torsion-injectivity argument and opened the original Stacks0F2A statement and proof that it expounds. The theorem concerns punctured local spectra with depth(A)≥3; it is known and not an unconditional smooth-projective-surface restriction theorem. No comparison-source claim supplies the missing cone depth hypothesis here. Its adjacent general injectivity discussion was not used as a proof input. This page is not attributed to a human author or treated as a new result of this task.

Liedtke's primary arXiv abstract and metadata, https://arxiv.org/abs/math/0608604, identify Uniruled Surfaces of General Type, v2 dated6November2006, published Math.Z.259(2008),775–797. Its constructions concern uniruled general-type surfaces, vector fields and nonreduced Picard schemes; the abstract does not assert the specified very-ample restriction equality. The whole paper has not been read for this comparison and is not an applied theorem. Secondary aggregator and discussion snippets were discovery leads only. The new duality argument uses the exact proper Cohen–Macaulay Stacks0FVZ(4)/0FW0 statements and the complete direct determinant argument; no norm or smoothness hypothesis is silently imported.

## Cached primary-book completion — 2026-11-23T13:33:24.417958+00:00

The attempted new raw download returned403 as previously recorded. Root subsequently located the existing official-author PDF cache, SHA2563c6bf1d54954e28728935bbe1f4b1e38435fe469cf2b8543d657087815a2f526,3483048bytes,704pages,19April2024version. Root read the entire extracted printedpp38–40 and individually opened physical pages54–56 visually at13:31UTC. The footer quotient in(0.2.17) is now checked directly: the additive-torsor flag has successive quotients L^(-i). This closes only the earlier extraction/visual limitation. It is standard-method context for the separately proved multiplicative-deformation flag with character twist. No external source copy or extraction enters the ZIP. Full metadata and raster/text hashes are in ROOT_A2_CANONICAL_SOURCE_RECEIPTS.json.

## Projection-source search — 2026-11-23T13:41:10.914496+00:00

Queries: `site.stacks.math.columbia.edu projection smooth projective variety unramified projective dimension`; `site.stacks.math.columbia.edu double point formula self intersection unramified`. The opened primary Stacks pages0B1N,0FV9,0FEZ,02G3 support the direct candidate reconstruction in ROOT_A2_PROJECTION_CANDIDATE.md. No third-party textbook mirror was used. This is a standard intersection-theoretic method, not a priority claim. Source identities and exact reading scopes are in ROOT_CONTEXT_PROJECTION_SOURCE_RECEIPTS.json. The candidate characteristic-three degree refinement has not yet been accepted.

## Positive-genus and projection comparisons — 2026-11-23T14:07:27.870345+00:00

General mathematical searches: Picard variety restriction ample divisor injective positive characteristic torsion Neron Severi; Lefschetz Picard reduced identity component smooth ample curve surface characteristic p kernel; Hexagon-domain Picard inseparable surface Albanese torsion. No exact equality-case refinement identified. Cotner–Zavyalov supplies strongly ample/complete-intersection results, not the general geometric-point statement. The complete Kleiman2005Remark5.8pp39–41 was read; its finite unipotent general-hyperplane kernel leaves characteristic-p points possible. FGA232/236 classical existence and Albanese duality were checked in attached LaTeX. The exact equality-case factorization and separability are proved here without claiming priority.

Catanese–Oguiso, JLMS102(3)(2020),1337–1356, DOI10.1112/jlms.12371, author-copy Section5pp12–18 supplies the known all-characteristic double-point theorem. Root and an exposed auditor rederived the required inequality by finite unramified projection and refined Gysin, retaining full finite scheme lengths. The rational-cover p3 specialization now requiresd≥22. Exact source hashes/locators and inaccessible final-journal endpoints are in a2_projection_audit/source_register.json. Intermediate author-copy slips are in the corrections dossier only.

## Generic-fibre refinement sources — 2026-11-23T14:24:51.965186+00:00

Official Stacks0BE6,0BE8,031T were opened and read in full, including both lemma proofs. The elementary divisor/separability argument is given completely, with no priority claim. The related0C5Y smooth-generic-fibre statement is comparison-only and is not invoked. Bounded Picard-restriction overlap and exact Kleiman/Yuan–Zhang reading scopes are in a2_odd_positive_genus_continuation/ns_residual/LITERATURE_OVERLAP.md; root independently checked Kleiman and the applied Stacks sources. No source copies enter the workbench.

## All-characteristic strict bound comparison — 2026-11-23T15:10:20.536823+00:00

The separate bounded primary-literature report froze15:07:55UTCin a2_allp_strict_literature. Exact queries cover arXiv,journals,authors,Stacks/taghistory,ECCCandHexagon,with failed nativeHexagonopens retained. LangerTheorem9.1 supplies a non-strict slope obstruction;Kweon's inspectedarXivv2Section7discusses the kernel/injectivity question;Cotner–Zavyalov requires stronger Hodge ampleness. No exact strict-bound overlap was located in that bounded scope;no novelty or exhaustive-search claim. Root has read RESULT.md;remainingmetadata and primarycomparison are pending and manuscriptreferences will be integrated afterward.

## Completed root comparison of Langer, Kweon and Cotner–Zavyalov — 2026-11-23T15:19:43.111896+00:00

All six frozen report files and the exact primary scopes specified in ROOT_A2_ALLP_LITERATURE_COMPARISON.md have been read. Thirteen hashes PASS. Three scoped comparisons are installed in Paper2. Kweon locators refer expressly to arXivv2, not uninspected published numbering. A separate current-status search continues; no current universal-open or novelty claim. Stacks0F2A depth restrictions and bounded Hexagon/ECCC failures are preserved.

## Bounded current-status follow-up through 2026 — 2026-11-23T15:30Z

The six-file report a2_picard_restriction_current_status froze15:26:48UTC; root fully read it and verified26hash occurrences. Correct publication DOI citation chains were followed to primary passages, with the OpenAlex arXiv-identity mismatch isolated. No unrestricted smooth very-ample surface point-injectivity result or explicit point counterexample was located within that scope. This is not a current-open or absence assertion. Exact searches, versions, dates, limitations and inaccessible final Kweon numbering are preserved.

## General adjoint and known general-type consequence — 2026-11-23T15:49:15.808934+00:00

The complete bounded comparison is ROOT_GENERAL_ADJOINT_LITERATURE.md. Root read EkedahlIITheorem1.6p125and the complete Langer/ZhangTheorem3.1proof,arXiv2103.04268v7pp4–5. Their vanishing theorems already imply that the hypothetical very-ample geometric Picard-point kernel surface is of general type. The stronger exact nef residual adjoint and canonical derivative subsystem are not identified in the bounded inspected sources;no priority claim. The attached A2W rank≥ambient-dimension−1 antecedent is explicitly compared with the stronger h0(O(Y))−1bound. Exact searches,partial response preservation,primary PDF hash and scopes are in that record. A newly found possible ZhengCor4.4source correction is under separate audit only.


## Record: workbench/records/root_current/LITERATURE.md


## 2026-11-23 05:59UTC — exact separated étale finite-fibre input

Root opened and read the complete official statements and proofs of Stacks Tags07RY (Lemma37.45.3, https://stacks.math.columbia.edu/tag/07RY) and086R (Lemma37.45.5, https://stacks.math.columbia.edu/tag/086R). Query mechanism: direct opens, not a novelty search. Neither requires quasi-compactness in its hypotheses. The latter makes the degree-at-least-d loci open; over a noetherian base, finite degree at each of the finitely many generic points gives a uniform finite bound. The former supplies a finite stratification with finite locally free restrictions. The strata are quasi-compact over a noetherian base, so their inverse images prove quasi-compactness of the whole morphism. This confirms the exact input to the revised openness proof without circularly assuming quasi-compactness. Search-service references:turn451292376view0 andturn451292376view1. No source copy is included.


### Published-version locator confirmation — 23 November2026,07:43UTC

The Cambridge published PDF has now also been retrieved and read directly: Example3.3.6 is on printedp1862; Example3.4.6 and its full proof are onpp1867–1868, with footnote6 onp1867. Root read those complete extracted passages after the separate worker located them. They agree with the previously inspected primary HTML and author text; this is a source-locator extension of the same correction, not a new correction or a new mathematical result. Published PDF URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8556201EDB51D7F2F76F5950A800CD64/S0010437X24007231a.pdf/lefschetz_theorems_in_flat_cohomology_and_applications.pdf . Bytes987695; SHA2564c6c3263ff5a77636d5771b8fedbfac91e2153f0b5fd67ce9339ece55a44f5a1. The PDF and its extraction remain outside the deliverable. No author was contacted.


## 23 November 2026, 08:25 UTC: modification audit and singular adjunction

Root read the entire frozen M2 exact-input/literature audit and its48-query receipt. Su–Wang, arXiv2409.10296v2, Lemmas3.22–3.23 and Remark3.24,pp19–21, supplies a verified rank-one determinant/ideal-of-points precedent. The exact arbitrary-base torsor schematicity consequence was not located by that bounded search; no priority claim is made. Kollár1990 Lemma6.13 was not directly accessible and is not an input. The primary sources used by the separate statement-only reconstruction were opened and compared by root, including attached French EGAIV11.3.7 and12.2.4(viii) and Stacks054F,0BBQ,00O7 and06NN. Exact source/exposure receipts are in ROOT_E4_MODIFICATION_FRESH_COMPARISON.md and the frozen worker records.

The singular-general normalized-cover identity uses the exact primary Stacks statements0AX2,0AA4,0FVZ,0FW0,0AY6,0AY7,0AYZ and0BFQ; root read their statements and proofs, with hypotheses checked in ROOT_A2_SINGULAR_ADJUNCTION_COMPARISON.md. The quasi-elliptic source passages and hashes are in root_current/A2_RESIDUAL_SOURCE_RECEIPTS.json and ROOT_A2_RESIDUAL_COMPARISON.md. The known formulas are credited; the new scoped deductions do not settle the general Picard-point question. The book proof typo is kept in the correction dossier only.

## 2026-11-23, normal-base projective bundles and F13 continuation

The exact normal-base theorem and bounded searches are documented in `papers_2_3/E4_PROJECTIVE_BUNDLE_NORMAL_PROOF.md` and its frozen source receipts, with root's complete comparison in `ROOT_E4_NORMAL_BUNDLE_COMPARISON.md`. Root read the full attached-LaTeX proofs of EGA IV4 21.12.7 (pp.307–308) and 21.14.3 (pp.325–328), the complete relevant Milne Propositions9.2/10.1 and Remark9.3 (author revision pp.14–17), and Stacks02TX/02TZ with their proofs. These are classical inputs, not novelty claims. Root subsequently read all five pages of Zomervrucht, Ineffective descent of genus one curves, arXiv:1501.04304 (PDF bears April22,2018 while arXivv1 bears January18,2015). Theorem2.1 and Section3 give nonschematic elliptic torsors over a normal noetherian local surface, so the normal-base obstruction is substantive. Root also read Brion, Homogeneous projective bundles over abelian varieties, ANT7(2013), printed2475–2479, DOI10.2140/ant.2013.7.2475. That work studies homogeneous bundles over an abelian variety over an algebraically closed field; the theorem here concerns arbitrary vector bundles over relative torsors and does not assume homogeneity. Its full later classification proofs were not checked or used. Exact source hashes and addresses are in the frozen projective-bundle receipts. No exact precedent was located in the bounded search; no priority claim is made.

For F13, primary journal searches and exact scope readings of Hu--Teyssier, Characteristic cycle and wild Lefschetz theorems (2026), and the public Grothendieck--Murre chapter9 preview are documented in `ROOT_RESEARCH_CONTINUATION_06.md` and `root_current/F13_REVIEW06_SOURCE_RECEIPTS.json`. The global finite-type theorems were not transferred to the required complete-local uniform gate; the limited preview is not a full proof check. The direct Hu--Teyssier download was empty and has no publication-byte hash. No new F13 result is asserted.
# 2026-11-23, 09:32 UTC: exact Ekedahl application and two source corrections

The smallest equality case is an application of T. Ekedahl, *Canonical models of surfaces of general type in positive characteristic*, Publ. Math. IHES67(1988),97–144, DOI10.1007/BF02699128. Root and a separate exposed auditor each read all of I.2.4 and its proof, printed109–115, and the forward-referenced II.1.7 proof at126–127. Root also read103–108 in full, checking the first-Betti lemma, Frobenius-twist convention, saturated foliation definition, double-cover algebra and dualising formula. The fixed normalized Kummer cover is identified by invariant fields and affine integral closure. The exact source hash, page scope, all hypotheses and residual branches are recorded in ROOT_A2_EKEDAHL_COMPARISON.md; the frozen separate audit and source receipts are in a3_a2_ekedahl_audit. This is a known theorem applied, and is not called new.

The source's first paragraph on printed112 omits two inverse signs. The correction follows from its own I.1.7 formula(1.9) and the finite-flat norm, and leaves I.2.4(d) unchanged. It is recorded only in ROOT_SOURCE_CORRECTIONS_09.md and the consolidated corrections dossier. No author was contacted.

A separate bounded check of Milne's Abelian Varieties Remark8.5 verified the same false product decomposition in the 2022 author revision p14 and original1986 chapter pp116–117. The complete explicit elliptic-curve counterexample, exact edition hashes, and official errata searches are frozen in papers_2_3/MILNE_AV_REMARK_8_5_CORRECTION.md and its source receipts. Root read the full proof and visually checked both editions. The published translation/Picard statements used by the projective-bundle theorem are separate and unaffected. The bounded official lists contained no matching correction; prior reporting is not exhaustively settled and no priority claim is made.



## 23 November 2026, 09:53 UTC — K3 refinements and scoped errata checks

The dated worker search/source JSON and full root comparison for the K3 branch identify the precise prior inputs: Matsumoto, JAG32(2023),271–322, arXiv1812.03466v5, Proposition2.10 p5, Theorem3.3/Table2 pp10–11 and Proposition4.1 with proof pp16–17; and arXiv1710.07158v3, Proposition4.8/Table3 pp13–15. Root read each entire required proof and the adjacent scope discussion. Exact URLs, PDF hashes and reading bounds are in ROOT_A2_K3_STRUCTURE_COMPARISON.md. The canonical-Enriques-cover derivation theorem does not apply and is not used. These are known classification/rational-quotient theorems applied to a conditional branch, with no priority assertion.

The Milne original1986 chapter and current2022 revision both contain the exact false p-torsion product assertion. The bounded official errata search and independent formal-group recomputation are in papers_2_3/MILNE_AV_REMARK_8_5_CORRECTION.md and MILNE_AV85_COMPUTATIONAL_CHECK.md. The separate Ekedahl inverse-sign search opened the original issue and publisher/Numdam records and queried both engines; no matching official correction was located within those bounds. See EKEDAHL_P112_OFFICIAL_ERRATA_SEARCH.md and its full receipt JSON. Search failure is not a claim of first discovery. Both corrections remain outside the papers in the author-correction dossier.



## 23November2026,10:25UTC — very ample exclusion and a nonnormal-base obstruction

The complete dated proof/source receipt a2_very_ample_sources_v1.json records25 queries and exact primary PDF/HTML hashes. Root read Kadets arXiv1809.07293v4 pp1–5 in full, including Proposition2.8 and its geometric induction, and checked the singular-curve trisecant and generic-separability bridges explicitly. The result used is only n-transitivity for nonstrange curves, not a stronger permutation-group classification. Stacks0FV9 and0FEZ supply regular-immersion self-intersection and Gysin identities; 01XT supplies the fully read Cech calculation; 02UO states all-characteristic GRR, whose surface numerical specialization is used as classical background. Exact root search terms, outcomes, reading bounds, failed/unused Rathmann and Hartshorne routes, and the primary-source comparison are in ROOT_A2_VERY_AMPLE_COMPARISON.md. Both search engines, ECCC and Hexagon were queried. No exact earlier corollary was identified in those bounds; no novelty or priority claim follows from that silence. A Catanese–Franciosi–Hulek–Reid search hit was not opened or used as an input.

For the nonnormal projective-bundle question, root read the complete Example6.1, Proposition6.2 and Corollary6.3 on printedpp1574–1575 of Bhatt, Algebra Number Theory6(2012),1561–1577, official https://msp.org/ant/2012/6-7/ant-v6-n7-p10-s.pdf, SHA256 b05d4ae51c8c8db240dbd24c7cca898cad85290afcf864b75c7eafca04abccf9. The cited normal semilocal infinite-order torsor obstructs the proposed shortcut from normalization-schematicity to semilocal projectivity. Raynaud's original example was not independently reconstructed, and this is recorded only as a source-based obstruction to that route. See ROOT_RESEARCH_CONTINUATION_07.md; no additional theorem or movement is claimed.

# 23 November 2026, 10:37 UTC — known FGA Hilbert erratum

Queries on both engines: `Grothendieck FGA exposé 221 lemme 3.5 correction polynome U_N`, `Hilbert Grothendieck 3.5 errata`, `Grothendieck 221 3.5 errata`, and `FGA P Q 3.5 correction`. The official Numdam metadata for the author's 1962 erratum, https://numdam.org/item/SB_1961-1962__7__302_1/ , was located. Root read the full attached French e221.tex, SHA256 ba1f156eea41e72646b75c956d6caf2482cedabea46911278588e1d7e103075a, and the original relevant proof in attached221.tex, SHA256 2485e1297c5aff1346ce7dcb031d5637778a974b47532a13de19a034d9754ee7. The polynomial-sign repair needed in Lemma3.5's proof is explicitly already corrected on p.302, referring to original exposé p.15 lines13 and15. It is recorded as known in ROOT_SOURCE_CORRECTIONS_09.md; no novelty or new movement is claimed. Search snippets concerning unrelated books were not used, and no EGA/FGA/SGA scan was fetched.

# Literature search: arbitrary-base projective bundles on abelian torsors

Date: 23 November 2026, approximately 10:28–10:51 UTC. Root search and source comparison. These are bounded searches, not a priority determination. Exact new result: a positive-rank projective bundle on an abelian-scheme torsor is schematic if and only if the torsor is schematic, over every scheme base.

## Queries and findings

The authoritative search engine was used for these general-term queries:

- `"projective bundle" "abelian torsor" scheme`
- `"projective bundle" "non-schematic" torsor`
- `"projective bundle" "algebraic space" "scheme" descent`
- `"Brauer-Severi" "nonschematic"`

The complementary engine was then used for:

- `site:arxiv.org abelian torsor schematic projective bundle`
- `site:hexagonmath.org abelian torsor projective bundle`
- `site:eccc.weizmann.ac.il schematic projective bundle torsor`
- `"fibré projectif" "torseur" "schéma abélien"`

No exact arbitrary-base schematicity implication was identified. The arXiv and journal/author hits included the already opened Brion and Zomervrucht sources, and Jef Laga's arXiv:2510.24678v2. Laga's relevant sections had already been read and compared in the earlier Paper2 literature record (Section3.6 p19, Section4.4 pp26–27, Sections5.3–5.4 pp30–33); the metadata was reopened here, not the entire work reread. Brion concerns homogeneous projective bundles over abelian varieties over a field; Zomervrucht gives nonschematic normal-local abelian torsors. The exact scopes and original hashes remain in the earlier source register. Hexagon returned general listings without the relative theorem. ECCC produced no useful exact result. Those negative search results are limited to these queries and date.

The primary journal page for D. Huybrechts and D. Mattei, *Splitting unramified Brauer classes by abelian torsors and the period-index problem*, Math. Ann.392(2025),2913–2932, was opened:
https://link.springer.com/article/10.1007/s00208-025-03161-2
Root read the introduction, Theorems1.1–1.2 and Section1.3. These concern splitting Brauer classes over the function field of an integral projective variety by abelian torsors, rather than schematicity of a relative projective-bundle base. No proof of that paper was relied on or claimed read. Cached journal HTML:426493bytes, SHA256000cd6b8b827f9da8c7d8b3eae91700c975fbda95fe8ff5646e135de55a3f4e2.

SGA4 cohomological projective-bundle hits concern a different assertion and were not downloaded. A Rydh approximation search snippet was not used as a substitute for a primary theorem. The exact approximation inputs are the attached EGA and the already opened Stacks07SK.

## Projectivity bridge: rejected and unused leads

These further queries explored the possible normal semilocal projectivity bridge:

- `abelian scheme normal semilocal base projective polarization Raynaud`
- `abelian scheme normal base not projective affine semilocal`
- `Faltings Chai degeneration abelian varieties Chapter I Remark 1.10 normal projective pdf`
- `Raynaud Faisceaux amples XI 1.4 pdf normal`
- `"Faltings" "Chai" "1.10" "normal" pdf`
- `"Degeneration of Abelian Varieties" filetype:pdf`

A secondary discussion suggested extending a generic polarization. That suggestion was not used. Faltings–Chai ChapterI publisher metadata was opened, but the primary proof was not obtained or bypassed. Cached metadata at https://link.springer.com/chapter/10.1007/978-3-662-02632-8_1 is225961bytes, SHA25607852415d69a14b8ec465e022c4adc01b43ba58d60fb9e6b9c86379e064f7b68. The final argument instead verifies the saturated-open hypothesis of BLR6.6.2(c) over the original local base, inherits AF through the finite map, and applies(d) over the normal cover. Root read that complete proof at printed164–166.

Laurent–Schroer, *Para-abelian varieties and Albanese maps*, journal HTML https://link.springer.com/article/10.1007/s00574-023-00378-0 was opened for Section4, especially Corollary4.6 and its complete proof. Root also read the matching author PDF Section4 pp12–15. The dual and finite-flat torsion inputs are used. Its cited unconditional AF/quasiprojectivity assertion is stronger than necessary and is not the bridge used here. Cached HTML:577655bytes, SHA256799fa481386a34e9a203bdaaece4636d7640dd411075b491567acfa77a056f37. Exact PDF and applied-source hashes appear in E4_NONNORMAL_SOURCE_RECEIPTS.json.

Bhatt's ANT paper was identified against its official publisher address, not the misleading cached filename of the different Compositio paper. Root read complete Section6, pp1574–1575, including Example6.1, Proposition6.2 and Corollary6.3. The example rules out the shortcut that every schematic normal-semilocal abelian torsor is projective. The final proof uses extra affine opens from the original projective-bundle scheme, so makes no such assertion. The exact source and rejected-filename metadata are preserved in the author receipt.

## Literature classification

No exact precedent for the full statement was located in this bounded search. Classical Cartier-boundary, group-action, Picard, intersection, norm and effective-descent inputs are credited by exact statement and page. The manuscript claims the stated implication with its proof, makes no priority claim, and states precisely how the neighboring works differ. General schematicity of Picard functors for all proper flat geometrically normal or integral families remains open.

## 23 November2026,11:03–11:08UTC: distinguished almost-ruled cover and adjacent source diagram

Root authoritative queries: "p-torsion" "ruled" "Picard"; "inseparably ruled" "differential"; "mu_p" "ruled" normalization ample. No exact distinguished-cover statement identified; Lang1984/Raynaud1979 and other leads not used as proof inputs. Full applied official Stacks031W,0C5H,0AGP and0BAK proofs were opened and read, with exact hashes in a2_almost_ruled_fresh/SOURCE_RECEIPTS.json and root scope in ROOT_A2_RULED_COVER_COMPARISON.md. No priority claim. Complementary queries "Stacks" "0AGS" quotient typo and "54.3.4" "quotient" correction, plus the complete official0AGS tag history, did not identify a listed quotient repair. The current proof reverses numerator and denominator in part(4); its exact repair is in ROOT_SOURCE_CORRECTIONS_10.md. The theorem is unchanged. No author contacted.

## 23 November2026,11:21–11:24UTC: checking continuations

Root numerical-source queries: Kleiman "Toward a numerical theory of ampleness" pdf293344; site.stacks.math.columbia.edu "Kleiman" "nef". The official Annals metadata confirms DOI10.2307/1970447 but supplies no full proof; no primary numerical proof accepted from this search. Root additionally opened and read full official Stacks031V,0AHI and0AHH statements/proofs to expand the distinguished-cover dependencies. Their hashes and acquisition receipts are in ruled_cover_exposed_audit/SOURCE_RECEIPTS.json. Exposed audit acceptance is not a new novelty search or mathematical movement.

## Normal-base source completion — 2026-11-23T11:46:16.177764+00:00

Root opened the author-hosted Lazarsfeld Chapter1 at https://www.math.stonybrook.edu/~roblaz/Reprints/Laz.PAG.Chapt1.pdf (SHA25668001621457020858e287168fc51648800759e3e1c6cc82d05049805852ba73b), and read the complete applied cone/ampleness proofs and explicit characteristic remarks recorded in ROOT_E4_NORMAL_THIRD_COMPARISON.md. Root opened https://chngr.github.io/assets/theorem-of-the-base.pdf (SHA2568360197abd11f49a67ac2c297c8d1d6e47a6db92e25bbb0fa72030cb5b515dba) and read its entire appliedSection5, author-versionpp14–16. Root opened both official Stacks Bertini sections0FD4 and0G4C and read every statement/proof, then read all of0D2N and0B44 from verified official cached HTML. Complete BLR6.6Theorem2 and attached EGA proof overlaps were reread. These are full alternative source verifications, not retrieval of the missing Kleiman1966 original. All metadata/search receipts of the exposed supplement are frozen and wholly read. No new theorem-priority claim follows from this source completion.

## First all-base isolated attempt: source inventory — 2026-11-23T11:54:13.405446+00:00

The entire34-entry SOURCES.json and exposure log in all_base_bundle_unaided were read by root. The report records unsuccessful Picard/Albanese, quotient, finite-multisection, normalization, positivity, frame/cone and torsion routes. It remains UNRESOLVED. Exact source snapshots/locators and inspection limits are preserved; root verified43source snapshots. Its literal complete search-query/result sequence was not retained, and no exhaustive archive is claimed. Its online SGA3 text fallback does not satisfy this task's attached-edition gate and is not promoted into a new checked paper result. No source bytes are delivered.


## Record: workbench/records/papers_2_3/LITERATURE.md

# Literature searches and source checks

All searches below were performed on 2026-11-23 in this run. Search negatives are not priority certificates. Sources fetched for inspection live only in temporary scratch; hashes are in FETCHED_SOURCES.tsv.

## Polarization torsors

Queries: `Poonen Rains Self cup products 3.6`; `Poonen Rains symmetric line sheaves polarization canonical theta characteristic rank 2 universal section`; `polarization at most one odd theta`. Opened Poonen–Rains, *Self cup products and the theta characteristic torsor*, Math. Res. Lett. 18 (2011), 1305–1318, publisher PDF https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/2011/0018/0006/MRL-2011-0018-0006-a018.pdf. Proposition 3.6 and diagram (3.7), pp.1312–1313, give exactly the sheaf-valued quadratic-refinement correspondence. Proposition3.12 includes field-specific criteria, but its part(f), statementp1314 and proofp1315, also gives exactly the canonical rank-at-most-two refinement used for the positive half here. The first record understated that overlap; the corrected attribution is explicit below and in the paper. The query also found the classical principal-polarization obstruction described in theta-divisor surveys; primary comparison is still to be opened. No settled novelty classification yet for the arbitrary type criterion.

## Very ample Kodaira nonvanishing

Queries: `very ample Kodaira vanishing surface characteristic 2 Raynaud`; `Lauritzen Rao elementary counterexamples Kodaira vanishing very ample surface H1 negative line bundle`; `very ample root Kodaira cover`; `root covers very ample Kodaira`; `very ample surface H1 Kodaira Raynaud`. Opened Lauritzen–Rao, arXiv:alg-geom/9604012, https://arxiv.org/pdf/alg-geom/9604012. Its introduction, pp.1–2, explicitly answers the very-ample question using dimension-six-or-higher examples; the simplest has H^5(L^{-1}) nonzero. The text warns that hyperplane sections need not inherit the nonvanishing. It does not contain the surface H^1 example under review. The searches have not yet established whether the simultaneous-root upgrade is folklore or in print. No novelty claim is certified.

## Representability

Queries: `Murre 1965 representability Corollary 2`; `Murre 1965 Representation of unramified functors 294 pdf`; `Grothendieck archives Montpellier 131 pdf Descentes`; `Grothendieck 131 14 modulaire`; `site:grothendieck.umontpellier.fr 131.pdf`; `Foncteurs représentables quasi fini Grothendieck`. Opened the primary Numdam PDF https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf. Theorem 1 is on printed p.246; Corollary 2 and the announced locally quasi-finite analogue are on printed p.247, PDF page6 including cover. The note does indeed announce a similar theorem with unramified replaced by locally quasi-finite, but gives no exact eight-axiom version there. Montpellier archive page https://grothendieck.umontpellier.fr/archives-grothendieck/ identifies cote131; its HTML viewer data links to https://grothendieck.umontpellier.fr/131.pdf. Direct web-tool opening failed; local public download is in progress.

## Metabelian local fundamental groups

Queries: `Krishna Majumder 2026 Swan`; `Krishna Majumder Swan ramification 2026`; `Krishna Majumder Kato ramification`; `local fundamental group metabelian surface`. Opened arXiv:2601.12177v2, https://arxiv.org/abs/2601.12177 and https://arxiv.org/pdf/2601.12177. The version is dated 8 November 2026 and remains a preprint on the opened record. Its standing snc-pair assumptions are regular, equidimensional, noetherian and F-finite, p.2. Theorem9.4(1), p.55, explicitly says level-wise monomorphism; Corollaries9.6–9.7, pp.55–56, and Lemma9.8, pp.56–57, match the input used by the source argument. The text compares the finite-type case with published Kato–Leal–Saito Thms4.2.2/4.3.1, and Remark9.12 p.58 points to Kato's integrality theorem7.1. This is a concrete next published-source route; replacement is not yet proved.

## Subsequent primary-source checks, 2026-11-23

### Published replacement for the refined Swan input

Queries: `Kato integrality theorem 7.1 refined Swan`; `Bright Newton Evaluating wild Brauer group regular local`; `Kato Leal Saito refined Swan conductor 3.2`. Opened Bright--Newton's author version https://arxiv.org/pdf/2009.03282 (v5, 5 October2023), and the published reference Inventiones234(2023),819--891, DOI10.1007/s00222-023-01210-8. Section4.3, Theorem4.1, author PDF pp24--25 / journal pp848--849, restates Kato1989Theorem7.1 for an excellent regular local ring, with a residue field of finite p-degree and a character unramified away from a simple normal crossings parameter divisor. It gives the integral logarithmic form of the refined Swan conductor. This is exactly the local integrality needed to extend the generic nonzero refined conductor to the exceptional curve in F10. The argument does not require the newer global levelwise injection. Kato's publication is *Swan conductors for characters of degree one in the imperfect residue field case*, Contemporary Math.83(1989),101--131, DOI10.1090/conm/083/991978. Remaining exact dependency audit is identified in CURRENT_GATES.md.

### Henselian descent

Opened the published author/institutional PDF https://pure.uva.nl/ws/files/230886016/On_weakly_tale_morphisms.pdf: A.J.deJong and N.Olander, *On weakly etale morphisms*, JPAA228(2024),107532, DOI10.1016/j.jpaa.2023.107532. Theorem2,p2 gives the henselian descent result for a weakly etale faithfully flat map. Applying it to etale covers proves the etale-sheaf step for the nilpotent functor P. It alone does not prove arbitrary fpqc descent; the paper supplies the separate local algebra argument for that.

### Archive numbering and actual text

Official primary archive files https://grothendieck.umontpellier.fr/131.pdf and /59.pdf were fetched, with hashes in FETCHED_SOURCES.tsv. Directly viewed cote131 sheets13,34,36 (PDF pages14,35,37). Thus the source's 'scan14' is archive sheet13, not sheet14. Sheet13's axiom7 has a crossed-out pro-modular formulation, while the displayed remaining premise is modularity on local tests. Sheet13's axiom8 does not include a finite-type qualification. That literal omission is addressed explicitly in the paper by a represented-functor counterexample and a qualified formulation. The definitions on sheets34 and36 match the local-ring interpretation. Cote59 sheet13 (PDF14) was directly viewed for the short canonical-torsor quotation. Cote128 was then fetched; sheets25 and26 were directly viewed. Sheet25 states all three parts of the finite semilocal theorem, including Artinian arbitrary-rank flat descent and finite-rank descent before completion. No guessed archive locator is used for these quotations.

### Representability dependencies and comparison literature

Queries: `Murre locally quasi finite analogue representability`; `SGA3 XV 8.9 Murre representability`; `Artin representability excellence Murre quasi finite`. Opened Murre's primary Numdam paper again, Theorem1 printedp246, Corollary2 and the unproved locally-quasi-finite announcement printedp247; Appendix section4 effective descent case(d) is the completion-descent input. Murre's published main theorem is unramified; it is not refuted by P, whose closed fibre is alpha_p. The exact later-publication status of the announced locally-quasi-finite analogue remains unadjudicated. No assertion of novelty is certified.

Opened primary Stacks pages https://stacks.math.columbia.edu/tag/04GH (finite local branches over henselian bases), /06DD (residue-field issue for modular branches), /086R and /07RY (finite fibre degrees and stratification used for quasi-compactness), /03KV (valuative separatedness), /0417 (separated locally quasi-finite algebraic spaces are schemes), and /00IN (Artin--Rees). Their precise hypotheses were compared to the rewritten proof. A complete tag-history audit is still pending.

### Finite-algebra logarithmic orbits (earlier proof route, now replaced)

Queries: `site:jmilne.org 17.64 unipotent`; `Kostant Rosenlicht orbits closed Milne`. Opened Milne's primary book PDF https://www.jmilne.org/math/Books/iAG2017.pdf, Theorem17.64, printedpp373--374 (PDF pages385--386). It states that a unipotent group variety over an algebraically closed field has closed orbits on an affine algebraic scheme. Its proof is present there. This was an input to the earlier finite-rank proof route. The current rewritten paper replaces that route by elementary normalized additive primitives and nilpotent matrix induction; it uses neither this orbit theorem nor an infinite nil-semigroup argument. This entry preserves the actual search history, not a current dependency.

### Completed local-group published-source audit and overlap searches

Further queries: `punctured spectrum metabelian fundamental group`, `local fundamental metabelian Grothendieck`, `punctured spectrum abelian inertia`, `Suzuki nilpotent tame coefficient`, `Sun Frobenius filtration truncated symmetric powers`. The stronger search engine returned Suzuki's nilpotent result and related local fundamental-group literature but no exact metabelian statement in the retrieved results. This is limited coverage, not proof of novelty. No priority claim was added.

Opened and downloaded Suzuki2023 arXiv2207.01563v4, Theorem1.2p2, Propositions2.1 and3.1–3.4pp4–7; Sun2008 arXivmath/0611360v2, local Frobenius calculationpp6–8 and Theorem3.7pp12–13; Cadman2007 author PDF root construction §§2.3–2.4pp7–10; Borne2007 arXivmath/0604458, Theorems4–5pp12,17 and Proposition6p22. The complete-local application of the Frobenius calculation was separately checked in completed regular charts, not inferred from a finite-type-over-k theorem without explanation.

The published replacement for the earlier preprint dependency is now complete: Bright–Newton2023 §4.3 Theorem4.1, author v5pp24–25, printedpp848–849, gives exactly Kato's local integrality input. Kato–Leal–Saito2019 §§3.2.2–3.2.3, printedpp152–153, gives the coordinate weights for the characteristic-p Witt filtration and the restriction calculation. The paper uses no theorem from Krishna–Majumder2026. The original Kato1989 PDF itself was not obtained; the precise published restatement was read in full and is explicitly cited as such.

Opened Lipman1969, *Rational singularities with applications to algebraic surfaces and unique factorization*, official Numdam PDF https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf. PartIV starts with an arbitrary two-dimensional normal local ring admitting a desingularization, printedpp221–222. Lemma14.1printedp224 proves negative definiteness in this exact generality. It is not a complex-analytic-only result. Opened SGA1 XIII Proposition5.2, reprintp315/originalpp428–429, for tame extension after prime-to-p roots in a regular SNC pair. Opened SGA1 XIII Corollary2.12, reprintpp290–292/originalpp392–395: its first statement bounds the full tame curve group, not merely its prime-to-p quotient. Opened Stacks59.91.11 Tag095S: proper base change is for all torsion sheaves and includes F_p coefficients. The root-stack reduction to this scheme theorem is proved explicitly.

### Completion descent, exact final locator

Murre1965 Appendix theorem case(d) is printedp259, official PDFpage18; its proof continues onp260. The hypotheses are an fpqc covering map with locally noetherian source and a separated, locally quasi-finite, locally finitely presented scheme over it. These are exactly satisfied by the completion cover used in the criterion. The original noetherian local base need not be excellent. Its complete local cover is the noetherian source required by case(d).

### Published connectedness input for the independent Paper1 check

Query: `Connectedness Bertini theorem via numerical equivalence journal Martinelli Naranjo Pirola`. Opened the author version arXiv1412.1978v2 and then the published University of Barcelona repository copy of Martinelli–Naranjo–Pirola, Advances in Geometry17(2017),31–38, DOI10.1515/advgeom-2016-0028. Theorem1.1 is printedp31 and works in any characteristic. It supplies connectedness of the inverse image of a fixed linear curve section under every finite normalization cover. Exact published file and SHA are in FETCHED_SOURCES.tsv; the old dspace/bitstream path returned404, while the current API bitstream path succeeded. Raynaud1972 Chapter4 section4 Proposition5p30 and SGA1 IX Corollary5.2 originalpp247–248 were also opened and checked for that independent task. Detailed derivation and exposure boundary: BLIND_PAPER1_BOUNDARY.md.

### Very ample surfaces and polarization literature, additional searches

Opened Zheng's author version https://arxiv.org/pdf/1509.04993. It corrects and generalizes Raynaud surface constructions; it does not establish that the particular generated line bundle here is very ample. Verified publication metadata against the publisher https://www.sciencedirect.com/science/article/pii/S0022404916302377: JPAA221(10)(2017),2431--2444, DOI10.1016/j.jpaa.2016.12.030. Corrected an erroneous page range in our first bibliography. Queries `very ample root Kodaira cover`, `simultaneous roots very ample surface`, `universal polarization odd theta Picard`, and `polarization at most one odd elementary divisor` did not settle exact overlap. A primary thesis on the Picard group of the universal abelian variety was found at https://arcadia.sba.uniroma3.it/bitstream/2307/6008/1/Tesi%20%281%29.pdf; its full comparison remains a next route, so this is a lead rather than a cited result. Raynaud's 1978 original is credited, but its complete original text has not yet been opened in this run; the construction is proved directly and compared with the opened Lauritzen--Rao and Zheng papers.

Searches scoped to Hexagon (`site:hexagonmath.org Kodaira`, `theta`, `representability`) and ECCC found no exact matching result in the retrieved sets. Opened the Hexagon homepage; the example URL2611.00789 did not resolve through the retrieval tool. These limited negatives neither establish absence nor justify a novelty claim. No unrelated AI result was inserted merely to mention AI laboratories.

### Published correction targets

Queries: `Chai Mumford non-flat Pic`, `mumford_ex_v2.pdf Theorem2.4`; author URLs were tried directly. Both Chai author PDF paths returned403. The search engine indexed a first-page excerpt, which is insufficient for the exact theorem audit. Opened Chai--Oort2017 publisher version through the Utrecht repository: section3.9(iv), printedp35, unequivocally asserts nonflatness for the universal first-order deformation. Opened Partsch2013 publisher PDF, Proposition6.6 pp102--103, Theorem6.7p104, Proposition6.9p106. The proof's final trace inference onp103 was read. The precise elementary counterexamples to the tangent and etale-source inferences, and the remaining gate before any geometric refutation is certified, are in CORRECTIONS_FOR_AUTHORS.md. No message has been sent to an author.


### Polarization attribution refined after Laga comparison

Opened Jef Laga, *Polarizations, torsors and theta groups*, arXiv2510.24678v2, dated7November2025,43pages, https://arxiv.org/pdf/2510.24678. Read §3.6p19, §4.4pp26–27 and §§5.3–5.4pp30–33. The survey onp27 explicitly lists d2 even as a known sufficient condition from Poonen–Rains Proposition3.12. Reopened the published Poonen–Rains Proposition3.12(f), statementp1314 and proofp1315: its quotient of order1or4 and canonical quadratic form are exactly the positive construction of our Theorem1.1. That construction is known, and its formula works under arbitrary base change when2is invertible. The paper now expressly credits this source rather than attributing only the torsor correspondence. The converse is the elementary integral-transvection obstruction proved in the paper. The complete formulation is presented as a synthesis with no priority claim. Laga's main question allows moving to an A-torsor, so its theorems are not interchangeable with a universal Picard section on A itself. Its paramodular discussion verifies the period-stack conventions used in the converse.

Laga §2.3p7 also confirms that the relative Picard presheaf needs no further sheafification when the smooth proper family has a section. For an abelian scheme the zero section rigidifies representatives. The paper's former caution about a further line-bundle descent obstruction was therefore misleading in this setting and has been replaced by the precise rigidified interpretation; the main theorem is unchanged.

### Roots of a basis: an explicit earlier use

Further queries: `ample line bundle very ample finite cover`, `cyclic covering trick very ample`, `globally generated very ample taking roots`, and `very ample roots Bhatt splinters`. Opened the published Cambridge PDF of Bhatt, *Derived splinters in positive characteristic*, Compositio148(2012),1757–1786, DOI10.1112/S0010437X12000309. In the proof of Proposition7.2, printedp1771/PDFpage16, he takes roots of every element of a basis of H0(L^m) in a finite flat cover to obtain global generation. That construction is explicitly credited in our opening. Bhatt's passage does not assert that the pullback is very ample or give the surface with invariants562,1,565; our affine-chart argument retains original sections to distinguish common scalar changes of the roots. Exact prior overlap for that stronger conclusion remains unsettled. The cyclic-cover step itself is not presented as new.

The official TIFR URL https://www.math.tifr.res.in/~publ/studies/CP-Ramanujam-A-Tribute.pdf was located. Direct downloads over both schemes and the alternate hostname returned503; the search tool opened a partial indexed retypesetting whose visible content ends with Ramanujam's Tate appendix and only lists Raynaud in the contents. This is not counted as reading Raynaud's1978 article. The original construction remains credited and independently proved here; the original full-text retrieval gap is retained.

## Murre corollary number: direct visual verification, 23 November 2026

The official Numdam PDF, printed page247/PDF page6, has the heading **COROLLARY2**. Its statement is representability by a separated etale locally finite type prescheme under the listed sheaf/finitary/effectivity/valuative conditions and unique nilpotent lifting. The owner visually inspected the full page at02:39UTC. The statement-only chart brief previously said Corollary3; it has been corrected to2. The paper already cites Corollary2 correctly. Worker5 independently caught the numbering error; no mathematical statement changes.

## Further principal-polarization and representability searches, 23 November2026

Queries `universal polarization type Picard group odd elementary divisors`, `Fringuelli Pirisi universal abelian variety`, `Murre locally quasi-finite criterion`, and `Murre1995 representability` led to two primary comparisons. Opened Fringuelli–Pirisi, arXiv1603.09190v3, TheoremC p3:over C, for g>=2, the relative Picard group of the universal principally polarized abelian variety with no level is generated by the canonical twice-polarization class. This contains the principal-type negative case of our criterion. TheoremA p2 treats principal leveln for g>=4 and distinguishes n even/odd; it concerns the level, not arbitrary elementary divisors. Published metadata was verified on the authors' institutional records:Michigan Math.J.68(3)(2019),651–671, DOI10.1307/mmj/1564106669. The primary author version was downloaded and read; the institutional PDF is the same17-page arXiv text, so the paper cites its exact author-versionp3 locator rather than inventing a journal-page offset. The positive arbitrary-type case is already Poonen–Rains3.12(f); the proof here assembles those known components with the elementary general-type obstruction.

Downloaded JarodAlper's primary Stacks and Moduli draft, dated5January2026, from https://sites.math.washington.edu/~jarod/moduli.pdf. Read Theorem3.1.14 and Remark3.1.15, printedp76/PDF84, and the bibliography entry Mur95, printedp662/PDF670. Mur95 is the1995 collected reprint of the same1965 Bourbaki exposé, not a later publication of the locally-quasi-finite criterion. The local-quasi-finite theorem there is effective fppf descent. AppendixC.7, printedpp624ff, states Artin's algebraicity criteria, not the eight-axiom pro-modular criterion on arbitrary locally noetherian bases. This search therefore closes a misleading possible1995 lead but does not settle the exact analogue's later-publication status. A2020 MathOverflow request about the announced analogue was used only as a source-search lead, not as evidence that no publication exists.

Additional queries `very ample taking roots line bundle`, `very ample simultaneous roots Kodaira`, and `Raynaud very ample surface` returned the known Lauritzen–Rao work and an OpenReferee preprint on a conditional abelianity theorem for complex special fourfold root orbifolds. Its retrieved original statement and cover construction concern a different dimension, characteristic and fundamental-group problem; they do not establish this Kodaira surface result. No unrelated AI claim is added to the paper. The original Raynaud retrieval is being pursued through another official TIFR filename route.

The modern completion-descent sources were reopened:Stacks0AP9 (separated locally quasi-finite implies ind-quasi-affine) and0APK (effective fpqc descent for ind-quasi-affine morphisms). Stacks02W8 is only fppf and is explicitly not used alone for completion descent. The older Murre Appendix case(d), pp259–260, already used in the paper is valid here.


## Raynaud original article: retrieval and complete reading closed, 23 November 2026

The TIFR site migrated to a new official Documents/Publications/Studies directory. Worker4 located its live Studies page and downloaded https://mathweb.tifr.res.in/Documents/Publications/Studies/CP-Ramanujam-A-Tribute.pdf . The complete book has431pages. Raynaud’s article occupies physical PDF pages329–335, retypeset pages319–325, with original page markers273–278. The owner read all seven pages as extracted text and as individually rendered page images; this supersedes the earlier failed-retrieval entries.

The exact construction matches the credited starting surface: §1, originalpp274–275/retypeset320–321, gives the Tango criterion and the Artin–Schreier equation X^p−X=T^(hp−1); §2, originalpp275–277/retypeset321–323, gives the ruled surface, disjoint horizontal divisors, and the triple cover in characteristic2 with M=O_P(−1)⊗N². Remark3, originalp278/retypesetp324, specifically chooses h=8 and N=O_C(2∞), matching the curve y²+y=x^15 used here. It then asks whether one can have a globally generated or very ample line bundle in the counterexample. That explicit question is now cited in the paper’s opening. Our Q=O_S(2T)⊗f*N is the globally generated variant proved directly; the simultaneous ninth-root cover supplies the stated very ample example. Reading the original question does not establish a novelty claim: whether the precise very-ample surface improvement was subsequently published remains an open literature-classification gate.

The retypesetting contains visible typographic slips in some formulas (for instance tensor-power symbols and a numerator in the odd-characteristic display); no proof is imported from those slips. Our characteristic2 construction, transition functions and direct images are independently written and checked.


## Final comparison additions, 23 November2026

See FINAL_CITATION_AUDIT.md for exact scope and locators. SGA2XIII Conjecture3.1 was checked directly at retypesetp134 (physical142). Lauritzen, Embeddings of homogeneous spaces in prime characteristics, arXiv alg-geom/9502016, pp1–2/section4.2, is an earlier higher-dimensional very-ample comparison. Bernasconi–Valloni arXiv2605.28278v1, Propositions3.13–3.14 pp16–17, gives global generation and point separation for the p-th power of the nonvanishing line bundle, with a purely inseparable fibre restriction; this is not the exact very-ample surface theorem here. Neither comparison closes the priority question. Retrieval hashes are in FETCHED_SOURCES.tsv.


## Record: workbench/records/papers_2_3/FRESH_P_H_DATED_LITERATURE_SEARCH.md

# Dated literature search for the polynomial-base H counterexample

Date of search and inspection: 2026-11-23 UTC. Checker: /root/p_fresh. This search was performed after the independent P proof had been frozen and after the H counterexample had been derived during the base-convention audit. It is a bounded related-literature check, not a proof of novelty or priority.

## 1. Exact result being compared

For \(S=\operatorname{Spec}\mathbf F_p[t]\), the functor
\[
 H(R)=\{x\in R:x^p=0,\ x\in tRx\}
\]
satisfies conditions 1–6, actual fixed-base propagation \(7_S\), and finite-type relative generic spreading 8, but the actual modularity locus of \((S,0)\) is the nonopen singleton \(\{(t)\}\). It fails relative propagation after base change to \(\mathbf F_p[[t]]\).

The formula is not newly invented in this search. The supplied research source already has it over the complete base:

source/ours/RESEARCH_SA17/RESEARCH_SA17/sections/A_finish_L2.tex, theorem A:L2-counterexample and equation (A.2.3).

Source SHA-256: 9f457cb0da7f8eea7cd00db0d7d708f693c9603de2f779229f4a129fb672bdd8.

The polynomial-base verification of \(7_S\), and its resulting refutation of fixed-base openness, are the additional assertions compared here. The exact fixed/relative distinction is essential to this search target.

## 2. Queries and coverage

The search began after the observed clock time 05:35:57 UTC. The first group below preceded the 05:41:36 UTC primary-PDF retrieval batch. Later retained calls completed at 05:55:12 and 05:58:54 UTC. Source byte receipts were then saved. No precise per-query time is invented for calls whose timestamp was not retained.

The routine search engine and a second, stronger-coverage search engine were both used. Exact query strings were:

### Initial formula and terminology queries

1. "modularity locus" counterexample henselian nilpotent
2. "Grothendieck" "modularity" "representability" counterexample functor
3. "x=tax" "functor"
4. "henselization" "alpha_p" "representability"
5. "modularity locus" Grothendieck functor
6. "henselized" "nilpotents"
7. "Grothendieck" "131" "representability"
8. "x=tax" nilpotent

### Domain and related-theorem queries

9. site:arxiv.org "modularity" "representability" "functor" -"modular forms" -elliptic -ribbon -operad -Fermat
10. site:hexagonmath.org "representability" "henselian"
11. site:stacks.math.columbia.edu "counterexample" "representability" "functor"
12. site:eccc.weizmann.ac.il "Grothendieck" "representability"
13. "openness" "versality" "counterexample" "functor" — restricted to arXiv, mathematical author/institution sites, Oxford journals, and Springer.
14. "modularity locus" OR "lieu de modularité" OR "lieu modulaire" — restricted to arXiv, NUMDAM, Hexagon, and Stacks.
15. "nilpotent" "representability" "counterexample" "functor" — restricted to arXiv, NUMDAM, Stacks, and Springer.
16. "Grothendieck" "modularity" "henselian" — restricted to Hexagon and ECCC.
17. "henselian" "nilpotent" "functors" "counterexample" representability
18. "nilpotent" "x = t" "functor"
19. "Artin" "algebraicity" "counterexample" "openness of versality"
20. "Grothendieck" "modulaire" "représentabilité" "7"
21. Hall Rydh Artin criteria algebraicity revisited arxiv
22. Murre Representation of unramified functors applications numdam 221
23. site:hexagonmath.org "modularity locus"
24. site:eccc.weizmann.ac.il "henselian"

The last two stronger-engine queries, with a 365-day recency filter, were:

25. "henselized nilpotents" OR "henselised nilpotents"
26. "modularity locus" "functor" -elliptic -Galois -Hida

The keyword 221 in query 22 was an exploratory query term, not an adopted bibliographic identification. The directly verified Murre source is exposé 294.

The returned material was largely unrelated uses of “modularity,” general representability references, or broad listings. The screened results and the directly inspected primary texts below did not identify an exact prior occurrence of the polynomial-base H conclusion. Hexagon domain searches returned broad listings and unrelated modularity topics; no matching primary paper was identified. The ECCC domain screens did not identify an applicable source, and no ECCC result is used as mathematical evidence. Secondary summaries and newly generated expository pages returned by search were not used to support the proof.

## 3. Primary sources directly inspected and scope comparison

### Murre, exposé 294

J. P. Murre, Representation of unramified functors. Applications, Séminaire Bourbaki, exposé 294, May 1965, published in volume 9, pp.243–261.

Primary PDF: https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf

Directly inspected: Theorem 1 on p.246; Corollary 2 and the following locally quasi-finite announcement on p.247; the descent appendix on pp.259–260. The published theorem has an unramified hypothesis. H has a nontrivial \(\alpha_p\) functor on the generic open, so this hypothesis is absent in the new example. The announcement does not specify the eight modified axioms or the fixed/relative propagation convention used here. The statement that the published conditions are stable under base change concerns that source's own unramified criterion; it does not identify the two versions of the later archival condition 7.

### Hall, openness via coherent functors

Jack Hall, Openness of versality via coherent functors, arXiv:1206.4182v2, 8 April 2013.

Primary PDF: https://arxiv.org/pdf/1206.4182

Directly inspected: Theorem A and the introduction; Theorem 4.5 on PDF p.14; Example 8.4 on PDF p.23. Theorem 4.5 uses an Aff-homogeneous limit-preserving groupoid and finite generation of the relevant Exal functor to obtain openness of formal smoothness from formal versality. Those are explicit additional structural hypotheses, not the fixed-base eight conditions tested here. Example 8.4 concerns a nonflat obstruction-theory example. It is not the polynomial-base supported-nilpotent functor.

### Hall–Rydh, algebraicity criteria

Jack Hall and David Rydh, Artin's criteria for algebraicity revisited, Algebra & Number Theory 13 (2019), 749–796.

Published primary PDF: https://msp.org/ant/2019/13-4/ant-v13-n4-p01-p.pdf

Directly inspected: published introduction p.749 and Main Theorem p.750. The criterion specifies an excellent base, homogeneity, effectivity, and conditions on automorphisms, deformations, and obstructions. It is not a theorem that the fixed-base hypotheses 1–8 in the present task imply openness. The comparison therefore identifies related methodology without claiming that H contradicts this criterion.

The arXiv PDF https://arxiv.org/pdf/1306.4599 was also inspected. It is v1, 19 June 2013, 34 pages, with an earlier main-theorem formulation. The published 52-page PDF including cover matter was checked separately; the two were not conflated. The publisher XHTML route returned an unsupported-content-type error in the search tool, so the official published PDF was used successfully.

### Stacks Project

The following exact tags were opened and their hypotheses read:

* https://stacks.math.columbia.edu/tag/00IN — Artin–Rees for finite modules over a noetherian ring.
* https://stacks.math.columbia.edu/tag/00IP — Krull intersection; the H proof spells out the extension to an ideal in the Jacobson radical.
* https://stacks.math.columbia.edu/tag/09XI — characterization of henselian pairs by idempotents in finite/integral algebras.
* https://stacks.math.columbia.edu/tag/0AGU — flatness of pair henselization and preservation of quotients by powers of the ideal.

These are proof inputs and hypothesis checks. None is presented as a published statement of the new H counterexample.

### Grothendieck's primary manuscript

https://grothendieck.umontpellier.fr/131.pdf was inspected at sheets13,34,36 and adjacent/continuation sheets14,38,40. The exact PDF hash and the observations about the base are in FRESH_P_BASE_CONVENTIONS_AND_RELATIVE7.md. The visible notation does not justify silently identifying fixed-base \(7_S\) with \(7_{\mathrm{rel}}\). This is a cautious source-reading conclusion, not a claim about an unstated intention.

## 4. Exact byte receipts and retrieval limits

FRESH_P_H_LITERATURE_SOURCE_RECEIPTS.json gives the requested/resolved URLs, UTC times, MIME types, byte counts, SHA-256 hashes, local paths, and exact inspected locators for eight newly downloaded primary sources. All eight were saved successfully. The PDFs and HTML source bytes are held under tmp/papers_2_3/fresh_p_h_literature/ and are not copied into the paper's deliverable text.

The two retained late search-service responses, including the failed publisher XHTML opening and the successful official-PDF fallback, are preserved at tmp/papers_2_3/fresh_p_h_literature/LATE_SEARCH_RESPONSES.json. Earlier full search-service results remained in the conversation transcript, but the temporary session-store copies were no longer available when the final log was assembled. Accordingly no complete raw-response byte archive is claimed for the earlier queries; their exact query strings and the directly inspected source URLs are recorded above.

The separate FRESH_P_PRIMARY_SOURCE_RECEIPTS.json preserves sixteen successful post-freeze byte downloads for sources used in the frozen P proof's failed or partial approaches. Those later downloads are not claimed to reproduce the bytes originally served during the blind proof attempt.

## 5. Bounded conclusion

Within the queries and primary-source sections actually inspected, no exact earlier polynomial-base H example satisfying \(7_S\) and having \(M_S(S,0)=\{(t)\}\) was identified. The formula itself is explicitly inherited from the supplied adic example. The valid research conclusion is the proved distinction between fixed-base and relative propagation, with related-literature comparison and dated search receipts. Absolute novelty, completeness of the search, and bibliographic priority remain unclaimed.


## Record: workbench/records/papers_2_3/E4_LITERATURE_SEARCH.md

# E4 transfer and full-Picard literature search

Date: 2026-11-23 UTC. Agent: /root/p_fresh, inherited GPT-6 Astra.
Primary-source acquisition and reading began about06:03. The targeted transfer/full-Picard search below ran about06:29–06:40. These are approximate session ranges, not invented exact per-query timestamps.

## Precise target and conclusion

Target T: if h:A→B is any homomorphism of abelian schemes over an arbitrary scheme S and T is an A-torsor whose total space is a scheme, is h_*T a scheme?

Target P: is the full fppf Picard functor of such a scheme torsor T a scheme, without projectivity or a normal/noetherian base assumption?

The bounded search located an explicit earlier statement of P for a connected locally noetherian base in Achter–Casalaina-Martin, author manuscript dated18December2024, §1.7.2 first paragraph, p13. Thus P is not presented as historically new. A full proof for the arbitrary-base form, keeping the varying NS parameter and nontrivial component torsors, is supplied in E4_RESEARCH_CONTINUATION.md and E4_TORSOR_SECTION.tex.

No exact statement of T with arbitrary h and arbitrary S was identified in this search. Its ingredients are classical Raynaud, BLR and EGA results. This negative search result is bounded evidence, not a priority or novelty claim. The meaningful change to the inherited research state is that T excludes its expressly unresolved degenerate-homomorphism construction.

## Exact targeted queries

The following35 queries were actually issued. Each numbered group was a single search call; results were inspected, and the relevant primary leads were opened or fetched. Some results were duplicates. Search engines are distinguished to make the receipt reproducible.

### Group1 — system1

1. "torsor" "abelian schemes" "pushout" scheme representable
2. "torsors" "abelian schemes" "representable" "homomorphism"
3. "Torsors under abelian schemes via Picard schemes"

### Group2 — system2

4. "torseurs" "schémas abéliens" "représentable" morphisme Raynaud
5. "torsors" "abelian schemes" "schemes" "pushout"
6. "torsor" "abelian scheme" "quotient" "scheme" Raynaud XIII
7. "Picard" "abelian torsor" "representable" scheme

### Group3 — system1

8. "Raynaud" "XIII" "1.1" torsor Picard scheme
9. "Complete moduli in the presence" Olsson pdf
10. "schémas abéliens" "changement de groupe" torseurs
11. "torsor" "abelian" "schematic" pushout

The author guess in query9 was wrong: the relevant *Complete moduli* paper is Alexeev's. Its primary arXiv and published version were then identified and read; the mistaken query is retained.

### Group4 — system2

12. "Raynaud" "Faisceaux amples" "torseurs" "représentables"
13. "abelian torsors" "schematic"
14. "abelian scheme" "Picard functor" "scheme" "torsor" representability
15. "torsors under abelian schemes" Lodh arxiv

### Group5 — system1

16. Raynaud "Faisceaux amples" pdf XIII
17. "schémas abéliens" "changement du groupe"
18. "abelian schemes" "representable torsors"
19. "abelian torsors" "Picard" "scheme" schematicity

### Group6 — system2

20. "Torseurs sous un schéma abélien" "1.2"
21. "schéma abélien" "torseur" "morphisme" "représentable" Raynaud XIII 2
22. "pushout" "torsor" "schematic" abelian Raynaud
23. "schematic" "abelian torsor" Picard

### Group7 — system1

24. "Faisceaux amples" filetype:pdf Raynaud -site:researchgate.net -site:academia.edu -site:scribd.com
25. "schematic" "torsors" "abelian" quotient morphism -site:kokunoyumeto.github.io -site:openmaths.org
26. "Picard scheme" "abelian torsor" -site:researchgate.net -site:academia.edu
27. "scheme torsor" "abelian" pushout

### Group8 — system1

28. Alexeev "Complete moduli" arxiv
29. "Torsors under abelian schemes via Picard schemes" pdf Lodh
30. "Picard scheme" "torsors" "Raynaud" "1.1" "schemes"
31. "torsor" "push-out" "abelian" "scheme" representable

### Group9 — system1

32. "abelian torsors" "schematic" site:arxiv.org
33. "Picard" "torsor" "schematicity" site:hexagonmath.org
34. "abelian torsor" "scheme" site:eccc.weizmann.ac.il
35. "schematicity" "abelian" torsor Raynaud

The domain checks did not locate an exact additional statement. ECCC is not a natural subject archive for this algebraic-geometric question; its empty relevance adds no meaningful completeness guarantee.

## Primary sources actually read and their exact role

| Source | Verified locator and result | Comparison with T/P |
| --- | --- | --- |
| Raynaud, *Un critère d'effectivité de descente*,1967/68 | Corollary3.8 and application p5-15; Theorem4.2 and proof pp5-16–5-18 | Exact AF and two-cover effective-descent inputs. Does not state T in the pages read. |
| Bosch–Lütkebohmert–Raynaud, *Néron Models* | §6.6 Theorem2(c),(d), pp164–166, statement and proof | AF from a saturated quasi-affine open and ampleness over a normal base. These supply the missing simultaneous-affine step. |
| EGA, attached French LaTeX | II6.6.1–6.6.4; IV3 8.8.2,8.9.1,8.10.5,11.3.8,13.1.3–4 | Norm ampleness, approximation, fibrewise regular-sequence flatness, and fibre dimension. No descent of projectivity through an arbitrary finite nonflat cover is asserted. |
| Poonen–Rains2011 | §§3.1–3.2, publishedpp1311–1312, read in full | Exact Picard/dual/self-dual-Hom sequence and symmetric B[2]-torsor. P retains the component torsor instead of assuming it trivial. |
| Laurent–Schroer, arXiv2101.10829 | Corollary4.6 pp14–15 with proof; relevant §§2,4 | Pic-tau of para-abelian families is an abelian scheme; general neutral-subfunctor caveats. Does not make general normal-family Pic0 flat or smooth. |
| Alexeev, *Complete moduli in the presence of semiabelian group action* | arXivmath/9905103v4; publishedpp663–664, especially Theorem3.0.3 p664 | Classical contracted-product Picard formula and canonical Pic0/NS identifications for an abelian torsor. This is explicitly credited. |
| Achter–Casalaina-Martin, *Putting the P back in Prym* | Author PDF dated18December2024; p3 standing convention; §1.7.2 first paragraph p13 | Explicit prior statement of full Picard schematicity over a connected locally noetherian base. No historical novelty claimed for P. A separate adjacent assertion is considered only in the external-corrections dossier. |
| Bertolin, arXiv1007.3875 | Theorem1.2.6 pp8–9; Lemma1.3.3 pp11–12 and surrounding remarks | Results for extensions involving abelian schemes; not an exact transfer statement for arbitrary scheme torsors in the portions read. |
| Brochard, arXiv0711.4545 | Theorem4.3.5 pp23–24 with proof; preceding §4.2 results | A conditional properness theorem assuming represented/open/separated/finite-type Pic0; it does not remove the general schematicity or nonflatness gates. |
| Official Stacks03XX and0DMD | Full theorem/proof of03XX; relevant Picard section of0DMD | Separated locally quasi-finite spaces are schemes; Picard separatedness under geometrically integral fibres. The zero-dimensional clarification is a standard consequence, not claimed research movement. |

Primary URLs and exact byte counts/hashes are in E4_PRIMARY_SOURCE_RECEIPTS.json. External PDFs remain only in tmp/e4_continuation. The record distinguishes downloaded bytes, attached-source bytes, and web-only observations.

## Primary leads that did not yield a full-text verification

- Rémi Lodh, *Torsors under abelian schemes via Picard schemes*, RSMUP147(2022),79–89: https://ems.press/journals/rsmup/articles/6577399 . The primary abstract assumes a principally polarized abelian scheme and a projective torsor over a noetherian base. The PDF link redirected to a subscription page. Only that explicit scope is recorded; no proof or stronger conclusion is attributed to the unseen article.
- Raynaud, LNM119, chapterXIII pp192–203: publisher chapter https://link.springer.com/chapter/10.1007/BFb0059519 . The requested PDF endpoint returned non-PDF content. Publisher metadata and the chapter locator were read, but no claim to have read the full chapter is made. This is a remaining limitation on any historical survey of T.
- Faltings–Chai, chapter1: the requested publisher PDF returned HTML. The abelian-algebraic-space consequence is verified in the primary Laurent–Schroer proof actually read; this run does not claim to have inspected the original book proof.
- Brochard's overview and published author PDF: direct attempts returned503, and repeated web opening of the overview returned502. The arXiv primary paper was successfully fetched and its relevant theorem/proof read instead.
- The Bordeaux abelian-varieties notes lead failed503. It was not used as a theorem source.

Search snippets, third-party mirrors, ResearchGate summaries, and AI-generated mathematics sites were not accepted as primary proof evidence. In particular, mirrored “Stacks” or “Quotients and torsors” pages encountered during the searches were rejected; the official Stacks domain was used.

## Scope and novelty verdict

The exact arbitrary-base transfer theorem T is proved in the continuation record and has passed root's targeted reconstruction; a genuinely statement-only re-proof remains a separate planned check. The full Picard corollary P is a detailed arbitrary-base proof of a conclusion already stated in the located literature. Both reduce the inherited unresolved construction list. Neither settles full Picard schematicity for all proper flat geometrically normal/integral families, and neither receives a historical-priority claim from this bounded search.


## Record: workbench/records/papers_2_3/E4_RESIDUAL_LITERATURE_SEARCH.md

# Dated literature and source audit for the residual E4 interval

Author: `/root/p_fresh`; date 2026-11-23; search/read interval approximately
07:00–07:45 UTC. This receipt is metadata and original analysis only.
All newly retrieved outside-source bytes and their extractions are under
`tmp/e4_residual/`. No manuscript file was edited.

## Scope and bounded result

The question investigated was whether a projective scheme modification
of a nonschematic torsor under an abelian surface can remain proper and
flat with geometrically integral fibres over an arbitrary scheme base.
The full independent proof M2/M2' was frozen at 07:42:54 UTC before
parent comparison. The exact theorem was not located in the bounded
searches below. That statement is limited to these searches and is not
an assertion of novelty or a comprehensive literature review.

The rank-one sheaf mechanism belongs to established deformation/sheaf
theory. A secondary search lead points specifically to Kollár 1990,
Lemma 6.13. The primary article could not be read because the publisher
PDF endpoints returned an Incapsula unsuccessful-request HTML page.
Those actual bytes and URLs are retained. The article is not cited as
a verified proof in M2; the record supplies a full independent argument
using perfection, relative depth, and the local criterion for flatness.

## Exact searches for the new construction

The following queries were issued during this interval, through the
available two web-search systems; search snippets were used only as
leads:

* `"birational" "abelian" "torsor" "scheme" "modification"`
* `"algebraic space" "surface" "flat" "modification" "scheme"`
* `"abelian" "torsor" "blowup" "flat" "scheme"`
* `"abelian surface" "torsor" "modification"`
* `"non-schematic" "torsor" "modification"`
* `"Picard" "geometrically integral" "Chow" schematic`

Results included work on Néron blowups of affine-group torsors over
traits, finite torsors, and the already located Rémi Lodh paper on
projective principally polarized torsors. These are different scopes.
No full unread article is being used as a theorem. Lodh's publisher
abstract remains only the earlier scope lead; no claim of a full PDF
read is made.

## Projective-bundle and general Picard leads

Earlier queries in the same interval included:

* `"algebraic space" "projective bundle" "scheme" representable`
* `"Brauer-Severi" "algebraic space" "scheme" nonschematic`
* `"algebraic space" "invertible" "Zariski locally" trivial`
* `"proper homogeneous" "Picard scheme" relative`
* `Schroer "Hilbert's Theorem 90" algebraic spaces pdf`
* `"projective bundle" "nonschematic"`
* `"Brauer-Severi" "non-schematic"`
* `"quotients of schemes by connected groups" scheme algebraic space`
* `"Picard functor" "geometrically normal" "scheme"`
* `"proper" "group algebraic space" "scheme" flat`
* `"AF-scheme" "normal" "quasi-projective"`
* `"projective bundle" "algebraic space" "schematic"`

The primary papers actually opened/downloaded were Schröer's Hilbert 90
paper and Fernández Herrero–Weißmann–Zhang arXiv:2411.07169v1. The former
rules out the tempting but invalid assumption that a vector bundle on
an algebraic space is Zariski locally trivial. The latter gives
schematic-point criteria in a finite-type-over-an-algebraically-closed-
field setting. Neither read scope supplied the desired arbitrary-base
Picard counterexample or the exact modification theorem.

Secondary leads to Kollár's nonquasiprojective moduli spaces, Totaro's
resolution property, and Gross's work were not converted into verified
primary theorems in this interval. They are not mathematical dependencies.

## The Kollár lead and exact unsuccessful retrievals

Queries:

* `"rank one" "flat" "determinant" "smooth surface" family`
* `Kollar 1990 "6.13" "torsion free"`
* `"Projectivity of complete moduli" "6.13"`
* `Kollar Projectivity complete moduli 1990 pdf`
* `Kollár 6.13 Lemma double dual locally free flat rank one sheaf smooth`
* `"Projectivity of complete moduli" "121444"`
* `"Projectivity of complete moduli" pdf Kollar 6.13`
* `"Kollár" "6.13" "locally free" "1990"`

The article is János Kollár, “Projectivity of complete moduli”, Journal
of Differential Geometry 32(1) (1990), 235–268, DOI
10.4310/jdg/1214445046. Princeton's bibliographic record confirms that
identity; this is bibliographic verification, not verification of the
lemma. The secondary paper titled “Picard Groups of Spectral Varieties
and Moduli of Higgs Sheaves” attributes a flat rank-one double-dual lemma
to §6.13. No statement from that snippet is relied upon.

Actual unsuccessful full-text fetches at 07:32:08 UTC:

| URL | Saved bytes | SHA256 |
|---|---:|---|
| https://projecteuclid.org/download/pdf_1/euclid.jdg/1214445046 | 1161 bytes of HTML | `887739e34da749283fa19f58ab615143ab58300a75da7218966862081551740e` |
| https://projecteuclid.org/journals/journal-of-differential-geometry/volume-32/issue-1/Projectivity-of-complete-moduli/10.4310/jdg/1214445046.pdf | 1153 bytes of HTML | `9136b9118a0654d2eee69796c4d09db134e8fea2f890d007da49fe64ae1bc23d` |

The local filenames end `.pdf.html`, accurately marking the response
type. An initial Python downloader failed before any network request
because `requests` was unavailable; it was replaced by standard-library
`urllib.request`. That failed import was not a source fetch.

## Primary technical checks actually read

The attached French EGA source was checked directly for IV_3 11.3.8
(lifting fibre regular sequences), 11.3.10 (fibre criterion for flatness),
8.10.5 and 8.10.5.2 (descent of morphism properties and relative
ampleness), and 9.7.7 (constructibility of geometric fibre properties).
The last theorem and its full proof were reread after the proof freeze
as a citation-scope confirmation; no mathematical correction resulted.
The file hashes and exact local locators are in the JSON citation index.

Official Stacks pages read for their statement and displayed proof:

* 00MP: noetherian fibre criterion for flatness.
* 00MK: local criterion using vanishing of Tor_1 with the residue field.
* 0E9I: extension of a coherent sheaf across a depth-at-least-two
  complement, without an integrality or normality hypothesis.
* 056K: associated-point injection facts, especially Lemmas31.5.6,
  31.5.10 and31.5.11.
* 05WX: the nonnoetherian finite-presentation fibre criterion for
  algebraic spaces, Theorem76.23.3 and its reduction to schemes.
* 039A: the corresponding scheme statement, Theorem37.16.2.
* 05XD: the universal open locus where a map of proper flat finitely
  presented families is an isomorphism.
* 07SK: descent of finitely presented algebraic spaces and their maps.
* 08K0 and08K1: descent of flatness and properness for spaces.
* 084V: surrounding descent lemmas for smoothness, surjectivity,
  monomorphisms, closed immersions and isomorphisms.
* 05FA: geometric-fibre-property approximation and finite-stage
  elimination of constructible bad loci, with the affine scope stated.
* 09MT: descent of ampleness along limits.

Additional diagnostic pages, not needed as final dependencies: 0AY6
(normal reflexive extension for the earlier route), 0E0C (geometrically
reduced fibres in proper flat families), 0FJW (determinants, whose fully
written construction has Tor amplitude[-1,0]), and090U
(Auslander–Buchsbaum). The final proof includes its own gluing of local
determinant lines across the depth-two complement, so does not silently
invoke the restricted construction for amplitude[-2,0]. Tag07SG was
opened while locating a limits section; it is only an equation and was
not used as a theorem.

The Raynaud1967 descent PDF and BLR §6.6 were already fully read in the
previous frozen E4 interval. The exact reused bytes, URLs and relevant
pages remain in `E4_PRIMARY_SOURCE_RECEIPTS.json`. In this interval the
application after Raynaud Corollary3.8, printed p5-15, was reread to
confirm that an abelian scheme over an affine base is AF even when
projectivity is not built into the definition. M2 uses that statement
and Theorem4.2, with an actual finite locally free splitting cover.

## Status boundaries

The main proof's author verdict is complete for M2/M2'. Parent comparison
and any fresh statement-only check are separate. General E4 remains
unsettled. The old abelian-torsor transfer result is a previously proved
subcase; it is not being counted again. The zero-dimensional-Picard
observation is not movement. No source correction or author contact is
initiated by this record.


## Record: workbench/records/abelian_torsor_fresh/m2_literature_input_audit_v1.md

# M2/M2′: targeted literature and exact-input audit

## Outcome

**The checked external inputs support the frozen proof, with citation refinements described below. I found a primary antecedent for the determinant/ideal-of-points construction. I did not locate an exact prior statement of M2 or M2′ in this bounded search. The latter is not evidence of novelty.**

This is a source and literature audit, not the separate statement-only proof check. In particular, the conclusion “no missing hypothesis found” below concerns the source applications actually audited. It does not replace the independent checker’s verdict on the complete mathematical argument.

The original proof of the rank-one defect lemma in the frozen record remains useful: it verifies the required generality over nonnormal and nonreduced Noetherian bases, and handles algebraic spaces by étale localization. Neither an unavailable Kollár paper nor a bibliographic attribution is needed as a theorem input.

## 1. Exposure and precise scope

I am the existing agent /root/abelian_torsor_fresh, using the inherited GPT-6 Astra model. This is a same-model targeted audit. I previously produced the frozen statement-only abelian-torsor proof and its reciprocal comparison. Those earlier files were preserved.

For this task I first read E4_MODIFICATION_STATEMENT_ONLY.md, then the entire frozen E4_MODIFICATION_PROOF.md and its freeze record. I subsequently read the available source-fetch receipt and the primary-source passages identified below. I did not read or contact the separate unexposed M2 checker. I did not read the newly drafted modifications.tex and made no paper edits. No author was contacted.

The audited inputs were:

| Input | SHA256 |
|---|---|
| E4_MODIFICATION_STATEMENT_ONLY.md | 3892345c7b769e9c8ce4f8e2fa6e025faec4215777617acac25e79ed29cebc59 |
| E4_MODIFICATION_PROOF.md | 342161e167194e1371c623cd91d43c8dc5618bc6ab1fb777b5e6d177dffceab8 |

M2 concerns a projective, geometrically fibrewise birational map from a proper flat finitely presented scheme with geometrically integral fibres to a torsor under an abelian scheme of relative dimension two. M2′ replaces fibrewise birationality by an isomorphism over a dense open of the total target. Both statements allow arbitrary bases and do not assume that the abelian scheme is projective. The output sought is schematicity of the target torsor.

All downloaded PDFs, HTML, and extracted source text are outside deliverable, under tmp. The accompanying receipt contains paths, hashes, exact queries, and reading locations, not source copies. Search results displayed incidental snippets from aggregators, ResearchGate, Academia.edu, MathOverflow, and newly indexed expository sites. I did not use such snippets as mathematical authority. They were leads only; all substantive literature findings below were checked in primary author papers or official sources.

## 2. Literature status

### 2.1 Verified antecedent for the rank-one construction

Xiaoyu Su and Bin Wang, *Picard Groups of Spectral Varieties and Moduli of Higgs Sheaves*, arXiv:2409.10296, contain the relevant determinant/ideal construction. In v1 (16 September 2024), see Lemmas 3.20–3.21 and Remark 3.22, pp.20–21. In v2 (17 November 2026), see Lemmas 3.22–3.23, Remark 3.24 and its following proof, pp.19–21. The latter explicitly obtains a flat quotient defining points and separates the possible lengths.

Their application is a smooth family of spectral surfaces associated with a smooth projective complex surface. The test sheaf is flat over the parameter scheme and has torsion-free rank-one geometric fibres, with a fixed Hilbert polynomial. This is a verified precedent for the construction, not a statement of M2/M2′. The work’s quoted general double-dual lemma is attributed to Kollár 1990, Lemma 6.13.

Primary files read:

- https://arxiv.org/pdf/2409.10296v1, SHA256 d25be20219013ae9220dc902879b0a2da3a7ac786b060672647d71b7bb2070bb.
- https://arxiv.org/pdf/2409.10296v2, SHA256 2a3e921980c985bacca6adf184cef2f25edb28bb5542931fdedbfba125f5a2d8.

Both are cached at /workspace/scratch/a69c78abe257/tmp/abelian_torsor_fresh_m2/ with names su_wang_2409_10296v1.pdf and su_wang_2409_10296v2.pdf. Their text extractions have the same stems.

### 2.2 Kollár 1990: attribution verified, original hypotheses not verified

The bibliographic record is János Kollár, *Projectivity of complete moduli*, Journal of Differential Geometry 32 (1990), 235–268, DOI 10.4310/jdg/1214445046. The original Lemma 6.13 was not successfully retrieved. Available Project Euclid download receipts contain HTML, not the paper; the full-article web endpoint returned an iframe without mathematical text. Further searches of the publisher, author and institutional sites found citations, not a readable primary copy.

A second primary paper supports the historical attribution: Pandharipande–Thomas, *Curve counting via stable pairs in the derived category*, author PDF https://people.math.ethz.ch/~rahul/pt.pdf, proof of Theorem 2.7, p.16, cites Kollár’s Lemma 6.13 for local freeness of a double dual. Bibliography item 31, p.46, identifies the 1990 paper. This verifies usage and attribution, not the exact hypotheses of the original lemma. No claim in this report treats that unread lemma as checked.

### 2.3 Related primary results that do not state M2

| Source and inspected location | What was verified and its relation to this task |
|---|---|
| Thomas Goller and Yinbang Lin, *Rank-one sheaves and stable pairs on surfaces*, arXiv:1907.05180, §2.1, pp.4–5 | The line-bundle/ideal-of-points decomposition is used as background for one torsion-free rank-one sheaf on a smooth connected projective complex surface. This reinforces the classical status of the single-fibre construction; it does not supply the arbitrary-base torsor theorem. |
| János Kollár, *Néron models, minimal models, and birational group actions*, arXiv:2502.13800, pp.4–6, especially Definition 16 and Theorem 17 | The result concerns a torsor over the fraction field of a DVR and a minimal model with terminal/numerical-canonical hypotheses; it extends an action of the identity component of a Néron model. These are different hypotheses and a different conclusion. |
| János Kollár, *Families of varieties of general type*, author draft dated 20 July 2017, pp.44–46, Lemma 1.70.2 and Example 1.70.5 | The example blows up points of the square of an elliptic curve and discusses isotrivial families and automorphism monodromy. It does not provide M2 or M2′. |
| Bhargav Bhatt, *Annihilating the cohomology of group schemes*, Algebra & Number Theory 6 (2012), 1561–1577, Theorem 1.2 and Example 6.1, pp.1561–1562,1574 | Proper covers kill abelian-scheme cohomology in the stated excellent Noetherian setting, whereas a Raynaud example is not killed by any finite cover. This is a caution against assuming a finite splitting cover for an arbitrary torsor. It does not conflict with constructing such a cover from a positive defect in M2. |

For the Bhatt example specifically, the torsor is Zariski locally trivial over a semilocal normal connected two-dimensional affine base. Thus it also warns that an argument cannot replace “Zariski locally on the base” by an unsupported global finite splitting assertion. The frozen M2 argument first works over an affine neighbourhood and obtains its finite flat cover from the sheaf defect; it makes no general assertion that all torsors admit such a cover.

### 2.4 Search limits

The receipt records 48 exact queries in twelve batches, using two search engines. They include the theorem’s general terms in English and French, fibrewise/fiberwise birational variants, abelian torsors and modifications, rank-one families and double duals, arXiv, publisher and author domains, and targeted Hexagon and ECCC checks. The initial Hexagon domain guess was incorrect; the mathematical repository was then identified as hexagonmath.org and queried directly by domain. The ECCC result was unrelated theoretical-computer-science material.

No matching M2/M2′ theorem was located in the primary passages examined. This is a finite search over accessible and indexed material. It is not an exhaustive bibliography, a priority determination, or a reason to label the theorem new. A defensible status sentence is: “The argument uses the classical determinant/ideal description of rank-one torsion-free families; we have not identified an exact published formulation of this schematicity consequence in the sources checked.”

## 3. Flatness, depth and determinant inputs

### 3.1 Perfection of the flat sheaf

In the Noetherian part of the proof, the local rings R and B are Noetherian, B is R-flat, and the fibre local ring is regular of dimension at most two. The finite presentations used to form successive syzygies therefore have R-flat kernels and remain exact over the residue field. The second fibre syzygy is free. The fibre-flatness criterion then makes the second syzygy B-flat and hence finite free over the local ring B. If that syzygy is zero, no nonzero-module criterion is needed.

The exact applicable source is Stacks Lemma 10.99.15, tag 00MP: it requires local maps of Noetherian local rings, a finite nonzero module over the last ring, base flatness and flatness over the fibre ring. Those hypotheses hold with the last two rings both B. This is also within attached EGA IV_3, 11.3.10. The finite nonzero hypothesis has not been suppressed.

The argument proves perfection locally; it does not require a global resolution property of the algebraic space. The frozen proof subsequently explains how the local determinant lines glue across the locus where the sheaf is a line bundle. Consequently it does not depend on extending a scheme-only determinant theorem to the étale topos without proof.

### 3.2 Lifting fibre regular sequences

Attached EGA IV_3, Theorem 11.3.8, pp.135–136, is directly applicable. Its assumptions are a locally finitely presented morphism, a finitely presented quasi-coherent module, and sections lying in the relevant maximal ideal. Its equivalence includes base flatness plus regularity on the fibre, yielding regularity upstairs and flatness of the successive quotients. The coherent modules in the Noetherian argument are finitely presented.

At a point outside the line-bundle locus, the regular surface fibre has local dimension two. Lifting a fibre regular sequence gives depth at least two for a line bundle on the total space. Torsion-freeness of the rank-one fibre sheaf gives a length-one regular sequence, hence depth at least one for that sheaf. These are depth assertions on the possibly nonnormal, possibly nonreduced total space. Normality of the total space is neither assumed nor supplied by this source.

### 3.3 Extension and the ideal quotient

Stacks Lemma 31.5.11, tag 0E9I, is precisely the extension result used: on a locally Noetherian scheme, a coherent module having depth at least two at every omitted point equals the pushforward of its restriction to the complementary open. Normality is not among its hypotheses. Its application to determinant lines and Hom lines is valid. The algebraic-space version needed here follows by the stated étale localization and unique gluing.

The inclusion of the original sheaf into that extension uses the separately established depth-at-least-one assertion. On a fibre, the resulting map is generically the prescribed identification; a torsion-free source on the integral smooth fibre then makes it injective. This is the relevant fibrewise injectivity, rather than an unsupported claim that taking double dual automatically commutes with arbitrary base change.

For the cokernel C, the exact source is Stacks Lemma 10.99.7, tag 00MK. It permits a finite module over a Noetherian local B, even though that module need not be finite over the base ring R. The vanishing Tor_1^R(k(s),C)=0 follows from fibrewise injectivity and flatness of the line bundle. Thus the cited local criterion applies and makes C R-flat. After twisting by the inverse line bundle, C defines a flat closed subscheme with zero-dimensional fibres. Properness of the target is then needed to make this subscheme finite; it is not part of the local rank-one lemma.

### 3.4 Higher direct images and base change

The proof uses relative Serre vanishing and generation for a sufficiently large power of a chosen relatively ample line bundle. These assertions can be checked over a finite affine étale cover of the quasi-compact Noetherian target and made uniform by increasing the exponent.

The subsequent flatness/base-change argument is a supplied argument, not a citation to an unstated cohomology theorem. On an affine étale chart, a finite affine cover of the separated source has affine intersections. Its bounded ordered Čech complex has base-flat terms. Once its positive cohomology vanishes, descending induction through the finite complex proves flatness of the cycles, and tensoring preserves the needed exact sequences. This proves both flatness of the zeroth cohomology and arbitrary base change. It avoids assuming the base-change conclusion in order to establish it.

No extra smoothness or normality of X is used in these source applications. Flatness over the base and geometric integrality of its fibres do separate jobs and should both remain in the statement.

## 4. From the defect to a scheme

Stacks Lemma 76.49.6, tag 05XD, supplies an open isomorphism locus on the base under the exact hypotheses used here: X is flat, locally finitely presented and universally closed over the base; the target is separated, closed and locally of finite type over it. Properness of X/S and Q/S supplies the closedness assumptions. If all geometric fibres are isomorphisms, the representing open is the whole base. The frozen proof also gives a direct finite-map argument.

On the positive-defect component, the defect has positive locally constant finite-flat rank. It is therefore a finite faithfully flat scheme over the affine base and carries a map to Q. That map splits the torsor after pullback. The split target is an abelian scheme over the affine defect scheme.

For this last step, the previously audited primary inputs are Raynaud’s application following Corollary 3.8, printed p.5-15, and Theorem 4.2, printed pp.5-16–5-18 of *Un critère d’effectivité de descente*. The applicable property of the split abelian scheme is that finite point sets lie in affine opens. Projectivity of the abelian scheme is not inserted into the definition or assumed in order to apply the descent criterion. The finite flat cover supplies the finite fibres required by the affine-orbit condition.

The rank-zero component uses the original schematic X via the isomorphism. On the positive component, finite scheme representability of the defect and the Raynaud criterion supply the scheme. These two components exhaust the base. The cited descent input does not require a condition on a homomorphism kernel, and no such homomorphism occurs in this M2 argument.

## 5. Arbitrary-base approximation and M2′

### 5.1 Fibrewise isomorphism near a fibre generic point

Attached EGA IV_3, Theorem 11.3.10, printed p.138, has an arbitrary-base finite-presentation alternative: the two structural morphisms are locally finitely presented and the module is finitely presented. Thus its use is not restricted to locally Noetherian bases.

For algebraic spaces, the exact modern statement is Stacks Theorem 76.23.3, tag 05X0, within the cited section 05WX. It requires X locally finitely presented over the bottom space, the module finitely presented, and Y locally of finite type over the bottom space. With the module O_X, flatness over S and fibrewise flatness at the generic point give the flatness required in the proof. The unramifiedness calculation and properness then produce an actual open where f is an isomorphism. Passing from that open to a finite quasi-compact subopen that still surjects onto the affine base is justified by smooth openness and quasi-compactness of the base.

### 5.2 Descent of spaces, diagrams and properties

Stacks Lemma 70.7.1, tag 07SK, applies to a directed inverse system of quasi-compact quasi-separated algebraic spaces with affine transition maps. It identifies finite-presentation objects and morphisms with their eventual models; finite diagram identities also descend. Here the bases are affine and the finite-presentation objects are quasi-compact and quasi-separated. Schematic objects are descended by ordinary scheme approximation, while this lemma handles Q and its finite diagrams.

For the retained properties, Stacks §70.6 gives separate statements with their finiteness assumptions. In particular, tag 08K0 (Lemma 70.6.12) requires the module and the morphism to be finitely presented for flatness descent; tag 08K1 (Lemma 70.6.13) requires the model morphism locally of finite type for properness descent. These assumptions are satisfied. Smoothness, étaleness, surjectivity and the finite diagram isomorphisms are covered by the other exact statements in that section.

### 5.3 Citation refinement: geometric fibre conditions

The frozen proof’s constructible-bad-locus argument is valid, but the citation should be made precise. Stacks §37.34.4, .6, .7 and .11 are stated for morphisms of affine schemes. Geometric connectedness or irreducibility of a proper fibre cannot simply be checked on an arbitrary affine cover of the source.

The direct attached reference is **EGA IV_3, Theorem 9.7.7, printed p.79**: for a morphism of finite presentation, each of the loci of geometrically irreducible, geometrically connected, geometrically reduced and geometrically integral fibres is locally constructible. This applies to the schematic models X_i and A_i used in the proof.

Equally precise Stacks references are tags 0579 (Lemma 37.26.5), 055B (Lemma 37.27.7), and 055I (Lemma 37.28.6). The first requires quasi-compactness and local finite presentation; the latter two require finite presentation and give constructibility of geometric component-count level sets. Tag 05F4 (Lemma 32.4.10) then removes the bad locus at a finite stage when the limit maps into the good locus. The frozen proof’s elementary finite-locally-closed-piece argument is the same applicable mechanism. This is a citation refinement, not a missing hypothesis or gap in that argument.

### 5.4 Citation refinement: the chosen relatively ample line bundle

Attached EGA IV_3, Lemma 8.10.5.2, printed p.41, is an exact relative-ampleness descent statement in the finite-presentation inverse-limit setting with quasi-compact starting base. It also treats relative very ampleness. The surrounding Theorem 8.10.5, pp.37–38, includes projectivity when the starting base is quasi-separated.

Stacks tag 09MT is an absolute-ampleness lemma, not by itself a statement about a relative algebraic-space morphism. It works after the proof’s stated reduction to affine étale charts and descent of the chosen line bundle. It is preferable to cite EGA 8.10.5.2 directly and explain the chart reduction for Q. No additional polarization of A is involved.

### 5.5 M2′ and virtual rank

The M2′ argument does not try to descend an arbitrary dense open. It descends the finite-presentation data, obtains the flat perfect direct image on a Noetherian model, and uses its locally constant virtual rank. Connected target fibres make this rank a function on the base; openness of the smooth surjection makes the function locally constant there. Density of the original isomorphism open forces rank one after pullback, so the base map factors through the rank-one open-and-closed component of the model.

The crucial fibre computation uses flatness of the direct image to preserve exactness of a finite free resolution under passage to the residue field. Hence its virtual rank is the actual generic rank on that fibre. Together with the proved base-change and generation statements, rank one supplies a globally generated trivial ample line bundle on the proper generic fibre of f. This forces that generic fibre to be a single rational point. The geometric-integrality hypothesis then gives fibrewise birationality on the model. These are internal deductions from the verified inputs, not an appeal to an external theorem asserting that total-space modifications are automatically fibrewise birational.

## 6. Recommended attribution and final status

The known rank-one construction should be acknowledged explicitly, using the verified primary family treatment and its attribution to Kollár. The paper can retain a full proof in the generality it needs. The historical reference must not imply that the unread original Kollár hypotheses have been checked.

The most useful citation edits are EGA IV_3 9.7.7 for the global geometric-fibre loci, 05F4 for eventual removal of a constructible bad locus, and EGA IV_3 8.10.5.2 for the particular relatively ample line bundle. The exact algebraic-space fibre-flatness theorem is 05X0. The proof already contains the mathematical reductions needed for these citations.

**Audit status:** external-input applications checked here pass, with the stated citation refinements. The determinant/ideal construction has verified precedent. An exact prior M2/M2′ schematicity theorem was not found in the bounded primary-source search. No claim of novelty, priority, or exhaustive coverage follows. The unavailable Kollár original is explicitly excluded from the proof’s dependency list.


## Record: workbench/records/paper_4/LITERATURE.md

# Literature searches and primary-source checks: Paper 4

Date: 2026-11-23. Search engine names identify retrieval only, not evidence of mathematical correctness. No negative search is treated as a proof of novelty. All downloaded external texts remain in scratch, outside the returned workbench.

## Search log

1. System 2 queries: `site:stacks.math.columbia.edu meromorphic functions nonzerodivisors stalk total quotient ring`; `EGA 19.3.12 formally smooth Artinian inverse limit erratum Deligne`; `algebraic field extension infinite regular sequence presentation Artinian flat lift`. Found Stacks sections on meromorphic functions and unrelated lifting material; no exact new-status conclusion.
2. System 1 queries: `site:stacks.math.columbia.edu "meromorphic functions" "not" "total"`; `"19.3.12" "smooth"`; `"Cohen" "nonlocal" "formally smooth"`; `"algebraic extension" "transfinite" "regular sequence"`. Found Stacks Tags 01X1 and 0EMG. These explicitly distinguish locally regular denominators from all nonzerodivisors of a stalk, and establish equality in the locally noetherian case. Other queries did not resolve the remaining three theorems' literature status.
3. Opened https://stacks.math.columbia.edu/tag/01X1 and https://stacks.math.columbia.edu/tag/0EMG. Followed the bibliography link to Kleiman. Initial direct bibliography open returned 403; search subsequently returned its exact publication metadata.
4. System 2 queries: `"misconceptions" "Kleiman" meromorphic`; `"EGA" "20.1.3" error`; `"19.3.12" "EGA" linear`; `"formally smooth" "pro-Artinian" lifting`. Located Kleiman, *Misconceptions about K_X*, Enseign. Math. (2) 25 (1979), 203–206, DOI 10.5169/seals-50379. Stacks' author blog describes the correction to EGA IV 20.1; this served as a route to the primary paper, not the final mathematical source.
5. System 1 queries: `Kleiman "Misconceptions" "203" pdf`; `"Kleiman" "seals-50379"`; `"EGA" "19.3.12" "proof" formally`; `"19.3.12" "linéaires"`. The first two found the E-Periodica journal archive; the latter two did not identify an earlier proof of the restored proposition.
6. Opened https://www.e-periodica.ch/cntmng?pid=ens-001%3A1979%3A25%3A%3A101 . The page offered a link expressly for crawlers, which led to https://www.e-periodica.ch/cntmng?bot=1&pid=ens-001:1979:25::101 . Opened the complete five-page PDF (one metadata page plus printed pp203–206). Read pp203–204: D12 is exactly the specialization A=k[t], M=(t) of Kleiman's first example; D13 is exactly the specialization B=k[x,y], p=(x), k algebraically closed of his second example. Their underlying corrections are known, and the purported new examples are already instances of his examples. Direct byte download returned HTTP429, so a SHA256 of the PDF bytes was not obtained in that attempt. The primary PDF was successfully read through the search tool. Ref: turn863627033view0.
7. Independently searched the attached French EGA sources for III4.3.6 and found the exact correction already in EGA III/2, *Errata et addenda*, Liste2, A, entry (III,4.3.6): replace equality by containment. Attached locator: `latex_sources/EGA_FR/source/ega3/ega3-7-fr.tex`, source lines4137–4139, following the edition's page marker218. A journal-page-to-edition-page comparison remains to be recorded; no unverified page91 claim is retained. Source theorem III4.3.6 at `ega3/ega3-1-fr.tex` line11583ff.
8. Read EGA 0_IV19.3.12 directly in the attached French file `ega4/ega0-19-fr.tex`, source lines1370ff, printed pp85–86. Read Err_IV8 in `ega4/ega4-errata-addenda-list3-fr.tex`, lines297–300. The latter deletes the proposition because the proposed varieties of lifts are not linear. It does not state a false-theorem counterexample.
9. System 2 queries: `"formally smooth" "adic" "lifting" "Cohen" noetherian`; `"19.3.12" Grothendieck`; `"formally smooth" "square-zero" "complete" "noetherian" lift algebra`; `"algebraic extension" "regular sequence" polynomial ring infinite`. Found standard complete-local Cohen and formal-scheme material; no exact nonlocal theorem with both topological module conditions was identified.
10. Opened Stacks Tags07ED,07NQ,07PK,08SM. Verified: completion preserves maximal-adic formal smoothness; noetherian local formal smoothness implies flatness; completed local formal smoothness gives a regular ring map; square-zero extension obstruction/classification/automorphisms are Ext2/Ext1/Ext0. Exact current statements: Lemma15.38.4, Proposition15.41.5, Proposition15.50.2, Lemma92.16.1.
11. System 2 queries: `site:stacks.math.columbia.edu regular ring map cotangent complex flat module Popescu`; `site:stacks.math.columbia.edu "Popescu" "Theorem"`; `Neeman chromatic tower D(R) lemma 2.12 1992 pdf`; `Blickle Fink 2501.09437 Theorem 2.10`. Opened Stacks Tag07GC, Theorem16.12.1: every regular noetherian ring map is a filtered colimit of smooth maps. Together with smooth cotangent complexes and commutation with filtered colimits, this replaces the 2025 preprint input in the proof of A14. The arXiv PDF open for2501.09437v1 was disabled; no assertion was attributed to unopened content.
12. Opened Neeman, *The chromatic tower for D(R)*, Topology31 (1992),519–532, at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/neeman-chrom.pdf . Read Theorem2.8, pp526–528, and Lemma2.12, p527: derived tensors with all residue fields detect zero objects in D(R) for noetherian R. Confirmed applicability to the possibly unbounded cone in A14. Author credit: Neeman, with appendix by Bökstedt.
13. Direct byte retrieval of https://grothendieck.umontpellier.fr/22.pdf succeeded:13,133,716 bytes; SHA256 4c0c0da024b937aafffc727d6fe192e42042d28ba6c42b3cad31e08ea8444c7b. Visually inspected physical PDF pages13–14, corresponding to archive pencil/footer sheets12–13. Definition4.7 is on sheet12; the square-zero existence question is on sheet13. The distinction changes the historical locator from the source run's physical-scan numbering. The main paper quotes20 words from sheet13 and does not reconstruct the missing earlier condition P.

## Current classifications

- D11: known correction, already in EGA III/2's own errata. The generic-formal-fibre example is exposition of a known phenomenon.
- D12, D13: known; the same constructions are Kleiman1979 pp203–204, specialized.
- D3: true statement restored by the written square-zero/closed-power proof; historical erratum verified. Earlier occurrence of the repair remains unresolved after the logged searches; no novelty certification.
- A16: targeted proof check confirms the deformation argument, with Popescu replacing the preprint input. Exact literature equivalence remains unresolved. A separate full statement-only re-proof was completed later in this run; see the final update below.
- B2-2: proof checked and independently re-derived by a separate same-model worker. Exact literature status remains unresolved; do not infer newness from failure to locate a matching formulation.

## Searches still required at the initial pass (subsequently addressed below)

Targeted arXiv, authors' pages, ECCC and Hexagon searches for the three main results; Stacks tag history; primary-source reading of the formal-scheme deformation comparisons; exact manuscript quotation for Deligne's presentation question. These are open source gates, not completed searches.

## 2026-11-23, second main-theorem search and exact formal-scheme comparison

The following searches were performed during the present run; a negative or irrelevant returned result is not treated as a proof of novelty.

| Search or opening | Result and consequence |
|---|---|
| `"formally smooth" "Artinian" "19.3.12"` | No exact alternative proof identified; generic lifting references returned |
| `"Cohen" "adic" "lifting" noetherian nonlocal` | Mostly Cohen–Macaulay formal-fibre lifting and coefficient-ring expositions, not the exact theorem |
| `"algebraic extension" "Artinian" "regular sequence" Deligne` | No exact prior formulation identified |
| Stronger-engine `"19.3.12" "smooth"` | Irrelevant numeric matches and topological-formal-smoothness sources; no settled literature classification |
| Stronger-engine `"formally smooth" "adic" "lifting" "square-zero"` | Stacks topological formal smoothness and standard sequential adic lifting; no arbitrary pro-Artinian theorem found |
| Stronger-engine `"algebraic extension" "Artinian" "Deligne"` | Basic field-extension material and Deligne publication listing, not the requested exact construction |
| `site:arxiv.org "pro-Artinian" "formally smooth"` | No direct exact result in the returned batch |
| `site:hexagonmath.org "Cohen" "lifting"` | No direct exact result in the returned batch |
| `site:eccc.weizmann.ac.il "formal smoothness"` | No direct result in the returned batch |
| `"Pérez Rodríguez" "formal schemes" "lifting"` | Located2008 and2016 published deformation papers and the author's primary page |
| Opened `https://martapr.webs.uvigo.es/Inv.html` | Author publication page; followed its Basic deformation PDF link |
| Opened `https://martapr.webs.uvigo.es/Investigacion/deformation-v3.2.pdf` | Definition1.3p3 includes pseudo finite type; Corollary4.3p13 proves existence of affine smooth formal lifts; this covers a narrower hypothesis than the full arbitrary-residue-algebra adic theorem |
| Opened `https://arxiv.org/pdf/2402.02879` | Author's2015 version of published JournalAlgebra445(2016)78–102, *Deformation of formal schemes through local homology*; Definition1.2p6, Proposition2.13pp10–11, Proposition4.3p20 and Proposition5.1p21 all checked in context |
| `site:arxiv.org "algebraic extensions" "flat" "Artinian"` | No exact presentation theorem identified |
| `site:github.com/openai/math "Cohen" "formally smooth"` | No directly relevant research result identified; no claim that all laboratory research was exhaustively reviewed |
| Opened Hexagon homepage and advanced search | Current public repository and search entry inspected; no exact theorem located by the domain searches |
| Stronger-engine searches restricted to arXiv, Hexagon and ECCC for `formal smoothness pro-Artinian lifting Cohen algebras` and `algebraic field extension arbitrary Artinian lift equations flat regular sequence` | Returned broad Hexagon catalogue entries and unrelated material; this does not settle priority |
| Stronger-engine search of OpenAI/GitHub for `Cohen lifting formally smooth adic algebra` | Returned unrelated educational/security material; no direct theorem found |

### Exact2016 comparison

Pérez Rodríguez's Proposition5.1 assumes a pseudo-finite-type morphism and characterizes smoothness by a completed cotangent complex in degree zero with finite-rank locally free differentials. The adic theorem here makes no finite-type assumption on B0/J over A0 and no finite-generation assumption on the quotient module of differentials. The earlier proposition therefore does not by itself give the present full scope. Proposition4.3 concerns completed versus ordinary Ext for coherent coefficients under pseudo-finite-type hypotheses; it supports the deformation-theoretic context but is not silently applied beyond those hypotheses. The draft now cites both published papers and explicitly compares the scopes.

### Stacks current statement and history checks

Opened Tag08R5, Lemma92.9.1 (smooth cotangent complex is the module of differentials in degree zero), and Tag08S9, Lemma92.3.4 (cotangent complexes commute with directed colimits). Opened both advertised history pages, `https://stacks.math.columbia.edu/tag/08R5/history` and `https://stacks.math.columbia.edu/tag/08S9/history`. The08S9 current statement page records the2017 correction of the order of the numerator/denominator indices and a2019 comment about affine-limit schemes; its2026 comment asks about the ambient category of the colimit. The current statement is used with constant base and scalar extension along the directed system. No stronger result about arbitrary adically formally smooth algebras was inferred from that history.

### Classification after this pass

D11: known, corrected in EGA's own Liste2A erratum. D12: known, exact specialization of Kleiman1979p203. D13: known, exact specialization of Kleiman1979p204. Pro-Artinian lifting: proof supplied for an expressly withdrawn EGA assertion, prior identical proof still unsettled. Nonlocal adic lifting: complete-local and pseudo-finite-type special cases identified precisely; exact full formulation still unsettled. Algebraic-extension theorem: statement-only reproof complete, exact earlier occurrence still unsettled. The paper asserts no priority and does not label an unsettled search result as new.

## Independent proof closure and further source checks

The nonlocal theorem now has a complete separate same-model statement-only reproof, compared by the author worker after its derivation; records/papers_5_6/BLIND_PAPER4_A16.md and PROOF_AUDIT.md give the exact scope. This closes a checking gate, not a literature gate. Reopened Stacks08SM,07PK,08R5 on2026-11-23: Lemma92.16.1 has no finite-presentation assumption on the algebra; Proposition15.50.2 concerns completed local rings and does not require a G-ring hypothesis, whereas15.50.3 does; the proof uses only15.50.2.

## 2026-11-23, 02:15–02:33 UTC: broader nonlocal and arbitrary-residue search

This pass deliberately searched formulations that might subsume the existence theorem without using the manuscript's terminology. Queries included `"formally smooth" "complete" "lifting" "nonlocal"`; `"Cohen" "formally projective" algebra lift`; `"cotangent complex" "adic" "not" "finite type" deformation`; `"Luna's fundamental lemma" Temkin Abramovich pdf`; `"formally smooth" "adic" "Illusie" lifting`; `"algèbres de Cohen" relèvement non local`; `"formally projective" "lifting"`; `"A characteristic p analog of formal lifting properties" authors arxiv`; `"formally smooth" "nonlocal" "adic"`; `"formellement lisse" "relèvement" "non local"`; `"Datta" "Olander" "formal lifting" pdf`; `"formally smooth" "lifting" "nonlocal" algebra cotangent`; `"formellement projectif" "relèvement"`; `"formellement lisse" "adique" "relèvement" "algèbre"`; `"formally smooth" "adic" "Ext" vanishing`; `"formally smooth" "non-local" lifting`; `"formally smooth" "complete" "square-zero" "nonlocal"`; `"formally smooth" "lifting" "Noetherian adic" algebras`; `"formellement lisse" "relèvement" "adique" Grothendieck`; `"deformations" "formally smooth" "adic" algebra noetherian`; `"relèvement" "algèbre" "formellement lisse" nilpotent`; `"topological algebra" "cotangent complex" "formally smooth" lifting`; `"Ionescu" "Hochschild homology of a topological algebra" pdf`; `"Illusie" "formellement lisse" "adique" relèvement`; `"formal smoothness" "deformation" "noetherian" nonlocal`; `"formally smooth" "lift" "nilpotent" "noetherian" algebra deformation`; `"homomorphisme régulier" "relèvement" "nilpotent"`; `"Illusie" "formally smooth" "complete" cotangent projective`. Both search engines were used in separate calls. The recent Datta–Olander publication was checked with a recency-filtered search and then its primary preprint.

### Primary texts opened and their exact scope

1. **D. Abramovich and M. Temkin, *Luna's fundamental lemma for diagonalizable groups*, Algebraic Geometry 5 (2018), 77–113**, DOI 10.14231/AG-2018-003. Primary author PDF opened and read: `https://math.huji.ac.il/~temkin/papers/Lunas_Fundamental_Lemma.pdf`; the journal PDF was also located at `https://content.algebraicgeometry.nl/2018-1/2018-1-003.pdf`. Section 2.2.10, printed p. 84, invokes Cohen lifting, and Theorem 2.2.11, pp. 84–85, gives a splitting result. The surrounding conventions in §2.1.2 are for local rings with their maximal-ideal topologies. The cited **Stacks Tag07NR, Lemma15.41.6**, was opened separately and explicitly assumes a complete noetherian local algebra. The apparently unqualified phrase about a complete algebra in §2.2.10 cannot be read as an unrestricted nonlocal lifting theorem. The source is a complete-local comparison, not an exact prior statement of A16.

2. **R. Datta and N. Olander, *A characteristic p analog of formal lifting properties***, published in IMRN 2026, issue15, rnag167. The current author publication page and the primary arXiv PDF `https://arxiv.org/pdf/2512.00648` were opened; the PDF identifies v3, 15 December 2025. Section4.1, printed pp.25–29, especially Proposition4.12, concerns formal lifting properties of completion maps in characteristic p. It distinguishes ordinary discrete formal smoothness from the automatic adic formal étaleness of completion. It does not state existence of deformations of arbitrary nonlocal adic algebras over square-zero base extensions. Its discussion also reinforces why higher cotangent homology cannot be discarded merely from a low-degree infinitesimal lifting criterion in nonnoetherian generality. The proof in this paper retains its noetherian regularity/Popescu/residue-detection argument.

3. **A. Arabia, *Relèvements des algèbres lisses et de leurs morphismes*, Comment. Math. Helv. 76 (2001), 607–639.** Opened the primary author PDF `https://webusers.imj-prg.fr/~alberto.arabia/pub/commentarii.pdf`. Theorem1.3.1 is stated in the introduction on printed p.608 and lifts smooth algebras over a quotient of a ring. The smoothness convention in §0.2, printed p.612, includes finite presentation. Section3 treats formal completions in this finite-presentation setting. Thus the broad base ring allowed there does not remove the finite-presentation restriction on the residual algebra. This is a strong classical comparison for smooth affine lifts, but not the exact arbitrary B0/J formulation.

4. **J.-Y. Etesse, *Relèvement de schémas et algèbres de Monsky–Washnitzer: théorèmes d'équivalence et de pleine fidélité*, Rend. Sem. Mat. Univ. Padova 107 (2002), 111–138.** Opened and read the primary Numdam PDF `https://www.numdam.org/item/RSMUP_2002__107__111_0.pdf`. Theorem4, printed pp.116–117, lifts smooth algebras using Elkik's theorem. Proposition6, pp.120–121, and Proposition6′, printed p.121, explicitly assume topologically finite type in the complete target category. The definitions on p.113 make this finiteness requirement explicit. These results do not cover an arbitrary residual noetherian algebra in A16. The PDF text extraction renders primes as digits; the item following Proposition6 is Proposition6′, not Proposition68.

5. **SGA1, Exposé III, Theorem2.1 and the following remark**, recomposed p.53 (original p.63), were read in the primary text. The remark anticipates lifting maps to a complete linearly topologized target through a closed topologically nilpotent ideal. Its theorem and the exposition's convention retain local rings and finite residual extension. It is relevant earlier context for the first theorem, but is not an exact source for arbitrary topological B and arbitrary pro-Artinian C. It is also a lifting-of-maps result, not the nonlocal deformation-existence theorem.

6. **EGA0_IV, §§19.1–19.2**, were reread in the supplied French source. Proposition19.2.4 identifies formal and strict formal projectivity when the module topology is induced by the base topology; Proposition19.2.5 proves completion and base-change stability. Neither statement gives the square-zero deformation preservation used here, where the base is discrete and the module has its own adic topology. This prevents silently applying19.2.4 to replace the two separate module arguments.

7. **C. Ionescu, *Hochschild homology of a topological algebra and formal smoothness*, Comm. Algebra22 (1994), 4801–4805** was located through the primary author's publication page `https://www.imar.ro/~cionescu/publications.html`, which was opened. The publisher endpoint returned HTTP403. The article itself was not read, so its exact relevance remains an explicit retrieval gap; neither an exclusion nor a theorem-level attribution is made. A secondary metadata service incorrectly suggested1995, whereas the author's bibliography and journal volume list1994.

Searches also returned modern translations, automatically generated course pages, Stacks mirrors, and user-associated pages. These were not used as independent prior-literature evidence. The proof's obstruction/classification formalism is classical; the possible contribution is its explicitly justified scope and module conditions, not a new deformation principle.

### Final literature assessment after this pass

No opened primary text in this pass states the exact combination of nonlocal noetherian adic formal smoothness, arbitrary residual algebra, square-zero base deformation, and preservation of both formal projectivity conditions. This is a report on the checked sources, not a theorem of nonexistence in the literature. The exact first occurrence of A16 remains unresolved. The same caution remains for the restored pro-Artinian statement and the arbitrary-cardinality presentation theorem. No change to the paper's non-priority wording is warranted; the current draft already says that it asserts no first occurrence.

## 2026-11-23: exact finite triangular construction attribution

Additional queries: `"field extension" "regular sequence" "infinite" presentation`; `"algebraic extension" "transfinite" "polynomial" "regular"`; `"extension de corps" "suite régulière" présentation`; `"field extension" "arbitrary lifts" "Artinian"`; primary-domain searches for `field extension cotangent complex regular sequence algebraic extension`, `algebraic field extension infinite regular sequence presentation lift`, and `extension corps presentation suite reguliere releve plat`; `"flat" "lifts" "regular sequence" Artinian`; `"algebraic extension" "monic" "transfinite"`; and `"Deligne" "algebraic extension" "flat" presentation`. Automatically generated course pages were excluded. Opened **Stacks Tag07BV, Lemma10.158.11**, `https://stacks.math.columbia.edu/tag/07BV`. It proves that every field extension is a filtered colimit of global complete intersection algebras, using a finite triangular monic presentation after a transcendence basis. This is exactly the classical finite construction inside the third theorem. The main paper now cites it explicitly. The tag does not state one arbitrary-cardinality presentation with flatness for every Artinian lift of all equations, including perturbations involving later variables. The exact earlier occurrence of that full formulation remains unresolved. Its finite algebraic ingredients are standard, and no newness is claimed for them.


## Further topological-algebra comparison, 2026-11-23, 02:39–02:43UTC

Queries included `"Hochschild homology of a topological algebra and formal smoothness" pdf`; `"Ionescu" "4801" "4805" pdf`; `"Ionescu" "formal smoothness" topological algebra`; `site:anstuocmath.ro/mathematics/pdf2/ionescu.pdf "5.2" "Theorem"`; `"Hochschild homology" "formal smoothness" "Brezuleanu"`; `"formal smoothness" "nonlocal" "cotangent"`; `"Cohen" "algebras" "lifting" "Radu"`; `"algèbres de Cohen" "relèvement"`; `"formal smoothness" "lifting algebras" noetherian`; `"Algebraic Differential Calculus" Kunz pdf`; `"Cohen algebra" "formally projective"`; `"Cohen algebras" "adic"`; `"relèvement" "formellement projectif" algèbre`; `"formally smooth" "linearly compact"`; `"formally smooth" "pseudocompact" lifting`; `"19.3.12" "EGA"` with user-associated mirrors excluded. Both engines were used in separate calls.

**Ionescu's own published survey narrows the remaining retrieval gap.** C. Ionescu, *Hochschild (co)homology in commutative algebra. A survey*, An. Şt. Univ. Ovidius Constanţa9(2001),87–96, was downloaded from the journal's primary server at `https://anstuocmath.ro/mathematics/pdf2/ionescu.pdf` (the www endpoint returned403). Its Theorem5.2, printed p.93, attributes the1994 article's main result to the topological Hochschild–Kostant–Rosenberg isomorphism under the additional noetherianity of all completed tensor powers. Theorem5.3, pp.93–94, states a converse with the completed tensor square noetherian. Those are homology characterizations, not a square-zero algebra-existence theorem or preservation of the two module conditions. The survey's exact statements have been read; the1994 original article remains unavailable and is not declared fully checked. Scratch PDF SHA256: `0553a79ac225e4b80088069f55f380719140e2e206957be2354c7d156ec13e52`.

**EGA's similarly named subsection was checked directly.** The attached French LaTeX, `EGA_FR/source/ega4/ega0-22-fr.tex`, §22.1, printed pp.183–186, was read. Theorem22.1.1 is a differential/associated-graded criterion for an algebra B already given; Proposition22.1.4 is a local Artinian test criterion and invokes the complete-local lifting theorem19.7.2. Neither is the general nonlocal existence theorem asserted here. The subsection heading about lifting formal smoothness is therefore not evidence that the full A16 statement is already there.

The pseudocompact/formal-group searches found special local or representability settings, but no primary text giving the exact unrestricted pro-Artinian statement was identified. These additional comparisons leave the exact priority gates open and do not alter the paper's non-priority wording.

## 2026-11-23, 03:05–03:11 UTC: two further primary lifting comparisons

Searches included `"relèvement" "formellement lisses" "adique"`, `"Cohen" "lifting" "non-local" rings`, `"adic" "formally smooth" "deformation" noetherian`, `"formally smooth" "lift" "algebra" "nonlocal"`, `"adic" "lifting" "Cohen" "square-zero"`, and `"formally smooth" "deformation" "not of finite type"`. Both search engines were used in separate calls. Search results from course mirrors and automatically generated material were excluded as priority evidence.

- **Paolo Valabrega, *On two-dimensional regular local rings and a lifting problem*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (3) 27 (1973), 787–807.** Primary PDF: https://www.numdam.org/item/ASNSP_1973_3_27_4_787_0.pdf . Remark7, printed pp.805–806, quotes the complete-local EGA0_IV19.7.2 theorem and then explicitly identifies the different problem of lifting an incomplete regular local ring. Theorem8 supplies a special-case answer to that local problem, as Remark8 explains. These passages do not give the arbitrary nonlocal complete-adic theorem. Pages805–806 were read as text and visually inspected. Scratch PDF SHA256: `0d7b3d48dadbd44676c706396291ffeef684e7d8f91243a0a6ab1f608dbf262d` (1,635,309 bytes,22 physical pages).

- **Moritz Kerz and Georg Tamme, *A remark on crystalline cohomology*, Mathematische Zeitschrift 309 (2025), article48**, DOI10.1007/s00209-024-03675-6. Primary publisher PDF: https://link.springer.com/content/pdf/10.1007/s00209-024-03675-6.pdf . Section3 begins on article p.3 with the explicit restriction to topologically finite-type, formally smooth algebras over a complete principal-adic base. Proposition3.1, article p.4, upgrades reduction to an equivalence after simplicial enrichment; its existence argument invokes vanishing of smooth-algebra deformation obstructions. This is a recent precise finite-type comparison, not the unrestricted residual-algebra assertion here. Article pp.3–4 were read as text and visually inspected. Scratch PDF SHA256: `39920f392b3226131320998f82a8362f67b354b911f1e6cd891dc7dbca09784c` (235,056 bytes,10 pages).

No exact earlier occurrence of the full A16 formulation was identified by this additional pass. The paper remains unchanged and continues to make no first-occurrence claim.

## Final terminology search for the pro-Artinian statement

Queries on2026-11-23: `formally smooth pro-artinian`, `formellement lisse pro-artinien`, `19.3.12 EGA correction`, `formally smooth linearly compact`, `formally smooth pseudocompact Brumer`, and `19.3.12 EGA false`. These found local pseudocompact deformation discussions and general formal-variety references, but no primary text giving the exact unrestricted lifting statement was identified. A text search of the attached English SGA3 compilation around ExposéVII_B found pseudocompact module theory and formal étaleness; its translator additions were not treated as primary evidence or as new original theorems. No additional claim of source closure is made from that search.


## Record: workbench/records/paper_4/ARITHMETIC_LITERATURE.md

# Arithmetic-example literature comparison

Current run: 23 November 2026, from 02:54 UTC. Worker GPT-6 Astra, paper_4. This is a literature check, not a blind reproof of the arithmetic construction. The current Paper1 introduction statement was read, and search results exposed short prior source summaries. No independent arithmetic-proof label is claimed here.

## Exact target

An excellent Dedekind domain R of characteristic zero, with2 invertible and fraction field algebraic over Q, such that cd₂(FracR)=1, Pic(U)/2 has infinite dimension for every nonempty open U, and every nonempty affine U has cd₂(U)=2 although the stated pointwise bound is1. The persistent mod-two class-group obstruction and control of local two-primary degrees must occur together.

## Primary comparison: Popescu–Vraciu1985

N. Popescu and C. Vraciu, *On Dedekind domains in infinite algebraic extensions*, Rend. Sem. Mat. Univ. Padova74(1985),39–44. Official full PDF: https://www.numdam.org/item/RSMUP_1985__74__39_0.pdf . Seven physical pages including repository cover; SHA256 ac2125693519f4648dfb83fe6e46b64f48a414b7cbc88b21392fdf8ddd6e0c7f.

The theorem on p.40, proved pp.40–41, characterizes intersections of discrete rank-one valuation rings in an algebraic extension: finitely many selected prolongations over each original prime are exactly the Dedekind condition. The corollary p.42 handles all prolongations. Examples1–3 pp.42–44 use quadratic towers and local splitting prescriptions to exhibit varied behavior of valuations and residue fields. This is prior art for the noetherian limit-ring mechanism. The complete mathematical text was read through the repository extraction. It contains no class-group preservation or cohomological-dimension theorem.

## Primary comparison: S. A. Popescu2022

Sever Angel Popescu, *Infinite algebraic extensions of Dedekind structures*, Mathematical Reports24(74)(2022),no.3,505–512. Official full PDF: https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/3/14.pdf . Eight pages; SHA25630510243519fe67cb4676ab7eea3eddb6d650db198916e816f011e15b6b6141b. Cached as tmp/paper_4/Popescu2022.pdf. The entire eight-page text was read in this run.

Section5, printed pp.511–512, begins with D=Z[1/2], K₀=Q and K₁=Q(i). At stage n it chooses an element nonsquare at every prime over the first n+1 odd rational primes and adjoins its square root. Each old odd prime is eventually unramified and inert. The integral closure in the union is Dedekind, using Theorem1 p.506, proved pp.508–509. This is a direct prior source for the eventual-inertness quadratic-tower construction. It has no Picard or ideal-class-group control, no assertion Pic=0, and no Brauer or cohomological-dimension calculation. Dyadic primes are not controlled by the written construction, so cd₂=1 is not a consequence supplied by the paper. Its bibliography points back to Hasse's *Zwei Existenztheoreme über algebraische Zahlkörper*, Math. Ann.95,229–238, and to Popescu–Vraciu1985.

## Heitmann1974: still not primary-text closed

R. C. Heitmann, *PID’s with specified residue fields*, Duke Math. J.41(3)(1974),565–582. Crossref primary publisher metadata confirms DOI10.1215/S0012-7094-74-04162-3 and the official download endpoint https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-74-04162-3 . The DOI landing page, old Euclid article link and verified download endpoint return a security-check HTML page; the Duke page returns403. No article text was obtained or read. No security control was bypassed.

Search-result discussions quote a TheoremB about arbitrary countable torsion class groups and finite residue fields. These are leads only: they do not close the primary-source gate, and no claim about the precise fraction field of Heitmann's construction is made from them. In particular, the theorem quoted in those discussions does not state the target's algebraic-over-Q or cd₂=1 requirement.

## Search scope and current classification

Both web-search systems were used, including exact Heitmann title/DOI queries and combinations of Dedekind, algebraic over Q, infinite class group, Picard, Brauer and cohomological dimension. The official Popescu sources above were opened; bibliographic discussions and unrelated local-cohomology papers were treated only as leads. No primary source with the full target combination has been identified in this pass. That is a bounded search outcome, not a priority theorem. The existing realization theorems and local inertness constructions should be credited explicitly, while the persistent mod-two classes plus all-local-degree control remain the exact comparison target.


## Visual and proof-scope note

Printed pp.511–512 of Popescu2022 were also visually inspected. A separate false intermediate assertion in its Section4 proof was found and recorded, with an explicit multiquadratic counterexample, only in CORRECTIONS_FOR_AUTHORS.md. That assertion is not part of the Section5 construction and is not used for any result in Paper1. The earlier Popescu–Vraciu1985 valuation criterion provides the needed known noetherian foundation.

## Hasse source and publication year, checked 2026-11-23

Helmut Hasse, *Zwei Existenztheoreme über algebraische Zahlkörper*, Mathematische Annalen95 (1926),229–238, DOI10.1007/BF01206607. The publisher-deposited Crossref metadata gives December1926; the 1925 date in Popescu2022's bibliography should not be repeated without a different bibliographic explanation. The primary GDZ volume and article were retrieved at https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0095/LOG_0017.pdf . Scratch PDF SHA256 `4a42741a697e7bbd1d0effb0913cdcd5ff374bf99475926b57520f61155f7e96`,11 physical pages including repository cover. Satz1, p.229, is a classical finite-extension existence theorem with prescribed finitely many local decomposition data. Satz2, p.232, has additional roots-of-unity and coprimality-of-class-number hypotheses; it is not a theorem that old 2-primary ideal classes persist up an arbitrary quadratic tower. The relevant statements and surrounding proof portions were read in OCR, and p.232 was visually inspected. This is a bounded source comparison, not a claim to have independently proved Hasse's results or read every page. Crossref metadata is saved only in scratch as `Hasse_crossref.json`.

## Final additional search and conditional Heitmann scope observation

Further searches, 2026-11-23: `Heitmann PID specified residue fields pdf`; `Heitmann 1974 565 pdf`; `Ray Heitmann publications residue fields`; the exact title with `dissertation` and `thesis`; `Dedekind Picard cohomological dimension infinite`; `Dedekind class group algebraic extension infinite`; `dimension cohomologique Pic Dedekind`; `Stiemke fields ideal class`; `Dedekind domain algebraic over class group`; `cohomological dimension Picard infinite algebraic`; and Schilling's exact book title with `111`, `Stiemke`, and `Lemma31`. Both search engines were used in separate calls. No exact persistent Pic/2 example with the required arithmetic fraction field and cohomological dimension was identified. This is a bounded search outcome, not a priority claim.

The AMS December1973 annual index identifies Heitmann's preliminary announcement at abstract page A-385, but opening and direct retrieval of https://www.ams.org/journals/notices/197312/197312FullIssue.pdf both returned403. No announcement text was read. The Schilling1950 publisher metadata at DOI10.1090/surv/004 identifies Chapter4, *Special ideal theory*, pp.89–123; the publisher full-text opening returned403. Popescu–Vraciu1985 p.42 cites Schilling's Lemma31p111 for Stiemke-field constructions. Schilling's lemma has not been read in its primary text.

The MathOverflow discussion at https://mathoverflow.net/questions/42430/two-questions-about-finiteness-of-ideal-classes-in-abstract-number-rings was reopened as a source lead only. It quotes Heitmann's TheoremB as prescribing a countable torsion class group and exactly one residue field F_p for each rational prime p. That attribution remains secondary and is not used as a verified statement of the primary paper.

**Independent conditional deduction from those quoted hypotheses.** Suppose R is a normal characteristic-zero domain, Frac(R)/Q is algebraic, and for every rational prime p there is a maximal ideal of R with residue field F_p. Let K be any number field contained in Frac(R). Every element of O_K is integral over Z⊂R, so normality puts O_K inside R. Contracting the selected maximal ideal gives a prime of O_K over p whose residue field injects into F_p, hence is F_p. Thus K has a degree-one prime over every p. Let N/Q be a normal closure of K and let its Galois group act transitively on the embeddings of K. If [K:Q]>1, this action has a derangement: the average number of fixed points is one, while the identity fixes more than one, so some element fixes none. Chebotarev supplies an unramified prime with that Frobenius conjugacy class; the standard factorization description then gives no degree-one prime of K over it, a contradiction. Therefore every such K is Q and Frac(R)=Q. An overring of Z in Q is a localization of Z, so R is a PID. In particular its Picard group is zero. Consequently, **if the secondary quotation of TheoremB is exact**, its nonzero-class-group examples cannot also have fraction field algebraic over Q. This deduction does not replace primary retrieval or determine the other conclusions of Heitmann's paper. It uses the classical Chebotarev theorem and the elementary transitive-action count; it is not presented as a new theorem or added to any paper.


## Record: workbench/records/paper_4/BOUNDARY_LITERATURE.md

# Boundary-neighborhood and finite exceptional wild inertia: literature pass

Date: 2026-11-23, current run. Worker: GPT-6 Astra, /root/paper_4. This is supplementary source work for Paper 1. The independent derivation was completed and saved in BLIND_PAPER1.md §§3.1–3.2 before the Drinfeld and Esnault–Kindler texts below were read. The later comparison is therefore targeted source attribution. No priority certification is made.

## Exact known projective input

Drinfeld, *On a conjecture of Deligne*, Mosc. Math. J.12 (2012), 515–542, has a primary current author preprint at `https://arxiv.org/pdf/1007.4004` (v7, 1 March2018). **Lemma C.2, preprint p.19**, gives connected restriction to a smooth complete-intersection curve transverse to the smooth divisorial boundary. Its proof explicitly invokes Fulton–Lazarsfeld, Theorem2.1(A), then uses tameness and transversality to make the pulled-back curve smooth. This is the mechanism independently reconstructed in BLIND_PAPER1.md. **Proposition C.1, pp.18–19**, supplies existence over finite fields. The exact journal-page correspondence was not established; the preprint locator is therefore retained without inventing a journal page.

Esnault–Kindler, *Lefschetz theorems for tamely ramified coverings*, Proc. Amer. Math. Soc.144 (2016), 5071–5080, DOI10.1090/proc/13151, **Proposition6.2**, extends the result to arbitrary fields. Primary author text: `https://page.mi.fu-berlin.de/esnault/preprints/helene/118-EK.pdf`, statement on author-PDF p.8, proof pp.8–9. The proof uses spreading and the local Kummer description. The original Theorem6.1 omitted the complete-intersection hypothesis. The authors' one-page erratum, dated29September2016, restores it: `https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf`. Both the theorem and erratum were opened and read. This is an already corrected omission, not a newly found error. The incomplete statement must not be cited in isolation.

## Reduction from these sources to the normal projective quotient

Here is the scope comparison, rather than an attribution of a literal unprinted statement. For normal projective X and closed Y, enlarge the reduced divisorial part of Y by an auxiliary divisor containing the singular locus and the higher-codimension parts of Y. Such an auxiliary divisor exists by taking a sufficiently positive hypersurface. Its additional generic points lie in X\Y. Removing a codimension-two subset makes both X and the reduced divisorial boundary smooth. Any connected finite étale cover of X\Y remains connected on this smaller dense open because its source is normal integral. Its ramification along the additional divisor is trivial, while its original divisorial ramification is tame by the definition of Q. The corrected Drinfeld–Esnault–Kindler theorem and tame curve finite generation apply. The resulting quotient surjects onto Q(X,Y). Thus projective finite generation is a known consequence of these published results.

For a proper X with one quasi-projective neighborhood of Y, Raynaud–Gruson, **Corollary I.5.7.14, printed p.52**, makes an isomorphism over that neighborhood to a projective modification after normalization. The surjection of Q groups was proved independently in BLIND_PAPER1.md. This is a direct deduction from the known projective input and the prescribed-open Chow lemma. No exact earlier occurrence of the neighborhood formulation was located. The record should call it a deduction with fully identified inputs, not a new Lefschetz principle.

## Other source comparisons

- Kerz–Schmidt, *On different notions of tameness in arithmetic geometry*, Math. Ann.346 (2010), 641–668; primary preprint `https://www.mathi.uni-heidelberg.de/~schmidt/papers/zahm-alles.pdf`, introduction and Theorem1.1 read. Their divisor-tameness quantifies over **all** normal compactifications. The quotient Q under study imposes conditions on divisors of **one fixed** compactification, so one cannot identify it with their intrinsic tame fundamental group on a singular compactification without another argument.
- Esnault–Shusterman–Srinivas, *Finite presentation of the tame fundamental group*, Selecta Math.28 (2022), article37; primary author PDF `https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf`, Theorem1.1 and introduction read. Its smooth quasi-projective variety has a smooth projective normal-crossings compactification. Its finite-presentation theorem is stronger in conclusion but has these extra hypotheses, and does not directly replace the fixed-normal-compactification argument.
- Diletta Martinelli, Juan Carlos Naranjo, and Gian Pietro Pirola, *Connectedness Bertini Theorem via numerical equivalence*, Adv. Geom.17(1) (2017),31–38, DOI10.1515/advgeom-2016-0028, Theorem1.1, printed p.31. The exact published title corrects an earlier descriptive title in a worker message. On2026-11-23 this worker opened the published-version repository PDF, read its first-page hypotheses and theorem, and visually inspected that page. It applies to every linear subspace satisfying the dimension inequality, over an algebraically closed field of any characteristic. The PDF SHA256 is `675188bfe88081a8a6f92aa67e7b46dc22dbd1c988154b1899e93b42dd52e36e`; primary URL: `https://diposit.ub.edu/server/api/core/bitstreams/d9e33fe8-dd1c-42a4-a579-a349a203ca25/content`. This is a targeted source check after the independent Fulton–Lazarsfeld route, not a second independent proof.

## Finite exceptional wild inertia criterion

The literal statement was read in Paper1's boundary.tex proposition, without its proof: if the finitely many boundary divisorial wild inertia images on one normal projective modification are finite inside Q(X,Y), then Q is finitely generated; only exceptional divisors need checking. This has the expected reduction to an open subgroup avoiding a finite union of finite nonidentity inertia images, followed by the known projective tame result. Exact earlier occurrence of this formulation was not located. It should be presented as an explicit sufficient criterion derived from classical input, without a priority claim.

## Search log and limitations

Queries included `tame fundamental group normal projective variety curve "Theorem 1.1"`; `fundamental group "quasi-projective neighborhood" boundary tame`; `fundamental group "quasiprojective neighbourhood" boundary`; `tame fundamental group "finite" "exceptional divisors" generation`; `"fundamental group" "quasi-projective" "neighborhood" tame normal proper`; `"wild inertia" "finitely generated" "divisors"`; `"Kerz" "Schmidt" "tame" "finite generation" normal`; `"Esnault" "Kindler" "6.1" correction Drinfeld`; `"Lefschetz theorems for tamely ramified coverings" erratum`; `"Drinfeld" "Corollary C.2" "curve"`; `"quasi-projective neighbourhood" "fundamental" proper`; `"wild inertia" "finite image" "finitely generated" fundamental`; `"finite wild" "fundamental group" divisors`; `"tame" "projective modification" "fundamental group"`; `"groupe fondamental" "inertie sauvage" "type fini"`. Both engines were used in separate calls.

The official MathNet bibliographic entry for Drinfeld was opened; its linked AMS journal endpoint returned403. Accordingly the primary preprint's exact numbering is used. Automatically generated courses and user-associated Stacks mirrors returned by the searches were excluded as independent prior literature. No new author correction or outgoing communication is proposed from this pass.


## Additional exact-formulation searches, 2026-11-23, 02:39–02:43UTC

Queries: `"fundamental group" "finite wild" "finitely generated"`; `"tame fundamental group" "finite image" inertia`; `"fundamental group" "exceptional divisors" "finite" "tame"`; `"fundamental group" "bounded ramification" "finitely generated"`; `"groupe fondamental" "voisinage" "quasi-projectif"`; `"tame fundamental group" "finite" "wild inertia" finitely generated`; `"fundamental group" "bounded ramification" "finite generation"`; `"potentially tame" "fundamental group" finitely generated`; `"finite inertia" "finitely generated" etale`; `"inertie sauvage" "image finie" "groupe fondamental"`; `"wild inertia groups" "finite image" "quotient" "tame" fundamental`; `"fundamental group" "finite image" "wild" "Esnault"`; `"tame fundamental group" "normal" "proper" "generated"`; `"fundamental group" "quasi-projective neighbourhood"`. Both engines were used in separate calls. No exact earlier occurrence of either specific formulation was identified.

A primary article by Toshiro Hiranouchi, *Class field theory for open curves over local fields*, J. Théor. Nombres Bordeaux30(2)(2018),501–524, was opened at `https://www.numdam.org/item/10.5802/jtnb.1036.pdf`; its introduction and Theorems1.1–1.2 were read. These are abelian reciprocity results over local fields, not the geometric nonabelian finite-generation criterion here. A search result for Florian Pop's2018 preprint `https://www2.math.upenn.edu/~pop/Research/files-Res/2018-12-24_IOM.pdf` reports finite generation of a valuation-tame group defined using all valuations. Both web opening and direct public retrieval returned403; the source itself was not read and no theorem-level use is made. User-associated course/Stacks mirrors and generic reposts were excluded as independent prior literature.

A subsequent targeted reading of the current Paper1 boundary proof, after the saved independent derivation, agrees with the projective-curve argument and the prescribed-neighborhood modification. Its finite-wild proof is an explicit finite-index reduction; no new independent-proof status is asserted for that proposition by this worker.


## Record: workbench/records/papers_5_6/LITERATURE.md

# Papers 5 and 6: literature and attribution audit

Search/read date: 23 November 2026. Worker: GPT-6 Astra, ChatGPT Pro; inherited effort was not separately exposed. This file records what was actually searched and opened. A search without an exact match does not establish novelty. Primary-source PDFs remain in scratch and are not deposited with these records. Download byte counts and SHA-256 hashes are in SOURCE_DOWNLOADS.json and LATE_SOURCE_DOWNLOADS.json; further hashes are recorded below where a source was already acquired by another worker.

## 1. Decisions by result

| Result | Closest opened sources and exact overlap | Current classification |
|---|---|---|
| Integral Albanese-family implication, SA06 E.3e | Bloch 1979 supplies the torsion cycle map, correspondence functoriality, specialization in Q_l/Z_l, and prime-to-characteristic Roitman theorem. The present proof spreads an entire finite Albanese-kernel relation; it never asserts a torsion preimage exists. | Full proof retained. The exact whole-relation formulation was not located in the searched literature; no priority or novelty claim follows from that negative search. |
| Rationalized-premise failure, E.3f | Classical torsion of E(Fpbar), divisor/Albanese duality and diagonal action. | Elementary counterexample illustrating the integral hypothesis, not a claimed new geometric construction. |
| All-pair algebraic Lefschetz failure, C.1f; finiteness range, C.1k | Clemens Th.(0.2) gives an infinite-dimensional rational Griffiths group on a very general quintic threefold. Projective-bundle and blow-up formulas propagate it. | Explicit uniform consequences of these inputs. The incidence-divisor recursion is written out; exact prior publication of this uniform formulation was not found. |
| Primitive middle radical, C.1j; homological/numerical comparison, C.2k | Hodge–Riemann, hard Lefschetz and the Lefschetz (1,1) theorem; Kleiman Remarks 3.4 and 3.10 record the divisor/curve and dimension-at-most-four cases. | Known Hodge-theoretic consequences. Codimension two in arbitrary dimension is proved explicitly instead of attributing that exact wording to Kleiman's remarks. |
| Scalar factorization mechanism, C.4h–i | Voisin Prop.2.1, Lemma2.7 and Cor.2.5 already use the curve-class pairing and a unimodular line bundle, including Poincare on A×Ahat. Scavia–Suzuki Prop.3.4 proves the general scalar n chi(L). | Known mechanism, explicitly credited. The factorial bound is a direct quantitative consequence; not a new factorization principle. |
| Low-dimensional scalar bounds, C.4j,m–p | Mumford principalization, Oort–Ueno in dimensions ≤3, Beauville generalized Pryms in dimensions ≤5, ADFIO exponent six in dimension six. Beckmann–de Gaay Fortman Prop.4.6 and Th.5.3 already use prime-to-prime isogenies, Bezout and denominator bounds for integral Hodge classes. | Quantitative consequences assembled here: gcd(2,delta) for surfaces and gcd(6,delta) for threefolds. The exact displayed bounds were not found in the inspected sources, but all geometric mechanisms are existing results. No unsupported claim of originality. |
| Walker applications, E.3t/u | Walker 2007, Example5.5, Th5.7, Cor5.9, Th6.2. | Known construction/application, not a new counterexample construction. |
| Surface-supported comparison, E.3q | Voisin Theorem3.14 and Fu–Tian Remark2 identify the BS surface-support conclusion as integral Griff²=0; ACMV2025 §10.1 treats the stronger curve-support algebraic-representative assertion. E3q additionally combines the diagonal factorization with Suzuki's whole Walker-kernel divisibility (ACMV Theorem2.3) and Saito Corollary6.3/Remark6.4. Those later inputs were opened and their scope compared. | Derived combination of known inputs; no novelty claim. The 1983 original full text/printed-page locator is still not recovered. See BS_SOURCE_COMPARISON.md for precise distinctions, retrieval attempts, and targeted proof comparison. Not an admitted main theorem in Paper05. |
| Compact-protorus Hasse principle and global class, SA05 Part A | Milne 1994 full Weil-number definition; Milne 2003 Props2.8,3.5(b),3.10,3.12,4.3 and Th6.3. | Known after the character-group dictionary. Paper06 is a source-comparison note, not a new research theorem. |

The independent proofs and their exposure histories are separate from this novelty decision: see PROOF_AUDIT.md, CHECK_EVENTS.tsv, ROOT_BLIND_CHECKS.md and paper_4/BLIND_PAPER5.md. Independent reconstruction does not make an already published result new.

## 2. Paper 5 primary sources actually opened

### Archive and torsion argument

- **Grothendieck, cote 14.** Official PDF: https://grothendieck.umontpellier.fr/14.pdf . The authentic handwritten sheet numbers are 37–38 for the Albanese-equivalence theorem, 43 for the letter of 27 August 1965, 44 for the positivity formulation, and 45 for the finiteness question. These correspond to PDF pages 38–39 and 44–46 because of the cover. All five pages were rendered and read. PDF SHA-256: `74f21f43a5291a938f7f4aa3c12d44f61ad2eea382d8b7079736844d0d3b61e2`. Earlier packet page references were not blindly reused.
- **S. Bloch, Torsion algebraic cycles and a theorem of Roitman, Compositio Math. 39 (1979), 107–127.** Official Numdam PDF: https://www.numdam.org/article/CM_1979__39_1_107_0.pdf . Proposition3.5, p.115, gives correspondence compatibility; Proposition3.8, pp.117–118, gives specialization compatibility and the required cohomological isomorphism with Q_l/Z_l coefficients; Proposition3.9, pp.118–119, identifies the zero-cycle map with the Albanese map; Theorem4.2, p.119, supplies the prime-to-characteristic torsion theorem. These pages were read in extracted text and visually. The proof in Paper05 uses this exact coefficient-level specialization, not only rational cohomology. PDF SHA-256: `722a5321f9e9d059954e85b6d5e9f15d47e09fad1425ca8d38175516ff501dfb`.
- The specialized zero-cycle torsion step does not need Kato–Saito: any finite support over Fpbar lies on a smooth connected curve, and every point of its Jacobian is defined over a finite field. This elementary deduction was independently obtained by the separate worker.

### Algebraic Lefschetz and primitive positivity

- **H. Clemens, Homological equivalence, modulo algebraic equivalence, is not finitely generated, Publ. Math. IHES 58 (1983), 19–38.** Official PDF: https://www.numdam.org/article/PMIHES_1983__58__19_0.pdf . Theorem(0.2), equation(0.1), printed p.19, and the genericity discussion on p.20 were opened. The theorem is used for the rational Griffiths group of a very general complex quintic threefold, not an arbitrary quintic. SHA-256: `ee74ae40d69ad2ff052ff23a7d15faf0a1b34011661f4ad52f9562aff43d83af`.
- **S. L. Kleiman, Algebraic cycles and the Weil conjectures (1968), 359–386.** Scan: https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf . Remarks3.4 and3.10, pp.379–380, were visually read. They cover the relevant classical divisor/curve cases and dimension≤4 consequence. They do not literally state the arbitrary-dimensional codimension-two claim in the words used in the source run; the new paper supplies that short proof. SHA-256: `e96e2465e0fb3a05084cc7472e6edec44a4cff920b199b271caed9251cab825a`.
- **Q. Jiang, On the Chow theory of projectivizations, J. Inst. Math. Jussieu 22 (2023), 1465–1508.** Primary published HTML: https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/on-the-chow-theory-of-projectivizations/3DA5197C99935D82CCB4E359214AF439 . Theorem2.4 is the projective-bundle formula; Theorem2.8(3) is the blow-up formula. These formulas and their explicit maps are compatible with algebraic equivalence and cycle class maps. The paper writes the codimension-two case used here.
- **Stacks project Tags 02TX and 0FGQ.** https://stacks.math.columbia.edu/tag/02TX and https://stacks.math.columbia.edu/tag/0FGQ . Both current entries and their history pages were opened. The 0FGQ history includes the July 2021 correction of the motive projective-bundle formula (Jiang); the current negative Tate twists are used. The 02TX recent history inspected was an editorial/macro change. This matters because an old formula should not silently be substituted for the current one.

### Jacobian factors: exact overlap and inputs

- **C. Voisin, Cycle classes on abelian varieties and the geometry of the Abel–Jacobi map, Pure Appl. Math. Q. 20(5) (2024), 2469–2496.** Author journal PDF: https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/PAMQ-20-5-a14-VOISIN.pdf . The inspected author preprint is https://arxiv.org/pdf/2212.03046v4 (6 July 2023), pp.5–7, Proposition2.1, Corollary2.5 and Lemma2.7. The theorem gives the direct-summand criterion from integral curve classes; the proof uses the signed curve pairing for a unimodular line bundle and Cor.2.5 explicitly uses the Poincare line bundle on A×Ahat. These mechanisms therefore cannot be presented as new. The author-preprint SHA-256 is `f61faf4c9b4e9a75ab8a99c749c04df93d858ca29a7057b895ecf56c87c83b43`.
- **T. Beckmann and O. de Gaay Fortman, Integral Fourier transforms and the integral Hodge conjecture for one-cycles on abelian varieties, Compos. Math. 159(6) (2023), 1188–1213.** Final author preprint https://arxiv.org/pdf/2202.05230v2 (8 February 2023). Theorem1.1 and Theorem1.2, p.2, identify the integral Fourier/minimal-class criteria and the product-of-Jacobians case. Proposition4.6, pp.14–17, uses prime-to-p isogenies and Bezout to remove denominators. Theorem5.3, p.19, gives an integral-Hodge bound gcd(n²,(2g−2)!) and factor4 for Pryms. This is a bound for the Hodge-class cokernel, not literally the same scalar ideal I_J used in Paper05. The two invariants must not be identified without proof. The exact gcd(2,delta(A)) and gcd(6,delta(A)) scalar statements were not found in the sections read. SHA-256: `ab63a64cc5be9444c4eb36609f4831e662e0f95b19e9be07d5ddb5d7d82f9fbc`.
- **F. Scavia and F. Suzuki, On direct summands of products of Jacobians over arbitrary fields, arXiv:2507.09821v2.** https://arxiv.org/abs/2507.09821 . Proposition3.4, pp.11–12, equations(3.1)–(3.3), already gives the scalar n chi(L) from a curve class. The introduction and nearby propositions/corollaries were read; whole-text searches for the low-dimensional/factorial claims did not locate the exact bounds used here. The present scalar lemma is restricted to rational l-adic class equality, which is enough for every application; the source proves a stronger numerical-class version. The paper's results over arbitrary fields have field and polarization hypotheses; no nonclosed-field statement is imported into the algebraically closed setting without checking it. SHA-256: `56dad8d0137d146439109273591157a6660eda49d570bc640f53b1d25e6bdb9f`.
- **D. Mumford, Abelian Varieties (1970), §23.** Theorem4, p.233, and Corollary1, p.234, were read in the original scan, including the all-characteristic finite subgroup-scheme principalization statement. Scan https://djvu.online/file/2tC7xp3dbqGCh ; printed pp.234–235 are image https://djvu.online/jpg1/2/t/C/2tC7xp3dbqGCh/121.webp . The degree is chi(L), and scheme-theoretic kernels are essential in positive characteristic.
- **F. Oort and K. Ueno (1973), Principally polarized abelian varieties of dimension two or three are Jacobian varieties.** Author preprint https://ir.cwi.nl/pub/27912/27912.pdf , Theorem4, author p.2 (PDF page3), visually read. Good reducible curves give products of Jacobians, which is the form needed. SHA-256: `49af68579791724e1c53a63a8a8c2cb45aca89b6b4a207d6483e6616ad94f9ee`.
- **A. Beauville, Prym varieties and the Schottky problem, Invent. Math. 41 (1977), 149–196.** Author PDF https://math.univ-cotedazur.fr/u/beauvill/pubs/pv.pdf . Proposition2.2, p.155; Theorem5.4, pp.175–176; Theorem6.5(i), p.178, all visually read. The original characteristic≠2 hypothesis is retained at this stage. The normalization Jacobians carry the theta class whose restriction is twice the Prym polarization; the explicit polarized adjoint gives the scalar2. SHA-256: `a072398a3b035dbf7dba79b225299afec3bb037673b5d960eb865a392a7e65f9`.
- **V. Alexeev, R. Donagi, G. Farkas, E. Izadi and A. Ortega, The uniformization of the moduli space of principally polarized abelian 6-folds, J. reine angew. Math. 761 (2020), 163–217.** Author PDF https://www.mathematik.hu-berlin.de/~farkas/a6cr.pdf . Theorem1 and Corollary2, printed p.165, were opened and read. Cor.2 is stated for every complex principally polarized sixfold, not only a generic member. SHA-256: `c637b9406cb644b7f55c7c13d8a63b46a93a766ad5bccfd64c095ff2e770a244`.
- **F. Oort, Finite group schemes, local moduli for abelian varieties, and lifting problems, Compositio Math. 23 (1971), 265–296.** https://www.numdam.org/item/CM_1971__23_3_265_0.pdf . Theorem2.4.1 and Corollary2.4.2, pp.286–287, visually read. Only the direction that a separable polarization lifts is used. A principal polarization is separable. The historical converse is not used. SHA-256: `d26f4320669876099dfbcab554bea1b2f4f90eb714bfdd22badc6a6cc9817c8c`.
- **W. Fulton, Intersection Theory, second edition (1998), §20.3.** Proposition20.3, p.399, and Example20.3.5, p.400, were read in the original scan https://djvu.online/file/Pl4avuZzLcI6I . Specialization preserves integral cycles and is compatible with the relevant proper/flat operations and l-adic classes. It does not require dividing by the residue characteristic. This closes the characteristic2/3 specialization in the displayed bounds.

### Forward neighbors and known examples

- **P. Engel, O. de Gaay Fortman and S. Schreieder, Matroids and the integral Hodge conjecture for abelian varieties**, https://arxiv.org/html/2507.15704v3 . Theorem1.1 and Corollary1.5 were opened. They obstruct minimal curve classes and integral Jacobian factors in very general dimension≥4. The result is a preprint. The page header and manuscript carry different 2026 dates; the version identifier is retained rather than inferring a publication date.
- **The same authors, Optimality of the Prym–Tyurin construction for A6**, manuscript dated 19 December 2025, https://www.iag.uni-hannover.de/fileadmin/iag/homepages/schreieder/publications/IHC_for_A_6.pdf . Introduction and Theorem1.2/Corollary1.3, pp.1–2, were read. The exact minimal algebraic multiple on a very general PPAV sixfold is6; very general dimension≥6 has no split embedding into a product of Pryms. This sharpens the neighboring obstruction. It does not decide s_J for the special sixfold A×Ahat arising from a threefold, nor remove the residual primes in Paper05. Its computer calculation was not reproduced and is not an input to a proof here.
- **M. E. Walker, The morphic Abel–Jacobi map, Compositio Math. 143 (2007), 909–944.** Original published PDF was opened: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4A44146CE680F4F3C857048FDEDD9F48/S0010437X07002278a.pdf/the-morphic-abel-jacobi-map.pdf . Example5.5, p.928, identifies the zero-cycle case; Theorem6.2, pp.933–934, supplies the product-with-a-curve obstruction. Theorem5.7 and Corollary5.9 are the functoriality inputs cited at pp.930 and932. The new paper describes this as an application of Walker.
- **S. Bloch and V. Srinivas, Remarks on correspondences and algebraic cycles**, Amer. J. Math.105 (1983),1235–1253, doi:10.2307/2374341. Bibliographic identity is verified; the 1983 original remains unavailable after the documented ordinary public routes. The later primary texts now distinguish BS Theorem1(ii), surface-supported integral Griff² vanishing, from the curve-supported algebraic-representative/Abel–Jacobi theorem and from the additional quotient assertion E3q. Exact opened modern locators, hashes, coefficient qualifications, proof comparison and the still-unverified original-page gate are in BS_SOURCE_COMPARISON.md and BS_COMPARISON_SOURCE_HASHES.json. Wittenberg's opened 2026 note, https://www.math.univ-paris13.fr/~wittenberg/sri.pdf , §2.3, p.6, Theorem2.4, remains a curve-support statement and is not substituted for E3q.

## 3. Paper 6 exact dictionary and knownness

- **J. S. Milne, Motives over finite fields (1994), corrected author version.** https://www.jmilne.org/math/xnotes/Seattle1.pdf , Definition2.5(a),(b), author p.13, includes integrality after multiplying by a power of p. Proposition2.6 and Remark2.7, p.14, supply the relevant motivic qualification. SHA-256: `4344a61cb7c3a6525b520754afa40c08dc138bfaf736931e104b042dfa5b4548`.
- **J. S. Milne, Gerbes and Abelian Motives (2003), author version dated 21 February 2003.** https://www.jmilne.org/math/articles/2003b.pdf . The precise inspected locators are: Proposition2.8 p.17 (derived-limit exact sequence); §3 and equation(26), p.23 (Weil-number germs); Proposition3.5(b), p.24 (finite-level local–global injection); Proposition3.10, p.25 (H2 inverse-limit comparison); proof of Proposition3.12, p.26 (weight-factor splitting); Proposition4.3, p.29 (unique prescribed global fundamental class); Theorem6.3, pp.36–37 (gerbe formulation). SHA-256: `b1e841b7447ffc46587aea3e1e8ff7bb00fc5bd1001572113dff1e4a40bac743`.
- The character-group isomorphism sends a germ [a,n] to [a^(1/n)] in Gamma/roots-of-unity. It uses the full definition from 1994. The compact factor is H0, while the Artin–Tate band is H0×mu2. Milne's P is H0×Gm. Its H2 injection and fundamental class therefore already imply the two proposed conclusions. No independent reproof can change this literature decision.
- **Milne, Arithmetic Duality Theorems**, https://www.jmilne.org/math/Books/ADTnot.pdf , ChapterI, Theorem4.20 and its proof, pp.65–66. The finite-torus Hasse step and duality were checked in the source. Division lattices kill the inverse-limit H1 obstruction; one must not define protorus cohomology as a naive limit and thereby discard lim1.
- A literal omission in the 2003 definition on p.23 and a transition-index typo are documented in CORRECTIONS_FOR_AUTHORS.md. The counterexample to the incomplete literal definition is (3+4i)/5 for p=2. The comparison note simply uses the full correct definition, without presenting an erratum as a new theorem.
- **Recent AI neighboring work.** OpenAI, *Milne's rationality conjecture for abelian varieties*, 7 October2026, official source https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf . The abstract and Theorem1.1, p.1, were read: the preprint states rationality of pairings of specialized rational Hodge classes with complementary products of divisors in every realization, including crystalline cohomology and residue characteristic2. The full proof was not audited here. SHA-256: `640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234`. This is relevant context for motivic realization comparisons but is not used in the unconditional cohomological argument. It does not by itself prove the full Tate hypotheses for arbitrary smooth projective varieties used in the all-pure-motives interpretation.
- The supplied intake also cites the 2026 van Hoften–Sempliner exposition of a CM-Hodge preprint, and later conditional uses of it. Those wider claims remain explicitly conditional in this register unless independently checked elsewhere by the team. They are not smuggled into Paper06's cohomological conclusions.

## 4. Searches and their limits

The following query families were run on 23 November2026 with the web search service. Routine searches used system2; narrow/novelty verification used system1. Searches are evidence of coverage only.

1. `Grothendieck Albanese equivalence Bloch torsion specialization finite field`; `"Grothendieck" "Albanese equivalence" "torsion"`; `"Albanese equivalence" Bloch cycles cohomology`; `"Albanese equivalent" "homologically"`; `"Albanese" "correspondence" "torsion" "specialization" Bloch 1979`. These found Bloch, Vial/Albanese-kernel discussions and modern Bloch-map work, not an exact identified publication of the whole finite-relation lemma.
2. `"Lefschetz" "algebraic equivalence" "blow"`; `"Albanese equivalence" theorem cohomology torsion`; `"Albanese equivalence" "Bloch" "Srinivas"`. Exact universal C1f formulation not found; no novelty conclusion is inferred.
3. `"Jacobians" "gcd" "six" abelian surface direct summand`; `"abelian surface" "Jacobians" "odd" direct summand`; `"abelian" "Jacobians" "Euler characteristic" factor`; `"direct summand" "Jacobians" "Euler characteristic" surface`. Followed by direct reading of Scavia–Suzuki, Beckmann–de Gaay Fortman and Voisin; this established substantive known overlap despite sparse keyword results.
4. `Beckmann de Gaay Fortman 2023 integral Fourier transforms abelian varieties Jacobian factor`; `Voisin 2024 Jacobian direct summand integral Hodge conjecture abelian varieties Proposition2.1`. Backward references led to Beauville, Mumford, Oort–Ueno and ADFIO; forward neighboring searches found the Engel–de Gaay Fortman–Schreieder sixfold optimality paper.
5. Multiple searches for the exact title `Remarks on correspondences and algebraic cycles`, JSTOR/IAS original PDF and Theorem1/page1236. Bibliographic records and Wittenberg's author note were found; the exact original full-text source gate is preserved.
6. `Milne motivic gerbe Hasse H2`; `"compact" "protorus" "Hasse" Milne`; primary author-site searches for 2003b.pdf and Seattle1.pdf. These directly closed Paper06's knownness decision.
7. `site:hexagonmath.org "algebraic cycles" Albanese`, Hexagon searches for Albanese/gerbe/Milne rationality, and `site:eccc.weizmann.ac.il "Albanese"`. No exact competing Albanese theorem or ECCC entry was identified. A Hexagon listing of the Milne-rationality exposition led back to the official OpenAI preprint. A direct Madapusi-hosted PDF and one Hexagon query endpoint returned retrieval errors; no contents are attributed to those unavailable pages.
8. Current Stacks entries and history were inspected for the projective-bundle formulas. The separate A16 blind proof also opened exact cotangent/deformation tags; its literature details and Neeman hash belong in BLIND_PAPER4_A16.md, not in the paper-5 dependency chain.

## 5. Remaining limits

The selected main theorems have full proofs with checked published inputs and separate-worker checks recorded at their actual scope. This is not a fresh audit of every inherited SA05/SA06 theorem. The 468-row reconstructed register retains those claims and their source/intake histories, including open and conditional statements, without upgrading them wholesale. Broad failed searches do not certify novelty. No external author was contacted, and no correction or paper was submitted anywhere.

## Additional primary AI-laboratory comparison, 23 November 2026

The root worker's official OpenAI mathematics overview identified entries 001 and 032 as relevant neighboring work. The overview is a discovery source, not a substitute for the preprints. The two official PDFs were fetched directly, opened, and their exact main statements and relevant consequence sections read. The search-service PDF endpoint returned `DisabledError`; direct retrieval of the official raw GitHub URLs succeeded. No unavailable page is being cited as though it had been read.

- **OpenAI, *The rational Hodge conjecture for CM abelian varieties*, 6 October 2026.** Official URL: https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf . Retrieved from the corresponding raw.githubusercontent.com URL. SHA-256: `6e3e66a407773ad5091d4cb48d9b4dc55a69c58fb0948a88daf19f3bb21bf27b`. Theorem 1.1, p. 1, states surjectivity of the rational Betti cycle-class map for every complex CM abelian variety in every codimension. The statement includes all finite products and powers. Section 8.2, Corollary 8.3, p. 49, states the rational Tate conjecture for all abelian varieties over finite fields and equality of numerical and prime-to-characteristic homological equivalence. Section 8.3, Corollary 8.4, p. 50, states the Hodge standard conjecture for abelian varieties in arbitrary characteristic; its proof cites Milne's Hodge-to-Tate and polarization theorems with their author corrections.
- **OpenAI, *Milne's rationality conjecture for abelian varieties*, 7 October 2026.** Official URL: https://github.com/openai/math/blob/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf . SHA-256: `640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234`. Theorem 1.1, pp. 1–2, states one rational value for the pairing of a specialized rational Hodge class with each complementary divisor product, simultaneously in all prime-to-p and crystalline realizations. Corollary 6.3, p. 32, states specialization into one fixed good theory of rational Tate classes. Corollary 6.4, p. 33, uses the separate CM Hodge theorem to assert a single rational algebraic cycle realizing every such specialized class in all these realizations, including p=2.

**Extent of this check:** the exact statements, scope, and the named implications in the cited consequence sections were read. The 53-page CM proof and the full rationality proof were not independently re-proved or audited. These are therefore cited as statements of neighboring preprints, not adopted as inputs in Papers 5 or the Paper 6 source comparison.

**Effect on Paper 5:** rational Hodge/Tate surjectivity does not identify the kernel of the cycle-class map modulo algebraic equivalence. Positivity modulo numerical or homological equivalence does not establish the unresolved radical assertion modulo algebraic equivalence. Rational algebraicity also does not remove the integral scalar denominators in the Jacobian factor ideal. The new context paragraph names these precise distinctions; no claim that the preprints settle or refute the paper's integral assertions is made.

**Effect on requested Paper 6:** the preprints bear on realization theories and abelian motives. They do not change the fact that Milne's 2003 results already give the two requested group-cohomology conclusions. Their stated abelian-variety consequences do not supply the full Tate hypothesis for arbitrary smooth projective varieties. The comparison therefore remains known, and the requested research note is withdrawn as known; see `PAPER6_DISPOSITION.md`.
