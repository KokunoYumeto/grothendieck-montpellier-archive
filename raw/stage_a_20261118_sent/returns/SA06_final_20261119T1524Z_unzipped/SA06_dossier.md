# SA06 — Théorie des motifs, part 2

## Consolidated dossier of cotes 14 and 15

**Assessment date: 19 November 2026.** This dossier consolidates every one of the **437 entries in the supplied NOTES_INDEX.tsv**, read against its corresponding transcription, together with the assigned Codex continuations and claims encountered in those texts. The mathematical record consists of the final item, claim, problem, reading and link tables. The narrative explains their structure and the findings that most change how these folders should be used. Earlier run identities survive in source-entry IDs; all cross-package mergers and compound redirects are documented in `MERGE_MAP.json`.

The folders preserve several distinct programmes, not a finished theory of motives with one recoverable definition. Cote 14 develops effectivity, a particular Albanese equivalence relation, proposed odd-cycle representatives, finite-field cycle arguments, a 1965 Lefschetz programme, Picard/Albanese correspondences, ampleness and local-cycle questions. Cote 15 develops normed Deuring categories and Brandt groupoids, Weil-number and CM-lattice constructions, real motivic gerbes, and the comparison of integral, crystalline, Betti and de Rham fibre objects. Reused algebra, analysis, topology and Lie-theory sheets contain substantial mathematics but have their own provenance.

Several conclusions govern the consolidation:

1. **The chosen cycle equivalence relation changes the theorem.** The 1965 letter's quotient by algebraic equivalence is stronger than the later cohomological standard-conjecture formulation. Its literal whole-cycle Lefschetz and affine-vanishing assertions have counterexamples. Numerical semisimplicity and cohomological hard Lefschetz do not remove those counterexamples.
2. **Integral inverses are a separate problem from rational inverses.** The Albanese H¹ inverse and the Picard/top-odd inverse are distinct questions. Recent counterexamples and parity obstructions address different sides; an isogeny argument supplies denominators, not an integral cycle for free.
3. **A band, a neutralization, a torsor and a chosen isomorphism are different data.** The scalar μ_n computation in the Deuring construction does not establish the whole gerbe. Frobenius invariance of classes does not establish coherent descent. Lang's theorem does not provide a canonical comparison in an arbitrary pro-category.
4. **There are exact own-publication matches.** They include the Brauer divisor-sequence argument, several SGA3/SGA4 passages, and Grothendieck's own correction of the naive generalized-Hodge formula. These matches are supported by theorem locators and hypotheses, rather than titles alone.
5. **The modern comparisons have a precise limit.** Nori–Ayoub comparison, Nori arithmetic descent and pure semisimplicity are substantial theorems in their specified settings. They do not identify every handwritten M, establish a general motivic t-structure, prove geometric connectedness, or solve the period and effectivity questions.
6. **Mathematical refutation does not decide the ink.** Every suspicious sign, exponent, quantifier and cancellation remains a scan alarm. No manuscript reading was changed in this run.

Each of these conclusions is developed below with exact claim IDs, scoped proofs and opened sources. A correction of an earlier note is not automatically a correction of Grothendieck: it may correct the note's quantifier, its context transfer, its source boundary or a literal transcription reading.

## Corpus, authority and coordinates

The original attached archive was unpacked once. Its already unpacked inner folders were used directly. The supplied `second_pass/` directory contains no checks for this part, so no second-pass reading was presumed missing or invented. The Pro and Codex texts are witnesses, and their disagreements are recorded. There are no manuscript scans. Images inspected during literature checking are pages of published sources, not images of the Montpellier manuscripts.

| Supplied indexed package | Indexed entries | Principal material |
|---|---:|---|
| MPL_14_002-044 | 97 | Effectivity, Albanese equivalence, Tate's trick, 1965 Serre letter; reused algebra and affine geometry |
| MPL_14_087-132 | 94 | Correspondences, ampleness, local cycle groups, Lefschetz and boundedness; SGA/EGA and group-scheme fragments |
| MPL_15_034-086 | 74 | Normed Deuring categories, quaternionic examples, Brandt groupoids, positive involutions; analytic leaves |
| MPL_15_087-138 | 110 | Weil numbers, CM lattices, real gerbes, Artin–Tate comparisons; Codex generator and analytic continuations |
| MPL_15_170-194r | 62 | Fibre-functor agenda, Brauer/cohomology fragment, polarization and comparisons; reused projectivity and Lie theory |
| **Total** | **437** | Every indexed entry has exactly one final verdict row |

The assigned Codex material is K14-02/03/04/05/06/08 and B15-01/02/03, K15-01/02/08. Those leads receive item and claim coverage as needed, but no invented NOTES_INDEX rows. A package boundary is not a mathematical boundary: the letter beginning at14/044 continues on045–047; Proposition 2.1 beginning at14/058 continues on059–061; the Deuring generator discussion at15/060–061 continues in B15-01 at063. Conversely, adjacent scans can be unrelated reused paper. Page numbers on a typescript, archival marginal numbers and scan numbers are kept separate.

The following table accounts for every folder in TOPIC.md while respecting the part boundary. Catalogue page totals are metadata, not counts of supplied mathematical leaves or authorial page totals.

| Cote | Catalogue topic | Catalogue pages | Treatment here |
|---:|---|---:|---|
| 10 | Catégories tensorielles | 197 | Other part; orientation only |
| 11 | Formalisme des correspondances | 57 | Other part; orientation only |
| 12 | Généralités, sous-groupes de Galois motiviques | 167 | Other part; no absent definition imported |
| 13 | Groupe de Galois motivique | 51 | Other part; orientation only |
| 14 | Cycles algébriques; Hodge, Tate, Lefschetz, Weil | 131 | Assigned Pro and Codex corpus consolidated |
| 15 | Théorie arithmétique; théorie de Galois des motifs | 227 | Assigned Pro and Codex corpus consolidated |
| 16 | Correspondences and Poincaré–Hodge algebras | 55 | Other part; particular external endpoints read for links |
| 18 | Motifs et théorie de Hodge | 61 | Other part; particular external endpoints read for links |
| 19 | Topos | 95 | Other part; orientation only |

The catalogue's 1965 date for cote 15, an administrative date on reused paper, or the date of a later publication is not assigned to every surrounding leaf. Exact dates are reported where the witness supplies them. In particular, the cote 14 letter is dated27 August 1965; the later letter to Mumford about the box-cycle obstruction is dated20 November 1968. First circulation and publication dates are separated in the reference audit.

### How to use the tables

`SA06_entries.tsv` is the closed coverage ledger: its source IDs are the supplied stable package-and-entry IDs. `SA06_items.json` merges the same objects, questions and readings while distinguishing historical assertions from ideas of earlier runs. `SA06_claims.json` records the author's claims and the explicitly labelled modern comparisons needed to judge the notes. Its `his_statement` is a brief transcription quotation or a transparent description of an incomplete clause, not a silently reconstructed theorem. Its `statement` gives the strongest formulation justified after the stated qualifications.

Line locators refer to physical, one-based lines of the specified supplied complete transcription unless an individual external page file is explicitly named. Pro fragments in the original notes sometimes used different per-page numbering; those locators are not passed off as physical lines of the combined file. The source-read audits identify the files and ranges inspected. For an external endpoint the archive, internal path and exact range are retained, with hashes where materialized.

The claim field `status_on_pages` describes the historical source and any explicit literal defect; `class` describes the literature fate. They answer different questions. A conjecture may still be open on the page but refuted later, or a cancelled argument may have a valid later theorem. ClassA means an exact match in his own subsequent publication; B an established later development; C a partial or qualified development with its remaining gap; D an unmatched development after the recorded bounded search, without a novelty inference; E standard mathematics or an independently checked standard correction; F a formulation not identifiable from the supplied words. Historical first-publication priority is not manufactured to justify classE.

`SA06_problems.json` is an index of *his open steps*, including questions later solved, refuted or corrected. Its count is not a count of currently open research conjectures. The historical formulation, a plausible modern formulation, the current source evidence and the historical reason for abandonment are separate fields. Where no source explains why work stopped, the record says so; a mathematical gap is not offered as a biographical explanation.

The proof supplements and exact programs carry the arguments that cannot fit in a short ledger cell. `CHECK_EVENTS.tsv` distinguishes actual source comparison, targeted proof checking, independent re-proof, exact computation, background use and refutation. An opened bibliography entry is not a checked proof. The ranked directions specify future tasks and their first finite steps; none is presented as newly developed research from this consolidation.

## The folders in their surviving mathematical order

The following sections follow each sequence's objects and questions before drawing cross-project comparisons. Locally authored counts and integration notes have been replaced by the final global counts at the end of this dossier.

## Cote 14, early segment: consolidated overview

**Assessment date:** 19 November 2026. **Run:** SA06-part2/cote 14_early.  
**Scope:** all 97 NOTES_INDEX entries of MPL_14_002-044; complete assigned Pro transcription and doubts; complete Codex K14-02, K14-03 and K14-04 transcriptions and their leads. The Codex leads do not receive extra NOTES_INDEX verdict rows.

### What this segment contains

The segment is not one continuous treatise. In its surviving order it contains the fourth part of an account of motivic structure, titled *Structure d'effectivité*; a sign calculation for an elliptic Poincaré correspondence; a systematic development of “équivalence d'Albanese”; a tentative transposition and odd-cohomology comparison; *Astuce de Tate sur les cycles décomposables*; the complete letter to Serre of 27 August 1965 once its Codex continuation is joined; and the opening of *Sorites sur VA, Picard, Albanese*. Reused English algebra and French affine-reflection typescripts occur between the handwritten leaves. Their mathematical assertions have been checked, but their presence is not evidence that Grothendieck authored them.

The Pro package retains 40 scans between 2 and 44, omitting 18, 23 and 43. Its `mspage` marks equal scan minus one; the Codex comments identify these as archival foliation, so the mapping is not silently called authorial pagination. No surviving heading states a total page count. The letter starts at scan 44 and continues on scans 45–47, with typed pages 2–4 and a signature. This corrects the earlier notes' statement that its second conjecture and conclusion were unavailable. The local French draft join is scan 22 to scan 20, internally pages −14− to −15−. The recovered cote 54/008 leaf really has page −13− and draft no. 391, but already gives chamber wall corollaries, while 14/020 only introduces section 5. The shared draft family is checked; a continuous 54/008→14/022 sequence remains unresolved because of this mathematical-order tension. These documentary conclusions are recorded in SA06-6, 86, 91 and95–98; the metadata merge sends source entry94 to SA06-6.

The singular-hypersurface programme is now directly located at cote 16/047, CT line 1791. It does not occur explicitly in the fully read early cote 14 text through scan 58. The 1965 letter uses a smooth projective variety, a smooth hyperplane section, and later smooth affine varieties. This is a bounded negative finding about supplied pages, not a verdict on whether later or other folders continue that separately located programme.

### 1. Effectivity in the author's order

The opening presupposes a category \(M\) and preceding structures. Its fourth structure is an effective subcategory stable under specified operations, containing the effective Tate object, and allowing each object to become effective after twisting. It then studies cocharacters, nonnegative-weight representation subcategories, conjugation, intersections, Galois-invariant cones, a withheld saturation condition, polarization data, and a possible intrinsic interpretation under change of fibre functor. The torus case introduces a character lattice, an invariant representation ring, and the compactness of the kernel of the Tate character. The final page tests positivity and fixed-weight finiteness.

The elementary weight statements are valid with their stated finite-dimensional hypotheses. Nonnegative weights are stable under sums, tensors and subobjects; a positive Tate weight eventually shifts every finite weight set into that range. Infinite intersections need a uniform bound. The family \(i_m(t)=(t,t^m)\) on \(\mathbb G_m^2\) gives an explicit failure of that uniformity. The representation ring of a finite-rank torus is described by Galois character orbits, and the finite-group invariant Laurent ring is finitely generated over \(\mathbb Z\). These checks are C-SA06-2–8 and14–15, with exact calculations T01–T04; the checked modern torus locator is Milne (2004, Proposition 15.6, p.122).

