# Literature and source-search record

All dates in this log are UTC on 23 November 2026 unless specified. Searches are evidence of what was checked, not proof that a result is absent from the literature. Published statements are cited by exact locators in the individual paper records. No result is labelled new merely because a search found no match.

## Root searches and source access

### 01:05–01:09: workbench format and benchmark article

- Opened https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/FORMAT.md through indexed retrieval; returned disabled fetch.
- Directly fetched https://raw.githubusercontent.com/KokunoYumeto/mathematics-workbenches/main/FORMAT.md successfully; format 1 dated 22 November 2026, SHA-256 `b6cff6c746787fc706e3db621a372b83ab49b84e76b218776807154a7cd92832`. The source is cited and kept outside deliverables. Version layout, immutable statement tags, source exclusion, check-event types, and manifest requirements were read in full.
- Opened https://hexagonmath.org/2611.00789: indexed tool access failed and direct fetch returned 403. Searches for the exact identifier found an indexed record of the named Deligne/Alpöge exposition, but the full primary article was not obtained at this stage. No mathematical input is taken from that secondary description.
- Queries: `site:github.com/KokunoYumeto/mathematics-workbenches FORMAT.md`; `site:hexagonmath.org/2611.00789`; `Grothendieck cristaux manuscrits cote 4 Montpellier`; stronger queries `"KokunoYumeto" "mathematics-workbenches"`, `"hexagon:2611.00789"`, `"Grothendieck" "MPL_8_079"`.

### 01:18–01:20: stable cohomology and ramification sources

- Opened Ogus's journal record: https://www.numdam.org/item/ASENS_1975_4_8_3_295_0/; title, volume, pages, and DOI verified. Exact mathematical statements are read in the obtained primary PDF in the paper records.
- Opened Bhatt–Morrow–Scholze journal record: https://www.numdam.org/item/PMIHES_2018__128__219_0/; verified bibliographic year 2018 despite online/acceptance metadata in 2019. Its references identify Berthelot's 1973 note on crystalline weak Lefschetz, to compare directly.
- Query `Katz Messing 1974 Some consequences Riemann hypothesis varieties finite fields pdf Princeton` found Katz's author-hosted PDF https://web.math.princeton.edu/~nmk/old/katzmessing.pdf and original publication metadata.
- Query `Serre Local Fields Herbrand theorem different Proposition 14 15 page 75` located the book; the derivation uses the original PDF independently obtained by the ramification worker. Exact statements: different transitivity, monogenic different, different as ramification-group sum, and Herbrand upper-numbering quotient theorem.

## Classification rule

`KNOWN` means an exact published theorem, or a stated direct consequence whose published inputs and deduction are explicitly identified. `NEW_CANDIDATE` means no exact precedent was found in the specified searches but no priority claim is made. `CORRECTS_PUBLISHED_STATEMENT` requires a verified published statement and a proved correction, kept in CORRECTIONS_FOR_AUTHORS.md. `UNRESOLVED` is retained when comparisons or source access remain incomplete. Historical novelty labels are never inherited automatically.

## Paper records

The dated query logs, exact source locators, byte hashes and comparisons from each mathematical worker will be appended here before the next checkpoint.

## 2026-11-23T01:24:06.570296+00:00 — broader novelty and neighboring-work searches

Queries (strong search): `site:arxiv.org integral weak Lefschetz crystalline counterexample`; `site:hexagonmath.org Grothendieck crystalline Lefschetz` (past365days); `site:eccc.weizmann.ac.il crystalline cohomology Lefschetz`; `OpenAI mathematical research crystalline cohomology Barsotti Tate` (past365days).

Results: Hexagon exact benchmark now accessible as versioned page https://hexagonmath.org/2611.00789v1; it is an exposition of Alpöge’s proof sketch of a rational Frobenius eigenvalue bound, not an integral torsion comparison. ECCC’s crystalline-cohomology index contains Mittmann–Saxena–Scheiblechner TR12-014, a Witt-Jacobian criterion for algebraic independence; no directly matching Lefschetz theorem was returned. OpenAI’s primary math catalogue https://github.com/openai/math/blob/main/overview.tex lists rational crystalline cycle results and other number-theory preprints; these are leads, not adopted theorems. Follow-up queries target exact overlap. An arXiv lead 2603.12407 on crystalline classes in the 1-motivic category was returned but is not used until read. No search result settles priority.

## Current topic logs

The full dated logs are in audit/paper1/LITERATURE.md, audit/paper2/ (source and gate records), and audit/papers3_4/LITERATURE.md. SOURCES.tsv normalizes citations, source hashes and pages actually used. These source files are not copied into the deliverable.

### 2026-11-23: OpenAI rationality preprint, direct inspection

Opened the primary October7 PDF and read pp1–3. Theorem1.1 explicitly concerns rational Hodge/divisor pairings after good reduction, with crystalline realization after inverting p and extension to C_w. Its stated Serre–Tate/local-Shimura ingredients are relevant context for lifting, but supply no integral weak-Lefschetz saturation or finite-level character theorem here. The proof of that preprint was not audited, and it is not used as an input. Exact URL/hash/pages are in SOURCES.tsv.

## Further paper source audits, 2026-11-23T03:20:36.305351+00:00

Detailed dated searches and exact comparisons: audit/paper6/LITERATURE.md (principally polarized and ordinary abelian surfaces), audit/paper7/LITERATURE.md (crystals and stratifications), audit/paper8/LITERATURE.md (co-Lie obstruction). No absence-of-search-result is treated as proof of priority.

## Weak-formal site: dated source comparison (2026-11-23)

Date: 2026-11-23. Root, GPT-6 Astra Pro; effort not exposed. Bounded searches do not establish priority.

Main status: the general failure of a dagger infinitesimal structural-sheaf comparison is known in another convention, Arabia-Mebkhout2010 Theorem8.6 and Corollary8.11. The precise vanishing statements for the flat nilpotent-test site, and the general proper criterion, were not located in these searches. They are presented as the precise results proved here, with no priority claim. The finite-level proper input is Ogus1975 Corollary4.7; the integral MW independence is explicitly known from Ertl-Sprang2018.

Queries used online: `"Grothendieck" "weak formal" infinitesimal cohomology`; `"weak formal" "cohomology" "multiplicative"`; `site:hexagonmath.org "Monsky"`; `site:eccc.weizmann.ac.il "Monsky"`; `"weak formal" "infinitesimal site" cohomology`; `"infinitesimal" "Monsky-Washnitzer" "Grothendieck"`; `"integral comparison" "Ertl" "64" "72"`. Author pages, journal listings, arXiv versions and primary PDFs were followed. The general queries found Meredith, Ogus, Zhang, Illusie2025 and Arabia-Mebkhout2010. Hexagon and ECCC yielded no matching theorem in returned results; this is not an exhaustive index assertion.

The Arabia-Mebkhout lead materially changed the context paragraph: their Definition3.1 requires reduction exactly equal to the open, while the manuscript site also includes nilpotent thickening ideals modulo p. Their coefficient sheaf is rational. Both distinctions are explicit in the paper. Their nonzero affine-space class is credited, not repeated as a new failure result.

Zhang2019 was read at the definitions, universal-enlargement example and final comparison. Its enlargements with arbitrary special maps and analytic B[1/p] coefficients do not answer either the integral sheaf calculation or its later tensor product with K here. Illusie2025 Section3pp834-835 supplies recent crystalline/de Rham-stack context, with divided powers; it is not a theorem about this ordinary weak-formal site. No relevant AI-laboratory result was identified in the returned targeted searches.

Each downloaded primary source and the exact pages used are recorded in sources.tsv, with SHA-256. No source copy is included in a deliverable archive.



## Lifting and mixed-polarization additions (23 November 2026)

The full topic logs are audit/paper13/LITERATURE.md and audit/paper10/LITERATURE.md. The lifting counterexample phenomenon is explicitly attributed to Bhatt–Morrow–Scholze; Ogus and Li–Liu supply known comparison inputs. Recent Zou/OpenAI items are contextual only. Mixed polarization uses exact integral Oda and theta-group descent inputs; its remaining determinant problem is not claimed solved. Exact checked passages and hashes are in SOURCES.tsv.


## Divided powers from two rules

The exact two-axiom equivalence is known in Stacks23.5.3/23.5.4, Tags07GS/0H87. The full primary passages and chapter PDF pp10–11 were checked after a frozen author derivation. It is classified as known background, with no new standalone paper. The attachment's inline integer claim is corrected to a p-local scalar; the main theorem is unchanged. See audit/pd_pi/LITERATURE.md and residue_check.md.


## Even thin systems: strengthened supersingular theorem

Recorded 2026-11-23T05:52:38.655757+00:00. The proof now treats every even first degree m ≥ 6 in bidegree (m,3), including 8 and 10. The fixed-system supersingular full and relative ranks are 3m−2; for an ordinary first factor the full rank is 3m−1 and the relative rank is 3m−2, uniformly in the ordinary parameter.

Targeted searches before incorporation used the exact queries `"supersingular elliptic" "p-rank" "product" curves characteristic 2`; `"Cartier" "bidegree" "elliptic" "rank"`; `"p-rank" "linear system" "elliptic curves" product`; `"Cartier" "supersingular" "3m" curves`; and `"generic" "p-rank" "abelian surface"`. They returned background on superspecial ranks, special low-genus families, and ordinary Frobenius pushforwards; no exact fixed thin-system result was identified. Secondary aggregators surfaced but were not used as mathematical sources.

