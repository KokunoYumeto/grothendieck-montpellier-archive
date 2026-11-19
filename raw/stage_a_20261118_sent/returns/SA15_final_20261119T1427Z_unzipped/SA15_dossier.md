# SA15 — Cristaux

## Scope, result and conventions

This dossier consolidates the supplied notes and diplomatic transcriptions for
Alexander Grothendieck's Montpellier cotes 4, 5, 6, 7, 8 and 9. Its mathematical
centre is the passage from connections and infinitesimal neighbourhoods to
crystals, their Frobenius structures, the deformation of Barsotti–Tate groups,
and the comparison of cohomological realizations. The folders repeatedly test
whether a proposed construction has enough information to recover a group, a
filtration, a lattice, or a cohomology theory. The failed tests and the author's
own changes of mind are part of that development.

The supplied material supports a substantial account of established results,
explicit errors, incomplete proofs and questions with a narrower modern
formulation. It does **not** support identifying every object called `cris`
with the later PD crystalline site, every object killed by p with a truncated
Barsotti–Tate group, or every arithmetic comparison diagram with a theorem of
modern p-adic Hodge theory. Those distinctions determine many of the verdicts.

The narrative below follows the working sequence 5 → 6 → 7 → 8 → 9 → 4. This
is an expository order through the supplied thematic packets, not a newly
asserted dating of the handwriting. Physical scan order is preserved inside
each discussion, while demonstrable continuations and reused typescripts are
identified. The catalogue dates and titles are taken from `TOPIC.md`; they do
not date each individual leaf.

### What was actually supplied

The attachment contains 23 files. There are four Pro transcription packages,
their notes and doubts, four additional Codex transcriptions with short notes,
the note index, the topic catalogue, and the transcription preamble. No scans
and no `second_pass/` files are present. All supplied in-scope transcription
blocks, Pro notes and doubts, and Codex alternatives were read. An absent
second pass is the expected source condition, not an unfinished task.

The index has **80 rows, all from one package**,
`MPL_7_061-072+8_001-078`, rather than 80 rows spread over four packages as the
brief describes. The other three packages use `##` note headings and are not
represented in that index. Their **847 in-scope entries** have nevertheless
been adjudicated separately: 444 from the first package, 255 from the second,
and 148 from the final package. `SA15_entries.tsv` preserves the exact 80
supplied IDs and one verdict per row. `SA15_supplementary_entries.tsv` records
the additional judgments without inventing entries in the supplied index.
The 80 indexed page-level entries themselves contain 235 separately labelled
subnotes, which are retained in the attribution and item records.

The final package also contains cote 100. Its 201 note entries are outside the
six-cote topic and are listed, with the exclusion reason, in
`SA15_out_of_scope_entries.tsv`. Two explicit links into its supplied scans
were checked at both endpoints solely for the link register. Cote 100 has not
been added to the SA15 claim or problem census.

| Cote | Catalogue subject and dates | Catalogue pages | Supplied Pro scan blocks | Additional Codex blocks |
|---|---|---:|---:|---:|
| 4 | Torsion in crystalline cohomology; undated manuscript and annotated typescript | 11 | 12 | 11 |
| 5 | Crystals and de Rham cohomology; Deligne/Berthelot correspondence, catalogue 1965–1969 | 52 | 52 | 0 |
| 6 | Tate letter, May 1966; typescript and manuscript material | 66 | 64 | 0 |
| 7 | Lecture notes, catalogue November–December 1967 and 1966–1967 | 71 | 70 | 0 |
| 8 | “Cristaux (1970). Gribouillis et calculs divers”; individual leaves undated | 80 | 77 | 3 |
| 9 | Barsotti–Tate groups and crystals, catalogue through summer 1969 | 28 | 29 | 28 |

These are different measures: catalogue pages, scan labels, covers and
alternative transcriptions must not be added indiscriminately. There are 304
in-scope Pro blocks and 42 Codex blocks. Some scan labels are absent from the
supplied sequence, and cote 5 reaches label 53 despite containing 52 blocks.
`work/page_map.json` records every supplied occurrence rather than renumbering
it. The independent Codex witnesses are alternatives for the same leaves,
not 42 newly discovered manuscript pages.

### How to read the registers

`SA15-n` identifies a consolidated item, `CL-SA15-nnn` a claim, and
`MP-SA15-nn` a problem. Source-entry IDs are never replaced by these IDs.
`SA15_id_map.json` preserves the temporary reviewer identifiers as well as the
final ones. A page-level entry may discuss several items; its single verdict
row points to the main item, while every associated item's `sources` field
retains the same entry ID. This preserves the mandated one-row verdict table
without suppressing its subordinate mathematics.

Locations name the cote, scan and **one-based transcription-file line**,
including blank lines. They are not invented line numbers on an unseen scan.
The full file path disambiguates the two Pro packages containing cote 6 or 7
and the Pro/Codex witnesses. Brief quotations reproduce the supplied
transcription; a mathematical correction in the commentary does not amend
that text.

The claim's status on the pages, its later fate, and its truth under stated
hypotheses are separate. Class A means an exact later endpoint in
Grothendieck's own authored published work. SGA's collective title does not
make an Artin or Deligne exposé class A. Class B records established later
development by others; C gives both the established part and the precise
remaining qualification; E records genuinely earlier standard material; F
means the statement or its intended category cannot be identified precisely
enough from the pages. No claim is assigned D merely because a search failed.
A false assertion can have a well-identified later history, and an open step
in the manuscript can be completely settled today.

An “idea of the earlier run” remains attributed to that run. This dossier's
new calculations and refinements are explicitly labelled as present-run
checks. In particular, redoing an earlier counterexample does not convert it
into a new discovery. `CHECK_EVENTS.tsv` distinguishes reading a theorem with
its hypotheses, checking a specific proof step, independently proving an
argument, and running an exact calculation. No proof assistant was executed.

Bibliographic citations below use the keys in `SA15_references.bib`, followed
by exact locators. `SA15_reference_evidence.json` records the URL opened, what
was read, and what was not. A `verified` bibliography note certifies that a
real linked source was opened; a publisher landing page alone does not
certify a theorem or its proof. The search register covers every final claim,
including standard, false and unidentifiable statements. Site-filtered
zbMATH searches are described as such, not as native database sessions.
All present-status judgments are dated **19 November 2026**. Dates of
circulation, the version inspected and publication are distinguished when
the opened sources supply them; unknown first-circulation dates remain
unknown.

## 1. Cote 5 and the first part of cote 6

### Cote 5: divided powers, sites and several inserted texts

The opening diagram connects crystals, stratifications, connections and their topoi. It asks about points and proposes a rank-one Chern obstruction. Those questions remain more specific than a general comparison slogan: the connection/ordinary-stratification equivalence requires a smooth morphism over a **Q-scheme**, not merely a ring of characteristic zero. Integral crystalline Chern vanishing now proves precise necessity statements, but does not identify the coefficient group or prove the ambiguous converse on this page (SA15-1–SA15-4; CL-SA15-001–CL-SA15-003; MP-SA15-01–MP-SA15-02; BO1978 2.15, EsnaultShihoChern2019 Theorem1.1, BhattChern2023 Theorem1.1).