The missing axioms matter more than the available counterexamples. The source never fully defines \(I(G)\), “types,” its saturation or the topology of the proposed cones. The dossier therefore does not turn a toy torus counterexample into a refutation of an unspecified motivic classification. Likewise, the cancelled compactness proof and the later “Fausse” cannot be scoped from text alone. Under the later polarized Tate-triple hypotheses the compact-kernel mechanism is precise, but identification of those hypotheses with structure 3° remains conditional (Deligne & Milne, 1982, Theorem 5.16 and Remark 5.17). The related real-fibre and polarization pages in cote 15/117–125 were read for links; they address gerbes and torsors more specifically and are not automatically duplicates.

The extensive Nori, Ayoub, Lefschetz-\(\mathfrak{sl}_2\), semisimplicity, period and anabelian discussions in the earlier notes are editorial additions. They are kept and checked as such in SA06-21 and29–39. The Nori–Ayoub comparison identifies the degree-zero stable Betti group under its coefficient/base-field hypotheses; it does not supply the absent definition of \(M\) or a general motivic \(t\)-structure (Choudhury & Gallauer, 2017, Theorem 9.1). Pure Nori/André semisimplicity does not imply mixed semisimplicity (Arapura, 2013, Theorem 6.4.1; Huber & Müller-Stach, 2017, Theorems 10.2.7–10.2.8). The arithmetic exact sequence does not identify its geometric kernel with the identity component; Terenzi (2026, Remark 1.11) still states geometric connectedness as conjectural. All of these boundaries are substantive corrections to possible overreadings, not new claims found on the early sheets.

### 2. The sign example and Albanese equivalence

The sign example starts with \(\Theta_0=\Delta-E\times0-0\times E\) on an elliptic square. Its square has degree \(-2\). A divisor embedding with a selected normal line bundle then gives intersection trace \(-2d\); choosing degrees \(d=1\) and \(d=-1\) realizes both signs. The computation survives after the projections are typed correctly. It does not contradict primitive Hodge positivity with its prescribed sign. The ambiguous support factor, arrow direction and normal-bundle index are left for the scans (SA06-40–41; C-SA06-21).

The next text defines an integral relation generated by correspondence-images of degree-zero Albanese kernels. This direction of definition is essential. It is not, merely by its name, Samuel's relation defined through all regular homomorphisms, or Saito's incidence relation defined through all divisor-valued correspondences (Samuel, 1960, §2.5; Saito, 1979, Theorem 3.6). The first comparison proved here is an inclusion into the incidence kernel; equality is not supplied by the opened literature.

The construction gives a graded subgroup containing rational equivalence, an ideal in the Chow-ring formulation, proper pushforward and smooth-target pullback through the correspondence formalism. The source's marked moving step is preserved separately from that modern reconstruction. The zero-cycle endpoint is the Albanese kernel; the divisor endpoint is linear equivalence. Products of two algebraically trivial classes vanish in the quotient because their product family is evaluated on a box zero-cycle with zero Albanese sum. Divisibility then extends this to a product of an algebraically trivial class with a \(\tau\)-trivial class. The proposed strengthening to numerical triviality remains a distinct problem. These are C-SA06-22–38 and MP-SA06-11–16.

The question whether Albanese equivalence might equal rational equivalence has an especially strong historical answer. On a product of elliptic curves, the box cycles generate the Albanese kernel, and Mumford's theorem forces some such cycle to be nonzero modulo rational equivalence. Grothendieck himself explicitly draws that conclusion in his letter to Mumford of 20 November 1968, Letter 46, p.151. This exact letter is stronger evidence than a broad later analogy. The archival sheet is not redated or amended by that later result (Mumford, 1969, theorem p.200; Grothendieck, 1968, Letter 46).

Families factor through graded Albanese groups, and a miniversal cycle represents a positive multiple of the resulting map. The integer cannot be discarded. The saturation sentence is valid inside the already factored maps but false for arbitrary point maps: a nonconstant \(\mathbb P^1(\mathbb C)\to E[2]\) has zero double and fails the factorization condition. C-SA06-91 records the corrected ambient group. Rational correspondences also need not act on integral point groups, since division by an integer is not canonical even on a divisible group with torsion.

The contemporary universal-cycle literature supplies a precise obstruction, not a blanket rejection of miniversality. Voisin's published Theorem 1.4 gives a smooth projective complex threefold with representable \(CH_0\) and no integral universal zero-cycle. Alexandrou's Theorem 1.3 gives surface examples for specified elliptic Albanese varieties, as a checked2026 preprint result. Both allow a positive multiple and neither automatically settles the distinct top-odd inverse question (Voisin, 2025, §2; Alexandrou, 2026).

### 3. Transposition and odd cohomology

The source asks whether transposition depends only on the induced \(P\)-group map, and then explicitly leaves the cohomological proof incomplete. Two limited assertions can be proved from the data without replacing its quotient.

First, for an **integral correspondence from an abelian source**, the transposed map to the dual abelian variety is independent of the representative. Compose with a parameter family for an algebraically trivial complementary cycle. The result is a divisor on the product of the abelian source and the parameter. Its parameter fibres are equal because \(N^1_{\rm Alb}=0\); seesaw forces the transposed difference to vanish. This is the independent proof in `parts/cote 14_early/proof_checks.md` §8. It does not prove the full \(P\)-to-\(P\) bijection or divide its transpose by the integer in the definition of an algebraic homomorphism.

Second, **over \(\mathbb C\)**, correspondence-images of Albanese kernels are killed by Abel–Jacobi. Hence a zero family in the archive quotient has zero map to the algebraic intermediate Jacobian. Faithfulness on the relevant level-one Hodge structure and Poincaré duality give zero rational cohomological transpose in every codimension. The recovered Hua modernization already gives this Abel–Jacobi route at 14.modern.tex:990–997; the complete scoped implication is independently checked here in §9 and is not claimed as a new idea. Positive characteristic and the integral converse remain separate. Achter et al. (2023, Proposition 8.2) supplies a different precise Tate-module result in codimensions1,2 and \(\dim X\), with a miniversal-degree prime restriction, rather than an unrestricted replacement.

Two scan alarms are forced by type. The source exponent must produce degree one after the correspondence shift, and the printed surjection from an ample curve's points must be distinguished from surjectivity of its Jacobian. These alarms are not silent corrections. Saito's established incidence-quotient duality is a relevant comparison, with its different relation and rational denominators retained (Saito, 1979, Theorems 4.4 and4.6).

### 4. Tate's trick and the complete 1965 letter

The finite-field fragment gives an invariant-generation strategy with an undefined pro-Lie algebra and alternative eigenvalue hypotheses. The elliptic-power assertion has an established interpretation: Tate classes, fixed over some finite extension, are generated by divisor classes. The divisor comparison is Tate's1966 theorem; the elliptic-power criterion was checked in Milne's AppendixA. The normalized-root-of-unity gloss is false if read for every elliptic curve. Exact enumeration of \(y^2=x^3+x+1\) over \(\mathbb F_5\) gives trace \(-3\); its normalized trace has square \(9/5\), ruling out a sum of roots of unity. The alternative two-eigenspace case is preserved (C-SA06-53–55).

The letter's equivalence relation is the central historical distinction. It defines \(C^i\) **modulo algebraic equivalence**, then conjectures a Lefschetz isomorphism \(A\), hyperplane surjectivity \(A'\), primitive positivity \(B\), and affine vanishing \(A''\). The continuation itself qualifies the reduction and retracts an earlier equivalence with Künneth algebraicity.

