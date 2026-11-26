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

## CP14 primary-source and bounded-literature records

These are exact owner/root reading records, not a new literature search by the metadata integrator.

### audit/remaining_B2_main/LITERATURE.md

# Literature and exact input scope

Recorded on 2026-11-23 by GPT-6 Astra (ChatGPT Pro mode), /root/blind_ramification. The bounded follow-up comprised the four exact queries in `literature_followup.json`; it is not an exhaustive priority search.

Anema, A. S. I., Top, J., and Tuijp, A. (2018), *Hesse pencils and 3-torsion structures*, SIGMA, 14, 102, DOI10.3842/SIGMA.2018.102, Section1, Theorem1.1, p.2, supplies the classical Hesse-family and symplectic-three-torsion context over perfect fields of characteristic different from three. The complete first two pages of the primary author PDF were read. The current generic field is characteristic zero. The displayed point identities and exact local degree-twelve good-reduction field are proved directly in the paper; this citation is not substituted for them.

Smith, H. (2023), *Ramification in division fields and sporadic points on modular curves*, Research in Number Theory, 9, Article17, DOI10.1007/s40993-023-00424-2, Theorem1.1, p.2 of the author version, proves the known division-field lower bound at its number-field good-supersingular scope. The relevant complete page was reread. Lemma5.1 gives the complete-DVR argument in the paper and proves the residue-field injection at equality using Galois descent.

Ozeki, Y., and Yoshida, M. (2026), *Fields of definition of p-torsion points of elliptic curves and their ramification*, arXiv:2609.06554, concerns curves defined over Qp. The complete first page of the retained primary PDF was read. Its field quantifier differs from a theorem allowing an elliptic curve to be defined over Qp(zeta_p). It is neighboring context only. The failed new arXiv open was not used; the retained primary PDF was identified and hashed.

The Neron mapping property and NOS inputs retain their exact previously checked scopes: Milne (2008), Theorem17.1 and Remark17.2, p.70, and Serre and Tate (1968), Theorem1, p.493. The height-one etale/multiplicative classification is an explicitly admitted checked input; the finite scalar recovery, including p=2, is proved in full. No new claim in this classical background is made.

The search also surfaced publisher metadata for Yasuda (2016) and primary-author abstracts for related cyclotomic-torsion papers. These were not used as proof inputs. Exact URLs, reading limits, local primary-file hashes and failed-open information are in `sources.tsv` and `literature_followup.json`. No priority conclusion follows from this bounded search, and no foreign paper or extract is included in the returned audit.


### audit/lt_lattice_root/LITERATURE.md

# Lubin–Tate lattice literature review

Recorded 2026-11-23T12:15:18.830692+00:00.

Bounded online status/context review for the all-ramification tangent theorem and exact e<=p full-lattice criterion. No priority claim.

##### Searches

- Lubin Tate integral crystalline comparison lattices ramification tangent different
- "Lubin-Tate" "lattices" "Lau"
- site:arxiv.org "Lubin-Tate" "integral" "comparison"
- site:hexagonmath.org "Lubin" "lattice"
- "Lubin-Tate" "lattices" "ramification" crystalline
- site:eccc.weizmann.ac.il "Lubin"
- site:hexagonmath.org "Lubin"
- "Lubin-Tate" "lattices" "e" "Grothendieck"
- "Prismatic F-crystals and E-crystalline Galois representations" Pham arxiv
- "Lubin-Tate" "crystalline" "Hexagon"
- "Lubin-Tate" "tangent" "lattice"
- "Samuel Marks" "Prismatic" "1009"
- "Lau" "crystalline Dieudonne" "Lubin" lattices
- "Dieudonne crystals and Wach modules" Cais Lau2017
- Kisin Ren2009 Galois representations Lubin Tate groups pdf441461
- site:hexagonmath.org "Lubin" "Tate"
- site:eccc.weizmann.ac.il "crystalline" "lattice"

##### Exact conclusions

- The general classification and crystalline comparison inputs are classical and credited exactly to Lau2014 and Lubin-Tate1965.
- The consulted contextual theorem statements concern stable Galois lattices, crystals/local systems or comparison determinants. None of the consulted spans states the exact equality criterion for the two archive-normalized de Rham/special lattices.
- The alpha0 conclusion and sharper threshold are proved in this manuscript; a bounded search cannot establish priority or exhaust the literature.
- Hexagon search returned adjacent arithmetic works mentioning Lubin-Tate in references, including2611.00723v1 and2611.00812v1. No consulted result supplied the exact lattice criterion; those works are not adopted as inputs.
- ECCC-indexed searches returned no relevant exact match in the visible search outputs. This is a coverage-limited negative search.

##### Sources and pages

### Kisin, M., & Ren, W. (2009). Galois representations and Lubin-Tate groups. Documenta Mathematica,14,441-461. doi:10.4171/DM/278.

https://emis.de/ft/10201

SHA-256: 343cf8ece7b4832a6f83540510d540b93c054468d0ff37abe71bb92e669bf584.

Introduction, printed441-443/PDF1-3; Theorem(0.1), printed442.

Full introduction and theorem statement read from primary PDF; context only. Analytic (phi_q,Gamma) modules classify stable O_L-lattices in L-crystalline representations, with base hypotheses stated in the introduction. No full theorem-proof reading claimed.

### Cais, B., & Lau, E. (2017). Dieudonne crystals and Wach modules for p-divisible groups. Proceedings of the London Mathematical Society,114(4),733-763. doi:10.1112/plms.12021. Accessed arXiv1412.3174v2(2016).

https://arxiv.org/pdf/1412.3174v2

SHA-256: 78ae55325971e420735b258504f641362bfcb56135e9d9f124b77b4e30597f9e.

Version2, abstractp1 and complete Introductionpp2-3, Theorem1p2.

Primary arXiv text and author publication page opened; journal metadata separately checked. Context only: p>2, cyclotomic bases, classification and crystal recovered by Frobenius base change. Version-specific theorem/page locators are not transferred to the journal PDF.

### Marks, S. (2025). Prismatic F-crystals and Lubin-Tate(phi_q,Gamma)-modules. Documenta Mathematica,30(4),787-838. doi:10.4171/DM/1009.

https://ems.press/content/serial-article-files/50901?nt=1

SHA-256: cc5f5ef2c365d35b4c2639585bad5e65dfa49701cb3c3a96e35ea17bba2c760e.

Abstract and opening introductionpp787-789, especially complete Theorem1.3pp788-789.

Primary journal PDF opened and downloaded. Laurent F-crystal/local-system equivalence and cohomology comparison read at statement scope; context only, no proof dependency.

### Pham, D. (2025). Prismatic F-crystals and E-crystalline Galois representations. arXiv2306.13205v2. Published in Publications mathematiques de Besancon(2025),59-96,doi:10.5802/pmb.62.

https://arxiv.org/pdf/2306.13205v2

SHA-256: d77bb3831f09b377d721a218db1432203165659c7e882ded5b81de23ac8af1e4.

Version2 introductionpp1-3, definitions1.1/1.4 and Theorems1.2/1.5/1.6; key lattice equivalence Theorem1.5p2.

Primary arXiv version2 read, final-version metadata confirmed; publisher PDF returned403. Cite version-specific theorem numbering, not unverified journal numbering. Classification context only, no full proof claim.

### Schneider, P., & Venjakob, O. (2026). Reciprocity laws for(phi_L,Gamma_L)-modules over Lubin-Tate extensions. Memoirs of the European Mathematical Society,24. doi:10.4171/MEMS/24.

https://ems.press/content/book-files/51694?nt=1

SHA-256: bb9f5dbe01e21b14e93b8df0c1fec80b31044eaa6c564098064e700b43f0e338.

Title/contents/abstract; section3.2 definition of D(T) and Proposition3.2.1, printed31/PDF40; nearby remarkspp31-32 exposed.

Primary book PDF opened and downloaded; cover gives2026 while copyright gives2025, so bibliographic year follows volume cover. Exact determinant-comparison statement read; no full section-proof or target-threshold dependency claimed.

### OpenAI. (2026, October7). Milne's rationality conjecture for abelian varieties [Preprint].

https://github.com/openai/math/tree/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026

SHA-256: 640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234.

Complete Theorem1.1 and its normalization, pp1-2; introductory origin/context pp1-3.

Previously downloaded primary PDF reused and first theorem fully reread. Current GitHub tree re-open failed in search service; original source bytes remain hash-identified. Context only: preprint states rational compatibility of specialized Hodge/divisor pairings, including crystalline realization. No new verification of that proof and no use as an input.

##### Public context guidance

The neighboring classifications provide the established setting for integral p-adic Hodge theory. The full-lattice criterion here is proved by the displayed normalized comparison and a coefficient obstruction in the original tensor order. No general classification is presented as new. The cited AI-laboratory preprint supplies recent context on crystalline specialization of rational pairings; the proof uses only the named classical comparison inputs.


### audit/pn_original_chain_inventory/LITERATURE.md

# Literature comparison for the original projective-hypersurface chains

Completed23November2026. This is bounded source verification, not an exhaustive priority search. No public manuscript or global record was edited in this task.

##### Exact known inputs

- **Odd hook modules are known.** Peel, M. H. (1971), *Hook representations of the symmetric groups*, Glasgow Mathematical Journal12(2),136–149, DOI10.1017/S0017089500001245, Theorem2 p142 and Propositions1/4 pp136–138, gives the odd-characteristic simplicity/two-factor indecomposability classification. The source theorem's hook module is the exterior power of the augmentation module; duality gives the quotient-permutation exterior module used here. Thus `lem:odd-wedge-submodules` and `lem:odd-general-hook-module` prove classical conclusions. The primary theorem and its printed proof pp142–145 were read; p142 was visually inspected. A harmless Imη/kerη typo in proof(b) is proposed separately for root confirmation. The elementary matching proof in the original source checks independently of this typo.
- **The transvection classification is a published input.** Kantor, W. M., and Seress, Á. (2001), *Black box classical groups*, Memoirs of the AMS148(708), DOI10.1090/memo/0708, §3.1.1 p20 and Theorem3.6 p22. Both exact pages were visually read. Its full-transvection-group hypothesis is satisfied over the prime field by taking powers. Its odd-characteristic alternatives are exactly those used. The original McLaughlin proofs, cited by Kantor–Seress, were not read or re-proved here.
- **Ordinary quartic monodromy is a published input.** Achter, J. D., and Pries, R. (2008), *Monodromy of the p-rank strata of the moduli space of curves*, arXiv0707.2110v2, §4.3/Proposition4.8 p16. The statement, complete printed proof, and ground-field convention were read. The ordinary g=f=3 case invokes Ekedahl(1991), Theorem2.1. The official Ekedahl chapter metadata/abstract was opened; the attempted full-PDF request returned non-PDF HTML. No page-level reading of that antecedent is claimed. The moduli-to-plane parameter-space passage is explicitly checked in the audit notes. Paper17 also has its complete alternative proof of the quartic conclusion.
- **Connected covers and the projection lemma's background.** Stacks tags035I,0BQL and0364, especially Lemma33.8.6, were opened and the relevant full proofs read. They give the normalization factorization, integrality of connected finite étale covers of a normal integral base, and the function-field criterion for geometric irreducibility. The actual exceptional-fibre argument is written out in the audit. Tag030V was also read as reducedness background; smoothness already suffices in the final argument.

The exact download URLs, hashes, and read scopes are in `sources.tsv`; foreign text, PDFs and page images remain under `external/pn_original_chain/`.

##### Queries and coverage

The searches used both search engines, with the stronger search used after routine retrieval did not locate Ekedahl's theorem text. Executed queries included:

1. `Ekedahl "The action of monodromy on torsion points of Jacobians" pdf theorem2.1`.
2. `Kantor Seress Black Box Classical Groups Theorem3.6 transvection groups McLaughlin1967`.
3. `"The action of monodromy" Ekedahl pdf` and `"978-1-4612-0457-2_4" pdf`.
4. `site.stacks.math.columbia.edu relative algebraic closure geometrically integral separably generated field extension` and the normal-morphism/finite-normalization variant.
5. `Peel hook representations symmetric groups odd characteristic exterior powers simple p divides n`.
6. `"linear projection" "finite étale" "center" monodromy connected`.
7. `site:arxiv.org "hook" "exterior" "odd characteristic" Peel`.
8. `site:eccc.weizmann.ac.il "transvection" "monodromy"`.
9. `site:hexagonmath.org "monodromy" "hypersurface"`.
10. `"SL_3" "H^1" "natural module" odd characteristic`.