The first sustained calculation constructs a finite universal divided-power algebra. Its p-typical variables satisfy triangular relations with factorial coefficients of valuation one. Translation by the canonical divided powers of p gives the Θ-coordinates used in the asserted normal form. The manuscript leaves the coefficient-necessity verification to the reader and then states quotient formulas W(ν,r). This run supplies a general weighted-ideal proof for every r, including ideal stability through carries and the terminal constant term. Twenty exact multiplication/Smith computations corroborate finite cases; they are not the proof. Hua2026 §35 reports a contemporary formalization of the basic construction but explicitly excludes the r>0 extension from its verified range. No Lean certificate was executed here. The underlying algebra is now justified; exact matching of every truncation axiom in the proposed universal category remains separate (SA15-6–SA15-10; CL-SA15-005–CL-SA15-011; MP-SA15-03).

Legendre’s factorial valuation then explains a boundary that recurs throughout the folder. For a mixed-characteristic DVR with e=vπ(p), divided powers on its maximal ideal exist exactly when e≤p−1. The structure **induced from that DVR** on a nontrivial quotient is PD-nilpotent exactly when e<p−1. At equality, the p-power divided powers of π retain valuation one. These are different assertions, and other PD structures on a quotient are not ruled out by the latter test (CL-SA15-017–CL-SA15-018, CL-SA15-040–CL-SA15-041; BO1978 Proposition3.28).

The parallel-arrow construction forms objects E with a map α*E→β*E, or its invertible variant. The omitted small-generator step can be supplied using accessible categorical inserters and isomorphers, followed by the other Giraud conditions. Its geometric universal property is outgoing: a lax coequalizer, not the incoming universal property of a geometric inserter. The later claim about higher direct images remains conditional on a missing exactness or acyclicity argument; existence of a left adjoint alone is insufficient (SA15-24–SA15-30; CL-SA15-019–CL-SA15-024; MP-SA15-04–MP-SA15-05; Positselski2024 Theorems1.6–1.7, StacksExactAdjoint).

The subsequent divided-power sheets develop free algebras, envelopes, quotient stability, p-typical generation and principal ideals. Modern exact counterparts are available in Roby and the checked Stacks passages. Three local corrections matter. The literal logarithm has the wrong initial sign; the proposed p-unit normalization need not be 1 modulo p; and a torsion-free principal ideal needs πⁿ/n! **inside the ideal**, not merely inside the ring. The earlier notes already isolated these difficulties. Their diagnostics are retained as earlier-run work and rechecked here, including the rank-three torsion-free counterexample x²=2y, xy=y²=0 (CL-SA15-031, CL-SA15-037–CL-SA15-039; MP-SA15-09–MP-SA15-12; StacksPDAxioms, StacksPDPolynomial).

The site pages use locally retractive truncated PD thickenings, explicitly without choosing a retraction as part of the object. Their diagonal envelopes, two-index system, Čech complex and affine inverse limits link directly to cote7/061–064. The modern PD comparison supports the method but does not erase the draft’s transition-map obligations. The finite-algebra Poincaré examples on c5/037 are a separate ordinary Kähler calculation: Euler contraction proves the positively graded cases, while a non-graded Artinian Jacobian algebra has nonconstant closed functions. That earlier-run counterexample does not refute completed-diagonal or derived comparison theorems (SA15-41–SA15-56; CL-SA15-042–CL-SA15-045, CL-SA15-082–CL-SA15-087; MP-SA15-06–MP-SA15-08, MP-SA15-14; BO1978 7.1, Liu2025).

Cote 5 is not a continuous crystal treatise. The CM conductor leaf is exactly Serre–Tate1968 Theorem12; quasi-function/height fragments remain unidentified; Kuiper and K-theory course leaves are foreign material. The finite-target differential leaves have a secure local order, 048→046, from both source pagination and the word join, but their draft numbering is not an exact final-EGA identification. The separate étale-normality note does match EGAIV4 18.12.15 and its proof dependencies. The closing 1965 letter raises relative étale duality and then doubts a naïve p-adic comparison. Deligne’s SGA4 XVIII gives precise later duality statements, classed B under the strict authorship rule; Scholze’s period-sheaf comparison changes both coefficients and topology and does not validate the literal constant-Z_p proposal (CL-SA15-004, CL-SA15-046–CL-SA15-063; EGA0IV, SGA4XVIII, Scholze2013).

### Cote 6: a theory revised while being built

The Pisa project begins with global nilpotent thickenings, then corrects the construction by varying the open subset and imposing stack descent. Crystals, ordinary stratifications and connections must be read with those revisions. Cartier descent describes one zero-p-curvature Frobenius descent; an ordinary stratification requires an infinite compatible system. The literal early equations FV=p and VF=1 force the object to vanish in the intended p-local setting, whereas later pages use symmetric weight relations. This raises an ink alarm rather than licensing an emendation (SA15-97–SA15-118; CL-SA15-067–CL-SA15-096; Grothendieck1968 §4.1, Katz1970 Theorem5.1, Gieseker1975 Theorem1.3).

The finite perfect-field lattice argument is sound: bounded positive F-orbits yield a finite F-stable lattice, and the corresponding F/V statement follows using the commuting relation and bounded denominators. It does not establish uniform effectiveness for arbitrary families. Proper algebraization assumes an actual proper lift. A useful strengthening of the literature verdict concerns local freeness: BO1978 Proposition2.16 and Note2.17 prove it for coherent **full ordinary stratifications on any finite-type field scheme**, without smoothness. Their Artin-neighborhood descent proof was checked. The nonfree connection and PD-lattice examples concern different categories and are not counterexamples (CL-SA15-097–CL-SA15-108; MP-SA15-22–MP-SA15-26).

The cohomological program asks for Gauss–Manin integrability, Leray, perfect derived objects, base change, duality and F/V operations. Katz–Oda1968 supplies exact integrability and Leray successors. PD crystalline theory supplies the later comparison package, with its base and coefficient hypotheses; derived base change does not imply unrestricted base change for every individual cohomology module. The author himself corrects the ordinary positive-characteristic comparison and retreats from automatic integral weight assertions (CL-SA15-110–CL-SA15-117; MP-SA15-28–MP-SA15-31; BO1978 7.1,7.8,7.13).

The abelian pages are especially revision-sensitive. Universal lift independence and a rigid group-valued crystal are followed by a “faux” margin, a modular elliptic-family obstruction and canceled ordinary-case arguments. Grothendieck1968 §3.5 publishes the obstruction. Messing establishes universal vector extensions and deformation by lifted Hodge filtrations under nilpotent PD hypotheses; this is not a restoration of arbitrary ordinary-thickening independence. The later Barsotti–Tate pages ask how much filtered data retains and how to recover the generic integral Tate module. AnschutzLeBras2023 v4 Proposition5.4.2 answers a precise successor using the stronger admissible prismatic invariant over quasisyntomic rings (SA15-141–SA15-160; CL-SA15-118–CL-SA15-136; MP-SA15-32–MP-SA15-41).