Draft \(A\) is false for a very general smooth quintic threefold: divisor classes form \(\mathbb QH\), while a nonzero rational Griffiths class in codimension two cannot lie in \(\mathbb QH^2\). Draft \(A'\) fails because the hyperplane surface has finite-rank Néron–Severi group but the target has an infinite-dimensional rational Griffiths quotient. Localization then gives a smooth affine hyperplane complement with nonzero \(C^2\), although \(2\cdot2>3\), disproving \(A''\). All hypotheses and the algebraic-equivalence localization step are checked in §11 (Clemens, 1983, Theorem 0.2 and Corollary 0.3; SGA6, XIII, Theorem 5.1). Those examples do **not** by themselves refute the even-dimensional primitive middle assertion \(B\).

Grothendieck's published standard conjectures use algebraic cohomology classes. Their consequences concerning Künneth algebraicity, traces, numerical/homological comparison and the Weil conjectures cannot be transferred back to equality of algebraic and homological equivalence (Grothendieck, 1969, §§2–4). Deligne's cohomological theorems and Jannsen's numerical semisimplicity establish major later portions of the programme with their own hypotheses. The mixed package of \(\tau\)-equivalence and standard-conjecture consequences in C-SA06-94 is consequently classC, not an exact classA match.

The 2026 search encountered very broad new preprint claims about CM Hodge and finite-field Tate conjectures. Their exact statements and proof status are recorded separately. The OpenAI paper was opened, but its central theta construction was not independently verified; it is not used as an established general settlement. The Broe primary endpoint could not be retrieved and remains unverified. Neither search failure nor the existence of a new preprint supplies a novelty or settlement verdict.

### 5. Sorites and reused leaves

The Sorites makes four choices of Picard/Albanese source and target. Its summary promises homomorphisms induced by correspondences, numerical dependence, rational realization of all such homomorphisms, and inverse correspondences for isogenies. The detailed assigned pages prove the Albanese-to-Albanese construction using a Poincaré divisor, include the integral cohomology compatibility, and begin the one-cycle Picard-to-Albanese case. The reference requested for numerical divisors is supplied precisely by SGA6, XIII, Theorem 4.6; torsion-freeness of abelian-variety Hom groups then removes the multiple. The relative arbitrary-base remark remains conditioned by representability and intersection theory (Grothendieck, 1962, Theorem 3.3 and Remark 3.4).

The continuation on scans 59–73 is included in the consolidated corpus. It completes Proposition 2.1, develops the mixed ample degree-one map through Jacobian polarization, writes rational inverse formulas and repeats the two integral questions. Exact duplicates are consolidated in the final claim table; the distinct four-case and integral refinements remain separate. The integral H¹ and top-odd torsion refinements there should not be flattened into the weaker rational summary here.

The English leaves contain separability, tensor-Hom, commutants, Morita evaluation and the Brauer group. Matrix identities and the local proofs were checked against Bass's primary treatment. The distinction between finite projectivity and faithful finite projectivity, the tensor base in Morita evaluation, and the split/non-split Brauer classes are explicit. A quaternion norm calculation verifies the latter distinction. The French leaves contain affine homogenization, reflections, translation by twice a normal vector and the convex description of chambers. Their elementary arguments have been independently completed. Exact published collation of the reused drafts remains unverified.

## Late cote 14: completed consolidation

**Scope:** MPL_14_087–132, all 94 indexed note entries, and the assigned Codex folders K14-05, K14-06 and K14-08. **As of:**19 November 2026. **Run:**SA06-part2/cote 14_late; GPT-6 Astra Pro, effort inherited/not exposed.

The assigned notes, full transcriptions, doubts and Codex leads have been read. The verdicts are individually reasoned mathematical adjudications serialized by code; headings and search keywords did not generate them. The Pro range contains41 scan markers. Positions105,110,119,125 and130 are absent from that transcription; their being blank is a prior-run report that cannot be verified without scans. No reading has been changed. The additional external endpoints in cotes16,44,47 and54 were read to check links, without expanding this part into a second consolidation of those cotes.

### What these leaves contain

The Codex material preceding scan 87 develops the algebra of correspondences associated with abelian varieties. Divisors, one-cycles, Picard varieties and Albanese varieties are compared through first and top-minus-one cohomology. Isogenies give rational inverses; the pages then ask whether particular inverse cycles can be integral. Kummer sequences bring in Néron–Severi torsion, and the following pages work through first cohomology, exterior powers, pushforward, degree and transpose signs. Interleaved foundational material concerns an associative polynomial law on the affine line and the Čech-to-derived comparison on a site.

Scans87–90 continue the abelian-correspondence and sheaf-cohomology themes. The warning that graph formation is not additive is explicit, while the mixed H¹ component is additive. The question at the end of89 stops before a complete algebraicity criterion is supplied. The sheet cannot be turned into an arithmetic Tate or anabelian theorem: neither a suitable arithmetic base field nor a Galois-invariance hypothesis appears there. The selected acyclicity and comparison leaves are portions of a fuller redaction, and the Codex continuations supply proof steps that the earlier Pro note could not see.

The cover at91 introduces the equivalence chart on92. The chart asks several distinct questions about discrete cycle groups, finite differences of equivalence relations, continuous quotients and abelian varieties. Its queried or cancelled arrows do not state a single established equivalence theorem. In particular, finite generation modulo numerical equivalence, representability of algebraically trivial cycles, and equality of numerical and algebraic equivalence are different problems.

The cover at93 introduces the Mumford–Nakai and ample-cycle leaves. Scans94–95 give an Euler-characteristic growth criterion and induction lemmas. Scans96,98 and100 explore strict positivity, square-zero divisors, cone duality and products of higher-codimension classes. Formal-smoothness and derivation sheets intervene at97 and99, followed by a truncated inverse-system lemma at101. They belong to a different foundational line and should not be used to manufacture a continuous ampleness argument.

The cover at102 groups Lefschetz conjectures for algebraic cycles, intermediate Jacobians and local questions. After a Picard-kernel discussion at103 and a dimension-formula sheet at104, scans 106–109 propose local vanishing, restriction, pairings, complements and monodromy-invariant interpretations on punctured local schemes. The pages keep X and Y regular. The integer N and the precise definitions of the local cycle groups are not supplied fully enough to identify every proposed range without reconstruction.

Scans111–117 formulate global restriction and Gysin maps, hard Lefschetz analogues for cycle groups, affine-complement/cone consequences and low-dimensional tables. The distinction between rational equivalence, algebraic equivalence, the algebraically trivial subgroup and a discrete quotient becomes decisive. The conditional “OK” marks in the surface/threefold tables rely on identifying rational and Albanese equivalence; they are not proofs that this identification holds.

Scans118,126 and128 concern bounded families, rectangle cycles and Albanese equivalence. K-theoretic boundedness and the factorial comparison with cycles occupy120–121 and continue at123, around the unrelated sheet122. The transporter typescript runs124(page2)→122(page3); the Cartan typescript runs129(page24bis)→127(page25). The instruction at127 restores text struck out by mistake. Scan131 gives a generic-fibre/blow-up diagram whose cleanly justified interpretation is a pencil with a regular codimension2 base. Scan132 retains fragments without enough definitions for a unique theorem.

### What was corrected in the earlier notes

#### Supplied continuations repair missing-proof reports

The Pro note on acyclicity understated the combined evidence. K14-06/079 continues the proposition begun on88, including its second condition, both implications and the definition. K14-06/077 supplies local effacement and vanishing of the Čech H⁰ of positive cohomology presheaves used on90. These are exact matches with SGA4 V Corollaries 3.4–3.5, Proposition 4.3 and Corollary 4.5. The more specific functor statement on82 is justified by cofinal covers and preservation of the relevant fibre products; continuity alone does not suffice. These checks are recorded as C-SA06-205–209.

The derivation note correctly flags the displayed domain mismatch at99. Its subsequent argument explicitly uses two genuine lifts B→E and is sound: subtracting the lifts gives an A-derivation into the square-zero ideal, and adding any such derivation gives another lift. Thus the second note is merged, not rejected as resting on the same type error. EGA IV₁,0_IV Proposition 20.1.1 and Corollary 20.1.3 give the exact published result.

The formal-smoothness and truncated-algebra sheets have closer published matches than a broad modern analogy. EGA IV₁,0_IV Corollary 19.5.4 identifies the completed symmetric-algebra criterion with its topology and quotient hypotheses; Lemmas 19.5.6.3 and19.5.6.5 identify the transition-preserving truncation argument. EGA IV₂,5.6.5 gives the dimension inequality and its catenary equality condition. The missing ambient hypotheses are supplied only in the separately labelled modern reconstruction, never inserted into the frozen transcription.

#### Coefficient rings and equivalence relations change the conclusions

The chart's numerical quotient is finite free: Kleiman (1968, Theorem 3.5) proves it, and this run independently embeds the quotient in a finite integer intersection lattice. This does not prove finite generation modulo algebraic equivalence. Clemens (1983, Theorem 0.2) supplies an infinite-dimensional rational Griffiths group on a very general quintic threefold, which obstructs the manuscript's hard Lefschetz surjectivity modulo algebraic equivalence.

The stronger whole-Chow assertions fail already on familiar smooth projective complex surfaces. If a fixed smooth curve on a K3 surface generated CH0 rationally, Mumford's theorem would force a finite-dimensionality that its nonzero holomorphic2form excludes. Pic⁰(K3)=0 while its degree-zero Chow group is nonzero, so the shifted algebraically trivial surjectivity also fails. Beauville and Voisin (2004, Theorem 1) put products of divisors in a single distinguished zero-cycle class, giving another direct obstruction to whole-Chow surjectivity. These are hypothesis-matched refutations of C-SA06-238,240 and241, not objections to cohomological hard Lefschetz.

On111–117, the subscript for algebraic equivalence cannot be read as homological or numerical equivalence merely because those versions resemble standard conjectures. Nor does a rational isomorphism imply a finite kernel and cokernel:0→Q/Z is a simple counterexample. The dossier retains integral, finite-error, rational and prime-to-characteristic assertions separately.

The localization formula on113 needs a codimension shift: CH^(i−1)(Y)→CH^i(X)→CH^i(X−Y)→0. A principal divisor kills classes pulled back from X under the relevant Gysin composition; it does not make the pushforward of every cycle on Y zero. The standard punctured affine cone has dimension n+1, and the primitive kernel uses L^(n−2i+1), one power beyond the hard Lefschetz isomorphism. These mathematical alarms have been indexed for later scan review.

#### Ampleness and cones: three different boundaries

The Euler-growth criterion itself is an established theorem: an invertible sheaf on a proper scheme over a field is ample if its Euler characteristics on every positive-dimensional integral closed subscheme tend to positive infinity (Mumford & Oda, n.d., VIII.1, Theorem 1.11). The stable reference key contains2015 for merge continuity, but the opened author draft is undated and no such publication date is inferred.

The literal fixed threshold≥2 over an arbitrary base field fails without a constants convention. P¹_C regarded as an integral R-scheme with its trivial bundle has χ_R=h⁰_R=2 for every power, although the bundle has degree zero. This earlier-run example was independently recomputed and proved. It does not refute the growth criterion.

Strict positivity on curves is weaker than ampleness: Mumford's strictly nef surface divisor can have square zero, as documented in Hartshorne (1970, Example10.6). Even adding positive top intersection is insufficient in dimension3. The run checks the explicit projective-bundle construction D=ξ+π*L with D³=A²+3A·L>0, while its restriction to a section is the nonample L. Finally, the successful continuity argument for powers of nef divisors does not extend to arbitrary nef higher-codimension classes. Debarre, Ein, Lazarsfeld and Voisin (2011, TheoremA and §2) give exact counterexamples to the stronger cone/product assertions.

#### Two integral inverse questions, two modern obstructions

The denominator question for an isogeny has a clean correction. The least d for which d·u⁻¹ is an actual homomorphism is the exponent annihilating its finite kernel group scheme, not generally the kernel's order. For multiplication bym on a g-dimensional abelian variety, the denominator is m and the degree is m^(2g). The ℓ-integral criterion remains valid for ℓ different from the characteristic: the Tate-module cokernel is the ℓ-primary geometric kernel, so invertibility is equivalent to ℓ not dividing the degree. This is C-SA06-265–266.

The first question on71 asks for an integral inverse to the Albanese H¹ isomorphism. The induced endomorphism of Alb(X) has identity H¹ action exactly when it is the identity, by faithfulness. This is the precise integral universal-zero-cycle condition, with the appropriate torsion-free Künneth component; no global torsion-free cohomology assumption is imposed. Voisin (2025, §2 before Lemma 2.1 and Theorem 1.4) gives a smooth projective complex threefold with representable CH0 and no universal zero-cycle. Alexandrou (2026, Theorem 1.3) improves this to a surface with Alb(S)=E under the stated endomorphism-ring conditions. The latter is a2026 preprint theorem, with v1 dated13 February and v2 dated8 March; no journal publication has been asserted. The rational generic-section condition proposed on the sheet remains a sufficient special hypothesis, and rational universal cycles exist.

The second question asks for an integral inverse to the Picard/top-cohomology map. This run gives a separate integral argument. For an abelian variety A, a putative one-cycle on A∨×A has only three possible Künneth components. Subtracting the two pushforward product cycles removes the unmixed components integrally, without algebraic Künneth projectors or division. The mixed inverse is, up to a unit sign, c₁(P)^(2g−1)/(2g−1)!, and the general exterior calculation proves the sign and coefficient. Its algebraicity would imply the integral Hodge conjecture for one-cycles by Beckmann and de Gaay Fortman (2023, Theorem 1.1). Engel, de Gaay Fortman and Schreieder (2025/2026, Theorem 1.1) refute that conjecture on very general principally polarized abelian varieties of dimension at least4. Thus the universal second assertion is false too, for a distinct reason. Equality in one ℓ-adic realization forces the same integral mixed class because the relevant integral cohomology lattice is free and injects into its ℓ-adic completion. The full deduction is in `parts/cote 14_late/computation_notes.md`; it is not attributed verbatim to either modern paper.

#### Rectangle cycles and boundedness

The rectangle relation modulo algebraic equivalence is automatic by varying a point in a connected family. It cannot imply rational equivalence or injectivity of an Albanese map. The rational version fails on a product of elliptic curves, and Grothendieck's letter to Mumford of20 November 1968, Letter 46 p.151, explicitly recognizes this failure. This dated primary letter is a stronger historical endpoint than an inference from a later general theorem. Roitman's torsion theorem, including the positive-characteristic completion used here from Milne (1982, Theorem 0.1), provides a restricted positive answer; it does not identify the entire Albanese kernel with zero.

The bounded K-class argument on120 is valid with its actual quantifiers. A common locally free quotient gives bounded kernels; a second common twist and generator count may be required. The Chern-class comparison carries (−1)^(i−1)(i−1)!, and the undefined K-equivalence prevents promotion of the whole condition list to an unconditional integral equivalence. Scan123 supplies the actual implication chain following121. These distinctions are retained in C-SA06-251–252.

### Modern context remains separate from the source

Twenty-five items record ideas of the earlier run. Twenty-one item checks are “not on the page”; that is an attribution verdict, not a blanket claim that the idea is false. The full audit in `contextual_comparisons.md` treats Lefschetz/sl₂ normalization, Tannakian tensor-unit and Tate-character constraints, numerical semisimplicity, abelian Chow-motivic Lefschetz, arithmetic Hom theorems, anabelian openness/inner-quotient hypotheses, centres, real descent, Kummer inertia, Nori exact sequences, formal periods and Ayoub's2026 reconstruction.

The exact external cote 16 endpoint confirms a singular-hypersurface programme following Serre's simple-connectedness objection. It does not put a completed singular correspondence theory into the assigned cote 14 sheets. Cote 47 confirms a derived Fourier programme with shifts and determinant/Todd factors, but also an admitted lemma and an unfinished fibre compatibility check. Cote 44 confirms a seven-theorem intermediate-Jacobian work programme and a positivity question with a primitive-decomposition warning. The project register's LM/WG statuses remain earlier-run claims or unchecked plans; the parent consolidation checks full available project endpoints separately. “New to us” in Hua's intake record is not a novelty claim.

The checked2026 literature materially changes two inverse-cycle statuses, but it does not justify claiming that the entire local or whole-Chow Lefschetz programme has been settled. No claim is assigned classD merely because a search failed. The three classF records explicitly identify missing definitions or insufficient statement content.

## Cote 15, scans 034–086: Deuring categories, norms and the commutative motivic band

The mathematical order of this packet is reasonably clear even though reused analytic leaves interrupt it. Grothendieck begins with a category and its norm, tries to rigidify the norm, studies the resulting automorphism and ramification data, specializes to the supersingular quaternion algebra, and then reformulates the construction through generators, invertible bimodules and a Brandt groupoid. Only near the end does the text return to the general commutative motivic band and positivity. This order matters: the category on scan 084 is assumed, not constructed from the correspondence rings of cote 16 in the intervening argument. Items SA06-700–766 preserve the 74 indexed note entries in this packet; the claim catalogue separates assertions, conditional constructions and earlier-run suggestions.

### Norm rigidification and its obstruction degrees

On scans 034–038 the decisive distinction is between the scalar automorphisms of an already existing normed object and the existence of the proposed gerbe of such objects. If a scalar λ acts on a rank-n object, its determinant acts by λⁿ. Fixing the determinant leaves μ_n. This proves the scalar-band calculation C-SA06-700. It does not prove local nonemptiness of a category on an unspecified site or coherence of its two Picard actions. The page marks the latter comparison “À vérifier!!” and begins the next step “Supposons qu’on ait pu associer.” C-SA06-701 and MP-SA06-300/302 retain these genuine gaps. The modernization's affirmative canonical object is therefore stronger than this witness.

The endpoint labelled Ram also needs its norm-line obstruction. Changing an ideal representative by a central line L changes its norm by Lⁿ, so the obstruction lives in Pic(A)/n. A norm-trivialized representative exists only when that class vanishes. This is the refined content of C-SA06-702, not an asserted counterexample to the principal bases actually used later. On Z, Z[1/p] and Z_p the Picard obstruction disappears. The fppf Kummer sequence is the appropriate framework when n is not invertible; the deleted étale qualification must not be restored as a universal assertion (Stacks Project, tag040N; exact checked locator in the bibliography).

In the quaternionic specialization, the local radical satisfies m²=pO and Nrd(m)=pZ_p. The normed class (m,p) squares to (pO,p²), which the central scalar p trivializes because its reduced norm is p². Thus it has order two and splits the displayed ramification extension. Unit square classes have order two at odd p and order four at p=2. Their product with the ramification factor has order four or eight, respectively. These are C-SA06-703–704; the odd and dyadic cases were recomputed rather than conflated. Voight (2021, §§18.3–18.4) supplies the checked ideal-theoretic setting. The real quaternionic Brauer class is a different degree of obstruction and is not cancelled by this local splitting.

Three levels of canonicity are repeatedly at risk of being compressed into one. A class of objects may be unique; an isomorphism between two objects may exist but form a torsor; and automorphisms of an isomorphism may still survive. In scans 044–048 Frobenius acts trivially on a quotient of classes, but a coherent descent action needs its two-isomorphisms and cocycle. Scan048 records a residual Z/2 in degree two and deletes a proposed canonical point. A neutral *comparison* does not neutralize both endpoints. The distinction is carried through C-SA06-705–709, with the actual cancellations retained. It is consistent with the Picard-stack formalism of SGA4 XVIII and with the care taken over residual automorphisms in later gerbe constructions (Deligne, in SGA4 XVIII, §§1.4.11–1.4.21; Milne, 2003).

### Two arithmetic failures that materially change the proposed construction

The formula F_p[T]/Φ_(pⁿ−1)(T) is not generally a field. At p=2,n=3,

\[
\Phi_7(T)=(T^3+T+1)(T^3+T^2+1)\quad\text{over }\mathbf F_2,
\]

and the quotient is F₈×F₈. Both cubics are irreducible because neither has an F₂ root. This exact factorization refutes the displayed general construction under its own numerical hypotheses (C-SA06-707). Choosing a factor gives a field; choosing compatible factors or embeddings in a tower is additional data. It does not follow from calling the original quotient canonical. Hua's modernization had already identified the product-of-fields defect; the new finite certificate confirms the point, without a novelty claim.

Scan056 also requires an order distinction. Frobenius with F²+p=0 gives an action of Z[√−p], but it need not extend to the full ring of integers of Q(√−p). The explicit p=7 curve y²=x³+x has eight F₇-points, hence trace zero, and only one nonzero rational two-torsion point. If (1+F)/2 were an endomorphism, F would act as −1=1 on all E[2], making all two-torsion rational. This contradiction checks the missing extension hypothesis on an actual nonsingular elliptic curve (C-SA06-711). The maximal-order statement is not rescued by trace zero alone. The point count, discriminant and two-torsion count are saved exact computations.

### The determinant orientation ξ_p remains a specific unfinished problem

Scans054–056 ask for a distinguished element through determinant trivializations of rank-two slope-one-half crystals and their compatibility under normed invertible bimodules. This is more specific than knowing that supersingular elliptic curves correspond to quaternionic ideal data, and more specific than a comparison of two cohomology theories. The independent calculation verifies the determinant/norm target but does not select the distinguished square class or prove its global naturality (C-SA06-710; MP-SA06-303).

The exact literature comparison is Oda's Corollary 5.11: for an abelian variety X over a perfect field, M(X[p]) is identified with H¹_dR(X), with the specified F,V and Hodge-subspace compatibility. The source does not write an additional quotient by p on M(X[p]), which is already the module attached to the p-torsion group scheme. Oda's introduction identifies the work as a modification of a Harvard dissertation submitted in June 1967; publication followed in1969. Neither that comparison nor the earlier finite-group-scheme discussion in cote 54 computes the manuscript's particular ξ_p (Oda, 1969, pp. 99–101,131). A future task must fix covariant versus contravariant conventions, the Tate normalization, the base field, and the square-class quotient before asking for a formula.

### Generators, Brandt groupoids and the commutor

The typed discussion on scans 060–061 continues in B15-01 at scan 063. Under the finite-projective closure and generator hypotheses, splitting idempotents gives the expected equivalence with finitely generated projective End(X)-modules. This is the concrete Morita mechanism behind C-SA06-712; merely naming a generator is not enough if the category lacks the relevant sums and summands. The earlier notes correctly recognized the bridge to bimodules, but universal properties and the meaning of “admissible” are retained with their actual hypotheses.

For maximal orders over a Dedekind base, invertible two-sided ideals admit local radical-exponent descriptions and commute. In that setting multiplication identifies I⊗_O J with IJ, and the equality IJ=JI defines the candidate commutor by

\[
I\otimes_O J\xrightarrow{\mu_{I,J}}IJ=JI
\xrightarrow{\mu_{J,I}^{-1}}J\otimes_O I.
\]

Associativity of ideal multiplication controls the diagrams in this model. The passage to an abstract category, its independence from a strict generator, and its compatibility with chosen Morita transports must still be stated at the correct categorical level (C-SA06-718–723). A commutative class group alone is insufficient. Likewise, a torsor under a Picard two-group is not a chosen point of it. The checked published comparison is the equivalence between strictly commutative Picard categories/stacks and appropriate two-term complexes in SGA4 XVIII, not a declaration that every monoidal equivalence preserves every chosen commutor.

That last overstatement has a finite counterexample. On objects F₂³, a bilinear alternating sign pairing supplies a strict symmetric Picard groupoid. A strict monoidal coordinate permutation can change that pairing, and hence fail to preserve the specified symmetry. The certificate checks all relevant pairs and triples and exhibits a possible tensorator repair. It disproves automatic symmetry preservation for the fixed monoidal data; it does not disprove generator independence of the specific inner/Morita transports intended elsewhere. The Pro reading is broader than the Codex “auto-intérieurs” reading, so the final textual decision belongs to the scans (C-SA06-721; SA06-737; MP-SA06-313).

The quaternionic tail supplies further localized corrections. For characteristic different from2 and3, j=0 has automorphism group order6 and j=1728 has order4, reversing the displayed pairing. The algebra relevant to supersingular curves is ramified at p and infinity. Frobenius pairing of orientations and conjugacy classes of maximal orders must be distinguished from isomorphism classes of elliptic curves. The last clause about O* is unfinished; a recognizable topic does not make it an identifiable theorem (Silverman, 2009, III.10.1; Voight, 2021, §42.4; C-SA06-716–717; MP-SA06-315).

### Positive involutions and the commutative motivic band

On scans 084–086, a faithful object embeds the rational points of a commutative motivic group in its endomorphism algebra. A polarization supplies a positive involution. The connected kernel of the similitude character is then compared with a compact real unitary torus. The faithfulness, connectedness and weight normalization matter separately. The correct semisimple commutative algebra can have totally real factors with identity involution as well as CM factors with complex conjugation. A Tate object already prevents excluding the real factors (Milne, 2020, Proposition 1.36 and Corollary 1.40; C-SA06-724–725).

Density for a connected torus cannot be extended indiscriminately to a disconnected multiplicative-type group. The three-torsion of the norm-one torus of Q(i) has three real points but only the identity rational point. Thus rational points need not meet every geometric component (C-SA06-726). On the other hand, rational density for a torus over an infinite field is the exact standard input used in the connected setting (Milne, 2015, Corollary 14.42).

Recovering ε and the cocharacter j from norm characters is an integral lattice question. Dividing an exponent in X*(G)⊗Q does not show divisibility in X*(G). Coprime exponents can give a Bézout reconstruction when the necessary relations are known. For Res_(Q(i)/Q) G_m, every rational split cocharacter has even composite with the norm, so the norm has no rational cocharacter section of weight one. A weight-two lift is a different statement. These exact lattice calculations distinguish the unfinished ε/j task from the universal Serre-group construction that later supplies a natural comparison object (Milne, 1981, §4; C-SA06-727–729; MP-SA06-316). The endpoint in cote 18/011, with ε∘j=id, was read directly and retained as a later formulation, not used to erase the obstruction in the more general norm-torus example.

### The reused analytic leaves

Scans067,069,071,073,075,077 and079 carry analytic arguments interleaved with the motivic pages. They are indexed because the user requested every recorded assertion, but their proof requests are not new motivic conjectures. The source's ODE integration coefficient, square-root expansion and majorant inequality were recomputed. On the literal readings, a missing reciprocal introduces a factor p²α² in the differentiated ODE term; the square-root coefficients need the factor2n−1; and an assertion that a majorant parameter is merely sufficiently small fails at a concrete coefficient. The correct formal recurrence or local analytic theorem can be stated, while the cause of the faulty written expression remains undecided (C-SA06-731–736).

The implicit-function and Frobenius arguments require their Banach/analytic, finite-dimensional or characteristic-zero hypotheses as appropriate. A derivative-zero argument over a positive-characteristic valued field cannot be justified by a characteristic-zero theorem: x↦xᵖ gives the basic obstruction. The manuscript's index and variable uncertainties are left in the reading table. The checked Bourbaki comparison supplies exact local theorems, not an ink decision or a proof for every arbitrary-valued-field variant (Bourbaki, 1967/1971, §§3.2,9.1,9.3; see the middle-part source audit). The cancelled Legendre-sign observation is likewise retained as withdrawn text, with the elementary residue calculation checked independently.

## Cote 15, middle sequence: consolidated overview

**Scope and date.** This part covers all 110 indexed entries of `MPL_15_087-138` and the complete Codex transcriptions and notes B15-01, B15-02 and B15-03. The Codex notes receive no independent index verdict rows. The findings are dated **19 November 2026**. Every assigned entry, its corresponding transcription, all doubt tables, and the complete assigned transcriptions were read. The source-read audit is retained in `progress.log` and `audit/`. There are no scans in this task; the 69 mathematical reading alarms remain undecided as ink.

The consolidation has three recurring results. First, the finite-field programme contains several correct arithmetic constructions whose integral, rationalized, and categorical versions must be distinguished. Second, the real fibre-functor analysis has genuine positivity and descent premises that cannot be replaced by bare torus equations. Third, many claims in the earlier notes are useful modern comparisons or material from recycled pages; their validity and provenance have to be recorded separately. The supplied sheets do not choose a modern motive category sufficiently explicitly to make every later theorem an unconditional interpretation of M.

### The author's mathematical sequence

#### Characters, Frobenius and compactness

Scans 88–94 study a commutative motivic band through character eigenvalues, a weight cocharacter and a Tate character. The reconstruction is naturally a group of multiplicative type, with finite-type and proalgebraic cases distinguished. The operator description also needs invertibility, rigidity and dual closure. A closure list containing only sums, tensor products and subobjects can generate a monoid of eigenvalues; it does not by itself recover a character group.

The compactness argument can be made precise. Under the stated density and weight hypotheses, compactness of the real Tate kernel is equivalent to the common-modulus relation for every character eigenvalue. This converse can be proved on characters without restoring the author's deleted argument. The crossed-out rank-two example generated by 2 and 3 misses the required compatible weight relation. The fractional real power in the surviving argument still needs an absolute value: that is a reading alarm, not a reason to reject the valid criterion. These distinctions are C-SA06-400–402 and C-SA06-511, proved in P1 of `parts/cote 15_middle/proofs.md`.

The common-rational-norm argument leads to totally real and CM fields. For nonzero algebraic lambda with all conjugates of squared modulus Q in positive rational numbers, lambda+Q/lambda is totally real and 4Q−(lambda+Q/lambda)^2 is either zero or totally positive. The real case allows both signs. The cancelled fourth-root example has irrational squared modulus and therefore does not contradict the rational-norm assertion. The later scans 131–132 provide a surviving version that helps explain the earlier cancellation. The inserted nonnegative exponent at scan 94 is a separate quantifier alarm when the first clause permits negative weights (C-SA06-403–404; Milne, 2020, Proposition 1.4 and Corollary 1.5, `MilneCM2020`).

#### Weil-number realization and the finite-field band

The strong numerical existence question on scan 100 has a clean later resolution. An integral Weil number of positive weight w has a w-th root that is a weight-one Weil number; Honda–Tate realizes that root in H1, and the w-fold product realizes the original eigenvalue in degree w. Negative integral weights cannot occur. Weight zero gives roots of unity, which occur in H0 of finite étale schemes when geometric connectedness is not imposed. The proof of this reduction is supplied in P3; Honda–Tate itself is an opened published input, not independently re-proved here (Tate, seminar November 1968, publication 1971, Theorem 1; `TateHonda1968`).

That result does not prove the proposed complete motivic-band description. The manuscript's weak conjecture, geometric limit and category-generation suggestions require an explicit motive theory and its Tate or cycle-equivalence hypotheses. Milne's finite-field comparison retains those hypotheses, and so does C-SA06-407. The power-map exact sequence and rationalization are verified arithmetically, while their identification with the entire motivic character group remains appropriately qualified (Milne, 1994, Proposition 2.6, Remark 2.7 and §§2.25–2.29; `MilneFiniteFields1994`).

#### Divisors, integral index, fields of definition and norms

The divisor construction proves finite index of a norm-one subgroup; it does not prove saturation. If an ideal class is killed by h, the displayed norm-one construction naturally produces the multiplier 2h. The exact example Q(sqrt(-23)) is useful here: the selected prime over 2 has class of order three, the anti-invariant principal divisor lattice has index three, and the larger lattice has the Smith invariants stated in P5. These are independently proved and recomputed, without relying on a class-number table. They separate rational isogeny assertions from integral lattice claims and expose the weakness of any parity conclusion drawn from finite index alone.

The prescribed-norm question also has distinct quantifiers. Q(i) has no rational element of norm three; Q(sqrt(-23)) has no integral element of norm two, although a rational field element of that norm exists. The author's enlargement construction survives because it permits a larger CM field. The current audit preserves that difference, the deleted fixed-field assertion, and the later formulation rather than collapsing them into one conjecture (C-SA06-416–418; P5–P6).

A selected p-adic valuation has a decomposition-group stabilizer only for the sufficiently large character/divisor lattice on which the different primes can be distinguished. Its field of definition and one completion can then be calculated. The normalized Frobenius lifting question requires an additional H1 obstruction; the mere presence of a nontrivial isogeny kernel does not prove that a specific rational point fails to lift. The p/q and square-root normalization issues precede that obstruction calculation (C-SA06-412–415; P7).

#### Real fibre functors, polarization and gerbes

Scans 117–125 distinguish primitive epsilon from a square character and compare polarization data with unmodified real fibre functors. The faithful reconstruction includes the inherited positivity axioms, the fundamental alternating form in odd degree and the fixed weight-zero realization. A neutral representation category of Gm with epsilon=t^2 shows that the torus equations alone are insufficient; it does not refute the contextual polarized assertion. The compact-torus H1 and H2 calculations and the rank-two quaternionic model explain precisely where the obstruction enters (C-SA06-423–427; Deligne & Milne, 1982, Theorem 3.2, Lemma 4.24 and Propositions 5.13, 5.15–5.19; `DeligneMilne1982`).

The final torsor comparison is valid once both nonempty torsors and their common action have been constructed. The larger automorphism-orbit questions remain separate. So do the integral valuation cocharacter, the finite-index differences of splittings, and the mod-two packet. A difference of splittings lies in the weight-zero kernel; it cannot span finite index in the whole nonzero-weight lattice. None of these integral qualifications is erased by rational character theory.

The global class on scan 125 is weakened from exact order two to order dividing two. This run supplies a **conditional modern test**, not an unconditional identification of that manuscript class. The simple F8 threefold with Frobenius 1+sqrt(-7) has a division endomorphism algebra of degree three and Brauer invariants 1/3 and 2/3. P11 checks absolute simplicity, the character field, the character pushout, and preservation under the stated Tate reduction. Under the explicit Tannakian, rank and endomorphism hypotheses, a reduced class mapping to that Brauer class cannot be killed by two. Whether the manuscript M and h have those precise meanings remains open. The real-place H2 calculation alone cannot decide this global question (C-SA06-433–435; Milne, 1994, Theorem 2.19 and Lemma 3.15).

#### Finite objects, Artin–Tate objects and modern comparisons

The closing scans 135–137 use a category of semisimple isomotives already taken as given. Finite tensor-orbit arguments and Artin representation constructions are checked, but they do not silently supply a missing descent theorem for every proposed motive category. A chosen geometric point gives the usual finite-étale fibre functor; it is not a canonical neutralization of the entire motivic gerbe.

The earlier notes bring in numerical, homological, motivated, Nori and Ayoub categories. Their provenance remains explicit in SA06-34–466 and C-SA06-440–450. Jannsen's numerical semisimplicity theorem does not establish equality of cycle equivalences. The pure Nori–André theorem and Nori–Ayoub Hopf-algebra comparison have their own base-field and coefficient hypotheses. The arithmetic exact sequence also does not identify the Artin quotient with the full component quotient without geometric connectedness. This last limitation is confirmed by the opened August 2026 version of Terenzi's preprint, Remark 1.11 on page12 (`Terenzi2026`).

The earlier-run Lefschetz calculations likewise concern graded correspondences. In particular, End(h(P1)) in ordinary degree zero is Q⊕Q; off-diagonal matrix units require Tate shifts in the total graded correspondence algebra. The universal sl2 string identities and rational coefficients have been checked, and Künnemann's and Beauville's abelian-motive results matched at their exact hypotheses. Their shifted Chow grading cannot be removed to assert general unshifted Chow hard Lefschetz. The external singular-hypersurface programme is now directly located at cote 16/047, CT1785–1796, with the qualified Coates letter at048–050. The supplied regular punctured-local and smooth cote 14 programmes do not construct that distinct singular theory. The final project links incorporate the recovered endpoints and retain the limits of the earlier-project proofs.

### Recycled mathematical sheets and Codex continuations

The intervening pages contain identifiable pieces of algebraic geometry, algebraic groups, topology and analysis. Three exact later-publication matches justify class A: SGA4 VIII3.13, SGA4 VIII9.4 and SGA3 VIII7.13. The SGA3 comparison is particularly instructive: a cancelled draft refinement can survive as a published theorem. The Steinberg excerpts match the perfect-field and split/quasi-split hypotheses of the opened original paper. Popov's later cross-section results give a bounded comparison; they do not classify every nonregular conjugacy class. These are C-SA06-454–463.

The anonymous reflexive-module fragment needs its omitted definitions before its exact theorem can be identified. Its opening is a tautology if the map already is an isomorphism; the substantive height-one homomorphism version is true under normal noetherian hypotheses. The projectivity sheets contain valid exact-sequence and generation steps, with a twist alarm and explicit vanishing inputs. Serre's theorem is used on the projective support, not circularly to assert projectivity of the unknown ambient variety. Cartier and Moishezon provide bibliographic context, but the exact English typescript remains unidentified.

B15-01 supplies the strict-generator continuation after Pro61. The combined source does define reasonable tensor products, so that apparent package-boundary gap is removed. The finite-projective and idempotent arguments verify the appropriate Morita equivalence; the stronger filtered-union statement for “jolie” categories and localization over Spec(R) still require their exact missing axioms. The administrative sheet and roster are recorded as nonmathematical material; personal identifiers are not repeated in the dossier.

B15-02 and B15-03 add the full analytic sequence, including scans 27 and29 that are not covered by the root's Pro package. Local primitives, polygonal paths, the identity principle, flows, Frobenius, inverse functions and majorants are treated with their actual real/complex or complete-valued-field hypotheses. Several literal formulas fail: the interpolation denominator, Frobenius index, ODE component product, radical sign, and remainder estimate. These are preserved as reading alarms with exact checks. The coefficient-division claim is valid after shrinking the polyradius, not as a blanket boundary-convergence statement. The Jacobian dependence question admits Osgood's classical counterexample to its strongest germ interpretation; the original 1916 paper was inaccessible, so the opened modern primary source and the independent proof are distinguished.

The Lusin passage has an especially useful comparison: the opened Bourbaki printing repeats the same dyadic sum from n=0 while naming [0,1]. That is evidence of a genuine normalization problem in the printed witness, not evidence that an OCR system necessarily misread the manuscript. The strong-dual topology in the D′/E′ claim is retained, and the historical word “éparpillé” is interpreted from its contemporary definition rather than a modern false friend.

### What the earlier notes get right, and what changes

The notes correctly isolate many difficult places: lattice saturation, real descent, the gerbe involution, missing hypotheses in norm assertions, and errors in analytic formulas. They also preserve valuable self-flagged and cancelled steps that an ordinary theorem list would lose. Their modern comparisons often contain mathematically useful calculations.

The consolidation changes their use in four ways. It separates fixed-field from enlarged-field statements, integral lattices from rationalized ones, bare group data from polarized-category axioms, and graded correspondence actions from tensor-group actions. It identifies exact published endpoints instead of relying on topic similarity. It removes the artificial Pro61/Codex63 gap while retaining genuinely incomplete fragments. Finally, it labels La Longue Marche, Les Dérivateurs, S6 and modern-category bridges as earlier-run material. The external project endpoints are being merged and checked by the root agent; the eight local lead rows are deliberately segregated in `our_projects.tsv`.

The administrative date 1 April 1968 does not date all surrounding mathematics. First circulation and publication are separated where established, notably Honda–Tate, Milne's finite-field comparison and the Nori–Ayoub paper. Where the exact edition or first-circulation date is unknown, the tables say so. No unsuccessful search is used as evidence that an assertion was novel or undeveloped.

## Cote 15, scans 170–206: fibre objects, comparisons, effectivity and reused sheets

The late packet contains an agenda, a cancelled supporting argument followed by a live cohomological assertion, a short Frobenius-distribution framework, and a sustained discussion of fibre objects with ℓ-adic, crystalline, Betti and real forms. The supplied K15-08 witness continues beyond the Pro selection. Reused projectivity and Lie-theory sheets occur between these pages. Their presence is documentary evidence of reuse; it does not make the mathematical sequence continuous in scan order or give it a single date.

### The agenda is not a collection of unstated theorems

Scan170 lists odd motives and abelian varieties, positivity, integral lattices, class field theory, an uncertain extension noun, L-functions and their functional equation, topology over SpecZ, Riemann-hypothesis methods and pencils. The noun and several quantifiers are not recoverable from the supplied text. C-SA06-800–803 therefore distinguish recognizable programmes from identifiable assertions. In particular, no theorem that all odd motives are abelian h¹'s is written there. Weight-one polarizable rational Hodge structures have an abelian interpretation, while higher odd cohomology requires Hodge-level and coniveau qualifications. Likewise, a heading about a functional equation supplies no normalization, completed L-function or exact equation to check.

These short clauses are included in the problem index because they are the author's programme. Their present state is sometimes “not identifiable as a unique assertion,” rather than “still an open theorem.” A precise modern reconstruction is labelled ours. The original category cannot be supplied from a Nori or Ayoub theorem without first fixing the coefficient ring, equivalence relation, fibre theory and tensor properties that theorem uses.

### The divisor sequence has an exact published counterpart

On scan 179 the Leray/torsion block is deleted, but the rational-function/divisor sequence and its boundary map survive. For a noetherian scheme without embedded associated primes, or the alternate reduced quasi-compact quasi-separated setting with finitely many components specified in the published source, the adjacent positive cohomology groups of rational-function units are torsion. The boundary

\[
H^i(X,\operatorname{Div}_X)\longrightarrow H^{i+1}(X,\mathbf G_m),\qquad i\geq1,
\]

is therefore an isomorphism modulo torsion. This is an exact own-publication match: *Le groupe de Brauer II*, Lemma 1.1 and Corollaries 1.2–1.3, pp. 290–291 (Grothendieck, 1966). It is not an integral isomorphism, and the deletion of the displayed proof route is not deletion of the surviving statement (C-SA06-804–805).

The following strictly henselian factorial clause stops at a colon. Proposition 1.4 of the same publication gives a highly plausible comparison, proving the stated higher G_m-cohomology torsion result under its hypotheses. It is not the missing words on this leaf. C-SA06-806 remains an unidentifiable incomplete clause, with the published proposition recorded as a contextual continuation candidate. This is a useful example of a strong literature match that does not authorize completing the diplomatic text.

### Real fibre objects, polarizations and effectivity

Scans183–187 work after a choice of a real fibre functor and relevant Artin/Tate identifications. With those data, the Isom tensor torsor has a reduced structure group G⁰⁰=ker(ε|G⁰), and the group at another fibre is an inner form. Changing a comparison trivialization produces conjugacy. These constructions are established at the indicated Tannakian level; they do not prove that every unspecified integral category in the agenda is neutral over R (Deligne & Milne, 1982, Proposition 2.8, Theorem 3.2 and §5; C-SA06-807–809).

The finite-polarization remark must be read literally before choosing a modern repair. For a complex torus T of rank r, Hom(μ₂,T) has 2ʳ elements. For GL₂, however,

\[
A_t=\begin{pmatrix}1&-2t\\0&-1\end{pmatrix},\qquad A_t^2=1,
\]

gives infinitely many literal homomorphisms μ₂→GL₂, all in one conjugacy class. This refutes literal finiteness without refuting finiteness of conjugacy classes or of admissible polarization classes. The deletion of “classes de” therefore matters (C-SA06-810). No classification theorem is inferred from this elementary counterexample.

There are two further losses of information. First, restriction of a cocharacter to μ₂ remembers only its class modulo2: μ and −μ have the same restriction and opposite oriented rays. An effectivity cone cannot be recovered from those involutions without retaining the full cocharacters and their normalization (C-SA06-811). Second, Frobenius integrality in *every representation* is incompatible with an unrestricted rigid category containing a Tate object and its dual. If one eigenvalue is an integer q>1, its dual eigenvalue q⁻¹ is not an algebraic integer. A corrected criterion must specify an effective subcategory or monoid; reconstructing it from all Frobenius conditions is a further conjectural step (C-SA06-812; MP-SA06-335–336).

The title about Frobenius distribution does not supply a measure, a counting order, a density or a limiting assertion. Polarization and inner-form constraints can be inputs to a distribution problem, but no Sato–Tate theorem is thereby stated or proved on the supplied leaves. The inserted restriction from “most” to “certain” questions is retained (C-SA06-813).

### Henselian origins, Lang's theorem and p-adic comparisons

On scan 191 the proposed ℓ-adic and Witt-valued objects are said to come “sans doute” from smaller henselian rings; these origins remain hypotheses. The invocation of Lang can be made exact in a limited setting: a torsor under a smooth finite-type group scheme over a henselian local ring, whose group-scheme special fibre is connected over the finite residue field, first has a point in the special fibre by Lang's theorem and then lifts by smooth Henselian lifting. Connectedness of the torsor itself is not a substitute: Spec(F_(q²)) is a connected finite étale Z/2-torsor over F_q without an F_q-point. That supplies an isomorphism class, not a unique isomorphism. An arbitrary proalgebraic group or inverse system does not automatically satisfy these hypotheses (Lang, 1956, Theorem 1 and corollary; Stacks Project, checked smooth-lifting and henselian tags; C-SA06-818).

The proposed extension to perfect fields of “dim ch1” is separately questioned and textually uncertain. It is not silently turned into a statement about cohomological dimension. Nor does levelwise nonemptiness imply a compatible point of every inverse system. The note's finite-stage/global distinction is retained; a countable inverse system with surjective transition maps gives a valid sufficient condition, whereas a projective system can fail it (C-SA06-819–820). The neighboring pages219–221 were read as actual endpoints: they later distinguish the finite-stage question from the global one and use a countable path-torsor argument under additional transition hypotheses.

For connected locally noetherian schemes, geometric fibre functors on finite étale covers are isomorphic, with noncanonical path torsors. This is the precise SGA1 comparison relevant to scan 193. It must not be rephrased as a unique canonical isomorphism (SGA1 V, Theorem 4.1, Proposition 5.6, Corollary 5.7 and §7; C-SA06-821). The p-adic paragraph separately distinguishes a semilinear automorphism of a fixed fibre from an automorphism that changes the field-valued point and therefore moves the fibre. The uncertain H¹/H² exponent is not resolved from expectations about Tannakian theory (C-SA06-814,822–823).

The relation FV=p has a concrete tensor boundary. In the saved rank-two slope-one-half linear model, F²=−p and V=−F. Then FV=p, but the unmodified tensor operators satisfy

\[
(F\otimes F)(V\otimes V)=p^2.
\]

An integral category in which the same fixed relation FV=p is required of every tensor power cannot use this unmodified tensor law. Oda's degree-one abelian comparison has precisely delimited content; it is not a construction of that whole tensor category (Oda, 1969, Corollary 5.11; C-SA06-816–817). This exact linear model tests the tensor relation. By itself it neither identifies the integral lattice of a particular elliptic curve nor settles the ξ_p determinant-orientation problem; semilinear realizations require the indicated coefficient twists.

### Betti/de Rham comparison and the three real involutions

Scans199–203 combine an integral Betti lattice, a complex comparison and real structures. The de Rham and torsion étale comparisons are established in their standard geometric domains. The exact SGA4 XVI Theorem 4.1 requires the indicated finite-type complex setting and properness or constructibility, with the degree ranges appropriate to sets, groups or torsion abelian sheaves. One cannot recover the unrestricted integral motivic programme merely by citing a rational comparison (Grothendieck, 1966, algebraic de Rham theorem; SGA4 XVI, Theorem 4.1; Bost & Charles, 2016, §2.1).

The conjugation discussion requires distinguishing semilinear coefficient conjugation, the conjugation coming from the real de Rham form, and the geometric real involution on Betti cohomology. After transport through comparison, the first two compose to the third under the real-structure compatibility being asserted. A Tate comparison with period2πi checks the necessary sign: conjugating coefficients changes2πi to−2πi. Replacing both semilinear operators by an unqualified ordinary conjugation erases the phenomenon. C-SA06-825–826 keeps this bookkeeping and the page's “à vérifier” flags separate from a universal motivic comparison theorem.

### The Hodge-filtration formula: false literal statement, own later correction

Scan205 expresses the temptation to identify a rational Hodge-level intersection with the corresponding motivic filtration. Its literal rational-intersection equality is too strong. Grothendieck's own 1969 note explicitly corrects the generalized formulation by taking the **largest rational sub-Hodge structure** contained in the prescribed Hodge-level subspace (Grothendieck, 1969, “Hodge's general conjecture is false for trivial reasons,” §§1–2, pp. 299–301). The note was received on27 October 1968; its publication year is1969. The title concerns this generalized formulation, not a disproof of the usual rational Hodge conjecture.