The exact source and search responses saved in `external/pn_original_chain/pn_original_*.json` identify the opened sources. The hook search produced the exact Peel primary paper, which was downloaded and inspected. The last arXiv/ECCC/Hexagon/group-cohomology batch returned unrelated finite-group and complex-geometric items and Hexagon search listings; no additional exact PN full-image result was identified. Those candidate texts were not opened and receive no theorem/proof-reading credit. The exact SL3 first-cohomology argument is proved directly in the audit; a search result about second-cohomology extensions is not used for it.

##### Outcome by mathematical family

The hook classification is credited as known. The original rank-one operator, finite cocycle, canonical-block, reflection and coordinate-generation arguments are completely checked elementary derivations; this record makes no novelty claim for them. The geometric projection and independent-quadric constructions are checked in their exact hypotheses. The bounded search did not identify an exact standalone formulation of the projection lemma, but that absence establishes no priority. Its algebraically closed ground-field convention is essential and is recorded explicitly.

The original whole odd-prime and characteristic-two PN conclusions have complete alternative proofs in Paper17. The present comparison additionally verifies their named original auxiliary routes, with the published inputs distinguished above. This does not certify the later effective-group algorithms, general determinant-image formulas, or abelian-polarization monodromy families. It also does not create a second proof-unseen reconstruction of these original chains.


### audit/paper17_auxiliary_public/LITERATURE.md

# Literature and public auxiliary scope

The two hook-module descriptions are known results: Peel (1971), Theorem 2, printed p. 142, together with Propositions 1 and 4, pp. 136–138, and augmentation/quotient duality. The primary theorem and its proof on pp. 142–145 were read. The public appendix gives the exact attribution and makes no novelty or independent-reproof claim for these statements.

Seven distinct auxiliary results are now stated and proved in Appendix A: natural/dual SL3 cohomology, normal transvection blocks, a symplectic reflection obstruction, connected projection fibres, independent restriction images in dimension n>=3, a normalized elliptic trait, and the exact characteristic-two coordinate generating set. These have complete targeted author and root proof checks. There is no additional main-reconstruction credit merely because they are now public. The finite-group arguments are elementary and add no classification input.

The projection proof uses the full statements and proofs of Stacks Lemma 29.54.4 (035I), Lemma 58.11.2 (0BQL), and Lemma 33.8.6 (0364), all previously read at their exact primary pages. The additional bibliography rows in this revision are Peel, 035I, and 0364; 0BQL was already cited.

Seven other auxiliary conclusions were already contained in, or directly implied by, the completed public image theorems. Their mapping records explicitly distinguish group membership from the particular geometric route of the original source. The separately frozen original-chain comparison supplies its own targeted status; no conclusion is used to certify an unseen proof.

The bounded primary-literature queries and candidate scope comparisons are recorded in audit/pn_original_chain_inventory/LITERATURE.md and its source manifest. No priority claim is made for the elementary auxiliary formulations. The classification and ordinary-curve inputs examined for the old source route are not added to the public main proofs.

Two unchanged original programs were fully inspected and rerun in the separate original-chain audit. Their finite corroboration and exposure limitations remain as recorded there; this public integration adds no computation or distinct-method claim. No foreign source files were copied into the workbench or this audit directory.

## CP15 primary-source and bounded-literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/paper10_uniform_push/LITERATURE.md

# Literature and exact scope of the ample-difference result

The result is a formal consequence of the already fully checked ordinary-index-zero sharp-curve theorem, the positive-index bound, and a two-component nodal degeneration. No priority claim is made. The bounded searches in search_log.json cover arXiv/journals/author pages, ECCC, and Hexagon. They did not produce an exact matching theorem; absence of a search hit is not evidence of novelty.

After the new author proof was frozen, a statement-only register comparison found that the earlier scope remark rem:DE-A3-positive-index-gate already warns that a Neron-Severi-rank-one obstruction can prevent decomposition into index-zero ample summands. It does not state the ample-difference theorem or explicit numerical range. This is credited as an anticipated construction whose precise sufficient range is now made explicit and proved, not as a new underlying deformation mechanism. No adjacent unchecked original proof was opened for this comparison.

The main admitted input is Paper10's exact a=0 odd-degree theorem. The new result applies to the same fixed surface, assumes an actual ample ordinary-index-zero N, and requires M^e tensor N^-1 ample. It proves defect two there and eventually in e. It does not show a(M)=0 classes always exist, nor prove restricted-cup rank at least two at a prescribed sharp source. The actual uniform determinant nonvanishing question remains open.

For the explicit numerical bound, the public proof uses EGM Proposition2.22 p25 (effective finite-kernel line bundles are ample) and Theorem9.11 pp131-133 (chi(L)=L^2/2 and deg(lambda_L)=chi(L)^2, including the degenerate case). Their full proofs and the immediate2.20-2.21 chain pp23-25 were read. A direct Riemann-Roch argument also proves the needed discriminant inequality, so the new public proof imports no additional Hodge-index or Nakai-Moishezon statement.

Biswas-Hanumanthu's author PDF Theorem2.1 and full proof pp1-3 were opened as nearby ampleness literature. Its direct local download returned503; no source-file hash is invented. Knutsen-Lelli-Chiesa-Mongardi's arXiv abstract concerns nodal and Brill-Noether geometry on general abelian surfaces; only abstract/metadata were read. Achter-Casalaina-Martin's introduction and TheoremA pp1-2 concern foundations of characteristic-two Pryms; only that scope was read. Neither result is imported into the new rank proof. Downloads and their exact scopes are recorded outside the public files.

The author and root froze separate complete statement-led derivations before seeing each other's proofs; both use the nodal-union method. The direct RR numerical refinement was written afterwards and is labeled accordingly. No globally pristine, different-model, or different-method claim is made. No new finite computation is required by the universal proof.


### audit/paper8/LITERATURE.md

# Co-Lie obstruction literature

Recorded 2026-11-23T03:20:36.305351+00:00. Search and source comparison by GPT-6 Astra Pro, effort not exposed.

- Searched general terms co-Lie non-split multiplicative type, representation lifting Z/p^2, Godeaux Serre Proposition15, and the named authors on arXiv and publisher/author pages.
- Bergh–Rydh May2 2019 PropositionB.4 gives the derived character-module formula. The earlier April17 author version numbers it B.3; this is a version distinction, not a published correction.
- Serre1958 Section20 Proposition15 pp50–51 gives free complete intersections of every positive dimension, crediting Godeaux. Its entire proof and quotient remark were read in the primary scan. The geometric existence result is known.
- Stasinski2020 Theorem6.2 pp12–13 gives the p>=5 transvection obstruction. It applies to GL by the same determinant-free proof. The manuscript's p2/p3 classification was not inferred from this theorem. Sah1974/1977 and Ginosar2001 were traced as classification leads; full original sources remain a gate.
- Antieau–Bhatt–Mathew2021 Theorem1.2 p2 and Section6 p18 give smooth projective approximation of classifying stacks preserving Hodge classes. Their method is closely related, but their theorem does not state the End(V)-coefficient co-Lie surface assertion.
- Petrov2025v2 Lemma10.5 pp62–63 computes a split cotangent complex for the p-torsion of an abelian scheme; Corollary10.7 pp65–66 produces liftable p+1-dimensional examples with nondegenerate conjugate spectral sequence. The source was read and its hypotheses distinguished.
- Bounded Hexagon query `site:hexagonmath.org co-Lie OR representation lifting` returned no exact theorem; a representation-theory listing was irrelevant. Bounded ECCC query `site:eccc.weizmann.ac.il group representation lifting` returned no pertinent primary result. These negative results are search limitations, not a priority claim.

Status: individual ingredients are known and credited; the exact synthesis and explicit degree-|Gamma| surface realization were not located in this bounded search. No priority claim is made. The paper proves the conditional representation-to-surface theorem; its separate statement-only main check remains pending.


## Dated completion update: 2026-11-23T13:05:05.944278+00:00

The complete GL/SL/Sp prime-field congruence-section classifications now have a separate 572-line statement-led reconstruction, a separately frozen root reconstruction, and postfreeze comparison. Earlier own p>=5/rank-one exposure and the root's explicit-matrix packet exposure are disclosed. The complete symbolic proof replaces the former small-prime mathematical gate; original-program verification remains a distinct scope. All previous geometry reconstruction and full comparison remain credited.

Postfreeze primary reading of Stasinski arXiv:1907.09878v2 introduction and full Section6 verifies its explicit attribution of the exact special-linear list to Sah1974 Theorem7. Singla's institutional thesis printedp3 gives the exact general-linear list and credits Sah1977p22 and Ginosar2001. Detinko–Flannery–Hulpke arXiv:1611.05921v4 Theorem2.5 and complete surrounding proof pp4-6 were read; its proper-supplement statement is not conflated with splitting. These establish known status; no priority claim is made. Original Sah/Ginosar full texts were not obtained through the attempted primary publisher routes, so original-page reading is not claimed. Exact source hashes, access failures and reading scopes are recorded in audit/congruence_split_clean/primary_sources_postfreeze.json and its immutable literature record.

The current paper contains complete elementary proofs and all-prime general-linear surface consequences. The obsolete pending phrases above are retained as historical notes dated03:20, not current gates.


## 2026-11-23T13:15:38.599597+00:00 — bounded recent AI-lab context

OpenAI (2026, October6), *Fontaine–Mazur modularity at the prime2*, commit4eaee8754825, Theorem1.1 p1, was read directly in the primary PDF (SHA3c8797c7d468cdcccbfedf719c9a758a083954ba3c3005975736eb911d26a636). Full extracted introduction pp1–3 and the page1 image were inspected. Its assertion concerns continuous irreducible odd two-dimensional representations over an algebraic closure ofQ2, unramified outside finitely many primes and deRham at2 with distinct Hodge–Tate weights; its conclusion is modularity up to Tate twist. It is neighboring characteristic-zero context only, not a congruence-section or co-Lie proof input. The external proof was not audited. The bounded queries, cached-source provenance and failed fresh web PDF fetch are in opening_correction_and_ai_context.json. No closer co-Lie/congruence result was identified in those returned queries; no completeness or novelty inference follows.

Root completed all572-line proof comparison and unchanged original-program verification, recorded in audit/congruence_split_root/complete_comparison.json. The original separate JSON certificate files were absent; the unchanged original program regenerated and checked their algebraic identities, not their equality to unavailable files.


### audit/ramification_next_push/LITERATURE.md

# Bounded primary-literature comparison for the later-wild extension

The exact searches, access scope and primary file hashes are in `LITERATURE_and_sources.json`. The author derivations were frozen before this follow-up.

Smith, H. (2023). Ramification in division fields and sporadic points on modular curves. *Research in Number Theory, 9*, Article17. https://doi.org/10.1007/s40993-023-00424-2 . Author version1810.04809v4, pp1--2, Theorem1.1 p2, directly reread. Its scope is elliptic curves over number fields, torsion-point valuations and ramification in their point/full division fields. The canonical-subgroup formulas are already credited precisely in the current paper. This work supplies important prior valuation context but does not, by its stated theorem alone, supply the actual varying-base mixed comparison construction or the full filtration-character recovery statement.

Anema, A. S. I., Top, J., & Tuijp, A. (2018). Hesse pencils and3-torsion structures. *SIGMA,14*,102. https://doi.org/10.3842/SIGMA.2018.102 . Primary Introduction and Theorem1.1 pp1--2 reread. Hesse-pencil preservation of symplectic3-torsion is classical; the public curve uses characteristic-zero generic fields, within that theorem's characteristic-not3 hypothesis. Its exact local defect is established by the displayed cubic and fourth-root calculation.

Bondarko's general finite-level extension theorem remains the already credited finite-flat context, not an asserted exact mixed threshold. The corrected status of Hoshi's tame-blind theorem is retained from the earlier literature correction; no uncorrected version is used.

Four bounded searches were made, followed by the two primary-source checks above. These checks distinguish the stated results and do not establish priority. No claim that the new formulas have no earlier occurrence is made.

## CP16 primary-source and bounded-literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/paper10_remaining_push/LITERATURE.md

# Finite-field polarizations and eventual generic rank

## Proved scope