A further check used `"supersingular" "Cartier" "elliptic curves" "product" p-rank` restricted to arXiv; `"p-rank" "product of elliptic curves"`; and `"Cartier" "elliptic" "p-rank"` restricted respectively to Hexagon and ECCC. The results again included the already checked Chang et al. (2026) paper on double covers in characteristic greater than two (https://doi.org/10.1017/nmj.2026.10107), and papers on endomorphism rings and ambient abelian-surface p-ranks. None returned the exact thin-system theorem. No new mathematical input was imported from these results, and absence of a search match is not a priority claim.

The precise inputs remain the primary Cartier, Oda and Tate passages recorded in the original Paper 11 source audit. The new all-even proof is a direct kernel-bundle and residue computation, with its full separate reconstruction, comparison and finite corroboration recorded under audit/root_post_checkpoint06.


# Simply connected smooth proper lifts: exact known scope

Date: 2026-11-23. This record concerns thm:DE-simply-connected-convergent and cor:DE-BT-constant, not the unqualified simply-connected-isocrystal conjecture.

## Statement-first work and comparison

The root author's entire statement-led derivation was frozen at 05:54:27.929333 UTC, SHA-256 20059329929ce665dc88864cb915455ff0632138214df4d2eac5348075c1dcbe, before opening the attached proofs or the primary passages used here. Related crystalline background exposure is disclosed in that record. This is an author derivation and targeted comparison, not a separate proof-unseen worker certificate.

After freezing, both complete attached proofs in D.tex, lines 1323–1368, were read. The argument is correct with an actual smooth proper algebraic lift over W(k), a specified embedding of its fraction field into C, and a connected topologically simply connected complex fibre. Proper GAGA algebraizes the convergent connection, analytic horizontal sections trivialize it, and horizontal sections descend by flat base change. Frobenius becomes a semilinear operator on the constant coefficient space. No rational point over k is assumed. A closed point with finite residue extension supplies an integral Dieudonne lattice; finite Galois intersection and etale descent produce an F,V-stable lattice over W(k). Perfect-field Dieudonne theory realizes it by a p-divisible group. Rational crystalline full faithfulness then lifts the isocrystal isomorphism to a quasi-isogeny; clearing denominators gives an isogeny over the quasi-compact base.

The independently written author derivation instead obtains the ground-field lattice through Weil restriction and the trace idempotent. Both arguments permit division by the residue extension degree in the fraction field, even when that degree is divisible by p. The lattice step cannot be omitted merely because the underlying isocrystal is constant.

## Primary literature and exact credit

Tsuzuki, N. (2017). Constancy of Newton polygons of F-isocrystals on Abelian varieties and isotriviality of families of curves. arXiv:1704.00856v3, Remark 1.7(1), p. 4. https://arxiv.org/pdf/1704.00856 . The remark already states constancy, with and without Frobenius, over arbitrary perfect ground fields for a projective smooth lift whose geometric generic etale fundamental group is trivial. Its given mechanism is rigid/complex GAGA and characteristic-zero monodromy. The present topologically simply connected hypothesis implies the needed monodromy triviality directly. Replacing projective by proper uses the corresponding proper GAGA theorem; this is a standard consequence, not a new constancy theorem. Entire introduction pp. 1–4 read. Published version: Journal of the Institute of Mathematics of Jussieu, 20(2) (2021), 587–625, https://doi.org/10.1017/S1474748019000276 ; online publication was 14 May 2019. Exact remark locator here refers to the opened 2017 preprint, not an unverified journal renumbering.

Esnault, H., & Shiho, A. (2018). Convergent isocrystals on simply connected varieties. Annales de l'Institut Fourier, 68(5), 2109–2148. https://www.numdam.org/item/AIF_2018__68_5_2109_0.pdf . Read the introduction pp. 2109–2113, crystalline realizations through (1.13), pp. 2113–2117, and convergent realizations/full faithfulness (1.24)–(1.26), pp. 2120–2122, with their relevant explanations. The paper's standing algebraically closed hypothesis is not silently extended. Tsuzuki's arbitrary-perfect-field statement and the perfect-field realization formalism cover that scope. This source is not cited as proving the attached proper-lift theorem verbatim.

de Jong, A. J. (1995). Crystalline Dieudonne module theory via formal and rigid geometry. Publications Mathematiques de l'IHES, 82, 5–96. https://www.numdam.org/item/PMIHES_1995__82__5_0.pdf . Read the whole used Chapter 5, pp. 50–67: Theorem 5.1.1, Corollary 5.1.2 and equation (5.1.2.1), its reduction, rigid construction, point criterion, and gluing proof. This is the rational full-faithfulness input on finite-type schemes over a perfect field. Read Theorem 4.1.1 and the start of section 4.2, p. 36, for the perfect-field essential image; no claim to have reread the entire earlier chapter is made. The convergent realization is discussed at pp. 50–51 and section 5.3, pp. 53–55.

de Jong, A. J. (1998). Erratum to Crystalline Dieudonne module theory via formal and rigid geometry. Publications Mathematiques de l'IHES, 87, 175. https://www.numdam.org/item/PMIHES_1998__87__175_0.pdf . Entire one-page correction read, including its Artin–Rees argument and the corrected beta_n construction. It repairs Lemma 7.1.13.1; it does not retract the used Corollary 5.1.2. The existing published correction is credited, not announced as a new finding.

The Stacks Project, Tags 088C and 0883, Proposition 30.25.4 and Lemma 30.24.1: both entire statements/proofs were opened and read for proper formal GAGA and full faithfulness. These give an alternative algebraization route using a coherent formal lattice and its principal-parts connection; no projectivity assumption is needed there. Ogus's original 1990 chapter landing page and abstract were accessed, but its full text was not available through that page, so no full-source-read claim is made. The initially opened adjacent chapter was irrelevant and unused.

## Search record and disposition

The primary title/DOI and author-page searches led to Tsuzuki's exact projective-lift predecessor. Follow-up search on 2026-11-23 used: (1) "convergent isocrystal" "projective smooth lift" Tsuzuki; (2) "simply connected" isocrystal lift site:hexagonmath.org; (3) "Constancy of Newton polygons" Tsuzuki 2021 587 625. The publisher confirms the 2021 volume and the 2019 online date. The indexed Hexagon search supplied no exact new match. Search snippets and ResearchGate were leads only, not mathematical inputs. D'Addezio's later abelian-variety slope-constancy result appeared in search, but is neither needed nor treated as a constancy-of-objects theorem here.

Disposition: KNOWN_CONSEQUENCE_WITH_EXACT_SCOPE. Both mathematical source rows pass the author/source comparison. No new paper, no priority claim, and no independent-worker credit are assigned. The archive quotation remark remains outside this closure, because its manuscript image was not newly checked as part of this audit.


## Primitive functions in the ramification graph — 2026-11-23

New searches used (1) "finite flat" "primitive elements" "ramification" "p-divisible"; (2) "torsion" "inertial type" "formal groups" ramification; and then stronger primary-source queries (3) "Primitively generated Hopf orders" arxiv; (4) "finite" "primitively generated" Hopf algebra "dimension" p; (5) "height two" "torsion" "inertial type" ramification. The first broad search supplied mostly unrelated results and was not treated as evidence of absence. The stronger search found Alan Koch's arXiv1509.07393 primary text. Its complete sections2.1–2.2, pp3–4, explicitly identify the primitive module, its p-semilinear presentation and the formula rank(H)=p^rank Prim(H). The full relevant passage was read after the separate worker had already frozen its elementary proof. That lemma is therefore classified as known and cited as such; no novelty is inferred from its independent reconstruction. The paper retains the short proof to make the graph argument self-contained.

The new application rescales unequal-type two-slope torsion graphs and counts their primitive weights; its necessary configurations are a further reduction of the separate reconstruction route. It neither changes the status of the existing authored upper theorem nor constructs a comparison in the residual families. The exact three-family gate remains an independent-proof completion gate. No theorem on general Hopf orders is used from Koch. A secondary search result and publisher contents metadata were leads only; the mathematical source is the opened primary preprint, with its hash and read pages in SOURCES.tsv.


## Primitive odd polarization ranks — 2026-11-23

# Literature and credit audit: primitive odd polarization ranks

## Scope and status

The paper covers the 21 exact source statements identified in crosswalk.tsv. It does not recertify the adjacent full-image theorem, a common wall, Lang-cover connectedness, or a monodromy group. The unconditional geometric rank theorem concerns fixed nonordinary abelian surfaces in characteristic two, with an ample globally generated line of type (1, ell), for ell = 3, 5, 7, 11, 13, 17. The arbitrary-odd-prime statement is conditional on generic dual Cartier rank ell−1. Global generation is never inferred merely from the polarization type.

## Known inputs and deductions

Grothendieck's desired eventual positivity is directly read in cote4 §8.5.8, archive sheets7–8 (PDF8–9). The paper gives exact ranks for specified primitive systems; it does not identify them with all large multiples of a principal polarization.

The Cartier coefficient formula, multiplicativity and duality are classical (Illusie1979, §0(2.1.4)–(2.1.13), pp514–515). Oda1969 supplies the coherent/Dieudonné p-rank identification at Propositions3.18 and3.22–3.24, pp89,99–101. The coherent divisor sequence and universal Euler map are derived in the paper.

Sun2006, Definition3.1, Lemmas3.2–3.5 and Theorem3.6, pp5–9, supplies the canonical Frobenius filtration. All these proofs were read. The paper's surface slope-stability proof uses the unipotent filtration and the integer equation 4 chi(Q) = rank(Q) chi(L), including zero-dimensional defects. It is presented as a consequence of classical Frobenius structure, not as a newly discovered general stability theorem. A Mukai1978 primary download was blocked; no assertion about the exact scope of Mukai's theorem is used. Gross, Kaur, Ulirsch and Werner2026, introduction/TheoremA, is explicitly characteristic zero and is not imported for this characteristic-two assertion.

EGM, Theorem8.10 and Corollary8.11, pp116–117, proves the exact theta descent used here. Proposition8.19, Corollary8.20, Lemma8.24 and Theorem8.28, pp119–123, supply theta structure/representations. Full cited proofs were read. The ample-surface cohomology citation is Theorems9.11 and9.14, pp131–133, with their intervening proof; the unrelated Corollary7.17 locator was removed during the exact audit. Kleiman2005, Theorem6.3, pp52–54, with full supporting Lemmas6.5–6.6, pp54–56, gives numerical equivalence up to torsion. EGM Corollaries7.23/7.25, pp106–107, removes that torsion. These exact steps support the rank-four evaluation proof.

Prime-degree Severi–Brauer incompressibility is KNOWN, not new. Karpenko's updated9July2011 author version (original18April2009), Lemmas2.21/2.23 and Corollaries2.22/2.24, pp9–10, was read in full and visually inspected. The manuscript gives the complete elementary prime-degree diagonal-trace specialization. The Heisenberg dominance argument is a consequence of this known input, by an explicit cyclic division twist. Birationality then follows from scheme-theoretic linear fibres. The maximal-Pfaffian gcd and Euler-gradient arguments are proved separately; no wall-meeting assertion follows from them.

Catanese–Sernesi, arXiv2212.14877v1, introductory Theorems0.1/0.2, pp1–2, concerns the singular-divisor discriminant for complex type(1,3) surfaces. It is compared only as neighboring Heisenberg/Hesse geometry. The characteristic-two Fermat cubic here is a Frobenius nonbijectivity locus.

## Exact computation

The universal six-prime coefficient theorem is checked by a new memoized Pfaffian recurrence, written and frozen before old primitive code was read. All360 nonempty coefficient supports have symbolic monomial witnesses. The old two perfect-matching programs were then read in full and rerun; all counts and all255 prime17 full witnesses agree. Original working copies remain outside deliverables/audit. Supplementary multiplication-minor and finite-field probes were not used or recertified. No finite list of primes is extrapolated.

## Bounded search and recent context

Searches used both search systems and combinations of Heisenberg, Cartier, primitive polarization, abelian surface, Frobenius direct image, odd Euler characteristic, Pfaffian, birational radical and the prime17 support calculation. Exact Heisenberg/Cartier/primitive and Pfaffian/seventeen searches did not identify an exact primary statement of the fixed-system six-prime formula in the results reviewed. EGM and other general Heisenberg references were found. arXiv, author pages (Karpenko, van der Geer, Sernesi), journal sources, Hexagon and ECCC were consulted. Hexagon homepage/advanced-search pages were opened; direct query URLs failed in the retrieval tool, and indexed site-restricted queries gave no exact match in the bounded results. This limitation is recorded rather than treated as a comprehensive absence claim.

ECCC TR26-287 by Karthik Sheshadri was opened: its introduction, Theorems1.1/1.2 and3.1, and AI declaration concern odd-characteristic permanent/Pfaffian complexity, not primitive Cartier ranks. It is search context only and no theorem is imported. Its reference led to the primary OpenAI24September2026 preprint; that preprint's introduction, Theorem1.1 and §1.2, pp2–5, were read. The paper narrowly cites its characteristic-two matrix geometry as AI-laboratory context. Zou2026, introductory TheoremsA–C and acknowledgement/declaration, is neighboring AI-assisted work on quasi-F-splitting/crystalline slopes; no theorem is used.

The exact rank formula, universal support certificates and geometric application were not matched as a single prior theorem in this bounded search. This is not evidence of priority. The known Frobenius, theta and incompressibility results remain credited individually, and the all-odd-prime dual-rank problem remains open.

## Retrieval limits

An ICTP Kleiman mirror returned503; the exact arXiv primary version succeeded. Mukai's Project Euclid download returned an HTML block; it was not treated as a PDF or read proof. Karpenko's1999 paper was downloaded as a possible context source but was not read or used. Hashes, exact passages and read scopes for successful sources actually used are in sources.tsv; source-download records retain failures separately.

## Integral infinitesimal comparison and determinant duality

# E3/R10 literature conclusion

The integral no-PD infinitesimal/étale comparison is known. Ogus (1975), Corollary4.7 p314 and Theorem4.9, Remark4.10, Corollary4.11 p315, explicitly provide the finite-level and integral statements, including torsion, under the printed global smooth ambient-embedding hypothesis. The arbitrary smooth proper scope is verified here by the attached local embedding and flat coefficient-induction argument, expanded in full_verification.md. It is also explicitly stated in Grammatica, arXiv2507.08568v2, Theorems3.3.2–3.3.3 pp22–24. No novelty or priority claim is appropriate.

The stratifying/coherent-stable/F_p-étale comparison is the characteristic-p version of the same known theory. Its scalar-extension step and finiteness appear in the Artin–Schreier argument, including Stacks59.63.2 and59.63.6. Vanishing above the dimension follows by coefficient induction and Mittag–Leffler. Grothendieck1968§7.1 p351 already publishes the ordinary abelian example; ordinarity is unnecessary for the stronger stated vanishing. His §§4.1–4.2 pp331–332 distinguish the sites precisely, and §§5.1–5.2 pp335–339 give the local completed Čech calculation.

The original archive cote7 image17 (printed sheet16) was visually inspected, together with context images14–18. The correction phrase and vanishing formula are confirmed. Modern PD crystalline cohomology is not being substituted for the old no-PD site.

Searches on23November2026 used both general search indexes and covered Numdam/journal records, arXiv, author pages at Berkeley and Strasbourg, Hexagon, and ECCC. Queries included the exact Ogus title, infinitesimal cohomology/étale/stable-part terms, Grammatica's title, and site-restricted Hexagon/ECCC searches. The primary journal PDF and current arXivv2 metadata were opened. The author pages identify the relevant works but are not used as proof sources. No additional exact comparison theorem was returned from the bounded Hexagon or ECCC searches; that limited negative search result is not evidence of priority. Raw lookup output remains outside deliverables under external/infinitesimal_etale.

The recent preprint's Remark4.6 p29 states its final fixed-point/scalar-extension consequences over a perfect field too broadly. A complete Spec(F_p) counterexample and minimal algebraically-closed repair are in CORRECTIONS_FOR_AUTHORS_PROPOSED.md, pending parent inspection/adoption. This does not affect the assigned theorem, whose algebraic-closure hypothesis is retained. The full recent descent proof chain outside §3.3 is not claimed separately checked.

Prior Ogus primary exposure is disclosed in the frozen author record. These are exact source checks, full targeted verifications and known-result closures, not independent proof-unseen certifications. No new paper is proposed.

# Literature and scope: Hasse and ordinary determinant duality

The Hasse theorem is known. Bijakowski (2018), Theorem 2.1.4, explicitly proves duality over arbitrary characteristic-p schemes, including nonreduced bases. Section 2.1, including its full proof, was read. Fargues (2011), Proposition 2, is the earlier formal-base version; its precise formal-base hypotheses and complete proof were followed back in the primary author manuscript. Paper 14 identifies the abelian determinant comparison with the specified cup–trace normalization and writes a complete matrix proof. No general Hasse-duality novelty is claimed.

Grothendieck's cote 9 supplies the normalized ordinary determinant construction and the inverse-duality formula, together with a question about the ordinary de Rham comparison. The original sheets 21 and 28 were visually inspected. The paper does not attribute a sign-free product formula to Grothendieck. The sign epsilon_g and product factor (-1)^(gh) are fixed by the stated positive Poincare biduality, translation convention and Hodge-first exterior order. This is a convention-specific completion and exposition, with no priority claim.

The integral construction and equality of its units are proved in full. Dwork–Ogus Theorem 1.4 and its following paragraph lift all morphisms and polarizations canonically for every prime. EGM Theorem 12.18 is invoked only on the characteristic-zero generic fibre, with coefficient prime p, so its prime-to-characteristic hypothesis is satisfied. The unfinished crystalline aside following that theorem is not used. EGM 9.11 proves the Euler-characteristic/degree polynomial; comparing monic squares eliminates the possible sign even over Q_2. The proof also handles polarizations whose degrees are divisible by p before reduction.

Ogus (1979), Section 6, printed page 59, gives the general abelian top crystalline exterior/trace identity and Frobenius factor p^g. The surrounding later supersingular theorem does not restrict that preceding statement. Paper 14 extends the trace scalar over the universal formal base using horizontality, torsion-free differentials and the zero-parameter W fibre. Its line-isomorphism argument uses finite-free H1, cup–trace, fibre exterior cohomology and Nakayama; it does not infer arbitrary relative cohomology flatness merely from a Hodge-degeneration assertion.

Maillot–Roessler's determinant-bundle theorem and OpenAI's 2026 rational trace preprint are neighboring context only. Their exact introductory scopes were opened and read; no proof input or full-proof verification of either is claimed here. Bounded arXiv, journal, author-site, Hexagon and ECCC searches did not return an exact later normalized-alpha/sign-pair theorem. This negative search observation is not priority evidence and does not claim an exhaustive literature search. Primary URLs, hashes, exact pages and read scopes are in sources.tsv.

The source-exposed author and root full comparisons pass. The subsequent complete separate reconstruction and full root comparison of the two main statements are recorded in the dated continuation below. The current records cover exactly the two historical statement IDs mapped in crosswalk.tsv and their stated supporting arguments, not the surrounding D/E families.


## 2026-11-23 07:29 UTC — Hasse and ordinary determinant reconstruction sources

The complete separate H/D reconstruction was compared. BBM1982 Proposition2.5.2, Corollary2.5.5 and site1.1.1 were read at their exact scope, including all primes. Katz1981 Theorem2.1 and canonical-lift section4.5, EGAIII1 Theorems5.4.1/5.4.5, and Milne1986 Theorem13.3 were checked directly. The alternative Poincare2lambda proof changes the verification route, not the prior literature classification: general-base Hasse duality is known from Bijakowski; no priority assertion is added for the ordinary convention-specific calculation. Exact URLs, hashes or download failure, and read pages are in SOURCES.tsv and the reconstruction manifest.

## 2026-11-23 07:30--07:43 UTC — Minimal cyclotomic character index

Queries: Bondarko finite flat group schemes ramification e p-1 torsion crystalline representations bound; height two Barsotti Tate torsion inertia character ramification p-1 Lubin Tate; site:arxiv.org inertia torsion height two; site:hexagonmath.org Barsotti Tate torsion ramification; site:eccc.weizmann.ac.il Barsotti Tate ramification; Conrad finite group schemes low ramification. Primary results reopened/identified include Bondarko2006 TheoremA and finite reduction criteria, Hattori2008 tame ramification characters, Liu potentially good reduction, and Conrad low-ramification finite-group models. Their stated extension/model/ramification conclusions do not assert this exact special-character index. Hexagon results were neighboring or unrelated; ECCC returned unrelated uses of ramification. No exhaustive absence or priority claim is inferred. Lubin--Tate1965 Lemma1/Theorem1 pp381--382 and Theorem2(b)--(d) pp383--384 were fully reread from the original scan; its SHA is b1d5502619d8f182861bef3b5f66b351a2274ed35afa445416a26aed8dae04f0, URL https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/lubin-tate.pdf . The construction applies their finite-residue theorem before base change and proves its own residual norm-one image. The original corpus already states the exact values as B61/B73; this is current verification, not a newly discovered corpus claim.


## 2026-11-23 — Primitive monodromy source audit and infinite-family extension

# Primitive monodromy: exact literature and scope assessment

Recorded 23 November 2026. This is a bounded source assessment, not a priority claim. Exact URLs, SHA256 digests, pages and read scopes are in `sources.tsv`; query families and negative-search limitations are in `search_log.tsv`.

## The archival question

The original Grothendieck cote4 PDF image12 is archive/manuscript sheet11, Section8.6. The short phrase “est-elle égale à Aut(V) tout entier?” was checked visually against the handwritten image. Its setting is hypersurfaces of a fixed projective embedding. The paper explains the primitive complete-system question as a smaller related setting. The degree-two elliptic-fibre examples are not very ample and do not refute an eventual statement about powers of one fixed embedding line.

## Known inputs, with exact scope

1. Illusie1979, Section0 (2.1.4)–(2.1.13), pp514–515, supplies the Cartier product/trace formula. Those passages and the neighboring proof through p517 were fully read earlier; the current use is the local perfect pairing and alternating specialization when the top Hasse scalar vanishes.
2. Sun2006v2, Definition3.1, Lemmas3.2–3.5 and Theorem3.6, pp5–9, supplies the higher-dimensional canonical Frobenius filtration. The complete proof was read for Paper12. The manuscript proves the needed surface slope stability itself, including saturation and zero-dimensional double-dual defects; it does not import a curve-only theorem as a surface statement.
3. Edixhoven–van der Geer–Moonen, Theorem8.10 and Corollary8.11, pp116–117, provide exact theta descent; Proposition8.19, Corollary8.20, Lemma8.24 and Theorem8.28, pp119–123, supply the finite theta representation; Theorems9.11 and9.14, pp131–133, supply Riemann–Roch and ample vanishing. All used statements and proofs were fully read during the earlier Papers10/12 audit. Their reuse is not recorded as a newly independent source reading.
4. Milne2008, TheoremI.5.5 p23 and PropositionI.8.4/RemarkI.8.5 pp35–36, were opened on the author's primary site and read in full, then checked in the downloaded PDF. They justify the degree-zero addition identity and polarization matrix. Nearby Example8.3 and the unfinished converse in Proposition8.1 are not inputs.
5. Stacks59.55.1/59.55.2 were read in full. Finite higher direct-image vanishing holds for arbitrary abelian étale sheaves, with no requirement that the coefficient prime be invertible. Together with the full Artin–Schreier sequence and Lemmas59.63.1–3, they imply the natural wild-double-cover branch permutation module. The numerical dimension is a special Deuring–Shafarevich case; the paper proves the actual functorial representation, not just its rank.
6. Stacks53.13.3–5 and53.13.8 were read in full. Relative-Frobenius factorization of a zero-differential curve linear series is known. The explicit descended degree-n line, its complete section space and its role as the branch-label series are proved in the paper. Stacks53.12.1 supplies the exact ramification/differential criterion.
7. Full symmetric monodromy of the reduced divisors in a complete elliptic series follows from the classical Abel-map fibre: the ordered sum fibre is an elliptic product, and deleting diagonals gives a connected symmetric-group torsor. The paper includes this complete argument and does not claim a new general theorem about Abel maps.

## Main-result classification

The fixed type(1,3) full-image result is proved for every fixed nonordinary abelian surface with explicit global generation. Its exact published match was not identified by the bounded search. Neither absence of a search hit nor the new presentation is evidence of priority.

The earlier supplied explicit counterexamples were restricted to n=5,7,11,13,17 and gave an image inclusion in S_n and lower component bounds using rank certificates. The authored strengthening proves, for the exact lines O(mV+H+Gamma) on the fixed supersingular E² and every odd n=2m+1>=3, a complete elliptic branch series, rank n-1, exact image S_n and exact component degrees binomial(n,j). This removes the finite-prime rank dependency only in that explicit family. It does not solve generic dual-Cartier rank or full-image questions for unrelated primitive polarizations.

No exact earlier all-odd statement was identified in searches of arXiv, author and journal sites, Hexagon and ECCC. The Frobenius factorization, theta descent, Artin–Schreier module calculation and ordered-divisor mechanism have explicit classical antecedents. The manuscript makes no priority claim and gives full proofs of its application.

## Neighboring literature, not proof inputs

Catanese–Sernesi2022v1, Introduction Theorems0.1–0.2 pp1–2 and Section1 p3, concerns complex type(1,3) singular-divisor discriminants and Hesse geometry. It does not identify the characteristic-two relative-Frobenius Fermat locus. The exact introduction/context was read.

Zou2026, Introduction including Section1.3, TheoremsA–C and declarations, is an opened primary AI-assisted work on quasi-F-splitting and crystalline slopes of primitive symplectic varieties. It is cited as neighboring recent context; none of its results enters a proof.

Search hits about characteristic-not-two bielliptic Picard curves, automorphism groups in characteristic two, elliptic scrolls, generalized Kummer surfaces and AI work on complex abelian sixfold reflection groups were screened as different questions. Unopened hits are not cited as mathematical evidence. ECCC searches yielded no relevant exact result; this is a limited negative search, not exhaustive coverage.

## Verification distinction

The author had prior related rank and Cartier exposure, declared in `exposure_start.json`. Its original A4 statement-led attempt was frozen before the selected old A4 proofs/programs were opened, but it is not called pristine. The all-odd argument was developed and frozen after source exposure. A separate proof-unseen worker reconstructed the original packet completely relative to its explicitly allowed inputs; that full proof and program comparison passed. The all-odd reconstruction was subsequently frozen, all443 lines and its exposure/source/failed-route records were fully read, and full comparison passed; see all_odd_clean_comparison.json. It retains only the type(1,3) smoothness base case and earlier natural module/coherent comparison, while proving all remaining all-odd steps. Root has reported a complete targeted reading of the manuscript, including the all-odd mechanism, with no mathematical defect.


## 2026-11-23 — First-wild point-field companions

# Primary literature and exact use in the B82–B90 audit

## Colmez: ramification over perfect residue fields

Colmez, P. (n.d.). *Corps locaux, notes du cours de M2*. Author course notes. https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf

The primary author PDF was downloaded on 2026-11-23 at07:46:45.764162UTC. Its SHA256 is33368619cb6ae74f085f3eeecd7d0d0d89e1d757110158389196084bba70ca44. The PDF and text extraction are retained only under external/B82_B90_ramification_worker/, outside the packaged audit.

Read scopes: p1 defines a local field as a field complete for a discrete valuation, without a finite-residue requirement. Section3, p13, assumes characteristic zero and perfect residue of characteristic p. Proposition3.7, pp14–15, including its complete two-divisibility norm-polynomial proof, gives the average formula for ramification indices in a finite Galois quotient. The preceding subgroup observation supplies lower-numbering compatibility. Theorem3.10, p15, and Proposition3.13(ii), p16, including their proofs, supply the Herbrand composition and upper-quotient compatibility used for the exact tables.

These hypotheses include the algebraically closed residue fields of B82/B85–B90 and the same perfect residue field of the abstract B87 coefficient lemma. No finite-residue class-field theorem or unexamined Hasse–Arf statement is imported. The fixed-coefficient lemmas, actual point-field stabilizers, matrix spaces, numerical tables and explicit cyclotomic examples are proved in the worker's frozen derivations. Colmez is an exact background source, not a source for the new local comparison conclusions. No priority claim is made.

## Cohen coefficient rings

The Stacks Project Authors. (2026). *The Cohen structure theorem*, Theorem10.160.8, Tag032A. https://stacks.math.columbia.edu/tag/032A

The primary page and displayed proof were opened and read before attempt02 was frozen. It provides existence of a coefficient ring in the complete local ring. For the perfect residue field used here this is W(k). The ensuing identification K=Frac(W(k))(mu_(p^2)) at the exact absolute index p(p-1) is proved locally by the cyclotomic Eisenstein polynomial and complete uniformizer expansion. The lower break N and its tame scaling to N^2 are also calculated locally; they are not claimed as conclusions of the Cohen theorem. The local HTML access hash is in sources.tsv.

## Retained mathematical inputs and boundaries

The formal universal-coordinate/Newton and descent-weight inputs were already independently reconstructed in audit/blind_ramification/attempt05 and attempt10, before original Paper2 exposure. Actual first-wild pattern inputs B77-square, B83-quotients and B84-first-wild are explicitly retained dependencies for the global dimension corollaries. Their ownership is separate; no new target-proof audit of B77/B83/B84 is claimed here. Addendum01 records the correction of attempt02's header to name B77 explicitly.

For each assigned auxiliary, the target statement and enclosing hypotheses were extracted before its new derivation. The author derivation and different-method computation were frozen before opening that target's old proof and original certificate. Prior original/public Paper2 exposure and incidental REGISTER provenance-remark exposure are preserved in initial_exposure.json. This is a same-model derivation and post-freeze source comparison, with no claim of different-model independence or human review.

## 2026-11-23, post-checkpoint09 residue and monodromy search

Root searched the web in general mathematical terms for alternating permutation factors and finite-field traces, Hasse--Witt monodromy of hypersurfaces, Entin monodromy of hyperplane sections in characteristic two, and alternating trace obstructions. Routine and stronger search engines were both used. Direct searches on ECCC and Hexagon for the target terms returned no exact matching theorem; the Hexagon request did not return usable content. These bounded negative results do not establish priority. Entin's author publication page, the primary arXiv v3 and journal metadata were opened. The complete primary pages6--11 were read, including Proposition3.1 and Theorem3. Journal metadata dates the volume2021(14), pp10409--10441, DOI10.1093/imrn/rnz120; online publication was2019. Stacks0BTN,09ZS and09ZL were read for the finite-part and henselian-pair arguments. Exact URLs, retrieved-file hashes and read scopes are in audit/root_post_checkpoint09/primary_source_metadata.json. No general hypersurface full-image theorem was accepted from search snippets.

Projective-space separate reconstruction primary searches and incidental snippet exposures are logged in audit/blind_residue_monodromy/pn_primary_exposure_manifest.md. Generic invertibility is treated as a classical framework result, not assigned priority. Exact higher full-group literature status remains unresolved.


# Literature status and bounded search

Recorded23November2026. This is a bounded comparison, not an assertion of priority.

The exact archive question is Grothendieck cote4, Section8.6, archive sheet11/PDFimage12. The full image was visually read. Katz1973 supplies the congruence and the stable/étale comparison. Sections1–2 and their proofs, printed pp403–409, were fully read; Theorem3.1 and Corollary3.2, printed pp410–411, were read, including the corollary proof. The entire later proof of Theorem3.1 was not re-audited. Entin's arXivv3 Proposition3.1 with proof, pp7–8, and Theorem3 with proof, pp9–11, were fully read. Their exact uses and geometric hypotheses are explicit in the manuscript. Stacks exact source scopes and hashes are in sources.tsv.

Queries executed in this author session included Katz's1973 congruence/Corollary3.2, his Princeton author repository, Entin's hyperplane-section monodromy/Proposition3.1, Stacks Bertini/connectedness/base-change/regularity, and the following wider phrases: smooth hypersurfaces every residue modulo characteristic point count Grothendieck monodromy; arXiv hypersurface point count residue density Hasse Witt monodromy; Hexagon hypersurface residues Frobenius; ECCC hypersurface point counts finite fields. Results included Katz's prime-to-p random-matrix monodromy, generalized Hasse–Witt computations, complex hypersurface monodromy, a recent Deligne-bound manuscript and finite-field algorithms. None of those snippets establishes the present finite-Fp relative trace theorem. No exact match for the improved explicit general-variety bound was identified. Absence of a search match is not evidence of novelty.

A later Poonen/Bucur–David–Feigon–Lalin context search returned an output truncated before it could be read; no factual conclusion or source citation is based on that unread output. The paper therefore does not compare its result to an unverified fixed-field asymptotic theorem.

The current results are classified as: classical stable-Frobenius, cohomology, incidence, finite-group and henselian ingredients with full proofs or exact primary citations; a fully proved general-variety combination and improved sufficient bound, with no priority claim; and a post-source all-node/characteristic-two plane application proved in full. The separate clean main reconstruction remains pending. Full-image and exact-rank classification gates are not closed by a trace theorem.

Recent context is the opened OpenAI Milne preprint, Theorem1.1 and Introduction pp1–3. It concerns rational specialized pairings for abelian varieties, not the varying finite-field trace system used here; it supplies no mathematical input.


## 2026-11-23, post-checkpoint10 — sharp projective residues and known matrix inputs

The complete all-prime cubic-plus-hyperplanes residue proof and its separate statement-only reconstruction have now been fully compared. This closes the sharp every-open threshold d=n+2 for projective n-space, n>=2, independently of the still-open higher full-image classification. The earlier statement in this log that the general-variety reconstruction was pending is superseded by its full comparison at09:08:52UTC; the sharp projective comparison was recorded at09:17:24UTC. Both occur after the immutable Review06 snapshot.

The primary Adolphson–Sperber2016 author PDF was opened and pp1–4, including the complete Section2 proof, and referencesp7 were read. Theorem2.3p2 and Proposition2.11p3 contain the exact generic Hasse–Witt invertibility and determinant constant-term-one result. The current independent derivation is therefore a verification of known mathematics. Its duplicate public proof is removed, and the exact result is cited. Published metadata is Finite Fields and Their Applications41,55–63, DOI10.1016/j.ffa.2016.05.001. The authors credit Miller's earlier generic invertibility theorem; Miller1976 metadata was found at the primary publisher/archive, but its original proof has not yet been read, so no exact Miller theorem is adopted from a snippet.

Katz1972, Algebraic solutions of differential equations (p-curvature and the Hodge filtration), Inventiones Mathematicae18(1–2),1–118, DOI10.1007/BF01389714, was opened from his Princeton author site. The complete primary scan pages33–36 (PDFimages34–37) were visually read, including the smooth-hypersurface hypotheses, coherent exact sequence and Cech basis, Frobenius diagram, Algorithm2.3.7.14 and formula2.3.7.16. Its stated smooth formula is known; the manuscript gives the needed extension to singular ordinary boundary hypersurfaces. Exact hashes and read scopes are in SOURCES.tsv and audit/root_post_checkpoint10/projective_source_readings.json.

General-term arXiv, author/journal, Hexagon and ECCC searches were repeated for Hasse–Witt monodromy and hypersurface point-count residues. The results include Adolphson–Sperber2017 generalized Hasse–Witt matrices, Huang–Lian–Yau–Yu period relations, and Koblitz1975. Snippets concerning these neighboring topics are not treated as exact matches. The Koblitz primary comparison is being completed separately. No bounded negative search is evidence of priority. The opened OpenAI Milne2026 Theorem1.1 is context about rational specializations of Hodge pairings and supplies no mathematical input to finite-Fp trace variation.

# Koblitz (1975): bounded primary-source verification

## Result and recommended credit

The requested primary pages were read in text and as rendered page images. This is a literature and proof-scope check, not a new theorem reconstruction or a whole-paper proof audit. No public manuscript or global register was changed.

For P16, add one historical context sentence, without adding a counterexample theorem:

> Koblitz proved generic Hasse–Witt invertibility for complete intersections, but posed eventual invertibility of the relative Hasse–Witt quotient for an arbitrary fixed smooth projective ambient variety as a question (1975, Theorem 3 and II.§3); the residue-density argument here does not assume this relative invertibility.

The final clause describes the independently frozen general-X argument, not an assertion attributed to Koblitz. The historical wording does not assert that Koblitz’s question remains open today. Exact source locators for root inspection are Theorem 3, pp.142–144, and II.§3, p.151. The singular example at pp.148–149 and the bounded-degree smooth example at p.152 must not be conflated. No new failure-of-ordinarity claim should be inferred from this source check.

For P17, give established-result credit to the generic-invertibility and coefficient-formula inputs. Their precise locations and Koblitz’s earlier attributions are recorded in `koblitz_sources.json`. The packet-level claims about exact finite-group images and every-open residue distribution require their own proofs; this reading supplies no replacement for those gates.

## Scope of the negative search

I found no finite-\(\mathbf F_p\) full-image or every-open all-residue theorem in the requested proof reading plus the whole-paper text and theorem-heading scan. This is a bounded search result, not a priority claim or proof of absence from the wider literature. OCR can omit formulas. The requested pages were therefore also checked visually, and the substantial `GL` occurrence on p.192 was inspected separately; it is a semilinear basis argument. The regexes, hit pages, and numbered headings are preserved in `koblitz_scan.json`.

## Verification limits

The visible proofs of Theorems 1, 3, 4 and 6, the coefficient algorithm, Lemma 8, and the requested counterexample arguments were read. Earlier supporting Lemmas 1, 4, 5 and 6 were not read in full. Only the end of Lemma 7 occurs in the requested range. Theorem 5’s intervening p.146 was not read. Theorem 7 was inspected for statement scope, not proof-checked. Thus this record gives exact local proof-read coverage without claiming complete dependency closure.

The numerical lower bound in II.§2 was checked in the visible argument; I do not independently certify its printed asymptotic-equivalence notation from that lower-bound argument alone. This does not affect the recommended historical sentence.

No Miller paper or Dwork paper was newly opened. My earlier Katz reading stopped before the coefficient-formula corollary cited by Koblitz. The Miller, Dwork and Katz entries below therefore distinguish a verified attribution in Koblitz from direct verification of the cited original.

## Citation

Koblitz, N. (1975). *p-adic variation of the zeta-function over families of varieties defined over finite fields*. **Compositio Mathematica, 31**(2), 119–218. https://www.numdam.org/item/CM_1975__31_2_119_0/

Primary PDF: https://www.numdam.org/item/CM_1975__31_2_119_0.pdf

Numdam’s displayed BibTeX and RIS metadata list no DOI. No DOI was verified elsewhere. Source and audit hashes, page mapping, exposure chronology and all statement locators are in `koblitz_sources.json` and `koblitz_verification_freeze.json`.

Prepared by `/root/blind_lefschetz`, GPT-6 Astra Pro, effort not exposed. Same-model verification; no human verification.

## 2026-11-23, plane full-image extension search

Root searched general mathematical terms for ordinary plane-curve monodromy, characteristic-two plane-curve monodromy, abelian lifted-point wreath monodromy, and Hasse–Witt monodromy of plane curves. Results included Salter's complex plane-curve mapping-class and spin constraints, enumerative wreath-product monodromy in sparse polynomial problems, and sectional permutation monodromy. These are distinct statements from the finite-Fp ordinary cohomology image. The exact primary comparisons are continuing; unopened snippets are not citations or evidence of absence. The current plane proof uses its own full curve-torsor, purity and graph-generation arguments, with exact classical inputs. No priority claim is made. Higher-dimensional full images remain open.


## 2026-11-23, complete tame criterion and higher hypersurface follow-up

Root searches around09:54UTC used: “elliptic curves full p^n torsion ramification potentially good reduction tame exact bounds”; “site:arxiv.org elliptic curve rational torsion ramification semistability defect”; “site:hexagonmath.org elliptic torsion ramification”; and “site:eccc.weizmann.ac.il elliptic torsion ramification”. Repeated searches around10:20UTC used “site:eccc.weizmann.ac.il elliptic curve torsion ramification”, “site:hexagonmath.org elliptic full torsion ramification”, “elliptic curves full division fields minimal ramification semistability defect tame torsion”, and “Lozano Robledo Smith ramification full p power torsion supersingular elliptic author”. No exact ECCC/Hexagon match was returned; this is a bounded search outcome, not proof of absence or priority.

Opened primary records include Smith's arXiv1810.04809 author version; Lozano-Robledo's journal pages at https://ems.press/journals/rmi/articles/13573 and https://link.springer.com/article/10.1007/s40993-016-0040-z; and the author publication listing https://alozano.clas.uconn.edu/. Only metadata/abstract and reference context were read in the two Lozano-Robledo journal pages. The 2015 work constructs global division fields attaining the cyclotomic minimal index; it is a different existence scope from additive potentially good full torsion of specified defect. The 2016 article concerns ramification in potential supersingular division fields. Its proof is not newly audited here and no new correction claim is made. Smith2023 Theorem1.1p2 explicitly contains the basic good-supersingular full-division-field lower bound (p²-1)p^{2n-2}; root read its complete introductory statement and surrounding scope, with its valuation theorem already checked at the earlier recorded scope. The current tame theorems add exact defect, the s-dependent integral constraint and every-index local realizations. No claim of priority is made for the basic bound or valuation classification.

Exact deformation inputs: Carter–Strauch2021 Theorem2.1.2p437 and Proposition2.2.3p439 with proof throughp441; Drinfeld1974 Section1C pp564–565 and Propositions4.2–4.3 pp570–573, including the full level-ring proof; Katz1981 Theorem1.2.1p143 and proof pp144–146; Serre–Tate1968 Theorem1/Corollary4 pp493–494 and root's separate Theorem2/Corollaries2–3 pp496–498. Different workers' precise read scopes and primary PDF hashes are in SOURCES.tsv and the immutable manifests. Katz's correct DOI for this chapter is10.1007/BFb0090648; the previous bibliography suffix was corrected without changing the theorem used. Root additionally reread Ozeki–Yoshida2026 Proposition3.25pp21–22 and its proof in the retained primary version; its division-field upper-break bound is a separate statement. A fresh arXiv-abstract open failed, and is not recorded as successful source access.

The10:08UTC higher-image searches used “Hasse-Witt monodromy hypersurfaces”, “unit root monodromy hypersurface Katz”, “site:arxiv.org plane curves monodromy characteristic p ordinary”, and “site:hexagonmath.org monodromy hypersurface”. Results included Huang–Lian–Yau–Yu on Hasse–Witt matrices/unit roots/period integrals and Adolphson–Sperber generalized Hasse–Witt matrices. At that search only snippets/metadata were read; precise subsequent primary reading is recorded separately by the paper integrator. These searches do not prove the new finite-group conclusions or establish priority. The complete same-model independent p>=5 comparison is mathematical evidence, not literature evidence.


# Literature status for the higher hypersurface image theorem

The new public scope is full geometric and arithmetic `GL_h(F_p)` for `p >= 5, n >= 3, d >= n + 2`, together with the first-degree characteristic-three case. A bounded search did not locate an exact prior theorem at that scope. This is a search outcome, not a claim of novelty or priority.

The coefficient formula is Katz’s classical formula. Generic Hasse–Witt invertibility is explicitly known from Koblitz (with Miller attribution) and from Adolphson–Sperber’s normalized determinant theorem. Those inputs are separately credited in the manuscript and are not the full finite-image statement.

The strongest additional primary candidate opened was Huang, Lian, Yau, and Yu, *Hasse–Witt matrices, unit roots and period integrals*, published in *Mathematische Annalen* 387 (2023),145–173, DOI10.1007/s00208-022-02464-y. The 26-page author version was downloaded and hashed; complete read scope is pp1–12 and17–26. Its Corollary2.3 recovers coefficient formulas for toric hypersurfaces, Corollary2.8 p11 proves generic invertibility, and Theorem5.3 pp19–22 identifies unit-root Frobenius/connection limits under the hypotheses stated on pp17–19. These are meaningful neighboring results. None of those opened statements gives the finite geometric Fp Lang image determined here. The author-version page/statement locators are kept distinct from the journal pagination.

The follow-up included arXiv, journal and author pages, ECCC, and Hexagon queries. Exact query strings, limitations, candidate dispositions, read spans, URLs and SHA256 are in `literature_followup.json` and `sources.tsv`. No secondary snippet was accepted as a mathematical dependency. The scope of this record does not certify all of the neighboring paper, and no correction to its published statement is proposed.

The higher-prime proof is written in full using the already established cubic-boundary image, elementary averaging, explicit exterior coefficients, and a proved block-generation lemma. The characteristic-three proof gives an actual affine coefficient isomorphism and a connected Lang torsor. Independent-check status is tracked separately from literature status.

The separate higher-prime main reconstruction subsequently passed full root comparison (all739 frozen lines), recorded at `audit/root_post_checkpoint11/higher_prime_complete_main_comparison.json`. This changes check status, not the literature conclusion.



## Complete prime-to-p index: bounded primary comparison


The exact seven search strings, sources and access outcomes are in `bounded_literature.json`. This was a bounded search; it supports no priority claim. No new literature theorem enters the iteration proof.

Bondarko, M. V. (2006). The generic fibre of finite group schemes; a “finite wild” criterion for good reduction of Abelian varieties. *Izvestiya: Mathematics, 70*(4), 661–691. https://doi.org/10.1070/IM2006v070n04ABEH002323

Printed page 661, Theorems A–B, gives an almost-fullness bound for the generic-fibre functor on finite flat commutative group schemes. The primary publisher metadata/abstract and that exact first-page theorem text were read. The direct PDF requests failed as recorded; no new full-paper reading is claimed.

The existing precise Hattori and Smith comparisons remain at their previously recorded scopes. Their conclusions concern generic ramification-graded characters and elliptic division-field valuations, respectively. The new exact table instead concerns the least uniform truncation determining special descent characters in the stated full height-two filtration class, with actual lower examples at every permitted ramification index. This is a comparison of inspected statements, not an assertion that no earlier identical theorem exists.

Root read the full search/access manifest and comparison text at10:41UTC. The exact seven queries and access failures are preserved in audit/prime_to_p_iteration/ramification_worker/bounded_literature.json. No new primary theorem enters this iteration proof.

## 2026-11-23 CP13 bounded literature and primary updates

The following records merge owner/source verification; they do not claim a new integrator literature search.

### Early ramification and first wild index

The exact logarithmic representation is classical: Berger(2004), SectionII.1.2,p9. The worker read the44-page2002 arXiv author version; root separately read the37-page author version, including the displayed Sen criterion/example. Their distinct PDF hashes remain separate in SOURCES.tsv. The new write-up gives the actual finite-etale filtered Barsotti–Tate interpretation using Grothendieck cote9,sheets10–11/PDFimages11–12; root visually reread both complete archive pages. The defect-two example is a consequence of the earlier complete tame theorem. Milne2008 I.13p57 and I.17Theorem17.1/Remark17.2p70, the Edixhoven–van der Geer–Moonen draft5.20–5.27pp80–82, and retained Serre–Tate1968Theorem1p493 are credited only at the exact recorded scopes. No claim of new Sen theory, new Neron theory or priority is made.

The owner executed these bounded queries at 2026-11-23T11:34:29.614013+00:00:

- `"p-divisible" "p(p-1)" inertia`
- `"special" "character" "Bondarko" ramification`
- `"ordinary" "unramified" "p-torsion" "good reduction"`
- `"potentially ordinary" torsion "good reduction"`

Selected results were institutional metadata on finite-flat kernel/cokernel boundedness and Ozeki–Yoshida arXiv2609.06554 on first-level elliptic torsion fields; these were context, not new inputs for the full-filtration first-wild theorem. No exact match was identified in those selected results. This is bounded coverage, not absence or priority evidence. Full query/access scope: audit/early_ramification_clean/integration/bounded_literature.json. The first-wild proof retains exactly its previously verified I1–I4; no new literature theorem is inferred from reconciliation.

### Complete projective images

### Exact bounded literature comparison: all-prime hypersurface images

The new public scope is the complete finite geometric and arithmetic image on the Hasse–Witt fixed-vector local system of universal projective hypersurfaces, over every perfect field. The characteristic-two parity stabilizer and the characteristic-three modular extension are proved in full in the paper. No priority claim is made.

#### Exact inputs and known results

Katz's coefficient and point-count formulas, projective-space cohomology, Artin–Schreier, purity and the finite-cover point-existence argument remain credited at the exact locators already recorded for Paper17. Generic Hasse–Witt invertibility is a known theorem: Adolphson–Sperber2016 Theorem2.3 and Proposition2.11 are used with their support hypothesis. Koblitz1975 Theorem3 and his explicit attribution of the hypersurface case to Miller are preserved. Huang–Lian–Yau–Yu concerns toric coefficient formulas, generic invertibility and p-adic unit-root Frobenius, at the precise author-version windows already read; it is neighboring context rather than a finite-image theorem input. The recent OpenAI Milne preprint is neighboring rational-pairing context only.

The new primary rereading covers Stacks0A3J Artin–Schreier and Lemmas59.63.1–3, Stacks0BYA Lemma53.9.3 in full, and Stacks01XS Lemmas30.8.1–2 in full. Exact downloaded hashes and proof scopes are in sources.tsv and audit/pn_char2_higher_author/source_manifest.json. These classical statements do not contain the local elliptic-cover computation or the complete hypersurface image conclusion. Zalesskii–Serezhkin classification was offered in a statement packet but is not used in the characteristic-three proof or anywhere in this new public integration.

#### Primary neighboring candidate

Tian2009, Theorem1.3, printed398–399, gives full p-adic general-linear monodromy for the universal deformation of a connected HW-cyclic Barsotti–Tate group. Definitions, introductory statement and proof outline through400 were opened and read; no full proof was imported. We have not identified the hypersurface family with that universal deformation, so this theorem is not substituted for any hypersurface-image argument. The publisher PDF and exact SHA are recorded in sources.tsv. The primary arXiv abstracts1701.04509 and2001.07280 concern generalized Hasse–Witt congruences/generic invertibility and A-hypergeometric unit roots, respectively; no unread theorem proof was imported.

#### Bounded search record

The complete earlier exact queries and result scopes are audit/pn_char2_higher_author/LITERATURE.md and audit/clean_char3_higher/LITERATURE.md. They include author, journal, arXiv, ECCC and Hexagon searches, with characteristic-two, characteristic-three, Artin–Schreier and finite-image variants. A final all-prime follow-up used:

- `site:arxiv.org "universal hypersurface" "monodromy" "p-adic"`
- `"Hasse-Witt" "monodromy" "GL" hypersurface`
- `site:eccc.weizmann.ac.il hypersurface monodromy finite characteristic`
- `site:hexagonmath.org hypersurface "monodromy" "characteristic"`

The final retrieval is preserved as external/pn_char2_higher/fullprime_search_followup.json. It rediscovered Tian and Katz metadata and returned unrelated quadratic-Hasse, polynomial-complexity and complex-geometric items. The ECCC and Hexagon results did not identify an exact universal finite Hasse–Witt-image theorem. This is a bounded search outcome, not exhaustive coverage and not evidence of priority. Only the primary sources and reading windows explicitly listed above are credited as read.

#### Proof and source-comparison limits

The exact characteristic-two main theorem has the author's234-line proof, a separate root244-line derivation and a further793-line separate reconstruction, all fully compared by root. The higher characteristic-three public proof is the complete351-line statement-led reconstruction, with a separate root233-line derivation and complete comparison. Their admitted cubic-boundary and ordinary-Lang inputs, prior related exposure and freezes are recorded. The original attached higher PN proof chains have not thereby been audited line by line; their auxiliary claims retain their separate states. All checks are by the same model, with no human review.

Recorded: 2026-11-23T11:28:34.647539+00:00


<!-- continuation14:representation_lifting/LITERATURE.md -->

# Continuation literature searches: congruence sections and sharp co-Lie rank

Date: 23 November 2026. Same-model worker /root/representation_lifting. No priority claim is made. Searches used both search engines, the journal records, arXiv and authors' institutional pages. Sources downloaded to scratch are excluded from deliverables; exact hashes and passages are in SOURCES.tsv.

1. Queries `GL n Z p2 splitting GL n Fp Sah 1974 2 3 3 2` and `symplectic groups reduction modulo p2 splitting Sp 4 F3 section` identified Sah/Ginosar, Stasinski, and Landesman–Swaminathan–Tao–Xu. Search snippets were exposed before the frozen statement-led classification proof; this is disclosed and is not called a pristine classification reconstruction.
2. Queries `Stasinski Representations SLn finite local rings length two arxiv 6.2`, `Yuval Ginosar On splitting canonical map mod p GL 2001 pdf`, and `Sah Cohomology split group extensions II Theorem 7 GL p2 pdf` found Stasinski's official arXiv and Durham versions. The complete relevant Section6 pp12–14 was read, including Theorem6.2 and Remark6.3. Its exact special-linear prime-field list agrees with the independent derivation.
3. Queries for DOI `10.1090/mcom/3236` located Detinko–Flannery–Hulpke, Zariski density and computing in arithmetic groups (2018), author version4 arXiv:1611.05921. Theorem2.5 pp4–6 and its printed proof/preparatory lemmas were read. The theorem concerns proper supplements, not complements. Our original classification distinguishes these notions, and the new elementary obstruction proves the required nonsplitting directly.
4. Ginosar's publisher PDF returned403; its journal and author's Haifa record verify citation metadata only. The Sah1974 journal endpoint also returned403. These inaccessible original proofs are not marked as read. Subsequent search `Pooja Singla thesis representations finite local rings pdf 3 splitting` led to Singla's original2010 article arXiv:1001.5304. Section1 p3 explicitly records the complete general-linear list and credits Sah1977 p22 and Ginosar2001. This exact primary research account is the public paper's locator; every case has also been proved independently in the audit.
5. General-term queries `co-Lie rank lifting representation` and `co-Lie minimal surface`, plus site-restricted queries on Hexagon and ECCC, did not identify the exact4/3/2 minimal-rank geometric consequence. Results with the unrelated topological meaning of co-Lie are not mathematical evidence for this problem. The bounded negative search does not establish novelty. The article presents the rank conclusion as a consequence of known representation theory and its stated surface realization theorem, with no priority claim.
6. The Singla author page and institutional publication record were opened through search results. The journal article DOI and arXiv metadata were compared. Landesman–Swaminathan–Tao–Xu's Theorem1p1 gives a stronger higher-genus symplectic lifting statement and confirms context; it is not an additional input to our elementary proof.

Known status: all three congruence splitting lists are classical. What the new article paragraph supplies is the precise co-Lie rank consequence over arbitrary characteristic-p bases and projective surface attainment, using the already proved geometric theorem. No claim is made to classify all representations of arbitrary finite groups.


<!-- continuation14:ramification/LITERATURE.md -->

# Primary literature and original-source comparison, CP13 continuation

Recorded 23 November 2026 by /root/ramification, GPT-6 Astra Pro. Effort is not exposed; no human check. This is a bounded search and exact-input comparison, not a priority claim.

## Scope and chronology

The all-wild author derivation was frozen at 14:02:13.166972 UTC before the subsidiary B101 proof was opened. The later original-source comparison found the same strict mixed construction for n>=v_p(e)+2 and the exact k=2 family. That is an earlier supplied candidate, not a newly found published theorem and not part of the original 1018-row main inclusion tree. The current derivation adds the all-high branch n<=v_p(e)+1 and the full k=1,...,p−1 bands. This distinction is retained in B101_supplement.tsv; no B101 row is inserted into the original register.

The original B101 proof was read completely and compared: the A,b choices, switch inequalities, full logarithm covariance, Eisenstein ring, marked point, tame descent, roots of unity, quotient/twist, compatible extension lift and exact k=2 upper recurrence are valid at their stated input scopes. Its all-height lower assertion follows by adjoining the same constant height-(h−2) group to both unequal-character pairs; truncations remain isomorphic and the common added character cancels. The subsidiary scope remark is a scope/history record, not an additional mathematical check. B100 and B101 original certificates were read and rerun unchanged only in isolated scratch directories; no original script was copied into deliverables. Their exact hashes and outputs are in original_rerun_receipts.json.

## Search coverage

Searches used both available web indexes on 23 November 2026. Earlier queries covered p-divisible inertia from finite torsion, Bondarko height-two ramification, supersingular formal rational points and minimal ramification, Hattori tame characters, and author/primary versions of the closest results. Domain queries included arXiv, Hexagon and ECCC. The Hexagon home was reachable; direct search routes for Hexagon/ECCC did not produce usable search pages, and the corresponding domain queries gave no exact matching theorem. These negative searches are not evidence of absence.

The final verification queries were:

- `"Equivariant vector bundles on the Lubin-Tate moduli space" Hopkins Gross pdf`
- `"Barsotti" "torsion" "inertia" "ramification" Bondarko`
- `"height two" "formal group" "rational point" ramification`

The results located the original Hopkins–Gross text, the author bibliography and neighboring crystalline-torsion results. No exact published statement of the current all-n mixed equivalence or all-k wild bands was located in this bounded search. No novelty or priority conclusion is drawn.

## Exact primary passages read

**Hopkins, M. J., & Gross, B. H. (1994).** Equivariant vector bundles on the Lubin–Tate moduli space. In *Topology and representation theory* (Contemporary Mathematics, Vol.158, pp.23–88). American Mathematical Society. https://doi.org/10.1090/conm/158/01453

Original hosted PDF: https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf . A direct local fetch returned HTTP503 and a direct web open timed out. The search-index PDF reference subsequently opened successfully; equations(5.3)–(5.6), Proposition5.7, equations(12.3)–(12.9), Proposition12.10 and its entire written proof were read. The universal full integral formal law, logarithm recurrence, height-two specialization and residue-extension scope agree with I2. Proposition5.7 explicitly attributes integrality to Hazewinkel; that published input is retained, not claimed to have been freshly reproved. No local PDF hash is fabricated. Retrieval references: turn888822757view0, turn888822757view1, turn888822757view2. The complete written proof of Proposition12.10 is a deformation-theoretic argument using Ext2 vanishing, rank n−1 of Ext1 and Hom vanishing; no finite-residue restriction is imposed on the target local algebra.

**Smith, H. (2023).** Ramification in division fields and sporadic points on modular curves. *Research in Number Theory, 9*, Article17. https://doi.org/10.1007/s40993-023-00424-0 . Author version: https://arxiv.org/pdf/1810.04809 . Fresh file SHA256 d8d9bbd0a5f82d383d9fa7975908e6c670ed59f8878a54d2b1633f6f69699ea9. Printed pp.1–3, including Theorem 1.1 on p.2, were reread. The good-supersingular full-division-field bound is (p²−1)p^(2n−2), and the rational-point bound has its stated elliptic/number-field hypotheses. These do not identify the exact current mixed comparison class. Paper2's existing separate inspection of Theorem4.4 and Corollaries4.5–4.6 remains the recorded valuation input; this continuation does not claim a fresh full reading of those later pages.

**Hattori, S. (2008).** Tame characters and ramification of finite flat group schemes. *Journal of Number Theory, 128*(5),1091–1108. https://doi.org/10.1016/j.jnt.2007.05.006 . Repository PDF: https://eprints.lib.hokudai.ac.jp/repo/huscap/all/69652/re843.pdf . Fresh downloaded file272059 bytes, SHA256 2f12ffe851d1a189777ef4b5a080dc79589b655bb55fb8a6fdc18ad819d3c40e. Theorem 1.1 on printed p.1 (PDF p.2, after repository cover) was read. It identifies tame characters of Abbes–Saito ramification graded pieces of a finite flat generic representation, not the good-special-fibre descent character used in the current index. This is a statement-scope comparison; no fresh reading of its entire proof is claimed. The hash differs from the previously recorded version because this is the newly downloaded repository file.

**Iovita, A., Morrow, J. S., & Zaharescu, A. (2022).** Ramification of p-power torsion points of formal groups. Author preprint https://arxiv.org/pdf/2205.04608 . Fresh file SHA256 0c73d6913e597bb77d49b144cbb7be87a01f32f66d956c6153ef94c43c081127. Printed pp.1–3, including TheoremsA–B, were read. These concern eventual ramification/differential criteria and first-torsion tameness for strict formal groups over an unramified base. They do not state the current exact mixed height-two threshold. This source is contextual and is not used as a proof input or added to the public paper bibliography.

## Retained input boundaries

I1 is the cyclic-point obstruction proved in Paper2 Section 5. I2 is the full integral universal formal law just identified. I3 is the actual quotient/twist and compatible Kummer-extension construction in Section 8. I4 is the invariant augmentation graph bound in Section 16, valid without a restriction on v_p(e). I5 is the height-two structural determinant, dimension, Brauer and connected–étale reduction. The clean worker reconstructed the new theorem relative to these exact inputs. Root separately reread all of the cyclic obstruction, extension lifting and graph proof. None of this turns every historical B auxiliary into a checked statement; old local tables retain their own checks.

## Failures and corrected claims

The source fetch failures above were overcome for reading by the indexed original text; no local hash is available for Hopkins–Gross. No mathematical counterexample was found to the all-wild statement. The previous restriction n>=v+2 is removed only by the separately supplied all-high construction; it cannot be silently removed from B101's printed proof. The full-class formula remains unproved outside the displayed k=1,...,p−1 wild families, and the elliptic full-torsion higher-dimensional gate remains open. Finite arithmetic does not establish field existence, descent or effectivity.


<!-- continuation14:abelian_monodromy/literature.md -->

# Bounded literature investigation

Date:2026-11-23. This is a search log and a statement/ingredient comparison, not evidence of priority.

## Queries and coverage

Before14:20UTC, queries included: “abelian variety characteristic two hypersurface monodromy invariant covectors Hasse Witt Frobenius”; “Frobenius invariant quotient abelian hypersurfaces”; “relative unit-root abelian monodromy”; Oda1971 Theorem1.2; “abelian hypersurfaces monodromy characteristic two”; site:arxiv.org “Frobenius invariant covectors”; site:hexagonmath.org abelian unit root Frobenius monodromy; site:eccc.weizmann.ac.il abelian Frobenius; and OpenAI mathematics abelian varieties monodromy Frobenius. Both web engines were used. Results reached Oda, the Brion–Kumar and EGM author texts, Javanpeykar–Krämer–Lehn–Maculan, recent OpenAI mathematics preprints, and several unrelated invariant-field or characteristic-zero monodromy papers. No exact quotient theorem was located by these bounded queries.

At observed14:22:06UTC, the stronger engine repeated three searches: “Frobenius” “abelian varieties” “invariant covectors”; “monodromy” “hypersurfaces” “abelian” characteristic2; and site:arxiv.org “Frobenius” “abelian” “Cartier” “invariants”. Its relevant primary result was again the Javanpeykar–Krämer–Lehn–Maculan paper, and the Lawrence–Sawin hypersurface Shafarevich paper appeared as neighboring Hodge-theoretic monodromy. The exact characteristic-equals-coefficient finite invariant module was not found. Unrelated search results were not used as technical evidence.

## Exact comparisons

Oda1971 Theorem1.2(i), p45, supplies simplicity of isogeny direct images when the polarization is injective on the scheme-theoretic kernel, including inseparable isogenies. This input is classical and fully credited. It gives the odd-polarization endomorphism algebra, while the current argument identifies the relative invariant quotient by the coefficient-space and Euler steps.

Brion–Kumar2005 Lemma1.3.6/Proposition1.3.7/Theorem1.3.8, pp26–28, supplies Cartier's local coefficient extraction and finite-Frobenius duality. EGM Theorem7.5 and Proposition7.34 identify the Cartier dual of ker(F) with the dual Verschiebung kernel; Proposition5.22 supplies p-rank isogeny invariance. These are rechecked standard ingredients, not claimed new results.

Javanpeykar et al.2025, Section1.1 pp1046–1050, studies characteristic-zero families with generic rank-one twists and Tannaka groups of perverse sheaves. It does not compute this characteristic-two mod-two coherent stable-system quotient. Only the cited introductory result is read; its full proof is not certified here.

OpenAI2026 October7, Theorem1.1 pp1–2, concerns rational realizations of cycle pairings on abelian varieties. It is cited only to distinguish the nearby rational-cycle problem from the present finite mod-two quotient. Its full theorem is not an input and is not audited by reading the introduction.

The original nonordinary surface theorem already gives exact dimensions1 or2 in even cubic-theta degrees. Paper18 rechecks it and generalizes to arbitrary dimensions, polarizations that are Frobenius pullbacks, and the actual arithmetic permutation module. The original ordinary theorem gives only a lower bound2^g−1; the current Euler extension gives exactness. The all-dimensional adjoint-of-squaring calculation and ordinary upper bound have no exact match in this bounded search. No novelty or priority conclusion follows from that absence.

All fetched primary URLs, file hashes and exact read scopes are in SOURCES.tsv. Primary PDFs and extracted pages remain outside deliverables. The bibliography uses author-year references with exact cited locators.


<!-- continuation14:lubin_tate/LITERATURE.md -->

# Literature search: normalized Lubin–Tate lattices

Searches made23November2026,14:00–14:37UTC. Both available search engines were used,
with stronger search for exact source and archive coverage. Exact queries:

- Lubin Tate group integral de Rham Dieudonne lattice crystalline comparison tangent lattice ramification Lau windows
- "Lubin-Tate" "lattices" "de Rham" integral comparison
- "Lubin-Tate" "Grothendieck" "different" Dieudonne
- "Lubin-Tate" "Breuil" "pi" "lattice" comparison
- site:arxiv.org "Lubin" "de Rham" "lattice" "comparison"
- site:hexagonmath.org Lubin Tate crystalline lattices
- site:eccc.weizmann.ac.il Lubin Tate crystalline cohomology
- "Prismatic F-crystals and E-crystalline Galois representations"
- "Grothendieck" "Lubin" "lattice" ramification
- "OpenAI" "Lubin-Tate" (past365days)
- "Formal Complex Multiplication in Local Fields" pdf Lubin Tate
- "LubinTateFormalCMinLocalFields.pdf"
- Serre Local Fields different inverse trace dual Chapter III Proposition7

## Findings and exact status

Lau2014 is the published classification/crystalline realization input, with all
relevant pp2243–2249 read. Its Proposition7.1 fixes a convention error in the first
independent attempt: Frobenius is sigma(E phi^{-1}), not the window map. The error
and source correction are preserved. Lubin–Tate1965 Lemma1/Theorem1 supplies the
classical formal-module construction and normalization; primary cached text was
read, while three direct raw PDF attempts returned503. Its source hash explicitly
identifies the retrieved text rather than pretending to hash an unavailable PDF.
The author bibliography at https://www.math.brown.edu/jlubin/CVRefs.html was opened.

Kisin–Ren2009 Theorem0.1 p442 classifies specified Galois-stable lattices by analytic
Lubin–Tate modules, under its stated field hypotheses. Pham2025 Theorems1.5/1.6,
arXiv version28Feb2025 pp2–3, gives the adjacent prismatic and pi-divisible-module
classifications. Both precise statements were opened. They do not state the
normalized equality criterion or the exact mutual denominator computed here.
Searches also located Marks and Anschütz–Le Bras in adjacent prismatic theory;
no claim about an unopened proof is adopted.

The exact all-Eisenstein criterion e<=p and the two exponents max(0,e-p) were not
matched in these bounded searches. Record as a new explicit calculation relative
to named known classification inputs, without a claim of priority. The old own
source already proves alpha=0 and the e=p+1 counterexample; those are not new to
this project. The new contribution is the all-field iff and exact denominator.
No correction of somebody else's published theorem is claimed.

The ECCC search found no relevant exact theorem; a de Rham–Witt algebraic
independence item is unrelated. Hexagon searches found no exact predecessor;
hexagon2611.00789v1 was opened as the requested writing example, not as a
mathematical input. The recent OpenAI/Lubin–Tate search found no relevant result.
No unrelated AI-laboratory paper is inserted into the manuscript.

The original scan cote8 was fetched and its PDF images44,46,48,50 viewed. Their
archive sheet numbers are43,45,47,49. The equality question and short quote occur
on archive sheet49, PDFimage50. Former own-source shorthand8:48–50 is not adopted
as archive sheet numbering. Serre1979 ChapterIII §3 p50 supplies the precise
inverse-different convention; the Herbrand theorem remains cited and checked in
Paper2. Every downloaded foreign item remains outside the deliverables.


<!-- continuation15:B2_lifting/LITERATURE.md -->

# B.2: primary literature and scope of the present check

Worker: `/root/representation_lifting`; model: GPT-6 Astra Pro; reasoning effort not exposed; no human verification.

## Precise primary sources inspected

1. Anema, A. S. I., Top, J., & Tuijp, A. (2018). Hesse pencils and 3-torsion structures. *SIGMA, 14*, 102. https://doi.org/10.3842/SIGMA.2018.102. Publisher PDF: https://sigma-journal.com/2018/102/sigma18-102.pdf. Theorem 1.1, p. 2, and the statement and neighboring discussion of Proposition 5.1 in Section 5 were inspected. These identify the classical Hesse pencil and prescribed three-torsion structures. The present full-rational-torsion assertion is proved directly by universal polynomial identities; it does not rely on an unread proof in this article. The complete article was not read.

2. Dembélé, L., Freitas, N., & Voight, J. (2025). *On Galois inertial types of elliptic curves over Q_p* (author manuscript dated April 23, 2025). https://jvoight.github.io/articles/inertial-types-042325.pdf. Accepted by *Mathematics of Computation*, https://doi.org/10.1090/mcom/4107. Section 3.2, p. 11, and Lemma 3.2.1 were inspected, including the semistability-field definition and the complete list of possible inertia groups. In residue characteristic three the noncyclic group of order twelve is already classical. The lemma attributes the result to Kraus (1990, pp. 354–357). The same relevant section of the September 26, 2024 author version was also read; no entire-paper proof check is claimed.

3. Kraus, A. (1990). Sur le défaut de semi-stabilité des courbes elliptiques à réduction additive. *Manuscripta Mathematica, 69*(4), 353–385. https://doi.org/10.1007/BF02567933. Bibliographic metadata and the precise attribution in Dembélé–Freitas–Voight were checked. The original Kraus article was not available as a readable PDF in this check. A publisher response advertised as PDF was detected to be HTML and retained only in scratch as HTML. No original Kraus proof was read or is claimed to have been read.

## Known facts and checked consequences

The Hesse construction, its three-torsion structure, and the occurrence of semistability defect twelve in residue characteristic three are known. This audit makes no claim to discover them. The exact coordinate specialization over Q_3(i, zeta_3), the all-index table under full rational three-torsion, and the exclusion over the fixed cyclotomic field were checked as statements of the supplied research source. Their exact historical priority was not established by the bounded search, and no novelty or priority claim is made.

The short proof of the table in the proposed article insertion uses the already checked tame criterion and all-wild criterion at level one. The complete original all-index Hesse proof was nevertheless read and checked afterward, including its exceptional indices six and ten. This distinction is retained in the freeze and comparison records.

The independent reconstruction of the cyclotomic exclusion isolates the residue-field obstruction at p=5. A mere existence criterion allowing arbitrary perfect residue fields does not exclude the prescribed base Q_5(zeta_5); the proof additionally uses a totally ramified good-reduction field with residue F_5 and the leading formal parameters of all twenty-four nonzero five-torsion points.

## Search bounds

Primary-source and metadata searches included full rational three-torsion with semistability defect, Hesse families with semistability defect, and full p-torsion over cyclotomic local fields. No exact external match to every target formulation was established. Absence of a match in this bounded search is not evidence of novelty. Foreign PDFs and the original source programs remain outside the deliverables tree; only the new proof, metadata, new independent program, and rerun outputs are included.

## Exposure and chronology

REGISTER statements and explicitly retained, already checked theorem inputs were read first. The complete 158-line reconstruction was frozen at 2026-11-23T14:43:09.700438+00:00. Only then were the original B.tex proofs (lines 404–677), both original verification programs, and primary-source material read. The original proofs and programs were fully compared and rerun. The post-exposure exceptional-index-ten calculation is marked as a full targeted source check, not a clean independent reconstruction. The audit comparison was recorded at 2026-11-23T14:54:08.470963+00:00; these later checks were not complete at the earlier checkpoint deadline.


<!-- continuation15:abelian_monodromy/full_image_followup/literature.md -->

# Paper20 bounded literature investigation

Date:2026-11-23. No priority inference is made from a bounded negative search.

## Dated queries and results

Between14:40 and14:43UTC, searches asked for GL8(2) subgroups containing127, primitive-prime-divisor criteria, Singer cycles, Kantor1980 and Bereczky2000. The primary author PDF of Kantor was retrieved at14:43:33.304823UTC. Its entire printed pp232–234 were read, and all three page images were inspected. The normal-subgroup sign in the theorem on p232 was checked visually. This exact input already proves the needed overgroup classification; later primitive-prime-divisor or transvection classifications are not inputs.

Between14:55 and14:57UTC, searches included: "supersingular" "product" "monodromy" "GL" "Cartier"; "supersingular abelian surface" "Hasse" "monodromy"; site:arxiv.org "Hasse-Witt" "monodromy" hypersurfaces; site:hexagonmath.org supersingular monodromy; "Irreducibility and p-adic monodromies" pdf Yu; "p-rank strata" "monodromy" curves GL p; "supersingular" "cubic" "monodromy" "hypersurface". Both web engines were used. Results included Yu's primary arXiv paper and official journal DOI, Achter–Pries's prime-to-p symplectic curve-stratum paper, and the neighboring characteristic-zero abelian-subvariety literature. No exact fixed E² cubic-product GL8 theorem was located by these queries. The Hexagon query reached the Deligne/Alpöge example and unrelated papers, not a technical input here.

At observed15:04:20UTC the further query batch was: site:eccc.weizmann.ac.il supersingular monodromy Singer cycle; "supersingular" "hyperplane" "GL8"; "Kantor" "Singer cycle" "1980" "Bereczky". The ECCC results were unrelated. Forward citation results from Kantor included Gill's On a conjecture of Degos and pairwise-generation papers citing Kantor and Bereczky; these were discovery results, not proof inputs. No claim about their full contents is made.

## Exact statement/ingredient comparison

Kantor1980, theorem p232 and proof pp232–234, gives G containing a Singer cycle a naturally embedded normal GL(n/s,q^s), s|n. The paper's dimension-eight criterion is an explicit elementary consequence: an order127 element rules out s=2,4,8. Kantor's complete printed proof was read, while earlier projective-group theorems cited inside it remain published background. Normality is essential to the centre/extension-field normalizer argument.

Yu2008, Theorem1.1 preprintp1, proofpp2–3, proves full p-adic monodromy on every p-rank-f Siegel stratum over an algebraically closed field. The exact statement and its short proof were read. Its result is context, not a dependency: universal-stratum surjectivity does not establish surjectivity after pullback to this particular fixed-surface linear system. The theorem uses the known ordinary case and stratum irreducibility; those are not audited here as separate theorem inputs.

Brion–Kumar2005 Lemma1.3.6 and Proposition1.3.7 pp26–27 provide the precise Cartier coefficient and Frobenius-duality formulas, read earlier in this continuation and reapplied to the explicit six-entry elliptic table. Grothendieck cote4 §8.5.8–9, archive sheets7–8/PDF8–9, supplies the hypersurface semisimple-rank and local-system programme; no full-GL conjecture is attributed to those scans.

Javanpeykar–Krämer–Lehn–Maculan2025 §1.1 pp1046–1050 is a neighboring characteristic-zero Tannakian monodromy result. OpenAI2026 October7 Theorem1.1 pp1–2 treats rational pairings of specialized Hodge classes after good reduction, including residue characteristic2. These precise introductory passages were read and are contextual only; neither full theorem proof is certified as a dependency.

All URLs, hashes and exact read locators are in SOURCES.tsv. External PDFs and plain-text extracts stay outside deliverables. The earlier attached source is our own AI research, but no unchanged original program or source file is copied into the deliverables; generated result records are retained.


<!-- continuation15:weak_formal_rational/LITERATURE.md -->

# Rational coefficients on the nilpotent weak-formal site — 23 November2026

Primary-source comparisons: Meredith(1972),§2 Theorem14pp10–11, gives weak-affine coherent acyclicity; it does not itself identify site cohomology after rationalization. Arabia–Mebkhout(2010),Theorem8.6,Lemmas8.7–8.9,Corollary8.11pp1987–1989, proves nonvanishing on a smaller exact-lift dagger site via logarithmic Jacobians; its objects exclude the ordinary nilpotent diagonal and two-branch tests essential here. Zhang(2019),Definitions3.1,3.7,Example3.8(ii)p14,Example4.4p17,Corollary5.19p27, uses a larger enlargement site and distinguishes rationalizing a sheaf from tensoring cohomology. Große-Klönne(2000),§1.4,Propositions1.5–1.6,authorpp4–5, provides Noetherianity, finite maximal residue fields and integral evaluation. Stacks tags00IN and00IP were opened and their full short proofs read for Artin–Rees and local Krull; the paper gives the annihilator deduction explicitly. Exact PDF hashes are in SOURCES.tsv; no fetched source is returned.

Dated searches:14:52UTC general integral stratification/weak formal cohomology and p-adic Taylor;14:55UTC weak formal logarithm cohomology, Arabia–Mebkhout8.6, Hexagon infinitesimal rational dagger, ECCC infinitesimal cohomology;15:03UTC Große-Klönne Noetherian dagger source;15:18UTC arXiv rational weak formal cohomology, Zhang author research page, OpenAI mathematics infinitesimal cohomology over preceding365days, nilpotent dagger logarithmic cocycles. Primary journal, arXiv and author pages were opened. Bounded results did not exhibit this full nilpotent-test affine calculation. This is a bounded search result, not a priority assertion or exhaustive nonexistence claim. Recent Illusie(2025) context remains the prior checked divided-power comparison, which is a different site.

Classification: new extension of the present manuscript calculation relative to explicitly credited known inputs; no published correction is claimed. General perfect-field zero-phantom and general proper rational coefficient gates remain open.


<!-- continuation16:abelian_monodromy/full_image_followup/literature.md -->

# Paper20 bounded literature investigation

Date:2026-11-23. No priority inference is made from a bounded negative search.

## Dated queries and results

Between14:40 and14:43UTC, searches asked for GL8(2) subgroups containing127, primitive-prime-divisor criteria, Singer cycles, Kantor1980 and Bereczky2000. The primary author PDF of Kantor was retrieved at14:43:33.304823UTC. Its entire printed pp232–234 were read, and all three page images were inspected. The normal-subgroup sign in the theorem on p232 was checked visually. This exact input already proves the needed overgroup classification; later primitive-prime-divisor or transvection classifications are not inputs.

Between14:55 and14:57UTC, searches included: "supersingular" "product" "monodromy" "GL" "Cartier"; "supersingular abelian surface" "Hasse" "monodromy"; site:arxiv.org "Hasse-Witt" "monodromy" hypersurfaces; site:hexagonmath.org supersingular monodromy; "Irreducibility and p-adic monodromies" pdf Yu; "p-rank strata" "monodromy" curves GL p; "supersingular" "cubic" "monodromy" "hypersurface". Both web engines were used. Results included Yu's primary arXiv paper and official journal DOI, Achter–Pries's prime-to-p symplectic curve-stratum paper, and the neighboring characteristic-zero abelian-subvariety literature. No exact fixed E² cubic-product GL8 theorem was located by these queries. The Hexagon query reached the Deligne/Alpöge example and unrelated papers, not a technical input here.

At observed15:04:20UTC the further query batch was: site:eccc.weizmann.ac.il supersingular monodromy Singer cycle; "supersingular" "hyperplane" "GL8"; "Kantor" "Singer cycle" "1980" "Bereczky". The ECCC results were unrelated. Forward citation results from Kantor included Gill's On a conjecture of Degos and pairwise-generation papers citing Kantor and Bereczky; these were discovery results, not proof inputs. No claim about their full contents is made.

## Exact statement/ingredient comparison

Kantor1980, theorem p232 and proof pp232–234, gives G containing a Singer cycle a naturally embedded normal GL(n/s,q^s), s|n. The paper's dimension-eight criterion is an explicit elementary consequence: an order127 element rules out s=2,4,8. Kantor's complete printed proof was read, while earlier projective-group theorems cited inside it remain published background. Normality is essential to the centre/extension-field normalizer argument.

Yu2008, Theorem1.1 preprintp1, proofpp2–3, proves full p-adic monodromy on every p-rank-f Siegel stratum over an algebraically closed field. The exact statement and its short proof were read. Its result is context, not a dependency: universal-stratum surjectivity does not establish surjectivity after pullback to this particular fixed-surface linear system. The theorem uses the known ordinary case and stratum irreducibility; those are not audited here as separate theorem inputs.

Brion–Kumar2005 Lemma1.3.6 and Proposition1.3.7 pp26–27 provide the precise Cartier coefficient and Frobenius-duality formulas, read earlier in this continuation and reapplied to the explicit six-entry elliptic table. Grothendieck cote4 §8.5.8–9, archive sheets7–8/PDF8–9, supplies the hypersurface semisimple-rank and local-system programme; no full-GL conjecture is attributed to those scans.

Javanpeykar–Krämer–Lehn–Maculan2025 §1.1 pp1046–1050 is a neighboring characteristic-zero Tannakian monodromy result. OpenAI2026 October7 Theorem1.1 pp1–2 treats rational pairings of specialized Hodge classes after good reduction, including residue characteristic2. These precise introductory passages were read and are contextual only; neither full theorem proof is certified as a dependency.

All URLs, hashes and exact read locators are in SOURCES.tsv. External PDFs and plain-text extracts stay outside deliverables. The earlier attached source is our own AI research, but no unchanged original program or source file is copied into the deliverables; generated result records are retained.

## Degree-three extension and general even-dimensional criterion

At observed15:33:47UTC, a further query batch was: "supersingular" "GL80"; "Cartier" "monodromy" "cubic" "abelian surface"; "Singer cycle" "irreducible" "fixed space" extension field. No exact fixed cubic-product GL80 theorem was located. The technical group results returned author-hosted Reflection factorizations of Singer cycles and Guralnick–Malle's Simple groups admit Beauville structures, plus broader probabilistic-generation literature. Those results were discovery context only, not read or adopted as theorem inputs. The even-dimensional Singer/fixed-space criterion in the author addendum is explicitly presented as an elementary consequence of Kantor1980, with its complete proof, not as a new classification theorem. The original attached all-odd theorem is stronger in scope; only its degree-three instance is newly established here by the different finite-certificate route.


## Combined cubic release: scope of the same primary input

Observed 2026-11-23T15:52:20.501360+00:00. The exact Kantor1980 normal-subgroup theorem is now applied in dimension80 as well as8. Its hypotheses are unchanged (subgroup of GL_n(F2) containing a Singer cycle), and the primary theorem/proof read and normality visual check are recorded above. The general even-n criterion and explicit n=5 parity counterexample are proved elementary consequences of this stated input; no separate classification or novelty claim is made. The original all-odd source theorem was read completely after author cubic freeze, but only its d=1,d=3 instances are now certified by alternative proofs. The previous exact GL80 queries and their negative/limited results remain the bounded literature search; no negative search is used to claim priority.


<!-- continuation16:weak_formal_rational/LITERATURE.md -->

# Rational coefficients on the nilpotent weak-formal site — 23 November2026

Primary-source comparisons: Meredith(1972),§2 Theorem14pp10–11, gives weak-affine coherent acyclicity; it does not itself identify site cohomology after rationalization. Arabia–Mebkhout(2010),Theorem8.6,Lemmas8.7–8.9,Corollary8.11pp1987–1989, proves nonvanishing on a smaller exact-lift dagger site via logarithmic Jacobians; its objects exclude the ordinary nilpotent diagonal and two-branch tests essential here. Zhang(2019),Definitions3.1,3.7,Example3.8(ii)p14,Example4.4p17,Corollary5.19p27, uses a larger enlargement site and distinguishes rationalizing a sheaf from tensoring cohomology. Große-Klönne(2000),§1.4,Propositions1.5–1.6,authorpp4–5, provides Noetherianity, finite maximal residue fields and integral evaluation. Stacks tags00IN and00IP were opened and their full short proofs read for Artin–Rees and local Krull; the paper gives the annihilator deduction explicitly. Exact PDF hashes are in SOURCES.tsv; no fetched source is returned.

Dated searches:14:52UTC general integral stratification/weak formal cohomology and p-adic Taylor;14:55UTC weak formal logarithm cohomology, Arabia–Mebkhout8.6, Hexagon infinitesimal rational dagger, ECCC infinitesimal cohomology;15:03UTC Große-Klönne Noetherian dagger source;15:18UTC arXiv rational weak formal cohomology, Zhang author research page, OpenAI mathematics infinitesimal cohomology over preceding365days, nilpotent dagger logarithmic cocycles. Primary journal, arXiv and author pages were opened. Bounded results did not exhibit this full nilpotent-test affine calculation. This is a bounded search result, not a priority assertion or exhaustive nonexistence claim. Recent Illusie(2025) context remains the prior checked divided-power comparison, which is a different site.

Classification: new extension of the present manuscript calculation relative to explicitly credited known inputs; no published correction is claimed. General perfect-field zero-phantom and general proper rational coefficient gates remain open.


## Continued primary comparison, 23 November 2026

Root read all seven pages of Ertl–Sprang (2018), including Proposition1 on the weak interval and its T(T−p) finite two-branch algebra. These constructions are credited; the present all-test nilpotent-thickening detector is a separate statement. Root read the complete Davis–Langer–Zink Overconvergent Witt Vectors Proposition2.31 passage (Bielefeld author pp19–21, proposition onp20), establishing the weak Hensel input. The source title was checked on its first page; an earlier working shorthand incorrectly called this the de Rham–Witt paper and is not used in the citation. Root and editor read the complete Stacks Lemma20.19.1 (01FF) statement/proof; its colimit theorem is used for the weak-formal Noetherian Zariski space only.

Recent context: Ertl–Shiho–Sprang arXiv2105.11009v3, revised13February2025, introduction pp1–4 read in full. Its unconditional degree-one construction uses log crystalline cohomology of split proper generically étale hypercovers and has a different site and integral aim. No equality with the present cohomology is asserted. Zhang2019 selected complete PDFpages13–15,17,27 were reread: the enlargement data and special-fibre map convention differ from prescribed nilpotent thickenings; no canonical site inclusion is claimed.

Bounded searches on23November2026 used weak formal/infinitesimal nilpotent-site rational cohomology, dagger Poincare comparison and homotopy queries through both search engines; arXiv, journal/author sources, ECCC and Hexagon were considered. The ECCC Witt-Jacobian item is a different problem. The Sprang research page led to the revised2025 preprint. No exact earlier all-test degree-one comparison was located in these bounded searches; this is not a novelty or priority certificate. Source hashes and exact read scopes are in SOURCES.tsv.