An independently checked example makes the distinction concrete. Let τ be the upper-half-plane root of T³−2 and let E=C/(Z+τZ). In

\[
V=H^1(E,\mathbf Q)^{\otimes3}\subset H^3(E^3,\mathbf Q),
\]

the projection to H^{0,3} has coefficients spanning 1,τ,τ²,τ³ over Q, of rank3. Its rational kernel K therefore has dimension8−3=5. Rationality forces simultaneous vanishing of the conjugate H^{3,0} component. K is exactly the naive rational level-one intersection in V, but an odd-weight rational Hodge structure has even dimension because its H^{p,q} summands occur in conjugate pairs. K cannot be a sub-Hodge structure.

The real-base qualification also was checked rather than assumed. For the real Weil restriction X=Res_(C/R)(E³), the relevant rational Hodge summand is W=V⊕V̄, and the naive intersection there is K⊕K̄. Its dimension10 is even; parity on the pair proves nothing. If the full naive intersection were a sub-Hodge structure, intersecting with W and projecting by its rational Hodge projection onto V would make K a sub-Hodge structure, a contradiction. The restriction-and-projection step is essential. The rank calculation and this proof received an independent second-agent check (C-SA06-827 and its certificate).

What remains conjectural in general is the corrected assertion relating that maximal sub-Hodge structure to geometric coniveau or motivic effectivity. Thus an exact historical correction and an open modern programme coexist. The dossier neither calls the false intersection an open conjecture nor claims that correcting it solves the generalized Hodge conjecture.