Finally, ordinary elliptic extensions lead to Kummer parameters, supersingular image speculation and reduction tests. The earlier CM example over Q₃(i) refutes unrestricted open GL₂ image; the ramified quadratic twist of a Tate curve shows that nonintegral j need not give multiplicative reduction over the original field. Both examples were rechecked, with their hypotheses and refined statements recorded. The split Tate valuation question and the p-divisible good-reduction criterion have exact classical answers; the equal-characteristic formula and the adjective before “simple” remain unresolved readings (CL-SA15-137–CL-SA15-146, CL-SA15-149, CL-SA15-151; MP-SA15-42–MP-SA15-45; KatzSerreTate1981, Tate1995, SGA7IX 5.10–5.13).


## 2. The latter part of cote 6 and cote 7 through scan 60

The latter part of cote6 joins Tate–Hodge questions, formal groups and deformation theory to the machinery that becomes the infinitesimal site. Cote7 first builds that machinery, then pauses for a critical account of de Rham and p-adic cohomology, and finally returns to stratification and Čech calculations. The package contains255 unindexed `##` notes. Their judgments are preserved through82 consolidated items;75 manuscript claims are distinguished from five explicitly labelled refinements made in this run. The supplied transcription, including covers and reused leaves, was read throughout. No scan reading has been changed.

### Tate–Hodge questions and formal groups

The headings on6/038–040 associate the packet with Tate without proving authorship of every leaf. On041 and045 the author seeks canonical comparisons compatible with products and cycles (SA15-175; CL-SA15-152–CL-SA15-153). Faltings1988, ChapterIII Theorem4.1, supplies the proper-smooth Hodge–Tate theorem. The earlier request involving a filtered de Rham splitting is stronger and is not silently identified with that graded comparison. The two representation questions on041 have different answers: an arbitrary continuous irreducible representation need not embed in a Tate twist of C_p, whereas an irreducible crystalline representation with two distinct Hodge–Tate weights gives simultaneous embeddings after twisting (CL-SA15-154–CL-SA15-155; BrinonConrad2009, Theorems8.3.6 and15.1.7). Both deductions are spelled out separately from the source theorems.

Reused analytical leaves interrupt the sequence on042,044 and046. They concern joint continuity of translation, holomorphic functional calculus and Cauchy measures, not crystalline cohomology. Their reconstructed statements have independent proofs, but the missing topology definitions, K/L mismatch and exact typescript source remain reading or identification questions (SA15-179,SA15-182–SA15-183; CL-SA15-157–CL-SA15-159).

The Barsotti question on047–048 uses “hypersingulières” to mean p-rank zero. That definition must survive modernization. In dimension two the slope restriction forces supersingularity; in higher dimension the broad isogeny assertion is false. LenstraOort1974 supplies geometrically simple varieties of the precise formal types needed to compare a simple fourfold with a threefold times a supersingular elliptic curve (CL-SA15-161–CL-SA15-162). On049 the strengthening from “isogenous to a product” to “isomorphic to a product” also fails. An explicit genus-two Jacobian over Fbar_7 has nonisogenous ordinary and supersingular elliptic quotients but cannot itself be their product (CL-SA15-164). The unsure surface/curve wording remains for the ink to decide.

The transcendental-unit construction on050–051 admits a rigorous finite-field reconstruction. A central p-adic unit yields continuous descent at every finite p-power level, and transcendental Frobenius eigenvalues prevent an abelian embedding after every finite extension. The further finitely generated extension clause needs another argument and is retained as a proof obligation, not advertised as a currently open theorem (CL-SA15-166–CL-SA15-167).

On052–057 extension classes become formal torsors and then equations for ordinary polarized moduli. Katz1981, Theorem2.1, verifies the formal torus and the pushout/pullback morphism criterion. Character-lattice equations give the characteristic-p complete-intersection, Gorenstein and smooth-reduction consequences with framing or an adequate level structure. They do not settle the cancelled mixed-characteristic flatness remark or every coarse moduli quotient (CL-SA15-168–CL-SA15-171).

The Witt-extension calculations on059–060 require greater restraint. The exact Demazure–Gabriel locators are recorded, but the opened perfect-field statements do not certify every arbitrary-base quantifier. The author’s immediate “Non” rejects a global Ext inference; a separate Hom paragraph is cancelled. These are different statuses (CL-SA15-172–CL-SA15-175). On061–066 finite étale groups lead to unit-Frobenius modules. SGA1I§8 and BhattScholze2023 Proposition3.4 supply precise counterparts. A derived-duality formula on062 needs a grading check: the elementary Z/p test detects a missing shift under standard conventions (CL-SA15-177,CL-SA15-227).

### Formalization and the first negative result

Cote7/003–015 constructs diagonal neighbourhoods as pro-objects, carefully keeping their several scalar actions. A decisive collation is internal to the package:005 ends where059 begins, and059 ends where006 resumes. The earlier notes’ apparent fragments therefore have extant continuations (SA15-204). Formalization of differential operators, the extra-degeneracy contraction and the spectral sequence must retain coherence, boundedness and inverse-limit conditions (CL-SA15-181–CL-SA15-187). Fiorot2011 gives a precise bounded coherent characteristic-zero development; it does not identify every proposed Artin–Rees category or remove quasi-coherence.

On016–017 the author corrects the hope that his first, non-PD site will provide the desired characteristic-p Weil cohomology. The ordinary-abelian example loses the upper degrees. Grothendieck1968 §6.5 preserves that withdrawal; Ogus1975 Theorem4.9 and Corollary4.11 later identify the Frobenius-stable part under explicit smooth-proper embedding hypotheses. Ogus’s proof flags one unchecked compatibility, which the dossier records. Modern PD crystalline cohomology must not be substituted into the rejected statement (CL-SA15-188). The weak-lifting site proposed on018–019 is a response to this failure, not a renaming of the same construction.

### The lecture’s tests and the return to stratification

The review on021–035 contrasts the smooth complex comparison with the deficiencies of naïve de Rham theory. Grothendieck1966 Theorems1 and1′ give the precise smooth theorem. The characteristic-p affine-line calculation is valid, but the ordinary cusp on024 is not the advertised singular counterexample: the full exterior Kähler complex, including its nonzero second term, is contracted by the Euler derivation. Its positive-degree cohomology vanishes (CL-SA15-193,CL-SA15-196). ArapuraKang2011 supplies a genuinely non-quasihomogeneous replacement; Hartshorne1975 concerns ambient completed complexes.

The finiteness and independence questions must be dated precisely. SGA4XIX5.1 retains a resolution hypothesis; unconditional ordinary positive-characteristic finiteness is assigned here to Deligne’s SGA4½VII1.1. KatzMessing1974 Theorem2(2) supplies integral correspondence polynomials in the smooth projective finite-field setting (CL-SA15-200–CL-SA15-201). Serre’s quaternion obstruction explains why a two-dimensional faithful Q_p-valued H¹ cannot serve as a universal Weil realization; Witt coefficients are a different proposal.