Every mixed abelian surface in characteristic two that has a finite-field model admits an ample line bundle of ordinary index zero. This refers only to the ordinary polarization block; the Euler characteristic need not be odd. Combining this construction with the already proved ample-difference theorem gives generic curve defect two in every sufficiently large system |M^(3e)| for every positive-index ample M on that surface. The qualitative statement permits arbitrary M after extending the surface to a larger algebraically closed field.

If the pair (A,M) is defined over F_q, q=2^f, a=a(M)>0 and m=ceil(2a/f), the complete explicit sufficient range is e>1+4q^m/2^a. This does not claim an optimal threshold, all smaller degrees, existence of an index-zero class on every mixed surface without a finite-field model, or uniform nonvanishing of the actual first-variation determinant.

## Classical inputs and exact primary reading

Edixhoven, van der Geer and Moonen supply the theorem of the cube and its pullback consequence (Theorem2.7/Corollary2.8 and proofs, pp19–20), multiplication formula (Corollary2.12 and proof, p21), canonical finite-group-scheme factors (Lemma4.44/Proposition4.45 and following paragraph, pp67–68), Cartier-dual Frobenius–Verschiebung identities (Proposition5.19 and proof, pp79–80), abelian identities and iterations (Proposition5.20/Section5.21, p80), and abelian isogeny duality (Proposition7.34 and proof, p111). These exact statements and complete local proofs were read by the author and separately by root. Section10.21 p149 was also read for the perfect-field splitting context. The primary file, URL and SHA are in sources.tsv. The integral polarization blocks and actual root are earlier fully checked Paper10 inputs, not newly reconstructed here.

The nilpotence estimate is elementary: a finite connected coordinate algebra of dimension h has augmentation ideal I with I^h=0. The public proof includes it. The numerical parallelogram is credited to the theorem of the cube, not to a differently numbered theorem of the square. Ampleness of the positive ample plus nef class is the standard ampleness criterion. The rank deduction is a formal consequence of the existing ample-difference theorem once the finite-field construction is established.

## Neighboring literature, with hypotheses preserved

Bergström, Karemaker and Marseglia (2023), Polarizations of abelian varieties over finite fields via canonical liftings, IMRN2023(4),3194–3248, DOI10.1093/imrn/rnab333, was opened in its author version. The introduction/TheoremA pp1–2 and Proposition2.10/Remark2.11/Theorem2.12 with their short proofs p7 were read. Their canonical-lift polarization classification has additional hypotheses; Theorem2.12 explicitly assumes odd q. It is neighboring context, not a proof input to the characteristic-two theorem here. No complete proof-chain audit of that paper is claimed.

The publisher's correction (2026), DOI10.1093/imrn/rnag227, published19November2026, corrects the quantifier in Proposition3.27 and replaces the counts in Example5.12. The primary publisher search-retrieval passage was read; full-page access failed, and no complete correction proof or local original hash is claimed. This is a known published correction, not a newly discovered error. No uncorrected assertion from that paper is used.

## Bounded search and verification status

The dated query log records searches of arXiv, journal/author sources, ECCC and Hexagon. No exact statement matching the ordinary-index-zero construction plus this explicit generic-rank bound was obtained. This bounded failure does not establish novelty or priority; no priority claim is made.

The author F/R proof was frozen before reading root's separate reconstruction. Root's proof was frozen from the clean target and the explicitly admitted earlier inputs. The author then froze a separate reconstruction of the stronger bound from its statement before reading root's proof. Reciprocal full comparisons passed. Both workers had related integral-polarization exposure; there is no globally pristine or different-model claim, and no claim of different methods for these related constructions. The superseded weaker bound is preserved only in audit records and is omitted from the public theorem.

No original program exists for this newly derived argument, and no rerun is invented. Its general proof is symbolic, not inferred from finite numerical experiments. Existing Paper10 local algebra certificates concern the older determinant reduction and do not certify the finite-field theorem.


### audit/all_wild_index_push/LITERATURE.md

# Bounded literature comparison for the arbitrary-index one-slope results

Five queries are recorded exactly in `LITERATURE_and_sources.json`. The primary arXiv pages and the already stored primary texts were opened again. Koch (2015), Sections2.1–2.2, pp.3–4, supplies the classical primitive-element/Frobenius-module correspondence and the rank relation. Smith (2023), author version Theorem4.4 and Corollaries4.5–4.6, pp.10–11, gives the elliptic canonical-subgroup valuation formulas and counts corresponding to the minimum-coordinate inputs. The present proofs establish their integral graph scaling, preservation of projected reduced supports by lying over, stable Frobenius dimensions, and comparison conclusions explicitly. The known correspondence and valuation formulas are not represented as new results.

The search does not establish priority or exhaust the literature. Search hits on unrelated uses of Newton slopes, primitive points or supersingular modular curves were not used as proof inputs. Smith's precise elliptic number-field scope is distinguished from arbitrary complete perfect-residue height-two Barsotti–Tate comparisons. All foreign papers and extracts remain under `external/`.

## Stronger uniform upper and larger exact bands

Nine further bounded queries, primary openings, exact retrieval records and access failures are recorded in `LITERATURE_uniform_and_band_followup.json`. Bondarko (2006), printed pp.661–662, Theorems A, B, A-prime and C, was reread with the complete-DVR, connected-target/unipotent-source and ramification hypotheses. Its generic-fibre almost-fullness and finite good-reduction criteria have a different conclusion from recovery of the special inertia character. The primary cached PDF retrieval is recorded; direct download failed and a later live opening redirected, so no new local PDF hash is asserted. Koch's classical primitive correspondence and Smith's elliptic Newton formulas retain the precise read scopes and PDF hashes of the earlier record.

The stronger uniform range and the extended band through coefficient 2p−1 are proved symbolically in the manuscript. The bounded search identified no exact matching statement, but does not settle novelty or priority. No source-search result was inserted as a new unverified proof input. The prior numerical band program retains its earlier finite scope and is not represented as checking the newly enlarged band. All foreign texts and retrieval extracts remain under `external/`.

## Half-square coefficient extension, 23 November 2026

The separately named reader's nine-query follow-up is preserved in `audit/all_wild_followup_independent/LITERATURE_DELTA_HALF_SQUARE.md` and `literature_delta_half_square.json`, with four exact source rows in `sources_delta_half_square.tsv`. It covers arXiv, journal and author primary sites, ECCC and Hexagon. The owner read the complete note and metadata; this does not represent an additional owner primary-proof reading. Tian's level-one canonical-subgroup statement, Hattori's tame-character statements, and the Liu–Moon and Iovita–Morrow–Zaharescu abstracts have the limited exact read scopes recorded there. No new result is imported into the proof and no priority claim follows. The separate scope addendum restricts the still-open next unit coefficient to r>=1, since r=0 is already settled by the complete prime-to-p theorem. The public piecewise band distinguishes unit coefficients from multiples ofp.


### audit/all_wild_followup_independent/LITERATURE_DELTA_HALF_SQUARE.md

# Bounded literature delta for the enlarged wild coefficient band

This is a narrowly scoped follow-up after the new half-square theorem
and its separate reconstruction were frozen and completely compared.
It does not replace the earlier Paper2 literature review or its full
primary-source checks. No novelty or priority claim is made. The
recent AI-laboratory context previously checked for Paper2 was not
repeated. No new published theorem is imported into the band proof.

## Search and access scope

Nine general mathematical queries were issued through the system1
search engine. They cover arXiv, journal sites, an author-site search,
ECCC, and Hexagon. Exact query strings, domain filters, opened URLs,
and retrieval-record hashes are in literature_delta_half_square.json.
The queries used p-divisible groups, torsion representations, truncated
Barsotti–Tate groups, finite flat groups, special inertia characters,
and ramification. They did not simply search the new manuscript's
invented theorem name or numerical expression.

Hexagon's homepage and advanced-search page were opened. The latter
loaded its form; no logged-in session or deposit was used. The
site-restricted indexed query produced no relevant exact-match item
in the returned results. ECCC's homepage and two indexed searches
were likewise inspected without a relevant match. These are limited
retrieval outcomes, not evidence of absence from either repository.

The publisher page for Hattori's article returned HTTP403 on direct
opening. Its author's own webpage and linked primary PDF were
successfully opened instead. Search-result mirrors and bibliographic
catalogues were discovery aids only; their author attributions and
metadata were not adopted as theorem evidence.

## Primary statements actually inspected

**Tian (2010).** The Annals publisher page and the primary PDF were
opened. The abstract and introductory statement of Theorem1.4
(printed p.956; PDF page3, including the publisher cover) were read.
For p>=3, this is a level-one canonical-subgroup theorem under a strict
Hodge-height bound, giving the expected rank and Frobenius-kernel
special fibre. This supplies neighboring canonical-subgroup context;
it is not an exact full-class character-index table. The search
function also returned scattered later proof matches, preserved in
the raw retrieval record. No complete proof reading is credited here.

**Hattori (2008).** The author's webpage entry and linked May9,2007
preprint were opened. The abstract, introduction, Theorem1.1 and
Corollary1.2 (author PDF pages2–4) were read. They connect tame
characters with the Abbes–Saito ramification filtration of finite flat
groups without an absolute-ramification restriction. These are
relevant established background on tame characters. The inspected
statements do not give the present half-square coefficient range or
its actual mixed lower constructions. This delta does not repeat or
upgrade the earlier Paper2 full Hattori-source reading.

**Liu and Moon (2020).** The arXiv v4 abstract and metadata were read
from the primary arXiv page. The result concerns relative crystalline
representations with Hodge–Tate weights in [0,1] arising from
p-divisible groups in the small-ramification range e<p−1. No proof
was read in this delta. Its hypotheses and conclusion differ from
uniform recovery of the special inertia character at wild indices.

**Iovita, Morrow, and Zaharescu (2022).** The primary arXiv v1 abstract
and metadata were read. The stated setting is an abelian variety with
good reduction over a finite unramified extension of Q_p, and the
abstract describes torsion-point ramification, including conditions
for tame p-torsion fields. No proof was read in this delta. This is
related point-field work, not the full potentially-good filtration
comparison or the new coefficient interval.

No inspected statement supplied the exact assertion
nu_F(p,k(p−1)p^r)=r+2 for p>=5, r>=0, p not dividing k and
2<=k<=(p²−1)/2. This means only that no such matching statement was
found in the listed retrieved spans. The theorem continues to be
presented with its proved dependencies and without a priority claim.

## Recommendation for the paper and records

Retain the existing literature and precise primary-input citations.
The new theorem is an extension of the already developed primitive
chain and residual-character argument. A short dated bounded-search
note in the literature record is enough; no additional mathematical
input or new public related-work claim is required. Preserve the
separate actual upper and existential lower quantifiers, the different
values for coefficients divisible by p, and the still-open next unit
coefficient and arbitrary-index formula.

## References

Hattori, S. (2008). Tame characters and ramification of finite flat
group schemes. *Journal of Number Theory, 128*(5), 1091–1108.
https://doi.org/10.1016/j.jnt.2007.05.006
Author preprint: https://www.comm.tcu.ac.jp/~shinh/HA/hasse-arf.pdf
Author listing: https://www.comm.tcu.ac.jp/~shinh/

Iovita, A., Morrow, J. S., & Zaharescu, A. (2022). *Ramification of
p-power torsion points of formal groups* (arXiv:2205.04608v1).
https://arxiv.org/abs/2205.04608v1

Liu, T., & Moon, Y. S. (2020). Relative crystalline representations
and p-divisible groups in the small ramification case. *Algebra &
Number Theory, 14*(10), 2773–2789.
https://doi.org/10.2140/ant.2020.14.2773
Primary arXiv version read: https://arxiv.org/abs/1902.06546v4

Tian, Y. (2010). Canonical subgroups of Barsotti–Tate groups.
*Annals of Mathematics, 172*(2), 955–988.
https://doi.org/10.4007/annals.2010.172.955
Primary PDF: https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p04-p.pdf


### audit/all_wild_followup_independent/literature_delta_half_square_scope_addendum.md

# Scope qualification for the bounded half-square literature delta

The phrase "still-open next unit coefficient" in the final recommendation
of LITERATURE_DELTA_HALF_SQUARE.md refers to the wild cases r>=1 at
k=(p²+1)/2. The case r=0 is already settled by the complete prime-to-p
character-index theorem. The coefficient lies beyond the new displayed
band for every r, but that does not make the r=0 problem open.