### Reused projectivity and Lie-theory sheets

The projectivity proof leaves have source folios 73,72,70 in archive scan order, with the earlier supplied folio 74 in the middle packet. Folio71 is not present. Their hyperplane/cohomology induction is comparable with Serre's exact sequence and eventual global-generation/vanishing theorem (Serre, 1955, §47 Theorem 5 and Corollary 2; §66 Theorem 2). FAC §66 is applied on the already projective divisor or support after the Cartier exact sequence; it is not used to assume the ambient projectivity that the argument seeks to prove. The missing folio is a source boundary, not an invitation to invent the author's completed proof (C-SA06-828).

The exceptional-root exercises were checked through integral Cartan matrices, determinant/radical calculations and root counts. E₆ and E₇ have Cartan determinants3 and2 and72 and126 roots, respectively; reducing in the corresponding bad prime makes the radical and quotient dimension part of the statement, not an optional convention. The later root-space and sl₂ leaves need finite dimension, splitting and characteristic assumptions. For a highest-weight vector v₀ of weight m in characteristic zero and v_n=fⁿv₀/n!, one obtains

\[
e v_n=(m-n+1)v_{n-1},\quad f v_n=(n+1)v_{n+1},\quad h v_n=(m-2n)v_n.
\]

The recurrence was re-proved directly from the brackets. Complete reducibility is a separate theorem, and the same manipulation does not justify an arbitrary characteristic-p version (Humphreys, 1972, §§6.3,7.2; C-SA06-832). In sl₂ the Killing orthogonal of the positive nilpotent algebra is the positive Borel, not the negative Borel; the incorrect alternative is already struck out in the source (C-SA06-831). In characteristic2 the scalar matrix lies in sl₂ and the algebra's structure changes; the exact small-field computation confirms the danger of importing the characteristic-zero statement unchanged (C-SA06-834).