The lifting discussion on035–047 supplies several exact tests. SGA1III§6, Corollaries8 and10, is the affine/formal lift reference. Restricted completion has infinite-rank H¹; integral primitives require both coefficientwise integrality and a convergence tail. The printed positive-exponent radius bound does not express overconvergence. Integral affine Monsky–Washnitzer finite generation fails already on A¹, although rational H¹ vanishes; ErtlSprang2018 proves integral lift independence and ErtlShiho2020 proves stronger nonfiniteness (CL-SA15-209–CL-SA15-217). BMS2018, Theorems1.1 and2.1, replaces the proposed universal torsion equality by inequalities and a strict example.

Finally048–060 seeks canonical comparison through stratification. Derived base change alone does not imply ordinary cohomology base change. Cartan homotopy gives Gauss–Manin, with the local construction published in Grothendieck1968 §3.3, while an explicit smooth Legendre family in characteristic3 has nonzero nilpotent p-curvature, confirming the author’s withdrawal of ordinary stratification (CL-SA15-208,CL-SA15-220–CL-SA15-222). The singular infinitesimal/Betti conjecture on056 is distinct from naïve Kähler cohomology; Liu2025 Theorems1.1/14.1 and1.2 give its exact modern comparison. The Čech–Alexander construction on057–060 continues into061 of the next package, where mutual induction of coefficients controls the limit calculation. The sequence ends with an existing continuation, not a lost page (CL-SA15-224–CL-SA15-226).



## 3. Cote 7: the completed diagonal, scans 61–72

The continuation of the Čech–Alexander calculation begins with a small but
decisive qualification: the coefficients on successive neighbourhoods must
induce one another. Affine vanishing then applies at each finite level, and
surjective transition maps control the inverse limit. Quasi-coherence alone
would not supply the Mittag–Leffler argument. The global version uses the
cosimplicial Zariski sheaf and its hypercohomology, with its first-quadrant
spectral sequence. The dossiers on either side of the package boundary have
therefore been merged at the item level, while their individual claims and
hypotheses remain visible. These are direct predecessors of
Grothendieck1968 §5.1 (SA15-252; CL-SA15-232–CL-SA15-233).

Scans 62–65 construct the covering object from an immersion into a formally
smooth ambient scheme. Formal smoothness supplies the local lifts; formal
neighbourhoods and their repeated products supply the resolution. The
following nilpotent-invariance argument is genuinely elementary once the
coefficient systems have been matched: if I⊂J and J/I is nilpotent, the I-adic
and J-adic powers are cofinal. This identifies the completions, not every
possible coefficient category. The author's separate question about dropping
quasi-coherence is accordingly kept open on the pages. Grothendieck1968
§§5.2–5.3 gives the direct published account (SA15-255–SA15-257;
CL-SA15-234–CL-SA15-236; MP-SA15-83).

Scan 66 then draws the characteristic-zero conclusion: de Rham cohomology of
a smooth lift is independent of the lift and acquires canonical
stratification. Here “characteristic zero” must mean a Q-base for the
factorial argument. The stronger phrase about the derived direct image being
a crystal is retained as a separate coherence requirement. Scans 67 and 69
explain the multiple module structures on the formal complex and its
possibly infinite-order differential operators. It is not an ordinary
O-linear complex by definition. The published endpoints are
Grothendieck1968 Theorem4.1 and §§6.1–6.2 (SA15-258–SA15-259).

The final analytic discussion has three layers. First, proper GAGA compares
the finite coherent neighbourhoods, and the inverse-limit argument must
control cycles and boundaries as well as the terms. Second, the intrinsic
completed-diagonal complex is conjectured to resolve the constant sheaf on
**every complex analytic space**. Third, a flat, locally finitely presented
relative comparison is explicitly marked for proof. The later algebraic
results are substantial but have different scopes: Hartshorne1975 IV.2.1
uses an ambient completed analytic de Rham complex; Bhatt2012
Corollary4.30 and Example4.23 identify the completed diagonal for the
finite-type flat noetherian Q-scheme setting with structure coefficients;
Liu2025 Theorems1.1/14.1 gives the infinitesimal–Betti comparison for locally
finite-type complex schemes. The literal arbitrary analytic-space and
arbitrary-coefficient extensions are not declared solved by substituting one
of these constructions for another (SA15-261–SA15-264;
CL-SA15-239–CL-SA15-243; MP-SA15-84–MP-SA15-86).

The earlier notes already understood this distinction. Their closed-disc
test is also correctly limited. In Q_p⟨T⟩ the form
Σ_{r≥1}p^r T^{p^r−1}dT has no primitive in that same Tate algebra, because
the required coefficients at T^{p^r} are all one. It has primitives on
smaller discs. Thus it obstructs a naïve global integration argument; it is
not a counterexample to every local Poincaré statement in the manuscript's
partly cancelled nonarchimedean terminology. The explicit dual-number
Amitsur contraction and this convergence check belong to the earlier run
and were rerun here (SA15-265; proof audit §§1–2).

## 4. Cote 8: finite groups, ordinary crystals and arithmetic realizations

### The finite-group construction, scans 2–22

The first mathematical leaves seek more than a Dieudonné module. They
assemble co-Lie complexes, two cohomology objects, F and V, triangles,
connecting morphisms, and compatibility with a pair of site morphisms. A
two-term derived object is not determined by its two cohomology objects:
there is an attaching class in Ext². The two boxed composites labelled
“nul?” on scan 8 cross between triangles, so they do not vanish merely by
the axiom for consecutive arrows in one triangle. These are distinct
problems in the final register (SA15-267–SA15-276;
CL-SA15-244–CL-SA15-255; MP-SA15-87–MP-SA15-91).

The manuscript changes its formulation. The large block on scan 5 is
cancelled; scans 10, 12, 16 and 18 propose related live versions. At scan 12
the extra condition for a truncated BT group is not cosmetic. A finite group
killed by p need not be BT1: α_p has F=V=0 and fails ker F=im V. On scan 13,
equality after pullback does not by itself prove equality before pullback.
Ordinary Frobenius over a nonreduced base provides a simple failure of that
inference, but does not by itself disprove the intended enriched crystalline
functor. On scan 20, a “relative Ext” group cannot be treated as a computed
obstruction group until its morphism and cone convention have been fixed.
The filtered vector-space kernel on scan 22 must also be realized by an
actual group before it is a group-scheme counterexample.

Later literature supplies exact answers to parts of this programme. Oda1969
Theorem3.19 and Corollary5.11 identify the perfect-field duality and the
abelian Hodge subspace. The general smooth-proper Picard statement in
Corollary5.12 is narrower. deJong1993 treats the height-one relative
construction; deJong1995 and deJongMessing1999 establish specified
crystalline equivalences or faithfulness under their stated base
hypotheses. Lau2018_2026 and AnschutzLeBras2023 provide further divided and
prismatic classifications in precisely defined categories. None of these
titles alone identifies the draft's enriched target. The 1998 de Jong
erratum and the 2025 Anschütz–Le Bras erratum are recorded with their actual
scope; the latter affects a nilpotence argument, not every classification
theorem in the paper.