This is a wording qualification only. The original literature note,
its manifest, the frozen mathematical proofs, and their hashes are
unchanged. The bounded searches add no proof input, independent-proof
credit, priority claim, or claim of absence of prior work.

## CP17 primary-source and bounded-literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/paper10_no_zero_class_author/LITERATURE.md

# Literature and exact mathematical scope

## Conclusion

The construction is a precise application of classical monodromy, theta descent and quotient-polarization arguments. Achter and Pries supply full symplectic monodromy in the exact genus-two, p-rank-one, characteristic-two stratum. Chai is a primary source for its small-genus input. EGM §11.24 already discusses the general obstruction obtained by quotienting a principally polarized variety with endomorphism ring Z by a prime-order subgroup, and explicitly notes inseparable-polarization phenomena in positive characteristic. No priority claim is made for this framework or for the present refinement.

The exact proposed consequence for the current project is stronger than absence of a principal polarization: there is a mixed surface with NS(A)=Z[L], chi(L)=2 and ordinary/local indices (1,0). Hence every ample class t[L] has a=1+v2(t), b=v2(t), so no ample ordinary-index-zero class exists. It does not refute the curve-rank prediction or establish the remaining uniform determinant. The finite-field-model theorem remains a separate positive result. The example necessarily lies outside that descent scope.

## Primary proof inputs actually inspected

The exact source table is sources.tsv. Achter–Pries Theorem4.5 and its proof chain pp12–15 were read, with characteristic conventions p3 and the passage from stacks to a scheme family pp17–18. Chai §§2–4.4, pp292–298, and Remark4.7 p301 were read from the published primary PDF; its deeper cited inputs are not claimed independently reconstructed. The author corrected PDF could not be downloaded (403). Its advertised split-group qualification in Lemma3.2 is satisfied by the actual split symplectic group used here.

Pries's short guide, Example2.2, Lemma3.1, Propositions3.2–3.3 and the genus-two table (preprint pp2–4,6) give the exact mixed BT1 decomposition and alpha2 subgroup, for arbitrary characteristic p. EGM Theorem8.10 and Corollary8.11, pp116–117, were read with their full proofs. The special alpha2 theta-extension splitting was explicitly derived after reading the statement of Fact8.7, so it is not labelled a source-unseen reconstruction. EGM §§7.22–7.26 and11.2–11.3 supply the exact integral NS statements; §11.24 and Proposition11.25 supply the classical neighboring quotient construction. Riemann–Roch Theorem9.11 was already checked in earlier work.

## Bounded search

Searches used general web, arXiv, author sites and journal sites, ECCC, and the specified Hexagon domain hexagonmath.org. Queries included “abelian surface p-rank one polarization”, “abelian varieties without separable polarization”, “Neron-Severi rank one p-rank one alpha2 quotient”, and the domain-restricted combinations in query_log.json. The resulting primary candidates with direct overlap were opened/read as recorded above. A recent finite-field polarizations paper was found as neighboring context; it was not used as a proof input and its full proof has not been claimed read.

Hexagon returned unrelated complex-geometry, Hodge-theoretic or arithmetic constructions; ECCC returned coding/computation papers with incidental abelian references. Those hits are not evidence for a characteristic-two polarization theorem. Initial queries to hexagon.com and hexagon.axiommath.ai used incorrect domains and are excluded from Hexagon coverage. Correct hexagonmath.org queries were then performed. No exact ordinary-index refinement was located in this bounded search, which establishes neither novelty nor absence from the literature.

## Verification boundaries

The author conditional proof was frozen before opening the new primary proofs. The later alpha2 addendum is explicitly post-statement exposure. The root's separately frozen full construction has now been completely read and compared; its relative-Frobenius factorization supplies an alternative actual line bundle. Its alpha2 extension proof uses the same cocycle calculation as the author's addendum, so no distinct-method claim is made for that auxiliary. No original project program exists for this newly formulated existence question, and no finite computation is substituted for a theorem. The root source comparison is complete and passed. The new theorem and full alpha2 lemma are integrated in the public manuscript; global adoption remains separate from this author record.

## Exact published seed and completion addendum

The publisher PDF of Pries–Zhu2012 was obtained and both author and root directly read printed pp711–712, including the full local proofs of Lemmas2.6–2.7 and Example2.8. Its binary hash and PDF-page offset are recorded in sources.tsv. The monodromy-to-End/NS deduction is explicitly credited as classical, including Chai Corollary4.2. EGM12.8–13 are read at their full named proofs; the public proof includes the Gram-lattice finite-generation detail. The elementary alpha2 extension splitting is a classical special case with a complete cocycle proof, not a new general finite-group theorem. No original attached program or empirical certificate applies to this new exact class-existence question. The independent reconstruction scopes are owned by the root event table; this author table contains targeted comparisons only.


### audit/boundary_point_field_push/LITERATURE.md

# Bounded literature follow-up: boundary normal forms and proper point fields

Date: 23 November 2026 UTC. Reader: GPT-6 Astra (ChatGPT Pro mode), same model; effort not exposed; no human. This is a bounded context update after the mathematical freezes. It supplies no additional proof hypothesis and makes no priority claim.

## Search and access

Three targeted search queries were used: (1) `"torsion" "point fields" "canonical" ramification`; (2) `"p-divisible groups" "torsion" "ramification" comparison`; and (3) `"Fields of definition" "torsion" Ozeki Yoshida`. The first two used primary arXiv/journal domain filters, and the third sought the already cited 2026 preprint. Numdam and arXiv landing pages were then opened. Raw retrieved foreign material is retained only under `external/boundary_point_field_push/bounded_search_results.json`.

The complete returned primary landing-page/abstract text was read. This delta does not claim a new full-paper reading of these sources. Earlier precisely recorded full theorem/proof inspections remain available in the preceding Paper2 records.

## Exact scope of nearby sources

- Fargues, L. (2011). *La filtration canonique des points de torsion des groupes p-divisibles*. Annales scientifiques de l’École Normale Supérieure, 44(6), 905–961. https://doi.org/10.24033/asens.2157 . The Numdam abstract describes a Hasse-invariant bound producing a canonical break in the Harder–Narasimhan filtration of truncated Barsotti–Tate groups over mixed-characteristic valuation rings. It does not state the present transported relative point-field obstruction. No assertion about the contents of the entire paper is inferred from its abstract.
- Smith, H. (2023). *Ramification in division fields and sporadic points on modular curves*. Primary author version: https://arxiv.org/abs/1810.04809v4 . The abstract describes elliptic supersingular torsion valuations and necessary ramification for exact-order points. Paper2 already credits the exact valuation theorem at its previously checked scope. This lookup supplies no arbitrary-group field-comparison theorem.
- Ozeki, Y., & Yoshida, M. (2026). *Fields of definition of p-torsion points of elliptic curves and their ramification*. https://arxiv.org/abs/2609.06554 . The primary abstract explicitly begins with elliptic curves over Q_p and describes first-level individual and full torsion fields, plus ramification of full division fields. This differs from an actual exchanged central comparison of two height-two groups over the tame good field. The earlier detailed Paper2 comparison of §§2.1,2.3 and Proposition3.25 remains the exact published/preprint-statement comparison; it is not broadened here.
- Phillips, T. (2026). *Local monodromy of 1-dimensional p-divisible groups*. Journal of Number Theory, 283, 259–284. https://doi.org/10.1016/j.jnt.2025.11.008 ; https://arxiv.org/abs/2102.08999v2 . The primary abstract explicitly assumes a complete discrete valuation ring of characteristic p. Its comparison of Lie and ramification filtrations is therefore neighboring equicharacteristic context, not an input to the present mixed-characteristic proof.

## Proof inputs and limits

The new proposition uses the preceding paper’s proved central Newton formula, rationality of canonical p-points, actual point stabilizers, and elementary lower-break estimate (the classical local-field framework of Serre, Chapter IV, §1). The proof re-establishes every supporting implication needed for the new degree bound: full first-level rationality; Galois relative multiplication fibres; equality of transported actual point fields; exact cyclic break only at a prime-to-p coordinate valuation; and next-level integrality. It never assumes that a higher point field is Galois over the original base or that a p-divisible numerator yields an exact break.

No exact match for this conditional proper-level assertion was identified in the bounded returned material. That limited observation is not a literature-exhaustiveness or novelty claim. The normal form and point-field bounds remain necessary conditions; actual existence, impossibility, and the boundary character index remain open.


### audit/boundary_point_field_push/LITERATURE_v3_supplement.md

# Translation-persistence literature supplement

This record supplements, and does not modify, the frozen three-query boundary literature note. The new proof uses only the rational-first-torsion Galois representation, an explicitly written binomial identity, and the previously compared proper-level degree bound. It imports no new theorem from the literature.

The author conducted the additional bounded eight-query context search recorded in `audit/boundary_point_field_clean/MONOTONE_LITERATURE_DELTA.md` and `monotone_literature_delta.json`. This integrating worker read those records in full after all mathematical freezes. Their exact source-read scope belongs to the named author; this is not a claim that the integrating worker has newly read those primary papers. Caruso–Liu's torsion semistable ramification bounds and Ozeki's crystalline-restriction theorem are context only. No novelty or literature-exhaustiveness claim is made.

The necessary-only limit is unchanged: the new lemma excludes the final cyclic-p alternative at r=1, leaving exact point-field degree p^6. No actual realization or impossibility of that remaining comparison is claimed.


### audit/paper10_spreading_public/LITERATURE.md

# Eventual rank on every mixed pair: exact literature scope

Date: 23 November 2026. Reader/author: GPT-6 Astra (ChatGPT Pro mode), /root/papers3_4. No human review.

## Classification

Theorem1.3 proves eventual generic defect two for every ample positive-ordinary-index mixed abelian-surface pair over any algebraically closed characteristic-two field. Its application-specific inputs are the previously completed finite-field eventual theorem, the zero-index exact formula, and the positive-index upper bound. The new proof combines these with classical spreading, relative Serre vanishing, proper derived cohomology and rank-minor openness. These general family facts are credited as known inputs; the full semilinear stable-iterate argument and their application are written out.

The result is existential for each pair. It does not give a uniform threshold across pairs, determine every smaller degree, or prove the actual first-variation determinant. The geometric-generic example with no index-zero ample class is compatible with this eventual theorem. No computation is used as evidence for a global geometric conclusion.

## Exact primary reading

The author opened/read the exact statements and complete displayed local proofs of Stacks Tags0B91,0B9T,0B5T,02O1,0D4E,062Y and09MT. The first five support perfect cohomology, Euler characteristic, relative Serre vanishing and base change. Tag062Y gives the locally principal fibrewise Cartier criterion, including flatness of the universal divisor. Tag09MT supplies descent of ampleness; its finite-section-cover proof is read with the usual replacement by a common positive power of the ample bundle. The source byte records are source_downloads.json and ampleness_source_addendum.json; all foreign HTML is outside the deliverables under external/paper10_spreading.

Root independently read the exact standard spread tags01ZM,0B8W,0C0C,081F and the overlapping cohomology statements. Its eleven-row source table and full reading manifest are audit/paper10_spreading_root/sources.tsv and primary_reading.json. The full local proof of0B91 reduces to its cited general perfect-cohomology theorem; neither reader claims to have reconstructed all recursive Stacks dependencies.

## Bounded follow-up searches

Root's complete dated twenty-one-query log is audit/paper10_spreading_root/LITERATURE.md. It covers arXiv, journal/author primary candidates, ECCC, Hexagon at hexagonmath.org, and neighboring recent AI mathematics. Root read only the first two pages of each versioned Terzi preprint listed there; those are context, not proof inputs. The public recent-AI context remains the previously inspected Zou source, with its different higher-dimensional scope stated explicitly.

This author additionally issued these exact queries:

1. System2: `"abelian surface" "p-rank" "ample" "generic curve"`.
2. System2: `"abelian surface" "generic" "Frobenius" "rank" characteristic two`.
3. System2: `site:arxiv.org "abelian surfaces" "p-rank" divisors`.
4. System2: `site:eccc.weizmann.ac.il "abelian" "p-rank"`.
5. System2: `site:arxiv.org "p-rank" "ample divisors"`.
6. System2: `"p-rank" "linear systems" "abelian surfaces"`.
7. System1: `site:hexagonmath.org "abelian" "Frobenius"`.
8. System1: `"p-rank" "ample" "abelian surfaces" generic curves`.
9. System1: `site:arxiv.org "p-rank" "divisors" "abelian"`.