For generalized weights, a bilinear equivariant operation adds additive weights, or multiplies multiplicative ones, after the nilpotence orders are combined. The proof uses commuting nilpotent defects and the binomial theorem; substituting eigenvectors proves only the ordinary-weight special case. Humphreys §15.1, pp. 78–79, was read for this exact result (C-SA06-835). The Cartan statements were checked with their actual field and characteristic restrictions. Bourbaki's publisher contents were available for locating corresponding chapters, but the theorem bodies in that volume were not accessed; no mathematical proof is certified merely by that contents match. The final triality/integral-form editorial list remains a set of identifiable topics and missing-reference requests, not a single new theorem (C-SA06-836).

## What the earlier notes got right, and what the consolidation changes

The earlier notes often isolated the right pressure points: the withheld saturation axiom, the integer in a miniversal correspondence, the ambiguity of the norm normalization, the missing coherence behind a commutative Brandt construction, and the difference between finite-stage and global comparison torsors. The consolidation preserves those observations. Its principal changes concern quantifiers, coefficient rings, attribution, and proof boundaries. A later theorem in the same subject is not treated as a solution until its objects and hypotheses match.

| Passage or earlier interpretation | Finding after the transcription and source checks | Canonical records |
|---|---|---|
| The 1965 Serre letter stops before the second conjecture and conclusion | Its supplied Codex continuation completes the letter. The second conjecture, affine proposal and author's qualification of an earlier equivalence must all be included. | SA06-98; C-SA06-56–64 |
| The 1965 cycle-space Lefschetz conjecture can be read as the published standard conjecture | The letter uses algebraic equivalence. The later cohomological formulation has a different quotient. Griffiths-group counterexamples refute the literal algebraic-equivalence Lefschetz and affine assertions. | C-SA06-56,58–59,94,239; MP-SA06-22,24,126,130 |
| The proposed Albanese relation is simply the familiar incidence relation | The manuscript defines a relation by images of Albanese kernels. The checked comparison gives an inclusion in the incidence kernel, with a limited transpose argument; equality is not supplied. | C-SA06-22–38,44–48; MP-SA06-11–18 |
| Rational existence removes the need for denominators | A family inducing a positive multiple on an Albanese is not a family inducing the identity. The two integral inverse questions have different modern obstructions. | C-SA06-35,270–271; MP-SA06-149–150 |
| A one-cycle correspondence is a new assertion each time it appears | The statement on14/058 and construction on059–061 are one Proposition 2.1. The mixed-ample summary and its later curve proof are likewise one assertion. | SA06-103; C-SA06-90,88 |
| Every normalized elliptic Frobenius eigenvalue in the finite-field fragment is a root of unity | The ordinary elliptic example over F₅ refutes that universal gloss. The alternative two-eigenspace case remains separate. | C-SA06-54–55 |
| A usual Lefschetz sl₂ action automatically sits in the motivic tensor group | On h(P¹), tensor automorphisms fix the unit inclusion and the prescribed raising map does not. The rational graded correspondence action, shifted Cartan relation and Tate-character conjugation are retained as three distinct clauses. | SA06-255; C-SA06-442–444 |
| Semisimplicity makes the relevant group centre-free or forces a kernel to vanish | Rep(Gₘ) and the dual-number example distinguish semisimplicity, centres, nilpotence and equality of quotient relations. Each comparison keeps its actual category and coefficient field. | SA06-2,36; C-SA06-441,446 |
| The Deuring norm character is automatically onto on global points | Its cokernel is the norm-line obstruction. Scalar μ_n automorphisms, a band and a chosen neutralization are different levels of the construction. | C-SA06-700–704; MP-SA06-300–304 |
| The Frobenius order automatically is the full ring of integers | The trace-zero p=7 elliptic case distinguishes Z[π] from the maximal order. The ξ_p problem survives with a necessary order hypothesis. | C-SA06-710–711; MP-SA06-307,303 |
| A finite-field construction exists canonically in the written generality | For p=2,n=3, the degree-six quotient F₂[T]/Φ₇ is F₈×F₈, not the asserted field F₈. Choosing an irreducible factor and compatible embeddings are extra data. Nearby cancellations and the later two-categorical alternative are retained separately. | C-SA06-707–708; MP-SA06-305 |
| Every monoidal autoequivalence automatically preserves the chosen Brandt/Picard commutor | The ideal-model commutor is valid under condition(C). A finite counterexample with a fixed tensorator refutes automatic symmetry preservation; a possible tensorator repair and the narrower inner/Morita reading are retained. | C-SA06-719–721; MP-SA06-312–313 |
| The finite-field gerbe's order is determined without specifying the motive and realization | The F₈ threefold calculation is conditional on a precise rank-six h¹/Tannakian interpretation and its usual endomorphism algebra. It does not identify the manuscript's unspecified M. | C-SA06-434; MP-SA06-214 |
| A polarization remark proves literal finiteness of all homomorphisms μ₂→G | There are infinitely many literal such homomorphisms to GL₂ in one conjugacy class. The missing or deleted qualification changes the assertion. | C-SA06-810; MP-SA06-335 |
| An involution determines the oriented effectivity ray | Restriction to μ₂ loses the distinction between μ and −μ. The full cocharacter lattice and orientation remain necessary data. | C-SA06-811; MP-SA06-336 |
| Frobenius integrality can be imposed on every representation in an unrestricted rigid Tate category | A Tate object and its dual give reciprocal eigenvalues. The criterion needs an effective range before any converse can be proposed. | C-SA06-812; MP-SA06-336 |
| FV=p can be imposed unchanged after taking tensor products | With the unmodified tensor operators, the relation becomes p² on a double tensor product. The degree-one Oda theorem does not construct the proposed integral tensor category. | C-SA06-816–817; MP-SA06-339 |
| Lang gives a canonical global fibre comparison in the pro-category | Smooth finite-type and connected-special-fibre hypotheses give finite-level existence after henselian lifting. Uniqueness, inverse-limit compatibility and descent from the proposed smaller rings are additional assertions. | C-SA06-818–823; MP-SA06-338–345 |
| The rational Hodge-level intersection is the desired sub-Hodge structure | An explicit rank-eight example has a rank-five intersection, and the real-base version has been checked by restriction and projection. Grothendieck's own later correction uses the largest rational sub-Hodge structure. | C-SA06-827; MP-SA06-348 |
| A source fragment with a missing adjacent page has no usable proof | Several supplied continuations close that gap. Other missing source folios and analytic formula alarms remain genuine limits. They are recorded separately from the valid local theorems. | C-SA06-468,496,499–500,828; MP-SA06-224,231–233,238–239 |