The source ambiguity about `VF=id` on cote 6 and the mismatch between an
inequality and a marginal “OK” in cote 8 remain scan questions. The
algebra diagnoses the danger; it supplies no authority to change the ink.

### Ordinary extensions and the virtual-reduction question, scans 25–32

The ordinary packet makes the proposal more explicit. Its connection and
Frobenius matrices, gauge transformation, and rank-one equations can be
checked directly. The deformation equations form a two-step complex only
with consistent matrix order, sign and semilinearity. The identity D₁D₀=0
was checked symbolically; finite freeness and p-torsion-freeness are needed
when an inverse up to a power of p is used. DeJong1995 §4.3,
Lemmas4.3.2 and4.3.5, supplies an exact comparison after the change of gauge
convention b=−L; Katz1981 §4.3 supplies the Serre–Tate interpretation.
This is stronger evidence than a thematic connection to ordinary p-divisible
groups, but still requires the base and the actual crystal structures
(SA15-283–SA15-287; CL-SA15-261–CL-SA15-264; MP-SA15-92).

Scan 32 asks whether virtual good reduction of length at most n descends
from a finite extension when virtual good reduction itself already holds.
Its exact later printed form is SGA7 IX Remark5.13.1, following
Definition5.12 and Proposition5.13. The prime-to-p argument uses the
unipotent inertia filtration; the p-case requires a different argument.
A general semistable comparison theorem is not accepted as a citation for
this exact integral filtration-length statement. A separate deduction in
this run proves it for finite K/Q_p and p>2: a potentially crystalline
descent lemma, an induction using the sum of Galois conjugates of the first
layer, and recovery of the specified saturated Tate lattices from Breuil
and Raynaud. The rational filtration argument works for every p. Integral
p=2 and arbitrary henselian traits are not certified by the sources read;
the unlocated full later endpoint is a documentary residual, not a claim
of contemporary openness (SA15-289; CL-SA15-266, CL-SA15-301; MP-SA15-93;
`work/cotes6_7/sga7_pcase_audit.md`).

### Lubin–Tate calculations, scans 34–56

The A-linear Dieudonné module has f components, each of A-rank one and
W-rank e. Its total W-rank is ef, while the formal-group dimension is
the sum of the exponents r_ν. Integral equivariant maps satisfy a recurrence
and cumulative valuation bounds; the rational classification does not make
every integral map an isomorphism. The stable-lattice construction uses both
ϖ and p^fϖ⁻¹. These finite calculations and the general recurrence proof are
recorded separately (SA15-290–SA15-293; CL-SA15-267–CL-SA15-270).

Two precision tests matter throughout. For ramified A, Ω/pΩ and Ω/πΩ have
different lengths, so they cannot be interchanged in identifying a tangent
line. For the ideal πA, rational divided powers stay in the ideal exactly
at the bound e≤p−1, but the endpoint need not give nilpotent divided powers.
The factor v_p(n!) explains both assertions. A deformation theorem requiring
nilpotent PD data cannot be applied merely from ideal stability.

LubinTate1965 Lemma1 and Theorem1 give the precise normalized formal-module
construction. The derivative-one normalization gives uniqueness of the
chosen isomorphism; unmarked objects retain unit automorphisms. This settles
the broad existence assertion under the appropriate special-fibre and
tangent-action identification. It does not identify the **two particular
integral lattices** compared on scans 48–50 or prove that their exponent α
vanishes. Likewise an arbitrary filtration on an isocrystal need not be
admissible. ColmezFontaine2000 TheoremA is a rational equivalence under weak
admissibility; FontaineLaffaille1982 and Breuil2000 impose additional
integral hypotheses. The dossier keeps the lattice question distinct from
these already established classifications (SA15-296–SA15-298;
CL-SA15-271–CL-SA15-274; MP-SA15-95–MP-SA15-96).

On scans 52–56 the A-rank-one Tate module becomes a Q_p-vector space of
dimension [K:Q_p]. Tensoring over A therefore differs from tensoring over
Z_p. Tate1967 Theorem3 and Corollary2 give the Hodge–Tate comparison, and the
structural embedding picks out the weight-one factor. Every factor carries
the semilinear Galois action, including its action on C. The displayed
eigen-equations determine a nonzero solution up to K×; A× requires a lattice
normalization. Independently rescaling eigenperiods also prevents recovering
all of them from one without compatibility data. Finally “every subgroup of
inertia” is too broad: the trivial subgroup already defeats that wording.
The corrected open-inertia reduction, based on Tate's theorem, is proved
with its field hypotheses in the proof audit. These warnings and tests
already appeared in the earlier notes and are not claimed as new insights
of this dossier (SA15-299–SA15-301; CL-SA15-275–CL-SA15-278;
MP-SA15-97; proof audit §12).

### Tannakian groups and the final agenda, scans 61–75

The later leaves ask for an arithmetic fibre functor, its tensor group,
weight decompositions, comparison torsors, and a common system of Betti,
de Rham, étale and crystalline realizations. Effective filtered objects
need not be stable under duality, so effectivity alone cannot define the
rigid category that the argument needs. Nor does full faithfulness by
itself identify the algebraic envelope of a Galois image. The earlier
notes' Borel restriction example is independently proved here. The
subobject criterion in DeligneMilne1982 Proposition2.21 is the precise
formal repair. André2023 Lemma1.5 adds the alternative of observability;
Theorem2.1 proves it for a specific geometric ℓ-adic setting. That geometric
theorem does not identify the unspecified local p-adic functor on these
leaves (SA15-304–SA15-305; CL-SA15-284–CL-SA15-287; MP-SA15-98).

The torsor calculations become definite once their choices are stated:
changing a period rescales a comparison by the appropriate cocharacter;
Frobenius changes by σ-conjugacy under a new trivialization; fixing an
associated-graded comparison determines the appropriate unipotent splitting
torsor. Ziegler2015 Theorems4.13–4.15 in the inspected arXiv version give
the relevant filtered-fibre-functor
development, subject to its hypotheses. A real comparison transports Betti
conjugation, while a p-adic period comparison belongs over its period ring,
not automatically over Q_p (SA15-306–SA15-308;
CL-SA15-288–CL-SA15-292; MP-SA15-99–MP-SA15-100).

The list on scan 75 names Hodge and Tate conjectures, Frobenius and
filtration, a “double réseau”, and a Tate group over several possible bases.
The classical rational and generalized Hodge statements are different;
Voisin2025 §4.2, Conjecture4.6, formulates the latter in terms of supported
Hodge substructures. Tate1966 settles the finite-field abelian
homomorphism theorem and its divisor consequences, not the general cycle
agenda. Recent 2026 low-dimensional search leads whose primary texts could
not be opened are explicitly unverified. BMS2018 Theorem4.28 identifies a
precise period-ring pair, but does not authorize replacing the undefined
double lattice by that pair. These entries remain divided into exact
conjectures, later established comparisons, and genuinely unidentified
categories (SA15-309–SA15-310; CL-SA15-293–CL-SA15-296;
MP-SA15-101–MP-SA15-104).