An initial query to hexagon.com used the wrong domain and is excluded from Hexagon coverage. Correct domain coverage is query7 and the root log. The returned results were largely adjacent questions about finite-field endomorphisms, reductions, moduli strata and Frobenius splitting. The primary Cambridge reductions paper and the Zou author page were located as neighboring work; no new proof input was taken from these search results. The exact eventual theorem was not located in the consulted spans. This bounded observation does not establish an exhaustive absence result or a priority claim.

Primary Stacks searches and direct opens were also used to locate the exact Cartier and ampleness lemmas. Foreign retrieval JSONs and HTML bytes remain in external/, excluded from the returned archives. No author was contacted.


### audit/paper10_spreading_root/LITERATURE.md

# Eventual curve rank by finite-field specialization

Search and reading date:23November2026, approximately15:30–15:38UTC.
Reader:root, GPT-6 Astra (ChatGPT Pro mode), effort not exposed; no human.

## Exact result and literature classification

The result proved in the new packet is eventual generic defect two for
every mixed characteristic-two pair (A,M) with positive ordinary index.
It is a consequence of the already fully checked finite-field theorem,
the old positive-index upper bound, and classical spreading and
semicontinuity. It requires neither a finite-field model of the original
pair nor an index-zero ample class on the original surface. It supplies
an existential threshold depending on the pair, and leaves smaller
degrees, uniform bounds and the actual first-variation determinant open.

Spreading, relative Serre vanishing, perfect cohomology/base change and
rank-minor openness are classical. Their exact statements are credited
as such. The elementary stable-iterate argument and the application to
this curve-rank problem are written in full. The bounded searches below
did not locate the exact eventual mixed-surface conclusion among their
returned material; that is a record of search scope, not an exhaustive
literature classification or a priority assertion.

## Query log

Each numbered item is an actual query issued during this extension.
The retrieval collections, including incidental irrelevant results,
are stored under external/paper10_spreading/ and are excluded from ZIPs.

1. System2: `abelian surface characteristic p generic ample curve p rank asymptotic specialization finite field`.
2. System2: `site.stacks.math.columbia.edu relative Serre vanishing cohomology base change ample invertible sheaf projective morphism`.
3. System2: `site.stacks.math.columbia.edu abelian scheme spreading out finite presentation limit line bundle`.
   These found the classical Stacks sections and broad neighboring material;
   no exact mixed-surface eventual-rank match appeared in the returned set.
4. System1: `"p-rank" "ample" "abelian surface" "generic"`.
5. System1: `site.stacks.math.columbia.edu "proper" "cohomology and base change" "locally free"`.
6. System1: `site.stacks.math.columbia.edu "Limits of schemes" "smooth" "proper" "invertible"`.
7. System1: `site.hexagonmath.org "Frobenius" "abelian"`.
   These verified exact cohomology inputs and returned Hexagon algebraic-
   geometry listings, including the already known Deligne exposition,
   and the neighboring Zou author page. No exact new rank claim was
   identified from those results.
8. System2: `site.stacks.math.columbia.edu "If $f$ is smooth" "there exists an" "32.8"`.
9. System2: `site.arxiv.org "p-rank" "linear system" "abelian surface"`.
10. System2: `site.eccc.weizmann.ac.il Frobenius rank abelian surface`.
11. System2: `site.hexagonmath.org "generic" "stable rank"`.
    These located the smoothness limit section and largely unrelated
    results. The indexed arXiv/ECCC/Hexagon queries did not supply an
    exact match; no completeness of those indexes is assumed.
12. System1: `"p-rank" "abelian" "linear system"`, with arxiv.org domain filter.
13. System1: `Frobenius curve rank polarization`, with hexagonmath.org and eccc.weizmann.ac.il domain filters.
    Results exposed Terzi's curve computations and more broad background.
    Returned results included sources outside the requested domains;
    the record does not treat the domain filters as an exhaustive search.
14. System2: `"On the p-rank of curves" 16841 arxiv author`.
15. System2: `"On the p-rank of singular curves and their smooth models" arxiv`.
    The exact arXiv author versions were then opened, downloaded and their
    first two pages read. The second work is a forward continuation of
    the first; the inspected scopes concern complete intersections,
    normalization and surfaces with pg=q=0, not the present mixed
    abelian-surface eventual theorem.
16. System2: `site.stacks.math.columbia.edu "reduced" "locally constant" "locally free" "cohomology" "base change"`.
17. System2: `site.stacks.math.columbia.edu "family of curves" "first cohomology" "locally free"`.
    These returned classical Grauert/base-change expositions. The public
    proof instead gives the finite-free-complex constant-rank argument
    directly, using the already opened Stacks perfect-base-change input.
18. System2: `"10.1090/proc/16841" Terzi`.
19. System2: `"On the p-rank of singular curves" "102" Terzi 2025`.
    Publisher metadata for the second work identifies Finite Fields and
    Their Applications103(2025),102578, DOI10.1016/j.ffa.2025.102578.
    The AMS DOI landing page was unavailable to the web tool, so the
    first source row cites the exact inspected arXiv version instead.
20. System1, recency365days: `Frobenius p-rank abelian surfaces mathematics AI OpenAI`.
21. System1, recency365days: `"On the p-rank of curves" "specialization" Terzi`.
    The returned set added neighboring p-rank, Brauer/Neron–Severi and
    Frobenius-distribution work, but no exact theorem at the present
    scope. The existing Paper10 recent-AI comparison remains separately
    sourced; this search gives no additional mathematical proof input.

## Primary inputs actually used

The Stacks Project Authors.(2026), exact tags01ZM,0B8W,0C0C,081F,
02O1,0B9T,0D4E and0B91. Source citations, complete used statement/proof
reading scopes, HTML-byte hashes and URLs appear in sources.tsv and
primary_reading.json. Section30.16(Tag0B5S) also records the complete
affine relative-Serre proof used to check Tag02O1. The deep general
cohomology theorem cited in the displayed proof of0B91 remains an
explicit classical input; this is not a reconstruction of all Stacks
dependencies.

The exact new theorem is not credited to these general lemmas. They
provide the standard family formalism, while the finite-field curve-rank
input and the original positive-index upper bound carry the application.

## Neighboring work and access qualifications

Terzi,S.(2024). *On the p-rank of curves* [arXiv:2001.03310v3].
https://arxiv.org/abs/2001.03310v3. Complete preprint pp1–2 read,
including the introductory statements and Definition3. These compute
Frobenius for complete intersections and discuss pg=q=0 surfaces.

Terzi,S.(2025). *On the p-rank of singular curves and their smooth models*.
*Finite Fields and Their Applications,103*,102578.
https://doi.org/10.1016/j.ffa.2025.102578.
Inspected author version:https://arxiv.org/abs/2309.06901v2,
complete pp1–2 only. The normalization sequence and generalized Fermat
families are context; no proof from this article is used here.

Both versioned PDF opens failed in the web tool but both complete
binaries downloaded successfully with urllib; hashes are in sources.tsv.
Their other pages were not read and are not certified. The publisher
page for the second work returned403 on direct open, but primary
publisher metadata and introductory text were returned by search.

Zou's2026 author page was reopened at
https://www.math.uni-bielefeld.de/~hzou/papers/qfpsv/.
Its abstract/introduction were compared at lines0–56; the earlier
Paper10 exact reading of its relevant main-results and acknowledgement
sections remains the prior record. The paper concerns higher-dimensional
primitive symplectic varieties and provides context, not this rank proof.

No author was contacted. No foreign source file or extraction is a
deliverable; only these own citations, reading records and hashes enter
the workbench.

## CP18 primary-source and bounded-literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/boundary_deformation_push/LITERATURE.md

# Divisorial Cartan calculation: bounded literature and source scope

Recorded 23 November 2026. Reader: GPT-6 Astra (ChatGPT Pro mode),
`/root/blind_ramification`; effort not exposed; no human. This note concerns
the supporting universal-deformation valuation calculation. It makes no
priority claim and does not settle the boundary character index.

## Classical inputs actually used

The complete author reading of Strauch's arXiv:math/0611109v1, pp.7–15,
supplies the universal mixed-characteristic rings, regular basis parameters,
finite flat transitions, the integral level action fixing the deformation
base, and the full-level product definition. The exact regular-parameter
statement is Theorem2.1.2(i), p.9; the proof and transition presentation occupy
pp.9–11, and the action is in §2.2, pp.12–14. The product quotient is a unit
by its reduction and the height-two leading term. The valuation and fixed-field
calculations are proved in full in the new argument, not imported from that
source.

The author also read Carter–Strauch's 2020 preprint through Theorem2.1.2,
Remarks2.1.3 and the beginning of Proposition2.2.3. That narrower reading was
only a cross-check of the ring and action setup. The author did not read its
full parameter proof at that stage. The frozen exact access, URL, binary hash,
and reading scope are in `primary_scope01.json`.

After the proof freezes, a separate same-model primary-source check read
Strauch pp.7–15 in full, the published Carter–Strauch pp.436–440, and original
Drinfeld pp.566–567 and570–573 at the precise recorded scopes. The parameter
locator in the published Carter–Strauch paper is Proposition2.2.3(i), p.439,
with proof pp.439–440; Theorem2.1.2, p.437, alone is not the explicit
basis-parameter statement. The original author's narrower exposure is not
retroactively enlarged. The integrating author read that complete source
report on23November2026, not all those primary pages afresh.

The exact check and five primary-source rows are preserved in
`audit/boundary_deformation_sources/source_check01.md`, `source_check01.json`,
`manifest01.json`, and `sources.tsv`. Strauch's journal publication is2008,
but the consulted proof locators refer to the2006 arXiv version. The public
bibliography identifies that consulted version explicitly.

Only the special-fibre leading term cT^(p²), c nonzero, is required. A linear
coordinate change over the algebraically closed residue field normalizes c
to one. No exact mixed-characteristic polynomial p-series is used. Strauch's
equal-characteristic Appendix5.1.1 is not an input; it was not opened by this
author. The source checker inspected it only to confirm that scope boundary.

## Search scope and limits

The six initial queries, exact first accesses and incidental search-result
exposure are preserved in `primary_scope01.json`. They concern Drinfeld
full-level parameters, nonsplit Cartan quotients, ramification and
inseparable residue extensions in the Lubin–Tate tower. No new local original
B proof or program was opened in this work.

Four later bounded queries were made after the proof freeze:

1. `"fierce" "cyclic" ramification extension Wewers residue field`
2. `"Semistable models for modular curves of arbitrary level" Weinstein arxiv`
3. `"Lubin-Tate" "Cartan" "inseparable"`
4. `"Lubin-Tate" "monomial valuation" ramification`

The first two led to primary abstracts/metadata for Wewers's work on fierce
cyclic extensions and Weinstein's semistable models. Only the opened
Weinstein introduction and contents, pp.1–5 of arXiv:1010.4241v3, were read;
no later proof or intersection-multiplicity theorem was used. The earlier
author-hosted Weinstein PDF open had timed out and was not counted as a
reading. The last two queries had weak exact coverage and introduced no
additional proof input. Their result snippets, including irrelevant
nonprimary results, were not treated as verified theorems.

These searches place the calculation in a known deformation and ramification
setting. They do not establish that the particular weighted fixed-field
calculation is new. They provide no evidence for an actual perfect-residue
boundary realization. No foreign PDF, scan or extracted primary text is
included under `audit/`; all such files remain under `external/`.

## References

Carter, A., & Strauch, M. (2021). Lubin–Tate deformation spaces and fields of
norms. *Journal de théorie des nombres de Bordeaux,33*(2),433–458.
https://doi.org/10.5802/jtnb.1166

Drinfeld, V. G. (1974). Elliptic modules. *Mathematics of the USSR-Sbornik,
23*(4),561–592. https://doi.org/10.1070/SM1974v023n04ABEH001731
The consulted English scan has translation copyright1976; the source check
records this bibliographic distinction.

Strauch, M. (2008). Deformation spaces of one-dimensional formal modules and
their cohomology. *Advances in Mathematics,217*(3),889–951.
https://doi.org/10.1016/j.aim.2007.07.005
Consulted proof: author preprint arXiv:math/0611109v1 (2006),
https://arxiv.org/pdf/math/0611109.