The distinctions in this table do not rest on the table alone. Each canonical claim contains the relevant source locator, the precise statement, the literature match and the proof or computation pointer. The source-entry verdicts remain attributable to the entry that made the earlier assertion. An entry can be mathematically sound as an editorial comparison while its comparison is explicitly absent from the historical page.

## Historical development and the state of the subject in November 2026

### Exact continuities with Grothendieck's own work

The strongest historical matches are local and testable. The live rational-function/divisor argument at15/179 matches *Le groupe de Brauer II*, Lemma 1.1 and Corollaries 1.2–1.3, including the isomorphism only modulo torsion. That publication records November 1965 as first circulation and appeared in1966. The unfinished factorial clause is kept unfinished even though Proposition 1.4 gives a very plausible continuation (Grothendieck, 1966; C-SA06-804–806).

The Picard and correspondence passages are illuminated by Grothendieck's 1962 Picard-scheme treatment and the exact numerical/algebraic-equivalence theorem in SGA6, ExposéXIII, **Théorème4.6**, pp. 645–647. The common earlier label “Proposition 4.6” was corrected in the consolidation's commentary and reference audit. This is a bibliographic correction, not an emendation of the manuscript. The relative Picard statements still need their representability and base hypotheses; one cannot extend a field-level argument to every base by suppressing them.

The finite étale fibre-functor assertion on15/193 has a direct SGA1 counterpart: ExposéV, Theorem 4.1, Proposition 5.6, Corollary 5.7 and §7. Its isomorphism is noncanonical. The complex étale comparison has a separate SGA4 XVI Theorem 4.1 match, with the actual properness/constructibility and coefficient qualifications. Several group-scheme fragments in late cote 14 can be matched just as precisely to SGA3, while the ampleness passages require the EGA/SGA hypotheses recorded in their individual claims. These sources are identified by exposé and theorem, rather than by the name of a large multivolume work.

Two later interventions by Grothendieck are especially decisive. His letter to Mumford of20 November 1968, Letter 46, p. 151, explicitly uses Mumford's zero-cycle result to reject the box-cycle expectation on products of elliptic curves. His note received27 October 1968 and published in1969 corrects the naive generalized-Hodge formulation by replacing a rational intersection with the largest rational sub-Hodge structure it contains. Neither observation redates the archival leaf. Both supply evidence stronger than a retrospective resemblance to a modern topic (Grothendieck, 1968, 1969; Mumford, 1969).

| Work or event | Date distinction retained | Exact role in this dossier |
|---|---|---|
| Letter to Serre in the manuscript | 27 August 1965 | Historical algebraic-equivalence Lefschetz programme, including its own qualifications |
| *Le groupe de Brauer II* | First circulation November 1965; publication1966 | Exact divisor-sequence and torsion statements |
| Oda's de Rham/Dieudonné comparison | Dissertation June 1967; journal1969 | Abelian p-kernel and full Picard-scheme statements under the chosen contravariant convention |
| Letter to Mumford, Letter 46 | 20 November 1968 | Explicit rejection of the box-cycle expectation |
| “Hodge's general conjecture is false for trivial reasons” | Received27 October 1968; publication1969 | Exact correction of the generalized formulation |
| Published standard conjectures | Publication1969 | Cohomological algebraic classes; not the algebraic-equivalence quotient of the 1965 letter |
| Beauville's SL₂ correspondence action | First arXiv version11 May 2008; journal2010 | Rational correspondence action with its grading and coefficient restrictions |
| Kahn's motivic descent article | Received30 May 2024; final29 May 2025; published25 June 2025 | Precise descent statements; an earlier first-preprint date was not independently established |
| Terenzi's geometric connectedness remark | First version23 March 2026; inspected v2 dated19 August 2026 | Exact arithmetic sequence plus explicit conjectural geometric connectedness |

These dates belong to the cited works or their documented circulation. They are not estimates of when Grothendieck wrote each reused or undated sheet.

### What is established, what fails, and what remains conditional

The established degree-one theory is substantial: Picard and Albanese varieties, their rational Tate realizations, the isogeny criterion, divisorial correspondences, rational inverse correspondences and degree-one Lefschetz isogenies. The complete-intersection curve argument also preserves the mixed product of n−1 possibly distinct ample divisors. Its validity does not establish the arbitrary-degree standard conjectures, a whole-Chow-ring hard Lefschetz assertion, or integral inverses (Kleiman, 1968; Milne, 2008; C-SA06-87–88,90,264–266,268–269).

The integral questions are now sharply separated. Voisin's published threefold example shows that representability of CH₀ does not guarantee an integral universal zero-cycle; Alexandrou's checked2026 preprint supplies surface examples under its elliptic endomorphism hypotheses. This answers the first universal assertion negatively, while the positive-multiple construction remains valid. For the second question, the dossier gives an explicit inference from primary results: an integral inverse-Poincaré mixed one-cycle would force the relevant integral one-cycle Hodge assertion, contradicted by the checked very-general principally polarized abelian-variety examples in dimension at least four. The factor components, torsion-free cohomology and factorial normalization are dealt with in the saved proof and exact exterior-algebra calculation. The second conclusion is labelled this run's inference from Beckmann and de Gaay Fortman and from Engel, de Gaay Fortman and Schreieder; it is not presented as a verbatim theorem of either source (C-SA06-270–271; MP-SA06-149–150).

The full algebraic-equivalence and Chow versions of the 1965 Lefschetz hopes cannot be recovered simply by citing cohomological hard Lefschetz. Griffiths groups supply the explicit obstruction used here. Jannsen's semisimplicity of numerical motives establishes a quotient-category theorem; it neither proves that algebraic and homological equivalence coincide nor forces every realization to factor through an unspecified quotient. For abelian schemes, Künnemann's rational Chow-motive decomposition and Beauville's correspondence action supply strong positive results with rational coefficients, an actual polarization and their specified base assumptions. They do not remove integral factorials or the Beauville grading shift (Clemens, 1983; Jannsen, 1992; Künnemann, 1993; Beauville, 2010).

The manuscript's various motivic groups cannot all be identified with a modern construction. Choudhury and Gallauer's Nori–Ayoub comparison is in the chosen Betti setting and concerns the degree-zero Hopf algebra under its coefficient hypotheses. The pure Nori/André comparison is rational and motivated; it does not prove that motivated correspondences are algebraic. The Nori arithmetic sequence is an exact sequence of affine group schemes, not automatically a sequence of surjective rational-point maps, a split sequence, or an identification of its geometric kernel with the identity component. The last geometric connectedness assertion is still explicitly conjectural in Terenzi's inspected2026 version (Arapura, 2013; Choudhury & Gallauer, 2017; Huber & Müller-Stach, 2017; Kahn, 2025; Terenzi, 2026, Remark 1.11).

The period comparison has the same boundary. A theorem constructing a formal-period torsor does not prove that its complex comparison point is generic, or that evaluation is injective. The manuscript's proposed change of realization can be compared with that framework only after fixing its category, coefficients and fibre functors. Statements about geometric connectedness, transcendence degree and period evaluation are recorded as different assertions (Huber & Müller-Stach, 2017, §13; SA06-39,275,453,828).

The 2026 search also encountered an unusually broad new claim: OpenAI's October 6 preprint *The rational Hodge conjecture for CM abelian varieties*. The primary PDF and its revision record were opened. Theorem 1.1 asserts the rational Hodge conjecture for all CM abelian varieties; the paper also states finite-field abelian Tate and standard-conjecture consequences. The central theta/Hecke construction was **not independently verified in this consolidation**, and no journal or refereed acceptance was verified. These statements are therefore recorded as current preprint claims, with their exact status, not as established settlements on which to close the manuscript's general problems. The separate Broe endpoint remained unavailable and is marked unverified. This distinction is material: a bibliographically verified primary preprint is not automatically a verified proof.