### Reused leaves and the return to co-Lie, scans 3–79

The folder also contains mathematics from other working documents. The
double-point fragment on scan 3 matches Lipman1969 §24. Proper-base-change
fragments on scans 7, 9, 11 and 15 match Artin's SGA4 XII; the later smooth
base-change and purity fragments match SGA4 XVI and XIX. Draft numbering,
cancelled hypotheses, the purity twist, and XIX's resolution hypothesis are
not silently imported or removed. The typed jet sequence runs in reverse
scan order and lacks an intermediate page. For origin-preserving k-jets
from dimension p to dimension q, the dimension is
q( binom(p+k,p)−1 ); the printed expression includes the constants.
Characteristic-p ordinary derivatives also fail to recover the T^p jet.
The convolution text already restricts its L∞ endpoint. Exact draft
catalogue identities that could not be opened remain provenance leads,
even where the underlying mathematics is standard (SA15-277–SA15-282,
SA15-294–SA15-295, SA15-302–SA15-303, SA15-311–SA15-312).

Finally scan 78 continues directly into 79 in the next package. For a
group of multiplicative type with character sheaf M, the formula is the
**derived** tensor M⊗ᴸ_Z O_S. Ordinary tensor would discard its torsion
term; μ_n is the elementary diagnostic. BerghRydh2019 AppendixB,
PropositionB.4, proves the formula for arbitrary locally constant character
sheaves. The independent finite-resolution proof here is explicitly
limited to finitely generated characters. This is one consolidated item and
claim with the continuation and coefficient-change steps preserved
(SA15-313; CL-SA15-300; MP-SA15-106).

## 5. The end of cote 8, cote 9 and cote 4

### Co-Lie and representation lifting, cote 8:79–81

The co-Lie calculation continues through the classifying topos of the
character local system. Its two cohomology sheaves are a tensor product and
a Tor group. Over a Z/n-base, when the character sheaf is finite locally
free over Z/n, the two
identified bundles carry a degree-two attaching class. The next leaf relates
this class to lifting a mod-p representation through GL_d(Z/p²). Rank one
lifts by the Teichmüller section; the conjectured universal nonvanishing for
every d≥2 has small exceptions. An explicit integral S₃ representation
gives a section for GL₂(F₂). Singla2010, introduction p.3, records the full
exception list with backward references to Sah and Ginosar. The latter's
publication identity was verified, but the original classification proofs
were not read and are not described as independently checked
(SA15-327–SA15-330; CL-SA15-304–CL-SA15-309; MP-SA15-107).

### Dieudonné duality and the virtual character, cote 9:2–14

Cote 9 first studies reduced F/V data, universal extensions and a
coefficient-functional model for Dieudonné duality. Oda1969 Theorem3.19 and
BerthelotMessing1979 §5 give exact later anchors. The draft's finite
presentation remains more delicate: the truncation index changes the target
of the perfect pairing, one V-action uses F in the supplied reading, and
Pro and Codex disagree about cancellation of the proposed bimodule
isomorphism. The coefficient identities were checked with nontrivial Witt
Frobenius, not only with k=F_p. None of these algebraic tests selects a
transcription reading (SA15-332–SA15-333; CL-SA15-310–CL-SA15-317,
CL-SA15-382–CL-SA15-383; MP-SA15-108).

A cancelled chain-map descent proposal follows. Pairwise null-homotopies do
not by themselves supply all the coherence of a global descended object.
It is kept as a separate construction problem rather than identified with
the already established Gauss–Manin connection (SA15-334;
CL-SA15-318; MP-SA15-109).

The next packet defines a virtual good-reduction class and an inertia
character. Tate's generic-fibre full faithfulness establishes uniqueness of
a good model, not by itself independence of a filtration in a Grothendieck
group. Inertia acts linearly on the special-fibre Dieudonné module; the
residual quotient also acts on its coefficients. A direct semilinear-trace
calculation shows that this defined inertia trace is Z_p-valued, without
the margin's additional condition μ_p⊂K. Independence for a genuinely
potentially-good object and the proposed virtual extension are therefore
recorded separately (SA15-335–SA15-337; CL-SA15-319–CL-SA15-324,
CL-SA15-380–CL-SA15-381; MP-SA15-110–MP-SA15-111).

The broad attempt to recover the character from generic mod-p torsion is
withdrawn. The restricted elliptic question also has a negative answer,
proved explicitly in this run. Let F/Q₅ be unramified of degree four and
K=F(5^(1/8)). Both

\[
E_b:y^2=x^3+5^4,\qquad E_g:y^2=x^3-x
\]

have constant 5-torsion over K, so μ₅⊂K. Their finite potentially-good
inertia traces are nevertheless −1 and 2 on an order-three element.
The first curve's 24 nonzero torsion points come from two simple-root
Hensel lifts after an explicit division-polynomial scaling. Its
discriminant valuation is incompatible with good reduction over K; a tame
cubic extension produces supersingular good reduction. The second curve
has good ordinary reduction, and its split CM action together with the
degree-four unramified extension trivializes its mod-5 representation.
All these steps are given in `work/cotes8_9_4/proofs.md`, with exact
finite-field and polynomial output. This concerns the finite
potentially-crystalline/Weil–Deligne character or ℓ≠5 inertia, **not the full
raw 5-adic Tate module**. It is not attributed to Tate or identified with an
unread marginal example (SA15-338; CL-SA15-325–CL-SA15-327,
CL-SA15-379; MP-SA15-112).

### Ordinary deformations and the Tate determinant, cote 9:15–29

The ordinary deformation pages seek a full stratification compatible with
F and V, then describe unit-F pieces and Hasse invariants. Equality after
arbitrary Frobenius pullback does not descend; the next leaf repairs that
argument on the smooth universal deformation space. The literal formula
using A[p](k) for every perfect k also fails: the ordinary elliptic curve
y²=x³−x over F₅ has eight rational points and no nonzero rational
5-torsion. Geometric points with descent, or the corresponding étale sheaf,
are required. Katz1981 Theorems1.2.1 and2.1 is the exact ordinary-deformation
comparison (SA15-339–SA15-346; CL-SA15-328–CL-SA15-338;
MP-SA15-113–MP-SA15-117).

The determinant discussion must be read to its conclusion. The author
rejects a universal endomorphism degree-square lemma, restricts to positive
Rosati-symmetric operators, proves the sign on scan 27, and checks the
integral lattice on scan 28. The normalized étale Tate determinant is then
independent of the polarization in the stated ordinary setting. The earlier
notes sometimes froze an intermediate sign doubt that the manuscript itself
resolves. Naturality requires the inverse dual map; the last biduality sign,
product convention and reduction comparison are still separate checks.
Milne2008 Theorem11.1 and §14, Proposition14.2/Theorem14.3, supply the
checked degree-square and Rosati-positivity framework; the
actual determinant argument was independently audited here
(SA15-347–SA15-350; CL-SA15-339–CL-SA15-346;
MP-SA15-118–MP-SA15-120).