## Final scalar and specialization context

The final public version also includes the completely compared scalar calculation and the conditional contact proposition. The separate scalar literature search and sources are in `audit/boundary_scalar_clean/LITERATURE.md` and its handoff manifest. The owner made a further two-query scalar-context search recorded in `scalar_literature_delta.json`; it established no exact priority comparison.

Bisatt, Furio, and Lombardo (2026), *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, arXiv:2603.04021v2, Theorem 1.3, p. 2, is contextual only. This owner read the official metadata and all of p. 2; root separately read pp. 1–4 and the start of p. 5. Its base is Q_p, p>7, with a nonsplit-Cartan-normalizer residual-image hypothesis and an additional bound in the higher-defect case. It is not an input to the weighted fixed-field proof.

The Stacks Project, Section 15.113 (Tag 0EXQ), especially Lemma 15.113.3 and Remark 15.113.6, was opened and its complete displayed section read by this owner. It supplies the finite separable complete-DVR degree formula and multiplicativity used in the conditional contact proof. Exact retrieval and primary binary hashes are in `final_context_source_reading.json`. Root's comparison with Carter–Strauch, Section 2.2.8 and Corollary 2.2.9, p. 443, distinguishes their one-coordinate height-one prime from the present valuation positive on both parameters. These additions make no priority claim.


### audit/boundary_scalar_clean/LITERATURE.md

# Scalar fixed-field literature and exact proof inputs

The universal full-level deformation rings, basis parameters, integral actions and product identities are classical Drinfeld theory, read in the exact original/Strauch/Carter–Strauch scopes recorded in `../boundary_deformation_sources/source_check01.md`. The original English Drinfeld proof of Proposition4.3 and the published Carter–Strauch parameter proof were additionally inspected. The separate scalar reconstruction does not count these inputs as newly proved or independently reconstructed.

The new scalar calculation uses the explicitly admitted last-layer result and proves two further actual fixed-field steps by controlled invariant approximation. The fixed fields, exact error estimates and construction-only1300 corollary have complete frozen proofs and reciprocal comparisons. No global torsion-index or perfect-residue construction conclusion follows.

A bounded post-freeze search made ten exact queries across arXiv, journal/author channels, ECCC and Hexagon; exact strings and five preserved retrieval records are in `literature_delta01.json`. Wewers’s original boundary-ramification paper was opened, including its Proposition3.1 statement and associated Corollary3.2. Its upper triangular determinant-one boundary stabilizers provide neighboring geometry. Fargues’s primary abstract was opened for skeleton/canonical-subgroup scope. A recent Hexagon primary on the non-split Cartan curve of level121 was opened through its local level-p² torsion-section and Cartan statements. The retrieved proof windows are partial and are not credited as full proof verification. No statement from these contextual items is a new proof input.

No exact level-four formula at weights(p²+p+1,p²) was identified in the inspected spans. This records the search outcome only. The three context records have no claimed PDF-binary hash; their saved retrieval hashes are explicitly separated. No public priority discussion is proposed.


### audit/boundary_specialization_clean/LITERATURE.md

# Bounded source and exploratory handoff: specialization and uniform rank

Recorded 23 November 2026 by /root/blind_lefschetz, GPT-6 Astra
(ChatGPT Pro mode). Reasoning effort is not exposed; no human has checked
this work. This is a dated bounded record, not a comprehensive literature
review or a novelty claim.

## 1. Conditional specialization at absolute index 260

The 299-line author attempt froze at 16:24:49.816490 UTC before any new
deformation proof was opened. It proves a contact-order restriction under
an actual unequal-character comparison and a specified local chart with
unit leading factor. It also supplies an elementary Kummer example
distinguishing downstairs transversality from upstairs contact. These are
supporting results with disclosed preceding point-field inputs. They do
not settle occurrence or exclusion of the remaining boundary pair.

The Stacks Project Authors. (2026). *Extensions of discrete valuation
rings*, Section 15.113, especially Lemma 15.113.3 and Remark 15.113.6
(Tag 0EXQ). https://stacks.math.columbia.edu/tag/0EXQ

Named reader: /root/blind_lefschetz. The entire displayed primary section
was opened and read. The proof uses the degree formula for finite
separable extensions of complete discrete valuation fields and
multiplicativity of ramification indices. Linked foundational lemmas
were not separately opened. The saved hash identifies a web-retrieval
JSON, not a PDF. Root's later independent read is recorded in its own
comparison, not credited as an additional read by this worker.

The discovery query was:
`site.stacks.math.columbia.edu complete discrete valuation ring finite extension ramification residue degree equality ef`.
Its output is saved in the foreign retrieval directory. Only the primary
Stacks section was opened for this task; other search snippets were not
imported as inputs. The standard deformation-ring sources named in the
statement packet were not newly opened by this worker.

Root's 81-line precheck froze at 16:27:19.418160 UTC before reading the
author proof. Root then read all 299 author lines and recorded a targeted
comparison PASS. The author subsequently read all 81 root lines and the
freeze manifest and recorded reciprocal PASS. Both checks preserve the
conditional scope. Neither is entered here as new main-theorem
independence. Root's full scalar statement was received while pending,
but neither its proof nor its conclusion was used in the author attempt.

## 2. Earlier negative uniform-threshold followup for Paper10

The preserved status in `audit/paper10_uniform_followup/` asks whether the
pair-dependent eventual sharp-rank theorem can be made uniform in
polarization invariants (D,a,b), or whether its exact small-degree range
can be enlarged. No such theorem, counterexample, or strict sufficient-gate
reduction was obtained. The counterexample concerning varying open subsets
only rules out an abstract compactness inference; it is not an example
of bad ranks on abelian surfaces. Curve unions, isogeny propagation and
bounded cohomological generation retained explicit unresolved steps.

Hoshi, Y. (2021, March). *A note on torsion points on ample divisors on
abelian varieties* [Author manuscript, 11 pp.].
https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1909revised.pdf

Named reader: /root/blind_lefschetz. All extracted lines 0–548 of the
11-page primary manuscript were read in two retrievals, including the
proofs of Theorem 1.7, Corollary 1.8, and the Section 2 results through
Corollary 2.8. Theorem 2.7(ii) supplies a new-ordinary cyclic degree-three
cover in characteristic two. Its full-Jacobian torsion avoidance does
not assert avoidance in the subgroup prescribed by an ambient abelian
surface. No uniform threshold or divisor in a prescribed complete
system is inferred. Referenced Mumford and Raynaud proofs were not
newly opened. The source is context only, not a new rank-proof input.

Two bounded searches concerned ordinary Prym covers and
Frobenius/cohomological generation. Their exact query objects and outputs
are preserved as `search_01.json` and `search_02.json` in the earlier
foreign retrieval directory. Only Hoshi was opened as a new mathematical
source during that push. No original program was run or computational
verification claimed. The record makes no exhaustive-search or priority
claim and is not a replacement for earlier broader literature records.

The actual status freeze is 16:05:42.163252 UTC. Its first save attempt
failed because the filesystem was full, after the outcome had already
been reported to root. The freeze must not be backdated to the 16:05:01
review cutoff. This negative push contributes no new mathematical
completion, independent proof, or strict-gate progress event.

## 3. Integration boundary

The raw mathematical event table contains only two targeted supporting
checks, for the conditional contact proposition and the elementary
specialization example. The crosswalk has no invented original REGISTER
identity. The source table contains the two primary items above, with
named-reader scope and explicit retrieval-JSON hash types. No public or
global file was edited by this worker. The 135-page divisorial v2 visual
record is preserved; final combined-PDF visual coverage is delivered
separately after the owner's stable build.


### audit/boundary_scalar_root/LITERATURE.md

# Scalar fixed fields and specialization: bounded supplementary search

Date: 23 November 2026. Reader: /root, GPT-6 Astra (ChatGPT Pro mode),
effort not exposed; no human verification. This supplements the author and
separate source-checker records, rather than replacing or enlarging them.

## Exact searches performed

The following fifteen queries were actually submitted through the public
search service. The first twelve used system1; the last three used system2.
The first three are preserved as a raw retrieval under external/ only.

1. `"Lubin-Tate" "Cartan" "ramification" residue field`
2. `"Drinfeld" "scalar" "inseparable" deformation`
3. `"Lubin-Tate deformation" "divisorial" valuation`
4. `site:arxiv.org "Lubin-Tate" "scalar" ramification`
5. `site:hexagonmath.org "Lubin" "Cartan"`
6. `site:eccc.weizmann.ac.il "Lubin Tate" ramification`
7. `"Lubin Tate deformation spaces and (φ,Γ)-modules" ramification Carter Strauch citations`
8. `"Drinfeld" "fierce ramification" scalar`
9. `site:openai.com mathematics research 2026 ramification` (recency365days)
10. `mathematics research ramification` (domains openai.com; recency365days)
11. `"Lubin–Tate" "ramification" scalar Cartan` (domains arxiv.org, numdam.org, jtnb.centre-mersenne.org)
12. `"Carter" "Strauch" "fields of norms" "cited"`
13. `site:hexagonmath.org Lubin Tate scalar ramification`
14. `site:eccc.weizmann.ac.il Lubin Tate`
15. `site:openai.com "math" "research" "2026"`

Queries1–3 led to Carter's author-hosted thesis and Anschütz's lecture notes.
Queries4–6 returned broad Lubin–Tate and local-class-field-theory results;
the search response had weak exact-domain coverage, so no absence conclusion
is drawn for arXiv, Hexagon or ECCC. Queries7–12 returned Carter–Strauch's
journal record, its published PDF and a forward-citation listing for Drinfeld,
as well as Esnault–Kindler–Srinivas on fierce ramification. The latter and the
forward-citation snippets are discovery material only, not proof inputs.
Queries13–15 returned the Hexagon level121 manuscript and current OpenAI
mathematics-release pages. The broad cross-domain results of query10 were
not mistaken for official OpenAI results; query15 supplied official pages.

Following the Hexagon manuscript's references led directly to the primary
arXiv page and PDF of Bisatt–Furio–Lombardo. This is a backward citation follow
from the new neighbor; query12 and the Drinfeld forward listing are the
separate bounded forward-citation search. No exhaustive citation census is
claimed. ECCC yielded no relevant theorem verified in this bounded search.

## Primary material actually read by root

### Carter–Strauch (2021)

The complete extracted printed pages442–445 of the published paper were read
in two bounded outputs, including Section2.2.8 and all of Corollary2.2.9
and its proof on p443, Proposition2.2.10 and its proof through p445, and
the beginning of2.2.13. The first page starts within the proof of2.2.7;
no claim of reading that whole proposition is made in this addition.
The PDF is the already checked published binary with SHA256
e194a1b20f822346ad5c2961230d74963330ee4c77578b595e35156d365b063b.

The field of2.2.8 is obtained by completing at the principal height-one
prime generated by the first level coordinate. Corollary2.2.9 computes
e=(q-1)q^(n-1) for that tower; q=p when the coefficient ring is Z_p.
Our valuation is positive on both level coordinates. The cited formula
therefore concerns a different valuation and is not substituted into the
scalar calculation. Its exact statement supplies the new public comparison.
The journal landing-page request at archive.numdam.org returned502; the
published PDF already present was the source actually read.

### Carter (2015)

Opened the author-hosted80-page thesis, title page and abstract, Section4.1
(printed41–45) in the displayed retrieval, and the statement and beginning
of the proof of Proposition4.5 on p46. The latter proof was not read in full
and is not used. The principal-prime tower and its ramification calculation
agree with the neighboring published setup at the level needed for comparison.
The thesis date is August2015; a search-engine freshness date was not treated
as its publication date. Binary SHA256:
d4485e5ef75a9f126b3c2f515d45cdd989890545bf44d07ea24f39afa683058a.

### Bisatt–Furio–Lombardo (2026)

Opened the arXiv metadata and the42-page version2 PDF. Read all printed
pages1–4 and the beginning ofp5 from the primary displayed text, including
the entire Theorem1.3 on p2. Its hypotheses include p>7, an elliptic curve
over Q_p and residual image in a nonsplit Cartan normalizer. The higher
semistability-defect case includes an additional explicit inequality
p>sqrt(n_0)+1, where n_0 is determined by v(j) or v(j-1728). The theorem is
contextual, not an imported proof of any current weighted-valuation result.
Its base-field/residual-image scope does not settle the boundary at e_K=260.
No whole-paper proof verification is claimed. Binary SHA256:
e3a0da5a4f709d91126d7b638e71847b4e9d59037e7615f4eacca73a543db83b.