The remaining positive-characteristic and integral constructions remain dependent on data the manuscript itself is trying to specify: the normed category, its integral lattices and orders, compatible tensors and duals, the band, the obstruction class, and coherent neutralizations. The saved elementary calculations can disprove a universal statement lacking one of those hypotheses; they do not determine all those data. The most useful remaining questions are consequently the finite, explicit ones in the direction list, rather than an assertion that the whole programme was either completed or abandoned.

No classD claim is assigned. This reflects the strength of the justified conclusions, not a declaration that every identifiable manuscript idea has a fully developed modern theory. The meaningful unresolved cases are classC with an explicit missing implication, or classF when the source does not determine a theorem. None of the failed searches is presented as evidence of originality.

## Cross-folder and other-project links

### Archive links are textual claims with two endpoints

The checked continuations repair several artificial boundaries introduced by transcription packages. They include14/044→045–047 for the Serre letter;14/058→059–061 for Proposition 2.1;15/060–061→B15-01/063 for the reasonable-tensor/strict-generator discussion; and15/184 sourcefolio73→15/126 sourcefolio74 for the projectivity argument. The analytic recursion, majorant completion and local-inverse corollary likewise form one theorem across Pro73/75, B15-03/049 and B15-02/047. Proofs of different theorems in the surrounding analytic material remain different records.

The documentary relation between the reused chamber sheets is more cautious. Cote 54/008 carries internal page−13− and no391, while cote 14/022 and020 carry−14− and−15−. The shared number and subject have been checked at both endpoints. But the cote 54 leaf already finishes a chamber-wall proof and Corollaries 2–3, whereas14/020 subsequently introduces the chamber section and Lemma 1. A continuous54→14 join is not established: another draft state or faulty pagination is possible, and the absent scans cannot decide. The local14/022→020 continuation is supported directly. The dossier records the relation and the tension rather than turning a page-number sequence into a proof of continuity.

Other actually read neighboring endpoints include cote 16's projector/Lefschetz normalization, smooth-hyperplane material and explicit singular-hypersurface reformulation request at047, its cohomological Kummer/Brauer sequence, cote 44's curve/Picard material, cote 47's derived Fourier/integral-transform programme at003–011, and cote 54's universal vector extension and Hodge/Dieudonné discussion. The regular punctured-local A/J/N programme belongs to cote 14/106–109; it is not moved to cote 16 or47. The specific “Kummerian” passage at16/052 concerns tame extensions of a complete discrete valuation ring obtained by adjoining uniformizer roots. Its shared word does not verify a motivic lattice-to-cyclotomic-character bridge. The relevant cohomological Kummer/Brauer endpoint is16/021. These are concrete examples of checking both ends changing a link's meaning.

The neighboring cote 15/207–223 and cote 18/005–013 texts were read for the explicitly cited comparisons. They do not become new indexed entries in this part. They qualify the broad places-comparison statement, distinguish finite-stage from global torsor questions, and mark Hodge/Tate premises and later period questions. A cancelled entire cote 18 page remains cancelled. The additional context is not used to decide an ambiguous reading in the frozen part2 transcription.

### Earlier-project leads remain a separate evidentiary layer

The final link table's `our projects` rows retain the cited run and original note IDs. The accompanying endpoint audits record the actual target file and range. A target theorem read in another project's return is described as that return's statement or reported proof unless its proof was independently checked here. This avoids importing those projects as premises for the historical mathematics.

| Earlier-project target | What the inspected endpoint actually supplies | Boundary retained |
|---|---|---|
| LM6 A.22 | A residual question about the stated nilpotent quotient/inclusion | The endpoint remains a question; A.50 is not a solution of it |
| LM6 A.50 | Under the number-field, affine hyperbolic and normalizer hypotheses, a cuspidal or weight-one Jacobian alternative for the procyclic subgroup | It does not say every open-normalizer character is cyclotomic |
| LM7 C.1 | The Picard 1-motive and generalized Jacobian of the punctured Fermat curve, including the cusp torus, dual lattices and full abelianized weight count | The whole abelianization is not replaced by a rank-two selected quotient |
| LM7 C.5 | The specified divisor-extension class, its exact order and splitting after the stated multiplication map | This is not a universal assertion about all Galois-cohomological extensions |
| LM7 C.8 | A precise obstruction to the earlier whole-Fermat rank-two description | Its hypotheses and selected versus whole representation distinction remain explicit |
| LM7 E.23 | A long updated section-image statement with later milestones and a final unrestricted target still marked open | Reading that current statement does not re-prove all intervening milestones |
| LM7 PUSH E.67 | A finite Gaussian/Mordell sign-comparison result and its separately stated origin-fibre analysis | The endpoint expressly does not provide a full GT lift; the computations were not independently repeated here |
| FLAGGED149 B.9 | A prime-to-p higher-genus injection question, still open in the retrieved target | The original cote 149 scans were not available or inspected |
| Hua modern transcription context | Concrete alternative wording and reconstruction of the normed Deuring, ξ_p, Brandt and positive-involution passages | It is a secondary textual comparison and cannot decide the manuscript ink |
| Registry #964 and WG-labelled leads | The particular neighboring mathematical passages or registry labels that were actually retrievable | No identity with an unretrieved original registry theorem or run is invented |

The reference to “S6/S17” in one context packet is a reference to its CN notes in the projector comparison. It is not automatically an independently identifiable S6 project theorem. No supplied Pro entry contains an explicit *Les Dérivateurs* cross-reference sufficient to establish a new link merely because the overall task names that project. Any broader analogy remains an earlier-context lead, not a checked dependency of the motivic claims.

For unresolvable named run identities, the final evidence statement records the bounded search and the unresolved attribution. Such a row is a **checked assessment of an asserted lead**, with the missing identity explicit; it is not counted as a verified mathematical implication between two theorems. The target that could actually be read, if any, is named separately. This is the remaining documentary limit of those leads, not unfinished mathematical consolidation.

## Search, proof and computation audit

Every pre-consolidation claim has an executed search mapping and a check event; these follow the aliases into every canonical claim. Searches were organized by the mathematical assertion and its hypotheses. Shared lemmas sometimes use one inspected primary source and one executed query family across several claims; no extra search is invented to make those rows appear independent. `CLAIM_SEARCH_AUDIT.json` preserves the original row and part so this reuse is visible.

The search work used arXiv, Numdam, MathOverflow, EGA/SGA texts, author bibliographies and published-paper reference chains. zbMATH Open was queried directly and through indexed searches; direct access was not uniformly available. Where title queries were weak, later sources were followed backwards to the theorem, correspondence or publication actually needed. Failed fetches and metadata-only access are retained as limits. The collected letters, Picard/Albanese sources, incidence-equivalence papers, finite-field abelian literature, Tannakian sources and reused-sheet treatments were opened at the locators recorded in the reference audit.

The consolidated bibliography contains only real source records retained from those checks. A `note={verified}` means the stated endpoint was opened and the recorded scope checked. It can mean a theorem statement and surrounding argument, or only publisher metadata/contents when that is explicitly the recorded scope. It never silently certifies an uninspected proof. `REFERENCE_AUDIT.json` retains the original records, alternate URLs, editions, page locators and limitations; `parts/reference_merge_review.json` documents the reviewed aliases and corrections. Four entries remain explicitly unverified rather than being cited from memory.

The exact programs are finite certificates attached to specific assertions: matrix and character calculations, elliptic point enumeration, integral lattices and orders, exterior-algebra factorials, polynomial ranks, quadratic forms, root lattices, and checks of analytic coefficient identities. Their saved outputs are included with the programs. A bounded enumeration is not described as a proof for every rank. A counterexample records its field, coefficients, category and failed hypothesis. Symbolic identities and independent arguments, where given, are separated from numerical tests.

The Hodge-filtration counterexample received an independent second-reader proof check, including its real Weil-restriction qualification. The whole-claim structural audit checks source-search/event coverage and that every named certificate resolves; it is not advertised as an independent proof of all 374 mathematical records. Similarly, the cross-package identity audit read candidate assertions and their source passages to decide identity and scope, not to manufacture new proof-check events for every inherited result.

All mathematical reading alarms remain undecided on the ink. They include alternate indices, the sign and size direction in majorants, deleted qualifiers, degree and Tate-shift conventions, uncertain group names and words, order/maximal-order distinctions, and inconsistent source pagination. The complete reading table retains the evidence and the amount of mathematics affected. The run made **zero transcription edits**.

The distributed archive contains the authored ledgers, narrative, proofs, search/open logs, merger decisions, validation, programs and useful program outputs. The attached source files, copied full external project returns, downloaded full publications and browser-response caches are excluded. Their locators, manifests and relevant scoped findings remain available for reproduction. Historical part-level files are retained as audit evidence; the top-level SA06 tables and their explicit alias map are the final consolidated records.

## Final counts and completeness

These are counts of the final canonical tables. The four original part tables are preserved as audit history. The semantic review merged 28 item records, four duplicate claim records and one duplicate problem record; it also redistributed one compound claim and one compound problem into their two already existing, distinct targets. Consequently the original 412 item, 379 claim and 178 problem records become the canonical totals below. No source-entry verdict row was deleted.

| Final measure | Count |
|---|---:|
| entries | 437 |
| items | 384 |
| claims | 374 |
| problems | 176 |
| readings | 219 |
| directions | 24 |
| links | 540 |
| references | 138 |
| check events | 1476 |

### Source-entry verdicts

| Category | Count |
|---|---:|
| kept | 323 |
| merged | 73 |
| corrected | 40 |
| rests on a misreading | 1 |

The verdict vocabulary is normalized for machine use. A corrected entry can also contribute to a merged item; its correction remains the principal verdict and the merger is recorded in its reason. Withdrawn statements in the manuscript are retained as items with that kind; this does not require withdrawing the note that correctly identified them.

### Item kinds and checks against the text

| Item kind | Count |
|---|---:|
| idea of the earlier run | 61 |
| other | 28 |
| reading question | 76 |
| unproved claim | 88 |
| self-flagged step | 49 |
| unpursued implication | 35 |
| conjecture | 16 |
| withdrawn in the same text | 16 |
| title, date or page count | 15 |

| Check | Count |
|---|---:|
| agrees | 339 |
| understates | 19 |
| overstates | 2 |
| misreads | 1 |
| not on the page | 23 |

### Literature-fate classes

| Class | Count |
|---|---:|
| A | 22 |
| B | 72 |
| C | 86 |
| D | 0 |
| E | 169 |
| F | 25 |

ClassA is an exact own-publication match; B is established later development, including an established negative answer; C is partial or conditional development; D would require an explicitly bounded unmatched-search finding; E is standard mathematics or a scoped standard correction; F is a formulation not identifiable from the available text. These counts are not a score of true versus false assertions.

### Principal status on the pages

| Principal source status | Count |
|---|---:|
| stated without proof | 100 |
| proof sketched | 89 |
| open on the pages | 79 |
| proved there | 56 |
| corrected by himself later | 10 |
| false as stated or literal reading refuted | 39 |
| editorial reconstruction of a qualification | 1 |

This display abbreviates the already authored status labels; `audit/source_status_display_map.json` records the mapping for every claim. In particular, a historically open claim can have a later refutation, and a literal reading alarm does not decide what the ink says. The complete qualified statuses remain in `SA06_claims.json` and `COUNTS.json`.

### Links and reference verification

| Link kind | Count |
|---|---:|
| folder | 186 |
| published work | 208 |
| our projects | 146 |

| Reference endpoint | Count |
|---|---:|
| verified | 134 |
| unverified | 4 |

The links include explicitly rejected or attribution-limited assessments of earlier leads, with their reasons; they are not all claims of mathematical implication. The four unverified bibliographic records are Auslander1966RingedSpace, Broe2026TateFourfolds, Osgood1916 and Giraud1971. Independently checked replacement sources or direct proofs are named where used. No claim is upgraded merely because an unverified reference was mentioned in an earlier note.

All 437 indexed entries have one verdict. All 374 canonical claims retain a literature-search mapping and a check event. All 176 historical problems have a literature-based state assessment; their number includes questions now solved, refuted, corrected or too weakly specified to become a modern conjecture. All 219 reading alarms remain for the scans. The 24 ranked directions are bounded future tasks with item, claim and problem origins; none is developed in this dossier.