### The revised torsion sequence, cote 4

Cote 4 estimates unit Frobenius eigenvalues in vanishing cohomology. Its
“semisimple” operation means the stable, bijective Frobenius part. This is
not a claim that the corresponding Galois representation is semisimple.
Universal coefficients, duality and an integral weak Lefschetz statement
are assumed or invoked before the correction term is revised. The live
sequence is

\[
0\longrightarrow\ker v\longrightarrow
H^n_{\mathrm{cris}}(X)[p]_{\mathrm{st}}\longrightarrow
(E(Y)/p)_{\mathrm{st}}\xrightarrow{\varphi}\operatorname{coker}v
\longrightarrow0.
\]

The old cup-product correction is cancelled. Thus φ is surjective in the
revised argument; live examples concern its injectivity or bijectivity.
BMS2016 Lemma2.12 verifies a modern integral Lefschetz statement for
sufficiently high ample powers, without supplying the draft's stronger
all-degree saturation hypothesis (SA15-351–SA15-357;
CL-SA15-347–CL-SA15-359; MP-SA15-121–MP-SA15-122).

The later results are unusually exact. Stable de Rham augmentation is
KatzSGA7XXII (3.3.4). Eventual generic positive stable vanishing rank is
KatzSGA7XXI Theorem1.4, pp.374–376, for projective equidimensional
Cohen–Macaulay X. Koblitz1975 I§2, Lemma4, p.132, and I§5,
Theorems1–2, pp.139–141, supply generic transfer and growth with leading
term Dd^n/n!. Subtracting a fixed ambient contribution preserves
unboundedness. Consequently generic rank growth is an established part of
the final programme, not an unresolved research obstacle
(SA15-358–SA15-361, SA15-366;
CL-SA15-360–CL-SA15-368, CL-SA15-376;
MP-SA15-125–MP-SA15-126, MP-SA15-131).

Full GL monodromy for every fixed-X hypersurface family remains a different
assertion. AchterPries2008 Proposition4.8 treats components of curve
p-rank strata in moduli, and does not settle these parameter spaces. A
boundary check is immediate when X=P¹: the vanishing H⁰ representation is
F_p^d/F_p, so monodromy factors through S_d. This prevents extending the
full-GL formulation indiscriminately to dimension one; it does not refute
the text's n≥2 question. The last point-count residue argument is conditional
on the exact monodromy and Frobenius-distribution inputs, even though the
trace-surjectivity calculation inside SL_r(F_p) is elementary and was
rerun (SA15-365–SA15-366; CL-SA15-375–CL-SA15-378,
CL-SA15-384; MP-SA15-130–MP-SA15-132).

Finally, the equality criterion needs an additional torsion term. Set
i=n−1, let b be the stable dimension of the torsion of H^i_cris modulo p,
let c=dim H^(i+1)_cris[p]_st, and let k₀=dim ker v. Universal coefficients
give defect **b+c** in the stated coherent-versus-free-crystalline rank
inequality, whereas the revised sequence gives dim ker φ=**c−k₀**.
Equality and bijectivity are therefore equivalent only with further
hypotheses, such as b=0 and k₀=0. The model b=1,c=k₀=0 refutes the formal
implication. It is an algebraic countermodel, not a claimed new geometric
example. The author's surface example avoids the preceding-degree torsion
issue. The separate comparison with torsion of a characteristic-zero lift
also remains an exact question, not an equality supplied by rational
comparison theory (SA15-362–SA15-364;
CL-SA15-369–CL-SA15-374; MP-SA15-127–MP-SA15-129).


## 6. What the earlier notes got right, and what changed

The earlier notes are not uniformly unreliable. Many already separate their
own diagnostics from the manuscript, preserve cancellations, and state the
hypotheses of the later theorems more carefully than a short thematic summary
would. Their Amitsur, convergence, Borel, period-normalization, principal-PD,
CM and Tate-twist tests remain attributed to them. The present run has
checked them; it has not claimed their authorship. The absence of a
“corrected” verdict for a page whose formula is false often means that the
earlier note had already diagnosed that false formula correctly.

The substantive changes fall into the following groups. Each is documented
at the item and claim level, rather than inferred from an automated search
of the notes.

| Issue | Consolidated finding | Principal records |
|---|---|---|
| A false or cancelled intermediate statement treated as the final position | Follow the correction on the same or later supplied leaf: the ordinary cohomology hope, the determinant sign argument, and the revised torsion sequence have different final statuses. | SA15-133; CL-SA15-188; CL-SA15-339–CL-SA15-346; CL-SA15-352–CL-SA15-359 |
| “Hypersingulière” silently modernized to supersingular | Preserve the author's p-rank-zero meaning. The broad higher-dimensional formal-isogeny conclusion is false; the all-slope-1/2 case is different. | CL-SA15-161–CL-SA15-164 |
| The ordinary cusp used as a singular de Rham counterexample | The full exterior Kähler complex includes its second term and has Euler contraction. A non-quasihomogeneous example is needed for the claimed failure. | CL-SA15-042; CL-SA15-196; MP-SA15-14; MP-SA15-69 |
| An ordinary connection, a full stratification and a PD crystal treated alike | Their local-freeness and comparison theorems have different scopes. BO's ordinary coherent stratification result does not require smoothness, while a general connection or PD lattice is another object. | CL-SA15-102–CL-SA15-104 |
| A literature title taken as a solution of the exact assertion | Retain the theorem's base, coefficient, completion and finiteness hypotheses. Rational comparison is not integral saturation; a theorem for moduli of curves is not a theorem for every fixed-X family. | CL-SA15-240–CL-SA15-243; CL-SA15-353; CL-SA15-375 |
| Every small nonzero mod-p lifting obstruction expected to be universal | There is an explicit GL₂(F₂) splitting; the complete classification is supported by the precisely identified later source, not an unread original proof. | CL-SA15-306–CL-SA15-309 |
| Generic mod-p torsion expected to determine finite potentially-good inertia | The explicit p=5 elliptic pair refutes the restricted comparison as well. Its hypotheses and finite-inertia scope are checked. | CL-SA15-325; CL-SA15-379 |
| Stable-rank growth left as a research obstacle | Katz's precise positivity theorem and Koblitz's leading-term/generic-transfer argument settle that part. The monodromy input remains separate. | CL-SA15-367; CL-SA15-375–CL-SA15-378 |
| Arithmetic normalization omitted | A× versus K×, Ω/p versus Ω/π, the inverse dual, a Tate twist, a Frobenius twist, or a missing degree shift can change the assertion. | CL-SA15-270; CL-SA15-277–CL-SA15-278; CL-SA15-343; CL-SA15-177 |