### Recent Hexagon and AI context

Opened the full displayed landing page for Jaswal's level121 preprint,
the PDF first three pages through the displayed part ofp3, and the located
passages around Lemma12.6 (p35) and Proposition9.5 (p27). These are limited
contextual excerpts, not a complete check of the manuscript or even of its
local Section8. The claim discussed in its introduction concerns rational
points on a global nonsplit-Cartan modular curve; it is not the present
mixed-characteristic scalar fixed-field theorem. A direct local PDF fetch
returned403, so no binary hash is claimed for that unsuccessful fetch.
The separate checker records its own more extensive local-source scope.

Opened and read the official OpenAI page *Sharing AI progress in mathematics*
(6October2026, update15October2026). It describes a release of mathematical
manuscripts and proof artifacts, not a ramification theorem. The paper's
existing exact citation of OpenAI's Fontaine–Mazur manuscript remains its
mathematical AI-research comparison; no claim that this broad release proves
or verifies our theorem is made. The other search-only AI pages are not
treated as mathematical evidence.

### Finite DVR extensions

Independently opened and read the complete displayed Stacks Section15.113
(Tag0EXQ), especially Lemma15.113.3 and Remark15.113.6. It supplies the
degree formula and multiplicativity used in the conditional contact
argument. The linked foundational lemmas were not separately opened.
This is a known input, not an independent new theorem.

## Conclusion and limits

The exact scalar equality, controlled approximation argument and contact
condition are proved in the separately frozen proofs and compared in full.
The literature checks identify neighboring results with different valuations
or base fields. They do not establish priority, exhaust all literature, prove
the existence of a tame quotient or perfect-residue specialization, or settle
the general first-boundary comparison. No earlier source is copied into the
returned archive; all fetched binaries and text extractions remain external.

## References

Bisatt, M., Furio, L., & Lombardo, D. (2026). *Explicit p-adic Hodge theory
for elliptic curves and non-split Cartan images* (arXiv:2603.04021v2).
https://arxiv.org/abs/2603.04021v2

Carter, A. T. (2015). *Lubin-Tate deformation spaces and (φ,Γ)-modules*
[Doctoral dissertation, Indiana University].
https://math.hawaii.edu/wordpress/atcarter/wp-content/uploads/sites/24/2018/10/Thesis42.pdf

Carter, A., & Strauch, M. (2021). Lubin–Tate deformation spaces and fields
of norms. *Journal de théorie des nombres de Bordeaux,33*(2),433–458.
https://doi.org/10.5802/jtnb.1166

Jaswal, M. (2026). *The rational points of the non-split Cartan modular curve
of level121* (Hexagon2611.00255v2; PDF dated18November2026).
https://hexagonmath.org/2611.00255v2

OpenAI. (2026, October6; updated October15). *Sharing AI progress in mathematics*.
https://openai.com/index/sharing-ai-progress-in-mathematics/

The Stacks Project Authors. (2026). *Extensions of discrete valuation rings*
(Section15.113, Tag0EXQ). https://stacks.math.columbia.edu/tag/0EXQ

## CP19 primary-source and bounded-literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/full_cartan_level4_clean/LITERATURE_SCOPE.md

# Source scope for the separate reconstruction

The exact classical universal-ring/action, torsion-initial-form, controlled-lifting and preceding scalar results are admitted as I1–I4 of the frozen packet. Their primary reading scopes are already recorded in audit/boundary_deformation_sources/manifest01.json and the prior public propositions. This worker makes no new primary-source or bounded-search completion claim for this target. The target owner/root maintain the new exact-scope literature follow-up. The same-code author arithmetic rerun was performed only after both proof freezes and is not an independent computational method. The event is one separate reconstruction of the whole supporting packet; no original REGISTER identity is invented.


### audit/boundary_noncartier_followup/LITERATURE.md

# Bounded literature delta: a known cyclic quotient and specialization

## Exact known attribution

The cyclic quotient used in the frozen reconstruction is already Example5.10 of Liedtke and Matsumoto (2018), printed pp.24–25. Root identified that exact source after both proof freezes and reciprocal comparison. The present worker then independently opened the publisher HTML and the exact published PDF. The public fragment credits Liedtke and Matsumoto before the construction and in the example heading. There is no claim that this quotient construction is new. The arbitrary complete-DVR adaptation, local Cartier-index calculation and explicit index260 specialization are presented as direct applications of that known model, without a priority claim.

Liedtke, C., & Matsumoto, Y. (2018). Good reduction of K3 surfaces. *Compositio Mathematica,154*(1),1–35. https://doi.org/10.1112/S0010437X17007400

The published PDF has36 PDF pages including the initial publisher page. Printed24–26 are PDF25–27. This worker read complete Example5.10 on printed24–25 and the complete statement/proof of Proposition5.11 on printed25–26, in HTML and PDF text. PDF24 (printed23) was also read while locating the offset; HTML supplied the adjacent complete5.9 and5.12 arguments. Referenced Kiraly–Lutkebohmert and Wewers source proofs were not opened by this worker. Proposition5.11 is contextual, not an input to the local calculation.

The minimal cyclotomic base in the published example must not be confused with the index260 adaptation. No augmentation-exponent assertion was imported. For the latter base, the direct action would give the augmentation ideal (zeta−1)(t,U), with normalized t-exponents325 and326 at p5; neither this observation nor a global quotient-smoothness criterion is used in the proof.

## Standard proof inputs actually checked

The Stacks Project, Section10.157 (Tag031O), was read in full over its displayed mathematical portion, including every statement and proof through Lemma10.157.6. Exact individual tags0567 (regular rings are normal) and031T (height-one intersection) were opened and read in full. These are ordinary commutative-algebra background for normality and the unit identity used in the Cartier-index constraint. Linked prerequisite lemmas were not all reopened. The previously read Tag0EXQ finite-DVR background retains its earlier scope; it was not newly reread.

## Broader primary context

Lorenzini, D. (2013). Wild quotient singularities of surfaces. *Mathematische Zeitschrift,275*,211–232. https://doi.org/10.1007/s00209-012-1132-7

The publisher abstract and bibliographic data were opened. The author's own dated3December2012 PDF was then opened, with extracted lines0–377 read: abstract/introduction, Lemmas2.1–2.2 and proofs, Theorem2.3 and its proof, Section2.5 and Theorem2.6 through the initial part of proof(c). This is a bounded read of author PDFpp1–6, not a full article verification. It supplies context on wild quotient surfaces, invariant rings and divisor/discriminant groups. No theorem from this article is needed for the explicit quotient proof.

Lorenzini, D., & Schroer, S. (2023). Discriminant groups of wild cyclic quotient singularities. *Algebra & Number Theory,17*(5),1017–1068. https://doi.org/10.2140/ant.2023.17.1017

The arXiv abstract and version1 PDF (arXiv2101.08090v1,21January2021) were opened. The displayed opening lines0–217 were read, covering the abstract and introduction through part of printedp4. This includes the distinction between ramification in codimension1 and only at the origin, and introductory theorem statements; their later proofs were not read. The journal PDF URL returned no readable text through the web tool. This source is context only; equal-characteristic quotient classifications are not substituted for the mixed-characteristic construction.

## Search scope and access limits

Seven new general mathematical system1 queries covered arXiv, journal domains, an author domain, ECCC and Hexagon. Two preceding system2 queries located the exact Stacks background. Exact query text/domain filters and saved retrieval hashes are recorded in literature_manifest.json. Domain-filtered repository searches returned some off-domain or broadly related results; these were not treated as repository-specific evidence. A direct ECCC homepage opening timed out. Hexagon's homepage and advanced-search page opened; the exact indexed query returned broadly related works, not an exact checked source for this model. No login, deposit or browser automation was used. These bounded searches do not establish absence from a repository or prove priority.

The exact Liedtke–Matsumoto attribution is a positive identification from the primary article, not an inference from a failed search. The prior Paper2 recent-AI context was not repeated. All original proof bytes are preserved; the later known-source record is separate. The actual first-boundary torsion occurrence/exclusion question remains open, and this auxiliary known-model application receives no automatic main-gate movement credit.


### audit/boundary_noncartier_root/LITERATURE.md

# Literature delta: cyclic quotients and specialization

Date: 2026-11-23. Reader: /root, GPT-6 Astra (ChatGPT Pro mode), effort
not exposed. No human verification. This is a bounded follow-up, not an
exhaustive search or a priority assessment.

## Exact searches

The following queries were issued after the independent root construction
had frozen and after the complete reciprocal proof comparison began.

1. `"augmentation ideal" "regular" "cyclic" quotient Kiraly Lutkebohmert`
2. `"wild" "quotient" "augmentation" "principal" regular local ring`
3. `"Group actions of prime order on local normal rings" site:msp.org`
4. `Wewers regularity quotients wild cyclic actions principal augmentation ideal 2010`
5. `"Good reduction of K3 surfaces" "pdf" Liedtke Matsumoto 2018`
6. `"good_reduction_of_k3_surfaces.pdf"`
7. `"Group actions of prime order on local normal rings" Kiraly Lütkebohmert author`

Queries 1–2 used the stronger search engine; 3–7 used the routine engine.
The search hits identified the Király–Lütkebohmert criterion and Wewers's
earlier criterion. The forward-citation search then located the EXACT
cyclic quotient construction in Liedtke–Matsumoto. Secondary search hits
were discovery aids only; every mathematical attribution below was checked
in the primary journal or author-preprint text. The author-name query did
not supply a separate author-hosted copy. Broader channel checks, if made
by another named reader, remain in that reader's own report.

## 1. Exact known construction

Liedtke, C., & Matsumoto, Y. (2018). Good reduction of K3 surfaces.
*Compositio Mathematica, 154*(1), 1–35.
https://doi.org/10.1112/S0010437X17007400

Journal HTML:
https://www.cambridge.org/core/journals/compositio-mathematica/article/good-reduction-of-k3-surfaces/9296E569F340B0BA56C0293FF6F5CCB3

Journal PDF, obtained from its citation_pdf_url metadata:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9296E569F340B0BA56C0293FF6F5CCB3/S0010437X17007400a.pdf/div-class-title-good-reduction-of-k3-surfaces-div.pdf

PDF SHA256:
`a9eea2543ab715542b2e17899dfdd182cc58e483351861a6c3ac82bdcb4d11b0`.
Local external-only path:
`external/normal_quotient_sources/liedtke_matsumoto2018.pdf`.

Root read the full published Example 5.10, pp. 24–25, and Proposition
5.11 with its full proof, pp. 25–26, first in the journal HTML and then
in the PDF. The entire printed pp. 24–26 were read; only the beginning
of Corollary 5.12's proof is covered by that PDF range. No full-paper
proof reading is claimed. The journal metadata confirms volume, pages,
authors and 2018 issue date; online publication was in September 2017.

Example 5.10 is exactly the weight-(1,-1) cyclic Kummer quotient:
sigma(varpi)=zeta varpi, sigma(x)=zeta^{-1}x, with invariant equation
z^p=pi u. The source explains normality, nonregularity, nonreduced
special fibre, the induced infinitesimal derivation and the nonprincipal
augmentation ideal. Its displayed base is Q_p(zeta_p). Our argument
uses this KNOWN model over a suitable further ramified complete base,
computes its local Cartier index, and exhibits the explicit arc and
normalized generic pullback at absolute index 260. Those elementary
consequences do not make the quotient construction new. The public text
must credit Liedtke–Matsumoto before introducing it. No correction of
their example is proposed.

The source's augmentation generators varpi^p x, varpi^(p+1) use its
minimal cyclotomic base. For the separately constructed e=260 base,
the unchanged general expression is (zeta-1)(varpi,x); at p=5 its
uniformizer exponents are 325 and 326. This distinction does not enter
the countermodel proof or its Cartier-index argument.

## 2. A known regularity criterion for the next attempted method

Király, F., & Lütkebohmert, W. (2013). Group actions of prime order on
local normal rings. *Algebra & Number Theory, 7*(1), 63–74.
https://doi.org/10.2140/ant.2013.7.63