The current run additionally supplies the general weighted-ideal proof for
W(ν,r), the explicit two-curve inertia counterexample, the stable-torsion
dimension calculation, and the finite-local-field deduction for the
virtual-good-reduction length question. Their precise scope and dependence
on previously established theorems are recorded in the proof audits and
check events. Finite computations corroborate some of these arguments;
they do not prove their universal quantifiers. Refinement records and
counterexample certificates have separate provenance, so their presence in
the claim map does not enlarge what the manuscript itself asserted.

## 7. Reading alarms, links and historical limits

The reading table contains mathematical alarms: inconsistent F/V products,
missing shifts, logarithm signs, truncation indices, scalar-ring changes,
Frobenius twists, inequality/equality discrepancies, cancelled clauses,
reversed arrows and omitted determinants. It also records where Pro and
Codex disagree. Each row gives the alternative suggested by the mathematics
and its weight. **No row chooses a reading, and no diplomatic file was
changed.** The next scan-based companion can decide the ink using this
prioritized register.

The main link table contains only links checked at both endpoints. This
includes continuations across the package boundaries, reused-text order,
the exact passages of EGA and SGA, and selected later mathematical
counterparts. Archive order is not treated as a chronology. In particular,
the continuation 7:005 → 7:059 → 7:006 and the reverse jet typescript order
are documentary findings, whereas a proposed date for the handwriting
would be an additional inference.

The references to cote 54 are genuine leads in the earlier notes, but that
cote is not supplied. They remain in `SA15_unverified_links.tsv` rather
than the two-ended link table. A Demazure–Gabriel locator whose exact
passage was not obtained is handled the same way. Opened bibliographic
metadata do not turn it into a checked mathematical endpoint.

No in-scope note explicitly names a La Longue Marche, Dérivateurs, S6, or
other external research-run endpoint. The empty
`SA15_project_leads.tsv` is therefore an audited result, not an omission.
The earlier notes' cote 100 references stay archive links. Neither those
references nor a general similarity of subject licenses attributing a
connection to an absent project.

The problem register includes every retained question, hope, self-flagged
step and doubt, including ones later resolved or retracted. It is not a
list of contemporary open conjectures. Where no source explains why a
question was abandoned, `why_open` says so. A mathematical explanation of a
failed argument is not invented as a historical account of the author's
motivation. Similarly, a searched but unidentified modern endpoint is not
labelled an unsolved theorem.

## 8. What the dossier makes possible next

The most useful next work is narrow. First fix the conventions and missing
data that control a definite argument: the finite-group triangles, the two
integral Lubin–Tate lattices, the dual variance, and the stable-torsion
criterion. Then compare the exact reconstructed objects to the exact later
categories. The directions file ranks those tasks by mathematical interest
and what one research run of a few hours could establish. It also states
where a scan-based reading task must precede a proof attempt.

Several attractive-looking tasks are deliberately absent: re-proving the
now-checked W(ν,r) coefficient formula as though it were still open,
seeking an affirmative p-rank-zero Barsotti isogeny theorem contradicted by
the counterexample, deriving a Weil theory from the rejected non-PD
construction without changing it, or pursuing stable-rank growth as an
unresolved prerequisite. Their checks belong to this dossier; future work
should begin from the corrected status.

## 9. Counts and completion record

| Record | Final count |
|---|---:|
| Supplied indexed entries, each adjudicated once | 80 |
| Additional in-scope note entries, each adjudicated once | 847 |
| Total entry verdicts | 927 |
| Consolidated items | 366 |
| Claims, including explicitly labelled refinements and earlier-note checks | 384 |
| Claims with a recorded fate search | 384 |
| Problems, including resolved and withdrawn questions | 132 |
| Undecided mathematical reading alarms | 217 |
| Links with both endpoints checked | 120 |
| Separate unverified endpoint leads | 4 |
| Named external-project leads found in supplied in-scope notes | 0 |
| Ranked directions | 12 |
| Bibliographic keys | 132 |
| Keys with a verified opened URL/DOI | 128 |
| Check events | 1108 |
| Cote 100 entries inventoried outside the topic | 201 |

### Verdicts

| Verdict | Supplied index | Supplementary entries | Total |
|---|---:|---:|---:|
| kept | 51 | 293 | 344 |
| merged | 27 | 493 | 520 |
| corrected | 0 | 51 | 51 |
| withdrawn | 2 | 8 | 10 |
| rests on a misreading | 0 | 2 | 2 |

### Items by kind

| Category | Count |
|---|---:|
| conjecture | 66 |
| idea of the earlier run | 89 |
| other | 22 |
| reading question | 32 |
| self-flagged step | 16 |
| title, date or page count | 6 |
| unproved claim | 106 |
| unpursued implication | 10 |
| withdrawn in the same text | 19 |
| **Total** | **366** |

### Claims by fate class

| Category | Count |
|---|---:|
| A | 37 |
| B | 139 |
| C | 95 |
| D | 0 |
| E | 77 |
| F | 36 |
| **Total** | **384** |

### Claims by documentary-status census

| Category | Count |
|---|---:|
| proved there | 17 |
| proof sketched | 104 |
| stated without proof | 83 |
| corrected or withdrawn by himself | 24 |
| false as stated | 21 |
| open on the pages | 85 |
| mixed or conditional page status | 22 |
| insufficient text | 12 |
| present-run refinement | 16 |
| **Total** | **384** |

### Claim-record provenance

| Category | Count |
|---|---:|
| earlier-run assertion rechecked here | 8 |
| foreign inserted text | 7 |
| later comparison identified by earlier run | 1 |
| manuscript or transcribed reused text | 352 |
| present-run refinement | 16 |
| **Total** | **384** |

The provenance categories describe the records, not publication-priority claims. The 16 present-run refinements include precise restatements of some earlier-run diagnostics. The status bucket “insufficient text” comprises nine earlier-run-only records that have no historical page-proof status and three inadequately identified manuscript statuses. It does not mean twelve missing source passages. The separate modern-validity column in `SA15_status_census.tsv` retains refutations of documentary-open or retracted assertions.

The item count is 369 independently curated records minus three cross-package identity overlaps. The claim count is 386 raw records minus two overlapping parts of the continuous co-Lie calculation. All 132 precise problem formulations remain separate after cross-review; related questions are linked without being identified merely because they share a technique or later reference.


Counts are computed from the final linked records after the manually
specified identity decisions, not from keyword matches. The complete
original page-status wording remains in every claim. The normalized
status census separates present-run refinements and mixed documentary
statuses; it does not backdate a modern refutation into an authorial
retraction. A reader can reproduce the structural joins and count tables
with `work/code/validate_final.py`. Its PASS certifies file structure,
coverage and references, not a formal proof of the mathematics.

The source inventory, source-read ledgers, per-claim search ledger,
bibliographic evidence, independent proof files, exact calculation code and
saved outputs are included under `work/`. The original attachments are
not duplicated. `progress.log` gives the UTC start, stage milestones,
checkpoint events and completion. The final archive is the complete
deliverable; none of its registers is a sample or a proposed future
catalogue.