Published PDF: https://msp.org/ant/2013/7-1/ant-v7-n1-p03-s.pdf
SHA256: `45b26d17f64f307b5664d62069db4c468218dfc7ca10f8fbd70bc83c3a85d09e`.
Local external-only path:
`external/normal_quotient_sources/kiraly_lutkebohmert2013.pdf`.

Root read the FULL printed pp. 64–69 in two bounded outputs, including
Theorem 2, Remark 3, Lemma 4 and its entire proof, Proposition 5 and its
entire proof, Proposition 6 and its entire proof, and both parts of the
proof of Theorem 2. Theorem 2 is stated on pp. 64–65. It implies that
for a prime-order cyclic action on a regular local ring, a principal
augmentation ideal gives a regular invariant ring. The proof passes
through a monogenous/free algebra using divided differences, then
faithfully flat descent of regularity. The classical descent inputs
quoted there were not separately opened afresh. The equal-residue-field
pseudoreflection equivalence has its extra hypothesis and must not be
silently used without it.

The arXiv landing page https://arxiv.org/abs/1001.1945 was read as
version/abstract metadata only. Its preprint title differs from the
published title. The journal text, not an abstract, carries the proof
reading above.

This criterion is a possible tool for investigating the actual Cartan
quotient at closed points. No claim that its augmentation ideals have
been proved principal follows from this source reading. In particular,
a generic graded-field calculation alone does not verify the local
regularity hypothesis along every admissible curve.

## 3. Related earlier criterion, statement scope only

Wewers, S. (2010). *Regularity of quotients by an automorphism of order p*
(arXiv:1001.0607v1). https://arxiv.org/abs/1001.0607
PDF: https://arxiv.org/pdf/1001.0607v1
SHA256: `ea4e2fd4d2d2e999ed030a5457ef703d4a03542ecfbeafb5c7a065b97e92cf58`.
Local external-only path: `external/normal_quotient_sources/wewers2010v1.pdf`.

Root read the introduction, §1.1 and the complete statement of Theorem
1.3 on p. 3 through the web-rendered PDF. The theorem assumes a regular
parameter pi, augmentation ideal (pi^delta), and the stated alternative
for sigma(pi)-pi. This is related context for the proposed local method.
Its complete proof was NOT read, and no fresh proof-verification credit
is claimed. The downloaded binary supplies a reproducible version hash.

## Attribution and research status

The model is known. Its exact numerical specialization and divisor-index
consequences were independently reconstructed before the primary example
was located, then compared in full. This exposure chronology changes
neither the known attribution nor the general boundary's open status.
The original proof freezes remain unchanged; this dated record adds the
literature identification. None of the downloaded source files or their
text extractions belongs in any returned ZIP.


### audit/boundary_noncartier_root/LITERATURE_CHART_FOLLOWUP.md

# Subsequent use of the known regularity criterion

Recorded 2026-11-23T17:33:07.207295+00:00. The earlier LITERATURE.md is preserved as the exact primary-reading/search record at its original stage. Its then-open proposed chart application has subsequently received complete separate derivations and reciprocal root/author comparison, recorded in audit/cartan_torus_root/ and audit/full_cartan_level4_push/. The external theorem remains Király–Lütkebohmert (2013), Theorem2 and Proposition5, pp64–69. Its proof was fully checked at the scope in that earlier record.

The new local argument verifies its augmentation hypotheses for the specified exceptional-torus Cartan charts. It establishes regular invariant local rings, a regular Cartier reduced vertical divisor, and the exact local p-power unit relation. This is a separately proved application; the source-reading event does not acquire additional independent mathematical credit. Further independent checking/public conversion may be recorded separately.

The known Liedtke–Matsumoto example still prevents promotion from arbitrary normal quotient models. The particular Cartan-chart result has extra proved local hypotheses. No proof reduces every surviving actual boundary torsion comparison to these charts. Thus the general first-boundary occurrence/exclusion question remains open.

Only current_events_v2.tsv and sources_v2.tsv are proposed for adoption; their first versions remain unchanged historical source-check records. The change clarifies the subsequent chart application and creates no duplicate event or source credit.


### audit/cartan_torus_clean/LITERATURE.md

# Cartan-torus reconstruction: exact primary input scope

The new local argument uses Király and Lütkebohmert (2013), *Group actions of prime order on local normal rings*, Algebra & Number Theory,7(1),63–74, DOI10.2140/ant.2013.7.63. Named reader /root/blind_lefschetz read the full displayed proof spans printed63–69, including Theorem2, Lemma4 and Propositions5–6, before freezing the separate local reconstruction. The published theorem, rather than a new assertion about all wild quotients, supplies regularity from principal augmentation and the monogenous free basis. Later article sections and the proofs in its Matsumura/Serre references were not newly read.

The publisher PDF at https://msp.org/ant/2013/7-1/ant-v7-n1-p03-p.pdf was independently opened; the XHTML endpoint failed for unsupported content type. One routine exact-author/topic search preceded that open. This is precise source verification, not a comprehensive fresh literature survey. The prior bounded wild-quotient literature and explicit Liedtke–Matsumoto known-model attribution remain in their separate records. No new priority or novelty claim is made.

The completed field theorem remains an explicitly admitted mathematical dependency. The public cross-first reordering was checked after reading the frozen root/BR chart arguments and is not counted as another independent reconstruction. The assertion is local to the specified actual exceptional torus; the general first-boundary occurrence or exclusion question is unchanged.


### audit/full_cartan_level4_push/LITERATURE.md

# Full-Cartan bounded literature follow-up

Observed UTC: 2026-11-23T17:07:48.547271+00:00

Four targeted queries, two search systems, followed the complete author proof freeze. The exact queries and retrieval hashes are in literature_delta01.json. The first pair had poor coverage; the stronger pair surfaced neighboring boundary ramification literature. Only the official arXiv abstract/version page for Wewers (2005), *Swan conductors on the boundary of Lubin–Tate spaces*, arXiv:math/0511434v1, was opened and read. No PDF proof or exact theorem from that source was adopted.

The present proof uses only the previously checked universal deformation/action inputs and the recorded controlled-lift lemma. Strauch, Carter–Strauch and Drinfeld remain credited at the exact versions/pages already checked. Carter–Strauch's one-coordinate height-one-prime valuation remains distinct from the two-positive-weight divisorial valuation. No new primary theorem is required by this extension.

The searches do not establish an exact published match, novelty, or priority. Raw retrieved foreign text remains under external/full_cartan_level4_push/, not inside this audit directory.


### audit/full_cartan_level4_push/LITERATURE_CHART.md

# Exact chart and known-model source delta

Recorded 2026-11-23T17:50:00.763658+00:00. Model: GPT-6 Astra (ChatGPT Pro mode); effort not exposed; no human.

The four-query full-Cartan context search and its retrieval/version limits remain frozen in LITERATURE.md and literature_delta01.json. This addendum adds no new search and no priority conclusion.

The actual local-chart argument uses Király, F., and Lütkebohmert, W. (2013), *Group actions of prime order on local normal rings*, Algebra & Number Theory,7(1),63–74, https://doi.org/10.2140/ant.2013.7.63. This worker fully read printed63–69: Theorem2 and its precise implications, Lemma4, Propositions5–6 and their proofs. The exact primary PDF hash and access scope are in chart_primary_scope01.json and sources.tsv. The imported input concerns principal augmentation, monogeneity/freeness and regular invariant rings. Every actual Cartan-chart principal augmentation ideal and local divisor calculation is proved in the new public text. The source does not supply that particular chart theorem.

The normal cyclic quotient used in noncartier_specialization.tex is the known construction of Liedtke and Matsumoto (2018), Example5.10, printed24–25. Its primary verification and related Lorenzini/Lorenzini–Schröer/Stacks scopes belong to the named readers in audit/boundary_noncartier_followup/public_handoff_manifest.json. This integrating worker read the full public proof and source report; no fresh full LM primary reading by this worker is claimed. The precise known attribution precedes the construction. The Cartier-index application and explicit index260 arc do not identify that ring with the Drinfeld Cartan quotient.

The separate Wewers2005 official abstract/version landing page was retrieved only as neighboring Lubin–Tate boundary context. No PDF theorem/proof reading or new proof input is inferred. Foreign PDFs and extracts remain under external/, not this packaged audit tree.

## Final finishing primary-source and literature records

The following records preserve named owner/root primary reading scopes. This metadata integration makes no new literature-verification claim. Original articles unavailable to the workers remain explicitly distinguished from later primary attributions.

### audit/general_to_cartan_root/LITERATURE.md

# Final bounded input-scope check

23 November 2026, /root, GPT-6 Astra (ChatGPT Pro mode); effort not exposed. This completes a source-scope check in the already assigned image-exclusion argument after Review15. It is not a new literature search or a restart of research.

Drinfeld, V. G. (1974). Elliptic modules. *Mathematics of the USSR-Sbornik, 23*(4), 561–592. https://doi.org/10.1070/SM1974v023n04ABEH001731. The already obtained English PDF is at https://www.mathnet.ru/links/5183a5fa878673db281ff375f6bf8a05/sm3735_eng.pdf, SHA-256 `95f17bfb606dd63c8068c4a257f080590f3ed349910e25aa2f96f15b707d63a9`.

Root read printed pages 570–573 completely in text extraction and inspected all four individual page images. The credited proof scope is the exact category and Propositions 4.1–4.3, including their complete proofs. The beginning of Proposition 4.4 was visible, but its full proof was not read in this follow-up. No new recursive reading of Section 1B or of the full paper is claimed.

The printed deformation category fixes the residue field. The scalar-compatible frame evaluation used in the final argument is therefore explained as a consequence of the coefficientwise proof: arbitrary coefficient vector spaces, degree-by-degree elimination with finitely many changes to each coefficient, rigidity, completeness, and the explicit primitive-factor and higher-level root-adjunction constructions. It is not attributed to a broader literal statement in the source. The exact verification is in `scalar_compatibility_primary_check01.json`.

The original Cartan chart and unit-factorization results remain over the original coefficient field. Algebraic and transcendental exceptional-torus residues are handled separately in the new proof; no assertion about arbitrary completed base change of wild invariant rings is imported. The abstract orbit and self-twist lemmas are elementary supporting results. No claim of priority is made for them, for the scalar-compatible consequence, or for the conditional image exclusion. Existing bounded literature records and known-result attributions remain in force.


### audit/general_to_cartan_push/LITERATURE.md

# Final input-scope record

This dated record completes the already-started image-exclusion check. It is not a new literature search or a research restart after Review15. No priority claim is made for the elementary orbit/self-twist arguments or the resulting actual-image obstruction. Existing bounded context searches and primary attributions remain unchanged.

Drinfeld, V. G. (1974). Elliptic modules. *Mathematics of the USSR-Sbornik, 23*(4), 561-592. https://doi.org/10.1070/SM1974v023n04ABEH001731. The already obtained English primary PDF has SHA256 `95f17bfb606dd63c8068c4a257f080590f3ed349910e25aa2f96f15b707d63a9`; exact URL, local external path and named-reader scopes are in `sources.tsv`. The precise part used is the category and complete Propositions4.1-4.3 on printed570-573. The beginning of4.4 is not a full-proof check.

The printed category fixes its residue field. Lemma20.23 derives the necessary arbitrary-residue scalar compatibility from its coefficientwise proof: arbitrary vector-space coefficient layers, degree elimination that modifies each fixed coefficient only finitely often, rigidity, compatible completeness, and the explicit primitive and higher division-root adjunctions. There is no tensor/infinite-product interchange or silent assertion that wild invariants commute with base extension. Root's exact primary verification is `audit/general_to_cartan_root/scalar_compatibility_primary_check01.json`; the owner read its complete report and the previously available primary text. This is targeted input verification, not a further independent main reconstruction.

The original chart theorem remains over k0=Fbar_p. The actual-image deduction evaluates one of those original rings even when the exceptional-torus residue is transcendental: in that case the map need not be local, and the proof uses the exact ring identity p=u*rho^N. The fresh179-line main reconstruction admits U and the earlier chart/normal-form/Newton inputs explicitly. It is not another independent proof of those inputs. The earlier algebraic-only and hinted general attempts remain separately qualified in their immutable handoffs.

The final necessary restriction excludes actual principal nonsplit-Cartan images and the irreducible-intertwiner tame self-twist case. It neither constructs nor excludes every first-boundary pair and does not decide the index. At p=5,e=260, the already proved mixed and uniform bounds leave3<=nu_min<=4.
